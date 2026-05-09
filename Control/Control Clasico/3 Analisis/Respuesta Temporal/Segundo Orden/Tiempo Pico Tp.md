---
title: Tiempo de Pico (Tp)
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

# Definición

> [!definicion] Tiempo de pico
> Es el tiempo que tarda la respuesta a escalón en alcanzar el **primer máximo** (el sobrepico).
> 
> $$T_p = \frac{\pi}{\omega_d} = \frac{\pi}{\omega_n \sqrt{1-\zeta^2}}$$
> 
> donde $\omega_d = \omega_n \sqrt{1-\zeta^2}$ es la **frecuencia amortiguada**.

> [!info] Unidades
> - $T_p$ se mide en **segundos** [s]
> - $\omega_n$ en radianes por segundo [rad/s]
> - $\zeta$ es adimensional

# Demostración

> [!teorema] Fórmula de $T_p$
> $$T_p = \frac{\pi}{\omega_n \sqrt{1-\zeta^2}}$$

> [!demostracion] Paso 1: Respuesta a escalón
> Para $G(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$ con entrada escalón unitario:
> $$y(t) = 1 - \frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}} \sin(\omega_d t + \theta)$$
> 
> donde $\omega_d = \omega_n \sqrt{1-\zeta^2}$, $\theta = \arccos(\zeta)$.
> 
> **Paso 2:** Derivar para encontrar extremos
> 
> $$\dot{y}(t) = \frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}} \left[ \zeta\omega_n \sin(\omega_d t + \theta) - \omega_d \cos(\omega_d t + \theta) \right]$$
> 
> Usando identidad trigonométrica, se puede demostrar que:
> $$\dot{y}(t) = \frac{\omega_n e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}} \sin(\omega_d t)$$
> 
> **Paso 3:** Condición de extremo
> 
> $\dot{y}(t) = 0 \implies \sin(\omega_d t) = 0$
> 
> $$\omega_d t = k\pi, \quad k = 0, 1, 2, \dots$$
> 
> **Paso 4:** Identificar el primer máximo
> 
> - $k = 0 \implies t = 0$ (mínimo, $y(0)=0$)
> - $k = 1 \implies t = \pi / \omega_d$ (primer máximo)
> - $k = 2 \implies t = 2\pi / \omega_d$ (primer mínimo, luego del pico)
> 
> Por lo tanto:
> $$T_p = \frac{\pi}{\omega_d} = \frac{\pi}{\omega_n \sqrt{1-\zeta^2}}$$

# Relación con parámetros del sistema

> [!info] Dependencia con $\zeta$ y $\omega_n$
> 
> | Parámetro | Efecto sobre $T_p$ |
> |-----------|-------------------|
> | Mayor $\omega_n$ (fijo $\zeta$) | $T_p$ **disminuye** (respuesta más rápida) |
> | Mayor $\zeta$ (fijo $\omega_n$) | $T_p$ **aumenta** (pico más tardío) |
> | $\zeta \to 0$ | $T_p \to \pi / \omega_n$ (oscilación pura) |
> | $\zeta \to 1$ | $T_p \to \infty$ (críticamente amortiguado, no hay pico) |

# Tabla de valores típicos

> [!info] $T_p$ normalizado ($\omega_n = 1$ rad/s)
> 
> | $\zeta$ | $\omega_d$ | $T_p$ [s] |
> |---------|------------|-----------|
> | 0.1 | 0.995 | 3.16 |
> | 0.2 | 0.980 | 3.21 |
> | 0.3 | 0.954 | 3.29 |
> | 0.4 | 0.917 | 3.43 |
> | 0.5 | 0.866 | 3.63 |
> | 0.6 | 0.800 | 3.93 |
> | 0.7 | 0.714 | 4.40 |
> | 0.8 | 0.600 | 5.24 |
> | 0.9 | 0.436 | 7.21 |
> 
> **Observación:** Para amortiguamientos altos, $T_p$ crece significativamente.

# Relación con $M_p$ y $T_s$

> [!info] Conexiones
> - $M_p = e^{-\zeta\omega_n T_p}$ (alternativa para calcular $M_p$ desde $T_p$)
> - $T_s \approx \frac{4}{\zeta\omega_n} = \frac{4T_p}{\pi} \cdot \sqrt{1-\zeta^2} \cdot \zeta^{-1}$
> 
> Ver [[Sobrepico Mp]] y [[Tiempo Establecimiento Ts]].

# Uso en diseño

> [!info] Especificación típica
> En control, se suele especificar $T_p$ máximo:
> $$T_p \le T_{p,\text{máx}}$$
> 
> Esto impone una condición sobre $\omega_n$ y $\zeta$:
> $$\frac{\pi}{\omega_n \sqrt{1-\zeta^2}} \le T_{p,\text{máx}} \implies \omega_n \ge \frac{\pi}{T_{p,\text{máx}} \sqrt{1-\zeta^2}}$$
> 
> Junto con $M_p$ (que fija $\zeta$), permite calcular $\omega_n$ mínimo requerido.
> 
> Ver [[Lugar Raices/index | lugar de las raíces]] para diseño por ubicación de polos.

# Ejemplo numérico

> [!ejemplo] Cálculo de $T_p$
> 
> **Problema:** Un sistema tiene $\zeta = 0.5$ y $\omega_n = 10$ rad/s. Calcule $T_p$.
> 
> **Solución:**
> $$\omega_d = \omega_n \sqrt{1-\zeta^2} = 10 \sqrt{1 - 0.25} = 10 \sqrt{0.75} = 10 \cdot 0.866 = 8.66 \text{ rad/s}$$
> 
> $$T_p = \frac{\pi}{\omega_d} = \frac{3.1416}{8.66} \approx 0.363 \text{ s}$$
> 
> **Verificación:** El sobrepico ocurre a los 0.363 segundos.

# Limitaciones

> [!warning]
> 1. **Solo aplica** a sistemas subamortiguados ($0 < \zeta < 1$)
> 2. Para $\zeta \ge 1$, no hay sobrepico → $T_p$ no está definido
> 3. La presencia de **ceros** puede desplazar el pico de la respuesta
> 4. La fórmula asume **realimentación unitaria** y **sistema de segundo orden sin ceros**
> 5. En sistemas de orden superior con polos dominantes, $T_p$ puede diferir ligeramente