---
title: "Ecuaciones $TdS$"
tags:
  - termodinamica
  - relaciones_termodinamicas
  - entropia
  - tds
draft: false
aliases:
  - TdS equations
  - ecuaciones Tds
  - Relaciones TdS
  - Gibbs equations
---

# Ecuaciones $TdS$

> [!definicion]
> Expresan el calor reversible $T\,ds$ —y por tanto el cambio de [[Entropia]]— en función de variables medibles ($T$, $P$, $v$) y los calores específicos. Permiten integrar $\Delta s$ entre dos estados a partir de la [[Ecuaciones de Estado/index | ecuación de estado]], sin medir la entropía directamente.

## Las dos ecuaciones

> [!teorema]
> Para una sustancia simple compresible (forma específica):
> $$
> T\,ds = c_v\,dT + T\left(\frac{\partial P}{\partial T}\right)_v dv \qquad \text{(primera ecuación } TdS\text{)}
> $$
> $$
> T\,ds = c_p\,dT - T\left(\frac{\partial v}{\partial T}\right)_P dP \qquad \text{(segunda ecuación } TdS\text{)}
> $$
>
> Equivalen a las formas compactas $T\,ds = du + P\,dv$ y $T\,ds = dh - v\,dP$, obtenidas de los diferenciales de la [[Energia Interna]] y la [[Entalpia]].

## Derivación

> [!demostracion]
> **Primera ecuación.** Tomando $s = s(T,v)$:
> $$
> ds = \left(\frac{\partial s}{\partial T}\right)_v dT + \left(\frac{\partial s}{\partial v}\right)_T dv
> $$
> El primer coeficiente se identifica con el calor específico a volumen constante, $\left(\partial s/\partial T\right)_v = c_v/T$; el segundo se sustituye por la relación de [[Maxwell]] desde $f$, $\left(\partial s/\partial v\right)_T = \left(\partial P/\partial T\right)_v$. Multiplicando por $T$ se obtiene la primera ecuación.
>
> **Segunda ecuación.** Tomando $s = s(T,P)$, con $\left(\partial s/\partial T\right)_P = c_p/T$ y la relación de [[Maxwell]] desde $g$, $\left(\partial s/\partial P\right)_T = -\left(\partial v/\partial T\right)_P$, se llega de forma análoga a la segunda.

## Aplicación: cambio de entropía

> [!proposicion]
> Integrando entre dos estados, el cambio de entropía específica es
> $$
> \Delta s = \int_1^2 \frac{c_v}{T}\,dT + \int_1^2 \left(\frac{\partial P}{\partial T}\right)_v dv
> = \int_1^2 \frac{c_p}{T}\,dT - \int_1^2 \left(\frac{\partial v}{\partial T}\right)_P dP
> $$
> Se elige la forma cuyo segundo término sea más simple según los datos: la primera para procesos descritos en $(T,v)$, la segunda en $(T,P)$.

> [!ejemplo]
> **Gas ideal.** Con $Pv = RT$: $\left(\partial P/\partial T\right)_v = R/v$ y $\left(\partial v/\partial T\right)_P = R/P$. Las ecuaciones $TdS$ se reducen a
> $$
> ds = c_v\frac{dT}{T} + R\frac{dv}{v}, \qquad ds = c_p\frac{dT}{T} - R\frac{dP}{P}
> $$
> que para $c_p$, $c_v$ constantes integran a las expresiones conocidas de $\Delta s$ del [[Gas Ideal]] (ver [[Entropia]]).

> [!ejemplo]
> **Sustancia incompresible** ($dv = 0$, $c_p = c_v = c$). La primera ecuación da directamente
> $$
> ds = c\,\frac{dT}{T} \;\Rightarrow\; \Delta s = c\,\ln\frac{T_2}{T_1}
> $$
> El cambio de entropía depende solo de la temperatura.

## Consecuencias

> [!proposicion]
> **Relación $c_p - c_v$.** Igualando las dos ecuaciones $TdS$ se obtiene
> $$
> c_p - c_v = T\left(\frac{\partial P}{\partial T}\right)_v \left(\frac{\partial v}{\partial T}\right)_P
> = -T\frac{\left(\partial v/\partial T\right)_P^2}{\left(\partial v/\partial P\right)_T}
> $$
> El desarrollo completo se trata en [[Cp Cv/index | $c_p - c_v$]]. El segundo miembro es siempre $\ge 0$, de modo que $c_p \ge c_v$.

> [!proposicion]
> **Procesos isentrópicos.** Imponiendo $ds = 0$ en cada ecuación se obtienen las relaciones que ligan $T$ con $v$ o con $P$ a entropía constante, base de las relaciones $Pv^\gamma = \text{cte}$ del [[Gas Ideal]] tratadas en [[Entropia]].

> [!warning]
> Válidas para sustancia simple compresible en equilibrio. Los calores específicos $c_p$, $c_v$ son en general funciones de $T$ (y, fuera del gas ideal, también de $P$ o $v$); no sacarlos de la integral salvo que se justifique constancia.

## Relación con otras notas

> [!info]
> - Se construyen sobre las relaciones de [[Maxwell]] y los diferenciales de [[Energia Interna]] y [[Entalpia]].
> - Son la herramienta de cálculo de $\Delta s$ que usa la nota de [[Entropia]].
> - Conducen a la relación [[Cp Cv/index | $c_p - c_v$]] y a la de Clapeyron.

> [!info]
> **Convención de notación**:
> - $s$: entropía específica [kJ/kg·K]; $c_p$, $c_v$: calores específicos [kJ/kg·K]
> - Derivadas $\left(\partial P/\partial T\right)_v$, $\left(\partial v/\partial T\right)_P$: evaluadas desde la ecuación de estado
