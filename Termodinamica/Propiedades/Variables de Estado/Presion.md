---
title: "Presión $P$"
tags:
  - termodinamica
  - propiedades
  - variables_de_estado
  - presion
draft: false
aliases:
  - pressure
  - P
---

# Presión $P$

> [!definicion]
> Propiedad **intensiva** de estado. Fuerza normal por unidad de área que ejerce un fluido sobre su frontera:
> $$
> P = \lim_{\delta A \to 0} \frac{\delta F_n}{\delta A} \quad [\text{Pa} = \text{N/m}^2]
> $$
>
> En un fluido en equilibrio, $P$ es isótropa (igual en toda dirección) y uniforme salvo por efectos gravitatorios. En equilibrio termodinámico es **uniforme entre fases** en contacto (equilibrio mecánico).

## Escalas y referencias

> [!proposicion]
> La presión absoluta se mide desde el vacío perfecto:
> $$
> P_{abs} = P_{atm} + P_{man} \qquad P_{vac} = P_{atm} - P_{abs}
> $$
>
> - $P_{abs}$: presión absoluta (la que entra en toda ecuación de estado y en las tablas).
> - $P_{man}$: presión manométrica (positiva sobre la atmosférica).
> - $P_{vac}$: presión de vacío (cuando $P_{abs} < P_{atm}$).

> [!warning]
> Las relaciones termodinámicas y las tablas de propiedades usan **presión absoluta**. Convertir toda lectura manométrica antes de aplicar $Pv = RT$, balances o búsqueda en tablas.

## Variación hidrostática

> [!proposicion]
> Para un fluido en reposo bajo gravedad, con $z$ medido hacia arriba:
> $$
> \frac{dP}{dz} = -\rho g
> $$
>
> Para densidad constante (líquido), entre dos puntos separados una altura $h$:
> $$
> \Delta P = \rho g h
> $$
>
> En un gas, $\rho$ es pequeña y la variación de $P$ con la altura suele despreciarse dentro de un sistema termodinámico.

## Unidades

> [!info]
> | Unidad | Equivalencia |
> |:---|:---|
> | $1\ \text{Pa}$ | $1\ \text{N/m}^2$ |
> | $1\ \text{kPa}$ | $10^3\ \text{Pa}$ |
> | $1\ \text{bar}$ | $10^5\ \text{Pa} = 100\ \text{kPa}$ |
> | $1\ \text{atm}$ | $101.325\ \text{kPa} = 1.01325\ \text{bar}$ |
> | $1\ \text{MPa}$ | $10^6\ \text{Pa} = 10\ \text{bar}$ |

## Papel en el estado termodinámico

> [!teoria]
> Junto con la [[Temperatura]] y el [[Volumen Especifico]], la presión es una de las propiedades intensivas que fija el estado de una sustancia simple compresible. El postulado de estado garantiza que dos propiedades intensivas independientes determinan el estado.
>
> En la región bifásica ([[Calidad]] entre 0 y 1), $P$ y $T$ **no son independientes**: quedan ligadas por la curva de saturación $P_{sat}(T)$. Allí se requiere una tercera propiedad (la calidad) para fijar el estado.

> [!proposicion]
> **Gas ideal:** la presión se relaciona con $T$ y $v$ mediante
> $$
> Pv = RT
> $$
> con $R$ la constante particular del gas. Para gases reales se corrige mediante una [[Ecuaciones de Estado/index | ecuación de estado]] o el factor de compresibilidad $Z = Pv/RT$.

## Relación con otras propiedades

> [!info]
> - Trabajo de frontera en proceso cuasiestático: $\delta W = P\,dV$ (ver [[Primera Ley SC]]).
> - Variable natural de la [[Entalpia]] y de la energía de [[Gibbs]]: $dH = T\,dS + V\,dP$, $dG = -S\,dT + V\,dP$.
> - Derivada de Maxwell asociada (desde $dG$): $\left(\dfrac{\partial S}{\partial P}\right)_T = -\left(\dfrac{\partial V}{\partial T}\right)_P$, ver [[Maxwell]].

> [!info]
> **Convención de notación**:
> - $P$: presión absoluta [kPa]
> - $P_{sat}$: presión de saturación a una temperatura dada [kPa]
> - $\rho$: densidad [kg/m³]
