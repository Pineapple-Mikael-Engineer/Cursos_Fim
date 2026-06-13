---
title: Sobrepico Máximo (Mp)
tags:
  - control-clasico
  - analisis
  - respuesta-temporal
  - segundo-orden
draft: false
aliases:
  - sobrepico
  - Mp
  - overshoot
  - maximum overshoot
---

# Sobrepico Máximo ($M_p$)

> [!definicion]
> Exceso de la respuesta a escalón sobre su valor final, en el primer pico. En por unidad depende **solo** de $\zeta$:
> $$M_p = e^{-\pi\zeta/\sqrt{1-\zeta^2}},\qquad M_p(\%)=100\,e^{-\pi\zeta/\sqrt{1-\zeta^2}}\quad(0<\zeta<1).$$
> Inversa: $\zeta=\sqrt{\dfrac{(\ln M_p)^2}{\pi^2+(\ln M_p)^2}}$. Definición general: $M_p(\%)=\dfrac{y(t_p)-y(\infty)}{y(\infty)}\times100\%$ (con ganancia unitaria, $y(\infty)=1$).

> [!info]
> Métrica de [[Segundo Orden/index | segundo orden]] derivada de la [[Formula General | respuesta $y(t)$]]. Es la única métrica que depende exclusivamente de $\zeta$, por lo que se usa para **fijar $\zeta$** en diseño. Se alcanza en el [[Tiempo Pico Tp | tiempo de pico $t_p$]]; junto con [[Tiempo Establecimiento Ts | $T_s$]] forma el par básico de especificaciones.

---

## Ejemplo

> [!ejemplo] Calcular $M_p$ y el $\zeta$ inverso
> **Problema.** Un sistema tiene $\zeta=0.5$, $\omega_n=10$ rad/s. (a) Hallar $M_p$. (b) Si la especificación fuera $M_p\le5\%$, ¿qué $\zeta$ mínimo se requiere?
>
> **(a) Sobrepico directo:**
> $$\sqrt{1-\zeta^2}=\sqrt{0.75}=0.866,\qquad \frac{\pi\zeta}{\sqrt{1-\zeta^2}}=\frac{\pi(0.5)}{0.866}=1.814,$$
> $$M_p=e^{-1.814}=0.163\;\Rightarrow\;M_p=16.3\%.$$
> El primer pico vale $y(t_p)=1+0.163=1.163$.
>
> **(b) $\zeta$ inverso desde $M_p=0.05$:**
> $$\ln M_p=\ln0.05=-2.996,\qquad (\ln M_p)^2=8.976,$$
> $$\zeta=\sqrt{\frac{8.976}{\pi^2+8.976}}=\sqrt{\frac{8.976}{18.846}}=\sqrt{0.476}=0.690.$$
> Se necesita $\zeta\ge0.69$. (Con $\zeta=0.5$ actual el sobrepico 16.3% incumple; habría que aumentar el amortiguamiento.)

> [!ejemplo] Sobrepico en la respuesta a escalón
> ![[resp_sobrepico_mp.svg|560]]
>
> El sobrepico $M_p$ es el exceso sobre el valor final, alcanzado en el primer pico $t_p$; en un 2.º orden puro depende solo de $\zeta$.

---

## Demostración

> [!teorema] Fórmula de $M_p$ para sistema subamortiguado
> $$M_p = e^{-\pi\zeta/\sqrt{1-\zeta^2}}.$$

> [!demostracion]
> **Paso 1 — Respuesta a escalón.** Para $G(s)=\frac{\omega_n^2}{s^2+2\zeta\omega_n s+\omega_n^2}$:
> $$y(t) = 1 - \frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}} \sin(\omega_d t + \theta),\qquad \omega_d=\omega_n\sqrt{1-\zeta^2},\;\theta=\arccos\zeta.$$
>
> **Paso 2 — Derivar para hallar el máximo.** El término constante aporta $0$; derivando el resto:
> $$\dot{y}(t) = \frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}} \left[ \zeta\omega_n \sin(\omega_d t + \theta) - \omega_d \cos(\omega_d t + \theta) \right].$$
>
> **Paso 3 — Simplificar con identidad trigonométrica.** Con $A\sin\phi+B\cos\phi=R\sin(\phi+\psi)$, $R=\sqrt{(\zeta\omega_n)^2+\omega_d^2}=\omega_n$, la fase desplaza $\theta$ de vuelta a $0$:
> $$\zeta\omega_n \sin(\omega_d t + \theta) - \omega_d \cos(\omega_d t + \theta) = \omega_n \sin(\omega_d t),$$
> $$\dot{y}(t) = \frac{\omega_n\,e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}} \sin(\omega_d t).$$
>
> **Paso 4 — Condición de máximo.** $\dot y=0\Rightarrow\sin(\omega_d t)=0\Rightarrow\omega_d t=k\pi$. El primer máximo (sobrepico) es $k=1$:
> $$t_p = \frac{\pi}{\omega_d} = \frac{\pi}{\omega_n\sqrt{1-\zeta^2}}\quad(\text{ver }[[Tiempo Pico Tp|tiempo de pico]]).$$
>
> **Paso 5 — Evaluar $y$ en $t_p$.** Como $\sin(\pi+\theta)=-\sin\theta=-\sqrt{1-\zeta^2}$:
> $$y(t_p) = 1 - \frac{e^{-\zeta\omega_n\pi/\omega_d}}{\sqrt{1-\zeta^2}}\,(-\sqrt{1-\zeta^2}) = 1 + e^{-\zeta\omega_n\pi/\omega_d}.$$
>
> **Paso 6 — Simplificar la exponencial:**
> $$\frac{\zeta\omega_n\pi}{\omega_d}=\frac{\zeta\omega_n\pi}{\omega_n\sqrt{1-\zeta^2}}=\frac{\pi\zeta}{\sqrt{1-\zeta^2}}\;\Rightarrow\;y(t_p)=1+e^{-\pi\zeta/\sqrt{1-\zeta^2}}.$$
>
> **Paso 7 — Sobrepico:**
> $$M_p = y(t_p)-y(\infty) = (1+e^{-\pi\zeta/\sqrt{1-\zeta^2}})-1 = e^{-\pi\zeta/\sqrt{1-\zeta^2}}.$$

> [!teorema] Relación inversa $\zeta$ a partir de $M_p$
> $$\zeta = \sqrt{\frac{(\ln M_p)^2}{\pi^2 + (\ln M_p)^2}}\qquad(M_p\text{ en por unidad}).$$

> [!demostracion]
> De $M_p=e^{-\pi\zeta/\sqrt{1-\zeta^2}}$, tomando logaritmo y elevando al cuadrado:
> $$\ln M_p = -\frac{\pi\zeta}{\sqrt{1-\zeta^2}}\;\Rightarrow\;(\ln M_p)^2 = \frac{\pi^2\zeta^2}{1-\zeta^2}.$$
> Despejando $\zeta^2$:
> $$(\ln M_p)^2(1-\zeta^2)=\pi^2\zeta^2\;\Rightarrow\;(\ln M_p)^2=\zeta^2[\pi^2+(\ln M_p)^2]\;\Rightarrow\;\zeta=\sqrt{\frac{(\ln M_p)^2}{\pi^2+(\ln M_p)^2}}.$$

---

## En qué consiste

> [!info] Tabla $\zeta$ – $M_p(\%)$
> | $\zeta$ | $M_p(\%)$ | $\zeta$ | $M_p(\%)$ |
> |---|---|---|---|
> | 0.1 | 72.9% | 0.6 | 9.5% |
> | 0.2 | 52.7% | 0.7 | 4.6% |
> | 0.3 | 37.2% | 0.8 | 1.5% |
> | 0.4 | 25.4% | 0.9 | 0.15% |
> | 0.5 | 16.3% | 1.0 | 0% |

> [!regla] Especificaciones de diseño típicas
> El sobrepico fija directamente el $\zeta$ mínimo:
> - $M_p\le10\%\Rightarrow\zeta\ge0.59$.
> - $M_p\le5\%\Rightarrow\zeta\ge0.69$.
>
> Por eso $M_p$ es la primera especificación que se traduce a $\zeta$; luego [[Tiempo Establecimiento Ts | $T_s$]] o [[Tiempo Pico Tp | $T_p$]] fijan $\omega_n$.

---

## Limitaciones

> [!warning]
> 1. La fórmula **solo aplica** a sistemas subamortiguados ($0<\zeta<1$).
> 2. Para $\zeta\ge1$, $M_p=0$.
> 3. La presencia de **ceros** puede modificar el sobrepico (incluso con $\zeta\ge1$).
> 4. Asume **realimentación unitaria** y sistema de 2.º orden sin ceros.
> 5. En orden superior con polos dominantes, $M_p$ puede diferir ligeramente.

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Definición | $\frac{y(t_p)-y(\infty)}{y(\infty)}\times100\%$ |
> | Fórmula | $M_p=e^{-\pi\zeta/\sqrt{1-\zeta^2}}$ |
> | Inversa | $\zeta=\sqrt{(\ln M_p)^2/[\pi^2+(\ln M_p)^2]}$ |
> | Depende de | solo $\zeta$ (no de $\omega_n$) |
> | $M_p\le10\%$ | $\zeta\ge0.59$ |
> | $M_p\le5\%$ | $\zeta\ge0.69$ |

> [!corolario]
> El sobrepico es función monótona decreciente de $\zeta$ únicamente: medirlo equivale a medir el amortiguamiento, y especificarlo equivale a imponer una cota inferior sobre $\zeta$. Es la puerta de entrada al diseño temporal, que luego se completa con $\omega_n$ vía $T_s$, $T_p$ o $T_r$.

> [!referencia]
> - Respuesta de la que deriva: [[Formula General]].
> - Instante del pico: [[Tiempo Pico Tp]].
> - Otras métricas: [[Tiempo Establecimiento Ts]] · [[Tiempo Subida Tr]].
> - Panorama: [[Segundo Orden/index]].
