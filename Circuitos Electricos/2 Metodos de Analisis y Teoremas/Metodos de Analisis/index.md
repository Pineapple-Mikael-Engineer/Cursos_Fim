---
title: Métodos de Análisis
tags:
  - circuitos-electricos
  - teoria
  - metodos-analisis
  - index
draft: false
aliases:
  - métodos de análisis
  - análisis de mallas y nodos
---

# Métodos de Análisis

> [!definicion]
> Los **métodos de análisis** resuelven cualquier circuito lineal de forma **sistemática** y con el
> **mínimo número de ecuaciones**, eligiendo bien las incógnitas. El **análisis de mallas** toma como
> incógnitas las **corrientes de malla** y aplica la LKV ($b-n+1$ ecuaciones); el **análisis de
> nodos** toma las **tensiones de nodo** y aplica la LKC ($n-1$ ecuaciones). No son leyes nuevas: son
> Kirchhoff aplicado con un criterio que **garantiza** ecuaciones independientes.

> [!info]
> Segunda sección del [[2 Metodos de Analisis y Teoremas/index| capítulo 2]]. Se apoya en la
> [[Topologia de Redes/index| topología]] (que dice cuántas ecuaciones hay) y en las
> [[Leyes de Kirchhoff/index| leyes de Kirchhoff]]. Es la maquinaria que luego se reutiliza tal cual
> en [[5 Circuitos AC Sinusoidal y Fasores/index| régimen sinusoidal]] cambiando $R$ por $Z$.

---

## La idea: elegir la incógnita correcta

> [!teoria] Por qué basta con corrientes de malla o tensiones de nodo
> El truco de ambos métodos es elegir una incógnita que haga que **una de las dos leyes de Kirchhoff
> se cumpla sola**, dejando solo la otra por imponer:
>
> - **Corrientes de malla** (análisis de mallas). Se imagina una corriente circulando por cada
>   ventana de la red. Como cada corriente de malla **entra y sale** de todos los nodos que recorre,
>   la **LKC se satisface automáticamente**; solo queda imponer la **LKV** en cada malla. Resultado:
>   $b-n+1$ ecuaciones. → [[Analisis de Mallas]].
>
> - **Tensiones de nodo** (análisis de nodos). Se elige un nodo de **referencia** (masa) y se toma la
>   tensión de cada otro nodo respecto a él. Como toda tensión de rama es una **diferencia** de esas
>   tensiones de nodo, la **LKV se satisface automáticamente** alrededor de cualquier lazo; solo queda
>   imponer la **LKC** en cada nodo. Resultado: $n-1$ ecuaciones. → [[Analisis de Nodos]].
>
> En ambos casos se pasa de las $2b$ incógnitas "a lo bruto" al mínimo que fija la
> [[Ramas y Mallas Independientes| topología]].

> [!teoria] Dos caras de la misma moneda (dualidad)
> Mallas y nodos son **duales**: cada concepto de uno tiene su gemelo en el otro.
>
> | Análisis de **mallas** | Análisis de **nodos** |
> |:---|:---|
> | incógnita: corriente de malla | incógnita: tensión de nodo |
> | ley impuesta: LKV | ley impuesta: LKC |
> | ley automática: LKC | ley automática: LKV |
> | número de ecuaciones: $b-n+1$ | número de ecuaciones: $n-1$ |
> | matriz de **resistencias** $R$ | matriz de **conductancias** $G$ |
>
> Por eso, **se elige el método con menos ecuaciones**: nodos si $n-1<b-n+1$, mallas en caso
> contrario. Y por eso lo que se aprende de un método se traduce de inmediato al otro.

## Cuando aparece una fuente "incómoda"

> [!teoria] Supermallas, supernodos y fuentes dependientes
> El procedimiento básico se complica con ciertas fuentes, y cada caso tiene su técnica:
> - Una **fuente de corriente compartida** entre dos mallas impide escribir la LKV de cada una por
>   separado: se combinan en una **supermalla**. → [[Mallas con Fuentes de Corriente]].
> - Una **fuente de tensión entre dos nodos** impide escribir la LKC de cada uno por separado: se
>   combinan en un **supernodo**. → [[Nodos con Fuentes de Voltaje]].
> - Una **fuente dependiente** (controlada por otra variable del circuito) añade una **ecuación de
>   restricción** que liga su valor con la variable de control. → [[Ecuaciones de Restriccion]].

## Mapa de la sección

> [!info] Qué desarrolla cada hija
> | Nota | Contenido |
> |:---|:---|
> | [[Analisis de Mallas]] | método de mallas: corrientes de malla, LKV, matriz $R$; ejemplo resuelto |
> | [[Mallas con Fuentes de Corriente]] | **supermalla**: fuente de corriente compartida |
> | [[Analisis de Nodos]] | método de nodos: tensiones de nodo, LKC, matriz $G$; ejemplo resuelto |
> | [[Nodos con Fuentes de Voltaje]] | **supernodo**: fuente de tensión entre dos nodos |
> | [[Ecuaciones de Restriccion]] | fuentes **dependientes**: la ecuación de control |

> [!corolario]
> Mallas y nodos son el mismo principio visto desde dos lados: imponer una ley de Kirchhoff tras haber
> hecho la otra automática. Elegir el método más corto, y conocer las técnicas de supermalla,
> supernodo y restricción, basta para resolver cualquier circuito lineal con fuentes de cualquier
> tipo.

> [!referencia]
> Fraile Mora, cap. 1, §1.12-1.13. Anterior: [[Topologia de Redes/index| Topología de redes]].
> Siguiente: [[Teoremas/index| Teoremas]].
