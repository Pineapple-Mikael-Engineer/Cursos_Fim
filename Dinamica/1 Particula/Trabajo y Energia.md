---
title: Trabajo y Energía
tags:
  - dinamica
  - teoria
  - particula
  - energia
draft: false
aliases:
  - trabajo y energía
  - teorema trabajo-energía
  - energía cinética
  - energía potencial
  - fuerzas conservativas
  - conservación de la energía
  - work-energy theorem
  - kinetic energy
  - potential energy
  - conservative forces
---

# Trabajo y Energía $\;U_{1\to2}=T_2-T_1$

> [!definicion]
> El **trabajo** de una fuerza $\vec{F}$ a lo largo de la trayectoria que va del punto $1$ al punto $2$
> es la integral de línea
> $$U_{1\to2}=\int_{1}^{2}\vec{F}\cdot d\vec{r}.$$
> La **energía cinética** de una partícula de masa $m$ y rapidez $v$ es el escalar
> $$T=\tfrac12 m v^2.$$
> Ambos se relacionan por el **teorema trabajo-energía**: el trabajo **neto** (de la resultante de
> todas las fuerzas) iguala la variación de energía cinética,
> $$\boxed{\;U_{1\to2}^{\text{neto}}=T_2-T_1.\;}$$
> El trabajo es energía transferida a la partícula por la fuerza; su unidad SI es el **julio**,
> $1\ \text{J}=1\ \text{N}\cdot\text{m}$.

> [!info]
> Tercera sección de la [[1 Particula/index | partícula]] ([[Dinamica/index | Dinámica]]). Es la
> **primera integral de la** [[Cinetica de la Particula | segunda ley de Newton]] **en el espacio**:
> integrando $\sum\vec{F}=m\vec{a}$ a lo largo de la trayectoria nace el teorema trabajo-energía. La
> integral **en el tiempo** es su gemela, [[Impulso y Momento]]. Por eso conviene **deducir** estos
> teoremas, no memorizarlos. Modelo: Taylor, *Classical Mechanics*, cap. 4.

---

## Ejemplo

> [!ejemplo]
> **Bloque que desliza por una rampa lisa.**
>
> Un bloque de masa $m$ parte del **reposo** y desliza, sin rozamiento, descendiendo una altura $h$ por
> una rampa de inclinación cualquiera. Hallar su **rapidez** al pie de la rampa usando el teorema
> trabajo-energía.
>
> ![[rampa_trabajo.svg|380]]
>
> *En la rampa lisa solo trabaja el peso (la normal es perpendicular al desplazamiento): el trabajo neto es $mgh$, con $h$ el desnivel.*
>
> Sobre el bloque actúan dos fuerzas: la **normal** $\vec{N}$ (perpendicular a la rampa) y el **peso**
> $m\vec{g}$. La normal es **perpendicular al desplazamiento**, así que su trabajo es nulo. El peso, en
> cambio, tiene una componente a favor del movimiento; al bajar una altura $h$ realiza un trabajo
> $$U^{\text{neto}}=U_{\text{peso}}=mgh,$$
> porque solo cuenta el **desnivel vertical** $h$, no la longitud de la rampa (la componente horizontal
> del peso es nula y la integral $\int\vec{F}\cdot d\vec{r}$ proyecta el peso sobre la altura).
>
> > [!solucion]
> > El bloque parte del reposo, $T_1=0$; al final $T_2=\tfrac12 m v^2$. El teorema da
> > $$mgh=\tfrac12 m v^2-0\;\Rightarrow\; \boxed{v=\sqrt{2gh}.}$$
> > El resultado es **independiente de la masa** y de la **inclinación** de la rampa (por ser superficie
> > lisa): solo importa la altura descendida. Es el mismo $v=\sqrt{2gh}$ de la caída libre, lo que
> > anticipa que el peso es una fuerza **conservativa**.

---

## En qué consiste

> [!teorema] Teorema trabajo-energía
> Para una partícula, el trabajo neto de **todas** las fuerzas entre dos puntos de su trayectoria iguala
> la variación de su energía cinética:
> $$\boxed{\;U_{1\to2}^{\text{neto}}=\int_{1}^{2}\Big(\textstyle\sum\vec{F}\Big)\cdot d\vec{r}=T_2-T_1,\qquad T=\tfrac12 m v^2.\;}$$

> [!demostracion]
> **Paso 1 — Partir de Newton y multiplicar por $d\vec{r}$.** La segunda ley es
> $\sum\vec{F}=m\,\dfrac{d\vec{v}}{dt}$. Multiplicamos escalarmente por el desplazamiento infinitesimal
> $d\vec{r}=\vec{v}\,dt$:
> $$\sum\vec{F}\cdot d\vec{r}=m\,\frac{d\vec{v}}{dt}\cdot\vec{v}\,dt=m\,\vec{v}\cdot d\vec{v}.$$
> **Paso 2 — Reconocer la diferencial exacta.** Como $\vec{v}\cdot d\vec{v}=\tfrac12\,d(\vec{v}\cdot\vec{v})=\tfrac12\,d(v^2)$,
> el lado derecho es la diferencial de la energía cinética:
> $$\sum\vec{F}\cdot d\vec{r}=d\!\left(\tfrac12 m v^2\right)=dT.$$
> **Paso 3 — Integrar de $1$ a $2$.** Integrando a lo largo de la trayectoria,
> $$U_{1\to2}^{\text{neto}}=\int_{1}^{2}\sum\vec{F}\cdot d\vec{r}=\int_{1}^{2}dT=T_2-T_1.\qquad\blacksquare$$

> [!teoria] Fuerzas conservativas y energía potencial
> Una fuerza $\vec{F}$ es **conservativa** si su trabajo **no depende del camino** recorrido, sino solo
> de los puntos inicial y final. Esto equivale a cualquiera de estas condiciones:
> $$\oint\vec{F}\cdot d\vec{r}=0\quad\Longleftrightarrow\quad \nabla\times\vec{F}=\vec{0}.$$
> Cuando se cumplen, existe una función escalar $V(\vec{r})$, la **energía potencial**, tal que
> $$\boxed{\;\vec{F}=-\nabla V,\qquad U_{1\to2}=-(V_2-V_1).\;}$$
> Es decir, el trabajo de una fuerza conservativa es **menos la variación** de su potencial. Ejemplos
> centrales del curso:
>
> | Fuerza | Energía potencial $V$ |
> |:---|:---|
> | Gravedad uniforme | $V=mgy$ |
> | Resorte (ley de Hooke) | $V=\tfrac12 k x^2$ |
> | Gravitación universal | $V=-\dfrac{GMm}{r}$ |
>
> El signo $-$ es convencional pero universal: la fuerza apunta hacia donde $V$ **decrece** (hacia el
> mínimo de potencial).

> [!teorema] Conservación de la energía mecánica
> Si **todas** las fuerzas que realizan trabajo sobre la partícula son **conservativas**, la suma de
> energía cinética y potencial se mantiene constante:
> $$\boxed{\;T_1+V_1=T_2+V_2\equiv E=\text{cte}.\;}$$
> La cantidad $E=T+V$ es la **energía mecánica** de la partícula.

> [!demostracion]
> **Paso 1 — Escribir el trabajo neto como variación de potencial.** Si todas las fuerzas que trabajan
> son conservativas, su trabajo neto es, por la sección anterior,
> $$U_{1\to2}^{\text{neto}}=-(V_2-V_1).$$
> **Paso 2 — Combinar con el teorema trabajo-energía.** Aquel mismo trabajo neto vale $T_2-T_1$, de modo
> que
> $$T_2-T_1=-(V_2-V_1).$$
> **Paso 3 — Reagrupar.** Pasando los términos del punto $2$ a un lado y los del $1$ al otro,
> $$T_1+V_1=T_2+V_2.$$
> Como los puntos $1$ y $2$ eran arbitrarios, $T+V$ no cambia a lo largo del movimiento:
> $E=T+V=\text{cte}$. $\blacksquare$

> [!proposicion] Cuándo conviene usar trabajo-energía
> El teorema trabajo-energía es **escalar**: una sola ecuación, no tres como $\sum\vec{F}=m\vec{a}$.
> Resulta ideal cuando se conoce la **fuerza en función de la posición** y se buscan **rapideces** entre
> dos puntos, **sin** necesidad de resolver la trayectoria completa ni el tiempo. La contrapartida es
> que, al ser una sola ecuación, no da información direccional: para eso siguen haciendo falta las
> ecuaciones de Newton o el [[Impulso y Momento | impulso-momento]].

> [!warning]
> Cuidados al aplicar trabajo y energía:
> - El trabajo $U=\int\vec{F}\cdot d\vec{r}$ depende del **camino** para fuerzas **no conservativas**.
>   El **rozamiento** es el caso típico: $U_{\text{roz}}<0$ siempre (se opone al movimiento) y **disipa**
>   energía mecánica.
> - La energía mecánica $T+V$ se conserva **solo** si no hay fuerzas no conservativas que realicen
>   trabajo. Con rozamiento, $E$ **decrece**.
> - El trabajo de una fuerza **perpendicular** al movimiento es **cero**: la normal de una superficie, o
>   la tensión de un hilo cuando no hay deslizamiento, no aportan ni quitan energía cinética.

## Resumen

> [!resumen]
> | Concepto | Expresión |
> |:---|:---|
> | Trabajo de una fuerza | $U_{1\to2}=\int_{1}^{2}\vec{F}\cdot d\vec{r}$ |
> | Energía cinética | $T=\tfrac12 m v^2$ |
> | Teorema trabajo-energía | $U_{1\to2}^{\text{neto}}=T_2-T_1$ |
> | Fuerza conservativa | $\vec{F}=-\nabla V$, $\quad U_{1\to2}=-(V_2-V_1)$ |
> | Conservación de la energía | $T+V=E=\text{cte}$ (sin fuerzas no conservativas) |

> [!corolario]
> Trabajo y energía es Newton **integrado en el espacio**: convierte una ley vectorial en una **ecuación
> escalar** que liga fuerza (vía su integral de camino) con rapidez. Cuando la fuerza deriva de un
> potencial, esa ecuación se vuelve la **conservación de $T+V$**, una constante del movimiento que
> resuelve buena parte de los problemas sin integrar la trayectoria. Su gemela en el tiempo es el
> [[Impulso y Momento | impulso-momento]].

> [!referencia]
> Taylor, *Classical Mechanics*, cap. 4 (energía y fuerzas conservativas). Integral en el tiempo:
> [[Impulso y Momento]]. Origen dinámico: [[Cinetica de la Particula]]. Mapa del capítulo:
> [[1 Particula/index]].
