---
title: Teorema de Helmholtz
tags:
  - analisis-tensorial
  - teoria
  - calculo-vectorial
  - teoremas-integrales
  - helmholtz
draft: false
aliases:
  - teorema de Helmholtz
  - descomposicion de Helmholtz
  - parte solenoidal e irrotacional
  - Helmholtz theorem
  - Helmholtz decomposition
---

# Teorema de Helmholtz

> [!definicion]
> Un campo vectorial, si existe, queda determinado de forma **única** por su **divergencia** y su **rotor** en cada punto de una región, más su **componente normal** en la superficie cerrada que la rodea.

> [!info]
> Es el *cap 2.5.4* del [[index | capítulo 2.5]] (Rogan & Muñoz); el libro lo destaca por no estar bien cubierto en otros textos. Su prueba de unicidad descansa en la 2ª forma del [[Teorema de Green]] (con $u=v=\Phi$) y en que un campo irrotacional deriva de un potencial ([[Teorema de Stokes]]). Lleva a la **descomposición de Helmholtz** en parte solenoidal e irrotacional, apoyada en las identidades $\vec\nabla\cdot(\vec\nabla\times\vec A)=0$ y $\vec\nabla\times\vec\nabla\Phi=0$ de las [[Operadores Diferenciales/Identidades Operadores | identidades de operadores]].

---

## Ejemplo

> [!ejemplo]
> **Identificar las dos partes en un campo dado.** Sea
> $$\vec v=\underbrace{(-y,\,x,\,0)}_{\text{rotacional}}+\underbrace{(x,\,y,\,z)}_{\text{con fuente}}.$$
> Calculamos sus invariantes:
> $$\vec\nabla\cdot\vec v=0+0+0\;+\;(1+1+1)=3,\qquad \vec\nabla\times\vec v=2\,\hat e_z+\vec 0=2\,\hat e_z.$$
> La **parte solenoidal** (divergencia nula, $\vec\nabla\times\vec A$) carga el rotor $2\hat e_z$, mientras que la **parte irrotacional** ($-\vec\nabla\Phi$, rotor nulo) carga la divergencia $3$. Tomando $\Phi=-\tfrac12(x^2+y^2+z^2)$ se reproduce $-\vec\nabla\Phi=(x,y,z)$ con $\nabla^2\Phi=-3$, consistente con $\vec\nabla\cdot\vec v=-\nabla^2\Phi=3$.
>
> Físicamente: en el electromagnetismo, $\vec B$ es puramente solenoidal ($\vec\nabla\cdot\vec B=0$, $\vec B=\vec\nabla\times\vec A$) y el campo electrostático es puramente irrotacional ($\vec\nabla\times\vec E=0$, $\vec E=-\vec\nabla\Phi$).

---

## Demostración (unicidad)

> [!teorema]
> Si dos campos $\vec v_1,\vec v_2$ tienen la misma divergencia, el mismo rotor en la región y la misma componente normal en la frontera, entonces $\vec v_1=\vec v_2$.

> [!demostracion]
> **Paso 1 — Campo diferencia.** Supongamos dos campos $\vec v_1,\vec v_2$ con idénticos $\vec\nabla\cdot\,$, $\vec\nabla\times\,$ y componente normal. Como estos operadores son **lineales**, su diferencia $\vec w=\vec v_1-\vec v_2$ cumple
> $$\vec\nabla\cdot\vec w=0\ \text{en la región},\qquad \vec\nabla\times\vec w=0\ \text{en la región},\qquad \hat n\cdot\vec w=0\ \text{en la superficie}.$$
>
> **Paso 2 — Potencial de $\vec w$.** Como $\vec\nabla\times\vec w=0$, por la consecuencia del [[Teorema de Stokes]] el campo deriva de un potencial escalar,
> $$\vec w=-\vec\nabla\Phi.$$
>
> **Paso 3 — Segunda forma de Green con $u=v=\Phi$.** La 2ª forma del [[Teorema de Green]],
> $$\oint_S d\vec\sigma\cdot(u\vec\nabla v)=\int_V d\tau\,(\vec\nabla u\cdot\vec\nabla v+u\nabla^2 v),$$
> con $u=v=\Phi$ y usando $\vec\nabla\Phi=-\vec w$, se escribe
> $$\oint_S d\vec\sigma\cdot\big(\Phi\vec\nabla\Phi\big)=\int_V d\tau\,\big(\vec\nabla\Phi\cdot\vec\nabla\Phi+\Phi\nabla^2\Phi\big),$$
> es decir, reemplazando $\vec\nabla\Phi=-\vec w$ y $\nabla^2\Phi=-\vec\nabla\cdot\vec w$,
> $$\oint_S d\vec\sigma\cdot(\Phi\vec w)=\int_V d\tau\,\big(\Phi\,\vec\nabla\cdot\vec w-\vec w\cdot\vec w\big).$$
>
> **Paso 4 — Anular los tres términos.** Examinamos cada uno:
> - La integral de superficie $\oint_S d\vec\sigma\cdot(\Phi\vec w)=\oint_S \Phi\,(\hat n\cdot\vec w)\,d\sigma=0$, porque $\hat n\cdot\vec w=0$ en $S$.
> - El término $\int_V d\tau\,\Phi\,\vec\nabla\cdot\vec w=0$, porque $\vec\nabla\cdot\vec w=0$ en la región.
>
> Solo sobrevive el último,
> $$\int_V d\tau\,\vec w\cdot\vec w=\int_V d\tau\,|\vec w|^2=0.$$
>
> **Paso 5 — Conclusión.** Como $|\vec w|^2\ge0$, la única forma de que su integral se anule es $\vec w=0$ en todo el volumen. Por tanto
> $$\vec v_1=\vec v_2.\qquad\blacksquare$$

---

## Descomposición de Helmholtz

> [!proposicion]
> Todo campo vectorial se separa en una parte **solenoidal** (rotacional, sin divergencia) y una **irrotacional** (sin rotor):
> $$\vec v=\vec\nabla\times\vec A-\vec\nabla\Phi,$$
> con $\vec A$ el **potencial vector** y $\Phi$ el **potencial escalar**.

> [!demostracion]
> **Paso 1 — Dos identidades.** Se apoya en dos identidades de operadores que se prueban directamente,
> $$\vec\nabla\cdot(\vec\nabla\times\vec A)=0,\qquad \vec\nabla\times\vec\nabla\Phi=0.$$
>
> **Paso 2 — Forma propuesta.** Escribimos el campo como suma de un término rotacional y un gradiente,
> $$\vec v=\vec\nabla\times\vec A-\vec\nabla\Phi.$$
>
> **Paso 3 — Sus invariantes.** Tomando divergencia, rotor y componente normal:
> $$\vec\nabla\cdot\vec v=-\nabla^2\Phi,\qquad \vec\nabla\times\vec v=\vec\nabla\times\vec\nabla\times\vec A,\qquad \hat n\cdot\vec v=\hat n\cdot(\vec\nabla\times\vec A-\vec\nabla\Phi),$$
> donde se usó $\vec\nabla\cdot(\vec\nabla\times\vec A)=0$ y $\vec\nabla\times\vec\nabla\Phi=0$. Como divergencia, rotor y componente normal quedan **fijos** si $\vec A$ y $\Phi$ lo están, por la unicidad ya probada el campo $\vec v$ es único.
>
> **Paso 4 — Interpretación.** La parte $\vec\nabla\times\vec A$ no tiene divergencia (es la **solenoidal** o rotacional; $\vec A$ es el potencial vector); la parte $-\vec\nabla\Phi$ no tiene rotor (es la **irrotacional**; $\Phi$ es el potencial escalar).$\qquad\blacksquare$

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Unicidad | $\vec v$ fijado por $\vec\nabla\cdot\vec v$, $\vec\nabla\times\vec v$ y $\hat n\cdot\vec v$ en $S$ |
> | Prueba | $\vec w=\vec v_1-\vec v_2$, Green 2ª forma $\Rightarrow\int_V\|\vec w\|^2=0\Rightarrow\vec w=0$ |
> | Descomposición | $\vec v=\vec\nabla\times\vec A-\vec\nabla\Phi$ |
> | Parte solenoidal | $\vec\nabla\times\vec A$, $\vec\nabla\cdot(\vec\nabla\times\vec A)=0$; potencial vector $\vec A$ |
> | Parte irrotacional | $-\vec\nabla\Phi$, $\vec\nabla\times\vec\nabla\Phi=0$; potencial escalar $\Phi$ |

> [!corolario]
> Helmholtz cierra el capítulo: un campo está unívocamente determinado por sus fuentes (divergencia), sus remolinos (rotor) y su comportamiento en la frontera, y se descompone limpiamente en una parte sin fuentes y una sin remolinos. Es el fundamento de los potenciales $\vec A$ y $\Phi$ del electromagnetismo.

> [!referencia]
> - Unicidad vía: [[Teorema de Green]] (2ª forma).
> - Potencial de campos irrotacionales: [[Teorema de Stokes]].
> - Identidades $\vec\nabla\cdot(\vec\nabla\times\vec A)=0$, $\vec\nabla\times\vec\nabla\Phi=0$: [[Operadores Diferenciales/Identidades Operadores]].
