---
title: "Válvulas de Estrangulamiento"
tags:
  - termodinamica
  - dispositivos_flujo
  - valvulas
  - estrangulamiento
draft: false
aliases:
  - throttle valve
  - válvula de expansión
  - estrangulador
---

# Válvulas de Estrangulamiento

> [!definicion]
> Dispositivo de [[Flujo Estacionario]] que reduce la presión de un fluido mediante una restricción parcial al flujo (orificio, válvula parcialmente abierta, tapón poroso). El proceso se denomina **estrangulamiento** y es esencialmente isentálpico.

## Hipótesis estándar para análisis

> [!info]
> 1. [[Flujo Estacionario]] ($dm_{VC}/dt = 0$, $dE_{VC}/dt = 0$)
> 2. Una entrada, una salida
> 3. Adiabática ($\dot{Q} = 0$) — área pequeña, tiempo de residencia corto
> 4. Sin trabajo de eje ($\dot{W} = 0$)
> 5. Despreciable $\Delta EC$ ($C_1 \approx C_2$) y $\Delta EP$ ($z_1 \approx z_2$)
> 6. Proceso **altamente irreversible** → $S_{gen} > 0$

## Ecuaciones de gobierno

> [!teorema]
> **Conservación de masa**: $\dot{m}_1 = \dot{m}_2 = \dot{m}$
>
> **Primera ley (energía)**:
> $$
> h_1 = h_2
> $$
> (con las hipótesis anteriores)
>
> **Segunda ley (entropía)**:
> $$
> \dot{S}_{gen} = \dot{m}(s_2 - s_1) \geq 0 \quad \Rightarrow \quad s_2 > s_1
> $$
>
> **Balance de exergía**:
> $$
> \dot{B}_{dest} = \dot{m}(\psi_1 - \psi_2) = T_0 \dot{S}_{gen}
> $$

## Propiedades del proceso de estrangulamiento

> [!info]
> - **Isentálpico**: $h_2 = h_1$ (por eso se usa en [[Ciclos de Refrigeracion]] y [[Bombas de Calor]])
> - **Irreversible**: $s_2 > s_1$ (caída de presión sin recuperación de trabajo)
> - **Temperatura**: puede aumentar, disminuir o permanecer constante dependiendo del fluido y condiciones

## Coeficiente de Joule-Thomson

> [!definicion]
> Mide el cambio de temperatura con respecto a la presión en un proceso de estrangulamiento:
> $$
> \mu_{JT} = \left(\frac{\partial T}{\partial P}\right)_h
> $$
>
> - $\mu_{JT} > 0$: el fluido se **enfría** al expandirse (la mayoría de gases a temperatura ambiente)
> - $\mu_{JT} = 0$: **curva de inversión** (cambio de signo)
> - $\mu_{JT} < 0$: el fluido se **calienta** al expandirse (H₂, He a temperatura ambiente; gases ideales $\mu_{JT} = 0$)

> [!proposicion]
> **Gas ideal**: $\mu_{JT} = 0$ (no hay cambio de temperatura, $h = h(T)$)
>
> **Gas real** (ecuación de estado):
> $$
> \mu_{JT} = \frac{1}{c_p} \left[ T \left(\frac{\partial v}{\partial T}\right)_P - v \right]
> $$

## Casos particulares

> [!proposicion]
> **Líquido incompresible** ($\rho$ constante):
> - $h_2 - h_1 = c(T_2 - T_1) + v(P_2 - P_1) = 0$
> - $T_2 - T_1 = -\frac{v}{c}(P_2 - P_1)$
> - Si $P_2 < P_1$, entonces $T_2 > T_1$ (el líquido se calienta ligeramente)

> [!proposicion]
> **Vapor húmedo** (región de saturación):
> - $h_1 = h_2 = h_f + x h_{fg}$
> - Si $P_2 < P_1$, la calidad aumenta: $x_2 > x_1$
> - Puede generar vapor adicional (efecto de "flash")

> [!proposicion]
> **Vapor sobrecalentado** (gas real):
> - Depende de $\mu_{JT}$ y de la zona termodinámica
> - Puede enfriarse o calentarse según esté por encima o debajo de la curva de inversión

## Gráfico $T-s$ (temperatura-entropía)

> [!info]
> En un diagrama $T-s$:
> - La válvula es una línea **horizontal** $h = \text{constante}$ (no vertical/necesariamente, depende de la pendiente)
> - La entropía aumenta: $s_2 > s_1$
> - El punto final se desplaza hacia la derecha (mayor $s$)

## Limitaciones y consideraciones prácticas

> [!warning]
> - **No recuperación de trabajo**: A diferencia de una turbina, la caída de presión no produce trabajo, solo genera entropía.
> - **Erosión**: Altas velocidades en la restricción pueden erosionar el asiento de la válvula.
> - **Cavitación**: En líquidos, la presión local puede caer por debajo de $P_{sat}$, formando burbujas de vapor que implosionan aguas abajo (daño por cavitación).
> - **Ruido**: Flujo de alta velocidad puede generar ruido significativo (silbatos, vibración).
> - **Congelamiento**: Si $\mu_{JT} > 0$ y $\Delta P$ es grande, la temperatura puede caer por debajo de $0°C$, congelando humedad o hidratos (problemas en líneas de gas natural).

> [!ejemplo]
> **Válvula de expansión en refrigerador** (R-134a)
>
> Datos: $P_1 = 1.0 MPa$, $T_1 = 40°C$ (líquido subenfriado), $P_2 = 0.2 MPa$, $\dot{m} = 0.05 kg/s$, $T_0 = 298 K$
>
> **1. Entrada (tablas R-134a, líquido subenfriado)**:
> A $P_1 = 1.0 MPa$, $T_{sat} \approx 40°C$ (coincide, entonces líquido saturado)
> $h_1 = h_f(1.0 MPa) \approx 256.4 kJ/kg$
> $s_1 = s_f(1.0 MPa) \approx 1.190 kJ/kg·K$
>
> **2. Salida** (estrangulamiento: $h_2 = h_1 = 256.4 kJ/kg$ a $P_2 = 0.2 MPa$):
> A $0.2 MPa$: $T_{sat} \approx -10.1°C$, $h_f = 186.7 kJ/kg$, $h_g = 392.7 kJ/kg$, $s_f = 0.950 kJ/kg·K$, $s_g = 1.732 kJ/kg·K$
>
> **3. Calidad a la salida**:
> $x_2 = (h_2 - h_f)/h_{fg} = (256.4 - 186.7)/(392.7 - 186.7) = 69.7/206.0 = 0.338$
>
> **4. Entropía de salida**:
> $s_2 = s_f + x_2 s_{fg} = 0.950 + 0.338 \times (1.732 - 0.950) = 0.950 + 0.338 \times 0.782 = 0.950 + 0.264 = 1.214 kJ/kg·K$
>
> **5. Generación de entropía**:
> $\dot{S}_{gen} = \dot{m}(s_2 - s_1) = 0.05 \times (1.214 - 1.190) = 0.05 \times 0.024 = 0.0012 kW/K$
>
> **6. Destrucción de exergía**:
> $\dot{B}_{dest} = T_0 \dot{S}_{gen} = 298 \times 0.0012 = 0.3576 kW$
>
> **Interpretación**: Se destruyen ~0.36 kW de potencial de trabajo en la válvula (pequeño, pero significativo en ciclo de refrigeración). La temperatura baja de $40°C$ a $-10.1°C$ (enfriamiento por efecto Joule-Thomson).

> [!ejemplo]
> **Válvula en línea de gas natural** (metano, gas real)
>
> Datos: $P_1 = 8.0 MPa$, $T_1 = 20°C$, $P_2 = 1.0 MPa$
>
> **1. Propiedades del metano** (tablas o gráficos):
> A $8.0 MPa$, $20°C$: $h_1 \approx 540 kJ/kg$
> $T_{inv}$ para metano es alta (>400 K), por lo que a $293 K$ está por debajo de la curva de inversión → $\mu_{JT} > 0$ → se enfría.
>
> **2. Estrangulamiento** ($h_2 = h_1 = 540 kJ/kg$, $P_2 = 1.0 MPa$):
> Se busca en tablas a $1.0 MPa$: $T_2$ con $h_2 = 540 kJ/kg$
> Por ejemplo, a $1.0 MPa$: a $-50°C$ ($223.15 K$), $h \approx 520 kJ/kg$; a $-40°C$ ($233.15 K$), $h \approx 550 kJ/kg$
> Interpolando: $T_2 \approx -46°C$ ($227 K$)
>
> **3. Caída de temperatura**:
> $\Delta T = 20°C - (-46°C) = 66°C$ (enfriamiento significativo)
>
> **Precaución**: Puede formar hidratos o congelar humedad, bloqueando la válvula.

## Relaciones con otras notas

> [!info]
> - [[Toberas]] (acelera flujo con caída de presión)
> - [[Turbinas]] (expansión con producción de trabajo)
> - [[Ciclos de Refrigeracion]] (válvula es componente clave)
> - [[Gas Real]] (comportamiento no ideal, $\mu_{JT}$)
> - [[Exergia]] (destrucción en válvula $= T_0 \dot{S}_{gen}$)

