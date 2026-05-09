---
title: Rampa Unitaria
tags:
  - control-clasico
  - señales-prueba
  - analisis
draft: false
aliases:
  - rampa
  - ramp
  - funcion rampa
---

# Rampa Unitaria

# Definición

> [!definicion] Rampa unitaria $r(t)$
> $$r(t) = \begin{cases} 0, & t < 0 \\ t, & t \ge 0 \end{cases}$$
> 
> También se denota como $t \cdot u(t)$ donde $u(t)$ es el [[Escalon | escalón unitario]].

> [!definicion] Desplazamiento temporal
> $$r(t - a) = (t - a) \cdot u(t - a) = \begin{cases} 0, & t < a \\ t - a, & t \ge a \end{cases}$$

# Transformada de Laplace

> [!teorema] Transformada de la rampa unitaria
> $$\mathcal{L}\{r(t)\} = \frac{1}{s^2}, \quad \Re(s) > 0$$

> [!demostracion] Método 1: Integración directa
> $$\mathcal{L}\{r(t)\} = \int_{0}^{\infty} t e^{-st} dt$$
> 
> Integración por partes: $u = t$, $dv = e^{-st} dt$, $du = dt$, $v = -\frac{1}{s} e^{-st}$:
> $$\int t e^{-st} dt = \left[ -\frac{t}{s} e^{-st} \right]_{0}^{\infty} + \frac{1}{s} \int_{0}^{\infty} e^{-st} dt$$
> 
> $$= 0 + \frac{1}{s} \cdot \frac{1}{s} = \frac{1}{s^2}$$

> [!demostracion] Método 2: Relación con [[Escalon]]
> Como $r(t) = \int_{0}^{t} u(\tau) d\tau$, por [[Propiedades | propiedad de integración]]:
> $$\mathcal{L}\{r(t)\} = \frac{1}{s} \cdot \mathcal{L}\{u(t)\} = \frac{1}{s} \cdot \frac{1}{s} = \frac{1}{s^2}$$

> [!teorema] Transformada de rampa desplazada
> $$\mathcal{L}\{r(t - a)\} = \frac{e^{-as}}{s^2}, \quad a \ge 0$$

# Relación con otras señales

> [!info] Derivada e integral
> 
> **Derivada:** $\frac{d}{dt} r(t) = u(t)$ ([[Escalon]])
> 
> **Derivada segunda:** $\frac{d^2}{dt^2} r(t) = \delta(t)$ ([[Impulso]])
> 
> **Integral:** $\int_{0}^{t} r(\tau) d\tau = \frac{t^2}{2} u(t)$ ([[Parabola]])

> [!info] Otras relaciones
> - [[Escalon]]: $u(t) = \frac{d}{dt} r(t)$
> - [[Impulso]]: $\delta(t) = \frac{d^2}{dt^2} r(t)$
> - [[Parabola]]: $\frac{t^2}{2} u(t) = \int_{0}^{t} r(\tau) d\tau$

# Respuesta de sistemas a la rampa

> [!info] Relación con respuesta al escalón
> Para un sistema LTI con función transferencia $G(s)$:
> 
> $$Y_{\text{rampa}}(s) = G(s) \cdot \frac{1}{s^2} = \frac{1}{s} \cdot \left( G(s) \cdot \frac{1}{s} \right) = \frac{1}{s} Y_{\text{escalón}}(s)$$
> 
> Por lo tanto:
> $$y_{\text{rampa}}(t) = \int_{0}^{t} y_{\text{escalón}}(\tau) d\tau$$

> [!ejemplo] Sistema de primer orden
> $$G(s) = \frac{K}{\tau s + 1}$$
> 
> $$Y_{\text{rampa}}(s) = \frac{K}{\tau s + 1} \cdot \frac{1}{s^2}$$
> 
> Descomposición en fracciones parciales:
> $$\frac{K}{s^2(\tau s + 1)} = \frac{A}{s} + \frac{B}{s^2} + \frac{C}{\tau s + 1}$$
> 
> Calculando: $A = -K\tau$, $B = K$, $C = K\tau^2$
> 
> $$Y_{\text{rampa}}(s) = -\frac{K\tau}{s} + \frac{K}{s^2} + \frac{K\tau^2}{\tau s + 1}$$
> 
> Transformada inversa:
> $$y_{\text{rampa}}(t) = -K\tau + Kt + K\tau e^{-t/\tau}, \quad t \ge 0$$
> 
> **Interpretación:** Para $t \gg \tau$, $y_{\text{rampa}}(t) \approx K(t - \tau)$
> 
> La salida sigue una rampa $Kt$ pero con un **retardo** $\tau$ y un **offset** inicial.

# Error estacionario a rampa

> [!definicion] Coeficiente de error de velocidad $K_v$
> $$K_v = \lim_{s \to 0} s G(s)$$
> 
> **Error estacionario a rampa unitaria:**
> $$e_{ss} = \frac{1}{K_v}$$

> [!demostracion]
> Para entrada rampa $R(s) = 1/s^2$, la función transferencia de error es $E(s) = \frac{1}{1+G(s)} R(s)$.
> 
> Aplicando [[Teorema Valor Inicial Final | TVF]]:
> $$e_{ss} = \lim_{s \to 0} s \cdot \frac{1}{1+G(s)} \cdot \frac{1}{s^2} = \lim_{s \to 0} \frac{1}{s(1+G(s))}$$
> 
> Multiplicando numerador y denominador por $s$:
> $$e_{ss} = \lim_{s \to 0} \frac{1}{\frac{1}{s} + \frac{G(s)}{s}} = \frac{1}{\lim_{s \to 0} s G(s)} = \frac{1}{K_v}$$

> [!info] Relación con otras señales y sus coeficientes de error
> 
> | Señal | Coeficiente | Error estacionario |
> |-------|-------------|-------------------|
> | [[Escalon]] | $K_p = \lim_{s \to 0} G(s)$ | $e_{ss} = \frac{1}{1+K_p}$ |
> | Rampa Unitaria| $K_v = \lim_{s \to 0} s G(s)$ | $e_{ss} = \frac{1}{K_v}$ |
> | [[Parabola]] | $K_a = \lim_{s \to 0} s^2 G(s)$ | $e_{ss} = \frac{1}{K_a}$ |
> 
> Ver [[Error Estacionario/index | error estacionario]] para:
> - Tabla completa por tipo de sistema (0, 1, 2)
> - Demostraciones unificadas
> - Casos con realimentación no unitaria

> [!warning] Nota sobre el [[Impulso]]
> El impulso no tiene coeficiente de error estacionario definido porque:
> - La entrada tiende a cero para $t > 0$
> - No es una entrada de referencia que se mantenga en régimen permanente
> - Su uso principal es obtener la respuesta impulsional $h(t)$

# Dependencia con el tipo de sistema

> [!info] $e_{ss}$ para rampa según el tipo
> | Tipo | $K_v$ | $e_{ss}$ (rampa unitaria) |
> |------|-------|---------------------------|
> | 0 | $0$ | $\infty$ (no sigue) |
> | 1 | $K$ (finito) | $\frac{1}{K}$ |
> | 2 | $\infty$ | $0$ (sigue perfectamente) |
> 
> Ver [[Error Estacionario/index | error estacionario]] para definición de tipos de sistema.

# Uso en control

> [!info] ¿Por qué la rampa?
> 1. **Evalúa seguimiento de velocidad:** ¿El sistema puede seguir una entrada que cambia linealmente?
> 2. **Define $K_v$:** Coeficiente de error de velocidad, especificación común en servomecanismos
> 3. **Relación con posición:** La rampa es la integral del escalón, útil para sistemas tipo 1 (con integrador)
> 4. **Detección de estado estacionario:** El error a rampa revela si el sistema tiene al menos un integrador
> 5. **Diseño de compensadores:** Los compensadores [[Lag]] aumentan $K_v$ sin afectar la estabilidad

# Ejemplo de extracción de parámetros

> [!ejemplo] Identificación desde respuesta a rampa
> 
> **Problema:** Un sistema tiene respuesta a rampa unitaria $y(t) = 3t - 6 + 2e^{-t/2}$ para $t \ge 0$. Determine su función transferencia.
> 
> **Paso 1:** Identificar el régimen permanente.
> 
> Para $t$ grande, $e^{-t/2} \to 0$, entonces $y(t) \approx 3t - 6$
> 
> Esto indica:
> - $K = 3$ (ganancia estática)
> - Retardo equivalente: $3(t - 2) = 3t - 6$ → $\tau = 2$ s
> 
> **Paso 2:** La forma general para primer orden es:
> $$y_{\text{rampa}}(t) = K(t - \tau + \tau e^{-t/\tau})$$
> 
> Con $K=3$, $\tau=2$:
> $$y(t) = 3(t - 2 + 2e^{-t/2}) = 3t - 6 + 6e^{-t/2}$$
> 
> **Paso 3:** Comparar con la respuesta dada: $3t - 6 + 2e^{-t/2}$
> 
> Hay discrepancia: coeficiente $2$ vs $6$ en el término exponencial.
> 
> **Conclusión:** El sistema NO es de primer orden. Tiene dinámica adicional.
> 
> **Paso 4:** Para un sistema más general, usar fracciones parciales o identificación en frecuencia.

# Limitaciones

> [!warning]
> 1. **Físicamente irrealizable:** Una rampa crece indefinidamente, ningún sistema físico puede generarla sin saturar
> 2. **Sistemas tipo 0:** No pueden seguir una rampa (error infinito)
> 3. **Señal de prueba matemática:** Útil para análisis pero no para excitación experimental directa (se usan escalón o señales sinusoidales)
> 4. **Integradores:** La rampa se usa principalmente para caracterizar sistemas con al menos un integrador (tipo 1 o superior)