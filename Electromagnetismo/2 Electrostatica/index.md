---
title: Electrostática
order: 2
tags:
  - electromagnetismo
  - teoria
  - electrostatica
  - indice
draft: false
aliases:
  - Electrostática
  - Campos de cargas en reposo
---

# Electrostática $\nabla\cdot\vec E=\dfrac{\rho}{\varepsilon_0},\quad \nabla\times\vec E=\vec 0$

> [!definicion]
> La **electrostática** estudia el campo eléctrico $\vec E$ producido por **cargas en reposo** (densidades $\rho$ independientes del tiempo). Todo el capítulo se resume en dos ecuaciones —las dos primeras de Maxwell en el caso estático—:
> $$\nabla\cdot\vec E=\frac{\rho}{\varepsilon_0}\qquad(\text{Gauss: la carga es fuente de }\vec E),$$
> $$\nabla\times\vec E=\vec 0\qquad(\vec E\text{ es conservativo: existe el potencial }V).$$
> De la primera sale la **ley de Gauss**; de la segunda, el **potencial** $\vec E=-\nabla V$ y la **ecuación de Poisson** $\nabla^2 V=-\rho/\varepsilon_0$.

---

> [!info]
> **Capítulo 2 del curso Electromagnetismo.** Usa íntegramente las herramientas de [[1 Calculo Vectorial/index | Cálculo Vectorial]]: la divergencia y el teorema de Gauss, el rotacional y Stokes, el gradiente, y la delta $\nabla\cdot(\hat r/r^2)=4\pi\,\delta^3(\vec r)$ que convierte Coulomb en $\nabla\cdot\vec E=\rho/\varepsilon_0$. **Referencia.** Griffiths, *Introduction to Electrodynamics*, caps. 2–4. Unidades SI; constante $k=\dfrac{1}{4\pi\varepsilon_0}$.

---

## La idea del capítulo

> [!teoria] De Coulomb a Maxwell estático, y de vuelta
> El punto de partida experimental es la **ley de Coulomb**: la fuerza entre dos cargas. De ella se define el **campo** $\vec E$ y, por superposición, el campo de cualquier distribución. Pero integrar la ley de Coulomb es costoso; el avance conceptual es traducirla a **ecuaciones diferenciales locales** (las dos de arriba) y resolverlas con la simetría del problema:
>
> $$\vec F=\frac{1}{4\pi\varepsilon_0}\frac{q\,q'}{r^2}\,\hat r\ \xrightarrow{\ \vec E=\vec F/q'\ }\ \vec E(\vec r)=\frac{1}{4\pi\varepsilon_0}\int\frac{\rho(\vec r\,')\,\hat{\mathscr r}}{\mathscr r^2}\,d^3r'\ \xrightarrow{\ \nabla\cdot\ }\ \nabla\cdot\vec E=\frac{\rho}{\varepsilon_0}.$$
>
> ![[campo_cargas.svg|460]]
> *El objeto central: el campo $\vec E$ de una carga puntual (radial) y de un dipolo. Toda distribución se construye superponiendo estos campos.*

> [!teorema] Las dos estrategias de cálculo
> Hay dos caminos para hallar $\vec E$, y el capítulo enseña ambos:
> 1. **Ley de Gauss** (cuando hay simetría): $\displaystyle\oint_S\vec E\cdot d\vec A=\frac{Q_{\text{enc}}}{\varepsilon_0}$ da $\vec E$ de inmediato en casos esférico, cilíndrico y plano. Es la forma integral de $\nabla\cdot\vec E=\rho/\varepsilon_0$.
> 2. **Vía potencial** (caso general): como $\nabla\times\vec E=0$, existe $V$ con $\vec E=-\nabla V$; se calcula el **escalar** $V=\dfrac{1}{4\pi\varepsilon_0}\displaystyle\int\dfrac{\rho}{\mathscr r}\,d^3r'$ (una integral, no tres) y se deriva. Si no se conoce $\rho$ en toda la región, se resuelve la **ecuación de Poisson/Laplace** con condiciones de frontera.

> [!proposicion] Estructura lógica del capítulo
> $$\underbrace{\text{Coulomb}}_{\text{experimento}}\ \to\ \underbrace{\vec E,\ \text{Gauss}}_{\text{campo y flujo}}\ \to\ \underbrace{V,\ \text{Poisson/Laplace}}_{\text{potencial}}\ \to\ \underbrace{W=\tfrac12\varepsilon_0\!\int E^2dV}_{\text{energía}}\ \to\ \underbrace{\text{conductores},\ \text{dieléctricos}}_{\text{la materia}}$$
> Las dos últimas etapas introducen la **respuesta de la materia**: los conductores ($\vec E=0$ dentro, carga en la superficie) y los dieléctricos (polarización $\vec P$, desplazamiento $\vec D$).

---

## Mapa del capítulo

> [!algoritmo] Notas de esta sección
> 1. **[[Ley de Coulomb y Campo Electrico]]** — fuerza entre cargas, definición de $\vec E$, campo de distribuciones por superposición, líneas de campo.
> 2. **[[Ley de Gauss]]** — $\oint\vec E\cdot d\vec A=Q_{\text{enc}}/\varepsilon_0$ y $\nabla\cdot\vec E=\rho/\varepsilon_0$; cálculo de $\vec E$ con simetría esférica, cilíndrica y plana.
> 3. **[[Potencial Electrico]]** — $\vec E=-\nabla V$, $V=\frac{1}{4\pi\varepsilon_0}\int\rho/\mathscr r\,d^3r'$; circulación nula; superficies equipotenciales.
> 4. **[[Poisson y Laplace]]** — $\nabla^2V=-\rho/\varepsilon_0$; ecuación de Laplace, teorema de unicidad y método de imágenes.
> 5. **[[Energia Electrostatica]]** — energía de una distribución; densidad $u=\tfrac12\varepsilon_0E^2$; energía en el campo.
> 6. **[[Conductores]]** — $\vec E=0$ dentro, equipotencial, carga superficial $\sigma=\varepsilon_0 E_\perp$; cavidades y apantallamiento.
> 7. **[[2 Electrostatica/Dielectricos/index | Dieléctricos]]** — respuesta de la materia: polarización $\vec P$, cargas ligadas y el campo de desplazamiento $\vec D$.

> [!corolario] Qué llevarse a Magnetostática
> La electrostática fija el patrón que el capítulo 3 repetirá con corrientes: una **ley de fuerza** (Coulomb $\to$ Lorentz/Biot–Savart), una **ley de flujo/circulación** (Gauss $\to$ Ampère) y un **potencial** ($V\to\vec A$). Reconocer este paralelismo es la mitad de aprender magnetostática.

> [!referencia]
> Griffiths, *Introduction to Electrodynamics*, caps. 2 (Electrostática), 3 (Potenciales y técnicas) y 4 (Campos en la materia). Para profundidad: Jackson, caps. 1–4.
