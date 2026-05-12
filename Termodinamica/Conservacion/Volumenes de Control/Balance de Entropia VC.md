---
title: "Balance de Entropía (Volumen de Control)"
tags:
  - termodinamica
  - conservacion
  - entropia
  - segunda_ley
  - volumen_de_control
draft: false
aliases:
  - segunda ley VC
  - balance entropico VC
  - entropy balance VC
---

# Balance de Entropía (Volumen de Control)

> [!definicion]
> **Segunda ley de la termodinámica** para un [[Volumenes de Control]] fijo en el espacio:
> $$
> \frac{dS_{VC}}{dt} = \sum_k \frac{\dot{Q}_k}{T_k} + \sum_{in} \dot{m}_i s_i - \sum_{out} \dot{m}_e s_e + \dot{S}_{gen}
> $$
>
> - $S_{VC} = \int_{VC} s \, dm$: entropía total en el VC [kJ/K]
> - $\dot{Q}_k$: tasa de transferencia de calor a través de la frontera a temperatura $T_k$ [kW]
> - $T_k$: temperatura en la frontera donde ocurre $\dot{Q}_k$ [K]
> - $s$: [[Entropia]] específica [kJ/kg·K]
> - $\dot{S}_{gen} \geq 0$: tasa de generación de entropía por irreversibilidades [kW/K]

## Formas particulares

> [!proposicion]
> **Flujo estacionario** ($dS_{VC}/dt = 0$):
> $$
> 0 = \sum_k \frac{\dot{Q}_k}{T_k} + \sum_{in} \dot{m}_i s_i - \sum_{out} \dot{m}_e s_e + \dot{S}_{gen}
> $$
> o equivalentemente:
> $$
> \dot{S}_{gen} = \sum_{out} \dot{m}_e s_e - \sum_{in} \dot{m}_i s_i - \sum_k \frac{\dot{Q}_k}{T_k} \geq 0
> $$

> [!proposicion]
> **Flujo estacionario, una entrada, una salida** ($\dot{m}_1 = \dot{m}_2 = \dot{m}$):
> $$
> \dot{S}_{gen} = \dot{m}(s_2 - s_1) - \sum_k \frac{\dot{Q}_k}{T_k} \geq 0
> $$

> [!proposicion]
> **Volumen de control adiabático** ($\dot{Q}_k = 0$):
> $$
> \dot{S}_{gen} = \sum_{out} \dot{m}_e s_e - \sum_{in} \dot{m}_i s_i \geq 0
> $$
> Para una entrada, una salida: $s_2 \geq s_1$

> [!proposicion]
> **Sistema cerrado** (caso particular: sin flujos másicos):
> $$
> \frac{dS}{dt} = \frac{\dot{Q}}{T} + \dot{S}_{gen}, \quad \dot{S}_{gen} \geq 0
> $$
> Integrando: $\Delta S = \int \frac{\delta Q}{T} + S_{gen}$

> [!demostracion]
> **De la desigualdad de Clausius a la forma de VC**
>
> 1. **Desigualdad de Clausius** para un sistema cerrado que experimenta un ciclo:
>    $$
>    \oint \frac{\delta Q}{T} \leq 0
>    $$
>    Para un proceso entre dos estados: $S_2 - S_1 \geq \int_1^2 \frac{\delta Q}{T}$
>
> 2. **Forma de tasa** para sistema cerrado:
>    $$
>    \frac{dS_{sis}}{dt} \geq \frac{\dot{Q}_{sis}}{T}
>    $$
>    Definiendo $\dot{S}_{gen} \geq 0$: $\frac{dS_{sis}}{dt} = \frac{\dot{Q}_{sis}}{T} + \dot{S}_{gen}$
>
> 3. **Sistema cerrado = VC + masa que entra/sale** (mismo procedimiento que en energía):
>    - $S_{sis}(t) = S_{VC}(t) + \delta m_i s_i$
>    - $S_{sis}(t+dt) = S_{VC}(t+dt) + \delta m_e s_e$
>
> 4. **Resta y divide por $dt$**:
>    $$
>    \frac{dS_{sis}}{dt} = \frac{dS_{VC}}{dt} + \dot{m}_e s_e - \dot{m}_i s_i
>    $$
>
> 5. **Transferencia de calor** en el VC puede ocurrir a múltiples temperaturas:
>    $$
>    \frac{\dot{Q}_{sis}}{T} = \sum_k \frac{\dot{Q}_k}{T_k}
>    $$
>    (se suma sobre cada frontera donde hay flujo de calor)
>
> 6. **Sustituir** en $\frac{dS_{sis}}{dt} = \frac{\dot{Q}_{sis}}{T} + \dot{S}_{gen}$:
>    $$
>    \frac{dS_{VC}}{dt} + \dot{m}_e s_e - \dot{m}_i s_i = \sum_k \frac{\dot{Q}_k}{T_k} + \dot{S}_{gen}
>    $$
>
> 7. **Forma final**:
>    $$
>    \frac{dS_{VC}}{dt} = \sum_k \frac{\dot{Q}_k}{T_k} + \sum_{in} \dot{m}_i s_i - \sum_{out} \dot{m}_e s_e + \dot{S}_{gen}, \quad \dot{S}_{gen} \geq 0
>    $$
>
> **Significado físico**:
> - $\sum \dot{Q}_k/T_k$: transferencia de entropía asociada al calor
> - $\sum \dot{m} s$: transferencia de entropía asociada al flujo de masa
> - $\dot{S}_{gen}$: entropía **generada** dentro del VC por irreversibilidades (fricción, transferencia de calor con diferencia finita, mezclado, reacciones, etc.)

## Relaciones con otras notas

> [!info]
> - [[Balance de Masa VC]] (provee $\dot{m}$)
> - [[Balance de Energia VC]] (determina estados, necesario para calcular $s$)
> - [[Exergia]] ($B_{destruida} = T_0 \dot{S}_{gen}$)
> - [[Irreversibilidad]] (relacionada con $\dot{S}_{gen}$)

> [!ejemplo]
> **Turbina adiabática** (flujo estacionario, una entrada, una salida, $\dot{Q}=0$)
>
> Datos: $\dot{m} = 10 kg/s$, $s_1 = 6.5 kJ/kg·K$, $s_2 = 6.7 kJ/kg·K$
>
> Balance: $\dot{S}_{gen} = \dot{m}(s_2 - s_1) = 10 \times (6.7 - 6.5) = 2 kW/K$
>
> Interpretación: Se generan $2 kW/K$ de entropía por irreversibilidades internas (fricción del fluido, turbulencia, etc.)

> [!ejemplo]
> **Compresor adiabático** (flujo estacionario, una entrada, una salida, $\dot{Q}=0$)
>
> Datos: $\dot{m} = 2 kg/s$, aire como gas ideal, $T_1 = 300K$, $P_1 = 100kPa$, $P_2 = 800kPa$, $\eta_{iso} = 0.85$
>
> 1. Proceso isentrópico: $T_{2s} = T_1 (P_2/P_1)^{(\gamma-1)/\gamma} = 300 \times 8^{0.2857} = 543.3K$
> 2. Eficiencia: $\eta = (h_{2s} - h_1)/(h_2 - h_1) \approx (T_{2s} - T_1)/(T_2 - T_1)$
> 3. $T_2 = T_1 + (T_{2s} - T_1)/\eta = 300 + 243.3/0.85 = 586.2K$
> 4. Para gas ideal con $c_p$ constante: $\Delta s = c_p \ln(T_2/T_1) - R \ln(P_2/P_1)$
>    $c_p = 1.005 kJ/kg·K$, $R = 0.287 kJ/kg·K$
>    $\Delta s = 1.005 \ln(586.2/300) - 0.287 \ln 8 = 0.678 - 0.597 = 0.081 kJ/kg·K$
> 5. $\dot{S}_{gen} = \dot{m} \Delta s = 2 \times 0.081 = 0.162 kW/K$

> [!ejemplo]
> **Intercambiador de calor** (flujo estacionario, dos corrientes)
>
> Datos: Fluido caliente: $\dot{m}_h = 2 kg/s$, $s_{h,ent} = 2.5 kJ/kg·K$, $s_{h,sal} = 2.3 kJ/kg·K$
> Fluido frío: $\dot{m}_c = 5 kg/s$, $s_{c,ent} = 0.8 kJ/kg·K$, $s_{c,sal} = 1.0 kJ/kg·K$
> Superficie de intercambio a $T_{sup} = 400K$, calor transferido $\dot{Q} = 500 kW$ desde el fluido caliente a la superficie
>
> Balance: $\dot{S}_{gen} = \sum \dot{m}_e s_e - \sum \dot{m}_i s_i - \sum \dot{Q}_k/T_k$
>
> $\Delta \dot{S}_{masa} = \dot{m}_h(s_{h,sal} - s_{h,ent}) + \dot{m}_c(s_{c,sal} - s_{c,ent})$
> $= 2 \times (2.3 - 2.5) + 5 \times (1.0 - 0.8) = -0.4 + 1.0 = 0.6 kW/K$
>
> Entropía cedida por calor: el calor sale del fluido caliente hacia la superficie a 400K. El VC incluye ambos fluidos y la pared. El calor cruza la frontera del VC desde la superficie hacia el ambiente exterior? Depende de la definición del VC. Para un VC adiabático externamente: $\dot{S}_{gen} = 0.6 kW/K$

> [!warning]
> - La entropía **no se conserva**: $\dot{S}_{gen} \geq 0$ estrictamente para procesos irreversibles, igual a cero solo para procesos reversibles
> - **No existe** "balance de entropía" sin el término $\dot{S}_{gen}$ — eso violaría la segunda ley
> - El término $\sum \dot{Q}_k/T_k$ **no es** $\dot{Q}/T$ global a menos que toda la frontera esté a temperatura uniforme
> - En flujo no estacionario, $dS_{VC}/dt$ puede ser positivo, negativo o cero; lo que nunca es negativo es $\dot{S}_{gen}$
> - Para procesos adiabáticos, $s_2 \geq s_1$ en flujo estacionario (la entropía específica nunca disminuye)

> [!info]
> **Casos con $\dot{S}_{gen} = 0$** (procesos internamente reversibles):
> - Flujo isentrópico en tobera o difusor
> - Compresión o expansión adiabática reversible en turbina/compresor
> - Transferencia de calor **reversible** (requiere $T_{fluido} = T_{fuente}$ → prácticamente irrealizable)
>
> **Convención de signos**:
> - $\dot{Q}_k$ positivo **hacia** el VC
> - El signo de $\sum \dot{Q}_k/T_k$ sigue el signo de $\dot{Q}_k$
> - $\dot{S}_{gen}$ siempre $\geq 0$ por definición