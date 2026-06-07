---
title: Reglas de redacción — Análisis Tensorial
draft: true
---

# Reglas de redacción — Análisis Tensorial

> Especialización de las reglas canónicas de la vault para el curso de **Análisis Tensorial**,
> siguiendo la Parte I (cap. 1-7) del libro *Física Matemática* de **J. Rogan y V. Muñoz**.
> Sirve de verificación de estilo antes de redactar y de fuente única para la **notación**.

---

## Rol y filosofía

Notas de **referencia para relectura frecuente**, no textbook ni explicación pedagógica lineal:
rigurosas, modulares, densas pero navegables, autocontenidas en su núcleo, expansibles por wikilinks.

Orden por **valor de relectura**: *lo que se consulta cien veces va antes que lo que se lee una vez*.
Patrón (igual que en Control/Métodos Numéricos): `[!definicion]` operativa arriba → **`## Ejemplo`
resuelto temprano** → teoría y demostraciones en medio → contexto/limitaciones/`## Resumen` al final.
Prohibido `Introducción`, `Objetivos`, `Panorama`.

---

## YAML obligatorio

```yaml
---
title: <nombre legible>            # puede diferir del nombre de archivo
tags:
  - analisis-tensorial
  - teoria
  - <tema-de-capitulo>            # notacion-indices, calculo-vectorial, coordenadas-curvilineas,
                                  # tensores, coordenadas-no-ortogonales, matrices, teoria-grupos
  - <subtema>                     # einstein, levi-civita, divergencia, covarianza, lorentz, ...
draft: false
aliases:
  - <sinónimo en español>
  - <nombre en inglés>            # Levi-Civita symbol, Covariant derivative, ...
---
```

- Siempre `analisis-tensorial` + `teoria` + al menos un tema de capítulo.
- Los `index.md` añaden el tag `index`.
- Nombres de archivo/carpeta **sin acentos ni signos**, estilo Título (`Simbolo Levi-Civita.md`),
  coincidiendo EXACTAMENTE con lo que se wikilinkeará. (Las notas heredadas con acentos se
  renombran al integrarlas.)

---

## Título principal

Un **solo `#`** por nota: `# <Concepto> $<notación si aplica>$`. Ejemplos:
`# Símbolo de Levi-Civita $\varepsilon_{ijk}$`, `# Tensor de Conductividad y Ley de Ohm`,
`# Covarianza y Contravarianza`. Secciones internas con `##`, separadas por `---`.

---

## Notación del libro (Rogan & Muñoz) — usar SIEMPRE esta

> Esta es la convención del texto. Mantenerla idéntica para que las notas y el libro se lean en paralelo.

**Índices y convenio de Einstein**

| Símbolo | Significado |
|:---|:---|
| `i, j, k, …` | índices que recorren $1\dots n$ (en 3D, $1,2,3$) |
| índice **repetido** en un término | se **suma** sobre él (convenio de Einstein); es *mudo* |
| índice que aparece **una vez** | *libre*; mismo valor en todos los términos de la ecuación |
| Regla de oro | un índice **no** aparece más de **dos** veces en un término |

**Vectores y operadores vectoriales**

| Símbolo | Significado |
|:---|:---|
| $\vec{A}$, $\vec{E}$ | vector (flecha encima); componentes $A_i$, $E_i$ |
| $\hat{e}_i$ | vectores base unitarios cartesianos ($\hat{e}_1,\hat{e}_2,\hat{e}_3$) |
| $\hat{q}_i$ | vectores base unitarios en **curvilíneas** ($\hat{q}_\rho,\hat{q}_\phi,\hat{q}_z$, etc.) |
| $\vec{A}\cdot\vec{B}=A_iB_i$ | producto punto |
| $(\vec{A}\times\vec{B})_i=\varepsilon_{ijk}A_jB_k$ | producto cruz |
| $\vec{\nabla}$ | operador nabla; $\vec{\nabla}\Phi$ gradiente, $\vec{\nabla}\cdot\vec{A}$ divergencia, $\vec{\nabla}\times\vec{A}$ rotor |

**Símbolos especiales**

| Símbolo | Significado |
|:---|:---|
| $\delta_{ij}$ | delta de Kronecker; $\delta_{ii}=n$, $\delta_{ij}A_j=A_i$ |
| $\varepsilon_{ijk}$ | símbolo de Levi-Civita (permutaciones); $\varepsilon_{123}=+1$ |
| identidad $\varepsilon$-$\delta$ | $\varepsilon_{ijk}\varepsilon_{ilm}=\delta_{jl}\delta_{km}-\delta_{jm}\delta_{kl}$ |

**Tensores (notación diádica del libro)**

| Símbolo | Significado |
|:---|:---|
| $\overleftrightarrow{\sigma}=\sigma_{ij}\hat{e}_i\hat{e}_j$ | tensor (doble flecha); las bases son "cajones", hay doble suma |
| $\sigma_{ij}$ | componentes del tensor; $[\sigma]$ es su **matriz** (sin info de la base) |
| $J_i=\sigma_{ij}E_j$ | ejemplo guía: ley de Ohm anisótropa ($\vec{J}=\overleftrightarrow{\sigma}\cdot\vec{E}$) |
| orden/rango | nº de índices = nº de vectores base |

**Coordenadas curvilíneas (¡ojo a las letras del libro!)**

| Sistema    | Coordenadas       | Factores de escala                                      |
| :--------- | :---------------- | :------------------------------------------------------ | 
| Cilíndrico | $(\rho,\phi,z)$   | $h_\rho=1,\ h_\phi=\rho,\ h_z=1$                        |
| Esférico   | $(r,\theta,\phi)$ | $h_r=1,\ h_\theta=r,\ h_\phi=r\operatorname{sen}\theta$ |
| General    | $(q_1,q_2,q_3)$   | $h_i=\left \| \partial\vec{r}/\partial q_i\right \|$ 

**Covariante / contravariante (cap. 5)**

| Símbolo | Significado |
|:---|:---|
| $A^i$ | componente **contravariante** (superíndice) |
| $A_i$ | componente **covariante** (subíndice) |
| $g_{ij}$, $g^{ij}$ | tensor métrico y su inverso; $g^{ik}g_{kj}=\delta^i_j$ |
| subir/bajar | $A_i=g_{ij}A^j$, $A^i=g^{ij}A_j$ |

**Convenciones tipográficas del texto**

- El libro escribe el seno como $\operatorname{sen}\theta$ (no $\sin$). Mantenerlo: `\operatorname{sen}`.
- Pseudo-objetos: $\overleftrightarrow{T}$, pseudo-vector, pseudo-escalar (mano derecha vs izquierda).
- Unidades MKS en los ejemplos físicos.

---

## Anatomía de una nota hoja (sustantiva)

De arriba abajo, con `---` entre bloques mayores:

1. `> [!definicion]` — **primera línea** tras el título; el objeto/fórmula clave en 2-5 líneas.
2. `> [!info]` — ubicación en el curso + wikilink a notas hermanas y al `# cap N.M` del libro.
3. `## Ejemplo` — `> [!ejemplo]` con un **problema concreto resuelto paso a paso** (con números o
   manipulación explícita de índices). Es lo más consultado: va temprano. Figuras embebidas aquí.
4. `## En qué consiste` / teoría — `[!teoria]`, e `[!teorema]`+`[!demostracion]` estructurada en
   **Paso 1 / Paso 2 / …** cuando haya deducción.
5. Propiedades, casos, comparativas: tablas con `[!info]`, `[!proposicion]`, `[!corolario]`.
6. `## Limitaciones` — `> [!warning]` con lista numerada (si aplica).
7. `## Resumen` — **tabla** `[!resumen]` de aspectos clave + `[!corolario]` de cierre, y un
   `[!referencia]` que delega a notas vecinas con wikilinks.

No todas las notas usan todas las secciones; las de método pesan más en ejemplo, las teóricas en
demostración.

## Anatomía de un `index.md`

1. `[!definicion]` marco del capítulo/sección.
2. `[!info]` por cada subnota, delegando con `[[Hija]]` o `[[Sub/index]]`.
3. `## Ejemplo` comparativo (si aplica).
4. Teoría/motivación al final.
5. `## Resumen` (tabla + `[!corolario]`).

---

## Callouts permitidos

Usar **solo** estos (en español, en minúscula). Regla: si quitar el callout no cambia nada, estaba
mal puesto.

**Núcleo:** `definicion`, `teorema`, `demostracion`, `lema`, `proposicion`, `corolario`, `axioma`,
`ejemplo`, `teoria`, `info`, `warning`, `algoritmo`.
**Extensiones con mesura:** `regla`, `solucion`, `referencia`, `resumen`.

**Prohibidos** (y sus reemplazos): `nota`/`observacion`/`conclusion` → integrar al texto o usar
`info`. **No usar los callouts en inglés** del material heredado: `[!example]`→`[!ejemplo]`,
`[!remark]`/`[!tip]`→`[!info]` o `[!regla]`, `[!summary]`→`[!resumen]`, `[!teoria]` se mantiene.
Por defecto los callouts van **sin título**; un título corto solo si desambigua de verdad.

---

## Wikilinks y delegación

- Formato `[[archivo | Texto]]`; enlace desnudo `[[Delta Kronecker]]` válido cuando el nombre ya
  es el texto.
- Carpetas **siempre** con `/index`: `[[Operadores Diferenciales/index | operadores]]`.
- Nombres coinciden EXACTAMENTE con el árbol (`_private/Tree Tensorial.md`). Se enlaza aunque la
  nota no exista todavía (promesa de expansión).
- **No duplicar**: cada concepto vive en una sola hoja; las demás lo referencian por wikilink.

---

## Código (opcional)

No es central en este curso. Cuando un ejemplo gane con cómputo simbólico/numérico (verificar una
identidad de índices, diagonalizar un tensor, evaluar factores de escala), usar **Python** con
`numpy`/`sympy` en bloque ```python. Mantenerlo breve y subordinado al desarrollo a mano.

---

## Referencia

- *Física Matemática*, **J. Rogan C. y V. Muñoz G.**, U. de Chile, 3ª ed. — Parte I, cap. 1-7.
- Cap. 4 (tensores) basado en *Mathematical Physics*, Kusse & Westwig (Wiley).
- PDF: `Tensorial/_private/Rogan y Muñoz.pdf`. Árbol: `Tensorial/_private/Tree Tensorial.md`.
