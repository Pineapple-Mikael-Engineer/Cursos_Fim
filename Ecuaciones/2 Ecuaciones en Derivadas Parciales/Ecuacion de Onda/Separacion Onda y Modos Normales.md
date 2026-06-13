---
title: Separación de Variables y Modos Normales de la Onda
tags:
  - ecuaciones
  - edp
  - teoria
  - onda
  - modos-normales
draft: false
aliases:
  - modos normales
  - separación de variables onda
  - armónicos de una cuerda
  - normal modes
  - standing waves
---

# Separación de Variables y Modos Normales de la Onda

> [!definicion]
> Para la cuerda vibrante $u_{tt}=c^2u_{xx}$ en $[0,L]$ con **extremos fijos** $u(0,t)=u(L,t)=0$ y
> datos iniciales $u(x,0)=f(x)$ (posición) y $u_t(x,0)=g(x)$ (velocidad), la **separación de
> variables** $u=X(x)\,T(t)$ produce autofunciones espaciales $\operatorname{sen}\frac{n\pi x}{L}$ y
> factores temporales **oscilantes** $\cos\omega_n t$, $\operatorname{sen}\omega_n t$. Cada una de
> esas piezas es un **modo normal** o armónico de la cuerda.

> [!info]
> Es el primero de los dos métodos de resolución de la
> [[Ecuacion de Onda/index| ecuación de onda]], complementario de la
> [[Solucion de dAlembert| solución de d'Alembert]]. Reutiliza la maquinaria de
> [[Separacion de Variables y Fourier/index| separación de variables y Fourier]]; la diferencia con
> el [[Ecuacion del Calor/index| calor]] está en el factor temporal, que aquí **oscila** en lugar de
> **decaer**. Parte de la cuerda deducida en [[Derivacion de Onda| la derivación de Newton]].

---

## Ejemplo

> [!ejemplo] Pulsar una cuerda y escuchar sus armónicos
> Resolvamos la cuerda de longitud $L$ con extremos fijos. Buscamos soluciones producto
> $u=X(x)T(t)$. Sustituyendo en $u_{tt}=c^2u_{xx}$ y dividiendo entre $c^2XT$:
> $$\frac{T''}{c^2T}=\frac{X''}{X}=-\lambda \quad(\text{constante, porque cada lado depende de una sola variable}).$$
>
> **Parte espacial.** $X''+\lambda X=0$ con $X(0)=X(L)=0$. Esto solo tiene soluciones no nulas para
> $\lambda_n=\big(\tfrac{n\pi}{L}\big)^2$, con autofunciones
> $$X_n(x)=\operatorname{sen}\frac{n\pi x}{L},\qquad n=1,2,3,\dots$$
>
> **Parte temporal.** Con ese $\lambda_n$, $T''+c^2\lambda_n T=0$ es un **oscilador armónico** de
> frecuencia $\omega_n=c\sqrt{\lambda_n}=\dfrac{n\pi c}{L}$, así que
> $T_n(t)=a_n\cos\omega_n t+b_n\operatorname{sen}\omega_n t$.
>
> **Superposición.** La solución general es la suma de todos los modos:
> $$\boxed{\,u(x,t)=\sum_{n=1}^{\infty}\operatorname{sen}\frac{n\pi x}{L}\Big[a_n\cos\omega_n t+b_n\operatorname{sen}\omega_n t\Big],\qquad \omega_n=\frac{n\pi c}{L}.}$$
>
> **Coeficientes a partir de los datos.** En $t=0$:
> - de la **posición inicial** $u(x,0)=f$ sale $\displaystyle a_n=\frac{2}{L}\int_0^L f(x)\operatorname{sen}\frac{n\pi x}{L}\,dx$ (coeficiente de Fourier en senos de $f$);
> - derivando en $t$ y poniendo $t=0$, de la **velocidad inicial** $u_t(x,0)=g$ sale
> $\displaystyle b_n=\frac{2}{n\pi c}\int_0^L g(x)\operatorname{sen}\frac{n\pi x}{L}\,dx$
> (porque $\partial_t$ baja un factor $\omega_n=\tfrac{n\pi c}{L}$).
>
> Si pulsamos la cuerda y la soltamos desde el reposo ($g=0$), todos los $b_n=0$ y la cuerda vibra
> con la mezcla de armónicos que dicta la forma inicial $f$.

## En qué consiste

> [!teoria] Modos normales, armónicos y timbre
> Cada término de la suma es un **modo normal**: una vibración en la que **toda** la cuerda oscila
> con la **misma** frecuencia $\omega_n$, sin que cambie la forma espacial $\operatorname{sen}\frac{n\pi x}{L}$
> —solo su amplitud sube y baja. Como $\omega_n=n\,\omega_1$, todas las frecuencias son **múltiplos
> enteros** de la fundamental $\omega_1=\pi c/L$: son los **armónicos**. Esta progresión entera es lo
> que hace que la cuerda produzca una nota musical bien definida y no un ruido.
>
> Lo que distingue a un violín de una flauta tocando la *misma* nota es **cómo se reparten las
> amplitudes** $a_n,b_n$ entre los armónicos: esa receta es el **timbre**. La fundamental fija la
> altura (qué nota), pero el peso relativo de los armónicos superiores fija el color del sonido. Por
> eso pulsar la cuerda en el centro (que excita los modos impares y silencia los pares, ya que estos
> tienen un nodo en $x=L/2$) suena más "redondo" que pulsarla cerca del puente, que aviva los
> armónicos agudos.

> [!algoritmo] Resolver una cuerda fija por modos normales
> 1. **Separa** $u=X(x)T(t)$ y obtén las dos EDO con constante $-\lambda$.
> 2. **Resuelve el problema espacial** $X''+\lambda X=0$ con las condiciones de frontera; lee los
>    autovalores $\lambda_n=(n\pi/L)^2$ y autofunciones $\operatorname{sen}\frac{n\pi x}{L}$.
> 3. **Resuelve el temporal**: oscilador de frecuencia $\omega_n=c\sqrt{\lambda_n}=n\pi c/L$.
> 4. **Superpón**: $u=\sum_n \operatorname{sen}\frac{n\pi x}{L}\,[a_n\cos\omega_n t+b_n\operatorname{sen}\omega_n t]$.
> 5. **Ajusta** $a_n$ con $f$ y $b_n$ con $g$ vía coeficientes de Fourier en senos.

> [!proposicion] Oscilar frente a decaer: onda contra calor
> El mismo esquema de separación aplicado al [[Ecuacion del Calor/index| calor]] $u_t=c^2u_{xx}$ da
> autofunciones espaciales **idénticas** $\operatorname{sen}\frac{n\pi x}{L}$, pero el factor temporal
> sale de $T'=-c^2\lambda_n T$, es decir $e^{-c^2\lambda_n t}$: un **decaimiento**. En la onda, en
> cambio, $T''=-c^2\lambda_n T$ da $\cos\omega_n t$ y $\operatorname{sen}\omega_n t$: una
> **oscilación que no decae**. Físicamente, la onda **conserva** la energía (ver
> [[Energia de la Onda]]) mientras que el calor la disipa. La diferencia entera entre las dos EDP
> está en ese único signo de la derivada temporal: primer orden (decae) frente a segundo orden
> (oscila).

## Resumen

> [!resumen]
> | Pieza | En la onda |
> |---|---|
> | Autofunción espacial | $\operatorname{sen}\frac{n\pi x}{L}$ |
> | Frecuencia del modo | $\omega_n=\dfrac{n\pi c}{L}=n\,\omega_1$ |
> | Factor temporal | $a_n\cos\omega_n t+b_n\operatorname{sen}\omega_n t$ (oscila) |
> | $a_n$ (de $f$) | $\dfrac{2}{L}\int_0^L f\operatorname{sen}\frac{n\pi x}{L}\,dx$ |
> | $b_n$ (de $g$) | $\dfrac{2}{n\pi c}\int_0^L g\operatorname{sen}\frac{n\pi x}{L}\,dx$ |

> [!corolario]
> La cuerda fija es una **superposición de armónicos** cuyas frecuencias son múltiplos enteros de la
> fundamental. La posición inicial reparte los $a_n$ y la velocidad inicial los $b_n$; juntos fijan el
> **timbre**. A diferencia del calor, los modos **oscilan indefinidamente** porque la energía se
> conserva.

> [!referencia]
> - De dónde sale la ecuación: [[Derivacion de Onda]].
> - Por qué los modos no decaen: [[Energia de la Onda]].
> - El panorama de la sección: [[Ecuacion de Onda/index]].
