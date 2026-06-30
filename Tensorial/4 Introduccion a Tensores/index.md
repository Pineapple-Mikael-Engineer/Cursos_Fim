---
title: Introducción a Tensores
order: 5
tags:
  - analisis-tensorial
  - teoria
  - tensores
  - index
draft: false
aliases:
  - introduccion a tensores
  - capitulo 4 tensorial
  - tensor de rango n
  - tensors
---

# Introducción a Tensores

> [!definicion]
> Un **tensor** de rango $n$ es un objeto geométrico con $n$ índices y $n$ vectores base, escrito en notación diádica
> $$\overleftrightarrow{T}=T_{ijk\dots}\,\hat e_i\hat e_j\hat e_k\dots$$
> Lo que lo define **no** son sus componentes (que cambian con el sistema) sino su **ley de transformación**: un tensor es "un objeto que transforma como un tensor". Un vector es un tensor de rango 1; un escalar, de rango 0.

> [!info]
> Es el **capítulo 4** del libro (Rogan & Muñoz, Parte I). Trabaja en cartesianas ortonormales (luego se generaliza a curvilíneas). Se desglosa en:
> - [[Tensor Conductividad y Ley de Ohm]] — la motivación física (cap. 4.1).
> - [[Notacion Tensorial y Terminologia]] — notación diádica, rango, producto externo (cap. 4.2).
> - [[Operaciones con Tensores]] — suma, producto diádico, contracción.
> - [[Transformaciones entre Sistemas/index | Transformaciones entre Sistemas]] — cómo cambian las componentes (cap. 4.3).
> - [[Diagonalizacion de Tensores/index | Diagonalización de Tensores]] — valores y vectores propios (cap. 4.4).
> - [[Pseudo-objetos/index | Pseudo-objetos]] — vectores/escalares/tensores axiales (cap. 4.6).

---

## Ejemplo

> [!ejemplo]
> **Por qué hace falta un tensor.** En un medio isótropo la ley de Ohm es $\vec J=\sigma\vec E$ con $\sigma$ **escalar**: la corriente es paralela al campo. Pero en un cristal anisótropo la corriente puede fluir en una dirección distinta a $\vec E$. Eso exige relacionar dos vectores por un objeto de **nueve** componentes:
> $$J_i=\sigma_{ij}E_j,$$
> donde $\sigma_{ij}$ es el **tensor de conductividad**. Los términos fuera de la diagonal ($\sigma_{12}$, etc.) describen corriente en la dirección $1$ por un campo en la dirección $2$. Un tensor es, en esencia, la **máquina lineal** que convierte un vector en otro. Ver [[Tensor Conductividad y Ley de Ohm]].

---

## En qué consiste

> [!teoria]
> La notación diádica $\overleftrightarrow{\sigma}=\sigma_{ij}\hat e_i\hat e_j$ tiene dos virtudes sobre la matriz $[\sigma]$: (1) incluye la **base**, así que las ecuaciones pueden mezclar sistemas de coordenadas; (2) hace **mecánica** la ley de transformación. El **rango** de un tensor es el número de índices = número de vectores base; la **dimensión** del espacio fija cuántos valores toma cada índice (3 en 3D).
>
> La idea central del capítulo: las **componentes** de un tensor cambian al rotar el sistema, pero el tensor —el objeto físico— es el mismo. Lo que distingue a un tensor de un arreglo cualquiera de números es que sus componentes obedecen la ley
> $$T'_{ij\dots}=T_{rs\dots}\,a_{ir}a_{js}\dots,$$
> un factor $a_{ij}$ por cada índice. Ese es el criterio que se usa para *reconocer* un tensor.

> [!info] Rango de los tensores
> | Rango | Objeto | Componentes (3D) | Ejemplo |
> |---|---|---|---|
> | 0 | escalar | 1 | temperatura, $(\vec A\times\vec B)\cdot\vec C$ |
> | 1 | vector | 3 | velocidad, $\vec E$ |
> | 2 | tensor | 9 | conductividad $\sigma_{ij}$, inercia $I_{ij}$, esfuerzo |
> | $n$ | tensor rango $n$ | $3^n$ | rigidez $C_{ijkl}$ (rango 4) |

## Resumen

> [!resumen]
> | Subnota | Aporta |
> |---|---|
> | [[Tensor Conductividad y Ley de Ohm]] | motivación física |
> | [[Notacion Tensorial y Terminologia]] | diádica, rango, producto externo |
> | [[Operaciones con Tensores]] | suma, producto, contracción |
> | [[Transformaciones entre Sistemas/index]] | ley de transformación |
> | [[Diagonalizacion de Tensores/index]] | valores y vectores propios |
> | [[Pseudo-objetos/index]] | objetos axiales |

> [!corolario]
> Un tensor generaliza la idea de vector a relaciones lineales entre vectores. Su notación diádica $T_{ij\dots}\hat e_i\hat e_j\dots$ guarda a la vez las componentes y la base, lo que vuelve trivial transformar entre sistemas. La marca de identidad de un tensor es su **ley de transformación** (un $a_{ij}$ por índice); las operaciones de [[Diagonalizacion de Tensores/index | diagonalización]] revelan su estructura intrínseca (valores propios), invariante bajo rotaciones.

> [!referencia]
> - Notación y producto externo: [[Notacion Tensorial y Terminologia]].
> - Ley de transformación: [[Transformaciones entre Sistemas/index]].
> - Base notacional (índices, $\delta$, $\varepsilon$): [[1 Algebra Lineal y Notacion/index]].
