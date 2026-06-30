---
title: El Tensor de Conductividad y la Ley de Ohm
order: 1
tags:
  - analisis-tensorial
  - teoria
  - tensores
  - conductividad
draft: false
aliases:
  - tensor de conductividad
  - ley de Ohm tensorial
  - medio anisotropo
  - conductivity tensor
---

# El Tensor de Conductividad y la Ley de Ohm

> [!definicion]
> En un medio **anisótropo** la densidad de corriente $\vec J$ no es paralela al campo $\vec E$; se relacionan por el **tensor de conductividad** $\overleftrightarrow{\sigma}=\sigma_{ij}\hat e_i\hat e_j$:
> $$\vec J=\overleftrightarrow{\sigma}\cdot\vec E\qquad\Longleftrightarrow\qquad J_i=\sigma_{ij}E_j.$$
> Las bases $\hat e_i\hat e_j$ no operan entre sí: son "cajones" que emparejan las componentes $\sigma_{ij}$ con el sistema de coordenadas.

> [!info]
> Es la motivación del [[index | capítulo 4]] (libro, cap. 4.1). Muestra por qué un arreglo $[\sigma]$ no basta y hace falta la notación diádica: la matriz no guarda la base, así que pierde la información del sistema de coordenadas. La manipulación de $\overleftrightarrow{\sigma}\cdot\vec E$ usa el producto punto entre bases y la [[1 Algebra Lineal y Notacion/Simbolos Especiales/Delta Kronecker | delta de Kronecker]].

---

## Ejemplo

> [!ejemplo]
> **De la ley de Ohm escalar al tensor.** Para una resistencia, $I=V/R$. En un medio distribuido, $\vec J=\sigma\vec E$ con $\sigma$ escalar: $\vec J\parallel\vec E$. Pero un cristal puede conducir mejor en una dirección que en otra, e incluso desviar la corriente. La forma general es lineal:
> $$\begin{pmatrix}J_1\\J_2\\J_3\end{pmatrix}=\begin{pmatrix}\sigma_{11}&\sigma_{12}&\sigma_{13}\\\sigma_{21}&\sigma_{22}&\sigma_{23}\\\sigma_{31}&\sigma_{32}&\sigma_{33}\end{pmatrix}\begin{pmatrix}E_1\\E_2\\E_3\end{pmatrix},\qquad J_i=\sigma_{ij}E_j.$$
> El elemento $\sigma_{12}$ es la corriente en la dirección $1$ producida por un campo en la dirección $2$. Si solo $\sigma_{11},\sigma_{22},\sigma_{33}$ son no nulos, $\vec J\parallel\vec E$ (medio "ortótropo"); los términos fuera de la diagonal son los que **desvían** la corriente.
>
> ![[conductividad_anisotropa.svg|420]]
>
> Campo $\vec E$ aplicado y corriente $\vec J$ resultante, **no** paralela, en un medio anisótropo.

> [!ejemplo]
> **La ley de Ohm en notación diádica.** Con $\vec E=E_l\hat e_l$ y $\overleftrightarrow{\sigma}=\sigma_{jk}\hat e_j\hat e_k$, el producto punto opera entre la **segunda** base de $\overleftrightarrow{\sigma}$ y la base de $\vec E$:
> $$\vec J=\overleftrightarrow{\sigma}\cdot\vec E=\sigma_{jk}\hat e_j\hat e_k\cdot E_l\hat e_l=\sigma_{jk}E_l\,\hat e_j\,(\hat e_k\cdot\hat e_l)=\sigma_{jk}E_l\,\hat e_j\,\delta_{kl}=\sigma_{jk}E_k\,\hat e_j.$$
> Proyectando con $\hat e_i$ se recupera la componente: $J_i=\sigma_{ik}E_k$. **Paso clave:** $\hat e_k\cdot\hat e_l=\delta_{kl}$ contrae los índices y deja la primera base $\hat e_j$ como la del vector resultante.

---

## En qué consiste

> [!teoria]
> Un arreglo matricial $[\sigma]$ tiene un defecto: sus valores **dependen del sistema** elegido, pero la matriz en sí no contiene esa información (igual que las componentes de un vector dependen de la base, pero $[v]$ no la guarda). La solución es la misma que con vectores: **incorporar la base en la notación**. Así nace el tensor
> $$\overleftrightarrow{\sigma}=\sigma_{ij}\hat e_i\hat e_j=\sum_{i}\sum_{j}\sigma_{ij}\hat e_i\hat e_j.$$
> Hay $3\times3=9$ términos, cada uno con **dos** vectores base (de ahí el rango 2). Las bases cumplen cuatro funciones: separan las componentes, las emparejan con un sistema, dan el formalismo algebraico y simplifican las transformaciones entre sistemas (lo que se desarrolla en [[Transformaciones entre Sistemas/index | transformaciones]]).

> [!warning] El orden de las bases importa
> $\overleftrightarrow{\sigma}\cdot\vec E\neq\vec E\cdot\overleftrightarrow{\sigma}$ en general, porque $\hat e_j\hat e_k\cdot\hat e_l\neq\hat e_l\cdot\hat e_j\hat e_k$. El producto punto actúa sobre la base **adyacente**; por eso $\overleftrightarrow{\sigma}\cdot\vec E$ contrae la segunda base de $\sigma$ y deja la primera.

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Ley de Ohm escalar | $\vec J=\sigma\vec E$ ($\vec J\parallel\vec E$) |
> | Ley de Ohm tensorial | $J_i=\sigma_{ij}E_j$ |
> | Tensor | $\overleftrightarrow{\sigma}=\sigma_{ij}\hat e_i\hat e_j$ (rango 2, 9 comp.) |
> | Diádica vs matriz | la diádica guarda la base |
> | Producto | $\overleftrightarrow{\sigma}\cdot\vec E$ contrae la base adyacente vía $\delta_{kl}$ |

> [!corolario]
> El tensor de conductividad es el ejemplo arquetípico: relaciona linealmente dos vectores ($\vec E\to\vec J$) cuando la respuesta del medio depende de la dirección. La notación diádica $\sigma_{ij}\hat e_i\hat e_j$ —no la matriz $[\sigma]$— es la que convierte esto en un objeto geométrico independiente del sistema, base de toda la [[Notacion Tensorial y Terminologia | terminología tensorial]] y de sus [[Transformaciones entre Sistemas/index | transformaciones]].

> [!referencia]
> - Notación general de tensores: [[Notacion Tensorial y Terminologia]].
> - Cómo transforma $\sigma_{ij}$ entre sistemas: [[Transformaciones entre Sistemas/Transformaciones Tensoriales]].
> - Hallar ejes donde $\overleftrightarrow{\sigma}$ es diagonal: [[Diagonalizacion de Tensores/index]].
