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

# Definición

> [!definicion] Sobrepico
> Es la cantidad en que la respuesta a escalón **excede** el valor final, expresada como porcentaje del valor final.
> 
> $$M_p(\%) = \frac{y(t_p) - y(\infty)}{y(\infty)} \times 100\%$$
> 
> Para un sistema con ganancia unitaria ($y(\infty)=1$):
> $$M_p(\%) = [y(t_p) - 1] \times 100\%$$

> [!definicion] Sobrepico en por unidad
> $$M_p = e^{-\pi\zeta/\sqrt{1-\zeta^2}}$$
> 
> donde $0 < \zeta < 1$ (sistemas subamortiguados).

# Demostración

> [!teorema] Fórmula de $M_p$ para sistema subamortiguado
> $$M_p = e^{-\pi\zeta/\sqrt{1-\zeta^2}}$$

> [!demostracion] Paso 1: Respuesta a escalón
> Para $G(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$ con entrada escalón unitario:
> $$y(t) = 1 - \frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}} \sin(\omega_d t + \theta)$$
> 
> donde $\omega_d = \omega_n\sqrt{1-\zeta^2}$, $\theta = \arccos(\zeta)$.
> 
> **Paso 2:** Derivar para encontrar el máximo
> 
> $$\dot{y}(t) = 0 \implies \frac{d}{dt} \left[1 - \frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}} \sin(\omega_d t + \theta)\right] = 0$$
> 
> La derivada del término constante es cero. Derivando el segundo término:
> 
> $$\dot{y}(t) = \frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}} \left[ \zeta\omega_n \sin(\omega_d t + \theta) - \omega_d \cos(\omega_d t + \theta) \right]$$
> 
> **Paso 3:** Simplificar usando identidad trigonométrica
> 
> $$A \sin(\phi) + B \cos(\phi) = R \sin(\phi + \psi)$$
> 
> En este caso:
> $$\zeta\omega_n \sin(\omega_d t + \theta) - \omega_d \cos(\omega_d t + \theta) = \omega_n \sin\left(\omega_d t\right)$$
> 
> (Verificar: $\sqrt{(\zeta\omega_n)^2 + \omega_d^2} = \omega_n$, y la fase corresponde)
> 
> Por lo tanto:
> $$\dot{y}(t) = \frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}} \cdot \omega_n \sin(\omega_d t)$$
> 
> **Paso 4:** Condición de máximo
> 
> $\dot{y}(t) = 0 \implies \sin(\omega_d t) = 0$
> 
> $$\omega_d t = k\pi, \quad k = 1, 2, 3, \dots$$
> 
> El primer máximo (el sobrepico) ocurre en $k=1$:
> $$t_p = \frac{\pi}{\omega_d} = \frac{\pi}{\omega_n\sqrt{1-\zeta^2}}$$
> 
> Ver [[Tiempo Pico Tp]].
> 
> **Paso 5:** Evaluar $y(t)$ en $t_p$
> 
> $\sin(\omega_d t_p + \theta) = \sin(\pi + \theta) = \sin(\pi + \theta) = -\sin(\theta)$
> 
> Como $\sin(\theta) = \sqrt{1-\zeta^2}$:
> $$\sin(\pi + \theta) = -\sqrt{1-\zeta^2}$$
> 
> $$y(t_p) = 1 - \frac{e^{-\zeta\omega_n \cdot \pi/\omega_d}}{\sqrt{1-\zeta^2}} \cdot (-\sqrt{1-\zeta^2}) = 1 + e^{-\zeta\omega_n \pi/\omega_d}$$
> 
> **Paso 6:** Simplificar la exponencial
> 
> $$\frac{\zeta\omega_n \pi}{\omega_d} = \frac{\zeta\omega_n \pi}{\omega_n\sqrt{1-\zeta^2}} = \frac{\pi\zeta}{\sqrt{1-\zeta^2}}$$
> 
> Por lo tanto:
> $$y(t_p) = 1 + e^{-\pi\zeta/\sqrt{1-\zeta^2}}$$
> 
> **Paso 7:** Calcular $M_p$
> 
> $$M_p = y(t_p) - y(\infty) = (1 + e^{-\pi\zeta/\sqrt{1-\zeta^2}}) - 1 = e^{-\pi\zeta/\sqrt{1-\zeta^2}}$$

# Relación inversa: $\zeta$ a partir de $M_p$

> [!teorema] Cálculo de $\zeta$ dado $M_p$
> $$\zeta = \sqrt{\frac{(\ln M_p)^2}{\pi^2 + (\ln M_p)^2}}$$
> 
> donde $M_p$ está en por unidad (ej. $M_p=0.5$ para 50%).

> [!demostracion]
> De $M_p = e^{-\pi\zeta/\sqrt{1-\zeta^2}}$, tomando logaritmo natural:
> 
> $$\ln M_p = -\frac{\pi\zeta}{\sqrt{1-\zeta^2}}$$
> 
> Elevando al cuadrado:
> $$(\ln M_p)^2 = \frac{\pi^2 \zeta^2}{1-\zeta^2}$$
> 
> Despejando $\zeta^2$:
> $$(\ln M_p)^2 (1-\zeta^2) = \pi^2 \zeta^2$$
> $$(\ln M_p)^2 - (\ln M_p)^2 \zeta^2 = \pi^2 \zeta^2$$
> $$(\ln M_p)^2 = \zeta^2[\pi^2 + (\ln M_p)^2]$$
> $$\zeta^2 = \frac{(\ln M_p)^2}{\pi^2 + (\ln M_p)^2}$$
> 
> Tomando raíz positiva (para sistemas estables):
> $$\zeta = \sqrt{\frac{(\ln M_p)^2}{\pi^2 + (\ln M_p)^2}}$$

# Tabla de valores típicos

> [!info] Relación $\zeta$ - $M_p(\%)$
> 
> | $\zeta$ | $M_p(\%)$ | $\zeta$ | $M_p(\%)$ |
> |---------|-----------|---------|-----------|
> | 0.1 | 72.9% | 0.6 | 9.5% |
> | 0.2 | 52.7% | 0.7 | 4.6% |
> | 0.3 | 37.2% | 0.8 | 1.5% |
> | 0.4 | 25.4% | 0.9 | 0.15% |
> | 0.5 | 16.3% | 1.0 | 0% |

# Relación con especificaciones de diseño

> [!info] Especificación típica
> En control, se suele especificar:
> $$M_p \le 10\% \quad \text{o} \quad M_p \le 5\%$$
> 
> Para $M_p \le 10\% \implies \zeta \ge 0.59$
> 
> Para $M_p \le 5\% \implies \zeta \ge 0.69$
> 
> Ver [[Tiempo Establecimiento Ts]] y [[Tiempo Pico Tp]] para especificaciones completas.

# Efecto del sobrepico en diferentes sistemas

> [!ejemplo] Comparación de respuestas
> 
> | $\zeta$ | $M_p$ | Característica |
> |---------|-------|----------------|
> | 0.2 | 52.7% | Muy oscilatorio, gran sobrepico |
> | 0.5 | 16.3% | Oscilaciones moderadas |
> | 0.7 | 4.6% | Sobre paso pequeño, respuesta rápida |
> | 0.9 | 0.15% | Prácticamente sin sobrepico |

# Limitaciones

> [!warning]
> 1. La fórmula **solo aplica** a sistemas subamortiguados ($0 < \zeta < 1$)
> 2. Para $\zeta \ge 1$, $M_p = 0$
> 3. La presencia de **ceros** puede modificar el sobrepico (incluso en sistemas con $\zeta \ge 1$)
> 4. La fórmula asume **realimentación unitaria** y **sistema de segundo orden** sin ceros
> 5. En sistemas de orden superior con polos dominantes, el sobrepico puede diferir ligeramente