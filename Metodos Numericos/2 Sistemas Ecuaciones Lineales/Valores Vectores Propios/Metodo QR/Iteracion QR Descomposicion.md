---
title: Iteración QR y Descomposición
order: 2
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - autovalores
  - metodo-qr
draft: false
aliases:
  - Iteración QR
  - QR iteration
  - Forma de Hessenberg
---

# Iteración QR y Descomposición

> [!definicion]
> La **iteración QR** genera, a partir de $A_0 = A$, la sucesión de matrices semejantes
> $$A_k = Q_k R_k \quad(\text{factorización}), \qquad A_{k+1} = R_k Q_k \quad(\text{recomposición}),$$
> donde $Q_k$ es ortogonal y $R_k$ triangular superior. La sucesión $\{A_k\}$ converge a una forma triangular cuya diagonal son los autovalores de $A$.

> [!info]
> Es el núcleo del [[Metodo QR/index|método QR]]. Cada paso es una [[Fundamentos Transformaciones Householder|transformación ortogonal]] que preserva el espectro; la novedad es que repetirla *ordena* la matriz hacia la forma triangular sin destruir los autovalores.

---

## Preservación del espectro

> [!teorema]
> Cada $A_{k+1}$ es **ortogonalmente semejante** a $A_k$, y por tanto a $A$:
> $$A_{k+1} = R_k Q_k = (Q_k^T Q_k) R_k Q_k = Q_k^T (Q_k R_k) Q_k = Q_k^T A_k Q_k.$$
> En consecuencia $A_{k+1}$ y $A_k$ tienen los **mismos autovalores**, y la diagonal de $A_k$ los aproxima cada vez mejor.

> [!demostracion]
> De $A_k = Q_k R_k$ se despeja $R_k = Q_k^T A_k$ (porque $Q_k^TQ_k = I$). Sustituyendo en la recomposición:
> $$A_{k+1} = R_k Q_k = Q_k^T A_k Q_k.$$
> La semejanza con matriz ortogonal preserva autovalores (mismo polinomio característico), y al ser $Q_k$ ortogonal también preserva normas y simetría: si $A$ es simétrica, todas las $A_k$ lo son.

---

## Convergencia a forma triangular

> [!teorema]
> Si $A$ tiene autovalores de módulos distintos $|\lambda_1| > |\lambda_2| > \cdots > |\lambda_n|$, la iteración QR (sin desplazamiento) converge a forma triangular superior, con
> $$(A_k)_{ij} \to 0 \quad (i > j), \qquad (A_k)_{ii} \to \lambda_i,$$
> y las entradas subdiagonales decaen como
> $$|(A_k)_{i+1,i}| = O\!\left(\left|\frac{\lambda_{i+1}}{\lambda_i}\right|^k\right).$$

> [!info]
> La iteración QR equivale a aplicar el [[Metodo Potencia Directo/index|método de la potencia]] simultáneamente a todos los modos manteniéndolos ortogonales (relación con la [[Iteracion Simultanea|iteración simultánea]]). De ahí que cada subdiagonal converja a la tasa del par de autovalores que separa, $|\lambda_{i+1}/\lambda_i|$.

---

## Reducción previa a forma de Hessenberg

> [!teoria]
> La iteración QR directa cuesta $O(n^3)$ **por paso**, inviable. La solución es reducir primero $A$ a forma de **Hessenberg superior** $H$ (ceros bajo la primera subdiagonal) por semejanza de [[Fundamentos Transformaciones Householder|Householder]]:
> $$A = U H U^T, \qquad H_{ij} = 0 \text{ si } i > j+1.$$
> La forma de Hessenberg es **invariante** bajo la iteración QR (cada $A_k$ sigue siendo Hessenberg), y un paso QR sobre Hessenberg cuesta solo $O(n^2)$. Para matrices simétricas, la forma de Hessenberg es **tridiagonal**, y el paso baja a $O(n)$.

> [!algoritmo]
> **Método QR práctico (esquema).**
>
> ```
> H = reducir_a_Hessenberg(A)          // O(n³), una sola vez, por Householder
> mientras no convergido:
>     elegir desplazamiento μ            // ver Convergencia y Desplazamientos
>     H - μI = Q R                       // factorización QR de Hessenberg (Givens), O(n²)
>     H = R Q + μ I                      // recomposición, sigue siendo Hessenberg
>     si |H[i+1, i]| < tol·(|H[i,i]|+|H[i+1,i+1]|):
>         H[i+1, i] = 0                  // deflación: se aísla un autovalor
> autovalores = diagonal(H)             // bloques 1×1 (reales) y 2×2 (pares complejos)
> ```

---

## Ejemplo: convergencia de la subdiagonal

> [!ejemplo]
> **Iteración QR sin desplazamiento sobre $A_0 = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$** (autovalores $3$ y $1$, $|\lambda_2/\lambda_1| = 1/3$):
>
> | $k$ | $(A_k)_{11}$ | $(A_k)_{22}$ | subdiagonal $(A_k)_{21}$ |
> |:---:|:---:|:---:|:---:|
> | 0 | 2.000 | 2.000 | 1.000 |
> | 1 | 2.800 | 1.200 | 0.600 |
> | 2 | 2.953 | 1.047 | 0.213 |
> | 3 | 2.995 | 1.005 | 0.071 |
> | 4 | 2.999 | 1.001 | 0.024 |
>
> La subdiagonal decae como $(1/3)^k$ y la diagonal converge a $(3, 1)$. El desplazamiento acelera drásticamente este decaimiento, como se ve en [[Convergencia y Desplazamientos]].

---

## Para matrices generales: forma de Schur real

> [!warning]
> Si $A$ tiene autovalores **complejos** (en pares conjugados, al ser $A$ real), la iteración QR real no converge a triangular estricta: lo hace a una **forma de Schur real cuasi-triangular**, con bloques $2\times2$ en la diagonal cuyos autovalores son los pares complejos. La diagonal por bloques sigue revelando todo el espectro.

---

## Relación con otras notas

> [!info]
> - Las reflexiones que construyen cada $Q_k$ y la reducción a Hessenberg: [[Fundamentos Transformaciones Householder]].
> - La aceleración por desplazamiento, esencial en la práctica: [[Convergencia y Desplazamientos]].
> - La interpretación como potencia simultánea: [[Iteracion Simultanea]] y [[Metodo Potencia Directo/index]].
> - Panorama y comparación: [[Metodo QR/index]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Iteración | $A_k = Q_kR_k \to A_{k+1} = R_kQ_k$ |
| Semejanza | $A_{k+1} = Q_k^T A_k Q_k$ (preserva espectro) |
| Límite | triangular (Schur real si hay complejos) |
| Tasa subdiagonal | $|\lambda_{i+1}/\lambda_i|^k$ |
| Coste por paso | $O(n^2)$ en Hessenberg, $O(n)$ tridiagonal |

> [!corolario]
> La iteración QR transforma $A$ por semejanzas ortogonales sucesivas $A_{k+1} = Q_k^T A_k Q_k$ que preservan el espectro y conducen la matriz hacia su forma triangular (o de Schur real), revelando los autovalores en la diagonal. Su viabilidad práctica depende de reducir primero a forma de Hessenberg —invariante bajo la iteración— para abaratar cada paso de $O(n^3)$ a $O(n^2)$. Sin desplazamiento, las subdiagonales decaen lentamente como $|\lambda_{i+1}/\lambda_i|^k$; la aceleración decisiva llega con los [[Convergencia y Desplazamientos|desplazamientos espectrales]].
