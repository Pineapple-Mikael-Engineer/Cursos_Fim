---
title: Cinemática en 3D
tags:
  - dinamica
  - teoria
  - cuerpo-rigido
  - cinematica
draft: false
aliases:
  - cinemática 3D del sólido
  - velocidad angular vectorial
  - 3D kinematics
---

# Cinemática en 3D $\;\vec v_P=\vec v_G+\vec\omega\times\vec r_{P/G}$

> [!definicion]
> En 3D la velocidad y la aceleración de un punto $P$ de un sólido respecto a su centro de masa $G$ son
> $$\boxed{\;\vec v_P=\vec v_G+\vec\omega\times\vec r_{P/G},\qquad \vec a_P=\vec a_G+\vec\alpha\times\vec r_{P/G}+\vec\omega\times(\vec\omega\times\vec r_{P/G})\;}$$
> con $\vec r_{P/G}$ el vector de $G$ a $P$, $\vec\omega$ la **velocidad angular** (un **vector** en 3D) y
> $\vec\alpha=\dot{\vec\omega}$ la aceleración angular. Ambas salen **directamente** del operador en base
> móvil, porque $\vec r_{P/G}$ es fijo en el cuerpo.

> [!info]
> La cinemática 3D del [[4 Cuerpo Rigido/index | cuerpo rígido]]; es el
> [[Operador Derivada en Base Movil | operador en base móvil]] aplicado a un punto fijo del sólido.
> **Generaliza** la [[Cinematica Plana]] (donde $\vec\omega=\omega\hat k$ es un escalar con signo) y
> **alimenta** las [[Ecuaciones de Euler 3D]]. Referencia: Goldstein §4.

---

## Ejemplo

> [!ejemplo]
> **Rotación compuesta: un disco montado en un eje que gira.**
>
> Un eje vertical gira con velocidad angular $\vec\omega_1$ (vertical). Sobre él va montado un disco que,
> además, gira con $\vec\omega_2$ **respecto al eje**. ¿Cuál es la velocidad angular total del disco y la
> velocidad de un punto $P$ de su borde?

> ![[velocidad_solido.svg|470]]
>
> *La velocidad de un punto del sólido es la del CM más la rotación: $\vec v_P=\vec v_C+\vec\omega\times\vec r_{P/C}$.*
>
> Como las velocidades angulares de rotaciones simultáneas **se suman como vectores**, la del disco es
> $$\vec\omega=\vec\omega_1+\vec\omega_2.$$
>
> > [!solucion]
> > La velocidad angular total del disco es $\vec\omega=\vec\omega_1+\vec\omega_2$. Para un punto $P$ del
> > borde, $\vec v_P=\vec v_G+\vec\omega\times\vec r_{P/G}$; si $G$ está sobre el eje y sólo gira (sin
> > trasladarse) puede tomarse el término $\vec v_G$ aparte y la **parte rotacional** del punto es
> > $\vec\omega\times\vec r_{P/G}=(\vec\omega_1+\vec\omega_2)\times\vec r_{P/G}$.

---

## En qué consiste

> [!teoria]
> El sólido es indeformable: la distancia entre cualquier par de puntos es constante. Eso obliga a que el
> campo de velocidades sea **rígido**: dos puntos sólo pueden diferir en una traslación común ($\vec v_G$)
> más un giro alrededor de un eje instantáneo, codificado por **un único** vector $\vec\omega$ compartido
> por todo el cuerpo. La cinemática 3D no es más que escribir ese giro con productos vectoriales.

> [!teorema] Velocidad y aceleración de un punto del sólido
> Para todo punto $P$ fijo en el cuerpo,
> $$\vec v_P=\vec v_G+\vec\omega\times\vec r_{P/G},\qquad
> \vec a_P=\vec a_G+\vec\alpha\times\vec r_{P/G}+\vec\omega\times(\vec\omega\times\vec r_{P/G}),$$
> con $\vec\alpha=\dot{\vec\omega}$.

> [!demostracion]
> **Velocidad.** Como $P$ es un punto **fijo en el marco del cuerpo**, $\vec r_{P/G}$ es **constante en
> ese marco**: $\left.\dfrac{d\vec r_{P/G}}{dt}\right|_{cuerpo}=\vec0$. Aplicando el operador en base
> móvil para pasar la derivada al marco fijo $F$,
> $$\left.\frac{d\vec r_{P/G}}{dt}\right|_F=\left.\frac{d\vec r_{P/G}}{dt}\right|_{cuerpo}+\vec\omega\times\vec r_{P/G}=\vec0+\vec\omega\times\vec r_{P/G}.$$
> Como $\vec r_P=\vec r_G+\vec r_{P/G}$, derivando en $F$ queda
> $$\vec v_P=\vec v_G+\vec\omega\times\vec r_{P/G}.$$
> **Aceleración.** Derivamos de nuevo en $F$. El término $\vec v_G$ da $\vec a_G$. Sobre
> $\vec\omega\times\vec r_{P/G}$ aplicamos la regla del producto y, para cada factor, el operador:
> $$\frac{d}{dt}\big(\vec\omega\times\vec r_{P/G}\big)=\dot{\vec\omega}\times\vec r_{P/G}+\vec\omega\times\underbrace{\left.\frac{d\vec r_{P/G}}{dt}\right|_F}_{=\,\vec\omega\times\vec r_{P/G}}=\vec\alpha\times\vec r_{P/G}+\vec\omega\times(\vec\omega\times\vec r_{P/G}).$$
> Sumando,
> $$\vec a_P=\vec a_G+\vec\alpha\times\vec r_{P/G}+\vec\omega\times(\vec\omega\times\vec r_{P/G}).\qquad\blacksquare$$

> [!proposicion] $\vec\omega$ es un vector y se compone aditivamente
> Para rotaciones **simultáneas** las velocidades angulares **se suman vectorialmente**,
> $$\vec\omega=\sum_i\vec\omega_i,$$
> a diferencia de las rotaciones **finitas**, que **no conmutan** y por tanto no se suman. Los
> **ángulos de Euler** (precesión $\phi$, nutación $\theta$, spin $\psi$) parametrizan la orientación del
> sólido, y $\vec\omega$ se compone de sus tres tasas $\dot\phi,\dot\theta,\dot\psi$ a lo largo de sus
> respectivos ejes.

> [!warning]
> Las **velocidades angulares** (infinitesimales) se suman como vectores, pero las **rotaciones finitas
> no** (no conmutan): orientar primero $90^\circ$ y luego otros $90^\circ$ por otro eje no da lo mismo
> que invertir el orden. El término $\vec\omega\times(\vec\omega\times\vec r_{P/G})$ es la aceleración
> **centrípeta** del punto (apunta hacia el eje instantáneo). En 3D $\vec\alpha$ puede **no** ser paralelo
> a $\vec\omega$: el eje de giro cambia de **módulo y de dirección**, algo imposible en el caso plano.

## Resumen

> [!resumen]
> | Magnitud | Expresión |
> |:---|:---|
> | Velocidad | $\vec v_P=\vec v_G+\vec\omega\times\vec r_{P/G}$ |
> | Aceleración | $\vec a_P=\vec a_G+\vec\alpha\times\vec r_{P/G}+\vec\omega\times(\vec\omega\times\vec r_{P/G})$ |
> | Composición de $\vec\omega$ | $\vec\omega=\sum_i\vec\omega_i$ (rotaciones simultáneas) |

> [!corolario]
> La cinemática 3D del sólido es el operador en base móvil aplicado a un punto rígidamente unido al
> cuerpo. Reducir $\vec\omega$ a un escalar recupera la [[Cinematica Plana]]; mantenerlo como vector y
> derivar el momento angular conduce a las [[Ecuaciones de Euler 3D]].

> [!referencia]
> Goldstein §4. Operador base: [[Operador Derivada en Base Movil]]. Caso plano:
> [[Cinematica Plana]]. Continuación cinética: [[Ecuaciones de Euler 3D]].
