---
title: Sistemas de Primer Orden
tags:
  - control-clasico
  - analisis
  - respuesta-temporal
draft: false
aliases:
  - primer orden
  - 1er orden
  - respuesta primer orden
---

# Sistemas de Primer Orden

# Definición

> [!definicion] Función transferencia de primer orden
> $$G(s) = \frac{K}{\tau s + 1}$$
> 
> donde:
> - $K$: [[Ganancia Estatica | ganancia estática]] ($G(0) = K$)
> - $\tau$: **constante de tiempo** [segundos]
> 
> **Polo:** $s = -\frac{1}{\tau}$ (siempre real y negativo para sistemas estables)

# Respuesta a escalón

> [!teorema] [[Escalon | Escalón unitario]] ($u(t)=1$, $U(s)=1/s$)
> $$Y(s) = \frac{K}{\tau s + 1} \cdot \frac{1}{s} = \frac{K}{s} - \frac{K}{s + 1/\tau}$$
> 
> **Transformada inversa:**
> $$y(t) = K(1 - e^{-t/\tau}), \quad t \ge 0$$

> [!ejemplo] Gráfico característico
> 
> ![[primer_orden_escalon.svg]]
> 
> **Puntos clave:**
> 
> | $t$ | $y(t)/K$ |
> |-----|----------|
> | $0$ | $0$ |
> | $\tau$ | $1 - e^{-1} \approx 0.632$ |
> | $2\tau$ | $1 - e^{-2} \approx 0.865$ |
> | $3\tau$ | $1 - e^{-3} \approx 0.950$ |
> | $4\tau$ | $1 - e^{-4} \approx 0.982$ |
> | $5\tau$ | $1 - e^{-5} \approx 0.993$ |
> | $\infty$ | $1$ |

# Criterios de tiempo de establecimiento

> [!definicion] Tiempo de establecimiento ($t_s$)
> Es el tiempo necesario para que la respuesta entre y permanezca dentro de una **banda porcentual** alrededor del valor final.
> 
> **Fundamento matemático:**
> $$|y(t) - y(\infty)| \le \frac{\%}{100} \cdot y(\infty)$$
> 
> Para primer orden: $y(\infty) = K$, $y(t) = K(1 - e^{-t/\tau})$
> 
> $$|K(1 - e^{-t/\tau}) - K| = K e^{-t/\tau} \le \frac{\%}{100} K$$
> 
> $$e^{-t/\tau} \le \frac{\%}{100}$$
> 
> Aplicando logaritmo natural:
> $$-\frac{t}{\tau} \le \ln\left(\frac{\%}{100}\right)$$
> 
> Multiplicando por $-1$ (invierte desigualdad):
> $$\frac{t}{\tau} \ge -\ln\left(\frac{\%}{100}\right)$$
> 
> **Por lo tanto:**
> $$t_s = -\tau \cdot \ln\left(\frac{\%}{100}\right)$$

> [!info] Tabla de criterios comunes
> | Criterio | $\%$ | $-\ln(\%/100)$ | $t_s$ |
> |----------|------|----------------|-------|
> | $\pm 5\%$ | $5$ | $-\ln(0.05) \approx 2.9957$ | $3\tau$ |
> | $\pm 2\%$ | $2$ | $-\ln(0.02) \approx 3.9120$ | $4\tau$ |
> | $\pm 1\%$ | $1$ | $-\ln(0.01) \approx 4.6052$ | $4.6\tau$ |
> 
> **Regla práctica:** $t_s(2\%) = 4\tau$ (la más usada en control clásico)

# Tiempo de subida

> [!definicion] Tiempo de subida ($t_r$)
> Tiempo en pasar del $10\%$ al $90\%$ del valor final.
> 
> **Cálculo:**
> 
> Para $90\%$: $0.9 = 1 - e^{-t_{90}/\tau} \implies e^{-t_{90}/\tau} = 0.1 \implies t_{90} = -\tau \ln(0.1) = \tau \ln(10)$
> 
> Para $10\%$: $0.1 = 1 - e^{-t_{10}/\tau} \implies e^{-t_{10}/\tau} = 0.9 \implies t_{10} = -\tau \ln(0.9)$
> 
> $$t_r = t_{90} - t_{10} = \tau [\ln(10) - \ln(0.9)] = \tau \ln\left(\frac{10}{0.9}\right) = \tau \ln(11.11\ldots)$$
> 
> $$t_r \approx 2.1972\tau \approx 2.2\tau$$

# Otras entradas

> [!info] Respuesta a otras señales de prueba
> 
> | Entrada | Respuesta|
> |------|-----|
> | [[Impulso]] | $y(t) = \frac{K}{\tau} e^{-t/\tau}$ |
> | [[Rampa]] | $y(t) = K(t - \tau + \tau e^{-t/\tau})$, $e_{ss} = K\tau$ |
> | [[Parabola]] | $y(t) = K\left(\frac{t^2}{2} - \tau t + \tau^2 - \tau^2 e^{-t/\tau}\right)$, $e_{ss} \to \infty$ |

# Ejemplo resuelto

> [!ejemplo] Problema: Sistema térmico
> Un horno se modela como un sistema de primer orden con función transferencia:
> $$G(s) = \frac{50}{10s + 1}$$
> donde la entrada $u(t)$ es el voltaje de control [V] y la salida $y(t)$ es la temperatura [°C].
> 
> **a)** Determine la constante de tiempo $\tau$ y la ganancia estática $K$.
> 
> **b)** Si se aplica un escalón de $2V$, ¿cuál es la temperatura final?
> 
> **c)** ¿Cuánto tarda en alcanzar el $95\%$ de la temperatura final?
> 
> **d)** ¿Cuánto tarda en pasar de $10\%$ a $90\%$ de la temperatura final?
> 
> **e)** Si se aplica una rampa $u(t) = 3t$, ¿cuál es el error estacionario?
> 
> ---
> 
> **Solución:**
> 
> **a)** Comparando con $G(s) = \frac{K}{\tau s + 1}$:
> $$K = 50, \quad \tau = 10 \text{ s}$$
> 
> **b)** Escalón de $2V$: $u(t) = 2 \cdot 1(t)$, $U(s) = 2/s$
> 
> Por linealidad, la salida final es $y(\infty) = K \cdot u_{ss} = 50 \cdot 2 = 100°C$.
> 
> O aplicando [[Teorema Valor Inicial Final | TVF]]:
> $$\lim_{t\to\infty} y(t) = \lim_{s\to 0} s \cdot \frac{50}{10s+1} \cdot \frac{2}{s} = \lim_{s\to 0} \frac{100}{10s+1} = 100°C$$
> 
> **c)** $95\%$ de $100°C$ es $95°C$.
> 
> Para $y(t) = 100(1 - e^{-t/10}) = 95$:
> $$1 - e^{-t/10} = 0.95 \implies e^{-t/10} = 0.05 \implies -\frac{t}{10} = \ln(0.05)$$
> $$t = -10 \ln(0.05) = 10 \cdot 2.9957 \approx 29.96 \text{ s}$$
> 
> Que es aproximadamente $3\tau = 30$ s (criterio del $5\%$).
> 
> **d)** $t_r = 2.2\tau = 22$ s.
> 
> **e)** Para rampa $u(t)=3t$, $U(s)=3/s^2$. Por [[Error Estacionario/index | error estacionario]]:
> $$K_v = \lim_{s\to 0} s G(s) = \lim_{s\to 0} s \cdot \frac{50}{10s+1} = 0$$
> 
> Sistemas tipo 0 tienen $e_{ss} \to \infty$ para rampa. Verificar con TVF:
> $$E(s) = \frac{1}{1+G(s)} U(s) = \frac{1}{1 + \frac{50}{10s+1}} \cdot \frac{3}{s^2} = \frac{10s+1}{10s+51} \cdot \frac{3}{s^2}$$
> 
> $$e_{ss} = \lim_{s\to 0} s E(s) = \lim_{s\to 0} \frac{10s+1}{10s+51} \cdot \frac{3}{s} = \frac{1}{51} \cdot \infty = \infty$$
> 
> El error tiende a infinito porque el sistema no puede seguir una rampa (necesita al menos un integrador, tipo 1).

# Relaciones importantes

> [!info] Conexiones con otras notas
> - [[Ganancia Estatica]]: $K = G(0)$
> - [[Polos Ceros]]: polo $s = -1/\tau$, condición de estabilidad $\tau > 0$
> - [[Teorema Valor Inicial Final]]: usado para calcular $y(\infty)$
> - [[Error Estacionario/index]]: coeficientes $K_p, K_v, K_a$
> - [[Escalon]], [[Rampa]], [[Parabola]], [[Impulso]]: señales de prueba
> - [[Funcion Transferencia/index | Función Transferencia]]: forma general

# Limitaciones

> [!warning]
> 1. Los sistemas reales rara vez son primer orden puro
> 2. En la práctica, se aproximan por primer orden si hay un [[Polos Ceros#Polos dominantes | polo dominante]]
> 3. La respuesta no tiene sobrepico, por lo que no puede modelar sistemas subamortiguados (ver [[Segundo Orden/index | segundo orden]])