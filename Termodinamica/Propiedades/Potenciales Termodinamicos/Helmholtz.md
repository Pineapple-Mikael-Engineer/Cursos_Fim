---
title: "Energía de Helmholtz $F$"
tags:
  - termodinamica
  - potenciales_termodinamicos
  - helmholtz
draft: false
aliases:
  - Helmholtz free energy
  - energía libre de Helmholtz
  - F
  - A
---

# Energía de Helmholtz $F$

> [!definicion]
> Función de estado extensiva definida a partir de [[Energia Interna]] y [[Entropia]]:
> $$
> F \equiv U - TS
> $$
> Es el potencial natural de las variables $(T, V)$ y mide el **trabajo máximo** extraíble de un sistema en un proceso isotérmico.

## Energía específica y molar

> [!proposicion]
> **Específica** (por unidad de masa) y **molar** (por unidad de mol):
> $$
> f = \frac{F}{m} = u - Ts \quad [\text{kJ/kg}], \qquad \bar f = \frac{F}{n} = \bar u - T\bar s
> $$

## Ecuación fundamental

> [!teorema]
> De $F = U - TS$ y $dU = T\,dS - P\,dV$ (ver [[Energia Interna]]):
> $$
> dF = -S\,dT - P\,dV
> $$
> Variables naturales: $F(T, V)$. Derivadas:
> $$
> S = -\left(\frac{\partial F}{\partial T}\right)_V, \qquad P = -\left(\frac{\partial F}{\partial V}\right)_T
> $$

## Relación de Maxwell asociada

> [!proposicion]
> Por la igualdad de derivadas cruzadas de $dF$ (ver [[Maxwell]]):
> $$
> \left(\frac{\partial S}{\partial V}\right)_T = \left(\frac{\partial P}{\partial T}\right)_V
> $$
> Es la relación de mayor uso práctico: liga un cambio de entropía con la [[Ecuaciones de Estado/index | ecuación de estado]] $P\text{-}v\text{-}T$, y genera la primera ecuación [[TdS]].

## Trabajo máximo isotérmico

> [!teorema]
> Para un proceso **isotérmico** ($dT = 0$), de $dF = -S\,dT - \delta W$ en condiciones reversibles:
> $$
> W_{rev,T} = -\Delta F = F_1 - F_2
> $$
> En un proceso isotérmico real (irreversible), $W \le -\Delta F$: la disminución de la energía de Helmholtz acota el trabajo obtenible.

## Criterio de equilibrio

> [!proposicion]
> Para un sistema a $T$ y $V$ constantes, todo proceso espontáneo cumple
> $$
> dF \le 0
> $$
> y el equilibrio corresponde al **mínimo** de $F$. Es el criterio de equilibrio análogo al de [[Gibbs]] (que opera a $T$ y $P$ constantes).

## Casos particulares

> [!proposicion]
> **[[Gas Ideal]]:** combinando $u = u(T)$ y $s(T,v)$, la energía de Helmholtz específica es
> $$
> f(T,v) = u(T) - T s(T,v), \qquad \left(\frac{\partial f}{\partial v}\right)_T = -P = -\frac{RT}{v}
> $$
> que reproduce la ecuación de estado al derivar respecto del volumen.

## Relación con otras notas

> [!info]
> - Junto con [[Energia Interna]], [[Entalpia]] y [[Gibbs]] forma los cuatro [[Potenciales Termodinamicos/index | potenciales termodinámicos]].
> - Genera una relación de [[Maxwell]] y la primera ecuación [[TdS]].
> - Su mínimo a $T,V$ constantes fija el equilibrio termodinámico y de fases.

> [!info]
> **Convención de notación**:
> - $F$: extensiva [kJ]; $f$: específica [kJ/kg]; $\bar f$: molar.
> - Algunos textos la denotan $A$ (de *Arbeit*, trabajo).
