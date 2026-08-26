"""
analysis_helpers.py
===================
Shared helper library for the ICD-IA survey analysis pipeline.

Imported by both analysis notebooks:
    - ia_icd_pymes_analysis.ipynb
    - ia_icd_competentes_analysis.ipynb

Contents
--------
1.  Configuration: column code sets, category orderings, palettes, themes
2.  Text utilities: normalization, accent folding
3.  Loading: preview_columns, build_rename_map, load_survey
4.  Labels: SPSS-style variable-label system (set/get/copy)
5.  Categoricals: apply_categoricals with unknown-value reporting
6.  Labeled displays: labeled_head, labeled_info, labeled_describe, ...
7.  Frequencies: freq_table, crosstab_pct, multiselect_summary
8.  Missingness: missingness_report
9.  Validation: validate_dataset (acceptance-criteria harness)
10. Visualization: set_theme, bar_freq, stacked_bar, heatmap, save_fig
11. Stats (optional): cramers_v, chi2_association

Run `python analysis_helpers.py` to execute the Step 1 validation report.

Usage
-----
    from analysis_helpers import *
    dfpymes = load_survey(PYMES_PATH, PYMES_CODES)
    dfcomp  = load_survey(COMP_PATH,  COMP_CODES)
    set_theme("light")
"""

from __future__ import annotations

import os
import re
import sys
import unicodedata
import warnings
from typing import Dict, Iterable, List, Optional, Sequence, Tuple

import numpy as np
import pandas as pd

__all__ = [
    "DATA_DIR", "PYMES_PATH", "COMP_PATH", "PYMES_CODES", "COMP_CODES",
    "DEMOGRAPHIC_CODES", "COMP_MULTISELECT", "CATEGORY_ORDERS", "ORDER_NSE",
    "OCUPACION_TO_ESTADO_LABORAL",
    "PALETTE", "SEQUENTIAL_CMAP", "DIVERGING_CMAP", "THEMES",
    "normalize_text", "strip_accents",
    "preview_columns", "build_rename_map", "load_survey", "lowercase_df",
    "set_labels", "get_label", "get_labels", "copy_labels",
    "apply_categoricals", "category_report", "add_estado_laboral",
    "labeled_head", "labeled_info", "labeled_describe",
    "labeled_value_counts", "labeled_value_counts_detailed", "labeled_crosstab",
    "freq_table", "crosstab_pct", "multiselect_summary", "missingness_report",
    "validate_dataset",
    "set_theme", "bar_freq", "stacked_bar", "heatmap", "missingness_heatmap",
    "save_fig", "cramers_v", "chi2_association",
    "correspondence_analysis", "ca_biplot",
    "response_profile", "chi2_scale_profile", "combined_profile",
    "plot_dendrogram",
]

# =============================================================================
# 1. CONFIGURATION
# =============================================================================

DATA_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data")
PYMES_PATH = os.path.join(DATA_DIR, "ia_pymes.xlsx")
COMP_PATH = os.path.join(DATA_DIR, "ia_comp.xlsx")
FIG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "figures")

DEMOGRAPHIC_CODES: List[str] = ["sexo", "edad", "niveduc", "ocupacion", "nse"]

PYMES_CODES: List[str] = [
    "id", "sexo", "edad", "niveduc", "ocupacion", "nse",
    "p01", "p01_otro", "p02", "p02_otro", "p03", "p03_otro", "p04",
]

COMP_CODES: List[str] = [
    "id", "sexo", "edad", "niveduc", "ocupacion", "nse",
    "p01", "p01_otro",
    "p_02a", "p_02b", "p_02c", "p_02d", "p_02e", "p02_otro",
    "p03",
]

COMP_MULTISELECT: List[str] = ["p_02a", "p_02b", "p_02c", "p_02d", "p_02e"]

CODE_DESCRIPTIONS: Dict[str, Dict[str, str]] = {
    "pymes": {
        "id": "ID de respuesta",
        "sexo": "Sexo",
        "edad": "Rango de edad",
        "niveduc": "Nivel educacional",
        "ocupacion": "Ocupacion",
        "nse": "Grupo socioeconomico",
        "p01": "Tarea del negocio que consume mas tiempo",
        "p01_otro": "P01 - otra respuesta",
        "p02": "Principal fuente de ayuda",
        "p02_otro": "P02 - otra respuesta",
        "p03": "Barreras para el crecimiento del negocio",
        "p03_otro": "P03 - otra respuesta",
        "p04": "Tiempo semanal dispuesto a dedicar a aprender herramientas digitales",
        "estado_laboral": "Estado laboral (categoria agrupada de ocupacion: "
                          "empleado / desempleado / estudiante / inactivo)",
    },
    "comp": {
        "id": "ID de respuesta",
        "sexo": "Sexo",
        "edad": "Rango de edad",
        "niveduc": "Nivel educacional",
        "ocupacion": "Ocupacion",
        "nse": "Grupo socioeconomico",
        "p01": "Principal barrera para aprender herramientas digitales",
        "p01_otro": "P01 - otra respuesta",
        "p_02a": "Apoyo requerido: curriculum vitae",
        "p_02b": "Apoyo requerido: entrevistas",
        "p_02c": "Apoyo requerido: busqueda de empleo",
        "p_02d": "Apoyo requerido: contacto con empresas",
        "p_02e": "Apoyo requerido: ninguno",
        "p02_otro": "P02 - otra respuesta",
        "p03": "Interes en formacion de habilidades via movil",
        "estado_laboral": "Estado laboral (categoria agrupada de ocupacion: "
                          "empleado / desempleado / estudiante / inactivo)",
    },
}

ORDER_NSE: bool = True

CATEGORY_ORDERS: Dict[str, List[str]] = {
    "sexo": ["femenino", "masculino"],
    "edad": ["[18-30]", "[31-40]", "[41-50]", "[51-60]", "[61+]"],
    "niveduc": [
        "basica incompleta",
        "basica completa",
        "media incompleta",
        "media completa",
        "tecnica superior incompleta",
        "tecnica superior completa",
        "universitaria incompleta",
        "universitaria completa",
        "postgrado",
    ],
    "ocupacion": [
        "cesante",
        "estudiante",
        "dueño(a) de casa",
        "jubilado(a)",
        "oficio menor",
        "oficio calificado",
        "empleado(a) administrativo(a) / tecnico",
    ],
    "nse": ["e", "d", "d+e", "c3", "c2", "c1b", "c1a", "ab", "abc1"],
    "estado_laboral": ["desempleado", "estudiante", "inactivo", "empleado"],
}

# Groups the 10 observed `ocupacion` values (7 canonicas + 3 fuera de orden
# jerarquico, ver Seccion 1 de ambos notebooks) en 4 categorias de estado
# laboral. Empleado incluye trabajo formal e informal (con o sin jerarquia
# definida); Inactivo agrupa a quienes no participan del mercado laboral por
# razones distintas al desempleo (dueño(a) de casa, jubilado(a)).
OCUPACION_TO_ESTADO_LABORAL: Dict[str, str] = {
    "cesante": "desempleado",
    "estudiante": "estudiante",
    "dueño(a) de casa": "inactivo",
    "jubilado(a)": "inactivo",
    "oficio menor": "empleado",
    "oficio calificado": "empleado",
    "empleado(a) administrativo(a) / tecnico": "empleado",
    "alto(a) ejecutivo(a)": "empleado",
    "ejecutivo(a) medio(a) / profesional independiente": "empleado",
    "trabajos menores e informales": "empleado",
}

CATEGORY_ALIASES: Dict[str, Dict[str, str]] = {
    "sexo": {"f": "femenino", "m": "masculino", "mujer": "femenino",
             "hombre": "masculino"},
    "edad": {
        "18-30": "[18-30]", "31-40": "[31-40]", "41-50": "[41-50]",
        "51-60": "[51-60]", "61+": "[61+]", "[61 y mas]": "[61+]",
        "61 y mas": "[61+]", "[61 o mas]": "[61+]",
    },
    "niveduc": {
        "ensenanza media incompleta": "media incompleta",
        "ensenanza media completa": "media completa",
        "tecnico superior incompleta": "tecnica superior incompleta",
        "tecnico superior completa": "tecnica superior completa",
    },
    "ocupacion": {
        "dueno(a) de casa": "dueño(a) de casa",
        "duena de casa": "dueño(a) de casa",
        "dueno de casa": "dueño(a) de casa",
    },
    "nse": {"de": "d+e", "d/e": "d+e", "d y e": "d+e"},
}

PALETTE: List[str] = [
    "#0072B2", "#E69F00", "#009E73", "#CC79A7", "#56B4E9",
    "#D55E00", "#F0E442", "#666666",
]

PALETTE_BINARY: List[str] = ["#0072B2", "#E69F00"]

SEQUENTIAL_CMAP = "viridis"
DIVERGING_CMAP = "RdBu_r"
MISSING_CMAP = "Greys"

FONT_STACK: List[str] = [
    "Inter", "Helvetica Neue", "Helvetica", "Arial", "DejaVu Sans",
]

THEMES: Dict[str, Dict[str, object]] = {
    "light": {
        "figure.facecolor": "#FFFFFF",
        "axes.facecolor": "#FFFFFF",
        "savefig.facecolor": "#FFFFFF",
        "text.color": "#1A1A1A",
        "axes.labelcolor": "#1A1A1A",
        "axes.edgecolor": "#4D4D4D",
        "xtick.color": "#4D4D4D",
        "ytick.color": "#4D4D4D",
        "grid.color": "#D9D9D9",
        "legend.facecolor": "#FFFFFF",
        "legend.edgecolor": "#D9D9D9",
    },
    "dark": {
        "figure.facecolor": "#12151A",
        "axes.facecolor": "#12151A",
        "savefig.facecolor": "#12151A",
        "text.color": "#E8EAED",
        "axes.labelcolor": "#E8EAED",
        "axes.edgecolor": "#8A9099",
        "xtick.color": "#B7BDC6",
        "ytick.color": "#B7BDC6",
        "grid.color": "#2A2F37",
        "legend.facecolor": "#12151A",
        "legend.edgecolor": "#2A2F37",
    },
}

BASE_RCPARAMS: Dict[str, object] = {
    "figure.figsize": (9, 5),
    "figure.dpi": 110,
    "savefig.dpi": 200,
    "savefig.bbox": "tight",
    "font.size": 11,
    "axes.titlesize": 13,
    "axes.titleweight": "semibold",
    "axes.labelsize": 11,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "axes.grid": True,
    "axes.axisbelow": True,
    "grid.linewidth": 0.6,
    "grid.alpha": 0.7,
    "xtick.labelsize": 10,
    "ytick.labelsize": 10,
    "legend.fontsize": 10,
    "legend.frameon": False,
    "lines.linewidth": 2.0,
}

_ACTIVE_THEME = "light"

# =============================================================================
# 2. TEXT UTILITIES
# =============================================================================

def strip_accents(text: str) -> str:
    """Remove diacritics from text (é -> e), leaving 'ñ' intact."""
    if not isinstance(text, str):
        return text
    placeholder = "\x00"
    text = text.replace("ñ", placeholder).replace("Ñ", placeholder)
    decomposed = unicodedata.normalize("NFKD", text)
    stripped = "".join(ch for ch in decomposed if not unicodedata.combining(ch))
    return stripped.replace(placeholder, "ñ")


def normalize_text(value, fold_enye: bool = False) -> str:
    """Lowercase, strip accents, collapse whitespace. Used as a lookup key."""
    if not isinstance(value, str):
        return value
    out = strip_accents(value.strip().lower())
    if fold_enye:
        out = out.replace("ñ", "n")
    out = re.sub(r"\s+", " ", out)
    out = re.sub(r"\s*-\s*", "-", out)
    return out


# =============================================================================
# 3. LOADING
# =============================================================================

HEADER_PATTERNS: Dict[str, str] = {
    "id": r"^(id|folio|n°|nro|numero|caso|case|registro|encuesta)\b",
    "sexo": r"\b(sexo|genero)\b",
    "edad": r"\b(edad|tramo etario|rango etario)\b",
    "niveduc": r"(educ|escolarid|estudios|instruccion)",
    "ocupacion": r"(ocupacion|situacion laboral|actividad laboral)",
    "nse": r"(\bnse\b|\bgse\b|socioeconom|grupo socio)",
}


def preview_columns(path: str, n: int = 3) -> pd.DataFrame:
    """Read a workbook and show raw headers plus the first n rows."""
    raw = pd.read_excel(path)
    print(f"File   : {path}")
    print(f"Shape  : {raw.shape[0]} rows x {raw.shape[1]} columns\n")
    for i, col in enumerate(raw.columns):
        print(f"  [{i:>2}] {col!r}")
    print()
    return raw.head(n)


def build_rename_map(columns: Sequence[str],
                     codes: Sequence[str],
                     verbose: bool = True) -> Dict[str, str]:
    """Map raw Spanish headers to short English codes."""
    columns = list(columns)
    codes = list(codes)
    mapping: Dict[str, str] = {}
    used_headers: set = set()

    for code, pattern in HEADER_PATTERNS.items():
        if code not in codes:
            continue
        for col in columns:
            if col in used_headers:
                continue
            if re.search(pattern, normalize_text(str(col), fold_enye=True)):
                mapping[col] = code
                used_headers.add(col)
                break

    remaining_codes = [c for c in codes if c not in mapping.values()]
    remaining_cols = [c for c in columns if c not in used_headers]

    if len(remaining_cols) != len(remaining_codes):
        warnings.warn(
            f"Column/code count mismatch: {len(remaining_cols)} unmapped "
            f"headers vs {len(remaining_codes)} unassigned codes.",
            stacklevel=2,
        )
    for col, code in zip(remaining_cols, remaining_codes):
        mapping[col] = code

    if verbose:
        print("Rename map (raw header -> code):")
        for col in columns:
            code = mapping.get(col, "<UNMAPPED>")
            print(f"  {code:<10} <- {col!r}")
        print()
    return mapping


def load_survey(path: str,
                codes: Sequence[str],
                dataset: Optional[str] = None,
                lowercase: bool = True,
                categoricals: bool = True,
                strict: bool = False,
                verbose: bool = True) -> pd.DataFrame:
    """Load a survey workbook, rename columns, attach labels, set categoricals."""
    raw = pd.read_excel(path)
    mapping = build_rename_map(raw.columns, codes, verbose=verbose)

    df = raw.rename(columns=mapping)
    labels = {code: str(header) for header, code in mapping.items()}
    if dataset in CODE_DESCRIPTIONS:
        for code, desc in CODE_DESCRIPTIONS[dataset].items():
            labels.setdefault(code, desc)
    df = set_labels(df, labels)

    if lowercase:
        df = lowercase_df(df)
    if categoricals:
        df = apply_categoricals(df, strict=strict, verbose=verbose)

    if verbose:
        print(f"Loaded {os.path.basename(path)}: "
              f"{df.shape[0]} rows x {df.shape[1]} columns\n")
    return df


def lowercase_df(df: pd.DataFrame) -> pd.DataFrame:
    """Lowercase and strip all string cells, preserving dtypes and labels."""
    out = df.copy()
    labels = get_labels(df)

    for col in out.columns:
        s = out[col]
        if isinstance(s.dtype, pd.CategoricalDtype):
            new_cats = [c.strip().lower() if isinstance(c, str) else c
                        for c in s.cat.categories]
            out[col] = s.cat.rename_categories(new_cats)
        elif s.dtype == object or pd.api.types.is_string_dtype(s.dtype):
            out[col] = s.map(
                lambda x: x.strip().lower() if isinstance(x, str) else x)
    return set_labels(out, labels)


# =============================================================================
# 4. VARIABLE LABELS (SPSS-style)
# =============================================================================

_LABEL_KEY = "variable_labels"


def set_labels(df: pd.DataFrame, labels: Dict[str, str]) -> pd.DataFrame:
    """Attach/merge a {code: label} dict onto df.attrs['variable_labels']."""
    current = dict(df.attrs.get(_LABEL_KEY, {}))
    current.update(labels or {})
    df.attrs[_LABEL_KEY] = current
    return df


def get_labels(df: pd.DataFrame) -> Dict[str, str]:
    """Return a copy of the full label dictionary (empty dict if unset)."""
    return dict(df.attrs.get(_LABEL_KEY, {}))


def get_label(df: pd.DataFrame, col: str) -> str:
    """Return the label for col, falling back to the column name itself."""
    return get_labels(df).get(col, col)


def copy_labels(src: pd.DataFrame, dst: pd.DataFrame) -> pd.DataFrame:
    """Propagate labels from src to dst."""
    return set_labels(dst, get_labels(src))


# =============================================================================
# 5. CATEGORICALS
# =============================================================================

def _canonical_lookup(code: str) -> Dict[str, str]:
    """Build {normalized_value: canonical_category} for one variable."""
    lookup: Dict[str, str] = {}
    for cat in CATEGORY_ORDERS.get(code, []):
        lookup[normalize_text(cat, fold_enye=True)] = cat
    for alias, target in CATEGORY_ALIASES.get(code, {}).items():
        lookup[normalize_text(alias, fold_enye=True)] = target
    return lookup


def category_report(df: pd.DataFrame,
                    code: str) -> Tuple[List[str], List[str]]:
    """Return (matched, unknown) raw values for a categorical column."""
    if code not in df.columns or code not in CATEGORY_ORDERS:
        return [], []
    lookup = _canonical_lookup(code)
    observed = [v for v in df[code].dropna().unique()]
    matched, unknown = [], []
    for v in observed:
        key = normalize_text(v, fold_enye=True) if isinstance(v, str) else v
        (matched if key in lookup else unknown).append(v)
    return matched, unknown


def apply_categoricals(df: pd.DataFrame,
                       codes: Optional[Iterable[str]] = None,
                       strict: bool = False,
                       verbose: bool = True) -> pd.DataFrame:
    """Convert demographic columns to ordered categoricals."""
    if codes is None:
        codes = [c for c in DEMOGRAPHIC_CODES
                 if c != "nse" or ORDER_NSE]
    out = df.copy()
    labels = get_labels(df)
    summary: List[Tuple[str, int, int, List[str]]] = []

    for code in codes:
        if code not in out.columns:
            warnings.warn(f"Column '{code}' not found; skipped.", stacklevel=2)
            continue

        lookup = _canonical_lookup(code)
        if not lookup:
            warnings.warn(f"No ordering defined for '{code}'; skipped.",
                          stacklevel=2)
            continue

        raw = out[code].astype(object)
        mapped = raw.map(
            lambda v: lookup.get(normalize_text(v, fold_enye=True), v)
            if isinstance(v, str) else v)

        canonical = CATEGORY_ORDERS[code]
        observed = set(mapped.dropna().unique())
        unknown = sorted(str(v) for v in observed - set(canonical))

        if unknown:
            msg = (f"Column '{code}' has {len(unknown)} value(s) outside the "
                   f"canonical ordering: {unknown}")
            if strict:
                raise ValueError(msg)
            warnings.warn(msg + " -- appended as trailing categories.",
                          stacklevel=2)

        categories = [c for c in canonical if c in observed] + unknown
        out[code] = pd.Categorical(mapped, categories=categories, ordered=True)
        summary.append((code, len(categories), int(out[code].isna().sum()),
                        unknown))

    if verbose and summary:
        print("Categorical conversion:")
        for code, n_cat, n_na, unknown in summary:
            flag = "  <-- CHECK" if unknown else ""
            print(f"  {code:<10} ordered, {n_cat} levels, "
                  f"{n_na} missing{flag}")
        print()
    return set_labels(out, labels)


def add_estado_laboral(df: pd.DataFrame, verbose: bool = True) -> pd.DataFrame:
    """Add `estado_laboral`, grouping `ocupacion` into 4 categories.

    Uses OCUPACION_TO_ESTADO_LABORAL to map each of the 10 observed
    `ocupacion` values (7 canonical + 3 outside the documented hierarchy,
    see Section 1) into Empleado / Desempleado / Estudiante / Inactivo.
    `ocupacion` itself is left untouched.
    """
    out = df.copy()
    labels = get_labels(df)
    raw = out["ocupacion"].astype(object)
    mapped = raw.map(OCUPACION_TO_ESTADO_LABORAL)

    unmapped = raw[raw.notna() & mapped.isna()].unique().tolist()
    if unmapped:
        raise ValueError(
            f"ocupacion value(s) with no estado_laboral mapping: {unmapped}")

    out["estado_laboral"] = mapped
    out = set_labels(out, labels)
    out = apply_categoricals(out, codes=["estado_laboral"], verbose=False)

    if verbose:
        print("estado_laboral (agrupacion de ocupacion):")
        print(out["estado_laboral"].value_counts(sort=False, dropna=False))
        print()
    return out


# =============================================================================
# 6. LABELED DISPLAYS
# =============================================================================

def labeled_head(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    """First n rows with two-line headers: 'code\\nlabel'."""
    out = df.head(n).copy()
    out.columns = [f"{c}\n{get_label(df, c)}" for c in df.columns]
    return out


def labeled_info(df: pd.DataFrame) -> pd.DataFrame:
    """Structured .info() replacement: code, label, dtype, non-null, %missing."""
    rows = []
    n = len(df)
    for col in df.columns:
        s = df[col]
        rows.append({
            "code": col,
            "label": get_label(df, col),
            "dtype": str(s.dtype),
            "n_valid": int(s.notna().sum()),
            "n_missing": int(s.isna().sum()),
            "pct_missing": round(100 * s.isna().mean(), 1) if n else np.nan,
            "n_unique": int(s.nunique(dropna=True)),
        })
    return pd.DataFrame(rows)


def labeled_describe(df: pd.DataFrame,
                     include: str = "all") -> pd.DataFrame:
    """df.describe() with labels appended to the column index."""
    desc = df.describe(include=include).T
    desc.insert(0, "label", [get_label(df, c) for c in desc.index])
    return desc


def labeled_value_counts(df: pd.DataFrame,
                         col: str,
                         normalize: bool = False,
                         dropna: bool = False,
                         sort: bool = False) -> pd.Series:
    """value_counts that prints the variable label as a title."""
    print(f"{col} - {get_label(df, col)}")
    return df[col].value_counts(normalize=normalize, dropna=dropna, sort=sort)


def labeled_value_counts_detailed(df: pd.DataFrame,
                                  col: str,
                                  width: int = 30) -> pd.DataFrame:
    """Formatted frequency table with counts, percentages and ASCII bar."""
    tbl = freq_table(df, col)
    print(f"{col} - {get_label(df, col)}   (n = {len(df)})")
    print("-" * 72)
    max_n = tbl["n"].max() if len(tbl) else 0
    for _, r in tbl.iterrows():
        bar = "#" * int(round(width * r["n"] / max_n)) if max_n else ""
        print(f"  {str(r['value'])[:32]:<34} {r['n']:>5}  "
              f"{r['pct']:>5.1f}%  {bar}")
    print("-" * 72)
    return tbl


def labeled_crosstab(df: pd.DataFrame,
                     rows: str,
                     cols: str,
                     margins: bool = True,
                     normalize: Optional[str] = None) -> pd.DataFrame:
    """Crosstab with labelled axis names and category order preserved."""
    ct = pd.crosstab(df[rows], df[cols], margins=margins,
                     normalize=normalize if normalize else False,
                     dropna=False)
    ct.index.name = f"{rows} - {get_label(df, rows)}"
    ct.columns.name = f"{cols} - {get_label(df, cols)}"
    return ct


# =============================================================================
# 7. FREQUENCIES
# =============================================================================

def freq_table(df: pd.DataFrame,
               col: str,
               sort_by_freq: bool = False,
               include_missing: bool = True,
               decimals: int = 1) -> pd.DataFrame:
    """Full frequency table: n, pct (of all), valid_pct, cum_valid_pct."""
    s = df[col]
    counts = s.value_counts(dropna=not include_missing, sort=sort_by_freq)
    total = len(s)
    valid_total = int(s.notna().sum())

    tbl = counts.rename("n").reset_index()
    tbl.columns = ["value", "n"]
    tbl["pct"] = (100 * tbl["n"] / total).round(decimals) if total else np.nan
    is_missing = tbl["value"].isna()
    tbl["valid_pct"] = np.where(
        is_missing, np.nan,
        (100 * tbl["n"] / valid_total).round(decimals) if valid_total else np.nan)
    tbl["cum_valid_pct"] = tbl["valid_pct"].fillna(0).cumsum().round(decimals)
    tbl.loc[is_missing, "cum_valid_pct"] = np.nan
    tbl.attrs["label"] = get_label(df, col)
    return tbl


def crosstab_pct(df: pd.DataFrame,
                 rows: str,
                 cols: str,
                 pct: Optional[str] = "row",
                 decimals: int = 1,
                 margins: bool = True) -> pd.DataFrame:
    """Contingency table as counts or percentages."""
    norm = {"row": "index", "col": "columns", "all": "all", None: False}[pct]
    ct = pd.crosstab(df[rows], df[cols], normalize=norm, margins=margins,
                     dropna=False)
    if pct:
        ct = (ct * 100).round(decimals)
    ct.index.name = f"{rows} - {get_label(df, rows)}"
    ct.columns.name = f"{cols} - {get_label(df, cols)}"
    return ct


def multiselect_summary(df: pd.DataFrame,
                        cols: Sequence[str],
                        decimals: int = 1) -> pd.DataFrame:
    """Summarise a multi-select block (e.g. COMP_MULTISELECT)."""
    n = len(df)
    rows = []
    for c in cols:
        if c not in df.columns:
            warnings.warn(f"Column '{c}' not found; skipped.", stacklevel=2)
            continue
        selected = int(df[c].notna().sum())
        rows.append({
            "code": c,
            "label": get_label(df, c),
            "n_selected": selected,
            "pct_of_respondents": round(100 * selected / n, decimals) if n else np.nan,
        })
    out = pd.DataFrame(rows)
    present = [c for c in cols if c in df.columns]
    if present:
        per_person = df[present].notna().sum(axis=1)
        print(f"Respondents: {n} | selections per respondent: "
              f"mean {per_person.mean():.2f}, max {int(per_person.max())}")
    return out


# =============================================================================
# 8. MISSINGNESS
# =============================================================================

def missingness_report(df: pd.DataFrame,
                       sort: bool = True,
                       decimals: int = 1) -> pd.DataFrame:
    """Per-column missingness with labels, sorted by severity."""
    n = len(df)
    out = pd.DataFrame({
        "code": df.columns,
        "label": [get_label(df, c) for c in df.columns],
        "n_missing": [int(df[c].isna().sum()) for c in df.columns],
    })
    out["pct_missing"] = (100 * out["n_missing"] / n).round(decimals) if n else np.nan
    if sort:
        out = out.sort_values("n_missing", ascending=False).reset_index(drop=True)
    return out


# =============================================================================
# 9. VALIDATION HARNESS (Step 1 acceptance criteria)
# =============================================================================

def validate_dataset(df: pd.DataFrame,
                     name: str,
                     expected_codes: Sequence[str],
                     verbose: bool = True) -> Dict[str, object]:
    """Check shape, schema, dtypes and categorical ordering for one dataset."""
    codes = list(df.columns)
    missing_codes = [c for c in expected_codes if c not in codes]
    extra_codes = [c for c in codes if c not in expected_codes]

    expected_ordered = [c for c in DEMOGRAPHIC_CODES
                        if c != "nse" or ORDER_NSE]
    unordered, unknown_values = [], {}
    for c in expected_ordered:
        if c not in df.columns:
            unordered.append(c)
            continue
        dt = df[c].dtype
        if not (isinstance(dt, pd.CategoricalDtype) and dt.ordered):
            unordered.append(c)
        _, unknown = category_report(df, c)
        if unknown:
            unknown_values[c] = unknown

    report = {
        "name": name,
        "n_rows": int(df.shape[0]),
        "n_cols": int(df.shape[1]),
        "missing_codes": missing_codes,
        "extra_codes": extra_codes,
        "ordered_ok": not unordered,
        "unordered": unordered,
        "unknown_values": unknown_values,
    }
    report["all_passed"] = (not missing_codes and not unordered
                            and not unknown_values)

    if verbose:
        print("=" * 72)
        print(f"VALIDATION - {name}")
        print("=" * 72)
        print(f"Shape: {report['n_rows']} rows x {report['n_cols']} columns")
        print(f"Schema: {'OK' if not missing_codes else 'MISSING ' + str(missing_codes)}"
              + (f" | extra: {extra_codes}" if extra_codes else ""))
        print(f"Ordered categoricals: "
              f"{'OK' if report['ordered_ok'] else 'FAILED ' + str(unordered)}")
        if unknown_values:
            print("Unmapped category values (review CATEGORY_ORDERS/ALIASES):")
            for c, vals in unknown_values.items():
                print(f"  {c}: {vals}")
        print("\nColumn detail:")
        print(labeled_info(df).to_string(index=False))
        print("\nDemographic distributions:")
        for c in expected_ordered:
            if c in df.columns:
                print(f"\n  {c} ({get_label(df, c)}):")
                vc = df[c].value_counts(sort=False, dropna=False)
                for k, v in vc.items():
                    print(f"    {str(k):<45} {v:>5}")
        print(f"\nRESULT: {'PASS' if report['all_passed'] else 'NEEDS REVIEW'}")
        print("=" * 72 + "\n")
    return report


# =============================================================================
# 10. VISUALIZATION
# =============================================================================

def _require_mpl():
    try:
        import matplotlib.pyplot as plt
        return plt
    except ImportError as exc:
        raise ImportError(
            "matplotlib is required for plotting. Install with:\n"
            "    pip install matplotlib seaborn"
        ) from exc


def _resolve_font() -> str:
    """Return the first font in FONT_STACK that is actually installed."""
    try:
        from matplotlib import font_manager
        available = {f.name for f in font_manager.fontManager.ttflist}
        for font in FONT_STACK:
            if font in available:
                return font
    except Exception:
        pass
    return "DejaVu Sans"


def set_theme(mode: str = "light", palette: Optional[Sequence[str]] = None):
    """Apply the project plotting theme."""
    global _ACTIVE_THEME
    plt = _require_mpl()
    from cycler import cycler

    if mode not in THEMES:
        raise ValueError(f"mode must be one of {list(THEMES)}, got {mode!r}")

    rc = dict(BASE_RCPARAMS)
    rc.update(THEMES[mode])
    rc["font.family"] = "sans-serif"
    rc["font.sans-serif"] = [_resolve_font()] + FONT_STACK
    rc["axes.prop_cycle"] = cycler(color=list(palette or PALETTE))
    plt.rcParams.update(rc)
    _ACTIVE_THEME = mode
    return plt


def _wrap(text: str, width: int = 42) -> str:
    """Wrap long Spanish category labels for axis readability."""
    import textwrap
    return "\n".join(textwrap.wrap(str(text), width=width)) if text else text


def bar_freq(df: pd.DataFrame,
             col: str,
             normalize: bool = True,
             horizontal: bool = True,
             top: Optional[int] = None,
             color: Optional[str] = None,
             ax=None,
             title: Optional[str] = None):
    """Frequency bar chart for one categorical column."""
    plt = _require_mpl()
    s = df[col]
    ordered = isinstance(s.dtype, pd.CategoricalDtype) and s.dtype.ordered
    counts = s.value_counts(sort=not ordered, dropna=False)
    if top:
        counts = counts.head(top)
    values = 100 * counts / len(s) if normalize else counts

    if ax is None:
        height = max(3.0, 0.45 * len(counts) + 1.5)
        _, ax = plt.subplots(figsize=(9, height) if horizontal else (9, 5))

    labels = [_wrap("(sin dato)" if pd.isna(i) else i) for i in counts.index]
    color = color or PALETTE[0]

    if horizontal:
        pos = np.arange(len(counts))[::-1]
        ax.barh(pos, values.values, color=color)
        ax.set_yticks(pos, labels)
        ax.set_xlabel("% de respondentes" if normalize else "Frecuencia")
        ax.grid(axis="y", visible=False)
        for p, v, n in zip(pos, values.values, counts.values):
            ax.text(v, p, f"  {v:.1f}% (n={n})" if normalize else f"  {n}",
                    va="center", fontsize=9)
    else:
        ax.bar(labels, values.values, color=color)
        ax.set_ylabel("% de respondentes" if normalize else "Frecuencia")
        ax.grid(axis="x", visible=False)

    ax.set_title(title or f"{col} - {get_label(df, col)}", loc="left")
    return ax


def stacked_bar(df: pd.DataFrame,
                rows: str,
                cols: str,
                pct: str = "row",
                ax=None,
                legend_title: Optional[str] = None):
    """100%-stacked bar chart of cols distribution within each rows level."""
    plt = _require_mpl()
    ct = crosstab_pct(df, rows, cols, pct=pct, margins=False)
    if ax is None:
        _, ax = plt.subplots(figsize=(9, max(3.0, 0.5 * len(ct) + 1.5)))

    left = np.zeros(len(ct))
    pos = np.arange(len(ct))[::-1]
    for i, c in enumerate(ct.columns):
        vals = ct[c].values
        ax.barh(pos, vals, left=left, color=PALETTE[i % len(PALETTE)],
                label=_wrap(c, 30))
        left += vals

    ax.set_yticks(pos, [_wrap(i, 28) for i in ct.index])
    ax.set_xlabel("% dentro de cada categoria" if pct == "row" else "%")
    ax.set_xlim(0, 100)
    ax.grid(axis="y", visible=False)
    ax.set_title(f"{get_label(df, cols)}\npor {get_label(df, rows)}", loc="left")
    ax.legend(title=legend_title or cols, bbox_to_anchor=(1.01, 1),
              loc="upper left", frameon=False)
    return ax


def heatmap(matrix: pd.DataFrame,
            cmap: Optional[str] = None,
            fmt: str = ".1f",
            annot: bool = True,
            ax=None,
            title: Optional[str] = None,
            diverging: bool = False,
            center: Optional[float] = None):
    """Annotated heatmap for crosstabs, effect sizes or correlation matrices."""
    plt = _require_mpl()
    cmap = cmap or (DIVERGING_CMAP if diverging else SEQUENTIAL_CMAP)
    if ax is None:
        _, ax = plt.subplots(
            figsize=(1.1 * len(matrix.columns) + 3, 0.5 * len(matrix) + 2.5))
    try:
        import seaborn as sns
        sns.heatmap(matrix, cmap=cmap, annot=annot, fmt=fmt, ax=ax,
                    center=center, linewidths=0.5,
                    cbar_kws={"shrink": 0.7})
    except ImportError:
        im = ax.imshow(matrix.values, cmap=cmap, aspect="auto")
        ax.set_xticks(range(len(matrix.columns)),
                      [_wrap(c, 18) for c in matrix.columns], rotation=45,
                      ha="right")
        ax.set_yticks(range(len(matrix.index)),
                      [_wrap(i, 24) for i in matrix.index])
        if annot:
            for i in range(matrix.shape[0]):
                for j in range(matrix.shape[1]):
                    ax.text(j, i, format(matrix.values[i, j], fmt),
                            ha="center", va="center", fontsize=8)
        ax.figure.colorbar(im, ax=ax, shrink=0.7)
        ax.grid(False)
    if title:
        ax.set_title(title, loc="left")
    return ax


def missingness_heatmap(df: pd.DataFrame, ax=None):
    """Binary missingness map: rows = respondents, columns = variables."""
    plt = _require_mpl()
    if ax is None:
        _, ax = plt.subplots(figsize=(max(7, 0.6 * df.shape[1]), 5))
    ax.imshow(df.isna().values, aspect="auto", cmap=MISSING_CMAP,
              interpolation="nearest", vmin=0, vmax=1)
    ax.set_xticks(range(df.shape[1]), df.columns, rotation=45, ha="right")
    ax.set_ylabel("Respondentes")
    ax.set_title("Patron de valores faltantes (oscuro = faltante)", loc="left")
    ax.grid(False)
    return ax


def save_fig(fig_or_ax, filename: str, subdir: str = "", dpi: int = 200) -> str:
    """Save a figure to figures/[subdir]/filename and return the path."""
    import matplotlib.pyplot as plt
    fig = getattr(fig_or_ax, "figure", fig_or_ax)
    out_dir = os.path.join(FIG_DIR, subdir) if subdir else FIG_DIR
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, filename)
    fig.savefig(path, dpi=dpi, bbox_inches="tight")
    return path


# =============================================================================
# 11. STATISTICS (used from Step 5 onward)
# =============================================================================

def cramers_v(confusion: pd.DataFrame, bias_correction: bool = True) -> float:
    """Cramer's V effect size for a contingency table of raw counts."""
    try:
        from scipy.stats import chi2_contingency
    except ImportError as exc:
        raise ImportError("scipy is required: pip install scipy") from exc

    arr = np.asarray(confusion, dtype=float)
    chi2 = chi2_contingency(arr, correction=False)[0]
    n = arr.sum()
    if n == 0:
        return np.nan
    phi2 = chi2 / n
    r, k = arr.shape
    if not bias_correction:
        return float(np.sqrt(phi2 / max(1, min(r - 1, k - 1))))
    phi2_corr = max(0.0, phi2 - (k - 1) * (r - 1) / (n - 1))
    r_corr = r - (r - 1) ** 2 / (n - 1)
    k_corr = k - (k - 1) ** 2 / (n - 1)
    denom = min(r_corr - 1, k_corr - 1)
    return float(np.sqrt(phi2_corr / denom)) if denom > 0 else np.nan


def chi2_association(df: pd.DataFrame, rows: str, cols: str) -> Dict[str, object]:
    """Chi-square test of independence plus Cramer's V for two columns."""
    try:
        from scipy.stats import chi2_contingency
    except ImportError as exc:
        raise ImportError("scipy is required: pip install scipy") from exc

    ct = pd.crosstab(df[rows], df[cols])
    ct = ct.loc[ct.sum(axis=1) > 0, ct.sum(axis=0) > 0]
    chi2, p, dof, expected = chi2_contingency(ct)
    return {
        "rows": rows, "cols": cols,
        "n": int(ct.values.sum()),
        "chi2": float(chi2), "p_value": float(p), "dof": int(dof),
        "cramers_v": cramers_v(ct),
        "min_expected": float(expected.min()),
        "pct_cells_lt5": float(100 * (expected < 5).mean()),
        "significant": bool(p < 0.05),
    }


# =============================================================================
# 12. PATTERN DETECTION -- correspondence analysis & profile clustering
#     (used from Step 7 onward)
# =============================================================================

def correspondence_analysis(ct: pd.DataFrame,
                            n_components: int = 2) -> Dict[str, object]:
    """Simple correspondence analysis (CA) via SVD of standardized residuals.

    Classic textbook formulation (Greenacre): for a contingency table N with
    grand total n, build the correspondence matrix P = N / n, row/column
    masses (marginal profiles), and the matrix of chi-square standardized
    residuals S = (P - rc') / sqrt(rc'), where r and c are the row/column
    mass vectors. The SVD of S, S = U diag(s) V', gives principal row/column
    coordinates after rescaling by the inverse square root of the masses.

    The sum of squared singular values equals total inertia = chi2 / n
    (i.e. phi-squared), so `explained_variance` sums to 1 across all
    dimensions and Cramer's V = sqrt(total_inertia / min(rows-1, cols-1))
    recovers the same effect size reported by `cramers_v()`.

    Parameters
    ----------
    ct : contingency table of raw counts (rows = one categorical variable,
        columns = another). No pre-normalization needed.
    n_components : number of CA dimensions to keep (2 for biplots).

    Returns
    -------
    dict with keys:
        row_coords, col_coords : DataFrames of principal coordinates
        explained_variance : array, share of total inertia per kept dimension
        total_inertia : float, phi-squared = chi2 / n
    """
    N = ct.to_numpy(dtype=float)
    n = N.sum()
    if n <= 0:
        raise ValueError("Contingency table is empty (sum == 0).")

    P = N / n
    row_masses = P.sum(axis=1)
    col_masses = P.sum(axis=0)
    expected = np.outer(row_masses, col_masses)
    resid = np.divide(P - expected, np.sqrt(expected),
                      out=np.zeros_like(P), where=expected > 0)

    U, s, Vt = np.linalg.svd(resid, full_matrices=False)
    k = min(n_components, len(s))
    Uk, sk, Vtk = U[:, :k], s[:k], Vt[:k, :]

    row_std = np.divide(Uk, np.sqrt(row_masses)[:, None],
                        out=np.zeros_like(Uk), where=row_masses[:, None] > 0)
    col_std = np.divide(Vtk.T, np.sqrt(col_masses)[:, None],
                        out=np.zeros_like(Vtk.T), where=col_masses[:, None] > 0)
    row_coords = row_std * sk[None, :]
    col_coords = col_std * sk[None, :]

    inertia_full = s ** 2
    total_inertia = float(inertia_full.sum())
    explained = (inertia_full[:k] / total_inertia
                if total_inertia > 0 else np.zeros(k))

    dims = [f"Dim{i + 1}" for i in range(k)]
    return {
        "row_coords": pd.DataFrame(row_coords, index=ct.index, columns=dims),
        "col_coords": pd.DataFrame(col_coords, index=ct.columns, columns=dims),
        "explained_variance": explained,
        "total_inertia": total_inertia,
    }


def ca_biplot(ca_result: Dict[str, object],
             ax=None,
             title: Optional[str] = None,
             row_label: str = "demografia",
             col_label: str = "respuesta",
             row_color: Optional[str] = None,
             col_color: Optional[str] = None):
    """Symmetric CA biplot: demographic categories (o) + response categories (^)."""
    plt = _require_mpl()
    if ax is None:
        _, ax = plt.subplots(figsize=(8, 7))

    rc = ca_result["row_coords"]
    cc = ca_result["col_coords"]
    row_color = row_color or PALETTE[0]
    col_color = col_color or PALETTE[1]

    ax.axhline(0, color="#999999", lw=0.8, zorder=1)
    ax.axvline(0, color="#999999", lw=0.8, zorder=1)

    ax.scatter(rc.iloc[:, 0], rc.iloc[:, 1], c=row_color, s=110, marker="o",
               edgecolor="white", linewidth=0.8, label=row_label, zorder=3)
    for idx, x, y in zip(rc.index, rc.iloc[:, 0], rc.iloc[:, 1]):
        ax.annotate(_wrap(idx, 22), (x, y), textcoords="offset points",
                    xytext=(7, 5), fontsize=8.5, color=row_color, weight="semibold")

    ax.scatter(cc.iloc[:, 0], cc.iloc[:, 1], c=col_color, s=110, marker="^",
               edgecolor="white", linewidth=0.8, label=col_label, zorder=3)
    for idx, x, y in zip(cc.index, cc.iloc[:, 0], cc.iloc[:, 1]):
        ax.annotate(_wrap(idx, 22), (x, y), textcoords="offset points",
                    xytext=(7, -10), fontsize=8.5, color=col_color)

    ev = ca_result["explained_variance"]
    ax.set_xlabel(f"Dim 1 ({100 * ev[0]:.1f}% de la inercia)" if len(ev) else "Dim 1")
    ax.set_ylabel(f"Dim 2 ({100 * ev[1]:.1f}% de la inercia)" if len(ev) > 1 else "Dim 2")
    ax.legend(loc="best", frameon=False)
    ax.grid(alpha=0.3)
    if title:
        ax.set_title(title, loc="left")
    return ax


def response_profile(df: pd.DataFrame,
                     group_col: str,
                     response_col: str) -> pd.DataFrame:
    """Row-normalized crosstab: for each level of group_col, the frequency
    distribution (profile) over response_col categories. Rows summing to
    zero (groups with no observations) are dropped."""
    ct = pd.crosstab(df[group_col], df[response_col], dropna=False)
    ct = ct.loc[ct.sum(axis=1) > 0]
    return ct.div(ct.sum(axis=1), axis=0)


def chi2_scale_profile(profile: pd.DataFrame) -> pd.DataFrame:
    """Rescale profile columns by 1/sqrt(average column profile).

    This is the same transform correspondence analysis applies internally
    to turn chi-square distance into ordinary Euclidean distance. Applying
    it before Ward-linkage clustering lets `scipy.cluster.hierarchy.linkage`
    (which requires Euclidean input for a valid Ward criterion) approximate
    chi-square-distance clustering on categorical response profiles.
    """
    weights = profile.mean(axis=0).replace(0, np.nan)
    return profile.div(np.sqrt(weights), axis=1).fillna(0)


def combined_profile(df: pd.DataFrame,
                     group_col: str,
                     response_cols: Sequence[str]) -> pd.DataFrame:
    """Concatenate chi-square-scaled response profiles across several
    response variables into one wide matrix (groups x categories), for
    clustering demographic levels on their *overall* response pattern
    rather than a single question."""
    blocks = []
    for resp in response_cols:
        prof = response_profile(df, group_col, resp)
        scaled = chi2_scale_profile(prof)
        scaled.columns = [f"{resp}::{c}" for c in scaled.columns]
        blocks.append(scaled)
    return pd.concat(blocks, axis=1).fillna(0)


def plot_dendrogram(profile: pd.DataFrame,
                    method: str = "ward",
                    ax=None,
                    title: Optional[str] = None,
                    color_threshold: Optional[float] = None,
                    label_wrap: int = 18):
    """Hierarchical clustering dendrogram over a (groups x features) profile
    matrix, e.g. the output of `combined_profile()` / `chi2_scale_profile()`.

    Returns (ax, Z) where Z is the scipy linkage matrix.
    """
    plt = _require_mpl()
    from scipy.cluster.hierarchy import linkage, dendrogram

    Z = linkage(profile.values, method=method)
    if ax is None:
        _, ax = plt.subplots(figsize=(max(7, 1.3 * len(profile) + 2), 5))

    labels = [_wrap(str(i), label_wrap) for i in profile.index]
    dendrogram(Z, labels=labels, ax=ax, color_threshold=color_threshold,
              leaf_font_size=10)
    ax.set_ylabel(f"Distancia ({method}, perfiles escalados chi-cuadrado)")
    ax.grid(axis="x", visible=False)
    ax.tick_params(axis="x", rotation=30)
    for lbl in ax.get_xticklabels():
        lbl.set_ha("right")
    if title:
        ax.set_title(title, loc="left")
    return ax, Z


# =============================================================================
# CLI: Step 1 validation
# =============================================================================

if __name__ == "__main__":
    pd.set_option("display.width", 160)
    pd.set_option("display.max_columns", 50)

    print("\nSTEP 1 - DATA VALIDATION\n" + "=" * 72 + "\n")
    reports = []
    for path, codes, name, key in [
        (PYMES_PATH, PYMES_CODES, "ia_pymes (PyMEs)", "pymes"),
        (COMP_PATH, COMP_CODES, "ia_comp (Competentes)", "comp"),
    ]:
        print(f"\n--- Loading {name} ---\n")
        try:
            df = load_survey(path, codes, dataset=key, verbose=True)
            reports.append(validate_dataset(df, name, codes))
        except Exception as exc:
            print(f"FAILED to load {name}: {type(exc).__name__}: {exc}\n")
            reports.append({"name": name, "all_passed": False,
                            "error": str(exc)})

    print("\nSUMMARY")
    print("-" * 72)
    for r in reports:
        status = "PASS" if r.get("all_passed") else "NEEDS REVIEW"
        shape = (f"{r.get('n_rows', '?')} x {r.get('n_cols', '?')}")
        print(f"  {r['name']:<26} {shape:<14} {status}")
    print("-" * 72)
    sys.exit(0 if all(r.get("all_passed") for r in reports) else 1)
