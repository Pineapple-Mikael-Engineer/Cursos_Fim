---
title: Condiciones de Frontera
tags:
  - ecuaciones
  - edo
  - teoria
  - lineales
  - problemas-frontera
  - autovalores
draft: false
aliases:
  - condiciones de contorno
  - Dirichlet
  - Neumann
  - Robin
  - boundary conditions
  - problema de autovalores
  - eigenvalue problem
---

# Condiciones de Frontera

> [!definicion]
> Las **condiciones de frontera** prescriben el comportamiento de la solución en los extremos $a,b$
> de $[a,b]$. Según qué cantidad fijen, se clasifican en:
> - **Dirichlet** — fija el **valor** de la función: $y(a)=\alpha$.
> - **Neumann** — fija el **valor de la derivada** (el flujo/pendiente): $y'(a)=\alpha$.
> - **Robin** (o mixta) — fija una **combinación lineal**: $\alpha\,y(a)+\beta\,y'(a)=\gamma$.
> - **Periódicas** — igualan ambos extremos: $y(a)=y(b)$ y $y'(a)=y'(b)$.
> Una condición se llama **homogénea** si su lado derecho es cero ($y(a)=0$, $y'(a)=0$, …). Las
> condiciones homogéneas son las que dan lugar a los problemas de autovalores.

> [!info]
> Primera nota de [[Problemas de Frontera EDO/index | problemas de frontera]]. Aquí se ve **cómo** las
> condiciones determinan la existencia y unicidad, y cómo las condiciones **homogéneas con un
> parámetro** producen los autovalores. La técnica para resolver el caso **no homogéneo** está en
> [[Problemas de Frontera EDO/Funcion de Green para EDO]], y la teoría general que generaliza todo
> esto es [[Sturm-Liouville/index | Sturm-Liouville]].

---

## Ejemplo

> [!ejemplo] El mismo operador, tres resultados según la frontera
> Sea $y''+y=0$ en $[0,\pi]$. Su [[Coeficientes Constantes Homogenea | solución general]] es
> $$y=c_1\cos x+c_2\operatorname{sen}x.$$
> Vamos a imponer tres pares de condiciones de Dirichlet distintos.
>
> **(a) $y(0)=0,\ y(\pi)=0$ → infinitas soluciones.**
> De $y(0)=c_1=0$ queda $y=c_2\operatorname{sen}x$. La segunda condición da
> $y(\pi)=c_2\operatorname{sen}\pi=c_2\cdot 0=0$, que se satisface **para cualquier** $c_2$. Hay
> infinitas soluciones $y=c_2\operatorname{sen}x$.
>
> **(b) $y(0)=0,\ y(\pi)=1$ → ninguna solución.**
> De nuevo $c_1=0$ y $y(\pi)=c_2\cdot 0=0$. Pero ahora se exige que esto valga $1$: queda $0=1$,
> **imposible**. El problema **no tiene solución**.
>
> **(c) $y(0)=0,\ y(\tfrac\pi2)=5$ → solución única.**
> $c_1=0$ y $y(\tfrac\pi2)=c_2\operatorname{sen}\tfrac\pi2=c_2=5$. Solución **única**
> $y=5\operatorname{sen}x$.
>
> Compárese con cualquier **PVI** sobre la misma EDO (p.ej. $y(0)=0,\ y'(0)=1$): siempre da una y solo
> una solución. La diferencia (una/ninguna/infinitas) es exclusiva del PVF.

---

## En qué consiste

> [!teorema] Existencia y unicidad de un PVF lineal
> Sea la solución general $y=c_1y_1+c_2y_2$ de una EDO lineal de segundo orden, y un PVF con dos
> condiciones de frontera lineales. Imponerlas equivale a un **sistema lineal** $M\vec c=\vec d$ en
> las constantes $\vec c=(c_1,c_2)$. Entonces:
> - si $\det M\neq 0$: **solución única**;
> - si $\det M=0$ y $\vec d$ es compatible: **infinitas** soluciones;
> - si $\det M=0$ y $\vec d$ es incompatible: **ninguna** solución.

> [!demostracion]
> **Paso 1 — montar el sistema.** Para condiciones de Dirichlet $y(a)=\alpha,\ y(b)=\beta$ se obtiene
> $$M=\begin{pmatrix} y_1(a) & y_2(a)\\ y_1(b) & y_2(b)\end{pmatrix},\qquad
> \vec c=\begin{pmatrix}c_1\\ c_2\end{pmatrix},\qquad \vec d=\begin{pmatrix}\alpha\\ \beta\end{pmatrix}.$$
>
> **Paso 2 — aplicar álgebra lineal.** Un sistema $M\vec c=\vec d$ con $M$ de $2\times2$ tiene
> solución única **si y solo si** $\det M\neq0$ (entonces $\vec c=M^{-1}\vec d$). Si $\det M=0$, la
> imagen de $M$ es un subespacio propio: $\vec d$ está en él (→ infinitas soluciones, pues el núcleo
> de $M$ es no trivial y se le suma libremente) o no lo está (→ ninguna).
>
> **Paso 3 — leer el ejemplo.** En $y''+y=0$ sobre $[0,\pi]$ con $y_1=\cos x,\ y_2=\operatorname{sen}x$:
> $M=\begin{pmatrix}1 & 0\\ -1 & 0\end{pmatrix}$, $\det M=0$. Por eso (a) tiene infinitas y (b) ninguna,
> según el lado derecho. $\blacksquare$

> [!teorema] El problema de autovalores $y''+\lambda y=0$ con $y(0)=y(L)=0$
> El PVF **homogéneo** con parámetro $\lambda$
> $$y''+\lambda y=0,\qquad y(0)=0,\ y(L)=0$$
> admite solución **no trivial** únicamente para los **autovalores**
> $$\lambda_n=\left(\frac{n\pi}{L}\right)^2,\qquad n=1,2,3,\dots,$$
> y a cada uno le corresponde la **autofunción**
> $$y_n(x)=\operatorname{sen}\frac{n\pi x}{L}.$$
> Para cualquier otro $\lambda$ la única solución es la trivial $y\equiv 0$.

> [!demostracion] Por qué $\lambda$ debe cuantizarse
> El sistema es homogéneo ($\vec d=\vec 0$), así que la solución trivial $y\equiv0$ **siempre** existe.
> Buscamos los $\lambda$ que además permiten una no trivial. Analizamos los tres signos de $\lambda$.
>
> **Paso 1 — caso $\lambda<0$ (escribimos $\lambda=-\mu^2$, $\mu>0$).** La general es
> $y=A\,e^{\mu x}+B\,e^{-\mu x}$ (o $A\cosh\mu x+B\operatorname{senh}\mu x$). Imponer $y(0)=0$ da
> $A+B=0$; con $y(L)=0$ queda $A\operatorname{senh}\mu L=0$. Como $\operatorname{senh}\mu L\neq0$ para
> $L>0$, sale $A=0$ y por tanto $B=0$: **solo la trivial**. No hay autovalores negativos.
>
> **Paso 2 — caso $\lambda=0$.** La EDO es $y''=0$, con $y=A+Bx$. $y(0)=0\Rightarrow A=0$;
> $y(L)=BL=0\Rightarrow B=0$. **Solo la trivial.** $\lambda=0$ no es autovalor.
>
> **Paso 3 — caso $\lambda>0$ (escribimos $\lambda=k^2$, $k>0$).** La general es
> $y=A\cos kx+B\operatorname{sen}kx$. De $y(0)=A=0$ queda $y=B\operatorname{sen}kx$. La condición en
> el otro extremo,
> $$y(L)=B\operatorname{sen}kL=0,$$
> obliga, **si queremos $B\neq0$**, a $\operatorname{sen}kL=0$, es decir $kL=n\pi$ con $n=1,2,\dots$
> Esto **cuantiza** $k=\tfrac{n\pi}{L}$ y por tanto $\lambda_n=k^2=\big(\tfrac{n\pi}{L}\big)^2$, con
> autofunción $y_n=\operatorname{sen}\tfrac{n\pi x}{L}$. Para los $\lambda$ que no son de esta forma,
> $\operatorname{sen}kL\neq0$ fuerza $B=0$ y solo queda la trivial. $\blacksquare$

> [!proposicion] La frontera elige el "modo": las autofunciones son ortogonales
> Las autofunciones $y_n=\operatorname{sen}\tfrac{n\pi x}{L}$ son mutuamente **ortogonales** en
> $[0,L]$:
> $$\int_0^L \operatorname{sen}\frac{n\pi x}{L}\,\operatorname{sen}\frac{m\pi x}{L}\,dx
> =\frac{L}{2}\,\delta_{nm}.$$
> Esto no es casualidad del seno: es una propiedad general de los operadores de frontera
> autoadjuntos, y es lo que permite **desarrollar** cualquier función como suma de autofunciones
> (serie de Fourier de senos). Cambiar las condiciones de frontera cambia las autofunciones (con
> Neumann $y'(0)=y'(L)=0$ saldrían **cosenos**), pero la estructura —autovalores discretos + base
> ortogonal— se conserva.

> [!info] Esto es el germen de Sturm-Liouville y de la separación de variables
> El problema $y''+\lambda y=0$ con condiciones homogéneas es el **caso más simple** de un
> [[Sturm-Liouville/index | problema de Sturm-Liouville]] $-(p\,y')'+q\,y=\lambda\,w\,y$. Y aparece
> de manera natural al separar variables en EDP: al resolver la ecuación del calor o de ondas en
> $[0,L]$ con extremos fijos, la parte espacial es **exactamente** este problema, y los $\lambda_n$
> son las frecuencias/modos propios del sistema. Por eso los PVF de autovalores son la bisagra entre
> las EDO y las [[2 Ecuaciones en Derivadas Parciales/index | EDP]].

---

## Resumen

> [!resumen]
> | Tipo | Forma en $x=a$ | Qué fija |
> |---|---|---|
> | Dirichlet | $y(a)=\alpha$ | el valor |
> | Neumann | $y'(a)=\alpha$ | la derivada (flujo) |
> | Robin (mixta) | $\alpha\,y(a)+\beta\,y'(a)=\gamma$ | combinación |
> | Periódicas | $y(a)=y(b),\ y'(a)=y'(b)$ | igualdad de extremos |
>
> | Caso del PVF | Condición | Solución |
> |---|---|---|
> | genérico | $\det M\neq0$ | **única** |
> | degenerado compatible | $\det M=0$, $\vec d$ compatible | **infinitas** |
> | degenerado incompatible | $\det M=0$, $\vec d$ incompatible | **ninguna** |

> [!corolario]
> La frontera no es un detalle de cierre: **selecciona** qué soluciones existen. Con condiciones
> homogéneas y un parámetro $\lambda$, esa selección se vuelve discreta —solo sobreviven los
> autovalores $\lambda_n$— y produce una base ortogonal de autofunciones. Ese es el mecanismo que,
> generalizado, sostiene toda la física matemática lineal.

> [!referencia]
> - Resolver el PVF **no homogéneo**: [[Problemas de Frontera EDO/Funcion de Green para EDO]].
> - La solución general que se impone: [[Coeficientes Constantes Homogenea]].
> - La teoría general de autovalores de EDO: [[Sturm-Liouville/index]].
> - Vista de conjunto de la sección: [[Problemas de Frontera EDO/index]].
