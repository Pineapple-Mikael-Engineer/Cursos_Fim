---
title: Rotor
order: 3
tags:
  - analisis-tensorial
  - teoria
  - calculo-vectorial
  - rotor
draft: false
aliases:
  - rotor
  - rotacional
  - nabla cruz A
  - circulacion
  - curl
---

# Rotor $\vec\nabla\times\vec A$

> [!definicion]
> El **rotor** de un campo vectorial $\vec A$ es el vector
> $$\vec\nabla\times\vec A=\varepsilon_{ijk}\frac{\partial A_j}{\partial x_i}\hat{e}_k.$$
> Describe, en escala **local**, la **circulación** del campo. Si $\vec v$ sólo depende de $x,y$, el rotor apunta en $z$:
> $$\vec\nabla\times\vec v=\left(\frac{\partial v_y}{\partial x}-\frac{\partial v_x}{\partial y}\right)\hat{e}_z.$$

> [!info]
> Sección **2.3.3** del libro, dentro de [[index | operadores diferenciales]]. Se obtiene por **producto cruz** $\vec\nabla\times\vec A$, escrito con el [[1 Algebra Lineal y Notacion/Simbolos Especiales/Simbolo Levi-Civita | símbolo de Levi-Civita]] $\varepsilon_{ijk}$. Su interpretación —circulación por unidad de área— se conecta con el teorema de Stokes en [[Teoremas Integrales/index | teoremas integrales]].

---

## Ejemplo

> [!ejemplo] Rotor: sólido rígido vs vórtice
> ![[rotor_vortice_vs_rigido.svg|540]]
>
> Ambos campos parecen circulares, pero el sólido rígido $(-y,x)$ tiene rotor $2\hat e_z$ y el vórtice $(-y,x)/r^2$ tiene rotor cero (salvo el origen).

> [!ejemplo]
> **Rotación rígida frente a vórtice $1/r^2$.**
>
> *Campo rígido* $\vec v=(-y,\,x,\,0)$ (gira como un sólido). En 2D:
> $$\vec\nabla\times\vec v=\left(\frac{\partial x}{\partial x}-\frac{\partial(-y)}{\partial y}\right)\hat{e}_z=(1-(-1))\hat{e}_z=2\,\hat{e}_z.$$
> Rotor constante no nulo: hay circulación local en cada punto.
>
> *Campo tipo vórtice* $\vec v=\dfrac{(-y,\,x,\,0)}{x^2+y^2}$, con $|\vec v|\propto 1/r$. Calculando (para $r\neq0$):
> $$\frac{\partial v_y}{\partial x}=\frac{y^2-x^2}{(x^2+y^2)^2},\qquad\frac{\partial v_x}{\partial y}=\frac{y^2-x^2}{(x^2+y^2)^2}\;\Rightarrow\;\vec\nabla\times\vec v=0.$$
> Las líneas son **círculos** (campo "curvado") y aun así el rotor es **cero** salvo en el origen: el decaimiento $1/r$ compensa exactamente la curvatura. Esto ilustra que el rotor mide circulación **local**, no macroscópica.

---

## En qué consiste

> [!teoria]
> "Rotor distinto de cero" no significa "líneas curvadas": un campo de líneas curvas puede tener rotor cero (vórtice $1/r$) y un campo de líneas rectas puede tener rotor no nulo (si su magnitud varía de un lado a otro). Para resolver la confusión hay que mirar el rotor en su escala correcta: la circulación alrededor de un camino que se encoge a un punto.

> [!teorema] El rotor como circulación por unidad de área
> La componente del rotor normal a una superficie es la integral de línea del campo alrededor de su borde, por unidad de área, en el límite infinitesimal:
> $$\hat{e}_z\cdot(\vec\nabla\times\vec v)=\lim_{C,S\to0}\frac{\oint_C d\vec r\cdot\vec v}{\int_S d\sigma_z}.$$

> [!ejemplo] Camino para la circulación
> ![[rotor_circulacion.svg|340]]
>
> La integral de línea $\oint_C d\vec r\cdot\vec v$ se calcula sobre el camino rectangular $C_1\!\to\!C_4$ de lados $\Delta x,\Delta y$.

> [!demostracion]
> Tomamos el rectángulo de la figura 2.9, de lados $\Delta x\times\Delta y$ con vértice en $(x_0,y_0)$, recorrido en sentido antihorario por cuatro tramos $C_1$ (abajo), $C_2$ (derecha), $C_3$ (arriba) y $C_4$ (izquierda). La circulación es $\oint_C d\vec r\cdot\vec v$.
>
> **Paso 1 — tramo $C_1$ ($y=y_0$, $x:x_0\to x_0+\Delta x$).**
> $$\int_{C_1}d\vec r\cdot\vec v=\int_{x_0}^{x_0+\Delta x}v_x(x,y_0)\,dx.$$
> Taylor de $v_x$ a primer orden en $x$:
> $$v_x(x,y_0)\approx v_x(x_0,y_0)+\left.\frac{\partial v_x}{\partial x}\right|_{(x_0,y_0)}(x-x_0),$$
> e integrando:
> $$\int_{C_1}d\vec r\cdot\vec v\approx v_x(x_0,y_0)\,\Delta x+\frac12\left.\frac{\partial v_x}{\partial x}\right|_{(x_0,y_0)}(\Delta x)^2.$$
>
> **Paso 2 — tramo $C_3$ ($y=y_0+\Delta y$, $x:x_0+\Delta x\to x_0$).** El sentido invierte los límites. Taylor de $v_x$ ahora en $x$ **y** en $y$:
> $$v_x(x,y_0+\Delta y)\approx v_x(x_0,y_0)+\left.\frac{\partial v_x}{\partial x}\right|(x-x_0)+\left.\frac{\partial v_x}{\partial y}\right|\Delta y,$$
> e integrando de $x_0+\Delta x$ a $x_0$:
> $$\int_{C_3}d\vec r\cdot\vec v\approx -v_x(x_0,y_0)\,\Delta x-\frac12\left.\frac{\partial v_x}{\partial x}\right|(\Delta x)^2-\left.\frac{\partial v_x}{\partial y}\right|\Delta x\,\Delta y.$$
>
> **Paso 3 — suma $C_1+C_3$.** Los términos en $v_x(x_0,y_0)\Delta x$ y en $(\Delta x)^2$ se cancelan, dejando
> $$\int_{C_1}d\vec r\cdot\vec v+\int_{C_3}d\vec r\cdot\vec v\approx-\left.\frac{\partial v_x}{\partial y}\right|_{(x_0,y_0)}\Delta x\,\Delta y.$$
>
> **Paso 4 — tramos $C_2$ y $C_4$.** El procedimiento análogo sobre los tramos verticales (Taylor de $v_y$ en $x$ e $y$) da
> $$\int_{C_2}d\vec r\cdot\vec v+\int_{C_4}d\vec r\cdot\vec v\approx+\left.\frac{\partial v_y}{\partial x}\right|_{(x_0,y_0)}\Delta x\,\Delta y.$$
>
> **Paso 5 — circulación total.** Sumando los cuatro tramos:
> $$\oint_C d\vec r\cdot\vec v\approx\left(\frac{\partial v_y}{\partial x}-\frac{\partial v_x}{\partial y}\right)\Delta x\,\Delta y.$$
>
> **Paso 6 — límite.** El error se anula cuando $\Delta x,\Delta y\to0$. El paréntesis es la componente $z$ del rotor (definición 2D), y $\int_S d\sigma_z=\Delta x\,\Delta y$ el área. Por tanto
> $$\lim_{C\to0}\oint_C d\vec r\cdot\vec v=\hat{e}_z\cdot(\vec\nabla\times\vec v)\lim_{S\to0}\int_S d\sigma_z,$$
> o bien
> $$\hat{e}_z\cdot(\vec\nabla\times\vec v)=\lim_{C,S\to0}\frac{\oint_C d\vec r\cdot\vec v}{\int_S d\sigma_z}.\qquad\blacksquare$$

> [!info] Generalización 3D
> La derivación se hizo en 2D para la componente $z$. Para cualquier orientación del camino diferencial,
> $$\lim_{C\to0}\oint_C d\vec r\cdot\vec v=(\vec\nabla\times\vec v)\cdot\lim_{S\to0}\int_S d\vec\sigma.$$
> El rotor mide la circulación **local**: por eso el vórtice $1/r$ del ejemplo, pese a tener líneas circulares, da rotor cero (la integral alrededor de cualquier camito que no encierre el origen se anula).

## Resumen

> [!resumen]
> | Aspecto | Expresión |
> |---|---|
> | Definición | $\vec\nabla\times\vec A=\varepsilon_{ijk}(\partial A_j/\partial x_i)\hat{e}_k$ |
> | En 2D | $(\partial v_y/\partial x-\partial v_x/\partial y)\,\hat{e}_z$ |
> | Significado | circulación por unidad de área (local) |
> | Forma integral | $\hat{e}_z\cdot(\vec\nabla\times\vec v)=\lim\dfrac{\oint_C d\vec r\cdot\vec v}{\int_S d\sigma_z}$ |
> | Cuidado | líneas curvas $\not\Rightarrow$ rotor $\neq0$ |

> [!corolario]
> El rotor es la densidad de circulación: el límite del cociente entre la integral de línea sobre un camito cerrado y el área que encierra. Es la cara infinitesimal del teorema de Stokes (ver [[Teoremas Integrales/index]]) y, junto con la divergencia, caracteriza por completo un campo vectorial (descomposición de Helmholtz).

> [!referencia]
> - Símbolo de Levi-Civita: [[1 Algebra Lineal y Notacion/Simbolos Especiales/Simbolo Levi-Civita]].
> - Operadores hermanos: [[Gradiente]], [[Divergencia]].
> - Rotor del rotor $\vec\nabla\times\vec\nabla\times\vec v$: [[Identidades Operadores]].
