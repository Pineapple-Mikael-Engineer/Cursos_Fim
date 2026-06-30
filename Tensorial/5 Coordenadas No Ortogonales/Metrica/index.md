---
title: Metrica y Componentes Covariantes/Contravariantes
order: 2
tags:
  - analisis-tensorial
  - teoria
  - coordenadas-no-ortogonales
  - covarianza
  - index
draft: false
aliases:
  - metrica
  - tensor metrico y componentes
  - covarianza contravarianza metrica
  - metric tensor and components
---

# Metrica y Componentes Covariantes/Contravariantes

> [!definicion]
> En un sistema inclinado un mismo vector tiene **dos** juegos de componentes y una **base dual**:
> $$\vec v=v^i\,\hat g_i=v_i\,\hat g^i,$$
> con $v^i$ **contravariantes** (superíndice, sobre $\hat g_i$) y $v_i$ **covariantes** (subíndice, sobre la dual $\hat g^i$). El **tensor métrico** $M_{ij}=\hat g_i\cdot\hat g_j$ (simétrico, $M_{ij}=M_{ji}$) conecta ambos: **baja** índices $v_i=M_{ij}v^j$ y, con su inverso $M^{ij}$, **sube** $v^i=M^{ij}v_j$.

> [!info]
> Es el corazón del [[../index | capítulo 5]] (libro, cap. 5.2.2 y 5.2.5). Toda la maquinaria nace del problema expuesto en [[../Sistema Inclinado | el sistema inclinado]]: sin ortogonalidad, la proyección no da la componente y el producto punto se llena de términos cruzados $\hat g_i\cdot\hat g_j$. Se desglosa en tres hijas:
> - [[Covarianza Contravarianza]] — las dos clases de componentes y cómo simplifican el producto punto (cap. 5.2.2).
> - [[Tensor Metrico]] — $M_{ij}=\hat g_i\cdot\hat g_j$, subir/bajar índices, $\vec A\cdot\vec B=A^iB^jM_{ij}$ (cap. 5.2.2).
> - [[Base Dual Reciproca]] — la base contravariante $\hat g^i$ con $\hat g_i\cdot\hat g^j=\delta_i{}^j$ (cap. 5.2.5).
>
> **Notación:** $M_{ij}$ es el tensor métrico (en otros textos y en Relatividad General se escribe $g_{ij}$); aquí seguimos al libro y reservamos $g$ para la matriz de transformación inversa $[g]$.

---

## En qué consiste

> [!teoria]
> Hay **dos** maneras equivalentes de devolverle al producto punto su forma simple $A_iB_i$ del caso ortonormal:
> 1. **Componentes covariantes/contravariantes:** se definen unas componentes covariantes $\tilde A_i$ que absorben los términos cruzados; entonces $\vec A\cdot\vec B=A^i\tilde B_i=\tilde A_iB^i$ mezcla un índice arriba y uno abajo (ver [[Covarianza Contravarianza]]).
> 2. **Tensor métrico:** se empaquetan los productos cruzados en $M_{ij}=\hat g_i\cdot\hat g_j$ y se usan componentes contravariantes para ambos vectores: $\vec A\cdot\vec B=A^iB^jM_{ij}$ (ver [[Tensor Metrico]]).
>
> Ambas vías son la misma: la métrica es justo la que baja el índice, $\tilde A_i=M_{ij}A^j$. La pieza que falta —dar sentido geométrico a $v_i$ como componente sobre una base— es la **base dual** $\hat g^i$ (ver [[Base Dual Reciproca]]).

> [!info] Las dos clases de componentes
> | | Contravariante | Covariante |
> |---|---|---|
> | Notación | $v^i$ (superíndice) | $v_i$ (subíndice) |
> | Base | $\hat g_i$ (paralela a los ejes) | $\hat g^i$ (dual, perpendicular) |
> | Geometría | proyección **paralela** a los ejes | proyección **perpendicular** a los ejes |
> | Se obtiene de la otra con | $v^i=M^{ij}v_j$ (sube) | \| $v_i=M_{ij}v^j$ (baja) \| |
> | Caso ortonormal | $M_{ij}=\delta_{ij}$, entonces $v^i=v_i$ | igual |

## Resumen

> [!resumen]
> | Subnota | Aporta |
> |---|---|
> | [[Covarianza Contravarianza]] | $\tilde A_i=A_j(\hat g_i\cdot\hat g_j)$; $\vec A\cdot\vec B=A^iB_i$ |
> | [[Tensor Metrico]] | $M_{ij}=\hat g_i\cdot\hat g_j$; $v_i=M_{ij}v^j$; $\vec A\cdot\vec B=A^iB^jM_{ij}$ |
> | [[Base Dual Reciproca]] | $\hat g_i\cdot\hat g^j=\delta_i{}^j$; $\vec v=v^i\hat g_i=v_i\hat g^i$; $v^i=M^{ij}v_j$ |

> [!corolario]
> El núcleo del capítulo cabe en una línea: $\vec v=v^i\hat g_i=v_i\hat g^i$ y $M_{ij}=\hat g_i\cdot\hat g_j$. La métrica está determinada **solo por la base** y es el puente entre las dos clases de componentes; en un sistema ortonormal $M_{ij}=\delta_{ij}$, las dos clases coinciden y se recupera todo lo anterior.

> [!referencia]
> - Origen del problema: [[../Sistema Inclinado]].
> - Las dos clases de componentes: [[Covarianza Contravarianza]].
> - El tensor que arregla el producto punto: [[Tensor Metrico]].
> - La base que cierra la construcción: [[Base Dual Reciproca]].
