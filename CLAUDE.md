# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a data analysis project analyzing survey data from two groups:
- **ia_pymes**: Survey responses from small business owners (PyMEs) about digital tools and business growth barriers
- **ia_comp**: Survey responses from job seekers (competentes) about digital skill barriers and job search needs

The notebook performs data cleaning, transformation, and exploratory analysis on Spanish-language survey responses. Column names are systematically mapped from Spanish to English short codes for easier manipulation.

## Running the Notebook

### Launch Jupyter Lab
```bash
jupyter lab ia_icd.ipynb
```

### Python Environment Setup
The notebook requires pandas and numpy. Install dependencies:
```bash
pip install pandas openpyxl numpy
```

## Data Architecture

### Data Sources
- `data/ia_pymes.xlsx` - 500+ responses from small business owners
- `data/ia_comp.xlsx` - 500+ responses from job seekers

### Column Naming Scheme

The first cell renames all columns from Spanish to concise English codes. Key mappings:

**Demographic columns (both datasets):**
- `id` - Response ID
- `sexo` - Gender (MASCULINO/FEMENINO)
- `edad` - Age range (e.g., [31-40], [41-50])
- `niveduc` - Education level (TÉCNICA SUPERIOR COMPLETA, MEDIA COMPLETA, etc.)
- `ocupacion` - Job type/occupation
- `nse` - Socioeconomic group (C2, C3, D+E, etc.)

**PyME-specific columns (business focus):**
- `p01` - Most time-consuming business task (customer service, advertising, accounting, inventory)
- `p01_otro` - Other responses for p01
- `p02` - Primary source of help (family, social media, courses, SERCOTEC)
- `p03` - Barriers to business growth
- `p04` - Willingness to spend weekly time learning digital tools

**Competente-specific columns (job search focus):**
- `p01` - Main barrier to learning digital tools
- `p01_otro` - Other responses for p01
- `p_02a` through `p_02e` - Specific job search support needs (CV, interviews, job search, company contact, none)
- `p02_otro` - Other responses
- `p03` - Interest in mobile-based skills training (Sí/No)

### Data Characteristics
- Extensive use of NaN values for multi-select responses (only selected options populate)
- Mixed case values (UPPERCASE predominant)
- Long, descriptive Spanish text in some columns
- Semicolon-separated multiple responses in some cells

## Variable Labels System (SPSS-style)

The notebook implements a **SPSS-style labeling system** where:
- **Column names in code** remain short and English (id, sexo, edad, p01, etc.)
- **Original Spanish names** are stored as variable labels
- **Output displays** automatically show the original long names when using helper functions

### Using Labels in Outputs

**Helper functions for labeled displays:**

```python
# Display first n rows with labels in headers
labeled_head(df, n=5)

# Detailed info table with labels and null counts
labeled_info(df)

# Value counts with column label as title
labeled_value_counts(df, 'sexo')

# Cross-tabulation with labeled rows and columns
labeled_crosstab(df, rows='edad', cols='sexo', margins=True)

# Describe with labeled column names
labeled_describe(df)
```

**Direct label lookup:**
```python
get_label(dfcomp, 'p01')  # Returns original Spanish question text
```

### Working with Labels

Labels are stored in `df.attrs['variable_labels']` as a dictionary. When creating new DataFrames from subsets, reapply labels:
```python
df_filtered = dfcomp[dfcomp['sexo'] == 'MASCULINO']
df_filtered = set_labels(df_filtered, get_label(dfcomp, 'id'))  # Preserve labels
```

## Common Data Operations

### Lowercase All Values
Use the built-in `lowercase_df()` function which safely converts all string values to lowercase while preserving:
- Non-string values (NaN, numbers, dates)
- Data types
- Variable labels

```python
# Convert a single DataFrame
dfcomp = lowercase_df(dfcomp)

# Both DataFrames are already converted after loading
# (applied automatically in notebook)
dfcomp[dfcomp['sexo'] == 'masculino']  # Works with lowercase
dfcomp['edad'].unique()  # Returns lowercase values
```

**Under the hood:**
```python
def lowercase_df(df):
    df_lower = df.copy()
    labels = df.attrs.get('variable_labels', {})
    
    for col in df_lower.columns:
        df_lower[col] = df_lower[col].apply(
            lambda x: x.lower() if isinstance(x, str) else x
        )
    
    if labels:
        df_lower = set_labels(df_lower, labels)
    
    return df_lower
```

### Sorting
Sort by multiple columns with ascending/descending control:
```python
dfcomp.sort_values(by=['edad', 'nse'], ascending=[True, False])
```

### Handling NaN in Multi-Select Columns
These columns contain NaN for non-selected options. When aggregating, use `.value_counts(dropna=False)` to include NaN counts.

### Categorical Variables with Logical Ordering

Four demographic columns are automatically converted to ordered categorical types with logical ordering applied:

**Sexo (Gender):**
- Order: femenino < masculino

**Edad (Age Range):**
- Order: [18-30] < [31-40] < [41-50] < [51-60] < [61+]

**Niveduc (Education Level):**
- Order: media incompleta < media completa < técnica superior incompleta < técnica superior completa < universitaria incompleta < universitaria completa
- Represents progression from lowest to highest education

**Ocupacion (Occupation):**
- Order: cesante < estudiante < dueño(a) de casa < jubilado(a) < oficio menor < oficio calificado < empleado(a) administrativo(a) / técnico
- Represents hierarchical job levels (unemployed/low → employed high-level)

### Benefits of Ordered Categoricals

```python
# Sorting respects category order
dfcomp.sort_values('edad')  # Chronological order, not alphabetical

# Comparisons work logically
dfcomp[dfcomp['ocupacion'] < 'oficio menor']  # Gets unemployed/students/homemakers/retirees

# Aggregations maintain order
dfcomp.groupby('niveduc', observed=True).size()  # Shows education progression
```

### Value Counts with Ordered Categories

The key is using `sort=False` to preserve the logical order instead of sorting by frequency:

**Basic usage:**
```python
# Maintain logical order (not frequency-sorted)
dfcomp['ocupacion'].value_counts(sort=False)

# Add percentages
dfcomp['edad'].value_counts(sort=False, normalize=True) * 100

# Include missing values
dfcomp['sexo'].value_counts(sort=False, dropna=False)

# Sort by frequency if needed
dfcomp['niveduc'].value_counts(sort=True)  # Descending by count
```

**With helper function (formatted output):**
```python
# Shows label, counts, percentages with visual bar
labeled_value_counts_detailed(dfcomp, 'ocupacion')
```

**Advanced patterns:**
```python
# Filter by category range, then count
trabajadores = dfcomp[dfcomp['ocupacion'] >= 'oficio menor']
trabajadores['edad'].value_counts(sort=False)

# Crosstab with category order preserved
pd.crosstab(
    dfcomp['ocupacion'],      # Rows in job hierarchy order
    dfcomp['niveduc'],        # Columns in education order
    margins=True
)

# Compare distributions between groups
for sexo in ['femenino', 'masculino']:
    subset = dfcomp[dfcomp['sexo'] == sexo]
    print(subset['edad'].value_counts(sort=False, normalize=True))
```

**Key parameters:**
- `sort=False` → keeps category order (essential!)
- `sort=True` → sorts by frequency (descending)
- `normalize=True` → returns proportions (0-1) instead of counts
- `dropna=False` → includes missing values in count
- Multiply by 100 for percentages: `.value_counts() * 100`

### Filtering and Analysis
Work with short column names in code for clean syntax:
```python
# Filter by education level
high_ed = dfcomp[dfcomp['niveduc'] >= 'universitaria incompleta']

# Filter by occupation level
unemployed = dfcomp[dfcomp['ocupacion'] <= 'jubilado(a)']

# Group by demographics
by_nse = dfcomp.groupby(['nse', 'edad'], observed=True)['p01'].value_counts()

# Sort by hierarchy
sorted_by_job = dfcomp.sort_values('ocupacion')  # Low to high level
```

## Development Notes

### Pandas Warnings
- You may see `Pandas4Warning` about Categorical dtype construction. This is typically safe for this dataset.
- Use `.astype()` carefully with categorical columns to avoid dtype mismatches.

### Data Quality
- Verify data integrity after each major transformation (check row count, spot-check values)
- Use `.info()` frequently to track dtypes and null counts

### Spanish Text Considerations
- Survey responses use Spanish terminology (CESANTE = unemployed, DUEÑO = owner, OFICIO = skilled trade)
- When creating new columns based on text matching, account for case sensitivity before conversion
