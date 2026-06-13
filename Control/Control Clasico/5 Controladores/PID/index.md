---
title: Control PID
tags:
  - control-clasico
  - controladores
  - pid
  - index
draft: false
aliases:
  - PID
  - controlador PID
  - control PID
---

# Control PID

> [!definicion]
> El controlador **PID** combina tres acciones sobre el error $e(t)=r(t)-y(t)$: proporcional (presente), integral (pasado acumulado) y derivativa (tendencia).
> $$u(t)=K_p\,e(t)+K_i\!\int_0^t e(\tau)\,d\tau+K_d\,\dot e(t)\quad\Longleftrightarrow\quad G_c(s)=K_p+\frac{K_i}{s}+K_d s=\frac{K_d s^2+K_p s+K_i}{s}.$$
> Forma estándar con tiempos: $G_c(s)=K_p\!\left(1+\tfrac{1}{T_i s}+T_d s\right)$, con $K_i=K_p/T_i$ y $K_d=K_p T_d$.

> [!info]
> Marco de la carpeta **PID** (en [[Lugar Raices/index | Diseño]]). Se desglosa en tres bloques:
> - [[Acciones/index | Acciones P, I, D]] — efecto individual de cada término.
> - [[Configuraciones/index | Configuraciones PI, PD, PID]] — combinaciones y su relación con [[Lead | lead]]/[[Lag | lag]].
> - [[Sintonizacion/index | Sintonización]] — métodos de Ziegler-Nichols para fijar las ganancias.
>
> Es el controlador más usado en la industria: cubre la mayoría de lazos sin necesitar un modelo exacto de la planta.

---

## Ejemplo

> [!ejemplo] Las cuatro configuraciones sobre una misma planta
> Planta $G(s)=\dfrac{1}{(s+1)(s+2)}$ (tipo 0) con realimentación unitaria. Comparar P, PI, PD y PID.
>
> ![[pid_efecto_acciones_escalon.svg|600]]
>
> **Solo P** ($K_p=10$): el lazo cerrado es $\dfrac{10}{s^2+3s+12}$ → $\omega_n=\sqrt{12}\approx3.46$, $\zeta\approx0.43$. Rápido pero con **error estacionario** $e_{ss}=\dfrac{1}{1+K_p\,G(0)}=\dfrac{1}{1+10\cdot0.5}=\dfrac{1}{6}\approx0.17$ y sobrepico.
>
> **PI** (añade $K_i$): introduce un polo en $s=0$ → sistema **tipo 1**, $e_{ss}\to0$ ante escalón. Cuesta algo de velocidad y margen.
>
> **PD** (añade $K_d$): aporta un **cero** que adelanta fase → menos sobrepico y $t_s$ más corto, pero no toca el $e_{ss}$.
>
> **PID** (las tres): el integrador anula $e_{ss}$ y el derivativo amortigua el transitorio que aquel introduce. Es la combinación que **a la vez** sigue sin error y responde bien amortiguada.
>
> **Lectura:** cada acción ataca una deficiencia distinta; el PID las reúne. Cómo elegir entre ellas está en [[Configuraciones/index | configuraciones]].

---

## En qué consiste

> [!teoria] Qué aporta cada acción
> | Acción | Mira | Efecto principal |
> |---|---|---|
> | **[[Proporcional P \| P]]** | el error **presente** | reduce el error; demasiada ganancia oscila |
> | **[[Integral I \| I]]** | el error **pasado** (acumulado) | **elimina** el error estacionario; ralentiza y desestabiliza |
> | **[[Derivativo D \| D]]** | la **tendencia** del error | anticipa, amortigua, mejora estabilidad; amplifica ruido |
>
> El PID equilibra las tres: P actúa, I corrige el sesgo, D estabiliza.

> [!info] Tendencias al aumentar cada ganancia
> | Ganancia | $t_r$ subida | $M_p$ sobrepico | $t_s$ establec. | $e_{ss}$ error | Estabilidad |
> |---|---|---|---|---|---|
> | $K_p\uparrow$ | baja | sube | cambia poco | baja | empeora |
> | $K_i\uparrow$ | baja | sube | sube | **elimina** | empeora |
> | $K_d\uparrow$ | cambia poco | baja | baja | cambia poco | mejora |
>
> Reglas cualitativas (no exactas): sirven para sintonizar a mano. Ver [[Sintonizacion/index | sintonización]] para métodos sistemáticos.

> [!info] PID como compensador lead-lag
> - **[[PD]]** $\equiv$ **lead** (adelanto): añade un cero, mejora el transitorio y el [[Margenes MF MG | margen de fase]].
> - **[[PI]]** $\equiv$ **lag** (retardo): añade un polo en el origen, elimina el [[Error Estacionario/index | error estacionario]].
> - **[[PID]]** $\equiv$ **lead-lag**: combina ambos efectos.

> [!info] En MATLAB
> ```matlab
> C = pid(Kp, Ki, Kd);     % controlador PID (forma paralela)
> T = feedback(C*G, 1);    % lazo cerrado con realimentación unitaria
> step(T), stepinfo(T)     % respuesta y métricas (Mp, ts, ess)
> ```

---

## Resumen

> [!resumen]
> | Pieza | Resultado |
> |---|---|
> | Ley | $u=K_p e+K_i\!\int e+K_d\dot e$ |
> | FT | $G_c(s)=K_p+\dfrac{K_i}{s}+K_d s$ |
> | P | reduce error, no lo anula |
> | I | anula $e_{ss}$ (sube el tipo), desestabiliza |
> | D | amortigua y anticipa, amplifica ruido |
> | Sintonía | [[Sintonizacion/index | Ziegler-Nichols]] |

> [!corolario]
> El PID es la combinación de tres miradas al error —presente, pasado y futuro— y por eso resuelve a la vez precisión (la I anula el error estacionario) y buen transitorio (la D amortigua). Equivale a un compensador lead-lag, lo que lo conecta con el [[Lugar Raices/index | diseño por lugar de raíces]] y por [[Respuesta Frecuencia/index | frecuencia]]. Las acciones individuales viven en [[Acciones/index]], las combinaciones en [[Configuraciones/index]] y el ajuste numérico en [[Sintonizacion/index]].

> [!referencia]
> - Acciones individuales: [[Acciones/index]].
> - Combinaciones P/PI/PD/PID: [[Configuraciones/index]].
> - Ajuste de ganancias: [[Sintonizacion/index]].
> - Efecto sobre polos: [[Lugar Raices/index]]; sobre el error: [[Error Estacionario/index]].
