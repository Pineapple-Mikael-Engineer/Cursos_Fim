---
title: Transformaciones de Componentes Contravariantes
order: 3
tags:
  - analisis-tensorial
  - teoria
  - coordenadas-no-ortogonales
  - covarianza
draft: false
aliases:
  - transformaciones contravariantes
  - componentes contravariantes
  - matriz de transformacion t
  - contravariant transformation
---

# Transformaciones de Componentes Contravariantes $v'^i=t^i{}_j v^j$

> [!definicion]
> Entre dos sistemas inclinados (no primado $x^i$, base $\hat g_i$; primado $x'^i$, base $\hat g'_i$), las componentes **contravariantes** de un vector transforman contrayendo el **segundo** índice de la matriz $[t]$:
> $$v'^i=t^i{}_j\,v^j,\qquad t^i{}_j=\frac{\partial x'^i}{\partial x^j},$$
> y la inversa, con la matriz $[g]=[t]^{-1}$:
> $$v^i=g^i{}_j\,v'^j,\qquad g^i{}_j=\frac{\partial x^i}{\partial x'^j}.$$
> A diferencia del caso ortonormal, **la inversa no es la transpuesta** ($g\neq t^{\mathsf T}$): se calcula con cofactores, $g^i{}_j=(t^{-1})_{ij}=c_{ji}/|t|$.

> [!info]
> Es el cap. 5.2.3 del libro, dentro del [[index | capítulo 5]]. Necesita el lenguaje de [[Metrica/index | covarianza/contravarianza]] (componentes $v^i$ sobre la base $\hat g_i$) y precede a las [[Transformaciones Covariantes | transformaciones covariantes]] (cap. 5.2.5), que contraen el **primer** índice. La notación arriba/abajo de $t^i{}_j$ se justifica en [[Notacion Subindices Superindices]] (cap. 5.2.4). Compárese con el caso cartesiano ortonormal [[4 Introduccion a Tensores/Transformaciones entre Sistemas/Matriz de Transformacion | de la matriz $[a]$]], donde sí $a^{-1}_{ij}=a_{ji}$.
>
> **Notación:** $[t]$ va de **no primado a primado**; $[g]$ de **primado a no primado**. Aquí $g$ es la matriz de transformación inversa, **no** el tensor métrico (ese es $M_{ij}$).

---

## Ejemplo

> [!ejemplo]
> **Una transformación inclinada concreta.** Sea el sistema no primado cartesiano $(x^1,x^2)$ y un sistema primado inclinado definido por
> $$x'^1=x^1-\tfrac{1}{\sqrt3}\,x^2,\qquad x'^2=\tfrac{2}{\sqrt3}\,x^2.$$
> La matriz de transformación se lee derivando, $t^i{}_j=\partial x'^i/\partial x^j$:
> $$[t]=\begin{pmatrix} 1 & -\tfrac{1}{\sqrt3}\\[2pt] 0 & \tfrac{2}{\sqrt3}\end{pmatrix},\qquad |t|=\frac{2}{\sqrt3}.$$
> Un vector con componentes contravariantes $v^1=3,\ v^2=\sqrt3$ se transforma con $v'^i=t^i{}_j v^j$:
> $$v'^1=1\cdot3+\left(-\tfrac{1}{\sqrt3}\right)\sqrt3=3-1=2,\qquad v'^2=0\cdot3+\tfrac{2}{\sqrt3}\cdot\sqrt3=2.$$
>
> **La inversa no es la transpuesta.** Con cofactores, $g^i{}_j=c_{ji}/|t|$:
> $$[g]=[t]^{-1}=\frac{1}{|t|}\begin{pmatrix} \tfrac{2}{\sqrt3} & \tfrac{1}{\sqrt3}\\[2pt] 0 & 1\end{pmatrix}=\begin{pmatrix} 1 & \tfrac12\\[2pt] 0 & \tfrac{\sqrt3}{2}\end{pmatrix}\;\neq\;[t]^{\mathsf T}.$$
> Volviendo atrás con $v^i=g^i{}_j v'^j$ se recupera $v^1=1\cdot2+\tfrac12\cdot2=3$ y $v^2=\tfrac{\sqrt3}{2}\cdot2=\sqrt3$. ✓ Y en efecto $t^i{}_j g^j{}_k=\delta^i{}_k$.

---

## En qué consiste

> [!teoria]
> Todos los vectores en un punto transforman con la **misma** matriz $[t]$. La diferencia con el caso ortonormal es que la inversa $[g]=[t]^{-1}$ ya **no** se obtiene transponiendo: hay que invertir de verdad. El libro da dos formas equivalentes de $[g]$:
> $$g^i{}_j=(t^{-1})_{ij}=\frac{c_{ji}}{|t|}\qquad\text{(cofactores)},\qquad\qquad g^i{}_j=\frac{\partial x^i}{\partial x'^j}\qquad\text{(desde las ecuaciones de coordenadas)},$$
> donde $c_{ji}=(-1)^{i+j}$ por el menor de $[t]$ con la fila $j$ y la columna $i$ tachadas. Ambas dan lo mismo y cumplen, por definición de inversa,
> $$t^i{}_j\,g^j{}_k=\delta^i{}_k.$$

> [!teorema] Por qué $t^i{}_j=\partial x'^i/\partial x^j$
> La matriz que transforma las componentes contravariantes es justo la jacobiana de las coordenadas.

> [!demostracion]
> **Paso 1 — el vector desplazamiento es invariante.** Un desplazamiento infinitesimal $d\vec r$ es el mismo objeto físico en ambos sistemas; expresado con componentes contravariantes y las respectivas bases,
> $$d\vec r=dx^i\,\hat g_i=dx'^i\,\hat g'_i.$$
>
> **Paso 2 — sus componentes son contravariantes.** Como $d\vec r$ es un vector, sus componentes $dx^i$ transforman con la regla contravariante $dx'^i=t^i{}_j\,dx^j$.
>
> **Paso 3 — regla de la cadena.** Las ecuaciones de coordenadas $x'^i=x'^i(x^1,x^2,x^3)$ dan el diferencial total
> $$dx'^i=\frac{\partial x'^i}{\partial x^j}\,dx^j.$$
>
> **Paso 4 — identificar.** Comparando los Pasos 2 y 3, válidos para todo $dx^j$,
> $$\boxed{\,t^i{}_j=\frac{\partial x'^i}{\partial x^j}\,}.$$
> El mismo argumento con $[g]$ en vez de $[t]$ (partiendo de $dx^i=g^i{}_j\,dx'^j$) da $g^i{}_j=\partial x^i/\partial x'^j$. $\blacksquare$

> [!proposicion] Transformación de la base: contrae el OTRO índice
> Las **bases** vectoriales no transforman como las componentes: contraen el **primer** índice de la matriz, no el segundo.
> $$\hat g_j=t^i{}_j\,\hat g'_i,\qquad\qquad \hat g'_j=g^i{}_j\,\hat g_i.$$
> **Razón:** el vector $\vec v=v^j\hat g_j=v'^i\hat g'_i$ es invariante. Sustituyendo $v'^i=t^i{}_j v^j$ se obtiene $v^j\hat g_j=v^j\,t^i{}_j\,\hat g'_i$; como vale para todo $v^j$, queda $\hat g_j=t^i{}_j\hat g'_i$. La suma corre sobre el índice **superior** de $t$ (el primero), opuesto al de las componentes (el segundo). Esta asimetría es lo que hace covariante a la base $\hat g_i$ y motiva su subíndice (ver [[Notacion Subindices Superindices]]).

> [!info] Resumen de relaciones (componentes y base)
> | Objeto | No primado → primado | Primado → no primado |
> |---|---|---|
> | Matriz | $t^i{}_j=\partial x'^i/\partial x^j$ | $g^i{}_j=\partial x^i/\partial x'^j$ |
> | Componentes $v^i$ | $v'^i=t^i{}_j\,v^j$ | $v^i=g^i{}_j\,v'^j$ |
> | Base $\hat g_i$ | $\hat g'_j=g^i{}_j\,\hat g_i$ | $\hat g_j=t^i{}_j\,\hat g'_i$ |
> | Inversa | $t^i{}_j\,g^j{}_k=\delta^i{}_k$ | $g^i{}_j=c_{ji}/\|t\|\neq t^{\mathsf T}$ |

## Resumen

> [!resumen]
> | Aspecto | Componente contravariante $v^i$ | Base covariante $\hat g_i$ |
> |---|---|---|
> | Transforma | $v'^i=t^i{}_j\,v^j$ | $\hat g_j=t^i{}_j\,\hat g'_i$ |
> | Índice contraído de $[t]$ | el **segundo** (inferior $j$) | el **primero** (superior $i$) |
> | Inversa con | $g^i{}_j=\partial x^i/\partial x'^j$ | $\hat g'_j=g^i{}_j\,\hat g_i$ |
> | Matriz inversa | $[g]=[t]^{-1}$, **no** $t^{\mathsf T}$; $\,g^i{}_j=c_{ji}/\|t\|$ | $t^i{}_j\,g^j{}_k=\delta^i{}_k$ |

> [!corolario]
> Las componentes contravariantes transforman con $t^i{}_j=\partial x'^i/\partial x^j$ contrayendo el **segundo** índice; la base $\hat g_i$ lo hace contrayendo el **primero**. La inversa $[g]$ ya no es la transpuesta (sistema no ortogonal), sino $[t]^{-1}=c_{ji}/|t|$. Esta es la mitad "contravariante" del cuadro; la otra mitad —las componentes covariantes $v_i$ y la base dual $\hat g^i$— está en [[Transformaciones Covariantes]].

> [!referencia]
> - El reverso simétrico: [[Transformaciones Covariantes]].
> - El convenio arriba/abajo de los índices de $[t]$: [[Notacion Subindices Superindices]].
> - Caso ortonormal donde $[a]^{-1}=[a]^{\mathsf T}$: [[4 Introduccion a Tensores/Transformaciones entre Sistemas/Matriz de Transformacion]].
> - La métrica que baja índices dentro de un mismo sistema: [[Metrica/Tensor Metrico]].
