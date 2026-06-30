---
title: Circuito Equivalente con Acoplo Conductivo
order: 9
tags:
  - circuitos-electricos
  - teoria
  - acoplamiento-magnetico
draft: false
aliases:
  - circuito equivalente en T
  - equivalente con acoplo conductivo
  - eliminar la inductancia mutua
---

# Circuito Equivalente con Acoplo Conductivo (en T)

> [!definicion]
> Dos bobinas **acopladas magnéticamente** (con $L_1$, $L_2$ y $M$, y un terminal común) pueden sustituirse por una red **en T** de **tres inductores sin acoplamiento**: en las ramas serie van $L_1-M$ y $L_2-M$, y en la rama común (paralelo) va $M$. Así desaparecen la mutua y los puntos, y el circuito se resuelve con los métodos ordinarios.

> [!info]
> Una herramienta de [[6 Acoplamiento Magnetico/index| acoplamiento magnético]] para analizar circuitos con [[Inductancia Mutua| inductancia mutua]] sin arrastrar el término $\pm M$: los convierte en redes corrientes. Fraile Mora, cap. 1, §1.19.

---

## Ejemplo

> [!ejemplo]
> **De dos bobinas acopladas a tres sin acoplar.**
>
> Dos bobinas con $L_1=4\ \text{H}$, $L_2=8\ \text{H}$ y $M=3\ \text{H}$ (puntos que dan $+M$), con un terminal común. Hallar su equivalente en T.
>
> ![[equivalente_T.svg|560]]
>
> *La red en T tiene las mismas relaciones $v$–$i$ en los terminales que el par acoplado, pero **sin acoplamiento magnético**: tres inductores ordinarios.*
>
> **Paso 1 — Ramas serie.**
> $$L_1-M=4-3=1\ \text{H},\qquad L_2-M=8-3=5\ \text{H}.$$
>
> **Paso 2 — Rama común.** $M=3\ \text{H}$.
>
> > [!solucion]
> > Equivalente en T: $1\ \text{H}$ y $5\ \text{H}$ en las ramas serie, $3\ \text{H}$ en la rama común. Visto desde los terminales, se comporta **igual** que las dos bobinas acopladas, pero ya se resuelve con serie/paralelo, mallas o nodos sin convenio de puntos.

---

## En qué consiste

> [!teoria] Por qué la T equivale al par acoplado
> Las ecuaciones del par acoplado son $v_1=L_1 i_1'+M i_2'$ y $v_2=M i_1'+L_2 i_2'$ (con terminal común). En la red en T, la corriente por la rama común es $i_1+i_2$, así que la tensión de entrada es
> $$v_1=(L_1-M)\,i_1'+M\,(i_1+i_2)'=L_1 i_1'+M i_2',$$
> idéntica a la del par; lo mismo para $v_2$. Como **ambas** redes imponen las mismas relaciones $v$–$i$ en los terminales, son **equivalentes**: una se puede usar en lugar de la otra.

> [!proposicion] La rama serie puede ser negativa
> Si $M>L_1$ (acoplo muy fuerte), la rama $L_1-M$ resulta **negativa**. No es un error: el modelo en T es un **equivalente matemático**, y un inductor negativo es realizable como parte de la red (su efecto lo absorben las otras ramas). El conjunto sigue siendo pasivo.

> [!warning]
> El signo de las ramas serie depende del **convenio de puntos**: con acoplo $+M$ van $L_1-M$ y $L_2-M$; con $-M$ (puntos opuestos) van $L_1+M$, $L_2+M$ y la rama común es $-M$. Y el equivalente exige un **terminal común** entre primario y secundario; si no lo hay, primero hay que crearlo.

## Resumen

> [!resumen]
> | Rama (acoplo $+M$) | Inductancia |
> |:---|:---|
> | Serie primario | $L_1-M$ |
> | Serie secundario | $L_2-M$ |
> | Común (paralelo) | $M$ |
> | Con acoplo $-M$ | $L_1+M$, $L_2+M$, común $-M$ |

> [!corolario]
> El equivalente en T cambia el acoplamiento **magnético** (mutua, puntos) por uno **conductivo** (tres inductores conectados). Es el truco que permite meter circuitos con $M$ en el análisis de mallas y nodos sin reglas especiales.

> [!referencia]
> Fraile Mora, cap. 1, §1.19. Origen: [[Inductancia Mutua]] y [[Regla de los Puntos]]. Aplicación: [[Transformador con Nucleo de Aire]].
