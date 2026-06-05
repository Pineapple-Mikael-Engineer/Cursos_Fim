---
title: "Relación $c_p - c_v$"
tags:
  - termodinamica
  - relaciones_termodinamicas
  - calores_especificos
  - index
draft: false
aliases:
  - cp menos cv
  - relación de Mayer
  - diferencia de calores específicos
---

# Relación $c_p - c_v$

> [!definicion]
> Los calores específicos a presión y a volumen constante miden la respuesta térmica de [[Entalpia]] y [[Energia Interna]]:
> $$
> c_v = \left(\frac{\partial u}{\partial T}\right)_v = T\left(\frac{\partial s}{\partial T}\right)_v, \qquad c_p = \left(\frac{\partial h}{\partial T}\right)_P = T\left(\frac{\partial s}{\partial T}\right)_P
> $$
> Su diferencia se expresa enteramente en términos de la [[Ecuaciones de Estado/index | ecuación de estado]].

## Relación general

> [!teorema]
> Igualando las dos ecuaciones [[TdS]] se obtiene:
> $$
> c_p - c_v = T\left(\frac{\partial P}{\partial T}\right)_v \left(\frac{\partial v}{\partial T}\right)_P
> = -\,T\,\frac{\left(\partial v/\partial T\right)_P^{\,2}}{\left(\partial v/\partial P\right)_T}
> $$
> La segunda forma, vía la regla cíclica, muestra que el signo está garantizado.

> [!demostracion]
> Las dos ecuaciones [[TdS]] son $T\,ds = c_v\,dT + T\left(\partial P/\partial T\right)_v dv$ y $T\,ds = c_p\,dT - T\left(\partial v/\partial T\right)_P dP$. Igualando y despejando $dT$:
> $$
> (c_p - c_v)\,dT = T\left(\frac{\partial P}{\partial T}\right)_v dv + T\left(\frac{\partial v}{\partial T}\right)_P dP
> $$
> Tomando $T = T(v, P)$ e identificando el coeficiente de $dv$ a $P$ constante se llega a la relación general. La regla cíclica $\left(\partial P/\partial T\right)_v = -\left(\partial v/\partial T\right)_P/\left(\partial v/\partial P\right)_T$ da la segunda forma.

## Signo y consecuencias

> [!proposicion]
> Como la compresibilidad isoterma satisface $\left(\partial v/\partial P\right)_T < 0$ para toda sustancia estable, y el numerador es un cuadrado:
> $$
> c_p - c_v \ge 0 \;\Rightarrow\; c_p \ge c_v
> $$
> La igualdad $c_p = c_v$ ocurre cuando $\left(\partial v/\partial T\right)_P = 0$ (p. ej. el agua líquida a $4\ ^\circ\text{C}$, donde la densidad es máxima).

## Casos particulares

> [!proposicion]
> **[[Gas Ideal]] (relación de Mayer).** Con $\left(\partial P/\partial T\right)_v = R/v$ y $\left(\partial v/\partial T\right)_P = R/P$:
> $$
> c_p - c_v = T\,\frac{R}{v}\cdot\frac{R}{P} = \frac{R^2 T}{Pv} = R
> $$

> [!proposicion]
> **Gas de van der Waals** (ver [[Problema 04]]):
> $$
> c_p - c_v = \frac{R}{\,1 - \dfrac{2a\,(\bar v - b)^2}{R T\,\bar v^{\,3}}\,}
> $$
> que tiende a $R$ cuando $a, b \to 0$.

> [!proposicion]
> **Sustancia incompresible** ($v$ constante, $\left(\partial v/\partial T\right)_P = 0$):
> $$
> c_p = c_v = c
> $$
> un único calor específico, como se usa para líquidos y sólidos.

## Forma con coeficientes medibles

> [!info]
> En términos del coeficiente de dilatación $\beta = \frac{1}{v}\left(\partial v/\partial T\right)_P$ y la compresibilidad isoterma $\kappa_T = -\frac{1}{v}\left(\partial v/\partial P\right)_T$:
> $$
> c_p - c_v = \frac{v T \beta^2}{\kappa_T}
> $$
> Forma directamente evaluable con propiedades tabuladas, sin derivar la ecuación de estado.

## Relación con otras notas

> [!info]
> - Se deduce de las ecuaciones [[TdS]] y las relaciones de [[Maxwell]].
> - Conecta los calores específicos de [[Energia Interna]] y [[Entalpia]].
> - Su límite ideal es la relación de Mayer del [[Gas Ideal]]; el cociente $\gamma = c_p/c_v$ gobierna los procesos isentrópicos.

> [!info]
> **Convención de notación**:
> - $c_p$, $c_v$: calores específicos [kJ/kg·K]; $\gamma = c_p/c_v$.
> - $\beta$: dilatación isobárica; $\kappa_T$: compresibilidad isoterma.
