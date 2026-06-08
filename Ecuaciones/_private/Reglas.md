---
title: Reglas de redacción — Ecuaciones
draft: true
---

# Reglas de redacción — Ecuaciones Diferenciales, Integrales y Difero-integrales

> Especialización de las reglas canónicas de la vault para el curso de **Ecuaciones**.
> **Modelo de estilo:** *Apuntes de Ecuaciones Diferenciales* de **Mariano Echeverría**
> (`apuntesma1005.pdf`) — explica todo, resuelve ejemplos de principio a fin, interpreta
> geométricamente. La parte integral/difero-integral sigue **Krasnov, Kiseliov, Makarenko**,
> *Ecuaciones Integrales* (Mir). Sirve de verificación de estilo antes de redactar y de fuente
> única para la **notación**.

---

## Rol y filosofía

Notas de **referencia para relectura frecuente**, no textbook ni explicación pedagógica lineal:
rigurosas, modulares, densas pero navegables, autocontenidas en su núcleo, expansibles por wikilinks.

Del modelo (Echeverría) tomamos su **vocación explicativa**: cada método se introduce con un
**ejemplo resuelto paso a paso** y, cuando aplica, con su **interpretación geométrica/cualitativa**
(campo de direcciones, curvas integrales, retrato de fase). Pero el orden es por **valor de
relectura**: *lo que se consulta cien veces va antes que lo que se lee una vez*. Patrón (igual que
en Tensorial/Control): `[!definicion]` operativa arriba → **`## Ejemplo` resuelto temprano** →
teoría y demostraciones en medio → contexto/limitaciones/`## Resumen` al final.
Prohibido `Introducción`, `Objetivos`, `Panorama`.

---

## YAML obligatorio

```yaml
---
title: <nombre legible>            # puede diferir del nombre de archivo
tags:
  - ecuaciones
  - teoria
  - <familia>                      # edo, edp, ecuaciones-integrales, difero-integrales
  - <tema-de-capitulo>            # separables, lineales, sistemas, series, laplace, fourier,
                                  # calor, onda, volterra, fredholm, ...
  - <subtema>                     # factor-integrante, wronskiano, resonancia, frobenius,
                                  # convolucion, nucleo-degenerado, funcion-green, ...
draft: false
aliases:
  - <sinónimo en español>
  - <nombre en inglés>            # Separable equations, Laplace transform, Integral equation, ...
---
```

- Siempre `ecuaciones` + `teoria` + al menos una `<familia>` y un `<tema-de-capitulo>`.
- Los `index.md` añaden el tag `index`.
- Nombres de archivo/carpeta **sin acentos ni signos**, estilo Título (`Variables Separables.md`,
  `Funcion de Green/`), coincidiendo EXACTAMENTE con lo que se wikilinkeará.

---

## Título principal

Un **solo `#`** por nota: `# <Concepto> $<notación si aplica>$`. Ejemplos:
`# Variables Separables $\frac{dy}{dx}=\frac{f(x)}{g(y)}$`, `# Transformada de Laplace $\mathcal{L}\{f\}$`,
`# Ecuación Integral de Fredholm de Segunda Especie`. Secciones internas con `##`, separadas por `---`.

---

## Notación del curso — usar SIEMPRE esta

> Mezcla la del modelo (Echeverría) para lo diferencial y la de Krasnov para lo integral.

**Ecuaciones diferenciales ordinarias (EDO)**

| Símbolo | Significado |
|:---|:---|
| $y=y(x)$, $y'=\dfrac{dy}{dx}$, $y''$, $y^{(n)}$ | variable dependiente y sus derivadas (notación de Leibniz/prima) |
| $\dot{x}=\dfrac{dx}{dt}$ | notación punto de Newton, cuando la variable independiente es el **tiempo** |
| orden / grado | orden = derivada más alta; grado = potencia de esa derivada |
| PVI | **problema de valor inicial**: la EDO + condiciones $y(x_0)=y_0,\dots$ |
| solución general / particular | familia con constantes $c_i$ / una elegida por las condiciones |
| $L[y]$ | operador diferencial lineal; $L[y]=a_n y^{(n)}+\dots+a_0 y$ |
| $W(y_1,\dots,y_n)$ | wronskiano; $W\neq0$ ⟺ soluciones linealmente independientes |
| $y_h$, $y_p$ | solución homogénea (complementaria) y particular; $y=y_h+y_p$ |

**Transformada de Laplace y Fourier**

| Símbolo | Significado |
|:---|:---|
| $\mathcal{L}\{f(t)\}=F(s)=\displaystyle\int_0^\infty e^{-st}f(t)\,dt$ | transformada de Laplace |
| $\mathcal{L}^{-1}\{F(s)\}=f(t)$ | transformada inversa (fracciones parciales) |
| $(f*g)(t)=\displaystyle\int_0^t f(\tau)g(t-\tau)\,d\tau$ | convolución; $\mathcal{L}\{f*g\}=F\,G$ |
| $\delta(t)$, $u(t)$ | delta de Dirac y escalón de Heaviside (funciones generalizadas) |
| $a_n,\,b_n$ | coeficientes de Fourier; $f(x)=\tfrac{a_0}{2}+\sum (a_n\cos\frac{n\pi x}{L}+b_n\operatorname{sen}\frac{n\pi x}{L})$ |

**Ecuaciones en derivadas parciales (EDP)**

| Símbolo | Significado |
|:---|:---|
| $u=u(x,t)$ | función incógnita; $u_t=\partial u/\partial t$, $u_{xx}=\partial^2u/\partial x^2$ |
| $u=X(x)\,T(t)$ | **separación de variables** |
| $u_t=\alpha^2 u_{xx}$ | ecuación del **calor** (difusión) |
| $u_{tt}=c^2 u_{xx}$ | ecuación de **onda** |
| $\nabla^2 u=u_{xx}+u_{yy}=0$ | ecuación de **Laplace** (estado estacionario) |
| Dirichlet / Neumann | condiciones de frontera: valor de $u$ fijo / valor de la derivada $\partial u/\partial n$ fijo |

**Ecuaciones integrales y difero-integrales (Krasnov)**

| Símbolo | Significado |
|:---|:---|
| $\varphi(x)$ | función **incógnita** (aparece bajo la integral) |
| $K(x,t)$ | **núcleo** (kernel) de la ecuación |
| $f(x)$ | término libre (independiente); si $f\equiv0$ la ecuación es **homogénea** |
| $\lambda$ | parámetro (autovalor cuando la homogénea tiene solución no trivial) |
| Volterra | límite superior **variable**: $\varphi(x)=f(x)+\lambda\displaystyle\int_0^x K(x,t)\varphi(t)\,dt$ |
| Fredholm | límites **fijos**: $\varphi(x)=f(x)+\lambda\displaystyle\int_a^b K(x,t)\varphi(t)\,dt$ |
| 1ª / 2ª especie | la incógnita aparece **solo** dentro de la integral / también fuera |
| $\Gamma(x,t;\lambda)$ | **resolvente** (núcleo resolvente); $\varphi=f+\lambda\int\Gamma f$ |
| $G(x,t)$ | **función de Green** del problema de frontera |
| difero-integral | mezcla derivadas e integrales de la incógnita: $\varphi'(x)=f(x)+\int K(x,t)\varphi(t)\,dt$ |

**Convenciones tipográficas**

- El modelo (Echeverría) escribe el seno como $\sin$ y coseno $\cos$ estándar; en las series de
  Fourier se admite $\operatorname{sen}$ por costumbre — **ser consistente dentro de cada nota**.
- Constantes de integración: $c$, $c_1$, $c_2,\dots$; autovalores $\lambda$, $\lambda_n$.
- Marcar el **resultado final** de un método con un `[!solucion]` o caja resumen, como en el libro.

---

## Anatomía de una nota hoja (sustantiva)

De arriba abajo, con `---` entre bloques mayores:

1. `> [!definicion]` — **primera línea** tras el título; la ecuación tipo / método clave en 2-5 líneas.
2. `> [!info]` — ubicación en el curso + wikilink a notas hermanas y al capítulo del libro.
3. `## Ejemplo` — `> [!ejemplo]` con un **problema concreto resuelto paso a paso** (estilo Echeverría:
   se plantea, se integra, se verifica). Es lo más consultado: va temprano. Figuras embebidas aquí.
4. `## En qué consiste` / método — `[!teoria]`, `[!algoritmo]` con los pasos del método, y
   `[!teorema]`+`[!demostracion]` estructurada en **Paso 1 / Paso 2 / …** cuando haya deducción.
5. Casos, variantes, comparativas: tablas con `[!info]`, `[!proposicion]`, `[!corolario]`.
6. `## Limitaciones` — `> [!warning]` (cuándo falla el método, condiciones de validez).
7. `## Resumen` — **tabla** `[!resumen]` de aspectos clave + `[!corolario]` de cierre, y un
   `[!referencia]` que delega a notas vecinas con wikilinks.

No todas las notas usan todas las secciones; las de método pesan más en ejemplo y algoritmo, las
teóricas en demostración.

## Anatomía de un `index.md`

1. `[!definicion]` marco del capítulo/sección.
2. `[!info]` por cada subnota, delegando con `[[Hija]]` o `[[Sub/index]]`.
3. `## Ejemplo` comparativo o motivador (si aplica).
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
`[!remark]`/`[!tip]`→`[!info]` o `[!regla]`, `[!summary]`→`[!resumen]`, `[!theorem]`→`[!teorema]`.
Por defecto los callouts van **sin título**; un título corto solo si desambigua de verdad.

---

## Wikilinks y delegación

- Formato `[[archivo | Texto]]`; enlace desnudo `[[Variables Separables]]` válido cuando el nombre
  ya es el texto.
- Cada nota **delega** lo que no le toca: un método de EDO lineal de 2º orden no re-deriva el
  wronskiano, lo enlaza. No duplicar contenido.
- Las notas de Laplace, Fourier y función de Green son **transversales**: las usan EDO, EDP e
  integrales; enlazarlas desde las tres partes.

---

## Tablas y matemáticas

- **Escapar `|` dentro de `$...$` en celdas de tabla**: usar `\|` (un `|` crudo rompe la tabla en
  Obsidian). Ej.: norma $\|f\|$, valor absoluto $\left|\,y\,\right|$ → `\left\|\,y\,\right\|`.
- Ecuaciones desplazadas con `$$...$$`; numerar solo si se referencian.
- Preferir `\dfrac` en displays y `\tfrac` en línea/tablas.

---

## Figuras

- Convención de la vault: SVG en `Ecuaciones/_media/img_gen/`, código fuente en `_media/code_gen/`.
- Dos estilos (skill `graficar-figuras`): **gráficas** matplotlib paleta *Ocean Forest* (campos de
  direcciones, curvas integrales, resonancia, retratos de fase, evolución del calor, modos de onda)
  y **diagramas** TikZ B/N (esquemas, dominios, condiciones de frontera).
- Embeber con `![[nombre.svg|ancho]]` dentro del `[!ejemplo]` o sección pertinente.
- Regla de oro: renderizar SVG→PNG y **verla** antes de dar por buena una figura.
