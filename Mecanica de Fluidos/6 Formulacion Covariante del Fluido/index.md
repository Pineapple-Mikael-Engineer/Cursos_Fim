---
title: Formulación Covariante del Fluido
order: 6
tags:
  - fluidos
  - teoria
  - covariante
  - relatividad
  - indice
draft: false
aliases:
  - Formulación covariante del fluido
  - Hidrodinámica relativista
  - Tensor energía-momento del fluido
---

# Formulación Covariante del Fluido $\partial_\mu T^{\mu\nu}=0$

> [!definicion]
> La **formulación covariante** reescribe la dinámica de fluidos en el lenguaje del **espaciotiempo** de Minkowski, válido cuando las velocidades se acercan a $c$ (chorros relativistas, estrellas de neutrones, el universo temprano). Toda la conservación de masa, momento y energía se condensa en **dos** ecuaciones tensoriales:
> $$\partial_\mu(n\,u^\mu)=0\quad(\text{número de partículas}),\qquad \partial_\mu T^{\mu\nu}=0\quad(\text{energía--momento}),$$
> con el **tensor energía-momento del fluido perfecto** $T^{\mu\nu}=(\varepsilon+p)\,\dfrac{u^\mu u^\nu}{c^2}-p\,\eta^{\mu\nu}$. De $\partial_\mu T^{\mu\nu}=0$ salen, por proyección, la **continuidad** y el **Euler relativistas**.

---

> [!info]
> **Capítulo 6 del curso Mecánica de Fluidos: el pico tensorial.** Es la culminación del viaje **vectorial → tensorial**, gemelo de la [[6 Formulacion Covariante/index | Formulación Covariante del electromagnetismo]]. Reúne la conservación del [[3 Ecuaciones de Conservacion/index | Capítulo 3]] en un solo objeto, $T^{\mu\nu}$. Es el puente a **Landau-Lifshitz Vol. 6** (§§133–134) y, más allá, a la relatividad general. **Convenio.** Métrica $\eta_{\mu\nu}=\mathrm{diag}(+1,-1,-1,-1)$; cuadrivelocidad $u^\mu=\gamma(c,\vec v)$ con $u_\mu u^\mu=c^2$; índices griegos $0\!-\!3$, latinos $1\!-\!3$; suma de Einstein.

---

## La idea del capítulo

> [!teoria] De la compresibilidad a la relatividad
> El puente entre la mecánica de fluidos clásica y la covariante pasa por la **energía** y la **compresibilidad**: cuando el flujo es rápido (número de Mach $\mathrm{Ma}=U/c_s$ no pequeño), la densidad varía, aparecen **ondas de sonido** y **ondas de choque**, y la energía deja de desacoplarse. Llevado al extremo $U\to c$, la descripción correcta es la **relativista**, donde masa y energía son lo mismo y el objeto natural es el tensor $T^{\mu\nu}$.
>
> ![[tensor_T_fluido.svg|460]]
> *El tensor energía-momento del fluido perfecto. En el marco en reposo es $\mathrm{diag}(\varepsilon,p,p,p)$: la densidad de energía $\varepsilon$ y la presión isótropa $p$. Toda la dinámica está en $\partial_\mu T^{\mu\nu}=0$.*

> [!proposicion] El diccionario covariante del fluido
> | Objeto | Definición | Reúne |
> |:---|:---|:---|
> | Cuadrivelocidad | $u^\mu=\gamma(c,\vec v)$, $u_\mu u^\mu=c^2$ | tiempo propio + movimiento |
> | Cuadricorriente de partículas | $N^\mu=n\,u^\mu$ | densidad + flujo de partículas |
> | Tensor energía-momento | $T^{\mu\nu}=(\varepsilon+p)\dfrac{u^\mu u^\nu}{c^2}-p\,\eta^{\mu\nu}$ | energía + momento + presión |
> | Conservación | $\partial_\mu N^\mu=0$, $\partial_\mu T^{\mu\nu}=0$ | continuidad + Euler |

> [!teorema] Dos ecuaciones que contienen toda la dinámica
> Proyectando $\partial_\mu T^{\mu\nu}=0$ **a lo largo** de $u_\nu$ se obtiene la conservación de la energía; proyectándola **perpendicular** a $u$ (con el proyector $h^{\mu\nu}=\eta^{\mu\nu}-u^\mu u^\nu/c^2$) se obtiene el **Euler relativista**. En el límite $v\ll c$ se recuperan exactamente la continuidad y la ecuación de Euler clásicas del [[4 Flujo Ideal/index | Capítulo 4]]. Es el mismo patrón que en electromagnetismo: cuatro ecuaciones vectoriales colapsan en dos tensoriales.

---

## Mapa del capítulo

> [!algoritmo] Notas de esta sección
> 1. **[[Flujo Compresible y Ondas de Choque]]** — el puente clásico: velocidad del sonido $c_s$, número de Mach, cono de Mach y saltos de Rankine–Hugoniot.
> 2. **[[Tensor Energia-Momento del Fluido]]** — $T^{\mu\nu}=(\varepsilon+p)u^\mu u^\nu/c^2-p\,\eta^{\mu\nu}$; sus componentes; el marco en reposo $\mathrm{diag}(\varepsilon,p,p,p)$.
> 3. **[[Hidrodinamica Relativista]]** — $\partial_\mu T^{\mu\nu}=0$ proyectado da continuidad y Euler relativistas; el límite no relativista.

> [!corolario] El final del viaje
> El curso recorrió **vectorial → Navier–Stokes → tensorial**: de la cinemática y el tensor de esfuerzos a las ecuaciones de Navier–Stokes, de ahí a los flujos ideal y viscoso, y por fin a la forma covariante donde la conservación se vuelve $\partial_\mu T^{\mu\nu}=0$. Desde aquí, el camino natural es **Landau-Lifshitz Vol. 6** (hidrodinámica relativista) y la relatividad general —donde $T^{\mu\nu}$ del fluido es la **fuente** del campo gravitatorio (cosmología, estrellas de neutrones)—.

> [!referencia]
> Landau-Lifshitz, Vol. 6, §§133–134 ("Hidrodinámica relativista"); Vol. 2 (*Teoría Clásica de Campos*) para el aparato tensorial. Weinberg, *Gravitation and Cosmology*, cap. 2, para $T^{\mu\nu}$ del fluido perfecto.
