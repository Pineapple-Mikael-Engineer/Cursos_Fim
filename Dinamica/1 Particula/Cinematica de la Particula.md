---
title: Cinemática de la Partícula
tags:
  - dinamica
  - teoria
  - particula
  - cinematica
draft: false
aliases:
  - cinemática de la partícula
  - coordenadas intrínsecas
  - coordenadas polares
  - componentes tangencial y normal
---

# Cinemática de la Partícula $\;\vec{v}=\dot{\vec{r}},\ \vec{a}=\dot{\vec{v}}$

> [!definicion]
> La **cinemática** describe el movimiento sin atender a sus causas. El estado de una partícula es su
> **posición** $\vec{r}(t)$; de ella se derivan la **velocidad** y la **aceleración**:
> $$\vec{v}=\frac{d\vec{r}}{dt},\qquad \vec{a}=\frac{d\vec{v}}{dt}=\frac{d^2\vec{r}}{dt^2}.$$
> Estas definiciones son **independientes del sistema de coordenadas**; lo que cambia con él son las
> **componentes**. Se elige el sistema según la geometría: **cartesianas** (movimiento general),
> **intrínsecas** $(\hat t,\hat n)$ (cuando importa la trayectoria) o **polares** $(\hat e_r,\hat e_\theta)$
> (cuando hay un centro natural).

> [!info]
> Primera sección de la [[1 Particula/index | partícula]] ([[Dinamica/index | Dinámica]]). Las
> derivadas de la base polar que aquí aparecen ($\dot{\hat e}_r=\dot\theta\,\hat e_\theta$) son el caso
> plano del **[[Operador Derivada en Base Movil | operador derivada en base móvil]]** (sección 2): una
> base que gira tiene versores con derivada no nula. Fraile las usa el resto del curso.

---

## Ejemplo

> [!ejemplo]
> **Movimiento circular: las dos descripciones coinciden.**
>
> Una partícula recorre una circunferencia de radio $R$ con rapidez $v$ variable. Hallar su
> aceleración en coordenadas **intrínsecas** y en **polares**, y comprobar que son la misma.
>
> ![[coordenadas_cinematica.svg|680]]
>
> *Intrínsecas: $\hat t$ tangente (sentido del movimiento), $\hat n$ hacia el centro de curvatura $C$;
> la aceleración se parte en $a_t=\dot v$ y $a_n=v^2/\rho$. Polares: $\hat e_r$ a lo largo de $\vec r$,
> $\hat e_\theta$ perpendicular, en el sentido de $\theta$ creciente.*
>
> **Intrínsecas.** Para la circunferencia $\rho=R$ (constante), así que
> $$\vec{a}=\dot v\,\hat t+\frac{v^2}{R}\,\hat n.$$
>
> **Polares.** Aquí $r=R$ constante ($\dot r=\ddot r=0$) y $v=R\dot\theta$. Sustituyendo en las
> fórmulas polares (deducidas abajo):
> $$\vec{a}=(\underbrace{\ddot r}_{0}-R\dot\theta^2)\,\hat e_r+(R\ddot\theta+2\underbrace{\dot r}_{0}\dot\theta)\,\hat e_\theta=-R\dot\theta^2\,\hat e_r+R\ddot\theta\,\hat e_\theta.$$
>
> > [!solucion]
> > Como en la circunferencia $\hat e_r=-\hat n$ (radial hacia afuera = opuesto a $\hat n$, que apunta
> > al centro) y $\hat e_\theta=\hat t$, las dos expresiones coinciden:
> > $$a_n=\frac{v^2}{R}=R\dot\theta^2,\qquad a_t=\dot v=R\ddot\theta.\ \checkmark$$
> > La componente **normal/centrípeta** existe aunque la rapidez sea constante: es el precio de
> > **cambiar de dirección**.

---

## En qué consiste

> [!teoria] Cartesianas: el caso trivial
> Con base fija $\{\hat\imath,\hat\jmath,\hat k\}$ (versores **constantes**), derivar es derivar
> componentes:
> $$\vec{r}=x\hat\imath+y\hat\jmath+z\hat k\ \Rightarrow\ \vec{v}=\dot x\hat\imath+\dot y\hat\jmath+\dot z\hat k,\quad \vec{a}=\ddot x\hat\imath+\ddot y\hat\jmath+\ddot z\hat k.$$
> Toda la sutileza de las otras bases viene de que **sus versores no son constantes**.

> [!teorema] Componentes intrínsecas (tangencial y normal)
> Expresando la velocidad como $\vec{v}=v\,\hat t$ (rapidez $v=ds/dt$ por el versor tangente), la
> aceleración se descompone en
> $$\boxed{\;\vec{a}=\dot v\,\hat t+\frac{v^2}{\rho}\,\hat n\;}$$
> con $\dot v$ la **aceleración tangencial** (cambia la rapidez) y $v^2/\rho$ la **normal** o
> **centrípeta** (cambia la dirección), dirigida al centro de curvatura; $\rho$ es el **radio de
> curvatura**.

> [!demostracion]
> **Paso 1 — Derivar $\vec{v}=v\,\hat t$.** Por la regla del producto,
> $$\vec{a}=\frac{d}{dt}(v\,\hat t)=\dot v\,\hat t+v\,\frac{d\hat t}{dt}.$$
> **Paso 2 — La derivada del tangente (Frenet).** $\hat t$ es unitario, luego $\dfrac{d\hat t}{dt}$ es
> perpendicular a $\hat t$ (de $\hat t\cdot\hat t=1$ sale $\hat t\cdot\dot{\hat t}=0$). Usando la regla
> de la cadena con la longitud de arco $s$,
> $$\frac{d\hat t}{dt}=\frac{d\hat t}{ds}\frac{ds}{dt}=v\,\frac{d\hat t}{ds}.$$
> Por definición de **curvatura** $\kappa=1/\rho$, $\dfrac{d\hat t}{ds}=\kappa\,\hat n=\dfrac{1}{\rho}\hat n$
> (el versor normal apunta hacia el centro de curvatura).
> **Paso 3 — Sustituir.**
> $$\vec{a}=\dot v\,\hat t+v\left(v\,\frac{1}{\rho}\hat n\right)=\dot v\,\hat t+\frac{v^2}{\rho}\,\hat n.\qquad\blacksquare$$

> [!teorema] Componentes polares
> En coordenadas polares planas, con $\vec{r}=r\,\hat e_r$,
> $$\boxed{\;\vec{v}=\dot r\,\hat e_r+r\dot\theta\,\hat e_\theta,\qquad \vec{a}=(\ddot r-r\dot\theta^2)\,\hat e_r+(r\ddot\theta+2\dot r\dot\theta)\,\hat e_\theta\;}$$
> El término $-r\dot\theta^2$ es la aceleración **centrípeta** y $2\dot r\dot\theta$ la de **Coriolis**
> (aparece cuando la partícula se aleja, $\dot r\neq0$, mientras gira).

> [!demostracion]
> **Paso 1 — Derivadas de la base que gira.** Los versores polares dependen de $\theta$:
> $\hat e_r=(\cos\theta,\operatorname{sen}\theta)$, $\hat e_\theta=(-\operatorname{sen}\theta,\cos\theta)$.
> Derivando respecto al tiempo (regla de la cadena, $\dot\theta$):
> $$\frac{d\hat e_r}{dt}=\dot\theta\,\hat e_\theta,\qquad \frac{d\hat e_\theta}{dt}=-\dot\theta\,\hat e_r.$$
> (Son el caso plano de $\dot{\hat e}=\vec\omega\times\hat e$ con $\vec\omega=\dot\theta\,\hat k$.)
> **Paso 2 — Velocidad.** Derivando $\vec{r}=r\,\hat e_r$:
> $$\vec{v}=\dot r\,\hat e_r+r\,\dot{\hat e}_r=\dot r\,\hat e_r+r\dot\theta\,\hat e_\theta.$$
> **Paso 3 — Aceleración.** Derivando $\vec{v}$, término a término:
> $$\vec{a}=\ddot r\,\hat e_r+\dot r\,\dot{\hat e}_r+(\dot r\dot\theta+r\ddot\theta)\,\hat e_\theta+r\dot\theta\,\dot{\hat e}_\theta.$$
> Sustituyendo $\dot{\hat e}_r=\dot\theta\hat e_\theta$ y $\dot{\hat e}_\theta=-\dot\theta\hat e_r$ y
> agrupando:
> $$\vec{a}=(\ddot r-r\dot\theta^2)\,\hat e_r+(r\ddot\theta+2\dot r\dot\theta)\,\hat e_\theta.\qquad\blacksquare$$

> [!proposicion] El hilo con el operador base móvil
> Las relaciones $\dot{\hat e}_r=\dot\theta\,\hat e_\theta$, $\dot{\hat e}_\theta=-\dot\theta\,\hat e_r$
> son la **fórmula de Poisson** $\dot{\hat e}=\vec\omega\times\hat e$ en el plano, con
> $\vec\omega=\dot\theta\,\hat k$. Toda la cinemática en bases móviles —incluida la del cuerpo rígido y
> el efecto Coriolis— se obtiene del mismo modo. → [[Operador Derivada en Base Movil]].

> [!warning]
> No confundir el **radio de curvatura** $\rho$ (intrínsecas) con la **coordenada radial** $r$
> (polares): coinciden solo en la circunferencia. La componente normal $a_n=v^2/\rho$ **nunca es
> negativa** y existe siempre que la trayectoria se curve, aun a rapidez constante. El término de
> Coriolis $2\dot r\dot\theta$ se olvida con frecuencia: aparece **solo** si $\dot r$ y $\dot\theta$
> son ambos no nulos.

## Resumen

> [!resumen]
> | Sistema | Velocidad | Aceleración |
> |:---|:---|:---|
> | Cartesianas | $\dot x\,\hat\imath+\dot y\,\hat\jmath$ | $\ddot x\,\hat\imath+\ddot y\,\hat\jmath$ |
> | Intrínsecas | $v\,\hat t$ | $\dot v\,\hat t+\dfrac{v^2}{\rho}\,\hat n$ |
> | Polares | $\dot r\,\hat e_r+r\dot\theta\,\hat e_\theta$ | $(\ddot r-r\dot\theta^2)\,\hat e_r+(r\ddot\theta+2\dot r\dot\theta)\,\hat e_\theta$ |

> [!corolario]
> La velocidad y la aceleración son únicas; cada base las **proyecta** distinto. La clave técnica es
> que las bases intrínseca y polar **giran**, y por eso sus versores tienen derivada no nula —el germen
> del operador en base móvil que vertebra toda la cinemática del curso.

> [!referencia]
> Taylor, *Classical Mechanics*, §1.7-1.9. Base móvil general: [[Operador Derivada en Base Movil]]. Su
> uso dinámico: [[Cinetica de la Particula]].
