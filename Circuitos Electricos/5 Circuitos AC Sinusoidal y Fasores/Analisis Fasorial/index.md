---
title: Análisis Fasorial
tags:
  - circuitos-electricos
  - teoria
  - fasores
  - index
draft: false
aliases:
  - análisis fasorial
  - análisis de circuitos en CA
---

# Análisis Fasorial

> [!definicion]
> El **análisis fasorial** resuelve circuitos de corriente alterna en régimen permanente aplicando
> **los mismos métodos** del análisis resistivo —ley de Ohm, Kirchhoff, mallas, nodos, superposición,
> Thévenin, Norton, divisores— pero con **fasores** (tensiones y corrientes complejas) e
> **impedancias** $Z$ en lugar de magnitudes reales y resistencias. El **diagrama fasorial** es su
> apoyo gráfico.

> [!info]
> Tercera sección del [[5 Circuitos AC Sinusoidal y Fasores/index| capítulo 5]]. Reúne los
> [[Fasores/index| fasores]] y la [[Impedancia y Admitancia/index| impedancia]] para resolver
> circuitos completos. Es la traducción a CA de los [[2 Metodos de Analisis y Teoremas/index| métodos y teoremas]] del capítulo 2. Fraile Mora, cap. 2, §2.8.

---

## Nada nuevo, solo números complejos

> [!teoria] Por qué todo se reutiliza
> La clave del análisis fasorial es que **no hay que aprender métodos nuevos**. Como la ley de cada
> elemento es ahora $\overline{V}=Z\,\overline{I}$ —idéntica en forma a $v=Ri$— y las leyes de
> Kirchhoff valen igual para fasores ($\sum\overline{I}=0$ en un nodo, $\sum\overline{V}=0$ en una
> malla), **toda** la maquinaria del capítulo 2 funciona cambiando:
> $$R\to Z,\qquad v,i\to \overline{V},\overline{I},\qquad \text{números reales}\to\text{complejos}.$$
> Mallas, nodos, Thévenin, Norton, divisores y superposición se aplican letra por letra. →
> [[Metodos en Regimen Fasorial]].

> [!teoria] El diagrama fasorial: ver las fases
> Como los fasores son vectores del plano complejo, las leyes de Kirchhoff se vuelven **sumas
> vectoriales**: el **diagrama fasorial** dibuja tensiones y corrientes como flechas y muestra de un
> vistazo sus módulos y desfases. Es a la CA lo que el diagrama de un circuito resistivo nunca pudo
> ser: una imagen de las **fases**. → [[Diagramas Fasoriales]].

## Mapa de la sección

> [!info] Las notas de esta sección
> | Nota | Contenido |
> |:---|:---|
> | [[Metodos en Regimen Fasorial]] | mallas, nodos, Thévenin… en complejo; circuito AC resuelto |
> | [[Diagramas Fasoriales]] | representación gráfica; Kirchhoff como suma de vectores |

> [!corolario]
> El análisis fasorial es el premio de todo el capítulo: convertida la senoide en fasor y el elemento
> en impedancia, resolver un circuito de CA es **el mismo problema** que uno resistivo, con la sola
> diferencia de operar con números complejos.

> [!referencia]
> Fraile Mora, cap. 2, §2.8. Anterior: [[Impedancia y Admitancia/index| Impedancia y admitancia]].
> Siguiente: [[Potencia en AC/index| Potencia en AC]].
