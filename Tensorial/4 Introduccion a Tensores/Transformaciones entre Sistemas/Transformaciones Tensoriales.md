---
title: Transformaciones Tensoriales
order: 3
tags:
  - analisis-tensorial
  - teoria
  - tensores
  - transformaciones
draft: false
aliases:
  - transformaciones tensoriales
  - ley de transformacion de un tensor
  - definicion operativa de tensor
  - tensor transformations
---

# Transformaciones Tensoriales

> [!definicion]
> Un tensor de rango 2 es el mismo objeto en ambos sistemas, $\overleftrightarrow{T}=T_{ij}\hat e_i\hat e_j=T'_{rs}\hat e'_r\hat e'_s$. Sus componentes se relacionan con **un factor $a$ por índice**:
> $$T'_{lm}=T_{rs}\,a_{lr}a_{ms},\qquad T_{lm}=T'_{rs}\,a_{rl}a_{sm}.$$
> En general, un tensor de rango $r$ transforma como
> $$T'_{ijk\dots}=T_{rst\dots}\,a_{ir}a_{js}a_{kt}\dots$$
> **Esta es la definición operativa de tensor:** un arreglo de números es un tensor de rango $r$ si, y solo si, sus componentes obedecen esta ley.

> [!info]
> Es la sección **4.3.4** del [[index | capítulo 4.3]] (libro, cap. 4.3.4). Aplica la [[Matriz de Transformacion | matriz $[a]$]] una vez por cada índice del tensor, extendiendo la ley vectorial $v'_i=a_{ij}v_j$. Es la sección que justifica por qué el [[../Tensor Conductividad y Ley de Ohm | tensor de conductividad]] $\sigma_{ij}$ es un objeto geométrico genuino y no un arreglo arbitrario.

---

## Ejemplo

> [!ejemplo]
> **Transformar un tensor de rango 2.** Sea, en 2D, el tensor diagonal con matriz $[T]=\begin{pmatrix}3&0\\0&1\end{pmatrix}$ y un sistema primado rotado $\theta_0=90^\circ$, $[a]=\begin{pmatrix}0&1\\-1&0\end{pmatrix}$ (de $\cos90^\circ=0$, $\operatorname{sen}90^\circ=1$). Usando $T'_{lm}=a_{lr}a_{ms}T_{rs}$, en forma matricial $[T']=[a][T][a]^\dagger$:
> $$[T']=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\begin{pmatrix}3&0\\0&1\end{pmatrix}\begin{pmatrix}0&-1\\1&0\end{pmatrix}=\begin{pmatrix}0&1\\-3&0\end{pmatrix}\begin{pmatrix}0&-1\\1&0\end{pmatrix}=\begin{pmatrix}1&0\\0&3\end{pmatrix}.$$
> Al rotar $90^\circ$ los ejes, las direcciones $1$ y $2$ se intercambian, y con ellas los autovalores $3$ y $1$ en la diagonal. La **traza** ($3+1=4$) y el **determinante** ($3$) se conservan: son invariantes de la transformación.

> [!ejemplo]
> **Mezclar bases es legítimo.** La ley de Ohm $\vec J=\overleftrightarrow{\sigma}\cdot\vec E$ puede evaluarse con $\overleftrightarrow{\sigma}$ en el sistema primado y $\vec E$ en el no primado (libro 4.51–4.53). Con $\overleftrightarrow{\sigma}=\sigma'_{jk}\hat e'_j\hat e'_k$ y $\vec E=E_l\hat e_l$:
> $$J_i\hat e_i=(\sigma'_{jk}\hat e'_j\hat e'_k)\cdot(E_l\hat e_l)=\sigma'_{jk}E_l\,\hat e'_j\,(\hat e'_k\cdot\hat e_l)=\sigma'_{jk}E_l\,\hat e'_j\,a_{kl}.$$
> El producto punto entre bases **mixtas** da $\hat e'_k\cdot\hat e_l=a_{kl}\neq\delta_{kl}$, y aun así el cálculo es válido **siempre que se respete el orden de las bases**. Esto es imposible con la notación matricial sin convertir todo a una sola base primero: es la ventaja de la notación diádica.

---

## En qué consiste

> [!teorema] Ley de transformación de un tensor de rango 2
> $$T_{lm}=T'_{rs}\,a_{rl}a_{sm},\qquad T'_{lm}=T_{rs}\,a_{lr}a_{ms}.$$

> [!demostracion]
> Partimos de que el tensor es el mismo objeto en ambos sistemas (libro 4.47):
> $$\overleftrightarrow{T}=T_{ij}\hat e_i\hat e_j=T'_{rs}\hat e'_r\hat e'_s.$$
> La idea es aplicar **dos veces** el producto punto, uno por cada índice, usando $\hat e_l\cdot\hat e_i=\delta_{li}$ y $\hat e_l\cdot\hat e'_r=a_{rl}$ (de $a_{rl}=\hat e'_r\cdot\hat e_l$).
>
> **Paso 1 — Producto punto por la izquierda con $\hat e_l$.**
> $$\hat e_l\cdot T_{ij}\hat e_i\hat e_j=\hat e_l\cdot T'_{rs}\hat e'_r\hat e'_s\ \Longrightarrow\ T_{ij}(\hat e_l\cdot\hat e_i)\hat e_j=T'_{rs}(\hat e_l\cdot\hat e'_r)\hat e'_s.$$
>
> **Paso 2 — Contraer el primer índice.** Con $\hat e_l\cdot\hat e_i=\delta_{li}$ y $\hat e_l\cdot\hat e'_r=a_{rl}$,
> $$T_{ij}\delta_{li}\hat e_j=T'_{rs}a_{rl}\hat e'_s\ \Longrightarrow\ T_{lj}\hat e_j=T'_{rs}a_{rl}\hat e'_s.$$
>
> **Paso 3 — Segundo producto punto con $\hat e_m$.** Repitiendo el proceso sobre la base restante, con $\hat e_m\cdot\hat e_j=\delta_{mj}$ y $\hat e_m\cdot\hat e'_s=a_{sm}$,
> $$T_{lj}\delta_{mj}=T'_{rs}a_{rl}a_{sm}\ \Longrightarrow\ T_{lm}=T'_{rs}\,a_{rl}a_{sm}.$$
>
> **Paso 4 — Inversa.** Para invertir se aplica la matriz inversa dos veces; como $a^{-1}_{ij}=a_{ji}$ en sistemas ortonormales, se obtiene
> $$T'_{lm}=T_{rs}\,a_{lr}a_{ms}.\qquad\blacksquare$$

> [!proposicion] Generalización a rango $r$
> Cada índice aporta un factor $a$. Para un tensor de rango $r$,
> $$T'_{ijk\dots}=T_{rst\dots}\,a_{ir}a_{js}a_{kt}\dots,\qquad T_{ijk\dots}=T'_{rst\dots}\,a_{ri}a_{sj}a_{tk}\dots$$
> **Patrón de índices** (como en [[Matriz de Transformacion]]): al ir del sistema **no primado al primado** se suma siempre sobre el **segundo** subíndice de cada $a$; al volver, sobre el **primero**. Un escalar (rango 0) lleva cero factores: es invariante. Un vector (rango 1) lleva uno: $v'_i=a_{ij}v_j$.

> [!info] Esta ley *es* la definición de tensor
> Al contrario que con la notación matricial —donde todos los términos deben estar en la misma base—, la notación diádica/tensorial **permite mezclar bases** (ejemplo de Ohm arriba), porque las bases viajan dentro de la expresión. Además contiene toda la información para transformar de un sistema a otro. Por eso un tensor es un objeto de **coordenadas independientes**, geométrico, tal como lo es un vector: lo que lo identifica no son sus $3^r$ componentes sino que estas obedezcan $T'=T\,a\,a\dots$

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Invariante | $\overleftrightarrow{T}=T_{ij}\hat e_i\hat e_j=T'_{rs}\hat e'_r\hat e'_s$ |
> | Rango 2 (directa) | $T'_{lm}=T_{rs}\,a_{lr}a_{ms}$ |
> | Rango 2 (inversa) | $T_{lm}=T'_{rs}\,a_{rl}a_{sm}$ |
> | Matricial | $[T']=[a][T][a]^\dagger$ |
> | Rango $r$ | $T'_{ijk\dots}=T_{rst\dots}\,a_{ir}a_{js}a_{kt}\dots$ |
> | Definición de tensor | un arreglo es tensor sii obedece esta ley |
> | Mezclar bases | válido en notación diádica ($\hat e'_k\cdot\hat e_l=a_{kl}$) |

> [!corolario]
> La ley $T'_{ijk\dots}=T_{rst\dots}a_{ir}a_{js}a_{kt}\dots$ —un factor $a$ por índice— es la **definición operativa** de tensor y el criterio para reconocer uno. Generaliza sin sorpresas la transformación vectorial: el procedimiento (producto punto por cada base, contrayendo con $\delta$ o con $a$) es el mismo, repetido tantas veces como el rango. Buscar el sistema donde esta ley deja a $[T]$ diagonal es el objetivo de la [[../Diagonalizacion de Tensores/index | diagonalización]].

> [!referencia]
> - La matriz $[a]$ que se aplica por índice: [[Matriz de Transformacion]].
> - El tensor físico de ejemplo: [[../Tensor Conductividad y Ley de Ohm]].
> - Hallar ejes donde $[T]$ es diagonal: [[../Diagonalizacion de Tensores/index]].
> - Generalización a bases curvilíneas: [[Transformaciones en Curvilineas]].
