---
title: Ondas Electromagnéticas
tags:
  - electromagnetismo
  - teoria
  - ondas
  - indice
draft: false
aliases:
  - Ondas electromagnéticas
  - La luz
---

# Ondas Electromagnéticas $\Box\vec E=0,\quad c=\dfrac{1}{\sqrt{\mu_0\varepsilon_0}}$

> [!definicion]
> Una **onda electromagnética** es una perturbación de $\vec E$ y $\vec B$ que se propaga por el espacio a la velocidad $c=1/\sqrt{\mu_0\varepsilon_0}$, sin necesidad de medio. Es una **consecuencia directa** de las ecuaciones de Maxwell: en el vacío, cada campo satisface la ecuación de ondas
> $$\nabla^2\vec E=\mu_0\varepsilon_0\frac{\partial^2\vec E}{\partial t^2},\qquad \nabla^2\vec B=\mu_0\varepsilon_0\frac{\partial^2\vec B}{\partial t^2}.$$
> La luz **es** un campo electromagnético: óptica y electromagnetismo son la misma teoría.

---

> [!info]
> **Capítulo 5 del curso Electromagnetismo.** Es la cosecha del capítulo 4: las ondas salen de las [[Ecuaciones de Maxwell]] sin postulado nuevo. Usa la ecuación de ondas, la identidad BAC–CAB ([[Identidades Vectoriales]]) y el vector de Poynting ([[Energia y Momento]]).
> **Referencia.** Griffiths, *Introduction to Electrodynamics*, cap. 9.

---

## La idea del capítulo

> [!teoria] De Maxwell a la luz
> Aplicando $\nabla\times$ a Faraday y usando la corriente de desplazamiento, el acoplamiento $\vec E\leftrightarrow\vec B$ se cierra en una ecuación de ondas con velocidad
> $$c=\frac{1}{\sqrt{\mu_0\varepsilon_0}}\approx 3{,}00\times10^8\ \text{m/s}.$$
> Que esta velocidad coincida con la de la luz fue la prueba de que la luz es electromagnetismo. Las soluciones más simples son las **ondas planas monocromáticas**: $\vec E$ y $\vec B$ perpendiculares entre sí y a la dirección de propagación $\vec k$, en fase, con $E=cB$.
>
> ![[onda_plana.svg|480]]
> *Onda plana: $\vec E$ (vertical) y $\vec B$ (horizontal) oscilan en fase, perpendiculares entre sí y a $\vec k$. La onda es transversal y transporta energía y momento en la dirección de $\vec k$.*

> [!proposicion] Lo que caracteriza a una onda EM
> | Propiedad | Enunciado |
> |:---|:---|
> | Transversal | $\vec E\perp\vec k$ y $\vec B\perp\vec k$ (de $\nabla\cdot\vec E=0$) |
> | $\vec E\perp\vec B$ | $\vec B=\dfrac{1}{c}\,\hat k\times\vec E$ (de Faraday) |
> | Amplitudes | $E=cB$ |
> | Velocidad | $c=1/\sqrt{\mu_0\varepsilon_0}$ en vacío; $v=c/n$ en un medio |
> | Energía | $\langle\vec S\rangle=\tfrac12 c\varepsilon_0 E_0^2\,\hat k$ (intensidad) |
> | Polarización | dirección de $\vec E$: lineal, circular o elíptica |

---

## Mapa del capítulo

> [!algoritmo] Notas de esta sección
> 1. **[[Ecuacion de Ondas]]** — $\Box\vec E=0$ desde Maxwell; solución de d'Alembert $f(z\mp ct)$; $c=1/\sqrt{\mu_0\varepsilon_0}$.
> 2. **[[Ondas Planas]]** — ondas planas monocromáticas; transversalidad, $\vec B=\hat k\times\vec E/c$, $E=cB$; energía e impedancia del vacío.
> 3. **[[5 Ondas Electromagneticas/Polarizacion | Polarización]]** — estado de polarización del campo $\vec E$: lineal, circular y elíptica.
> 4. **[[Ondas en Medios]]** — índice de refracción $n$; reflexión y refracción (Snell, Fresnel); ondas en conductores.

> [!corolario] Hacia la formulación covariante
> Que **todas** las ondas EM viajen a la misma $c$ —independiente del observador— es incompatible con la relatividad galileana y exige la **relatividad especial**. Reescribir Maxwell en lenguaje **tensorial** ($F^{\mu\nu}$) hace manifiesta esa invariancia: es el destino del curso ([[6 Formulacion Covariante/index | Formulación Covariante]], la parte que enlaza con Landau Vol. 2).

> [!referencia]
> Griffiths, *Introduction to Electrodynamics*, cap. 9 ("Electromagnetic Waves"). Para profundidad: Jackson, cap. 7; Landau-Lifshitz Vol. 2.
