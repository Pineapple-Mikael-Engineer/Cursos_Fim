---
title: "Turbinas"
tags:
  - termodinamica
  - dispositivos_flujo
  - turbinas
  - conversion_energia
draft: false
aliases:
  - turbine
  - expansor
---

# Turbinas

> [!definicion]
> Dispositivo de [[Flujo Estacionario]] que extrae trabajo de un fluido en expansión. El fluido pasa de alta presión/alta temperatura a baja presión/baja temperatura, produciendo trabajo de eje.

## Hipótesis estándar para análisis

> [!info]
> 1. [[Flujo Estacionario]] ($dm_{VC}/dt = 0$, $dE_{VC}/dt = 0$)
> 2. Una entrada, una salida
> 3. Adiabática ($\dot{Q} = 0$) — común en turbinas de vapor/gas, excepto casos con enfriamiento
> 4. Despreciables $\Delta EC$ y $\Delta EP$ ($C_1 \approx C_2$, $z_1 \approx z_2$)
> 5. Proceso internamente irreversible (real) → $S_{gen} > 0$

## Ecuaciones de gobierno

> [!teorema]
> **Conservación de masa**: $\dot{m}_1 = \dot{m}_2 = \dot{m}$
>
> **Primera ley (energía)**:
> $$
> \dot{W}_{turb} = \dot{m}(h_1 - h_2)
> $$
> (convención: $\dot{W}_{turb} > 0$ cuando sale del VC)
>
> **Segunda ley (entropía)**:
> $$
> \dot{S}_{gen} = \dot{m}(s_2 - s_1) \geq 0 \quad \Rightarrow \quad s_2 \geq s_1
> $$
>
> **Balance de exergía**:
> $$
> \dot{B}_{dest} = \dot{m}(\psi_1 - \psi_2) - \dot{W}_{turb} = T_0 \dot{S}_{gen}
> $$

## Eficiencia isoentrópica (de turbina)

> [!definicion]
> Relación entre trabajo real y trabajo isentrópico (reversible):
> $$
> \eta_t = \frac{\dot{W}_{real}}{\dot{W}_s} = \frac{h_1 - h_2}{h_1 - h_{2s}}
> $$
>
> - Estado 1: entrada real
> - Estado 2: salida real
> - Estado $2s$: salida para proceso isentrópico ($s_{2s} = s_1$, $P_{2s} = P_2$)

> [!info]
> **Rango típico**: $\eta_t \approx 0.85 - 0.92$ para turbinas de vapor/gas modernas

## Casos particulares

> [!proposicion]
> **Gas ideal con $c_p$ constante**:
> $$
> \eta_t = \frac{T_1 - T_2}{T_1 - T_{2s}}
> $$
> donde $T_{2s} = T_1 (P_2/P_1)^{(\gamma-1)/\gamma}$

> [!proposicion]
> **Vapor de agua**:
> - Usar tablas de vapor para $h_1$, $s_1$, $h_{2s}$ (buscando $P_2$ con $s_{2s}=s_1$)
> - Salida real puede estar en región húmeda → $x_2 = (h_2 - h_f)/h_{fg}$

## Eficiencia exergética (segunda ley)

> [!definicion]
> $$
> \varepsilon_t = \frac{\dot{W}_{turb}}{\dot{m}(\psi_1 - \psi_2)} = 1 - \frac{\dot{B}_{dest}}{\dot{m}(\psi_1 - \psi_2)}
> $$
>
> Para turbina adiabática: $\varepsilon_t = \eta_t$ solo si el fluido es gas ideal con $c_p$ constante y $T_0$ coincide con temperatura de referencia? **No siempre**. Difieren si $T_0 \neq T_{ambiente}$ del problema.

## Limitaciones y consideraciones prácticas

> [!warning]
> - **Turbina de vapor**: entrada típicamente vapor sobrecalentado o saturado. Salida puede ser mezcla húmeda (problemas de erosión si $x < 0.88-0.90$)
> - **Turbina de gas**: entrada gases de combustión a alta temperatura. El compresor consume parte del trabajo generado ($W_{neto} = W_{turb} - W_{comp}$)
> - **Turbina hidráulica**: el fluido es incompresible. Usar $h_1 - h_2 \approx v(P_1 - P_2)$ (despreciando $\Delta T$), o mejor usar Bernoulli con eficiencia

> [!ejemplo]
> **Turbina de vapor** (calcular trabajo, eficiencia, destrucción de exergía)
>
> Datos: $\dot{m} = 10 kg/s$, $P_1 = 6 MPa$, $T_1 = 600°C$, $P_2 = 10 kPa$, $\eta_t = 0.90$, $T_0 = 298K$, $P_0 = 100 kPa$
>
> **1. Entrada (tablas de vapor)**:
> $P_1 = 6 MPa$, $T_1 = 600°C$ → $h_1 = 3658.4 kJ/kg$, $s_1 = 7.167 kJ/kg·K$
>
> **2. Salida isentrópica**:
> $P_2 = 10 kPa$, $s_{2s} = s_1 = 7.167 kJ/kg·K$
> A $10 kPa$: $s_f = 0.649 kJ/kg·K$, $s_g = 8.151 kJ/kg·K$
> $x_{2s} = (7.167 - 0.649)/(8.151 - 0.649) = 6.518/7.502 = 0.869$
> $h_{2s} = h_f + x_{2s} h_{fg} = 191.8 + 0.869 \times 2392.8 = 191.8 + 2079.0 = 2270.8 kJ/kg$
>
> **3. Eficiencia isoentrópica**:
> $\eta_t = (h_1 - h_2)/(h_1 - h_{2s})$ → $0.90 = (3658.4 - h_2)/(3658.4 - 2270.8) = (3658.4 - h_2)/1387.6$
> $3658.4 - h_2 = 0.90 \times 1387.6 = 1248.8$
> $h_2 = 3658.4 - 1248.8 = 2409.6 kJ/kg$
>
> **4. Trabajo real**:
> $\dot{W} = \dot{m}(h_1 - h_2) = 10 \times (3658.4 - 2409.6) = 10 \times 1248.8 = 12488 kW$
>
> **5. Entropía salida real** (con $h_2 = 2409.6 kJ/kg$ a $P_2=10kPa$):
> $x_2 = (2409.6 - 191.8)/2392.8 = 2217.8/2392.8 = 0.927$
> $s_2 = s_f + x_2 s_{fg} = 0.649 + 0.927 \times 7.502 = 0.649 + 6.954 = 7.603 kJ/kg·K$
>
> **6. Destrucción de exergía**:
> $\psi_1 = (h_1 - h_0) - T_0(s_1 - s_0)$
> $h_0$ (líquido saturado a $P_0$) ≈ $417.5 kJ/kg$, $s_0 ≈ 1.303 kJ/kg·K$
> $\psi_1 = (3658.4 - 417.5) - 298(7.167 - 1.303) = 3240.9 - 298 \times 5.864 = 3240.9 - 1747.5 = 1493.4 kJ/kg$
> $\psi_2 = (2409.6 - 417.5) - 298(7.603 - 1.303) = 1992.1 - 298 \times 6.300 = 1992.1 - 1877.4 = 114.7 kJ/kg$
> $\dot{B}_{dest} = \dot{m}(\psi_1 - \psi_2) - \dot{W} = 10 \times (1493.4 - 114.7) - 12488 = 10 \times 1378.7 - 12488 = 13787 - 12488 = 1299 kW$
>
> **7. Eficiencia exergética**:
> $\varepsilon = \dot{W} / [\dot{m}(\psi_1 - \psi_2)] = 12488 / 13787 = 0.906$ (vs. $\eta_t=0.90$)

## Relaciones con otras notas

> [!info]
> - [[Compresores]] (proceso inverso: consume trabajo)
> - [[Ciclos de Potencia]] (Rankine, Brayton)
> - [[Segunda Ley SC]] (para $S_{gen}$)
> - [[Balance de Exergia VC]] (para $B_{dest}$)

