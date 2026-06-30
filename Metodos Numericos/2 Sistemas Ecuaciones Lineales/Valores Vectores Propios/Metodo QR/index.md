---
title: Método QR
order: 3
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - autovalores
  - metodo-qr
  - index
draft: false
aliases:
  - Algoritmo QR
  - QR algorithm
  - Iteración QR
---

# Método QR

> [!definicion]
> El **método QR** es el algoritmo estándar para calcular **todos** los autovalores de una matriz $A \in \mathbb{R}^{n\times n}$. Genera una sucesión de matrices semejantes $A = A_0, A_1, A_2, \dots$ mediante factorizaciones $A_k = Q_k R_k$ y recomposición $A_{k+1} = R_k Q_k$, que converge a una forma triangular (o cuasi-triangular) cuya diagonal son los autovalores.

> [!info]
> Frente al [[Metodo Potencia Directo/index|método de la potencia]], que extrae un solo autovalor (el dominante), el método QR obtiene el espectro completo. Es el motor de las rutinas `eig` de LAPACK/MATLAB/NumPy. Esta sección lo descompone en sus tres piezas: las transformaciones ortogonales, la iteración básica y las aceleraciones por desplazamiento.

---

## Semejanza ortogonal: la idea unificadora

> [!teoria]
> Cada paso del método QR es una **transformación de semejanza ortogonal**, que preserva los autovalores:
> $$A_{k+1} = R_k Q_k = Q_k^T (Q_k R_k) Q_k = Q_k^T A_k Q_k.$$
> Como $A_{k+1}$ es semejante a $A_k$ vía la matriz ortogonal $Q_k$, comparten espectro. La sucesión $\{A_k\}$ converge a una forma triangular superior (matrices generales: forma de Schur real cuasi-triangular), revelando los autovalores en la diagonal.

---

## Las tres piezas del algoritmo

> [!info]
> **Transformaciones de Householder.** La factorización $A = QR$ se construye con reflexiones ortogonales que anulan columnas por debajo de la diagonal, de forma numéricamente estable. Se desarrollan en [[Fundamentos Transformaciones Householder]].

> [!info]
> **Iteración QR.** La repetición factorizar–recomponer $A_k = Q_kR_k \to A_{k+1} = R_kQ_k$, su reducción previa a forma de Hessenberg y la convergencia a forma triangular se tratan en [[Iteracion QR Descomposicion]].

> [!info]
> **Desplazamientos.** La aceleración mediante desplazamientos espectrales $A_k - \mu_k I$, que llevan la convergencia de lineal a cuadrática/cúbica, está en [[Convergencia y Desplazamientos]].

---

## Ejemplo: una iteración QR

> [!ejemplo]
> **Primer paso sobre una matriz simétrica.** Sea
> $$A_0 = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}, \quad \text{autovalores } 3 \text{ y } 1.$$
> Su factorización $A_0 = Q_0 R_0$ y la recomposición dan
> $$A_1 = R_0 Q_0 = \begin{pmatrix} 2.8 & 0.6 \\ 0.6 & 1.2 \end{pmatrix},$$
> cuya diagonal $(2.8,\,1.2)$ ya se acerca a los autovalores $(3,1)$. Iterando, los elementos fuera de la diagonal tienden a cero como $|\lambda_2/\lambda_1|^k = (1/3)^k$ y la diagonal converge al espectro.

---

## Comparación con el método de la potencia

> [!info]
> | | [[Metodo Potencia Directo/index\|Potencia]] | Método QR |
> |:---|:---|:---|
> | Autovalores | solo el dominante | todos |
> | Costo | $O(k\,n^2)$ | $O(n^3)$ (con reducción a Hessenberg) |
> | Idea | amplificar $v_1$ | semejanzas ortogonales iteradas |
> | Conexión | — | QR ≈ potencia simultánea sobre todos los modos |

> [!teoria]
> El método QR equivale conceptualmente a aplicar el método de la potencia a **todos** los modos a la vez, manteniéndolos ortogonales en cada paso (relación con la [[Iteracion Simultanea|iteración simultánea]]). Por eso revela el espectro completo en lugar de un solo autovalor.

---

## Resumen

| Pieza | Nota |
|:---|:---|
| Reflexiones ortogonales | [[Fundamentos Transformaciones Householder]] |
| Iteración factorizar–recomponer | [[Iteracion QR Descomposicion]] |
| Aceleración por desplazamiento | [[Convergencia y Desplazamientos]] |

> [!corolario]
> El método QR calcula el espectro completo de una matriz mediante transformaciones de semejanza ortogonal $A_{k+1} = Q_k^T A_k Q_k$ que preservan los autovalores y convergen a una forma triangular. Se construye sobre tres pilares: las [[Fundamentos Transformaciones Householder|reflexiones de Householder]] que dan factorizaciones estables, la [[Iteracion QR Descomposicion|iteración básica]] reducida a forma de Hessenberg, y los [[Convergencia y Desplazamientos|desplazamientos espectrales]] que aceleran la convergencia. Es el algoritmo de referencia para el problema de autovalores y la base de las rutinas `eig` de las bibliotecas numéricas modernas.
