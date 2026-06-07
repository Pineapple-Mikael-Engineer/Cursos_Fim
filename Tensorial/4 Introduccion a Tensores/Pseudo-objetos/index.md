---
title: Pseudo-objetos
tags:
  - analisis-tensorial
  - teoria
  - tensores
  - pseudo-objetos
  - index
draft: false
aliases:
  - pseudo-objetos
  - pseudovectores escalares tensores
  - objetos axiales
  - pseudo-objects
---

# Pseudo-objetos

> [!definicion]
> Un **pseudo-objeto** (pseudo-escalar, pseudo-vector o pseudo-tensor) transforma como su contraparte regular **salvo por un factor $|a|$ extra** bajo el cambio de sistema, donde $|a|=\det[a]$ es el determinante de la matriz de transformación:
> $$\text{regular: } v'_r=v_i\,a_{ri}\qquad\Longleftrightarrow\qquad\text{pseudo: } v'_r=|a|\,v_i\,a_{ri}.$$
> Como $|a|=+1$ para sistemas de **igual orientación** (ambos de mano derecha) y $|a|=-1$ para **orientación opuesta** (reflexión/inversión), el factor $|a|$ solo se nota al cambiar la mano del sistema: ahí el pseudo-objeto **cambia de signo**.

> [!info]
> Es la sección **4.6** del [[index | capítulo 4]] (libro, cap. 4.6). Las traslaciones y rotaciones rígidas **no** cambian la orientación de un sistema (no convierten mano derecha en mano izquierda); para eso hace falta una **reflexión**. Bajo reflexiones, ciertos objetos físicos adquieren un signo extra. Se desglosa en:
> - [[Pseudo-vectores]] — el producto cruz, campo magnético, momento angular (cap. 4.6.1).
> - [[Pseudo-escalares]] — el producto triple/volumen (cap. 4.6.2).
> - [[Pseudo-tensores]] — el símbolo de Levi-Civita $\varepsilon_{ijk}$ (cap. 4.6.3).
>
> ![[mano_derecha_izquierda.svg|460]]
>
> Sistema de mano derecha vs mano izquierda (reflexión): los pseudo-objetos cambian de signo al pasar de uno a otro.

---

## Ejemplo

> [!ejemplo]
> **El producto cruz delata el problema.** Toma $\vec A=A_0\hat e_1$ y $\vec B=B_0\hat e_2$ en un sistema **derecho**: $\vec A\times\vec B=A_0B_0\hat e_3$. Aplica la reflexión $x'_1=-x_1$, que invierte el eje 1 y produce un sistema **izquierdo** con $[a]=\operatorname{diag}(-1,1,1)$, $|a|=-1$. Hay dos formas de obtener $\vec A\times\vec B$ en el sistema primado:
> 1. **Transformando** el resultado como un vector regular ($v'_r=v_i a_{ri}$): da $+A_0B_0\hat e'_3$.
> 2. **Recalculando** el producto cruz directamente con la base primada: da $-A_0B_0\hat e'_3$.
>
> Difieren en un signo. La salida: el producto cruz **no** es un vector regular sino un **pseudo-vector**, que transforma con el factor $|a|$ extra. Con $|a|=-1$, ambos cálculos coinciden. El desarrollo completo está en [[Pseudo-vectores]].

---

## En qué consiste

> [!teoria]
> Una matriz de transformación entre dos sistemas ortonormales tiene $|a|=\det[a]=\pm 1$. El signo codifica la **orientación relativa**: $|a|=+1$ si ambos sistemas son de la misma mano (rotación pura), $|a|=-1$ si uno es la imagen especular del otro (reflexión o inversión). Los objetos regulares —vectores polares, escalares verdaderos, tensores— ignoran ese signo: su ley de transformación no contiene $|a|$. Los pseudo-objetos lo arrastran, por lo que **solo bajo reflexiones** se comportan distinto.
>
> El origen físico es el producto cruz: $\vec A\times\vec B$ se define con la regla de la mano derecha, una convención de orientación. Al reflejar el sistema, la regla deja de servir y aparece el signo extra. Todo objeto construido con un número **impar** de productos cruz hereda este carácter axial.

> [!info] Regulares vs pseudo
> | Rango | Regular | Pseudo | Ley pseudo |
> |---|---|---|---|
> | 0 | escalar | pseudo-escalar | $S'=\|a\|\,S$ |
> | 1 | vector (polar) | pseudo-vector (axial) | $v'_r=\|a\|\,v_i a_{ri}$ |
> | 2 | tensor | pseudo-tensor | $T'_{rs}=\|a\|\,T_{ij}a_{ri}a_{sj}$ |
> | $n$ | tensor rango $n$ | pseudo-tensor rango $n$ | un $a$ por índice $+$ un $\|a\|$ |

## Resumen

> [!resumen]
> | Subnota | Aporta |
> |---|---|
> | [[Pseudo-vectores]] | producto cruz, $\vec B$, $\vec L$; ley $v'_r=\|a\|\,v_i a_{ri}$ |
> | [[Pseudo-escalares]] | producto triple/volumen; ley $S'=\|a\|\,S$ |
> | [[Pseudo-tensores]] | símbolo de Levi-Civita; ley $T'=\|a\|\,T\,a\dots a$ |

> [!corolario]
> Un pseudo-objeto es indistinguible de su contraparte regular mientras solo se hagan rotaciones y traslaciones ($|a|=+1$). La diferencia aflora **únicamente** ante una reflexión ($|a|=-1$), donde el pseudo-objeto cambia de signo. El prototipo es el producto cruz: genera pseudo-vectores ([[Pseudo-vectores]]), su producto punto con un tercer vector da el pseudo-escalar volumen ([[Pseudo-escalares]]), y el símbolo $\varepsilon_{ijk}$ que lo define es el pseudo-tensor por excelencia ([[Pseudo-tensores]]).

> [!referencia]
> - Definición del producto cruz: [[Producto Cruz]].
> - El símbolo $\varepsilon_{ijk}$: [[Simbolo Levi-Civita]].
> - Ley de transformación regular ($v'_r=v_i a_{ri}$): [[Transformaciones entre Sistemas/index]].
