---
title: Ecuaciones de Euler 3D
tags:
  - dinamica
  - teoria
  - cuerpo-rigido
draft: false
aliases:
  - ecuaciones de Euler
  - dinámica rotacional 3D
  - cinética del cuerpo rígido 3D
---

# Ecuaciones de Euler $\;\sum\vec M=\mathbf I\vec\alpha+\vec\omega\times(\mathbf I\vec\omega)$

> [!definicion]
> La cinética rotacional de un cuerpo rígido en 3D (respecto al centro de masa $G$ o a un punto fijo)
> es
> $$\boxed{\;\sum\vec M=\mathbf I\vec\alpha+\vec\omega\times(\mathbf I\vec\omega)\;}$$
> donde $\mathbf I\vec\alpha$ es el cambio "directo" del giro y $\vec\omega\times(\mathbf I\vec\omega)$ el
> término **giroscópico** (genuinamente 3D). En **ejes principales** del cuerpo se separa en las tres
> **ecuaciones de Euler** escalares. La traslación la rige $\sum\vec F=m\vec a_G$.

> [!info]
> La cinética 3D del [[4 Cuerpo Rigido/index| cuerpo rígido]]; **aplica** el tensor y la
> [[Deduccion del Torque | deducción del torque]] de la [[3 Inercia/index | inercia]], y se obtiene
> también con el [[Operador Derivada en Base Movil | operador en base móvil]]. Referencia: Goldstein §5.5.

---

## Ejemplo

> [!ejemplo]
> **Precesión libre de un cuerpo simétrico (sin torque).**
>
> Un sólido axisimétrico ($I_1=I_2=I_t$, $I_3=I_a$) gira **libre de torque** ($\sum\vec M=\vec0$).
> ¿Cómo evoluciona $\vec\omega$?
>
> ![[precesion_cono.svg|360]]
>
> *Sin torque, $\vec\omega$ recorre un cono alrededor del eje de simetría (precesión libre), mientras $\vec H$ se mantiene fijo.*
>
> **Eje de simetría:** la 3.ª ecuación de Euler da $I_a\dot\omega_3=(I_1-I_2)\omega_1\omega_2=0$, luego
> $\omega_3=$ cte.
> **Plano transversal:** las otras dos quedan $I_t\dot\omega_1=(I_t-I_a)\omega_2\omega_3$ y
> $I_t\dot\omega_2=(I_a-I_t)\omega_1\omega_3$, un oscilador: $\omega_1,\omega_2$ giran con frecuencia
> $\Omega=\dfrac{I_a-I_t}{I_t}\,\omega_3$.
>
> > [!solucion]
> > $\vec\omega$ describe un cono alrededor del eje de simetría (**precesión libre**) a velocidad
> > $\Omega=\frac{I_a-I_t}{I_t}\omega_3$, sin necesidad de torque alguno. Es el bamboleo de un disco o un
> > planeta que gira.

---

## En qué consiste

> [!teorema] Ecuación rotacional y forma de Euler
> $\sum\vec M=\mathbf I\vec\alpha+\vec\omega\times(\mathbf I\vec\omega)$. En **ejes principales** del
> cuerpo (donde $\mathbf I=\mathrm{diag}(I_1,I_2,I_3)$):
> $$\begin{aligned} M_1&=I_1\dot\omega_1-(I_2-I_3)\,\omega_2\omega_3,\\ M_2&=I_2\dot\omega_2-(I_3-I_1)\,\omega_3\omega_1,\\ M_3&=I_3\dot\omega_3-(I_1-I_2)\,\omega_1\omega_2.\end{aligned}$$

> [!demostracion]
> Partimos de $\sum\vec M=\left.\dfrac{d\vec H}{dt}\right|_F$ con $\vec H=\mathbf I\vec\omega$.
> **Paso 1 — Operador en base móvil** hacia el marco **del cuerpo** (donde $\mathbf I$ es **constante**,
> porque la masa no se mueve respecto al sólido):
> $$\sum\vec M=\left.\frac{d\vec H}{dt}\right|_{cuerpo}+\vec\omega\times\vec H.$$
> **Paso 2 — Derivada en el cuerpo:** como $\mathbf I$ no cambia en ese marco,
> $\left.\dfrac{d\vec H}{dt}\right|_{cuerpo}=\mathbf I\,\dot{\vec\omega}=\mathbf I\vec\alpha$.
> **Paso 3 — Sustituir:** $\sum\vec M=\mathbf I\vec\alpha+\vec\omega\times(\mathbf I\vec\omega)$.
> Proyectando en ejes principales ($\vec H=(I_1\omega_1,I_2\omega_2,I_3\omega_3)$ y desarrollando
> $\vec\omega\times\vec H$) salen las tres ecuaciones escalares. $\blacksquare$

> [!proposicion] El caso plano es un límite
> Si $\vec\omega=\omega\hat k$ con $\hat k$ eje principal, entonces $\mathbf I\vec\omega=I_3\omega\hat k$
> es **paralelo** a $\vec\omega$ y $\vec\omega\times(\mathbf I\vec\omega)=\vec0$: el término giroscópico
> desaparece y queda $\sum M_z=I_3\dot\omega$, la cinética plana de [[Dinamica Plana 2D]].

> [!proposicion] Energía y momento angular
> Las otras magnitudes ya están deducidas: $\vec H=\mathbf I\vec\omega$
> ([[Deduccion del Momento Angular]]) y $T=\tfrac12 m v_G^2+\tfrac12\vec\omega\cdot\mathbf I\vec\omega$
> ([[Deduccion de la Energia Cinetica]]). Sin torque, $\vec H$ (en $F$) y $T$ se **conservan**, aunque
> $\vec\omega$ cambie de dirección.

> [!warning]
> El tensor $\mathbf I$ se toma en **ejes del cuerpo** (rotantes) para que sea constante; por eso las
> ecuaciones de Euler se escriben en ese marco. El término $\vec\omega\times(\mathbf I\vec\omega)$ no
> existe en 2D pero **domina** en 3D: ignorarlo es el error típico. $\vec H$ no es paralelo a
> $\vec\omega$ salvo en ejes principales.

## Resumen

> [!resumen]
> | Magnitud | Expresión |
> |:---|:---|
> | Traslación | $\sum\vec F=m\vec a_G$ |
> | Rotación | $\sum\vec M=\mathbf I\vec\alpha+\vec\omega\times(\mathbf I\vec\omega)$ |
> | Euler (eje 1) | $M_1=I_1\dot\omega_1-(I_2-I_3)\omega_2\omega_3$ |
> | Momento angular | $\vec H=\mathbf I\vec\omega$ |
> | Energía | $T=\tfrac12 m v_G^2+\tfrac12\vec\omega\cdot\mathbf I\vec\omega$ |

> [!corolario]
> La dinámica rotacional 3D es la ecuación de Euler, y se obtiene aplicando el operador en base móvil al
> momento angular $\mathbf I\vec\omega$. Su término giroscópico —invisible en el plano— es la raíz de la
> precesión y de todo el [[Movimiento Giroscopico | comportamiento giroscópico]].

> [!referencia]
> Goldstein §5.5; Taylor cap. 10. Deducción integral: [[Deduccion del Torque]]. Operador:
> [[Operador Derivada en Base Movil]]. Aplicación espectacular: [[Movimiento Giroscopico]].
