---
title: Reducción de Circuitos
order: 4
tags:
  - circuitos-electricos
  - teoria
  - resistivos
  - index
draft: false
aliases:
  - reducción de circuitos
  - simplificación de circuitos
---

# Reducción de Circuitos

> [!definicion]
> **Reducir** un circuito es sustituir un grupo de elementos por otro **equivalente** más simple que se comporta igual visto desde sus terminales. Asociar resistencias en **serie** y **paralelo**, repartir con **divisores** de tensión y de corriente, **transformar** una fuente de tensión en una de corriente, y convertir **estrella en triángulo**: todas son herramientas para llegar a la respuesta con el mínimo de ecuaciones.

> [!info]
> Cuarta y última sección del [[1 Conceptos Fundamentales y Resistivos/index| capítulo 1]]. Se apoya en la ley de Ohm ([[Elementos del Circuito/index| Elementos]]) y en [[Leyes de Kirchhoff/index| Kirchhoff]]. Es la antesala de los [[Teorema de Thevenin| equivalentes de Thévenin y Norton]] del capítulo 2, que llevan esta idea de "equivalencia vista desde dos terminales" hasta el final.

---

## Equivalencia vista desde los terminales

> [!teoria] Misma respuesta, menos elementos
> Dos circuitos son **equivalentes** entre dos terminales si imponen la misma relación $v$–$i$ ahí. Esa idea genera todas las técnicas de la sección:
>
> - **Serie y paralelo.** Resistencias en serie suman ($R_{eq}=\sum R_k$); en paralelo suman sus conductancias ($1/R_{eq}=\sum 1/R_k$). → [[Resistencias en Serie y Paralelo]].
> - **Divisores.** Una vez en serie/paralelo, la tensión se reparte proporcional a la resistencia ([[Divisor de Voltaje]]) y la corriente proporcional a la conductancia ([[Divisor de Corriente]]).
> - **Transformación de fuentes.** Una fuente de tensión real en serie con $R$ equivale a una de corriente en paralelo con la misma $R$ ($I=V/R$). → [[Transformacion de Fuentes]].
> - **Estrella-triángulo.** Tres resistencias en Y equivalen a tres en Δ por las fórmulas de **Kennelly**, indispensable cuando no hay ninguna serie ni paralelo a la vista. → [[Estrella Triangulo Kennelly]].
> - **Simetría.** Reconocer simetrías evita cálculo: nodos al mismo potencial pueden unirse o separarse. → [[Simetria en Circuitos]].

> [!info] Las notas de esta sección
> | Nota | Contenido |
> |:---|:---|
> | [[Resistencias en Serie y Paralelo]] | $R_{eq}$ en serie y en paralelo |
> | [[Divisor de Voltaje]] | reparto de tensión entre resistencias en serie |
> | [[Divisor de Corriente]] | reparto de corriente entre resistencias en paralelo |
> | [[Transformacion de Fuentes]] | fuente de tensión real ↔ fuente de corriente real |
> | [[Estrella Triangulo Kennelly]] | equivalencia Y↔Δ (teorema de Kennelly) |
> | [[RINCE]] | ramas independientes para el cálculo del equivalente |
> | [[Simetria en Circuitos]] | explotar simetrías para simplificar |

> [!warning]
> Serie/paralelo y divisores solo aplican a configuraciones **reconocibles** como tales. Cuando un puente (red en Δ/Y) no presenta ninguna, hay que recurrir a **Kennelly** o directamente a los métodos de [[2 Metodos de Analisis y Teoremas/index| mallas/nodos]].

> [!referencia]
> Fraile Mora, cap. 1, §1.10, §1.11. Continúa en [[2 Metodos de Analisis y Teoremas/index| Métodos de análisis y teoremas]].
