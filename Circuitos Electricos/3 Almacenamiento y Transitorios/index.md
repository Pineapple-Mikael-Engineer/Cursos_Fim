---
title: Almacenamiento de Energía y Transitorios
order: 3
tags:
  - circuitos-electricos
  - teoria
  - transitorios
  - index
draft: false
aliases:
  - almacenamiento y transitorios
  - régimen transitorio
---

# Almacenamiento de Energía y Transitorios

> [!definicion]
> Hasta aquí los elementos eran **resistivos**: relaciones $v$-$i$ algebraicas, sin memoria del tiempo. Este capítulo introduce los elementos que **almacenan energía** —el **condensador** (campo eléctrico, $q=Cv$) y el **inductor** (campo magnético, $\phi=Li$)—, cuyas relaciones $v$-$i$ contienen **derivadas** ($i=C\,dv/dt$, $v=L\,di/dt$). Por eso los circuitos con ellos se rigen por **ecuaciones diferenciales** y su respuesta **evoluciona en el tiempo**: aparece el **régimen transitorio**.

> [!info]
> Tercer bloque del curso (sílabo ML 140, semanas 5-7; Fraile Mora, cap. 1 §1.5 y cap. 4). Usa todo el [[1 Conceptos Fundamentales y Resistivos/index| análisis resistivo]] y los [[2 Metodos de Analisis y Teoremas/index| métodos y teoremas]]: las leyes de Kirchhoff siguen valiendo, pero ahora con derivadas. Es el puente hacia el [[4 Ondas Periodicas Sinusoidales/index| régimen sinusoidal]].

---

## Por qué ahora importa el tiempo

> [!teoria] De lo algebraico a lo diferencial
> Una resistencia responde **al instante**: si cambia la tensión, la corriente cambia a la vez. Un condensador y un inductor, no: **acumulan** energía y se oponen a los cambios bruscos. Sus leyes llevan una derivada, así que al aplicar Kirchhoff ya no sale un sistema algebraico, sino una **ecuación diferencial**.
>
> Resolverla revela dos partes:
> - la **respuesta forzada** (o permanente), que sigue a las fuentes una vez que todo se asienta;
> - la **respuesta natural** (o transitoria), la forma en que el circuito **transita** desde su estado inicial hasta el nuevo régimen permanente, y que **se extingue** con el tiempo.
>
> El **transitorio** es justo ese tránsito: lo que ocurre tras accionar un interruptor, entre un estado estable y el siguiente.

> [!teoria] Primer orden, segundo orden y Laplace
> El número de elementos almacenadores fija el **orden** de la ecuación:
> - **Un** almacenador (un $C$ o un $L$) → ecuación de **primer orden** → respuesta **exponencial** gobernada por una **constante de tiempo** $\tau$. → [[Transitorios Primer Orden/index]].
> - **Dos** almacenadores ($L$ y $C$) → ecuación de **segundo orden** → respuesta que puede **oscilar** y amortiguarse. → [[Transitorios Segundo Orden/index]].
>
> Resolver estas ecuaciones a mano se complica; la **transformada de Laplace** las convierte en **álgebra** (impedancias en el dominio de $s$) y es la herramienta sistemática del capítulo. → [[Laplace en Circuitos/index]].

## Mapa del capítulo

> [!info] Las cuatro secciones
> | Sección | Qué aporta |
> |:---|:---|
> | [[Elementos de Almacenamiento/index| Elementos de almacenamiento]] | el condensador y el inductor: leyes, energía, continuidad, comportamiento en DC |
> | [[Transitorios Primer Orden/index| Transitorios de primer orden]] | RL y RC: exponenciales y constante de tiempo $\tau$ |
> | [[Transitorios Segundo Orden/index| Transitorios de segundo orden]] | RLC: amortiguamiento y oscilación |
> | [[Laplace en Circuitos/index| Laplace en circuitos]] | el dominio de $s$: ecuaciones diferenciales → álgebra |

> [!corolario]
> Almacenar energía es lo que da **memoria** al circuito y hace que el tiempo importe. Las mismas leyes de Kirchhoff, ahora con derivadas, describen cómo el circuito pasa de un estado a otro. Dominado el transitorio, el [[4 Ondas Periodicas Sinusoidales/index| régimen sinusoidal]] será el caso permanente con excitación senoidal.

> [!referencia]
> Fraile Mora, cap. 1 §1.5 y cap. 4. Viene de [[2 Metodos de Analisis y Teoremas/index| Métodos y teoremas]]; continúa en [[4 Ondas Periodicas Sinusoidales/index| Ondas periódicas sinusoidales]].
