---
title: "Balance de Exergía (Volumen de Control)"
tags:
  - termodinamica
  - conservacion
  - exergia
  - segunda_ley
  - volumen_de_control
draft: false
aliases:
  - balance exergético VC
  - disponibilidad VC
  - exergy balance VC
---

# Balance de Exergía (Volumen de Control)

> [!definicion]
> **Balance de exergía** para un [[Volumenes de Control]] fijo en el espacio, combinando primera y segunda ley:
> $$
> \frac{dB_{VC}}{dt} = \sum_k \left(1 - \frac{T_0}{T_k}\right) \dot{Q}_k - \left(\dot{W}_{VC} - P_0 \frac{dV_{VC}}{dt}\right) + \sum_{in} \dot{m}_i \psi_i - \sum_{out} \dot{m}_e \psi_e - \dot{B}_{dest}
> $$
>
> - $B_{VC} = \int_{VC} \phi \, dm$: exergía total en el VC [kJ]
> - $\phi = (u - u_0) - T_0(s - s_0) + P_0(v - v_0)$: exergía específica de no flujo [kJ/kg]
> - $\psi = (h - h_0) - T_0(s - s_0) + \frac{C^2}{2} + gz$: exergía específica de flujo [kJ/kg]
> - $T_0$, $P_0$: temperatura y presión del ambiente muerto
> - $\dot{B}_{dest} = T_0 \dot{S}_{gen} \geq 0$: tasa de destrucción de exergía [kW]

## Formas particulares

> [!proposicion]
> **Flujo estacionario** ($dB_{VC}/dt = 0$, $dV_{VC}/dt = 0$ para VC rígido):
> $$
> 0 = \sum_k \left(1 - \frac{T_0}{T_k}\right) \dot{Q}_k - \dot{W}_{VC} + \sum_{in} \dot{m}_i \psi_i - \sum_{out} \dot{m}_e \psi_e - \dot{B}_{dest}
> $$
>
> Reordenando:
> $$
> \dot{B}_{dest} = \sum_{in} \dot{m}_i \psi_i - \sum_{out} \dot{m}_e \psi_e + \sum_k \left(1 - \frac{T_0}{T_k}\right) \dot{Q}_k - \dot{W}_{VC} \geq 0
> $$

> [!proposicion]
> **Flujo estacionario, una entrada, una salida** ($\dot{m}_1 = \dot{m}_2 = \dot{m}$):
> $$
> \dot{B}_{dest} = \dot{m}(\psi_1 - \psi_2) + \sum_k \left(1 - \frac{T_0}{T_k}\right) \dot{Q}_k - \dot{W}_{VC} \geq 0
> $$

> [!proposicion]
> **Volumen de control adiabático** ($\dot{Q}_k = 0$):
> $$
> \dot{B}_{dest} = \sum_{in} \dot{m}_i \psi_i - \sum_{out} \dot{m}_e \psi_e - \dot{W}_{VC} \geq 0
> $$
>
> Para una entrada, una salida: $\dot{B}_{dest} = \dot{m}(\psi_1 - \psi_2) - \dot{W}_{VC}$

> [!proposicion]
> **Sistema cerrado** (caso particular: sin flujos másicos):
> $$
> \frac{d\Phi}{dt} = \sum_k \left(1 - \frac{T_0}{T_k}\right) \dot{Q}_k - \left(\dot{W} - P_0 \frac{dV}{dt}\right) - \dot{B}_{dest}
> $$
> Integrando: $\Delta \Phi = \int \left(1 - \frac{T_0}{T}\right) \delta Q - \underbrace{ \left[W - P_0(V_2 - V_1)\right] }_{ W_{util} } - B_{dest}$

> [!proposicion]
> **Dispositivos comunes** (flujo estacionario, una entrada, una salida, $\dot{Q}=0$, despreciando $EC$ y $EP$):
> - **Turbina**: $\dot{W} = \dot{m}(\psi_1 - \psi_2) - \dot{B}_{dest}$ (trabajo real menor que la disminución de exergía)
> - **Compresor**: $\dot{W} = \dot{m}(\psi_2 - \psi_1) + \dot{B}_{dest}$ (trabajo real mayor que el aumento de exergía)
> - **Tobera/Difusor** ($\dot{W}=0$, $\dot{Q}=0$): $\dot{B}_{dest} = \dot{m}(\psi_1 - \psi_2)$

> [!demostracion]
> **De la combinación de primera y segunda ley**
>
> 1. **Balance de energía** para VC (flujo estacionario, una entrada, una salida):
>    $$
>    \dot{Q} - \dot{W} = \dot{m}(h_2 - h_1)
>    $$
>    (despreciando $EC$ y $EP$ por simplicidad; se añaden después)
>
> 2. **Balance de entropía** para VC:
>    $$
>    0 = \frac{\dot{Q}}{T} + \dot{m}(s_1 - s_2) + \dot{S}_{gen}
>    $$
>    donde se usó $T$ constante para la transferencia de calor (caso simple)
>
> 3. **Despejar** $\dot{Q}$ del balance de entropía:
>    $$
>    \dot{Q} = T \dot{m}(s_2 - s_1) - T \dot{S}_{gen}
>    $$
>
> 4. **Sustituir** en el balance de energía:
>    $$
>    T \dot{m}(s_2 - s_1) - T \dot{S}_{gen} - \dot{W} = \dot{m}(h_2 - h_1)
>    $$
>
> 5. **Reordenar**:
>    $$
>    \dot{W} = \dot{m} \left[(h_1 - h_2) - T(s_1 - s_2)\right] - T \dot{S}_{gen}
>    $$
>
> 6. **Identificar exergía de flujo** (despreciando $EC$, $EP$ y con $h_0$, $s_0$ como referencia):
>    $$
>    \psi = (h - h_0) - T_0(s - s_0)
>    $$
>    Notar que $(h_1 - h_2) - T_0(s_1 - s_2) = \psi_1 - \psi_2$ (los términos $h_0$, $s_0$ se cancelan)
>
> 7. **Sustituir**:
>    $$
>    \dot{W} = \dot{m}(\psi_1 - \psi_2) - T_0 \dot{S}_{gen}
>    $$
>
> 8. **Identificar destrucción de exergía**: $\dot{B}_{dest} = T_0 \dot{S}_{gen} \geq 0$
>    $$
>    \dot{B}_{dest} = \dot{m}(\psi_1 - \psi_2) - \dot{W}
>    $$
>
> 9. **Generalización**:
>    - Múltiples entradas/salidas
>    - Transferencia de calor a temperaturas variables: el término $(1 - T_0/T_k)\dot{Q}_k$ representa la exergía asociada al calor
>    - Términos de energía cinética y potencial se añaden dentro de $\psi$
>    - Para flujo no estacionario, se incluye $dB_{VC}/dt$
>    - Para VC con frontera móvil, se resta $P_0 dV_{VC}/dt$ del trabajo
>
> **Forma general**:
> $$
> \frac{dB_{VC}}{dt} = \sum_k \left(1 - \frac{T_0}{T_k}\right) \dot{Q}_k - \left(\dot{W}_{VC} - P_0 \frac{dV_{VC}}{dt}\right) + \sum_{in} \dot{m}_i \psi_i - \sum_{out} \dot{m}_e \psi_e - \dot{B}_{dest}
> $$

## Relaciones con otras notas

> [!info]
> - [[Balance de Masa VC]] (provee $\dot{m}$)
> - [[Balance de Energia VC]] (determina estados)
> - [[Balance de Entropia VC]] (provee $\dot{S}_{gen}$ para calcular $\dot{B}_{dest} = T_0 \dot{S}_{gen}$)
> - [[Exergia]] (definiciones y propiedades de $\phi$ y $\psi$)
> - [[Eficiencia Exergética]] ($\varepsilon$)

> [!ejemplo]
> **Turbina de vapor** (flujo estacionario, adiabática, una entrada, una salida)
>
> Datos: $\dot{m} = 12 kg/s$, $h_1 = 3400 kJ/kg$, $s_1 = 6.5 kJ/kg·K$
> $h_2 = 2500 kJ/kg$, $s_2 = 6.7 kJ/kg·K$, $T_0 = 298 K$, $h_0 \approx 104 kJ/kg$, $s_0 \approx 0.367 kJ/kg·K$
>
> 1. Exergías de flujo:
>    $\psi_1 = (h_1 - h_0) - T_0(s_1 - s_0) = (3400 - 104) - 298(6.5 - 0.367) = 3296 - 1827.6 = 1468.4 kJ/kg$
>    $\psi_2 = (2500 - 104) - 298(6.7 - 0.367) = 2396 - 1887.2 = 508.8 kJ/kg$
>
> 2. Trabajo real: $\dot{W} = \dot{m}(h_1 - h_2) = 12 \times 900 = 10800 kW$
>
> 3. Destrucción: $\dot{B}_{dest} = \dot{m}(\psi_1 - \psi_2) - \dot{W} = 12 \times (1468.4 - 508.8) - 10800 = 12 \times 959.6 - 10800 = 11515.2 - 10800 = 715.2 kW$
>
> 4. Eficiencia exergética: $\varepsilon = \dot{W} / [\dot{m}(\psi_1 - \psi_2)] = 10800 / 11515.2 = 0.938$ (93.8%)

> [!ejemplo]
> **Válvula de estrangulamiento** (flujo estacionario, adiabática, sin trabajo)
>
> Datos: $\dot{m} = 0.5 kg/s$, R-134a, $h_1 = h_2$, $P_1 = 1.0 MPa$, $P_2 = 0.2 MPa$, $T_0 = 298 K$
>
> De tablas: $s_1 = 0.95 kJ/kg·K$, $s_2 = 1.01 kJ/kg·K$ (aprox., depende de $T$)
>
> $\psi_1 - \psi_2 = (h_1 - h_2) - T_0(s_1 - s_2) = 0 - 298 \times (0.95 - 1.01) = -298 \times (-0.06) = 17.88 kJ/kg$
>
> $\dot{B}_{dest} = \dot{m}(\psi_1 - \psi_2) - \dot{W} = 0.5 \times 17.88 - 0 = 8.94 kW$
>
> Interpretación: La caída de presión irreversible destruye exergía, aunque la energía se conserva ($h$ constante).

> [!ejemplo]
> **Intercambiador de calor** (flujo estacionario, dos corrientes, $\dot{W}=0$)
>
> Datos: Fluido caliente: $\dot{m}_h = 2 kg/s$, $\psi_{h,ent} = 500 kJ/kg$, $\psi_{h,sal} = 300 kJ/kg$
> Fluido frío: $\dot{m}_c = 5 kg/s$, $\psi_{c,ent} = 50 kJ/kg$, $\psi_{c,sal} = 120 kJ/kg$
> Transferencia de calor desde el fluido caliente al frío a través de una pared.
>
> Balance (VC que incluye ambas corrientes, adiabático externamente):
> $\dot{B}_{dest} = \sum_{in} \dot{m}\psi - \sum_{out} \dot{m}\psi - \dot{W}$
>
> $\dot{B}_{dest} = [\dot{m}_h \psi_{h,ent} + \dot{m}_c \psi_{c,ent}] - [\dot{m}_h \psi_{h,sal} + \dot{m}_c \psi_{c,sal}]$
> $= [2 \times 500 + 5 \times 50] - [2 \times 300 + 5 \times 120]$
> $= [1000 + 250] - [600 + 600] = 1250 - 1200 = 50 kW$
>
> Interpretación: La diferencia finita de temperatura en la transferencia de calor destruye exergía.

> [!warning]
> - $\dot{B}_{dest} = T_0 \dot{S}_{gen}$ **solo** si $T_0$ es constante y corresponde al ambiente muerto
> - La exergía **no se conserva**: $\dot{B}_{dest} \geq 0$ para procesos irreversibles
> - El término $(1 - T_0/T_k)\dot{Q}_k$ puede ser positivo (calor a $T_k > T_0$) o negativo (calor a $T_k < T_0$)
> - En flujo no estacionario, $dB_{VC}/dt$ puede ser positivo o negativo
> - Un balance de exergía por sí solo **no reemplaza** la primera y segunda ley; requiere estados termodinámicos ya determinados
> - La exergía de flujo $\psi$ incluye $h$, no $u$; no confundir con $\phi$ (sistema cerrado)

> [!info]
> **Interpretación de términos**:
> - $\sum (1 - T_0/T_k)\dot{Q}_k$: exergía asociada a la transferencia de calor (trabajo máximo obtenible de ese calor)
> - $\dot{W}_{VC} - P_0 dV_{VC}/dt$: trabajo útil (descontando el trabajo contra la atmósfera)
> - $\sum \dot{m}\psi$: exergía que entra/sale con el flujo de masa
> - $\dot{B}_{dest}$: exergía destruida por irreversibilidades (pérdida de potencial de trabajo)
>
> **Convención de signos**:
> - $\dot{Q}_k$ positivo hacia el VC
> - $\dot{W}_{VC}$ positivo realizado por el VC
> - $\dot{B}_{dest}$ siempre $\geq 0$
> - $\psi$ puede ser negativo si el estado está por debajo del ambiente muerto (ej. fluido muy frío)