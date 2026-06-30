---
title: Flujo Viscoso
order: 5
tags:
  - fluidos
  - teoria
  - flujo-viscoso
  - indice
draft: false
aliases:
  - Flujo viscoso
  - Número de Reynolds
  - Flujos viscosos
---

# Flujo Viscoso $\mathrm{Re}=\dfrac{\rho U L}{\mu}=\dfrac{\text{inercia}}{\text{viscosidad}}$

> [!definicion]
> El **flujo viscoso** reintroduce la fricción ($\mu\neq0$) que el [[4 Flujo Ideal/index | flujo ideal]] ignoraba. Su parámetro rector es el **número de Reynolds** $\mathrm{Re}=\rho U L/\mu=UL/\nu$, que mide la competencia entre la **inercia** ($\rho U^2/L$) y la **fricción viscosa** ($\mu U/L^2$). Reynolds lo gobierna todo: para $\mathrm{Re}\ll1$ manda la viscosidad (**flujo de Stokes**, reptante); para $\mathrm{Re}\gg1$ manda la inercia salvo en una **capa límite** delgada pegada a las paredes.

---

> [!info]
> **Capítulo 5 del curso Mecánica de Fluidos.** Resuelve las [[Ecuaciones de Navier-Stokes]] del [[3 Ecuaciones de Conservacion/index | Capítulo 3]] en los regímenes donde la viscosidad importa, y repara la **paradoja de d'Alembert** del [[4 Flujo Ideal/index | Capítulo 4]] (el arrastre nace de la viscosidad). **Referencia.** Landau-Lifshitz, Vol. 6, §§17–20 (flujo viscoso, Stokes) y §§39–41 (capa límite); Batchelor, caps. 4 y 5; Acheson, caps. 2, 7–8.

---

## La idea del capítulo

> [!teoria] Un solo número decide el régimen
> Al **adimensionalizar** Navier–Stokes con escalas $L$ (longitud), $U$ (velocidad), $L/U$ (tiempo) y $\rho U^2$ (presión), la ecuación queda
> $$\frac{D\vec v^*}{Dt^*}=-\nabla^* p^*+\frac{1}{\mathrm{Re}}\nabla^{*2}\vec v^*,$$
> con **un único parámetro**, $\mathrm{Re}$. De ahí dos consecuencias:
> - **Semejanza dinámica**: dos flujos geométricamente semejantes con el mismo $\mathrm{Re}$ son **idénticos** (base de los ensayos en túnel de viento con modelos a escala).
> - **Dos límites resolubles**: $\mathrm{Re}\ll1$ borra la inercia (ecuaciones lineales de Stokes); $\mathrm{Re}\gg1$ confina la viscosidad a una capa límite y deja flujo ideal afuera.
>
> ![[reynolds_regimenes.svg|560]]
> *El número de Reynolds decide la física: a bajo $\mathrm{Re}$ el flujo es laminar y simétrico (la viscosidad domina); a alto $\mathrm{Re}$ aparece una estela turbulenta detrás del cuerpo (la inercia domina).*

> [!proposicion] El mapa de regímenes
> | Régimen | Física | Herramienta |
> |:---|:---|:---|
> | $\mathrm{Re}\ll1$ | viscosidad domina; reptante, reversible | [[Flujo de Stokes]] |
> | $\mathrm{Re}$ moderado | soluciones unidireccionales exactas | [[Soluciones Viscosas Exactas]] |
> | $\mathrm{Re}\gg1$ | inercia afuera, viscosidad en capa fina | [[Capa Limite]] |
> | $\mathrm{Re}$ muy alto | inestabilidad y turbulencia | (más allá del curso) |

> [!teorema] La viscosidad arregla d'Alembert
> El [[Flujo Potencial]] predecía **arrastre nulo**. La viscosidad, aunque sea pequeña, impone **no deslizamiento** en la pared y crea una **capa límite** que puede **desprenderse**, formando una estela. Esa ruptura de la simetría adelante-atrás es la que produce el **arrastre** real. Así, la viscosidad —despreciable lejos del cuerpo— es **decisiva** cerca de él.

---

## Mapa del capítulo

> [!algoritmo] Notas de esta sección
> 1. **[[Numero de Reynolds y Adimensionalizacion]]** — $\mathrm{Re}=\rho UL/\mu$ desde Navier–Stokes adimensional; semejanza dinámica; otros números (Mach, Froude).
> 2. **[[Soluciones Viscosas Exactas]]** — flujos de Couette y Poiseuille (perfiles lineal y parabólico); ley $R^4$ de Hagen–Poiseuille.
> 3. **[[Capa Limite]]** — el concepto de Prandtl; espesor $\delta\sim\sqrt{\nu x/U}$; arrastre y separación.
> 4. **[[Flujo de Stokes]]** — flujo reptante $\mathrm{Re}\ll1$; ecuaciones de Stokes; arrastre $F=6\pi\mu R U$ y velocidad terminal.

> [!corolario] Qué prepara este capítulo
> Con los flujos viscosos completos, el [[6 Formulacion Covariante del Fluido/index | Capítulo 6]] da el salto final: reescribir la conservación de masa y momento en lenguaje **tensorial** ($T^{\mu\nu}$) y llegar a la **hidrodinámica relativista** —el puente a Landau Vol. 6 (y Vol. 2)—.

> [!referencia]
> Landau-Lifshitz, Vol. 6, §§17–20 y §§39–41. Batchelor, *An Introduction to Fluid Dynamics*, caps. 4–5; Acheson, *Elementary Fluid Dynamics*, caps. 2, 7–8.
