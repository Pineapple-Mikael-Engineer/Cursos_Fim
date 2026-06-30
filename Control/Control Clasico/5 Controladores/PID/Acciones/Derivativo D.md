---
title: Acción Derivativa $D$
order: 3
tags:
  - control-clasico
  - controladores
  - pid
draft: false
aliases:
  - acción derivativa
  - control D
  - derivativo
---

# Acción Derivativa $D$

> [!definicion]
> La señal de control es proporcional a la **velocidad de cambio** del error (su tendencia futura):
> $$u(t) = K_d\,\frac{de(t)}{dt}, \qquad G_c(s) = K_d\,s.$$
> Acción **anticipatoria**: reacciona a hacia dónde va el error, no a su valor actual. Aporta $+90^\circ$ de fase, añade amortiguamiento y **mejora la estabilidad**, pero no corrige el error estacionario y amplifica el ruido.

> [!info]
> Es la acción "predictiva" del [[PID/index | controlador PID]], hermana de la [[Proporcional P | proporcional]] y la [[Integral I | integral]]; las tres se comparan en [[index | Acciones P, I, D]]. Hace lo contrario que la $I$: la $D$ **estabiliza** lo que la $I$ desestabiliza. Combinada con $P$ da el compensador [[PD | PD]] (tipo lead).

---

## Ejemplo

> [!ejemplo]
> **Amortiguamiento que aporta la acción D.** Planta de segundo orden poco amortiguada $G(s)=\dfrac{4}{s^2+0.4s}$ (un integrador + polo lento) con realimentación unitaria. Comparamos $P$ solo ($G_c=K_p$) con $PD$ ($G_c=K_p+K_d s$), fijando $K_p=1$.
>
> **Paso 1 — Solo $P$.** El polinomio característico $1+K_p G(s)=0$:
> $$s^2+0.4s+4K_p = s^2+0.4s+4=0\ \Rightarrow\ \omega_n=2,\quad \zeta=\frac{0.4}{2\cdot2}=0.10.$$
> Con $\zeta=0.10$ el sobrepico es $M_p=e^{-\pi\zeta/\sqrt{1-\zeta^2}}\approx73\%$: muy oscilatorio.
>
> **Paso 2 — Añadir $D$.** Ahora $1+(K_p+K_d s)G(s)=0$:
> $$s^2+0.4s+4(K_p+K_d s)=s^2+(0.4+4K_d)s+4=0.$$
> El término de la derivada **suma amortiguamiento** sin tocar $\omega_n$ (sigue siendo 2):
> $$\zeta=\frac{0.4+4K_d}{2\cdot2}=0.10+K_d.$$
>
> **Paso 3 — Barrido de $K_d$.**
>
> | $K_d$ | $\zeta=0.10+K_d$ | $M_p$ | Comportamiento |
> |---|---|---|---|
> | $0$ | $0.10$ | $73\%$ | $P$ solo: muy oscilatorio |
> | $0.3$ | $0.40$ | $25\%$ | bastante amortiguado |
> | $0.6$ | $0.70$ | $4.6\%$ | casi sin sobrepico |
> | $0.9$ | $1.00$ | $0\%$ | críticamente amortiguado |
>
> **Paso 4 — Lectura.** $D$ inyecta amortiguamiento $\zeta$ directamente (aquí $\zeta=0.10+K_d$) sin alterar $\omega_n$ ni la rapidez: baja el sobrepico de 73 % a 0 sin volver lenta la respuesta. Nótese que **no cambia el error estacionario** (el término $K_d s$ se anula en $s=0$, no aporta a $G(0)$): solo amortigua.

> [!ejemplo] Efecto de la acción derivativa
> ![[d_efecto_kd_escalon.svg|550]]
>
> La acción $D$ reduce el sobrepico y las oscilaciones; "frena" la respuesta antes de que sobrepase.

---

## En qué consiste

> [!info] Al aumentar $K_d$
> | Métrica | Efecto |
> |---|---|
> | Sobrepico $M_p$ | baja |
> | Tiempo de establecimiento $t_s$ | baja |
> | Estabilidad | **mejora** (amortigua) |
> | Error estacionario | no afecta |
> | Tiempo de subida $t_r$ | cambia poco |

> [!teoria] Anticipación
> La derivada del error estima hacia dónde va: si el error disminuye rápido, $D$ **reduce** la acción antes de llegar a la referencia, evitando el sobrepico. Es como un amortiguador que se opone a la velocidad — añade amortiguamiento $\zeta$ efectivo al [[Segundo Orden/index | sistema]] (como en el ejemplo, $\zeta=0.10+K_d$).

> [!teorema] Adelanto de fase
> El derivativo aporta $+90^\circ$ de fase, aumentando el [[Margenes MF MG | margen de fase]]:
> $$\angle G_c(j\omega) = \angle(K_d\,j\omega) = +90^\circ.$$
> Es lo opuesto a la [[Integral I | acción integral]]: la $D$ **estabiliza** lo que la $I$ desestabiliza.

---

## Coste: amplificación de ruido

> [!warning] El derivativo amplifica el ruido
> La ganancia $|G_c(j\omega)| = K_d\,\omega$ **crece** con la frecuencia: el ruido de medición de alta frecuencia se amplifica enormemente, saturando el actuador. Es el defecto crítico de la acción $D$ pura.

> [!regla] Derivativo filtrado (realizable)
> En la práctica nunca se usa $K_d s$ puro (impropio, irrealizable), sino con un **polo de filtro**:
> $$G_c(s) = \frac{K_d\,s}{1 + \dfrac{s}{N}} , \qquad N \approx 5\text{–}20.$$
> El polo en $s=-N$ limita la ganancia a alta frecuencia a $K_d N$, atenuando el ruido. Es lo que implementan los PID reales.

> [!info] *Derivative on measurement*
> Para evitar el **"derivative kick"** (impulso enorme cuando la referencia cambia en escalón), se deriva la **salida** $y$ en vez del error $e$:
> $$u_D = -K_d\,\dot y \quad\text{en lugar de}\quad K_d\,\dot e.$$
> Como $\dot r = 0$ salvo en los saltos de referencia, el comportamiento ante perturbaciones es idéntico pero sin el pico al cambiar la consigna.

---

## Limitaciones

> [!warning]
> - **Ruido alto:** el derivativo lo amplifica; a veces se omite (control PI).
> - **No corrige error estacionario:** debe combinarse con $P$ (y a menudo $I$).
> - **Señales con saltos:** requiere filtrado y derivada sobre la medición.

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Ley de control | $u=K_d\,\dot e$ |
> | $G_c(s)$ | $K_d\,s$ |
> | Info del error | tendencia (futuro) |
> | Fase aportada | $+90^\circ$ |
> | Error estacionario | no afecta |
> | Al subir $K_d$ | $M_p\downarrow$, $t_s\downarrow$, estabilidad $\uparrow$, ruido $\uparrow$ |
> | Forma realizable | $\dfrac{K_d s}{1+s/N}$ |

> [!corolario]
> La acción $D$ deriva el error para anticipar su evolución: inyecta amortiguamiento (mejora $\zeta$, baja el sobrepico) y suma $+90^\circ$ de fase, justo lo contrario que la [[Integral I | I]]. No corrige offset (debe ir con $P$, [[PD]]) y amplifica el ruido, por lo que siempre se filtra y se deriva sobre la medición. Junto a $P$ e $I$ completa el [[PID]].

> [!referencia]
> - Combinación con P (compensador lead): [[PD]].
> - PID completo: [[PID]].
> - Compensar el retardo de la integral: [[Integral I]].
> - Margen de fase y amortiguamiento: [[Margenes MF MG]] · [[Segundo Orden/index]].
