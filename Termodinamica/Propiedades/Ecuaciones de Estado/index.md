---
title: "Ecuaciones de Estado"
tags:
  - termodinamica
  - propiedades
  - ecuaciones_de_estado
  - index
draft: false
aliases:
  - equations of state
  - EOS
  - ecuación de estado
---

# Ecuaciones de Estado

> [!definicion]
> Una **ecuación de estado** (EOS) es una relación $f(P, v, T) = 0$ entre las variables de estado de una sustancia simple compresible. Fija la tercera propiedad cuando se conocen dos, y es el ingrediente que cierra los balances y las relaciones de propiedades.

## Modelo base: gas ideal

> [!info]
> La EOS más simple es la del [[Gas Ideal]], $Pv = RT$, válida a baja presión y alta temperatura. Sirve de referencia: toda EOS real debe reducirse a ella en el límite $P \to 0$.

## Factor de compresibilidad

> [!proposicion]
> El apartamiento del comportamiento ideal se mide con el factor de compresibilidad:
> $$
> Z = \frac{Pv}{RT}
> $$
> $Z = 1$ para el gas ideal; $Z \lessgtr 1$ según dominen las fuerzas atractivas o el volumen molecular. El **principio de estados correspondientes** expresa $Z$ como función de las propiedades reducidas $P_r = P/P_c$, $T_r = T/T_c$, base de las cartas de compresibilidad generalizadas.

## Ecuaciones de estado reales

> [!info]
> Las EOS cúbicas corrigen el gas ideal con un término atractivo y un covolumen. La de **van der Waals** es el prototipo (ver [[Gas Real]] y [[Problema 04]]):
> $$
> \left(P + \frac{a}{\bar v^{\,2}}\right)(\bar v - b) = R_u T
> $$
> - $a$: corrige la atracción intermolecular.
> - $b$: covolumen (volumen excluido por las moléculas).
>
> Refinamientos habituales: Redlich–Kwong, Soave–Redlich–Kwong y Peng–Robinson, de mejor ajuste cerca del punto crítico.

## Papel en las relaciones de propiedades

> [!teoria]
> La EOS provee las derivadas $\left(\partial P/\partial T\right)_v$ y $\left(\partial v/\partial T\right)_P$ que aparecen en las relaciones de [[Maxwell]] y en las ecuaciones [[TdS]]. Por eso, conocida la EOS y los calores específicos, quedan determinados todos los cambios de [[Energia Interna]], [[Entalpia]] y [[Entropia]].

## Resumen

> [!info]
> | Modelo | Ecuación | Cuándo usar |
> |:---|:---|:---|
> | [[Gas Ideal]] | $Pv = RT$ | baja $P$, alta $T$ |
> | Compresibilidad | $Pv = ZRT$ | desvío moderado, vía cartas |
> | van der Waals / cúbicas | $(P+a/\bar v^2)(\bar v-b)=R_uT$ | gas real, cercanía al crítico |
> | Tablas | datos tabulados | sustancias puras, región bifásica |

> [!info]
> **Convención de notación**:
> - $Z = Pv/RT$: factor de compresibilidad; $P_r$, $T_r$: propiedades reducidas.
> - $a$, $b$: constantes de la EOS cúbica; barra: magnitudes molares.
