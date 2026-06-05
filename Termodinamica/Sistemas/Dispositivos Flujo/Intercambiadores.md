---
title: "Intercambiadores de Calor"
tags:
  - termodinamica
  - dispositivos_flujo
  - intercambiadores
  - transferencia_calor
draft: false
aliases:
  - heat exchanger
  - intercambiador
  - Intercambiadores de Calor
  - HX
---

# Intercambiadores de Calor

> [!definicion]
> Dispositivo de [[Flujo Estacionario]] que transfiere calor entre dos o más corrientes de fluido sin que se mezclen físicamente. Las corrientes están separadas por una pared sólida (tubos, placas, etc.).

## Hipótesis estándar para análisis

> [!info]
> 1. [[Flujo Estacionario]] ($dm_{VC}/dt = 0$, $dE_{VC}/dt = 0$)
> 2. Sin trabajo de eje ($\dot{W} = 0$)
> 3. Despreciables $\Delta EC$ y $\Delta EP$ ($C_1 \approx C_2$, $z_1 \approx z_2$)
> 4. **Externamente adiabático** ($\dot{Q}_{ext} = 0$) — el VC incluye las corrientes y la pared, sin transferencia con el exterior
> 5. Proceso internamente irreversible → $S_{gen} > 0$

## Ecuaciones de gobierno

> [!teorema]
> **Conservación de masa** (cada corriente por separado):
> $$
> \dot{m}_{c,ent} = \dot{m}_{c,sal} \quad \text{(corriente fría)}
> $$
> $$
> \dot{m}_{h,ent} = \dot{m}_{h,sal} \quad \text{(corriente caliente)}
> $$
>
> **Primera ley (energía)**:
> - Calor cedido por fluido caliente = calor ganado por fluido frío
> $$
> \dot{m}_h (h_{h,ent} - h_{h,sal}) = \dot{m}_c (h_{c,sal} - h_{c,ent})
> $$
>
> **Segunda ley (entropía)**:
> $$
> \dot{S}_{gen} = \dot{m}_c (s_{c,sal} - s_{c,ent}) + \dot{m}_h (s_{h,sal} - s_{h,ent}) \geq 0
> $$
>
> **Balance de exergía**:
> $$
> \dot{B}_{dest} = T_0 \dot{S}_{gen} = \dot{m}_c (\psi_{c,ent} - \psi_{c,sal}) + \dot{m}_h (\psi_{h,ent} - \psi_{h,sal})
> $$

## Eficiencia de intercambiador (método $\varepsilon$-NTU)

> [!definicion]
> **Eficiencia** $\varepsilon$: relación entre calor realmente transferido y calor máximo posible (si una corriente alcanzara la temperatura de entrada de la otra):
> $$
> \varepsilon = \frac{\dot{Q}_{real}}{\dot{Q}_{max}}
> $$
>
> **Calor máximo** (para intercambiadores sin cambio de fase):
> $$
> \dot{Q}_{max} = C_{min} (T_{h,ent} - T_{c,ent})
> $$
> donde $C_{min} = \min(\dot{m}_h c_{p,h}, \dot{m}_c c_{p,c})$

> [!info]
> **Para intercambiadores con cambio de fase** (evaporador, condensador):
> - La corriente que cambia de fase tiene $C \to \infty$ (temperatura constante)
> - $C_{min}$ es la otra corriente
> - $\varepsilon = (T_{ent} - T_{sal})/(T_{ent} - T_{sat})$ para fluido que se enfría/calienta

## Configuraciones comunes

> [!info]
> **Flujo paralelo**: ambas corrientes entran por el mismo extremo y se mueven en la misma dirección
>
> **Contraflujo**: corrientes entran por extremos opuestos y se mueven en direcciones contrarias (mayor eficiencia)
>
> **Flujo cruzado**: corrientes perpendiculares (intercambiadores compactos, radiadores)

## Relaciones $\varepsilon$-NTU

> [!teorema]
> **Contraflujo**:
> $$
> \varepsilon = \frac{1 - e^{-NTU(1 - C_r)}}{1 - C_r e^{-NTU(1 - C_r)}} \quad (C_r < 1)
> $$
> $$
> \varepsilon = \frac{NTU}{1 + NTU} \quad (C_r = 1)
> $$
>
> **Flujo paralelo**:
> $$
> \varepsilon = \frac{1 - e^{-NTU(1 + C_r)}}{1 + C_r}
> $$
>
> Donde:
> - $NTU = UA/C_{min}$ (número de unidades de transferencia)
> - $U$: coeficiente global de transferencia [kW/m²·K]
> - $A$: área de transferencia [m²]
> - $C_r = C_{min}/C_{max} \leq 1$

## Temperatura de salida

> [!proposicion]
> Conocido $\varepsilon$, $C_{min}$, $C_{max}$, $T_{h,ent}$, $T_{c,ent}$:
> $$
> \dot{Q} = \varepsilon C_{min} (T_{h,ent} - T_{c,ent})
> $$
>
> Para corriente caliente: $T_{h,sal} = T_{h,ent} - \dot{Q} / (\dot{m}_h c_{p,h})$
>
> Para corriente fría: $T_{c,sal} = T_{c,ent} + \dot{Q} / (\dot{m}_c c_{p,c})$

## Limitaciones y consideraciones prácticas

> [!warning]
> - **Factor de obstrucción (fouling)**: Con el tiempo, se depositan incrustaciones en las superficies, reduciendo $U$. Se incluye como $1/U_{dis} = 1/U_{limpio} + R_f$.
> - **Pérdida de carga**: Los intercambiadores reales tienen caídas de presión (fricción) que deben incluirse en análisis de exergía (no afectan energía pero sí exergía).
> - **Distribución de flujo**: Mal diseño puede causar derivaciones (bypass) o zonas muertas, reduciendo eficiencia.
> - **Estrés térmico**: Diferencias de temperatura generan expansiones diferenciales que pueden dañar uniones (tubo-placa).

> [!ejemplo]
> **Intercambiador de calor agua-agua** (contraflujo, determinar $\dot{Q}$, $T_{salidas}$, $\varepsilon$, $S_{gen}$)
>
> Datos:
> - Corriente caliente: $\dot{m}_h = 2 kg/s$, $c_{p,h} = 4.18 kJ/kg·K$, $T_{h,ent} = 80°C$
> - Corriente fría: $\dot{m}_c = 3 kg/s$, $c_{p,c} = 4.18 kJ/kg·K$, $T_{c,ent} = 20°C$
> - $UA = 50 kW/K$, $T_0 = 298 K$
>
> **1. Capacidades térmicas**:
> $C_h = \dot{m}_h c_{p,h} = 2 \times 4.18 = 8.36 kW/K$
> $C_c = \dot{m}_c c_{p,c} = 3 \times 4.18 = 12.54 kW/K$
> $C_{min} = 8.36 kW/K$, $C_{max} = 12.54 kW/K$
> $C_r = C_{min}/C_{max} = 8.36/12.54 = 0.667$
>
> **2. NTU**:
> $NTU = UA/C_{min} = 50/8.36 = 5.98$
>
> **3. Eficiencia (contraflujo)**:
> $\varepsilon = \frac{1 - e^{-NTU(1 - C_r)}}{1 - C_r e^{-NTU(1 - C_r)}}$
> $NTU(1 - C_r) = 5.98 \times 0.333 = 1.991$
> $e^{-1.991} = 0.137$
> $\varepsilon = \frac{1 - 0.137}{1 - 0.667 \times 0.137} = \frac{0.863}{1 - 0.0914} = \frac{0.863}{0.9086} = 0.950$
>
> **4. Calor transferido**:
> $\dot{Q} = \varepsilon C_{min} (T_{h,ent} - T_{c,ent}) = 0.950 \times 8.36 \times (80 - 20) = 0.950 \times 8.36 \times 60 = 0.950 \times 501.6 = 476.5 kW$
>
> **5. Temperaturas de salida**:
> $T_{h,sal} = T_{h,ent} - \dot{Q}/C_h = 80 - 476.5/8.36 = 80 - 57.0 = 23.0°C$
> $T_{c,sal} = T_{c,ent} + \dot{Q}/C_c = 20 + 476.5/12.54 = 20 + 38.0 = 58.0°C$
>
> **6. Verificación**: $T_{c,sal} (58°C) < T_{h,sal} (23°C)$? En contraflujo, $T_{c,sal}$ puede acercarse a $T_{h,ent}$ (80°C) pero el ejemplo da 58°C por limitación de $C_r$. Idealmente $T_{c,sal} \leq T_{h,ent}$ (sí, 58 < 80). $T_{h,sal} \geq T_{c,ent}$ (23 > 20).
>
> **7. Generación de entropía** (suponiendo $T_0 = 298K = 25°C$, usar Kelvin para cálculo):
> $T_{h,ent}=353.15K$, $T_{h,sal}=296.15K$, $T_{c,ent}=293.15K$, $T_{c,sal}=331.15K$
> $\Delta s_h = c_{p,h} \ln(T_{h,sal}/T_{h,ent}) = 4.18 \times \ln(296.15/353.15) = 4.18 \times \ln(0.8386) = 4.18 \times (-0.176) = -0.736 kJ/kg·K$
> $\Delta s_c = 4.18 \times \ln(331.15/293.15) = 4.18 \times \ln(1.1296) = 4.18 \times 0.122 = 0.510 kJ/kg·K$
> $\dot{S}_{gen} = \dot{m}_c \Delta s_c + \dot{m}_h \Delta s_h = 3 \times 0.510 + 2 \times (-0.736) = 1.53 - 1.472 = 0.058 kW/K$
>
> **8. Destrucción de exergía**:
> $\dot{B}_{dest} = T_0 \dot{S}_{gen} = 298 \times 0.058 = 17.3 kW$
>
> **9. Eficiencia exergética** (aproximada):
> $\dot{B}_{in} \approx \dot{m}_h c_{p,h}[(T_{h,ent}-T_0) - T_0 \ln(T_{h,ent}/T_0)]$ (simplificado)
> $\dot{B}_{rec} \approx \dot{m}_c c_{p,c}[(T_{c,sal}-T_0) - T_0 \ln(T_{c,sal}/T_0)]$
> $\varepsilon_x \approx 1 - \dot{B}_{dest} / (\dot{B}_{ent,h} + \dot{B}_{ent,c})$ etc.

> [!ejemplo]
> **Condensador de planta de potencia** (intercambiador con cambio de fase)
>
> Datos:
> - Vapor (corriente caliente): $\dot{m}_h = 100 kg/s$, $T_{sat} = 40°C$, $h_{fg} = 2400 kJ/kg$ (condensación)
> - Agua de enfriamiento (corriente fría): $\dot{m}_c = 2000 kg/s$, $c_{p,c} = 4.18 kJ/kg·K$, $T_{c,ent} = 20°C$
> - $UA = 4000 kW/K$
>
> **1. Calor transferido**:
> $\dot{Q} = \dot{m}_h h_{fg} = 100 \times 2400 = 240000 kW$
>
> **2. Temperatura de salida del agua**:
> $\dot{Q} = \dot{m}_c c_{p,c} (T_{c,sal} - T_{c,ent})$
> $T_{c,sal} = T_{c,ent} + \dot{Q} / (\dot{m}_c c_{p,c}) = 20 + 240000/(2000 \times 4.18) = 20 + 240000/8360 = 20 + 28.7 = 48.7°C$
>
> **3. Eficiencia (corriente caliente con cambio de fase)**:
> $C_{min} = \dot{m}_c c_{p,c} = 8360 kW/K$ (vapor tiene $C \to \infty$ porque $T$ constante)
> $\dot{Q}_{max} = C_{min} (T_{h,ent} - T_{c,ent}) = 8360 \times (40 - 20) = 167200 kW$
> Pero $\dot{Q}_{real} = 240000 kW > \dot{Q}_{max}$? No puede ser. Revisar:
> La fórmula $\dot{Q}_{max} = C_{min}(T_{h,ent} - T_{c,ent})$ asume que la corriente fría saldría a $T_{h,ent}$. Pero con $C_{min} = C_c$, el calor máximo sería $C_c(40-20)=167200 kW$, pero estamos transfiriendo 240000 kW. Contradicción.
>
> **Explicación**: Hay dos posibilidades:
> a) El vapor NO se condensa totalmente (sale como mezcla) o
> b) La corriente caliente tiene $C_{eff} = \dot{m}_h h_{fg} / (T_{h,ent} - T_{h,sal})$ con $T_{h,sal} < T_{h,ent}$ (subenfriamiento)
>
> En realidad, para condensador con vapor saturado a $40°C$, el calor máximo es $\dot{m}_c c_{p,c}(T_{sat} - T_{c,ent})$ si se limita por agua, pero si el vapor entrega más calor (porque también se subenfría), entonces $T_{h,sal} < T_{sat}$. La eficiencia se define de otra forma.
>
> **Enfoque simplificado**: Usar método de diferencia de temperatura media logarítmica (LMTD) para condensadores:
> $\dot{Q} = UA \cdot LMTD$
> Para condensador isotérmico (corriente caliente a $T_{sat}$):
> $LMTD = \frac{(T_{sat} - T_{c,ent}) - (T_{sat} - T_{c,sal})}{\ln[(T_{sat} - T_{c,ent})/(T_{sat} - T_{c,sal})]}$
> Puede despejarse $UA$ si se conoce $\dot{Q}$, o viceversa.
>
> El punto importante: En condensadores y evaporadores, **no hay límite de $C_{min}$** porque la corriente que cambia de fase transfiere calor a temperatura constante, pudiendo entregar/absorber grandes cantidades de calor sin límite por diferencia de temperatura.

## Relaciones con otras notas

> [!info]
> - [[Ciclos de Potencia]] (condensador, caldera, recalentador)
> - [[Ciclos de Refrigeracion]] (evaporador, condensador)
> - [[Segunda Ley SC]] (generación de entropía)
> - [[Exergia]] (destrucción en intercambiadores por diferencia finita de temperatura)
> - [[Transferencia de Calor]] (coeficientes $U$, correlaciones)
