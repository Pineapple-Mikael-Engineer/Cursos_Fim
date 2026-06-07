---
title: Álgebra Lineal para Tensores
tags:
  - analisis-tensorial
  - teoria
  - notacion-indices
  - matrices
draft: false
aliases:
  - algebra lineal para tensores
  - vectores y matrices en indices
  - producto de matrices en indices
  - Linear algebra for tensors
  - matrix product index notation
---

# Álgebra Lineal para Tensores

> [!definicion]
> Un vector se escribe $\vec{v}=v_i\hat{e}_i$ y se **representa** como arreglo columna $\vec{v}\rightarrow[v]$ (con $\rightarrow$, no $=$). Una **matriz** completa es $[M]$; su elemento de la fila $i$, columna $j$ es $M_{ij}$. El **producto de matrices** $[M][N]=[P]$ es, en índices,
> $$M_{ij}N_{jk}=P_{ik},$$
> con suma implícita sobre $j$ (columnas de $M$ contra filas de $N$).

> [!info]
> Es la pieza de **álgebra de matrices** del [[index | capítulo 1]] (libro, cap. 1.1), apoyada en la [[Notacion Indices Sumatorias | notación de índices]]. Trabajamos en cartesianas con base $\hat{e}_i$ ortonormal y fija. Su primer uso intensivo son las [[Operaciones Vectoriales/index | operaciones vectoriales]] (rotación, punto, cruz). El producto $M_{ij}N_{jk}=P_{ik}$ es el patrón que reaparece en todo el álgebra tensorial.

---

## Ejemplo

> [!ejemplo]
> **Producto matriz-matriz $2\times 2$ con $M_{ij}N_{jk}=P_{ik}$.** Sean
> $$[M]=\begin{bmatrix}1&2\\3&4\end{bmatrix},\qquad [N]=\begin{bmatrix}5&6\\7&8\end{bmatrix}.$$
> Cada elemento $P_{ik}$ se obtiene sumando sobre el índice mudo $j$ (que recorre $1,2$):
> $$P_{ik}=M_{ij}N_{jk}=M_{i1}N_{1k}+M_{i2}N_{2k}.$$
> - $P_{11}=M_{11}N_{11}+M_{12}N_{21}=1\cdot5+2\cdot7=19$
> - $P_{12}=M_{11}N_{12}+M_{12}N_{22}=1\cdot6+2\cdot8=22$
> - $P_{21}=M_{21}N_{11}+M_{22}N_{21}=3\cdot5+4\cdot7=43$
> - $P_{22}=M_{21}N_{12}+M_{22}N_{22}=3\cdot6+4\cdot8=50$
>
> $$[P]=\begin{bmatrix}19&22\\43&50\end{bmatrix}.$$
> El índice mudo $j$ ocupa la **segunda** posición de $M$ y la **primera** de $N$: ese orden es la firma de un producto matricial.

> [!ejemplo]
> **Producto matriz-vector $A\vec{x}$.** Una transformación lineal $b_i=A_{ij}x_j$ con
> $$[A]=\begin{bmatrix}2&1\\0&3\end{bmatrix},\qquad [x]=\begin{bmatrix}1\\4\end{bmatrix}.$$
> El índice libre $i$ genera una ecuación por fila; $j$ es mudo:
> - $b_1=A_{1j}x_j=A_{11}x_1+A_{12}x_2=2\cdot1+1\cdot4=6$
> - $b_2=A_{2j}x_j=A_{21}x_1+A_{22}x_2=0\cdot1+3\cdot4=12$
>
> $$[b]=\begin{bmatrix}6\\12\end{bmatrix}.$$
> Es el mismo patrón $M_{ij}N_{jk}=P_{ik}$ con un vector ($k$ desaparece porque la columna es única).

---

## En qué consiste

> [!teoria]
> **Vector.** Un vector tridimensional se expresa con su base:
> $$\vec{v}=v_x\hat{e}_x+v_y\hat{e}_y+v_z\hat{e}_z=v_1\hat{e}_1+v_2\hat{e}_2+v_3\hat{e}_3=v_i\hat{e}_i,$$
> donde las $v_i$ son las componentes **cartesianas** y $\hat{e}_i$ los vectores base ortonormales. La igualdad $\vec{v}=v_i\hat{e}_i$ es completa: incluye la base.
>
> **Matriz.** Un arreglo bidimensional $[M]$ tiene elemento genérico $M_{ij}$, **fila $i$, columna $j$**:
> $$[M]=\begin{bmatrix}M_{11}&M_{12}&\cdots&M_{1c}\\M_{21}&M_{22}&\cdots&M_{2c}\\\vdots&\vdots&\ddots&\vdots\\M_{r1}&M_{r2}&\cdots&M_{rc}\end{bmatrix}.$$
> El primer índice es la fila, el segundo la columna; $r$ no tiene por qué ser igual a $c$.

> [!proposicion] Producto de matrices
> El producto $[M][N]=[P]$ existe si el nº de columnas de $M$ iguala el nº de filas de $N$. En índices:
> $$\boxed{M_{ij}N_{jk}=P_{ik}}$$
> con suma implícita sobre $j$ (Einstein). El índice mudo $j$ está en **segunda** posición de $M$ y **primera** de $N$; los índices libres $i$ (fila del resultado) y $k$ (columna del resultado) sobreviven. Es la expresión del elemento $ik$-ésimo de $[P]$. A diferencia de la notación matricial, **el orden de los factores escritos no importa** en índices ($M_{ij}N_{jk}=N_{jk}M_{ij}$): son números, y la posición del índice lleva la información.

## Vector como arreglo: columna, fila y traspuesta

> [!warning] $\rightarrow$, no $=$
> Un vector puede representarse como matriz **columna** $(3\times1)$ o **fila** $(1\times3)$:
> $$\vec{v}\rightarrow[v]=\begin{bmatrix}v_1\\v_2\\v_3\end{bmatrix}\qquad\text{o}\qquad\vec{v}\rightarrow[v]^\dagger=\begin{bmatrix}v_1&v_2&v_3\end{bmatrix}.$$
> Se usa $\rightarrow$ y **no** $=$ porque el arreglo $[v]$ **no contiene la base** $\hat{e}_i$: un mismo $\vec{v}$ tiene infinitas representaciones $[v]$, una por cada base. La notación $[v]^\dagger$ indica la **traspuesta** de $[v]$ (intercambio de filas por columnas): convierte la columna en fila.

> [!info] Para qué fila vs columna
> La distinción importa al multiplicar: un producto punto se escribe $\vec{A}\cdot\vec{B}\rightarrow[A]^\dagger[B]$ (fila por columna $\to$ escalar), y una rotación admite tanto $[a']=[R][a]$ (columnas) como $[a']^\dagger=[a]^\dagger[R]^\dagger$ (filas). En notación de índices esa contabilidad de fila/columna queda absorbida por la posición de los subíndices, y deja de ser un cuidado aparte.

## Resumen

> [!resumen]
> | Objeto | Notación de índices | Arreglo |
> |---|---|---|
> | Vector | $\vec{v}=v_i\hat{e}_i$ | $\vec{v}\rightarrow[v]$ (columna) |
> | Componente | $v_i$ | $i$-ésima entrada |
> | Matriz | $[M]$, elemento $M_{ij}$ | fila $i$, columna $j$ |
> | Producto matriz-matriz | $M_{ij}N_{jk}=P_{ik}$ | suma sobre $j$ |
> | Producto matriz-vector | $b_i=A_{ij}x_j$ | $A\vec{x}$ |
> | Traspuesta (fila) | $[v]^\dagger$ | columna $\to$ fila |

> [!corolario]
> Todo el álgebra de matrices de este capítulo se reduce a un patrón: **índice mudo en segunda-primera posición = producto matricial** ($M_{ij}N_{jk}$). La distinción fila/columna y el cuidado del orden de factores, centrales en notación matricial, se vuelven contabilidad automática de subíndices. Esta es la razón por la que la notación de índices simplifica el álgebra lineal antes de tocar tensores.

> [!referencia]
> - Reglas de índice mudo/libre y convenio de Einstein: [[Notacion Indices Sumatorias]].
> - Primeros productos con esta notación: [[Operaciones Vectoriales/index]].
> - Las herramientas $\delta_{ij}$ y $\varepsilon_{ijk}$ que aparecen al multiplicar bases: [[Simbolos Especiales/Delta Kronecker]] · [[Simbolos Especiales/Simbolo Levi-Civita]].
