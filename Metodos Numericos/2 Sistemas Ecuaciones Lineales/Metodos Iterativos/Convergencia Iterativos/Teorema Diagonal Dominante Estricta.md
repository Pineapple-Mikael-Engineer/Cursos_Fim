---
title: Teorema Diagonal Dominante Estricta
order: 1
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - sistemas-lineales
  - metodos-iterativos
  - convergencia
  - diagonal-dominante
draft: false
aliases:
  - Diagonal dominante estricta
  - Teorema de las diagonales dominantes
  - Condición suficiente de Jacobi
---

# Teorema de la Diagonal Dominante Estricta

> [!definicion]
> Una matriz $A \in \mathbb{R}^{n \times n}$ es **estrictamente diagonal dominante por filas** si:
> $$|a_{ii}| > \sum_{\substack{j=1 \\ j \neq i}}^n |a_{ij}|, \quad \forall i = 1, \dots, n$$
>
> Análogamente, es **estrictamente diagonal dominante por columnas** si:
> $$|a_{jj}| > \sum_{\substack{i=1 \\ i \neq j}}^n |a_{ij}|, \quad \forall j = 1, \dots, n$$

---

## Ejemplo

> [!ejemplo]
> **Matriz diagonal dominante.**
>
> $$A = \begin{pmatrix} 4 & -1 & 0 \\ -1 & 4 & -1 \\ 0 & -1 & 4 \end{pmatrix}$$
>
> Verificación fila por fila:
> - Fila 1: $|4| = 4 > |-1| + |0| = 1$ ✓
> - Fila 2: $|4| = 4 > |-1| + |-1| = 2$ ✓
> - Fila 3: $|4| = 4 > |0| + |-1| = 1$ ✓
>
> **Matriz NO diagonal dominante.**
>
> $$B = \begin{pmatrix} 2 & 5 & 0 \\ 1 & 3 & 1 \\ 0 & 2 & 1 \end{pmatrix}$$
>
> - Fila 1: $|2| = 2 < |5| + |0| = 5$ ✗ (ya falla)
>
> **Consecuencias en la convergencia.**
>
> Para la matriz $A$, el método de [[Jacobi]] converge. Para la matriz $B$, puede no converger (puede que si o que no).

---

## Teorema

> [!teorema]
> Si $A \in \mathbb{R}^{n \times n}$ es estrictamente diagonal dominante por filas (o por columnas), entonces:
> 1. $A$ es no singular.
> 2. El método de [[Jacobi]] converge para cualquier $y^{(0)}$.
> 3. El método de [[Gauss Seidel]] converge para cualquier $y^{(0)}$.

---

## Demostración

### Parte 1: $A$ es no singular

> [!demostracion]
> Supóngase que $A$ es singular. Entonces existe $x \neq 0$ tal que $Ax = 0$.
>
> Sea $i$ un índice donde $|x_i| = \max_{1 \leq j \leq n} |x_j| > 0$. La ecuación $i$-ésima del sistema $Ax = 0$ es:
> $$a_{ii} x_i + \sum_{\substack{j=1 \\ j \neq i}}^n a_{ij} x_j = 0$$
>
> Despejando:
> $$a_{ii} x_i = -\sum_{\substack{j=1 \\ j \neq i}}^n a_{ij} x_j$$
>
> Tomando valor absoluto y usando desigualdad triangular:
> $$|a_{ii}| |x_i| = \left| \sum_{\substack{j=1 \\ j \neq i}}^n a_{ij} x_j \right| \leq \sum_{\substack{j=1 \\ j \neq i}}^n |a_{ij}| |x_j| \leq \left( \sum_{\substack{j=1 \\ j \neq i}}^n |a_{ij}| \right) |x_i|$$
>
> Como $|x_i| > 0$, se cancela:
> $$|a_{ii}| \leq \sum_{\substack{j=1 \\ j \neq i}}^n |a_{ij}|$$
>
> Esto contradice la definición de diagonal dominante estricta ($|a_{ii}| > \sum_{j \neq i} |a_{ij}|$). Por lo tanto $A$ es no singular.

### Parte 2: Convergencia de Jacobi

> [!demostracion]
> Para el método de [[Jacobi]], la matriz de iteración es:
> $$T_J = I - D^{-1}A$$
>
> donde $D = \operatorname{diag}(a_{11}, \dots, a_{nn})$.
>
> Sea $\lambda$ un autovalor de $T_J$ con autovector $v \neq 0$, es decir $T_J v = \lambda v$. Esto equivale a:
> $$(I - D^{-1}A)v = \lambda v \quad \implies \quad D^{-1}A v = (1 - \lambda) v \quad \implies \quad A v = (1 - \lambda) D v$$
>
> Escribiendo componente a componente:
> $$a_{ii} v_i + \sum_{\substack{j=1 \\ j \neq i}}^n a_{ij} v_j = (1 - \lambda) a_{ii} v_i$$
>
> Despejando:
> $$\sum_{\substack{j=1 \\ j \neq i}}^n a_{ij} v_j = (1 - \lambda) a_{ii} v_i - a_{ii} v_i = -\lambda a_{ii} v_i$$
>
> Por lo tanto:
> $$\lambda a_{ii} v_i = -\sum_{\substack{j=1 \\ j \neq i}}^n a_{ij} v_j$$
>
> Sea $i$ un índice donde $|v_i| = \max_{1 \leq j \leq n} |v_j| > 0$. Tomando valor absoluto:
> $$|\lambda| |a_{ii}| |v_i| = \left| \sum_{\substack{j=1 \\ j \neq i}}^n a_{ij} v_j \right| \leq \sum_{\substack{j=1 \\ j \neq i}}^n |a_{ij}| |v_j| \leq \left( \sum_{\substack{j=1 \\ j \neq i}}^n |a_{ij}| \right) |v_i|$$
>
> Cancelando $|v_i| > 0$:
> $$|\lambda| |a_{ii}| \leq \sum_{\substack{j=1 \\ j \neq i}}^n |a_{ij}|$$
>
> Usando la hipótesis de diagonal dominante estricta:
> $$|\lambda| \leq \frac{\sum_{j \neq i} |a_{ij}|}{|a_{ii}|} < 1$$
>
> Esto vale para todo autovalor $\lambda$ de $T_J$, por lo tanto $\rho(T_J) < 1$. Por el [[Criterio Radio Espectral Convergencia|criterio del radio espectral]], el método de Jacobi converge.

### Parte 3: Convergencia de Gauss-Seidel

> [!demostracion]
> Para el método de [[Gauss Seidel]], la matriz de iteración es $T_{GS} = (D - E)^{-1}F$. Se puede demostrar que $\rho(T_{GS}) \leq \rho(T_J) < 1$ bajo la misma hipótesis (véase el teorema de Stein-Rosenberg en [[Gauss Seidel]]). Por lo tanto, Gauss-Seidel también converge.
>
> Una demostración directa sigue un argumento similar al de Jacobi pero con un poco más de álgebra.

---

## Condición por columnas

> [!teorema]
> Si $A$ es estrictamente diagonal dominante por columnas, entonces $A^T$ es estrictamente diagonal dominante por filas. Como los autovalores de $T_J$ (y $T_{GS}$) para $A$ están relacionados con los de $A^T$, la convergencia también está garantizada.

---

## Relación con otras condiciones

> [!info]
> La diagonal dominante estricta es una **condición suficiente**, no necesaria. Existen matrices que no son diagonal dominantes pero para las cuales Jacobi o Gauss-Seidel convergen.
>
> **Ejemplo.**
> $$A = \begin{pmatrix} 2 & 3 \\ 1 & 2 \end{pmatrix}$$
>
> Esta matriz **no** es diagonal dominante, porque en la primera fila:
> $$|2| < |3|$$
>
> Sin embargo:
>
> Para Jacobi:
>
> $$D=\begin{pmatrix}2&0\\0&2\end{pmatrix}, \qquad L+U=\begin{pmatrix}0&-3\\-1&0\end{pmatrix}$$
>
> $$T_J=D^{-1}(L+U)=
> \begin{pmatrix}
> 0 & -3/2\\
> -1/2 & 0
> \end{pmatrix}$$
>
> Sus autovalores satisfacen:
>
> $$\lambda^2-\frac{3}{4}=0$$
>
> por lo tanto:
>
> $$\lambda=\pm \frac{\sqrt{3}}{2} \approx \pm 0.866$$
>
> así que:
>
> $$\rho(T_J)=0.866<1$$
>
> ⇒ **Jacobi converge**.
>
> Para Gauss-Seidel:
>
> $$T_{GS}=(D-L)^{-1}U=
> \begin{pmatrix}
> 0 & -3/2\\
> 0 & 3/4
> \end{pmatrix}$$
>
> Sus autovalores son:
>
> $$0,\; 3/4$$
>
> entonces:
>
> $$\rho(T_{GS})=0.75<1$$
>
> ⇒ **Gauss-Seidel converge**.

---

## Implicaciones prácticas

> [!info]
> **¿Cuándo es útil este teorema?**
>
> - Muchas matrices que surgen de discretizaciones de EDPs (ecuaciones diferenciales parciales) son diagonal dominantes.
> - La condición es fácil de verificar: solo requiere inspeccionar los coeficientes de $A$.
> - No requiere calcular autovalores ni normas.
> - Es una garantía de convergencia rápida (cuanto más estricta la desigualdad, menor $\rho(T_J)$).

> [!warning]
> **Limitaciones.**
>
> - La diagonal dominante estricta es suficiente pero no necesaria.
> - Matrices que no cumplen la condición pueden seguir convergendo (por ejemplo, matrices simétricas definidas positivas para Gauss-Seidel).
> - Para matrices muy grandes y dispersas, verificar la condición es $O(\text{nnz})$, lo cual es aceptable.

---

## Resumen

> [!corolario]
> La diagonal dominante estricta es la condición suficiente más simple y práctica para garantizar la convergencia de los métodos de Jacobi y Gauss-Seidel:
>
> - **Definición:** $|a_{ii}| > \sum_{j \neq i} |a_{ij}|$ para toda fila $i$.
> - **Consecuencia:** $\rho(T_J) < 1$ y $\rho(T_{GS}) < 1$.
> - **Ventaja:** Fácil de verificar, no requiere cálculos complejos.
> - **Limitación:** Es suficiente, no necesaria.
>
> Este teorema se aplica directamente a [[Jacobi]] y [[Gauss Seidel]]. Para condiciones de convergencia más generales (como matrices simétricas definidas positivas), véase [[Criterio Radio Espectral Convergencia]]. Para estimaciones cuantitativas de la velocidad de convergencia bajo esta condición, véase [[Convergencia Iterativos/Estimacion Error y Cotas A Priori|Estimacion Error y Cotas A Priori]].
