---
title: Partícula
order: 1
tags:
  - dinamica
  - teoria
  - particula
  - index
draft: false
aliases:
  - dinámica de la partícula
  - mecánica de la partícula
---

# Partícula

> [!definicion]
> La **partícula** (o punto material) es el modelo más simple de la mecánica: un cuerpo cuya **extensión y orientación se desprecian**, de modo que su estado queda descrito solo por la **posición** $\vec{r}(t)$ de un punto. Toda su dinámica se reduce a dos preguntas: **cómo se mueve** (cinemática) y **por qué** (cinética), $\sum\vec{F}=m\vec{a}$.

> [!info]
> Primer bloque del curso de [[Dinamica/index | Dinámica]]. Es la base de todo lo demás: el [[4 Cuerpo Rigido/index| cuerpo rígido]] se trata como un **sistema de partículas** rígidamente unidas, y sus teoremas (momento, energía) se **deducen** de los de la partícula. Modelo: Taylor / Marion-Thornton.

---

## El programa de la mecánica de la partícula

![[particula_trayectoria.svg|470]]

*La cinemática describe el movimiento ($\vec r,\vec v,\vec a$); la cinética lo explica con $\sum\vec F=m\vec a$.*

> [!teoria] Cuatro preguntas, cuatro herramientas
> Toda la dinámica de la partícula se organiza en cuatro piezas, cada una deducida de la anterior:
>
> 1. **Cinemática** — describir el movimiento sin sus causas: $\vec{r}$, $\vec{v}=\dot{\vec{r}}$, $\vec{a}=\dot{\vec{v}}$, en los sistemas de coordenadas que convengan (cartesianas, intrínsecas 3D de Frenet, cilíndricas, esféricas). → [[Cinematica/index | cinemática de la partícula]].
> 2. **Cinética** — la causa del movimiento: las leyes de Newton, $\sum\vec{F}=m\vec{a}$, proyectadas según la geometría del problema. → [[Cinetica de la Particula]].
> 3. **Trabajo y energía** — primera integral de Newton **en el espacio**: integrando $\sum\vec{F}=m\vec{a}$ a lo largo de la trayectoria nace el teorema trabajo-energía. → [[Trabajo y Energia]].
> 4. **Impulso y momento** — primera integral de Newton **en el tiempo**: integrando en $dt$ nacen los teoremas de impulso-cantidad de movimiento y del momento angular. → [[Impulso y Momento]].
>
> Y al juntar muchas partículas, las fuerzas internas se cancelan y reaparecen las mismas leyes para el conjunto, gobernadas por el **centro de masa**. → [[Sistemas de Particulas]].

> [!teoria] Energía y momento son Newton integrado
> No son principios nuevos: son $\sum\vec{F}=m\vec{a}$ integrada. En el espacio, $\int\sum\vec{F}\cdot d\vec{r}=\Delta\left(\tfrac12 m v^2\right)$ (energía); en el tiempo, $\int\sum\vec{F}\,dt=\Delta(m\vec{v})$ (momento). Por eso conviene **deducirlos**, no memorizarlos: cada uno es útil cuando se conoce, respectivamente, la fuerza **en función de la posición** o **del tiempo**.

## Mapa del capítulo

> [!info] Las notas de este capítulo
> | Nota | Contenido |
> |:---|:---|
> | [[Cinematica/index | cinemática de la partícula]] | $\vec{r},\vec{v},\vec{a}$ en cartesianas, intrínsecas 3D (Frenet), cilíndricas y esféricas |
> | [[Cinetica de la Particula]] | leyes de Newton; ecuaciones de movimiento proyectadas |
> | [[Trabajo y Energia]] | teorema trabajo-energía; fuerzas conservativas; conservación |
> | [[Impulso y Momento]] | impulso-cantidad de movimiento; momento angular; choques |
> | [[Sistemas de Particulas]] | centro de masa; teoremas del sistema; König |

> [!corolario]
> La partícula fija el método de todo el curso: **describir** (cinemática), **plantear** Newton, e **integrar** —en el espacio o en el tiempo— para obtener energía y momento. El cuerpo rígido no añadirá principios: solo sumará sobre las partículas que lo forman.

> [!referencia]
> Taylor, *Classical Mechanics*, caps. 1-4; Marion-Thornton, cap. 2. Continúa en [[2 Movimiento Relativo/index| Movimiento relativo]] y [[4 Cuerpo Rigido/index| Cuerpo rígido]].
