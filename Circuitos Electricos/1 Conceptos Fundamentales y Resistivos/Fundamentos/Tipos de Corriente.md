---
title: Tipos de Corriente
tags:
  - circuitos-electricos
  - teoria
  - resistivos
  - formas-de-onda
draft: false
aliases:
  - tipos de corriente
  - corriente continua y alterna
  - formas de onda
  - DC and AC
---

# Tipos de Corriente: CC y CA

> [!definicion]
> Según cómo varíe en el tiempo, la corriente (o la tensión) se clasifica en:
> - **Corriente continua (CC):** su valor se mantiene **constante**, $i(t)=I$. No cambia de sentido.
> - **Corriente alterna (CA):** varía periódicamente, típicamente **senoidal**,
>   $$i(t)=I_m\operatorname{sen}(\omega t),$$
>   con amplitud $I_m$ y pulsación $\omega=2\pi f$. Cambia de sentido cada medio período.

---

> [!info]
> Quinta nota de [[Fundamentos/index| Fundamentos]] del
> [[1 Conceptos Fundamentales y Resistivos/index| capítulo 1]]. Apoyada en las
> [[Variables del Circuito| variables del circuito]]. El estudio cuantitativo de las ondas
> (valor medio, valor eficaz, fase) corresponde al
> [[4 Ondas Periodicas Sinusoidales/index| capítulo 4]].

---

## Ejemplo

> [!ejemplo] Distinguir CC de CA; período y frecuencia
> Se observan dos señales:
> - **Señal A:** $i_A(t)=5\ \text{A}$, recta horizontal. Es **CC**: valor constante, no depende de
>   $t$ ni cambia de signo.
> - **Señal B:** $i_B(t)=10\operatorname{sen}(100\pi\,t)\ \text{A}$, una senoide que oscila entre
>   $+10\ \text{A}$ y $-10\ \text{A}$. Es **CA** senoidal de amplitud $I_m=10\ \text{A}$.
>
> Para la señal B, la pulsación es $\omega=100\pi\ \text{rad/s}$. La **frecuencia** y el **período**:
> $$f=\frac{\omega}{2\pi}=\frac{100\pi}{2\pi}=50\ \text{Hz},
> \qquad T=\frac{1}{f}=\frac{1}{50}=0{,}02\ \text{s}=20\ \text{ms}.$$
>
> > [!solucion]
> > A es **CC** ($5\ \text{A}$ constante); B es **CA** senoidal de $I_m=10\ \text{A}$, $f=50\ \text{Hz}$
> > y $T=20\ \text{ms}$ (la frecuencia de la red eléctrica europea).

---

## En qué consiste

> [!teoria] CC frente a CA
> En **corriente continua** la magnitud no cambia con el tiempo: la entrega una pila, una batería o
> una fuente de CC, y la corriente circula siempre en el mismo sentido. En **corriente alterna** la
> magnitud varía periódicamente y, en el caso senoidal, invierte su sentido cada semiperíodo. La CA
> senoidal domina en generación y transporte de energía porque se transforma de tensión con facilidad
> y se genera de forma natural en los alternadores. Su descripción usa la **amplitud** $I_m$ (valor
> de pico), la **pulsación** $\omega$ y, si está desfasada, una **fase** $\varphi$:
> $i(t)=I_m\operatorname{sen}(\omega t+\varphi)$.

> [!info] Clasificación de formas de onda
> Una señal $i(t)$ se clasifica primero por su repetición y luego por su forma:
>
> | Criterio | Tipos |
> |:---|:---|
> | Repetición | **periódica** ($i(t+T)=i(t)$) / **no periódica** |
> | Sentido | unidireccional (CC) / bidireccional (CA) |
> | Forma de onda | senoidal, cuadrada, triangular, diente de sierra, escalón, pulso |
>
> La **senoidal** es la forma de onda de referencia del análisis en régimen permanente. El
> **escalón** y el **pulso** modelan conmutaciones (encendido/apagado) y son la entrada típica del
> estudio de transitorios.

> [!proposicion] Período y frecuencia
> Para toda señal periódica, el **período** $T$ es la mínima duración tras la cual se repite, y la
> **frecuencia** $f$ es el número de ciclos por segundo, recíproco del período:
> $$f=\frac{1}{T}\quad[\text{Hz}=\text{s}^{-1}],\qquad \omega=2\pi f\quad[\text{rad/s}].$$
> Así, $50\ \text{Hz}$ equivalen a $T=20\ \text{ms}$ y $\omega=100\pi\ \text{rad/s}$.

> [!warning] El valor medio y el eficaz se ven después
> Una señal de CA senoidal tiene **valor medio nulo** en un período (sube tanto como baja), por lo que
> describirla solo por su amplitud no basta para comparar potencias con la CC. El **valor eficaz**
> (RMS), $I_{\text{rms}}=I_m/\sqrt2$, es el que permite esa comparación. Ambos conceptos se estudian
> en el [[4 Ondas Periodicas Sinusoidales/index| capítulo 4]]; aquí basta saber que existen.

---

## Resumen

> [!resumen] CC, CA y formas de onda
> | Concepto | Descripción | Expresión |
> |:---|:---|:---|
> | CC | valor constante | $i(t)=I$ |
> | CA senoidal | oscila periódicamente | $i(t)=I_m\operatorname{sen}(\omega t+\varphi)$ |
> | Período | duración de un ciclo | $T$ (s) |
> | Frecuencia | ciclos por segundo | $f=1/T$ (Hz) |
> | Pulsación | frecuencia angular | $\omega=2\pi f$ (rad/s) |
> | Otras ondas | cuadrada, triangular, escalón, pulso | — |

> [!corolario]
> La distinción CC/CA organiza todo el curso: las técnicas resistivas y de CC se ven primero; la CA
> senoidal exige amplitud, frecuencia y fase, y se trata con fasores más adelante.

> [!referencia]
> Fraile Mora, cap. 1, §1.6 (clasificación de señales). Continúa en
> [[4 Ondas Periodicas Sinusoidales/index| Ondas periódicas sinusoidales]]. Relacionada:
> [[Variables del Circuito]].
