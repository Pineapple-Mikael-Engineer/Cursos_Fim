---
title: Álgebra Lineal y Notación
order: 2
tags:
  - analisis-tensorial
  - teoria
  - notacion-indices
  - index
draft: false
aliases:
  - algebra lineal y notacion
  - capitulo 1 tensorial
  - revision algebra lineal
---

# Álgebra Lineal y Notación

> [!definicion]
> El capítulo repasa el álgebra de vectores y matrices reescrita con **subíndices** y el **convenio de suma de Einstein**: la herramienta que vuelve mecánica la manipulación tensorial. Toda la sección trabaja en coordenadas **cartesianas ortonormales** ($\hat{e}_i\cdot\hat{e}_j=\delta_{ij}$, base fija).

> [!info]
> Es el **capítulo 1** del libro (Rogan & Muñoz, Parte I). Se desglosa en:
> - [[Notacion Indices Sumatorias]] — componentes $v_i$, índice mudo/libre, convenio de Einstein.
> - [[Algebra Lineal para Tensores]] — vectores, matrices $[M]$ y su producto $M_{ij}N_{jk}=P_{ik}$.
> - [[Operaciones Vectoriales/index | Operaciones Vectoriales]] — rotación, producto punto y cruz.
> - [[Simbolos Especiales/index | Símbolos Especiales]] — la delta $\delta_{ij}$ y el símbolo $\varepsilon_{ijk}$.
>
> Es la base de todo el curso: la misma notación reaparece en [[Coordenadas Curvilineas/index | curvilíneas]], [[Introduccion a Tensores/index | tensores]] y [[Coordenadas No Ortogonales/index | covarianza]].

---

## Ejemplo

> [!ejemplo]
> **La misma ecuación en cuatro notaciones.** La suma de dos vectores $\vec{c}=\vec{a}+\vec{b}$ en $\mathbb{R}^3$:
>
> | Notación | Escritura | Comentario |
> |---|---|---|
> | Vectorial | $\vec{c}=\vec{a}+\vec{b}$ | independiente de coordenadas |
> | Por componentes | $c_1=a_1+b_1,\ c_2=a_2+b_2,\ c_3=a_3+b_3$ | tres ecuaciones |
> | Subíndices | $c_i=a_i+b_i$ | una sola línea, $i$ libre |
> | Matricial | $[c]=[a]+[b]$ | arreglos columna |
>
> El salto clave es de tres ecuaciones a **una**: el subíndice libre $i$ representa los tres valores a la vez. Cuando además hay un índice **repetido**, el convenio de Einstein omite el $\sum$: $\vec{v}=\sum_{i=1}^{3}v_i\hat{e}_i \equiv v_i\hat{e}_i$.

---

## En qué consiste

> [!teoria]
> La idea del capítulo es introducir dos abreviaturas que se combinan:
> 1. **Notación de subíndices:** un índice libre condensa un conjunto de ecuaciones ($c_i=a_i+b_i$).
> 2. **Convenio de Einstein:** un índice repetido en un término implica suma sobre él ($v_i\hat{e}_i$).
>
> Juntas forman la **notación de Einstein**. Su ventaja es la *contabilidad notacional*: los índices libres del lado izquierdo y derecho deben coincidir, lo que permite **detectar errores** y guía las manipulaciones. Su desventaja es que ata la expresión a un sistema de coordenadas; por eso, al final de un cálculo se vuelve a la notación vectorial, válida en cualquier sistema.

> [!info] Convención de trabajo del capítulo
> | Aspecto | Convención |
> |---|---|
> | Coordenadas | cartesianas, base $\hat{e}_i$ ortonormal y fija |
> | Índices | $i,j,k,\dots\in\{1,2,3\}$ |
> | Suma | implícita sobre índice repetido (Einstein) |
> | Vector | $\vec{v}=v_i\hat{e}_i$; matriz $[M]$; tensor $\overleftrightarrow{T}$ |

## Resumen

> [!resumen]
> | Subnota | Aporta |
> |---|---|
> | [[Notacion Indices Sumatorias]] | índice mudo/libre, convenio de Einstein |
> | [[Algebra Lineal para Tensores]] | vectores y matrices en índices |
> | [[Operaciones Vectoriales/index]] | rotación, producto punto y cruz |
> | [[Simbolos Especiales/index]] | $\delta_{ij}$ y $\varepsilon_{ijk}$ |

> [!corolario]
> El capítulo no introduce física nueva: reescribe el álgebra lineal conocida en un lenguaje de índices que, a partir del [[Introduccion a Tensores/index | capítulo 4]], hará la manipulación de tensores tan mecánica como sumar componentes. Dominar el convenio de Einstein y los símbolos $\delta_{ij}$, $\varepsilon_{ijk}$ es el prerequisito de todo lo que sigue.

> [!referencia]
> - Núcleo notacional: [[Notacion Indices Sumatorias]].
> - Herramientas $\delta$ y $\varepsilon$: [[Simbolos Especiales/index]].
> - Primer uso intensivo: [[Operaciones Vectoriales/Calculos con Notacion Einstein]].
