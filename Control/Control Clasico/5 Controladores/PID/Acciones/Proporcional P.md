---
title: Acción Proporcional $P$
tags:
  - control-clasico
  - controladores
  - pid
draft: false
aliases:
  - acción proporcional
  - control P
  - proporcional
---

# Acción Proporcional $P$

> [!definicion]
> La señal de control es proporcional al error **presente**:
> $$u(t) = K_p\,e(t), \qquad G_c(s) = K_p.$$
> $K_p$ es la **ganancia proporcional** (a veces dada como **banda proporcional** $BP = 100/K_p\ \%$). Reduce el error estacionario y acelera la respuesta, pero nunca anula el error en plantas sin integrador y empeora la estabilidad.

> [!info]
> Es la acción base del [[PID/index | controlador PID]], hermana de la [[Integral I | integral]] y la [[Derivativo D | derivativa]]; las tres se comparan en [[index | Acciones P, I, D]]. Solo $P$ aporta $0^\circ$ de fase, así que mueve los polos sin reconfigurar el [[Lugar Raices/index | lugar de raíces]].

---

## Ejemplo

> [!ejemplo]
> **Efecto de $K_p$ sobre $e_{ss}$ y el sobrepico.** Planta tipo 0 $G(s)=\dfrac{1}{(s+1)(s+2)}$ con realimentación unitaria y control $G_c=K_p$. Estudiar $K_p=2,\ 8,\ 20$.
>
> **Paso 1 — Error estacionario ante escalón.** La planta es tipo 0, así que $G(0)=\frac{1}{1\cdot2}=0.5$. La constante de posición es $K_{pos}=K_p\,G(0)=0.5\,K_p$ y
> $$e_{ss}=\frac{1}{1+K_p G(0)}=\frac{1}{1+0.5\,K_p}.$$
>
> | $K_p$ | $K_{pos}=0.5K_p$ | $e_{ss}=1/(1+K_{pos})$ |
> |---|---|---|
> | $2$ | $1$ | $0.50$ (50 %) |
> | $8$ | $4$ | $0.20$ (20 %) |
> | $20$ | $10$ | $0.091$ (9.1 %) |
>
> Subir $K_p$ reduce el offset, pero **nunca lo anula**: con $K_p=20$ aún queda 9 % de error.
>
> **Paso 2 — Polos de lazo cerrado.** El denominador es $1+K_p G(s)=0$:
> $$(s+1)(s+2)+K_p = s^2+3s+(2+K_p)=0.$$
> Comparando con $s^2+2\zeta\omega_n s+\omega_n^2$:
> $$\omega_n=\sqrt{2+K_p},\qquad \zeta=\frac{3}{2\sqrt{2+K_p}}.$$
>
> **Paso 3 — Amortiguamiento y sobrepico.** Con $M_p=e^{-\pi\zeta/\sqrt{1-\zeta^2}}$:
>
> | $K_p$ | $\omega_n$ | $\zeta$ | Régimen | $M_p$ |
> |---|---|---|---|---|
> | $2$ | $2.0$ | $0.75$ | subamortiguado | $2.8\%$ |
> | $8$ | $3.16$ | $0.47$ | subamortiguado | $18\%$ |
> | $20$ | $4.69$ | $0.32$ | subamortiguado | $35\%$ |
>
> **Paso 4 — Lectura.** Al multiplicar $K_p$ por 10 (de 2 a 20): $\omega_n$ sube (respuesta más rápida, menor $t_r$), $e_{ss}$ cae de 50 % a 9 %, pero $\zeta$ baja de 0.75 a 0.32 y el sobrepico salta de 3 % a 35 %. Es el **compromiso rígido** de $P$: velocidad y error mejoran a costa de la estabilidad, sin poder separarlos.

> [!ejemplo] Respuesta al escalón variando $K_p$
> ![[p_efecto_kp_escalon.svg|550]]
>
> Mayor $K_p$ ⇒ respuesta más rápida y menor error, pero más oscilatoria, tal como predicen las tablas anteriores.

---

## En qué consiste

> [!info] Al aumentar $K_p$
> | Métrica | Efecto |
> |---|---|
> | Tiempo de subida $t_r$ | baja (más rápido) |
> | Sobrepico $M_p$ | sube |
> | Error estacionario $e_{ss}$ | baja (no lo elimina) |
> | Estabilidad | empeora (polos hacia el eje $j\omega$) |

> [!teoria] Mira solo el presente
> La acción $P$ responde al valor **actual** del error: cuanto mayor es $e(t)$, mayor es la corrección $u(t)=K_p e(t)$. No tiene memoria del pasado (eso es la [[Integral I | I]]) ni anticipa el futuro (eso es la [[Derivativo D | D]]). Por eso, cuando el error se hace pequeño la corrección también se hace pequeña, y el sistema se "estanca" en un punto donde la corrección residual equilibra justo lo que falta: el **offset**.

---

## El control P no elimina el error

> [!teorema]
> Para una planta sin integradores (tipo 0) y realimentación unitaria, el error de [[Coeficientes Kp Kv Ka | posición]] ante escalón es
> $$e_{ss} = \frac{1}{1 + K_p\,G(0)} \neq 0.$$
> Aumentar $K_p$ lo reduce pero nunca lo anula: siempre queda un **offset** (sesgo). Eliminarlo requiere [[Integral I | acción integral]].

> [!demostracion]
> Con $G_c = K_p$ y planta $G(s)$, el error ante escalón unitario por el [[Formula General | teorema del valor final]]:
> $$e_{ss} = \lim_{s\to0} s\,\frac{1}{1 + K_p G(s)}\frac{1}{s} = \frac{1}{1 + K_p G(0)}.$$
> Finito y no nulo salvo que $G(0)=\infty$ (planta con integrador).

> [!info] Efecto sobre los polos
> Variar $K_p$ desplaza los polos de lazo cerrado a lo largo del [[Lugar Raices/index | lugar de las raíces]]: aumentar $K_p$ los lleva hacia los ceros (o al infinito), típicamente acercándolos al eje imaginario y reduciendo el [[Segundo Orden/index | amortiguamiento]] $\zeta$. La acción $P$ **mueve sobre** el lugar, no lo reconfigura.

---

## Limitaciones

> [!warning]
> - **Offset** inevitable en plantas tipo 0.
> - Compromiso rígido: subir $K_p$ mejora velocidad y error pero empeora estabilidad y sobrepico, sin grados de libertad para separarlos.
>
> El control puramente proporcional conviene cuando un offset residual es **tolerable**, cuando la planta ya tiene un integrador (tipo $\geq1$, que anula el error por sí solo), o cuando se busca simplicidad y robustez sin los problemas de $I$ y $D$.

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Ley de control | $u=K_p\,e$ |
> | $G_c(s)$ | $K_p$ |
> | Info del error | presente |
> | Fase aportada | $0^\circ$ |
> | $e_{ss}$ (escalón, tipo 0) | $1/(1+K_p G(0))\neq0$ |
> | Al subir $K_p$ | $t_r\downarrow$, $e_{ss}\downarrow$, $M_p\uparrow$, estabilidad $\downarrow$ |

> [!corolario]
> La acción $P$ corrige en proporción al error actual: es rápida y simple, pero deja un **offset** en plantas tipo 0 y endurece el compromiso velocidad–estabilidad. Para anular el offset se añade [[Integral I | I]] ([[PI]]); para recuperar amortiguamiento, [[Derivativo D | D]] ([[PD]]); ambas cosas, [[PID]].

> [!referencia]
> - Eliminar el offset: [[Integral I]] · [[PI]].
> - Mejorar estabilidad: [[Derivativo D]] · [[PD]].
> - Error estacionario y tipos: [[Coeficientes Kp Kv Ka]] · [[Error Estacionario/index]].
> - Desplazamiento de polos: [[Lugar Raices/index]].
