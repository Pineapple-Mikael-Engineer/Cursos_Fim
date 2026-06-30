---
title: Existencia Unicidad LU Matrices No Singulares
order: 1
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - sistemas-lineales
  - metodos-directos
  - factorizacion-matricial
draft: false
aliases:
  - Condiciones de existencia LU
  - Unicidad de la factorización LU
  - Menores principales líderes
---

# Existencia y Unicidad de la Factorización LU para Matrices No Singulares

> [!definicion]
> Dada una matriz $A \in \mathbb{R}^{n \times n}$ no singular, se dice que admite una **factorización LU** si existen matrices $L, U \in \mathbb{R}^{n \times n}$ tales que:
> $$A = L U$$
> donde $L$ es **triangular inferior unitaria** ($\ell_{ii} = 1$ para $i = 1, \dots, n$) y $U$ es **triangular superior**.

La cuestión fundamental es: ¿bajo qué condiciones existe tal descomposición y cuándo es única?

---

## Menores principales líderes

La existencia de la factorización LU está íntimamente ligada a los menores principales de la matriz.

> [!definicion]
> Para una matriz $A \in \mathbb{R}^{n \times n}$, el **menor principal líder de orden $k$**, denotado $\Delta_k$, es el determinante de la submatriz formada por las primeras $k$ filas y $k$ columnas:
> $$\Delta_k = \det(A_{1:k, 1:k}), \quad k = 1, 2, \dots, n$$
> 
> Por convención, $\Delta_0 = 1$.

> [!ejemplo]
> **Cálculo de menores principales líderes.**
> 
> Para $A = \begin{pmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{pmatrix}$:
> - $\Delta_1 = \det(2) = 2$
> - $\Delta_2 = \det\begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix} = 4 - 1 = 3$
> - $\Delta_3 = \det(A) = 2(4-1) - (-1)(-2-0) + 0 = 6 - 2 = 4$

---

## Teorema de existencia

> [!teorema]
> **Condición necesaria y suficiente para la existencia de LU.** Sea $A \in \mathbb{R}^{n \times n}$ una matriz no singular. Entonces $A$ admite una factorización $A = LU$ con $L$ triangular inferior unitaria y $U$ triangular superior **si y solo si** todos sus menores principales líderes son no nulos:
> $$\Delta_k \neq 0, \quad k = 1, 2, \dots, n-1$$
> 
> Nota: La condición $\Delta_n \neq 0$ está garantizada por la hipótesis de que $A$ es no singular.

> [!demostracion]
> **Demostración (constructiva vía eliminación Gaussiana).**
> 
> **($\Rightarrow$) Necesidad:** Supongamos que existe $A = LU$. Para cualquier $k$, las submatrices principales satisfacen:
> $$A_{1:k, 1:k} = L_{1:k, 1:k} \cdot U_{1:k, 1:k}$$
> 
> Como $L$ es triangular inferior unitaria, $\det(L_{1:k, 1:k}) = 1$. Como $U$ es triangular superior, $\det(U_{1:k, 1:k}) = \prod_{i=1}^{k} u_{ii}$.
> 
> Por tanto:
> $$\Delta_k = \det(A_{1:k, 1:k}) = \det(L_{1:k, 1:k}) \cdot \det(U_{1:k, 1:k}) = \prod_{i=1}^{k} u_{ii}$$
> 
> Para que la eliminación Gaussiana proceda sin intercambios, cada pivote $u_{ii}$ debe ser no nulo. Luego $\Delta_k = \prod_{i=1}^{k} u_{ii} \neq 0$ para $k = 1, \dots, n-1$.
> 
> **($\Leftarrow$) Suficiencia:** Supongamos que $\Delta_k \neq 0$ para $k = 1, \dots, n-1$. Construimos $L$ y $U$ mediante eliminación Gaussiana sin pivoteo.
> 
> En el paso $k$, el pivote es $a_{kk}^{(k)}$. Se puede demostrar por inducción que:
> $$a_{kk}^{(k)} = \frac{\Delta_k}{\Delta_{k-1}}$$
> 
> Como $\Delta_k \neq 0$ y $\Delta_{k-1} \neq 0$, el pivote $a_{kk}^{(k)} \neq 0$. Por tanto, la eliminación puede continuar sin intercambios hasta completar $n-1$ pasos, produciendo los factores $L$ y $U$.

> [!corolario]
> **Relación entre pivotes y menores principales.** Los pivotes $u_{kk}$ generados durante la eliminación Gaussiana sin pivoteo satisfacen:
> $$u_{kk} = \frac{\Delta_k}{\Delta_{k-1}}, \quad k = 1, 2, \dots, n$$
> 
> Esta relación es fundamental para entender por qué ciertas matrices requieren [[Pivoteo Parcial Total Estabilidad|pivoteo]].

---

## Teorema de unicidad

> [!teorema]
> **Unicidad de la factorización LU.** Si $A \in \mathbb{R}^{n \times n}$ es no singular y admite una factorización $A = LU$ con $L$ triangular inferior unitaria y $U$ triangular superior, entonces dicha factorización es **única**.

> [!demostracion]
> Supongamos que existen dos factorizaciones:
> $$A = L_1 U_1 = L_2 U_2$$
> 
> con $L_1, L_2$ triangulares inferiores unitarias y $U_1, U_2$ triangulares superiores no singulares (pues $A$ es no singular).
> 
> Multiplicando por $L_2^{-1}$ por la izquierda y $U_1^{-1}$ por la derecha:
> $$L_2^{-1} L_1 = U_2 U_1^{-1}$$
> 
> Analicemos ambos lados:
> - **Lado izquierdo:** $L_2^{-1} L_1$ es producto de triangulares inferiores unitarias, por tanto es **triangular inferior unitaria**.
> - **Lado derecho:** $U_2 U_1^{-1}$ es producto de triangulares superiores, por tanto es **triangular superior**.
> 
> La única matriz que es simultáneamente triangular inferior unitaria y triangular superior es la **matriz identidad** $I$.
> 
> Por tanto:
> $$L_2^{-1} L_1 = I \implies L_1 = L_2$$
> $$U_2 U_1^{-1} = I \implies U_1 = U_2$$
> 
> Queda demostrada la unicidad.

---

## Ejemplos y contraejemplos

> [!ejemplo]
> **Matriz que admite LU sin pivoteo.**
> 
> $$A = \begin{pmatrix} 4 & 3 \\ 6 & 3 \end{pmatrix}$$
> 
> Menores principales: $\Delta_1 = 4 \neq 0$, $\Delta_2 = 12 - 18 = -6 \neq 0$.
> 
> Factorización:
> $$L = \begin{pmatrix} 1 & 0 \\ 1.5 & 1 \end{pmatrix}, \quad U = \begin{pmatrix} 4 & 3 \\ 0 & -1.5 \end{pmatrix}$$
> 
> Verificación: $L U = \begin{pmatrix} 4 & 3 \\ 6 & 4.5 - 1.5 \end{pmatrix} = \begin{pmatrix} 4 & 3 \\ 6 & 3 \end{pmatrix} = A$.

> [!ejemplo]
> **Matriz no singular que NO admite LU sin pivoteo.**
> 
> $$A = \begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix}$$
> 
> Menores principales: $\Delta_1 = 0$.
> 
> No existe factorización $A = LU$ con $L$ unitaria. En efecto, si existiera:
> $$\begin{pmatrix} 0 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ \ell_{21} & 1 \end{pmatrix} \begin{pmatrix} u_{11} & u_{12} \\ 0 & u_{22} \end{pmatrix} = \begin{pmatrix} u_{11} & u_{12} \\ \ell_{21}u_{11} & \ell_{21}u_{12} + u_{22} \end{pmatrix}$$
> 
> De la posición $(1,1)$: $u_{11} = 0$. Entonces de $(2,1)$: $\ell_{21} \cdot 0 = 1$, ¡imposible!
> 
> **Solución:** Usar pivoteo: $P = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}$, entonces $PA = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ que sí admite LU.

> [!ejemplo]
> **Matriz singular con factorización LU no única.**
>
> $$A=\begin{pmatrix}
> 0 & 0\\
> 0 & 1
> \end{pmatrix}$$
>
> Es singular porque:
>
> $$\det(A)=0$$
>
> Factorización:
>
> $$L=\begin{pmatrix}
> 1 & 0\\
> \ell & 1
> \end{pmatrix},
> \quad
> U=\begin{pmatrix}
> 0 & 0\\
> 0 & 1
> \end{pmatrix}$$
>
> para cualquier $\ell$.
>
> Verificación:
>
> $$LU=
> \begin{pmatrix}
> 0 & 0\\
> 0 & 1
> \end{pmatrix}=A$$
>
> **Observación:** La factorización no es única.
>
> Por ejemplo:
>
> $$L_1=\begin{pmatrix}
> 1 & 0\\
> 0 & 1
> \end{pmatrix},
> \quad
> L_2=\begin{pmatrix}
> 1 & 0\\
> 7 & 1
> \end{pmatrix}$$
>
> con el mismo:
>
> $$U=\begin{pmatrix}
> 0 & 0\\
> 0 & 1
> \end{pmatrix}$$
>
> satisfacen:
>
> $$L_1U=L_2U=A$$
---

## Generalización: Factorización $P A = L U$

Cuando $\Delta_k = 0$ para algún $k < n$, la factorización $A = LU$ sin pivoteo no existe. Sin embargo, siempre existe una matriz de permutación $P$ tal que $P A$ admite factorización LU.

> [!teorema]
> **Existencia de factorización LU con pivoteo.** Para cualquier matriz no singular $A \in \mathbb{R}^{n \times n}$, existe al menos una matriz de permutación $P$ tal que $P A$ admite factorización $P A = L U$ con $L$ triangular inferior unitaria y $U$ triangular superior.
> 
> El [[Pivoteo Parcial Total Estabilidad|pivoteo parcial]] construye explícitamente dicha $P$ durante la eliminación.

> [!info]
> **Equivalencia con eliminación Gaussiana con pivoteo.** La factorización $P A = L U$ es exactamente el resultado de aplicar eliminación Gaussiana con pivoteo parcial a $A$. Los multiplicadores forman $L$, la matriz triangular resultante es $U$, y $P$ registra todos los intercambios de filas.

---

## Condiciones suficientes para $\Delta_k \neq 0$

Ciertas clases de matrices garantizan automáticamente que todos los menores principales líderes son no nulos.

> [!proposicion]
> **Clases de matrices que admiten LU sin pivoteo.**
> 
> 1. **Matrices estrictamente diagonal dominantes por filas:**
>    $$|a_{ii}| > \sum_{j \neq i} |a_{ij}|, \quad \forall i$$
>    Para estas matrices, todos los menores principales son no nulos.
> 
> 2. **Matrices simétricas definidas positivas:** Todos los menores principales líderes son positivos ($\Delta_k > 0$). Esto es la base de la [[Factorizacion Cholesky Matrices Definidas Positivas|factorización de Cholesky]].
> 
> 3. **Matrices M (M-matrices):** Matrices con $a_{ii} > 0$, $a_{ij} \leq 0$ para $i \neq j$, y que son estrictamente diagonal dominantes. Todos los menores principales son positivos.

---

## Implicaciones prácticas

El teorema de existencia y unicidad tiene consecuencias directas para el análisis numérico.

> [!warning]
> **¿Qué implica $\Delta_k \approx 0$ aunque no sea exactamente cero?** Si algún $\Delta_k$ es muy pequeño, el pivote $u_{kk} = \Delta_k / \Delta_{k-1}$ también será pequeño. Esto causa:
> 1. Multiplicadores $m_{ik} = a_{ik} / u_{kk}$ de gran magnitud.
> 2. Amplificación del [[Acumulacion Error Redondeo Gauss|error de redondeo]].
> 3. Posible [[Perdida Significancia y Cancelacion Catastrofica|pérdida de significancia]] en la actualización de filas.
> 
> El [[Pivoteo Parcial Total Estabilidad|pivoteo]] evita este problema al intercambiar filas para evitar pivotes pequeños.

> [!info]
> **Relación con el número de condición.** Aunque $\Delta_k \neq 0$ garantiza existencia, no dice nada sobre la estabilidad numérica. Una matriz puede tener todos $\Delta_k \neq 0$ pero estar mal condicionada, como la [[Matriz de Hilbert]]. En esos casos, incluso con LU sin pivoteo, la precisión será pobre debido al [[Condicionamiento Numerico Numero Condicion|mal condicionamiento]].

---

## Algoritmo de verificación de existencia

Para determinar si una matriz admite LU sin pivoteo, no es necesario calcular todos los determinantes explícitamente (costoso e inestable). Basta intentar la eliminación Gaussiana sin pivoteo.

> [!algoritmo]
> **Verificación de existencia de LU.**
> 
> ```python
> import numpy as np
> 
> def admite_LU_sin_pivoteo(A, tol=1e-12):
>     """
>     Verifica si A admite factorización LU sin pivoteo.
>     """
>     n = A.shape[0]
>     U = A.copy().astype(float)
>     
>     for k in range(n-1):
>         if abs(U[k, k]) < tol:
>             return False  # Pivote demasiado pequeño o cero
>         for i in range(k+1, n):
>             factor = U[i, k] / U[k, k]
>             U[i, k:] -= factor * U[k, k:]
>     
>     return True
> 
> # Ejemplo
> A1 = np.array([[2, -1, 0], [-1, 2, -1], [0, -1, 2]])
> A2 = np.array([[0, 1], [1, 1]])
> 
> print(f"A1 admite LU: {admite_LU_sin_pivoteo(A1)}")  # True
> print(f"A2 admite LU: {admite_LU_sin_pivoteo(A2)}")  # False
> ```