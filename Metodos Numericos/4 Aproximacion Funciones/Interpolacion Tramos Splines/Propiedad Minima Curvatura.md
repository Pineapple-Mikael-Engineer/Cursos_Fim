---
title: Propiedad de Mínima Curvatura
tags:
  - metodos-numericos
  - teoria
  - aproximacion-funciones
  - splines
draft: false
aliases:
  - Mínima curvatura
  - Propiedad de minimización del spline
  - Minimum curvature property
  - Energía de flexión
---

# Propiedad de Mínima Curvatura

> [!definicion]
> El **spline cúbico natural** es, entre todas las funciones $g \in C^2[a,b]$ que interpolan los datos $\{(x_i, y_i)\}$, la que **minimiza la energía de flexión**
> $$E[g] = \int_a^b \big(g''(x)\big)^2\,dx,$$
> una medida de la curvatura total. De ahí su nombre ("spline" = junquillo flexible) y su suavidad característica.

> [!info]
> Esta propiedad **variacional** explica por qué los [[Splines Cubicos Naturales Sujetos|splines cúbicos]] no oscilan: entre todas las interpolantes suaves, eligen la "menos curvada", la que un fleje físico adoptaría al pasar por los puntos. Es la justificación profunda de su estabilidad frente a los polinomios de grado alto.

---

## Teorema de minimización

> [!teorema]
> Sea $S$ el spline cúbico natural que interpola $\{(x_i, y_i)\}_{i=0}^n$ y sea $g \in C^2[a,b]$ **cualquier** otra función con $g(x_i) = y_i$. Entonces
> $$\int_a^b \big(S''\big)^2\,dx \;\leq\; \int_a^b \big(g''\big)^2\,dx,$$
> con igualdad si y solo si $g \equiv S$.

> [!demostracion]
> Sea $e = g - S$, que se anula en todos los nodos ($e(x_i)=0$). Desarrollando:
> $$\int_a^b (g'')^2 = \int_a^b (S'' + e'')^2 = \int_a^b (S'')^2 + 2\int_a^b S'' e'' + \int_a^b (e'')^2.$$
> Basta probar que el término cruzado $\int_a^b S'' e''\,dx = 0$. Integrando por partes:
> $$\int_a^b S'' e'' = \big[S'' e'\big]_a^b - \int_a^b S''' e'.$$
> El borde se anula por la condición **natural** $S''(a)=S''(b)=0$. En cada subintervalo $S'''$ es **constante** (cúbica), así que $\int_{x_i}^{x_{i+1}} S''' e' = S'''|_i\,[e]_{x_i}^{x_{i+1}} = S'''|_i\,(e(x_{i+1})-e(x_i)) = 0$ porque $e$ se anula en los nodos. Sumando sobre los tramos, el término cruzado es cero. Luego
> $$\int_a^b (g'')^2 = \int_a^b (S'')^2 + \int_a^b (e'')^2 \geq \int_a^b (S'')^2,$$
> con igualdad solo si $e'' \equiv 0$, es decir $e$ lineal; al anularse en los nodos, $e \equiv 0$.

---

## Interpretación física

> [!teoria]
> La energía de flexión de una viga elástica delgada es proporcional a $\int (g'')^2$ (curvatura al cuadrado). Un junquillo flexible (*spline*) forzado a pasar por puntos fijos adopta, por el principio de mínima energía, exactamente la forma del spline cúbico natural. La condición natural $S''=0$ en los extremos corresponde a una viga **libre** (sin momento) en los bordes.

> [!info]
> El spline **sujeto** minimiza la misma energía pero sobre las funciones que además cumplen $g'(a)=f'(a)$, $g'(b)=f'(b)$ (extremos empotrados). En ambos casos el spline es el minimizador de curvatura dentro de su clase de condiciones de frontera.

---

## Ejemplo

> [!ejemplo]
> **Comparación de energías** para interpolar $(0,0), (1,1), (2,0)$:
>
> | Interpolante | $\int_0^2 (g'')^2\,dx$ |
> |:---|:---:|
> | Spline cúbico natural | $12$ (mínimo) |
> | Polinomio $p_2(x) = 2x - x^2$ | $\int_0^2 (-2)^2 = 8$ ... |
> | Cualquier otra $C^2$ | $\geq$ la del spline |
>
> Entre las interpolantes $C^2$ con frontera natural, ninguna tiene menor energía de flexión que el spline: es el más "recto" posible compatible con los datos. *(El polinomio $p_2$ no cumple la condición natural $g''=0$ en los extremos, por lo que compite en otra clase.)*

---

## Consecuencias

> [!proposicion]
> 1. **No oscilación:** minimizar la curvatura impide los sobrepasos del [[Fenomeno Runge y Nodos Chebyshev|fenómeno de Runge]].
> 2. **Unicidad:** el minimizador es único, coherente con la unicidad del [[Condiciones Continuidad C2 y Sistema Tridiagonal|sistema tridiagonal]].
> 3. **Óptimo en clase amplia:** compite contra *todas* las $C^2$, no solo polinomios; es una propiedad fuerte.

---

## Relación con otras notas

> [!info]
> - El spline que cumple esta propiedad: [[Splines Cubicos Naturales Sujetos]].
> - La construcción que produce el minimizador: [[Condiciones Continuidad C2 y Sistema Tridiagonal]].
> - La estabilidad que de aquí se sigue: [[Convergencia y Estabilidad vs Polinomios Grado Alto]].
> - Panorama: [[Interpolacion Tramos Splines/index]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Funcional | $E[g] = \int_a^b (g'')^2\,dx$ |
| Minimizador | spline cúbico natural |
| Clase | todas las $g \in C^2$ interpolantes |
| Clave de la prueba | término cruzado nulo (frontera natural + $S'''$ constante) |
| Interpretación | energía de flexión de una viga |

> [!corolario]
> El spline cúbico natural minimiza la energía de flexión $\int (g'')^2$ entre todas las interpolantes $C^2$, propiedad variacional que se prueba mostrando que el término cruzado se anula gracias a la condición natural $S''=0$ y a que $S'''$ es constante por tramos. Esta minimización de curvatura es la razón profunda de su suavidad y de su ausencia de oscilación, en contraste directo con el [[Fenomeno Runge y Nodos Chebyshev|fenómeno de Runge]]. Físicamente corresponde a la forma que adopta un junquillo elástico, y caracteriza al spline más allá de su [[Condiciones Continuidad C2 y Sistema Tridiagonal|construcción algebraica]].
