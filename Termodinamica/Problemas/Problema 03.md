---
title: "Problema 03 — Estrangulamiento de agua en una válvula"
tags:
  - termodinamica
  - problemas
  - volumen_de_control
  - exergia
draft: false
aliases:
  - válvula de estrangulamiento
  - flash isentálpico
  - exergía destruida válvula
---

# Problema 03 — Estrangulamiento de agua en una válvula

> [!definicion] Enunciado
> Agua como líquido saturado a $P_1 = 1.5\ \text{MPa}$ se estrangula en una [[Valvulas | válvula]] adiabática hasta $P_2 = 100\ \text{kPa}$. Se desprecian los cambios de energía cinética y potencial. El entorno está a $T_0 = 298\ \text{K}$.
>
> Se pide:
> 1. El estado de salida (temperatura y [[Calidad]]).
> 2. La entropía generada por unidad de masa.
> 3. La exergía destruida por unidad de masa.

## Estrategia

> [!teoria]
> Volumen de control en flujo estacionario, adiabático ($\dot Q = 0$) y sin trabajo ($\dot W = 0$). Aplican:
> - [[Balance de Masa VC]]: $\dot m_1 = \dot m_2$.
> - [[Balance de Energia VC]]: con $\dot Q = \dot W = 0$ y $\Delta\text{EC}=\Delta\text{EP}=0$ se reduce a $h_2 = h_1$ → proceso **isentálpico**, el rasgo distintivo del estrangulamiento (ver [[Flash]]).
> - [[Balance de Entropia VC]]: $\dot S_{gen} = \dot m\,(s_2 - s_1) \ge 0$.
> - [[Balance de Exergia VC]]: $\dot X_{dest} = T_0\,\dot S_{gen}$ (Gouy–Stodola).

## Estado de entrada

> [!info]
> Líquido saturado a $P_1 = 1.5\ \text{MPa}$. De tablas de saturación:
> $$
> h_1 = h_f = 844.9\ \text{kJ/kg}, \qquad s_1 = s_f = 2.315\ \text{kJ/kg·K}, \qquad T_1 = 198.3\ ^\circ\text{C}
> $$

## Inciso 1 — Estado de salida

> [!proposicion]
> Por ser isentálpico, $h_2 = h_1 = 844.9\ \text{kJ/kg}$. A $P_2 = 100\ \text{kPa}$ ($h_f = 417.5$, $h_{fg} = 2258.0\ \text{kJ/kg}$), como $h_f < h_2 < h_g$ la salida es **bifásica**. La [[Calidad]]:
> $$
> x_2 = \frac{h_2 - h_f}{h_{fg}} = \frac{844.9 - 417.5}{2258.0} = 0.189
> $$

> [!solucion]
> La temperatura de salida es la de saturación a $100\ \text{kPa}$:
> $$
> T_2 = T_{sat}(100\ \text{kPa}) = 99.6\ ^\circ\text{C}
> $$
> El líquido se enfría de $198.3$ a $99.6\ ^\circ\text{C}$ y se vaporiza parcialmente ($\sim 19\%$): es el **flash** que aprovechan los evaporadores y los ciclos de refrigeración.

## Inciso 2 — Entropía generada

> [!solucion]
> Entropía de salida con la [[Calidad]] hallada ($s_f = 1.3026$, $s_{fg} = 6.0568\ \text{kJ/kg·K}$):
> $$
> s_2 = s_f + x_2\,s_{fg} = 1.3026 + 0.189\,(6.0568) = 2.449\ \text{kJ/kg·K}
> $$
> Del [[Balance de Entropia VC]] adiabático, por unidad de masa:
> $$
> s_{gen} = s_2 - s_1 = 2.449 - 2.315 = 0.134\ \text{kJ/kg·K} \; > 0
> $$

## Inciso 3 — Exergía destruida

> [!solucion]
> Por el teorema de Gouy–Stodola (ver [[Exergia]] y [[Balance de Exergia VC]]):
> $$
> x_{dest} = T_0\,s_{gen} = 298 \times 0.134 = 40.0\ \text{kJ/kg}
> $$

> [!info] Verificación física
> En un estrangulamiento adiabático sin trabajo, toda la disminución de exergía de flujo se **destruye**: $\psi_1 - \psi_2 = (h_1 - h_2) - T_0(s_1 - s_2) = T_0(s_2 - s_1) = x_{dest}$. La válvula no produce trabajo pero degrada $40\ \text{kJ/kg}$ de potencial útil; es el precio termodinámico de reducir presión por fricción en lugar de hacerlo en una turbina (comparar con [[Problema 01]]).

## Notas usadas

> [!referencia]
> [[Valvulas]] · [[Flash]] · [[Balance de Masa VC]] · [[Balance de Energia VC]] · [[Balance de Entropia VC]] · [[Balance de Exergia VC]] · [[Entalpia]] · [[Entropia]] · [[Exergia]] · [[Calidad]] · [[Presion]] · [[Temperatura]]

> [!info]
> **Convención de notación**:
> - $\psi = (h - h_0) - T_0(s - s_0)$: exergía de flujo específica; $x_{dest}$: exergía destruida [kJ/kg].
> - proceso isentálpico: $h_2 = h_1$ aunque $P$, $T$ y $s$ cambien.
