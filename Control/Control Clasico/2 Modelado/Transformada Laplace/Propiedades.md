---
title: Propiedades de la TL
tags:
  - control-clasico
  - teoria
  - transformada-laplace
draft: false
aliases:
  - propiedades laplace
  - linealidad laplace
  - derivacion laplace
  - integracion laplace
---

# Propiedades de la Transformada de Laplace

# Linealidad

> [!teorema] Linealidad
> $$\mathcal{L}\{a f_1(t) + b f_2(t)\} = a F_1(s) + b F_2(s)$$

> [!demostracion]
> Por definición:
> $$\mathcal{L}\{a f_1(t) + b f_2(t)\} = \int_0^\infty [a f_1(t) + b f_2(t)] e^{-st} dt$$
> 
> $$= a \int_0^\infty f_1(t) e^{-st} dt + b \int_0^\infty f_2(t) e^{-st} dt = a F_1(s) + b F_2(s)$$

> [!ejemplo]
> $f(t) = 3e^{-2t} + 5\sin(4t)$
> 
> $$F(s) = 3 \cdot \frac{1}{s+2} + 5 \cdot \frac{4}{s^2+16} = \frac{3}{s+2} + \frac{20}{s^2+16}$$

# Derivación en tiempo

> [!teorema] Primera derivada
> $$\mathcal{L}\{f'(t)\} = sF(s) - f(0^-)$$

> [!demostracion]
> Por definición:
> $$\mathcal{L}\{f'(t)\} = \int_0^\infty f'(t) e^{-st} dt$$
> 
> Integrando por partes: $u = e^{-st}$, $dv = f'(t) dt$, $du = -s e^{-st} dt$, $v = f(t)$:
> 
> $$\int_0^\infty f'(t) e^{-st} dt = \left[ f(t) e^{-st} \right]_0^\infty - \int_0^\infty f(t) (-s e^{-st}) dt$$
> 
> $$= \lim_{t \to \infty} f(t) e^{-st} - f(0^-) + s \int_0^\infty f(t) e^{-st} dt$$
> 
> Para $\Re(s)$ suficientemente grande, $\lim_{t \to \infty} f(t) e^{-st} = 0$. Por lo tanto:
> $$\mathcal{L}\{f'(t)\} = -f(0^-) + sF(s) = sF(s) - f(0^-)$$

> [!teorema] Segunda derivada
> $$\mathcal{L}\{f''(t)\} = s^2 F(s) - s f(0^-) - f'(0^-)$$

> [!demostracion]
> Aplicando el teorema de la primera derivada dos veces:
> 
> $\mathcal{L}\{f''(t)\} = \mathcal{L}\{(f')'(t)\} = s \mathcal{L}\{f'(t)\} - f'(0^-)$
> 
> Sustituyendo $\mathcal{L}\{f'(t)\} = sF(s) - f(0^-)$:
> 
> $$\mathcal{L}\{f''(t)\} = s[sF(s) - f(0^-)] - f'(0^-) = s^2 F(s) - s f(0^-) - f'(0^-)$$

> [!teorema] Derivada de orden $n$
> $$\mathcal{L}\{f^{(n)}(t)\} = s^n F(s) - \sum_{k=1}^n s^{n-k} f^{(k-1)}(0^-)$$

> [!demostracion]
> Por inducción usando el teorema de la primera derivada.

> [!ejemplo] EDO con condiciones iniciales
> Resolver $\ddot{y} + 3\dot{y} + 2y = u(t)$ con $y(0)=1$, $\dot{y}(0)=0$.
> 
> Aplicando Laplace:
> $$[s^2 Y(s) - s y(0) - \dot{y}(0)] + 3[sY(s) - y(0)] + 2Y(s) = \frac{1}{s}$$
> 
> $$s^2 Y(s) - s + 3sY(s) - 3 + 2Y(s) = \frac{1}{s}$$
> 
> $$(s^2 + 3s + 2)Y(s) = \frac{1}{s} + s + 3$$
> 
> $$Y(s) = \frac{s^2 + 3s + \frac{1}{s}}{(s+1)(s+2)} = \frac{s^3 + 3s^2 + 1}{s(s+1)(s+2)}$$

# Integración en tiempo

> [!teorema] Integración
> $$\mathcal{L}\left\{ \int_0^t f(\tau) d\tau \right\} = \frac{F(s)}{s}$$

> [!demostracion]
> Sea $g(t) = \int_0^t f(\tau) d\tau$. Entonces $g'(t) = f(t)$ y $g(0) = 0$.
> 
> Por el teorema de la derivada: $\mathcal{L}\{g'(t)\} = sG(s) - g(0) = sG(s)$.
> 
 Pero $\mathcal{L}\{g'(t)\} = \mathcal{L}\{f(t)\} = F(s)$.
> 
> Por lo tanto: $sG(s) = F(s) \implies G(s) = \frac{F(s)}{s}$.

> [!ejemplo]
> $f(t) = t^2$, sabiendo que $\mathcal{L}\{2t\} = \frac{2}{s^2}$:
> 
> $$t^2 = \int_0^t 2\tau d\tau \implies \mathcal{L}\{t^2\} = \frac{1}{s} \cdot \frac{2}{s^2} = \frac{2}{s^3}$$

# Desplazamiento en tiempo (traslación)

> [!teorema] Desplazamiento a la derecha
> $$\mathcal{L}\{f(t - a) u(t - a)\} = e^{-as} F(s), \quad a \ge 0$$

> [!demostracion]
> Por definición:
> $$\mathcal{L}\{f(t - a) u(t - a)\} = \int_0^\infty f(t - a) u(t - a) e^{-st} dt$$
> 
> Para $t < a$, $u(t-a)=0$. Para $t \ge a$, $u(t-a)=1$. Cambiando variable $\tau = t - a$:
> 
> $$\int_a^\infty f(t - a) e^{-st} dt = \int_0^\infty f(\tau) e^{-s(\tau + a)} d\tau = e^{-as} \int_0^\infty f(\tau) e^{-s\tau} d\tau = e^{-as} F(s)$$

> [!ejemplo]
> Pulso rectangular de altura $A$ y duración $T$:
> $$f(t) = A[u(t) - u(t - T)]$$
> 
> $$\mathcal{L}\{f(t)\} = A\left( \frac{1}{s} - \frac{e^{-Ts}}{s} \right) = \frac{A}{s}(1 - e^{-Ts})$$

# Desplazamiento en frecuencia (traslación en $s$)

> [!teorema] Desplazamiento en $s$
> $$\mathcal{L}\{e^{-at} f(t)\} = F(s + a)$$

> [!demostracion]
> $$\mathcal{L}\{e^{-at} f(t)\} = \int_0^\infty e^{-at} f(t) e^{-st} dt = \int_0^\infty f(t) e^{-(s+a)t} dt = F(s + a)$$

> [!ejemplo]
> Sabiendo $\mathcal{L}\{\cos(\omega t)\} = \frac{s}{s^2 + \omega^2}$:
> 
> $$\mathcal{L}\{e^{-at} \cos(\omega t)\} = \frac{s + a}{(s + a)^2 + \omega^2}$$

# Escalamiento en tiempo

> [!teorema] Escalamiento
> $$\mathcal{L}\{f(at)\} = \frac{1}{a} F\left(\frac{s}{a}\right), \quad a > 0$$

> [!demostracion]
> $$\mathcal{L}\{f(at)\} = \int_0^\infty f(at) e^{-st} dt$$
> 
> Cambiando variable $\tau = at$, $dt = d\tau / a$:
> 
> $$\int_0^\infty f(\tau) e^{-(s/a)\tau} \frac{d\tau}{a} = \frac{1}{a} \int_0^\infty f(\tau) e^{-(s/a)\tau} d\tau = \frac{1}{a} F\left(\frac{s}{a}\right)$$

> [!ejemplo]
> $f(t) = \sin(t)$, $F(s) = \frac{1}{s^2+1}$
> 
> $\mathcal{L}\{\sin(\omega t)\} = \frac{1}{\omega} \cdot \frac{1}{(s/\omega)^2 + 1} = \frac{\omega}{s^2 + \omega^2}$

# Multiplicación por $t^n$

> [!teorema] Multiplicación por $t$
> $$\mathcal{L}\{t f(t)\} = -\frac{dF(s)}{ds}$$

> [!teorema] Multiplicación por $t^n$
> $$\mathcal{L}\{t^n f(t)\} = (-1)^n \frac{d^n F(s)}{ds^n}$$

> [!demostracion] Para $n=1$
> $$\frac{dF(s)}{ds} = \frac{d}{ds} \int_0^\infty f(t) e^{-st} dt = \int_0^\infty f(t) \frac{\partial}{\partial s} e^{-st} dt = \int_0^\infty f(t) (-t) e^{-st} dt$$
> 
> $$= -\int_0^\infty t f(t) e^{-st} dt = -\mathcal{L}\{t f(t)\}$$
> 
> Por lo tanto $\mathcal{L}\{t f(t)\} = -F'(s)$.

> [!ejemplo]
> Sabiendo $\mathcal{L}\{1\} = 1/s$:
> 
> $\mathcal{L}\{t \cdot 1\} = -\frac{d}{ds}\left(\frac{1}{s}\right) = \frac{1}{s^2}$
> 
> $\mathcal{L}\{t^2\} = (-1)^2 \frac{d^2}{ds^2}\left(\frac{1}{s}\right) = \frac{d}{ds}\left(-\frac{1}{s^2}\right) = \frac{2}{s^3}$

# Teoremas del valor inicial y final

> [!teorema] Valor inicial
> $$f(0^+) = \lim_{s \to \infty} sF(s)$$

> [!teorema] Valor final
> Si todos los polos de $sF(s)$ tienen $\Re(s) < 0$ (excepto posible $s=0$ simple):
> $$\lim_{t \to \infty} f(t) = \lim_{s \to 0} sF(s)$$

> [!demostracion] Ver [[Teorema Valor Inicial Final]]

> [!ejemplo]
> $f(t) = 1 - e^{-t}$, $F(s) = \frac{1}{s(s+1)}$
> 
> Valor inicial: $\lim_{s \to \infty} s \cdot \frac{1}{s(s+1)} = \lim_{s \to \infty} \frac{1}{s+1} = 0$ ✓
> 
> Valor final: $\lim_{s \to 0} s \cdot \frac{1}{s(s+1)} = \lim_{s \to 0} \frac{1}{s+1} = 1$ ✓

# Convolución

> [!teorema] Teorema de convolución en tiempo
> $$\mathcal{L}\{(f * g)(t)\} = F(s) G(s)$$
> 
> donde $(f * g)(t) = \int_0^t f(\tau) g(t - \tau) d\tau$

> [!demostracion] Ver [[Convolucion]]

> [!ejemplo]
> Respuesta de un sistema $G(s) = \frac{1}{s+1}$ a entrada $u(t) = e^{-2t}$:
> 
> $Y(s) = \frac{1}{s+1} \cdot \frac{1}{s+2} = \frac{1}{s+1} - \frac{1}{s+2}$
> 
> $y(t) = e^{-t} - e^{-2t}$

# Resumen de propiedades

> [!info] Tabla resumen
> | Propiedad | $f(t)$ | $F(s)$ |
> |-----------|--------|--------|
> | Linealidad | $a f_1 + b f_2$ | $a F_1 + b F_2$ |
> | Derivada primera | $f'(t)$ | $sF(s) - f(0^-)$ |
> | Derivada segunda | $f''(t)$ | $s^2 F(s) - s f(0^-) - f'(0^-)$ |
> | Derivada $n$ | $f^{(n)}(t)$ | $s^n F(s) - \sum s^{n-k} f^{(k-1)}(0^-)$ |
> | Integral | $\int_0^t f(\tau) d\tau$ | $\frac{F(s)}{s}$ |
> | Desplazamiento temporal | $f(t - a)u(t - a)$ | $e^{-as} F(s)$ |
> | Desplazamiento frecuencial | $e^{-at} f(t)$ | $F(s + a)$ |
> | Escalamiento | $f(at)$ | $\frac{1}{a} F(s/a)$ |
> | Multiplicación por $t^n$ | $t^n f(t)$ | $(-1)^n F^{(n)}(s)$ |
> | Convolución | $(f * g)(t)$ | $F(s) G(s)$ |
> | Valor inicial | $f(0^+)$ | $\lim_{s \to \infty} sF(s)$ |
> | Valor final | $\lim_{t \to \infty} f(t)$ | $\lim_{s \to 0} sF(s)$ |

# Limitaciones

> [!warning]
> 1. Las propiedades de derivación requieren que $f(t)$ sea derivable a tramos
> 2. El teorema del valor final requiere estabilidad (polos de $sF(s)$ en semiplano izquierdo abierto)
> 3. El desplazamiento temporal requiere $a \ge 0$ (causalidad)