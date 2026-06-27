---
title: "Ciclo Rankine"
order: 1
tags:
  - termodinamica
  - ciclos
  - rankine
  - vapor
  - index
draft: false
aliases:
  - Rankine
  - Ciclo Rankine
  - vapor cycle
---

# Ciclo Rankine

> [!definicion]
> El **ciclo Rankine** es el ciclo estándar de las plantas de potencia de vapor. Usa agua como fluido de trabajo, aprovechando que la compresión de un líquido requiere casi ningún trabajo (a diferencia de comprimir un gas). El fluido pasa por cuatro dispositivos en serie: **bomba** (compresión del líquido), **caldera** (evaporación y sobrecalentamiento), **turbina** (expansión con producción de trabajo) y **condensador** (condensación a baja presión). El ciclo convierte calor de combustión o nuclear en trabajo eléctrico.
>
> *¿Por qué vapor de agua y no otro fluido?* El agua tiene alta entalpía de vaporización ($h_{fg} \approx 2257\,\mathrm{kJ/kg}$ a $100°\mathrm{C}$), es no tóxica, barata y estable. La región bifásica permite transferir grandes cantidades de calor a temperatura constante (isoterma de saturación), acercándose al comportamiento de Carnot.

![[rankine_esquema_planta.svg|500]]
*Esquema de planta de vapor con ciclo Rankine. Los cuatro dispositivos: bomba (1→2), caldera (2→3), turbina (3→4), condensador (4→1). Las numeraciones de estado se usan en todos los balances.*

---

## Los cuatro procesos del ciclo

> [!teoria]
> | Estado | Proceso | Dispositivo | Hipótesis |
> |:---:|:---|:---:|:---|
> | $1\to2$ | Compresión isentrópica del líquido | Bomba | $s_2=s_1$, incompresible |
> | $2\to3$ | Adición de calor isobárica | Caldera | $P=\text{cte}$, $w=0$ |
> | $3\to4$ | Expansión isentrópica | Turbina | $s_4=s_3$, adiabática |
> | $4\to1$ | Rechazo de calor isobárico | Condensador | $P=\text{cte}$, $w=0$, hasta $x=0$ |
>
> El estado 1 es **líquido saturado** a la presión del condensador ($x_1=0$).
> El estado 3 es **vapor sobrecalentado** o vapor saturado a la presión de la caldera.
> El estado 4 puede ser **mezcla líquido-vapor** o vapor sobrecalentado.

---

## Diagramas $T$-$s$ y $P$-$h$

![[rankine_diagrama_Ts.svg|440]]
*Diagrama $T$-$s$ del ciclo Rankine. El proceso $2\to3$ es la adición de calor: primero calienta el líquido (tramo 2→2'), luego lo evapora a $T_{\rm sat}$ (2'→2'') y finalmente sobrecalienta el vapor (2''→3). La eficiencia mejora cuando la temperatura media de adición de calor se acerca a $T_3$.*

![[rankine_diagrama_Ph.svg|440]]
*Diagrama $P$-$h$ del ciclo Rankine. La expansión en la turbina (3→4) puede cruzar la campana de saturación (región húmeda). La calidad $x_4 < 1$ limita el diseño: la ASME recomienda $x_4 \geq 0.88$ para evitar erosión de los álabes por impacto de gotitas.*

---

## Balances de energía

> [!proposicion]
> Aplicando la primera ley a cada dispositivo (flujo estacionario, sin cambios de EC ni EP):
>
> **Bomba** ($1\to2$, isentrópica):
> $$
> w_P = v_1(P_2 - P_1) \approx h_2 - h_1 \qquad [\mathrm{kJ/kg}].
> $$
>
> **Caldera** ($2\to3$, isobárica):
> $$
> q_H = h_3 - h_2 \qquad [\mathrm{kJ/kg}].
> $$
>
> **Turbina** ($3\to4$, isentrópica):
> $$
> w_T = h_3 - h_4 \qquad [\mathrm{kJ/kg}].
> $$
>
> **Condensador** ($4\to1$, isobárico):
> $$
> q_L = h_4 - h_1 \qquad [\mathrm{kJ/kg}].
> $$

> [!demostracion]
> **Deducción del trabajo de bomba como $v_1 \Delta P$.**
>
> **Hipótesis:** fluido incompresible ($v \approx v_1 = \text{cte}$), proceso isentrópico.
>
> **Paso 1.** Primera ley para VC estacionario, adiabático, sin EC ni EP:
> $w_P = -(h_2 - h_1)$ (el trabajo es suministrado al fluido: convenio $w_P > 0$).
>
> **Paso 2.** Para proceso isentrópico de fluido incompresible, la ecuación de Gibbs $dh = T\,ds + v\,dP$ con $ds=0$ da: $dh = v\,dP$.
>
> **Paso 3.** Como $v \approx v_1 = \text{cte}$:
> $$
> h_2 - h_1 = \int_1^2 v\,dP = v_1(P_2-P_1). \qquad \blacksquare
> $$
>
> *Interpretación física:* comprimir un líquido cuesta muy poco trabajo porque su volumen específico $v_1 \approx 10^{-3}\,\mathrm{m^3/kg}$ es 1000 veces menor que el de un gas. En el ciclo Rankine, $w_P \ll w_T$, lo que es la principal ventaja sobre el ciclo Brayton (donde el compresor consume 40% del trabajo de turbina).

---

## Eficiencia y relación de retrabajo

> [!proposicion]
> **Eficiencia térmica** del ciclo Rankine:
> $$
> \eta_{\rm th} = \frac{w_T - w_P}{q_H} = \frac{(h_3-h_4)-(h_2-h_1)}{h_3-h_2}.
> $$
>
> **Relación de retrabajo** (back work ratio):
> $$
> \text{bwr} = \frac{w_P}{w_T} = \frac{h_2-h_1}{h_3-h_4} \approx 0.5\text{–}2\%
> $$
> (muy pequeña comparada con el ciclo Brayton donde bwr $\approx$ 40–80%).

---

## Formas de mejorar la eficiencia

El límite $\eta_{\rm th} \leq \eta_{\rm Carnot}(T_H^{\rm max}, T_L)$ se puede acercar mediante:

| Estrategia | Efecto | Nota |
|:---|:---|:---|
| Aumentar $P$ de la caldera | ↑ $T_{m,{\rm entrada}}$, ↑ $\eta_{\rm th}$ | Limita $x_4$ → vapor húmedo |
| Aumentar $T_{\rm sup}$ (sobrecalentamiento) | ↑ $T_{m,{\rm entrada}}$, ↑ $x_4$ | Limitado por resistencia de materiales |
| Reducir $P$ del condensador | ↓ $T_L$, ↑ $\eta_{\rm th}$ | $T_L \geq T_{\rm ambiente}$ |
| Recalentamiento | Evita vapor húmedo; ↑ $w_T$ | Ver [[Rankine con Recalentamiento]] |
| Regeneración | ↑ $T_{m,{\rm entrada}}$ | Ver [[Rankine Regenerativo]] |

---

## Mapa de notas

> [!info]
> - [[Rankine Simple]] — ciclo básico con 4 estados; ejemplo completo con tablas de vapor a 5 MPa/500°C.
> - [[Rankine con Recalentamiento]] — expansión en dos etapas con recalentamiento intermedio; mejora calidad y eficiencia.
> - [[Rankine Regenerativo]] — extracción de vapor para calentar el condensado; calentador abierto de alimentación.

> [!referencia]
> Borgnakke & Sonntag, *Fundamentals of Thermodynamics*, cap. 11; Çengel & Boles, *Termodinámica*, §10-1 a 10-4; Moran & Shapiro, §8.1–8.5.
