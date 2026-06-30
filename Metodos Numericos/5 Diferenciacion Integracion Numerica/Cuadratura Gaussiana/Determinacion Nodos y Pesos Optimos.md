---
title: Determinación de Nodos y Pesos Óptimos
order: 2
tags:
  - metodos-numericos
  - teoria
  - diferenciacion-integracion
  - cuadratura-gaussiana
draft: false
aliases:
  - Nodos y pesos de Gauss
  - Cálculo de pesos gaussianos
  - Gauss nodes and weights
---

# Determinación de Nodos y Pesos Óptimos

> [!definicion]
> En la [[Cuadratura Gaussiana/index|cuadratura gaussiana]] de orden $n$, los **nodos** $x_i$ son los ceros del [[Fundamentos Gauss Legendre Polinomios Ortogonales|polinomio de Legendre]] $P_n$, y los **pesos** se obtienen integrando los [[Formulacion Polinomios Cardinales L i x|polinomios cardinales]] asociados a esos nodos:
> $$w_i = \int_{-1}^1 L_i(x)\,dx = \frac{2}{(1-x_i^2)\,[P_n'(x_i)]^2}.$$

> [!info]
> Una vez fijados los nodos (ceros de $P_n$), los pesos quedan determinados por la condición de que la regla sea exacta para polinomios de grado $\leq n-1$. La fórmula cerrada del peso evita integrar explícitamente cada cardinal.

---

## Cálculo de los pesos

> [!teorema]
> Con los nodos $x_i$ (ceros de $P_n$), los pesos de Gauss-Legendre son
> $$w_i = \frac{2}{(1-x_i^2)\,[P_n'(x_i)]^2} > 0, \qquad \sum_{i=1}^n w_i = 2.$$
> Todos los pesos son **estrictamente positivos**, lo que garantiza la estabilidad de la cuadratura.

> [!demostracion]
> Los pesos se definen por $w_i = \int_{-1}^1 L_i$, lo que hace la regla exacta para grado $\leq n-1$ (integra los cardinales). La positividad se ve aplicando la regla —exacta hasta grado $2n-1$— al polinomio $L_i(x)^2$ (grado $2n-2 < 2n-1$):
> $$0 < \int_{-1}^1 L_i^2\,dx = \sum_j w_j L_i(x_j)^2 = \sum_j w_j \delta_{ij}^2 = w_i.$$
> Luego $w_i > 0$. La suma $\sum w_i = 2$ por exactitud sobre $f\equiv1$ (integra $\int_{-1}^1 1 = 2$).

---

## Tabla de nodos y pesos

> [!info]
> **Gauss-Legendre en $[-1,1]$:**
>
> | $n$ | Nodos $x_i$ | Pesos $w_i$ | Grado exacto |
> |:---:|:---|:---|:---:|
> | 1 | $0$ | $2$ | 1 |
> | 2 | $\pm0.577350$ | $1,\ 1$ | 3 |
> | 3 | $0,\ \pm0.774597$ | $0.888889,\ 0.555556$ | 5 |
> | 4 | $\pm0.339981,\ \pm0.861136$ | $0.652145,\ 0.347855$ | 7 |
> | 5 | $0,\ \pm0.538469,\ \pm0.906180$ | $0.568889,\ 0.478629,\ 0.236927$ | 9 |
>
> Nodos y pesos son simétricos respecto a $0$. Se tabulan o se calculan numéricamente.

---

## Cálculo numérico: el algoritmo de Golub-Welsch

> [!teoria]
> Los nodos y pesos se obtienen de un problema de **autovalores**. La [[Fundamentos Gauss Legendre Polinomios Ortogonales|recurrencia de tres términos]] de los polinomios ortogonales define una matriz **tridiagonal simétrica** $J$ (matriz de Jacobi); entonces:
> - los **nodos** $x_i$ son los **autovalores** de $J$ (calculables por el método [[Metodo QR/index|QR]]),
> - los **pesos** son $w_i = 2\,(v_i^{(1)})^2$, con $v_i^{(1)}$ la primera componente del autovector normalizado.
>
> Es el método estándar (Golub-Welsch), estable y eficiente, conectando la cuadratura con el [[Valores Vectores Propios/index|cálculo de autovalores]].

---

## Ejemplo

> [!ejemplo]
> **Peso para $n=2$, nodo $x_1 = 1/\sqrt3$.** Con $P_2(x) = \frac12(3x^2-1)$, $P_2'(x) = 3x$:
> $$w_1 = \frac{2}{(1 - 1/3)\,[3/\sqrt3]^2} = \frac{2}{(2/3)\cdot 3} = \frac{2}{2} = 1.$$
> Igualmente $w_2 = 1$. La regla de 2 nodos es $\int_{-1}^1 f \approx f(-1/\sqrt3) + f(1/\sqrt3)$, exacta hasta grado $3$.

---

## Relación con otras notas

> [!info]
> - Por qué los nodos son ceros de $P_n$: [[Fundamentos Gauss Legendre Polinomios Ortogonales]].
> - La exactitud que estos pesos garantizan: [[Grado Exactitud Polinomica 2n 1]].
> - El cálculo por autovalores: [[Metodo QR/index]] y [[Valores Vectores Propios/index]].
> - El traslado a $[a,b]$: [[Cambio Variable Intervalo General]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Nodos | ceros de $P_n$ |
| Pesos | $w_i = \frac{2}{(1-x_i^2)[P_n'(x_i)]^2}$ |
| Positividad | $w_i > 0$ (estabilidad) |
| Suma | $\sum w_i = 2$ |
| Cálculo numérico | Golub-Welsch (autovalores de matriz de Jacobi) |

> [!corolario]
> Los nodos de Gauss-Legendre son los ceros de $P_n$ y los pesos $w_i = \frac{2}{(1-x_i^2)[P_n'(x_i)]^2}$ se fijan por la exactitud para grado $\leq n-1$. Todos los pesos son estrictamente positivos —se prueba aplicando la regla a $L_i^2$— lo que garantiza estabilidad, a diferencia de [[Inestabilidad Pesos Negativos Grado Alto|Newton-Cotes de grado alto]]. En la práctica se calculan por el algoritmo de Golub-Welsch como autovalores de una matriz tridiagonal, conectando la cuadratura con el [[Metodo QR/index|método QR]]. Estos nodos y pesos producen el [[Grado Exactitud Polinomica 2n 1|grado de exactitud $2n-1$]].
