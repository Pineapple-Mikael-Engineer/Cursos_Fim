---
title: Regla de los Puntos
tags:
  - circuitos-electricos
  - teoria
  - acoplamiento-magnetico
draft: false
aliases:
  - regla de los puntos
  - convención de los puntos
  - dot convention
---

# Regla de los Puntos

> [!definicion]
> La **regla (o convención) de los puntos** fija el **signo** del término de inducción mutua. Un
> **punto** marca en cada bobina el terminal de **igual polaridad magnética**. La regla: si las dos
> corrientes **entran** (o las dos **salen**) por los terminales con punto, el término mutuo es
> **positivo** ($+M$); si una entra y la otra sale, es **negativo** ($-M$).

> [!info]
> Lo que completa la [[Inductancia Mutua| inductancia mutua]] en [[6 Acoplamiento Magnetico/index| Inducción magnética]] ([[6 Acoplamiento Magnetico/index| capítulo 6]]): sin los puntos, el signo de
> $M$ queda indeterminado. Imprescindible para plantear bien las mallas del [[Transformador con Nucleo de Aire| transformador]]. Fraile Mora, cap. 1, §1.19.

---

## Ejemplo

> [!ejemplo]
> **El signo según la posición de los puntos.**
>
> Las mismas dos bobinas, con los puntos colocados de dos formas. ¿Qué signo tiene el término mutuo?
>
> ![[regla_puntos.svg|600]]
>
> *Izquierda: puntos enfrentados (ambos arriba) → término $+M$. Derecha: puntos en lados opuestos →
> término $-M$. El punto marca el terminal de igual polaridad inducida.*
>
> **Caso de la izquierda — puntos del mismo lado.** Con $i_1$ entrando por el punto de $L_1$, la
> tensión inducida en $L_2$ es **positiva** en su terminal con punto:
> $$v_2=+M\frac{di_1}{dt}.$$
>
> **Caso de la derecha — puntos opuestos.** Ahora la polaridad inducida se invierte:
> $$v_2=-M\frac{di_1}{dt}.$$
>
> > [!solucion]
> > Mismas bobinas, **distinto signo** del acoplamiento según los puntos. Por eso el convenio es
> > imprescindible: cambia el resultado del circuito.

---

## En qué consiste

> [!teoria] Qué significan los puntos
> Los puntos resumen la **orientación relativa de los devanados** (cómo está enrollado cada uno
> respecto al núcleo), información que el dibujo de las bobinas no muestra. El punto señala el terminal
> que se vuelve **positivo** cuando la corriente entra por el punto de la otra bobina y crece. Así,
> sin dibujar el bobinado real, el circuito conserva toda la información magnética necesaria.

> [!algoritmo] Aplicar la regla en las ecuaciones
> **Paso 1 — Corrientes y puntos.** Marcar el sentido de cada corriente y los puntos.
> **Paso 2 — Signo del término mutuo.** Si ambas corrientes entran (o salen) por sus puntos: $+M$. Si
> una entra y otra sale: $-M$.
> **Paso 3 — Escribir las tensiones.** $v_1=L_1\,i_1'\,\pm M\,i_2'$ y $v_2=\pm M\,i_1'+L_2\,i_2'$, con
> el signo del Paso 2 (el mismo en ambas ecuaciones, por simetría).
> **Paso 4 — Plantear las mallas** con esas tensiones, como en cualquier circuito.

> [!proposicion] Regla práctica para la tensión inducida
> La tensión mutua inducida en una bobina es **positiva en su terminal con punto** cuando la corriente
> de la **otra** bobina **entra por el punto** y **aumenta**. Es la versión "operativa" de la regla,
> útil para colocar polaridades directamente en el esquema.

> [!warning]
> Los puntos son **relativos**: lo que importa es si están del mismo lado o no, no su posición
> absoluta. Cambiar el sentido de referencia de una corriente **también** cambia el signo efectivo:
> hay que ser coherente entre sentidos de corriente y puntos al escribir las ecuaciones.

## Resumen

> [!resumen]
> | Situación | Término mutuo |
> |:---|:---|
> | Ambas corrientes entran por el punto | $+M$ |
> | Ambas salen por el punto | $+M$ |
> | Una entra y otra sale | $-M$ |
> | Tensión inducida | $+$ en el terminal con punto si la otra corriente entra por su punto y crece |

> [!corolario]
> La regla de los puntos traduce la geometría del bobinado en un simple signo. Es el dato que falta
> para que las [[Inductancia Mutua| ecuaciones del par acoplado]] queden completamente determinadas.

> [!referencia]
> Fraile Mora, cap. 1, §1.19. Completa: [[Inductancia Mutua]]. Se usa en: [[Transformador con Nucleo de Aire]] y [[Acoplamiento Multiple]].
