---
title: "Potenciales Termodinámicos"
tags:
  - termodinamica
  - potenciales_termodinamicos
  - index
draft: false
aliases:
  - thermodynamic potentials
  - potenciales termodinámicos
  - energías libres
---

# Potenciales Termodinámicos

> [!definicion]
> Cuatro funciones de estado extensivas cuyos diferenciales exactos generan, por las parejas de variables naturales, toda la estructura de relaciones de propiedades. Se obtienen de la [[Energia Interna]] mediante transformadas de Legendre que intercambian una variable extensiva por su conjugada intensiva.

## Los cuatro potenciales

> [!teorema]
> | Potencial | Definición | Diferencial | Variables naturales |
> |:---|:---|:---|:---|
> | [[Energia Interna]] $U$ | — | $dU = T\,dS - P\,dV$ | $(S, V)$ |
> | [[Entalpia]] $H$ | $H = U + PV$ | $dH = T\,dS + V\,dP$ | $(S, P)$ |
> | [[Helmholtz]] $F$ | $F = U - TS$ | $dF = -S\,dT - P\,dV$ | $(T, V)$ |
> | [[Gibbs]] $G$ | $G = H - TS$ | $dG = -S\,dT + V\,dP$ | $(T, P)$ |
>
> Cada potencial es mínimo en el equilibrio cuando se mantienen constantes **sus** variables naturales.

## Idea unificadora

> [!teoria]
> De cada diferencial se leen directamente las propiedades como derivadas primeras (p. ej. $T = (\partial U/\partial S)_V$, $V = (\partial G/\partial P)_T$), y de la igualdad de derivadas cruzadas surgen las cuatro relaciones de [[Maxwell]]. Combinándolas con los calores específicos se obtienen las ecuaciones [[TdS]] y la relación [[Cp Cv/index | $c_p-c_v$]]. Toda la termodinámica de propiedades de una sustancia simple cabe en este esquema.

## Elección del potencial según el proceso

> [!regla]
> Se usa el potencial cuyas variables naturales se mantienen constantes en el proceso:
> - $S, V$ constantes → [[Energia Interna]].
> - $S, P$ constantes → [[Entalpia]] (procesos a presión constante, flujo).
> - $T, V$ constantes → [[Helmholtz]] (trabajo máximo isotérmico).
> - $T, P$ constantes → [[Gibbs]] (cambios de fase, equilibrio químico).

## Criterios de equilibrio

> [!proposicion]
> Para un sistema aislado, el equilibrio maximiza la [[Entropia]]. En condiciones controladas equivale al **mínimo** del potencial adecuado:
> $$
> (dU)_{S,V} \le 0, \quad (dH)_{S,P} \le 0, \quad (dF)_{T,V} \le 0, \quad (dG)_{T,P} \le 0
> $$

## Relación con otras notas

> [!info]
> - Propiedad auxiliar de aprovechamiento: [[Exergia]] (trabajo útil máximo respecto a un ambiente).
> - Maquinaria derivada: [[Maxwell]], [[TdS]], [[Cp Cv/index | $c_p-c_v$]].
> - Caso modelo: [[Gas Ideal]].

> [!info]
> **Convención de notación**:
> - mayúscula: potencial extensivo ($U, H, F, G$); minúscula: específico; barra: molar.
> - $\bar g = \mu$: potencial químico de la sustancia pura.
