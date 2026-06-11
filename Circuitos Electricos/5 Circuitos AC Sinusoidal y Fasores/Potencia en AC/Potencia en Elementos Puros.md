---
title: Potencia en Elementos Puros
tags:
  - circuitos-electricos
  - teoria
  - potencia
draft: false
aliases:
  - potencia en elementos puros
  - power in pure elements
  - potencia en R L C
---

# Potencia en Elementos Puros $\;(R,\ L,\ C)$

> [!definicion]
> La potencia en cada elemento pasivo ideal revela su **papel energético**. La **resistencia**
> absorbe potencia siempre positiva ($p\geq0$): **disipa** energía, con valor medio
> $$P=V_{ef}I_{ef}>0.$$
> El **inductor** y el **condensador** tienen potencia de **valor medio cero**: no disipan, solo
> **almacenan y devuelven** energía al circuito (potencia **reactiva** $Q$). El desfase $\varphi$ entre
> tensión y corriente decide cuál de los dos comportamientos domina.

> [!info]
> Caso particular de la [[Potencia Instantanea| potencia instantánea]] en
> [[Potencia en AC/index| Potencia en AC]] ([[5 Circuitos AC Sinusoidal y Fasores/index| capítulo 5]]);
> explica el **origen físico** de la potencia activa (en $R$) y de la reactiva (en $L$ y $C$). Conecta
> directamente con el desfase introducido por [[Fasores Electricos]] y se formaliza con las expresiones
> de [[Potencia en Sinuidal y Fasorial]]. Fraile Mora, cap. 2, §2.9.

---

## Ejemplo

> [!ejemplo]
> **Potencia instantánea en $R$, $L$ y $C$.**
>
> Sea una tensión $v=V_m\operatorname{sen}\omega t$ aplicada por separado a cada elemento puro. Hallar la
> potencia instantánea $p=vi$ y su valor medio en cada caso.
>
> ![[potencia_elementos.svg|640]]
>
> *Resistencia: $p\geq0$ siempre (área neta positiva: disipa). Inductor y condensador: $p$ oscila
> simétrica, de media nula (almacena y devuelve).*
>
> **Resistencia ($\varphi=0$).** La corriente está en fase, $i=I_m\operatorname{sen}\omega t$, así que
> $$p=V_m I_m\operatorname{sen}^2\omega t\geq0,$$
> nunca cambia de signo. Usando $\operatorname{sen}^2\omega t=\tfrac12(1-\cos2\omega t)$, el valor medio es
> $$P=\frac{V_m I_m}{2}=V_{ef}I_{ef}.$$
>
> **Inductor ($\varphi=90^\circ$).** La corriente atrasa $90^\circ$,
> $i=I_m\operatorname{sen}(\omega t-90^\circ)=-I_m\cos\omega t$, de modo que
> $$p=-V_m I_m\operatorname{sen}\omega t\cos\omega t=-\frac{V_m I_m}{2}\operatorname{sen}2\omega t,$$
> una sinusoide de frecuencia doble y **valor medio $0$**.
>
> **Condensador ($\varphi=-90^\circ$).** La corriente adelanta $90^\circ$,
> $i=I_m\cos\omega t$, y entonces
> $$p=V_m I_m\operatorname{sen}\omega t\cos\omega t=\frac{V_m I_m}{2}\operatorname{sen}2\omega t,$$
> igual que el inductor pero con **signo opuesto**: también de valor medio $0$.
>
> > [!solucion]
> > Solo la **resistencia disipa** (su potencia media $P=V_{ef}I_{ef}$ es la potencia **activa**). El
> > inductor y el condensador tienen potencia media nula: su contribución es puramente **reactiva**, y sus
> > potencias instantáneas van en oposición de fase (uno absorbe energía mientras el otro la devuelve).

---

## En qué consiste

> [!teoria] El desfase decide
> El comportamiento energético de cada elemento lo fija el **desfase** $\varphi$ entre $v$ e $i$:
> - **Con $\varphi=0$ (resistencia):** tensión y corriente "tiran a la vez" (mismo signo en todo
>   instante), por lo que $p\geq0$ y la energía fluye **siempre** hacia el elemento, donde se convierte en
>   calor. Es potencia **activa**.
> - **Con $\varphi=\pm90^\circ$ (inductor, condensador):** durante medio ciclo la energía entra al campo
>   (magnético en $L$, eléctrico en $C$) y durante el otro medio sale de vuelta hacia la fuente. La media
>   es **cero**: no hay disipación, solo un trasiego de energía.
>
> Esa energía que va y viene es la **potencia reactiva** $Q$. El inductor **absorbe** reactiva ($Q>0$) y
> el condensador la **entrega** ($Q<0$): por eso, conectados juntos, se compensan mutuamente —fundamento de
> la corrección del factor de potencia.

> [!proposicion] Potencia en cada elemento ideal
> Con $V_{ef}$, $I_{ef}$ los valores eficaces y $X_L=\omega L$, $X_C=1/(\omega C)$ las reactancias:
> $$
> \begin{aligned}
> \text{Resistencia:}\quad & P=V_{ef}I_{ef}=I_{ef}^2 R=\frac{V_{ef}^2}{R}>0, \\[2pt]
> \text{Inductor:}\quad & Q_L=I_{ef}^2 X_L>0, \\[2pt]
> \text{Condensador:}\quad & Q_C=-I_{ef}^2\lvert X_C\rvert<0.
> \end{aligned}
> $$
> El **signo opuesto** de $Q_L$ y $Q_C$ es la base de la corrección del factor de potencia: un
> condensador en paralelo aporta $Q_C<0$ que cancela el $Q_L>0$ de las cargas inductivas.

> [!warning]
> "Valor medio cero" **no** significa que no circule corriente por $L$ o $C$: sí circula corriente y sí
> existe potencia instantánea $p(t)\neq0$ en cada instante (que en cables reales con resistencia parásita
> **sí calienta**). Lo que es nulo es la **potencia activa** (la media), y solo en el elemento **ideal**.
> La corriente reactiva es real y tiene un coste: más corriente transportada para igual potencia útil.

## Resumen

> [!resumen]
> | Elemento | Desfase $\varphi$ | Potencia que aporta | Expresión |
> |:---|:---:|:---|:---|
> | Resistencia $R$ | $0$ | Activa (disipa) | $P=V_{ef}I_{ef}=I_{ef}^2 R=V_{ef}^2/R$ |
> | Inductor $L$ | $+90^\circ$ | Reactiva (absorbe) | $Q_L=I_{ef}^2 X_L>0$ |
> | Condensador $C$ | $-90^\circ$ | Reactiva (entrega) | $Q_C=-I_{ef}^2\lvert X_C\rvert<0$ |

> [!corolario]
> La potencia separa los elementos en dos familias: la resistencia **consume** energía (activa,
> $p\geq0$), mientras inductor y condensador solo la **prestan y la devuelven** (reactiva, media nula). El
> signo contrario de $Q_L$ y $Q_C$ permite que se compensen, idea que se explota al corregir el factor de
> potencia y se sintetiza en la [[Potencia Compleja]].

> [!referencia]
> Fraile Mora, cap. 2, §2.9. Origen general: [[Potencia Instantanea]] y
> [[Potencia en Sinuidal y Fasorial]]. Desfase: [[Fasores Electricos]]. Síntesis $P$–$Q$–$S$:
> [[Potencia Compleja]].
