---
title: Onda Sinusoidal
tags:
  - circuitos-electricos
  - teoria
  - sinusoidal
draft: false
aliases:
  - onda sinusoidal
  - senoide
  - señal sinusoidal
  - sinusoidal wave
---

# Onda Sinusoidal $\;v=V_m\operatorname{sen}(\omega t+\varphi)$

> [!definicion]
> Una **onda sinusoidal** se describe por completo con tres parámetros:
> $$v(t)=V_m\,\operatorname{sen}(\omega t+\varphi),$$
> la **amplitud** $V_m$ (valor de pico), la **frecuencia angular** $\omega$ (rapidez de la
> oscilación, en rad/s) y la **fase inicial** $\varphi$ (su adelanto/retraso respecto al origen). El
> argumento $\omega t+\varphi$ es la **fase** instantánea.

> [!info]
> La onda central de las [[4 Ondas Periodicas Sinusoidales/index| ondas periódicas sinusoidales]]. Sus
> magnitudes temporales ($T$, $f$, $\omega$) se detallan en [[Caracteristicas de Ondas Periodicas]], y
> de ella salen el [[Valores Caracteristicos]] y el [[Valores Caracteristicos]]. Es lo que el capítulo siguiente
> representará con un [[Fasores| fasor]]. Fraile Mora, cap. 2, §2.2.

---

## Ejemplo

> [!ejemplo]
> **Anatomía de una senoide.**
>
> La tensión $v(t)=10\,\operatorname{sen}(\omega t+\tfrac{\pi}{6})\ \text{V}$ con $f=50\ \text{Hz}$.
> Identificar sus parámetros.
>
> ![[onda_sinusoidal.svg|600]]
>
> *La amplitud $V_m$ es la altura del pico; el período $T=2\pi/\omega$, lo que tarda en repetirse; la
> fase $\varphi$ desplaza la curva respecto al origen.*
>
> **Paso 1 — Amplitud.** $V_m=10\ \text{V}$ (el pico).
>
> **Paso 2 — Frecuencia angular y período.** $\omega=2\pi f=2\pi\cdot50=100\pi\approx314\ \text{rad/s}$;
> el período $T=1/f=20\ \text{ms}$.
>
> **Paso 3 — Fase.** $\varphi=\pi/6=30^\circ$: la onda está **adelantada** $30^\circ$, alcanza su
> primer cruce ascendente antes del origen.
>
> > [!solucion]
> > $V_m=10\ \text{V}$, $\omega\approx314\ \text{rad/s}$, $T=20\ \text{ms}$, $\varphi=30^\circ$. El
> > valor instantáneo en, p. ej., $t=0$ es $v(0)=10\operatorname{sen}(30^\circ)=5\ \text{V}$.

---

## En qué consiste

> [!teoria] Los tres parámetros, uno a uno
> - **Amplitud $V_m$:** el valor de pico, máxima desviación respecto a cero. No confundir con el valor
>   eficaz ($V_m/\sqrt2$) ni con el de pico a pico ($2V_m$).
> - **Frecuencia angular $\omega$:** mide cuántos radianes de fase avanza por segundo,
>   $\omega=2\pi f=2\pi/T$. A más $\omega$, oscilación más rápida.
> - **Fase inicial $\varphi$:** el valor del argumento en $t=0$. Fija el "punto de partida" de la
>   onda; comparar fases de dos senoides de igual $\omega$ da su **desfase**.

> [!teoria] Seno o coseno: la misma onda
> Que se escriba con $\operatorname{sen}$ o con $\cos$ es solo cuestión de fase, pues
> $\cos\theta=\operatorname{sen}(\theta+90^\circ)$. Lo esencial es la terna $(V_m,\omega,\varphi)$.
> Esta descripción compacta es la que, en régimen permanente, permite sustituir la senoide por un
> número complejo —un [[Fasores| fasor]] $\overline{V}=V\angle\varphi$— y convertir
> el cálculo en álgebra.

> [!proposicion] Derivar e integrar conserva la senoide
> La derivada de una senoide es otra senoide de **igual frecuencia**, adelantada $90^\circ$ y escalada
> por $\omega$: $\dfrac{d}{dt}\big[V_m\operatorname{sen}\omega t\big]=\omega V_m\operatorname{sen}(\omega
> t+90^\circ)$. Integrar la retrasa $90^\circ$ y la divide por $\omega$. Por eso un circuito lineal
> excitado con una senoide responde, en permanente, con senoides de la misma frecuencia: el fundamento
> del análisis fasorial.

> [!warning]
> $\omega$ (rad/s) y $f$ (Hz) **no** son lo mismo: $\omega=2\pi f$. Y la fase debe compararse en las
> mismas unidades (todo en grados o todo en radianes), y solo tiene sentido **relativa** entre ondas
> de igual frecuencia.

## Resumen

> [!resumen]
> | Parámetro | Símbolo | Relación |
> |:---|:---|:---|
> | Amplitud (pico) | $V_m$ | pico a pico $=2V_m$ |
> | Frecuencia angular | $\omega$ | $\omega=2\pi f=2\pi/T$ |
> | Fase inicial | $\varphi$ | argumento en $t=0$ |
> | Valor instantáneo | $v(t)$ | $V_m\operatorname{sen}(\omega t+\varphi)$ |

> [!corolario]
> Tres números —$V_m$, $\omega$, $\varphi$— describen por completo una senoide. Esa economía es la que
> hará posible representarla con un solo fasor y resolver los circuitos de CA como si fueran
> resistivos.

> [!referencia]
> Fraile Mora, cap. 2, §2.2. Magnitudes temporales: [[Caracteristicas de Ondas Periodicas]]. Valores
> asociados: [[Valores Caracteristicos]], [[Valores Caracteristicos]]. Representación: [[Fasores]].
