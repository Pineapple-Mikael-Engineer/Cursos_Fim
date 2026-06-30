---
title: "Refrigeración y Bombas de Calor"
order: 3
tags:
  - termodinamica
  - ciclos
  - refrigeracion
  - bomba_de_calor
  - index
draft: false
aliases:
  - Refrigeración
  - ciclos de refrigeración
  - bombas de calor
---

# Refrigeración y Bombas de Calor

> [!definicion]
> Los **ciclos de refrigeración** operan en **sentido inverso** al de los ciclos de potencia: reciben trabajo neto de entrada y transfieren calor de un espacio frío ($T_L$) a un espacio caliente ($T_H$). El objetivo puede ser:
>
> - **Refrigeración:** mantener un espacio a temperatura menor que la del ambiente. El efecto útil es el calor extraído $q_L$. Coeficiente de desempeño: $\text{COP}_R = q_L/w_{\rm neto}$.
> - **Bomba de calor:** calentar un espacio con calor tomado del exterior. El efecto útil es el calor cedido $q_H$. Coeficiente de desempeño: $\text{COP}_{HP} = q_H/w_{\rm neto}$.
>
> *Relación fundamental:* como $q_H = q_L + w_{\rm neto}$ por la primera ley: $\text{COP}_{HP} = \text{COP}_R + 1$.
>
> *Límite de Carnot:* el ciclo de Carnot operado en reversa da el COP máximo posible:
> $$
> \text{COP}_{R,\rm Carnot} = \frac{T_L}{T_H - T_L}, \qquad \text{COP}_{HP,\rm Carnot} = \frac{T_H}{T_H - T_L}.
> $$

![[refrigeracion_diagrama_flujos.svg|440]]
*Balance de energía del ciclo de refrigeración/bomba de calor. La bomba/compresor aporta trabajo $w_{\rm neto}$; el ciclo extrae $q_L$ del espacio frío y cede $q_H = q_L + w_{\rm neto}$ al espacio caliente.*

---

## COP vs eficiencia

> [!teoria]
> El COP **no está limitado a 1**: a diferencia de la eficiencia térmica $\eta < 1$, el COP puede ser $\gg 1$. Un refrigerador con $\text{COP}_R = 4$ extrae 4 kJ de calor del espacio frío por cada 1 kJ de trabajo eléctrico consumido. Un refrigerador de $\text{COP}_R = 4$ no viola la primera ley porque transfiere (no crea) energía.
>
> Una **bomba de calor** con $\text{COP}_{HP} = 3$ cede 3 kJ de calor a la habitación por cada 1 kJ eléctrico. Es siempre más eficiente que una resistencia eléctrica ($\text{COP}_{resistencia} = 1$) en términos de energía entregada. La limitación práctica es el costo de instalación y la disponibilidad de la fuente fría (exterior, suelo, agua).

---

## Mapa de notas

> [!info]
> - [[Compresión de Vapor]] — ciclo de refrigeración estándar; 4 estados; $\text{COP}_R$ y $\text{COP}_{HP}$; fluidos refrigerantes; ejemplo con R-134a.
> - [[Bomba de Calor]] — mismo ciclo, énfasis en $q_H$; comparación con resistencia eléctrica; condición de ventaja sobre calefacción eléctrica.

> [!referencia]
> Borgnakke & Sonntag, §11.6–11.7; Çengel & Boles, §11-1 a 11-3; Moran & Shapiro, §10.1–10.2.
