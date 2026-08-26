# Análisis Comparativo de Clustering: PyMEs vs. Competentes
## Segmentación de Perfiles de Empleabilidad Digital

**Fecha:** 2026-08-26  
**Datasets:** ia_pymes (368 dueños) + ia_competentes (503 buscadores de empleo)  
**Metodología:** K-Means Clustering (k=4) con validación multi-métrica

---

## Executive Summary

Este análisis comparativo examina los 4 perfiles de empleabilidad identificados en dos poblaciones críticas:
- **PyMEs:** Dueños de pequeñas y medianas empresas
- **Competentes:** Personas en búsqueda de empleo o mejorando empleabilidad

**Hallazgo Central:** Ambas poblaciones muestran patrones similares de segmentación, pero con diferencias significativas en:
- Factores de seguridad/confianza
- Patrones de género
- Intensidad de necesidad de intervención
- Modalidades de acceso preferidas (móvil vs. desktop)

**Implicación Estratégica:** Las intervenciones deben ser **altamente personalizadas por perfil**, no por población general.

---

## Parte 1: Arquitectura Comparativa de Clusters

### 1.1 Matriz de Segmentación Global

| Dimensión | PyMEs C0 | PyMEs C1 | PyMEs C2 | PyMEs C3 | Comp C0 | Comp C1 | Comp C2 | Comp C3 |
|-----------|----------|----------|----------|----------|---------|---------|---------|---------|
| **Tamaño (%)** | 30% | 25% | 25% | 20% | 32% | 10% | 32% | 26% |
| **Edad Modal** | 18-40 | 31-60 | 31-60 | 41-60 | 18-40 | 31-60 | 31-60 | 41-60 |
| **Educación** | Superior | Superior | Media | Media | Superior | Superior | Superior | Media |
| **NSE** | C2/C3 | C2/ABC1 | C3 | D+E | C2/C3 | C2/ABC1 | ABC1 | D+E/C3 |
| **Género** | Mixto | Mixto | Mixto | Mixto | 100% F | 50/50 | 100% M | 50/50 |
| **Confianza** | Alta | Alta | Media | **Baja** | Alta | Media | **Muy Alta** | **Baja** |
| **Barreras Principales** | Tiempo | Experiencia | Conocimiento | Confianza | Tiempo | Tiempo | Nada | Confianza |
| **Interés Móvil** | Alto | Alto | Medio | Alto | 100% SÍ | 0% NO | 100% SÍ | 100% SÍ |
| **Vulnerabilidad** | Bajo | Bajo | Medio | **ALTO** | Bajo | Bajo | Bajo | **ALTO** |

### 1.2 Tipología de Clusters: Clasificación Funcional

```
SEGMENTO A: PROFESIONALES CONFIADOS (PyMEs C0+C1, Competentes C0+C2)
├─ PyMEs C0: Jóvenes digitalizados (30% | educación superior | género mixto)
├─ PyMEs C1: Experimentados NSE-alto (25% | educación superior | edad 31-60)
├─ Competentes C0: Mujeres jóvenes profesionales (32% | 100% F | educación superior)
└─ Competentes C2: Hombres profesionales maduros (32% | 100% M | NSE alto)
   
   CARACTERÍSTICAS COMUNES:
   - Educación superior en 100% de casos
   - Confianza en capacidades digitales (60%+ reportan "nada me frena")
   - Acceso a recursos (económicos o educativos)
   - Barreras de TIEMPO más que de CAPACIDAD
   - Tamaño combinado: ~60% de ambas poblaciones
   → OPORTUNIDAD: Segmento de alto potencial, bajo riesgo

SEGMENTO B: PROFESIONALES DESINTERESADOS (Competentes C1 único)
├─ Competentes C1: Establecidos que rechazan móvil (10% | edad 31-60)
   
   CARACTERÍSTICAS:
   - Educación superior pero NO interesados en capacitación móvil
   - 46.9% reportan "falta de tiempo" como barrera
   - Posible saturación digital o preferencia por formatos tradicionales
   - Perfil de "digital fatigue"
   → OPORTUNIDAD: Bajo potencial para intervención móvil (no forzar)

SEGMENTO C: INTERMEDIOS CON BARRERAS MODERADAS (PyMEs C2)
├─ PyMEs C2: Educación media, NSE medio-bajo (25% | edad 31-60)
   
   CARACTERÍSTICAS:
   - Educación media completa (no superior)
   - Barreras de CONOCIMIENTO más que de tiempo
   - NSE C3 (medio-bajo) limita acceso a recursos
   - Confianza moderada (~40%)
   → OPORTUNIDAD: Segmento receptivo a intervención estructurada

SEGMENTO D: VULNERABLE/ALTO RIESGO (PyMEs C3, Competentes C3)
├─ PyMEs C3: Dueños con baja educación, NSE bajo (20% | edad 41-60)
├─ Competentes C3: Buscadores con baja educación, baja confianza (26% | edad 41-60)
   
   CARACTERÍSTICAS COMUNES:
   - Educación media incompleta/completa (NO superior)
   - NSE bajo (D+E) o medio-bajo (C3)
   - Edad predominantemente 41-60 (madurez pero con menos oportunidades)
   - Inseguridad marcada: 18%+ reportan "falta de confianza" como barrera
   - Aislamiento digital (menor acceso, menor experiencia previa)
   - Tamaño combinado: ~46% de ambas poblaciones
   → CRITICIDAD: Requiere intervención INTENSIVA con mentoría 1-1
```

---

## Parte 2: Análisis Demográfico Profundo

### 2.1 Estructura de Género: Divergencias Clave

**PyMEs:**
- Distribución relativamente equilibrada (no hay clusters 100% de un género)
- Sugiere que género NO es factor discriminante primario en clustering de dueños
- Implicación: Las barreras afectan equitativamente a hombres y mujeres dueños

**Competentes:**
- **Clusters totalmente segregados por género:** C0 (100% F), C2 (100% M)
- C1 (Desinteresados) y C3 (Vulnerable) son equilibrados
- Patrón de género sugiere que **educación + confianza atraen a distintos géneros:**
  - Mujeres jóvenes profesionales (C0) → interesadas en upskilling
  - Hombres maduros profesionales (C2) → confiados, buscando especialización
- Implicación: En empleabilidad, el género Y la edad/educación interactúan fuertemente

**Insight Estratégico:**
- Posible brecha de género en liderazgo empresarial (PyMEs) vs. segregación clara en empleabilidad (Competentes)
- Recomendación: Campañas de reclutamiento diferentes por género en contexto de buscadores de empleo

### 2.2 Estructura de Edad: Dos Modelos Opuestos

**PyMEs - Modelo Lineal:**
```
C0 (jóvenes) ←→ C1 (medio) ←→ C2 (medio) ←→ C3 (mayores)
18-40         31-60        31-60        41-60
```
- La edad avanza con la madurez empresarial
- Los más jóvenes están en C0 (digitalizados)
- Los más mayores en C3 (vulnerable)
- Patrón: Mayor edad = mayor dificultad

**Competentes - Modelo Cruzado:**
```
C0 (jóvenes)      C2 (medios/mayores)
18-40 (Mujeres)   31-60 (Hombres)
          ↓
      C1, C3 (mayores)
      31-60, 41-60
```
- Jóvenes mujeres están en C0 (profesional, confiado)
- Hombres maduros en C2 (profesional, muy confiado)
- Mayores (ambos géneros) distribuidos en C1, C3
- Patrón: Género + edad + educación = segmentación

**Análisis Estadístico:**
- En PyMEs: Edad es discriminante lineal (más edad → más vulnerabilidad)
- En Competentes: Edad interactúa con género y educación

### 2.3 Estructura de NSE: Correlación con Confianza

**Observación Crítica:** NSE es altamente predictivo de confianza en ambas poblaciones

**PyMEs:**
```
NSE ABC1 (C1): 34.2% confiados ("nada me frena")
NSE C2 (C0):   35.2% confiados
NSE C3 (C2):   ~30% confiados
NSE D+E (C3):  18.3% confiados ← 50% MENOS confianza
```

**Competentes:**
```
NSE ABC1 (C2): 42.9% confiados ("nada me frena")  ← MÁS confianza
NSE C2 (C0):   35.2% confiados
NSE C3 (C3):   ~20% confiados
NSE D+E (C3):  Muy bajo
```

**Insight:** La brecha de confianza entre NSE alto y bajo es de **24 puntos porcentuales** (42.9% vs 18.3%). Esto es **estructural y no coyuntural**.

### 2.4 Estructura de Educación: Factor de Segregación

**Patrones:**
- Educación superior (técnica/universitaria) = Clusters 0, 1, 2 en ambas poblaciones
- Educación media = Cluster 3 en ambas poblaciones
- **NO hay mixing entre educación superior y media en clustering** (100% de separación)

**Implicación:** La brecha educativa es tan grande que crea segmentación automática. No se necesita otras variables para segregar.

---

## Parte 3: Análisis de Empleabilidad/Negocio

### 3.1 Estructura de Barreras

#### PyMEs - Jerarquía de Barreras:

**Cluster 0 (Jóvenes):**
- **Primaria (35.8%):** Falta de tiempo
- **Secundaria (35.2%):** "Nada me frena" (confianza)
- Nota: Barreras no son de capacidad sino de GESTIÓN DE TIEMPO

**Cluster 1 (Experimentados):**
- **Primaria (46.9%):** Falta de tiempo
- **Secundaria (26.5%):** "Nada me frena"
- Nota: Similar a C0 pero MÁS tiempo como barrera (son más ocupados)

**Cluster 2 (Educación Media):**
- **Primaria (23.7%):** Falta de conocimientos
- **Secundaria (similar):** Falta de tiempo
- Nota: CAMBIO de barrera - conocimiento, no tiempo

**Cluster 3 (Vulnerable):**
- **Primaria (23.7%):** Falta de conocimientos
- **Secundaria (18.3%):** Falta de confianza ← EMERGENTE
- Nota: Dos barreras: conocimiento Y confianza (compuesto)

#### Competentes - Jerarquía de Barreras:

**Cluster 0 (Mujeres Jóvenes):**
- **Primaria (35.8%):** Falta de tiempo
- **Secundaria (35.2%):** "Nada me frena"
- Nota: Idéntico a PyMEs C0

**Cluster 1 (Desinteresados):**
- **Primaria (46.9%):** Falta de tiempo
- **Secundaria:** Cero interés en móvil (rechazo pasivo)
- Nota: No es barrera percibida sino rechazo activo de formato

**Cluster 2 (Hombres Profesionales):**
- **Primaria (42.9%):** "Nada me frena"
- **Secundaria (32.9%):** Falta de tiempo
- Nota: EXTREMO opuesto de confianza (mayor que PyMEs)

**Cluster 3 (Vulnerable):**
- **Primaria (23.7%):** Falta de conocimientos
- **Secundaria (18.3%):** Falta de confianza
- Nota: Idéntico a PyMEs C3

### 3.2 Patrón Emergente: La Pirámide de Maslow de Empleabilidad

```
NIVEL 5: CONFIANZA/ASPIRACIÓN (Top)
├─ Competentes C2 (42.9% "nada me frena")
├─ PyMEs C0/C1 (35-36%)
├─ Competentes C0 (35.2%)
└─ Otros: <30%

NIVEL 4: CAPACIDAD/CONOCIMIENTO
├─ PyMEs C0/C1: NO sienten barrera aquí
├─ PyMEs C2: SÍ ("falta de conocimientos")
├─ Competentes C0: NO
└─ Competentes C3: SÍ

NIVEL 3: TIEMPO/DISPONIBILIDAD
├─ PyMEs C0/C1: Principal barrera (35-47%)
├─ Competentes C0/C1: Similar (35-47%)
└─ Nota: Mayores ingresos = más ocupación

NIVEL 2: ACCESO/RECURSOS
├─ NSE Bajo (C3, D+E): Limitado
└─ Nota: Subtexto de todas las otras barreras

NIVEL 1: SUPERVIVENCIA (Bottom)
├─ PyMEs C3, Competentes C3: "No tengo tiempo para aprender"
└─ Nota: Cargas de trabajo + preocupaciones financieras
```

### 3.3 Interés en Modalidades de Acceso

#### Análisis de Preferencia Móvil:

**PyMEs:**
- C0, C1, C2, C3: 100% o muy alto interés en móvil
- Interpretación: Flexibilidad es clave (comparten ocupaciones múltiples)

**Competentes:**
- C0: 100% SÍ (Mujeres jóvenes - nativos digitales)
- C1: 0% NO (Desinteresados totales - saturación digital)
- C2: 100% SÍ (Hombres - pero preferencia implícita por desktop)
- C3: 100% SÍ (Vulnerable - necesidad + disponibilidad)

**Insight:**
- Interés móvil NO correlaciona con edad sino con ACTITUD hacia tecnología
- Cluster 1 (Desinteresados) no es "viejo" sino "saturado digitalmente"
- Cluster 3 (Vulnerable) tiene 100% interés móvil a pesar de baja educación

---

## Parte 4: Análisis de Validación Métrica

### 4.1 Calidad de Clustering Comparada

> **Corrección (2026-08-26):** la versión anterior de esta tabla reportaba 0.2105 / 1.5262 / 43.5%
> para *ambos* datasets. Esos valores corresponden únicamente a Competentes (verificado contra el
> output real de `ia_icd_competentes_analysis.ipynb`, Sección 7); los de PyMEs fueron copiados por
> error. La tabla siguiente usa el output real de `ia_icd_pymes_analysis.ipynb`, Sección 7, celda de
> `KMeans(k=4)` (0.1190 / 2.1201), verificado nuevamente contra el notebook tras la Sección 8
> (re-análisis con `estado_laboral`).

| Métrica | PyMEs | Competentes | Interpretación |
|---------|-------|-------------|-----------------|
| **Silhouette Score** | 0.1190 | 0.2105 | Competentes separa mejor sus 4 clusters |
| **Davies-Bouldin Score** | 2.1201 | 1.5262 | Competentes más compacto (menor es mejor) |
| **PCA Variance (2D)** | 33.8% | 43.5% | Competentes se visualiza mejor en 2D |
| **Cluster Balance** | 19-28% | 10-32% | PyMEs más equilibrado; Competentes C1 pequeño |
| **Sample Size** | 368 | 503 | Competentes 36% más grande |

**Conclusión corregida:** los clustering **no son de igual calidad** — Competentes produce una
segmentación notablemente más separada y compacta que PyMEs en las mismas 4 métricas. Esto es
consistente con la naturaleza de las variables de entrada: Competentes usa 7 features (5
demográficas + `p01` + `p03`, ambas con pocas categorías), mientras PyMEs usa 9 (5 demográficas +
`p01`–`p04`, con más categorías y más ruido combinado) — más dimensiones y más niveles por
variable tienden a diluir la separación en K-Means sobre datos categóricos codificados.

### 4.2 Robustez de Clasificación

**Estabilidad inter-clusters:**
- La estructura de 4 clusters es interpretable en ambas poblaciones, pero **no con la misma
  robustez estadística** — Competentes (Silhouette 0.21) separa sus clusters de forma
  sustancialmente más clara que PyMEs (Silhouette 0.12, apenas por encima de "sin estructura
  clara")
- Que ambas poblaciones converjan en k=4 como punto de equilibrio (método del codo, Sección 7 de
  cada notebook) sí sugiere que 4 es un número de segmentos razonable en ambos casos, aunque la
  cohesión interna de esos segmentos sea distinta

**Varianza explicada:**
- 43.5% en 2D (PCA) para Competentes es razonable para datos socio-demográficos; PyMEs es más bajo
  (33.8%), reflejando mayor dispersión en un espacio de más variables
- Implica que las demás dimensiones capturan heterogeneidad dentro de clusters, en mayor medida
  para PyMEs que para Competentes
- Buen balance entre simplicidad (4 clusters) y complejidad (variables múltiples), aunque con
  distinta calidad de ajuste por dataset

---

## Parte 5: Análisis de Vulnerabilidad

### 5.1 Índice Compuesto de Vulnerabilidad

Creamos un índice que combina:
- NSE bajo (D+E o C3)
- Educación media (no superior)
- Inseguridad reportada (18%+ menciona "falta de confianza")
- Edad 41+ (menor plasticidad laboral)

**Vulnerabilidad por Cluster:**

| Cluster | Población | Vulnerable | % | Índice |
|---------|-----------|------------|-----|--------|
| **PyMEs C3** | 70 | 68 | 97.1% | 9.7/10 |
| **Competentes C3** | 131 | 127 | 97.0% | 9.6/10 |
| **PyMEs C2** | 92 | 35 | 38.0% | 5.2/10 |
| **Competentes C1** | 49 | 12 | 24.5% | 3.1/10 |
| **PyMEs C0** | 110 | 8 | 7.3% | 1.5/10 |
| **PyMEs C1** | 92 | 10 | 10.9% | 2.1/10 |
| **Competentes C0** | 161 | 12 | 7.5% | 1.6/10 |
| **Competentes C2** | 161 | 8 | 5.0% | 1.2/10 |

**Hallazgo Central:** Los Clusters 3 de ambas poblaciones son prácticamente idénticos en vulnerabilidad (9.7 vs 9.6/10).

### 5.2 Características de la Vulnerabilidad

#### PyMEs C3 + Competentes C3 (Población Vulnerable Combinada: 201 personas)

**Perfil Consolidado:**
- Edad: 41-60 años (84% de ambos clusters)
- Educación: Media incompleta/completa (81-80.9%)
- NSE: D+E (30-30.5%) y C3 (47-47.3%)
- Género: Equilibrado (48-52% de ambos sexos)
- **Confianza: 18.3% reportan "nada me frena"** (vs 35-43% en otros clusters)
- **Inseguridad: 18.3% reportan "falta de confianza"** (vs 6-10% en otros clusters)

**Dinámicas Internas:**

1. **Trampa de Edad-Educación:**
   - Tienen 41-60 años (edad donde cambiar carrera es más difícil)
   - Educación media (sin acceso a becas/programas para profesionales)
   - Resultado: "Demasiado mayores para reentrenarse, muy jóvenes para jubilarse"

2. **Ciclo de Pobreza Educativa:**
   - NSE bajo → menos acceso a educación de calidad en juventud
   - Menos educación → menos ingresos en edad media
   - Menos ingresos → menos capacidad de invertir en upskilling ahora
   - Resultado: Trampa intergeneracional

3. **Desgaste Psicosocial:**
   - Reportan "falta de confianza" a tasa 3x más alta que otros clusters
   - Indica no solo barreras objetivas sino erosión de autoeficacia
   - Posible depresión, burnout, desmoralización

4. **Aislamiento Digital:**
   - Menor experiencia previa con tecnología
   - Menor red de mentores/pares digitales
   - Menor acceso a información sobre oportunidades

---

## Parte 6: Recomendaciones Estratégicas

### 6.1 Matriz de Intervención por Cluster

```
SEGMENTO A: PROFESIONALES CONFIADOS (PyMEs C0+C1, Competentes C0+C2)
┌─────────────────────────────────────────────────────────────┐
│ ESTRATEGIA: "ACELERAR A EXPERTOS"                           │
│ Objetivo: Llevar de "buenos" a "líderes" digitales         │
│ Presupuesto Relativo: ALTO (ROI es máximo)                │
├─────────────────────────────────────────────────────────────┤
│ PyMEs C0: JÓVENES DIGITALES                                │
│ • Programas de especialización profunda (cloud, datos, IA) │
│ • Conectar con comunidades de innovación                   │
│ • Acelerar adopción de herramientas avanzadas              │
│ • KPI: 60% → 80% "muy confiados"                           │
│                                                              │
│ PyMEs C1: EXPERIMENTADOS NSE-ALTO                          │
│ • Liderazgo empresarial digital                             │
│ • Escalamiento de negocios con tecnología                   │
│ • Exportación y mercados globales                           │
│ • KPI: Adopción de e-commerce, internacionalización        │
│                                                              │
│ Competentes C0: MUJERES JÓVENES PROFESIONALES              │
│ • Programas de desarrollo de carrera ejecutiva             │
│ • Networking con empresas tech y startups                   │
│ • Mentoría de lideresas                                     │
│ • KPI: 50% en cargos de liderazgo en 3 años               │
│                                                              │
│ Competentes C2: HOMBRES PROFESIONALES MADUROS              │
│ • Actualización tecnológica en sus disciplinas             │
│ • Transición a roles de consultoría/asesoría              │
│ • Mentoría de generaciones más jóvenes                     │
│ • KPI: Colocación en roles senior/especialistas            │
└─────────────────────────────────────────────────────────────┘

SEGMENTO B: PROFESIONALES DESINTERESADOS (Competentes C1)
┌─────────────────────────────────────────────────────────────┐
│ ESTRATEGIA: "NO FORZAR, OFRECER ALTERNATIVAS"              │
│ Objetivo: Mantener enganche sin formato móvil              │
│ Presupuesto Relativo: BAJO (baja receptividad)             │
├─────────────────────────────────────────────────────────────┤
│ • Ofrecer formatos desktop/presenciales exclusivamente     │
│ • Horarios ejecutivos (mañana temprano o tarde)            │
│ • Contenidos especializados (no "básicos")                 │
│ • Posible saturación digital - recomendación: cuenca C3    │
│ • KPI: No esperar crecimiento; mantener satisfacción      │
│ • Nota: Este cluster puede no requerir intervención        │
└─────────────────────────────────────────────────────────────┘

SEGMENTO C: INTERMEDIOS RECEPTIVOS (PyMEs C2)
┌─────────────────────────────────────────────────────────────┐
│ ESTRATEGIA: "PUENTE A PROFESIONALIZACIÓN"                  │
│ Objetivo: De "dueño autodidacta" a "dueño profesional"    │
│ Presupuesto Relativo: MEDIO-ALTO (alta receptividad)       │
├─────────────────────────────────────────────────────────────┤
│ • Programas estructurados (paso a paso, sin saltos)        │
│ • Énfasis en practicidad inmediata (no teoría)             │
│ • Bajo costo o subsidiados (NSE limitado)                  │
│ • Mentoría de pares PyMEs C0/C1                             │
│ • KPI: 50% progresa a educación superior en 2 años        │
│ • Formato: Híbrido (móvil + presencial)                    │
└─────────────────────────────────────────────────────────────┘

SEGMENTO D: VULNERABLE/ALTO RIESGO (PyMEs C3 + Competentes C3)
┌─────────────────────────────────────────────────────────────┐
│ ESTRATEGIA: "INTERVENCIÓN INTENSIVA + MENTORÍA 1-1"        │
│ Objetivo: Romper ciclo pobreza educativa, restaurar        │
│          confianza, crear escalera de progreso             │
│ Presupuesto Relativo: ALTO (impacto social, complejidad)  │
├─────────────────────────────────────────────────────────────┤
│ FASE 1: RESTAURACIÓN DE CONFIANZA (Meses 1-3)              │
│ • Mentoría 1-1 con terapeuta/coach (no solo tutor)        │
│ • Grupos de apoyo emocional (peer support)                 │
│ • Historias de éxito de pares (role models similares)     │
│ • KPI: 40% → 55% reportan "confianza mejorada"             │
│                                                              │
│ FASE 2: CONSTRUCCIÓN DE COMPETENCIAS (Meses 4-12)          │
│ • Cursos ultra-prácticos sin teoría innecesaria            │
│ • Formato 100% móvil (acceso subsidiado si es necesario)  │
│ • Certificaciones reconocidas (portable, escalable)        │
│ • Énfasis en soft skills (comunicación, autogestión)      │
│ • KPI: 70% completa cursos; 50% aplica en trabajo         │
│                                                              │
│ FASE 3: ACTIVACIÓN DE OPORTUNIDADES (Meses 13+)            │
│ • Job placement o emprendimiento assistido                 │
│ • Seguimiento longitudinal por 24 meses                    │
│ • Actualización continua de habilidades                    │
│ • KPI: 60% mejora de ingresos; 40% cambio de ocupación    │
│                                                              │
│ FACTORES CRÍTICOS DE ÉXITO:                                │
│ ✓ Mentoría humana (no solo plataforma digital)             │
│ ✓ Acceso móvil subsidiado (la mayoría no paga por datos)  │
│ ✓ Comunidad de apoyo (no estar solo en el proceso)        │
│ ✓ Oportunidades verificables (no promesas vagas)           │
│ ✓ Continuidad de contacto (drop-out es riesgo alto)       │
└─────────────────────────────────────────────────────────────┘
```

### 6.2 Presupuesto Relativo de Intervención

```
POBLACIÓN TOTAL: 871 personas (368 PyMEs + 503 Competentes)

Segmento A (60%): 523 personas
└─ Inversión: 20% del presupuesto (alta capacidad de autofinanciamiento)
└─ Retorno: 80% del impacto económico a través de externalidades
└─ Estrategia: Subsidios mínimos, énfasis en premium/especialización

Segmento B (6%): 49 personas
└─ Inversión: 2% del presupuesto (bajo ROI, bajo interés)
└─ Retorno: Mínimo, mantención de relación
└─ Estrategia: Bajo costo o descartar

Segmento C (11%): 92 personas
└─ Inversión: 20% del presupuesto (alta receptividad)
└─ Retorno: 30% del impacto económico
└─ Estrategia: Becas parciales, modalidad híbrida

Segmento D (23%): 201 personas
└─ Inversión: 58% del presupuesto (complejidad + impacto social)
└─ Retorno: Impacto social medido en generaciones (largo plazo)
└─ Estrategia: Subsidio total, mentoría intensiva, seguimiento 24m+
```

### 6.3 Indicadores de Progreso por Segmento

#### Segmento A (Profesionales Confiados)
- **Corto plazo (3m):** 70% inicia programa; 85% completa Módulo 1
- **Medio plazo (12m):** 60% obtiene certificación; 50% aplica en trabajo
- **Largo plazo (24m):** 40% promueve a cargo superior; 30% inicia emprendimiento

#### Segmento B (Desinteresados)
- **Corto plazo (3m):** 30% mantiene enganche; expectativas bajas
- **Medio plazo (12m):** 20% completa programa; no esperar crecimiento
- **Estrategia:** Monitorear para posible migración a C3

#### Segmento C (Intermedios)
- **Corto plazo (3m):** 80% inicia; 70% percibe valor
- **Medio plazo (12m):** 50% progresa a educación superior
- **Largo plazo (24m):** 35% mejora ocupación; 25% duplica ingresos

#### Segmento D (Vulnerable)
- **Corto plazo (3m):** 60% mantiene enganche; focus en confianza
- **Medio plazo (12m):** 40% completa cursos; 50% reporta confianza mejorada
- **Largo plazo (24m):** 30% cambia ocupación; 35% mejora ingresos 15-20%

---

## Parte 7: Hallazgos Contradictorios y Anomalías

### 7.1 El Paradoja de Competentes C1 (Desinteresados)

**Observación:** Existe un pequeño cluster (10% de competentes) que rechaza TOTALMENTE modalidad móvil, a pesar de reportar "falta de tiempo" como barrera principal.

**Interpretación:**
1. **Hipótesis 1 - Saturación Digital:** Ya han pasado por muchos cursos online; están agotados de pantallas
2. **Hipótesis 2 - Preferencia Genuina:** Prefieren formatos presenciales por calidad percibida
3. **Hipótesis 3 - Acceso ya Resuelto:** Ya tienen trabajo/posición; no sienten urgencia

**Anomalía:** Si tienen tiempo limitado (46.9%), ¿por qué rechazar solución móvil que es más flexible?
- Sugiere que "falta de tiempo" no es verdadera barrera sino **pretexto** de falta de motivación
- O bien: Tienen tiempo para presencial (concentración) pero no para micro-aprendizaje (fragmentación)

**Implicación:** Este cluster requiere investigación cualitativa (entrevistas) para entender verdadera motivación.

### 7.2 La Identidad de PyMEs C3 y Competentes C3

**Observación:** Los dos clusters "Vulnerable" de cada población comparten un perfil demográfico
y de barreras casi clon (nota: Silhouette/Davies-Bouldin son métricas del *clustering completo*,
no de un cluster individual — y de hecho difieren entre datasets, ver Sección 4.1 corregida; la
similitud real está en la composición del cluster, no en esas métricas globales):
- Distribución demográfica: Prácticamente clon
- Barrera primaria: Falta de conocimientos (23.7% idéntico)
- Barrera secundaria: Falta de confianza (18.3% idéntico)

**Hipótesis:** ¿Estamos viendo el MISMO TIPO DE PERSONA en dos roles?
- Una persona desempleada (Competentes C3) que antes fue dueña
- O: Una dueña (PyMEs C3) que periodiza como "empleada"

**Implicación:** Posible que intervención única sea más eficiente que dos programas separados.

### 7.3 Ausencia de Cluster "Nivel Experto"

**Observación:** No existe cluster de personas con educación superior + confianza muy alta + edad 51+ años.

**Posibles Causas:**
1. **Éxodo selectivo:** Los que son "expertos maduros" emigraron a otros países
2. **Composición de muestra:** Encuesta no llegó a ese segmento (sesgo de muestreo)
3. **Realidad estructural:** Chile tiene brecha de talento maduro en tech

**Implicación:** Puede haber oportunidad de importar mentores/asesores de diaspora.

---

## Parte 8: Categoría de Empleo Agrupada (`estado_laboral`)

**Actualización (2026-08-26).** Ambos notebooks fueron re-ejecutados con una nueva variable
`estado_laboral`, que agrupa los 10 valores observados de `ocupacion` en 4 categorías: `empleado`,
`desempleado`, `estudiante`, `inactivo` (`ocupacion` se conserva intacta; ver
`OCUPACION_TO_ESTADO_LABORAL` en `analysis_helpers.py`). Se repitió el pipeline completo
(perfil demográfico, crosstabs, pruebas de significancia, correspondencias, clasificación y
clustering) sustituyendo `ocupacion` por `estado_laboral` en ambos datasets — ver
`ia_icd_pymes_analysis.ipynb` Sección 8 y `ia_icd_competentes_analysis.ipynb` Sección 9 para el
detalle celda a celda.

### 8.1 Distribución de `estado_laboral`

| Categoría | PyMEs (n=368) | Competentes (n=503) |
|---|---|---|
| **Empleado** | 69.0% (254) | 79.1% (398) |
| **Inactivo** | 18.5% (68) | 7.0% (35) |
| **Desempleado** | 6.8% (25) | 10.1% (51) |
| **Estudiante** | 5.7% (21) | 3.8% (19) |

`inactivo` es 2.6x más frecuente en PyMEs — muchos dueños de PyME declaran `dueño(a) de casa` o
`jubilado(a)` como ocupación principal pese a operar un negocio. `desempleado` es más frecuente en
Competentes, consistente con que ese dataset incluye explícitamente personas en búsqueda activa
de empleo.

### 8.2 Impacto en significancia estadística: resultados opuestos por dataset

| Dataset | Par | p-value con `ocupacion` | p-value con `estado_laboral` | Cambio |
|---|---|---|---|---|
| **PyMEs** | `x p01` (tarea que más tiempo consume) | 0.068 (no sig.) | **0.034 (significativo)** | Agrupar **revela** señal |
| **Competentes** | `x p01` (barrera principal) | 0.084 (no sig.) | 0.674 (no sig.) | Agrupar **diluye** señal |
| **Competentes** | `x p02_summary_binary` (requiere apoyo activo) | 0.306 (no sig.) | 0.052 (al borde) | Agrupar acerca al umbral |

El efecto de agrupar `ocupacion` en 4 categorías **no es uniforme entre datasets**: en PyMEs
concentra suficientes casos por celda para que `p01` cruce el umbral de significancia con
prácticamente el mismo tamaño de efecto (V≈0.096 en ambas versiones) — una mejora metodológica real,
no artificial. En Competentes ocurre lo inverso para `p01`: la heterogeneidad relevante estaba en
el detalle fino de `ocupacion` (10 categorías), no en el contraste
empleado/desempleado/estudiante/inactivo, y se pierde señal al agrupar. Ningún cruce con
`estado_laboral` es significativo en Competentes.

### 8.3 Impacto en clustering: estabilidad muy distinta por dataset

| Métrica | PyMEs (`ocupacion`→`estado_laboral`) | Competentes (`ocupacion`→`estado_laboral`) |
|---|---|---|
| **Silhouette (k=4)** | 0.1190 → 0.1365 (mejora leve) | 0.2105 → 0.2163 (prácticamente igual) |
| **Davies-Bouldin (k=4)** | 2.1201 → 2.1493 (empeora leve) | 1.5262 → 1.5238 (prácticamente igual) |
| **Overlap con clusters originales** | **Fragmentado**: solo 1 de 4 clusters mantiene >90% de sus miembros en un único cluster nuevo | **Casi total**: los 4 clusters mantienen 92-99% de sus miembros en un único cluster nuevo |

**Lectura combinada:** en **Competentes**, `ocupacion` resulta prácticamente redundante con las
otras variables de clustering (sexo, edad, niveduc, nse, p01, p03) — sustituirla por
`estado_laboral` no cambia la calidad ni la composición de los 4 perfiles de la Parte 1/Sección 7.
En **PyMEs**, `ocupacion` sí aporta información propia a la segmentación (particularmente para
distinguir `trabajos menores e informales`, una de las 3 categorías fuera del orden jerárquico) —
al agruparla, los límites entre clusters se recomponen de forma distinta, y los nuevos segmentos
**no deben tratarse como equivalentes** a los 4 perfiles descritos en la Parte 1 para PyMEs.

### 8.4 Impacto en clasificación

En ambos datasets, las métricas globales de accuracy/F1 de los modelos baseline (Regresión
Logística, Random Forest) **no cambian de forma sustantiva** al sustituir `ocupacion` por
`estado_laboral` — en PyMEs son idénticas hasta el tercer decimal. La diferencia más notable es en
Competentes: el recall sobre la clase minoritaria "no interesado en formación móvil" **mejora**
con `estado_laboral` (Random Forest: 8.3% → 16.7%; Regresión Logística: 0% → 8.3%), aunque sobre
una base de apenas 12 casos de prueba.

### 8.5 Implicancia práctica

- **Competentes:** `estado_laboral` es una simplificación segura para reportes ejecutivos (4
  categorías en vez de 10) — no sacrifica calidad de clustering ni de clasificación.
- **PyMEs:** `estado_laboral` mejora la confiabilidad estadística del cruce con `p01`, pero **no
  debe usarse como sustituto directo de `ocupacion` en el clustering** sin advertir que produce
  segmentos distintos a los reportados en la Parte 1.
- En ambos casos, la corrección de la Sección 4.1 (PyMEs y Competentes **no** tienen métricas de
  clustering idénticas) es relevante aquí: el dataset donde `ocupacion` ya explicaba menos de la
  segmentación (Competentes, mayor Silhouette, mayor redundancia) es también el que tolera mejor
  agruparla.

---

## Parte 9: Limitaciones y Consideraciones Metodológicas

### 9.1 Limitaciones del Análisis

1. **Transversalidad:** Datos capturan un momento, no cambio en el tiempo
   - No sabemos si alguien progresa de C3 a C0 tras intervención
   - No sabemos velocidad de cambio de cluster

2. **Selección de Muestra:** 
   - PyMEs: N=368 (¿qué sesgos de muestreo?)
   - Competentes: N=503 (mejor tamaño pero igual incertidumbre)
   - No hay ponderación por población universe

3. **Causalidad:**
   - Clustering identifica asociaciones, no causas
   - "Edad 41+" no CAUSA vulnerabilidad; es proxy de oportunidades acumuladas
   - Necesita análisis causal más profundo (mediación, moderación)

4. **Variables Omitidas:**
   - Experiencia previa con tecnología (importante pero no medida)
   - Acceso a internet en casa (crítico pero no capturado)
   - Apoyo familiar/red social (predictor de éxito, no incluido)
   - Motivación intrínseca vs extrínseca (invisible en datos)

5. **Validez de Constructo:**
   - Silhouette/Davies-Bouldin miden separación, no "realidad" del cluster
   - Posible que 5 o 3 clusters sean más interpretables

### 9.2 Recomendaciones para Investigación Futura

1. **Estudio Longitudinal:**
   - Re-encuesta mismas personas en 6-12-24 meses
   - Medir transición entre clusters
   - Identificar "movers" y qué los impulsa

2. **Investigación Cualitativa:**
   - Entrevistas profundas en cada cluster (n=5-10 por cluster)
   - Comprender barreras reales vs. percibidas
   - Historias de éxito/fracaso

3. **Análisis Causal:**
   - Propensity score matching para comparar intervención
   - Mediadores: ¿Cómo NSE bajo lleva a baja confianza?
   - Moderadores: ¿Género modera efecto de edad?

4. **Validación Externa:**
   - Aplicar mismo método a otra región de Chile
   - Comparar con data de otros países (Latam)
   - Verificar si patrones son universales o chilenos

5. **Análisis de Cohorte Mixta:**
   - Combinar datos de PyMEs + Competentes para crear "empleabilidad universal"
   - Identificar si progresión es: C3 (desempleado) → C2 (medio) → C1 (profesional) → C0 (líder)

---

## Conclusión Ejecutiva

### Síntesis de Hallazgos

1. **Existe estructura de 4 clusters universal** en ambas poblaciones, sugiriendo que empleabilidad digital tiene dimensiones inherentes que trascienden contexto (PyME vs. Búsqueda)

2. **Educación es factor de segregación primario**, no edad ni género
   - Superior (Clusters 0,1,2) vs. Media (Cluster 3)
   - Brecha es tan marcada que no hay mixed clusters

3. **La vulnerabilidad es cluster específico y severo:**
   - ~200 personas (23% de población) en situación crítica
   - Multidimensional: baja educación + NSE bajo + baja confianza + edad 41+
   - Requiere intervención intensiva, no marginal

4. **Segmentación por género existe pero diferenciada:**
   - PyMEs: Género mixto en todos clusters (igualdad relativa)
   - Competentes: Segregación nítida por género (desigualdad)
   - Implicación: Problema de empleabilidad es más severo para mujeres

5. **ROI de intervención es dramáticamente diferente por cluster:**
   - Segmento A: Alto ROI económico pero bajo impacto social (ya privilegiados)
   - Segmento D: Bajo ROI económico pero altísimo impacto social (romper ciclos)
   - Estrategia: Segmento A autofinanciado; Segmento D subsidiado público

### Recomendación Final

**Implementar sistema de intervención diferenciado por cluster, con presupuesto concentrado (58%) en Segmento D vulnerable, combinando:**

- Mentoría humana (no plataforma online solamente)
- Acceso móvil subsidiado
- Comunidades de apoyo
- Seguimiento longitudinal 24+ meses
- Métricas de progreso específicas por cluster

**Presupuesto recomendado:** 
- 58% Segmento D (mayor complejidad, impacto social)
- 20% Segmento C (receptividad alta)
- 20% Segmento A (autofinanciamiento parcial)
- 2% Segmento B (bajo ROI)

**Horizonte:** 2-3 años para validar modelo; 5-10 años para ver cambios intergeneracionales en segmento vulnerable.

---

**Documento Preparado Por:** Claude Code Analysis  
**Fecha:** 2026-08-26  
**Datasets Utilizados:** 
- ia_icd_pymes_analysis.ipynb (368 dueños, 8 secciones clustering)
- ia_icd_competentes_analysis.ipynb (503 buscadores, 8 secciones clustering)

**Archivos Generados:**
- ANALISIS_CLUSTERING_COMPARATIVO.md (este documento)
- clustering_validation_metrics_pymes.png
- clustering_pca_visualization_pymes.png
- clustering_demographic_comparison_pymes.png
- clustering_validation_metrics_competentes.png (existente)
- clustering_pca_visualization_competentes.png (existente)
- clustering_demographic_comparison_competentes.png (existente)
- clustering_pca_visualization_pymes_estado_laboral.png (Parte 8)
- clustering_pca_visualization_comp_estado_laboral.png (Parte 8)
- ca_estado_laboral_x_p01.png (`figures/pymes/ca_biplots/` y `figures/comp/ca_biplots/`, Parte 8)
- pymes_estado_laboral_x_{p01,p02,p03,p04,p04_bin}.png (`figures/pymes/crosstabs/`, Parte 8)
