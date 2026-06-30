---
title: Propiedades de la TL
order: 2
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

> [!definicion]
> Reglas operativas de la [[index | transformada de Laplace]] que permiten transformar combinaciones, derivadas, integrales, retardos y productos sin recurrir a la integral de definición. La más explotada en control es la **derivación**, $\mathcal{L}\{f'\}=sF(s)-f(0^-)$, que convierte EDOs en álgebra incluyendo las condiciones iniciales.

> [!info] Tabla de propiedades
> | Propiedad | $f(t)$ | $F(s)$ |
> |---|---|---|
> | Linealidad | $a f_1+b f_2$ | $a F_1+b F_2$ |
> | Derivada 1.ª | $f'(t)$ | $sF(s)-f(0^-)$ |
> | Derivada 2.ª | $f''(t)$ | $s^2F(s)-sf(0^-)-f'(0^-)$ |
> | Derivada $n$ | $f^{(n)}(t)$ | $s^nF(s)-\sum_{k=1}^n s^{n-k}f^{(k-1)}(0^-)$ |
> | Integración | $\int_0^t f(\tau)\,d\tau$ | $\dfrac{F(s)}{s}$ |
> | Retardo en $t$ | $f(t-a)u(t-a)$ | $e^{-as}F(s)$ |
> | Traslación en $s$ | $e^{-at}f(t)$ | $F(s+a)$ |
> | Escalamiento | $f(at)$ | $\dfrac{1}{a}F\!\left(\dfrac{s}{a}\right)$ |
> | Mult. por $t^n$ | $t^n f(t)$ | $(-1)^n F^{(n)}(s)$ |
> | [[Convolucion \| Convolución]] | $(f*g)(t)$ | $F(s)\,G(s)$ |
> | Valor inicial | $f(0^+)$ | $\lim_{s\to\infty}sF(s)$ |
> | Valor final | $\lim_{t\to\infty}f(t)$ | $\lim_{s\to0}sF(s)$ |

---

## Ejemplo

> [!ejemplo] EDO con condiciones iniciales no nulas
> Resolver $\ddot{y}+3\dot{y}+2y=u(t)$ con $y(0)=1$, $\dot{y}(0)=0$.
>
> **Paso 1 — Transformar** usando derivada 1.ª y 2.ª (las CI entran solas):
> $$\bigl[s^2Y-s\,y(0)-\dot y(0)\bigr]+3\bigl[sY-y(0)\bigr]+2Y=\frac{1}{s}.$$
>
> **Paso 2 — Sustituir CI y agrupar:**
> $$s^2Y-s+3sY-3+2Y=\frac{1}{s}\;\Longrightarrow\;(s^2+3s+2)Y=\frac{1}{s}+s+3.$$
>
> **Paso 3 — Despejar $Y(s)$:**
> $$Y(s)=\frac{s^3+3s^2+1}{s(s+1)(s+2)}.$$
> Listo para antitransformar por [[Tabla Pares | fracciones parciales]]: los polos $s=0,-1,-2$ dan los términos constante, $e^{-t}$ y $e^{-2t}$.

---

## Demostraciones

> [!teorema] Linealidad
> $$\mathcal{L}\{a f_1+b f_2\}=aF_1(s)+bF_2(s).$$

> [!demostracion]
> Por linealidad de la integral:
> $$\int_0^\infty[af_1+bf_2]e^{-st}dt=a\int_0^\infty f_1 e^{-st}dt+b\int_0^\infty f_2 e^{-st}dt=aF_1+bF_2.$$

> [!ejemplo]
> $f(t)=3e^{-2t}+5\sin(4t)\Rightarrow F(s)=\dfrac{3}{s+2}+\dfrac{20}{s^2+16}$.

> [!teorema] Derivación en tiempo
> $$\mathcal{L}\{f'(t)\}=sF(s)-f(0^-),\qquad \mathcal{L}\{f''(t)\}=s^2F(s)-sf(0^-)-f'(0^-).$$

> [!demostracion]
> Integrando por partes ($u=e^{-st}$, $dv=f'(t)dt$):
> $$\int_0^\infty f'e^{-st}dt=\bigl[f(t)e^{-st}\bigr]_0^\infty+s\int_0^\infty f e^{-st}dt=-f(0^-)+sF(s),$$
> donde el término evaluado se anula en $\infty$ para $\Re(s)$ grande. La segunda derivada se obtiene aplicando la regla dos veces:
> $$\mathcal{L}\{f''\}=s\mathcal{L}\{f'\}-f'(0^-)=s^2F(s)-sf(0^-)-f'(0^-).$$
> El caso general $\mathcal{L}\{f^{(n)}\}=s^nF(s)-\sum_{k=1}^n s^{n-k}f^{(k-1)}(0^-)$ sale por inducción.

> [!teorema] Integración en tiempo
> $$\mathcal{L}\left\{\int_0^t f(\tau)\,d\tau\right\}=\frac{F(s)}{s}.$$

> [!demostracion]
> Sea $g(t)=\int_0^t f\,d\tau$, con $g'(t)=f(t)$ y $g(0)=0$. Por la derivada, $\mathcal{L}\{g'\}=sG(s)-g(0)=sG(s)$. Pero $\mathcal{L}\{g'\}=F(s)$, luego $G(s)=F(s)/s$.

> [!ejemplo]
> Como $t^2=\int_0^t 2\tau\,d\tau$ y $\mathcal{L}\{2t\}=2/s^2$: $\;\mathcal{L}\{t^2\}=\dfrac{1}{s}\cdot\dfrac{2}{s^2}=\dfrac{2}{s^3}$.

> [!teorema] Desplazamiento en tiempo (retardo)
> $$\mathcal{L}\{f(t-a)u(t-a)\}=e^{-as}F(s),\qquad a\ge0.$$

> [!demostracion]
> Con $u(t-a)$ recortando la integral a $[a,\infty)$ y el cambio $\tau=t-a$:
> $$\int_a^\infty f(t-a)e^{-st}dt=\int_0^\infty f(\tau)e^{-s(\tau+a)}d\tau=e^{-as}F(s).$$

> [!ejemplo]
> Pulso de altura $A$ y duración $T$: $f(t)=A[u(t)-u(t-T)]$:
> $$F(s)=A\left(\frac{1}{s}-\frac{e^{-Ts}}{s}\right)=\frac{A}{s}\bigl(1-e^{-Ts}\bigr).$$

> [!teorema] Desplazamiento en frecuencia
> $$\mathcal{L}\{e^{-at}f(t)\}=F(s+a).$$

> [!demostracion]
> $$\int_0^\infty e^{-at}f(t)e^{-st}dt=\int_0^\infty f(t)e^{-(s+a)t}dt=F(s+a).$$

> [!ejemplo]
> Con $\mathcal{L}\{\cos\omega t\}=\dfrac{s}{s^2+\omega^2}$: $\;\mathcal{L}\{e^{-at}\cos\omega t\}=\dfrac{s+a}{(s+a)^2+\omega^2}$.

> [!teorema] Escalamiento en tiempo
> $$\mathcal{L}\{f(at)\}=\frac{1}{a}F\!\left(\frac{s}{a}\right),\qquad a>0.$$

> [!demostracion]
> Cambio $\tau=at$, $dt=d\tau/a$:
> $$\int_0^\infty f(at)e^{-st}dt=\frac{1}{a}\int_0^\infty f(\tau)e^{-(s/a)\tau}d\tau=\frac{1}{a}F\!\left(\frac{s}{a}\right).$$

> [!teorema] Multiplicación por $t^n$
> $$\mathcal{L}\{t^n f(t)\}=(-1)^n\frac{d^n F(s)}{ds^n}.$$

> [!demostracion]
> Para $n=1$, derivando bajo el signo integral:
> $$\frac{dF}{ds}=\int_0^\infty f(t)\frac{\partial}{\partial s}e^{-st}dt=-\int_0^\infty t f(t)e^{-st}dt=-\mathcal{L}\{tf(t)\}.$$

> [!ejemplo]
> $\mathcal{L}\{t\cdot1\}=-\dfrac{d}{ds}\dfrac{1}{s}=\dfrac{1}{s^2}$; $\;\mathcal{L}\{t^2\}=\dfrac{d^2}{ds^2}\dfrac{1}{s}=\dfrac{2}{s^3}$.

> [!teorema] Valor inicial y valor final
> $$f(0^+)=\lim_{s\to\infty}sF(s),\qquad \lim_{t\to\infty}f(t)=\lim_{s\to0}sF(s).$$
> El valor final solo es válido si todos los polos de $sF(s)$ tienen $\Re(s)<0$ (se permite un polo simple en $s=0$).

> [!demostracion] Detalle en [[Teorema Valor Inicial Final | teoremas de valor inicial y final]].

> [!ejemplo]
> $f(t)=1-e^{-t}$, $F(s)=\dfrac{1}{s(s+1)}$:
> $$\text{inicial}=\lim_{s\to\infty}\frac{1}{s+1}=0\;\checkmark,\qquad \text{final}=\lim_{s\to0}\frac{1}{s+1}=1\;\checkmark.$$

> [!teorema] Convolución
> $$\mathcal{L}\{(f*g)(t)\}=F(s)G(s),\qquad (f*g)(t)=\int_0^t f(\tau)g(t-\tau)\,d\tau.$$

> [!demostracion] Desarrollo completo en [[Convolucion | convolución]].

> [!ejemplo]
> Respuesta de $G(s)=\dfrac{1}{s+1}$ a $u(t)=e^{-2t}$:
> $$Y(s)=\frac{1}{(s+1)(s+2)}=\frac{1}{s+1}-\frac{1}{s+2}\;\Longrightarrow\;y(t)=e^{-t}-e^{-2t}.$$

---

## Limitaciones

> [!warning]
> 1. La derivación requiere que $f(t)$ sea derivable a tramos.
> 2. El teorema del valor final exige estabilidad: polos de $sF(s)$ en el semiplano izquierdo abierto (un polo simple en $0$ admitido); si no, da resultados falsos.
> 3. El retardo $f(t-a)u(t-a)$ requiere $a\ge0$ (causalidad).

## Resumen

> [!resumen]
> | Operación en $t$ | Se vuelve en $s$ |
> |---|---|
> | Sumar / escalar | Sumar / escalar |
> | Derivar | $\times s$ (menos CI) |
> | Integrar | $\div s$ |
> | Retardar $a$ | $\times e^{-as}$ |
> | Modular por $e^{-at}$ | $s\to s+a$ |
> | Convolucionar | Multiplicar |

> [!corolario]
> Cada operación temporal complicada tiene una contraparte algebraica simple en $s$: derivar es multiplicar por $s$, integrar es dividir, retardar es multiplicar por $e^{-as}$ y convolucionar es multiplicar. Esto es lo que hace de Laplace la herramienta natural para resolver EDOs y analizar sistemas LTI. Los teoremas de valor inicial/final dan, además, los extremos de $y(t)$ sin antitransformar.

> [!referencia]
> - Marco general: [[index]].
> - Pares para identificar las antitransformadas: [[Tabla Pares]].
> - Convolución en detalle: [[Convolucion]].
> - Valor inicial/final: [[Teorema Valor Inicial Final]].
