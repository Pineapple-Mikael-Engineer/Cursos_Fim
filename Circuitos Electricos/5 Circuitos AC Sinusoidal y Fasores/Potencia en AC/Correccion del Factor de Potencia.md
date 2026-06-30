---
title: Correccion del Factor de Potencia
tags:
  - circuitos-electricos
  - teoria
  - potencia
  - factor-potencia
draft: false
aliases:
  - correccion del factor de potencia
  - compensacion de reactiva
  - power factor correction
---

# Corrección del Factor de Potencia

> [!definicion]
> **Corregir el factor de potencia** es subir un FP bajo (típico de una carga **inductiva**) conectando un **condensador en paralelo** con la carga. El condensador aporta localmente la potencia reactiva $Q_C$ que la carga demanda, de modo que la **reactiva neta** que se toma de la red baja —y con ella la aparente $S$ y la corriente $I$— **sin cambiar la potencia activa** $P$ ni el consumo útil. Es la solución práctica y rentable a un $\cos\varphi$ pobre.

> [!info]
> La solución práctica a un [[Factor de Potencia| factor de potencia]] bajo, dentro de la [[Potencia en AC/index| potencia en CA]] ([[5 Circuitos AC Sinusoidal y Fasores/index| capítulo 5]]). Se apoya en la [[Potencia en Regimen Sinusoidal| potencia compleja]] (triángulo de potencias) y en el [[Capacitor| condensador]] como fuente de reactiva negativa. Fraile Mora, cap. 2, §2.12.

---

## Ejemplo

> [!ejemplo]
> **Corregir una carga inductiva de $0{,}6$ a $0{,}9$.**
>
> Una carga consume $P=1200\ \text{W}$ con $\cos\varphi=0{,}6$ inductivo, alimentada a $V=100\ \text{V}$ y $f=50\ \text{Hz}$. Se quiere corregir el factor de potencia a $\cos\varphi'=0{,}9$. Hallar el condensador necesario.
>
> ![[correccion_fp.svg|480]]
>
> *El condensador aporta $Q_C$, reduciendo la reactiva de $Q=1600$ a $Q'=580\ \text{VAr}$ (y la aparente de $2000$ a $1333\ \text{VA}$). La activa $P=1200\ \text{W}$ no cambia.*
>
> **Paso 1 — Reactiva inicial.** Con $\cos\varphi=0{,}6$ es $\varphi=53{,}1^\circ$, así que
> $$Q=P\tan\varphi=1200\tan(53{,}1^\circ)=1600\ \text{VAr}.$$
>
> **Paso 2 — Reactiva final (objetivo).** Con $\cos\varphi'=0{,}9$ es $\varphi'=\arccos0{,}9=25{,}8^\circ$, luego
> $$Q'=P\tan\varphi'=1200\tan(25{,}8^\circ)\approx580\ \text{VAr}.$$
>
> **Paso 3 — Reactiva que debe aportar el condensador.** Es justo la diferencia:
> $$Q_C=Q-Q'=1600-580=1020\ \text{VAr}.$$
>
> **Paso 4 — Capacidad.** Como $Q_C=\dfrac{V^2}{X_C}=V^2\omega C$, despejamos
> $$C=\frac{Q_C}{\omega V^2}=\frac{1020}{2\pi\cdot 50\cdot 100^2}\approx 325\ \mu\text{F}.$$
>
> > [!solucion]
> > Con $C\approx 325\ \mu\text{F}$ en paralelo, el factor de potencia sube de $0{,}6$ a $0{,}9$. La aparente baja de $S=2000$ a $S'=P/\cos\varphi'=1200/0{,}9\approx 1333\ \text{VA}$, y la corriente de línea cae de $I=20\ \text{A}$ a $I'=S'/V=1333/100\approx 13{,}3\ \text{A}$ —un tercio menos— para entregar la **misma** potencia útil $P=1200\ \text{W}$.

---

## En qué consiste

> [!teoria] Por qué un condensador
> Un condensador entrega potencia reactiva **negativa** ($Q_C<0$) que **cancela** parte de la reactiva **positiva** (inductiva) que demanda la carga. Al conectarlo en **paralelo**, la tensión sobre la carga no cambia, de modo que la carga sigue recibiendo exactamente su $P$ y su $Q$ de siempre; lo que ocurre es que ahora el condensador **suministra localmente** una parte $Q_C$ de esa reactiva, y la red solo tiene que aportar el resto $Q'=Q-Q_C$. La potencia activa $P$ queda **intacta** porque un condensador ideal no disipa energía: solo intercambia reactiva. El resultado neto es un triángulo de potencias más "tumbado" (menor $\varphi$), con la misma base $P$ y menor hipotenusa $S$.

> [!proposicion] Reactiva del condensador
> Para un condensador a tensión $V$ y frecuencia angular $\omega=2\pi f$:
> $$X_C=\frac{1}{\omega C},\qquad Q_C=\frac{V^2}{X_C}=\omega C\,V^2,$$
> tomada como reactiva que **resta** de la inductiva. Combinando con el objetivo de FP se llega a la fórmula de diseño directa
> $$C=\frac{P\,(\tan\varphi-\tan\varphi')}{\omega V^2}.$$

> [!algoritmo] Dimensionar el condensador
> 1. Hallar la reactiva inicial: $Q=P\tan\varphi$, con $\varphi=\arccos(\cos\varphi)$.
> 2. Fijar el FP objetivo $\cos\varphi'$ y su reactiva: $Q'=P\tan\varphi'$.
> 3. Reactiva que aporta el condensador: $Q_C=Q-Q'=P(\tan\varphi-\tan\varphi')$.
> 4. Capacidad en paralelo: $C=\dfrac{Q_C}{\omega V^2}$, con $\omega=2\pi f$.

> [!warning]
> El condensador va en **paralelo** con la carga (a la misma tensión), **no** en serie. No conviene **sobrecorregir**: pasarse de $\cos\varphi=1$ hacia un FP **capacitivo** vuelve a aumentar $Q$ (ahora negativa) y la compañía también lo penaliza. Recuerda que corregir reduce $Q$, $S$ e $I$ pero **no** cambia $P$ ni el consumo útil: no es un "ahorro de energía" en la carga, sino de corriente y pérdidas en la red.

## Resumen

> [!resumen]
> | Concepto | Expresión |
> |:---|:---|
> | Reactiva inicial | $Q=P\tan\varphi$ |
> | Reactiva final (objetivo) | $Q'=P\tan\varphi'$ |
> | Reactiva del condensador | $Q_C=P(\tan\varphi-\tan\varphi')$ |
> | Capacidad (en paralelo) | $C=Q_C/(\omega V^2)$, $\;\omega=2\pi f$ |

> [!corolario]
> Corregir el FP es un cálculo de tres pasos: medir la reactiva que sobra, decidir cuánta dejar y poner el condensador que aporte la diferencia. A coste bajo se reduce la corriente de línea y las pérdidas $RI^2$, manteniendo intacta la potencia útil $P$.

> [!referencia]
> Fraile Mora, cap. 2, §2.12. Problema que resuelve: [[Factor de Potencia]]. Marco: [[Potencia en Regimen Sinusoidal]] y [[Potencia en AC/index]]. Elemento usado: [[Capacitor]].
