---
title: Parábola Unitaria
tags:
  - control-clasico
  - señales-prueba
  - analisis
draft: false
aliases:
  - parabola
  - parabolic
  - funcion parabola
  - aceleracion
---

# Parábola Unitaria

> [!definicion]
> La **parábola unitaria** $p(t)$ crece como $t^2/2$ a partir de $t=0$. Modela una referencia de **aceleración constante**:
> $$p(t)=\begin{cases}0,&t<0\\[2pt]\dfrac{t^2}{2},&t\ge0\end{cases}=\frac{t^2}{2}\,u(t)\qquad\Longrightarrow\qquad \mathcal{L}\{p(t)\}=\frac{1}{s^3},\quad\Re(s)>0.$$
> Desplazada: $p(t-a)=\dfrac{(t-a)^2}{2}u(t-a)\ \xrightarrow{\ \mathcal{L}\ }\ e^{-as}/s^3$.

> [!info]
> Es la [[Escalon | señal de prueba]] más exigente: mide el seguimiento de aceleración en la [[Primer Orden | respuesta temporal]]. Es la **integral** de la [[Rampa | rampa]] $r(t)$ (y doble integral del [[Escalon | escalón]]); sus derivadas sucesivas dan rampa, escalón e [[Impulso | impulso]]. En el [[Error Estacionario/index | error estacionario]] le corresponde el coeficiente de aceleración $K_a$.

---

## Ejemplo

> [!ejemplo] Parábola unitaria
> ![[senal_parabola.svg|460]]
>
> $p(t)=t^2/2$ para $t\ge0$; su transformada es $1/s^3$.

> [!ejemplo] Error de aceleración de un sistema tipo 2
> Sea el lazo abierto $G(s)=\dfrac{20}{s^2(s+4)}$ (dos integradores → **tipo 2**) con realimentación unitaria. ¿Qué error deja una parábola unitaria?
>
> **Paso 1 — Coeficiente de aceleración.**
> $$K_a=\lim_{s\to0}s^2G(s)=\lim_{s\to0}s^2\cdot\frac{20}{s^2(s+4)}=\lim_{s\to0}\frac{20}{s+4}=\frac{20}{4}=5.$$
>
> **Paso 2 — Error estacionario.**
> $$e_{ss}=\frac{1}{K_a}=\frac{1}{5}=0.2.$$
>
> El sistema sigue la parábola con error permanente $0.2$. Un tipo 0 o 1 daría $e_{ss}=\infty$ (no la sigue); solo tipo 2 o superior consigue error finito.

> [!ejemplo] Respuesta a parábola de un sistema de primer orden
> Sea $G(s)=\dfrac{K}{\tau s+1}$. Hallar $y_{\text{parábola}}(t)$ con $R(s)=1/s^3$.
>
> **Paso 1 — Salida y fracciones parciales.**
> $$Y(s)=\frac{K}{s^3(\tau s+1)}=\frac{A}{s}+\frac{B}{s^2}+\frac{C}{s^3}+\frac{D}{\tau s+1},\qquad A=K\tau^2,\ B=-K\tau,\ C=K,\ D=-K\tau^3.$$
>
> **Paso 2 — Antitransformada.**
> $$y_{\text{parábola}}(t)=K\tau^2-K\tau\,t+K\frac{t^2}{2}-K\tau^2 e^{-t/\tau},\qquad t\ge0.$$
>
> **Paso 3 — Interpretación.** Para $t\gg\tau$: $y\approx K\bigl(\tfrac{t^2}{2}-\tau t+\tau^2\bigr)$. La salida sigue la parábola $K\,t^2/2$ pero con retardo y offset que dependen de $\tau$.

---

## Transformada de Laplace

> [!teorema]
> $$\mathcal{L}\{p(t)\}=\frac{1}{s^3},\quad\Re(s)>0;\qquad\qquad \mathcal{L}\{p(t-a)\}=\frac{e^{-as}}{s^3},\quad a\ge0.$$

> [!demostracion] Integración directa
> Usando $\mathcal{L}\{t^2\}=2/s^3$:
> $$\mathcal{L}\{p(t)\}=\int_0^{\infty}\frac{t^2}{2}e^{-st}\,dt=\frac{1}{2}\,\mathcal{L}\{t^2\}=\frac{1}{2}\cdot\frac{2}{s^3}=\frac{1}{s^3}.$$

> [!demostracion] Vía rampa y escalón
> Como $p(t)=\int_0^t r(\tau)\,d\tau$, la [[Propiedades | propiedad de integración]] divide por $s$:
> $$\mathcal{L}\{p(t)\}=\frac{1}{s}\,\mathcal{L}\{r(t)\}=\frac{1}{s}\cdot\frac{1}{s^2}=\frac{1}{s^3}.$$

---

## En qué consiste

> [!teoria]
> La respuesta a parábola es la doble integral de la respuesta al escalón, porque $1/s^3=(1/s^2)(1/s)$:
> $$Y_{\text{parábola}}(s)=G(s)\frac{1}{s^3}=\frac{1}{s^2}Y_{\text{escalón}}(s)\quad\Longrightarrow\quad y_{\text{parábola}}(t)=\int_0^t\!\!\int_0^\tau y_{\text{escalón}}(\sigma)\,d\sigma\,d\tau.$$
> Por eso seguir una parábola con error finito exige **dos integradores** en el lazo (tipo 2).

> [!info] Relación con otras señales
> | Relación | Expresión | Lleva a |
> |---|---|---|
> | Derivada | $\dfrac{d}{dt}p(t)=r(t)$ | [[Rampa \| rampa]] |
> | Derivada segunda | $\dfrac{d^2}{dt^2}p(t)=u(t)$ | [[Escalon \| escalón]] |
> | Derivada tercera | $\dfrac{d^3}{dt^3}p(t)=\delta(t)$ | [[Impulso \| impulso]] |
> | Integral | $\displaystyle\int_0^t p(\tau)\,d\tau=\tfrac{t^3}{6}u(t)$ | — |

> [!info] Jerarquía de señales
> | Señal | Operador físico | Tipo mínimo | Error finito |
> |---|---|---|---|
> | [[Escalon \| escalón]] | posición | 0 | $1/(1+K_p)$ |
> | [[Rampa \| rampa]] | velocidad | 1 | $1/K_v$ |
> | Parábola | aceleración | 2 | $1/K_a$ |
>
> Cada integración de la señal exige un integrador más en el lazo para mantener el error acotado.

---

## Error estacionario a parábola

> [!definicion]
> El **coeficiente de error de aceleración** y el error que deja una parábola unitaria en lazo cerrado con realimentación unitaria son:
> $$K_a=\lim_{s\to0}s^2G(s),\qquad e_{ss}=\frac{1}{K_a}.$$

> [!demostracion]
> Con $R(s)=1/s^3$ y $E(s)=\dfrac{1}{1+G(s)}R(s)$, por el [[Teorema Valor Inicial Final | teorema del valor final]]:
> $$e_{ss}=\lim_{s\to0}s\cdot\frac{1}{1+G(s)}\cdot\frac{1}{s^3}=\lim_{s\to0}\frac{1}{s^2(1+G(s))}=\frac{1}{\lim_{s\to0}s^2G(s)}=\frac{1}{K_a}.$$

> [!info] Dependencia con el tipo de sistema
> | Tipo | $K_a$ | $e_{ss}$ (parábola unitaria) |
> |---|---|---|
> | 0 | $0$ | $\infty$ (no sigue) |
> | 1 | $0$ | $\infty$ (no sigue) |
> | 2 | $K$ (finito) | $\dfrac{1}{K}$ |
>
> Familia completa: al [[Escalon \| escalón]] le corresponde $K_p$ con $e_{ss}=1/(1+K_p)$, y a la [[Rampa \| rampa]] $K_v$ con $e_{ss}=1/K_v$. Detalle por tipos en [[Error Estacionario/index | error estacionario]].

> [!warning]
> El [[Impulso | impulso]] no tiene coeficiente de error definido: su entrada tiende a cero para $t>0$ y no se mantiene en régimen permanente.

---

## Identificación desde la respuesta a parábola

> [!ejemplo]
> **Problema:** un sistema tipo 2 responde a la parábola unitaria con $y(t)=\dfrac{t^2}{2}-2t+2-2e^{-t}$ ($t\ge0$). Determine $K_a$.
>
> **Paso 1 — Régimen permanente.** Para $t$ grande $e^{-t}\to0$, luego $y\approx\dfrac{t^2}{2}-2t+2$.
>
> **Paso 2 — Comparar con la forma esperada** $y=\dfrac{K_a}{2}t^2-K_a\tau\,t+K_a\tau^2+\text{transitorio}$:
> - Coef. de $t^2/2$: $\dfrac{K_a}{2}=\dfrac{1}{2}\Rightarrow K_a=1$.
> - Coef. de $t$: $-K_a\tau=-2\Rightarrow\tau=2\ \text{s}$.
> - Término constante teórico $K_a\tau^2=4$, pero el dato trae $2$ → hay offset adicional.
>
> **Paso 3 — Transitorio.** El exponencial teórico de primer orden sería $K_a\tau^2 e^{-t/\tau}=4e^{-t/2}$, pero el dato muestra $2e^{-t}$.
>
> **Conclusión:** el sistema **NO** es de primer orden; la respuesta a parábola revela dinámica más rica que el escalón o la rampa.

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Definición | $p(t)=\tfrac{t^2}{2}u(t)$ |
> | Transformada | $\mathcal{L}\{p(t)\}=1/s^3$ |
> | Desplazada | $\mathcal{L}\{p(t-a)\}=e^{-as}/s^3$ |
> | Derivada / integral | $r(t)$ / $\tfrac{t^3}{6}u(t)$ |
> | Coeficiente de error | $K_a=\lim_{s\to0}s^2G(s)$ |
> | $e_{ss}$ | $1/K_a$ |
> | Tipo mínimo para seguir | 2 (dos integradores) |

> [!corolario]
> La parábola es la señal de prueba de aceleración: su transformada $1/s^3$ da $Y=G(s)/s^3$, doble integral de la respuesta al escalón. El error $e_{ss}=1/K_a$ con $K_a=\lim_{s\to0}s^2G(s)$ solo es finito en sistemas tipo 2 o superiores, cerrando la jerarquía escalón→rampa→parábola en posición, velocidad y aceleración.

> [!referencia]
> - Derivada: [[Rampa]]. Segunda derivada: [[Escalon]]. Tercera derivada: [[Impulso]].
> - Respuestas: [[Primer Orden]], [[Segundo Orden/index]].
> - Error estacionario completo: [[Error Estacionario/index]].
> - Teorema del valor final: [[Teorema Valor Inicial Final]].
