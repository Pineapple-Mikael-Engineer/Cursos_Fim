---
title: Formulación Covariante
tags:
  - electromagnetismo
  - teoria
  - covariante
  - relatividad
  - indice
draft: false
aliases:
  - Formulación covariante
  - Electromagnetismo relativista
  - Maxwell tensorial
---

# Formulación Covariante $\partial_\mu F^{\mu\nu}=\mu_0 J^\nu$

> [!definicion]
> La **formulación covariante** reescribe el electromagnetismo en el lenguaje de la **relatividad especial**, donde el espacio y el tiempo son un solo **espaciotiempo** de Minkowski. En ella, las cuatro ecuaciones de Maxwell colapsan en **dos** ecuaciones tensoriales,
> $$\partial_\mu F^{\mu\nu}=\mu_0 J^\nu\qquad\text{y}\qquad \partial_\mu(\!*F)^{\mu\nu}=0,$$
> y la invariancia de las leyes bajo cambios de observador inercial —la **covariancia de Lorentz**— se vuelve **manifiesta**: lo que para un observador es campo eléctrico, para otro es una mezcla de eléctrico y magnético. $\vec E$ y $\vec B$ son las componentes de un único objeto, el **tensor de campo** $F^{\mu\nu}$.

---

> [!info]
> **Capítulo 6 del curso Electromagnetismo: el pico tensorial.** Es la culminación del viaje **vectorial → tensorial**. No requiere mecánica analítica; sí, soltura con índices ([[Identidades Vectoriales]]) y las [[Ecuaciones de Maxwell]]. Es el puente directo a **Landau-Lifshitz Vol. 2** (*Teoría Clásica de Campos*).
> **Convenio.** Métrica $\eta_{\mu\nu}=\mathrm{diag}(+1,-1,-1,-1)$; índices griegos $0\!-\!3$, latinos $1\!-\!3$; convenio de suma de Einstein; unidades SI.
> **Referencia.** Griffiths cap. 12; Jackson cap. 11; Landau-Lifshitz Vol. 2.

---

## La idea del capítulo

> [!teoria] Maxwell ya era relativista
> La pista estaba en el capítulo 5: las ondas viajan a $c=1/\sqrt{\mu_0\varepsilon_0}$ **sin referencia a ningún observador**. Eso es incompatible con la suma galileana de velocidades y exige la relatividad especial: $c$ es la misma en todo marco inercial. Las transformaciones que dejan invariante el **intervalo**
> $$ds^2=c^2dt^2-d\vec x^{\,2}=\eta_{\mu\nu}\,dx^\mu dx^\nu$$
> son las de **Lorentz**. Magnitudes que se transforman como $x^\mu=(ct,\vec x)$ son **cuadrivectores**; con ellos, las leyes de Maxwell adoptan una forma que **todo** observador inercial ve idéntica.
>
> ![[cono_luz.svg|360]]
> *El espaciotiempo de Minkowski: el cono de luz separa futuro, pasado y región espacial. La métrica $\eta_{\mu\nu}$ —con su signo relativo entre tiempo y espacio— es la geometría que el electromagnetismo respeta.*

> [!proposicion] El diccionario covariante
> Todo el capítulo se construye sobre estos objetos:
> 
> | Objeto | Definición | Reúne |
> |:---|:---|:---|
> | Cuadriposición | $x^\mu=(ct,\vec x)$ | tiempo + espacio |
> | Cuadricorriente | $J^\mu=(c\rho,\vec J)$ | carga + corriente |
> | Cuadripotencial | $A^\mu=(V/c,\vec A)$ | potencial escalar + vector |
> | Tensor de campo | $F^{\mu\nu}=\partial^\mu A^\nu-\partial^\nu A^\mu$ | $\vec E$ + $\vec B$ |
> | Tensor energía-momento | $T^{\mu\nu}$ | energía + Poynting + esfuerzos |
>
> La conservación de la carga es $\partial_\mu J^\mu=0$; el gauge de Lorenz es $\partial_\mu A^\mu=0$; Maxwell es $\partial_\mu F^{\mu\nu}=\mu_0 J^\nu$. Cuatro ideas del curso, una línea cada una.

> [!teorema] Las cuatro ecuaciones en dos
> Con $F^{\mu\nu}$ antisimétrico que empaqueta $\vec E$ y $\vec B$, las **inhomogéneas** (Gauss eléctrico + Ampère–Maxwell) son $\partial_\mu F^{\mu\nu}=\mu_0 J^\nu$, y las **homogéneas** (Gauss magnético + Faraday) son la identidad de Bianchi $\partial_\mu(\!*F)^{\mu\nu}=0$ (equivalente a $\partial_\lambda F_{\mu\nu}+\partial_\mu F_{\nu\lambda}+\partial_\nu F_{\lambda\mu}=0$). Detalle en [[Maxwell Covariante]].

---

## Mapa del capítulo

> [!algoritmo] Notas de esta sección
> 1. **[[Cuadrivectores]]** — espaciotiempo, métrica $\eta_{\mu\nu}$, índices arriba/abajo; $x^\mu$, $J^\mu$, $A^\mu$; invariantes y transformaciones de Lorentz.
> 2. **[[Tensor de Campo]]** — $F^{\mu\nu}=\partial^\mu A^\nu-\partial^\nu A^\mu$; $\vec E$ y $\vec B$ como sus componentes; cómo un boost los mezcla; los invariantes $F_{\mu\nu}F^{\mu\nu}$ y $F_{\mu\nu}\tilde F^{\mu\nu}$.
> 3. **[[Maxwell Covariante]]** — $\partial_\mu F^{\mu\nu}=\mu_0 J^\nu$ y $\partial_\mu(\!*F)^{\mu\nu}=0$: las cuatro ecuaciones en dos; conservación de la carga y gauge.
> 4. **[[Tensor Energia-Momento]]** — $T^{\mu\nu}$ del campo; energía, momento (Poynting) y esfuerzos de Maxwell unificados; $\partial_\mu T^{\mu\nu}=-F^{\nu}{}_{\lambda}J^\lambda$.

> [!corolario] El final del viaje
> El curso recorrió **vectorial → unificación → tensorial**: del cálculo vectorial a Coulomb y Ampère, de ahí a Maxwell y las ondas, y por fin a la forma covariante donde la teoría revela su simetría más profunda. Desde aquí, el camino natural es **Landau-Lifshitz Vol. 2**: acción del campo, fuerza de Lorentz desde un principio variacional, y la puerta a la relatividad general y la teoría de campos.

> [!referencia]
> Griffiths, *Introduction to Electrodynamics*, cap. 12 ("Electrodynamics and Relativity"). Jackson, caps. 11–12. **Landau-Lifshitz, Vol. 2** (*Teoría Clásica de Campos*) — la referencia rectora de esta parte.
