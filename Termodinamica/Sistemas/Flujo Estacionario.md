---
title: "Flujo estacionario"
tags:
  - termodinamica
  - sistemas
  - flujo_estacionario
draft: false
aliases:
  - steady flow
  - SFEE
  - flujo permanente
  - régimen estacionario
---

# Flujo estacionario

> [!definicion]
> Régimen de un [[Volumenes de Control | volumen de control]] en el que **ninguna propiedad cambia con el tiempo**: ni dentro del VC ni en las corrientes. Es la hipótesis de operación normal de la mayoría de los equipos.
> $$
> \frac{dm_{vc}}{dt} = 0, \qquad \frac{dE_{vc}}{dt} = 0, \qquad \frac{dS_{vc}}{dt} = 0
> $$

## Balances reducidos

> [!teorema]
> Con las derivadas temporales nulas, los balances del [[Volumenes de Control | volumen de control]] se reducen a relaciones algebraicas. Para una entrada y una salida:
> $$
> \dot m_1 = \dot m_2 = \dot m \qquad \text{(ver [[Balance de Masa VC]])}
> $$
> $$
> \dot Q - \dot W = \dot m\left[(h_2 - h_1) + \frac{C_2^2 - C_1^2}{2} + g(z_2 - z_1)\right] \qquad \text{(ver [[Balance de Energia VC]])}
> $$
> $$
> \dot S_{gen} = \dot m\,(s_2 - s_1) - \sum_k \frac{\dot Q_k}{T_k} \ge 0 \qquad \text{(ver [[Balance de Entropia VC]])}
> $$
> La segunda es la **ecuación de la energía para flujo estacionario** (SFEE).

## Hipótesis habituales

> [!regla]
> En la mayoría de los dispositivos se desprecian los términos cinético y potencial frente al de entalpía, salvo donde son el efecto buscado:
>
> | Término | Se desprecia salvo en |
> |:---|:---|
> | $\Delta\text{EC} = \tfrac{1}{2}(C_2^2 - C_1^2)$ | [[Toberas]], [[Difusores]] |
> | $\Delta\text{EP} = g(z_2 - z_1)$ | columnas de líquido, gran desnivel |
>
> Adiabático ($\dot Q = 0$) en turbinas, compresores y válvulas bien aisladas; sin trabajo ($\dot W = 0$) en toberas, difusores, válvulas e intercambiadores.

## Aplicación por dispositivo

> [!info]
> | Dispositivo | Balance reducido |
> |:---|:---|
> | [[Turbinas]] / [[Compresores]] | $\dot W = \dot m\,(h_1 - h_2)$ |
> | [[Toberas]] / [[Difusores]] | $h_1 + \tfrac{1}{2}C_1^2 = h_2 + \tfrac{1}{2}C_2^2$ |
> | [[Valvulas]] | $h_2 = h_1$ (isentálpico) |
> | [[Intercambiadores]] | $\sum \dot m_i h_i = \sum \dot m_e h_e$ |

> [!ejemplo]
> La [[Turbinas | turbina]] adiabática del [[Problema 01]] y la [[Valvulas | válvula]] del [[Problema 03]] son aplicaciones directas de la SFEE con $\dot Q = 0$ y $\Delta\text{EC} = \Delta\text{EP} \approx 0$.

## Relación con otras notas

> [!info]
> - Caso particular del [[Volumenes de Control | volumen de control]] general.
> - Balances: [[Balance de Masa VC]], [[Balance de Energia VC]], [[Balance de Entropia VC]], [[Balance de Exergia VC]].
> - Equipos: [[Dispositivos de Flujo | dispositivos de flujo]].

> [!info]
> **Convención de notación**:
> - $\dot m$: flujo másico [kg/s]; $C$: velocidad [m/s]; $z$: altura [m].
> - SFEE: *steady-flow energy equation*; subíndices $1$ entrada, $2$ salida.
