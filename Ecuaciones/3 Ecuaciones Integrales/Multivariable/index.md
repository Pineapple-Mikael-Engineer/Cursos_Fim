---
title: Ecuaciones Integrales Multivariable y Física
order: 8
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - multivariable
  - index
draft: false
aliases:
  - ecuaciones integrales multivariable
  - teoría de potencial
  - dispersión
  - multidimensional integral equations
---

# Ecuaciones Integrales Multivariable y Física

> [!definicion]
> Una **ecuación integral multidimensional** tiene la incógnita $\varphi(\mathbf{x})$ definida sobre un dominio $\Omega\subset\mathbb{R}^n$ (o su frontera $\partial\Omega$), con un núcleo $K(\mathbf{x}, \mathbf{y})$ que integra sobre ese dominio:
> $$\varphi(\mathbf{x})=f(\mathbf{x})+\lambda\int_{\Omega}K(\mathbf{x},\mathbf{y})\,\varphi(\mathbf{y})\,d\mathbf{y}.$$
> Es el lenguaje natural de la **física**: el potencial de una distribución de carga, la onda dispersada por un obstáculo, la radiación en un medio. La teoría de [[Fredholm/index| Fredholm]] se extiende casi sin cambios; la novedad está en los **núcleos singulares geométricos** y las **aplicaciones**.

> [!info]
> Sección que lleva las ecuaciones integrales a $\mathbb{R}^n$ y a la física. Reúne tres hilos: reescribir EDPs ([[Ecuacion de Laplace y Poisson/index| Laplace]], Helmholtz) como ecuaciones integrales sobre la **frontera** ([[Teoria de Potencial| teoría de potencial]]), la **dispersión** de ondas ([[Ecuacion de Lippmann-Schwinger| Lippmann-Schwinger]]) y el **transporte** de radiación ([[Transferencia Radiativa| transferencia radiativa]]).

---

## Por qué la física habla en ecuaciones integrales

> [!teoria]
> La [[Solucion Fundamental| solución fundamental]] de un operador (el potencial de Coulomb $\tfrac{1}{4\pi r}$, el núcleo de Helmholtz $\tfrac{e^{ikr}}{4\pi r}$) **es** un núcleo integral. Convolucionar una fuente con ella da el campo: $u=\Phi*\rho$. Esto convierte una **EDP en un dominio** en una **ecuación integral**, con dos ventajas enormes:
> 1. **Reducción de dimensión.** Una EDP en el volumen $\Omega\subset\mathbb{R}^3$ se reescribe como una ecuación integral sobre la **superficie** $\partial\Omega$ (2D): menos incógnitas, y la condición en el infinito se cumple automáticamente. Es la base del **método de elementos de frontera (BEM)**.
> 2. **Problemas inversos y dispersión.** Medir el campo lejano y reconstruir la fuente o el obstáculo es resolver una ecuación integral (a menudo de primera especie, mal planteada).
>
> El precio: los núcleos heredan la **singularidad** de la solución fundamental ($1/r$, $\ln r$), así que aparecen integrales singulares como las de la sección [[Singulares/index| Singulares]].

> [!info] Recorrido de la sección
> | Nota | Aporte |
> |---|---|
> | [[Fredholm Multidimensional\|Fredholm Multidimensional]] | la teoría de Fredholm en $\Omega\subset\mathbb{R}^n$ |
> | [[Teoria de Potencial\|Teoría de Potencial]] | capas simple y doble; EDP → ecuación de frontera (BEM) |
> | [[Ecuacion de Lippmann-Schwinger\|Lippmann-Schwinger]] | dispersión de ondas; campo incidente + dispersado |
> | [[Transferencia Radiativa\|Transferencia Radiativa]] | transporte de radiación; ecuación íntegro-diferencial |

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Forma | $\varphi(\mathbf{x})=f+\lambda\int_\Omega K(\mathbf{x},\mathbf{y})\varphi\,d\mathbf{y}$ |
> | Núcleo físico | solución fundamental ($1/r$, $e^{ikr}/r$, $\ln r$) |
> | Ventaja | EDP de volumen → ecuación de **frontera** (BEM) |
> | Aplicaciones | potencial, dispersión, transporte radiativo |

> [!corolario]
> En varias dimensiones, las ecuaciones integrales son el **idioma de los campos**: encapsulan el operador, el dominio y las condiciones en un núcleo (la solución fundamental). Por eso una EDP sobre un volumen se vuelve una ecuación sobre su frontera —el truco que hace prácticos los problemas de potencial y dispersión en ingeniería y física—.

> [!referencia]
> - El puente EDP↔integral: [[Teoria de Potencial]].
> - La física de ondas: [[Ecuacion de Lippmann-Schwinger]].
> - La solución fundamental como núcleo: [[Solucion Fundamental]].
