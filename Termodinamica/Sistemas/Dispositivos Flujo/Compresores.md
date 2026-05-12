---
title: "Compresores"
tags:
  - termodinamica
  - dispositivos_flujo
  - compresores
  - conversion_energia
draft: false
aliases:
  - compressor
  - compresor
---

# Compresores

> [!definicion]
> Dispositivo de [[Flujo Estacionario]] que consume trabajo para aumentar la presión de un fluido (gas o vapor). El fluido entra a baja presión y sale a alta presión.

## Hipótesis estándar para análisis

> [!info]
> 1. [[Flujo Estacionario]] ($dm_{VC}/dt = 0$, $dE_{VC}/dt = 0$)
> 2. Una entrada, una salida
> 3. Adiabática ($\dot{Q} = 0$) — común en análisis ideal; real pueden tener enfriamiento
> 4. Despreciables $\Delta EC$ y $\Delta EP$ ($C_1 \approx C_2$, $z_1 \approx z_2$)
> 5. Proceso internamente irreversible (real) → $S_{gen} > 0$

## Ecuaciones de gobierno

> [!teorema]
> **Conservación de masa**: $\dot{m}_1 = \dot{m}_2 = \dot{m}$
>
> **Primera ley (energía)**:
> $$
> \dot{W}_{comp} = \dot{m}(h_2 - h_1)
> $$
> (convención: $\dot{W}_{comp} > 0$ cuando entra al VC — trabajo consumido)
>
> **Segunda ley (entropía)**:
> $$
> \dot{S}_{gen} = \dot{m}(s_2 - s_1) \geq 0 \quad \Rightarrow \quad s_2 \geq s_1
> $$
>
> **Balance de exergía**:
> $$
> \dot{B}_{dest} = \dot{W}_{comp} - \dot{m}(\psi_2 - \psi_1) = T_0 \dot{S}_{gen}
> $$

## Eficiencia isoentrópica (de compresor)

> [!definicion]
> Relación entre trabajo isentrópico (mínimo requerido) y trabajo real:
> $$
> \eta_c = \frac{\dot{W}_s}{\dot{W}_{real}} = \frac{h_{2s} - h_1}{h_2 - h_1}
> $$
>
> - Estado 1: entrada real
> - Estado 2: salida real
> - Estado $2s$: salida para proceso isentrópico ($s_{2s} = s_1$, $P_{2s} = P_2$)

> [!info]
> **Rango típico**: $\eta_c \approx 0.80 - 0.88$ para compresores industriales

## Casos particulares

> [!proposicion]
> **Gas ideal con $c_p$ constante**:
> $$
> \eta_c = \frac{T_{2s} - T_1}{T_2 - T_1}
> $$
> donde $T_{2s} = T_1 (P_2/P_1)^{(\gamma-1)/\gamma}$

> [!proposicion]
> **Compresión isotérmica** (ideal, con enfriamiento perfecto):
> - Trabajo mínimo para gas ideal: $W_{isot} = \dot{m} R T \ln(P_2/P_1)$
> - $\eta_{isot} = W_{isot}/W_{real}$ (otra definición usada en compresores refrigeración)

## Eficiencia exergética (segunda ley)

> [!definicion]
> $$
> \varepsilon_c = \frac{\dot{m}(\psi_2 - \psi_1)}{\dot{W}_{comp}} = 1 - \frac{\dot{B}_{dest}}{\dot{W}_{comp}}
> $$

## Compresión en etapas múltiples

> [!info]
> Para altas relaciones de presión ($P_2/P_1 > 5-6$), se usa compresión en etapas con enfriamiento intermedio.
>
> **Relación de presión óptima por etapa** (para minimizar trabajo total en $n$ etapas):
> $$
> r_{opt} = \left(\frac{P_{final}}{P_{inicial}}\right)^{1/n}
> $$
>
> **Trabajo total** (gas ideal, $c_p$ constante, enfriamiento perfecto a $T_1$):
> $$
> W_{total} = n \cdot \dot{m} c_p T_1 \left(r_{opt}^{(\gamma-1)/\gamma} - 1\right)
> $$

## Limitaciones y consideraciones prácticas

> [!warning]
> - **Temperatura de salida**: $T_2 = T_1 + (T_{2s} - T_1)/\eta_c$. Valores altos pueden requerir enfriamiento para evitar daños.
> - **Problemas de lubricación**: Aceite se degrada a altas temperaturas.
> - **Limitación por volumen específico**: A bajas presiones, $v$ es grande → compresores grandes.
> - **Separación de turbina**: En ciclos de gas, el compresor consume 60-80% del trabajo de la turbina.

> [!ejemplo]
> **Compresor centrífugo de aire** (calcular trabajo, eficiencia, potencia)
>
> Datos: $\dot{m} = 2 kg/s$, $P_1 = 100 kPa$, $T_1 = 300 K$, $P_2 = 800 kPa$, $\eta_c = 0.85$, $c_p = 1.005 kJ/kg·K$, $\gamma = 1.4$
>
> **1. Salida isentrópica**:
> $T_{2s} = T_1 (P_2/P_1)^{(\gamma-1)/\gamma} = 300 \times 8^{0.2857} = 300 \times 1.811 = 543.3 K$
>
> **2. Eficiencia isoentrópica**:
> $\eta_c = (h_{2s} - h_1)/(h_2 - h_1) \approx (T_{2s} - T_1)/(T_2 - T_1)$
> $0.85 = (543.3 - 300)/(T_2 - 300) = 243.3/(T_2 - 300)$
> $T_2 - 300 = 243.3/0.85 = 286.2 K$
> $T_2 = 586.2 K$
>
> **3. Trabajo real**:
> $W_{real} = \dot{m} c_p (T_2 - T_1) = 2 \times 1.005 \times 286.2 = 575.3 kW$
>
> **4. Trabajo isentrópico (mínimo)**:
> $W_s = \dot{m} c_p (T_{2s} - T_1) = 2 \times 1.005 \times 243.3 = 489.0 kW$
> Verificar: $\eta_c = 489.0/575.3 = 0.85$ ✓
>
> **5. Destrucción de exergía** (adiabático, $T_0 = 298 K$):
> $\Delta s = c_p \ln(T_2/T_1) - R \ln(P_2/P_1)$
> $R = c_p - c_v = 1.005 - 0.718 = 0.287 kJ/kg·K$
> $\Delta s = 1.005 \ln(586.2/300) - 0.287 \ln 8 = 1.005 \times 0.670 - 0.287 \times 2.079 = 0.673 - 0.597 = 0.076 kJ/kg·K$
> $\dot{S}_{gen} = \dot{m} \Delta s = 2 \times 0.076 = 0.152 kW/K$
> $\dot{B}_{dest} = T_0 \dot{S}_{gen} = 298 \times 0.152 = 45.3 kW$
>
> **6. Eficiencia exergética**:
> $\psi_1 = (h_1 - h_0) - T_0(s_1 - s_0)$
> Suponiendo $T_0 = T_1$, $P_0 = P_1$: $\psi_1 = 0 - T_0(0) = 0$? No exactamente, pero simplificando:
> $\psi_2 \approx c_p (T_2 - T_0) - T_0 [c_p \ln(T_2/T_0) - R \ln(P_2/P_0)]$
> Alternativa rápida: $\varepsilon_c = \dot{m}(\psi_2 - \psi_1)/\dot{W}_{comp} \approx (W_s / \dot{W}_{comp}) \times \text{corrección}$
> Para este caso, $\varepsilon_c \approx 0.85$ (similar a $\eta_c$) porque $\psi$ escala aproximadamente con $\Delta h$.

## Relaciones con otras notas

> [!info]
> - [[Turbinas]] (proceso inverso: produce trabajo)
> - [[Ciclos de Potencia]] (Rankine, Brayton)
> - [[Toberas]] (diferente función: acelera fluido sin trabajo)
> - [[Valvulas]] (reduce presión sin trabajo)

