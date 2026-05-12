---
title: "Difusores"
tags:
  - termodinamica
  - dispositivos_flujo
  - difusores
  - conversion_energia
draft: false
aliases:
  - diffuser
  - difusor
---

# Difusores

> [!definicion]
> Dispositivo de [[Flujo Estacionario]] que desacelera un fluido de alta velocidad, convirtiendo energía cinética en aumento de presión (entalpía). Es el proceso inverso de una [[Toberas | tobera]].

## Hipótesis estándar para análisis

> [!info]
> 1. [[Flujo Estacionario]] ($dm_{VC}/dt = 0$, $dE_{VC}/dt = 0$)
> 2. Una entrada, una salida
> 3. Adiabática ($\dot{Q} = 0$) — común, aunque puede haber pérdidas
> 4. Sin trabajo de eje ($\dot{W} = 0$)
> 5. Despreciable $\Delta EP$ ($z_1 \approx z_2$)
> 6. Proceso internamente irreversible (real) → $S_{gen} > 0$

## Ecuaciones de gobierno

> [!teorema]
> **Conservación de masa**: $\dot{m} = \rho_1 C_1 A_1 = \rho_2 C_2 A_2$
>
> **Primera ley (energía)**:
> $$
> h_1 + \frac{C_1^2}{2} = h_2 + \frac{C_2^2}{2}
> $$
>
> Despejando aumento de entalpía:
> $$
> h_2 - h_1 = \frac{C_1^2 - C_2^2}{2}
> $$
>
> **Segunda ley (entropía)**:
> $$
> \dot{S}_{gen} = \dot{m}(s_2 - s_1) \geq 0 \quad \Rightarrow \quad s_2 \geq s_1
> $$
>
> **Balance de exergía**:
> $$
> \dot{B}_{dest} = \dot{m}(\psi_1 - \psi_2) \geq 0
> $$

## Aumento de presión ideal (isentrópico)

> [!teorema]
> Para un difusor **reversible y adiabático** ($s_2 = s_1$):
> - La presión aumenta al máximo posible para una dada desaceleración
> - Para gas ideal: $P_{2s} = P_1 \left( \frac{T_{2s}}{T_1} \right)^{\gamma/(\gamma-1)}$
> - $T_{2s}$ se obtiene de $h_{2s} = h_1 + (C_1^2 - C_2^2)/2$

## Eficiencia de difusor

> [!definicion]
> Relación entre el aumento de presión real y el ideal (isentrópico):
> $$
> \eta_d = \frac{P_2 - P_1}{P_{2s} - P_1}
> $$
>
> **Forma alternativa** (basada en velocidades, para gas ideal):
> $$
> \eta_d = \frac{h_{2s} - h_1}{h_2 - h_1} = \frac{T_{2s} - T_1}{T_2 - T_1}
> $$

> [!info]
> **Rango típico**: $\eta_d \approx 0.80 - 0.92$ para difusores bien diseñados

## Recuperación de presión

> [!definicion]
> Porcentaje de presión cinética recuperada como presión estática:
> $$
> R = \frac{P_2 - P_1}{P_{01} - P_1}
> $$
> donde $P_{01} = P_1 + \rho_1 C_1^2/2$ es la presión de estancamiento (para flujo incompresible)

## Casos particulares

> [!proposicion]
> **Gas ideal con $c_p$ constante**:
> - Aumento de temperatura: $T_2 = T_1 + (C_1^2 - C_2^2)/(2c_p)$
> - Isentrópico: $T_{2s} = T_1 + \eta_d (T_2 - T_1)$ ¿cuidado? mejor: $T_{2s} = T_2$ no, la eficiencia relaciona presiones
> - Relación de presiones: $\frac{P_{2s}}{P_1} = \left(\frac{T_{2s}}{T_1}\right)^{\gamma/(\gamma-1)}$

> [!proposicion]
> **Líquido incompresible** ($\rho$ constante):
> - Ecuación de Bernoulli con pérdidas:
>   $$
>   P_2 = P_1 + \frac{\rho}{2}(C_1^2 - C_2^2) - \Delta P_{perd}
>   $$
> - Eficiencia: $\eta_d = \frac{P_2 - P_1}{\frac{\rho}{2}(C_1^2 - C_2^2)}$

> [!proposicion]
> **Flujo supersónico en entrada**:
> - Se forma una onda de choque normal si el difusor no está diseñado para condiciones supersónicas
> - La onda de choque causa pérdida de presión total significativa

## Limitaciones y consideraciones prácticas

> [!warning]
> - **Desprendimiento de la capa límite**: Si el ángulo de divergencia es muy grande (>7-10°), el flujo se separa de la pared, reduciendo la recuperación de presión.
> - **Ondas de choque**: En difusores supersónicos, se requiere geometría convergente-divergente (inverso de tobera de Laval).
> - **Pérdidas por fricción**: Dominantes en difusores de baja velocidad.
> - **Limitación de Mach**: Para $M_1 > 1.5-2.0$, la recuperación de presión es muy pobre debido a ondas de choque.

> [!ejemplo]
> **Difusor de entrada de motor a reacción** (calcular presión de salida y eficiencia)
>
> Datos: $C_1 = 200 m/s$, $P_1 = 40 kPa$, $T_1 = 230 K$, $C_2 = 50 m/s$, $\eta_d = 0.85$, $c_p = 1.005 kJ/kg·K$, $\gamma = 1.4$, $R = 0.287 kJ/kg·K$
>
> **1. Aumento de entalpía**:
> $h_2 - h_1 = (C_1^2 - C_2^2)/2 = (200^2 - 50^2)/2 = (40000 - 2500)/2 = 37500/2 = 18750 J/kg = 18.75 kJ/kg$
>
> **2. Temperatura real de salida**:
> $T_2 = T_1 + (h_2 - h_1)/c_p = 230 + 18.75/1.005 = 230 + 18.66 = 248.66 K$
>
> **3. Para calcular $P_2$, usar eficiencia**:
> $\eta_d = (P_2 - P_1)/(P_{2s} - P_1)$ ⇒ necesito $P_{2s}$
>
> **4. Estado isentrópico** (misma entalpía):
> $h_{2s} = h_1 + (C_1^2 - C_2^2)/2 = h_2$, entonces $T_{2s} = T_2 = 248.66 K$ (para gas ideal, si $c_p$ constante, $T$ determina $h$)
> ¿Conflicto? Si $h_{2s} = h_2$, entonces $T_{2s} = T_2$, pero el proceso isentrópico requiere $s_{2s}=s_1$, y $s_2 > s_1$ por irreversibilidades. Entonces $T_{2s}$ y $T_2$ no son iguales.
>
> **Enfoque correcto**:
> - Para isentrópico: $s_{2s} = s_1$ ⇒ $T_{2s} = T_1 (P_{2s}/P_1)^{(\gamma-1)/\gamma}$
> - Pero $h_{2s} = h_1 + (C_1^2 - C_2^2)/2$ ⇒ $T_{2s} = T_1 + (C_1^2 - C_2^2)/(2c_p) = 230 + 18.66 = 248.66 K$
> - Esto implica que $T_{2s}$ está fijado por la conservación de energía
> - Entonces $s_{2s} = s_1$ no se cumple automáticamente; se requiere una $P_{2s}$ específica
>
> **5. Calcular $P_{2s}$**:
> Relación isentrópica: $P_{2s} = P_1 (T_{2s}/T_1)^{\gamma/(\gamma-1)} = 40 \times (248.66/230)^{3.5}$
> $248.66/230 = 1.0811$
> $1.0811^{3.5} = e^{3.5 \ln(1.0811)} = e^{3.5 \times 0.0780} = e^{0.273} = 1.314$
> $P_{2s} = 40 \times 1.314 = 52.56 kPa$
>
> **6. Calcular $P_2$ real**:
> $\eta_d = (P_2 - P_1)/(P_{2s} - P_1)$
> $0.85 = (P_2 - 40)/(52.56 - 40) = (P_2 - 40)/12.56$
> $P_2 - 40 = 0.85 \times 12.56 = 10.68$
> $P_2 = 50.68 kPa$
>
> **7. Verificar aumento de entropía**:
> $\Delta s = c_p \ln(T_2/T_1) - R \ln(P_2/P_1) = 1.005 \ln(248.66/230) - 0.287 \ln(50.68/40)$
> $\Delta s = 1.005 \times 0.0780 - 0.287 \times 0.237 = 0.0784 - 0.0680 = 0.0104 kJ/kg·K$
> $S_{gen} = \dot{m} \Delta s > 0$ (irreversible)

> [!ejemplo]
> **Difusor incompresible** (flujo de agua)
>
> Datos: $C_1 = 15 m/s$, $P_1 = 150 kPa$, $C_2 = 3 m/s$, $\rho = 1000 kg/m^3$, $\eta_d = 0.88$
>
> **1. Presión ideal (sin pérdidas)**:
> $P_{2s} = P_1 + \frac{\rho}{2}(C_1^2 - C_2^2) = 150000 + 500 \times (225 - 9) = 150000 + 500 \times 216 = 150000 + 108000 = 258000 Pa = 258 kPa$
>
> **2. Presión real**:
> $\eta_d = (P_2 - P_1)/(P_{2s} - P_1)$
> $0.88 = (P_2 - 150)/(258 - 150) = (P_2 - 150)/108$
> $P_2 - 150 = 0.88 \times 108 = 95.04$
> $P_2 = 245.04 kPa$
>
> **3. Pérdida de presión**:
> $\Delta P_{perd} = (P_{2s} - P_2) = 258 - 245.04 = 12.96 kPa$

## Relaciones con otras notas

> [!info]
> - [[Toberas]] (proceso inverso: acelera flujo, disminuye presión)
> - [[Compresores]] (aumenta presión con trabajo de eje)
> - [[Flujo Estacionario]] (aplicación directa)
> - [[Gas Ideal]] (ecuaciones específicas para aire y gases)

