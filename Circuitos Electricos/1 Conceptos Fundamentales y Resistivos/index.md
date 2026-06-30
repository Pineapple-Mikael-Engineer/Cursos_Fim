---
title: Conceptos Fundamentales y Circuitos Resistivos
tags:
  - circuitos-electricos
  - teoria
  - resistivos
  - index
draft: false
aliases:
  - fundamentos de circuitos
  - circuitos resistivos
---

# Conceptos Fundamentales y Circuitos Resistivos

> [!definicion]
> Un **circuito eléctrico** es una interconexión de elementos que ofrece un camino cerrado a la **corriente**. Para analizarlo basta con dos variables —la **tensión** $v$ y la **corriente** $i$—, dos tipos de elementos —**activos** (entregan energía) y **pasivos** (la disipan o almacenan)— y dos leyes de conservación —las de **Kirchhoff**—. Este capítulo construye ese lenguaje y lo aplica a los **circuitos resistivos** (solo fuentes y resistencias), donde todo se resuelve con álgebra.

> [!info]
> Primer bloque del curso (sílabo ML 140, semanas 1-2; Fraile Mora, cap. 1). Es la base de **todo** lo que sigue: los [[2 Metodos de Analisis y Teoremas/index| métodos y teoremas]] (cap. 2) sistematizan lo de aquí, y los [[3 Almacenamiento y Transitorios/index| transitorios]] y el [[5 Circuitos AC Sinusoidal y Fasores/index| régimen sinusoidal]] reutilizan las mismas leyes.

---

## La idea en cuatro piezas

> [!teoria] De qué trata todo el análisis de circuitos
> Analizar un circuito es **hallar la tensión y la corriente en cada elemento**. Toda la maquinaria del curso se apoya en cuatro piezas que se introducen en este capítulo:
>
> 1. **Las variables.** La corriente $i=\dfrac{dq}{dt}$ (carga en movimiento, en A) y la tensión $v$ (energía por unidad de carga, en V). Su producto es la **potencia** $p=vi$ (W): el ritmo al que un elemento absorbe o entrega energía. Todo se mide con un **convenio de signos** coherente. → [[Fundamentos/index| Fundamentos]].
>
> 2. **Los elementos.** Pasivos —la **resistencia** $R$, que obedece la ley de Ohm $v=Ri$— y activos —las **fuentes** de tensión y de corriente, ideales o reales, independientes o dependientes—. → [[Elementos del Circuito/index| Elementos del circuito]].
>
> 3. **Las leyes.** Las dos **leyes de Kirchhoff**: la de corrientes (LKC, conservación de la carga en un nodo) y la de tensiones (LKV, conservación de la energía en una malla). Con ellas y la ley de Ohm, cualquier circuito resistivo queda determinado. → [[Leyes de Kirchhoff/index| Kirchhoff]].
>
> 4. **La reducción.** Antes de resolver, conviene **simplificar**: asociar resistencias en serie y paralelo, usar **divisores**, **transformar fuentes** y aplicar la equivalencia **estrella-triángulo**. → [[Reduccion de Circuitos/index| Reducción de circuitos]].

> [!info] Por qué empezar por lo resistivo
> En un circuito puramente resistivo no hay derivadas ni integrales: las leyes de Kirchhoff y la de Ohm dan un **sistema de ecuaciones algebraicas lineales**. Es el banco de pruebas ideal para aprender los conceptos sin la complicación del tiempo. Cuando aparezcan [[Capacitor| condensadores]] e [[Inductor| inductores]] (cap. 3) las mismas leyes seguirán valiendo, pero con ecuaciones diferenciales; y en [[5 Circuitos AC Sinusoidal y Fasores/index| régimen sinusoidal]] volverán a ser algebraicas gracias a los **fasores**.

## Mapa del capítulo

> [!info] Las cuatro secciones
> | Sección | Qué resuelve |
> |:---|:---|
> | [[Fundamentos/index| Fundamentos]] | el lenguaje: $i$, $v$, $p$, convenios, unidades, tipos de corriente |
> | [[Elementos del Circuito/index| Elementos]] | qué hay dentro: resistencia y fuentes (ideales/reales/dependientes) |
> | [[Leyes de Kirchhoff/index| Kirchhoff]] | las dos leyes de conservación que gobiernan toda red |
> | [[Reduccion de Circuitos/index| Reducción]] | simplificar la red antes de resolverla |

> [!corolario]
> Con solo $v$, $i$, la ley de Ohm y las dos leyes de Kirchhoff queda resuelto cualquier circuito resistivo. Los capítulos siguientes no cambian estas reglas: las **extienden** a elementos que almacenan energía y a excitaciones que varían en el tiempo.

> [!referencia]
> Fuente principal: **Fraile Mora**, *Circuitos Eléctricos*, cap. 1. Continúa en [[2 Metodos de Analisis y Teoremas/index| Métodos de análisis y teoremas]].
