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

> [!definicion]
> Tabla de referencia de pares $f(t)\leftrightarrow F(s)$ de la [[index | transformada de Laplace]] unilateral ($t\ge0$). Para antitransformar $F(s)$: descomponer en fracciones parciales y reconocer cada término en la tabla. ROC = región de convergencia.

> [!info] Pares completos
> | $f(t)$, $t\ge0$ | $F(s)$ | ROC |
> |---|---|---|
> | $\delta(t)$ (impulso) | $1$ | todo $s$ |
> | $\delta^{(n)}(t)$ | $s^n$ | todo $s$ |
> | $u(t)$ (escalón) | $\dfrac{1}{s}$ | $\Re(s)>0$ |
> | $t$ | $\dfrac{1}{s^2}$ | $\Re(s)>0$ |
> | $t^n$ | $\dfrac{n!}{s^{n+1}}$ | $\Re(s)>0$ |
> | $e^{-at}$ | $\dfrac{1}{s+a}$ | $\Re(s)>-a$ |
> | $t^n e^{-at}$ | $\dfrac{n!}{(s+a)^{n+1}}$ | $\Re(s)>-a$ |
> | $1-e^{-at}$ | $\dfrac{a}{s(s+a)}$ | $\Re(s)>0$ |
> | $\sin(\omega t)$ | $\dfrac{\omega}{s^2+\omega^2}$ | $\Re(s)>0$ |
> | $\cos(\omega t)$ | $\dfrac{s}{s^2+\omega^2}$ | $\Re(s)>0$ |
> | $e^{-at}\sin(\omega t)$ | $\dfrac{\omega}{(s+a)^2+\omega^2}$ | $\Re(s)>-a$ |
> | $e^{-at}\cos(\omega t)$ | $\dfrac{s+a}{(s+a)^2+\omega^2}$ | $\Re(s)>-a$ |
> | $\sinh(at)$ | $\dfrac{a}{s^2-a^2}$ | $\Re(s)>\lvert a\rvert$ |
> | $\cosh(at)$ | $\dfrac{s}{s^2-a^2}$ | $\Re(s)>\lvert a\rvert$ |
> | $f(t-a)\,u(t-a)$ | $e^{-as}F(s)$ | (retardo) |
> | $\delta(t-a)$ | $e^{-as}$ | todo $s$ |
> | $u(t-a)$ | $\dfrac{e^{-as}}{s}$ | $\Re(s)>0$ |

> [!info] FT → respuesta impulsional (atajo en control)
> | $G(s)$ | $g(t)=\mathcal{L}^{-1}\{G\}$ |
> |---|---|
> | $\dfrac{K}{\tau s+1}$ | $\dfrac{K}{\tau}e^{-t/\tau}$ |
> | $\dfrac{K\omega_n^2}{s^2+2\zeta\omega_n s+\omega_n^2}$ | $\dfrac{K\omega_n}{\sqrt{1-\zeta^2}}e^{-\zeta\omega_n t}\sin(\omega_d t)$ |
> | $\dfrac{K}{s}$ | $K\,u(t)$ |
> | $\dfrac{K}{s^2}$ | $K\,t$ |
> | $\dfrac{K}{s(s+a)}$ | $\dfrac{K}{a}(1-e^{-at})$ |

---

## Ejemplos de uso

> [!ejemplo] Fracciones parciales — raíces reales distintas
> Hallar $f(t)$ para $F(s)=\dfrac{3s+5}{(s+1)(s+2)}$.
>
> **Paso 1 — Expandir:**
> $$\frac{3s+5}{(s+1)(s+2)}=\frac{A}{s+1}+\frac{B}{s+2}.$$
>
> **Paso 2 — Residuos** (tapar el factor y evaluar en su raíz):
> $$A=\left.\frac{3s+5}{s+2}\right|_{s=-1}=\frac{2}{1}=2,\qquad B=\left.\frac{3s+5}{s+1}\right|_{s=-2}=\frac{-1}{-1}=1.$$
>
> **Paso 3 — Identificar en tabla** ($1/(s+a)\leftrightarrow e^{-at}$):
> $$f(t)=2e^{-t}+e^{-2t},\qquad t\ge0.$$

> [!ejemplo] Fracciones parciales — par complejo conjugado
> Hallar $f(t)$ para $F(s)=\dfrac{2s+3}{s^2+2s+5}$.
>
> **Paso 1 — Completar el cuadrado:** $s^2+2s+5=(s+1)^2+2^2$.
>
> **Paso 2 — Acomodar el numerador** al patrón $s+a$ con $a=1$:
> $$2s+3=2(s+1)+1.$$
>
> **Paso 3 — Separar** en los dos pares de la tabla:
> $$F(s)=\underbrace{\frac{2(s+1)}{(s+1)^2+2^2}}_{\to\,e^{-t}\cos2t}+\underbrace{\frac{1}{(s+1)^2+2^2}}_{\to\,\frac12 e^{-t}\sin2t}.$$
>
> **Paso 4 — Antitransformar** ($a=1$, $\omega=2$):
> $$f(t)=2e^{-t}\cos(2t)+\tfrac{1}{2}e^{-t}\sin(2t),\qquad t\ge0.$$

> [!ejemplo] Fracciones parciales — raíz repetida
> Hallar $f(t)$ para $F(s)=\dfrac{1}{(s+1)^2(s+2)}$.
>
> **Paso 1 — Expandir** (la raíz doble aporta dos términos):
> $$\frac{1}{(s+1)^2(s+2)}=\frac{A}{s+1}+\frac{B}{(s+1)^2}+\frac{C}{s+2}.$$
>
> **Paso 2 — Coeficientes:**
> $$B=\left.\frac{1}{s+2}\right|_{s=-1}=1,\qquad C=\left.\frac{1}{(s+1)^2}\right|_{s=-2}=1.$$
> $A$ evaluando en $s=0$: $\tfrac{1}{2}=A+1+\tfrac{1}{2}\Rightarrow A=-1$.
>
> **Paso 3 — Identificar** ($1/(s+1)^2\leftrightarrow t e^{-t}$):
> $$f(t)=-e^{-t}+t\,e^{-t}+e^{-2t},\qquad t\ge0.$$

---

## Demostración de pares clave

> [!teorema] $\mathcal{L}\{e^{-at}\}=\dfrac{1}{s+a}$ para $\Re(s)>-a$

> [!demostracion]
> Por definición:
> $$F(s)=\int_0^\infty e^{-at}e^{-st}\,dt=\int_0^\infty e^{-(s+a)t}\,dt=\left[\frac{e^{-(s+a)t}}{-(s+a)}\right]_0^\infty.$$
> Para $\Re(s+a)>0$ el límite superior se anula:
> $$F(s)=0-\frac{1}{-(s+a)}=\frac{1}{s+a}.$$

> [!teorema] $\mathcal{L}\{t^n\}=\dfrac{n!}{s^{n+1}}$ para $\Re(s)>0$

> [!demostracion]
> Para $n=1$, integración por partes ($u=t$, $dv=e^{-st}dt$):
> $$\int_0^\infty t e^{-st}\,dt=\left[-\frac{t}{s}e^{-st}\right]_0^\infty+\frac{1}{s}\int_0^\infty e^{-st}\,dt=0+\frac{1}{s}\cdot\frac{1}{s}=\frac{1}{s^2}.$$
> Para $n$ general, por inducción (o función gamma): $\mathcal{L}\{t^n\}=\dfrac{\Gamma(n+1)}{s^{n+1}}=\dfrac{n!}{s^{n+1}}$.

> [!teorema] $\mathcal{L}\{\sin(\omega t)\}=\dfrac{\omega}{s^2+\omega^2}$ para $\Re(s)>0$

> [!demostracion]
> Con $\sin(\omega t)=\dfrac{e^{j\omega t}-e^{-j\omega t}}{2j}$ y el par exponencial:
> $$\mathcal{L}\{\sin(\omega t)\}=\frac{1}{2j}\left(\frac{1}{s-j\omega}-\frac{1}{s+j\omega}\right)=\frac{1}{2j}\cdot\frac{2j\omega}{s^2+\omega^2}=\frac{\omega}{s^2+\omega^2}.$$

---

## Limitaciones

> [!warning]
> 1. Las inversas por tabla asumen **CI nulas**; con condiciones iniciales no nulas, usar las [[Propiedades | propiedades de derivación]].
> 2. La tabla no cubre todo: para productos y retardos combinar con [[Propiedades | propiedades]] y [[Convolucion | convolución]].

## Resumen

> [!resumen]
> | Familia | Patrón en $s$ | Antitransformada |
> |---|---|---|
> | Polo real | $\dfrac{1}{s+a}$ | $e^{-at}$ |
> | Polo real doble | $\dfrac{1}{(s+a)^2}$ | $t\,e^{-at}$ |
> | Par imaginario | $\dfrac{\omega}{s^2+\omega^2}$ | $\sin\omega t$ |
> | Par complejo | $\dfrac{\omega}{(s+a)^2+\omega^2}$ | $e^{-at}\sin\omega t$ |
> | Integrador | $\dfrac{1}{s}$ | $u(t)$ |
> | Retardo | $e^{-as}F(s)$ | $f(t-a)u(t-a)$ |

> [!corolario]
> Antitransformar es un proceso mecánico: factorizar el denominador, descomponer en fracciones parciales y leer cada término en la tabla. La estructura de los polos (real, repetido, complejo) fija la familia de funciones temporales; la posición $-a$ del polo fija la rapidez de decaimiento. Para casos fuera de tabla, recurrir a [[Propiedades]] y [[Convolucion]].

> [!referencia]
> - Marco general: [[index]].
> - Propiedades para transformar derivadas, retardos y productos: [[Propiedades]].
> - Inversa de un producto $F(s)G(s)$: [[Convolucion]].
