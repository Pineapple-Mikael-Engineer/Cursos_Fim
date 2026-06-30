---
title: Movimiento Relativo
order: 2
tags:
  - dinamica
  - teoria
  - movimiento-relativo
  - index
draft: false
aliases:
  - movimiento relativo
  - sistemas de referencia
  - marcos de referencia
---

# Movimiento Relativo

> [!definicion]
> El **movimiento relativo** estudia cómo se transforman la posición, la velocidad y la aceleración de una partícula **al cambiar de sistema de referencia**. Entre un marco **fijo** $F$ y uno **móvil** $M$, la posición siempre cumple $\vec r=\vec R_M+\vec r\,'$ (con $\vec R_M$ el origen de $M$ y $\vec r\,'$ medido en $M$); lo que cambia es **cómo derivar**, según $M$ solo **traslade** o también **rote**.

> [!info]
> Segundo bloque del curso de [[Dinamica/index | Dinámica]]. Cierra la cinemática de la [[1 Particula/index | partícula]] y entrega la herramienta —el operador en base móvil— con la que se deducen después la cinemática del [[4 Cuerpo Rigido/index| cuerpo rígido]] y las [[Ecuaciones de Euler 3D | ecuaciones de Euler]]. Referencia: PDF *Física I* (GETI), Lección 2; Taylor §9.

---

## Dos marcos, una partícula

> [!teoria] La descomposición básica y sus dos casos
> Siempre $\vec r=\vec R_M+\vec r\,'$:
>
> ![[marcos_referencia.svg|620]]
>
> *El marco fijo $F$ y el móvil $M$ (que aquí rota con $\vec\omega$). La partícula $P$ se ubica con $\vec r$ desde $F$ o con $\vec r\,'$ desde $M$; $\vec R_M$ une los orígenes.*
>
> - Si $M$ solo **traslada** (sus versores no giran), derivar es directo y la aceleración se conserva cuando $M$ va a velocidad constante: $\vec a=\vec a\,'$ (relatividad de Galileo). → [[Marcos en Traslacion]].
> - Si $M$ **rota** con velocidad angular $\vec\omega$, sus versores **cambian** vistos desde $F$, y derivar exige el **operador derivada en base móvil** $\left.\tfrac{d}{dt}\right|_F=\left.\tfrac{d}{dt}\right|_M+\vec\omega\times$, del que salen la velocidad de arrastre y la aceleración de **Coriolis**. → [[Operador Derivada en Base Movil]].

> [!corolario]
> Toda la dificultad del movimiento relativo está en un hecho: una **base que gira tiene versores con derivada no nula**. El operador en base móvil lo encapsula, y de él se deduce el resto —Coriolis, la cinemática del sólido y el término giroscópico de Euler—.

> [!referencia]
> PDF *Física I* (GETI), Lección 2; Taylor §9. Notas: [[Marcos en Traslacion]] y [[Operador Derivada en Base Movil]].
