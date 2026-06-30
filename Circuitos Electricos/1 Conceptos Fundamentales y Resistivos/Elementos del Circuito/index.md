---
title: Elementos del Circuito
order: 2
tags:
  - circuitos-electricos
  - teoria
  - resistivos
  - index
draft: false
aliases:
  - elementos del circuito
  - elementos activos y pasivos
---

# Elementos del Circuito

> [!definicion]
> Un circuito se arma con dos clases de elementos. Los **pasivos** no pueden entregar más energía de la que reciben: la **resistencia** la disipa, el [[Capacitor| condensador]] y el [[Inductor| inductor]] la almacenan. Los **activos** son las **fuentes** (o generadores), que entregan energía al circuito. Modelarlos correctamente —ideales frente a reales, independientes frente a dependientes— es el segundo paso del análisis.

> [!info]
> Segunda sección del [[1 Conceptos Fundamentales y Resistivos/index| capítulo 1]]. Usa el lenguaje de [[Fundamentos/index| Fundamentos]] ($v$, $i$, $p$ y el convenio) y alimenta a [[Leyes de Kirchhoff/index| Kirchhoff]], que conecta estos elementos en una red.

---

## Activos y pasivos

> [!teoria] La resistencia y las fuentes
> El único elemento pasivo de este capítulo es la **resistencia**, gobernada por la **ley de Ohm**
> $$v=Ri,$$
> una relación **algebraica y lineal**: por eso los circuitos resistivos se resuelven sin ecuaciones diferenciales. Disipa potencia $p=Ri^2=v^2/R\ge0$ (siempre absorbe), nunca la entrega.
>
> Las **fuentes** son los elementos activos. Una **fuente de tensión** ideal impone $v$ sin importar la corriente; una **fuente de corriente** ideal impone $i$ sin importar la tensión. En la realidad ninguna es ideal: una fuente **real** lleva una resistencia interna que limita lo que puede entregar. Y además de las **independientes** (valor fijo) existen las **dependientes**, cuyo valor lo controla otra tensión o corriente del circuito —el modelo de transistores y amplificadores—.

> [!info] Las notas de esta sección
> | Nota | Contenido |
> |:---|:---|
> | [[Resistencia y Ley de Ohm]] | $v=Ri$; conductancia $G=1/R$; potencia disipada |
> | [[Fuentes Independientes]] | fuente de tensión y de corriente **ideales** |
> | [[Fuentes Dependientes]] | controladas: VCVS, VCCS, CCVS, CCCS |
> | [[Fuentes Reales]] | resistencia interna; recta de carga; límites de entrega |
> | [[Elementos Activos y Pasivos]] | clasificación general y modelos lineales |

> [!warning]
> No confundir **fuente ideal** con **real**: cortocircuitar una fuente de tensión ideal daría corriente infinita. La resistencia interna de la fuente real es la que vuelve físico el modelo; ignorarla es la causa más común de resultados absurdos.

> [!referencia]
> Fraile Mora, cap. 1, §1.3, §1.5, §1.9. Siguiente sección: [[Leyes de Kirchhoff/index| Leyes de Kirchhoff]].
