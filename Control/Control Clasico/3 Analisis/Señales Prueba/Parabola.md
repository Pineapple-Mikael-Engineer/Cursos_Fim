---
title: Parábola Unitaria
tags:
  - control-clasico
  - señales-prueba
  - analisis
draft: false
aliases:
  - parabola
  - parabolic
  - funcion parabola
  - aceleracion
---

# Parábola Unitaria

# Definición

> [!definicion] Parábola unitaria $p(t)$
> $$p(t) = \begin{cases} 0, & t < 0 \\ \frac{t^2}{2}, & t \ge 0 \end{cases}$$
> 
> También se denota como $\frac{t^2}{2} \cdot u(t)$ donde $u(t)$ es el [[Escalon | escalón unitario]].

> [!definicion] Desplazamiento temporal
> $$p(t - a) = \frac{(t - a)^2}{2} \cdot u(t - a) = \begin{cases} 0, & t < a \\ \frac{(t - a)^2}{2}, & t \ge a \end{cases}$$

# Transformada de Laplace

> [!teorema] Transformada de la parábola unitaria
> $$\mathcal{L}\{p(t)\} = \frac{1}{s^3}, \quad \Re(s) > 0$$

> [!demostracion] Método 1: Integración directa
> $$\mathcal{L}\{p(t)\} = \int_{0}^{\infty} \frac{t^2}{2} e^{-st} dt = \frac{1}{2} \int_{0}^{\infty} t^2 e^{-st} dt$$
> 
> Sabemos que $\mathcal{L}\{t^2\} = \frac{2}{s^3}$, entonces:
> $$\mathcal{L}\{p(t)\} = \frac{1}{2} \cdot \frac{2}{s^3} = \frac{1}{s^3}$$

> [!demostracion] Método 2: Relación con [[Escalon]] y [[Rampa]]
> Como $p(t) = \int_{0}^{t} r(\tau) d\tau = \int_{0}^{t} \int_{0}^{\tau} u(\sigma) d\sigma d\tau$, por [[Propiedades | propiedad de integración]]:
> $$\mathcal{L}\{p(t)\} = \frac{1}{s} \cdot \mathcal{L}\{r(t)\} = \frac{1}{s} \cdot \frac{1}{s^2} = \frac{1}{s^3}$$

> [!teorema] Transformada de parábola desplazada
> $$\mathcal{L}\{p(t - a)\} = \frac{e^{-as}}{s^3}, \quad a \ge 0$$

# Relación con otras señales

> [!info] Derivada e integral
> 
> **Derivada:** $\frac{d}{dt} p(t) = r(t)$ ([[Rampa]])
> 
> **Derivada segunda:** $\frac{d^2}{dt^2} p(t) = u(t)$ ([[Escalon]])
> 
> **Derivada tercera:** $\frac{d^3}{dt^3} p(t) = \delta(t)$ ([[Impulso]])
> 
> **Integral:** $\int_{0}^{t} p(\tau) d\tau = \frac{t^3}{6} u(t)$

> [!info] Otras relaciones
> - [[Escalon]]: $u(t) = \frac{d^2}{dt^2} p(t)$
> - [[Rampa]]: $r(t) = \frac{d}{dt} p(t)$
> - [[Impulso]]: $\delta(t) = \frac{d^3}{dt^3} p(t)$

# Respuesta de sistemas a la parábola

> [!info] Relación con respuesta al escalón
> Para un sistema LTI con función transferencia $G(s)$:
> 
> $$Y_{\text{parábola}}(s) = G(s) \cdot \frac{1}{s^3} = \frac{1}{s^2} \cdot \left( G(s) \cdot \frac{1}{s} \right) = \frac{1}{s^2} Y_{\text{escalón}}(s)$$
> 
> Por lo tanto:
> $$y_{\text{parábola}}(t) = \int_{0}^{t} \int_{0}^{\tau} y_{\text{escalón}}(\sigma) d\sigma d\tau$$

> [!ejemplo] Sistema de primer orden
> $$G(s) = \frac{K}{\tau s + 1}$$
> 
> $$Y_{\text{parábola}}(s) = \frac{K}{\tau s + 1} \cdot \frac{1}{s^3}$$
> 
> Descomposición en fracciones parciales:
> $$\frac{K}{s^3(\tau s + 1)} = \frac{A}{s} + \frac{B}{s^2} + \frac{C}{s^3} + \frac{D}{\tau s + 1}$$
> 
> Calculando:
> - $C = K$
> - $B = -K\tau$
> - $A = K\tau^2$
> - $D = -K\tau^3$
> 
> $$Y_{\text{parábola}}(s) = \frac{K\tau^2}{s} - \frac{K\tau}{s^2} + \frac{K}{s^3} - \frac{K\tau^3}{\tau s + 1}$$
> 
> Transformada inversa:
> $$y_{\text{parábola}}(t) = K\tau^2 - K\tau t + K\frac{t^2}{2} - K\tau^2 e^{-t/\tau}, \quad t \ge 0$$
> 
> **Interpretación:** Para $t \gg \tau$, $y_{\text{parábola}}(t) \approx K\left(\frac{t^2}{2} - \tau t + \tau^2\right)$
> 
> La salida sigue una parábola $K\frac{t^2}{2}$ pero con un **retardo** y un **offset** que dependen de $\tau$.

# Error estacionario a parábola

> [!definicion] Coeficiente de error de aceleración $K_a$
> $$K_a = \lim_{s \to 0} s^2 G(s)$$
> 
> **Error estacionario a parábola unitaria:**
> $$e_{ss} = \frac{1}{K_a}$$

> [!demostracion]
> Para entrada parábola $R(s) = 1/s^3$, la función transferencia de error es $E(s) = \frac{1}{1+G(s)} R(s)$.
> 
> Aplicando [[Teorema Valor Inicial Final | TVF]]:
> $$e_{ss} = \lim_{s \to 0} s \cdot \frac{1}{1+G(s)} \cdot \frac{1}{s^3} = \lim_{s \to 0} \frac{1}{s^2(1+G(s))}$$
> 
> Multiplicando numerador y denominador por $s^2$:
> $$e_{ss} = \lim_{s \to 0} \frac{1}{s^2 + s^2 G(s)} = \frac{1}{\lim_{s \to 0} s^2 G(s)} = \frac{1}{K_a}$$

> [!info] Relación con otras señales y sus coeficientes de error
> 
> | Señal | Coeficiente | Error estacionario |
> |-------|-------------|-------------------|
> | [[Escalon]] | $K_p = \lim_{s \to 0} G(s)$ | $e_{ss} = \frac{1}{1+K_p}$ |
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

> [!info] $e_{ss}$ para parábola según el tipo
> | Tipo | $K_a$ | $e_{ss}$ (parábola unitaria) |
> |------|-------|------------------------------|
> | 0 | $0$ | $\infty$ (no sigue) |
> | 1 | $0$ | $\infty$ (no sigue) |
> | 2 | $K$ (finito) | $\frac{1}{K}$ |
> 
> **Importante:** Solo los sistemas tipo 2 o superior pueden seguir una parábola sin error infinito.
> 
> Ver [[Error Estacionario/index | error estacionario]] para definición de tipos de sistema.

# Uso en control

> [!info] ¿Por qué la parábola?
> 1. **Evalúa seguimiento de aceleración:** ¿El sistema puede seguir una entrada que cambia cuadráticamente?
> 2. **Define $K_a$:** Coeficiente de error de aceleración, especificación para sistemas de posicionamiento de alta precisión
> 3. **Relación con posición:** La parábola es la doble integral del escalón, útil para sistemas tipo 2 (con dos integradores)
> 4. **Detección de estado estacionario:** El error a parábola revela si el sistema tiene al menos dos integradores
> 5. **Sistemas de seguimiento:** Especificación común en sistemas de seguimiento de trayectorias (ej. radares, robots)

# Jerarquía de señales

> [!info] Escalón → Rampa → Parábola
> 
> | Señal | Operador | Tipo mínimo requerido | Error finito |
> |--------|----------|----------------------|--------------|
> | [[Escalon]] | posición | 0 | $e_{ss} = 1/(1+K_p)$ |
> | [[Rampa]] | velocidad | 1 | $e_{ss} = 1/K_v$ |
> | Parábola Unitaria | aceleración | 2 | $e_{ss} = 1/K_a$ |
> 
> **Interpretación física:**
> - Un sistema tipo 0 puede mantener posición constante
> - Un sistema tipo 1 puede seguir velocidades constantes (error finito)
> - Un sistema tipo 2 puede seguir aceleraciones constantes (error finito)

# Ejemplo de extracción de parámetros

> [!ejemplo] Identificación desde respuesta a parábola
> 
> **Problema:** Un sistema tipo 2 tiene respuesta a parábola unitaria $y(t) = \frac{t^2}{2} - 2t + 2 - 2e^{-t}$ para $t \ge 0$. Determine $K_a$ y la función transferencia.
> 
> **Paso 1:** Identificar el régimen permanente.
> 
> Para $t$ grande, $e^{-t} \to 0$, entonces $y(t) \approx \frac{t^2}{2} - 2t + 2$
> 
> **Paso 2:** La forma general para parábola en sistema tipo 2 es:
> $$y(t) = \frac{K_a}{2} t^2 - K_a \tau t + K_a \tau^2 + \text{términos transitorios}$$
> 
> Comparando:
> - Coeficiente de $t^2/2$: $\frac{K_a}{2} = \frac{1}{2} \implies K_a = 1$
> - Coeficiente de $t$: $-K_a \tau = -2 \implies \tau = 2$ s
> - Término constante: $K_a \tau^2 = 4$, pero tenemos $2$ → hay offset adicional
> 
> **Paso 3:** El término exponencial $2e^{-t}$ tiene coeficiente $2$, pero la fórmula esperada es $K_a \tau^2 e^{-t/\tau} = 4e^{-t/2}$ si fuera primer orden.
> 
> Hay discrepancia → el sistema NO es de primer orden. Tiene dinámica más compleja.
> 
> **Conclusión:** La respuesta a parábola revela más detalles de la dinámica que el escalón o la rampa.

# Limitaciones

> [!warning]
> 1. **Físicamente irrealizable:** Una parábola crece como $t^2$, ningún sistema físico puede generarla sin saturar rápidamente
> 2. **Sistemas tipo 0 y 1:** No pueden seguir una parábola (error infinito)
> 3. **Señal de prueba avanzada:** Se usa principalmente para sistemas tipo 2 (ej. posicionadores con doble integrador)
> 4. **Sensibilidad al ruido:** La doble integración amplifica el ruido de medición
> 5. **Experimentalmente difícil:** No se usa como entrada de prueba directa; se prefiere escalón + integración numérica o identificación en frecuencia