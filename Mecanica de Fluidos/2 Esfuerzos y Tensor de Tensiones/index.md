---
title: Esfuerzos y Tensor de Tensiones
order: 2
tags:
  - fluidos
  - teoria
  - esfuerzos
  - indice
draft: false
aliases:
  - Esfuerzos y tensor de tensiones
  - Tensor de esfuerzos
  - Estado de tensiones
---

# Esfuerzos y Tensor de Tensiones $t_i=\sigma_{ij}\,n_j,\qquad \sigma_{ij}=-p\,\delta_{ij}+\tau_{ij}$

> [!definicion]
> Sobre un fluido actúan dos clases de fuerzas: **másicas** (por unidad de volumen, como la gravedad $\rho\vec g$) y **de superficie** (por unidad de área, el contacto entre porciones de fluido). La fuerza de superficie sobre un plano de normal $\hat n$ es la **tracción** $\vec t$, y depende **linealmente** de $\hat n$ a través del **tensor de esfuerzos de Cauchy** $\sigma_{ij}$:
> $$t_i=\sigma_{ij}\,n_j.$$
> En un fluido, el estado de tensión se separa en una parte **isótropa** (la **presión** $p$) y una **desviadora viscosa** $\tau_{ij}$: $\ \sigma_{ij}=-p\,\delta_{ij}+\tau_{ij}$. Que $\tau_{ij}$ dependa linealmente de la **rapidez de deformación** $e_{ij}$ define al **fluido newtoniano**.

---

> [!info]
> **Capítulo 2 del curso Mecánica de Fluidos: el corazón tensorial.** Toma la cinemática del [[1 Cinematica del Flujo/index | Capítulo 1]] (el tensor $e_{ij}$) y le añade la **dinámica local**: cómo se transmiten las fuerzas dentro del fluido. Su fruto —$\nabla\cdot\boldsymbol\sigma$— es el ingrediente que faltaba para el balance de momento. **Referencia.** Landau-Lifshitz, Vol. 6, §15; Batchelor, caps. 1 y 3; Aris, caps. 5–6.

---

## La idea del capítulo

> [!teoria] De una fuerza a un tensor
> En un sólido o un fluido, la fuerza que una porción ejerce sobre otra a través de una superficie **no es paralela** a la normal en general: tiene componentes normales (presión, tracción) y tangenciales (cortante). Para capturar *todas* las direcciones de corte posibles en un punto hace falta un objeto de **nueve componentes**: el tensor $\sigma_{ij}$, donde el primer índice es la **dirección de la fuerza** y el segundo la **cara** sobre la que actúa.
>
> ![[tensor_esfuerzos.svg|420]]
> *Las nueve componentes $\sigma_{ij}$ sobre las caras de un elemento cúbico: en cada cara, una componente normal (presión/tracción) y dos cortantes. El balance de momento angular obliga a que el tensor sea **simétrico**, $\sigma_{ij}=\sigma_{ji}$.*

> [!proposicion] Las tres piezas del capítulo
> | Concepto | Resultado | De dónde sale |
> |:---|:---|:---|
> | Tensor de Cauchy | $t_i=\sigma_{ij}n_j$ | balance de fuerzas en un tetraedro |
> | Simetría | $\sigma_{ij}=\sigma_{ji}$ | balance de momento angular |
> | Descomposición | $\sigma_{ij}=-p\,\delta_{ij}+\tau_{ij}$ | separar isótropo + desviador |
> | Ley newtoniana | $\tau_{ij}=2\mu\,e_{ij}+\lambda\,\delta_{ij}e_{kk}$ | linealidad e isotropía |

> [!teorema] Por qué importa: cierra las ecuaciones
> La segunda ley de Newton para un fluido (Capítulo 3) necesita la **fuerza neta de superficie** sobre un elemento, que es la **divergencia del tensor de esfuerzos** $\partial_j\sigma_{ij}$. Sin una ley que ligue $\sigma_{ij}$ al movimiento (la **relación constitutiva** newtoniana), el sistema tendría más incógnitas que ecuaciones. Por eso este capítulo es el puente: convierte "hay fuerzas de contacto" en un término calculable, $\nabla\cdot\boldsymbol\sigma=-\nabla p+\mu\nabla^2\vec v$, que es el corazón de **Navier–Stokes**.

---

## Mapa del capítulo

> [!algoritmo] Notas de esta sección
> 1. **[[Tensor de Esfuerzos de Cauchy]]** — la tracción $t_i=\sigma_{ij}n_j$ desde el tetraedro de Cauchy; simetría $\sigma_{ij}=\sigma_{ji}$ por momento angular.
> 2. **[[Presion y Esfuerzos Viscosos]]** — descomposición $\sigma_{ij}=-p\,\delta_{ij}+\tau_{ij}$; presión mecánica y termodinámica; el desviador.
> 3. **[[Fluido Newtoniano]]** — relación constitutiva $\tau_{ij}=2\mu\,e_{ij}+\lambda\,\delta_{ij}e_{kk}$; viscosidad de corte y de volumen; hipótesis de Stokes.

> [!corolario] Qué prepara este capítulo
> Con el tensor de esfuerzos y la ley newtoniana, el [[3 Ecuaciones de Conservacion/index | Capítulo 3]] podrá escribir la **ecuación de Cauchy** $\rho\,D\vec v/Dt=\nabla\cdot\boldsymbol\sigma+\rho\vec g$ y, sustituyendo la relación constitutiva, las **ecuaciones de Navier–Stokes** completas.

> [!referencia]
> Landau-Lifshitz, Vol. 6, §15 ("El tensor de tensiones"). Batchelor, *An Introduction to Fluid Dynamics*, §1.3 y §3.3; Aris, *Vectors, Tensors and the Basic Equations of Fluid Mechanics*, cap. 5.
