---
title: Flujo Ideal
tags:
  - fluidos
  - teoria
  - flujo-ideal
  - indice
draft: false
aliases:
  - Flujo ideal
  - Fluido ideal
  - Flujo no viscoso
---

# Flujo Ideal $\rho\,\dfrac{D\vec v}{Dt}=-\nabla p+\rho\vec g\quad(\mu=0)$

> [!definicion]
> Un **flujo ideal** es el de un fluido **sin viscosidad** ($\mu=0$). Las ecuaciones de Navier–Stokes pierden el término de fricción y se reducen a la **ecuación de Euler** $\rho\,D\vec v/Dt=-\nabla p+\rho\vec g$. Es el límite donde la mecánica de fluidos se resuelve **a mano**: de Euler salen la **hidrostática** (como el caso $\vec v=0$), la **ecuación de Bernoulli**, el **flujo potencial** y los **teoremas de vorticidad** de Kelvin y Helmholtz.

---

> [!info]
> **Capítulo 4 del curso Mecánica de Fluidos.** Es el límite $\mu=0$ de las [[Ecuaciones de Navier-Stokes]] del [[3 Ecuaciones de Conservacion/index | Capítulo 3]]. Siguiendo a **Landau** (Vol. 6, cap. 1), la **hidrostática no es un capítulo aparte**: vive como el corolario $\vec v=0$ de Euler.
> **Referencia.** Landau-Lifshitz, Vol. 6, §§2–9; Batchelor, cap. 5–6; Acheson, cap. 1, 3–5.

---

## La idea del capítulo

> [!teoria] Quitar la viscosidad lo simplifica todo
> Sin viscosidad desaparece la condición de **no deslizamiento** (el fluido puede deslizar sobre las paredes; solo se iguala la componente **normal** de la velocidad) y desaparece la disipación. La ecuación de Euler, reescrita con la identidad $(\vec v\cdot\nabla)\vec v=\nabla(\tfrac12 v^2)-\vec v\times\vec\omega$ ([[Descripcion Euleriana y Lagrangiana]]), revela su estructura:
> $$\partial_t\vec v+\nabla\!\left(\tfrac12 v^2\right)-\vec v\times\vec\omega=-\frac1\rho\nabla p+\vec g.$$
> De aquí, según las hipótesis, se desprenden los grandes resultados clásicos:
> - **$\vec v=0$** → hidrostática $\nabla p=\rho\vec g$ (presión, empuje de Arquímedes, atmósfera).
> - **estacionario** → **Bernoulli** $\tfrac12 v^2+p/\rho+gz=$ cte a lo largo de una línea de corriente.
> - **irrotacional** ($\vec\omega=0$) → **flujo potencial** $\vec v=\nabla\phi$, $\nabla^2\phi=0$, y Bernoulli vale en *todo* el campo.
>
> ![[flujo_cilindro.svg|460]]
> *Flujo potencial alrededor de un cilindro: las líneas de corriente son simétricas adelante-atrás. Esa simetría implica **fuerza de arrastre nula** (paradoja de d'Alembert): la marca —y la limitación— del flujo ideal.*

> [!proposicion] Los frutos de Euler
> | Hipótesis añadida | Resultado | Nota |
> |:---|:---|:---|
> | $\vec v=0$ | $\nabla p=\rho\vec g$ (hidrostática) | [[Ecuacion de Euler]] |
> | estacionario, a lo largo de una línea | $\tfrac12 v^2+p/\rho+gz=$ cte | [[Ecuacion de Bernoulli]] |
> | irrotacional + incompresible | $\nabla^2\phi=0$ | [[Flujo Potencial]] |
> | barotrópico, ideal | $D\Gamma/Dt=0$ (Kelvin) | [[Vorticidad y Teoremas]] |

> [!warning] El precio de idealizar
> El flujo ideal **no puede** explicar el arrastre, la sustentación con circulación realista, ni la capa límite: sin viscosidad, un cuerpo no siente fuerza neta en flujo uniforme (**paradoja de d'Alembert**). La viscosidad —por pequeña que sea— cambia la física cerca de las paredes; eso es el [[5 Flujo Viscoso/index | Capítulo 5]]. Aun así, lejos de las paredes el flujo ideal describe muy bien la realidad.

---

## Mapa del capítulo

> [!algoritmo] Notas de esta sección
> 1. **[[Ecuacion de Euler]]** — el límite $\mu=0$; la hidrostática como corolario $\vec v=0$ (presión, Arquímedes, atmósfera); condición de deslizamiento.
> 2. **[[Ecuacion de Bernoulli]]** — $\tfrac12 v^2+p/\rho+gz=$ cte desde Euler; Torricelli, Venturi, tubo de Pitot.
> 3. **[[Flujo Potencial]]** — $\vec v=\nabla\phi$, $\nabla^2\phi=0$; función de corriente; flujo alrededor de un cilindro; paradoja de d'Alembert.
> 4. **[[Vorticidad y Teoremas]]** — ecuación de vorticidad $D\vec\omega/Dt=(\vec\omega\cdot\nabla)\vec v$; teoremas de Kelvin y Helmholtz.

> [!corolario] Qué prepara este capítulo
> El flujo ideal fija el comportamiento **lejos de las paredes**. El [[5 Flujo Viscoso/index | Capítulo 5]] reintroduce $\mu$ y muestra dónde el modelo ideal falla —la **capa límite** pegada a las superficies— y cómo el **número de Reynolds** mide la competencia entre inercia y viscosidad.

> [!referencia]
> Landau-Lifshitz, Vol. 6, cap. 1 ("Fluidos ideales"), §§2–9. Batchelor, *An Introduction to Fluid Dynamics*, caps. 5–6; Acheson, *Elementary Fluid Dynamics*.
