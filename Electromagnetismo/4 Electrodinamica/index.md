---
title: Electrodinámica
order: 4
tags:
  - electromagnetismo
  - teoria
  - electrodinamica
  - indice
draft: false
aliases:
  - Electrodinámica
  - Ecuaciones de Maxwell
  - La unificación
---

# Electrodinámica $\nabla\times\vec E=-\partial_t\vec B,\quad \nabla\times\vec B=\mu_0\vec J+\mu_0\varepsilon_0\,\partial_t\vec E$

> [!definicion]
> La **electrodinámica** es el régimen en que los campos **varían en el tiempo**. Aquí las dos estáticas independientes —$\vec E$ y $\vec B$— se **acoplan** y dejan de poder estudiarse por separado. Dos términos nuevos producen el acoplamiento:
> $$\nabla\times\vec E=-\frac{\partial\vec B}{\partial t}\quad(\text{Faraday: }\partial_t\vec B\text{ genera }\vec E),$$
> $$\nabla\times\vec B=\mu_0\vec J+\mu_0\varepsilon_0\frac{\partial\vec E}{\partial t}\quad(\text{corriente de desplazamiento: }\partial_t\vec E\text{ genera }\vec B).$$
> Con ellos, las cuatro leyes se cierran en las **ecuaciones de Maxwell**, de las que salen las **ondas electromagnéticas**.

---

> [!info]
> **Capítulo 4 del curso Electromagnetismo: la unificación.** Reúne [[2 Electrostatica/index | Electrostática]] y [[3 Magnetostatica/index | Magnetostática]] añadiendo la dependencia temporal. Usa el rotacional, Stokes y las identidades de [[1 Calculo Vectorial/index | Cálculo Vectorial]]. **Referencia.** Griffiths, *Introduction to Electrodynamics*, caps. 7–8.

---

## La idea del capítulo

> [!teoria] Dos estáticas que se vuelven una dinámica
> En estática, $\nabla\times\vec E=0$ y $\nabla\times\vec B=\mu_0\vec J$: el campo eléctrico no sabe del magnético. Dos hechos lo cambian:
> - **Faraday** (experimental): un flujo magnético variable induce un campo eléctrico circulante, $\oint\vec E\cdot d\vec l=-d\Phi_B/dt$.
> - **Corriente de desplazamiento** (teórica, exigida por la conservación de la carga): Ampère $\nabla\times\vec B=\mu_0\vec J$ es **inconsistente** cuando $\partial_t\rho\neq0$; Maxwell añade $\mu_0\varepsilon_0\,\partial_t\vec E$ para repararla.
>
> ![[maxwell_acoplamiento.svg|460]]
> *El bucle de la unificación: $\partial_t\vec B$ crea $\vec E$ (Faraday) y $\partial_t\vec E$ crea $\vec B$ (Ampère–Maxwell). Cada campo regenera al otro: por eso una perturbación se autosostiene y viaja —es la luz.*

> [!teorema] La reparación de Ampère fuerza el término de Maxwell
> Tomando la divergencia de $\nabla\times\vec B=\mu_0\vec J$ se obtiene $\nabla\cdot\vec J=0$, falso si la carga varía. La continuidad **exacta** es $\nabla\cdot\vec J+\partial_t\rho=0$. Sustituyendo $\rho=\varepsilon_0\nabla\cdot\vec E$:
> $$\nabla\cdot\vec J+\frac{\partial}{\partial t}(\varepsilon_0\nabla\cdot\vec E)=0\ \Rightarrow\ \nabla\cdot\!\left(\vec J+\varepsilon_0\frac{\partial\vec E}{\partial t}\right)=0.$$
> La combinación $\vec J+\varepsilon_0\partial_t\vec E$ **sí** es solenoidal, así que es ella —y no $\vec J$ sola— la que debe ir en el rotacional de $\vec B$. Ese segundo término es la **corriente de desplazamiento** (ver [[Corriente de Desplazamiento]]).

> [!proposicion] Las cuatro ecuaciones de Maxwell (vacío)
> $$\nabla\cdot\vec E=\frac{\rho}{\varepsilon_0},\qquad \nabla\cdot\vec B=0,$$
> $$\nabla\times\vec E=-\frac{\partial\vec B}{\partial t},\qquad \nabla\times\vec B=\mu_0\vec J+\mu_0\varepsilon_0\frac{\partial\vec E}{\partial t}.$$
> Más la **fuerza de Lorentz** $\vec F=q(\vec E+\vec v\times\vec B)$, contienen toda la electrodinámica clásica. Detalle en [[Ecuaciones de Maxwell]].

---

## Mapa del capítulo

> [!algoritmo] Notas de esta sección
> 1. **[[Ley de Faraday]]** — $\nabla\times\vec E=-\partial_t\vec B$; fem inducida, ley de Lenz, fem de movimiento.
> 2. **[[Corriente de Desplazamiento]]** — por qué Ampère fallaba; $+\mu_0\varepsilon_0\,\partial_t\vec E$ desde la continuidad.
> 3. **[[Ecuaciones de Maxwell]]** — las cuatro, en forma integral y diferencial, en el vacío y en medios.
> 4. **[[Potenciales y Gauge]]** — $\vec E,\vec B$ desde $V,\vec A$; libertad de gauge; gauge de Lorenz y $\Box A=-\mu_0 J$.
> 5. **[[Energia y Momento]]** — vector de Poynting $\vec S=\vec E\times\vec B/\mu_0$; teorema de Poynting; momento del campo.

> [!corolario] Qué se desprende de aquí
> Las ecuaciones de Maxwell predicen que $\vec E$ y $\vec B$ satisfacen la **ecuación de ondas** con velocidad $c=1/\sqrt{\mu_0\varepsilon_0}$: la luz es un campo electromagnético ([[5 Ondas Electromagneticas/index | Ondas Electromagnéticas]]). Y su simetría —cuatro ecuaciones vectoriales con una velocidad invariante $c$— apunta directo a la **relatividad** y a su forma tensorial $F^{\mu\nu}$ ([[6 Formulacion Covariante/index | Formulación Covariante]]).

> [!referencia]
> Griffiths, *Introduction to Electrodynamics*, cap. 7 (Electrodinámica) y cap. 8 (Leyes de conservación). Para profundidad: Jackson, caps. 6–7.
