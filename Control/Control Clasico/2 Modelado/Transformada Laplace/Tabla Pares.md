---
title: Tabla de Pares de TL
tags:
  - control-clasico
  - teoria
  - transformada-laplace
draft: false
aliases:
  - tabla laplace
  - pares laplace
---

# Tabla de Pares de Transformada de Laplace

# Transformadas básicas

> [!definicion] Funciones elementales
> | $f(t)$ para $t \ge 0$ | $F(s)$ | ROC |
> |----------------------|--------|-----|
> | $\delta(t)$ (impulso) | $1$ | todo $s$ |
> | $\delta^{(n)}(t)$ | $s^n$ | todo $s$ |
> | $u(t)$ (escalón) | $\frac{1}{s}$ | $\Re(s) > 0$ |
> | $t$ | $\frac{1}{s^2}$ | $\Re(s) > 0$ |
> | $t^n$ | $\frac{n!}{s^{n+1}}$ | $\Re(s) > 0$ |
> | $t^n e^{-at}$ | $\frac{n!}{(s+a)^{n+1}}$ | $\Re(s) > -a$ |

# Exponenciales y trigonométricas

> [!definicion] Funciones exponenciales y oscilatorias
> | $f(t)$ para $t \ge 0$ | $F(s)$ | ROC |
> |----------------------|--------|-----|
> | $e^{-at}$ | $\frac{1}{s+a}$ | $\Re(s) > -a$ |
> | $1 - e^{-at}$ | $\frac{a}{s(s+a)}$ | $\Re(s) > 0$ |
> | $\sin(\omega t)$ | $\frac{\omega}{s^2 + \omega^2}$ | $\Re(s) > 0$ |
> | $\cos(\omega t)$ | $\frac{s}{s^2 + \omega^2}$ | $\Re(s) > 0$ |
> | $e^{-at} \sin(\omega t)$ | $\frac{\omega}{(s+a)^2 + \omega^2}$ | $\Re(s) > -a$ |
> | $e^{-at} \cos(\omega t)$ | $\frac{s+a}{(s+a)^2 + \omega^2}$ | $\Re(s) > -a$ |
> | $\sinh(at)$ | $\frac{a}{s^2 - a^2}$ | $\Re(s) > \|a\|$ |
> | $\cosh(at)$ | $\frac{s}{s^2 - a^2}$ | $\Re(s) > \|a\|$ |

# Funciones con desplazamiento

> [!definicion] Desplazamiento temporal
> | $f(t)$ para $t \ge 0$ | $F(s)$ |
> |----------------------|--------|
> | $f(t - a) u(t - a)$ | $e^{-as} F(s)$ |
> | $\delta(t - a)$ | $e^{-as}$ |
> | $u(t - a)$ | $\frac{e^{-as}}{s}$ |

# Ejemplos de uso

> [!ejemplo] Fracciones parciales – caso reales distintos
> Encontrar $f(t)$ para $F(s) = \frac{3s+5}{(s+1)(s+2)}$.
> 
> **Paso 1:** Expandir en fracciones parciales:
> $$\frac{3s+5}{(s+1)(s+2)} = \frac{A}{s+1} + \frac{B}{s+2}$$
> 
> $A = \left. \frac{3s+5}{s+2} \right|_{s=-1} = \frac{-3+5}{1} = 2$
> 
> $B = \left. \frac{3s+5}{s+1} \right|_{s=-2} = \frac{-6+5}{-1} = 1$
> 
> **Paso 2:** Identificar en tabla:
> $$F(s) = \frac{2}{s+1} + \frac{1}{s+2}$$
> 
> **Paso 3:** Aplicar transformada inversa:
> $$f(t) = 2e^{-t} + e^{-2t}, \quad t \ge 0$$

> [!ejemplo] Fracciones parciales – par complejo conjugado
> Encontrar $f(t)$ para $F(s) = \frac{2s+3}{s^2 + 2s + 5}$.
> 
> **Paso 1:** Completar el cuadrado en el denominador:
> $$s^2 + 2s + 5 = (s+1)^2 + 4$$
> 
> **Paso 2:** Reescribir el numerador:
> $$2s+3 = 2(s+1) + 1$$
> 
> **Paso 3:** Separar:
> $$F(s) = \frac{2(s+1)}{(s+1)^2 + 2^2} + \frac{1}{(s+1)^2 + 2^2}$$
> 
> **Paso 4:** Identificar en tabla:
> $$\frac{s+a}{(s+a)^2 + \omega^2} \leftrightarrow e^{-at} \cos(\omega t)$$
> $$\frac{\omega}{(s+a)^2 + \omega^2} \leftrightarrow e^{-at} \sin(\omega t)$$
> 
> Con $a = 1$, $\omega = 2$:
> $$f(t) = 2e^{-t} \cos(2t) + \frac{1}{2} e^{-t} \sin(2t), \quad t \ge 0$$

> [!ejemplo] Fracciones parciales – raíces repetidas
> Encontrar $f(t)$ para $F(s) = \frac{1}{(s+1)^2(s+2)}$.
> 
> **Paso 1:** Expansión:
> $$\frac{1}{(s+1)^2(s+2)} = \frac{A}{s+1} + \frac{B}{(s+1)^2} + \frac{C}{s+2}$$
> 
> **Paso 2:** Calcular coeficientes:
> $B = \left. \frac{1}{s+2} \right|_{s=-1} = 1$
> 
> $C = \left. \frac{1}{(s+1)^2} \right|_{s=-2} = 1$
> 
> $A$ se obtiene evaluando en un punto (ej. $s=0$):
> $$\frac{1}{2} = A + 1 + \frac{1}{2} \implies A = -1$
> 
> **Paso 3:** Identificar en tabla:
> $$\frac{1}{(s+1)^2} \leftrightarrow t e^{-t}$$
> $$\frac{1}{s+1} \leftrightarrow e^{-t}$$
> $$\frac{1}{s+2} \leftrightarrow e^{-2t}$$
> 
> **Paso 4:** Resultado:
> $$f(t) = -e^{-t} + t e^{-t} + e^{-2t}, \quad t \ge 0$$

# Demostración de transformadas clave

> [!teorema] $\mathcal{L}\{e^{-at}\} = \frac{1}{s+a}$ para $\Re(s) > -a$

> [!demostracion]
> Por definición:
> $$F(s) = \int_0^\infty e^{-at} e^{-st} dt = \int_0^\infty e^{-(s+a)t} dt$$
> 
> $$\int_0^\infty e^{-(s+a)t} dt = \left[ \frac{e^{-(s+a)t}}{-(s+a)} \right]_0^\infty$$
> 
> Para $\Re(s+a) > 0$ (i.e., $\Re(s) > -a$), $e^{-(s+a)\infty} = 0$:
> $$F(s) = 0 - \frac{1}{-(s+a)} = \frac{1}{s+a}$$

> [!teorema] $\mathcal{L}\{t^n\} = \frac{n!}{s^{n+1}}$, $\Re(s) > 0$

> [!demostracion]
> Por definición para $n=1$:
> $$\mathcal{L}\{t\} = \int_0^\infty t e^{-st} dt$$
> 
> Integración por partes: $u = t$, $dv = e^{-st} dt$, $du = dt$, $v = -\frac{1}{s} e^{-st}$:
> $$\int_0^\infty t e^{-st} dt = \left[ -\frac{t}{s} e^{-st} \right]_0^\infty + \frac{1}{s} \int_0^\infty e^{-st} dt$$
> 
> El término evaluado vale $0$ para $\Re(s) > 0$. La integral restante es $\frac{1}{s} \cdot \frac{1}{s} = \frac{1}{s^2}$.
> 
> Para $n$ general, inducción o función gamma: $\mathcal{L}\{t^n\} = \frac{\Gamma(n+1)}{s^{n+1}} = \frac{n!}{s^{n+1}}$.

> [!teorema] $\mathcal{L}\{\sin(\omega t)\} = \frac{\omega}{s^2 + \omega^2}$, $\Re(s) > 0$

> [!demostracion]
> Usando identidad exponencial: $\sin(\omega t) = \frac{e^{j\omega t} - e^{-j\omega t}}{2j}$.
> 
> $$\mathcal{L}\{\sin(\omega t)\} = \frac{1}{2j} \left( \frac{1}{s - j\omega} - \frac{1}{s + j\omega} \right)$$
> 
> $$\frac{1}{2j} \cdot \frac{(s + j\omega) - (s - j\omega)}{(s - j\omega)(s + j\omega)} = \frac{1}{2j} \cdot \frac{2j\omega}{s^2 + \omega^2} = \frac{\omega}{s^2 + \omega^2}$$

# Regla práctica: pares útiles en control

> [!info] Función transferencia → respuesta temporal
> | $G(s)$ | $g(t)$ (respuesta impulsional) |
> |--------|-------------------------------|
> | $\frac{K}{\tau s + 1}$ | $\frac{K}{\tau} e^{-t/\tau}$ |
> | $\frac{K\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$ | $\frac{K\omega_n}{\sqrt{1-\zeta^2}} e^{-\zeta\omega_n t} \sin(\omega_d t)$ |
> | $\frac{K}{s}$ | $K u(t)$ |
> | $\frac{K}{s^2}$ | $K t$ |
> | $\frac{K}{s(s+a)}$ | $\frac{K}{a}(1 - e^{-at})$ |

# Limitaciones

> [!warning]
> 1. Las transformadas inversas por tabla asumen condiciones iniciales nulas. Si no, usar propiedades de derivación.
> 2. La tabla no cubre todos los casos; usar [[Propiedades]] y [[Convolucion]] para extender.