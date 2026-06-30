---
title: La Matriz de Transformación
order: 2
tags:
  - analisis-tensorial
  - teoria
  - tensores
  - transformaciones
  - matrices
draft: false
aliases:
  - matriz de transformacion
  - cosenos directores
  - matriz de cosenos directores
  - transformation matrix
---

# La Matriz de Transformación $a_{ij}$

> [!definicion]
> La **matriz de transformación** $[a]$ lleva las componentes de un vector del sistema no primado al primado,
> $$v'_i=a_{ij}v_j.$$
> Sus elementos se obtienen de dos formas equivalentes:
> $$a_{ij}=(\hat e'_i\cdot\hat e_j)\qquad(\text{cosenos directores}),\qquad a_{ij}=\frac{\partial x'_i}{\partial x_j}\qquad(\text{desde las coordenadas}).$$
> Para sistemas **ortonormales** es ortogonal: $[a][a]^\dagger=[1]$, de modo que $[a]^{-1}=[a]^\dagger$ y $a^{-1}_{ij}=a_{ji}$.

> [!info]
> Es la sección **4.3.2** del [[index | capítulo 4.3]] (libro, cap. 4.3.2). Generaliza la rotación de las [[Transformaciones Vectoriales Cartesianas]] a cualquier transformación lineal ortonormal en $n$ dimensiones, y sus propiedades (ortogonalidad, inversa = transpuesta) se usan tal cual en las [[Transformaciones Tensoriales]]. Usa el producto punto y la [[../../1 Algebra Lineal y Notacion/Simbolos Especiales/Delta Kronecker | delta de Kronecker]].

---

## Ejemplo

> [!ejemplo]
> **Construir $[a]$ desde las bases.** Tomemos en 2D un sistema primado rotado $\theta_0=60^\circ$: $\hat e'_1$ forma $60^\circ$ con $\hat e_1$ y $\hat e'_2$ forma $60^\circ$ con $\hat e_2$. Con $a_{nm}=(\hat e'_n\cdot\hat e_m)=\cos(\angle\,\hat e'_n,\hat e_m)$:
> $$a_{11}=\cos 60^\circ=\tfrac12,\quad a_{12}=\cos 30^\circ=\tfrac{\sqrt3}{2},\quad a_{21}=\cos 150^\circ=-\tfrac{\sqrt3}{2},\quad a_{22}=\cos 60^\circ=\tfrac12,$$
> que reproduce $[a]=\begin{pmatrix}\cos\theta_0&\operatorname{sen}\theta_0\\-\operatorname{sen}\theta_0&\cos\theta_0\end{pmatrix}$.
>
> **Verificar ortonormalidad** $a_{ij}a_{ik}=\delta_{jk}$ (suma sobre $i$, fila por fila):
> $$a_{i1}a_{i1}=\left(\tfrac12\right)^2+\left(-\tfrac{\sqrt3}{2}\right)^2=\tfrac14+\tfrac34=1=\delta_{11},$$
> $$a_{i1}a_{i2}=\tfrac12\cdot\tfrac{\sqrt3}{2}+\left(-\tfrac{\sqrt3}{2}\right)\cdot\tfrac12=\tfrac{\sqrt3}{4}-\tfrac{\sqrt3}{4}=0=\delta_{12}.\ \checkmark$$
> Entonces $[a]^{-1}=[a]^\dagger$ y la transformación inversa es $v_i=a_{ji}v'_j$.

---

## En qué consiste

> [!teorema] $[a]$ desde la base de vectores (cosenos directores)
> Si las dos bases ortonormales son conocidas,
> $$a_{nm}=(\hat e'_n\cdot\hat e_m).$$
> Los elementos de $[a]$ son los cosenos de los ángulos entre cada par de versores de ambos sistemas.

> [!demostracion]
> **Paso 1 — La ley vale para cualquier vector.** Como $v'_i=a_{ij}v_j$ rige las componentes de **todo** vector, y $\vec v=v_k\hat e_k=v'_i\hat e'_i$, sustituyendo $v'_i$ queda
> $$v_k\hat e_k=a_{ij}v_j\hat e'_i.$$
>
> **Paso 2 — Elegir $\vec v=\hat e_m$.** Tomando como vector uno de los versores no primados ($v_{k}=\delta_{km}$, es decir $v_j=\delta_{jm}$) se obtiene la transformación de la base:
> $$\hat e_m=a_{im}\hat e'_i.$$
>
> **Paso 3 — Proyectar con $\hat e'_n$.** Aplicando producto punto por $\hat e'_n$ y usando $\hat e'_i\cdot\hat e'_n=\delta_{in}$,
> $$\hat e'_n\cdot\hat e_m=a_{im}\,(\hat e'_i\cdot\hat e'_n)=a_{im}\delta_{in}=a_{nm}.$$
> Luego $a_{nm}=(\hat e'_n\cdot\hat e_m)$: cosenos directores. $\blacksquare$

> [!teorema] $[a]$ desde las ecuaciones de coordenadas
> Si se conocen las funciones $x'_i=x'_i(x_1,x_2,x_3)$ que relacionan los dos sistemas cartesianos,
> $$a_{ij}=\frac{\partial x'_i}{\partial x_j}.$$

> [!demostracion]
> **Paso 1 — El desplazamiento es un vector.** El vector desplazamiento se escribe en ambos sistemas como $d\vec r=dx_i\hat e_i=dx'_i\hat e'_i$. Como $v'_i=a_{ij}v_j$ vale para las componentes de **cualquier** vector, en particular
> $$dx'_i=a_{ij}\,dx_j.$$
>
> **Paso 2 — Diferencial total.** Por otro lado, de $x'_i=x'_i(x_1,x_2,x_3)$ la regla de la cadena da
> $$dx'_i=\frac{\partial x'_i}{\partial x_j}\,dx_j.$$
>
> **Paso 3 — Comparar.** Ambas expresiones valen para $dx_j$ arbitrarios, así que sus coeficientes coinciden:
> $$a_{ij}=\frac{\partial x'_i}{\partial x_j}.\qquad\blacksquare$$

> [!proposicion] Propiedad ortonormal e inversa
> Aplicando producto punto por $\hat e_k$ a $\hat e_j=a_{ij}\hat e'_i$ y usando $\hat e_j\cdot\hat e_k=\delta_{jk}$, $\hat e'_i\cdot\hat e_k=a_{ik}$:
> $$\delta_{jk}=a_{ij}a_{ik},\qquad\text{equivalente a }[a][a]^\dagger=[1].$$
> De aquí la inversa es la transpuesta (conjugada):
> $$[a]^{-1}=[a]^\dagger,\qquad a^{-1}_{ij}=a_{ji},$$
> y la transformación inversa de componentes es
> $$v_i=a_{ji}v'_j.$$

> [!info] Transformación de la base y patrón de índices
> Las cuatro relaciones de la sección quedan:
> $$v'_i=a_{ij}v_j,\qquad v_i=a_{ji}v'_j,\qquad \hat e'_i=a_{ij}\hat e_j,\qquad \hat e_i=a_{ji}\hat e'_i\ \ (\hat e_i=a_{ji}\hat e'_j).$$
> **Patrón:** del sistema **no primado al primado** se suma sobre el **segundo** índice de $a_{ij}$; del **primado al no primado** se suma sobre el **primero**. Nótese que las **componentes** y las **bases** usan índices opuestos: si $v'_i=a_{ij}v_j$, entonces $\hat e_i=a_{ji}\hat e'_j$.

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Definición | $v'_i=a_{ij}v_j$ |
> | Desde bases | $a_{ij}=(\hat e'_i\cdot\hat e_j)$ (cosenos directores) |
> | Desde coordenadas | $a_{ij}=\partial x'_i/\partial x_j$ |
> | Ortonormalidad | $a_{ij}a_{ik}=\delta_{jk}$, $[a][a]^\dagger=[1]$ |
> | Inversa | $[a]^{-1}=[a]^\dagger$, $a^{-1}_{ij}=a_{ji}$ |
> | Inversa de componentes | $v_i=a_{ji}v'_j$ |
> | Base | $\hat e'_i=a_{ij}\hat e_j$, $\hat e_i=a_{ji}\hat e'_j$ |

> [!corolario]
> Una **sola** matriz de cosenos directores $a_{ij}=\hat e'_i\cdot\hat e_j=\partial x'_i/\partial x_j$ codifica todo el cambio de sistema. Que sea ortogonal ($[a]^{-1}=[a]^\dagger$) es lo que vuelve triviales las inversas y conserva magnitudes y ángulos. Esta misma matriz, aplicada un índice a la vez, transforma tensores de cualquier rango en [[Transformaciones Tensoriales]].

> [!referencia]
> - Caso 2D que la motiva: [[Transformaciones Vectoriales Cartesianas]].
> - Uso con un factor $a$ por índice: [[Transformaciones Tensoriales]].
> - Versión en bases curvilíneas: [[Transformaciones en Curvilineas]].
