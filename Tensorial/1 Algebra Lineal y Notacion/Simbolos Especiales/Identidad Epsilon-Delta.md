---
title: Identidad Épsilon-Delta
tags:
  - analisis-tensorial
  - teoria
  - notacion-indices
  - levi-civita
draft: false
aliases:
  - identidad epsilon-delta
  - identidad e-delta
  - producto de dos epsilon
  - epsilon-delta identity
  - BAC-CAB
---

# Identidad Épsilon-Delta $\varepsilon_{ijk}\varepsilon_{mnk}=\delta_{im}\delta_{jn}-\delta_{in}\delta_{jm}$

> [!definicion]
> El producto de **dos** símbolos de Levi-Civita con un índice **común** (aquí $k$, en la última posición) se reduce a deltas de Kronecker:
> $$\varepsilon_{ijk}\,\varepsilon_{mnk}=\delta_{im}\delta_{jn}-\delta_{in}\delta_{jm}.$$
> Es la herramienta que convierte el producto cruz doble en producto punto, y con ella toda identidad vectorial se vuelve un cálculo de índices.

> [!info]
> Vive en [[index | Símbolos Especiales]] del [[../index | capítulo 1]] (libro, cap. 1.2.3, eq. 1.78). Combina [[Delta Kronecker | $\delta_{ij}$]] y [[Simbolo Levi-Civita | $\varepsilon_{ijk}$]] sobre la [[Notacion Indices Sumatorias | notación de Einstein]]. Es el motor de los [[Operaciones Vectoriales/Productos Vectoriales | productos vectoriales dobles]].

---

## Ejemplo

> [!ejemplo]
> **Derivación de BAC-CAB.** Demostrar $\vec{A}\times(\vec{B}\times\vec{C})=(\vec{A}\cdot\vec{C})\vec{B}-(\vec{A}\cdot\vec{B})\vec{C}$.
>
> *Paso 1.* Componente $i$ del doble cruz, con la forma de índice común primero:
> $$[\vec{A}\times(\vec{B}\times\vec{C})]_i=\varepsilon_{ijk}A_j(\vec{B}\times\vec{C})_k=\varepsilon_{ijk}A_j\,\varepsilon_{klm}B_lC_m.$$
> *Paso 2.* El índice común es $k$; reordenando $\varepsilon_{ijk}\varepsilon_{klm}=\varepsilon_{kij}\varepsilon_{klm}$ y aplicando la identidad (común en primera posición):
> $$\varepsilon_{kij}\varepsilon_{klm}=\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}.$$
> *Paso 3.* Sustituir y usar la propiedad de sustitución de las deltas:
> $$[\,\cdot\,]_i=(\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl})A_jB_lC_m=A_jB_iC_j-A_jB_jC_i.$$
> *Paso 4.* Reconocer $A_jC_j=\vec{A}\cdot\vec{C}$ y $A_jB_j=\vec{A}\cdot\vec{B}$:
> $$[\,\cdot\,]_i=(\vec{A}\cdot\vec{C})B_i-(\vec{A}\cdot\vec{B})C_i\ \Longrightarrow\ \vec{A}\times(\vec{B}\times\vec{C})=(\vec{A}\cdot\vec{C})\vec{B}-(\vec{A}\cdot\vec{B})\vec{C}.$$
> Sin geometría: solo la identidad $\varepsilon$-$\delta$ y sustitución. La misma maquinaria da $\vec{\nabla}\times(\vec{\nabla}\times\vec{F})=\vec{\nabla}(\vec{\nabla}\cdot\vec{F})-\nabla^2\vec{F}$ tratando $\vec{\nabla}$ como un "vector" $\partial_i$.

---

## En qué consiste

> [!teoria]
> Un producto cruz doble lleva dos símbolos $\varepsilon$ que comparten un índice mudo (el de la operación intermedia). La identidad **elimina ambos $\varepsilon$** a cambio de dos deltas con signo, y cada delta se reabsorbe por sustitución. El resultado siempre queda en términos de productos punto: por eso BAC-CAB no tiene producto cruz a la derecha. La posición del índice común fija qué forma usar.

> [!regla] Forma según el índice común
> | Índice común | Identidad |
> |---|---|
> | última posición | $\varepsilon_{ijk}\varepsilon_{mnk}=\delta_{im}\delta_{jn}-\delta_{in}\delta_{jm}$ |
> | primera posición | $\varepsilon_{ijk}\varepsilon_{ilm}=\delta_{jl}\delta_{km}-\delta_{jm}\delta_{kl}$ |
>
> Ambas son la misma identidad reordenada por permutación cíclica de los índices ($\varepsilon_{ijk}=\varepsilon_{kij}$). Regla mnemónica: con el común alineado primero, las deltas emparejan los índices restantes "en orden menos en cruz".

> [!corolario] Contracciones sucesivas
> Contrayendo un segundo par de índices se obtienen escalares útiles:
> $$\varepsilon_{ijk}\varepsilon_{ijl}=2\,\delta_{kl},\qquad \varepsilon_{ijk}\varepsilon_{ijk}=6.$$
> La primera sale de $\varepsilon_{ijk}\varepsilon_{ilm}=\delta_{jl}\delta_{km}-\delta_{jm}\delta_{kl}$ poniendo $l=j$ y sumando: $\delta_{jj}\delta_{km}-\delta_{jm}\delta_{kj}=3\delta_{km}-\delta_{km}=2\delta_{km}$. La segunda, con $k=l$: $2\delta_{kk}=2\cdot3=6$ (las $6$ entradas no nulas, cada una $(\pm1)^2=1$).

> [!teorema] Identidad $\varepsilon$-$\delta$
> $$\varepsilon_{ijk}\varepsilon_{mnk}=\delta_{im}\delta_{jn}-\delta_{in}\delta_{jm}.$$

> [!demostracion]
> **Verificación por estructura y un caso concreto.**
> *Paso 1 (anulación).* El lado izquierdo solo es no nulo si $\{i,j\}$ y $\{m,n\}$ son ambos $\{1,2,3\}\setminus\{k\}$, es decir si $\{i,j\}=\{m,n\}$ como conjuntos e $i\neq j$. El lado derecho refleja lo mismo: si $i=j$ entonces $\delta_{im}\delta_{jn}-\delta_{in}\delta_{jm}$ es antisimétrico en $i,j$ y se anula.
> *Paso 2 (caso $i=m$, $j=n$, $i\neq j$).* Lado derecho: $\delta_{ii}\delta_{jj}-\delta_{ij}\delta_{ji}=1\cdot1-0=1$. Lado izquierdo: $\varepsilon_{ijk}\varepsilon_{ijk}$ (sin sumar $i,j$, solo el $k$ restante) $=(\pm1)^2=1$. Coinciden.
> *Paso 3 (caso $i=n$, $j=m$, $i\neq j$).* Lado derecho: $\delta_{in}\!\to\!\delta_{ii}=1$ via $m=j,n=i$ da $\delta_{im}\delta_{jn}-\delta_{in}\delta_{jm}=0-1\cdot1=-1$. Lado izquierdo: $\varepsilon_{ijk}\varepsilon_{jik}=-\varepsilon_{ijk}\varepsilon_{ijk}=-1$ (antisimetría). Coinciden.
> *Paso 4 (numérico).* Con $i=1,j=2,m=1,n=2$: $\varepsilon_{12k}\varepsilon_{12k}=\varepsilon_{123}\varepsilon_{123}=1$, y derecho $\delta_{11}\delta_{22}-\delta_{12}\delta_{21}=1-0=1$. ✓ La igualdad se verifica entrada por entrada.

## Resumen

> [!resumen]
> | Forma | Fórmula |
> |---|---|
> | Común último | $\varepsilon_{ijk}\varepsilon_{mnk}=\delta_{im}\delta_{jn}-\delta_{in}\delta_{jm}$ |
> | Común primero | $\varepsilon_{ijk}\varepsilon_{ilm}=\delta_{jl}\delta_{km}-\delta_{jm}\delta_{kl}$ |
> | Una contracción | $\varepsilon_{ijk}\varepsilon_{ijl}=2\delta_{kl}$ |
> | Contracción total | $\varepsilon_{ijk}\varepsilon_{ijk}=6$ |
> | Uso estrella | BAC-CAB: $\vec{A}\times(\vec{B}\times\vec{C})=(\vec{A}\cdot\vec{C})\vec{B}-(\vec{A}\cdot\vec{B})\vec{C}$ |

> [!corolario]
> La identidad $\varepsilon$-$\delta$ es el único hecho que hace falta memorizar de toda la sección: convierte $\varepsilon\varepsilon$ en $\delta\delta$, y las deltas se reabsorben. Con ella, las identidades del cálculo vectorial (BAC-CAB, doble rotor) se derivan en cuatro líneas, sin dibujos ni casos.

> [!referencia]
> - Símbolos que combina: [[Delta Kronecker]] · [[Simbolo Levi-Civita]].
> - Aplicación sistemática: [[Operaciones Vectoriales/Calculos con Notacion Einstein]].
> - Productos que mecaniza: [[Operaciones Vectoriales/Productos Vectoriales]].
