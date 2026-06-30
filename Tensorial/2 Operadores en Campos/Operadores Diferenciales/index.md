---
title: Operadores Diferenciales
order: 3
tags:
  - analisis-tensorial
  - teoria
  - calculo-vectorial
  - operadores
  - index
draft: false
aliases:
  - operadores diferenciales
  - nabla
  - differential operators
  - del operator
---

# Operadores Diferenciales

> [!definicion]
> El **operador nabla** combina las derivadas parciales con el álgebra vectorial. En cartesianas,
> $$\vec\nabla=\hat{e}_i\frac{\partial}{\partial x_i}.$$
> Según actúe **directamente** sobre un escalar, por **producto punto** o por **producto cruz** sobre un vector, genera las tres operaciones fundamentales del cálculo vectorial: **gradiente**, **divergencia** y **rotor**.

> [!info]
> Sección **2.3** del libro (Rogan & Muñoz), dentro del [[index | capítulo 2]]. Actúa sobre los [[Campos Escalares y Vectoriales | campos]] (cap. 2.1) en escala infinitesimal. Se desglosa en:
> - [[Gradiente]] — escalar → vector, normal a las equipotenciales (cap. 2.3.1).
> - [[Divergencia]] — vector → escalar, fuentes y sumideros (cap. 2.3.2).
> - [[Rotor]] — vector → vector, circulación local (cap. 2.3.3).
> - [[Identidades Operadores]] — $\nabla^2\Phi$ y $\vec\nabla\times\vec\nabla\times\vec v$ (cap. 2.3.4).
> - [[Definiciones Integrales Operadores]] — definiciones como cociente integral/volumen (cap. 2.4).
>
> Su escritura en notación de Einstein es la que permite generalizarlos a [[Coordenadas Curvilineas/index | coordenadas curvilíneas]] (cap. 3).

---

## Ejemplo

> [!ejemplo]
> **Las tres operaciones sobre un mismo objeto.** Con $\vec\nabla=\hat{e}_i\partial/\partial x_i$, sea el escalar $\Phi=-xy$ y el vector $\vec A=(x^2,\,yz,\,z)$.
>
> **Gradiente** $\vec\nabla\Phi=\hat{e}_i\dfrac{\partial\Phi}{\partial x_i}$ (escalar → vector):
> $$\vec\nabla(-xy)=-y\,\hat{e}_x-x\,\hat{e}_y.$$
>
> **Divergencia** $\vec\nabla\cdot\vec A=\dfrac{\partial A_i}{\partial x_i}$ (vector → escalar):
> $$\vec\nabla\cdot\vec A=\frac{\partial x^2}{\partial x}+\frac{\partial(yz)}{\partial y}+\frac{\partial z}{\partial z}=2x+z+1.$$
>
> **Rotor** $\vec\nabla\times\vec A=\varepsilon_{ijk}\dfrac{\partial A_j}{\partial x_i}\hat{e}_k$ (vector → vector):
> $$\vec\nabla\times\vec A=\Big(\tfrac{\partial A_z}{\partial y}-\tfrac{\partial A_y}{\partial z}\Big)\hat{e}_x+\dots=-y\,\hat{e}_x.$$
>
> El mismo operador $\vec\nabla$ produce las tres operaciones según el modo en que se combine con su argumento.

---

## En qué consiste

> [!teoria]
> El operador $\vec\nabla=\hat{e}_i\partial/\partial x_i$ es **vectorial** (tiene componentes $\hat{e}_i$) y **diferencial** (cada componente es una derivada). No es un vector ordinario: su carácter de operador obliga a respetar el orden y a no conmutar con lo que tiene a la derecha. Las tres maneras del álgebra vectorial del [[1 Algebra Lineal y Notacion/index | capítulo 1]] de combinar un vector con un campo dan lugar a las tres operaciones.

> [!info] Las tres operaciones
> | Operador | Actúa sobre | Produce | En índices |
> |---|---|---|---|
> | Gradiente $\vec\nabla\Phi$ | escalar $\Phi$ | vector | $\hat{e}_i\,\partial\Phi/\partial x_i$ |
> | Divergencia $\vec\nabla\cdot\vec A$ | vector $\vec A$ | escalar | $\partial A_i/\partial x_i$ |
> | Rotor $\vec\nabla\times\vec A$ | vector $\vec A$ | vector | $\varepsilon_{ijk}\,(\partial A_j/\partial x_i)\,\hat{e}_k$ |

## Resumen

> [!resumen]
> | Subnota | Aporta |
> |---|---|
> | [[Gradiente]] | $\vec\nabla\Phi$, perpendicular a las equipotenciales, $\vec E=-\vec\nabla\Phi$ |
> | [[Divergencia]] | $\vec\nabla\cdot\vec A$, ecuación de continuidad, fuente/sumidero |
> | [[Rotor]] | $\vec\nabla\times\vec A$, circulación por unidad de área |
> | [[Identidades Operadores]] | $\nabla^2\Phi$ y $\vec\nabla\times\vec\nabla\times\vec v$ |
> | [[Definiciones Integrales Operadores]] | definiciones integrales (base de los teoremas) |

> [!corolario]
> Un único operador $\vec\nabla=\hat{e}_i\partial/\partial x_i$ genera el gradiente (directo), la divergencia (producto punto) y el rotor (producto cruz). Escrito en notación de Einstein, las identidades entre ellos ($\nabla^2$, rotor del rotor) se demuestran como puro álgebra de índices, y las [[Definiciones Integrales Operadores | definiciones integrales]] lo conectan con los [[Teoremas Integrales/index | teoremas integrales]].

> [!referencia]
> - Sobre qué actúan: [[Campos Escalares y Vectoriales]].
> - Marco del capítulo: [[index | capítulo 2]].
> - Base notacional ($\varepsilon_{ijk}$, $\delta_{ij}$): [[1 Algebra Lineal y Notacion/index]].
