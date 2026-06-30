---
title: Ecuaciones Integrales Singulares
order: 6
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - singulares
  - index
draft: false
aliases:
  - ecuaciones integrales singulares
  - singular integral equations
---

# Ecuaciones Integrales Singulares

> [!definicion]
> Una ecuación integral es **singular** cuando su núcleo se vuelve **infinito** (no acotado) en el dominio —típicamente sobre la diagonal $t=x$— o el dominio es **no acotado**. Según la fuerza de la singularidad del núcleo $\sim 1/(x-t)^{\alpha}$:
> - **Débilmente singular** ($0<\alpha<1$): la integral aún **converge** ([[Problema de Abel| Abel]]).
> - **Singular de Cauchy** ($\alpha=1$): hay que interpretarla como **valor principal**.
> - **Hipersingular** ($\alpha>1$): requiere parte finita de Hadamard.

> [!info]
> Sección de los casos **fuera del marco clásico** del [[3 Ecuaciones Integrales/index| capítulo]]: los métodos de [[Fredholm/index| Fredholm]] (núcleo continuo) ya no aplican. Cada tipo tiene su herramienta: inversión de [[Problema de Abel| Abel]] / cálculo fraccionario para las débiles, el **problema de Riemann-Hilbert** para las de Cauchy, y la **técnica de Wiener-Hopf** para dominios semiinfinitos.

---

## Ejemplo

> [!ejemplo] La fuerza de la singularidad
> ![[nucleos_singulares.svg|470]]
>
> Los núcleos $1/(x-t)^{\alpha}$ cerca de $t=x$: para $\alpha=\tfrac12$ (débil) el área bajo el pico es **finita** y la ecuación de [[Problema de Abel| Abel]] tiene sentido como integral ordinaria; para $\alpha=1$ (Cauchy) la integral **diverge** y solo cobra sentido como **valor principal** $\operatorname{vp}\!\int\frac{\varphi(t)}{t-x}\,dt$; para $\alpha>1$ ni siquiera eso basta. La **fuerza** del pico decide qué teoría se necesita.

---

## En qué consiste

> [!teoria]
> La singularidad cambia la naturaleza del operador. Un núcleo continuo da un operador **compacto** (suaviza, espectro discreto → Fredholm). Un núcleo singular de Cauchy da un operador **acotado pero no compacto** cuyo "espectro" es un **continuo**: por eso la teoría es distinta y se apoya en el análisis complejo (funciones analíticas, saltos de Plemelj). Tres caminos:
> 1. **Débilmente singular** → tratar como [[Problema de Abel| Abel]]/convolución; invertir con [[Calculo Fraccionario/index| derivadas fraccionarias]].
> 2. **Cauchy** → [[Nucleo de Cauchy y Riemann-Hilbert| problema de Riemann-Hilbert]]: convertir la ecuación en un problema de contorno para una función analítica y **factorizar**.
> 3. **Dominio semiinfinito** (convolución en $[0,\infty)$) → [[Metodo de Wiener-Hopf| Wiener-Hopf]]: factorizar en el plano complejo según semiplanos de analiticidad.

> [!info] Recorrido de la sección
> | Nota | Aporte |
> |---|---|
> | [[Ecuacion de Abel Generalizada\|Abel Generalizada]] | núcleo $1/(x-t)^\alpha$; cálculo fraccionario |
> | [[Nucleo de Cauchy y Riemann-Hilbert\|Cauchy y Riemann-Hilbert]] | valor principal; Plemelj; factorización |
> | [[Metodo de Wiener-Hopf\|Método de Wiener-Hopf]] | convolución semiinfinita; factorización ± |

## Resumen

> [!resumen]
> | Singularidad | Núcleo | Método |
> |---|---|---|
> | Débil ($0<\alpha<1$) | $1/(x-t)^\alpha$ | Abel / cálculo fraccionario |
> | Cauchy ($\alpha=1$) | $1/(t-x)$ (vp) | Riemann-Hilbert (análisis complejo) |
> | Dominio $[0,\infty)$ | convolución $K(x-t)$ | Wiener-Hopf (factorización) |

> [!corolario]
> La singularidad del núcleo marca la frontera entre la teoría de Fredholm (compacta, espectro discreto) y un mundo gobernado por el **análisis complejo**: saltos de funciones analíticas y factorizaciones. La **fuerza** del pico —el exponente $\alpha$— decide qué herramienta hace falta.

> [!referencia]
> - El caso integrable: [[Ecuacion de Abel Generalizada]].
> - El salto de Cauchy: [[Nucleo de Cauchy y Riemann-Hilbert]].
> - El dominio semiinfinito: [[Metodo de Wiener-Hopf]].
