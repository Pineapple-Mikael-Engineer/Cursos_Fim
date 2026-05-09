---
title: Escalón Unitario
tags:
  - control-clasico
  - señales-prueba
  - analisis
draft: false
aliases:
  - escalon
  - step
  - funcion escalon
  - Heaviside
---

# Escalón Unitario

# Definición

> [!definicion] Escalón unitario $u(t)$
> $$u(t) = \begin{cases} 0, & t < 0 \\ 1, & t \ge 0 \end{cases}$$
> 
> También se denota como $1(t)$ o $H(t)$ (función de Heaviside).

> [!definicion] Desplazamiento temporal
> $$u(t - a) = \begin{cases} 0, & t < a \\ 1, & t \ge a \end{cases}$$

# Transformada de Laplace

> [!teorema] Transformada del escalón unitario
> $$\mathcal{L}\{u(t)\} = \frac{1}{s}, \quad \Re(s) > 0$$

> [!demostracion]
> $$\mathcal{L}\{u(t)\} = \int_{0^-}^{\infty} 1 \cdot e^{-st} dt = \left[ \frac{e^{-st}}{-s} \right]_{0}^{\infty}$$
> 
> Para $\Re(s) > 0$, $\lim_{t\to\infty} e^{-st} = 0$, entonces:
> $$\mathcal{L}\{u(t)\} = 0 - \frac{1}{-s} = \frac{1}{s}$$

> [!teorema] Transformada del escalón desplazado
> $$\mathcal{L}\{u(t - a)\} = \frac{e^{-as}}{s}, \quad a \ge 0$$

> [!demostracion]
> Por [[Propiedades | propiedad de desplazamiento temporal]]:
> $$\mathcal{L}\{f(t - a) u(t - a)\} = e^{-as} F(s)$$
> 
> Con $f(t) = 1$ y $F(s) = 1/s$:
> $$\mathcal{L}\{u(t - a)\} = \frac{e^{-as}}{s}$$

# Respuesta de sistemas al escalón

> [!info] Respuesta al escalón
> Para un sistema con función transferencia $G(s)$, la respuesta al escalón es:
> $$y(t) = \mathcal{L}^{-1}\left\{ G(s) \cdot \frac{1}{s} \right\}$$

> [!ejemplo] Sistema de primer orden
> $$G(s) = \frac{K}{\tau s + 1}$$
> 
> $$Y(s) = \frac{K}{\tau s + 1} \cdot \frac{1}{s} = \frac{K}{s} - \frac{K}{s + 1/\tau}$$
> 
> $$y(t) = K(1 - e^{-t/\tau}), \quad t \ge 0$$
> 
> Ver [[Primer Orden]].

> [!ejemplo] Sistema de segundo orden (subamortiguado)
> $$G(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}, \quad 0 < \zeta < 1$$
> 
> $$y(t) = 1 - \frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}} \sin(\omega_d t + \theta)$$
> 
> donde $\omega_d = \omega_n\sqrt{1-\zeta^2}$, $\theta = \arccos(\zeta)$
> 
> Ver [[Segundo Orden/index]].

# Relación con otras señales

> [!info] Derivada e integral
> 
> **Derivada:** $\frac{d}{dt} u(t) = \delta(t)$ ([[Impulso]])
> 
> **Integral:** $\int_{-\infty}^{t} u(\tau) d\tau = t \cdot u(t)$ ([[Rampa]])

> [!info] Otras relaciones
> - [[Impulso]]: $\delta(t)$ es la derivada generalizada del escalón
> - [[Rampa]]: $t \cdot u(t) = \int_0^t u(\tau) d\tau$
> - [[Parabola]]: $\frac{t^2}{2} u(t) = \int_0^t \int_0^\tau u(\sigma) d\sigma d\tau$
> - **Pulso rectangular:** $u(t) - u(t - T)$

# Propiedades importantes

> [!info] Lista de propiedades
> 
> | Propiedad | Expresión |
> |-----------|-----------|
> | Valor inicial | $u(0^+) = 1$ |
> | Valor final | $\lim_{t\to\infty} u(t) = 1$ |
> | Linealidad | $a \cdot u(t) + b \cdot u(t) = (a+b) u(t)$ |
> | Desplazamiento | $u(t - a)$ retrasa la activación |
> | Escalamiento | $u(at) = u(t)$ para $a > 0$ (no cambia la forma) |
> | Multiplicación por función | $f(t) \cdot u(t)$ hace la función causal |

# Error estacionario a escalón

> [!definicion] Coeficiente de error de posición $K_p$
> $$K_p = \lim_{s \to 0} G(s) = G(0)$$
> 
> **Error estacionario a escalón unitario:**
> $$e_{ss} = \frac{1}{1 + K_p}$$

> [!demostracion]
> Para entrada escalón $R(s) = 1/s$, la función transferencia de error es $E(s) = \frac{1}{1+G(s)} R(s)$.
> 
> Aplicando [[Teorema Valor Inicial Final | TVF]]:
> $$e_{ss} = \lim_{s \to 0} s \cdot \frac{1}{1+G(s)} \cdot \frac{1}{s} = \lim_{s \to 0} \frac{1}{1+G(s)} = \frac{1}{1 + G(0)} = \frac{1}{1 + K_p}$$

> [!info] Relación con otras señales y sus coeficientes de error
> 
> | Señal | Coeficiente | Error estacionario |
> |-------|-------------|-------------------|
> | Escalon Unitario | $K_p = \lim_{s \to 0} G(s)$ | $e_{ss} = \frac{1}{1+K_p}$ |
> | [[Rampa]] | $K_v = \lim_{s \to 0} s G(s)$ | $e_{ss} = \frac{1}{K_v}$ |
> | [[Parabola]] | $K_a = \lim_{s \to 0} s^2 G(s)$ | $e_{ss} = \frac{1}{K_a}$ |
> 
> Ver [[Error Estacionario/index | error estacionario]] para:
> - Tabla completa por tipo de sistema (0, 1, 2)
> - Demostraciones unificadas
> - Casos con realimentación no unitaria

> [!warning] Nota sobre el [[Impulso]]
> El impulso no tiene coeficiente de error estacionario definido porque la entrada tiende a cero para $t > 0$.

# Dependencia con el tipo de sistema

> [!info] $e_{ss}$ para escalón según el tipo
> | Tipo | $K_p$ | $e_{ss}$ (escalón unitario) |
> |------|-------|----------------------------|
> | 0 | $K$ (finito) | $\frac{1}{1+K}$ |
> | 1 | $\infty$ | $0$ |
> | 2 | $\infty$ | $0$ |
> 
> Ver [[Error Estacionario/index | error estacionario]] para definición de tipos de sistema.

# Uso en control

> [!info] ¿Por qué el escalón?
> 1. **Responde a una pregunta práctica:** "¿Qué pasa si enciendo el sistema de repente?"
> 2. **Contiene todas las frecuencias:** su espectro es $1/(j\omega)$, útil para análisis frecuencial
> 3. **Relación con respuesta impulsional:** $y_{\text{escalón}}(t) = \int_0^t h(\tau) d\tau$
> 4. **Caracteriza el sistema:** si conozco la respuesta al escalón, conozco el sistema (para sistemas LTI)
> 5. **Parámetros de desempeño:** $t_r$, $t_s$, $M_p$, $e_{ss}$ se definen sobre respuesta al escalón
> 6. **Diseño de compensadores:** Los compensadores [[Lag]] aumentan $K_p$ para reducir $e_{ss}$

# Ejemplo de extracción de parámetros

> [!ejemplo] Identificación de sistema desde respuesta al escalón
> 
> ![[identificacion_escalon.svg]]
> 
> **Para primer orden:**
> 1. Medir $y(\infty) = K$
> 2. Encontrar $t$ tal que $y(t) = 0.632K$ → $\tau$
> 3. Verificar: $y(2\tau) \approx 0.865K$, $y(3\tau) \approx 0.95K$
> 
> **Para segundo orden:** (ver [[Segundo Orden/index]])
> - Medir $M_p = \frac{y_{\text{máx}} - y(\infty)}{y(\infty)}$ → $\zeta$
> - Medir $T_p$ (tiempo del primer pico) → $\omega_n$
> - Medir $T_s(2\%)$ → $4/(\zeta\omega_n)$

# Limitaciones

> [!warning]
> 1. **Matemáticamente ideal:** No se puede generar un escalón perfecto en la práctica (subida siempre tiene pendiente finita)
> 2. **Sistemas inestables:** Respuesta al escalón diverge → no se pueden definir tiempos de establecimiento
> 3. **No linealidades:** En presencia de saturación, la respuesta a escalón NO caracteriza completamente el sistema