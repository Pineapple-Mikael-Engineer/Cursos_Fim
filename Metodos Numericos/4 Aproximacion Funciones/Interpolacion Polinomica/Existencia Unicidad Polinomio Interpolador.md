---
title: Existencia y Unicidad del Polinomio Interpolador
order: 1
tags:
  - metodos-numericos
  - teoria
  - aproximacion-funciones
  - interpolacion
draft: false
aliases:
  - Existencia y unicidad del interpolador
  - Unicidad del polinomio interpolador
  - Teorema de unicidad de interpolación
---

# Existencia y Unicidad del Polinomio Interpolador

> [!definicion]
> Dados $n+1$ nodos **distintos** $x_0, \dots, x_n$ y valores $y_0, \dots, y_n$, el problema de interpolación busca $p \in \mathbb{P}_n$ (polinomios de grado $\leq n$) con $p(x_i) = y_i$ para todo $i$.

> [!info]
> El resultado fundamental es que tal polinomio **existe y es único** mientras los nodos sean distintos. La unicidad es lo que da sentido a hablar de "el" polinomio interpolador, sin importar la base ([[Lagrange/index|Lagrange]], [[Newton Diferencias Divididas/index|Newton]], [[Matriz Vandermonde Mal Condicionamiento|Vandermonde]]) con que se construya.

---

## Teorema fundamental

> [!teorema]
> Sean $x_0, x_1, \dots, x_n$ nodos distintos. Para cualesquiera valores $y_0, \dots, y_n \in \mathbb{R}$, existe un **único** polinomio $p \in \mathbb{P}_n$ tal que $p(x_i) = y_i$ para $i = 0, \dots, n$.

> [!demostracion]
> **Existencia (constructiva, vía Lagrange).** Definidos los [[Formulacion Polinomios Cardinales L i x|polinomios cardinales]]
> $$L_i(x) = \prod_{\substack{j=0 \\ j\neq i}}^n \frac{x - x_j}{x_i - x_j} \in \mathbb{P}_n, \qquad L_i(x_k) = \delta_{ik},$$
> el polinomio $p(x) = \sum_{i=0}^n y_i L_i(x)$ tiene grado $\leq n$ y cumple $p(x_k) = \sum_i y_i \delta_{ik} = y_k$. Existe.
>
> **Unicidad.** Supóngase que $p, q \in \mathbb{P}_n$ ambos interpolan. La diferencia $r = p - q \in \mathbb{P}_n$ se anula en los $n+1$ nodos distintos $x_0, \dots, x_n$. Un polinomio de grado $\leq n$ con $n+1$ raíces distintas es idénticamente nulo (teorema fundamental del álgebra). Luego $r \equiv 0$ y $p = q$.

---

## Lectura algebraica: sistema de Vandermonde

> [!teorema]
> En la base de monomios $p(x) = \sum_{j=0}^n c_j x^j$, las condiciones de interpolación forman el sistema lineal $V c = y$ con la [[Matriz Vandermonde Mal Condicionamiento|matriz de Vandermonde]]
> $$V = \begin{pmatrix} 1 & x_0 & \cdots & x_0^n \\ 1 & x_1 & \cdots & x_1^n \\ \vdots & & & \vdots \\ 1 & x_n & \cdots & x_n^n \end{pmatrix}, \qquad \det V = \prod_{0 \leq i < j \leq n} (x_j - x_i).$$
> Con nodos distintos, $\det V \neq 0$, luego $V$ es no singular y el sistema tiene solución única: otra prueba de existencia y unicidad.

> [!demostracion]
> El determinante de Vandermonde $\prod_{i<j}(x_j - x_i)$ es no nulo si y solo si todos los nodos son distintos. Un sistema lineal con matriz no singular tiene solución única $c = V^{-1}y$, que son los coeficientes del único interpolador.

---

## Ejemplo

> [!ejemplo]
> **Tres nodos, unicidad ilustrada.** Para $(0,1), (1,2), (2,5)$, el determinante de Vandermonde es
> $$\det V = (1-0)(2-0)(2-1) = 2 \neq 0,$$
> luego existe un único $p_2$. Es $p_2(x) = x^2 + 1$. Cualquier intento de hallar otro polinomio de grado $\leq 2$ por esos tres puntos conduce al mismo, pues su diferencia tendría $3$ raíces siendo de grado $\leq 2$.

> [!warning]
> **La unicidad exige nodos distintos.** Si dos nodos coinciden ($x_i = x_j$, $i\neq j$) con $y_i \neq y_j$, no existe polinomio (una función no toma dos valores en el mismo punto); si $y_i = y_j$, el problema queda subdeterminado. La interpolación con nodos repetidos se generaliza a la [[Relacion Diferencias Divididas Derivadas|interpolación de Hermite]], donde se prescriben también derivadas.

---

## Consecuencias

> [!proposicion]
> 1. **Independencia de la base:** todas las construcciones dan el mismo $p_n$; la elección es por eficiencia/estabilidad, no por el resultado.
> 2. **Dimensión:** $\mathbb{P}_n$ tiene dimensión $n+1$, exactamente el número de condiciones; por eso el problema está exactamente determinado.
> 3. **Linealidad:** $p_n$ depende linealmente de los datos $y_i$, lo que permite construir el [[Error Interpolacion Formula Cauchy|término de error]] y las fórmulas de [[Integracion Numerica Newton Cotes/index|cuadratura]].

---

## Relación con otras notas

> [!info]
> - La construcción explícita usada en la prueba de existencia: [[Formulacion Polinomios Cardinales L i x]].
> - El sistema lineal subyacente y su condicionamiento: [[Matriz Vandermonde Mal Condicionamiento]].
> - La generalización con derivadas (nodos confluentes): [[Relacion Diferencias Divididas Derivadas]].
> - Panorama: [[Interpolacion Polinomica/index]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Enunciado | $n+1$ nodos distintos → único $p \in \mathbb{P}_n$ |
| Existencia | constructiva vía polinomios cardinales |
| Unicidad | diferencia con $n+1$ raíces de grado $\leq n$ ⇒ nula |
| Versión algebraica | $\det V = \prod_{i<j}(x_j-x_i) \neq 0$ |
| Condición | nodos distintos |

> [!corolario]
> Dados $n+1$ nodos distintos, existe un único polinomio de grado $\leq n$ que interpola los datos: la existencia se prueba construyéndolo con los polinomios cardinales de Lagrange, y la unicidad porque la diferencia de dos interpoladores tendría más raíces que su grado. Equivalentemente, la [[Matriz Vandermonde Mal Condicionamiento|matriz de Vandermonde]] es no singular cuando los nodos son distintos. Esta unicidad es la base conceptual del capítulo: justifica que [[Lagrange/index|Lagrange]] y [[Newton Diferencias Divididas/index|Newton]] sean dos caras del mismo polinomio y habilita el análisis del [[Error Interpolacion Formula Cauchy|error de interpolación]].
