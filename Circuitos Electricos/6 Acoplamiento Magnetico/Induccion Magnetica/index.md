---
title: Inducción Magnética
tags:
  - circuitos-electricos
  - teoria
  - acoplamiento-magnetico
  - index
draft: false
aliases:
  - inducción magnética
  - autoinducción e inducción mutua
---

# Inducción Magnética

> [!definicion]
> La **inducción magnética** entre bobinas tiene dos caras: la **autoinducción** $L$ —el flujo que la
> corriente de una bobina crea sobre **sí misma**— y la **inducción mutua** $M$ —el flujo que esa
> corriente crea sobre **otra** bobina cercana—. Cuánto se comparte lo mide el **coeficiente de
> acoplamiento** $k$, y el **signo** del efecto mutuo lo fija la **regla de los puntos**.

> [!info]
> Primera sección del [[6 Acoplamiento Magnetico/index| capítulo 6]]. Generaliza el [[Inductor]] del
> capítulo 3 a pares de bobinas; es la física que después usa el [[Transformador Ideal| transformador]].
> Fraile Mora, cap. 1, §1.19.

---

## Las cuatro piezas del acoplamiento

> [!teoria] De la bobina sola al par acoplado
> Todo parte de la ley de Faraday: una corriente variable crea un flujo variable que **induce**
> tensión. Según a quién enlace ese flujo, surgen los conceptos de la sección:
>
> - **Autoinducción** $L$: el flujo propio enlaza a la propia bobina, $v=L\,di/dt$ (el
>   [[Inductor| inductor]] de siempre). → [[Autoinduccion]].
> - **Inducción mutua** $M$: parte de ese flujo enlaza a una **segunda** bobina, induciendo en ella
>   $v_2=M\,di_1/dt$. Las dos quedan ligadas por ecuaciones acopladas. → [[Inductancia Mutua]].
> - **Regla de los puntos:** el **signo** del término mutuo ($\pm M$) depende de la orientación
>   relativa de los devanados, que se marca con un **punto** en cada bobina. → [[Regla de los Puntos]].
> - **Coeficiente de acoplamiento** $k=M/\sqrt{L_1L_2}\in[0,1]$: qué fracción del flujo se comparte.
>   → [[Coeficiente de Acoplamiento]].
>
> Cuando hay **más de dos** bobinas, todo se ordena en una **matriz de inductancias**. →
> [[Acoplamiento Multiple]].

> [!info] Las notas de esta sección
> | Nota | Contenido |
> |:---|:---|
> | [[Autoinduccion]] | $L$; el flujo propio; $v=L\,di/dt$ |
> | [[Inductancia Mutua]] | $M$; ecuaciones acopladas $v_1,v_2$ |
> | [[Regla de los Puntos]] | el signo $\pm M$ según los puntos |
> | [[Coeficiente de Acoplamiento]] | $k=M/\sqrt{L_1L_2}$, $0\le k\le1$ |
> | [[Acoplamiento Multiple]] | varias bobinas; matriz de inductancias |

> [!corolario]
> Con la autoinducción, la mutua, su signo (puntos) y su intensidad ($k$), queda descrito por completo
> cualquier conjunto de bobinas acopladas, lista para alimentar el análisis del transformador.

> [!referencia]
> Fraile Mora, cap. 1, §1.19. Siguiente: [[Acoplamiento Magnetico Fasorial]] (en régimen sinusoidal) y
> [[Transformador con Nucleo de Aire]].
