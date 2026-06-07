---
title: Rotación de Vectores
tags:
  - analisis-tensorial
  - teoria
  - notacion-indices
  - rotacion
draft: false
aliases:
  - rotacion de vectores
  - matriz de rotacion
  - rotacion 2D
  - Vector rotation
  - rotation matrix
---

# Rotación de Vectores

> [!definicion]
> Al rotar un vector $\vec{a}$ un ángulo $\phi$ en sentido antihorario en el plano, sus componentes se transforman con la **matriz de rotación**
> $$[R(\phi)]=\begin{bmatrix}\cos\phi&-\operatorname{sen}\phi\\\operatorname{sen}\phi&\cos\phi\end{bmatrix},\qquad [a']=[R(\phi)][a],$$
> que en notación de Einstein se escribe $a_i'=R_{ij}a_j$ (suma sobre $j$). La rotación cambia la orientación pero **no la magnitud** de $\vec{a}$.

> [!info]
> Es la operación 1.2.1 del libro, dentro de [[index | Operaciones Vectoriales]] del [[../index | capítulo 1]]. Usa el [[Algebra Lineal para Tensores | producto matriz-vector]] $b_i=A_{ij}x_j$ y la [[Notacion Indices Sumatorias | contabilidad de índices]]. Que la rotación conserva la magnitud se demuestra en [[Calculos con Notacion Einstein]] usando la ortogonalidad $R_{ru}R_{rv}=\delta_{uv}$.

---

## Ejemplo

> [!ejemplo]
> **Rotar un vector 90° antihorario.** Sea $\vec{a}=3\hat{e}_1+1\hat{e}_2$, es decir $[a]=\begin{bmatrix}3\\1\end{bmatrix}$. Con $\phi=90^\circ$: $\cos90^\circ=0$, $\operatorname{sen}90^\circ=1$, luego
> $$[R(90^\circ)]=\begin{bmatrix}0&-1\\1&0\end{bmatrix}.$$
> Aplicando $a_i'=R_{ij}a_j$ (suma sobre $j$):
> - $a_1'=R_{11}a_1+R_{12}a_2=0\cdot3+(-1)\cdot1=-1$
> - $a_2'=R_{21}a_1+R_{22}a_2=1\cdot3+0\cdot1=3$
>
> $$[a']=\begin{bmatrix}-1\\3\end{bmatrix},\qquad \vec{a}\,'=-\hat{e}_1+3\hat{e}_2.$$
> Verificación de magnitud: $\lvert\vec{a}\rvert=\sqrt{3^2+1^2}=\sqrt{10}$ y $\lvert\vec{a}\,'\rvert=\sqrt{(-1)^2+3^2}=\sqrt{10}$. Coinciden, como debe ser. Geométricamente, $90^\circ$ antihorario lleva $(3,1)$ a $(-1,3)$.

---

## En qué consiste

> [!teoria]
> Partimos de $\vec{a}$ orientado un ángulo $\theta$ respecto al eje-1, escrito en componentes cartesianas
> $$\vec{a}=a_1\hat{e}_1+a_2\hat{e}_2,\qquad a_1=a\cos\theta,\quad a_2=a\operatorname{sen}\theta,$$
> con $a=\lvert\vec{a}\rvert=\sqrt{a_1^2+a_2^2}$. El vector rotado $\vec{a}\,'$ se obtiene **girando $\vec{a}$ un ángulo $\phi$** antihorario, lo que suma $\phi$ al ángulo total sin cambiar la magnitud:
> $$\vec{a}\,'=\underbrace{a\cos(\theta+\phi)}_{a_1'}\hat{e}_1+\underbrace{a\operatorname{sen}(\theta+\phi)}_{a_2'}\hat{e}_2.$$

> [!teorema] Forma de la matriz de rotación
> $$[R(\phi)]=\begin{bmatrix}\cos\phi&-\operatorname{sen}\phi\\\operatorname{sen}\phi&\cos\phi\end{bmatrix}.$$

> [!demostracion]
> **Paso 1 — Expandir con la suma de ángulos.** Aplicando las identidades del coseno y seno de una suma a $a_1'$ y $a_2'$:
> $$a_1'=a\cos(\theta+\phi)=\underbrace{a\cos\theta}_{a_1}\cos\phi-\underbrace{a\operatorname{sen}\theta}_{a_2}\operatorname{sen}\phi,$$
> $$a_2'=a\operatorname{sen}(\theta+\phi)=\underbrace{a\cos\theta}_{a_1}\operatorname{sen}\phi+\underbrace{a\operatorname{sen}\theta}_{a_2}\cos\phi.$$
>
> **Paso 2 — Reconocer $a_1,a_2$.** Sustituyendo $a_1=a\cos\theta$ y $a_2=a\operatorname{sen}\theta$ queda un sistema lineal en las componentes originales:
> $$a_1'=a_1\cos\phi-a_2\operatorname{sen}\phi,\qquad a_2'=a_1\operatorname{sen}\phi+a_2\cos\phi.$$
>
> **Paso 3 — Forma matricial.** Representando $\vec{a}\rightarrow[a]$ y $\vec{a}\,'\rightarrow[a']$ como columnas, el sistema es
> $$\begin{bmatrix}a_1'\\a_2'\end{bmatrix}=\begin{bmatrix}\cos\phi&-\operatorname{sen}\phi\\\operatorname{sen}\phi&\cos\phi\end{bmatrix}\begin{bmatrix}a_1\\a_2\end{bmatrix}\;\Longrightarrow\;[a']=[R(\phi)][a],$$
> de donde se lee $[R(\phi)]$. $\blacksquare$

> [!proposicion] Forma en notación de Einstein
> Las mismas manipulaciones se logran en índices. El producto $[a']=[R(\phi)][a]$ suma sobre las columnas de $[R]$, lo que en índices es la suma implícita sobre $j$:
> $$a_i'=R_{ij}a_j.$$
> A diferencia de la notación matricial, **el orden de los factores no importa** aquí: $R_{ij}a_j=a_jR_{ij}$, porque son números y la información va en la posición del subíndice. Incluyendo las bases, el vector rotado completo es $\vec{a}\,'=R_{ij}a_j\hat{e}_i$. La contabilidad notacional confirma la consistencia: en $a_i'=R_{ij}a_j$ el lado izquierdo tiene $i$ libre y el derecho también ($j$ se contrae).

> [!info] Versión con filas
> Si se representan $[a]$ y $[a']$ como matrices **fila**, hay que usar las traspuestas y posmultiplicar:
> $$[a']^\dagger=[a]^\dagger[R(\phi)]^\dagger,\qquad [a_1'\ \ a_2']=[a_1\ \ a_2]\begin{bmatrix}\cos\phi&\operatorname{sen}\phi\\-\operatorname{sen}\phi&\cos\phi\end{bmatrix},$$
> enteramente equivalente a la versión con columnas. En índices esta distinción desaparece.

## Resumen

> [!resumen]
> | Aspecto | Expresión |
> |---|---|
> | Vector original | $\vec{a}=a_1\hat{e}_1+a_2\hat{e}_2$, $a_1=a\cos\theta$, $a_2=a\operatorname{sen}\theta$ |
> | Componentes rotadas | $a_1'=a_1\cos\phi-a_2\operatorname{sen}\phi$, $a_2'=a_1\operatorname{sen}\phi+a_2\cos\phi$ |
> | Matriz de rotación | $[R(\phi)]=\begin{bmatrix}\cos\phi&-\operatorname{sen}\phi\\\operatorname{sen}\phi&\cos\phi\end{bmatrix}$ |
> | Forma matricial | $[a']=[R(\phi)][a]$ |
> | Forma Einstein | $a_i'=R_{ij}a_j$; con base $\vec{a}\,'=R_{ij}a_j\hat{e}_i$ |

> [!corolario]
> La rotación es el primer ejemplo donde la notación de Einstein muestra su economía: una sola expresión $a_i'=R_{ij}a_j$ resume el sistema $2\times2$ (o $3\times3$) y libera del cuidado de filas/columnas y del orden de factores. Que esta transformación **preserva la magnitud** ($\vec{a}\,'\cdot\vec{a}\,'=\vec{a}\cdot\vec{a}$) es consecuencia de la ortogonalidad $R_{ru}R_{rv}=\delta_{uv}$, y se prueba en [[Calculos con Notacion Einstein]].

> [!referencia]
> - Producto matriz-vector que sustenta $a_i'=R_{ij}a_j$: [[Algebra Lineal para Tensores]].
> - Invariancia de la magnitud bajo rotación: [[Calculos con Notacion Einstein]].
> - Delta de Kronecker (ortogonalidad $R_{ru}R_{rv}=\delta_{uv}$): [[Simbolos Especiales/Delta Kronecker]].
