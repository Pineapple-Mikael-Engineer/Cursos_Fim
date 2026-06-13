---
title: Reglas
tags:
  - electromagnetismo
  - meta
  - escritura
  - convenciones
draft: true
aliases:
  - Guía de redacción
  - Convenciones del curso Electromagnetismo
  - Reglas de notas
---

# Reglas — Curso Electromagnetismo

## Filosofía

Notas técnicas de **referencia para relectura**, no textbook ni explicación pedagógica de IA.
Rigurosas, modulares, densas pero navegables, autocontenidas en su núcleo y expansibles por wikilinks.
Curso de **enfoque vectorial → tensorial**: se empieza con cálculo vectorial y se culmina en la
formulación covariante. Lo más consultado va arriba.

> Lo que se consulta cien veces va antes que lo que se lee una sola vez.

## Regla rectora: DEMOSTRAR TODO

Toda fórmula no trivial se **deduce, no se postula**. Cada resultado central lleva su
`> [!demostracion]` con los pasos (**Paso 1 —…**, identidades vectoriales/indiciales explícitas,
teoremas de Gauss/Stokes aplicados a la vista) y cierre `$\blacksquare$`. En la parte tensorial,
mostrar las contracciones de índices completas (no condensar). Una nota que solo enuncia fórmulas sin
derivarlas está incompleta.

---

## YAML obligatorio

```yaml
---
title: <nombre legible>
tags:
  - electromagnetismo
  - teoria
  - <tema-especifico>
draft: false
aliases:
  - <sinónimos / nombre en inglés si aplica>
---
```

---

## Anatomía de una nota sustantiva

Separar bloques con `---`. Orden típico:

1. `# Título $notación$` (p. ej. `# Ley de Gauss $\nabla\cdot\vec E=\rho/\varepsilon_0$`)
2. `> [!definicion]` — primera línea, con la ecuación central.
3. `> [!info]` — ubicación (sección, wikilinks), referencia al libro.
4. `## Ejemplo` — `> [!ejemplo]` con un cálculo **resuelto** (números, simetría usada) y `> [!solucion]`
   anidada.
5. `## En qué consiste` — `> [!teoria]`, `> [!teorema]` + `> [!demostracion]` (**Paso 1 —…**,
   `$\blacksquare$`), `> [!proposicion]`, `> [!warning]`.
6. `## Resumen` — `> [!resumen]` (tabla) + `> [!corolario]` + `> [!referencia]`.

Para `index.md`: definición marco + idea unificadora + **teoría propia** (no solo listar hijas) +
mapa de hijas + corolario. Un índice **enseña** y puede llevar figuras y ecuaciones.

---

## Callouts permitidos

```
definicion · teorema · demostracion · lema · proposicion · corolario · axioma
ejemplo · solucion · teoria · info · warning · algoritmo · regla · referencia · resumen
```

Prohibidos: `nota`, `observacion`, `conclusion`, `importante` y cualquier callout en inglés.

---

## Notación (mantener UNA convención)

**Unidades: SI** (como Griffiths). Vectores con flecha.

| Concepto | Notación |
|:---|:---|
| Campos | $\vec E$ (eléctrico), $\vec B$ (magnético), $\vec D=\varepsilon_0\vec E+\vec P$, $\vec H=\vec B/\mu_0-\vec M$ |
| Fuentes | carga $q$, densidades $\rho$, $\vec J$; corriente $I$ |
| Constantes | $\varepsilon_0$, $\mu_0$, $c=1/\sqrt{\mu_0\varepsilon_0}$ |
| Potenciales | escalar $V$, vector $\vec A$; $\vec E=-\nabla V-\partial_t\vec A$, $\vec B=\nabla\times\vec A$ |
| Operadores | $\nabla\cdot$ (div), $\nabla\times$ (rot), $\nabla$ (grad), $\nabla^2$ (laplaciano), $\Box=\nabla^2-\tfrac1{c^2}\partial_t^2$ |
| Polarización/Mag. | $\vec P$, $\vec M$; cargas/corrientes ligadas $\rho_b=-\nabla\cdot\vec P$, $\vec J_b=\nabla\times\vec M$ |
| Indicial | $\delta_{ij}$, $\epsilon_{ijk}$, convenio de suma |

**Parte covariante (tensorial):** métrica de Minkowski $\eta_{\mu\nu}=\mathrm{diag}(+1,-1,-1,-1)$;
cuadrivectores $x^\mu=(ct,\vec x)$, $J^\mu=(c\rho,\vec J)$, $A^\mu=(V/c,\vec A)$; tensor de campo
$F^{\mu\nu}=\partial^\mu A^\nu-\partial^\nu A^\mu$; Levi-Civita $\epsilon^{\mu\nu\rho\sigma}$. Índices
griegos $0\!-\!3$, latinos $1\!-\!3$. Maxwell: $\partial_\mu F^{\mu\nu}=\mu_0 J^\nu$.

Unidades SI con espacio fino (`5\ \text{V/m}`); decimales con coma.

---

## Figuras

Generadas en `Electromagnetismo/_media/code_gen/` → `img_gen/*.svg`, embebidas con `![[fig.svg|ancho]]`:
- **Diagramas** (líneas de campo, superficies de Gauss, lazos de Ampère, geometrías, ondas): **TikZ**
  en blanco y negro (con `tikz`/`circuitikz` y `pgfplots` cuando convenga).
- **Gráficas** (campos, ondas, coeficientes de Fresnel, espectros): **matplotlib** con la paleta
  **Ocean Forest** (`ocean_forest.py`).

Regla de oro: renderizar SVG→PNG y **revisar** la figura antes de darla por buena. Embeds de figura
dentro de un callout `[!ejemplo]` requieren `>` también en las líneas en blanco (si no, rompen el
callout).

---

## Wikilinks

`[[Archivo | texto]]`; índices `[[N Carpeta/index | texto]]` (con el número). Basename exacto del
árbol. Nunca `[[index]]` solo, ni `../`, ni saltos de línea dentro de `[[ ]]`. En tablas, escapar
`|`→`\|` dentro de `$...$`. **No duplicar**: delegar por wikilink.

---

## Estilo y referencias

Deductivo y económico. Declarar siempre: la **simetría** usada (para Gauss/Ampère), las **condiciones
de frontera**, el **gauge** elegido, el **medio** (vacío / dieléctrico / conductor). No fórmulas sin
hipótesis. Imitar: **Griffiths** (*Introduction to Electrodynamics*) para lo vectorial; **Jackson**
(*Classical Electrodynamics*) para profundidad; **Landau-Lifshitz Vol. 2** (*Teoría Clásica de
Campos*) para la formulación covariante. Buscar economía, precisión y la deducción que hace **emerger**
la estructura (las ondas desde Maxwell; $F^{\mu\nu}$ desde $A^\mu$).
