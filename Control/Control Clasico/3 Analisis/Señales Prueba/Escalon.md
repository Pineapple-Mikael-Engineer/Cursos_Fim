---
title: Escalón Unitario
tags:
  - control-clasico
  - señales-prueba
  - analisis
draft: false
aliases:
  - escalon
  - step
  - funcion escalon
  - Heaviside
---

# Escalón Unitario

> [!definicion]
> El **escalón unitario** $u(t)$ vale $0$ para $t<0$ y salta a $1$ en $t=0$, manteniéndose constante. Modela un encendido o un cambio brusco de referencia:
> $$u(t)=\begin{cases}0,&t<0\\[2pt]1,&t\ge0\end{cases}\qquad\Longrightarrow\qquad \mathcal{L}\{u(t)\}=\frac{1}{s},\quad\Re(s)>0.$$
> También se denota $1(t)$ o $H(t)$ (Heaviside). Desplazado: $u(t-a)\;\xrightarrow{\ \mathcal{L}\ }\;e^{-as}/s$.

> [!info]
> Es la [[Impulso | señal de prueba]] más usada en el análisis de la [[Primer Orden | respuesta temporal]]. Es la **integral** del [[Impulso | impulso]] $\delta(t)$ y la **derivada** de la [[Rampa | rampa]] $r(t)$. Junto con [[Rampa | rampa]] y [[Parabola | parábola]] forma la familia que mide el [[Error Estacionario/index | error estacionario]]; al escalón le corresponde el coeficiente de posición $K_p$.

---

## Ejemplo

> [!ejemplo] Respuesta al escalón de un sistema de primer orden
> Sea $G(s)=\dfrac{K}{\tau s+1}$ con $K=5$ y $\tau=2\ \text{s}$. Hallar $y(t)$ ante un escalón unitario y su valor final.
>
> **Paso 1 — Salida en Laplace.** Con $R(s)=1/s$:
> $$Y(s)=G(s)\,R(s)=\frac{5}{2s+1}\cdot\frac{1}{s}=\frac{5}{s(2s+1)}.$$
>
> **Paso 2 — Fracciones parciales.** $\dfrac{5}{s(2s+1)}=\dfrac{A}{s}+\dfrac{B}{2s+1}$. Resolviendo $A=5$, $B=-10$:
> $$Y(s)=\frac{5}{s}-\frac{10}{2s+1}=\frac{5}{s}-\frac{5}{s+1/2}.$$
>
> **Paso 3 — Antitransformada.**
> $$y(t)=5\bigl(1-e^{-t/2}\bigr),\qquad t\ge0.$$
>
> **Paso 4 — Valor final** (TVF): $y(\infty)=\lim_{s\to0}sY(s)=\dfrac{5}{2\cdot0+1}=5=K$. Coincide: el escalón "revela" la ganancia estática $K$.
>
> **Paso 5 — Constante de tiempo.** En $t=\tau=2\,\text{s}$: $y(2)=5(1-e^{-1})=5(0.632)=3.16$, es decir el **63.2 %** del valor final. Este es el criterio gráfico para medir $\tau$.

> [!ejemplo] Error estacionario a escalón
> Para el lazo cerrado con $G(s)=\dfrac{5}{2s+1}$ (sistema **tipo 0**) y realimentación unitaria, ¿qué error deja un escalón unitario de referencia?
>
> **Paso 1 — Coeficiente de posición.** $K_p=\lim_{s\to0}G(s)=\dfrac{5}{1}=5$.
>
> **Paso 2 — Error estacionario.**
> $$e_{ss}=\frac{1}{1+K_p}=\frac{1}{1+5}=\frac{1}{6}\approx0.167.$$
>
> El sistema sigue el escalón con un **16.7 % de error permanente**. Para anularlo habría que añadir un integrador (subir a tipo 1) o un compensador [[Lag | lag]] que aumente $K_p$.

---

## Transformada de Laplace

> [!teorema]
> $$\mathcal{L}\{u(t)\}=\frac{1}{s},\quad\Re(s)>0;\qquad\qquad \mathcal{L}\{u(t-a)\}=\frac{e^{-as}}{s},\quad a\ge0.$$

> [!demostracion]
> $$\mathcal{L}\{u(t)\}=\int_{0^-}^{\infty}1\cdot e^{-st}\,dt=\left[\frac{e^{-st}}{-s}\right]_{0}^{\infty}.$$
> Para $\Re(s)>0$ se tiene $\lim_{t\to\infty}e^{-st}=0$, luego $\mathcal{L}\{u(t)\}=0-\dfrac{1}{-s}=\dfrac{1}{s}$. El caso desplazado sale de la [[Propiedades | propiedad de desplazamiento temporal]] $\mathcal{L}\{f(t-a)u(t-a)\}=e^{-as}F(s)$ con $f=1$.

---

## En qué consiste

> [!teoria]
> La respuesta al escalón es el ensayo estándar para caracterizar un sistema LTI: con $Y(s)=G(s)/s$ se obtiene la salida temporal por antitransformada. Casos típicos:
>
> **Primer orden** — $G(s)=\dfrac{K}{\tau s+1}$:
> $$y(t)=K\bigl(1-e^{-t/\tau}\bigr).$$
>
> **Segundo orden subamortiguado** — $G(s)=\dfrac{\omega_n^2}{s^2+2\zeta\omega_n s+\omega_n^2}$, $0<\zeta<1$:
> $$y(t)=1-\frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}}\sin(\omega_d t+\theta),\quad \omega_d=\omega_n\sqrt{1-\zeta^2},\ \theta=\arccos\zeta.$$
>
> Ver [[Primer Orden | primer orden]] y [[Segundo Orden/index | segundo orden]].

> [!info] Relación con otras señales
> | Relación | Expresión | Lleva a |
> |---|---|---|
> | Derivada | $\dfrac{d}{dt}u(t)=\delta(t)$ | [[Impulso \| impulso]] |
> | Integral | $\displaystyle\int_{-\infty}^{t}u(\tau)\,d\tau=t\,u(t)$ | [[Rampa \| rampa]] |
> | Doble integral | $\displaystyle\frac{t^2}{2}u(t)$ | [[Parabola \| parábola]] |
> | Pulso | $u(t)-u(t-T)$ | rectángulo de ancho $T$ |

> [!info] Propiedades
> | Propiedad | Expresión |
> |---|---|
> | Valor inicial | $u(0^+)=1$ |
> | Valor final | $\lim_{t\to\infty}u(t)=1$ |
> | Linealidad | $a\,u(t)+b\,u(t)=(a+b)\,u(t)$ |
> | Desplazamiento | $u(t-a)$ retrasa la activación |
> | Escalamiento | $u(at)=u(t)$ para $a>0$ |
> | Causalidad | $f(t)\,u(t)$ hace causal a $f$ |

---

## Error estacionario a escalón

> [!definicion]
> El **coeficiente de error de posición** y el error que deja un escalón unitario en lazo cerrado con realimentación unitaria son:
> $$K_p=\lim_{s\to0}G(s)=G(0),\qquad e_{ss}=\frac{1}{1+K_p}.$$

> [!demostracion]
> Con $R(s)=1/s$, la señal de error es $E(s)=\dfrac{1}{1+G(s)}R(s)$. Por el [[Teorema Valor Inicial Final | teorema del valor final]]:
> $$e_{ss}=\lim_{s\to0}s\cdot\frac{1}{1+G(s)}\cdot\frac{1}{s}=\frac{1}{1+G(0)}=\frac{1}{1+K_p}.$$

> [!info] Dependencia con el tipo de sistema
> | Tipo | $K_p$ | $e_{ss}$ (escalón unitario) |
> |---|---|---|
> | 0 | $K$ (finito) | $\dfrac{1}{1+K}$ |
> | 1 | $\infty$ | $0$ |
> | 2 | $\infty$ | $0$ |
>
> Familia completa: a la [[Rampa \| rampa]] le corresponde $K_v=\lim_{s\to0}sG(s)$ con $e_{ss}=1/K_v$, y a la [[Parabola \| parábola]] $K_a=\lim_{s\to0}s^2G(s)$ con $e_{ss}=1/K_a$. Detalle por tipos en [[Error Estacionario/index | error estacionario]].

> [!warning]
> El [[Impulso | impulso]] no tiene coeficiente de error definido: su entrada tiende a cero para $t>0$ y no se mantiene en régimen permanente.

---

## Identificación desde la respuesta al escalón

> [!ejemplo]
> ![[identificacion_escalon.svg]]
>
> **Primer orden:**
> 1. Medir $y(\infty)=K$ (ganancia estática).
> 2. Buscar el instante en que $y(t)=0.632\,K$ → ese tiempo es $\tau$.
> 3. Verificar: $y(2\tau)\approx0.865\,K$ y $y(3\tau)\approx0.95\,K$.
>
> **Segundo orden** (ver [[Segundo Orden/index | segundo orden]]):
> - $M_p=\dfrac{y_{\text{máx}}-y(\infty)}{y(\infty)}\ \to\ \zeta$.
> - $T_p$ (tiempo del primer pico) $\to\ \omega_n$.
> - $T_s(2\%)\approx 4/(\zeta\omega_n)$.

> [!info] En MATLAB
> ```matlab
> K = 5; tau = 2;
> G = tf(K, [tau 1]);
> step(G)            % respuesta al escalon
> stepinfo(G)        % tr, ts, Mp, valor final
> dcgain(G)          % ganancia estatica K = G(0)
> ```

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Definición | $u(t)=0$ ($t<0$), $1$ ($t\ge0$) |
> | Transformada | $\mathcal{L}\{u(t)\}=1/s$ |
> | Desplazada | $\mathcal{L}\{u(t-a)\}=e^{-as}/s$ |
> | Derivada / integral | $\delta(t)$ / $t\,u(t)$ |
> | Coeficiente de error | $K_p=G(0)$ |
> | $e_{ss}$ | $1/(1+K_p)$ |
> | Respuesta 1.º orden | $K(1-e^{-t/\tau})$ |

> [!corolario]
> El escalón es la señal de prueba canónica: su transformada $1/s$ convierte la respuesta en $G(s)/s$, de donde se leen la ganancia estática $K=G(0)$, los tiempos de respuesta ($t_r$, $t_s$, $M_p$) y el error de posición $e_{ss}=1/(1+K_p)$. Solo los sistemas con integrador (tipo 1 o superior) lo siguen sin error.

> [!referencia]
> - Derivada: [[Impulso]]. Integral: [[Rampa]]. Doble integral: [[Parabola]].
> - Respuestas: [[Primer Orden]], [[Segundo Orden/index]].
> - Error estacionario completo: [[Error Estacionario/index]].
> - Teorema del valor final: [[Teorema Valor Inicial Final]].
