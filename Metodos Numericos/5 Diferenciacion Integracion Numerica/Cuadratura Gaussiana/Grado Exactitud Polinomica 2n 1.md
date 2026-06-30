---
title: Grado de Exactitud Polinómica 2n−1
order: 3
tags:
  - metodos-numericos
  - teoria
  - diferenciacion-integracion
  - cuadratura-gaussiana
draft: false
aliases:
  - Grado de exactitud 2n-1
  - Exactitud de Gauss
  - Degree of exactness
---

# Grado de Exactitud Polinómica $2n-1$

> [!definicion]
> La **cuadratura gaussiana** de $n$ nodos tiene **grado de exactitud $2n-1$**: integra exactamente todo polinomio de grado $\leq 2n-1$. Es el grado máximo alcanzable con $n$ nodos, el doble del de [[Formulacion General Pesos Newton Cotes|Newton-Cotes]] ($\sim n$).

> [!info]
> El resultado es óptimo: ninguna regla de $n$ nodos puede integrar exactamente todo polinomio de grado $2n$. La cuadratura gaussiana satura esta cota gracias a la libertad de elegir los $2n$ parámetros (nodos y pesos).

---

## Teorema de exactitud

> [!teorema]
> La regla de Gauss-Legendre con $n$ nodos (ceros de $P_n$) y pesos $w_i = \int L_i$ satisface
> $$\int_{-1}^1 p(x)\,dx = \sum_{i=1}^n w_i\, p(x_i) \quad \text{para todo } p \text{ de grado} \leq 2n-1.$$

> [!demostracion]
> Sea $p$ de grado $\leq 2n-1$. Dividiendo por $P_n$ (grado $n$):
> $$p(x) = q(x)P_n(x) + r(x), \qquad \deg q,\ \deg r \leq n-1.$$
> **Integral exacta:**
> $$\int_{-1}^1 p\,dx = \int_{-1}^1 q P_n\,dx + \int_{-1}^1 r\,dx = 0 + \int_{-1}^1 r\,dx,$$
> donde $\int q P_n = 0$ por [[Fundamentos Gauss Legendre Polinomios Ortogonales|ortogonalidad]] ($\deg q < n$). **Suma de cuadratura:** en los nodos $P_n(x_i) = 0$, así que $p(x_i) = r(x_i)$. Luego
> $$\sum_i w_i p(x_i) = \sum_i w_i r(x_i) = \int_{-1}^1 r\,dx,$$
> porque la regla es exacta para $r$ (grado $\leq n-1$, por construcción de los pesos). Ambas expresiones coinciden con $\int r$, luego son iguales. $\blacksquare$

---

## Optimalidad: no se puede más

> [!teorema]
> Ninguna regla de cuadratura de $n$ nodos tiene grado de exactitud $\geq 2n$.

> [!demostracion]
> Sea cualquier regla con nodos $x_1,\dots,x_n$. El polinomio
> $$p(x) = \prod_{i=1}^n (x - x_i)^2$$
> tiene grado $2n$ y es $\geq 0$, con $p(x_i) = 0$. La cuadratura da $\sum_i w_i p(x_i) = 0$, pero $\int_{-1}^1 p\,dx > 0$ (integrando positivo no nulo). La regla falla para este polinomio de grado $2n$. Luego $2n-1$ es el máximo posible, y Gauss lo alcanza.

---

## Ejemplo: verificación

> [!ejemplo]
> **Gauss de 2 nodos integra exactamente hasta grado 3.** Regla: $\int_{-1}^1 f \approx f(-1/\sqrt3) + f(1/\sqrt3)$.
>
> | $p(x)$ | $\int_{-1}^1 p\,dx$ | Cuadratura | ¿Exacta? |
> |:---|:---:|:---:|:---:|
> | $1$ | $2$ | $1+1=2$ | ✓ |
> | $x$ | $0$ | $-\tfrac{1}{\sqrt3}+\tfrac{1}{\sqrt3}=0$ | ✓ |
> | $x^2$ | $2/3$ | $\tfrac13+\tfrac13=\tfrac23$ | ✓ |
> | $x^3$ | $0$ | $-\tfrac{1}{3\sqrt3}+\tfrac{1}{3\sqrt3}=0$ | ✓ |
> | $x^4$ | $2/5$ | $\tfrac19+\tfrac19=\tfrac29$ | ✗ ($\tfrac29\neq\tfrac25$) |
>
> Exacta hasta grado $3 = 2(2)-1$, falla en grado $4$. Confirma el teorema.

---

## Error de la cuadratura gaussiana

> [!info]
> Para $f \in C^{2n}[-1,1]$, el error de Gauss-Legendre es
> $$\int_{-1}^1 f - \sum_i w_i f(x_i) = \frac{2^{2n+1}(n!)^4}{(2n+1)[(2n)!]^3}\,f^{(2n)}(\xi).$$
> Depende de $f^{(2n)}$: para $n$ moderado, un orden de derivada altísimo, lo que explica la convergencia extremadamente rápida (espectral para $f$ analítica).

---

## Relación con otras notas

> [!info]
> - La ortogonalidad que sostiene la prueba: [[Fundamentos Gauss Legendre Polinomios Ortogonales]].
> - Los nodos y pesos concretos: [[Determinacion Nodos y Pesos Optimos]].
> - El grado $\sim n$ de la alternativa: [[Formulacion General Pesos Newton Cotes]].
> - La comparación de eficiencia: [[Comparacion Eficiencia vs Newton Cotes]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Grado de exactitud | $2n-1$ con $n$ nodos |
| Clave de la prueba | $p = qP_n + r$; $\int qP_n = 0$; $p(x_i)=r(x_i)$ |
| Optimalidad | $\prod(x-x_i)^2$ falla en grado $2n$ |
| Error | $\propto f^{(2n)}(\xi)$ |

> [!corolario]
> La cuadratura gaussiana de $n$ nodos tiene grado de exactitud $2n-1$: dividiendo cualquier polinomio de grado $\leq 2n-1$ por $P_n$, la parte con $P_n$ se anula por [[Fundamentos Gauss Legendre Polinomios Ortogonales|ortogonalidad]] y el resto de grado $\leq n-1$ se integra exactamente. Es óptimo —el polinomio $\prod(x-x_i)^2$ de grado $2n$ demuestra que no se puede mejorar— y duplica el grado de [[Formulacion General Pesos Newton Cotes|Newton-Cotes]] con los mismos nodos. Su error, proporcional a $f^{(2n)}$, produce la [[Comparacion Eficiencia vs Newton Cotes|convergencia rapidísima]] que la hace el método de cuadratura más eficiente para integrandos suaves.
