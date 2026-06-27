---
title: "Sistemas Termodinámicos"
order: 1
tags:
  - termodinamica
  - sistemas
  - index
draft: false
---

# Sistemas Termodinámicos

> [!definicion]
> Un **sistema termodinámico** es cualquier región del espacio o porción de materia que se elige como objeto de análisis. Todo lo que queda fuera es el **entorno** (ambiente, surroundings). La **frontera** separa sistema y entorno; puede ser real o imaginaria, rígida o deformable, permeable o impermeable a la masa.
>
> La elección del sistema no es única — el mismo problema puede resolverse con distintos sistemas — pero una buena elección simplifica el álgebra enormemente. El primer paso de cualquier análisis termodinámico es **dibujar y definir el sistema** con claridad.

---

## Tipología: las tres elecciones posibles

> [!teoria]
> | Tipo | ¿Pasa masa? | ¿Pasa energía? | Ecuación característica | Cuándo usarlo |
> |:---|:---:|:---:|:---|:---|
> | **Sistema cerrado (SC)** | No | Sí ($Q$, $W$) | $\Delta U = Q - W$ | Pistón-cilindro, recipiente sellado, proceso por lotes |
> | **Volumen de control (VC)** | Sí | Sí ($Q$, $W$, $\dot{m}\,h$) | Balance de energía con $h$ en flujos | Turbinas, compresores, toberas, calderas |
> | **Sistema aislado** | No | No | $\Delta U = 0$, $\Delta S = S_{\rm gen} \ge 0$ | Referencia teórica, máquinas perfectamente aisladas |
>
> La diferencia operativa más importante entre SC y VC es que los flujos de masa en el VC transportan entalpía $h = u + Pv$, no solo energía interna $u$. El término $Pv$ es el trabajo de flujo: la corriente de entrada "empuja" contra la presión.

---

## Régimen estacionario vs. no estacionario

> [!teoria]
> **Régimen estacionario** (steady-state): las propiedades en cada punto del VC no cambian con el tiempo ($dm_{VC}/dt = 0$, $dE_{VC}/dt = 0$). Es la hipótesis de operación nominal de la mayoría de los equipos industriales. Los balances se reducen a relaciones algebraicas entre los estados de entrada y salida.
>
> **Régimen transitorio**: el VC acumula o pierde masa y/o energía. Ejemplos: llenado de un tanque, arranque de una turbina, vaciado de un recipiente presurizado.

---

## Cómo elegir el sistema en un problema

> [!teoria]
> El criterio práctico:
> 1. Si el problema involucra **una masa fija** que se comprime, expande, calienta o enfría — sistema cerrado.
> 2. Si el fluido **fluye** a través de un equipo (turbina, bomba, compresor, intercambiador) y el equipo opera en régimen permanente — VC estacionario.
> 3. Si se mezclan o separan corrientes, o hay acumulación transitoria — VC general o sistema abierto transitorio.
>
> El error más común es aplicar $Q_P = \Delta H$ (SC isobárico) a una turbina o bomba: esas ecuaciones son para sistema cerrado; el VC adiabático usa $w = h_1 - h_2$.

---

## Mapa de notas

> [!info]
> **Sistemas:**
> - [[Sistemas Cerrados]] (order 1) — masa fija; $\Delta U = Q - W$; tipos de frontera.
> - [[Volumenes de Control]] (order 2) — flujo de masa; por qué $h$ en vez de $u$.
> - [[Flujo Estacionario]] (order 3) — hipótesis SFSS; balances reducidos; tabla de dispositivos.
>
> **Dispositivos de flujo:**
> - [[Dispositivos Flujo/index | Dispositivos de Flujo]] — mapa y criterio de selección de ecuaciones.
> - [[Dispositivos Flujo/Turbinas | Turbinas]], [[Dispositivos Flujo/Compresores | Compresores]], [[Dispositivos Flujo/Toberas | Toberas]], [[Dispositivos Flujo/Difusores | Difusores]], [[Dispositivos Flujo/Valvulas | Válvulas]], [[Dispositivos Flujo/Intercambiadores | Intercambiadores]], [[Dispositivos Flujo/Flash | Flash]].

> [!referencia]
> Borgnakke & Sonntag, *Fundamentals of Thermodynamics*, §2.1 y caps. 4–6; Çengel & Boles, *Termodinámica*, caps. 1, 4–5; Moran & Shapiro, §1.2–1.4.
