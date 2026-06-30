---
title: Vibración Forzada
order: 2
tags:
  - dinamica
  - teoria
  - vibraciones
draft: false
aliases:
  - vibración forzada
  - resonancia
  - factor de amplificación
  - respuesta en frecuencia
---

# Vibración Forzada $\;m\ddot x+c\dot x+kx=F_0\cos\omega t$

> [!definicion]
> La **vibración forzada** es la respuesta a una excitación armónica $F_0\cos\omega t$. Tras el transitorio, el sistema oscila en **régimen estacionario** a la **frecuencia de la excitación** $\omega$, con amplitud
> $$X=\frac{F_0/k}{\sqrt{(1-r^2)^2+(2\zeta r)^2}},\qquad r=\frac{\omega}{\omega_n},$$
> y un desfase $\varphi$ respecto a la fuerza. Cuando $r\to1$ (excitación cerca de la frecuencia natural) y el amortiguamiento es bajo, la amplitud se dispara: **resonancia**.

> [!info]
> Segunda nota de las [[5 Vibraciones/index | vibraciones]] ([[Dinamica/index | Dinámica]]). Añade la excitación a la [[Vibracion Libre | vibración libre]]; la solución completa es transitorio (libre, decae) + estacionario (forzado, permanece). Referencia: Taylor §5.5-5.6.

---

## Ejemplo

> [!ejemplo]
> **Amplificación en resonancia.**
>
> Un sistema con amortiguamiento $\zeta=0{,}1$ se excita en resonancia ($r\approx1$). ¿Cuánto amplifica respecto a la deformación estática $F_0/k$?
>
> ![[resonancia.svg|620]]
>
> *Factor de amplificación $M=X/(F_0/k)$ frente a $r=\omega/\omega_n$. El pico en $r\approx1$ es la resonancia, tanto más alto cuanto **menor** el amortiguamiento.*
>
> En $r=1$, $M=\dfrac{1}{\sqrt{(1-1)^2+(2\zeta)^2}}=\dfrac{1}{2\zeta}=\dfrac{1}{0{,}2}=5$.
>
> > [!solucion]
> > La amplitud en resonancia es $\approx5$ veces la estática: $X\approx5\,F_0/k$. Con $\zeta=0{,}05$ serían $10$ veces; sin amortiguamiento, **infinita**. Por eso la resonancia es a la vez útil (instrumentos) y peligrosa (puentes, máquinas).

---

## En qué consiste

> [!teorema] Respuesta estacionaria
> La solución particular es $x_p=X\cos(\omega t-\varphi)$ con
> $$X=\frac{F_0/k}{\sqrt{(1-r^2)^2+(2\zeta r)^2}},\qquad \tan\varphi=\frac{2\zeta r}{1-r^2},$$
> y el **factor de amplificación** $M=\dfrac{X}{F_0/k}=\dfrac{1}{\sqrt{(1-r^2)^2+(2\zeta r)^2}}$.

> [!demostracion]
> Conviene la forma compleja: con $F=F_0 e^{i\omega t}$ y solución $x=X_c e^{i\omega t}$, sustituyendo en $m\ddot x+c\dot x+kx=F$:
> $$(-m\omega^2+i c\omega+k)\,X_c=F_0\ \Rightarrow\ X_c=\frac{F_0}{(k-m\omega^2)+i c\omega}.$$
> El **módulo** es $X=|X_c|=\dfrac{F_0}{\sqrt{(k-m\omega^2)^2+(c\omega)^2}}$. Dividiendo numerador y denominador por $k$ y usando $r=\omega/\omega_n$ ($\omega_n^2=k/m$) y $2\zeta r=c\omega/k$:
> $$X=\frac{F_0/k}{\sqrt{(1-r^2)^2+(2\zeta r)^2}}.$$
> El **argumento** de $X_c$ da el retraso de fase, $\tan\varphi=\dfrac{c\omega}{k-m\omega^2}=\dfrac{2\zeta r}{1-r^2}$. $\blacksquare$

> [!teorema] Resonancia
> El máximo de $M$ está en
> $$r_{\text{res}}=\sqrt{1-2\zeta^2}\quad(\zeta<\tfrac{1}{\sqrt2}),\qquad M_{\max}=\frac{1}{2\zeta\sqrt{1-\zeta^2}}.$$
> Para amortiguamiento pequeño, $r_{\text{res}}\approx1$ y $M_{\max}\approx\dfrac{1}{2\zeta}$.

> [!demostracion]
> $M$ es máximo cuando el radicando $g(r)=(1-r^2)^2+(2\zeta r)^2$ es **mínimo**. Derivando, $g'(r)=2(1-r^2)(-2r)+8\zeta^2 r=4r\big[-(1-r^2)+2\zeta^2\big]=0$. Descartando $r=0$, $r^2=1-2\zeta^2$. Sustituyendo en $M=1/\sqrt{g}$ sale $M_{\max}=\dfrac{1}{2\zeta\sqrt{1-\zeta^2}}$. Para $\zeta\to0$, $r_{\text{res}}\to1$ y $M_{\max}\to1/(2\zeta)\to\infty$. $\blacksquare$

> [!proposicion] Tres zonas de frecuencia
> - **$r\ll1$** (excitación lenta): $M\approx1$, la masa sigue a la fuerza (régimen **rígido**).
> - **$r\approx1$**: resonancia, $M$ máximo, fase $\varphi\approx90^\circ$.
> - **$r\gg1$** (excitación rápida): $M\approx1/r^2\to0$, la masa apenas se mueve (aislamiento), fase $\varphi\to180^\circ$ (en oposición).

> [!warning]
> En resonancia la fase es $90^\circ$ (la fuerza va en cuadratura con el desplazamiento, entregando máxima energía). Sin amortiguamiento la amplitud crece **sin cota** (linealmente en el tiempo si $\omega=\omega_n$): de ahí los desastres por resonancia. La fórmula de $X$ es **estacionaria**; el transitorio libre se superpone al principio.

## Resumen

> [!resumen]
> | Magnitud | Expresión |
> |:---|:---|
> | Amplitud | $X=\dfrac{F_0/k}{\sqrt{(1-r^2)^2+(2\zeta r)^2}}$ |
> | Amplificación | $M=1/\sqrt{(1-r^2)^2+(2\zeta r)^2}$ |
> | Fase | $\tan\varphi=2\zeta r/(1-r^2)$ |
> | Resonancia | $r_{\text{res}}=\sqrt{1-2\zeta^2}$, $M_{\max}\approx1/(2\zeta)$ |

> [!corolario]
> La respuesta forzada depende de la **relación de frecuencias** $r$: lejos de $\omega_n$ es modesta, pero cerca se amplifica drásticamente, limitada solo por el amortiguamiento. Comprender la resonancia —buscarla o evitarla— es el objetivo práctico de toda la teoría de vibraciones.

> [!referencia]
> Taylor §5.5-5.6. Sistema libre: [[Vibracion Libre]]. Análogo eléctrico: resonancia en el circuito RLC.
