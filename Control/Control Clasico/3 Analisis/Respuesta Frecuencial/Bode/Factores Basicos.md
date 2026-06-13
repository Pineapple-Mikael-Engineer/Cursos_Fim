---
title: Factores Básicos de Bode
tags:
  - control-clasico
  - analisis
  - respuesta-frecuencial
  - bode
draft: false
aliases:
  - factores básicos
  - aportes de Bode
  - factores de Bode
---

# Factores Básicos de Bode

> [!definicion]
> Toda $G(s)$ se factoriza en términos elementales (forma de Bode, con constantes de tiempo): ganancia $K$, integradores/derivadores $s^{\pm N}$, polos y ceros simples $1+s/\omega_0$ y pares de segundo orden. El [[index | diagrama de Bode]] se construye **sumando** la magnitud (dB) y la fase de cada factor:
> $$G(s)=K\,\frac{\prod(1+s/z_i)}{s^N\prod(1+s/p_j)}\cdots$$

> [!info]
> Es el ladrillo de la subsección [[index | Bode]] en [[Respuesta Frecuencial/index | Respuesta Frecuencial]]. Estos aportes se suman en [[Construccion Asintotica]] y se afinan en [[Correcciones]]. El pico del par de 2.º orden enlaza con [[Segundo Orden/index]].

---

## Ejemplo

> [!ejemplo]
> **Evaluar factor por factor $G(s)=\dfrac{20}{s(1+s/10)}$ en $\omega=5\ \text{rad/s}$.** Sumar los aportes de cada factor en dB y en grados.
>
> ![[bode_factores_basicos.svg|600]]
>
> Tres factores: ganancia $K=20$, integrador $1/(j\omega)$ y polo simple $1/(1+j\omega/10)$.
>
> | Factor | Magnitud en $\omega=5$ | Fase en $\omega=5$ |
> |---|---|---|
> | $K=20$ | $20\log20=+26.0$ dB | $0^\circ$ |
> | $1/(j\omega)$ | $-20\log5=-14.0$ dB | $-90^\circ$ |
> | $1/(1+j5/10)$ | $-20\log\sqrt{1+0.25}=-0.97$ dB | $-\arctan0.5=-26.6^\circ$ |
>
> **Magnitud total** (suma de dB):
> $$|G(j5)|_{\text{dB}}=26.0-14.0-0.97\approx +11.0\text{ dB}\;\;\Rightarrow\;\;|G(j5)|\approx3.55.$$
>
> **Fase total** (suma de grados):
> $$\angle G(j5)=0-90^\circ-26.6^\circ=-116.6^\circ.$$
>
> **Comprobación directa:** $G(j5)=\dfrac{20}{j5\,(1+j0.5)}=\dfrac{20}{j5-2.5}=\dfrac{20}{-2.5+j5}$, de módulo $20/\sqrt{2.5^2+5^2}=20/5.59=3.58$ y fase $-(180^\circ-\arctan\frac{5}{2.5})=-116.6^\circ$. Coincide: **sumar factores equivale a multiplicar**.

---

## En qué consiste

> [!info] Aporte de cada factor a magnitud y fase
> | Factor | Magnitud (dB) | Pendiente | Fase |
> |---|---|---|---|
> | Ganancia $K$ | $20\log K$ (constante) | $0$ | $0^\circ$ ($K>0$) |
> | Cero en origen $j\omega$ | $+20\log\omega$ | $+20$ dB/dec | $+90^\circ$ |
> | Polo en origen $1/j\omega$ (integrador) | $-20\log\omega$ | $-20$ dB/dec | $-90^\circ$ |
> | Cero simple $1+j\omega/\omega_0$ | $0\to+20$ dB/dec en $\omega_0$ | $+20$ dB/dec | $0^\circ\to+90^\circ$ |
> | Polo simple $1/(1+j\omega/\omega_0)$ | $0\to-20$ dB/dec en $\omega_0$ | $-20$ dB/dec | $0^\circ\to-90^\circ$ |
> | Par 2.º orden $1/(1+2\zeta\frac{j\omega}{\omega_n}+(\frac{j\omega}{\omega_n})^2)$ | $0\to-40$ dB/dec en $\omega_n$ | $-40$ dB/dec | $0^\circ\to-180^\circ$ |
> | Retardo $e^{-j\omega T}$ | $0$ (constante) | $0$ | $-\omega T$ rad (crece sin límite) |

> [!teorema] Polo simple $\dfrac{1}{1+j\omega/\omega_0}$
> - **Magnitud:** $0$ dB para $\omega\ll\omega_0$; $-20$ dB/dec para $\omega\gg\omega_0$. En $\omega=\omega_0$ vale exactamente $-3$ dB.
> - **Fase:** $0^\circ\to-90^\circ$, pasando por $-45^\circ$ en $\omega_0$. La transición ocupa $\pm$ una década alrededor de $\omega_0$.

> [!info] Cero simple
> Idéntico al polo pero con **signos opuestos**: $+20$ dB/dec y $+90^\circ$, con $+45^\circ$ y $+3$ dB en $\omega_0$. Un cero "levanta" la magnitud y "adelanta" la fase — base del [[Lugar Raices/index | compensador lead]].

> [!teorema] Par cuadrático (segundo orden)
> $$\frac{1}{1+2\zeta\frac{j\omega}{\omega_n}+\left(\frac{j\omega}{\omega_n}\right)^2}$$
> - **Magnitud:** $0$ dB en baja frecuencia; $-40$ dB/dec sobre $\omega_n$.
> - **Pico resonante** si $\zeta<0.707$: máximo $M_r=\dfrac{1}{2\zeta\sqrt{1-\zeta^2}}$ en $\omega_r=\omega_n\sqrt{1-2\zeta^2}$.
> - **Fase:** $0^\circ\to-180^\circ$, con $-90^\circ$ exactos en $\omega_n$.
>
> El valor del pico depende de $\zeta$ (ver [[Segundo Orden/index | segundo orden]] y [[Correcciones]]).

> [!ejemplo] Efecto de $\zeta$ en el par de 2.º orden
> ![[bode_segundo_orden_zeta.svg|600]]
>
> Para $\omega_n=1$: con $\zeta=0.1$ el pico es $M_r=1/(2\cdot0.1\sqrt{0.99})\approx5.03\;(+14\text{ dB})$; con $\zeta=0.5$ baja a $M_r\approx1.15\;(+1.2\text{ dB})$. Menor $\zeta\Rightarrow$ pico más pronunciado cerca de $\omega_n$.

---

## Resumen

> [!resumen]
> | Factor | Pendiente | Fase asintótica | En $\omega_0$/$\omega_n$ |
> |---|---|---|---|
> | $K>0$ | $0$ | $0^\circ$ | $20\log K$ |
> | Integrador $1/j\omega$ | $-20$ dB/dec | $-90^\circ$ | — |
> | Polo simple | $-20$ dB/dec | $-90^\circ$ | $-3$ dB, $-45^\circ$ |
> | Cero simple | $+20$ dB/dec | $+90^\circ$ | $+3$ dB, $+45^\circ$ |
> | Par 2.º orden | $-40$ dB/dec | $-180^\circ$ | pico $M_r$, $-90^\circ$ |

> [!corolario]
> Cada factor aporta una pendiente fija ($\pm20$ o $\pm40$ dB/dec) y un salto de fase ($\pm90^\circ$ o $\pm180^\circ$) en torno a su frecuencia de esquina. Conocidos estos siete ladrillos, cualquier Bode se levanta sumándolos en dB y en grados, como muestra [[Construccion Asintotica]].

> [!referencia]
> - Suma de estos factores: [[Construccion Asintotica]].
> - Ajustes finos: [[Correcciones]].
> - Pico resonante y $\zeta$: [[Segundo Orden/index]] · [[Sobrepico Mp]].
> - El cero como compensador: [[Lugar Raices/index]].
