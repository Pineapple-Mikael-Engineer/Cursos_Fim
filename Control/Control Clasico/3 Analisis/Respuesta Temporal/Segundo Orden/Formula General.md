---
title: Fórmula General de la Respuesta de Segundo Orden
order: 1
tags:
  - control-clasico
  - analisis
  - respuesta-temporal
draft: false
aliases:
  - fórmula general segundo orden
  - respuesta al escalón segundo orden
  - derivación y(t)
---

# Fórmula General de la Respuesta de Segundo Orden

> [!definicion]
> Respuesta a escalón unitario de $G(s)=\dfrac{\omega_n^2}{s^2+2\zeta\omega_n s+\omega_n^2}$ para $0<\zeta<1$:
> $$y(t) = 1 - \frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}}\,\sin(\omega_d t + \theta),\qquad \theta=\arccos\zeta=\arctan\frac{\sqrt{1-\zeta^2}}{\zeta},$$
> con $\omega_d=\omega_n\sqrt{1-\zeta^2}$. Es la suma del valor final ($1$) más una senoide de frecuencia $\omega_d$ encerrada en la envolvente exponencial $\pm e^{-\zeta\omega_n t}/\sqrt{1-\zeta^2}$.

> [!info]
> Nota núcleo de la carpeta [[Segundo Orden/index | segundo orden]]: de esta única $y(t)$ se derivan todas las métricas. El [[Sobrepico Mp | sobrepico]] es el máximo de $y$, el [[Tiempo Pico Tp | tiempo de pico]] el instante donde $\dot y=0$, el [[Tiempo Establecimiento Ts | establecimiento]] viene de la envolvente y el [[Tiempo Subida Tr | tiempo de subida]] del cruce $10\%\to90\%$.

---

## Ejemplo

> [!ejemplo] Evaluar $y(t)$ en instantes concretos
> **Problema.** Para $\zeta=0.5$ y $\omega_n=10$ rad/s, calcular $y(t)$ en $t=0$, en el pico y en $t=0.5$ s.
>
> **Paso 1 — Parámetros derivados:**
> $$\omega_d=\omega_n\sqrt{1-\zeta^2}=10\sqrt{0.75}=8.66\ \text{rad/s},\qquad \theta=\arccos0.5=1.047\ \text{rad}\,(60°),$$
> $$\frac{1}{\sqrt{1-\zeta^2}}=\frac{1}{\sqrt{0.75}}=1.155,\qquad \zeta\omega_n=5.$$
>
> **Paso 2 — Fórmula concreta:**
> $$y(t)=1-1.155\,e^{-5t}\sin(8.66\,t+1.047).$$
>
> **Paso 3 — En $t=0$** (verificación de condición inicial):
> $$y(0)=1-1.155\cdot1\cdot\sin(1.047)=1-1.155\cdot0.866=1-1.0=0.\;\checkmark$$
>
> **Paso 4 — En el pico** $t_p=\pi/\omega_d=3.1416/8.66=0.363$ s:
> $$y(t_p)=1-1.155\,e^{-5(0.363)}\sin(8.66\cdot0.363+1.047)=1-1.155\,e^{-1.814}\sin(\pi+1.047).$$
> Como $\sin(\pi+\theta)=-\sin\theta=-0.866$ y $e^{-1.814}=0.163$:
> $$y(t_p)=1-1.155(0.163)(-0.866)=1+0.163=1.163.$$
> El sobrepico es $M_p=y(t_p)-1=0.163\;(16.3\%)$, coincidiendo con $e^{-\pi\zeta/\sqrt{1-\zeta^2}}$.
>
> **Paso 5 — En $t=0.5$ s** (ya pasado el pico):
> $$y(0.5)=1-1.155\,e^{-2.5}\sin(4.33+1.047)=1-1.155(0.0821)\sin(5.377).$$
> $\sin(5.377)=-0.785$, luego $y(0.5)=1-1.155(0.0821)(-0.785)=1+0.0744=1.074$ (segunda cresta, menor que la primera).

---

## Demostración

> [!demostracion] Por transformada inversa de Laplace
> **Paso 1 — Salida en Laplace.** Ante escalón $R(s)=1/s$:
> $$Y(s) = \frac{\omega_n^2}{s(s^2 + 2\zeta\omega_n s + \omega_n^2)}.$$
>
> **Paso 2 — Fracciones parciales** con los polos $s_{1,2}=-\zeta\omega_n\pm j\omega_d$:
> $$Y(s) = \frac{1}{s} - \frac{s + 2\zeta\omega_n}{s^2 + 2\zeta\omega_n s + \omega_n^2}.$$
>
> **Paso 3 — Completar cuadrados** en el denominador ($=(s+\zeta\omega_n)^2+\omega_d^2$) y reescribir el numerador para separar términos coseno y seno:
> $$Y(s) = \frac{1}{s} - \frac{(s+\zeta\omega_n)}{(s+\zeta\omega_n)^2 + \omega_d^2} - \frac{\zeta\omega_n}{(s+\zeta\omega_n)^2 + \omega_d^2}.$$
>
> **Paso 4 — Antitransformar** (pares coseno y seno amortiguados $e^{-at}\cos\omega_d t$ y $e^{-at}\sin\omega_d t$):
> $$y(t) = 1 - e^{-\zeta\omega_n t}\left(\cos\omega_d t + \frac{\zeta}{\sqrt{1-\zeta^2}}\sin\omega_d t\right).$$
>
> **Paso 5 — Combinar en una sola senoide.** Usando $A\cos\phi+B\sin\phi=R\sin(\phi+\theta)$ con $R=1/\sqrt{1-\zeta^2}$ y $\tan\theta=\sqrt{1-\zeta^2}/\zeta$ (es decir $\theta=\arccos\zeta$):
> $$y(t) = 1 - \frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}}\,\sin(\omega_d t + \theta).$$

---

## En qué consiste

> [!teoria] Estructura de la respuesta
> - **Envolvente exponencial:** $1\pm\dfrac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}}$ — decae con constante de tiempo $1/(\zeta\omega_n)$; fija el [[Tiempo Establecimiento Ts | establecimiento]].
> - **Oscilación:** $\sin(\omega_d t+\theta)$ — frecuencia $\omega_d$; fija el [[Tiempo Pico Tp | tiempo de pico]] y el periodo del *ringing*.
> - **Fase $\theta=\arccos\zeta$:** garantiza $y(0)=0$ y $\dot y(0)=0$ (condiciones iniciales en reposo).

> [!ejemplo] Respuesta y su envolvente
> ![[segundo_orden_envolvente.svg|550]]
>
> La oscilación amortiguada (frecuencia $\omega_d$) queda encerrada entre las envolventes exponenciales (decaimiento $\zeta\omega_n$).

> [!info] Otros casos según $\zeta$
> | $\zeta$ | Respuesta |
> |---|---|
> | $\zeta=0$ | $y=1-\cos\omega_n t$ (oscila sin amortiguar) |
> | $0<\zeta<1$ | subamortiguada (fórmula de arriba) |
> | $\zeta=1$ | $y=1-e^{-\omega_n t}(1+\omega_n t)$ (crítica, sin sobrepico) |
> | $\zeta>1$ | sobreamortiguada (dos exponenciales reales) |

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Salida a escalón | $y(t)=1-\frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}}\sin(\omega_d t+\theta)$ |
> | Fase | $\theta=\arccos\zeta$ |
> | Frecuencia amortiguada | $\omega_d=\omega_n\sqrt{1-\zeta^2}$ |
> | Envolvente | $\pm e^{-\zeta\omega_n t}/\sqrt{1-\zeta^2}$ |
> | Valor final | $y(\infty)=1$ |

> [!corolario]
> Una sola expresión $y(t)$ concentra toda la información de la respuesta subamortiguada: producto de una exponencial decreciente (amortiguamiento $\zeta\omega_n$) y una senoide (frecuencia $\omega_d$). Derivándola, acotándola o evaluándola se obtienen $M_p$, $T_p$, $T_s$ y $T_r$.

> [!referencia]
> - Panorama y parámetros: [[Segundo Orden/index]].
> - Parámetros derivados: [[Sobrepico Mp]] · [[Tiempo Pico Tp]] · [[Tiempo Establecimiento Ts]] · [[Tiempo Subida Tr]].
> - Polos y clasificación: [[Polos Ceros]].
> - Caso de primer orden: [[Primer Orden]].
