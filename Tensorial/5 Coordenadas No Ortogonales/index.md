---
title: Sistemas de Coordenadas No Ortogonales
order: 6
tags:
  - analisis-tensorial
  - teoria
  - coordenadas-no-ortogonales
  - index
draft: false
aliases:
  - coordenadas no ortogonales
  - capitulo 5 tensorial
  - covarianza contravarianza
  - non-orthogonal coordinates
---

# Sistemas de Coordenadas No Ortogonales

> [!definicion]
> En un sistema **no ortogonal** los vectores base $\hat g_i$ no son perpendiculares entre sí: $\hat g_i\cdot\hat g_j\neq\delta_{ij}$. Esto obliga a distinguir **dos tipos de componentes** de un vector: las **contravariantes** $v^i$ (superíndice, proyección paralela a los ejes) y las **covariantes** $v_i$ (subíndice, proyección perpendicular), relacionadas por el **tensor métrico** $M_{ij}=\hat g_i\cdot\hat g_j$.

> [!info]
> Es el **capítulo 5** del libro (Rogan & Muñoz, Parte I; basado en Kusse & Westwig cap. 14). Aquí nos limitamos a sistemas **inclinados** con base invariante en la posición. Se desglosa en:
> - [[Sistema Inclinado]] — por qué el producto punto se complica (cap. 5.2.1).
> - [[Metrica/index | Métrica]] — covarianza/contravarianza, $M_{ij}$, base dual (cap. 5.2.2).
> - [[Transformaciones Contravariantes]] · [[Transformaciones Covariantes]] (cap. 5.2.3, 5.2.5).
> - [[Notacion Subindices Superindices]] — el convenio arriba/abajo (cap. 5.2.4).
> - [[Covarianza Contravarianza en Tensores]] · [[Derivadas Parciales Co y Contravariantes]] (cap. 5.2.6, 5.2.7).
>
> **Notación:** $M_{ij}$ es el tensor métrico (en otros textos y en Relatividad se escribe $g_{ij}$); aquí $g$ se reserva para la matriz de transformación inversa.

---

## Ejemplo

> [!ejemplo]
> **Dónde aparecen: la relatividad.** En relatividad especial, un mismo **evento** (posición y tiempo) se describe en dos sistemas $(x,ct)$ y $(x',ct')$. Los ejes $x$ y $ct$ se cruzan en ángulo recto, pero los ejes $x'$ y $ct'$ del sistema en movimiento **no**: forman un sistema **inclinado**.
>
> ![[relatividad_sistemas.svg|420]]
>
> En relatividad general, las líneas de la malla de coordenadas siguen **geodésicas** curvadas por la gravedad (la luz se dobla cerca de una masa, medido por Eddington en 1919). En ambos casos la base no es ortonormal, y hace falta la maquinaria de covarianza/contravarianza.

---

## En qué consiste

> [!teoria]
> En un sistema ortonormal, una componente se obtiene proyectando: $v_1=\vec v\cdot\hat e_1$. En uno inclinado esto **falla** ($\vec v\cdot\hat g'_1\neq v'_1$) porque los ejes no son perpendiculares. La solución es admitir **dos** descomposiciones del mismo vector:
> $$\vec v=v^i\,\hat g_i=v_i\,\hat g^i,$$
> con componentes **contravariantes** $v^i$ sobre la base $\hat g_i$, y componentes **covariantes** $v_i$ sobre una **base dual** $\hat g^i$ (que cumple $\hat g_i\cdot\hat g^j=\delta_i{}^j$). El **tensor métrico** $M_{ij}=\hat g_i\cdot\hat g_j$ es la pieza que conecta ambas: $v_i=M_{ij}v^j$ (bajar el índice). Con él, el producto punto recupera su forma simple: $\vec A\cdot\vec B=A^iB_i=A_iB^i$.

> [!info] Las dos clases de componentes
> | | Contravariante | Covariante |
> |---|---|---|
> | Notación | $v^i$ (superíndice) | $v_i$ (subíndice) |
> | Base | $\hat g_i$ (paralela a los ejes) | $\hat g^i$ (dual, perpendicular) |
> | Geometría | proyección **paralela** a los ejes | proyección **perpendicular** a los ejes |
> | Transforma con | $t^i{}_j=\partial x'^i/\partial x^j$ | $g^j{}_i=\partial x^j/\partial x'^i$ |
> | Conexión | \|  $v_i=M_{ij}v^j$  \| | $v^i=M^{ij}v_j$ |

## Resumen

> [!resumen]
> | Subnota | Aporta |
> |---|---|
> | [[Sistema Inclinado]] | el problema del producto punto |
> | [[Metrica/index]] | $M_{ij}$, subir/bajar índices, base dual |
> | [[Transformaciones Contravariantes]] | $v'^i=t^i{}_j v^j$ |
> | [[Transformaciones Covariantes]] | $v'_i=g^j{}_i v_j$ |
> | [[Notacion Subindices Superindices]] | convenio arriba/abajo |
> | [[Covarianza Contravarianza en Tensores]] | $T^{ij}$, $T_{ij}$, $T^i{}_j$ |

> [!corolario]
> Cuando la base no es ortogonal, un vector tiene dos juegos de componentes —contravariantes $v^i$ y covariantes $v_i$— y el tensor métrico $M_{ij}=\hat g_i\cdot\hat g_j$ es el puente entre ellos. Esta maquinaria, que parece un tecnicismo, es exactamente la que sostiene la [[Notacion Subindices Superindices | notación arriba/abajo]] de la Relatividad y la base de la geometría diferencial: el producto interno $A^iB_i$ es invariante porque mezcla un índice arriba y uno abajo.

> [!referencia]
> - El problema concreto: [[Sistema Inclinado]].
> - Métrica y base dual: [[Metrica/index]].
> - Caso ortonormal (donde $v^i=v_i$): [[1 Algebra Lineal y Notacion/index]].
