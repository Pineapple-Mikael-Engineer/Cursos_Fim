---
title: Métodos Compuestos
tags:
  - metodos-numericos
  - teoria
  - diferenciacion-integracion
  - integracion-numerica
  - newton-cotes
  - index
draft: false
aliases:
  - Métodos compuestos
  - Reglas compuestas
  - Composite rules
---

# Métodos Compuestos

> [!definicion]
> Un **método compuesto** subdivide $[a,b]$ en $n$ subintervalos y aplica una regla simple de [[Reglas Cerradas/index|Newton-Cotes]] (trapecio o Simpson) en cada uno, sumando las contribuciones. Mantiene el **grado bajo** y mejora la precisión reduciendo el paso $h$, no subiendo el grado.

> [!info]
> Es la forma **práctica** de la integración numérica: evita la [[Inestabilidad Pesos Negativos Grado Alto|inestabilidad de grado alto]] conservando pesos positivos, y su error se controla por $h = (b-a)/n$. El [[Trapecio Compuesto Convergencia O h2|trapecio compuesto]] da $O(h^2)$ y el [[Simpson Compuesto Convergencia O h4|Simpson compuesto]] da $O(h^4)$.

---

## Las dos reglas compuestas

> [!info]
> - **[[Trapecio Compuesto Convergencia O h2|Trapecio compuesto]]:** suma de trapecios, $O(h^2)$. Base de la extrapolación de [[Extrapolacion Richardson Aceleracion Convergencia|Romberg]].
> - **[[Simpson Compuesto Convergencia O h4|Simpson compuesto]]:** suma de parábolas, $O(h^4)$. Mejor relación precisión/costo para integrandos suaves.

---

## Ejemplo

> [!ejemplo]
> **$\int_0^1 e^x\,dx = e-1 \approx 1.718282$**, error al duplicar $n$:
>
> | $n$ | Trapecio comp. | factor | Simpson comp. | factor |
> |:---:|:---:|:---:|:---:|:---:|
> | 2 | $3.0\times10^{-2}$ | — | $1.7\times10^{-4}$ | — |
> | 4 | $7.4\times10^{-3}$ | 4.0 | $1.1\times10^{-5}$ | 16 |
> | 8 | $1.8\times10^{-3}$ | 4.0 | $6.8\times10^{-7}$ | 16 |
>
> El error del trapecio se cuartea (factor $4$, $O(h^2)$); el de Simpson se divide por $16$ (factor $16$, $O(h^4)$). La convergencia rápida de Simpson lo hace preferible.

---

## Por qué compuestas y no grado alto

> [!teoria]
> Subdividir con grado fijo:
> - **Estable:** pesos siempre positivos, $\sum|w_i| = b-a$ acotado.
> - **Convergente:** error $O(h^p) \to 0$ garantizado al refinar.
> - **Robusto:** sin oscilaciones de [[Fenomeno Runge y Nodos Chebyshev|Runge]].
>
> Es exactamente la misma filosofía que los [[Interpolacion Tramos Splines/index|splines]] frente a la interpolación de grado alto: muchos tramos de grado bajo en lugar de uno de grado alto.

---

## Resumen

| Regla | Nota |
|:---|:---|
| Trapecio compuesto $O(h^2)$ | [[Trapecio Compuesto Convergencia O h2]] |
| Simpson compuesto $O(h^4)$ | [[Simpson Compuesto Convergencia O h4]] |

> [!corolario]
> Los métodos compuestos subdividen el intervalo y aplican una regla simple de grado bajo en cada panel, sumando: el [[Trapecio Compuesto Convergencia O h2|trapecio compuesto]] converge $O(h^2)$ y el [[Simpson Compuesto Convergencia O h4|Simpson compuesto]] $O(h^4)$. Al mantener el grado bajo conservan pesos positivos y eluden la [[Inestabilidad Pesos Negativos Grado Alto|inestabilidad de grado alto]], siguiendo la misma filosofía que los [[Interpolacion Tramos Splines/index|splines]]. Son la forma estándar de integrar numéricamente, refinables por [[Extrapolacion Richardson Aceleracion Convergencia|Romberg]] y comparables con la [[Cuadratura Gaussiana/index|cuadratura gaussiana]].
