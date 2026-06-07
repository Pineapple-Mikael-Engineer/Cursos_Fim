---
title: Integral de Linea
tags:
  - analisis-tensorial
  - teoria
  - calculo-vectorial
  - operadores-integrales
  - integral-de-linea
draft: false
aliases:
  - integral de linea
  - trabajo
  - circulacion
  - line integral
---

# Integral de Linea $\int_C d\vec r$

> [!definicion]
> La **integral de línea** suma una cantidad a lo largo de un camino $C$. Su caso central es el **trabajo** de una fuerza $\vec F$,
> $$W=\int_C d\vec r\cdot\vec F=\int_C dx_i\,F_i,$$
> un **escalar** (el índice $i$ está sumado). El desplazamiento diferencial $d\vec r=dx_i\hat{e}_i$ es tangente a $C$ en cada punto. Si el camino se cierra sobre sí mismo se escribe $\oint_C d\vec r$ y la integral se llama **circulación**.

> [!info]
> Sección **2.2.2** del libro; primera hija de [[index | Operadores Integrales]] (cap. 2.2). El integrando es un [[Campos Escalares y Vectoriales | campo]] vectorial o escalar. Cuando $\vec F=-\vec\nabla\Phi$ deriva de un potencial, la integral se relaciona con el [[Operadores Diferenciales/Gradiente | gradiente]] vía $\Delta\Phi=\int_C d\vec r\cdot\vec\nabla\Phi$, y con el [[Teoremas Integrales/Teorema de Stokes | teorema de Stokes]] cuando el camino es cerrado.

---

## Ejemplo

> [!ejemplo]
> **Trabajo del campo $\vec F=(-y,\,x,\,0)$ y dependencia del camino.** Calculamos $W=\int_C d\vec r\cdot\vec F=\int_C(F_x\,dx+F_y\,dy)$ entre $A=(1,0)$ y $B=(0,1)$ por dos caminos.
>
> **Camino 1: cuarto de circunferencia** $\vec r(t)=(\cos t,\,\operatorname{sen} t)$, $t:0\to\pi/2$. Entonces $dx=-\operatorname{sen} t\,dt$, $dy=\cos t\,dt$, y sobre el camino $F_x=-y=-\operatorname{sen} t$, $F_y=x=\cos t$:
> $$d\vec r\cdot\vec F=(-\operatorname{sen} t)(-\operatorname{sen} t\,dt)+(\cos t)(\cos t\,dt)=(\operatorname{sen}^2 t+\cos^2 t)\,dt=dt.$$
> $$W_1=\int_0^{\pi/2}dt=\frac{\pi}{2}\approx 1{,}571.$$
>
> **Camino 2: segmento recto** de $A$ a $B$, $\vec r(t)=(1-t,\,t)$, $t:0\to1$. Aquí $dx=-dt$, $dy=dt$, $F_x=-y=-t$, $F_y=x=1-t$:
> $$d\vec r\cdot\vec F=(-t)(-dt)+(1-t)(dt)=(t+1-t)\,dt=dt.$$
> $$W_2=\int_0^1 dt=1.$$
>
> Como $W_1=\pi/2\neq 1=W_2$, **el trabajo depende del camino**: este campo no es conservativo. En efecto, $\vec\nabla\times\vec F=(\partial_x x-\partial_y(-y))\hat{e}_z=2\,\hat{e}_z\neq 0$, así que no existe potencial $\Phi$ con $\vec F=-\vec\nabla\Phi$.
>
> **Circulación cerrada.** Sobre la circunferencia unidad completa $\vec r(t)=(\cos t,\operatorname{sen} t)$, $t:0\to2\pi$, el mismo integrando da $dt$, luego
> $$\oint_C d\vec r\cdot\vec F=\int_0^{2\pi}dt=2\pi\neq 0,$$
> lo que vuelve a confirmar que el campo tiene circulación no nula (rotor $\neq 0$).

---

## En qué consiste

> [!teoria]
> Como la ecuación $W=\int_C d\vec r\cdot\vec F$ está escrita en notación vectorial, vale en cualquier sistema de coordenadas. En cartesianas $d\vec r=dx_i\hat{e}_i$, y desarrollando el producto punto con $\vec F=F_i\hat{e}_i$ y $\hat{e}_i\cdot\hat{e}_j=\delta_{ij}$:
> $$\int_C d\vec r\cdot\vec F=\int_C dx_i\hat{e}_i\cdot F_j\hat{e}_j=\int_C dx_i\,F_j\,\delta_{ij}=\int_C dx_i\,F_i.$$
> El índice $i$ queda repetido y sumado, así que el resultado es un **escalar**. En la práctica se parametriza $C$ por $\vec r(t)$, se sustituyen $x_i(t)$ y $dx_i=\dot x_i\,dt$, y queda una integral ordinaria en $t$.

> [!proposicion] Operaciones menos comunes
> El operador integral de línea también puede actuar de otras formas que **no** son productos punto:
> $$\int_C d\vec r\,\Phi=\hat{e}_i\int_C dx_i\,\Phi\quad(\text{produce un vector}),$$
> $$\int_C d\vec r\times\vec v=\hat{e}_k\int_C dx_i\,\varepsilon_{ijk}\,v_j\quad(\text{produce un vector, vía producto cruz}).$$
> En ambos, los versores $\hat{e}_i$, $\hat{e}_k$ salen de la integral porque la base cartesiana es ortonormal e **independiente de la posición**.

> [!info] Lectura geométrica
> $d\vec r\cdot\vec F=|d\vec r|\,|\vec F|\cos\theta$ retiene solo la componente de $\vec F$ **tangente** al camino. Una fuerza perpendicular al desplazamiento no realiza trabajo. Si $\vec F=-\vec\nabla\Phi$, entonces $\int_C d\vec r\cdot\vec F=-\Delta\Phi=\Phi(A)-\Phi(B)$ depende solo de los extremos, y la circulación cerrada se anula: el campo es **conservativo**.

## Resumen

> [!resumen]
> | Operación | Fórmula en índices | Resultado |
> |---|---|---|
> | Trabajo / circulación | $\int_C d\vec r\cdot\vec F=\int_C dx_i\,F_i$ | escalar |
> | Camino cerrado | $\oint_C d\vec r\cdot\vec F$ | escalar (circulación) |
> | Sobre escalar | $\int_C d\vec r\,\Phi=\hat{e}_i\int_C dx_i\,\Phi$ | vector |
> | Producto cruz | $\int_C d\vec r\times\vec v=\hat{e}_k\int_C dx_i\,\varepsilon_{ijk}v_j$ | vector |

> [!corolario]
> La integral de línea proyecta el campo sobre la tangente del camino y lo acumula. Para un campo con rotor no nulo el resultado depende del camino (como $\vec F=(-y,x,0)$, con $W_1=\pi/2\neq W_2=1$); para un campo conservativo $\vec F=-\vec\nabla\Phi$ depende solo de los extremos y su circulación es nula. Esta distinción es la que cuantifica el [[Teoremas Integrales/Teorema de Stokes | teorema de Stokes]].

> [!referencia]
> - Forma de operador y reglas: [[index | Operadores Integrales]].
> - Hermanas: [[Integral de Superficie]], [[Integral de Volumen]].
> - Circulación y rotor: [[Operadores Diferenciales/Rotor]], [[Teoremas Integrales/Teorema de Stokes]].
