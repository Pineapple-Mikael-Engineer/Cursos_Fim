---
title: Convolución TF
tags:
  - control-clasico
  - teoria
  - transformada-laplace
draft: false
aliases:
  - convolucion
  - integral de convolucion
  - teorema de convolucion
---

# Convolución

# Definición

> [!definicion] Convolución en tiempo
> Dadas dos funciones $f(t)$ y $g(t)$ definidas para $t \ge 0$, su convolución es:
> $$(f * g)(t) = \int_0^t f(\tau) g(t - \tau) d\tau$$
> 
> La integral se evalúa desde $0$ hasta $t$ porque ambas funciones son causales (cero para $t < 0$).

> [!definicion] Propiedades de la convolución
> | Propiedad | Expresión |
> |-----------|-----------|
> | Conmutativa | $f * g = g * f$ |
> | Asociativa | $f * (g * h) = (f * g) * h$ |
> | Distributiva | $f * (g + h) = f * g + f * h$ |
> | Elemento neutro | $f * \delta = f$ |
> | Elemento absorbente | $f * 0 = 0$ |

# Teorema de convolución

> [!teorema] Teorema de convolución en Laplace
> $$\mathcal{L}\{(f * g)(t)\} = F(s) G(s)$$
> 
> donde $F(s) = \mathcal{L}\{f(t)\}$ y $G(s) = \mathcal{L}\{g(t)\}$.

> [!demostracion]
> Por definición de transformada de Laplace:
> $$\mathcal{L}\{(f * g)(t)\} = \int_0^\infty \left[ \int_0^t f(\tau) g(t - \tau) d\tau \right] e^{-st} dt$$
> 
> **Paso 1:** Cambiar el orden de integración. La región de integración es $0 \le \tau \le t < \infty$. Invirtiendo:
> $$\int_0^\infty \int_\tau^\infty f(\tau) g(t - \tau) e^{-st} dt d\tau$$
> 
> **Paso 2:** Factorizar $f(\tau)$ (no depende de $t$):
> $$\int_0^\infty f(\tau) \left[ \int_\tau^\infty g(t - \tau) e^{-st} dt \right] d\tau$$
> 
> **Paso 3:** Cambio de variable en la integral interna: $u = t - \tau$, $du = dt$, cuando $t = \tau$, $u = 0$; cuando $t \to \infty$, $u \to \infty$:
> $$\int_\tau^\infty g(t - \tau) e^{-st} dt = \int_0^\infty g(u) e^{-s(u + \tau)} du = e^{-s\tau} \int_0^\infty g(u) e^{-su} du = e^{-s\tau} G(s)$$
> 
> **Paso 4:** Sustituir:
> $$\mathcal{L}\{(f * g)(t)\} = \int_0^\infty f(\tau) e^{-s\tau} G(s) d\tau = G(s) \int_0^\infty f(\tau) e^{-s\tau} d\tau = F(s) G(s)$$

# Corolario: transformada inversa de un producto

> [!teorema] Transformada inversa de un producto
> Si $Y(s) = F(s) G(s)$, entonces:
> $$y(t) = (f * g)(t) = \int_0^t f(\tau) g(t - \tau) d\tau$$

> [!ejemplo]
> $F(s) = \frac{1}{s+1}$, $G(s) = \frac{1}{s+2}$.
> 
> $f(t) = e^{-t}$, $g(t) = e^{-2t}$.
> 
> Por convolución:
> $$y(t) = \int_0^t e^{-\tau} e^{-2(t - \tau)} d\tau = e^{-2t} \int_0^t e^{\tau} d\tau = e^{-2t} (e^{t} - 1) = e^{-t} - e^{-2t}$$
> 
> Directo por fracciones parciales:
> $$Y(s) = \frac{1}{(s+1)(s+2)} = \frac{1}{s+1} - \frac{1}{s+2} \implies y(t) = e^{-t} - e^{-2t}$$

# Propiedad conmutativa

> [!teorema] $f * g = g * f$

> [!demostracion]
> Partiendo de la definición:
> $$(f * g)(t) = \int_0^t f(\tau) g(t - \tau) d\tau$$
> 
> Cambio de variable $u = t - \tau$, $du = -d\tau$, cuando $\tau = 0$, $u = t$; cuando $\tau = t$, $u = 0$:
> $$\int_0^t f(\tau) g(t - \tau) d\tau = \int_t^0 f(t - u) g(u) (-du) = \int_0^t g(u) f(t - u) du = (g * f)(t)$$

# Aplicación en sistemas LTI

> [!info] Respuesta a cualquier entrada
> Para un sistema LTI con respuesta impulsional $h(t)$:
> $$y(t) = (h * u)(t) = \int_0^t h(\tau) u(t - \tau) d\tau$$
> 
> En Laplace: $Y(s) = H(s) U(s)$.

> [!ejemplo] Sistema de primer orden
> $h(t) = 2e^{-3t}$, entrada $u(t) = e^{-t}$.
> 
> $$y(t) = \int_0^t 2e^{-3\tau} \cdot e^{-(t - \tau)} d\tau = 2e^{-t} \int_0^t e^{-2\tau} d\tau$$
> 
> $$= 2e^{-t} \cdot \frac{1 - e^{-2t}}{2} = e^{-t} - e^{-3t}$$
> 
> Verificación en Laplace:
> $$Y(s) = \frac{2}{s+3} \cdot \frac{1}{s+1} = \frac{1}{s+1} - \frac{1}{s+3} \implies y(t) = e^{-t} - e^{-3t}$$

# Demostración de la propiedad conmutativa mediante Laplace

> [!demostracion] Alternativa usando teorema de convolución
> Por el teorema de convolución:
> $$\mathcal{L}\{f * g\} = F(s) G(s) = G(s) F(s) = \mathcal{L}\{g * f\}$$
> 
> Por unicidad de la transformada inversa, $f * g = g * f$.

# Ejemplos adicionales

> [!ejemplo] Convolución con escalón
> $f(t) = e^{-at}$, $g(t) = u(t)$.
> 
> $$(f * u)(t) = \int_0^t e^{-a\tau} \cdot 1 d\tau = \frac{1 - e^{-at}}{a}$$
> 
> En Laplace: $F(s) = \frac{1}{s+a}$, $U(s) = \frac{1}{s}$:
> $$Y(s) = \frac{1}{s(s+a)} = \frac{1/a}{s} - \frac{1/a}{s+a} \implies y(t) = \frac{1}{a}(1 - e^{-at})$$

> [!ejemplo] Convolución de dos escalones
> $f(t) = u(t)$, $g(t) = u(t)$.
> 
> $$(u * u)(t) = \int_0^t 1 \cdot 1 d\tau = t$$
> 
> En Laplace: $U(s) = 1/s$, $U(s)^2 = 1/s^2 \implies \mathcal{L}^{-1}\{1/s^2\} = t$.

> [!ejemplo] Convolución de un pulso consigo mismo
> $f(t) = 1$ para $0 \le t \le 1$, cero en otro caso. $f(t) = u(t) - u(t-1)$.
> 
> Para $0 \le t \le 1$:
> $$(f * f)(t) = \int_0^t 1 \cdot 1 d\tau = t$$
> 
> Para $1 \le t \le 2$:
> $$(f * f)(t) = \int_{t-1}^1 1 \cdot 1 d\tau = 2 - t$$
> 
> Para $t > 2$: $0$.
> 
> Resultado: señal triangular en $[0,2]$ con pico $1$ en $t=1$.

# Relación con la respuesta escalón

> [!info] Respuesta escalón desde respuesta impulsional
> Si $h(t)$ es la respuesta impulsional, la respuesta al escalón $u(t)$ es:
> $$y_{\text{escalón}}(t) = \int_0^t h(\tau) d\tau$$

> [!demostracion]
> $$y_{\text{escalón}}(t) = (h * u)(t) = \int_0^t h(\tau) u(t - \tau) d\tau = \int_0^t h(\tau) \cdot 1 d\tau$$

# Limitaciones

> [!warning]
> 1. La convolución solo se define para $t \ge 0$ si las señales son causales
> 2. En sistemas no lineales el teorema de convolución **no aplica**
> 3. La integral puede ser difícil de calcular analíticamente; usar Laplace cuando sea posible