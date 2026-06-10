---
title: Fundamentos del Circuito Eléctrico
tags:
  - circuitos-electricos
  - teoria
  - resistivos
  - index
draft: false
aliases:
  - fundamentos del circuito
  - variables del circuito
---

# Fundamentos del Circuito Eléctrico

> [!definicion]
> Antes de resolver un circuito hay que fijar su **lenguaje**: qué es la corriente, qué es la
> tensión, cómo se relacionan con la energía a través de la **potencia**, y con qué **convenio de
> signos** se interpretan. Estas tres magnitudes —$i$, $v$, $p$— y su convenio son el alfabeto sobre
> el que se escribe todo el curso.

> [!info]
> Primera sección del [[1 Conceptos Fundamentales y Resistivos/index| capítulo 1]]. Lo de aquí se
> usa en **cada** nota posterior: la ley de Ohm, Kirchhoff y el balance de potencias presuponen estas
> definiciones y este convenio.

---

## El alfabeto de los circuitos

> [!teoria] De la carga a la potencia
> Todo parte de la **carga** $q$ (en culombios). Cuando la carga se mueve aparece la **corriente**
> $$i=\frac{dq}{dt}\quad[\text{A}],$$
> el ritmo al que la carga atraviesa una sección. Mover esa carga cuesta o libera energía: la
> **tensión** (o diferencia de potencial)
> $$v=\frac{dw}{dq}\quad[\text{V}]$$
> es la energía por unidad de carga entre dos puntos. El producto de ambas es la **potencia**
> $$p=vi=\frac{dw}{dt}\quad[\text{W}],$$
> el ritmo de transferencia de energía. Saber **el signo** de $p$ —si el elemento absorbe o
> entrega— exige un **convenio** consistente, y de ahí la importancia de fijarlo desde el principio.

> [!info] Las notas de esta sección
> | Nota | Contenido |
> |:---|:---|
> | [[Variables del Circuito]] | carga, corriente $i=dq/dt$ y tensión $v$; su sentido físico |
> | [[Convenio de Signos]] | signo pasivo (receptor) vs activo (generador); cuándo $p>0$ |
> | [[Potencia y Energia]] | $p=vi$, energía $W=\int p\,dt$, potencia absorbida/entregada |
> | [[Sistema de Unidades]] | SI, prefijos y magnitudes eléctricas |
> | [[Tipos de Corriente]] | corriente continua (CC) y alterna (CA); formas de onda |
> | [[Instrumentos de Medicion]] | voltímetro, amperímetro y vatímetro; cómo se conectan |

> [!corolario]
> Fijado el convenio, la frase "este elemento absorbe $5\ \text{W}$" o "esta fuente entrega
> $5\ \text{W}$" deja de ser ambigua. Ese rigor es lo que permite el [[Balance de Potencias| balance de potencias]] de toda la red.

> [!referencia]
> Fraile Mora, cap. 1, §1.2. Siguiente sección: [[Elementos del Circuito/index| Elementos del circuito]].
