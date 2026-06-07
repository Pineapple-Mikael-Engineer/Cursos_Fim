---
title: Transformaciones Vectoriales Cartesianas
tags:
  - analisis-tensorial
  - teoria
  - tensores
  - transformaciones
draft: false
aliases:
  - transformaciones vectoriales cartesianas
  - rotacion de sistema cartesiano
  - cambio de base por rotacion
  - cartesian vector transformations
---

# Transformaciones Vectoriales Cartesianas

> [!definicion]
> Si un sistema **primado** está rotado un ángulo $\theta_0$ respecto a uno **no primado** (mismo origen, plano $1$-$2$), el mismo vector $\vec v=v_i\hat e_i=v'_i\hat e'_i$ tiene componentes relacionadas por
> $$v'_1=v_1\cos\theta_0+v_2\operatorname{sen}\theta_0,\qquad v'_2=-v_1\operatorname{sen}\theta_0+v_2\cos\theta_0.$$
> En forma matricial $[v']=[a][v]$, con la **matriz de rotación**
> $$[a]=\begin{pmatrix}\cos\theta_0&\operatorname{sen}\theta_0\\-\operatorname{sen}\theta_0&\cos\theta_0\end{pmatrix}.$$

> [!info]
> Es la sección **4.3.1** del [[index | capítulo 4.3]] (libro, cap. 4.3.1). Es el caso más simple de transformación: una rotación rígida del sistema en el plano. Generaliza a la [[Matriz de Transformacion | matriz $[a]$]] en $n$ dimensiones y, con un factor $a$ por índice, a las [[Transformaciones Tensoriales]].

> [!info] Sistema primado rotado un ángulo $\theta_0$
> ![[sistemas_rotados.svg|360]]
>
> Sistema primado rotado un ángulo $\theta_0$ respecto al no primado; el vector $\vec v$ es el mismo, cambian sus componentes.

---

## Ejemplo

> [!ejemplo]
> **Rotar el sistema $30^\circ$.** Sea $\vec v$ con componentes $(v_1,v_2)=(2,1)$ en el sistema no primado, y un sistema primado rotado $\theta_0=30^\circ$ ($\cos 30^\circ=\tfrac{\sqrt3}{2}\approx0.866$, $\operatorname{sen}30^\circ=\tfrac12$). Las componentes en el sistema primado son
> $$v'_1=2\cdot\tfrac{\sqrt3}{2}+1\cdot\tfrac12=\sqrt3+\tfrac12\approx2.232,$$
> $$v'_2=-2\cdot\tfrac12+1\cdot\tfrac{\sqrt3}{2}=-1+\tfrac{\sqrt3}{2}\approx-0.134.$$
> **Verificación (la magnitud es invariante):**
> $$v_1^2+v_2^2=2^2+1^2=5,\qquad v'^2_1+v'^2_2\approx2.232^2+(-0.134)^2\approx4.98+0.02=5.\ \checkmark$$
> La longitud de $\vec v$ no cambió, como debe ser: solo cambió su descripción al rotar la base.

---

## En qué consiste

> [!teorema] Componentes bajo rotación
> Para un sistema primado rotado $\theta_0$ respecto al no primado en el plano $1$-$2$,
> $$v'_1=v_1\cos\theta_0+v_2\operatorname{sen}\theta_0,\qquad v'_2=-v_1\operatorname{sen}\theta_0+v_2\cos\theta_0.$$

> [!demostracion]
> Partimos de que el vector es el mismo objeto, $\vec v=v'_i\hat e'_i$, de modo que cada componente primada es la **proyección** de $\vec v$ sobre el eje primado correspondiente: $v'_i=\vec v\cdot\hat e'_i$.
>
> **Paso 1 — Expresar la base primada en la no primada.** Al rotar el sistema un ángulo $\theta_0$, los versores primados son
> $$\hat e'_1=\cos\theta_0\,\hat e_1+\operatorname{sen}\theta_0\,\hat e_2,\qquad \hat e'_2=-\operatorname{sen}\theta_0\,\hat e_1+\cos\theta_0\,\hat e_2.$$
> ($\hat e'_1$ forma ángulo $\theta_0$ con $\hat e_1$; $\hat e'_2$ es $\hat e'_1$ girado otros $90^\circ$.)
>
> **Paso 2 — Proyectar $\vec v$ sobre $\hat e'_1$.** Con $\vec v=v_1\hat e_1+v_2\hat e_2$ y usando $\hat e_i\cdot\hat e_j=\delta_{ij}$,
> $$v'_1=\vec v\cdot\hat e'_1=(v_1\hat e_1+v_2\hat e_2)\cdot(\cos\theta_0\,\hat e_1+\operatorname{sen}\theta_0\,\hat e_2)=v_1\cos\theta_0+v_2\operatorname{sen}\theta_0.$$
>
> **Paso 3 — Proyectar $\vec v$ sobre $\hat e'_2$.** Análogamente,
> $$v'_2=\vec v\cdot\hat e'_2=(v_1\hat e_1+v_2\hat e_2)\cdot(-\operatorname{sen}\theta_0\,\hat e_1+\cos\theta_0\,\hat e_2)=-v_1\operatorname{sen}\theta_0+v_2\cos\theta_0.$$
>
> **Paso 4 — Forma matricial.** Apilando ambas como $[v']=[a][v]$ se lee directamente
> $$[a]=\begin{pmatrix}\cos\theta_0&\operatorname{sen}\theta_0\\-\operatorname{sen}\theta_0&\cos\theta_0\end{pmatrix}.\qquad\blacksquare$$

> [!info] Lectura geométrica
> Las filas de $[a]$ son las proyecciones de los **ejes primados sobre los no primados**: la fila $i$ son los cosenos directores de $\hat e'_i$. Por eso $a_{ij}=(\hat e'_i\cdot\hat e_j)$, identidad que se generaliza en [[Matriz de Transformacion]]. La matriz es **ortogonal**: $[a][a]^\dagger=[1]$, lo que garantiza que $|\vec v|$ se conserve.

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Situación | sistema primado rotado $\theta_0$ en el plano $1$-$2$ |
> | Invariante | el vector $\vec v=v_i\hat e_i=v'_i\hat e'_i$ (y su magnitud) |
> | Componente $1$ | $v'_1=v_1\cos\theta_0+v_2\operatorname{sen}\theta_0$ |
> | Componente $2$ | $v'_2=-v_1\operatorname{sen}\theta_0+v_2\cos\theta_0$ |
> | Matriz | $[a]=\begin{pmatrix}\cos\theta_0&\operatorname{sen}\theta_0\\-\operatorname{sen}\theta_0&\cos\theta_0\end{pmatrix}$ |
> | Origen de $a_{ij}$ | proyección $a_{ij}=\hat e'_i\cdot\hat e_j$ |

> [!corolario]
> La rotación plana es el prototipo de toda transformación ortonormal: las nuevas componentes son combinaciones lineales de las viejas con coeficientes $a_{ij}=\hat e'_i\cdot\hat e_j$. Generalizar este caso a $n$ dimensiones da la [[Matriz de Transformacion | matriz de transformación]] $v'_i=a_{ij}v_j$; aplicar la misma idea un índice a la vez da las [[Transformaciones Tensoriales]].

> [!referencia]
> - Matriz $[a]$ general y sus propiedades: [[Matriz de Transformacion]].
> - Transformación de tensores de rango $\geq2$: [[Transformaciones Tensoriales]].
> - Marco de la sección: [[index | Transformaciones entre Sistemas]].
