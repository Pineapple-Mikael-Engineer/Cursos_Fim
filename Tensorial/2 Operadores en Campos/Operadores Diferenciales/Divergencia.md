---
title: Divergencia
tags:
  - analisis-tensorial
  - teoria
  - calculo-vectorial
  - divergencia
draft: false
aliases:
  - divergencia
  - nabla punto A
  - ecuacion de continuidad
  - divergence
  - continuity equation
---

# Divergencia $\vec\nabla\cdot\vec A$

> [!definicion]
> La **divergencia** de un campo vectorial $\vec A$ es el escalar
> $$\vec\nabla\cdot\vec A=\frac{\partial A_i}{\partial x_i}=\frac{\partial A_x}{\partial x}+\frac{\partial A_y}{\partial y}+\frac{\partial A_z}{\partial z}.$$
> Mide el **flujo neto por unidad de volumen** que sale de un punto: si $\vec\nabla\cdot\vec A>0$ el punto es una **fuente** (las líneas nacen), si $<0$ un **sumidero** (mueren), si $=0$ las líneas pasan sin acumularse.

> [!info]
> Sección **2.3.2** del libro, dentro de [[index | operadores diferenciales]]. Se obtiene por **producto punto** $\vec\nabla\cdot\vec A$. Su interpretación física surge de la **ecuación de continuidad**, deducida más abajo, y su versión integral se conecta con el teorema de Gauss en [[Teoremas Integrales/index | teoremas integrales]]. Actúa sobre los [[Campos Escalares y Vectoriales | campos vectoriales]].

---

## Ejemplo

> [!ejemplo]
> **Fuente, sumidero y campo solenoidal.**
>
> *Campo radial* $\vec A=(x,y,z)$:
> $$\vec\nabla\cdot\vec A=\frac{\partial x}{\partial x}+\frac{\partial y}{\partial y}+\frac{\partial z}{\partial z}=3>0.$$
> Divergencia positiva en todo el espacio: cada punto es una **fuente** (campo que "explota" hacia afuera).
>
> *Campo entrante* $\vec A=(-x,-y,-z)$: $\vec\nabla\cdot\vec A=-3<0$, **sumidero** en todo punto.
>
> *Campo de cizalla* $\vec A=(-y,\,x,\,0)$ (rotación rígida):
> $$\vec\nabla\cdot\vec A=\frac{\partial(-y)}{\partial x}+\frac{\partial x}{\partial y}+0=0.$$
> Divergencia nula: campo **solenoidal**, no hay fuentes ni sumideros aunque las líneas estén curvadas.

---

## En qué consiste

> [!teoria]
> La divergencia se describe físicamente desarrollando la **ecuación de continuidad**, que relaciona el cambio temporal de la densidad de partículas con el flujo que entra y sale de un volumen. Sea $\rho(x,y,z,t)$ el número de partículas por unidad de volumen y $\vec v(x,y,z,t)$ su velocidad; se define el **vector densidad de corriente** $\vec J=\rho\vec v$.

> [!teorema] Ecuación de continuidad
> Si las partículas no se crean ni se destruyen, el cambio de densidad en un punto se debe únicamente al flujo neto de corriente:
> $$\boxed{\frac{\partial\rho}{\partial t}=-\vec\nabla\cdot\vec J.}$$

> [!demostracion]
> Tomamos un volumen diferencial $d\tau=dx\,dy\,dz$ con vértice en $(x_0,y_0,z_0)$ y medimos el flujo por sus **seis caras**. Sea $N\equiv\rho\,d\tau$ el número de partículas dentro:
> $$\frac{\partial N}{\partial t}=\frac{\partial\rho(x_0,y_0,z_0,t)}{\partial t}\,dx\,dy\,dz.$$
>
> **Paso 1 — cara inferior.** En un tiempo $dt$ entran al volumen las partículas contenidas en la columna $dx\,dy\,(v_z\,dt)$ que cruza la cara inferior. Una $v_z>0$ aporta partículas; la contribución es
> $$\frac{\partial N_{\text{inf}}}{\partial t}=\rho(x_0,y_0,z_0,t)\,v_z(x_0,y_0,z_0,t)\,dx\,dy=J_z(x_0,y_0,z_0,t)\,dx\,dy,$$
> usando $\vec J=\rho\vec v$.
>
> **Paso 2 — cara superior.** Está en $z_0+dz$ y una $v_z>0$ ahora **retira** partículas, con signo opuesto:
> $$\frac{\partial N_{\text{sup}}}{\partial t}=-J_z(x_0,y_0,z_0+dz,t)\,dx\,dy.$$
>
> **Paso 3 — suma de las dos caras en $z$.** Sumando,
> $$\frac{\partial N_{\text{inf}}}{\partial t}+\frac{\partial N_{\text{sup}}}{\partial t}=\big[J_z(x_0,y_0,z_0,t)-J_z(x_0,y_0,z_0+dz,t)\big]\,dx\,dy.$$
>
> **Paso 4 — Taylor en $z$.** Desarrollamos a primer orden,
> $$J_z(x_0,y_0,z_0+dz,t)=J_z(x_0,y_0,z_0,t)+\left.\frac{\partial J_z}{\partial z}\right|_{(x_0,y_0,z_0)}dz,$$
> y al sustituir el término constante se cancela:
> $$\frac{\partial N_{\text{inf}}}{\partial t}+\frac{\partial N_{\text{sup}}}{\partial t}=-\left.\frac{\partial J_z}{\partial z}\right|_{(x_0,y_0,z_0)}dx\,dy\,dz.$$
>
> **Paso 5 — las tres direcciones.** El proceso es idéntico para los pares de caras en $x$ e $y$. Sumando las tres contribuciones, el flujo total que cambia $N$ es
> $$\frac{\partial N}{\partial t}=\left[-\frac{\partial J_x}{\partial x}-\frac{\partial J_y}{\partial y}-\frac{\partial J_z}{\partial z}\right]dx\,dy\,dz=-\frac{\partial J_i}{\partial x_i}\,d\tau=-\vec\nabla\cdot\vec J\,d\tau.$$
>
> **Paso 6.** Igualando con $\partial N/\partial t=(\partial\rho/\partial t)\,d\tau$ y cancelando $d\tau$:
> $$\frac{\partial\rho}{\partial t}=-\vec\nabla\cdot\vec J.\qquad\blacksquare$$

> [!info] Interpretación física
> Si $\vec\nabla\cdot\vec J>0$, salen más partículas de las que entran y $\partial\rho/\partial t<0$: el punto es **fuente**. Si $\vec\nabla\cdot\vec J<0$, es **sumidero**. Si $\vec\nabla\cdot\vec J=0$, toda línea que entra a la región sale de ella (campo **solenoidal**). Un caso físico directo es la ley de Gauss en forma diferencial,
> $$\vec\nabla\cdot\vec E=4\pi\rho,$$
> donde la carga actúa como fuente del campo eléctrico.

## Resumen

> [!resumen]
> | Aspecto | Expresión |
> |---|---|
> | Definición | $\vec\nabla\cdot\vec A=\partial A_i/\partial x_i$ |
> | Resultado de | producto punto, vector → escalar |
> | Ecuación estrella | $\partial\rho/\partial t=-\vec\nabla\cdot\vec J$ |
> | $\vec\nabla\cdot\vec A>0$ | fuente (líneas nacen) |
> | $\vec\nabla\cdot\vec A<0$ | sumidero (líneas mueren) |
> | $\vec\nabla\cdot\vec A=0$ | solenoidal (las líneas pasan) |
> | Caso físico | $\vec\nabla\cdot\vec E=4\pi\rho$ |

> [!corolario]
> La divergencia mide el flujo neto por unidad de volumen: la ecuación de continuidad muestra que un exceso de flujo saliente ($\vec\nabla\cdot\vec J>0$) vacía el punto. Es la cara infinitesimal del teorema de Gauss, que la integra sobre un volumen finito (ver [[Definiciones Integrales Operadores]] y [[Teoremas Integrales/index]]).

> [!referencia]
> - Definición integral de la divergencia: [[Definiciones Integrales Operadores]].
> - Operadores hermanos: [[Gradiente]], [[Rotor]].
> - Identidad $\vec\nabla\cdot(\vec\nabla\Phi)=\nabla^2\Phi$: [[Identidades Operadores]].
