---
title: Gradiente
tags:
  - analisis-tensorial
  - teoria
  - calculo-vectorial
  - gradiente
draft: false
aliases:
  - gradiente
  - nabla phi
  - gradient
---

# Gradiente $\vec\nabla\Phi$

> [!definicion]
> El **gradiente** de un campo escalar $\Phi$ es el vector
> $$\vec\nabla\Phi=\hat{e}_i\frac{\partial\Phi}{\partial x_i}=\frac{\partial\Phi}{\partial x}\hat{e}_x+\frac{\partial\Phi}{\partial y}\hat{e}_y+\frac{\partial\Phi}{\partial z}\hat{e}_z.$$
> Describe, en cada punto, cómo cambia $\Phi$ con la posición. Su propiedad geométrica clave: **apunta en la dirección de máximo crecimiento de $\Phi$ y es perpendicular a las superficies $\Phi=$ cte**.

> [!info]
> Sección **2.3.1** del libro, dentro de [[index | operadores diferenciales]]. Es el operador que liga un campo escalar con uno vectorial: convierte las equipotenciales de los [[Campos Escalares y Vectoriales | campos]] en líneas de campo perpendiculares. Su inverso en escala finita es la integral de línea (ver [[Operadores Integrales/index | operadores integrales]]).

> [!info] El gradiente es normal
> ![[gradiente_normal.svg|380]]
>
> $\vec\nabla\Phi$ apunta perpendicular a las superficies $\Phi=$ cte, en el sentido de mayor crecimiento.

---

## Ejemplo

> [!ejemplo]
> **El potencial $\Phi=-xy$** (figura 2.4 del libro). El gradiente es
> $$\vec\nabla\Phi=-y\,\hat{e}_x-x\,\hat{e}_y.$$
>
> **Movimiento sobre el eje $x$ desde $(1,2)$.** Con $d\vec r=dr\,\hat{e}_x$:
> $$d\Phi=\vec\nabla\Phi\cdot d\vec r=(-2\,\hat{e}_x-1\,\hat{e}_y)\cdot(dr\,\hat{e}_x)=-2\,dr.$$
> $\Phi$ disminuye 2 unidades por cada paso infinitesimal en esa dirección.
>
> **Movimiento a $45^\circ$ desde $(3,4)$.** Con $d\vec r=\dfrac{dr}{\sqrt2}(\hat{e}_x+\hat{e}_y)$:
> $$d\Phi=(-4\,\hat{e}_x-3\,\hat{e}_y)\cdot\frac{dr}{\sqrt2}(\hat{e}_x+\hat{e}_y)=-\frac{7}{\sqrt2}\,dr.$$
>
> **Cambio finito.** Sobre un camino $C$ donde el gradiente varía punto a punto se integra:
> $$\Delta\Phi=\int_C d\vec r\cdot\vec\nabla\Phi.$$

---

## En qué consiste

> [!teoria]
> El gradiente nace al aplicar **producto punto** a la definición $\vec\nabla=\hat{e}_i\partial/\partial x_i$ con un desplazamiento $d\vec r=dx_i\,\hat{e}_i$. Eso produce la diferencia total de $\Phi$, que es la propiedad fundamental del operador.

> [!teorema] El gradiente es normal a las superficies $\Phi=$ cte
> El cambio infinitesimal de un campo escalar al desplazarse $d\vec r$ es
> $$d\Phi=\vec\nabla\Phi\cdot d\vec r,$$
> de donde $d\Phi$ es **máximo** cuando $d\vec r\parallel\vec\nabla\Phi$ y **nulo** cuando $d\vec r\perp\vec\nabla\Phi$. Por tanto el gradiente apunta hacia el máximo crecimiento de $\Phi$ y es perpendicular a las superficies $\Phi=$ cte.

> [!demostracion]
> **Paso 1.** Aplicamos producto punto con $d\vec r=dx_i\,\hat{e}_i$ a ambos lados de $\vec\nabla\Phi=\hat{e}_j\,\partial\Phi/\partial x_j$:
> $$d\vec r\cdot\vec\nabla\Phi=dx_i\,\hat{e}_i\cdot\hat{e}_j\frac{\partial\Phi}{\partial x_j}.$$
>
> **Paso 2.** Usamos la ortonormalidad de la base, $\hat{e}_i\cdot\hat{e}_j=\delta_{ij}$, y la delta de Kronecker colapsa la suma fijando $j=i$:
> $$d\vec r\cdot\vec\nabla\Phi=\delta_{ij}\frac{\partial\Phi}{\partial x_j}dx_i=\frac{\partial\Phi}{\partial x_i}dx_i.$$
>
> **Paso 3.** El lado derecho es exactamente la **diferencial total** de $\Phi$ por la regla de la cadena, $d\Phi=\dfrac{\partial\Phi}{\partial x_i}dx_i$. En notación vectorial:
> $$\boxed{d\Phi=\vec\nabla\Phi\cdot d\vec r.}$$
>
> **Paso 4.** Escribiendo $d\Phi=|\vec\nabla\Phi|\,|d\vec r|\cos\theta$, con $\theta$ el ángulo entre $\vec\nabla\Phi$ y $d\vec r$: para $|d\vec r|$ fijo, $d\Phi$ es máximo en $\theta=0$ (desplazamiento paralelo al gradiente) y nulo en $\theta=\pi/2$. Un desplazamiento **sobre** la superficie $\Phi=$ cte tiene $d\Phi=0$, luego es perpendicular a $\vec\nabla\Phi$: el gradiente es **normal** a las superficies de nivel. $\blacksquare$

> [!info] Campo eléctrico
> Al usar el gradiente para generar un campo vectorial suele añadirse un signo negativo. El campo eléctrico se obtiene del potencial electrostático por
> $$\vec E=-\vec\nabla\Phi,$$
> convención con la que, moviéndose **en contra** de las líneas de campo, $\Phi$ aumenta. Para $\Phi=-xy$ esto da $-\vec\nabla\Phi=y\,\hat{e}_x+x\,\hat{e}_y$, cuyas líneas $y^2-x^2=c$ son perpendiculares a las equipotenciales (figura 2.5).

## Resumen

> [!resumen]
> | Aspecto | Expresión |
> |---|---|
> | Definición | $\vec\nabla\Phi=\hat{e}_i\,\partial\Phi/\partial x_i$ |
> | Propiedad clave | $d\Phi=\vec\nabla\Phi\cdot d\vec r$ |
> | Dirección | máximo crecimiento de $\Phi$ |
> | Geometría | normal a las superficies $\Phi=$ cte |
> | Cambio finito | $\Delta\Phi=\int_C d\vec r\cdot\vec\nabla\Phi$ |
> | Uso físico | $\vec E=-\vec\nabla\Phi$ |

> [!corolario]
> El gradiente es la derivada direccional empaquetada en un vector: $d\Phi=\vec\nabla\Phi\cdot d\vec r$ contiene toda la variación local de $\Phi$. De ahí se sigue que es normal a las equipotenciales, lo que explica la perpendicularidad $\vec E\perp$ equipotenciales vista en los [[Campos Escalares y Vectoriales | campos]]. No tiene límite en el número de dimensiones.

> [!referencia]
> - Geometría de equipotenciales y líneas de campo: [[Campos Escalares y Vectoriales]].
> - Operadores hermanos: [[Divergencia]], [[Rotor]].
> - Definición integral del gradiente: [[Definiciones Integrales Operadores]].
