---
title: Cinemática del Flujo
tags:
  - fluidos
  - teoria
  - cinematica
  - indice
draft: false
aliases:
  - Cinemática del flujo
  - Cinemática de fluidos
---

# Cinemática del Flujo $\dfrac{D}{Dt}=\partial_t+(\vec v\cdot\nabla),\qquad \partial_j v_i=e_{ij}+\omega_{ij}$

> [!definicion]
> La **cinemática** describe el movimiento de un fluido —su campo de velocidades $\vec v(\vec x,t)$— **sin preguntarse aún por las fuerzas** que lo causan. Dos herramientas la organizan: la **derivada material** $\dfrac{D}{Dt}=\partial_t+(\vec v\cdot\nabla)$, que da la tasa de cambio siguiendo a una partícula fluida, y la **descomposición del gradiente de velocidad**
> $$\partial_j v_i=\underbrace{\tfrac12(\partial_i v_j+\partial_j v_i)}_{e_{ij}\ \text{(deformación)}}+\underbrace{\tfrac12(\partial_j v_i-\partial_i v_j)}_{\omega_{ij}\ \text{(rotación)}},$$
> que separa cómo un elemento fluido **se deforma** de cómo **rota**. Con ellas y el **teorema del transporte de Reynolds** queda lista toda la maquinaria para la dinámica.

---

> [!info]
> **Capítulo 1 del curso Mecánica de Fluidos.** Es la base puramente cinemática: el lenguaje con el que luego escribiremos las leyes de balance. Notación SI, $\vec v$ campo de velocidades, convenio de suma de Einstein, $\delta_{ij},\epsilon_{ijk}$.
> **Referencia.** Landau-Lifshitz, Vol. 6 (*Mecánica de Fluidos*), §1; Batchelor, cap. 2; Aris, caps. 4–5.

---

## La idea del capítulo

> [!teoria] Mirar el fluido de dos maneras, y descomponer su movimiento
> Un fluido se puede describir **siguiendo cada partícula** (descripción **lagrangiana**, $\vec x(t)$) o **mirando puntos fijos del espacio** por los que el fluido pasa (descripción **euleriana**, el campo $\vec v(\vec x,t)$). El puente entre ambas es la **derivada material**: la aceleración de una partícula fluida es
> $$\vec a=\frac{D\vec v}{Dt}=\underbrace{\partial_t\vec v}_{\text{local}}+\underbrace{(\vec v\cdot\nabla)\vec v}_{\text{convectivo}},$$
> donde el término **convectivo** —no lineal— es el que hace difícil (y rica) la mecánica de fluidos.
>
> El movimiento local de un elemento se entiende mirando la velocidad **relativa** entre puntos vecinos, $dv_i=\partial_j v_i\,dx_j$. Ese gradiente $\partial_j v_i$ se parte en una **deformación** (parte simétrica $e_{ij}$) y una **rotación** rígida (parte antisimétrica $\omega_{ij}$, ligada a la vorticidad $\vec\omega=\nabla\times\vec v$):
>
> ![[gradiente_velocidad.svg|620]]
> *Todo movimiento local de un elemento fluido se descompone en deformación pura ($e_{ij}$, simétrica) más rotación rígida ($\omega_{ij}$, antisimétrica). Es la descomposición tensorial que vertebra el curso.*

> [!proposicion] Lo que mide cada pieza
> | Objeto | Definición | Significado |
> |:---|:---|:---|
> | Derivada material | $\dfrac{D}{Dt}=\partial_t+v_j\partial_j$ | tasa de cambio siguiendo la partícula |
> | Rapidez de deformación | $e_{ij}=\tfrac12(\partial_i v_j+\partial_j v_i)$ | estiramientos ($e_{ii}$) y cizallas ($e_{i\neq j}$) |
> | Dilatación | $e_{kk}=\nabla\cdot\vec v$ | tasa de cambio de volumen; $=0$ si incompresible |
> | Vorticidad | $\vec\omega=\nabla\times\vec v$ | el doble de la velocidad angular local |
> | Transporte de Reynolds | $\dfrac{d}{dt}\!\int_V\phi\,dV=\int_V[\partial_t\phi+\nabla\cdot(\phi\vec v)]\,dV$ | derivar integrales sobre volúmenes móviles |

> [!teorema] El puente a la dinámica
> El **teorema del transporte de Reynolds** convierte "la tasa de cambio de una cantidad que viaja con el fluido" en integrales que sí sabemos manejar. Aplicado a la masa da la **continuidad**; aplicado al momento dará las ecuaciones de movimiento. Por eso la cinemática no es un preámbulo: es la mitad del trabajo. Lo demás (capítulo 3) es decir **qué** se conserva.

---

## Mapa del capítulo

> [!algoritmo] Notas de esta sección
> 1. **[[Descripcion Euleriana y Lagrangiana]]** — los dos puntos de vista; derivada material $\dfrac{D}{Dt}=\partial_t+(\vec v\cdot\nabla)$ y la aceleración convectiva.
> 2. **[[Lineas de Flujo]]** — líneas de corriente, trayectorias y trazas; cuándo coinciden (flujo estacionario).
> 3. **[[Tensor Gradiente de Velocidad]]** — $\partial_j v_i=e_{ij}+\omega_{ij}$; velocidad relativa entre puntos vecinos.
> 4. **[[Deformacion y Vorticidad]]** — significado de $e_{ij}$ (dilatación $\nabla\cdot\vec v$, cizalla) y de $\vec\omega=\nabla\times\vec v$; circulación.
> 5. **[[Teorema del Transporte de Reynolds]]** — derivar integrales sobre volúmenes materiales; la puerta a las leyes de conservación.

> [!corolario] Qué prepara este capítulo
> Con la **derivada material** (cómo cambia algo que viaja con el fluido), la **descomposición $e_{ij}+\omega_{ij}$** (cómo se mueve un elemento) y el **transporte de Reynolds** (cómo derivar balances integrales), el capítulo 2 podrá introducir el **tensor de esfuerzos** y el capítulo 3 escribir las **ecuaciones de Navier–Stokes** sin herramienta nueva.

> [!referencia]
> Landau-Lifshitz, Vol. 6, §1 (introduce la cinemática y la continuidad casi de inmediato — estilo dinámica-primero). Batchelor, *An Introduction to Fluid Dynamics*, cap. 2; Aris, *Vectors, Tensors and the Basic Equations of Fluid Mechanics*.
