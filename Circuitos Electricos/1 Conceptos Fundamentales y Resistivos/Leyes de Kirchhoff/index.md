---
title: Leyes de Kirchhoff
order: 3
tags:
  - circuitos-electricos
  - teoria
  - resistivos
  - kirchhoff
  - index
draft: false
aliases:
  - leyes de Kirchhoff
  - lemas de Kirchhoff
---

# Leyes de Kirchhoff

> [!definicion]
> Las dos **leyes de Kirchhoff** son las ecuaciones de conservación que gobiernan **toda** red eléctrica, sea resistiva o no. La **ley de corrientes (LKC)** dice que la suma de corrientes en un **nodo** es cero (se conserva la carga); la **ley de tensiones (LKV)** dice que la suma de tensiones en una **malla** es cero (se conserva la energía). Junto con la ley de Ohm, bastan para resolver cualquier circuito resistivo.

> [!info]
> Tercera sección del [[1 Conceptos Fundamentales y Resistivos/index| capítulo 1]]. Conecta los [[Elementos del Circuito/index| elementos]] en una red. Son el fundamento de los [[2 Metodos de Analisis y Teoremas/index| métodos de mallas y nodos]] del capítulo 2, que no son más que LKV y LKC aplicadas sistemáticamente.

---

## Las dos conservaciones

> [!teoria] Carga en los nodos, energía en las mallas
> Kirchhoff traduce dos principios físicos al lenguaje de los circuitos:
>
> - **Conservación de la carga → LKC.** En un **nodo** (punto de unión de ramas) no se acumula carga, así que todo lo que entra sale:
>   $$\sum_{k} i_k = 0.$$
>   → [[Ley de Corrientes LKC]].
>
> - **Conservación de la energía → LKV.** Al recorrer una **malla** (camino cerrado) y volver al punto de partida, la energía por unidad de carga vuelve a su valor: las subidas y caídas de tensión se cancelan:
>   $$\sum_{k} v_k = 0.$$
>   → [[Ley de Voltajes LKV]].
>
> Ambas son **lineales** y no dependen de qué elementos haya: valen igual con resistencias, con condensadores o en régimen sinusoidal. Lo único que cambia entre capítulos es la **relación $v$–$i$** de cada elemento (Ohm, $C\,dv/dt$, $L\,di/dt$, o $Z$ fasorial).

> [!info] Las notas de esta sección
> | Nota | Contenido |
> |:---|:---|
> | [[Ley de Corrientes LKC]] | primer lema; $\sum i=0$ en un nodo; supernodo |
> | [[Ley de Voltajes LKV]] | segundo lema; $\sum v=0$ en una malla |
> | [[Ecuaciones Independientes]] | cuántas LKC/LKV son independientes ($n-1$ nodos, $b-n+1$ mallas) |
> | [[Balance de Potencias]] | $\sum$ potencia entregada $=\sum$ disipada (teorema de Tellegen) |

> [!corolario]
> Un circuito de $b$ ramas tiene $2b$ incógnitas (una $v$ y una $i$ por rama). Las relaciones de los elementos dan $b$ ecuaciones; Kirchhoff aporta las otras $b$ (las **independientes**). El sistema queda determinado: ese es, en el fondo, **todo** el análisis de circuitos.

> [!referencia]
> Fraile Mora, cap. 1, §1.8. Siguiente sección: [[Reduccion de Circuitos/index| Reducción de circuitos]].
