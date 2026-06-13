---
title: "Volumen de control"
tags:
  - termodinamica
  - sistemas
  - volumen_de_control
draft: false
aliases:
  - control volume
  - sistema abierto
  - volúmenes de control
  - VC
---

# Volumen de control

> [!definicion]
> Región del espacio, de frontera fija o deformable, **a través de la cual fluye masa**. Es el modelo de los sistemas abiertos. La frontera se llama *superficie de control* y puede cruzarla materia, calor y trabajo.

## Balances generales (no estacionario)

> [!teorema]
> Para un volumen de control con varias entradas $i$ y salidas $e$:
> $$
> \frac{dm_{vc}}{dt} = \sum_i \dot m_i - \sum_e \dot m_e \qquad \text{(ver [[Balance de Masa VC]])}
> $$
> $$
> \frac{dE_{vc}}{dt} = \dot Q - \dot W + \sum_i \dot m_i\,\theta_i - \sum_e \dot m_e\,\theta_e \qquad \text{(ver [[Balance de Energia VC]])}
> $$
> $$
> \frac{dS_{vc}}{dt} = \sum_k \frac{\dot Q_k}{T_k} + \sum_i \dot m_i s_i - \sum_e \dot m_e s_e + \dot S_{gen} \qquad \text{(ver [[Balance de Entropia VC]])}
> $$
> donde $\theta = h + \tfrac{1}{2}C^2 + gz$ es la energía transportada por la corriente.

## Trabajo de flujo y entalpía

> [!proposicion]
> El término $\dot m\,h$ aparece —en lugar de $\dot m\,u$— porque al cruzar la frontera cada corriente realiza **trabajo de flujo** $P v$ para entrar o salir:
> $$
> h = u + Pv
> $$
> Por eso la [[Entalpia]] es la propiedad natural de los sistemas abiertos, mientras que en el [[Sistemas Cerrados | sistema cerrado]] lo es la [[Energia Interna]].

## Caso estacionario

> [!info]
> Cuando las propiedades del VC no cambian en el tiempo, los balances se simplifican notablemente: es el régimen de [[Flujo Estacionario]], aplicable a turbinas, compresores, toberas y válvulas (ver [[Dispositivos de Flujo | dispositivos de flujo]]).

## Cuándo usarlo

> [!info]
> Modelo adecuado para cualquier equipo con corrientes que entran y salen: [[Turbinas]], [[Compresores]], [[Toberas]], [[Valvulas]], [[Intercambiadores]], cámaras de mezcla, calderas. Para procesos de carga/descarga de tanques se usa la forma **no estacionaria** completa.

## Relación con otras notas

> [!info]
> - Balances: [[Balance de Masa VC]], [[Balance de Energia VC]], [[Balance de Entropia VC]], [[Balance de Exergia VC]].
> - Régimen más común: [[Flujo Estacionario]].
> - Contraparte de masa fija: [[Sistemas Cerrados]].

> [!info]
> **Convención de notación**:
> - $\dot m$: flujo másico [kg/s]; $C$: velocidad [m/s]; $z$: altura [m].
> - $\theta = h + \tfrac{1}{2}C^2 + gz$: energía específica transportada por la corriente.
> - subíndices $i$: entrada; $e$: salida.
