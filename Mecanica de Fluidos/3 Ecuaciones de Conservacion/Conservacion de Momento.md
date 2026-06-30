---
title: Conservación de Momento
order: 2
tags:
  - fluidos
  - teoria
  - conservacion
draft: false
aliases:
  - Conservación de momento
  - Ecuación de Cauchy
  - Ecuación de movimiento
---

# Conservación de Momento $\rho\,\dfrac{D\vec v}{Dt}=\nabla\cdot\boldsymbol\sigma+\rho\vec g$

> [!definicion]
> La **conservación de momento** es la segunda ley de Newton escrita para un medio continuo: la inercia de la partícula fluida iguala las fuerzas que actúan sobre ella. En forma local (indicial) es la **ecuación de Cauchy**
> $$\boxed{\;\rho\,\frac{Dv_i}{Dt}=\partial_j\sigma_{ij}+\rho\,g_i\;}\qquad\Longleftrightarrow\qquad \rho\,\frac{D\vec v}{Dt}=\nabla\cdot\boldsymbol\sigma+\rho\vec g.$$
> El término $\dfrac{Dv_i}{Dt}=\partial_t v_i+v_j\,\partial_j v_i$ es la **aceleración material** ([[Derivada Material]]); $\boldsymbol\sigma$ es el [[Tensor de Esfuerzos de Cauchy]] y $\rho\vec g$ la fuerza másica (gravedad) por unidad de volumen. La divergencia $\partial_j\sigma_{ij}$ representa la **fuerza neta de superficie por unidad de volumen**.

---

> [!info]
> **Ubicación.** Tercera ley de balance de la sección [[3 Ecuaciones de Conservacion/index | Ecuaciones de Conservación]]. Sus notas hermanas son [[Conservacion de Masa]] (continuidad) y [[Ecuaciones de Navier-Stokes]] (donde se cierra el sistema). Esta nota apoya su deducción en el [[Tensor de Esfuerzos de Cauchy]] (tracción $t_i=\sigma_{ij}n_j$) y en el [[Teorema del Transporte de Reynolds]]. **Convenio.** Índices repetidos suman ($\sum_j\to$ implícito); $\partial_j\equiv\partial/\partial x_j$; $\delta_{ij}$ es la delta de Kronecker. Vectores con flecha. **Referencia.** Landau-Lifshitz, Vol. 6, §15; Batchelor, *An Introduction to Fluid Dynamics*, cap. 3.

---

## En qué consiste

> [!teoria] La segunda ley de Newton para un volumen material
> Tomamos un **volumen material** $V(t)$ —una porción de fluido que se mueve con él, formada siempre por las mismas partículas, de superficie $S(t)$ y normal exterior $\vec n$—. Su momento lineal es $\displaystyle\int_V\rho\vec v\,dV$. La segunda ley de Newton dice que su **tasa de cambio** iguala la **fuerza total**, que tiene dos contribuciones:
> $$\frac{d}{dt}\int_{V}\rho\,v_i\,dV=\underbrace{\int_V\rho\,g_i\,dV}_{\text{fuerza másica}}+\underbrace{\oint_S t_i\,dA}_{\text{fuerza de superficie}}.$$
> La fuerza **másica** (volumétrica) es la gravedad $\rho\vec g$; la fuerza de **superficie** la ejerce el fluido vecino sobre $S$ mediante la **tracción** $\vec t=\boldsymbol\sigma\cdot\vec n$. Todo el trabajo siguiente consiste en convertir esta igualdad integral en una **ley local** válida punto a punto.

> [!teoria] Las tres piezas técnicas
> 1. **El lado izquierdo** (derivada del momento) se simplifica con un lema sobre cómo derivar integrales materiales de cantidades $\times\rho$: la masa se conserva, así que la derivada "entra" como derivada material.
> 2. **La fuerza de superficie** se vuelve volumétrica con el [[Tensor de Esfuerzos de Cauchy]] ($t_i=\sigma_{ij}n_j$) y el **teorema de la divergencia**.
> 3. **El volumen es arbitrario**, lo que permite igualar integrandos y obtener la ecuación local.

---

## Demostración: el lema de la derivada material

> [!lema] Derivada de una integral material de $\rho\psi$
> Para cualquier campo escalar o componente $\psi(\vec x,t)$ transportado por el fluido, y un volumen material $V(t)$,
> $$\frac{d}{dt}\int_{V(t)}\rho\,\psi\,dV=\int_{V(t)}\rho\,\frac{D\psi}{Dt}\,dV.$$
> Esta es la pieza que limpia el balance de momento: la densidad $\rho$ "no estorba" porque la masa se conserva.

> [!demostracion]
> **Paso 1 — Transporte de Reynolds sobre $\rho\psi$.** El [[Teorema del Transporte de Reynolds]] aplicado a la densidad $\phi=\rho\psi$ da, en su forma diferencial,
> $$\frac{d}{dt}\int_{V(t)}\rho\psi\,dV=\int_{V}\left[\partial_t(\rho\psi)+\partial_j\big(\rho\psi\,v_j\big)\right]dV.$$
>
> **Paso 2 — Expandir las derivadas con la regla del producto.**
> $$\partial_t(\rho\psi)+\partial_j(\rho\psi v_j)=\psi\,\partial_t\rho+\rho\,\partial_t\psi+\psi\,\partial_j(\rho v_j)+\rho v_j\,\partial_j\psi.$$
> Agrupamos los términos que llevan $\psi$ y los que llevan $\rho$:
> $$=\underbrace{\psi\big[\partial_t\rho+\partial_j(\rho v_j)\big]}_{(\ast)}+\underbrace{\rho\big[\partial_t\psi+v_j\,\partial_j\psi\big]}_{(\ast\ast)}.$$
>
> **Paso 3 — Aplicar la conservación de la masa.** Por la [[Conservacion de Masa | ecuación de continuidad]], $\partial_t\rho+\partial_j(\rho v_j)=0$, de modo que el corchete $(\ast)$ se anula idénticamente.
>
> **Paso 4 — Reconocer la derivada material.** En $(\ast\ast)$, el corchete $\partial_t\psi+v_j\partial_j\psi$ es por definición la [[Derivada Material]] $\dfrac{D\psi}{Dt}$. Por tanto
> $$\frac{d}{dt}\int_{V(t)}\rho\psi\,dV=\int_{V}\rho\,\frac{D\psi}{Dt}\,dV.\qquad\blacksquare$$

---

## Demostración: la ecuación de Cauchy

> [!teorema] Ecuación de Cauchy (forma local del momento)
> En todo punto de un medio continuo,
> $$\rho\,\frac{Dv_i}{Dt}=\partial_j\sigma_{ij}+\rho\,g_i.$$

> [!demostracion]
> **Paso 1 — Lado izquierdo con el lema.** Aplicamos el lema anterior con $\psi=v_i$ (la $i$-ésima componente de la velocidad):
> $$\frac{d}{dt}\int_{V}\rho\,v_i\,dV=\int_{V}\rho\,\frac{Dv_i}{Dt}\,dV.$$
> Esto convierte la derivada de un momento (donde $V$ cambia y $\rho$ varía) en una integral limpia de la aceleración material.
>
> **Paso 2 — Convertir la fuerza de superficie en volumétrica.** Por el [[Tensor de Esfuerzos de Cauchy]], la tracción sobre la cara de normal $\vec n$ es $t_i=\sigma_{ij}n_j$. Aplicamos el **teorema de la divergencia** a cada componente:
> $$\oint_S t_i\,dA=\oint_S\sigma_{ij}\,n_j\,dA=\int_V\partial_j\sigma_{ij}\,dV.$$
>
> **Paso 3 — Reescribir el balance integral.** Sustituyendo los Pasos 1 y 2 en la segunda ley de Newton:
> $$\int_V\rho\,\frac{Dv_i}{Dt}\,dV=\int_V\rho\,g_i\,dV+\int_V\partial_j\sigma_{ij}\,dV.$$
> Pasamos todo a un solo lado:
> $$\int_V\left[\rho\,\frac{Dv_i}{Dt}-\partial_j\sigma_{ij}-\rho\,g_i\right]dV=0.$$
>
> **Paso 4 — Localización por volumen arbitrario.** La igualdad vale para **cualquier** subvolumen material $V$. Si el integrando (continuo) fuese positivo en un punto, lo sería en una bola alrededor y la integral sobre esa bola sería positiva, contradicción; lo mismo si fuese negativo. Por tanto el integrando se anula punto a punto:
> $$\boxed{\;\rho\,\frac{Dv_i}{Dt}=\partial_j\sigma_{ij}+\rho\,g_i\;}\qquad\Longleftrightarrow\qquad \rho\,\frac{D\vec v}{Dt}=\nabla\cdot\boldsymbol\sigma+\rho\vec g.\qquad\blacksquare$$

![[fuerzas_elemento.svg|400]]
*Fuerzas sobre un elemento fluido: sobre las seis caras actúan los esfuerzos de superficie —presión normal y esfuerzos viscosos— cuyo desbalance neto es $\nabla\cdot\boldsymbol\sigma$ por unidad de volumen; sobre el volumen actúa la gravedad $\rho\vec g$. Su suma iguala la inercia $\rho\,D\vec v/Dt$.*

> [!proposicion] Interpretación de $\nabla\cdot\boldsymbol\sigma$
> El término $\partial_j\sigma_{ij}$ es la **fuerza neta de superficie por unidad de volumen** en la dirección $i$. Que aparezca una **divergencia** dice que solo un esfuerzo **desbalanceado** (que cambia de una cara a la opuesta) produce fuerza neta: un campo de esfuerzos uniforme comprime el elemento por igual desde todos lados y no lo acelera. Descomponiendo $\sigma_{ij}=-p\,\delta_{ij}+\tau_{ij}$ se separa en $-\partial_i p$ (gradiente de presión) y $\partial_j\tau_{ij}$ (fricción viscosa).

---

## Forma conservativa

> [!proposicion] Forma de divergencia del momento
> La ecuación de Cauchy admite la escritura equivalente
> $$\partial_t(\rho v_i)+\partial_j(\rho v_i v_j)=\partial_j\sigma_{ij}+\rho\,g_i,$$
> donde $\Pi_{ij}=\rho v_i v_j-\sigma_{ij}$ es el **tensor de flujo de momento**: $\rho v_iv_j$ transporta momento por convección y $-\sigma_{ij}$ por esfuerzos.

> [!demostracion]
> **Paso 1 — Expandir el lado izquierdo conservativo.** Con la regla del producto,
> $$\partial_t(\rho v_i)+\partial_j(\rho v_i v_j)=v_i\,\partial_t\rho+\rho\,\partial_t v_i+v_i\,\partial_j(\rho v_j)+\rho v_j\,\partial_j v_i.$$
>
> **Paso 2 — Agrupar y usar continuidad.** Reunimos los términos con factor $v_i$:
> $$=v_i\underbrace{\big[\partial_t\rho+\partial_j(\rho v_j)\big]}_{=\,0\ \text{(continuidad)}}+\rho\underbrace{\big[\partial_t v_i+v_j\,\partial_j v_i\big]}_{=\,Dv_i/Dt}=\rho\,\frac{Dv_i}{Dt}.$$
>
> **Paso 3 — Reemplazar por Cauchy.** Como $\rho\,Dv_i/Dt=\partial_j\sigma_{ij}+\rho g_i$, se concluye
> $$\partial_t(\rho v_i)+\partial_j(\rho v_i v_j)=\partial_j\sigma_{ij}+\rho\,g_i.\qquad\blacksquare$$
>
> Pasando $\partial_j\sigma_{ij}$ a la izquierda, $\;\partial_t(\rho v_i)+\partial_j\big(\rho v_iv_j-\sigma_{ij}\big)=\rho g_i$, que es una **ley de conservación** con flujo $\Pi_{ij}$ y fuente $\rho g_i$.

---

## Ejemplo

> [!ejemplo] Fuerza sobre un codo de tubería (balance integral)
> Por un codo de $90^\circ$ circula agua ($\rho=1000\ \mathrm{kg/m^3}$) en régimen **estacionario**. La sección de entrada y salida es $A=0{,}01\ \mathrm{m^2}$ y el caudal másico $\dot m=20\ \mathrm{kg/s}$. El agua entra horizontal en $+x$ y sale vertical en $+y$, con rapidez $V$ en ambas caras. Despreciando presión y peso frente al cambio de momento, halla la fuerza $\vec R$ que el codo ejerce sobre el fluido.

> [!solucion]
> **Paso 1 — Forma integral estacionaria.** Integrando la forma conservativa sobre el volumen de control fijo y anulando $\partial_t$, queda el **balance de momento de volumen de control**:
> $$\oint_S\rho v_i(v_jn_j)\,dA=R_i\quad\Longrightarrow\quad \sum F_i=\dot m\,(v_{i,\text{out}}-v_{i,\text{in}}).$$
>
> **Paso 2 — Rapidez del flujo.** De $\dot m=\rho A V$,
> $$V=\frac{\dot m}{\rho A}=\frac{20}{1000\cdot 0{,}01}=2{,}0\ \mathrm{m/s}.$$
>
> **Paso 3 — Velocidades de entrada y salida.**
> $$\vec v_{\text{in}}=(2{,}0,\;0)\ \mathrm{m/s},\qquad \vec v_{\text{out}}=(0,\;2{,}0)\ \mathrm{m/s}.$$
>
> **Paso 4 — Componentes de la fuerza.**
> $$R_x=\dot m\,(0-2{,}0)=20\cdot(-2{,}0)=-40\ \mathrm{N},$$
> $$R_y=\dot m\,(2{,}0-0)=20\cdot(+2{,}0)=+40\ \mathrm{N}.$$
>
> **Paso 5 — Resultante.** El codo empuja al fluido con
> $$\vec R=(-40,\;+40)\ \mathrm{N},\qquad |\vec R|=\sqrt{40^2+40^2}=40\sqrt2\approx 56{,}6\ \mathrm{N},$$
> a $135^\circ$ del eje $+x$. Por la tercera ley de Newton, el fluido reacciona sobre el codo con $-\vec R$: este tiende a "abrirse" hacia fuera de la curva. $\blacksquare$

> [!ejemplo] Caso estático: recuperar la hidrostática
> Si el fluido está en reposo, $\vec v=\vec 0$, la aceleración material se anula y el esfuerzo se reduce a la presión, $\sigma_{ij}=-p\,\delta_{ij}$.

> [!solucion]
> **Paso 1 — Anular la inercia.** Con $\vec v=\vec 0$, $\;Dv_i/Dt=0$, de modo que Cauchy queda $0=\partial_j\sigma_{ij}+\rho g_i$.
>
> **Paso 2 — Sustituir el esfuerzo estático.** $\partial_j\sigma_{ij}=\partial_j(-p\,\delta_{ij})=-\partial_i p$. Entonces
> $$0=-\partial_i p+\rho g_i\;\Longrightarrow\;\boxed{\nabla p=\rho\vec g}.$$
> Se recupera la **ecuación fundamental de la hidrostática**: el gradiente de presión equilibra el peso. $\blacksquare$

> [!warning] Cauchy vale para cualquier medio continuo
> La ecuación $\rho\,Dv_i/Dt=\partial_j\sigma_{ij}+\rho g_i$ **no distingue** entre sólido y fluido: es válida para todo medio continuo (gelatina, acero, agua o aire). Lo que la **especializa a un fluido** es la **relación constitutiva** que liga el esfuerzo con la deformación. Para un [[Fluido Newtoniano]], $\sigma_{ij}=-p\,\delta_{ij}+2\mu\,e_{ij}$ (con $e_{ij}$ el tensor de tasa de deformación); sustituida en Cauchy produce las [[Ecuaciones de Navier-Stokes]]. Sin la relación constitutiva, Cauchy tiene más incógnitas (las seis componentes de $\sigma_{ij}$) que ecuaciones y **no está cerrada**.

---

## Resumen

> [!resumen]
> | Concepto | Expresión | Significado |
> |---|---|---|
> | Balance integral | $\dfrac{d}{dt}\displaystyle\int_V\rho\vec v\,dV=\displaystyle\int_V\rho\vec g\,dV+\oint_S\vec t\,dA$ | 2ª ley de Newton para $V(t)$ |
> | Lema material | $\dfrac{d}{dt}\displaystyle\int_V\rho\psi\,dV=\displaystyle\int_V\rho\dfrac{D\psi}{Dt}\,dV$ | la masa se conserva: $\rho$ "pasa" dentro |
> | Tracción | $t_i=\sigma_{ij}n_j$ | esfuerzo sobre cara de normal $\vec n$ |
> | Cauchy (local) | $\rho\dfrac{Dv_i}{Dt}=\partial_j\sigma_{ij}+\rho g_i$ | inercia = fuerza de superficie + másica |
> | Forma vectorial | $\rho\dfrac{D\vec v}{Dt}=\nabla\cdot\boldsymbol\sigma+\rho\vec g$ | $\nabla\cdot\boldsymbol\sigma$ = fuerza de superficie / volumen |
> | Forma conservativa | $\partial_t(\rho v_i)+\partial_j(\rho v_iv_j)=\partial_j\sigma_{ij}+\rho g_i$ | flujo de momento $\Pi_{ij}=\rho v_iv_j-\sigma_{ij}$ |
> | Caso estático | $\nabla p=\rho\vec g$ | hidrostática ($\vec v=\vec 0$) |

> [!corolario] Lo esencial
> La conservación de momento es la **ecuación de movimiento** del fluido: inercia $=$ fuerzas de superficie $+$ fuerzas másicas. El lema de la derivada material (apoyado en la [[Conservacion de Masa]]) limpia el lado izquierdo; el [[Tensor de Esfuerzos de Cauchy]] y el teorema de la divergencia vuelven local la fuerza de superficie. La ecuación de Cauchy es **universal** para medios continuos; al inyectar la ley del [[Fluido Newtoniano]] se transforma en las [[Ecuaciones de Navier-Stokes]].

> [!referencia]
> Landau-Lifshitz, Vol. 6, §15 (ecuaciones del fluido viscoso); Batchelor, *An Introduction to Fluid Dynamics*, cap. 3 (ecuaciones de movimiento). Véase también [[Teorema del Transporte de Reynolds]] y [[Tensor de Esfuerzos de Cauchy]].
