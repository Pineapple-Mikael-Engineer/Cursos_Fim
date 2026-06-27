---
title: "Conversión de Energía: Ciclos Termodinámicos"
order: 4
tags:
  - termodinamica
  - ciclos
  - conversion_energia
  - index
draft: false
aliases:
  - Ciclos Termodinámicos
  - Conversión de Energía
---

# Conversión de Energía: Ciclos Termodinámicos

> [!definicion]
> Un **ciclo termodinámico** es una secuencia de procesos que devuelve el fluido de trabajo al estado inicial, convirtiendo de forma neta calor en trabajo (ciclo de potencia) o trabajo en efecto de refrigeración/calefacción (ciclo de refrigeración/bomba de calor). Los ciclos son el fundamento de todas las máquinas de conversión de energía: plantas de vapor, turbinas de gas, motores de automóvil, refrigeradores y bombas de calor.
>
> La segunda ley impone un techo a la eficiencia: ningún ciclo operando entre $T_H$ y $T_L$ puede superar al ciclo de **Carnot**, cuya eficiencia es $\eta_{\rm Carnot} = 1 - T_L/T_H$. Los ciclos reales se comparan con este ideal.

![[ciclos_clasificacion.svg|480]]
*Clasificación de los ciclos termodinámicos. Los ciclos de potencia (Rankine, Brayton, Otto, Diesel) convierten calor en trabajo. Los ciclos invertidos (refrigeración, bomba de calor) convierten trabajo en transferencia de calor. La eficiencia de todos ellos está acotada por el límite de Carnot.*

---

## Eficiencia térmica y COP

Para los **ciclos de potencia** (generan trabajo):
$$
\eta_{\rm th} = \frac{w_{\rm neto}}{q_{\rm entrada}} = 1 - \frac{q_{\rm salida}}{q_{\rm entrada}} \leq 1 - \frac{T_L}{T_H} = \eta_{\rm Carnot}.
$$

Para los **ciclos de refrigeración** (transfieren calor del frío al caliente gastando trabajo):
$$
\text{COP}_R = \frac{q_L}{w_{\rm neto}} = \frac{q_L}{q_H - q_L} \leq \frac{T_L}{T_H - T_L}.
$$

Para las **bombas de calor** (entregan calor al espacio caliente):
$$
\text{COP}_{HP} = \frac{q_H}{w_{\rm neto}} = \text{COP}_R + 1 \leq \frac{T_H}{T_H - T_L}.
$$

---

## Mapa de ciclos

| Ciclo | Fluido | Procesos clave | Aplicación |
|:---|:---:|:---|:---|
| [[Rankine/index \| Rankine]] | Vapor de agua | Vapor → turbina → condensador → bomba → caldera | Plantas eléctricas |
| [[Brayton/index \| Brayton]] | Gas (aire) | Compresor → cámara → turbina → descarga | Turbinas de gas, aviación |
| [[../Ciclos de Combustión Interna/index \| Otto]] | Aire (SI) | Compresión → combustión isocórica → expansión | Motor gasolina |
| [[../Ciclos de Combustión Interna/index \| Diesel]] | Aire (CI) | Compresión → combustión isobárica → expansión | Motor diésel |
| [[../Refrigeración/index \| Compresión de Vapor]] | Refrigerante | Evaporador → compresor → condensador → válvula | AC, refrigerador |
| [[../Refrigeración/Bomba de Calor \| Bomba de Calor]] | Refrigerante | Igual al anterior, pero el efecto útil es $q_H$ | Calefacción eficiente |

---

## Notas de esta sección

> [!info] Mapa
> **Ciclos de Potencia:**
> - [[Ciclos de Potencia/index | Ciclos de Potencia]] — fundamentos comunes: diagrama $T$-$s$, eficiencia, ciclo de Carnot como referencia.
> - [[Ciclos de Potencia/Rankine/index | Rankine]] — ciclo de vapor estándar.
>   - [[Ciclos de Potencia/Rankine/Rankine Simple | Rankine Simple]] — ciclo básico de 4 procesos.
>   - [[Ciclos de Potencia/Rankine/Rankine con Recalentamiento | Rankine con Recalentamiento]] — evita vapor húmedo a baja presión.
>   - [[Ciclos de Potencia/Rankine/Rankine Regenerativo | Rankine Regenerativo]] — sangrado para mejorar eficiencia.
> - [[Ciclos de Potencia/Brayton/index | Brayton]] — ciclo de turbina de gas.
>   - [[Ciclos de Potencia/Brayton/Brayton Simple | Brayton Simple]] — ciclo estándar de turbina de gas.
>   - [[Ciclos de Potencia/Brayton/Brayton con Regeneración | Brayton con Regeneración]] — recuperador de calor.
>
> **Ciclos de Combustión Interna:**
> - [[Ciclos de Combustión Interna/index | Ciclos de Combustión Interna]] — modelo aire-estándar.
> - [[Ciclos de Combustión Interna/Ciclo Otto | Ciclo Otto]] — motor de encendido provocado (gasolina).
> - [[Ciclos de Combustión Interna/Ciclo Diesel | Ciclo Diesel]] — motor de encendido por compresión (diésel).
>
> **Refrigeración y Bombas de Calor:**
> - [[Refrigeración/index | Refrigeración]] — fundamentos: COP, ciclo de Carnot inverso.
> - [[Refrigeración/Compresión de Vapor | Compresión de Vapor]] — ciclo estándar de refrigeración.
> - [[Refrigeración/Bomba de Calor | Bomba de Calor]] — ciclo invertido para calefacción.

> [!referencia]
> Borgnakke & Sonntag, *Fundamentals of Thermodynamics*, caps. 11–14; Çengel & Boles, *Termodinámica*, caps. 9–11; Moran & Shapiro, *Fundamentals of Engineering Thermodynamics*, caps. 9–10.
