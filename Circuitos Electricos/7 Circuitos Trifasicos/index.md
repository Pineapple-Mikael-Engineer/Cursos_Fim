---
title: Circuitos Trifásicos
tags:
  - circuitos-electricos
  - teoria
  - trifasico
  - index
draft: false
aliases:
  - circuitos trifásicos
  - sistemas trifásicos
  - sistema trifásico
---

# Circuitos Trifásicos

> [!definicion]
> Un **sistema trifásico** está formado por **tres** tensiones sinusoidales de **igual amplitud y
> frecuencia**, desfasadas **$120^\circ$** entre sí. Es la forma universal de **generar, transportar y
> distribuir** la energía eléctrica: la suma de las tres tensiones (o corrientes) equilibradas es
> **cero** en todo instante, y eso le da ventajas decisivas sobre el monofásico.

> [!info]
> Séptimo y último bloque del curso (sílabo ML 140, semanas 13-15; Fraile Mora, cap. 3). Es la
> aplicación cumbre de los [[5 Circuitos AC Sinusoidal y Fasores/index| fasores]], la
> [[Impedancia Compleja| impedancia]] y la [[Potencia en AC/index| potencia en CA]] a la red real.

---

## Tres tensiones a 120°

> [!teoria] Qué es y por qué tres
> Las tres tensiones de fase, tomando $a$ como referencia, son
> $$v_a=V_m\operatorname{sen}\omega t,\quad v_b=V_m\operatorname{sen}(\omega t-120^\circ),\quad v_c=V_m\operatorname{sen}(\omega t-240^\circ),$$
> o en fasores, $\overline{V}_a=V\angle0^\circ$, $\overline{V}_b=V\angle{-}120^\circ$,
> $\overline{V}_c=V\angle{+}120^\circ$:
>
> ![[tres_fases.svg|640]]
>
> *Tres senoides iguales separadas $120^\circ$ (izquierda) y sus tres fasores formando una estrella
> simétrica (derecha). En todo instante $v_a+v_b+v_c=0$.*
>
> ¿Por qué tres y no una? Porque el trifásico entrega **potencia constante** (no pulsante como el
> monofásico), crea el **campo giratorio** que mueve los motores, y transporta la misma potencia con
> **menos cobre**. → [[Ventajas del Trifasico]].

> [!teoria] Cómo se conecta y se analiza
> Las tres fuentes y las tres cargas se conectan en **estrella (Y)** —con un punto común, el neutro— o
> en **triángulo (Δ)**. Distinguir **tensión/corriente de fase** (en cada rama) de las de **línea**
> (entre conductores) es la clave del capítulo, y aparece la relación $\sqrt3$. Si el sistema está
> **equilibrado**, basta analizar **una fase**; si no, hay que tratarlo completo.
> → [[Conexiones Balanceadas/index| Conexiones]] y [[Sistemas Desbalanceados/index| Desbalanceados]].

## Mapa del capítulo

> [!info] Las cuatro secciones
> | Sección | Qué aporta |
> |:---|:---|
> | [[Fundamentos Trifasicos/index| Fundamentos]] | qué es, cómo se genera, secuencia de fases, ventajas |
> | [[Conexiones Balanceadas/index| Conexiones balanceadas]] | Y y Δ; relación $\sqrt3$; equivalente por fase |
> | [[Potencia Trifasica/index| Potencia trifásica]] | $P=\sqrt3\,V_LI_L\cos\varphi$; dos vatímetros |
> | [[Sistemas Desbalanceados/index| Desbalanceados]] | cargas desiguales; el neutro |

> [!corolario]
> El trifásico no es "tres monofásicos juntos": su simetría a $120^\circ$ hace que la potencia sea
> constante, el cobre menor y los motores posibles. Dominarlo —Y/Δ, $\sqrt3$, potencia— es entender la
> red eléctrica tal como existe.

> [!referencia]
> Fraile Mora, cap. 3. Viene de [[6 Acoplamiento Magnetico/index| Acoplamiento magnético]]. Cierra el
> curso de **Circuitos Eléctricos (ML 140)**.
