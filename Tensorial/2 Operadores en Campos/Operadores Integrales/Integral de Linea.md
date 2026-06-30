---
title: Integral de Linea
order: 1
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

> [!info] Integral de línea
> ![[integral_linea.svg|330]]
>
> $d\vec r$ es tangente al camino $C$ en cada punto; la integral $\int_C d\vec r\cdot\vec F$ acumula a lo largo de $C$.

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

## Ejemplo

> [!ejemplo]
> **Parametrización completa de $\vec F=(x^2,\,xy,\,0)$ sobre un arco de parábola.** Calculamos $\int_C d\vec r\cdot\vec F$ a lo largo del arco $y=x^2$ desde $A=(0,0)$ hasta $B=(1,1)$.
>
> **Paso 1 — parametrizar el camino.** Tomamos $x=t$ como parámetro, de modo que $y=t^2$, $z=0$, con $t:0\to1$:
> $$\vec r(t)=(t,\,t^2,\,0),\qquad d\vec r=\dot{\vec r}\,dt=(1,\,2t,\,0)\,dt\ \Rightarrow\ dx=dt,\ dy=2t\,dt.$$
>
> **Paso 2 — evaluar el campo sobre el camino.** Sustituyendo $x=t$, $y=t^2$:
> $$F_x=x^2=t^2,\qquad F_y=xy=t\cdot t^2=t^3,\qquad F_z=0.$$
>
> **Paso 3 — formar el integrando $d\vec r\cdot\vec F=dx_i\,F_i$.**
> $$d\vec r\cdot\vec F=F_x\,dx+F_y\,dy=t^2\,(dt)+t^3\,(2t\,dt)=(t^2+2t^4)\,dt.$$
>
> **Paso 4 — integrar en $t$.**
> $$\int_C d\vec r\cdot\vec F=\int_0^1 (t^2+2t^4)\,dt=\Big[\tfrac{t^3}{3}+\tfrac{2t^5}{5}\Big]_0^1=\frac13+\frac25=\frac{11}{15}\approx 0{,}733.$$
>
> El rotor $\vec\nabla\times\vec F=(\partial_x(xy)-\partial_y(x^2))\hat{e}_z=y\,\hat{e}_z\neq 0$, así que el campo **tampoco** es conservativo y el valor $11/15$ depende del arco elegido.

---

## En qué consiste

> [!teoria]
> Como la ecuación $W=\int_C d\vec r\cdot\vec F$ está escrita en notación vectorial, vale en cualquier sistema de coordenadas. En cartesianas $d\vec r=dx_i\hat{e}_i$, y desarrollando el producto punto con $\vec F=F_i\hat{e}_i$ y $\hat{e}_i\cdot\hat{e}_j=\delta_{ij}$:
> $$\int_C d\vec r\cdot\vec F=\int_C dx_i\hat{e}_i\cdot F_j\hat{e}_j=\int_C dx_i\,F_j\,\delta_{ij}=\int_C dx_i\,F_i.$$
> El índice $i$ queda repetido y sumado, así que el resultado es un **escalar**. En la práctica se parametriza $C$ por $\vec r(t)$, se sustituyen $x_i(t)$ y $dx_i=\dot x_i\,dt$, y queda una integral ordinaria en $t$.

> [!teorema] Paso a índices
> $$\int_C d\vec r\cdot\vec F=\int_C dx_i\,F_i.$$

> [!demostracion]
> Partimos del desplazamiento diferencial expresado en la base cartesiana.
>
> **Paso 1 — escribir $d\vec r$ y $\vec F$ en índices.** En cartesianas, con base ortonormal independiente de la posición,
> $$d\vec r=dx_i\,\hat{e}_i,\qquad \vec F=F_j\,\hat{e}_j.$$
> Los índices $i$ y $j$ son **mudos e independientes** (no comparten nombre todavía).
>
> **Paso 2 — formar el producto punto.** Por linealidad del producto escalar y como las constantes $dx_i$, $F_j$ salen del producto entre versores,
> $$d\vec r\cdot\vec F=(dx_i\,\hat{e}_i)\cdot(F_j\,\hat{e}_j)=dx_i\,F_j\,(\hat{e}_i\cdot\hat{e}_j).$$
>
> **Paso 3 — aplicar la ortonormalidad $\hat{e}_i\cdot\hat{e}_j=\delta_{ij}$.** La delta de Kronecker iguala los índices, $\delta_{ij}F_j=F_i$:
> $$d\vec r\cdot\vec F=dx_i\,F_j\,\delta_{ij}=dx_i\,F_i.$$
>
> **Paso 4 — integrar.** El operador integral es lineal y actúa término a término, de modo que
> $$\int_C d\vec r\cdot\vec F=\int_C dx_i\,F_i=\int_C\big(F_1\,dx_1+F_2\,dx_2+F_3\,dx_3\big),$$
> con $i$ repetido y sumado: el resultado es un escalar. $\blacksquare$

> [!teorema] Independencia del camino (campo conservativo)
> Si $\vec\nabla\times\vec F=0$ en una región simplemente conexa, entonces $\int_C d\vec r\cdot\vec F$ **no depende del camino** $C$, sólo de sus extremos $A$ y $B$; equivalentemente, $\oint_C d\vec r\cdot\vec F=0$ sobre todo camino cerrado.

> [!demostracion]
> **Paso 1 — comparar dos caminos.** Sean $C_1$ y $C_2$ dos caminos de $A$ a $B$. Recorrer $C_1$ hacia adelante y $C_2$ hacia atrás forma un **camino cerrado** $C=C_1-C_2$, de modo que
> $$\int_{C_1}d\vec r\cdot\vec F-\int_{C_2}d\vec r\cdot\vec F=\oint_{C}d\vec r\cdot\vec F.$$
>
> **Paso 2 — convertir la circulación en flujo del rotor.** Por el [[../Teoremas Integrales/Teorema de Stokes | teorema de Stokes]], la circulación sobre $C$ iguala el flujo del rotor a través de cualquier superficie $S$ que tenga a $C$ por borde:
> $$\oint_{C}d\vec r\cdot\vec F=\int_S d\vec\sigma\cdot(\vec\nabla\times\vec F).$$
>
> **Paso 3 — anular por hipótesis.** Como $\vec\nabla\times\vec F=0$ en toda la región (y $S$ cabe en ella por ser simplemente conexa), el integrando es nulo y
> $$\oint_{C}d\vec r\cdot\vec F=0\ \Rightarrow\ \int_{C_1}d\vec r\cdot\vec F=\int_{C_2}d\vec r\cdot\vec F.$$
> La integral depende sólo de $A$ y $B$. En tal caso existe un potencial $\Phi$ con $\vec F=-\vec\nabla\Phi$ y $\int_C d\vec r\cdot\vec F=\Phi(A)-\Phi(B)$. $\blacksquare$

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
