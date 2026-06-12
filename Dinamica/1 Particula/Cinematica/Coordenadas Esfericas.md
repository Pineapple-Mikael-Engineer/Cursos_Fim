---
title: Coordenadas Esféricas
tags:
  - dinamica
  - teoria
  - particula
  - cinematica
draft: false
aliases:
  - coordenadas esféricas
  - spherical coordinates
  - base esférica
  - velocidad y aceleración esféricas
---

# Coordenadas Esféricas $(\hat e_r,\hat e_\theta,\hat e_\varphi)$

> [!definicion]
> Las **coordenadas esféricas** $(r,\theta,\varphi)$ localizan la partícula respecto de un **centro**:
> - $r\ge 0$ es la **distancia al origen**,
> - $\theta\in[0,\pi]$ es el **ángulo polar**, medido desde el eje $+z$,
> - $\varphi\in[0,2\pi)$ es el **azimut**, el ángulo de la proyección sobre el plano $xy$.
>
> La posición es, simplemente,
> $$\vec r=r\,\hat e_r.$$
> La base $(\hat e_r,\hat e_\theta,\hat e_\varphi)$ es **ortonormal y directa** ($\hat e_r\times\hat e_\theta=\hat e_\varphi$),
> pero **gira con la partícula**: sus tres versores cambian de dirección al moverse $\theta$ o $\varphi$.
> La velocidad resulta
> $$\vec v=\dot r\,\hat e_r+r\dot\theta\,\hat e_\theta+r\operatorname{sen}\theta\,\dot\varphi\,\hat e_\varphi.$$

> [!info]
> Nota de la [[Cinematica/index | cinemática de la partícula]] ([[1 Particula/index | partícula]]).
> Las esféricas son las coordenadas idóneas para los **campos centrales** —gravitación, Coulomb—,
> donde la fuerza solo depende de $r$ y conviene una base radial; **generalizan** las
> [[Coordenadas Cilindricas | cilíndricas]] midiendo la distancia al **centro** en lugar de al eje.
> El que los versores tengan derivada no nula es el caso particular del
> [[Operador Derivada en Base Movil | operador derivada en base móvil]]. Referencia: Taylor §1.7.

---

## Ejemplo

> [!ejemplo]
> **Movimiento sobre una esfera ($r=R$ constante).**
>
> Una partícula está obligada a moverse sobre una esfera de radio $R$ (por ejemplo, una cuenta en un
> casquete liso). Con $r=R$, $\dot r=\ddot r=0$, hallar su velocidad y la componente radial de su
> aceleración.

> ![[coordenadas_esfericas.svg|350]]
>
> *Coordenadas esféricas $(r,\theta,\varphi)$: $r$ al origen, $\theta$ polar desde $z$, $\varphi$ azimut; base móvil $(\hat e_r,\hat e_\theta,\hat e_\varphi)$.*
>
> **Paso 1 — Velocidad.** Anulando $\dot r$ en la fórmula general,
> $$\vec v=R\dot\theta\,\hat e_\theta+R\operatorname{sen}\theta\,\dot\varphi\,\hat e_\varphi.$$
> No hay parte radial: el movimiento es **tangente** a la esfera, como debe ser.
>
> **Paso 2 — Aceleración radial.** En $a_r=\ddot r-r\dot\theta^2-r\operatorname{sen}^2\theta\,\dot\varphi^2$
> se anula $\ddot r$:
> $$a_r=-R\big(\dot\theta^2+\operatorname{sen}^2\theta\,\dot\varphi^2\big)=-\frac{v^2}{R},$$
> usando $v^2=R^2\dot\theta^2+R^2\operatorname{sen}^2\theta\,\dot\varphi^2$.
>
> > [!solucion]
> > La aceleración radial es **centrípeta** y vale $-v^2/R$, exactamente la que apunta hacia el centro
> > de la esfera; la ligadura $r=R$ la suministra a través de la reacción normal del casquete. El
> > resto de la aceleración ($\hat e_\theta,\hat e_\varphi$) es tangente a la superficie y la fijan las
> > fuerzas reales sobre la partícula.

---

## En qué consiste

> [!teoria] La base esférica como vectores cartesianos
> Expresada en la base fija $\{\hat\imath,\hat\jmath,\hat k\}$, la terna esférica es
> $$\hat e_r=(\operatorname{sen}\theta\cos\varphi,\ \operatorname{sen}\theta\operatorname{sen}\varphi,\ \cos\theta),$$
> $$\hat e_\theta=(\cos\theta\cos\varphi,\ \cos\theta\operatorname{sen}\varphi,\ -\operatorname{sen}\theta),$$
> $$\hat e_\varphi=(-\operatorname{sen}\varphi,\ \cos\varphi,\ 0).$$
> Se comprueba directamente que son **unitarios y ortogonales** entre sí, y que $\hat e_r\times\hat e_\theta=\hat e_\varphi$.
> El versor $\hat e_r$ apunta hacia afuera (crece $r$), $\hat e_\theta$ en el sentido de crecer $\theta$
> (hacia el ecuador) y $\hat e_\varphi$ en el de crecer $\varphi$ (tangente a los paralelos).

> [!teorema] Derivadas temporales de la base
> Al moverse la partícula, los versores giran según
> $$\dot{\hat e}_r=\dot\theta\,\hat e_\theta+\dot\varphi\operatorname{sen}\theta\,\hat e_\varphi,$$
> $$\dot{\hat e}_\theta=-\dot\theta\,\hat e_r+\dot\varphi\cos\theta\,\hat e_\varphi,$$
> $$\dot{\hat e}_\varphi=-\dot\varphi\operatorname{sen}\theta\,\hat e_r-\dot\varphi\cos\theta\,\hat e_\theta.$$

> [!demostracion]
> **Paso 1 — Derivar $\hat e_r$.** Las componentes de $\hat e_r$ dependen del tiempo solo a través de
> $\theta(t)$ y $\varphi(t)$; por la regla de la cadena,
> $$\dot{\hat e}_r=\frac{\partial\hat e_r}{\partial\theta}\dot\theta+\frac{\partial\hat e_r}{\partial\varphi}\dot\varphi.$$
> Calculando las parciales sobre $\hat e_r=(\operatorname{sen}\theta\cos\varphi,\operatorname{sen}\theta\operatorname{sen}\varphi,\cos\theta)$:
> $$\frac{\partial\hat e_r}{\partial\theta}=(\cos\theta\cos\varphi,\cos\theta\operatorname{sen}\varphi,-\operatorname{sen}\theta)=\hat e_\theta,$$
> $$\frac{\partial\hat e_r}{\partial\varphi}=(-\operatorname{sen}\theta\operatorname{sen}\varphi,\operatorname{sen}\theta\cos\varphi,0)=\operatorname{sen}\theta\,(-\operatorname{sen}\varphi,\cos\varphi,0)=\operatorname{sen}\theta\,\hat e_\varphi.$$
> Por tanto $\dot{\hat e}_r=\dot\theta\,\hat e_\theta+\dot\varphi\operatorname{sen}\theta\,\hat e_\varphi$.
> **Paso 2 — Derivar $\hat e_\theta$.** Igual procedimiento con $\hat e_\theta=(\cos\theta\cos\varphi,\cos\theta\operatorname{sen}\varphi,-\operatorname{sen}\theta)$:
> $$\frac{\partial\hat e_\theta}{\partial\theta}=(-\operatorname{sen}\theta\cos\varphi,-\operatorname{sen}\theta\operatorname{sen}\varphi,-\cos\theta)=-\hat e_r,$$
> $$\frac{\partial\hat e_\theta}{\partial\varphi}=(-\cos\theta\operatorname{sen}\varphi,\cos\theta\cos\varphi,0)=\cos\theta\,\hat e_\varphi,$$
> de donde $\dot{\hat e}_\theta=-\dot\theta\,\hat e_r+\dot\varphi\cos\theta\,\hat e_\varphi$.
> **Paso 3 — Derivar $\hat e_\varphi$.** Con $\hat e_\varphi=(-\operatorname{sen}\varphi,\cos\varphi,0)$,
> que **no depende de $\theta$**:
> $$\frac{\partial\hat e_\varphi}{\partial\theta}=\vec 0,\qquad \frac{\partial\hat e_\varphi}{\partial\varphi}=(-\cos\varphi,-\operatorname{sen}\varphi,0).$$
> Falta proyectar este último sobre la base. Como $(-\cos\varphi,-\operatorname{sen}\varphi,0)=-\operatorname{sen}\theta\,\hat e_r-\cos\theta\,\hat e_\theta$
> (compruébese sumando $-\operatorname{sen}\theta\,\hat e_r-\cos\theta\,\hat e_\theta$ componente a componente),
> resulta $\dot{\hat e}_\varphi=-\dot\varphi\operatorname{sen}\theta\,\hat e_r-\dot\varphi\cos\theta\,\hat e_\theta$. $\blacksquare$

> [!teorema] Velocidad en esféricas
> $$\boxed{\;\vec v=\dot r\,\hat e_r+r\dot\theta\,\hat e_\theta+r\operatorname{sen}\theta\,\dot\varphi\,\hat e_\varphi\;}$$
> La componente $\dot r$ es **radial** (la partícula se aleja del centro), $r\dot\theta$ es la velocidad
> sobre los **meridianos** y $r\operatorname{sen}\theta\,\dot\varphi$ la velocidad sobre los **paralelos**
> (el radio efectivo del paralelo es $r\operatorname{sen}\theta$).

> [!demostracion]
> **Paso 1 — Derivar la posición $\vec r=r\,\hat e_r$.** Por la regla del producto,
> $$\vec v=\frac{d}{dt}(r\,\hat e_r)=\dot r\,\hat e_r+r\,\dot{\hat e}_r.$$
> **Paso 2 — Sustituir $\dot{\hat e}_r$** del teorema anterior:
> $$\vec v=\dot r\,\hat e_r+r\big(\dot\theta\,\hat e_\theta+\dot\varphi\operatorname{sen}\theta\,\hat e_\varphi\big)
> =\dot r\,\hat e_r+r\dot\theta\,\hat e_\theta+r\operatorname{sen}\theta\,\dot\varphi\,\hat e_\varphi.\ \blacksquare$$

> [!teorema] Aceleración en esféricas
> $$\vec a=\big(\ddot r-r\dot\theta^2-r\operatorname{sen}^2\theta\,\dot\varphi^2\big)\,\hat e_r
> +\big(r\ddot\theta+2\dot r\dot\theta-r\operatorname{sen}\theta\cos\theta\,\dot\varphi^2\big)\,\hat e_\theta$$
> $$+\big(r\operatorname{sen}\theta\,\ddot\varphi+2\dot r\operatorname{sen}\theta\,\dot\varphi+2r\cos\theta\,\dot\theta\dot\varphi\big)\,\hat e_\varphi.$$

> [!demostracion]
> Se deriva $\vec v=\dot r\,\hat e_r+r\dot\theta\,\hat e_\theta+r\operatorname{sen}\theta\,\dot\varphi\,\hat e_\varphi$
> término a término y se sustituyen las derivadas de la base.
>
> **Paso 1 — Derivar los tres términos.** Por la regla del producto,
> $$\vec a=\underbrace{\ddot r\,\hat e_r+\dot r\,\dot{\hat e}_r}_{(\mathrm{I})}
> +\underbrace{(\dot r\dot\theta+r\ddot\theta)\,\hat e_\theta+r\dot\theta\,\dot{\hat e}_\theta}_{(\mathrm{II})}
> +\underbrace{(\dot r\operatorname{sen}\theta\,\dot\varphi+r\cos\theta\,\dot\theta\dot\varphi+r\operatorname{sen}\theta\,\ddot\varphi)\,\hat e_\varphi+r\operatorname{sen}\theta\,\dot\varphi\,\dot{\hat e}_\varphi}_{(\mathrm{III})}.$$
>
> **Paso 2 — Insertar las derivadas de la base.**
> $$\dot{\hat e}_r=\dot\theta\,\hat e_\theta+\dot\varphi\operatorname{sen}\theta\,\hat e_\varphi,\quad
> \dot{\hat e}_\theta=-\dot\theta\,\hat e_r+\dot\varphi\cos\theta\,\hat e_\varphi,\quad
> \dot{\hat e}_\varphi=-\dot\varphi\operatorname{sen}\theta\,\hat e_r-\dot\varphi\cos\theta\,\hat e_\theta.$$
>
> **Paso 3 — Componente $\hat e_r$ en detalle.** Solo aportan parte radial: el $\ddot r\,\hat e_r$ de (I),
> el $r\dot\theta\,\dot{\hat e}_\theta$ de (II) y el $r\operatorname{sen}\theta\,\dot\varphi\,\dot{\hat e}_\varphi$ de (III).
> De (II): $r\dot\theta\,(-\dot\theta\,\hat e_r+\cdots)$ da $-r\dot\theta^2\,\hat e_r$. De (III):
> $r\operatorname{sen}\theta\,\dot\varphi\,(-\dot\varphi\operatorname{sen}\theta\,\hat e_r-\cdots)$ da
> $-r\operatorname{sen}^2\theta\,\dot\varphi^2\,\hat e_r$. Sumando,
> $$a_r=\ddot r-r\dot\theta^2-r\operatorname{sen}^2\theta\,\dot\varphi^2.$$
>
> **Paso 4 — Componentes $\hat e_\theta$ y $\hat e_\varphi$ por el mismo procedimiento.** Recogiendo de
> (I)-(III) todos los términos con $\hat e_\theta$ —el $(\dot r\dot\theta+r\ddot\theta)$ de (II), el
> $\dot r\,\dot{\hat e}_r$ de (I) que aporta $\dot r\dot\theta\,\hat e_\theta$, y el
> $r\operatorname{sen}\theta\,\dot\varphi\,\dot{\hat e}_\varphi$ de (III) que aporta $-r\operatorname{sen}\theta\cos\theta\,\dot\varphi^2\,\hat e_\theta$— se obtiene
> $$a_\theta=r\ddot\theta+2\dot r\dot\theta-r\operatorname{sen}\theta\cos\theta\,\dot\varphi^2.$$
> Análogamente, los términos con $\hat e_\varphi$ —el $\dot r\,\dot{\hat e}_r$ aporta
> $\dot r\operatorname{sen}\theta\,\dot\varphi\,\hat e_\varphi$, el $r\dot\theta\,\dot{\hat e}_\theta$
> aporta $r\dot\theta\cos\theta\,\dot\varphi\,\hat e_\varphi$, más el paréntesis explícito de (III)— dan
> $$a_\varphi=r\operatorname{sen}\theta\,\ddot\varphi+2\dot r\operatorname{sen}\theta\,\dot\varphi+2r\cos\theta\,\dot\theta\dot\varphi.$$
> Reuniendo las tres componentes se obtiene la fórmula del teorema. $\blacksquare$

> [!proposicion] Casos particulares
> - **Plano ecuatorial.** Si $\theta=\pi/2$ constante (luego $\dot\theta=\ddot\theta=0$,
>   $\operatorname{sen}\theta=1$, $\cos\theta=0$), la velocidad se reduce a
>   $\vec v=\dot r\,\hat e_r+r\dot\varphi\,\hat e_\varphi$ y la aceleración a
>   $\vec a=(\ddot r-r\dot\varphi^2)\,\hat e_r+(r\ddot\varphi+2\dot r\dot\varphi)\,\hat e_\varphi$: se
>   recuperan exactamente las **coordenadas polares** (con $\varphi$ en el papel del ángulo polar).
> - **Términos centrípetos y de Coriolis.** En $a_r$ aparecen los términos **centrípetos**
>   $-r\dot\theta^2$ y $-r\operatorname{sen}^2\theta\,\dot\varphi^2$ (van hacia el centro al rotar la
>   base); los $2\dot r\dot\theta$, $2\dot r\operatorname{sen}\theta\,\dot\varphi$ y
>   $2r\cos\theta\,\dot\theta\dot\varphi$ son términos tipo **Coriolis**, productos de dos velocidades
>   distintas que aparecen porque la base gira.

> [!warning]
> Aquí $r$ es la distancia al **origen**, no al eje como en [[Coordenadas Cilindricas | cilíndricas]]
> (allí el radio cilíndrico es $r=r_{\text{esf}}\operatorname{sen}\theta$). La aceleración esférica es
> larga: conviene **deducirla** con las derivadas de la base, no memorizarla. Cuidado con la convención
> $(\theta$ polar desde $+z$, $\varphi$ azimut$)$: muchos textos de matemáticas o física la intercambian,
> lo que altera los senos y cosenos de todas las fórmulas.

## Resumen

> [!resumen]
> | Magnitud | Expresión |
> |:---|:---|
> | Base (cartesiana) | $\hat e_r=(\operatorname{sen}\theta\cos\varphi,\operatorname{sen}\theta\operatorname{sen}\varphi,\cos\theta)$; $\hat e_\theta=(\cos\theta\cos\varphi,\cos\theta\operatorname{sen}\varphi,-\operatorname{sen}\theta)$; $\hat e_\varphi=(-\operatorname{sen}\varphi,\cos\varphi,0)$ |
> | Derivadas de la base | $\dot{\hat e}_r=\dot\theta\hat e_\theta+\dot\varphi\operatorname{sen}\theta\,\hat e_\varphi$; $\dot{\hat e}_\theta=-\dot\theta\hat e_r+\dot\varphi\cos\theta\,\hat e_\varphi$; $\dot{\hat e}_\varphi=-\dot\varphi\operatorname{sen}\theta\,\hat e_r-\dot\varphi\cos\theta\,\hat e_\theta$ |
> | Velocidad | $\vec v=\dot r\,\hat e_r+r\dot\theta\,\hat e_\theta+r\operatorname{sen}\theta\,\dot\varphi\,\hat e_\varphi$ |
> | $a_r$ | $\ddot r-r\dot\theta^2-r\operatorname{sen}^2\theta\,\dot\varphi^2$ |
> | $a_\theta$ | $r\ddot\theta+2\dot r\dot\theta-r\operatorname{sen}\theta\cos\theta\,\dot\varphi^2$ |
> | $a_\varphi$ | $r\operatorname{sen}\theta\,\ddot\varphi+2\dot r\operatorname{sen}\theta\,\dot\varphi+2r\cos\theta\,\dot\theta\dot\varphi$ |
> | Caso polar ($\theta=\pi/2$) | $\vec v=\dot r\,\hat e_r+r\dot\varphi\,\hat e_\varphi$; $\vec a=(\ddot r-r\dot\varphi^2)\hat e_r+(r\ddot\varphi+2\dot r\dot\varphi)\hat e_\varphi$ |

> [!corolario]
> Toda la cinemática esférica se sigue de un único hecho: la base $(\hat e_r,\hat e_\theta,\hat e_\varphi)$
> **gira** con la partícula, de modo que $\vec v$ y $\vec a$ se obtienen derivando $\vec r=r\hat e_r$ y
> arrastrando las derivadas de los versores. Es el mismo mecanismo de las
> [[Coordenadas Cilindricas | cilíndricas]] y de las [[Componentes Intrinsecas | componentes intrínsecas]],
> el germen del [[Operador Derivada en Base Movil | operador en base móvil]].

> [!referencia]
> Taylor, §1.7. Base móvil general: [[Operador Derivada en Base Movil]]. Otras coordenadas:
> [[Coordenadas Cilindricas]] y [[Componentes Intrinsecas]]. Sección: [[Cinematica/index]],
> [[1 Particula/index]].
