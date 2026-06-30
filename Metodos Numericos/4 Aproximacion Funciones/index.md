---
title: Aproximación de Funciones
order: 4
tags:
  - metodos-numericos
  - teoria
  - aproximacion-funciones
  - index
draft: false
aliases:
  - Aproximación de funciones
  - Interpolación y ajuste
  - Function approximation
---

# Aproximación de Funciones

> [!definicion]
> La **aproximación de funciones** construye una función simple $\tilde f$ —típicamente un polinomio o una función a tramos— que represente datos discretos $\{(x_i, y_i)\}_{i=0}^n$ o una función complicada. Se distinguen dos objetivos: **interpolar** (pasar exactamente por los datos) y **ajustar** (minimizar la desviación a los datos sin pasar por ellos).

> [!info]
> El criterio decide el método: si los datos son exactos y se quieren reproducir, se interpola; si contienen ruido o son más que los grados de libertad, se ajusta. Este capítulo cubre la [[Interpolacion Polinomica/index|interpolación polinómica]], la [[Interpolacion Tramos Splines/index|interpolación por tramos (splines)]] y el [[Ajuste Minimos Cuadrados/index|ajuste por mínimos cuadrados]].

---

## Interpolar frente a ajustar

> [!info]
> | | Interpolación | Ajuste (mínimos cuadrados) |
> |:---|:---|:---|
> | Condición | $\tilde f(x_i) = y_i$ exacto | minimiza $\sum (\tilde f(x_i) - y_i)^2$ |
> | Datos | exactos | con ruido / sobredeterminados |
> | Grados de libertad | $= n+1$ (tantos como datos) | $< n+1$ |
> | Riesgo | oscilación ([[Fenomeno Runge y Nodos Chebyshev\|Runge]]) | sesgo si el modelo es pobre |

---

## Las tres familias

> [!info]
> **Interpolación polinómica.** Un único polinomio $p_n$ de grado $\leq n$ que pasa por los $n+1$ datos. Existe y es único, pero degrada con grado alto. Se estudia en [[Interpolacion Polinomica/index]].

> [!info]
> **Splines.** Polinomios de grado bajo (típicamente cúbicos) empalmados con continuidad, que evitan la oscilación de los polinomios de grado alto. Se estudian en [[Interpolacion Tramos Splines/index]].

> [!info]
> **Mínimos cuadrados.** Cuando los datos tienen ruido o son más que los parámetros, se ajusta un modelo minimizando el residuo en norma euclídea. Se estudia en [[Ajuste Minimos Cuadrados/index]].

---

## Ejemplo

> [!ejemplo]
> **Cuatro puntos de $f(x) = \cos x$ en $[0, \pi]$:** $(0, 1)$, $(\pi/3, 0.5)$, $(2\pi/3, -0.5)$, $(\pi, -1)$.
>
> | Método | Resultado |
> |:---|:---|
> | Interpolación cúbica ($p_3$) | pasa por los 4 puntos; buena aquí, pero oscila si se añaden muchos nodos |
> | Spline cúbico | pasa por los 4 puntos con curvatura mínima; estable al refinar |
> | Mínimos cuadrados (recta) | $\approx -0.64x + 1$; no pasa por los puntos, capta la tendencia |
>
> Con pocos nodos suaves los tres coinciden en calidad; las diferencias se revelan al aumentar nodos o al introducir ruido.

---

## Resumen

| Familia | Subdirectorio |
|:---|:---|
| Interpolación polinómica | [[Interpolacion Polinomica/index]] |
| Splines (interpolación por tramos) | [[Interpolacion Tramos Splines/index]] |
| Ajuste por mínimos cuadrados | [[Ajuste Minimos Cuadrados/index]] |

> [!corolario]
> La aproximación de funciones se organiza según se quieran reproducir los datos exactamente (interpolación) o capturar su tendencia minimizando el error (ajuste). La [[Interpolacion Polinomica/index|interpolación polinómica]] es la base teórica —existencia, unicidad y error—, pero su inestabilidad con grado alto motiva los [[Interpolacion Tramos Splines/index|splines]]; cuando los datos tienen ruido, el [[Ajuste Minimos Cuadrados/index|ajuste por mínimos cuadrados]] es la herramienta adecuada. Las tres familias reaparecen en la [[Diferenciacion Numerica/index|diferenciación e integración numérica]], que se construyen sobre funciones interpolantes.
