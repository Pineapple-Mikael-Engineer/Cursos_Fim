---
title: Coordenadas Cilíndricas
tags:
  - dinamica
  - teoria
  - particula
  - cinematica
draft: false
aliases:
  - coordenadas cilíndricas
  - coordenadas polares
  - cylindrical coordinates
  - polar coordinates
---

# Coordenadas Cilíndricas $(r,\theta,z)$ y la base $(\hat e_r,\hat e_\theta,\hat e_z)$

> [!definicion]
> Las **coordenadas cilíndricas** $(r,\theta,z)$ son las **coordenadas polares** del plano $xy$ más el
> eje $z$, con $r$ = **distancia al eje $z$**, $\theta$ el ángulo azimutal y $z$ la altura. La posición es
> $$\vec r=r\,\hat e_r+z\,\hat e_z,$$
> donde la base móvil $(\hat e_r,\hat e_\theta,\hat e_z)$ cumple
> - $\hat e_r=(\cos\theta,\operatorname{sen}\theta,0)$ apunta **radialmente** hacia afuera del eje,
> - $\hat e_\theta=(-\operatorname{sen}\theta,\cos\theta,0)$ es **azimutal** (sentido de $\theta$ creciente),
> - $\hat e_z=(0,0,1)$ es **constante**.
>
> Mientras $\hat e_z$ no cambia, $\hat e_r$ y $\hat e_\theta$ **giran** con $\theta$. La velocidad y la
> aceleración resultan ser **las polares más una parte axial** trivial:
> $$\vec v=\dot r\,\hat e_r+r\dot\theta\,\hat e_\theta+\dot z\,\hat e_z,\qquad
> \vec a=(\ddot r-r\dot\theta^2)\,\hat e_r+(r\ddot\theta+2\dot r\dot\theta)\,\hat e_\theta+\ddot z\,\hat e_z.$$

> [!info]
> Nota de la [[Cinematica/index | cinemática de la partícula]]. El caso plano $z=0$ son las
> **coordenadas polares**. Que la base gire es una instancia del
> [[Operador Derivada en Base Movil | operador derivada en base móvil]]: las derivadas
> $d\hat e_r/dt$ y $d\hat e_\theta/dt$ son lo único no trivial del cálculo. Referencia: Taylor §1.7.

---

## Ejemplo

> [!ejemplo]
> **Movimiento helicoidal.**
>
> Una partícula sube por una **hélice** de radio $R$: el radio es constante, $r=R$; gira con velocidad
> angular constante, $\theta=\omega t$ (luego $\dot\theta=\omega$, $\ddot\theta=0$); y asciende
> uniformemente, $z=ct$ (luego $\dot z=c$, $\ddot z=0$). Hallar $\vec v$ y $\vec a$.
>
> ![[coordenadas_cilindricas.svg|330]]
>
> *Coordenadas cilíndricas $(r,\theta,z)$: base $(\hat e_r,\hat e_\theta,\hat e_z)$ con $\hat e_z$ fijo y $\hat e_r,\hat e_\theta$ girando con $\theta$.*
>
> **Paso 1 — Derivadas de las coordenadas.** De $r=R$ const: $\dot r=0$, $\ddot r=0$. De $\theta=\omega t$:
> $\dot\theta=\omega$, $\ddot\theta=0$. De $z=ct$: $\dot z=c$, $\ddot z=0$.
>
> **Paso 2 — Velocidad.** Sustituyendo en $\vec v=\dot r\,\hat e_r+r\dot\theta\,\hat e_\theta+\dot z\,\hat e_z$:
> $$\vec v=0\,\hat e_r+R\omega\,\hat e_\theta+c\,\hat e_z=R\omega\,\hat e_\theta+c\,\hat e_z.$$
>
> **Paso 3 — Aceleración.** En $\vec a=(\ddot r-r\dot\theta^2)\,\hat e_r+(r\ddot\theta+2\dot r\dot\theta)\,\hat e_\theta+\ddot z\,\hat e_z$
> sobreviven solo $-r\dot\theta^2=-R\omega^2$ (los demás términos llevan $\ddot r$, $\ddot\theta$, $\dot r$ o $\ddot z$, todos nulos):
> $$\vec a=-R\omega^2\,\hat e_r.$$
>
> > [!solucion]
> > La **rapidez** $v=\lvert\vec v\rvert=\sqrt{R^2\omega^2+c^2}$ es **constante**: la partícula avanza
> > uniformemente por la hélice. Aun así, la aceleración **no es nula**: vale
> > $\vec a=-R\omega^2\,\hat e_r$, puramente **radial hacia el eje** (centrípeta), de módulo
> > $R\omega^2$. No hay componente azimutal (no se acelera el giro) ni axial (la subida es uniforme):
> > toda la aceleración mantiene a la partícula en su circunferencia de radio $R$.

---

## En qué consiste

> [!teorema] Velocidad y aceleración en cilíndricas
> Para $\vec r=r\,\hat e_r+z\,\hat e_z$,
> $$\boxed{\;\vec v=\dot r\,\hat e_r+r\dot\theta\,\hat e_\theta+\dot z\,\hat e_z\;}$$
> $$\boxed{\;\vec a=(\ddot r-r\dot\theta^2)\,\hat e_r+(r\ddot\theta+2\dot r\dot\theta)\,\hat e_\theta+\ddot z\,\hat e_z\;}$$
> Las dos primeras componentes de cada una son las **polares**; la tercera es la parte **axial**,
> idéntica a un movimiento rectilíneo en $z$ porque $\hat e_z$ es fijo.

> [!demostracion]
> **Paso 1 — Derivadas de la base.** De $\hat e_r=(\cos\theta,\operatorname{sen}\theta,0)$ y
> $\hat e_\theta=(-\operatorname{sen}\theta,\cos\theta,0)$, derivando respecto del tiempo con la regla de
> la cadena ($d/dt=\dot\theta\,d/d\theta$):
> $$\frac{d\hat e_r}{dt}=\dot\theta\,(-\operatorname{sen}\theta,\cos\theta,0)=\dot\theta\,\hat e_\theta,
> \qquad
> \frac{d\hat e_\theta}{dt}=\dot\theta\,(-\cos\theta,-\operatorname{sen}\theta,0)=-\dot\theta\,\hat e_r,
> \qquad
> \frac{d\hat e_z}{dt}=\vec 0.$$
>
> **Paso 2 — Velocidad.** Derivamos $\vec r=r\,\hat e_r+z\,\hat e_z$, usando la regla del producto y el
> Paso 1:
> $$\vec v=\dot r\,\hat e_r+r\,\frac{d\hat e_r}{dt}+\dot z\,\hat e_z+z\,\frac{d\hat e_z}{dt}
> =\dot r\,\hat e_r+r\dot\theta\,\hat e_\theta+\dot z\,\hat e_z.$$
>
> **Paso 3 — Aceleración.** Derivamos $\vec v$ término a término y sustituimos de nuevo el Paso 1:
> $$\vec a=\frac{d}{dt}\big(\dot r\,\hat e_r\big)+\frac{d}{dt}\big(r\dot\theta\,\hat e_\theta\big)+\frac{d}{dt}\big(\dot z\,\hat e_z\big).$$
> Desarrollando cada bloque:
> $$\frac{d}{dt}(\dot r\,\hat e_r)=\ddot r\,\hat e_r+\dot r\,\dot\theta\,\hat e_\theta,$$
> $$\frac{d}{dt}(r\dot\theta\,\hat e_\theta)=(\dot r\dot\theta+r\ddot\theta)\,\hat e_\theta+r\dot\theta\,(-\dot\theta\,\hat e_r)=-r\dot\theta^2\,\hat e_r+(\dot r\dot\theta+r\ddot\theta)\,\hat e_\theta,$$
> $$\frac{d}{dt}(\dot z\,\hat e_z)=\ddot z\,\hat e_z.$$
> Agrupando por versor:
> $$\vec a=(\ddot r-r\dot\theta^2)\,\hat e_r+(r\ddot\theta+2\dot r\dot\theta)\,\hat e_\theta+\ddot z\,\hat e_z.$$
> $\blacksquare$

> [!proposicion] Lectura de los términos
> En la componente radial, $-r\dot\theta^2$ es la aceleración **centrípeta**: aparece por girar, apunta
> hacia el eje y es la que mantiene una órbita circular. En la azimutal, $2\dot r\dot\theta$ es el
> término de **Coriolis**: surge al **alejarse del eje** ($\dot r\neq0$) **mientras se gira**
> ($\dot\theta\neq0$). La parte axial $\ddot z\,\hat e_z$ es trivial: como $\hat e_z$ es fijo, $z$ se
> comporta como una coordenada rectilínea independiente.

> [!warning]
> Aquí $r$ es la distancia al **eje $z$**, no al origen (en
> [[Coordenadas Esfericas | esféricas]] la coordenada radial sí mide al origen): no confundir ambas.
> El término de **Coriolis** $2\dot r\dot\theta$ se olvida con frecuencia; recuerda que aparece **solo**
> si $\dot r$ y $\dot\theta$ son **ambos** no nulos (radio variable y giro simultáneos). Y $\hat e_z$ es
> el único versor constante: las derivadas no nulas son las de $\hat e_r$ y $\hat e_\theta$.

## Resumen

> [!resumen]
> | Magnitud | Expresión |
> |:---|:---|
> | Base | $\hat e_r$ (radial), $\hat e_\theta$ (azimutal), $\hat e_z$ (axial, **fijo**) |
> | Derivadas de la base | $\dot{\hat e}_r=\dot\theta\,\hat e_\theta$, $\;\dot{\hat e}_\theta=-\dot\theta\,\hat e_r$, $\;\dot{\hat e}_z=\vec 0$ |
> | Velocidad | $\vec v=\dot r\,\hat e_r+r\dot\theta\,\hat e_\theta+\dot z\,\hat e_z$ |
> | Aceleración | $\vec a=(\ddot r-r\dot\theta^2)\,\hat e_r+(r\ddot\theta+2\dot r\dot\theta)\,\hat e_\theta+\ddot z\,\hat e_z$ |
> | Caso plano $z=0$ | **coordenadas polares** (se suprime $\hat e_z$) |

> [!corolario]
> Las cilíndricas son las **polares con un eje añadido**: toda la riqueza está en el plano $xy$
> (centrípeta $-r\dot\theta^2$ y Coriolis $2\dot r\dot\theta$), mientras la dirección $z$ se desacopla por
> tener versor constante. Son las coordenadas naturales de cualquier problema con **simetría de
> revolución** alrededor de un eje.

> [!referencia]
> Taylor, §1.7. Caso plano y base móvil general: [[Operador Derivada en Base Movil]]. Otras
> descripciones: [[Componentes Intrinsecas]] (triedro de Frenet) y [[Coordenadas Esfericas]]. Marco:
> [[Cinematica/index]] dentro de [[1 Particula/index]].
