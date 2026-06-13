---
title: Acción Integral $I$
tags:
  - control-clasico
  - controladores
  - pid
draft: false
aliases:
  - acción integral
  - control I
  - integral
  - reset
---

# Acción Integral $I$

> [!definicion]
> La señal de control es proporcional al error **acumulado** (pasado):
> $$u(t) = K_i\!\int_0^t e(\tau)\,d\tau, \qquad G_c(s) = \frac{K_i}{s}.$$
> Añade un **polo en el origen** ($s=0$) —un integrador en la rama directa— que sube en uno el tipo del sistema y **elimina el error estacionario** ante escalón, a costa de aportar $-90^\circ$ de fase y empeorar la estabilidad.

> [!info]
> Es la acción que aporta "memoria" al [[PID/index | controlador PID]], hermana de la [[Proporcional P | proporcional]] y la [[Derivativo D | derivativa]]; las tres se comparan en [[index | Acciones P, I, D]]. Rara vez se usa sola: se combina con $P$ en [[PI | PI]] (equivalente a un compensador lag) y, para estabilizar, con $D$ en [[PID]].

---

## Ejemplo

> [!ejemplo]
> **Cómo la acción I anula el offset que deja P.** Misma planta tipo 0 $G(s)=\dfrac{1}{(s+1)(s+2)}$ con realimentación unitaria. Comparamos $P$ puro ($G_c=K_p$) con un $PI$ ($G_c=K_p+K_i/s$).
>
> **Paso 1 — Recordatorio: con $P$ queda offset.** Con $K_p=8$, $G(0)=0.5$:
> $$e_{ss}^{P}=\frac{1}{1+K_p G(0)}=\frac{1}{1+4}=0.20\quad(20\%).$$
>
> **Paso 2 — Añadir el integrador.** Con $G_c=K_i/s$ la ganancia de lazo es $L(s)=\dfrac{K_i}{s}\,G(s)$. Ante escalón unitario, por el [[Formula General | teorema del valor final]]:
> $$e_{ss}=\lim_{s\to0} s\,\frac{1}{1+L(s)}\frac{1}{s}=\lim_{s\to0}\frac{1}{1+\frac{K_i G(s)}{s}}=\lim_{s\to0}\frac{s}{s+K_i G(s)}=\frac{0}{0+K_i\,0.5}=0.$$
> El polo en el origen hace $L(0)\to\infty$, así que el error se anula **exactamente**, sea cual sea $K_i$.
>
> **Paso 3 — Por qué (mecanismo).** Mientras quede error, la integral $\int e\,d\tau$ **sigue creciendo** y empuja $u(t)$; solo cuando $e=0$ se detiene la acumulación. El integrador "no descansa" hasta cancelar el sesgo.
>
> **Paso 4 — El coste: $K_i$ y la estabilidad.** Con $PI$ el polinomio característico es $s\,(s+1)(s+2)+K_p s+K_i=0$, es decir
> $$s^3+3s^2+(2+K_p)s+K_i=0.$$
> Por Routh, la estabilidad exige $(2+K_p)\cdot3 > K_i$. Con $K_p=8$: $K_i<30$.
>
> | $K_i$ | Comportamiento |
> |---|---|
> | $5$ | estable, corrección lenta del error, poco sobrepico |
> | $20$ | estable, error se anula rápido pero mayor sobrepico |
> | $30$ | **límite de estabilidad** (oscilación sostenida) |
> | $40$ | **inestable** |
>
> **Lectura.** La acción $I$ garantiza $e_{ss}=0$ independientemente de su valor, pero subir $K_i$ acelera la corrección a cambio de más sobrepico y, pasado el límite de Routh, inestabilidad.

> [!ejemplo] Efecto de la acción integral
> ![[i_efecto_ki_escalon.svg|550]]
>
> La acción $I$ lleva el error a cero (sin offset), pero con mayor sobrepico y respuesta más lenta que $P$ solo.

---

## En qué consiste

> [!teoria] Acumula el pasado
> La integral suma todo el error ocurrido hasta el instante actual. Aunque el error sea pequeño, si **persiste** la integral sigue creciendo y aumenta la corrección: por eso es capaz de borrar un offset que $P$ no puede tocar (cuando $e$ es pequeño, $K_p e$ también lo es). El precio es el **retardo**: la acción depende de la historia, no del valor instantáneo, así que reacciona con desfase.

> [!info] Por qué funciona
> Mientras haya error, la integral **sigue creciendo** y mueve la señal de control, hasta que $e=0$ detiene la acumulación. Es un mecanismo de **autocorrección** del sesgo que $P$ deja.

---

## Anulación del error estacionario

> [!teorema]
> La acción integral **sube en uno el [[Coeficientes Kp Kv Ka | tipo del sistema]]**: el polo en el origen hace que $G(0)\to\infty$, y por el teorema del valor final el error estacionario ante escalón se anula:
> $$e_{ss} = \frac{1}{1 + K_p G(0)}\to 0 \quad\text{(con integrador, } G(0)=\infty).$$

> [!demostracion]
> Con $G_c = K_i/s$, la ganancia de lazo $L = K_i G(s)/s$ tiene un polo en el origen. El error ante escalón:
> $$e_{ss} = \lim_{s\to0} s\,\frac{1}{1 + K_i G(s)/s}\frac{1}{s} = \lim_{s\to0}\frac{s}{s + K_i G(s)} = 0,$$
> mientras $G(0)\neq0$. El integrador "no descansa" hasta que el error es cero.

---

## Coste: retardo de fase

> [!warning] La acción integral desestabiliza
> El integrador aporta $-90^\circ$ de fase, reduciendo el [[Margenes MF MG | margen de fase]] y empeorando la estabilidad:
> $$\angle G_c(j\omega) = \angle\frac{K_i}{j\omega} = -90^\circ.$$
> Aumentar $K_i$ acelera la corrección del error pero **incrementa el sobrepico** y puede inestabilizar (ver el límite de Routh del ejemplo). Es el compromiso de la acción $I$.

> [!info] Efecto sobre los polos
> El polo en el origen del integrador **atrae** el lugar de raíces hacia el semiplano derecho, reduciendo el [[Segundo Orden/index | amortiguamiento]]. Por eso la acción $I$ rara vez se usa sola: se combina con $P$ ([[PI | PI]]) y, si hace falta estabilizar, con $D$ ([[PID | PID]]).

---

## Limitaciones

> [!warning] Saturación e *integral windup*
> Si el actuador **satura**, el error persiste y la integral sigue acumulando un valor enorme (*windup*). Al salir de la saturación, ese valor produce un sobrepico severo y lento de descargar. Se corrige con **anti-windup** (limitar o congelar la integral en saturación). Es el problema práctico más común de la acción $I$.

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Ley de control | $u=K_i\int e\,d\tau$ |
> | $G_c(s)$ | $K_i/s$ |
> | Info del error | pasado (acumulado) |
> | Fase aportada | $-90^\circ$ |
> | $e_{ss}$ (escalón) | $0$ (sube el tipo en 1) |
> | Al subir $K_i$ | corrección más rápida, $M_p\uparrow$, estabilidad $\downarrow$ |
> | Riesgo práctico | *windup* en saturación |

> [!corolario]
> La acción $I$ integra el error pasado hasta anularlo: garantiza $e_{ss}=0$ ante escalón sin importar su ganancia, pero introduce $-90^\circ$ de fase que desestabiliza y un valor de $K_i$ excesivo lleva a la inestabilidad. Se empareja con $P$ para tener velocidad y error nulo ([[PI]]), y con $D$ para recuperar amortiguamiento ([[PID]]); en la práctica exige protección **anti-windup**.

> [!referencia]
> - Combinación práctica con P: [[PI]].
> - Compensar el retardo de fase con D: [[Derivativo D]] · [[PID]].
> - Tipos de sistema y error: [[Coeficientes Kp Kv Ka]] · [[Tabla Tipos]] · [[Error Estacionario/index]].
> - Relación con compensador lag: [[PI]].
