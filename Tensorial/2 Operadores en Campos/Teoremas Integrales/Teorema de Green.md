---
title: Teorema de Green
tags:
  - analisis-tensorial
  - teoria
  - calculo-vectorial
  - teoremas-integrales
  - divergencia
draft: false
aliases:
  - identidades de Green
  - teorema de Green
  - Green's identities
  - Green theorem
---

# Teorema de Green

> [!definicion]
> Para dos campos escalares $u,v$ en un volumen $V$ encerrado por la superficie cerrada $S$, valen las dos **identidades de Green**:
> $$\textbf{1ª forma:}\quad \oint_S d\vec\sigma\cdot(u\vec\nabla v-v\vec\nabla u)=\int_V d\tau\,(u\nabla^2 v-v\nabla^2 u),$$
> $$\textbf{2ª forma:}\quad \oint_S d\vec\sigma\cdot(u\vec\nabla v)=\int_V d\tau\,(\vec\nabla u\cdot\vec\nabla v+u\nabla^2 v).$$
> Ambas se obtienen aplicando el [[Teorema de Gauss]] a un producto del tipo $u\vec\nabla v$.

> [!info]
> Es el *cap 2.5.2* del [[index | capítulo 2.5]] (Rogan & Muñoz). Se deriva **directamente** del [[Teorema de Gauss]] y de la identidad de la [[Operadores Diferenciales/Divergencia | divergencia]] de un producto escalar-vector. Aparece $\nabla^2=\vec\nabla\cdot\vec\nabla$, el [[Operadores Diferenciales/Identidades Operadores | laplaciano]]. Es la herramienta central de los problemas de potencial y la base de la unicidad en el [[Teorema de Helmholtz]].

---

## Ejemplo

> [!ejemplo]
> **Unicidad de la ecuación de Laplace.** Sean $u_1,u_2$ dos soluciones de $\nabla^2 u=0$ en $V$ con el mismo valor en la frontera ($u_1=u_2$ sobre $S$). Su diferencia $w=u_1-u_2$ cumple $\nabla^2 w=0$ en $V$ y $w=0$ sobre $S$.
>
> Aplicamos la **2ª forma** con $u=v=w$:
> $$\oint_S d\vec\sigma\cdot(w\vec\nabla w)=\int_V d\tau\,\big(\vec\nabla w\cdot\vec\nabla w+w\,\nabla^2 w\big).$$
> El término de superficie se anula porque $w=0$ sobre $S$; el segundo término del volumen se anula porque $\nabla^2 w=0$. Queda
> $$0=\int_V d\tau\,|\vec\nabla w|^2.$$
> Como $|\vec\nabla w|^2\ge0$, debe ser $\vec\nabla w=0$, es decir $w=$ cte; y como $w=0$ en $S$, esa constante es cero. Por tanto $u_1=u_2$: **la solución de Laplace con dato en la frontera es única.**

---

## Demostración

> [!teorema]
> $$\oint_S d\vec\sigma\cdot(u\vec\nabla v-v\vec\nabla u)=\int_V d\tau\,(u\nabla^2 v-v\nabla^2 u),\qquad \oint_S d\vec\sigma\cdot(u\vec\nabla v)=\int_V d\tau\,(\vec\nabla u\cdot\vec\nabla v+u\nabla^2 v).$$

> [!demostracion]
> **Paso 1 — Identidad del producto.** Partimos de la divergencia de $u\vec\nabla v$. Por la regla del producto del operador,
> $$\vec\nabla\cdot(u\vec\nabla v)=\vec\nabla u\cdot\vec\nabla v+u\,\nabla^2 v,$$
> ya que $\vec\nabla\cdot\vec\nabla v=\nabla^2 v$.
>
> **Paso 2 — Intercambiar $u\leftrightarrow v$.** Escribiendo la misma identidad con los papeles cambiados,
> $$\vec\nabla\cdot(v\vec\nabla u)=\vec\nabla v\cdot\vec\nabla u+v\,\nabla^2 u.$$
>
> **Paso 3 — Restar.** El término $\vec\nabla u\cdot\vec\nabla v=\vec\nabla v\cdot\vec\nabla u$ es común y se cancela al restar:
> $$\vec\nabla\cdot(u\vec\nabla v-v\vec\nabla u)=u\,\nabla^2 v-v\,\nabla^2 u.$$
>
> **Paso 4 — Integrar y aplicar Gauss (1ª forma).** Integramos sobre $V$ y usamos el [[Teorema de Gauss]] en el lado izquierdo, $\int_V d\tau\,\vec\nabla\cdot(\,\cdot\,)=\oint_S d\vec\sigma\cdot(\,\cdot\,)$:
> $$\oint_S d\vec\sigma\cdot(u\vec\nabla v-v\vec\nabla u)=\int_V d\tau\,(u\nabla^2 v-v\nabla^2 u).$$
> Esta es la **primera forma** del teorema de Green.
>
> **Paso 5 — Gauss directo (2ª forma).** Aplicando el teorema de Gauss directamente a la identidad del Paso 1, sin restar,
> $$\oint_S d\vec\sigma\cdot(u\vec\nabla v)=\int_V d\tau\,\vec\nabla\cdot(u\vec\nabla v)=\int_V d\tau\,(\vec\nabla u\cdot\vec\nabla v+u\nabla^2 v).$$
> Esta es la **segunda forma**.$\qquad\blacksquare$

> [!info] Casos particulares
> | Elección | 2ª forma se reduce a |
> |---|---|
> | $v=u$ | $\oint_S d\vec\sigma\cdot(u\vec\nabla u)=\int_V d\tau\,(\|\vec\nabla u\|^2+u\nabla^2 u)$ |
> | $u=1$ | $\oint_S d\vec\sigma\cdot\vec\nabla v=\int_V d\tau\,\nabla^2 v$ (Gauss para $\vec\nabla v$) |
> | $v$ armónico ($\nabla^2 v=0$) | $\oint_S d\vec\sigma\cdot(u\vec\nabla v)=\int_V d\tau\,\vec\nabla u\cdot\vec\nabla v$ |

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | 1ª forma | $\oint_S d\vec\sigma\cdot(u\vec\nabla v-v\vec\nabla u)=\int_V d\tau\,(u\nabla^2 v-v\nabla^2 u)$ |
> | 2ª forma | $\oint_S d\vec\sigma\cdot(u\vec\nabla v)=\int_V d\tau\,(\vec\nabla u\cdot\vec\nabla v+u\nabla^2 v)$ |
> | Origen | identidad $\vec\nabla\cdot(u\vec\nabla v)=\vec\nabla u\cdot\vec\nabla v+u\nabla^2 v$ + [[Teorema de Gauss]] |
> | Uso típico | unicidad de Laplace/Poisson; demostración de Helmholtz |

> [!corolario]
> Green traduce integrales del laplaciano en el volumen a integrales sobre la frontera. Es Gauss aplicado a $u\vec\nabla v$, y su 2ª forma con $u=v=\Phi$ es el paso decisivo en la prueba del [[Teorema de Helmholtz]].

> [!referencia]
> - Teorema del que deriva: [[Teorema de Gauss]].
> - Laplaciano $\nabla^2$: [[Operadores Diferenciales/Identidades Operadores]].
> - Aplicación a unicidad de campos: [[Teorema de Helmholtz]].
