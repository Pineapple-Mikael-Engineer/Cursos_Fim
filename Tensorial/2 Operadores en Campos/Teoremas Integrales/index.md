---
title: Teoremas Integrales
order: 4
tags:
  - analisis-tensorial
  - teoria
  - calculo-vectorial
  - teoremas-integrales
  - index
draft: false
aliases:
  - teoremas integrales
  - teoremas del calculo vectorial
  - integral theorems
---

# Teoremas Integrales

> [!definicion]
> Los **teoremas integrales** convierten las definiciones integrales de los operadores diferenciales (válidas en escala **infinitesimal**) en igualdades entre una integral sobre una región y una integral sobre su frontera, válidas en escala **macroscópica**. Son cuatro: **Gauss** (volumen $\leftrightarrow$ superficie cerrada), **Green** (dos identidades con $\nabla^2$), **Stokes** (superficie $\leftrightarrow$ contorno) y **Helmholtz** (unicidad y descomposición de un campo).

> [!info]
> Sección **2.5** del [[index | capítulo 2]] (Rogan & Muñoz, *cap 2.5*). Recoge los frutos de los [[Operadores Diferenciales/index | operadores diferenciales]] (cap. 2.3) y los [[Operadores Integrales/index | operadores integrales]] (cap. 2.2). Se desglosa en:
> - [[Teorema de Gauss]] — divergencia integrada sobre un volumen (*cap 2.5.1*).
> - [[Teorema de Green]] — dos identidades para el laplaciano (*cap 2.5.2*).
> - [[Teorema de Stokes]] — rotor integrado sobre una superficie y campos conservativos (*cap 2.5.3*).
> - [[Teorema de Helmholtz]] — unicidad y descomposición de un campo vectorial (*cap 2.5.4*).
>
> Todos se derivan de las **definiciones integrales** de la divergencia y el rotor: se aplican a dos celdas adyacentes, las contribuciones de la frontera común se **cancelan**, y se suman las celdas hasta cubrir la región.

---

## Ejemplo

> [!ejemplo]
> **Qué conecta cada teorema.** La idea común es *bajar una dimensión*: la integral de un operador diferencial sobre una región $D$ se reduce a una integral sobre su frontera $\partial D$.
>
> | Teorema | Operador en el interior | Integral sobre $D$ | Integral sobre $\partial D$ |
> |---|---|---|---|
> | Gauss | $\vec\nabla\cdot\vec A$ | volumen $V$ | superficie cerrada $S$ |
> | Stokes | $\vec\nabla\times\vec A$ | superficie $S$ | contorno cerrado $C$ |
> | Green (1ª) | $u\nabla^2 v-v\nabla^2 u$ | volumen $V$ | superficie cerrada $S$ |
> | Green (2ª) | $\vec\nabla u\cdot\vec\nabla v+u\nabla^2 v$ | volumen $V$ | superficie cerrada $S$ |
>
> Gauss y Stokes son los dos teoremas básicos; Green se obtiene de Gauss aplicado a $u\vec\nabla v$, y Helmholtz se prueba con la 2ª forma de Green.

---

## En qué consiste

> [!teoria]
> Los operadores diferenciales informan de la variación de un campo **punto a punto**. Para aplicarlos a una escala finita hace falta *integrarlos*, y los teoremas dan el valor de esa integral en términos de la frontera. El mecanismo de demostración de Gauss y Stokes es idéntico:
> 1. Se parte de la **definición integral** del operador en una celda infinitesimal.
> 2. Se juntan dos celdas con una **cara (o borde) común**; las contribuciones de esa frontera interna se cancelan porque la atraviesan con orientaciones opuestas.
> 3. Se acumulan celdas hasta llenar la región; solo sobrevive la frontera **externa**.

> [!proposicion] Jerarquía de derivación
> $$\text{def. integral de }\vec\nabla\cdot\;\Rightarrow\;\text{Gauss}\;\Rightarrow\;\text{Green}\;\Rightarrow\;\text{Helmholtz},\qquad \text{def. integral de }\vec\nabla\times\;\Rightarrow\;\text{Stokes}.$$
> Gauss es el tronco del que cuelgan Green y Helmholtz; Stokes es independiente y añade la noción de **campo conservativo**.

## Resumen

> [!resumen]
> | Subnota | Aporta |
> |---|---|
> | [[Teorema de Gauss]] | $\int_V d\tau\,\vec\nabla\cdot\vec A=\oint_S d\vec\sigma\cdot\vec A$ |
> | [[Teorema de Green]] | dos identidades con $\nabla^2$, base de problemas de potencial |
> | [[Teorema de Stokes]] | $\int_S d\vec\sigma\cdot(\vec\nabla\times\vec A)=\oint_C d\vec r\cdot\vec A$; campos conservativos |
> | [[Teorema de Helmholtz]] | unicidad ($\vec\nabla\cdot$, $\vec\nabla\times$, $\hat n\cdot$) y descomposición solenoidal + irrotacional |

> [!corolario]
> Los cuatro teoremas suben los operadores diferenciales de lo infinitesimal a lo macroscópico. Gauss y Stokes son los pilares geométricos; Green traduce el laplaciano a la frontera (núcleo de la teoría de potencial) y Helmholtz garantiza que un campo queda fijado por su divergencia, su rotor y su componente normal, descomponiéndolo en parte **solenoidal** e **irrotacional**.

> [!referencia]
> - Definiciones integrales de origen: [[Operadores Diferenciales/index]].
> - Integrales de frontera ($d\vec\sigma$, $d\vec r$): [[Operadores Integrales/index]].
> - Generalización a [[Coordenadas Curvilineas/index | curvilíneas]] (cap. 3).
