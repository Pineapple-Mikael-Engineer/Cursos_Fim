---
title: Transformada de Laplace
tags:
  - control-clasico
  - teoria
  - modelado
draft: false
aliases:
  - Laplace
  - transformada de Laplace
---

# Transformada de Laplace

# Definición

> [!definicion] Transformada de Laplace unilateral
> Dada una función $f(t)$ definida para $t \ge 0$, su transformada de Laplace es:
> $$F(s) = \mathcal{L}\{f(t)\} = \int_{0^-}^{\infty} f(t) e^{-st} dt$$
> 
> donde $s = \sigma + j\omega$ es una variable compleja.

> [!definicion] Transformada inversa
> $$f(t) = \mathcal{L}^{-1}\{F(s)\} = \frac{1}{2\pi j} \int_{\sigma - j\infty}^{\sigma + j\infty} F(s) e^{st} ds$$
> 
> En la práctica se usa [[Tabla Pares | tabla de pares]] + [[Propiedades | propiedades]].

# Condiciones de existencia

> [!info] Condiciones suficientes
> - $f(t)$ es continua por tramos en $[0, \infty)$
> - Existen constantes $M > 0$ y $\sigma_0$ tales que $|f(t)| \le M e^{\sigma_0 t}$ para todo $t \ge 0$
> 
> La integral converge para $\Re(s) > \sigma_0$ (región de convergencia).

# Por qué es útil en control

> [!info] Ventajas
> 1. **Convierte EDOs en ecuaciones algebraicas**: la derivación se vuelve multiplicación por $s$
> 2. **Condiciones iniciales**: se incorporan automáticamente (versión unilateral)
> 3. **Convolución** en tiempo se convierte en **producto** en $s$
> 4. **Sistemas LTI**: $Y(s) = G(s) U(s)$

> [!ejemplo] EDO a ecuación algebraica
> Dada $\dot{y} + 2y = u$, con $y(0)=y_0$:
> 
> $$\mathcal{L}\{\dot{y}\} = sY(s) - y_0$$
> 
> La ecuación se transforma en:
> $$sY(s) - y_0 + 2Y(s) = U(s)$$
> $$(s+2)Y(s) = U(s) + y_0$$
> 
> Despejando $Y(s)$:
> $$Y(s) = \frac{U(s)}{s+2} + \frac{y_0}{s+2}$$

# Transformadas básicas

> [!definicion] Tabla de pares fundamentales
> | $f(t)$ para $t \ge 0$ | $F(s)$ | Región de convergencia |
> |----------------------|--------|----------------------|
> | $\delta(t)$ | $1$ | todo $s$ |
> | $u(t)$ (escalón) | $\frac{1}{s}$ | $\Re(s) > 0$ |
> | $t$ | $\frac{1}{s^2}$ | $\Re(s) > 0$ |
> | $t^n$ | $\frac{n!}{s^{n+1}}$ | $\Re(s) > 0$ |
> | $e^{-at}$ | $\frac{1}{s+a}$ | $\Re(s) > -a$ |
> | $t e^{-at}$ | $\frac{1}{(s+a)^2}$ | $\Re(s) > -a$ |
> | $\sin(\omega t)$ | $\frac{\omega}{s^2 + \omega^2}$ | $\Re(s) > 0$ |
> | $\cos(\omega t)$ | $\frac{s}{s^2 + \omega^2}$ | $\Re(s) > 0$ |
> | $e^{-at} \sin(\omega t)$ | $\frac{\omega}{(s+a)^2 + \omega^2}$ | $\Re(s) > -a$ |
> | $e^{-at} \cos(\omega t)$ | $\frac{s+a}{(s+a)^2 + \omega^2}$ | $\Re(s) > -a$ |
> 
> Ver [[Tabla Pares]] para versión extendida.

# Propiedades fundamentales

> [!info] Propiedades operativas
> | Propiedad | Tiempo $f(t)$ | Laplace $F(s)$ |
> |-----------|---------------|----------------|
> | Linealidad | $a f_1(t) + b f_2(t)$ | $a F_1(s) + b F_2(s)$ |
> | Derivación | $f'(t)$ | $sF(s) - f(0^-)$ |
> | Derivación segunda | $f''(t)$ | $s^2 F(s) - s f(0^-) - f'(0^-)$ |
> | Derivación orden $n$ | $f^{(n)}(t)$ | $s^n F(s) - \sum_{k=1}^n s^{n-k} f^{(k-1)}(0^-)$ |
> | Integración | $\int_0^t f(\tau) d\tau$ | $\frac{1}{s} F(s)$ |
> | Desplazamiento en $t$ | $f(t-a) u(t-a)$ | $e^{-as} F(s)$ |
> | Desplazamiento en $s$ | $e^{-at} f(t)$ | $F(s+a)$ |
> | Escalamiento | $f(at)$ | $\frac{1}{a} F\left(\frac{s}{a}\right)$ |
> | [[Convolucion \| Convolución]] | $(f * g)(t) = \int_0^t f(\tau) g(t-\tau) d\tau$ | $F(s) G(s)$ |
> | Teorema valor inicial | $f(0^+)$ | $\lim_{s \to \infty} sF(s)$ |
> | Teorema valor final | $\lim_{t \to \infty} f(t)$ | $\lim_{s \to 0} sF(s)$ |
> 
> Ver [[Propiedades]] para demostraciones y ejemplos.

# Relación con función transferencia

> [!info] Función transferencia desde Laplace
> Para un sistema LTI con CI nulas:
> $$G(s) = \frac{\mathcal{L}\{\text{salida}\}}{\mathcal{L}\{\text{entrada}\}}$$
> 
> Ver [[Funcion Transferencia/index | función transferencia]].

# Limitaciones

> [!warning]
> 1. Solo aplica a señales definidas para $t \ge 0$ (unilateral)
> 2. Requiere que la integral converja (señales de orden exponencial)
> 3. No aplica directamente a sistemas no lineales o variantes en el tiempo