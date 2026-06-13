---
title: Reglas de redacción — Circuitos Eléctricos
draft: true
---

# Reglas de redacción — Circuitos Eléctricos (ML 140)

> Especialización de las reglas canónicas de la vault para **Circuitos Eléctricos**.
> **Modelo de estilo:** *Circuitos Eléctricos* de **Jesús Fraile Mora** (Pearson, 2012) — muchos
> **ejemplos resueltos completos**, figuras claras, normas **CENELEC/IEC**. Orden y alcance: **sílabo
> ML 140**. Sirve de verificación de estilo antes de redactar y de fuente única para la **notación**.

---

## Rol y filosofía

Notas de **referencia para relectura frecuente**, no textbook lineal: rigurosas, modulares, densas
pero navegables, autocontenidas en su núcleo, expansibles por wikilinks.

Este es un curso **aplicado de ingeniería**: el corazón de cada nota es el **circuito resuelto paso a
paso** (estilo Fraile Mora). Orden por **valor de relectura**: `[!definicion]`/ley operativa arriba →
**`## Ejemplo` con un circuito resuelto temprano** → teoría/deducción en medio → casos/limitaciones/
`## Resumen` al final. Prohibido `Introducción`, `Objetivos`, `Panorama`.

---

## YAML obligatorio

```yaml
---
title: <nombre legible>
tags:
  - circuitos-electricos
  - teoria
  - <tema-de-capitulo>            # resistivos, metodos-analisis, transitorios, sinusoidal,
                                  # fasores, potencia, acoplamiento-magnetico, trifasicos
  - <subtema>                     # kirchhoff, thevenin, rlc, impedancia, factor-potencia, ...
draft: false
aliases:
  - <sinónimo en español>
  - <nombre en inglés>            # mesh analysis, phasor, power factor, ...
---
```

- Siempre `circuitos-electricos` + `teoria` + al menos un `<tema-de-capitulo>`.
- Los `index.md` añaden el tag `index`.
- Nombres de archivo/carpeta **sin acentos ni signos**, estilo Título (`Teorema de Thevenin.md`),
  coincidiendo EXACTAMENTE con lo que se wikilinkeará.

---

## Título principal

Un **solo `#`** por nota: `# <Concepto> $<notación si aplica>$`. Ejemplos:
`# Teorema de Thévenin`, `# Impedancia Compleja $Z=R+jX$`, `# Circuito RC de Primer Orden`.
Secciones internas con `##`, separadas por `---`.

---

## Notación del curso — usar SIEMPRE esta

> Convención eléctrica estándar (CENELEC/IEC, como Fraile Mora). **Unidad imaginaria $j$** (NO $i$,
> reservada a la corriente).

**Variables y minúsculas/mayúsculas**

| Símbolo | Significado |
|:---|:---|
| $i(t)$, $v(t)$, $p(t)$ | corriente, tensión, potencia **instantáneas** (minúscula) |
| $I$, $V$, $P$ | valores **constantes** (CC) o **eficaces** (CA) (mayúscula) |
| $q$, $W$ | carga (C) y energía (J); $i=dq/dt$, $W=\int p\,dt$ |
| convenio pasivo | la corriente entra por el borne **+**: $p=vi>0$ ⇒ **absorbe** |

**Elementos pasivos**

| Elemento | Relación | Unidad |
|:---|:---|:---|
| Resistencia $R$ (conductancia $G=1/R$) | $v=Ri$ (ley de Ohm) | $\Omega$ (S) |
| Inductor $L$ | $v=L\,\dfrac{di}{dt}$; $W=\tfrac12 LI^2$ | H |
| Condensador $C$ | $i=C\,\dfrac{dv}{dt}$; $W=\tfrac12 CV^2$ | F |
| Inductancia mutua $M$ | $v_2=M\,\dfrac{di_1}{dt}$; $k=M/\sqrt{L_1L_2}$ | H |

**Régimen sinusoidal / fasores**

| Símbolo | Significado |
|:---|:---|
| $v(t)=V_m\operatorname{sen}(\omega t+\varphi)$ | senoide; $\omega=2\pi f$, $V_{\text{rms}}=V_m/\sqrt2$ |
| $\overline{V}=V\angle\varphi$ | **fasor** (raya encima); magnitud eficaz $V$, fase $\varphi$ |
| $Z=R+jX$ | impedancia; $X_L=\omega L$, $X_C=-1/(\omega C)$ |
| $Y=1/Z=G+jB$ | admitancia |
| $S=\overline{V}\,\overline{I}^{\,*}=P+jQ$ | potencia compleja: activa $P$ (W), reactiva $Q$ (VAr), aparente $\lvert S\rvert$ (VA) |
| $\cos\varphi$ | factor de potencia |

**Trifásicos**

| Símbolo | Significado |
|:---|:---|
| $V_F,\ I_F$ / $V_L,\ I_L$ | tensión/corriente de **fase** / de **línea** |
| estrella (Y) | $V_L=\sqrt3\,V_F$, $I_L=I_F$ |
| triángulo (Δ) | $I_L=\sqrt3\,I_F$, $V_L=V_F$ |
| $P_{3\phi}=\sqrt3\,V_LI_L\cos\varphi$ | potencia trifásica equilibrada |

**Convenciones tipográficas**

- El seno como $\operatorname{sen}$ (uso hispano de Fraile); coseno $\cos$ estándar.
- Unidad imaginaria **$j$**. Conjugado $\overline{I}^{\,*}$.
- Marca el **resultado final** de un cálculo con `[!solucion]` o caja recuadrada.

---

## Anatomía de una nota hoja (sustantiva)

De arriba abajo, con `---` entre bloques mayores:

1. `> [!definicion]` — **primera línea** tras el título; la ley/relación clave en 2-5 líneas.
2. `> [!info]` — ubicación en el curso + wikilink a notas hermanas y al capítulo del sílabo/Fraile.
3. `## Ejemplo` — `> [!ejemplo]` con un **circuito concreto resuelto paso a paso** (con números y
   unidades, estilo Fraile). Es lo más consultado: va temprano. **Figura del circuito embebida aquí.**
4. `## En qué consiste` / teoría — `[!teoria]`, `[!algoritmo]` (pasos del método) y
   `[!teorema]`+`[!demostracion]` en **Paso 1 / Paso 2 / …** cuando haya deducción (p. ej. Thévenin).
5. Propiedades, casos, comparativas: tablas con `[!info]`, `[!proposicion]`, `[!corolario]`, `[!warning]`.
6. `## Resumen` — **tabla** `[!resumen]` de fórmulas clave + `[!corolario]` de cierre, y un
   `[!referencia]` que delega a notas vecinas con wikilinks.

Las notas de método (mallas, Thévenin) pesan más en **ejemplo + algoritmo**; las conceptuales, en
definición y deducción.

## Anatomía de un `index.md`

Un index **enseña**, no solo enumera: `[!definicion]` marco del capítulo → `[!teoria]` que explica el
panorama y la idea unificadora → `[!info]` mapa que delega a las hijas con `[[Hija]]` → `## Resumen`.

---

## Callouts permitidos

Usar **solo** estos (en español, en minúscula). Regla: si quitar el callout no cambia nada, estaba
mal puesto.

**Núcleo:** `definicion`, `teorema`, `demostracion`, `lema`, `proposicion`, `corolario`, `axioma`,
`ejemplo`, `teoria`, `info`, `warning`, `algoritmo`.
**Extensiones con mesura:** `regla`, `solucion`, `referencia`, `resumen`.

**Prohibidos** (y reemplazos): `nota`/`observacion`/`conclusion` → integrar al texto o usar `info`.
**No usar callouts en inglés** (`[!example]`→`[!ejemplo]`, etc.). Por defecto sin título; un título
corto solo si desambigua.

---

## Wikilinks y delegación

- Formato `[[archivo | Texto]]`; enlace desnudo `[[Teorema de Thevenin]]` válido cuando el nombre ya
  es el texto. Usa el **basename** (único) para hojas; `[[Carpeta/index]]` para índices.
- **NUNCA** `[[index]]` solo (ambiguo) ni `[[../...]]` (Obsidian no lo resuelve). Cada `[[...]]` en
  **una sola línea**.
- Cada nota **delega**: el análisis de mallas no re-deduce Kirchhoff, lo enlaza. No duplicar.
- Transversales (Laplace, fasores, impedancia) se enlazan desde todas las partes que las usan.

---

## Tablas y matemáticas

- **Escapar `|` dentro de `$...$` en celdas de tabla** como `\|` (un `|` crudo rompe la tabla en
  Obsidian). P. ej. módulo $\lvert Z\rvert$, $\lvert S\rvert$.
- Ecuaciones desplazadas con `$$...$$`; numerar solo si se referencian.
- `\dfrac` en displays, `\tfrac` en línea/tablas; matrices con `\begin{pmatrix}` (mallas/nodos).

---

## Figuras (clave en este curso)

Dos estilos, vía skill `graficar-figuras`. Salida SVG en `Circuitos Electricos/_media/img_gen/`,
fuentes en `_media/code_gen/` (`tikz/*.tex` y `*.py`):

- **Circuitos (diagramas B/N) → circuitikz** (LaTeX): esquemas con $R$, $L$, $C$, fuentes, AO,
  transformador, conexiones Y/Δ. Símbolos `american`; bornes con `+`/`−`; nodos de bifurcación
  rellenos. Es el grueso de las figuras del curso.
- **Ondas, fasores, potencia (gráficas) → matplotlib** paleta *Ocean Forest*: senoides, respuestas
  transitorias $e^{-t/\tau}$, regímenes de amortiguamiento, **diagramas fasoriales**, **triángulo de
  potencias**, $\lvert Z\rvert(\omega)$ de resonancia, las 3 senoides trifásicas.
- Embeber con `![[nombre.svg|ancho]]` dentro del `[!ejemplo]` pertinente, con una línea descriptiva.
- Regla de oro: renderizar SVG→PNG y **verla** antes de dar por buena una figura.
