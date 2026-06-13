---
title: Rampa Unitaria
tags:
  - control-clasico
  - señales-prueba
  - analisis
draft: false
aliases:
  - rampa
  - ramp
  - funcion rampa
---

# Rampa Unitaria

> [!definicion]
> La **rampa unitaria** $r(t)$ crece linealmente con pendiente $1$ a partir de $t=0$. Modela una referencia de **velocidad constante**:
> $$r(t)=\begin{cases}0,&t<0\\[2pt]t,&t\ge0\end{cases}=t\,u(t)\qquad\Longrightarrow\qquad \mathcal{L}\{r(t)\}=\frac{1}{s^2},\quad\Re(s)>0.$$
> Desplazada: $r(t-a)=(t-a)\,u(t-a)\ \xrightarrow{\ \mathcal{L}\ }\ e^{-as}/s^2$.

> [!info]
> Es la [[Escalon | señal de prueba]] que mide el seguimiento de velocidad en la [[Primer Orden | respuesta temporal]]. Es la **integral** del [[Escalon | escalón]] $u(t)$ y la **derivada** de la [[Parabola | parábola]] $p(t)$; su segunda derivada es el [[Impulso | impulso]] $\delta(t)$. En el [[Error Estacionario/index | error estacionario]] le corresponde el coeficiente de velocidad $K_v$.

---

## Ejemplo

> [!ejemplo] Rampa unitaria
> ![[senal_rampa.svg|460]]
>
> Crece con pendiente unitaria a partir de $t=0$; su transformada es $1/s^2$.

> [!ejemplo] Error de velocidad de un sistema tipo 1
> Sea el lazo abierto $G(s)=\dfrac{10}{s(s+2)}$ (un integrador → **tipo 1**) con realimentación unitaria. ¿Qué error deja una rampa unitaria?
>
> **Paso 1 — Coeficiente de velocidad.**
> $$K_v=\lim_{s\to0}sG(s)=\lim_{s\to0}s\cdot\frac{10}{s(s+2)}=\lim_{s\to0}\frac{10}{s+2}=\frac{10}{2}=5.$$
>
> **Paso 2 — Error estacionario.**
> $$e_{ss}=\frac{1}{K_v}=\frac{1}{5}=0.2.$$
>
> El sistema sigue la rampa con un **retraso permanente de $0.2$** en la salida (no diverge, pero nunca alcanza la referencia). Un tipo 0 daría $e_{ss}=\infty$; un tipo 2 daría $e_{ss}=0$.

> [!ejemplo] Respuesta a rampa de un sistema de primer orden
> Sea $G(s)=\dfrac{K}{\tau s+1}$. Hallar $y_{\text{rampa}}(t)$ con $R(s)=1/s^2$.
>
> **Paso 1 — Salida y fracciones parciales.**
> $$Y(s)=\frac{K}{s^2(\tau s+1)}=\frac{A}{s}+\frac{B}{s^2}+\frac{C}{\tau s+1},\qquad A=-K\tau,\ B=K,\ C=K\tau^2.$$
>
> **Paso 2 — Antitransformada.**
> $$y_{\text{rampa}}(t)=-K\tau+Kt+K\tau\,e^{-t/\tau}=K\bigl(t-\tau+\tau e^{-t/\tau}\bigr),\qquad t\ge0.$$
>
> **Paso 3 — Interpretación.** Para $t\gg\tau$ el exponencial se anula y $y\approx K(t-\tau)$: la salida sigue la rampa $Kt$ pero con un **retardo $\tau$**. Con $K=1$, ese retardo $\tau$ es exactamente $e_{ss}=1/K_v$.

---

## Transformada de Laplace

> [!teorema]
> $$\mathcal{L}\{r(t)\}=\frac{1}{s^2},\quad\Re(s)>0;\qquad\qquad \mathcal{L}\{r(t-a)\}=\frac{e^{-as}}{s^2},\quad a\ge0.$$

> [!demostracion] Integración directa
> Con $r(t)=t$ e integración por partes ($u=t$, $dv=e^{-st}dt$):
> $$\mathcal{L}\{r(t)\}=\int_0^{\infty}t\,e^{-st}\,dt=\left[-\frac{t}{s}e^{-st}\right]_0^{\infty}+\frac{1}{s}\int_0^{\infty}e^{-st}\,dt=0+\frac{1}{s}\cdot\frac{1}{s}=\frac{1}{s^2}.$$

> [!demostracion] Vía el escalón
> Como $r(t)=\int_0^t u(\tau)\,d\tau$, la [[Propiedades | propiedad de integración]] divide por $s$:
> $$\mathcal{L}\{r(t)\}=\frac{1}{s}\,\mathcal{L}\{u(t)\}=\frac{1}{s}\cdot\frac{1}{s}=\frac{1}{s^2}.$$

---

## En qué consiste

> [!teoria]
> La respuesta a rampa se obtiene integrando la respuesta al escalón, porque $1/s^2=(1/s)(1/s)$:
> $$Y_{\text{rampa}}(s)=G(s)\frac{1}{s^2}=\frac{1}{s}\,Y_{\text{escalón}}(s)\quad\Longrightarrow\quad y_{\text{rampa}}(t)=\int_0^t y_{\text{escalón}}(\tau)\,d\tau.$$
> Por eso un sistema necesita al menos un **integrador** (tipo 1) para no acumular error indefinido al seguir una rampa.

> [!info] Relación con otras señales
> | Relación | Expresión | Lleva a |
> |---|---|---|
> | Derivada | $\dfrac{d}{dt}r(t)=u(t)$ | [[Escalon \| escalón]] |
> | Derivada segunda | $\dfrac{d^2}{dt^2}r(t)=\delta(t)$ | [[Impulso \| impulso]] |
> | Integral | $\displaystyle\int_0^t r(\tau)\,d\tau=\tfrac{t^2}{2}u(t)$ | [[Parabola \| parábola]] |

---

## Error estacionario a rampa

> [!definicion]
> El **coeficiente de error de velocidad** y el error que deja una rampa unitaria en lazo cerrado con realimentación unitaria son:
> $$K_v=\lim_{s\to0}sG(s),\qquad e_{ss}=\frac{1}{K_v}.$$

> [!demostracion]
> Con $R(s)=1/s^2$ y $E(s)=\dfrac{1}{1+G(s)}R(s)$, por el [[Teorema Valor Inicial Final | teorema del valor final]]:
> $$e_{ss}=\lim_{s\to0}s\cdot\frac{1}{1+G(s)}\cdot\frac{1}{s^2}=\lim_{s\to0}\frac{1}{s\,(1+G(s))}=\frac{1}{\lim_{s\to0}sG(s)}=\frac{1}{K_v}.$$

> [!info] Dependencia con el tipo de sistema
> | Tipo | $K_v$ | $e_{ss}$ (rampa unitaria) |
> |---|---|---|
> | 0 | $0$ | $\infty$ (no sigue) |
> | 1 | $K$ (finito) | $\dfrac{1}{K}$ |
> | 2 | $\infty$ | $0$ (sigue perfectamente) |
>
> Familia completa: al [[Escalon \| escalón]] le corresponde $K_p=\lim_{s\to0}G(s)$ con $e_{ss}=1/(1+K_p)$, y a la [[Parabola \| parábola]] $K_a=\lim_{s\to0}s^2G(s)$ con $e_{ss}=1/K_a$. Detalle por tipos en [[Error Estacionario/index | error estacionario]].

> [!warning]
> El [[Impulso | impulso]] no tiene coeficiente de error definido: su entrada tiende a cero para $t>0$ y no se mantiene en régimen permanente.

---

## Identificación desde la respuesta a rampa

> [!ejemplo]
> **Problema:** un sistema responde a la rampa unitaria con $y(t)=3t-6+2e^{-t/2}$ ($t\ge0$). ¿Es de primer orden?
>
> **Paso 1 — Régimen permanente.** Para $t$ grande $e^{-t/2}\to0$, luego $y\approx3t-6$. Esto sugiere $K=3$ y un retardo equivalente $3(t-2)$, es decir $\tau=2\ \text{s}$.
>
> **Paso 2 — Forma teórica de primer orden.** $y_{\text{rampa}}(t)=K(t-\tau+\tau e^{-t/\tau})$. Con $K=3$, $\tau=2$:
> $$y(t)=3(t-2+2e^{-t/2})=3t-6+6e^{-t/2}.$$
>
> **Paso 3 — Comparar.** El término exponencial teórico tiene coeficiente $6$, pero el dato trae $2$.
>
> **Conclusión:** el sistema **NO** es de primer orden; tiene dinámica adicional. Habría que recurrir a fracciones parciales o identificación en frecuencia.

> [!info] En MATLAB
> ```matlab
> G = tf(10, [1 2 0]);     % 10 / (s(s+2)), tipo 1
> Kv = dcgain(minreal(tf([10],[1 2]) ));  % lim s->0 de s*G = 10/2 = 5
> t = 0:0.01:10;  u = t;   % rampa unitaria
> lsim(feedback(G,1), u, t)
> ```

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Definición | $r(t)=t\,u(t)$ |
> | Transformada | $\mathcal{L}\{r(t)\}=1/s^2$ |
> | Desplazada | $\mathcal{L}\{r(t-a)\}=e^{-as}/s^2$ |
> | Derivada / integral | $u(t)$ / $\tfrac{t^2}{2}u(t)$ |
> | Coeficiente de error | $K_v=\lim_{s\to0}sG(s)$ |
> | $e_{ss}$ | $1/K_v$ |
> | Tipo mínimo para seguir | 1 (un integrador) |

> [!corolario]
> La rampa mide el seguimiento de velocidad: su transformada $1/s^2$ da $Y=G(s)/s^2$, integral de la respuesta al escalón. El error permanente $e_{ss}=1/K_v$ con $K_v=\lim_{s\to0}sG(s)$ revela cuántos integradores tiene el lazo: nulo si es tipo 0, finito si es tipo 1 y cero si es tipo 2 o superior.

> [!referencia]
> - Derivada: [[Escalon]]. Segunda derivada: [[Impulso]]. Integral: [[Parabola]].
> - Respuestas: [[Primer Orden]], [[Segundo Orden/index]].
> - Error estacionario completo: [[Error Estacionario/index]].
> - Teorema del valor final: [[Teorema Valor Inicial Final]].
