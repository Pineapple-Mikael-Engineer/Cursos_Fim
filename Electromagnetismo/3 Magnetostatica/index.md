---
title: Magnetostática
order: 3
tags:
  - electromagnetismo
  - teoria
  - magnetostatica
  - indice
draft: false
aliases:
  - Magnetostática
  - Campos de corrientes estacionarias
---

# Magnetostática $\nabla\cdot\vec B=0,\quad \nabla\times\vec B=\mu_0\vec J$

> [!definicion]
> La **magnetostática** estudia el campo magnético $\vec B$ producido por **corrientes estacionarias** ($\vec J$ independiente del tiempo, con $\nabla\cdot\vec J=0$). Se resume en dos ecuaciones —las otras dos de Maxwell en el caso estático—:
> $$\nabla\cdot\vec B=0\qquad(\text{no hay monopolos magnéticos: }\vec B\text{ es solenoidal}),$$
> $$\nabla\times\vec B=\mu_0\vec J\qquad(\text{Ampère: la corriente es la fuente de circulación de }\vec B).$$
> De la primera sale el **potencial vector** $\vec B=\nabla\times\vec A$; de la segunda, la **ley de Ampère** $\oint\vec B\cdot d\vec l=\mu_0 I_{\text{enc}}$.

---

> [!info]
> **Capítulo 3 del curso Electromagnetismo.** Reutiliza toda la maquinaria de [[1 Calculo Vectorial/index | Cálculo Vectorial]] (rotacional, Stokes, divergencia) y corre **en paralelo** con [[2 Electrostatica/index | Electrostática]]. Constante magnética $\mu_0$ (permeabilidad del vacío); $c=1/\sqrt{\mu_0\varepsilon_0}$. **Referencia.** Griffiths, *Introduction to Electrodynamics*, cap. 5.

---

## La idea del capítulo

> [!teoria] El paralelo con la electrostática (y sus diferencias)
> La magnetostática repite el patrón del capítulo 2, con una **ley de fuerza**, una **ley de fuente** y un **potencial**, pero con dos diferencias esenciales: el campo $\vec B$ ejerce una fuerza que **no realiza trabajo** ($\perp$ a $\vec v$), y **no existe carga magnética** (las líneas de $\vec B$ se cierran sobre sí mismas).
>
> | | Electrostática | Magnetostática |
> |:---|:---|:---|
> | Fuente | carga $\rho$ | corriente $\vec J$ |
> | Ley de fuerza | $\vec F=q\vec E$ | $\vec F=q\,\vec v\times\vec B$ (Lorentz) |
> | Ley integral | Coulomb / Gauss | Biot–Savart / Ampère |
> | Divergencia | $\nabla\cdot\vec E=\rho/\varepsilon_0$ | $\nabla\cdot\vec B=0$ |
> | Rotacional | $\nabla\times\vec E=0$ | $\nabla\times\vec B=\mu_0\vec J$ |
> | Potencial | escalar $V$, $\vec E=-\nabla V$ | vector $\vec A$, $\vec B=\nabla\times\vec A$ |
>
> ![[campo_hilo.svg|360]]
> *Las líneas de $\vec B$ de un hilo se cierran en círculos: no nacen ni mueren en ninguna parte. Eso es $\nabla\cdot\vec B=0$ —no hay monopolos magnéticos—, el contraste clave con $\vec E$.*

> [!teorema] Por qué las corrientes deben ser estacionarias
> La consistencia de Ampère exige $\nabla\cdot\vec J=0$. En efecto, tomando la divergencia de $\nabla\times\vec B=\mu_0\vec J$ y usando que $\nabla\cdot(\nabla\times\vec B)=0$ ([[Identidades Vectoriales]]):
> $$0=\nabla\cdot(\nabla\times\vec B)=\mu_0\,\nabla\cdot\vec J\ \Rightarrow\ \nabla\cdot\vec J=0.$$
> Esta es la **ecuación de continuidad estacionaria** (la carga no se acumula). Cuando deje de cumplirse —cargas variables en el tiempo— habrá que añadir la **corriente de desplazamiento**, y ahí nace la electrodinámica ([[4 Electrodinamica/index | Electrodinámica]]).

> [!proposicion] Las dos estrategias de cálculo
> Igual que en electrostática, hay dos caminos para hallar $\vec B$:
> 1. **Ley de Ampère** (con simetría): $\displaystyle\oint_C\vec B\cdot d\vec l=\mu_0 I_{\text{enc}}$ da $\vec B$ de inmediato en hilo, solenoide y toroide. Es la forma integral de $\nabla\times\vec B=\mu_0\vec J$.
> 2. **Vía Biot–Savart / potencial vector** (caso general): $\vec B=\dfrac{\mu_0}{4\pi}\displaystyle\int\dfrac{\vec J\times\hat{\mathscr r}}{\mathscr r^2}\,d^3r'$, o bien el potencial $\vec A=\dfrac{\mu_0}{4\pi}\displaystyle\int\dfrac{\vec J}{\mathscr r}\,d^3r'$ (que cumple $\nabla^2\vec A=-\mu_0\vec J$, tres ecuaciones de Poisson).

---

## Mapa del capítulo

> [!algoritmo] Notas de esta sección
> 1. **[[Fuerza de Lorentz]]** — $\vec F=q(\vec E+\vec v\times\vec B)$; fuerza sobre corrientes $\vec F=I\vec L\times\vec B$; el campo no trabaja; movimiento ciclotrónico.
> 2. **[[Ley de Biot-Savart]]** — campo de una corriente $\vec B=\frac{\mu_0}{4\pi}\int\frac{\vec J\times\hat{\mathscr r}}{\mathscr r^2}d^3r'$; hilo, espira en el eje.
> 3. **[[Ley de Ampere]]** — $\oint\vec B\cdot d\vec l=\mu_0 I_{\text{enc}}$ y $\nabla\times\vec B=\mu_0\vec J$; hilo, solenoide y toroide por simetría.
> 4. **[[Potencial Vector]]** — $\vec B=\nabla\times\vec A$; gauge de Coulomb $\nabla\cdot\vec A=0$; $\nabla^2\vec A=-\mu_0\vec J$.
> 5. **[[Materiales Magneticos]]** — magnetización $\vec M$; corrientes ligadas $\vec J_b=\nabla\times\vec M$, $\vec K_b=\vec M\times\hat n$; campo auxiliar $\vec H=\vec B/\mu_0-\vec M$, $\nabla\times\vec H=\vec J_{\text{libre}}$.

> [!corolario] Qué prepara este capítulo
> Con $\vec E$ (cap. 2) y $\vec B$ (cap. 3) descritos por sus cuatro ecuaciones estáticas, solo falta **acoplarlos**: permitir que los campos varíen en el tiempo. Faraday ligará $\nabla\times\vec E$ a $\partial_t\vec B$, y la corriente de desplazamiento ligará $\nabla\times\vec B$ a $\partial_t\vec E$. Ese acoplamiento son las **ecuaciones de Maxwell** completas ([[4 Electrodinamica/index | Electrodinámica]]).

> [!referencia]
> Griffiths, *Introduction to Electrodynamics*, cap. 5 ("Magnetostatics"). Para profundidad: Jackson, cap. 5.
