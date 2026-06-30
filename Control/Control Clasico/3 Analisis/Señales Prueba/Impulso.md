---
title: Impulso Unitario
order: 4
tags:
  - control-clasico
  - señales-prueba
  - analisis
draft: false
aliases:
  - impulso
  - delta
  - dirac
  - funcion delta
---

# Impulso Unitario

> [!definicion]
> El **impulso unitario** $\delta(t)$ (delta de Dirac) no es una función ordinaria sino una **distribución**: vale cero salvo en $t=0$, donde concentra un área unitaria. Su transformada es la unidad:
> $$\delta(t)=0\ (t\neq0),\quad \int_{-\infty}^{\infty}\delta(t)\,dt=1\qquad\Longrightarrow\qquad \mathcal{L}\{\delta(t)\}=1\ \text{(todo }s).$$
> Propiedad de muestreo (sifting): $\displaystyle\int_{-\infty}^{\infty}f(t)\,\delta(t-a)\,dt=f(a)$.

> [!info]
> Es la [[Escalon | señal de prueba]] más básica del análisis de la [[Primer Orden | respuesta temporal]]: su salida es la **respuesta impulsional** $h(t)$, que caracteriza por completo al sistema LTI. Es la **derivada** del [[Escalon | escalón]] $u(t)$; integrando $\delta$ se recupera $u$, luego la [[Rampa | rampa]] y la [[Parabola | parábola]].

---

## Ejemplo

> [!ejemplo] Impulso unitario
> ![[senal_impulso.svg|460]]
>
> Idealización con área unitaria concentrada en $t=0$; su transformada es $\mathcal{L}\{\delta(t)\}=1$.

> [!ejemplo] Respuesta impulsional de un sistema de primer orden
> Sea $G(s)=\dfrac{K}{\tau s+1}$ con $K=6$ y $\tau=3\ \text{s}$. Hallar $h(t)$.
>
> **Paso 1 — Salida en Laplace.** Con $U(s)=\mathcal{L}\{\delta(t)\}=1$:
> $$H(s)=G(s)\cdot1=\frac{6}{3s+1}.$$
>
> **Paso 2 — Forma estándar.** Factorizando para que el polo quede explícito:
> $$H(s)=\frac{6}{3\,(s+1/3)}=\frac{2}{s+1/3}.$$
>
> **Paso 3 — Antitransformada.** Como $\mathcal{L}^{-1}\{1/(s+a)\}=e^{-at}$:
> $$h(t)=2\,e^{-t/3},\qquad t\ge0.$$
> Equivale a $\dfrac{K}{\tau}e^{-t/\tau}=\dfrac{6}{3}e^{-t/3}=2e^{-t/3}$.
>
> **Paso 4 — Verificación con el escalón.** La respuesta al escalón es $y_{\text{esc}}(t)=K(1-e^{-t/\tau})=6(1-e^{-t/3})$. Derivando: $\dfrac{d}{dt}y_{\text{esc}}=6\cdot\dfrac{1}{3}e^{-t/3}=2e^{-t/3}=h(t)$. Confirma que **$h(t)$ es la derivada de la respuesta al escalón**.
>
> **Paso 5 — Estabilidad BIBO.** $\displaystyle\int_0^{\infty}|h(t)|\,dt=\int_0^{\infty}2e^{-t/3}\,dt=2\cdot3=6<\infty$ → sistema estable.

---

## Transformada de Laplace

> [!teorema]
> $$\mathcal{L}\{\delta(t)\}=1\ \text{(todo }s);\qquad\qquad \mathcal{L}\{\delta(t-a)\}=e^{-as},\quad a\ge0.$$

> [!demostracion]
> Por la definición unilateral y la propiedad de muestreo con $a=0$, $f(t)=e^{-st}$:
> $$\mathcal{L}\{\delta(t)\}=\int_{0^-}^{\infty}\delta(t)\,e^{-st}\,dt=e^{-s\cdot0}=1.$$
> El caso desplazado sale de la [[Propiedades | propiedad de desplazamiento temporal]]: $\mathcal{L}\{\delta(t-a)\}=e^{-as}\cdot1=e^{-as}$.

---

## En qué consiste

> [!teoria]
> Como $\mathcal{L}\{\delta(t)\}=1$, alimentar un sistema con un impulso devuelve directamente su función transferencia en el tiempo:
> $$Y(s)=G(s)\,U(s)\ \xrightarrow{\,u=\delta\,}\ Y(s)=G(s)\quad\Longrightarrow\quad h(t)=\mathcal{L}^{-1}\{G(s)\}.$$
> Por eso $h(t)$ —la **respuesta impulsional**— contiene toda la información del sistema LTI. Respuestas típicas:
>
> **Primer orden** — $h(t)=\dfrac{K}{\tau}e^{-t/\tau}$.
>
> **Segundo orden subamortiguado** — $h(t)=\dfrac{\omega_n}{\sqrt{1-\zeta^2}}e^{-\zeta\omega_n t}\sin(\omega_d t)$, $\omega_d=\omega_n\sqrt{1-\zeta^2}$.
>
> Ver [[Primer Orden | primer orden]] y [[Segundo Orden/index | segundo orden]].

> [!teorema] El impulso es la derivada del escalón
> $$\delta(t)=\frac{d}{dt}u(t),\qquad u(t)=\int_{-\infty}^{t}\delta(\tau)\,d\tau.$$

> [!demostracion]
> Para una función de prueba $f$ que decae en infinito ($f(\infty)=0$), integrando por partes:
> $$\int_{-\infty}^{\infty}f(t)\,\frac{d}{dt}u(t)\,dt=-\int_{-\infty}^{\infty}f'(t)\,u(t)\,dt=-\int_{0}^{\infty}f'(t)\,dt=f(0)-f(\infty)=f(0),$$
> que coincide con $\int f(t)\,\delta(t)\,dt=f(0)$. Luego $\delta=du/dt$ en sentido distribucional.

> [!info] Propiedades de $h(t)$
> | Propiedad | Expresión |
> |---|---|
> | Causalidad | $h(t)=0$ para $t<0$ |
> | Estabilidad BIBO | $\displaystyle\int_0^{\infty}|h(t)|\,dt<\infty$ |
> | Convolución | $y(t)=\displaystyle\int_0^t h(\tau)\,u(t-\tau)\,d\tau$ |
> | Relación con escalón | $h(t)=\dfrac{d}{dt}y_{\text{escalón}}(t)$ |

> [!info] Relación con otras señales
> | Operación | Resultado | Lleva a |
> |---|---|---|
> | Integral | $\displaystyle\int_{-\infty}^{t}\delta(\tau)\,d\tau=u(t)$ | [[Escalon \| escalón]] |
> | Doble integral | $r(t)=t\,u(t)$ | [[Rampa \| rampa]] |
> | Triple integral | $\tfrac{t^2}{2}u(t)$ | [[Parabola \| parábola]] |
> | Límite de pulso | $\delta(t)=\lim_{\epsilon\to0}\tfrac{1}{\epsilon}[u(t)-u(t-\epsilon)]$ | pulso estrecho |

---

## Convolución y función transferencia

> [!teorema]
> La respuesta a cualquier entrada $u(t)$ es la convolución con $h(t)$:
> $$y(t)=(h*u)(t)=\int_0^t h(\tau)\,u(t-\tau)\,d\tau,\qquad\text{en Laplace}\quad Y(s)=G(s)\,U(s).$$
> Ver [[Convolucion | convolución]].

> [!ejemplo] Aproximación práctica del impulso
> El impulso ideal no es realizable (amplitud infinita, duración cero). En la práctica se usa un **pulso corto de área 1**:
> $$p(t)=\frac{1}{\epsilon}\bigl[u(t)-u(t-\epsilon)\bigr].$$
> Si $\epsilon$ es mucho menor que la constante de tiempo del sistema, $p(t)\approx\delta(t)$ y la salida medida aproxima $h(t)$.

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Definición | distribución, área $1$ en $t=0$ |
> | Muestreo | $\int f(t)\delta(t-a)\,dt=f(a)$ |
> | Transformada | $\mathcal{L}\{\delta(t)\}=1$ |
> | Desplazado | $\mathcal{L}\{\delta(t-a)\}=e^{-as}$ |
> | Salida del sistema | $h(t)=\mathcal{L}^{-1}\{G(s)\}$ |
> | Relación con escalón | $\delta=\dfrac{d}{dt}u$, $h=\dfrac{d}{dt}y_{\text{esc}}$ |
> | Error estacionario | no definido |

> [!corolario]
> El impulso es la señal de prueba que extrae directamente la dinámica del sistema: como $\mathcal{L}\{\delta\}=1$, la salida es $h(t)=\mathcal{L}^{-1}\{G(s)\}$, base de la convolución y criterio de estabilidad BIBO ($\int|h|<\infty$). Integrando $h$ se obtiene la respuesta al [[Escalon | escalón]] y, sucesivamente, a la [[Rampa | rampa]] y la [[Parabola | parábola]].

> [!referencia]
> - Integral: [[Escalon]]. Doble/triple integral: [[Rampa]], [[Parabola]].
> - Respuestas: [[Primer Orden]], [[Segundo Orden/index]].
> - Convolución: [[Convolucion]].
> - Desplazamiento temporal: [[Propiedades]].
