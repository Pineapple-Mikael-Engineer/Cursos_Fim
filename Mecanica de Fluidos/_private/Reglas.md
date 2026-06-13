---
title: Reglas
tags:
  - fluidos
  - meta
  - escritura
  - convenciones
draft: true
aliases:
  - Guía de redacción
  - Convenciones del curso Mecánica de Fluidos
  - Reglas de notas
---

# Reglas — Curso Mecánica de Fluidos

## Filosofía

Notas técnicas de **referencia para relectura**, no textbook ni explicación pedagógica de IA.
Rigurosas, modulares, densas pero navegables, autocontenidas en su núcleo y expansibles por wikilinks.
Curso de **enfoque vectorial → tensorial**: se empieza con la cinemática y el campo de velocidades y se
culmina en la formulación covariante (tensor energía-momento del fluido). Lo más consultado va arriba.

> Lo que se consulta cien veces va antes que lo que se lee una sola vez.

## Regla rectora: DEMOSTRAR TODO

Toda fórmula no trivial se **deduce, no se postula**. Cada resultado central lleva su
`> [!demostracion]` con los pasos (**Paso 1 —…**, identidades vectoriales/indiciales explícitas,
teoremas de Gauss/Stokes y el de transporte de Reynolds aplicados a la vista) y cierre `$\blacksquare$`.
En la parte tensorial, mostrar las **contracciones de índices completas** (no condensar: el tensor de
rapidez de deformación $e_{ij}$, el de esfuerzos $\sigma_{ij}$ y el energía-momento $T^{\mu\nu}$ se
desarrollan componente a componente cuando hace falta). Una nota que solo enuncia fórmulas sin
derivarlas está incompleta.

---

## YAML obligatorio

```yaml
---
title: <nombre legible>
tags:
  - fluidos
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

1. `# Título $notación$` (p. ej. `# Ecuaciones de Navier-Stokes $\rho\,\frac{D\vec v}{Dt}=-\nabla p+\mu\nabla^2\vec v+\rho\vec g$`)
2. `> [!definicion]` — primera línea, con la ecuación central.
3. `> [!info]` — ubicación (sección, wikilinks), referencia al libro.
4. `## Ejemplo` — `> [!ejemplo]` con un cálculo **resuelto** (geometría, números, régimen) y `> [!solucion]`
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

**Unidades: SI.** Vectores con flecha; convenio de suma de Einstein para índices repetidos.

| Concepto | Notación |
|:---|:---|
| Velocidad y posición | $\vec v$ (campo de velocidades), $\vec x$, tiempo $t$ |
| Derivada material | $\dfrac{D}{Dt}=\partial_t+(\vec v\cdot\nabla)$ |
| Propiedades | densidad $\rho$, presión $p$, temperatura $T$ |
| Viscosidad | dinámica $\mu$, cinemática $\nu=\mu/\rho$; segundo coef. $\lambda$ |
| Fuerzas | gravedad $\vec g$; fuerza másica $\vec f$ |
| Tensor de esfuerzos | $\sigma_{ij}=-p\,\delta_{ij}+\tau_{ij}$; tracción $t_i=\sigma_{ij}n_j$ |
| Rapidez de deformación | $e_{ij}=\tfrac12(\partial_i v_j+\partial_j v_i)$ (simétrico) |
| Vorticidad | $\vec\omega=\nabla\times\vec v$; $\omega_{ij}=\tfrac12(\partial_i v_j-\partial_j v_i)$ (antisimétrico) |
| Indicial | $\delta_{ij}$, $\epsilon_{ijk}$, convenio de suma |
| Adimensionales | Reynolds $\mathrm{Re}=\rho U L/\mu$, Mach $\mathrm{Ma}=U/c_s$, Froude, Euler |

**Parte covariante (tensorial):** métrica de Minkowski $\eta_{\mu\nu}=\mathrm{diag}(+1,-1,-1,-1)$;
cuadrivelocidad $u^\mu=\gamma(c,\vec v)$ con $u_\mu u^\mu=c^2$; densidad de energía propia $\varepsilon$,
presión $p$; **tensor energía-momento del fluido perfecto**
$T^{\mu\nu}=(\varepsilon+p)\,\dfrac{u^\mu u^\nu}{c^2}-p\,\eta^{\mu\nu}$. Índices griegos $0\!-\!3$,
latinos $1\!-\!3$. Conservación: $\partial_\mu T^{\mu\nu}=0$.

Decimales con coma; unidades SI con espacio fino (`5\ \text{m/s}`).

---

## Convención de signos y operadores

- **Derivada material** siempre $\dfrac{D}{Dt}=\partial_t+(\vec v\cdot\nabla)$ (aceleración de una
  partícula fluida).
- **Tensor de esfuerzos**: tracción $t_i=\sigma_{ij}n_j$ con $\hat n$ normal exterior; $\sigma_{ij}$
  **simétrico** (sin pares de cuerpo). Presión termodinámica $p=-\tfrac13\sigma_{kk}$.
- **Descomposición del gradiente de velocidad**: $\partial_j v_i=e_{ij}+\omega_{ij}$ (simétrico +
  antisimétrico). $\nabla\cdot\vec v=e_{kk}$ (dilatación); incompresible $\Leftrightarrow e_{kk}=0$.

---

## Figuras

Generadas en `Mecanica de Fluidos/_media/code_gen/` → `img_gen/*.svg`, embebidas con `![[fig.svg|ancho]]`:
- **Diagramas** (líneas de corriente, volúmenes de control, elemento fluido deformándose, perfiles de
  velocidad, capa límite, ondas de choque, geometrías): **TikZ** en blanco y negro (con `tikz` y
  `pgfplots` cuando convenga).
- **Gráficas** (perfiles Couette/Poiseuille, $\delta(x)$, curvas de arrastre, diagramas $p$–$v$):
  **matplotlib** con la paleta **Ocean Forest** (`ocean_forest.py`).

Regla de oro: renderizar SVG→PNG y **revisar** la figura antes de darla por buena. Embeds de figura
dentro de un callout `[!ejemplo]` requieren `>` también en las líneas en blanco (si no, rompen el
callout).

---

## Wikilinks

`[[Archivo | texto]]`; índices `[[N Carpeta/index | texto]]` (con el número). Basename exacto del
árbol. Nunca `[[index]]` solo, ni `../`, ni saltos de línea dentro de `[[ ]]`. En tablas, escapar
`|`→`\|` dentro de `$...$`. **No duplicar**: delegar por wikilink. Si un basename se repite entre
secciones, **cualificar la ruta** en el enlace.

---

## Estilo y referencias

Deductivo y económico. Declarar siempre: las **hipótesis** del modelo (incompresible / compresible,
newtoniano, ideal / viscoso, estacionario, irrotacional), las **condiciones de frontera** (no
deslizamiento, superficie libre), el **régimen** ($\mathrm{Re}$, $\mathrm{Ma}$). No fórmulas sin
hipótesis. Imitar: **Landau-Lifshitz, Vol. 6** (*Mecánica de Fluidos*) como libro **rector** (su ídolo
es Landau); **Batchelor** (*An Introduction to Fluid Dynamics*) y **Kundu & Cohen** para profundidad;
**Aris** (*Vectors, Tensors and the Basic Equations of Fluid Mechanics*) para el aparato tensorial;
**Acheson** para intuición. Buscar economía, precisión y la deducción que hace **emerger** la
estructura (Navier–Stokes desde el balance de momento; las ondas y el sonido desde la compresibilidad;
$T^{\mu\nu}$ desde la conservación).
