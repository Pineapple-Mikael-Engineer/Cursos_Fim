---
title: "Energía Interna $U$"
tags:
  - termodinamica
  - potenciales_termodinamicos
  - primera_ley
draft: false
aliases:
  - internal energy
  - U
---

# Energía Interna $U$

> [!definicion]
> Función de estado extensiva. Energía total de un sistema en equilibrio, excluyendo energía cinética y potencial macroscópicas.

## Energía interna específica y molar

> [!proposicion]
> **Energía interna específica** (por unidad de masa):
> $$
> u = \frac{U}{m} \quad [\text{kJ/kg}]
> $$
> 
> **Energía interna molar** (por unidad de mol):
> $$
> \bar{u} = \frac{U}{n} \quad [\text{kJ/mol}]
> $$
> 
> Relación: $\bar{u} = u \cdot M$, donde $M$ es la masa molar [kg/mol]

## Ecuación fundamental

> [!teorema]
> Para sistema cerrado simple compresible con composición fija:
> $$
> dU = T\,dS - P\,dV
> $$
> 
> Variables naturales: $U(S, V)$

## Relaciones con otras propiedades

> [!info]
> **Con [[Entalpia]]**:
> $$
> H = U + PV
> $$
> 
> **Con [[Entropia]]** (primera ecuación $TdS$):
> $$
> TdS = dU + PdV
> $$
> 
> **Con calor específico a volumen constante**:
> $$
> c_v = \left(\frac{\partial u}{\partial T}\right)_v
> $$
> 
> **Con [[Presion]] y [[Temperatura]]** (desde $dU$):
> $$
> P = -\left(\frac{\partial U}{\partial V}\right)_S, \quad T = \left(\frac{\partial U}{\partial S}\right)_V
> $$

## Derivadas útiles

> [!proposicion]
> **Coeficiente de Joule** (gas ideal):
> $$
> \left(\frac{\partial U}{\partial V}\right)_T = 0
> $$
> 
> **Relación de [[Maxwell]]** (desde $dU$):
> $$
> \left(\frac{\partial T}{\partial V}\right)_S = -\left(\frac{\partial P}{\partial S}\right)_V
> $$

## Casos particulares

> [!proposicion]
> **[[Gas Ideal]]**:
> $$
> du = c_v(T)\,dT
> $$
> Para $c_v$ constante: $\Delta u = c_v \Delta T$
> 
> **Sustancia incompresible**:
> $$
> du = c(T)\,dT
> $$

> [!ejemplo]
> **Calentamiento isocórico de aire** (gas ideal)
> 
> Datos: $m=2kg$, $c_v=0.718 kJ/kg·K$, $T_1=300K$, $T_2=500K$
> 
> Volumen constante → $W=0$ → $\Delta U = Q$
> 
> $\Delta U = m c_v (T_2 - T_1) = 2 \times 0.718 \times 200 = 287.2 kJ$
> 
> Calor requerido: $Q = 287.2 kJ$

> [!warning]
> $U$ es función de estado, pero $\delta Q$ y $\delta W$ no lo son. La igualdad $\Delta U = Q - W$ es válida independientemente del camino, pero $Q$ y $W$ por separado dependen del proceso.