---
title: Ecuaciones de Conservación
tags:
  - fluidos
  - teoria
  - conservacion
  - indice
draft: false
aliases:
  - Ecuaciones de conservación
  - Leyes de balance
  - Navier-Stokes
---

# Ecuaciones de Conservación $\rho\,\dfrac{D\vec v}{Dt}=-\nabla p+\mu\nabla^2\vec v+\rho\vec g$

> [!definicion]
> Las **ecuaciones de conservación** son las leyes de balance de la mecánica de fluidos: **masa**, **momento** y **energía**. Todas nacen de la misma receta —aplicar el [[Teorema del Transporte de Reynolds]] a la densidad de la cantidad conservada— y, junto con la **relación constitutiva** newtoniana ([[Fluido Newtoniano]]), producen el sistema cerrado que gobierna el flujo:
> $$\partial_t\rho+\nabla\cdot(\rho\vec v)=0\quad(\text{masa}),\qquad \rho\frac{D\vec v}{Dt}=\nabla\cdot\boldsymbol\sigma+\rho\vec g\quad(\text{momento}).$$
> Sustituyendo $\sigma_{ij}=-p\,\delta_{ij}+2\mu e_{ij}$ se obtienen las **ecuaciones de Navier–Stokes**, la ecuación maestra del curso.

---

> [!info]
> **Capítulo 3 del curso Mecánica de Fluidos: la unificación.** Reúne la cinemática del [[1 Cinematica del Flujo/index | Capítulo 1]] (derivada material, transporte de Reynolds) y la dinámica local del [[2 Esfuerzos y Tensor de Tensiones/index | Capítulo 2]] (tensor de esfuerzos) en las ecuaciones de movimiento.
> **Referencia.** Landau-Lifshitz, Vol. 6, §1 (continuidad, Euler), §15 (Navier–Stokes), §49 (energía); Batchelor, cap. 3.

---

## La idea del capítulo

> [!teoria] Una sola receta para tres leyes
> Para cualquier cantidad transportada por el fluido con densidad $\phi$ por unidad de volumen, el [[Teorema del Transporte de Reynolds]] da
> $$\frac{d}{dt}\int_{V(t)}\phi\,dV=\int_V\left[\frac{\partial\phi}{\partial t}+\nabla\cdot(\phi\vec v)\right]dV=\text{(fuentes)}.$$
> Eligiendo $\phi$ se obtienen las tres leyes:
> - $\phi=\rho$ (masa, sin fuentes) → **continuidad**.
> - $\phi=\rho\vec v$ (momento, fuente = fuerzas) → **ecuación de Cauchy** y **Navier–Stokes**.
> - $\phi=\rho(e+\tfrac12 v^2)$ (energía, fuente = trabajo + calor) → **ecuación de la energía**.
>
> ![[navier_stokes.svg|480]]
> *La ecuación maestra: la inercia de la partícula fluida ($\rho\,D\vec v/Dt$) iguala la suma de las fuerzas —gradiente de presión, fricción viscosa y gravedad—. Es a los fluidos lo que las ecuaciones de Maxwell son al electromagnetismo.*

> [!proposicion] El sistema cerrado (incompresible, newtoniano)
> $$\nabla\cdot\vec v=0,\qquad \rho\Big(\partial_t\vec v+(\vec v\cdot\nabla)\vec v\Big)=-\nabla p+\mu\nabla^2\vec v+\rho\vec g.$$
> Cuatro ecuaciones escalares (continuidad + 3 de momento) para cuatro incógnitas ($p$ y las tres componentes de $\vec v$). El término **no lineal** $(\vec v\cdot\nabla)\vec v$ es la fuente de toda la dificultad —y de la turbulencia—.

> [!teorema] Por qué Navier–Stokes es el centro
> De estas ecuaciones sale **todo** el resto del curso: poniendo $\mu=0$ se obtienen el [[4 Flujo Ideal/index | flujo ideal]] (Euler, Bernoulli, flujo potencial); conservando $\mu$ y adimensionalizando aparece el [[5 Flujo Viscoso/index | número de Reynolds]] y sus regímenes; y escribiéndolas en lenguaje tensorial se llega a la [[6 Formulacion Covariante del Fluido/index | hidrodinámica relativista]]. Navier–Stokes es el nodo del que todo se ramifica.

---

## Mapa del capítulo

> [!algoritmo] Notas de esta sección
> 1. **[[Conservacion de Masa]]** — continuidad $\partial_t\rho+\nabla\cdot(\rho\vec v)=0$; forma incompresible $\nabla\cdot\vec v=0$.
> 2. **[[Conservacion de Momento]]** — ecuación de Cauchy $\rho\,D\vec v/Dt=\nabla\cdot\boldsymbol\sigma+\rho\vec g$ desde la 2ª ley de Newton.
> 3. **[[Ecuaciones de Navier-Stokes]]** — sustituir la ley newtoniana en Cauchy; la ecuación maestra y sus términos.
> 4. **[[Conservacion de Energia]]** — 1ª ley para el fluido; energía cinética e interna; disipación viscosa $\Phi\ge0$.

> [!corolario] Qué prepara este capítulo
> Con el sistema cerrado de Navier–Stokes, el [[4 Flujo Ideal/index | Capítulo 4]] explorará el límite ideal ($\mu=0$) —donde la hidrostática vive como el caso $\vec v=0$ de Euler— y el [[5 Flujo Viscoso/index | Capítulo 5]] el papel de la viscosidad a través del número de Reynolds.

> [!referencia]
> Landau-Lifshitz, Vol. 6, §§1–2 (continuidad y Euler), §15 (Navier–Stokes), §49 (energía). Batchelor, *An Introduction to Fluid Dynamics*, cap. 3.
