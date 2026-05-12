---
title: "Balance de Energía (Volumen de Control)"
tags:
  - termodinamica
  - conservacion
  - energia
  - primera_ley
  - volumen_de_control
draft: false
aliases:
  - primera ley VC
  - balance energetico VC
  - conservacion de la energia VC
---

# Balance de Energía (Volumen de Control)

> [!definicion]
> **Primera ley de la termodinámica** para un [[Volumenes de Control]] fijo en el espacio:
> $$
> \frac{dE_{VC}}{dt} = \dot{Q} - \dot{W} + \sum_{in} \dot{m}_i \left(h_i + \frac{C_i^2}{2} + gz_i\right) - \sum_{out} \dot{m}_e \left(h_e + \frac{C_e^2}{2} + gz_e\right)
> $$
>
> - $E_{VC} = \int_{VC} \left(u + \frac{C^2}{2} + gz\right) dm$: energía total en el VC [kJ]
> - $\dot{Q}$: tasa de transferencia de calor neta **hacia** el VC [kW]
> - $\dot{W}$: tasa de trabajo neto **realizado por** el VC [kW] (incluye eje, frontera móvil, eléctrico, etc.)
> - $h = u + Pv$: [[Entalpia]] específica [kJ/kg]
> - $C$: velocidad [m/s]
> - $z$: altura [m]

## Formas particulares

> [!proposicion]
> **Flujo estacionario** ($dE_{VC}/dt = 0$, $\dot{m}$ constante por conservación de masa):
> $$
> \dot{Q} - \dot{W} = \dot{m} \left[ (h_e - h_i) + \frac{C_e^2 - C_i^2}{2} + g(z_e - z_i) \right]
> $$
> Para múltiples entradas/salidas:
> $$
> \dot{Q} - \dot{W} = \sum_{out} \dot{m}_e \left(h_e + \frac{C_e^2}{2} + gz_e\right) - \sum_{in} \dot{m}_i \left(h_i + \frac{C_i^2}{2} + gz_i\right)
> $$

> [!proposicion]
> **Flujo estacionario, unidimensional, una entrada, una salida**:
> $$
> \dot{Q} - \dot{W} = \dot{m} \left( h_2 - h_1 + \frac{C_2^2 - C_1^2}{2} + g(z_2 - z_1) \right)
> $$

> [!proposicion]
> **Dispositivos comunes** (flujo estacionario, despreciando $\Delta EC$ y $\Delta EP$):
> - **Turbina/Compresor/Bomba**: $\dot{W} = \dot{m}(h_1 - h_2)$ (adiabático: $\dot{Q}=0$)
> - **Tobera/Difusor**: $\dot{W}=0$, $\dot{Q}=0$ → $h_1 + C_1^2/2 = h_2 + C_2^2/2$
> - **Válvula de estrangulamiento**: $\dot{W}=0$, $\dot{Q}=0$, $\Delta EC \approx 0$ → $h_1 = h_2$
> - **Intercambiador de calor**: $\dot{W}=0$, $\Delta EC \approx 0$, $\Delta EP \approx 0$ → $\dot{Q} = \dot{m}(h_2 - h_1)$

> [!demostracion]
> **De la primera ley para sistema cerrado a la forma de VC**
>
> 1. **Sistema cerrado** (masa fija) en instante $t$:
>    $$
>    \frac{dE_{sis}}{dt} = \dot{Q}_{sis} - \dot{W}_{sis}
>    $$
>
> 2. **Sistema cerrado = VC + masa que entra/sale** en $dt$:
>    $$E_{sis}(t+dt) = E_{VC}(t+dt) + \delta m_e e_e$$
>    $$E_{sis}(t) = E_{VC}(t) + \delta m_i e_i$$
>    donde $e = u + C^2/2 + gz$ es la energía total específica.
>
> 3. **Resta** y divide por $dt$:
>    $$
>    \frac{dE_{sis}}{dt} = \frac{dE_{VC}}{dt} + \dot{m}_e e_e - \dot{m}_i e_i
>    $$
>
> 4. **Trabajo total** del sistema cerrado: $\dot{W}_{sis} = \dot{W}_{VC} + \dot{W}_{flujo}$
>    - El trabajo de flujo asociado a la masa que entra/sale:
>      $$\dot{W}_{flujo} = \dot{m}_e (P_e v_e) - \dot{m}_i (P_i v_i)$$
>      (signo: trabajo **hecho por** el sistema para expulsar masa)
>
> 5. **Sustituir** en $\frac{dE_{sis}}{dt} = \dot{Q}_{sis} - \dot{W}_{sis}$:
>    $$\frac{dE_{VC}}{dt} + \dot{m}_e e_e - \dot{m}_i e_i = \dot{Q} - \dot{W}_{VC} - \left[ \dot{m}_e (P_e v_e) - \dot{m}_i (P_i v_i) \right]$$
>
> 6. **Agrupar** términos de flujo:
>    $$\frac{dE_{VC}}{dt} = \dot{Q} - \dot{W}_{VC} + \dot{m}_i (e_i + P_i v_i) - \dot{m}_e (e_e + P_e v_e)$$
>
> 7. **Identificar entalpía**: $h = u + Pv$, y $e = u + C^2/2 + gz$, por lo tanto:
>    $$e + Pv = (u + Pv) + \frac{C^2}{2} + gz = h + \frac{C^2}{2} + gz$$
>
> 8. **Forma final**:
>    $$
>    \frac{dE_{VC}}{dt} = \dot{Q} - \dot{W}_{VC} + \sum_{in} \dot{m}_i \left(h_i + \frac{C_i^2}{2} + gz_i\right) - \sum_{out} \dot{m}_e \left(h_e + \frac{C_e^2}{2} + gz_e\right)
>    $$
>
> **Flujo estacionario** ($dE_{VC}/dt = 0$, $\dot{m}_{in} = \dot{m}_{out} = \dot{m}$):
> $$
> \dot{Q} - \dot{W} = \dot{m} \left( h_2 - h_1 + \frac{C_2^2 - C_1^2}{2} + g(z_2 - z_1) \right)
> $$

## Relaciones con otras notas

> [!info]
> - [[Balance de Masa VC]] (provee $\dot{m}$ y relación entre flujos)
> - [[Entalpia]] ($h$) es la propiedad clave para flujo estacionario
> - [[Balance de Entropia VC]] (complementa para procesos irreversibles)
> - [[Dispositivos de Flujo]] (aplicaciones específicas)

> [!ejemplo]
> **Turbina de vapor** (flujo estacionario, adiabática, despreciando $\Delta EC$ y $\Delta EP$)
>
> Datos: $\dot{m} = 12 kg/s$, $h_1 = 3400 kJ/kg$, $h_2 = 2500 kJ/kg$
>
> Balance: $\dot{Q} = 0$, $\Delta EC = 0$, $\Delta EP = 0$ → $-\dot{W} = \dot{m}(h_2 - h_1)$
>
> $\dot{W} = \dot{m}(h_1 - h_2) = 12 \times (3400 - 2500) = 10800 kW$

> [!ejemplo]
> **Tobera** (flujo estacionario, adiabática, sin trabajo)
>
> Datos: $h_1 = 3200 kJ/kg$, $C_1 = 50 m/s$, $h_2 = 2800 kJ/kg$
>
> Balance: $\dot{Q}=0$, $\dot{W}=0$, $\Delta EP=0$ → $h_1 + C_1^2/2 = h_2 + C_2^2/2$
>
> $C_2 = \sqrt{2(h_1 - h_2) + C_1^2} = \sqrt{2 \times (400 \times 10^3) + 50^2} = \sqrt{800000 + 2500} \approx 896 m/s$

> [!ejemplo]
> **Intercambiador de calor** (agua caliente enfriando)
>
> Datos: $\dot{m}_h = 2 kg/s$, $h_{h,ent} = 600 kJ/kg$, $h_{h,sal} = 400 kJ/kg$
> $\dot{m}_c = 5 kg/s$, $h_{c,ent} = 100 kJ/kg$
>
> Balance: $\dot{Q}=0$ (externamente adiabático), $\dot{W}=0$ → calor cedido por fluido caliente = calor ganado por fluido frío
>
> $\dot{m}_h(h_{h,ent} - h_{h,sal}) = \dot{m}_c(h_{c,sal} - h_{c,ent})$
>
> $h_{c,sal} = h_{c,ent} + \frac{\dot{m}_h}{\dot{m}_c}(h_{h,ent} - h_{h,sal}) = 100 + \frac{2}{5} \times 200 = 180 kJ/kg$

> [!warning]
> - **No confundir** $\dot{W}$ en VC con trabajo de frontera ($P\,dV$) de sistema cerrado. $\dot{W}$ incluye eje, eléctrico, y generalmente **excluye** trabajo de flujo (ya está contabilizado en $h$)
> - La entalpía $h$ **no es** energía total de flujo, sino $h + C^2/2 + gz$
> - En flujo **no estacionario**, el término $dE_{VC}/dt$ NO es despreciable (ej. llenado de tanques)
> - La convención de signos: $\dot{Q}$ hacia el VC (+), $\dot{W}$ realizado por el VC (+)

> [!info]
> **Convención de notación**:
> - $C$: velocidad [m/s] (mayúscula)
> - $c_p$, $c_v$: calores específicos [kJ/kg·K]
> - $h = u + Pv$: [[Entalpia]] específica
> - En flujo estacionario, $\dot{m}$ es constante por [[Balance de Masa VC]]