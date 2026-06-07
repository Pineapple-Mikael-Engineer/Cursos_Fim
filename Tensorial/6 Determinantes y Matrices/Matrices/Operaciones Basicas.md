---
title: Operaciones Basicas con Matrices
tags:
  - analisis-tensorial
  - teoria
  - matrices
  - operaciones
draft: false
aliases:
  - operaciones con matrices
  - producto matricial
  - conmutador
  - transpuesta
  - matrix operations
---

# Operaciones Basicas con Matrices

> [!definicion]
> Con matrices $\mathsf{A},\mathsf{B}$ de elementos $a_{ij},b_{ij}$ y un escalar $\alpha$:
> - **Suma:** $(\mathsf{A}+\mathsf{B})_{ij}=a_{ij}+b_{ij}$ (mismo tamaño).
> - **Escalar:** $(\alpha\mathsf{A})_{ij}=\alpha\,a_{ij}$ (cada elemento).
> - **Producto:** $\mathsf{A}\mathsf{B}=\mathsf{C}$ con $\displaystyle c_{ij}=\sum_k a_{ik}b_{kj}$ (producto punto fila$_i$ de $\mathsf{A}$ por columna$_j$ de $\mathsf{B}$; columnas de $\mathsf{A}$ = filas de $\mathsf{B}$).
> - **Transpuesta:** $(\tilde{\mathsf{A}})_{ik}=a_{ki}$ (intercambio filas$\leftrightarrow$columnas).

> [!info]
> Sección **6.2** del [[../index | capítulo 6]] (Rogan & Muñoz). Son las reglas que hacen de las matrices un [[index | anillo]]. El producto matricial codifica la **composición de operadores lineales**: si $x'=\mathsf{A}x$ y $x''=\mathsf{B}x'$, entonces $x''=(\mathsf{B}\mathsf{A})x$. La inversa de estas operaciones se trata en [[Matriz Inversa]].

---

## Ejemplo

> [!ejemplo]
> **El producto no conmuta (matrices de Pauli).** Con
> $$\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\qquad \sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix},$$
> el elemento $(\sigma_1\sigma_3)_{ij}=\sum_k(\sigma_1)_{ik}(\sigma_3)_{kj}$ da
> $$\sigma_1\sigma_3=\begin{pmatrix}0&1\\1&0\end{pmatrix}\begin{pmatrix}1&0\\0&-1\end{pmatrix}=\begin{pmatrix}0&-1\\1&0\end{pmatrix},$$
> mientras que
> $$\sigma_3\sigma_1=\begin{pmatrix}1&0\\0&-1\end{pmatrix}\begin{pmatrix}0&1\\1&0\end{pmatrix}=\begin{pmatrix}0&1\\-1&0\end{pmatrix}=-\,\sigma_1\sigma_3.$$
> Luego $\sigma_1\sigma_3=-\sigma_3\sigma_1$: **anticonmutan**, y el conmutador $[\sigma_1,\sigma_3]=\sigma_1\sigma_3-\sigma_3\sigma_1=\begin{pmatrix}0&-2\\2&0\end{pmatrix}\neq\mathsf{0}$.

---

## Producto matricial y no conmutatividad

> [!teorema] No conmutatividad
> En general $\mathsf{A}\mathsf{B}\neq\mathsf{B}\mathsf{A}$. La falla se mide con el **conmutador**
> $$[\mathsf{A},\mathsf{B}]=\mathsf{A}\mathsf{B}-\mathsf{B}\mathsf{A},$$
> que es $\mathsf{0}$ si y solo si las matrices conmutan.

> [!demostracion] $\sigma_1\sigma_3\neq\sigma_3\sigma_1$
> **Paso 1.** Elemento $(\sigma_1\sigma_3)_{ij}=\sum_k(\sigma_1)_{ik}(\sigma_3)_{kj}$. La fila $1$ de $\sigma_1$ es $(0,1)$; multiplicada por las columnas de $\sigma_3$ da $(0,-1)$. La fila $2$ de $\sigma_1$ es $(1,0)$; da $(1,0)$. Así
> $$\sigma_1\sigma_3=\begin{pmatrix}0&-1\\1&0\end{pmatrix}.$$
> **Paso 2.** Ahora $(\sigma_3\sigma_1)_{ij}=\sum_k(\sigma_3)_{ik}(\sigma_1)_{kj}$. La fila $1$ de $\sigma_3$ es $(1,0)$ $\to(0,1)$; la fila $2$ es $(0,-1)$ $\to(-1,0)$. Así
> $$\sigma_3\sigma_1=\begin{pmatrix}0&1\\-1&0\end{pmatrix}.$$
> **Paso 3.** Comparando, $\sigma_3\sigma_1=-\sigma_1\sigma_3$, luego $[\sigma_1,\sigma_3]=2\,\sigma_1\sigma_3\neq\mathsf{0}$. La no conmutatividad es **estructural** del producto, no un accidente numérico. $\blacksquare$

> [!warning] Divisores de cero
> El producto puede ser nulo sin que lo sea ninguno de los factores. Con
> $$\mathsf{A}=\begin{pmatrix}1&1\\0&0\end{pmatrix},\quad \mathsf{B}=\begin{pmatrix}1&0\\-1&0\end{pmatrix}\ \Rightarrow\ \mathsf{A}\mathsf{B}=\mathsf{0}.$$
> Por eso las matrices forman un **anillo** (con divisores de cero), no un cuerpo: no se puede "dividir" libremente.

---

## Propiedades y notación

> [!proposicion] Reglas del álgebra
> | Operación | Propiedad |
> |---|---|
> | Suma | conmutativa $\mathsf{A}+\mathsf{B}=\mathsf{B}+\mathsf{A}$, asociativa, neutro $\mathsf{0}$ |
> | Escalar | $\alpha\mathsf{A}=\mathsf{A}\alpha$ (conmuta con escalares) |
> | Producto | asociativo $(\mathsf{A}\mathsf{B})\mathsf{C}=\mathsf{A}(\mathsf{B}\mathsf{C})$; **no** conmutativo |
> | Distributiva | $\mathsf{A}(\mathsf{B}+\mathsf{C})=\mathsf{A}\mathsf{B}+\mathsf{A}\mathsf{C}$ |
> | Unidad | $\mathsf{1}\,\mathsf{A}=\mathsf{A}\,\mathsf{1}=\mathsf{A}$, con $(\mathsf{1})_{ij}=\delta_{ij}$ |

> [!proposicion] Transpuesta e inversa de un producto
> Ambas **invierten el orden** de los factores:
> $$\widetilde{\mathsf{A}\mathsf{B}}=\tilde{\mathsf{B}}\,\tilde{\mathsf{A}},\qquad (\mathsf{A}\mathsf{B})^{-1}=\mathsf{B}^{-1}\mathsf{A}^{-1}.$$
> La segunda se verifica con $\mathsf{A}\mathsf{B}\,\mathsf{B}^{-1}\mathsf{A}^{-1}=\mathsf{A}\,\mathsf{1}\,\mathsf{A}^{-1}=\mathsf{1}$.

> [!teorema] Teorema del producto (determinantes)
> El determinante del producto es el producto de los determinantes:
> $$\|\mathsf{A}\mathsf{B}\|=\|\mathsf{A}\|\,\|\mathsf{B}\|.$$
> En particular $\|\mathsf{A}\mathsf{B}\|=\|\mathsf{B}\mathsf{A}\|$ aunque $\mathsf{A}\mathsf{B}\neq\mathsf{B}\mathsf{A}$, y $\|\mathsf{A}^{-1}\|=1/\|\mathsf{A}\|$.

## Resumen

> [!resumen]
> | Operación | Definición |
> |---|---|
> | Suma | $(\mathsf{A}+\mathsf{B})_{ij}=a_{ij}+b_{ij}$, conmutativa |
> | Escalar | $(\alpha\mathsf{A})_{ij}=\alpha a_{ij}$ |
> | Producto | $c_{ij}=\sum_k a_{ik}b_{kj}$, **no** conmutativo |
> | Conmutador | $[\mathsf{A},\mathsf{B}]=\mathsf{A}\mathsf{B}-\mathsf{B}\mathsf{A}$ |
> | Transpuesta | $(\tilde{\mathsf{A}})_{ik}=a_{ki}$; $\widetilde{\mathsf{A}\mathsf{B}}=\tilde{\mathsf{B}}\tilde{\mathsf{A}}$ |
> | Inversa producto | $(\mathsf{A}\mathsf{B})^{-1}=\mathsf{B}^{-1}\mathsf{A}^{-1}$ |
> | Determinante | $\|\mathsf{A}\mathsf{B}\|=\|\mathsf{A}\|\|\mathsf{B}\|$ |

> [!corolario]
> El producto matricial es la composición de operadores: por eso es asociativo y distributivo pero **no** conmutativo, como muestran las matrices de Pauli al anticonmutar. Transpuesta e inversa de un producto invierten el orden de los factores, y el determinante respeta el producto. Estas reglas son el motor de cálculo de [[../Matrices Ortogonales]], [[../Matrices Hermiticas y Unitarias]] y de la [[Matriz Inversa]].

> [!referencia]
> - El marco de anillo y la traza: [[index]].
> - Inversión de matrices: [[Matriz Inversa]].
> - Propiedades de $\|\mathsf{A}\|$: [[../Determinantes]].
