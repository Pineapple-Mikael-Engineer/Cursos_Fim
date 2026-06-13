---
title: "Energía de Gibbs $G$"
tags:
  - termodinamica
  - potenciales_termodinamicos
  - gibbs
draft: false
aliases:
  - Gibbs free energy
  - energía libre de Gibbs
  - entalpía libre
  - G
---

# Energía de Gibbs $G$

> [!definicion]
> Función de estado extensiva definida a partir de [[Entalpia]] y [[Entropia]]:
> $$
> G \equiv H - TS = U + PV - TS = F + PV
> $$
> Es el potencial natural de las variables $(T, P)$ —las dos más fáciles de controlar en el laboratorio—, lo que lo hace central en cambios de fase y equilibrio químico.

## Energía específica y molar

> [!proposicion]
> **Específica** y **molar**:
> $$
> g = \frac{G}{m} = h - Ts \quad [\text{kJ/kg}], \qquad \bar g = \frac{G}{n} = \bar h - T\bar s
> $$
> La forma molar $\bar g$ es el **potencial químico** $\mu$ de una sustancia pura.

## Ecuación fundamental

> [!teorema]
> De $G = H - TS$ y $dH = T\,dS + V\,dP$ (ver [[Entalpia]]):
> $$
> dG = -S\,dT + V\,dP
> $$
> Variables naturales: $G(T, P)$. Derivadas:
> $$
> S = -\left(\frac{\partial G}{\partial T}\right)_P, \qquad V = \left(\frac{\partial G}{\partial P}\right)_T
> $$

## Relación de Maxwell asociada

> [!proposicion]
> Por la igualdad de derivadas cruzadas de $dG$ (ver [[Maxwell]]):
> $$
> \left(\frac{\partial S}{\partial P}\right)_T = -\left(\frac{\partial V}{\partial T}\right)_P
> $$
> Genera la segunda ecuación [[TdS]] y permite calcular cambios de entropía con la presión a partir de la [[Ecuaciones de Estado/index | ecuación de estado]].

## Criterio de equilibrio

> [!teorema]
> Para un sistema a $T$ y $P$ constantes, todo proceso espontáneo cumple
> $$
> dG \le 0
> $$
> y el equilibrio corresponde al **mínimo** de $G$. Es el criterio de equilibrio más usado por operar en las condiciones habituales de procesos a presión atmosférica.

## Equilibrio de fases: relación de Clapeyron

> [!proposicion]
> En una transición de fase a $T$ y $P$ de saturación, ambas fases coexisten con **igual energía de Gibbs específica**:
> $$
> g_f = g_g
> $$
> De $dg_f = dg_g$ a lo largo de la curva de saturación se obtiene la ecuación de **Clapeyron**:
> $$
> \left(\frac{dP}{dT}\right)_{sat} = \frac{s_{fg}}{v_{fg}} = \frac{h_{fg}}{T\,v_{fg}}
> $$
> que liga la pendiente de la curva de saturación con la entalpía de vaporización (ver [[Calidad]] para la notación $f$, $g$, $fg$).

## Trabajo útil máximo

> [!proposicion]
> Para un proceso isotérmico e isobárico, $-\Delta G$ acota el **trabajo útil** (distinto del de frontera $P\,dV$) que puede extraerse. Es la base del rendimiento de pilas de combustible y de la espontaneidad en reacciones a $T,P$ constantes.

## Relación con otras notas

> [!info]
> - Junto con [[Energia Interna]], [[Entalpia]] y [[Helmholtz]] forma los cuatro [[Potenciales Termodinamicos/index | potenciales termodinámicos]].
> - Genera una relación de [[Maxwell]] y la segunda ecuación [[TdS]].
> - Su igualdad entre fases ($g_f = g_g$) es el criterio de [[Equilibrio de Fases | equilibrio de fases]].

> [!info]
> **Convención de notación**:
> - $G$: extensiva [kJ]; $g$: específica [kJ/kg]; $\bar g = \mu$: molar = potencial químico.
> - subíndice $fg$: diferencia vapor − líquido saturados.
