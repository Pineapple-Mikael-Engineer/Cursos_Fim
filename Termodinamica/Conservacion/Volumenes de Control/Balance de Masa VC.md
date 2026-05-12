---
title: "Balance de Masa (Volumen de Control)"
tags:
  - termodinamica
  - conservacion
  - masa
  - volumen_de_control
draft: false
aliases:
  - continuidad
  - conservation of mass
  - balance de masa
---

# Balance de Masa (Volumen de Control)

> [!definicion]
> Principio de conservación de la masa para un [[Volumenes de Control]] fijo en el espacio:
> $$
> \frac{dm_{VC}}{dt} = \sum_{in} \dot{m}_i - \sum_{out} \dot{m}_e
> $$
> 
> - $m_{VC} = \int_{VC} \rho \, dV$: masa contenida en el VC [kg]
> - $\dot{m} = \rho C A$: flujo másico a través de una sección [kg/s]
> - $\rho$: densidad [kg/m³]
> - $C$: velocidad normal al área [m/s]
> - $A$: área de la sección [m²]

## Formas particulares

> [!proposicion]
> **Flujo estacionario** ($dm_{VC}/dt = 0$):
> $$
> \sum_{in} \dot{m}_i = \sum_{out} \dot{m}_e
> $$
> 
> **Una entrada, una salida, flujo estacionario**:
> $$
> \dot{m}_1 = \dot{m}_2 \quad \Rightarrow \quad \rho_1 C_1 A_1 = \rho_2 C_2 A_2
> $$
> 
> **Flujo incompresible** ($\rho = \text{constante}$):
> $$
> \sum_{in} (C A)_i = \sum_{out} (C A)_e
> $$
> Para una entrada y una salida: $C_1 A_1 = C_2 A_2$

> [!demostracion]
> **De la forma integral a la forma de tasa**
> 
> 1. **Balance integral** para un VC fijo:
>    $$
>    \frac{d}{dt} \int_{VC} \rho \, dV = - \int_{SC} \rho (\vec{C} \cdot \hat{n}) \, dA
>    $$
>    - $SC$: superficie de control
>    - $\hat{n}$: vector normal unitario **saliente**
>    - $\vec{C} \cdot \hat{n} > 0$ donde el flujo sale
> 
> 2. **Discretización por portales** (entradas/salidas discretas):
>    - En cada entrada: $\vec{C} \cdot \hat{n} < 0$, se define $\dot{m}_i = -\int \rho (\vec{C} \cdot \hat{n}) dA > 0$
>    - En cada salida: $\vec{C} \cdot \hat{n} > 0$, se define $\dot{m}_e = \int \rho (\vec{C} \cdot \hat{n}) dA > 0$
> 
> 3. **Hipótesis de flujo unidimensional** (propiedades uniformes en cada sección):
>    $$
>    \dot{m} = \rho C A
>    $$
>    donde $C$ es la velocidad promedio.
> 
> 4. **Sustitución**:
>    $$
>    \frac{d}{dt} \int_{VC} \rho dV = \sum_{in} \dot{m}_i - \sum_{out} \dot{m}_e
>    $$
>    El signo negativo de la integral se absorbe invirtiendo el producto punto para las entradas.
> 
> **Caso flujo estacionario** ($\partial/\partial t = 0$):
> - Acumulación nula → $\sum \dot{m}_{in} = \sum \dot{m}_{out}$
> 
> **Caso flujo incompresible** ($\rho = \text{constante}$):
> - $dm_{VC}/dt = \rho \, dV_{VC}/dt$. Si además VC rígido ($dV_{VC}/dt=0$):
>   $$
>   \sum_{in} (CA)_i = \sum_{out} (CA)_e
>   $$

> [!info]
> El balance de masa se acopla con:
> - [[Balance de Energia VC]] (términos $\dot{m}$ aparecen multiplicando propiedades específicas)
> - [[Balance de Entropia VC]] (términos $\dot{m}s$)
> - [[Volumen Especifico]] ($v = 1/\rho$)

> [!ejemplo]
> **Llenado de tanque rígido** (flujo no estacionario)
> 
> Un tanque rígido vacío se llena desde una línea a presión constante. Válvula se abre y entra aire con $\dot{m}_{in} = 0.02 kg/s$ constante.
> 
> Balance: $\frac{dm_{VC}}{dt} = \dot{m}_{in}$
> 
> Integrando: $m_{VC}(t) = \dot{m}_{in} \cdot t = 0.02 t$
> 
> Si volumen del tanque $V = 0.5 m^3$, el llenado se completa cuando $\rho = m_{VC}/V$ iguala la densidad de la línea.

> [!ejemplo]
> **Tobera** (flujo estacionario, una entrada, una salida)
> 
> Datos: $C_1 = 50 m/s$, $A_1 = 0.01 m^2$, $\rho_1 = 4 kg/m^3$, $A_2 = 0.002 m^2$, $\rho_2 = 2 kg/m^3$
> 
> $\dot{m} = \rho_1 C_1 A_1 = 4 \times 50 \times 0.01 = 2 kg/s$
> 
> Velocidad de salida: $C_2 = \dot{m} / (\rho_2 A_2) = 2 / (2 \times 0.002) = 500 m/s$

> [!warning]
> - El balance de masa **no se aplica por especie** si hay reacciones químicas (ver [[Combustion]])
> - En flujo supersónico, la densidad varía fuertemente; no usar aproximación incompresible
> - Para VC con deformación de frontera (ej. pistón), la forma general es más compleja

> [!info]
> **Convención de signos**:
> - $\dot{m}_{in}$ positivo al VC
> - $\dot{m}_{out}$ positivo desde el VC
> - La ecuación está escrita como acumulación = entrada - salida
