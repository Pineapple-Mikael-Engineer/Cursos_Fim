---
title: "Exergía (Disponibilidad) $B$"
tags:
  - termodinamica
  - exergia
  - segunda_ley
  - conversion_energia
draft: false
aliases:
  - disponibilidad
  - work potential
  - exergy
  - B
---

# Exergía (Disponibilidad) $B$

> [!definicion]
> Trabajo máximo teórico obtenible de un sistema cuando interactúa con un **medio ambiente** ($T_0$, $P_0$) hasta alcanzar el equilibrio termomecánico completo.
> 
> La exergía se destruye en procesos irreversibles ($B_{destruida} = T_0 S_{gen} \geq 0$).

## Exergía de un sistema cerrado (no flujo)

> [!teorema]
> Para un [[Sistemas Cerrados]] en estado ($U$, $S$, $V$) con ambiente a ($T_0$, $P_0$):
> $$
> \Phi = (U - U_0) - T_0(S - S_0) + P_0(V - V_0)
> $$
> 
> Forma específica:
> $$
> \phi = (u - u_0) - T_0(s - s_0) + P_0(v - v_0)
> $$
> 
> Estado muerto: $U_0$, $S_0$, $V_0$ en equilibrio con ambiente.

## Exergía de flujo (corriente)

> [!teorema]
> Para flujo estacionario en [[Volumenes de Control]], exergía asociada a una corriente:
> $$
> \psi = (h - h_0) - T_0(s - s_0) + \frac{C^2}{2} + gz
> $$
> 
> Despreciando términos cinético y potencial:
> $$
> \psi = (h - h_0) - T_0(s - s_0)
> $$
> 
> Unidades: [kJ/kg]

## Balance de exergía

> [!teorema]
> **Para [[Sistemas Cerrados]]**:
> $$
> \Delta \Phi = \int \left(1 - \frac{T_0}{T}\right) \delta Q - \left[W - P_0(V_2 - V_1)\right] - B_{destruida}
> $$
> 
> **Para [[Volumenes de Control]] en [[Flujo Estacionario]]** (una entrada, una salida):
> $$
> \dot{B}_{destruida} = \sum \left(1 - \frac{T_0}{T_k}\right) \dot{Q}_k - \dot{W}_{eje} + \dot{m}(\psi_1 - \psi_2)
> $$

## Eficiencia exergética (segunda ley)

> [!definicion]
> Relación entre exergía recuperada y exergía suministrada:
> $$
> \varepsilon = \frac{B_{recuperada}}{B_{suministrada}} = 1 - \frac{B_{destruida}}{B_{suministrada}}
> $$
> 
> Para turbina: $\varepsilon_{turb} = \dot{W}_{eje} / \dot{m}(\psi_1 - \psi_2)$
> 
> Para compresor: $\varepsilon_{comp} = \dot{m}(\psi_2 - \psi_1) / \dot{W}_{eje}$
> 
> Para intercambiador: $\varepsilon_{interc} = (\dot{m}_c \Delta \psi_c) / (\dot{m}_h (\psi_{h,ent} - \psi_{h,sal}))$

## Relaciones con otras propiedades

> [!info]
> **Exergía y Helmholtz**:
> En un sistema a $T_0$, $V_0$ constantes, el trabajo máximo es $\Delta F = \Delta(U - TS)$
> 
> **Exergía y Gibbs**:
> En un sistema a $T_0$, $P_0$ constantes, el trabajo máximo (excluyendo $P_0 \Delta V$) es $\Delta G = \Delta(H - TS)$
> 
> **Destrucción de exergía**:
> $$
> B_{destruida} = T_0 S_{gen}
> $$
> donde $S_{gen}$ es [[Entropia - Generacion]]

## Casos particulares

> [!proposicion]
> **Para [[Gas Ideal]] con $c_p$ constante** (ambiente $T_0$, $P_0$):
> $$
> \psi = c_p (T - T_0) - T_0\left(c_p \ln\frac{T}{T_0} - R \ln\frac{P}{P_0}\right)
> $$
> 
> **Para flujo incompresible** ($v \approx v_0$ constante):
> $$
> \psi = c(T - T_0) - T_0 c \ln\frac{T}{T_0} + v(P - P_0)
> $$

## Exergía química

> [!definicion]
> Trabajo máximo obtenible al llevar una sustancia desde el estado de equilibrio termomecánico ($T_0$, $P_0$) hasta el equilibrio químico con el ambiente.
> 
> Para combustibles, se tabula o estima.
> 
> Exergía total (termomecánica + química):
> $$
> B_{total} = B_{tm} + B_{quim}
> $$

## Destrucción en componentes comunes

> [!info]
> **Válvula de estrangulamiento**:
> $h_2 = h_1$, $P_2 < P_1$ → $\dot{B}_{destruida} = \dot{m} T_0 (s_2 - s_1)$
> 
> **Intercambiador de calor** con diferencia finita de temperatura:
> $\dot{B}_{destruida} = T_0 \dot{S}_{gen} = T_0 \left[\dot{m}_h(s_{h,sal} - s_{h,ent}) + \dot{m}_c(s_{c,sal} - s_{c,ent})\right]$
> 
> **Tubería adiabática** con caída de presión:
> $\dot{B}_{destruida} = \dot{m} T_0 \left[-R \ln\frac{P_2}{P_1}\right]$ para gas ideal

> [!ejemplo]
> **Turbina de vapor** con datos reales
> 
> Datos: $\dot{m}=12 kg/s$, $h_1=3400 kJ/kg$, $s_1=6.5 kJ/kg·K$, $h_2=2600 kJ/kg$, $s_2=6.7 kJ/kg·K$, $T_0=298K$, $P_0=100kPa$
> 
> Exergía de entrada: $\psi_1 = (h_1 - h_0) - T_0(s_1 - s_0)$. Suponiendo agua líquida a $T_0$, $P_0$: $h_0 \approx 104 kJ/kg$, $s_0 \approx 0.367 kJ/kg·K$
> 
> $\psi_1 = (3400 - 104) - 298(6.5 - 0.367) = 3296 - 298(6.133) = 3296 - 1827.6 = 1468.4 kJ/kg$
> 
> $\psi_2 = (2600 - 104) - 298(6.7 - 0.367) = 2496 - 298(6.333) = 2496 - 1887.2 = 608.8 kJ/kg$
> 
> Trabajo real: $\dot{W} = \dot{m}(h_1 - h_2) = 12 \times 800 = 9600 kW$
> 
> Exergía recuperada: $\dot{B}_{rec} = \dot{m}(\psi_1 - \psi_2) = 12 \times (1468.4 - 608.8) = 12 \times 859.6 = 10315.2 kW$
> 
> Destrucción: $\dot{B}_{dest} = \dot{B}_{rec} - \dot{W} = 10315.2 - 9600 = 715.2 kW$
> 
> Eficiencia exergética: $\varepsilon = \dot{W} / \dot{B}_{rec} = 9600 / 10315.2 = 0.931$ (93.1%)

> [!warning]
> **Errores comunes**:
> - Confundir exergía con energía: energía se conserva, exergía se destruye
> - Usar $T_0$ incorrecta: debe ser temperatura del ambiente **muerto**, no del entorno inmediato
> - En flujo estacionario, no olvidar $P_0(v - v_0)$ en sistema cerrado pero usar $\psi$ para corrientes
> - Exergía **no es** propiedad termodinámica en sentido estricto (depende de $T_0$, $P_0$ del ambiente)

> [!info]
> **Convención de notación**:
> - $B$: exergía total (extensiva) [kJ]
> - $\Phi$: exergía de sistema cerrado (alternativa)
> - $\psi$: exergía específica de flujo [kJ/kg]
> - $\phi$: exergía específica de no flujo [kJ/kg]
> - $\varepsilon$: eficiencia exergética (segunda ley)