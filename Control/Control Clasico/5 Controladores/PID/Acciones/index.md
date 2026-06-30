---
title: Acciones de Control P, I, D
order: 1
tags:
  - control-clasico
  - controladores
  - pid
  - index
draft: false
aliases:
  - acciones P I D
  - acciones de control
  - términos del PID
---

# Acciones de Control P, I, D

> [!definicion]
> El [[PID/index | controlador PID]] suma tres acciones que actúan sobre distintas características temporales del error $e(t)$ —presente, pasado y futuro:
> $$u(t) = \underbrace{K_p\,e(t)}_{\text{presente}} + \underbrace{K_i\!\int e\,d\tau}_{\text{pasado}} + \underbrace{K_d\,\dot e(t)}_{\text{futuro}}.$$
> Cada término tiene su propio efecto sobre rapidez, error estacionario y estabilidad; combinarlos da los controladores [[PI]], [[PD]] y [[PID]].

> [!info] [[Proporcional P | Acción proporcional $P$]]
> $u=K_p e$, $G_c=K_p$. Responde al error **presente**; reduce $e_{ss}$ y acelera la respuesta, pero deja **offset** en plantas tipo 0 y empeora la estabilidad. Aporta $0^\circ$ de fase.

> [!info] [[Integral I | Acción integral $I$]]
> $u=K_i\int e\,d\tau$, $G_c=K_i/s$. Acumula el error **pasado**; sube el tipo del sistema y **elimina el error estacionario**, pero aporta $-90^\circ$ de fase y desestabiliza (riesgo de *windup*).

> [!info] [[Derivativo D | Acción derivativa $D$]]
> $u=K_d\dot e$, $G_c=K_d s$. Anticipa el error **futuro** por su pendiente; añade amortiguamiento y **mejora la estabilidad** ($+90^\circ$ de fase), pero no corrige $e_{ss}$ y amplifica el ruido.

---

## Ejemplo

> [!ejemplo]
> **Las tres acciones sobre la misma planta.** Planta poco amortiguada $G(s)=\dfrac{4}{s^2+0.4s}$ con realimentación unitaria. Vemos qué hace cada término al pasar de $P$ a $PI$ y a $PD$ (base de partida $K_p=1$).
>
> **Solo $P$ ($G_c=1$).** Característica $s^2+0.4s+4=0\Rightarrow\omega_n=2,\ \zeta=0.10$. Respuesta rápida pero muy oscilatoria ($M_p\approx73\%$). Como esta planta ya tiene un integrador (tipo 1), aquí $e_{ss}=0$ ante escalón sin necesidad de $I$.
>
> **Añadir $I$ → $PI$ ($G_c=1+K_i/s$).** Para una planta tipo 0 el integrador anularía el offset que $P$ deja; el coste es $-90^\circ$ de fase: el polinomio gana un grado ($s^3+0.4s^2+4s+4K_i=0$) y, subiendo $K_i$, el sobrepico crece y puede inestabilizar.
>
> **Añadir $D$ → $PD$ ($G_c=1+K_d s$).** Característica $s^2+(0.4+4K_d)s+4=0\Rightarrow\zeta=0.10+K_d$. El derivativo **inyecta amortiguamiento** sin tocar $\omega_n$:
>
> | Acción | $\zeta$ efectivo | $M_p$ | Qué cambia |
> |---|---|---|---|
> | $P$ ($K_d=0$) | $0.10$ | $73\%$ | rápido pero oscila |
> | $PD$, $K_d=0.3$ | $0.40$ | $25\%$ | menos sobrepico |
> | $PD$, $K_d=0.6$ | $0.70$ | $4.6\%$ | casi sin sobrepico |
>
> **Lectura.** $P$ fija la rapidez, $I$ borra el error estacionario residual (a costa de fase y estabilidad) y $D$ amortigua (sube $\zeta$, baja $M_p$). El $PID$ las usa juntas para tener velocidad, error nulo y buen amortiguamiento a la vez.

> [!ejemplo] Las tres acciones ante un escalón
> ![[pid_efecto_acciones_escalon.svg|600]]
>
> Cada acción modifica la respuesta de forma característica: $P$ acelera, $I$ anula el offset, $D$ amortigua.

---

## Comparación

> [!info] Las tres acciones de un vistazo
> | | [[Proporcional P \| Proporcional]] | [[Integral I \| Integral]] | [[Derivativo D \| Derivativo]] |
> |---|---|---|---|
> | Término | $K_p e$ | $K_i\int e\,d\tau$ | $K_d\,\dot e$ |
> | $G_c(s)$ | $K_p$ | $K_i/s$ | $K_d s$ |
> | Info del error | presente | pasado (acumulado) | tendencia (futuro) |
> | Fase aportada | $0^\circ$ | $-90^\circ$ | $+90^\circ$ |
> | Error estacionario | lo reduce | lo **elimina** | no afecta |
> | Estabilidad | la empeora | la empeora | la **mejora** |
> | Ruido | neutro | filtra | **amplifica** |

> [!teoria] Presente, pasado y futuro
> Cada acción "mira" el error en un tiempo distinto:
> - **P** responde al error **actual** — acción inmediata, pero deja error residual.
> - **I** acumula el error **pasado** — no descansa hasta anular el error, pero introduce retardo.
> - **D** estima el error **futuro** por su pendiente — anticipa y amortigua, pero es sensible al ruido.

> [!info] Aporte de fase
> | Acción | $G_c(j\omega)$ | Fase |
> |---|---|---|
> | P | $K_p$ | $0^\circ$ |
> | I | $K_i/j\omega$ | $-90^\circ$ |
> | D | $K_d\,j\omega$ | $+90^\circ$ |
>
> El integrador **resta** fase (reduce el [[Margenes MF MG | margen de fase]]); el derivativo la **suma** (lo aumenta). Es la base de la equivalencia [[PD | PD]]$\to$lead y [[PI | PI]]$\to$lag.

## Resumen

> [!resumen]
> | Acción | Ley | $G_c(s)$ | Tiempo | $e_{ss}$ | Estabilidad |
> |---|---|---|---|---|---|
> | $P$ | $K_p e$ | $K_p$ | presente | reduce | empeora |
> | $I$ | $K_i\int e\,d\tau$ | $K_i/s$ | pasado | **elimina** | empeora |
> | $D$ | $K_d\dot e$ | $K_d s$ | futuro | no afecta | **mejora** |

> [!corolario]
> Las tres acciones son complementarias: $P$ da la corrección base proporcional al error, $I$ garantiza error estacionario nulo y $D$ aporta amortiguamiento y adelanto de fase. Sus defectos también se compensan —el $-90^\circ$ de la $I$ con el $+90^\circ$ de la $D$—, por lo que combinarlas en [[PI]], [[PD]] o el [[PID]] completo permite cumplir a la vez rapidez, error nulo y estabilidad.

> [!referencia]
> - Detalle de cada acción: [[Proporcional P]] · [[Integral I]] · [[Derivativo D]].
> - Combinaciones: [[Configuraciones/index]].
> - Efecto sobre el error: [[Error Estacionario/index]] · [[Coeficientes Kp Kv Ka]].
> - Efecto sobre la respuesta: [[Segundo Orden/index]].
