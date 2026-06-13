---
title: Operaciones con Tensores
tags:
  - analisis-tensorial
  - teoria
  - tensores
  - contraccion
draft: false
aliases:
  - operaciones tensoriales
  - contraccion de indices
  - producto interno tensorial
  - traza de un tensor
  - tensor operations
---

# Operaciones con Tensores

> [!definicion]
> El álgebra tensorial tiene cuatro operaciones básicas:
> - **Suma** (solo entre tensores del **mismo rango**): componente a componente, $S_{ij\dots}+T_{ij\dots}$.
> - **Producto externo / diádico**: yuxtaposición; los rangos **se suman** ($p+q$).
> - **Contracción**: igualar dos índices y sumar sobre ellos; **baja el rango en 2**. Para rango 2, $T_{ii}$ es la **traza** (un escalar).
> - **Producto interno / punto**: contrae las bases adyacentes de dos tensores; equivale a *producto externo seguido de una contracción*.

> [!info]
> Es el álgebra del [[index | capítulo 4]], apoyada en la [[Notacion Tensorial y Terminologia | notación diádica]]. La contracción usa la [[1 Algebra Lineal y Notacion/Simbolos Especiales/Delta Kronecker | delta de Kronecker]] ($\hat e_k\cdot\hat e_l=\delta_{kl}$) y el convenio de Einstein de [[1 Algebra Lineal y Notacion/Notacion Indices Sumatorias | índices y sumatorias]]. El producto punto $\overleftrightarrow{\sigma}\cdot\vec E$ de la [[Tensor Conductividad y Ley de Ohm | ley de Ohm]] es el caso guía.

---

## Ejemplo

> [!ejemplo]
> **Suma de dos tensores de rango 2.** Solo se suman tensores del mismo rango, componente a componente:
> $$[S]=\begin{pmatrix}1&2&0\\0&1&3\\1&0&2\end{pmatrix},\quad [T]=\begin{pmatrix}0&1&1\\2&0&0\\1&1&1\end{pmatrix}\;\Rightarrow\;[S]+[T]=\begin{pmatrix}1&3&1\\2&1&3\\2&1&3\end{pmatrix}.$$
> Componente a componente, $(S+T)_{ij}=S_{ij}+T_{ij}$. **No** tiene sentido sumar un rango 2 con un vector (rango 1): faltarían/sobrarían bases.

> [!ejemplo]
> **Contracción de un rango 2: la traza.** Contraer $T_{ij}$ sobre $i=j$ significa poner el mismo índice y sumar (Einstein):
> $$T_{ii}=T_{11}+T_{22}+T_{33}.$$
> Para el $[T]$ anterior: $T_{ii}=0+0+1=1$. El resultado no tiene índices libres $\Rightarrow$ es un **escalar** (rango $2-2=0$), la **traza** $\operatorname{tr}\overleftrightarrow{T}$.

> [!ejemplo]
> **Contraer un rango 3 da un vector.** Sea $T_{ijk}$ (rango 3, $3^3=27$ componentes). Contrayéndolo sobre $j=k$:
> $$V_i=T_{ijj}=T_{i11}+T_{i22}+T_{i33}.$$
> Queda **un** índice libre ($i$) $\Rightarrow$ rango $3-2=1$, un **vector** $\vec V=V_i\hat e_i$. Numéricamente, si para $i=1$ se tiene $T_{111}=2,\;T_{122}=1,\;T_{133}=-1$, entonces $V_1=2+1-1=2$.

> [!ejemplo]
> **Producto punto $\overleftrightarrow{\sigma}\cdot\vec E$ como contracción.** Con $\overleftrightarrow{\sigma}=\sigma_{jk}\hat e_j\hat e_k$ y $\vec E=E_l\hat e_l$, el punto opera entre la base **adyacente** ($\hat e_k$ de $\sigma$ y $\hat e_l$ de $E$):
> $$\vec J=\overleftrightarrow{\sigma}\cdot\vec E=\sigma_{jk}E_l\,\hat e_j(\hat e_k\cdot\hat e_l)=\sigma_{jk}E_l\,\hat e_j\,\delta_{kl}=\sigma_{jk}E_k\,\hat e_j,$$
> de donde $J_i=\sigma_{ik}E_k$. El rango total pasa de $2+1=3$ (producto externo $\sigma_{jk}E_l$) a $3-2=1$ tras la contracción $k=l$: un **vector**. Ver [[Tensor Conductividad y Ley de Ohm]].

---

## En qué consiste

> [!teoria]
> Las cuatro operaciones se distinguen por lo que hacen al **rango**. La **suma** lo conserva (y exige rango igual). El **producto externo** lo *sube* (suma los rangos). La **contracción** lo *baja en 2* (elimina dos bases). El **producto interno** es la combinación de las dos últimas: yuxtaponer (externo) y luego identificar la base adyacente (contracción). Por eso $\overleftrightarrow{\sigma}\cdot\vec E$ baja de rango $3$ a rango $1$.

> [!definicion] Contracción
> Dado un tensor de rango $n\ge2$, **contraer** un par de índices es igualarlos y sumar sobre ellos (Einstein). Operacionalmente, el producto punto de las dos bases correspondientes introduce un $\delta$ que las colapsa:
> $$T_{\dots i \dots i \dots}\quad\Rightarrow\quad \text{rango}=n-2.$$
> Cada contracción elimina **dos** índices/bases (un par), de ahí que el rango baje en 2.

> [!proposicion] Producto interno = externo + contracción
> El producto interno de dos tensores es su producto externo seguido de **una** contracción sobre el par de índices de las bases adyacentes. Si los rangos son $p$ y $q$, el producto interno tiene rango $p+q-2$.

> [!teorema] La traza $T_{ii}$ es un invariante
> Para un tensor de rango 2, la contracción $T_{ii}$ (la traza) es un **escalar**: su valor es el mismo en todo sistema de coordenadas obtenido por rotación.

> [!demostracion]
> **Paso 1.** Bajo una rotación de matriz ortogonal $a_{ij}$, un tensor de rango 2 transforma con un factor $a$ por índice:
> $$T'_{ij}=a_{ir}\,a_{js}\,T_{rs}.$$
>
> **Paso 2.** Contraer poniendo $i=j$ y sumar (calcular la traza en el sistema primado):
> $$T'_{ii}=a_{ir}\,a_{is}\,T_{rs}.$$
>
> **Paso 3.** Usar la **ortogonalidad** de la matriz de rotación, $a_{ir}a_{is}=\delta_{rs}$ (las columnas son ortonormales):
> $$T'_{ii}=\delta_{rs}\,T_{rs}.$$
>
> **Paso 4.** La delta de Kronecker contrae $s\to r$:
> $$T'_{ii}=T_{rr}=T_{ii}.$$
> La traza es la misma antes y después de rotar: es **invariante**. $\blacksquare$

> [!info] Resumen de operaciones y su efecto sobre el rango
> | Operación | Notación | Efecto en el rango | Restricción |
> |---|---|---|---|
> | Suma | $S_{ij\dots}+T_{ij\dots}$ | conserva | mismo rango |
> | Producto externo | $T_{ij\dots}\,U_{kl\dots}$ | $p+q$ | — |
> | Contracción | $T_{\dots i\dots i\dots}$ | $n-2$ | rango $\ge2$ |
> | Producto interno | $\overleftrightarrow{T}\cdot\overleftrightarrow{U}$ | $p+q-2$ | bases adyacentes |

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Suma | componente a componente, **mismo rango** |
> | Producto externo | rangos se suman ($p+q$) |
> | Contracción | rango $n\to n-2$ (un par de índices) |
> | Traza | $T_{ii}=T_{11}+T_{22}+T_{33}$, escalar invariante |
> | Producto interno | externo + contracción $\Rightarrow p+q-2$ |
> | $\overleftrightarrow{\sigma}\cdot\vec E$ | contrae vía $\delta_{kl}$, da $J_i=\sigma_{ik}E_k$ |

> [!corolario]
> El rango es la magnitud que ordena el álgebra tensorial: la suma lo conserva, el producto externo lo sube, la contracción lo baja en 2 y el producto interno combina ambos. La traza $T_{ii}$ —una contracción— produce el primer **invariante** de un tensor, anticipo de los invariantes que revela la [[Diagonalizacion de Tensores/index | diagonalización]].

> [!referencia]
> - Rango y producto externo: [[Notacion Tensorial y Terminologia]].
> - Producto punto base-a-base y $\delta_{kl}$: [[1 Algebra Lineal y Notacion/Simbolos Especiales/Delta Kronecker | delta de Kronecker]].
> - Cómo transforma (ley de transformación, ortogonalidad de $a_{ij}$): [[Transformaciones entre Sistemas/index]].
