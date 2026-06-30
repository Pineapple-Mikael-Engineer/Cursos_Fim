---
title: Variables del Circuito
order: 1
tags:
  - circuitos-electricos
  - teoria
  - resistivos
  - variables
draft: false
aliases:
  - variables del circuito
  - corriente y tension
  - circuit variables
---

# Variables del Circuito $i=\dfrac{dq}{dt}$, $v=\dfrac{dw}{dq}$

> [!definicion]
> Un circuito se describe con dos variables eléctricas fundamentales. La **corriente** es el ritmo al que la carga atraviesa una sección,
> $$i=\frac{dq}{dt}\quad[\text{A}],$$
> y la **tensión** (o diferencia de potencial) es la energía que cuesta mover la unidad de carga entre dos puntos,
> $$v=\frac{dw}{dq}\quad[\text{V}].$$
> El sentido convencional de la corriente es el del movimiento de las cargas **positivas**. Toda tensión y toda corriente exigen una **referencia** (polaridad $+,-$ y sentido) para tener signo.

---

> [!info]
> Primera nota de la sección [[Fundamentos/index| Fundamentos]], dentro del [[1 Conceptos Fundamentales y Resistivos/index| capítulo 1]]. Fija el alfabeto que usan todas las notas siguientes: [[Convenio de Signos]] (signo de las variables), [[Potencia y Energia]] (producto $p=vi$) y [[Sistema de Unidades]] (unidades de cada magnitud).

---

## Ejemplo

> [!ejemplo] Corriente a partir de la carga, y carga a partir de la corriente
> **(a)** Por una sección de un conductor la carga transportada sigue la ley $q(t)=2t^2\ \text{C}$ (con $t$ en segundos). Hallar la corriente $i(t)$ y su valor en $t=3\ \text{s}$.
>
> La corriente es la derivada de la carga:
> $$i(t)=\frac{dq}{dt}=\frac{d}{dt}\big(2t^2\big)=4t\quad[\text{A}].$$
> En el instante pedido,
> $$i(3)=4\cdot 3=12\ \text{A}.$$
>
> > [!solucion]
> > $i(t)=4t\ \text{A}$ y $i(3\ \text{s})=12\ \text{A}$.
>
> **(b)** Por un conductor circula una corriente **constante** de $I=5\ \text{A}$ durante $t=2\ \text{min}$. ¿Qué carga total se ha transportado?
>
> Con corriente constante, $q=It$. Pasando el tiempo a segundos, $t=2\cdot 60=120\ \text{s}$:
> $$q=I\,t=5\ \text{A}\cdot 120\ \text{s}=600\ \text{C}.$$
>
> > [!solucion]
> > Se han transportado $q=600\ \text{C}$.

---

## En qué consiste

> [!teoria] Carga, corriente y tensión
> La **carga** $q$ (en culombios, C) es la magnitud eléctrica básica; la del electrón vale $-1{,}602\times 10^{-19}\ \text{C}$. Cuando la carga se mueve por un conductor aparece la **corriente**: el número de culombios que cruzan una sección por segundo. Un amperio es, por tanto, un culombio por segundo, $1\ \text{A}=1\ \text{C/s}$.
>
> Mover la carga a través de un elemento implica intercambiar **energía** $w$ (en julios, J). La **tensión** entre dos puntos $a$ y $b$ mide cuánta energía por culombio se gana o se pierde al ir de $a$ a $b$: $v_{ab}=dw/dq$. Un voltio es un julio por culombio, $1\ \text{V}=1\ \text{J/C}$. Por eso la tensión se asocia a una **polaridad** $+,-$: indica entre qué punto y cuál se mide la diferencia.

> [!info] Sentido y referencia de la corriente
> El **sentido convencional** de la corriente es el del flujo de cargas **positivas**, contrario al movimiento real de los electrones (que son negativos). Esta convención es universal y la seguiremos siempre. Sobre el circuito se dibuja una **flecha de referencia**: si al resolver obtenemos $i>0$, la corriente fluye en el sentido de la flecha; si $i<0$, fluye al revés. La flecha no es una hipótesis sobre "hacia dónde va realmente", sino el eje de signos para la incógnita.

> [!info] Nodo de referencia (tierra)
> Solo tienen sentido las **diferencias** de potencial. Para hablar del potencial de un nodo aislado se elige un **nodo de referencia** o **masa/tierra**, al que se asigna $0\ \text{V}$ (símbolo de tierra $\bot$). El potencial de cualquier otro nodo se mide entonces respecto a esa referencia, y la tensión entre dos nodos es la resta de sus potenciales: $v_{ab}=V_a-V_b$.

> [!warning] Polaridad y signo
> Una misma tensión escrita como $v_{ab}$ o $v_{ba}$ cambia de signo: $v_{ab}=-v_{ba}$. Indicar siempre la polaridad ($+$ en un borne, $-$ en el otro) evita ambigüedades. Lo mismo ocurre con la corriente y su flecha: sin referencia, un número como "$i=-3\ \text{A}$" no significa nada.

---

## Resumen

> [!resumen] Magnitudes y sus relaciones
> | Magnitud | Símbolo | Definición | Unidad SI |
> |:---|:---|:---|:---|
> | Carga | $q$ | magnitud básica | culombio, $\text{C}$ |
> | Corriente | $i$ | $i=\dfrac{dq}{dt}$ | amperio, $\text{A}=\text{C/s}$ |
> | Energía | $w$ | energía intercambiada | julio, $\text{J}$ |
> | Tensión | $v$ | $v=\dfrac{dw}{dq}$ | voltio, $\text{V}=\text{J/C}$ |
> | Potencia | $p$ | $p=vi=\dfrac{dw}{dt}$ | vatio, $\text{W}=\text{J/s}$ |

> [!corolario]
> Con corriente constante la carga es $q=It$; en general $q(t)=q_0+\int i\,dt$. Y como $v$ y $p$ tienen signo, hace falta un **convenio** que diga cuándo el elemento absorbe o entrega: ese es el objeto de la nota siguiente.

> [!referencia]
> Fraile Mora, cap. 1, §1.2–1.3. Continúa en [[Convenio de Signos]] y [[Potencia y Energia]]; unidades y prefijos en [[Sistema de Unidades]].
