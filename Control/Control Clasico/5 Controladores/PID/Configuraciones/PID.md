---
title: Controlador PID
tags:
  - control-clasico
  - controladores
  - pid
draft: false
aliases:
  - PID completo
  - control PID
  - proporcional integral derivativo
---

# Controlador PID

> [!definicion]
> El control **proporcional-integral-derivativo** combina las tres [[Acciones/index | acciones]]. En forma estándar (ISA) y en forma paralela:
> $$G_c(s)=K_p\left(1+\frac{1}{T_i s}+T_d s\right)=K_p+\frac{K_i}{s}+K_d s=\frac{K_d s^2+K_p s+K_i}{s}.$$
> Introduce **un polo en el origen** y **dos ceros** (reales o complejos según las ganancias). Logra a la vez **error estacionario nulo** (vía I) y **buen transitorio** (vía D), lo que ninguna configuración parcial consigue.

> [!info]
> Es la configuración completa de las [[index | combinaciones del PID]], que engloba a [[PI | PI]] y [[PD | PD]]. Equivale a un compensador **lead-lag**: lag a baja frecuencia (como [[PI]]), lead a media frecuencia (como [[PD]]). Se diseña sobre el [[Lugar Raices/index | lugar de raíces]] o el [[Margenes MF MG | margen de fase]].

---

## Ejemplo

> [!ejemplo]
> **Diseñar un PID completo: anular error y amortiguar a la vez.** Sea la planta (realimentación unitaria)
> $$G(s)=\frac{1}{(s+1)(s+3)}.$$
> Especificaciones: $e_{ss}=0$ a escalón, polos dominantes con $\zeta=0.6$ y $\omega_n=5\ \text{rad/s}$. La planta es tipo 0 y poco amortiguada al subir la ganancia → necesitamos **I** (error) **y D** (amortiguamiento): un PID.
>
> **Paso 1 — Polos deseados.** Con $\zeta=0.6$, $\omega_n=5$:
> $$s_{1,2}=-\zeta\omega_n\pm j\,\omega_n\sqrt{1-\zeta^2}=-3\pm j\,5(0.8)=-3\pm j\,4.$$
>
> **Paso 2 — Estrategia de los dos ceros.** Factorizamos $G_c(s)=\dfrac{K_d(s+z_1)(s+z_2)}{s}$:
> - El **polo en el origen + cero $z_1$ cercano** ⇒ acción **lag**: anula $e_{ss}$ sin mover los polos dominantes. Lo colocamos cerca del origen: $z_1=0.5$.
> - El **cero $z_2$ a media frecuencia** ⇒ acción **lead**: aporta el adelanto de fase para alcanzar $s_1$.
>
> **Paso 3 — Cancelar un polo de la planta (truco habitual).** Elegimos $z_2$ para cancelar el polo en $-1$ de la planta: $z_2=1$. El lazo abierto queda
> $$G_cG=\frac{K_d(s+0.5)(s+1)}{s}\cdot\frac{1}{(s+1)(s+3)}=\frac{K_d(s+0.5)}{s(s+3)}.$$
>
> **Paso 4 — Condición de ángulo en $s_1=-3+j4$.** Ángulos hacia $s_1$:
> $$\theta_{s=0}=180^\circ-\arctan\tfrac{4}{3}=180^\circ-53.1^\circ=126.9^\circ,\quad \theta_{s=-3}=90^\circ,\quad \phi_{z=0.5}=180^\circ-\arctan\tfrac{4}{2.5}=180^\circ-58^\circ=122^\circ.$$
> Suma: $\angle G_cG=\phi_{z}-\theta_{s=0}-\theta_{s=-3}=122^\circ-126.9^\circ-90^\circ=-94.9^\circ$. Falta poco para $-180^\circ$; ajustando $z_1$ (p. ej. $z_1\approx0.5$–$0.6$) se cumple la condición sobre la rama. Tomamos $z_1=0.5$ como diseño aproximado.
>
> **Paso 5 — Ganancia por condición de módulo** $|G_cG(s_1)|=1$ con $z_1=0.5$:
> $$|s_1+0.5|=|{-2.5+j4}|=4.72,\quad|s_1|=|{-3+j4}|=5,\quad|s_1+3|=4.$$
> $$K_d\cdot\frac{4.72}{5\cdot4}=1\;\Rightarrow\;K_d=\frac{5\cdot4}{4.72}=4.24.$$
>
> **Paso 6 — Recuperar las ganancias del PID.** De $G_c=K_d(s+z_1)(s+z_2)/s=K_d(s+0.5)(s+1)/s=K_d\dfrac{s^2+1.5s+0.5}{s}$, e igualando con $\dfrac{K_d s^2+K_p s+K_i}{s}$:
> $$K_d=4.24,\qquad K_p=4.24\cdot1.5=6.36,\qquad K_i=4.24\cdot0.5=2.12.$$
> Y en forma ISA: $T_i=K_p/K_i=6.36/2.12=3.0\ \text{s}$, $T_d=K_d/K_p=4.24/6.36=0.667\ \text{s}$.
>
> **Paso 7 — Verificación del efecto.**
> - **Error estacionario:** el polo en el origen hace el sistema tipo 1 ⇒ $e_{ss}=0$ a escalón.
> - **Transitorio:** los polos dominantes quedan en $\approx-3\pm j4$ ($\zeta=0.6$, $\omega_n=5$): sobrepico $M_p\approx9\%$ y $t_s\approx4/(\zeta\omega_n)=4/3\approx1.3\ \text{s}$.
> - **Resumen:** el cero $z_2=1$ aporta el lead (amortigua), el par integrador$+z_1=0.5$ aporta el lag (anula offset). El PID consigue **ambos objetivos a la vez**, imposible con PI o PD por separado.

> [!ejemplo] Comparación P, PI, PD, PID
> ![[pid_comparacion_configuraciones.svg|600]]
>
> El PID combina lo mejor: respuesta rápida (P), sin offset (I) y bien amortiguada (D) — el equilibrio de las cuatro métricas.

---

## En qué consiste

> [!teoria]
> El PID es la superposición de tres respuestas al error: al **valor** ($K_p$), a su **acumulación** ($K_i/s$, anula offset) y a su **tendencia** ($K_d s$, amortigua). Su FT tiene un polo fijo en el origen y dos ceros ajustables, que son los dos grados de libertad del diseño: uno se usa para el lag (cerca del origen) y otro para el lead (a media frecuencia, cerca de los polos dominantes o cancelando un polo lento de la planta).

> [!teorema] PID como compensador lead-lag
> Factorizando los dos ceros:
> $$G_c(s)=\frac{K_d(s+z_1)(s+z_2)}{s}.$$
> - Polo en el origen + cero cercano $z_1$ ⇒ acción **lag** (elimina error estacionario, [[PI | como PI]]).
> - Cero $z_2$ a media frecuencia ⇒ acción **lead** (amortigua, [[PD | como PD]]).
>
> El PID es un **lead-lag**: lag a baja frecuencia, lead a media frecuencia.

> [!info] Representaciones equivalentes
> | Forma | Expresión | Relaciones |
> |---|---|---|
> | Paralela | $K_p+\dfrac{K_i}{s}+K_d s$ | — |
> | Estándar (ISA) | $K_p\left(1+\dfrac{1}{T_i s}+T_d s\right)$ | $T_i=K_p/K_i,\; T_d=K_d/K_p$ |
> | Serie | $K_p'\left(1+\dfrac{1}{T_i' s}\right)(1+T_d' s)$ | factorizada |
>
> La forma estándar es la más usada en sintonización ([[Ziegler Nichols Oscilacion | Ziegler-Nichols]]).

> [!regla] Procedimiento de diseño
> 1. Definir especificaciones: $e_{ss}$, $M_p$, $t_s$ → traducir a $\zeta$, $\omega_n$ ([[Segundo Orden/index | polos deseados]]).
> 2. ¿Hace falta anular el error? → incluir **I** (cero $z_1$ cerca del origen).
> 3. ¿Falta amortiguamiento? → incluir **D** (cero $z_2$ a media frecuencia).
> 4. Ubicar los ceros vía [[Lugar Raices/index | lugar de raíces]] (condición de ángulo) o [[Margenes MF MG | margen de fase]].
> 5. Calcular la ganancia (condición de módulo) y ajustar; [[Sintonizacion/index | Ziegler-Nichols]] como punto de partida.

---

## Limitaciones

> [!warning] Filtro del derivativo y correcciones industriales
> El término $K_d s$ es impropio; el PID real filtra la derivada:
> $$G_c(s)=K_p+\frac{K_i}{s}+\frac{K_d s}{1+s/N},\qquad N\approx 8\text{–}20.$$
> Además se aplica [[Integral I | anti-windup]] (evita el *windup* del integrador ante saturación) y [[Derivativo D | derivada sobre la medición]] (evita el *kick* derivativo ante cambios de referencia). Estas tres correcciones son estándar en cualquier PID industrial. La sintonización de tres parámetros también es más laboriosa que la de PI o PD.

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | FT (ISA) | $G_c(s)=K_p\left(1+\dfrac{1}{T_i s}+T_d s\right)$ |
> | FT (paralela) | $\dfrac{K_d s^2+K_p s+K_i}{s}=\dfrac{K_d(s+z_1)(s+z_2)}{s}$ |
> | Aporta | polo en el origen + dos ceros |
> | Equivale a | compensador **lead-lag** |
> | Error estacionario | **eliminado** (escalón) |
> | Sobrepico / amortiguamiento | **mejora** (acción D) |
> | Velocidad | buena (acción P) |
> | Ruido | amplifica (requiere filtro de D) |
> | Coste | sintonizar 3 parámetros |

> [!corolario]
> El PID es la combinación completa: su polo en el origen anula el error estacionario y sus dos ceros se reparten entre el lag (cerca del origen) y el lead (a media frecuencia), logrando simultáneamente $e_{ss}=0$ y buen transitorio. Es la unión de [[PI | PI]] y [[PD | PD]] y, por ello, el controlador de propósito general por excelencia. El precio es mayor complejidad de implementación (filtro, anti-windup) y de sintonización.

> [!referencia]
> - Acciones y configuraciones parciales: [[Acciones/index]] · [[PI]] · [[PD]].
> - Diseño: [[Lugar Raices/index]] · [[Margenes MF MG]] · [[Segundo Orden/index]].
> - Marco general: [[index]].
> - Sintonización sistemática: [[Sintonizacion/index]] · [[Ziegler Nichols Oscilacion]].
