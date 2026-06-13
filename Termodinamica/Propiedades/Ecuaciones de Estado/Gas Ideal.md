---
title: "Gas ideal"
tags:
  - termodinamica
  - propiedades
  - ecuaciones_de_estado
  - gas_ideal
draft: false
aliases:
  - ideal gas
  - gas perfecto
  - ley de los gases ideales
---

# Gas ideal

> [!definicion]
> Modelo de sustancia cuyas moléculas no interaccionan (sin fuerzas atractivas ni volumen propio). Su ecuación de estado liga [[Presion]], [[Volumen Especifico | volumen específico]] y [[Temperatura]]:
> $$
> PV = mRT \qquad Pv = RT \qquad P\bar v = R_u T
> $$
> - $R = R_u/M$: constante particular del gas [kJ/kg·K], con $R_u = 8.314\ \text{kJ/kmol·K}$ y $M$ la masa molar.
> - Forma molar con $\bar v = V/n$.

## Propiedades calóricas

> [!teorema]
> Para un gas ideal, [[Energia Interna]] y [[Entalpia]] dependen **solo de la temperatura** (ley de Joule):
> $$
> u = u(T), \qquad h = u + Pv = u(T) + RT = h(T)
> $$
> En consecuencia los calores específicos son funciones solo de $T$ y cumplen la **relación de Mayer**:
> $$
> du = c_v(T)\,dT, \qquad dh = c_p(T)\,dT, \qquad c_p - c_v = R
> $$
> El cociente $\gamma = c_p/c_v$ caracteriza al gas (aire: $\gamma \approx 1.4$). La independencia de $u$ y $h$ respecto del volumen es el caso límite $a\to 0$ del desarrollo de [[Cp Cv/index | $c_p-c_v$]] para gases reales.

> [!demostracion]
> Que $u = u(T)$ se sigue de la ecuación térmica de la energía (ver [[TdS]] y [[Maxwell]]):
> $$
> \left(\frac{\partial u}{\partial v}\right)_T = T\left(\frac{\partial P}{\partial T}\right)_v - P
> $$
> Con $P = RT/v$ se tiene $\left(\partial P/\partial T\right)_v = R/v$, de modo que $T(R/v) - P = RT/v - RT/v = 0$. La energía interna no depende del volumen.

## Cambios de propiedades

> [!proposicion]
> Entre dos estados, con $c_p$, $c_v$ tratados como constantes (gas ideal calóricamente perfecto):
> $$
> \Delta u = c_v (T_2 - T_1), \qquad \Delta h = c_p (T_2 - T_1)
> $$
> El cambio de [[Entropia]] se obtiene de las ecuaciones [[TdS]]:
> $$
> \Delta s = c_v \ln\frac{T_2}{T_1} + R \ln\frac{v_2}{v_1} = c_p \ln\frac{T_2}{T_1} - R \ln\frac{P_2}{P_1}
> $$

## Procesos isentrópicos

> [!proposicion]
> Imponiendo $\Delta s = 0$ con $c_p$, $c_v$ constantes se obtienen las relaciones isentrópicas:
> $$
> T v^{\gamma-1} = \text{cte}, \qquad T P^{(1-\gamma)/\gamma} = \text{cte}, \qquad P v^{\gamma} = \text{cte}
> $$
> Son el caso politrópico $P v^{\,n} = \text{cte}$ con $n = \gamma$ (ver [[Problema 02]]).

> [!ejemplo]
> **Aire en compresión isentrópica.** De $T_1 = 300\ \text{K}$, $P_1 = 100\ \text{kPa}$ a $P_2 = 800\ \text{kPa}$, con $\gamma = 1.4$:
> $$
> T_2 = T_1 \left(\frac{P_2}{P_1}\right)^{(\gamma-1)/\gamma} = 300\,(8)^{0.2857} = 543.4\ \text{K}
> $$

## Validez del modelo

> [!warning]
> El modelo es preciso a **baja presión y alta temperatura** (lejos de la saturación), donde el volumen específico es grande y las interacciones moleculares son despreciables. Falla cerca del punto crítico, en la región bifásica y a altas presiones; allí se requiere una [[Ecuaciones de Estado/index | ecuación de estado]] real o el factor de compresibilidad:
> $$
> Z = \frac{Pv}{RT}, \qquad Z \to 1 \text{ en el límite ideal}
> $$
> El desvío $Z \ne 1$ mide cuánto se aparta el [[Gas Real | gas real]] del comportamiento ideal.

## Relación con otras notas

> [!info]
> - Caso límite de la [[Ecuaciones de Estado/index | ecuación de estado]] general.
> - Sus calores específicos y la relación $c_p - c_v = R$ se generalizan en [[Cp Cv/index | $c_p-c_v$]].
> - Aparece como hipótesis en casi todos los problemas con aire o gases (ver [[Problema 02]]).

> [!info]
> **Convención de notación**:
> - $R$: constante particular [kJ/kg·K]; $R_u = 8.314\ \text{kJ/kmol·K}$: universal.
> - $\gamma = c_p/c_v$; $Z = Pv/RT$: factor de compresibilidad.
> - barra: magnitudes molares.
