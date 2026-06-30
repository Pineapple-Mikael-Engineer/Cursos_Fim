---
title: "Volúmenes de Control"
order: 2
tags:
  - termodinamica
  - conservacion
  - volumen_de_control
  - index
draft: false
---

# Volúmenes de Control

> [!definicion]
> Un **volumen de control** (VC) es una región del espacio a través de cuya **superficie de control** puede pasar masa, calor y trabajo. A diferencia del sistema cerrado, la masa contenida en el VC puede variar: fluye hacia adentro por las entradas y hacia afuera por las salidas. Los motores de avión, turbinas, compresores, calderas e intercambiadores de calor son todos volúmenes de control. La superficie de control es la frontera del VC — puede ser real o imaginaria, rígida o móvil.

---

## Por qué la entalpía $h$ aparece en el balance de energía del VC

> [!teoria]
> Esta es **la diferencia más importante** entre SC y VC. En un sistema cerrado, la energía que "pertenece" a la masa es $u$ (energía interna). En un VC, cuando 1 kg de fluido **entra** a través de la superficie de control, no solo trae su energía interna $u$ — la corriente aguas arriba también realiza un **trabajo de flujo** $Pv$ para empujar ese kg hacia adentro. La energía total transportada por el fluido que fluye es:
> $$e_{\rm flujo} = u + Pv = h.$$
> Por esto, todos los balances de energía de VC contienen $h$, no $u$. El trabajo de flujo $Pv$ es un mecanismo de transferencia de energía que no existe en los SC. Ver la demostración completa en [[Entalpia]].
>
> **Analogía:** en un sistema de tuberías a presión, empujar 1 litro de agua a través de una válvula requiere trabajo incluso si no cambia la energía del litro. Ese trabajo es el $Pv$ que la entalpía captura.

---

## El régimen estacionario: hipótesis SFSS

> [!teoria]
> La mayoría de los dispositivos industriales (turbinas, compresores, calderas) operan en **régimen estacionario** (*steady-state, steady-flow*, SFSS): las propiedades en cada punto del VC no cambian con el tiempo, aunque el fluido se mueva. Bajo estas hipótesis:
>
> 1. $dm_{VC}/dt = 0$ → el balance de masa se reduce a $\sum \dot{m}_{\rm ent} = \sum \dot{m}_{\rm sal}$.
> 2. $dE_{VC}/dt = 0$ → el balance de energía se reduce a balancear los flujos de $h$, $\dot{Q}$ y $\dot{W}$.
> 3. $dS_{VC}/dt = 0$ → similar para entropía.
>
> El régimen estacionario es una **idealización potente**: no describe el arranque ni la parada del equipo, pero sí su operación nominal de diseño. Para análisis transitorios (llenado de tanques, descarga de recipientes), se usa el balance general no-estacionario.

---

## Los cuatro balances del VC en forma general y en régimen estacionario

> [!teoria]
> | Balance | Forma general | Régimen estacionario (SFSS) |
> |:---|:---|:---|
> | **Masa** | $\dfrac{dm_{VC}}{dt} = \sum \dot{m}_i - \sum \dot{m}_e$ | $\sum \dot{m}_i = \sum \dot{m}_e$ |
> | **Energía** | $\dfrac{dE_{VC}}{dt} = \dot{Q} - \dot{W} + \sum \dot{m}_i e_i - \sum \dot{m}_e e_e$ | $\dot{Q} - \dot{W} = \sum \dot{m}_e h_e - \sum \dot{m}_i h_i$ |
> | **Entropía** | $\dfrac{dS_{VC}}{dt} = \sum \dfrac{\dot{Q}_k}{T_k} + \dot{S}_{\rm gen} + \sum \dot{m}_i s_i - \sum \dot{m}_e s_e$ | $\dot{S}_{\rm gen} = \sum \dot{m}_e s_e - \sum \dot{m}_i s_i - \sum \dfrac{\dot{Q}_k}{T_k} \ge 0$ |
> | **Exergía** | $\dfrac{dB_{VC}}{dt} = \sum \dot{m}_i \psi_i - \sum \dot{m}_e \psi_e + \sum (1 - T_0/T_k)\dot{Q}_k - \dot{W}_{\rm útil} - \dot{B}_{\rm dest}$ | $\dot{B}_{\rm dest} = T_0 \dot{S}_{\rm gen} \ge 0$ |
>
> Donde $\psi_i = h_i - h_0 - T_0(s_i - s_0)$ es la exergía de flujo del fluido en la entrada $i$.

![[volumen_control_flujos.svg|460]]
*Volumen de control genérico con una entrada (1) y una salida (2), calor $\dot{Q}$ que entra desde una fuente a $T_k$, y trabajo de eje $\dot{W}$ que sale. La superficie de control (línea punteada) define el VC. La entalpía $h_1$ y $h_2$ captura la energía total del fluido incluyendo el trabajo de flujo.*

---

## Casos especiales habituales

> [!proposicion]
> **VC adiabático de flujo estacionario con una entrada y una salida** ($\dot{m}_1 = \dot{m}_2 = \dot{m}$, $\dot{Q} = 0$):
> $$\dot{W} = \dot{m}(h_1 - h_2), \qquad \dot{S}_{\rm gen} = \dot{m}(s_2 - s_1) \ge 0.$$
> Cubre turbinas y compresores ideales ($s_2 = s_1$) y reales ($s_2 > s_1$).
>
> **VC sin trabajo de eje** ($\dot{W} = 0$, $\dot{Q} = 0$, una entrada y salida):
> $$h_1 = h_2.$$
> Cubre válvulas de estrangulamiento (proceso isentálpico).
>
> **VC sin trabajo** pero con $\dot{Q} \ne 0$ y $\dot{m}_1 = \dot{m}_2$:
> $$\dot{Q} = \dot{m}(h_2 - h_1).$$
> Cubre calderas ($h_2 > h_1$) y condensadores ($h_2 < h_1$).

---

## Mapa de notas

> [!info]
> - [[Balance de Masa VC]] (order 1) — ecuación de continuidad; flujo másico $\dot{m} = \rho V A$.
> - [[Balance de Energia VC]] (order 2) — primera ley del VC; por qué $h$ no $u$; SFSS.
> - [[Balance de Entropia VC]] (order 3) — generación de entropía $\dot{S}_{\rm gen}$; dirección del proceso.
> - [[Balance de Exergia VC]] (order 4) — exergía de flujo $\psi$; Gouy-Stodola $\dot{B}_{\rm dest} = T_0\dot{S}_{\rm gen}$.
>
> Para los dispositivos específicos que aplican estos balances: [[Sistemas/Dispositivos Flujo/index | Dispositivos de Flujo]].

> [!referencia]
> Borgnakke & Sonntag, *Fundamentals of Thermodynamics*, cap. 6 (VC general) y cap. 9 (exergía en VC); Çengel & Boles, *Termodinámica*, caps. 5 y 10; Moran & Shapiro, caps. 4–7.
