---
title: Dinámica
tags:
  - dinamica
  - teoria
  - index
draft: false
aliases:
  - dinámica
  - mecánica clásica
  - curso de dinámica
---

# Dinámica

> [!definicion]
> La **dinámica** estudia el movimiento de los cuerpos y sus causas. Parte de un único principio —las leyes de Newton, $\sum\vec F=m\vec a$— y, **deduciendo** de él, construye toda la mecánica clásica: de la **partícula** al **cuerpo rígido**, pasando por los marcos de referencia, el tensor de inercia y las vibraciones. Este curso privilegia la **deducción desde primeros principios**: aquí se **demuestra todo**.

> [!info]
> Curso de mecánica clásica vectorial (Newton-Euler), de enfoque teórico. Modelo de profundidad: Taylor (*Classical Mechanics*), Goldstein (cap. 4-5), Marion-Thornton. Las convenciones de notación y redacción están en `_private/Reglas.md`.

---

## El recorrido

![[particula_trayectoria.svg|460]]

*Toda la dinámica: describir el movimiento (cinemática) y explicarlo con las leyes de Newton (cinética).*

> [!teoria] De la partícula al sólido
> El curso avanza generalizando un mismo método —describir (cinemática), plantear Newton, integrar—:
> 1. **Partícula.** Cinemática (cartesianas, intrínsecas 3D, cilíndricas, esféricas), cinética, trabajo-energía, impulso-momento y sistemas de partículas. → [[1 Particula/index | Partícula]].
> 2. **Movimiento relativo.** Cómo cambian $\vec r,\vec v,\vec a$ entre marcos; el **operador derivada en base móvil**, del que salen el arrastre y Coriolis. → [[2 Movimiento Relativo/index | Movimiento relativo]].
> 3. **Inercia.** El **tensor de inercia** —análogo rotacional de la masa— y las deducciones de $\vec H$, $\vec\tau$ y $T$ desde primeros principios. → [[3 Inercia/index | Inercia]].
> 4. **Cuerpo rígido.** Cinemática (plana y 3D) y cinética (Newton-Euler 2D, ecuaciones de Euler, giróscopo), aplicando la inercia. → [[4 Cuerpo Rigido/index | Cuerpo rígido]].
> 5. **Vibraciones.** Oscilaciones libres, amortiguadas y forzadas. → [[5 Vibraciones/index | Vibraciones]].

> [!teoria] Dos herramientas vertebran el curso
> - El **operador en base móvil** $\left.\tfrac{d}{dt}\right|_F=\left.\tfrac{d}{dt}\right|_M+\vec\omega\times$: de él salen Coriolis, la cinemática del sólido y el término giroscópico de Euler.
> - El **tensor de inercia** $\mathbf I=\mathrm{Tr}(\mathbf Q)\mathbb 1-\mathbf Q$: de una integral nacen el momento angular, la energía y el torque del cuerpo rígido.

## Mapa del curso

> [!info] Los cinco bloques
> | Bloque | Contenido |
> |:---|:---|
> | [[1 Particula/index | Partícula]] | cinemática, cinética, energía, momento, sistemas |
> | [[2 Movimiento Relativo/index | Movimiento relativo]] | Galileo; operador base móvil; Coriolis |
> | [[3 Inercia/index | Inercia]] | tensor de inercia; ejes principales; deducciones |
> | [[4 Cuerpo Rigido/index | Cuerpo rígido]] | cinemática y cinética; Euler; giróscopo |
> | [[5 Vibraciones/index | Vibraciones]] | libre, amortiguada, forzada |

> [!corolario]
> Toda la dinámica clásica se deduce de $\sum\vec F=m\vec a$ y su versión rotacional. Dominando dos herramientas —el operador en base móvil y el tensor de inercia— se cubre desde el tiro parabólico hasta el giróscopo.

> [!referencia]
> Taylor, *Classical Mechanics*; Goldstein, *Classical Mechanics*, caps. 4-5; Marion-Thornton.
