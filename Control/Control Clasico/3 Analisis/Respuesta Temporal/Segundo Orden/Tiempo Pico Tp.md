---
title: Tiempo de Pico (Tp)
order: 3
tags:
  - control-clasico
  - analisis
  - respuesta-temporal
  - segundo-orden
draft: false
aliases:
  - tiempo pico
  - Tp
  - peak time
---

# Tiempo de Pico ($T_p$)

> [!definicion]
> Instante en que la respuesta a escalón alcanza su **primer máximo** (el sobrepico). Depende solo de la frecuencia amortiguada:
> $$T_p = \frac{\pi}{\omega_d} = \frac{\pi}{\omega_n\sqrt{1-\zeta^2}}\quad[\text{s}],\qquad \omega_d=\omega_n\sqrt{1-\zeta^2}.$$
> $T_p$ en segundos, $\omega_n$ en rad/s, $\zeta$ adimensional.

> [!info]
> Métrica de [[Segundo Orden/index | segundo orden]] derivada de la [[Formula General | respuesta $y(t)$]]; es el instante donde se mide el [[Sobrepico Mp | sobrepico $M_p$]]. Junto con $M_p$ (que fija $\zeta$) permite despejar $\omega_n$. Para el régimen permanente ver [[Tiempo Establecimiento Ts | $T_s$]].

---

## Ejemplo

> [!ejemplo] Cálculo de $T_p$
> **Problema.** Un sistema tiene $\zeta=0.5$ y $\omega_n=10$ rad/s. Calcular $T_p$.
>
> **Paso 1 — Frecuencia amortiguada:**
> $$\omega_d=\omega_n\sqrt{1-\zeta^2}=10\sqrt{1-0.25}=10\sqrt{0.75}=10(0.866)=8.66\ \text{rad/s}.$$
>
> **Paso 2 — Tiempo de pico:**
> $$T_p=\frac{\pi}{\omega_d}=\frac{3.1416}{8.66}\approx0.363\ \text{s}.$$
>
> **Paso 3 — Interpretación.** El primer máximo (sobrepico de $16.3\%$) ocurre a los $0.363$ s. Si se duplicara $\omega_n$ a $20$ rad/s con el mismo $\zeta$, $\omega_d=17.3$ y $T_p$ caería a $0.181$ s (respuesta doblemente rápida).

> [!ejemplo] Tiempo de pico
> ![[resp_tiempo_pico_tp.svg|560]]
>
> $t_p$ es el instante del primer máximo de la respuesta subamortiguada: $t_p=\pi/\omega_d$.

---

## Demostración

> [!teorema] Fórmula de $T_p$
> $$T_p = \frac{\pi}{\omega_n\sqrt{1-\zeta^2}}.$$

> [!demostracion]
> **Paso 1 — Respuesta a escalón.** Para $G(s)=\frac{\omega_n^2}{s^2+2\zeta\omega_n s+\omega_n^2}$:
> $$y(t) = 1 - \frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}} \sin(\omega_d t + \theta),\qquad \theta=\arccos\zeta.$$
>
> **Paso 2 — Derivar.** Tras simplificar con la identidad $A\sin\phi+B\cos\phi=R\sin(\phi+\psi)$ (con $R=\omega_n$):
> $$\dot{y}(t) = \frac{\omega_n\,e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}} \sin(\omega_d t).$$
>
> **Paso 3 — Condición de extremo:** $\dot y=0\Rightarrow\sin(\omega_d t)=0\Rightarrow\omega_d t=k\pi$, $k=0,1,2,\dots$
>
> **Paso 4 — Identificar el primer máximo:**
> - $k=0\Rightarrow t=0$ (mínimo, $y(0)=0$).
> - $k=1\Rightarrow t=\pi/\omega_d$ (**primer máximo**).
> - $k=2\Rightarrow t=2\pi/\omega_d$ (primer mínimo posterior al pico).
>
> Por tanto:
> $$T_p=\frac{\pi}{\omega_d}=\frac{\pi}{\omega_n\sqrt{1-\zeta^2}}.$$

---

## En qué consiste

> [!info] Dependencia con $\zeta$ y $\omega_n$
> | Parámetro | Efecto sobre $T_p$ |
> |---|---|
> | Mayor $\omega_n$ (fijo $\zeta$) | $T_p$ **disminuye** (más rápido) |
> | Mayor $\zeta$ (fijo $\omega_n$) | $T_p$ **aumenta** (pico más tardío) |
> | $\zeta\to0$ | $T_p\to\pi/\omega_n$ (oscilación pura) |
> | $\zeta\to1$ | $T_p\to\infty$ (crítico, sin pico) |

> [!info] $T_p$ normalizado ($\omega_n=1$ rad/s)
> | $\zeta$ | $\omega_d$ | $T_p$ [s] |
> |---|---|---|
> | 0.1 | 0.995 | 3.16 |
> | 0.3 | 0.954 | 3.29 |
> | 0.5 | 0.866 | 3.63 |
> | 0.7 | 0.714 | 4.40 |
> | 0.9 | 0.436 | 7.21 |
>
> Para amortiguamientos altos $T_p$ crece notablemente.

> [!info] Conexiones con $M_p$ y $T_s$
> - $M_p=e^{-\zeta\omega_n T_p}$ (alternativa para calcular $M_p$ desde $T_p$).
> - $T_s\approx\dfrac{4}{\zeta\omega_n}=\dfrac{4T_p}{\pi}\cdot\dfrac{\sqrt{1-\zeta^2}}{\zeta}$.
>
> Ver [[Sobrepico Mp | sobrepico]] y [[Tiempo Establecimiento Ts | tiempo de establecimiento]].

> [!regla] Uso en diseño
> Especificar $T_p\le T_{p,\text{máx}}$ impone una cota sobre $\omega_n$:
> $$\frac{\pi}{\omega_n\sqrt{1-\zeta^2}}\le T_{p,\text{máx}}\;\Rightarrow\;\omega_n\ge\frac{\pi}{T_{p,\text{máx}}\sqrt{1-\zeta^2}}.$$
> Junto con $M_p$ (que fija $\zeta$) determina $\omega_n$ mínimo. Ver [[Lugar Raices/index | lugar de las raíces]].

---

## Limitaciones

> [!warning]
> 1. **Solo aplica** a sistemas subamortiguados ($0<\zeta<1$).
> 2. Para $\zeta\ge1$ no hay sobrepico → $T_p$ no está definido.
> 3. Los **ceros** pueden desplazar el pico.
> 4. Asume **realimentación unitaria** y 2.º orden sin ceros.
> 5. En orden superior con polos dominantes, $T_p$ puede diferir ligeramente.

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Definición | instante del primer máximo |
> | Fórmula | $T_p=\pi/\omega_d=\pi/(\omega_n\sqrt{1-\zeta^2})$ |
> | Depende de | $\omega_d$ (es decir $\zeta$ y $\omega_n$) |
> | Diseño | $\omega_n\ge\pi/(T_{p,\text{máx}}\sqrt{1-\zeta^2})$ |

> [!corolario]
> El tiempo de pico es simplemente medio periodo de la oscilación amortiguada ($T_p=\pi/\omega_d$): cuanto mayor sea $\omega_d$, antes llega el sobrepico. Fijado $\zeta$ por $M_p$, $T_p$ se traduce directamente en un requisito sobre $\omega_n$.

> [!referencia]
> - Respuesta de la que deriva: [[Formula General]].
> - Valor en el pico: [[Sobrepico Mp]].
> - Otras métricas: [[Tiempo Establecimiento Ts]] · [[Tiempo Subida Tr]].
> - Panorama: [[Segundo Orden/index]].
