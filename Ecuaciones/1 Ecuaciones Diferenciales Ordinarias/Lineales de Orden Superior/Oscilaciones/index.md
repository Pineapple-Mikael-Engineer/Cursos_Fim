---
title: Oscilaciones
order: 9
tags:
  - ecuaciones
  - edo
  - teoria
  - lineales
  - oscilaciones
  - index
draft: false
aliases:
  - oscilaciones
  - oscilador armónico
  - oscillations
  - harmonic oscillator
---

# Oscilaciones: la aplicación física de las EDO lineales de 2º orden

> [!definicion]
> El **oscilador masa–resorte–amortiguador** es el arquetipo de toda EDO lineal de segundo orden con coeficientes constantes:
> $$m\ddot x+c\dot x+kx=F(t),$$
> donde $m$ es la masa, $c$ el coeficiente de amortiguamiento, $k$ la rigidez del resorte y $F(t)$ una fuerza externa. Dividiendo por $m$ aparecen los **dos parámetros que lo gobiernan todo**:
> $$\omega_0=\sqrt{\frac{k}{m}}\quad(\text{frecuencia natural}),\qquad
> \zeta=\frac{c}{2\sqrt{mk}}\quad(\text{razón de amortiguamiento}),$$
> y la ecuación se reescribe en su forma canónica $\ddot x+2\zeta\omega_0\dot x+\omega_0^2 x=F(t)/m$. Casi cualquier sistema físico cerca de un equilibrio estable se comporta así.

> [!info]
> Este es el corazón **físico** del bloque [[Lineales de Orden Superior/index| lineales de orden superior]]. Toda la maquinaria de la [[Coeficientes Constantes Homogenea| ecuación característica]] (raíces reales, complejas, repetidas) y de la [[No Homogenea/index| parte no homogénea]] (particular + homogénea) se traduce aquí en fenómenos que se ven y se miden: vibraciones, amortiguamiento y resonancia.

---

## Ejemplo

> [!ejemplo] Leer la física en las raíces de la característica
> Suelta una masa con $m=1,\ c=2,\ k=5$ y sin fuerza: $\ddot x+2\dot x+5x=0$. Aquí $\omega_0=\sqrt5$ y $\zeta=\dfrac{2}{2\sqrt5}=\dfrac{1}{\sqrt5}\approx0.45<1$. La característica $r^2+2r+5=0$ da
> $$r=-1\pm 2i.$$
> La **parte real** $-1$ es el ritmo de decaimiento (envolvente $e^{-t}$); la **parte imaginaria** $2$ es la frecuencia con que oscila. Resultado: una oscilación que se apaga,
> $$x(t)=e^{-t}\big(\cos 2t+\tfrac12\operatorname{sen}2t\big).$$
> Una sola fórmula —las raíces de un polinomio de grado 2— nos dijo *cómo se mueve* el sistema. Ese es el programa de todo este bloque.

---

## En qué consiste

> [!teoria] De las raíces al comportamiento físico
> Para el oscilador **libre** ($F=0$), la característica de $\ddot x+2\zeta\omega_0\dot x+\omega_0^2x=0$ es $r^2+2\zeta\omega_0 r+\omega_0^2=0$, con raíces
> $$r=-\zeta\omega_0\pm\omega_0\sqrt{\zeta^2-1}.$$
> Estas raíces **dictan la física**, y cada una de sus dos partes tiene un significado:
> - **Parte real** $-\zeta\omega_0$: el factor $e^{-\zeta\omega_0 t}$ que **decae** (disipación de energía por el amortiguamiento). Cuanto mayor $\zeta$, más rápido se pierde energía.
> - **Parte imaginaria** (cuando existe): la frecuencia $\omega_d=\omega_0\sqrt{1-\zeta^2}$ con que el sistema **oscila**.
>
> El signo de $\zeta^2-1$ separa tres regímenes (subamortiguado, crítico, sobreamortiguado): es la traducción directa del discriminante de la [[Coeficientes Constantes Homogenea| ecuación característica]].
>
> Cuando hay **forzamiento** ($F\neq0$), la solución se parte en dos:
> $$x(t)=\underbrace{x_h(t)}_{\text{transitorio}}+\underbrace{x_p(t)}_{\text{estacionario}}.$$
> El **transitorio** $x_h$ es la solución homogénea: contiene el factor $e^{-\zeta\omega_0 t}$ y **desaparece** con el tiempo. El **estado estacionario** $x_p$ es la particular: oscila a la frecuencia de la fuerza y **persiste**. El fenómeno estrella aparece cuando la frecuencia de forzamiento se acerca a $\omega_0$: la amplitud estacionaria se dispara. Eso es la **resonancia**.

> [!info] Mapa de las hijas
> - [[Oscilador Libre y Amortiguado| Oscilador libre y amortiguado]] — desarrolla el caso $F=0$ y sus **tres regímenes** según $\zeta$: subamortiguado (oscila y decae), crítico (retorno más rápido sin oscilar) y sobreamortiguado (decae lento). Es leer el discriminante de la característica como movimiento.
> - [[Oscilaciones Forzadas y Resonancia| Oscilaciones forzadas y resonancia]] — desarrolla el caso $F\neq0$: la separación transitorio/estacionario, la curva de amplitud $A(\omega)$ y el fenómeno de la **resonancia**, incluyendo el crecimiento sin cota cuando no hay amortiguamiento.

> [!proposicion] El mismo modelo, muchos sistemas
> La estructura $m\ddot x+c\dot x+kx=F(t)$ reaparece, término a término, en física e ingeniería:
> | Sistema | "Masa" | "Amortiguador" | "Resorte" | "Fuerza" |
> |:--|:--:|:--:|:--:|:--:|
> | Masa–resorte mecánico | $m$ | $c$ | $k$ | $F(t)$ |
> | Circuito RLC en serie | $L$ | $R$ | $1/C$ | $V(t)$ |
> | Péndulo (pequeñas amplitudes) | $mL^2$ | $b$ | $mgL$ | $\tau(t)$ |
>
> Para el circuito, $L\ddot q+R\dot q+\dfrac{q}{C}=V(t)$ con frecuencia natural $\omega_0=\dfrac{1}{\sqrt{LC}}$. Resolver una vez el oscilador es resolverlos todos.

## Resumen

> [!resumen]
> | Concepto | Significado físico |
> |:--|:--|
> | $\omega_0=\sqrt{k/m}$ | frecuencia natural (a la que querría oscilar libre y sin pérdidas) |
> | $\zeta=\dfrac{c}{2\sqrt{mk}}$ | razón de amortiguamiento (cuánta disipación, sin unidades) |
> | parte real de $r$ | decaimiento/crecimiento de la envolvente |
> | parte imaginaria de $r$ | frecuencia de oscilación $\omega_d$ |
> | $x_h$ (homogénea) | régimen **transitorio**, decae |
> | $x_p$ (particular) | régimen **estacionario**, persiste |
> | resonancia | pico de amplitud cuando $\omega\approx\omega_0$ |

> [!corolario]
> El oscilador convierte el álgebra de la ecuación característica en intuición física: **parte real → disipación**, **parte imaginaria → oscilación**, **forzamiento cerca de $\omega_0$ → resonancia**. Por eso las EDO lineales de segundo orden son tan importantes: no son un ejercicio abstracto, sino el lenguaje con que vibra el mundo.

> [!referencia]
> - El caso libre y sus tres regímenes: [[Oscilador Libre y Amortiguado]].
> - El caso forzado y la resonancia: [[Oscilaciones Forzadas y Resonancia]].
> - La maquinaria algebraica de fondo: [[Coeficientes Constantes Homogenea]].
> - El bloque completo: [[Lineales de Orden Superior/index]].
