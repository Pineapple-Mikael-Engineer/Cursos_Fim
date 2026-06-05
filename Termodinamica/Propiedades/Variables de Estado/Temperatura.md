---
title: "Temperatura $T$"
tags:
  - termodinamica
  - propiedades
  - variables_de_estado
  - temperatura
draft: false
aliases:
  - temperature
  - T
---

# Temperatura $T$

> [!definicion]
> Propiedad **intensiva** de estado que mide el nivel de energía térmica y determina la dirección de la transferencia de calor: el calor fluye espontáneamente del cuerpo de mayor $T$ al de menor $T$.
>
> En equilibrio termodinámico, $T$ es **uniforme** en todo el sistema (equilibrio térmico) e **igual entre fases** en contacto.

## Ley cero y equilibrio térmico

> [!axioma]
> **Ley cero de la termodinámica.** Si dos sistemas están cada uno en equilibrio térmico con un tercero, lo están entre sí.
>
> La ley cero garantiza la existencia de una propiedad —la temperatura— cuyo valor común caracteriza el equilibrio térmico, y da fundamento a la medición mediante termómetros.

## Escalas

> [!proposicion]
> Escala absoluta (Kelvin) y escala Celsius:
> $$
> T[\text{K}] = T[^\circ\text{C}] + 273.15
> $$
>
> Una diferencia de temperatura es idéntica en ambas: $\Delta T[\text{K}] = \Delta T[^\circ\text{C}]$.

> [!warning]
> Toda relación termodinámica que contiene $T$ de forma absoluta —ecuación de estado, rendimientos de Carnot, $\delta Q_{rev}=T\,dS$, integrales de entropía— exige **kelvin**. Usar grados Celsius solo es válido en diferencias.

## Temperatura termodinámica

> [!teorema]
> La escala absoluta se define de forma independiente de la sustancia a partir de la segunda ley. Para una máquina reversible operando entre dos focos:
> $$
> \frac{Q_C}{Q_F} = \frac{T_C}{T_F}
> $$
>
> Equivalentemente, desde la ecuación fundamental:
> $$
> \frac{1}{T} = \left(\frac{\partial S}{\partial U}\right)_V
> $$
> que expresa $T$ como la respuesta de la energía interna al cambio de [[Entropia]] a volumen constante (ver [[Energia Interna]]).

## Gas ideal como termómetro

> [!proposicion]
> A presión suficientemente baja todos los gases satisfacen $Pv = RT$, lo que permite usar el gas ideal como termómetro:
> $$
> T = \lim_{P \to 0} \frac{Pv}{R}
> $$
> La escala del gas ideal coincide con la escala termodinámica de Kelvin.

## Papel en el estado termodinámico

> [!teoria]
> Junto con [[Presion]] y [[Volumen Especifico]], $T$ fija el estado de una sustancia simple compresible (postulado de estado: dos propiedades intensivas independientes).
>
> En la región bifásica, $T$ y $P$ quedan ligadas por la saturación $T_{sat}(P)$ y dejan de ser independientes; se necesita la [[Calidad]] para fijar el estado.

## Relación con otras propiedades

> [!info]
> - Variable natural de la energía de [[Helmholtz]] y de [[Gibbs]]: $dF = -S\,dT - P\,dV$, $dG = -S\,dT + V\,dP$.
> - Calores específicos: $c_v = \left(\dfrac{\partial u}{\partial T}\right)_v$, $c_p = \left(\dfrac{\partial h}{\partial T}\right)_P$.
> - Calor reversible: $\delta Q_{rev} = T\,dS$ (ver [[TdS]]).

> [!info]
> **Convención de notación**:
> - $T$: temperatura absoluta [K]
> - $T_{sat}$: temperatura de saturación a una presión dada [K]
> - $T_C$, $T_F$: temperaturas de foco caliente y frío [K]
