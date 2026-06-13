---
title: Acoplamiento Magnético
tags:
  - circuitos-electricos
  - teoria
  - acoplamiento-magnetico
  - index
draft: false
aliases:
  - acoplamiento magnético
  - circuitos acoplados magnéticamente
  - inductancia mutua y transformador
---

# Acoplamiento Magnético

> [!definicion]
> Dos bobinas cercanas están **acopladas magnéticamente** cuando el flujo creado por una **enlaza** a
> la otra: un cambio de corriente en la primera **induce** tensión en la segunda. Ese efecto se
> describe con la **inductancia mutua** $M$, que se suma a las **autoinductancias** $L$. Es el
> principio del **transformador**, la máquina que vertebra todo el sistema eléctrico.

> [!info]
> Sexto bloque del curso (sílabo ML 140, semana 12; Fraile Mora, cap. 1, §1.19). Extiende el
> [[Inductor]] del capítulo 3 a **pares** de bobinas, y se analiza en régimen sinusoidal con las
> [[Impedancia y Admitancia/index| impedancias]] del capítulo 5. Es la base de las máquinas
> eléctricas.

---

## Del flujo propio al flujo compartido

> [!teoria] Autoinducción, inducción mutua y la regla de los puntos
> El [[Inductor| inductor]] ya tenía **autoinducción** $L$: su propia corriente crea un flujo que lo
> enlaza a sí mismo, $v=L\,di/dt$. Cuando una segunda bobina recoge parte de ese flujo, aparece la
> **inducción mutua**: la corriente de una induce tensión en la otra, $v_2=M\,di_1/dt$. Las dos
> bobinas quedan descritas por **ecuaciones acopladas**, y el **signo** del término mutuo lo fija la
> **regla de los puntos** (la orientación relativa de los devanados).
> → [[Induccion Magnetica/index| Inducción magnética]].

> [!teoria] Cuánto se acoplan, y el transformador
> El **coeficiente de acoplamiento** $k=\dfrac{M}{\sqrt{L_1 L_2}}$ (entre $0$ y $1$) mide qué fracción
> del flujo se comparte: $k\to0$ bobinas casi independientes, $k\to1$ acoplo perfecto. Sobre esta
> física se construye el **transformador**: con núcleo de aire ([[Transformador con Nucleo de Aire]]) o
> en el límite ideal ([[Transformador Ideal]]), que **transforma** tensiones y corrientes y **refleja**
> impedancias de un lado a otro. Un par acoplado también guarda **energía** en función de $L_1$, $L_2$
> y $M$ ([[Energia en Bobinas Acopladas]]).

## Mapa del capítulo

> [!info] Las secciones y notas
> | Nota | Contenido |
> |:---|:---|
> | [[Induccion Magnetica/index\| Inducción magnética]] | autoinducción, mutua, $k$, regla de los puntos |
> | [[Acoplamiento Magnetico Fasorial]] | bobinas acopladas en régimen sinusoidal ($j\omega M$) |
> | [[Transformador con Nucleo de Aire]] | el transformador real acoplado |
> | [[Circuito Equivalente con Acoplo Conductivo]] | el equivalente en T (sin acoplo) |
> | [[Transformador Ideal]] | relación de transformación; reflejo de impedancias |
> | [[Energia en Bobinas Acopladas]] | $W=\tfrac12 L_1 i_1^2+\tfrac12 L_2 i_2^2\pm M i_1 i_2$ |

> [!corolario]
> El acoplamiento magnético añade un canal nuevo —el flujo compartido— por el que los circuitos
> interactúan sin tocarse. Dominar $M$, la regla de los puntos y el transformador es entender cómo se
> transmite y transforma la energía eléctrica.

> [!referencia]
> Fraile Mora, cap. 1, §1.19. Viene de [[5 Circuitos AC Sinusoidal y Fasores/index| Circuitos AC sinusoidal y fasores]]; continúa en [[7 Circuitos Trifasicos/index| Circuitos trifásicos]].
