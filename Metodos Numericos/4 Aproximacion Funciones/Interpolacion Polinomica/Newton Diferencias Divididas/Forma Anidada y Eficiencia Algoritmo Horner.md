---
title: Forma Anidada y Eficiencia del Algoritmo de Horner
order: 2
tags:
  - metodos-numericos
  - teoria
  - aproximacion-funciones
  - interpolacion
  - newton-interpolacion
draft: false
aliases:
  - Algoritmo de Horner
  - Forma anidada
  - Horner's method
  - Evaluación anidada de Newton
---

# Forma Anidada y Eficiencia del Algoritmo de Horner

> [!definicion]
> La **forma anidada de Horner** reescribe el polinomio de [[Newton Diferencias Divididas/index|Newton]]
> $$p_n(x) = c_0 + c_1(x-x_0) + c_2(x-x_0)(x-x_1) + \cdots + c_n\prod_{j=0}^{n-1}(x-x_j)$$
> como una anidación que se evalúa de adentro hacia afuera:
> $$p_n(x) = c_0 + (x-x_0)\big[c_1 + (x-x_1)\big[c_2 + \cdots + (x-x_{n-1})c_n\big]\big].$$

> [!info]
> La forma anidada evalúa $p_n$ en **$O(n)$** operaciones por punto (frente al $O(n^2)$ de la suma término a término), sin calcular potencias ni productos repetidos. Es el análogo, para la base de Newton, de la [[Costo Computacional Evaluacion Directa|forma baricéntrica]] de Lagrange.

---

## Algoritmo de Horner generalizado

> [!algoritmo]
> **Evaluación de Newton por Horner.** Dados los coeficientes $c_0,\dots,c_n$ (diagonal de la [[Tabla Diferencias Divididas y Coeficientes|tabla de diferencias divididas]]) y los nodos $x_0,\dots,x_{n-1}$:
>
> ```
> p = c[n]
> para k = n-1 hasta 0:
>     p = c[k] + (x - x[k]) * p
> retornar p
> ```
>
> Cada paso: una multiplicación y dos sumas → $2n$ multiplicaciones/sumas, es decir $O(n)$.

> [!proposicion]
> El algoritmo de Horner es **óptimo** en número de multiplicaciones para evaluar un polinomio general de grado $n$: ningún método usa menos de $n$ multiplicaciones (teorema de Ostrowski). Además es numéricamente más estable que evaluar potencias $x^k$ por separado.

---

## Ejemplo

> [!ejemplo]
> **Evaluar $p_3(x) = 1 + 2(x-0) - 1.5(x-0)(x-1) + 0.5(x-0)(x-1)(x-2)$ en $x = 3$.**
>
> Con $c = (1, 2, -1.5, 0.5)$ y nodos $(0, 1, 2)$, Horner de adentro afuera:
>
> | Paso $k$ | $p \leftarrow c_k + (x - x_k)\,p$ |
> |:---:|:---|
> | inicio | $p = 0.5$ |
> | 2 | $p = -1.5 + (3-2)(0.5) = -1.0$ |
> | 1 | $p = 2 + (3-1)(-1.0) = 0.0$ |
> | 0 | $p = 1 + (3-0)(0.0) = 1.0$ |
>
> $p_3(3) = 1.0$, con $3$ multiplicaciones en lugar de las $\sim 9$ de la forma desarrollada.

---

## Comparación de evaluaciones

> [!info]
> | Forma | Operaciones por punto | Observación |
> |:---|:---:|:---|
> | Suma directa de Newton | $O(n^2)$ | recalcula productos $\prod(x-x_j)$ |
> | **Horner (anidada)** | $O(n)$ | óptima en multiplicaciones |
> | Lagrange directa | $O(n^2)$ | — |
> | [[Costo Computacional Evaluacion Directa\|Lagrange baricéntrica]] | $O(n)$ | requiere pesos $w_i$ |
>
> Newton + Horner y Lagrange baricéntrico son las dos formas $O(n)$ por punto; Newton tiene además coeficientes explícitos e incrementales.

---

## Horner y derivadas

> [!teoria]
> El esquema de Horner extendido (síntesis de Ruffini repetida) produce, junto al valor $p_n(x)$, también las **derivadas** $p_n'(x), p_n''(x), \dots$ con costo $O(n)$ adicional por orden. Esto es útil en [[Newton Raphson/index|Newton-Raphson]] sobre polinomios y en la [[Diferenciacion Numerica/index|diferenciación numérica]] basada en interpolantes.

---

## Relación con otras notas

> [!info]
> - Los coeficientes que Horner evalúa: [[Tabla Diferencias Divididas y Coeficientes]].
> - El polinomio que se construye: [[Newton Diferencias Divididas/index]].
> - La forma $O(n)$ análoga en Lagrange: [[Costo Computacional Evaluacion Directa]].
> - Uso de las derivadas obtenidas: [[Relacion Diferencias Divididas Derivadas]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Forma | anidada $c_0 + (x-x_0)[c_1 + (x-x_1)[\cdots]]$ |
| Costo | $O(n)$ por punto |
| Multiplicaciones | $n$ (óptimo) |
| Estabilidad | mejor que evaluar potencias |
| Extensión | derivadas en $O(n)$ por orden |

> [!corolario]
> La forma anidada de Horner evalúa el polinomio de Newton en $O(n)$ operaciones por punto —óptimo en multiplicaciones— recorriendo los coeficientes de la [[Tabla Diferencias Divididas y Coeficientes|tabla de diferencias divididas]] de adentro hacia afuera, sin recalcular productos. Junto con la incrementalidad de las diferencias divididas, hace de [[Newton Diferencias Divididas/index|Newton + Horner]] la formulación más eficiente con coeficientes explícitos, equiparable a la [[Costo Computacional Evaluacion Directa|forma baricéntrica]] de Lagrange y extensible al cálculo simultáneo de derivadas.
