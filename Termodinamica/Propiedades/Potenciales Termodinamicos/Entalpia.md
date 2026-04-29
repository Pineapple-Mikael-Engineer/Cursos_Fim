---
title: "Entalpía $H$"
tags:
  - termodinamica
  - potenciales_termodinamicos
  - primera_ley
draft: false
aliases:
  - enthalpy
  - H
---

# Entalpía $H$

> [!definicion]
> Función de estado extensiva definida a partir de [[Energia Interna]]:
> $$
> H \equiv U + PV
> $$
> 
> Útil para sistemas con transformaciones a presión constante o con flujo de masa.

## Entalpía específica y molar

> [!proposicion]
> **Entalpía específica** (por unidad de masa):
> $$
> h = \frac{H}{m} = u + Pv \quad [\text{kJ/kg}]
> $$
> donde $v = V/m$ es el [[Volumen Especifico]]
> 
> **Entalpía molar** (por unidad de mol):
> $$
> \bar{h} = \frac{H}{n} = \bar{u} + P\bar{v} \quad [\text{kJ/mol}]
> $$

## Ecuación fundamental

> [!teorema]
> De la definición $H = U + PV$ y $dU = TdS - PdV$:
> $$
> dH = T\,dS + V\,dP
> $$
> 
> Variables naturales: $H(S, P)$

## Relaciones con otras propiedades

> [!info]
> **Con [[Entropia]]** (segunda ecuación $TdS$):
> $$
> TdS = dH - VdP
> $$
> 
> **Con calor específico a presión constante**:
> $$
> c_p = \left(\frac{\partial h}{\partial T}\right)_P
> $$
> 
> **Con [[Temperatura]] y [[Volumen Especifico]]** (desde $dH$):
> $$
> T = \left(\frac{\partial H}{\partial S}\right)_P, \quad V = \left(\frac{\partial H}{\partial P}\right)_S
> $$
> 
> **Relación entre $c_p$ y $c_v$** para [[Gas Ideal]]:
> $$
> c_p - c_v = R
> $$
> donde $R$ es la constante particular del gas

## Derivadas útiles

> [!proposicion]
> **Coeficiente de Joule-Thomson**:
> $$
> \mu_{JT} = \left(\frac{\partial T}{\partial P}\right)_H
> $$
> Describe el cambio de temperatura en una expansión isentálpica (válvula de estrangulamiento)
> 
> **Relación de [[Maxwell]]** (desde $dH$):
> $$
> \left(\frac{\partial T}{\partial P}\right)_S = \left(\frac{\partial V}{\partial S}\right)_P
> $$

## Casos particulares

> [!proposicion]
> **[[Gas Ideal]]**:
> - $h = h(T)$ solamente (independiente de $P$)
> - $dh = c_p(T)\,dT$
> - $c_p$ constante: $\Delta h = c_p \Delta T$
> 
> **Sustancia incompresible** ($v$ constante):
> $$
> dh = c(T)\,dT + v\,dP
> $$
> Para cambios de presión moderados, $v\,dP$ suele ser despreciable frente a $c\,dT$

## Uso en primera ley

> [!teorema]
> **Para [[Sistemas Cerrados]]** a presión constante ($dP=0$, $W_{borde} = P\Delta V$):
> $$
> Q_P = \Delta H
> $$
> 
> **Para [[Volumenes de Control]] en [[Flujo Estacionario]]** (unidimensional, una entrada, una salida):
> $$
> \dot{Q} - \dot{W}_{eje} = \dot{m}(h_2 - h_1) + \dot{m}\left(\frac{C_2^2 - C_1^2}{2}\right) + \dot{m}g(z_2 - z_1)
> $$
> Despreciando energía cinética y potencial:
> $$
> \dot{Q} - \dot{W}_{eje} = \dot{m}(h_2 - h_1)
> $$

> [!ejemplo]
> **Calentamiento de agua en caldera** (proceso isobárico)
> 
> Datos: $m=5kg$ de agua, $P=1atm$, $T_1=20°C$ (líquido subenfriado), $T_2=100°C$ (vapor saturado). De tablas: $h_1 \approx 83.9 kJ/kg$, $h_2 = 2676 kJ/kg$
> 
> A presión constante, $Q = \Delta H = m(h_2 - h_1)$
> 
> $Q = 5 \times (2676 - 83.9) = 5 \times 2592.1 = 12960.5 kJ$

> [!ejemplo]
> **Turbina de vapor** (volumen de control, adiabática, despreciando $\Delta EC$ y $\Delta EP$)
> 
> Datos: $\dot{m}=10 kg/s$, $h_1=3400 kJ/kg$, $h_2=2500 kJ/kg$, $C_1 \approx C_2$
> 
> $\dot{Q}=0$ → $-\dot{W}_{eje} = \dot{m}(h_2 - h_1)$
> 
> $\dot{W}_{eje} = \dot{m}(h_1 - h_2) = 10 \times (3400 - 2500) = 9000 kW$

> [!warning]
> **No usar $H$ directamente** cuando:
> - El sistema es cerrado y el trabajo no es únicamente $P\Delta V$ (ej. trabajo de eje en sistema cerrado)
> - Hay flujo no estacionario en volumen de control (usar balances integrales)
> 
> **En válvulas de estrangulamiento**: $h_2 = h_1$ (proceso isentálpico), incluso si $P$ y $T$ cambian

> [!info]
> **Convención de notación**:
> - $C$: velocidad [m/s]
> - $c_p$, $c_v$: calores específicos [kJ/kg·K]
> - $v$: [[Volumen Especifico]] [m³/kg]