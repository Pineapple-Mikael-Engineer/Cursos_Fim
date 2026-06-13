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

> [!definicion]
> La convolución de dos señales causales es $(f*g)(t)=\int_0^t f(\tau)g(t-\tau)\,d\tau$. El **teorema de convolución** dice que se vuelve un producto en Laplace:
> $$\mathcal{L}\{(f*g)(t)\}=F(s)\,G(s).$$
> Por eso un sistema LTI con respuesta impulsional $g(t)$ y entrada $u(t)$ da $y=g*u$ en el tiempo y, equivalentemente, $Y(s)=G(s)U(s)$ en $s$ — la base de la [[Funcion Transferencia/index | función de transferencia]].

> [!info]
> Es la propiedad de la [[index | transformada de Laplace]] que justifica el producto $G(s)U(s)$. Convolucionar a mano es costoso; lo habitual es pasar a $s$, multiplicar y antitransformar con la [[Tabla Pares | tabla de pares]]. Ver también [[Propiedades | propiedades]].

---

## Ejemplo

> [!ejemplo] Convolución vs. producto en $s$
> Calcular $y=f*g$ con $f(t)=e^{-t}$, $g(t)=e^{-2t}$, por los dos caminos.
>
> **Camino 1 — Integral de convolución:**
> $$y(t)=\int_0^t e^{-\tau}e^{-2(t-\tau)}\,d\tau=e^{-2t}\int_0^t e^{\tau}\,d\tau=e^{-2t}(e^{t}-1)=e^{-t}-e^{-2t}.$$
>
> **Camino 2 — Producto en Laplace** ($F=\tfrac{1}{s+1}$, $G=\tfrac{1}{s+2}$):
> $$Y(s)=\frac{1}{(s+1)(s+2)}=\frac{1}{s+1}-\frac{1}{s+2}\;\Longrightarrow\;y(t)=e^{-t}-e^{-2t}.$$
>
> Ambos coinciden: el camino en $s$ evita la integral. Esta es la razón práctica del teorema.

---

## Demostración del teorema

> [!teorema] Teorema de convolución
> $$\mathcal{L}\{(f*g)(t)\}=F(s)\,G(s).$$

> [!demostracion]
> Partir de la definición y meter la convolución en la integral de Laplace:
> $$\mathcal{L}\{(f*g)(t)\}=\int_0^\infty\!\left[\int_0^t f(\tau)g(t-\tau)\,d\tau\right]e^{-st}\,dt.$$
>
> **Paso 1 — Invertir el orden** sobre la región $0\le\tau\le t<\infty$:
> $$=\int_0^\infty\!\int_\tau^\infty f(\tau)g(t-\tau)e^{-st}\,dt\,d\tau.$$
>
> **Paso 2 — Sacar $f(\tau)$** de la integral interna (no depende de $t$):
> $$=\int_0^\infty f(\tau)\left[\int_\tau^\infty g(t-\tau)e^{-st}\,dt\right]d\tau.$$
>
> **Paso 3 — Cambio $u=t-\tau$** en la integral interna:
> $$\int_\tau^\infty g(t-\tau)e^{-st}\,dt=\int_0^\infty g(u)e^{-s(u+\tau)}\,du=e^{-s\tau}G(s).$$
>
> **Paso 4 — Sustituir** y reconocer $F(s)$:
> $$\mathcal{L}\{(f*g)(t)\}=G(s)\int_0^\infty f(\tau)e^{-s\tau}\,d\tau=F(s)G(s).\qquad\blacksquare$$

> [!corolario] Inversa de un producto
> Si $Y(s)=F(s)G(s)$, entonces $y(t)=(f*g)(t)=\int_0^t f(\tau)g(t-\tau)\,d\tau$. Es la lectura inversa del teorema: un producto en $s$ corresponde a una convolución en $t$.

---

## Propiedades

> [!info] Álgebra de la convolución
> | Propiedad | Expresión |
> |---|---|
> | Conmutativa | $f*g=g*f$ |
> | Asociativa | $f*(g*h)=(f*g)*h$ |
> | Distributiva | $f*(g+h)=f*g+f*h$ |
> | Elemento neutro | $f*\delta=f$ |
> | Elemento absorbente | $f*0=0$ |

> [!teorema] Conmutatividad
> $$f*g=g*f.$$

> [!demostracion]
> Cambio $u=t-\tau$ ($d\tau=-du$, límites $\tau:0\to t$ pasan a $u:t\to0$):
> $$(f*g)(t)=\int_0^t f(\tau)g(t-\tau)\,d\tau=\int_0^t g(u)f(t-u)\,du=(g*f)(t).$$
> También se ve directo en $s$: $F(s)G(s)=G(s)F(s)$ y, por unicidad de la inversa, $f*g=g*f$.

---

## Aplicación en sistemas LTI

> [!info] Respuesta a cualquier entrada
> Para un sistema LTI con respuesta impulsional $h(t)$:
> $$y(t)=(h*u)(t)=\int_0^t h(\tau)u(t-\tau)\,d\tau\quad\Longleftrightarrow\quad Y(s)=H(s)U(s).$$
> Conocida $h(t)$ (o $H(s)$), la salida ante cualquier entrada queda determinada.

> [!ejemplo] Sistema de primer orden
> $h(t)=2e^{-3t}$, entrada $u(t)=e^{-t}$.
>
> **Convolución:**
> $$y(t)=\int_0^t 2e^{-3\tau}e^{-(t-\tau)}\,d\tau=2e^{-t}\int_0^t e^{-2\tau}\,d\tau=2e^{-t}\cdot\frac{1-e^{-2t}}{2}=e^{-t}-e^{-3t}.$$
>
> **Verificación en Laplace:**
> $$Y(s)=\frac{2}{s+3}\cdot\frac{1}{s+1}=\frac{1}{s+1}-\frac{1}{s+3}\;\Longrightarrow\;y(t)=e^{-t}-e^{-3t}.$$

> [!ejemplo] Convolución con escalón
> $f(t)=e^{-at}$, $g(t)=u(t)$:
> $$(f*u)(t)=\int_0^t e^{-a\tau}\,d\tau=\frac{1-e^{-at}}{a},$$
> que coincide con $\mathcal{L}^{-1}\left\{\dfrac{1}{s(s+a)}\right\}=\dfrac{1}{a}(1-e^{-at})$.

> [!ejemplo] Pulso consigo mismo
> $f(t)=u(t)-u(t-1)$ (pulso unitario en $[0,1]$):
> $$(f*f)(t)=\begin{cases}t,&0\le t\le1\\2-t,&1\le t\le2\\0,&t>2\end{cases}$$
> Resultado: señal **triangular** en $[0,2]$ con pico $1$ en $t=1$. La convolución suaviza.

> [!info] Respuesta escalón desde la impulsional
> Como $u(t-\tau)=1$ en $[0,t]$:
> $$y_{\text{escalón}}(t)=(h*u)(t)=\int_0^t h(\tau)\,d\tau,$$
> es decir, la respuesta al escalón es la **integral** de la respuesta impulsional.

---

## Limitaciones

> [!warning]
> 1. La integral se evalúa en $[0,t]$ solo si ambas señales son **causales** (cero para $t<0$).
> 2. En sistemas **no lineales** el teorema de convolución **no aplica**.
> 3. La integral puede ser intratable analíticamente; usar Laplace ($Y=FG$) cuando sea posible.

## Resumen

> [!resumen]
> | Dominio | Operación |
> |---|---|
> | Tiempo | $y(t)=\int_0^t f(\tau)g(t-\tau)\,d\tau$ |
> | Laplace | $Y(s)=F(s)G(s)$ |
> | Sistema LTI | $y=h*u\;\leftrightarrow\;Y=HU$ |
> | Resp. escalón | $\int_0^t h(\tau)\,d\tau$ |
> | Neutro | $f*\delta=f$ |

> [!corolario]
> El teorema de convolución es lo que convierte el análisis de sistemas en multiplicación: en lugar de integrar $h*u$, se multiplican $H(s)U(s)$ y se antitransforma. Conmutatividad, asociatividad y el elemento neutro $\delta$ hacen de la convolución un álgebra limpia; su lectura en $s$ es, directamente, la [[Funcion Transferencia/index | función de transferencia]].

> [!referencia]
> - Marco general: [[index]].
> - Propiedad listada entre las demás: [[Propiedades]].
> - Pares para antitransformar el producto: [[Tabla Pares]].
> - Objeto resultante $Y=GU$: [[Funcion Transferencia/index]].
