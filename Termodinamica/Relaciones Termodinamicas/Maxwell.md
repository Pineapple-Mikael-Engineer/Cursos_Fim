---
title: "Relaciones de Maxwell"
tags:
  - termodinamica
  - relaciones_termodinamicas
  - maxwell
  - potenciales_termodinamicos
draft: false
aliases:
  - Maxwell relations
  - relaciones de Maxwell
---

# Relaciones de Maxwell

> [!definicion]
> Conjunto de cuatro igualdades entre derivadas parciales de las variables de estado, obtenidas al imponer la **igualdad de las derivadas parciales cruzadas** sobre los diferenciales exactos de los cuatro [[Potenciales Termodinamicos/index | potenciales termodinámicos]]. Permiten sustituir derivadas de la [[Entropia]] —no medibles directamente— por derivadas de $P$, $v$ y $T$, sí medibles. Se construyen sobre la [[Ecuaciones de Estado/index | ecuación de estado]] de la sustancia.

## Las cuatro relaciones

> [!teorema]
> Para una sustancia simple compresible (forma específica, por unidad de masa):
> $$
> \left(\frac{\partial T}{\partial v}\right)_s = -\left(\frac{\partial P}{\partial s}\right)_v \qquad \text{(desde } u\text{)}
> $$
> $$
> \left(\frac{\partial T}{\partial P}\right)_s = \left(\frac{\partial v}{\partial s}\right)_P \qquad \text{(desde } h\text{)}
> $$
> $$
> \left(\frac{\partial s}{\partial v}\right)_T = \left(\frac{\partial P}{\partial T}\right)_v \qquad \text{(desde } f\text{)}
> $$
> $$
> \left(\frac{\partial s}{\partial P}\right)_T = -\left(\frac{\partial v}{\partial T}\right)_P \qquad \text{(desde } g\text{)}
> $$
>
> Las dos últimas son las de mayor valor práctico: expresan cambios de entropía en términos de la [[Ecuaciones de Estado/index | ecuación de estado]] $P\text{-}v\text{-}T$.

## Origen: exactitud de los diferenciales

> [!demostracion]
> Cada potencial tiene un diferencial exacto con dos variables naturales. Para una función de estado $dz = M\,dx + N\,dy$, la exactitud exige $\left(\partial M/\partial y\right)_x = \left(\partial N/\partial x\right)_y$.
>
> **Energía de [[Helmholtz]]** $f = u - Ts$, con $df = -s\,dT - P\,dv$:
> $$
> M = -s = \left(\frac{\partial f}{\partial T}\right)_v, \quad N = -P = \left(\frac{\partial f}{\partial v}\right)_T
> \;\Rightarrow\;
> \left(\frac{\partial s}{\partial v}\right)_T = \left(\frac{\partial P}{\partial T}\right)_v
> $$
>
> **Energía de [[Gibbs]]** $g = h - Ts$, con $dg = -s\,dT + v\,dP$:
> $$
> \left(\frac{\partial(-s)}{\partial P}\right)_T = \left(\frac{\partial v}{\partial T}\right)_P
> \;\Rightarrow\;
> \left(\frac{\partial s}{\partial P}\right)_T = -\left(\frac{\partial v}{\partial T}\right)_P
> $$
>
> Las otras dos se siguen igual de $du = T\,ds - P\,dv$ (ver [[Energia Interna]]) y $dh = T\,ds + v\,dP$ (ver [[Entalpia]]).

## Regla mnemotécnica

> [!regla]
> Cada relación nace del diferencial de un potencial y sus dos variables naturales:
>
> | Potencial | Diferencial | Variables naturales | Relación de Maxwell |
> |:---|:---|:---|:---|
> | $u$ ([[Energia Interna]]) | $du = T\,ds - P\,dv$ | $(s,v)$ | $\left(\partial T/\partial v\right)_s = -\left(\partial P/\partial s\right)_v$ |
> | $h$ ([[Entalpia]]) | $dh = T\,ds + v\,dP$ | $(s,P)$ | $\left(\partial T/\partial P\right)_s = \left(\partial v/\partial s\right)_P$ |
> | $f$ ([[Helmholtz]]) | $df = -s\,dT - P\,dv$ | $(T,v)$ | $\left(\partial s/\partial v\right)_T = \left(\partial P/\partial T\right)_v$ |
> | $g$ ([[Gibbs]]) | $dg = -s\,dT + v\,dP$ | $(T,P)$ | $\left(\partial s/\partial P\right)_T = -\left(\partial v/\partial T\right)_P$ |
>
> El signo lo fija el signo del término $P\,dv$ frente a $v\,dP$ en cada diferencial.

## Aplicaciones

> [!proposicion]
> **Cambio de entropía desde la ecuación de estado.** Sustituyendo las dos relaciones con $T$ constante en los diferenciales de la [[Entropia]] se obtienen las [[TdS | ecuaciones $TdS$]], que permiten integrar $\Delta s$ conociendo solo $P\text{-}v\text{-}T$ y los calores específicos.

> [!ejemplo]
> **Gas ideal: verificación.** Con $Pv = RT$,
> $$
> \left(\frac{\partial P}{\partial T}\right)_v = \frac{R}{v}, \qquad \left(\frac{\partial s}{\partial v}\right)_T = \frac{R}{v}
> $$
> La relación de Maxwell desde $f$ reproduce el término $R\,dv/v$ que aparece en el cambio de entropía del [[Gas Ideal]], sin necesidad de medir la entropía directamente.

> [!proposicion]
> **Relación de Clapeyron.** Aplicada a la transición de fase, la relación desde $f$ conduce a
> $$
> \left(\frac{dP}{dT}\right)_{sat} = \frac{s_{fg}}{v_{fg}} = \frac{h_{fg}}{T\,v_{fg}}
> $$
> que liga la pendiente de la curva de saturación con la entalpía de vaporización (ver [[Calidad]] para la notación $f$, $g$, $fg$).

> [!warning]
> Las relaciones de Maxwell valen para sustancias simples compresibles en equilibrio, donde el estado se fija con dos propiedades intensivas independientes. Con trabajo adicional (eléctrico, magnético, superficial) aparecen potenciales y relaciones extra.

## Relación con otras notas

> [!info]
> - Derivan de los cuatro [[Potenciales Termodinamicos/index | potenciales]]; revisar sus variables naturales antes de aplicarlas.
> - Alimentan las [[TdS | ecuaciones $TdS$]] y las relaciones [[Cp Cv/index | $c_p - c_v$]].
> - Caso particular de verificación: [[Gas Ideal]].

> [!info]
> **Convención de notación**:
> - Forma específica (minúsculas): $u$, $h$, $f$, $g$, $s$, $v$ por unidad de masa; misma forma para las versiones molares con barra.
> - $f = u - Ts$: Helmholtz; $g = h - Ts$: Gibbs.
> - subíndice $fg$: diferencia vapor − líquido saturados.
