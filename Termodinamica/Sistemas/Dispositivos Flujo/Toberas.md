---
title: "Toberas"
tags:
  - termodinamica
  - dispositivos_flujo
  - toberas
  - conversion_energia
draft: false
aliases:
  - nozzle
  - tobera
---

# Toberas

> [!definicion]
> Dispositivo de [[Flujo Estacionario]] que acelera un fluido hasta alta velocidad, convirtiendo entalpía (presión) en energía cinética. La presión disminuye a lo largo de la tobera, mientras que la velocidad aumenta.

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
> Despejando velocidad de salida:
> $$
> C_2 = \sqrt{C_1^2 + 2(h_1 - h_2)}
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

## Velocidad máxima (isentrópica)

> [!teorema]
> Para una tobera **reversible y adiabática** ($s_2 = s_1$):
> $$
> C_{2,max} = \sqrt{C_1^2 + 2(h_1 - h_{2s})}
> $$
> donde $h_{2s}$ es la entalpía de salida para expansión isentrópica hasta $P_2$.

## Eficiencia de tobera

> [!definicion]
> Relación entre la velocidad real y la velocidad isentrópica (ideal):
> $$
> \eta_n = \frac{C_2^2 - C_1^2}{C_{2s}^2 - C_1^2} = \frac{h_1 - h_2}{h_1 - h_{2s}}
> $$
>
> - $C_1$: velocidad real de entrada
> - $C_2$: velocidad real de salida
> - $C_{2s}$: velocidad de salida para proceso isentrópico

> [!info]
> **Rango típico**: $\eta_n \approx 0.90 - 0.98$ para toberas bien diseñadas

## Flujo supersónico

> [!info]
> **Tobera convergente-divergente (de Laval)**:
> - Sección convergente → acelera flujo hasta $M = 1$ (sónico) en la garganta
> - Sección divergente → acelera flujo a $M > 1$ (supersónico)
>
> **Relación de áreas** (flujo isentrópico, gas ideal):
> $$
> \frac{A}{A^*} = \frac{1}{M} \left[ \frac{2}{\gamma+1} \left(1 + \frac{\gamma-1}{2} M^2\right) \right]^{\frac{\gamma+1}{2(\gamma-1)}}
> $$
> - $A^*$: área de garganta (donde $M = 1$)
> - $M = C/c$: número de Mach ($c = \sqrt{\gamma R T}$: velocidad del sonido)

## Casos particulares

> [!proposicion]
> **Gas ideal con $c_p$ constante**:
> - Isentrópico: $T_{2s} = T_1 (P_2/P_1)^{(\gamma-1)/\gamma}$
> - $C_{2s} = \sqrt{C_1^2 + 2c_p(T_1 - T_{2s})}$
> - Real: $T_2 = T_1 - \eta_n (T_1 - T_{2s})$

> [!proposicion]
> **Vapor de agua**:
> - Usar tablas de vapor para $h_1$, $s_1$, $h_{2s}$ (buscando $P_2$ con $s_{2s}=s_1$)
> - Salida real puede estar en región húmeda → $x_2 = (h_2 - h_f)/h_{fg}$

> [!proposicion]
> **Líquido incompresible** ($\rho$ constante):
> - Ecuación de Bernoulli con pérdidas: $P_1 + \frac{\rho C_1^2}{2} = P_2 + \frac{\rho C_2^2}{2} + \Delta P_{perd}$
> - Velocidad máxima: $C_2 = \sqrt{C_1^2 + 2(P_1 - P_2)/\rho}$

## Limitaciones y consideraciones prácticas

> [!warning]
> - **Ondas de choque**: En flujo supersónico, si la contrapresión $P_{back}$ es mayor que $P_{diseño}$, se forman ondas de choque que reducen la velocidad.
> - **Condensación**: En vapor o gases húmedos, la expansión rápida puede causar condensación (gotas de líquido), afectando eficiencia.
> - **Erosión**: Partículas en suspensión pueden erosionar las paredes de la tobera.
> - **Temperaturas extremas**: En toberas de cohete, los materiales deben soportar altas temperaturas.

> [!ejemplo]
> **Tobera convergente de vapor** (calcular velocidad de salida y eficiencia)
>
> Datos: $\dot{m}$ no dado, $P_1 = 2.0 MPa$, $T_1 = 300°C$, $P_2 = 0.1 MPa$, $\eta_n = 0.92$, $C_1 \approx 0$
>
> **1. Entrada (tablas de vapor)**:
> $P_1 = 2.0 MPa$, $T_1 = 300°C$ → $h_1 = 3024.7 kJ/kg$, $s_1 = 6.768 kJ/kg·K$
>
> **2. Salida isentrópica**:
> $P_2 = 0.1 MPa$, $s_{2s} = s_1 = 6.768 kJ/kg·K$
> A $0.1 MPa$: $s_f = 1.303 kJ/kg·K$, $s_g = 7.359 kJ/kg·K$
> $x_{2s} = (6.768 - 1.303)/(7.359 - 1.303) = 5.465/6.056 = 0.902$
> $h_{2s} = h_f + x_{2s} h_{fg} = 417.5 + 0.902 \times 2257.5 = 417.5 + 2036.3 = 2453.8 kJ/kg$
>
> **3. Velocidad isentrópica** ($C_1 \approx 0$):
> $C_{2s} = \sqrt{2(h_1 - h_{2s}) \times 1000} = \sqrt{2 \times (3024.7 - 2453.8) \times 1000}$
> $C_{2s} = \sqrt{2 \times 570.9 \times 1000} = \sqrt{1.1418 \times 10^6} = 1068.5 m/s$
>
> **4. Eficiencia de tobera**:
> $\eta_n = (h_1 - h_2)/(h_1 - h_{2s})$ → $0.92 = (3024.7 - h_2)/570.9$
> $3024.7 - h_2 = 0.92 \times 570.9 = 525.2$
> $h_2 = 3024.7 - 525.2 = 2499.5 kJ/kg$
>
> **5. Velocidad real**:
> $C_2 = \sqrt{2(h_1 - h_2) \times 1000} = \sqrt{2 \times 525.2 \times 1000} = \sqrt{1.0504 \times 10^6} = 1024.9 m/s$
>
> **6. Verificar** $\eta_n = C_2^2/C_{2s}^2 = (1024.9^2)/(1068.5^2) = 1.0504/1.1418 = 0.92$ ✓
>
> **7. Calidad a la salida real** (con $h_2 = 2499.5 kJ/kg$ a $0.1 MPa$):
> $x_2 = (2499.5 - 417.5)/2257.5 = 2082.0/2257.5 = 0.922$

> [!ejemplo]
> **Tobera convergente de aire** (gas ideal, calcular $C_2$, $T_2$)
>
> Datos: $\dot{m} = 0.5 kg/s$, $P_1 = 500 kPa$, $T_1 = 400 K$, $P_2 = 100 kPa$, $C_1 \approx 0$, $\eta_n = 0.95$, $c_p = 1.005 kJ/kg·K$, $\gamma = 1.4$
>
> **1. Salida isentrópica**:
> $T_{2s} = T_1 (P_2/P_1)^{(\gamma-1)/\gamma} = 400 \times (0.2)^{0.2857} = 400 \times 0.631 = 252.4 K$
> $h_1 - h_{2s} = c_p (T_1 - T_{2s}) = 1.005 \times (400 - 252.4) = 1.005 \times 147.6 = 148.3 kJ/kg$
> $C_{2s} = \sqrt{2 \times 148.3 \times 1000} = \sqrt{296600} = 544.6 m/s$
>
> **2. Eficiencia**:
> $h_1 - h_2 = \eta_n (h_1 - h_{2s}) = 0.95 \times 148.3 = 140.9 kJ/kg$
> $C_2 = \sqrt{2 \times 140.9 \times 1000} = \sqrt{281800} = 530.9 m/s$
>
> **3. Temperatura real de salida**:
> $T_2 = T_1 - (h_1 - h_2)/c_p = 400 - 140.9/1.005 = 400 - 140.2 = 259.8 K$
>
> **4. Flujo másico** (verificar área):
> $\rho_2 = P_2/(R T_2)$, $R = 0.287 kJ/kg·K = 287 J/kg·K$
> $\rho_2 = 100000/(287 \times 259.8) = 100000/74526 = 1.342 kg/m^3$
> $A_2 = \dot{m}/(\rho_2 C_2) = 0.5/(1.342 \times 530.9) = 0.5/712.5 = 0.000702 m^2 = 7.02 cm^2$

## Relaciones con otras notas

> [!info]
> - [[Difusores]] (proceso inverso: desacelera flujo, aumenta presión)
> - [[Turbinas]] (expande fluido con producción de trabajo)
> - [[Valvulas]] (reduce presión sin trabajo, pero sin aceleración significativa)
> - [[Flujo Estacionario]] (aplicación directa)

