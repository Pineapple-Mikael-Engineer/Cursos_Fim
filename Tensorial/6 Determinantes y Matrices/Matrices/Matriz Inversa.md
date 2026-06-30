---
title: Matriz Inversa
order: 2
tags:
  - analisis-tensorial
  - teoria
  - matrices
  - inversa
draft: false
aliases:
  - inversa
  - matriz inversa
  - Gauss-Jordan
  - matriz singular
  - matrix inverse
---

# Matriz Inversa $\mathsf{A}^{-1}$

> [!definicion]
> La **inversa** de una matriz cuadrada $\mathsf{A}$ es la matriz $\mathsf{A}^{-1}$ que deshace su acción:
> $$\mathsf{A}\mathsf{A}^{-1}=\mathsf{A}^{-1}\mathsf{A}=\mathsf{1}.$$
> Existe **si y solo si** $\|\mathsf{A}\|\neq0$. Si $\|\mathsf{A}\|=0$ la matriz es **singular** y no tiene inversa.

> [!info]
> Parte final de la sección **6.2** del [[../index | capítulo 6]] (Rogan & Muñoz). $\mathsf{A}^{-1}$ es la transformación que restablece los ejes originales (p. ej. deshacer una rotación). El criterio $\|\mathsf{A}\|\neq0$ enlaza con [[../Determinantes]], y la inversa de un producto $(\mathsf{A}\mathsf{B})^{-1}=\mathsf{B}^{-1}\mathsf{A}^{-1}$ con [[Operaciones Basicas]].

---

## Ejemplo

> [!ejemplo] Inversión por Gauss-Jordan paso a paso
> Invertir $\displaystyle\mathsf{A}=\begin{pmatrix}3&2&1\\2&3&1\\1&1&4\end{pmatrix}$ ($\|\mathsf{A}\|=18\neq0$). Se escribe $[\mathsf{A}\,|\,\mathsf{1}]$ y se opera por filas hasta llegar a $[\mathsf{1}\,|\,\mathsf{A}^{-1}]$.
>
> **Paso 1.** Punto de partida:
> $$\left(\begin{array}{ccc}3&2&1\\2&3&1\\1&1&4\end{array}\right)\quad\left(\begin{array}{ccc}1&0&0\\0&1&0\\0&0&1\end{array}\right).$$
>
> **Paso 2.** Cada fila se multiplica para hacer $a_{k1}=1$ en su pivote inicial (fila 1 por $\tfrac13$, fila 2 por $\tfrac12$):
> $$\left(\begin{array}{ccc}1&\tfrac23&\tfrac13\\1&\tfrac32&\tfrac12\\1&1&4\end{array}\right)\quad\left(\begin{array}{ccc}\tfrac13&0&0\\0&\tfrac12&0\\0&0&1\end{array}\right).$$
>
> **Paso 3.** Se resta la fila 1 de la fila 2 y de la fila 3 (se anula la primera columna debajo del pivote):
> $$\left(\begin{array}{ccc}1&\tfrac23&\tfrac13\\0&\tfrac56&\tfrac16\\0&\tfrac13&\tfrac{11}{3}\end{array}\right)\quad\left(\begin{array}{ccc}\tfrac13&0&0\\-\tfrac13&\tfrac12&0\\-\tfrac13&0&1\end{array}\right).$$
>
> **Paso 4.** Se divide la fila 2 por $\tfrac56$; luego se resta $\tfrac23$ de la fila 1 y $\tfrac13$ de la fila 3 (se limpia la segunda columna):
> $$\left(\begin{array}{ccc}1&0&\tfrac15\\0&1&\tfrac15\\0&0&\tfrac{18}{5}\end{array}\right)\quad\left(\begin{array}{ccc}\tfrac35&-\tfrac25&0\\-\tfrac25&\tfrac35&0\\-\tfrac15&-\tfrac15&1\end{array}\right).$$
>
> **Paso 5.** Se divide la fila 3 por $\tfrac{18}{5}$ y, como último paso, se resta $\tfrac15$ de la fila 3 a cada una de las dos primeras filas (se limpia la tercera columna). El bloque izquierdo queda $\mathsf{1}$ y el derecho es $\mathsf{A}^{-1}$:
> $$\left(\begin{array}{ccc}1&0&0\\0&1&0\\0&0&1\end{array}\right)\quad\mathsf{A}^{-1}=\left(\begin{array}{ccc}\tfrac{11}{18}&-\tfrac{7}{18}&-\tfrac1{18}\\[2pt]-\tfrac{7}{18}&\tfrac{11}{18}&-\tfrac1{18}\\[2pt]-\tfrac1{18}&-\tfrac1{18}&\tfrac{5}{18}\end{array}\right).$$
>
> **Verificación** $\mathsf{A}\mathsf{A}^{-1}=\mathsf{1}$, fila 1 de $\mathsf{A}$ por columna 1 de $\mathsf{A}^{-1}$:
> $$3\cdot\tfrac{11}{18}+2\cdot(-\tfrac{7}{18})+1\cdot(-\tfrac1{18})=\tfrac{33-14-1}{18}=\tfrac{18}{18}=1,$$
> y los elementos fuera de la diagonal dan $0$ (p. ej. $3\cdot(-\tfrac7{18})+2\cdot\tfrac{11}{18}+1\cdot(-\tfrac1{18})=\tfrac{-21+22-1}{18}=0$). $\checkmark$

> [!warning] Errata del texto
> La ecuación (6.56) del libro imprime $\tfrac{11}{8}$ en la esquina superior izquierda; el valor correcto es $\tfrac{11}{18}$ (la inversa es simétrica porque $\mathsf{A}$ lo es, y solo así $\mathsf{A}\mathsf{A}^{-1}=\mathsf{1}$).

---

## Métodos de inversión

> [!proposicion] Fórmula por cofactores
> $$a^{-1}_{ij}=\frac{C_{ji}}{\|\mathsf{A}\|},$$
> con $C_{ji}=(-1)^{j+i}M_{ji}$ el [[../Determinantes | cofactor]] (nótese el **intercambio de índices** $ji$: es la transpuesta de la matriz de cofactores, la adjunta clásica). Hace explícito que la inversa existe solo si $\|\mathsf{A}\|\neq0$, pero es **inviable** para matrices grandes (requiere $\sim n^2$ determinantes de orden $n-1$).

> [!algoritmo] Gauss-Jordan (método recomendado)
> Resuelve $\mathsf{M}_L\,\mathsf{A}=\mathsf{1}$, donde $\mathsf{M}_L=\mathsf{A}^{-1}$ es el producto de las operaciones elementales de fila. Como $\mathsf{M}_L\,\mathsf{1}=\mathsf{M}_L$, basta aplicar a $\mathsf{1}$ las **mismas** operaciones que reducen $\mathsf{A}$ a $\mathsf{1}$:
> 1. Escribir el bloque aumentado $[\mathsf{A}\,|\,\mathsf{1}]$.
> 2. Operaciones elementales de fila permitidas: (a) multiplicar una fila por una constante, (b) restar a una fila un múltiplo de otra, (c) intercambiar filas.
> 3. Reducir el bloque izquierdo a $\mathsf{1}$ (pivotes a $1$, ceros arriba y abajo).
> 4. El bloque derecho es $\mathsf{A}^{-1}$.
>
> Bien adaptado al cómputo, igual que la eliminación de Gauss para sistemas.

## Resumen

> [!resumen]
> | Concepto | Resultado |
> |---|---|
> | Definición | $\mathsf{A}\mathsf{A}^{-1}=\mathsf{A}^{-1}\mathsf{A}=\mathsf{1}$ |
> | Existencia | solo si $\|\mathsf{A}\|\neq0$; si $\|\mathsf{A}\|=0$, **singular** |
> | Cofactores | $a^{-1}_{ij}=C_{ji}/\|\mathsf{A}\|$ |
> | Gauss-Jordan | $[\mathsf{A}\,\|\,\mathsf{1}]\to[\mathsf{1}\,\|\,\mathsf{A}^{-1}]$ |
> | Producto | $(\mathsf{A}\mathsf{B})^{-1}=\mathsf{B}^{-1}\mathsf{A}^{-1}$; $\|\mathsf{A}^{-1}\|=1/\|\mathsf{A}\|$ |

> [!corolario]
> La inversa deshace el operador y existe exactamente cuando $\|\mathsf{A}\|\neq0$. La fórmula por cofactores la define teóricamente, pero el cálculo real se hace por **Gauss-Jordan**: reducir $[\mathsf{A}\,|\,\mathsf{1}]$ a $[\mathsf{1}\,|\,\mathsf{A}^{-1}]$ con operaciones de fila, robusto y mecanizable.

> [!referencia]
> - El criterio $\|\mathsf{A}\|\neq0$ y la eliminación de Gauss: [[../Determinantes]].
> - Inversa de un producto y transpuesta: [[Operaciones Basicas]].
> - Marco general del álgebra matricial: [[index]].
