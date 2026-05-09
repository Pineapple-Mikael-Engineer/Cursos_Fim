---
title: Tiempo de Establecimiento (Ts)
tags:
  - control-clasico
  - analisis
  - respuesta-temporal
  - segundo-orden
draft: false
aliases:
  - tiempo establecimiento
  - Ts
  - settling time
---

# Tiempo de Establecimiento ($T_s$)

# Definición

> [!definicion] Tiempo de establecimiento
> Es el tiempo que tarda la respuesta a escalón en **entrar y permanecer** dentro de una **banda porcentual** alrededor del valor final.
> 
> Criterios comunes:
> - $T_s(2\%)$: banda $\pm 2\%$ del valor final
> - $T_s(5\%)$: banda $\pm 5\%$ del valor final

> [!definicion] Aproximación estándar (subamortiguado)
> $$T_s(2\%) \approx \frac{4}{\zeta \omega_n}$$
> $$T_s(5\%) \approx \frac{3}{\zeta \omega_n}$$

# Demostración

> [!teorema] Fórmula de $T_s(2\%)$ para sistema subamortiguado
> $$T_s(2\%) \approx \frac{4}{\zeta \omega_n}$$

> [!demostracion] Paso 1: Envolvente de la respuesta
> Para $G(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$ con entrada escalón unitario:
> $$y(t) = 1 - \frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}} \sin(\omega_d t + \theta)$$
> 
> El término oscilatorio está acotado por:
> $$\left| \frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}} \sin(\omega_d t + \theta) \right| \le \frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}}$$
> 
> Por lo tanto:
> $$1 - \frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}} \le y(t) \le 1 + \frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}}$$
> 
> **Paso 2:** Condición de entrada en la banda
> 
> Para que $y(t)$ entre y permanezca dentro de $\pm 2\%$ del valor final, la envolvente debe ser $\le 0.02$:
> $$\frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}} \le 0.02$$
> 
> Para $\zeta$ típicos ($0.3 \le \zeta \le 0.8$), $\sqrt{1-\zeta^2}$ es del orden de $0.6$ a $0.95$. La aproximación común ignora este factor:
> $$e^{-\zeta\omega_n t} \le 0.02$$
> 
> **Paso 3:** Despejar $t$
> 
> $$-\zeta\omega_n t \le \ln(0.02) \approx -3.912$$
> 
> Multiplicando por $-1$ (invierte desigualdad):
> $$\zeta\omega_n t \ge 3.912$$
> 
> $$t \ge \frac{3.912}{\zeta\omega_n} \approx \frac{4}{\zeta\omega_n}$$
> 
> **Paso 4:** Aproximación
> 
> Se redondea $3.912$ a $4$ por simplicidad y para dar un margen de seguridad.
> 
> $$T_s(2\%) \approx \frac{4}{\zeta\omega_n}$$

> [!info] Análogo para $T_s(5\%)$
> $$\frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}} \le 0.05 \implies e^{-\zeta\omega_n t} \le 0.05$$
> 
> $$-\zeta\omega_n t \le \ln(0.05) \approx -2.996 \implies t \ge \frac{2.996}{\zeta\omega_n} \approx \frac{3}{\zeta\omega_n}$$

# Relación con parámetros del sistema

> [!info] Dependencia con $\zeta$ y $\omega_n$
> 
> | Parámetro | Efecto sobre $T_s$ |
> |-----------|-------------------|
> | Mayor $\omega_n$ (fijo $\zeta$) | $T_s$ **disminuye** (sistema más rápido) |
> | Mayor $\zeta$ (fijo $\omega_n$) | $T_s$ **disminuye** (menos oscilaciones) |
> | Producto $\zeta \omega_n$ | Constante de amortiguamiento (inverso de $T_s$) |

# Limitaciones de la aproximación

> [!warning] La fórmula $\frac{4}{\zeta\omega_n}$ es una **aproximación**
> 
> **Fuentes de error:**
> 1. Se despreció el factor $1/\sqrt{1-\zeta^2}$ (error del ~10-40% para $\zeta$ pequeños)
> 2. Se usó una cota superior ($e^{-\zeta\omega_n t}$ en lugar de la envolvente completa)
> 3. La respuesta real puede cruzar la banda varias veces antes de establecerse
> 4. Para $\zeta$ muy pequeños, la aproximación no es válida

> [!info] Fórmula más precisa (para $\zeta$ pequeño)
> Incluyendo el factor $1/\sqrt{1-\zeta^2}$:
> $$\frac{e^{-\zeta\omega_n T_s}}{\sqrt{1-\zeta^2}} = 0.02 \implies T_s = \frac{-\ln(0.02 \sqrt{1-\zeta^2})}{\zeta\omega_n}$$
> 
> Para $\zeta = 0.3$: $\sqrt{1-0.09}=0.954$, $-\ln(0.02 \cdot 0.954)= -\ln(0.0191)=3.96 \approx 4$
> 
> Para $\zeta = 0.1$: $\sqrt{1-0.01}=0.995$, $-\ln(0.02 \cdot 0.995)= -\ln(0.0199)=3.92 \approx 4$
> 
> La aproximación $\frac{4}{\zeta\omega_n}$ funciona sorprendentemente bien para $0.1 \le \zeta \le 0.9$.

# Tabla de valores típicos

> [!info] $T_s$ normalizado ($\omega_n = 1$ rad/s)
> 
> | $\zeta$ | $T_s(2\%)$ real (simulación) | $T_s(2\%)$ aproximado | Error |
> |---------|------------------------------|----------------------|-------|
> | 0.1 | 40.0 s | 40.0 s | 0% |
> | 0.3 | 13.3 s | 13.3 s | 0% |
> | 0.5 | 8.0 s | 8.0 s | 0% |
> | 0.7 | 5.7 s | 5.7 s | 0% |
> | 0.9 | 4.5 s | 4.4 s | 2% |
> 
> **Observación:** La aproximación es excelente para $\zeta \ge 0.3$.

# Relación con $M_p$ y $T_p$

> [!info] Conexiones
> - $T_s \approx \frac{4}{\zeta\omega_n} = \frac{4T_p}{\pi} \cdot \frac{\sqrt{1-\zeta^2}}{\zeta}$
> - Para un $M_p$ dado (que fija $\zeta$), $T_s$ es inversamente proporcional a $\omega_n$
> - Especificaciones típicas: $M_p \le 10\%$ y $T_s \le 2$ s determinan $\zeta \ge 0.59$ y $\omega_n \ge 4/(0.59 \cdot 2) \approx 3.4$ rad/s
> 
> Ver [[Sobrepico Mp]] y [[Tiempo Pico Tp]].

# Uso en diseño

> [!info] Especificación típica
> En control, se suele especificar $T_s$ máximo:
> $$T_s \le T_{s,\text{máx}}$$
> 
> Esto impone una condición sobre $\zeta\omega_n$:
> $$\frac{4}{\zeta\omega_n} \le T_{s,\text{máx}} \implies \zeta\omega_n \ge \frac{4}{T_{s,\text{máx}}}$$
> 
> El producto $\zeta\omega_n$ es la **parte real** de los polos complejos (distancia al eje imaginario).
> 
> Ver [[Lugar Raices/index | lugar de las raíces]] para diseño por ubicación de polos.

# Ejemplo numérico

> [!ejemplo] Cálculo de $T_s$
> 
> **Problema:** Un sistema tiene $\zeta = 0.5$ y $\omega_n = 10$ rad/s. Calcule $T_s(2\%)$ aproximado y real (simulado).
> 
> **Solución aproximada:**
> $$T_s(2\%) \approx \frac{4}{\zeta\omega_n} = \frac{4}{0.5 \cdot 10} = \frac{4}{5} = 0.8 \text{ s}$$
> 
> **Solución exacta (resolviendo numéricamente):**
> $$y(t) = 1 - \frac{e^{-5t}}{\sqrt{0.75}} \sin(8.66t + \arccos 0.5)$$
> 
> El tiempo real de establecimiento (último cruce de la banda $\pm 2\%$) es aproximadamente $0.78$ s.
> 
> **Error:** $0.8 - 0.78 = 0.02$ s (2.5%), excelente aproximación.

# Limitaciones

> [!warning]
> 1. **Solo aplica** a sistemas subamortiguados ($0 < \zeta < 1$)
> 2. Para $\zeta \ge 1$, el tiempo de establecimiento es más largo que $\frac{4}{\zeta\omega_n}$ (fórmula conservadora)
> 3. La presencia de **ceros** puede extender el tiempo de establecimiento
> 4. La fórmula asume **realimentación unitaria** y **sistema de segundo orden sin ceros**
> 5. En sistemas de orden superior con polos dominantes, $T_s$ puede diferir (usar polos dominantes como aproximación)
> 6. El criterio $\pm 2\%$ es arbitrario; elegir según aplicación