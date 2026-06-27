---
title: "Balance de Energía (Volumen de Control)"
order: 2
tags:
  - termodinamica
  - conservacion
  - energia
  - primera_ley
  - volumen_de_control
draft: false
aliases:
  - primera ley VC
  - balance energetico VC
  - conservacion de la energia VC
---

# Balance de Energía — Volumen de Control

> [!definicion]
> La **primera ley de la termodinámica** para un [[Volumenes de Control/index | volumen de control]] fijo en el espacio:
> $$\boxed{\frac{dE_{VC}}{dt} = \dot{Q} - \dot{W} + \sum_i \dot{m}_i\!\left(h_i + \frac{V_i^2}{2} + gz_i\right) - \sum_e \dot{m}_e\!\left(h_e + \frac{V_e^2}{2} + gz_e\right),}$$
> donde:
> - $E_{VC}$ [kJ]: energía total (interna + cinética + potencial) almacenada en el VC.
> - $\dot{Q}$ [kW]: calor neto **que entra** al VC.
> - $\dot{W}$ [kW]: trabajo de eje neto **que sale** del VC (turbina, compresor).
> - $h = u + Pv$ [kJ/kg]: entalpía específica — incluye el trabajo de flujo $Pv$.
>
> **Diferencia esencial con el SC:** en el SC la energía transportada por la masa es $u$; en el VC es $h = u + Pv$ porque el fluido que entra "empuja" contra la presión, realizando trabajo de flujo. Ver la derivación completa en [[Entalpia]].

---

## Derivación: por qué $h$ y no $u$ en los balances de flujo

> [!demostracion]
> **Meta:** mostrar que al aplicar el balance de energía a un VC, la energía transportada por la corriente de flujo es $h$, no $u$.
>
> **Hipótesis:** VC fijo en el espacio, fluido entrando por la sección 1 (presión $P_1$, velocidad $V_1$, área $A_1$). Consideramos 1 kg de fluido que entra en un intervalo de tiempo $dt$.
>
> **Paso 1 — Energía del kilogramo de fluido entrante.**
> El kg de fluido que entra al VC trae su energía interna $u_1$ [kJ/kg]. También trae energía cinética $V_1^2/2$ y potencial $gz_1$. La energía total que "posee" es $u_1 + V_1^2/2 + gz_1$.
>
> **Paso 2 — Trabajo de flujo: el fluido de atrás empuja.**
> Para que ese kg entre al VC, el fluido que viene detrás ejerce una fuerza $P_1 A_1$ sobre él. Para desplazarlo a través de la sección (ocupando su volumen $v_1\cdot 1\,\text{kg} = v_1\,\text{m}^3$), realiza un trabajo:
> $$W_{\rm flujo,\,ent} = P_1\cdot(A_1\cdot v_1/A_1) = P_1\,v_1 \quad [\text{kJ/kg}].$$
> Este trabajo lo "paga" el fluido corriente arriba; no lo paga ninguna fuente de trabajo de eje.
>
> **Paso 3 — Energía total aportada por 1 kg de fluido entrante.**
> La energía total que llega al VC por cada kg que entra es:
> $$e_{\rm total,\,ent} = u_1 + P_1 v_1 + \frac{V_1^2}{2} + gz_1 = h_1 + \frac{V_1^2}{2} + gz_1.$$
>
> **Paso 4 — Análisis equivalente en la salida.**
> Al salir, el kg del fluido empuja el fluido que viene detrás contra $P_e$: ese trabajo de flujo $P_e v_e$ sale del VC. La energía que "lleva" el kg saliente es $h_e + V_e^2/2 + gz_e$.
>
> **Paso 5 — Ensamble del balance de energía.**
> Aplicando la primera ley al VC (la energía del VC cambia porque entra/sale calor $\dot{Q}$, sale trabajo de eje $\dot{W}$, y los flujos másicos traen y llevan $h + V^2/2 + gz$):
> $$\frac{dE_{VC}}{dt} = \dot{Q} - \dot{W} + \sum_i \dot{m}_i\!\left(h_i + \frac{V_i^2}{2} + gz_i\right) - \sum_e \dot{m}_e\!\left(h_e + \frac{V_e^2}{2} + gz_e\right). \qquad \blacksquare$$

---

## Régimen estacionario (SFSS): la forma más usada

> [!proposicion]
> En **régimen estacionario** ($dE_{VC}/dt = 0$), con una entrada y una salida, $\dot{m}_1 = \dot{m}_2 = \dot{m}$:
> $$\dot{Q} - \dot{W} = \dot{m}\!\left[(h_e - h_i) + \frac{V_e^2 - V_i^2}{2} + g(z_e - z_i)\right].$$
> En forma específica (dividiendo por $\dot{m}$):
> $$q - w = (h_e - h_i) + \frac{V_e^2 - V_i^2}{2} + g(z_e - z_i),$$
> donde $q = \dot{Q}/\dot{m}$ [kJ/kg] y $w = \dot{W}/\dot{m}$ [kJ/kg].

![[balance_energia_VC_SFSS.svg|460]]
*Volumen de control en régimen estacionario (turbina de vapor): el fluido entra por la sección 1 con entalpía $h_1$ y sale por la sección 2 con $h_2 < h_1$. El trabajo de eje $w = h_1 - h_2$ para proceso adiabático. El diagrama muestra también la entalpía de flujo ($Pv$) y la energía interna ($u$) como componentes de $h = u + Pv$.*

---

## Aproximaciones habituales

> [!teoria]
> En la mayoría de los dispositivos termodinámicos, los términos de energía cinética y potencial son despreciables frente a las diferencias de entalpía:
>
> | Dispositivo | Término dominante | ¿Cuándo conservar $V^2/2$? |
> |:---|:---|:---|
> | Turbina de vapor | $h_1 - h_2 \sim 1000\,\text{kJ/kg}$ | Nunca necesario (cinética $\ll 1\,\text{kJ/kg}$) |
> | Compresor | $h_2 - h_1 \sim 100\,\text{kJ/kg}$ | Raramente necesario |
> | Tobera/Difusor | $h_1 - h_2 \sim V^2/2$ | Siempre (es el intercambio $h \leftrightarrow V^2$) |
> | Intercambiador | $h_2 - h_1 \sim 100\,\text{kJ/kg}$ | Raramente necesario |
>
> Para toberas y difusores no hay trabajo de eje ($\dot{W} = 0$) y el balance se reduce a: $h_1 + V_1^2/2 = h_2 + V_2^2/2$ (Bernoulli generalizado).

---

## Casos habituales en régimen estacionario

> [!proposicion]
> **Turbina adiabática** ($\dot{Q} = 0$, un fluido entrante y saliente, $V^2$ y $gz$ despreciables):
> $$w_{\rm turbina} = h_1 - h_2 > 0 \quad (h_1 > h_2\text{: fluido sale con menos entalpía}).$$
>
> **Compresor/bomba adiabático** ($\dot{Q} = 0$, igual):
> $$w_{\rm compresor} = h_2 - h_1 > 0 \quad (\text{trabajo entra}: w = -\dot{W}/\dot{m} > 0 \text{ en convención de entrada}).$$
> O usando la convención $w > 0$ cuando sale: $w = h_1 - h_2 < 0$.
>
> **Caldera/condensador** ($\dot{W} = 0$):
> $$q = h_e - h_i \quad (\text{positivo si el fluido sale con más entalpía}).$$
>
> **Válvula de estrangulamiento** ($\dot{Q} \approx 0$, $\dot{W} = 0$, $V^2$ y $gz$ despreciables):
> $$h_1 = h_2 \quad (\text{proceso isentálpico}).$$

---

## Ejemplo: turbina de vapor en régimen estacionario

> [!ejemplo]
> **Turbina adiabática.** Vapor entra a $P_1 = 4\,\text{MPa}$, $T_1 = 400\,°\text{C}$ ($h_1 = 3213.6\,\text{kJ/kg}$) y sale a $P_2 = 0.1\,\text{MPa}$ ($h_2 = 2675.5\,\text{kJ/kg}$, vapor saturado). Flujo másico $\dot{m} = 10\,\text{kg/s}$.
>
> **Paso 1 — Identificar hipótesis.** Régimen estacionario, adiabático, $V^2$ y $gz$ despreciables.
>
> **Paso 2 — Balance de energía simplificado.**
> $$w = h_1 - h_2 = 3213.6 - 2675.5 = 538.1\,\text{kJ/kg}.$$
>
> **Paso 3 — Potencia de la turbina.**
> $$\dot{W} = \dot{m}\,w = 10 \times 538.1 = 5381\,\text{kW} = 5.38\,\text{MW}.$$
>
> **Paso 4 — Interpretar.** Cada kilogramo de vapor cedió 538.1 kJ de entalpía al eje de la turbina. El vapor "entra" con una suma de energía interna + trabajo de flujo $Pv$ de 3213.6 kJ/kg y "sale" con 2675.5 kJ/kg. La diferencia es el trabajo mecánico extraído. $\blacksquare$

---

## Relación con otras notas

> [!info]
> - [[Balance de Masa VC]] — determina $\dot{m}$ que aparece en este balance.
> - [[Entalpia]] — explica por qué $h$ (no $u$) aparece aquí: el trabajo de flujo $Pv$.
> - [[Balance de Entropia VC]] — añade la restricción de segunda ley a este balance.
> - [[Sistemas/Dispositivos Flujo/index | Dispositivos de Flujo]] — aplica este balance a turbinas, compresores, toberas, etc.

> [!warning]
> - $\dot{W}$ es el **trabajo de eje** (turbina, compresor); no incluye el trabajo de flujo (ya está en $h$).
> - Los términos cinético $V^2/2$ y potencial $gz$ son [kJ/kg] solo si $V$ es en m/s y $g$ en m/s². No olvidar el factor $10^{-3}$ si se trabaja en kJ: $V^2/(2 \times 10^3)$ [kJ/kg].

> [!referencia]
> Borgnakke & Sonntag, *Fundamentals of Thermodynamics*, §6.3–6.4; Çengel & Boles, *Termodinámica*, §5-2 a 5-5; Moran & Shapiro, §4.2–4.3.
