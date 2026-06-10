---
title: Valor Medio
tags:
  - circuitos-electricos
  - teoria
  - sinusoidal
  - valor-medio
draft: false
aliases:
  - valor medio
  - valor promedio
  - componente continua
  - componente DC
  - mean value
  - average value
---

# Valor Medio $\;V_{med}=\dfrac{1}{T}\displaystyle\int_0^T v(t)\,dt$

> [!definicion]
> El **valor medio** de una onda periódica es su **promedio a lo largo de un período**:
> $$V_{med}=\frac{1}{T}\int_0^{T} v(t)\,dt.$$
> Equivale a la **componente continua (DC)** de la onda: el "nivel" constante alrededor del que oscila.
> Para una **senoide completa** vale **cero** (las áreas positiva y negativa se cancelan); para una
> **rectificada de onda completa** vale $\dfrac{2V_m}{\pi}\approx0{,}637\,V_m$, y para una **rectificada
> de media onda**, $\dfrac{V_m}{\pi}$.

> [!info]
> Una de las magnitudes con que se caracterizan las [[4 Ondas Periodicas Sinusoidales/index| ondas periódicas]]. Se compara con el [[Valor Eficaz RMS]] mediante el [[Factor de Forma y Cresta| factor de forma]]. Se define sobre la [[Onda Sinusoidal]] y su versión rectificada. Fraile Mora, cap. 2, §2.2.

---

## Ejemplo

> [!ejemplo]
> **Media de la senoide completa y de la rectificada.**
>
> Mostrar que una senoide completa tiene valor medio **cero** y que su **rectificada de onda completa**
> promedia $2V_m/\pi$.
>
> ![[valor_medio.svg|560]]
>
> *Arriba: la senoide completa promedia cero (las áreas $+$ y $-$ se cancelan). Abajo: la rectificada de
> onda completa promedia $2V_m/\pi$.*
>
> **Senoide completa.** En un período el área positiva del primer semiciclo iguala en magnitud al área
> negativa del segundo, de modo que su suma —y por tanto la integral— es nula:
> $$V_{med}=\frac{1}{2\pi}\int_0^{2\pi} V_m\operatorname{sen}\theta\,d\theta=0.$$
>
> **Rectificada de onda completa.** Al rectificar, el semiciclo negativo se vuelve positivo, y basta
> promediar sobre medio período (de $0$ a $\pi$):
> $$V_{med}=\frac{1}{\pi}\int_0^{\pi} V_m\operatorname{sen}\theta\,d\theta=\frac{V_m}{\pi}\bigl[-\cos\theta\bigr]_0^{\pi}=\frac{V_m}{\pi}(1+1)=\frac{2V_m}{\pi}.$$
>
> > [!solucion]
> > Senoide completa: $V_{med}=0$. Rectificada de onda completa: $V_{med}=\dfrac{2V_m}{\pi}\approx
> > 0{,}637\,V_m$.

---

## En qué consiste

> [!teoria] La componente DC de la onda
> El valor medio es la **componente continua (DC)** de la onda: el "nivel" constante alrededor del que
> oscila. Si se descompone $v(t)$ en una parte constante más una parte de promedio nulo, esa parte
> constante **es** $V_{med}$. Para ondas **simétricas respecto al eje horizontal** —como la senoide pura,
> en la que cada valor positivo tiene su simétrico negativo— el valor medio es **cero**. Por eso, para
> caracterizar una onda de CA por un valor medio útil, primero se **rectifica**: así el promedio deja de
> cancelarse. Es lo que mide físicamente un **instrumento de bobina móvil**, cuyo par responde al valor
> medio de la corriente que lo atraviesa.

> [!proposicion] Media onda y onda completa
> La **rectificada de media onda** (que anula el semiciclo negativo en vez de invertirlo) promedia sobre
> el período completo solo el semiciclo positivo:
> $$V_{med}^{\,\text{media onda}}=\frac{1}{2\pi}\int_0^{\pi} V_m\operatorname{sen}\theta\,d\theta=\frac{V_m}{\pi}.$$
> Es **la mitad** del de la rectificada de onda completa, $\dfrac{2V_m}{\pi}$, porque esta aprovecha los
> dos semiciclos y aquella solo uno.

> [!warning]
> El valor medio **no** es el valor eficaz: el medio de una senoide completa es $0$, pero su
> [[Valor Eficaz RMS| eficaz]] es $V_m/\sqrt2\neq0$. Además, cuando se habla del "valor medio de una
> corriente alterna" casi siempre se refiere al de la **señal rectificada** ($2V_m/\pi$ o $V_m/\pi$), no
> al de la onda completa, que sería trivialmente cero.

## Resumen

> [!resumen]
> | Onda | Valor medio |
> |:---|:---|
> | Definición | $V_{med}=\dfrac{1}{T}\displaystyle\int_0^T v(t)\,dt$ |
> | Senoide completa | $0$ |
> | Rectificada de onda completa | $\dfrac{2V_m}{\pi}\approx0{,}637\,V_m$ |
> | Rectificada de media onda | $\dfrac{V_m}{\pi}$ |

> [!corolario]
> El valor medio mide la **componente DC** de la onda. Como en una senoide pura es nulo, en la práctica el
> "valor medio de una CA" se calcula sobre su rectificada; junto con el [[Valor Eficaz RMS]] permite
> definir el [[Factor de Forma y Cresta| factor de forma]] $k_f=V_{ef}/V_{med}$, que para la senoide
> rectificada vale $\approx1{,}11$.

> [!referencia]
> Fraile Mora, cap. 2, §2.2. Se compara con [[Valor Eficaz RMS]] mediante el
> [[Factor de Forma y Cresta]]. Se construye sobre la [[Onda Sinusoidal]] y se ubica entre las
> [[4 Ondas Periodicas Sinusoidales/index| ondas periódicas sinusoidales]].
