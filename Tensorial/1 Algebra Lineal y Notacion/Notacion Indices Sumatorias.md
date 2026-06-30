---
title: Notación de Índices y Convenio de Einstein
order: 1
tags:
  - analisis-tensorial
  - teoria
  - notacion-indices
  - einstein
draft: false
aliases:
  - notacion de indices
  - convenio de Einstein
  - indice mudo libre
  - Einstein summation convention
  - index notation
---

# Notación de Índices y Convenio de Einstein

> [!definicion]
> Un **índice libre** aparece **una vez** por término y representa tantas ecuaciones como valores toma. Un **índice mudo** aparece **repetido** en un término y, por el **convenio de suma de Einstein**, indica suma sobre él (se omite el $\sum$):
> $$\vec{v}=\sum_{i=1}^{n}v_i\hat{e}_i\;\equiv\;v_i\hat{e}_i,\qquad c_i=a_i+b_i\ \ (i\ \text{libre}).$$

> [!info]
> Es el núcleo notacional del [[index | capítulo 1]] (libro, cap. 1.1). Trabajamos en cartesianas con base $\hat{e}_i$ ortonormal y fija. Esta notación sostiene los [[Operaciones Vectoriales/Productos Vectoriales | productos vectoriales]] y todo el [[Introduccion a Tensores/index | álgebra tensorial]]; las herramientas $\delta_{ij}$ y $\varepsilon_{ijk}$ viven en [[Simbolos Especiales/index | Símbolos Especiales]].

> [!info] Sistema cartesiano
> ![[cartesiano_base.svg|300]]
>
> Los vectores base $\hat e_1,\hat e_2,\hat e_3$ son ortonormales y de posición fija; todo vector se escribe $\vec v=v_i\hat e_i$.

---

## Ejemplo

> [!ejemplo]
> **Identificar índices libres y mudos.**
>
> - $S=a_i x_i$ → $i$ es **mudo** (aparece dos veces, se suma); $S$ no tiene índices libres → es un **escalar**.
> - $b_j=A_{ji}x_i$ → $j$ es **libre** (genera $n$ ecuaciones, $j=1,\dots,n$); $i$ es **mudo** (suma sobre las columnas).
>
> Explícitamente, para $n=2$ la segunda da dos ecuaciones:
> $$b_1=A_{11}x_1+A_{12}x_2,\qquad b_2=A_{21}x_1+A_{22}x_2,$$
> es decir, el producto matriz-vector $A\mathbf{x}$.

> [!ejemplo]
> **Doble suma numérica.** Evaluar $a_{ij}x_iy_j$ con $n=2$, $a_{ij}=i+j$, $x_i=i$, $y_j=j$ (suma sobre $i$ **y** $j$):
> $$a_{ij}x_iy_j=\sum_{i=1}^{2}\sum_{j=1}^{2}(i+j)\,i\,j.$$
> - $i=1:\ (1{+}1)(1)(1)+(1{+}2)(1)(2)=2+6=8$
> - $i=2:\ (2{+}1)(2)(1)+(2{+}2)(2)(2)=6+16=22$
>
> Total $=8+22=\mathbf{30}$. Dos índices repetidos ⇒ doble suma; el resultado es un escalar (sin índices libres).

> [!ejemplo]
> **Cambio de índice mudo (evitar colisiones).** Sustituir $y_i=a_{ij}x_j$ en $Q=b_{ij}y_ix_j$.
>
> El índice $j$ ya es mudo en $Q$: reutilizarlo en la sustitución daría $j$ **cuatro** veces (ambiguo). Se **renombra** el mudo de la sustitución a $r$:
> $$y_i=a_{ir}x_r\ \Longrightarrow\ Q=b_{ij}(a_{ir}x_r)x_j=b_{ij}a_{ir}\,x_r x_j.$$
> Ahora $i,j,r$ aparecen a lo sumo dos veces: $i$ mudo, $j$ y $r$ mudos. Cálculo sin ambigüedad.

---

## En qué consiste

> [!teoria]
> Un vector se escribe con su base: $\vec{v}=v_1\hat{e}_1+v_2\hat{e}_2+v_3\hat{e}_3$. Renombrando los ejes $(x,y,z)\to(1,2,3)$ y aplicando el convenio de Einstein,
> $$\vec{v}=\sum_{i=1}^{3}v_i\hat{e}_i\equiv v_i\hat{e}_i.$$
> El convenio supone **suma sobre todo índice repetido** en un mismo término. Una relación vectorial como $\vec{c}=\vec{a}+\vec{b}$ se vuelve $c_i=a_i+b_i$: el índice **libre** $i$ comprime tres ecuaciones en una.

> [!regla] Regla de oro de los índices
> En un término, un índice **no** debe aparecer más de **dos** veces. Si aparece tres o más, hay un conflicto: renombrar el mudo a una letra libre. Un índice mudo puede renombrarse a cualquier letra no usada —igual que la variable de integración: $\int f(x)\,dx=\int f(t)\,dt$.

> [!proposicion] Contabilidad notacional
> Los índices **libres** del lado izquierdo y del derecho de una ecuación deben **coincidir** (mismas letras, una vez cada una). Es un test de consistencia: en $a_i'=R_{ij}a_j$, el lado izquierdo tiene $i$ libre y el derecho también ($j$ se contrae) → correcto. En $\vec{a}'\neq R_{ij}a_j$ falla, porque el lado izquierdo es un vector (lleva flecha) y el derecho tiene un índice libre $i$ → son objetos distintos.

## Notación matricial y su relación

> [!info] Matrices en notación de índices
> Una matriz completa se escribe $[M]$; su elemento fila $i$, columna $j$ es $M_{ij}$. El producto de matrices $[M][N]=[P]$ es, en índices,
> $$M_{ij}N_{jk}=P_{ik},$$
> con suma implícita sobre $j$ (columnas de $M$ con filas de $N$). El índice repetido $j$ está en **segunda** posición de $M$ y **primera** de $N$: ese orden es lo que distingue un producto matricial.

> [!warning] Vector como arreglo: $\rightarrow$, no $=$
> Un vector puede representarse como matriz columna, pero se escribe con flecha:
> $$\vec{v}\rightarrow[v]=\begin{bmatrix}v_1\\v_2\\v_3\end{bmatrix}.$$
> Se usa $\rightarrow$ y **no** $=$ porque el arreglo $[v]$ **no contiene la información de la base** $\hat{e}_i$. Dos vectores con las mismas componentes en bases distintas tienen el mismo $[v]$ pero son vectores diferentes. La igualdad $\vec{v}=v_i\hat{e}_i$ sí es completa (incluye la base).

## Producto de matrices y asociatividad

> [!ejemplo]
> **Producto $M_{ij}N_{jk}$ elemento a elemento.** Sean, con $n=2$,
> $$[M]=\begin{bmatrix}1&2\\0&1\end{bmatrix},\qquad [N]=\begin{bmatrix}3&1\\2&4\end{bmatrix}.$$
> El producto $P_{ik}=M_{ij}N_{jk}$ suma sobre el índice mudo $j=1,2$ (segunda posición de $M$, primera de $N$):
> - $P_{11}=M_{11}N_{11}+M_{12}N_{21}=1\cdot3+2\cdot2=7$
> - $P_{12}=M_{11}N_{12}+M_{12}N_{22}=1\cdot1+2\cdot4=9$
> - $P_{21}=M_{21}N_{11}+M_{22}N_{21}=0\cdot3+1\cdot2=2$
> - $P_{22}=M_{21}N_{12}+M_{22}N_{22}=0\cdot1+1\cdot4=4$
>
> $$[P]=\begin{bmatrix}7&9\\2&4\end{bmatrix}.$$
> Solo los índices libres $i$ (fila) y $k$ (columna) sobreviven; $j$ se contrae.

> [!teorema] Asociatividad del producto matricial
> El producto de matrices escrito en índices es **asociativo**:
> $$(AB)C=A(BC),$$
> es decir, ambas agrupaciones dan la misma matriz de componentes $A_{ij}B_{jk}C_{kl}$.

> [!demostracion]
> **Paso 1 — Agrupar como $(AB)C$.** Primero $A_{ij}B_{jk}=(AB)_{ik}$ (suma sobre $j$); luego se multiplica por $C$ contrayendo $k$:
> $$[(AB)C]_{il}=(AB)_{ik}\,C_{kl}=\big(A_{ij}B_{jk}\big)\,C_{kl}=A_{ij}B_{jk}C_{kl}.$$
>
> **Paso 2 — Agrupar como $A(BC)$.** Primero $B_{jk}C_{kl}=(BC)_{jl}$ (suma sobre $k$); luego se multiplica por $A$ contrayendo $j$:
> $$[A(BC)]_{il}=A_{ij}\,(BC)_{jl}=A_{ij}\,\big(B_{jk}C_{kl}\big)=A_{ij}B_{jk}C_{kl}.$$
>
> **Paso 3 — Comparar.** Ambas rutas terminan en la **misma** expresión $A_{ij}B_{jk}C_{kl}$ con sumas sobre $j$ y $k$. Por el convenio de Einstein esas sumas son ordinarias de números, y la suma es conmutativa y asociativa: el orden en que se agrupen $\sum_j$ y $\sum_k$ no altera el resultado. Por tanto
> $$[(AB)C]_{il}=A_{ij}B_{jk}C_{kl}=[A(BC)]_{il}\;\Longrightarrow\;(AB)C=A(BC).\qquad\blacksquare$$
> La asociatividad matricial, laboriosa de probar con matrices explícitas, es inmediata en índices: el paréntesis solo decide qué suma se hace primero, y eso es irrelevante.

## Resumen

> [!resumen]
> | Concepto | Definición | Ejemplo |
> |---|---|---|
> | Índice libre | aparece 1 vez; tantas ecuaciones como valores | $i$ en $c_i=a_i+b_i$ |
> | Índice mudo | aparece 2 veces; se suma sobre él | $i$ en $S=a_ix_i$ |
> | Convenio Einstein | omite el $\sum$ del índice repetido | $v_i\hat{e}_i$ |
> | Regla de oro | un índice $\le 2$ veces por término | renombrar mudo si colisiona |
> | Producto matricial | $M_{ij}N_{jk}=P_{ik}$ | suma sobre $j$ |
> | Asociatividad | $(AB)C=A(BC)=A_{ij}B_{jk}C_{kl}$ | el paréntesis solo elige qué suma va antes |
> | Vector como arreglo | $\vec{v}\rightarrow[v]$ (flecha, no $=$) | la base no está en $[v]$ |

> [!corolario]
> Toda la potencia del capítulo cabe en dos reglas: **índice repetido = suma** e **índices libres deben casar a ambos lados**. Con ellas, las tres ecuaciones de una suma vectorial se vuelven una, y la contabilidad de índices se convierte en un detector de errores automático. Esta notación es el alfabeto del resto del curso.

> [!referencia]
> - Objetos del álgebra lineal en esta notación: [[Algebra Lineal para Tensores]].
> - Primeros usos (rotación, productos): [[Operaciones Vectoriales/index]].
> - Símbolos que la acompañan: [[Simbolos Especiales/Delta Kronecker]] · [[Simbolos Especiales/Simbolo Levi-Civita]].
