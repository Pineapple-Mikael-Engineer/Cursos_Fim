---
title: Cinética de la Partícula
tags:
  - dinamica
  - teoria
  - particula
  - cinetica
draft: false
aliases:
  - cinética de la partícula
  - leyes de Newton
  - ecuaciones de movimiento
  - segunda ley de Newton
  - kinetics
  - equations of motion
---

# Cinética de la Partícula $\;\sum\vec F=m\vec a$

> [!definicion]
> La **cinética** relaciona las **fuerzas** con el **movimiento** mediante las **leyes de Newton**. En
> un **marco inercial**, el movimiento de la partícula queda gobernado por la **segunda ley**:
> $$\sum\vec F=m\vec a=\frac{d\vec p}{dt},\qquad \vec p=m\vec v.$$
> Las tres leyes de Newton son:
> 1. **Ley de inercia.** Existe un **marco inercial** en el que una partícula libre ($\sum\vec F=\vec 0$)
>    permanece en reposo o en movimiento rectilíneo uniforme ($\vec v=\text{cte}$).
> 2. **Ley fundamental.** En ese marco, $\displaystyle\sum\vec F=m\vec a$: la fuerza neta es la causa de
>    la aceleración, proporcional a ella por la **masa inercial** $m$.
> 3. **Acción y reacción.** Si la partícula $A$ ejerce $\vec F_{AB}$ sobre $B$, entonces $B$ ejerce
>    $\vec F_{BA}=-\vec F_{AB}$ sobre $A$ (misma recta, sentido opuesto).

> [!info]
> Segunda sección de la [[1 Particula/index | partícula]] ([[Dinamica/index | Dinámica]]): es el puente
> entre la descripción y sus causas. Toma la aceleración $\vec a$ deducida en
> [[Cinematica de la Particula]] y la inserta en $\sum\vec F=m\vec a$, proyectándola según la geometría
> (intrínsecas o polares). Integrada **en el espacio** da [[Trabajo y Energia]]; integrada **en el
> tiempo**, [[Impulso y Momento]]. En marcos **no inerciales** la segunda ley exige añadir
> **pseudofuerzas** → [[Operador Derivada en Base Movil]]. Referencia: Taylor, caps. 1-2.

---

## Ejemplo

> [!ejemplo]
> **Curva plana: rapidez máxima sin derrapar.**
>
> Un automóvil de masa $m$ toma una curva **plana** (sin peralte) de radio $R$ con rapidez $v$
> constante. El coeficiente de rozamiento **estático** entre neumáticos y asfalto es $\mu$. Hallar la
> **rapidez máxima** $v_{max}$ con la que puede tomar la curva sin derrapar.
>
> Es un movimiento circular uniforme: conviene proyectar $\sum\vec F=m\vec a$ en **coordenadas
> intrínsecas**. La única fuerza horizontal es el **rozamiento** $\vec f$, que debe aportar toda la
> aceleración normal (centrípeta) que curva la trayectoria hacia el centro.
>
> > [!solucion]
> > **Vertical (eje vertical fijo).** No hay aceleración vertical, así que la normal del suelo
> > equilibra el peso:
> > $$N-mg=0\ \Rightarrow\ N=mg.$$
> > **Dirección normal $\hat n$ (hacia el centro).** La rapidez es constante ($\dot v=0$), luego solo
> > hay componente normal $a_n=v^2/R$, suministrada por el rozamiento:
> > $$\sum F_n=m\frac{v^2}{R}\ \Rightarrow\ f=m\frac{v^2}{R}.$$
> > **Condición de no derrape.** El rozamiento estático está acotado, $f\le\mu N=\mu mg$. En el
> > **límite** ($f=\mu N$) se alcanza la rapidez máxima:
> > $$\mu mg=m\frac{v_{max}^2}{R}\ \Rightarrow\ \boxed{\,v_{max}=\sqrt{\mu g R}\,}.$$
> > La masa $m$ **se cancela**: la rapidez máxima **no depende de la masa**, solo de $\mu$, $g$ y $R$.
> > Por ejemplo, con $\mu=0{,}80$, $R=50\ \text{m}$ y $g=9{,}8\ \text{m/s}^2$,
> > $v_{max}=\sqrt{0{,}80\cdot 9{,}8\cdot 50}\approx 19{,}8\ \text{m/s}$ (unos $71\ \text{km/h}$).

---

## En qué consiste

> [!teoria] Qué dicen realmente las leyes
> - La **primera ley** no es un caso particular de la segunda: **define** los marcos en que vale la
>   segunda. Un **marco inercial** es aquel en el que una partícula libre no acelera; solo en él tiene
>   sentido escribir $\sum\vec F=m\vec a$.
> - En la **segunda ley**, $m\vec a$ **no es una fuerza**: es el *efecto* de las fuerzas, no una de
>   ellas. **Nunca se dibuja en el diagrama de cuerpo libre (DCL)**; en el DCL solo van las fuerzas
>   reales (peso, normal, tensión, rozamiento…).
> - $\sum\vec F=m\vec a$ es una ecuación **vectorial**: en el espacio equivale a **hasta tres
>   ecuaciones escalares** (una por eje). Se elige el sistema de coordenadas que **desacople** esas
>   ecuaciones —el que alinee los ejes con las direcciones naturales del problema (tangente/normal a la
>   trayectoria, radial/transversal a un centro).
> - La **tercera ley** garantiza que las fuerzas internas de un sistema se cancelan por pares: es la
>   que permite tratar luego un cuerpo extenso como [[Sistemas de Particulas | sistema de partículas]].

> [!teorema] Ecuaciones de movimiento proyectadas (intrínsecas y polares)
> Proyectando $\sum\vec F=m\vec a$ sobre las bases móviles de la cinemática se obtienen las **ecuaciones
> de movimiento** escalares:
> $$\boxed{\;\sum F_t=m\dot v,\qquad \sum F_n=m\frac{v^2}{\rho}\;}\qquad\text{(intrínsecas)}$$
> $$\boxed{\;\sum F_r=m(\ddot r-r\dot\theta^2),\qquad \sum F_\theta=m(r\ddot\theta+2\dot r\dot\theta)\;}\qquad\text{(polares)}$$
> donde $v$ es la rapidez, $\rho$ el radio de curvatura, $(r,\theta)$ las coordenadas polares planas.

> [!demostracion]
> **Paso 1 — La aceleración ya está deducida.** En [[Cinematica de la Particula]] se demostró que, en
> las bases móviles,
> $$\vec a=\dot v\,\hat t+\frac{v^2}{\rho}\,\hat n\qquad\text{(intrínsecas)},$$
> $$\vec a=(\ddot r-r\dot\theta^2)\,\hat e_r+(r\ddot\theta+2\dot r\dot\theta)\,\hat e_\theta\qquad\text{(polares)}.$$
> **Paso 2 — Insertar en la segunda ley.** Como $m$ es constante, multiplicar por $m$:
> $$m\vec a=m\dot v\,\hat t+m\frac{v^2}{\rho}\,\hat n,\qquad
> m\vec a=m(\ddot r-r\dot\theta^2)\,\hat e_r+m(r\ddot\theta+2\dot r\dot\theta)\,\hat e_\theta.$$
> **Paso 3 — Igualar componente a componente.** La igualdad vectorial $\sum\vec F=m\vec a$ vale para
> **cada** versor por separado (la base es ortonormal). Escribiendo la fuerza neta en la misma base,
> $\sum\vec F=\sum F_t\,\hat t+\sum F_n\,\hat n$ y $\sum\vec F=\sum F_r\,\hat e_r+\sum F_\theta\,\hat e_\theta$,
> e identificando coeficientes:
> $$\sum F_t=m\dot v,\quad \sum F_n=m\frac{v^2}{\rho};\qquad
> \sum F_r=m(\ddot r-r\dot\theta^2),\quad \sum F_\theta=m(r\ddot\theta+2\dot r\dot\theta).\qquad\blacksquare$$

> [!proposicion] La normal neta es la que curva la trayectoria
> La componente **normal** de la fuerza neta es la responsable del **cambio de dirección**:
> $$\sum F_n=m\frac{v^2}{\rho}>0\quad\text{(dirigida al centro de curvatura)}.$$
> Como $v^2/\rho\ge 0$, la fuerza normal neta **siempre apunta hacia el centro** (es centrípeta) y se
> anula solo en trayectoria recta ($\rho\to\infty$). Sin fuerza con componente normal **no hay cambio
> de dirección**: la partícula sigue recto. Por su parte, la componente **tangencial** $\sum F_t=m\dot v$
> es la única que **cambia la rapidez**; si $\sum F_t=0$, el movimiento es a rapidez constante (aunque
> la dirección sí cambie).

> [!warning]
> - La segunda ley **solo** vale en un **marco inercial**. En un marco **acelerado o rotante** hay que
>   añadir **pseudofuerzas** (centrífuga, Coriolis, de arrastre) para que $\sum\vec F=m\vec a$ siga
>   siendo válida → [[Operador Derivada en Base Movil]].
> - $m\vec a$ **no es una fuerza**: no aparece en el DCL. Sumar fuerzas reales en un lado, $m\vec a$ en
>   el otro.
> - La forma $\sum\vec F=m\vec a$ supone $m$ **constante**. Si la masa varía (cohetes, cuerpos que
>   acretan/expulsan masa) hay que volver a la forma general $\sum\vec F=\dfrac{d\vec p}{dt}$.

## Resumen

> [!resumen]
> | Ley / proyección | Enunciado o ecuación |
> |:---|:---|
> | 1ª — inercia | partícula libre $\Rightarrow \vec v=\text{cte}$; define el marco inercial |
> | 2ª — fundamental | $\sum\vec F=m\vec a=d\vec p/dt$, con $\vec p=m\vec v$ |
> | 3ª — acción-reacción | $\vec F_{BA}=-\vec F_{AB}$ |
> | Intrínsecas $(\hat t,\hat n)$ | $\sum F_t=m\dot v,\;\;\sum F_n=m\,v^2/\rho$ |
> | Polares $(\hat e_r,\hat e_\theta)$ | $\sum F_r=m(\ddot r-r\dot\theta^2),\;\;\sum F_\theta=m(r\ddot\theta+2\dot r\dot\theta)$ |

> [!corolario]
> Plantear cinética es siempre el mismo método: **(1)** dibujar el DCL con las fuerzas reales; **(2)**
> elegir la base que **desacople** (intrínseca si importa la trayectoria, polar si hay un centro);
> **(3)** escribir $\sum\vec F=m\vec a$ componente a componente usando la aceleración de la cinemática;
> **(4)** resolver. Integrar después estas ecuaciones —en el espacio o en el tiempo— produce los
> teoremas de [[Trabajo y Energia]] e [[Impulso y Momento]].

> [!referencia]
> Taylor, *Classical Mechanics*, caps. 1-2. Aceleración proyectada:
> [[Cinematica de la Particula]]. Marcos no inerciales y pseudofuerzas:
> [[Operador Derivada en Base Movil]]. Primeras integrales: [[Trabajo y Energia]],
> [[Impulso y Momento]]. Capítulo: [[1 Particula/index]].
