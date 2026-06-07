---
title: Operadores en Campos Escalares y Vectoriales
tags:
  - analisis-tensorial
  - teoria
  - calculo-vectorial
  - index
draft: false
aliases:
  - operadores en campos
  - capitulo 2 tensorial
  - calculo vectorial
---

# Operadores en Campos Escalares y Vectoriales

> [!definicion]
> Un **campo** es una función de la posición (y a veces del tiempo). Es **escalar** si asigna un número a cada punto (potencial, temperatura, presión) o **vectorial** si asigna un vector (campo eléctrico, velocidad de un fluido). Sobre ellos actúan dos familias de operadores: **diferenciales** ($\vec\nabla\Phi$, $\vec\nabla\cdot\vec A$, $\vec\nabla\times\vec A$) e **integrales** ($\int d\vec r$, $\int d\vec\sigma$, $\int d\tau$).

> [!info]
> Es el **capítulo 2** del libro (Rogan & Muñoz, Parte I). Construye el cálculo vectorial en notación de Einstein, sobre la base del [[1 Algebra Lineal y Notacion/index | capítulo 1]]. Se desglosa en:
> - [[Campos Escalares y Vectoriales]] — cómo se representan y dibujan (cap. 2.1).
> - [[Operadores Integrales/index | Operadores Integrales]] — integrales de línea, superficie y volumen (cap. 2.2).
> - [[Operadores Diferenciales/index | Operadores Diferenciales]] — gradiente, divergencia, rotor e identidades (cap. 2.3).
> - [[Teoremas Integrales/index | Teoremas Integrales]] — Gauss, Green, Stokes y Helmholtz (cap. 2.5).
>
> Los operadores diferenciales viven en escala **infinitesimal**; los teoremas los conectan con la escala **macroscópica**. Todo se reescribe luego en [[Coordenadas Curvilineas/index | curvilíneas]] (cap. 3).

---

## Ejemplo

> [!ejemplo]
> **El operador nabla sobre un mismo campo.** Sea el campo escalar $\Phi=-xy$ y el campo vectorial $\vec A=(x^2,\,yz,\,z)$. Aplicar los tres operadores diferenciales.
>
> **Gradiente** (escalar → vector), $\vec\nabla\Phi=\hat{e}_i\dfrac{\partial\Phi}{\partial x_i}$:
> $$\vec\nabla(-xy)=-y\,\hat{e}_x-x\,\hat{e}_y.$$
>
> **Divergencia** (vector → escalar), $\vec\nabla\cdot\vec A=\dfrac{\partial A_i}{\partial x_i}$:
> $$\vec\nabla\cdot\vec A=\frac{\partial x^2}{\partial x}+\frac{\partial (yz)}{\partial y}+\frac{\partial z}{\partial z}=2x+z+1.$$
>
> **Rotor** (vector → vector), $\vec\nabla\times\vec A=\varepsilon_{ijk}\dfrac{\partial A_j}{\partial x_i}\hat{e}_k$:
> $$\vec\nabla\times\vec A=\Big(\tfrac{\partial A_z}{\partial y}-\tfrac{\partial A_y}{\partial z}\Big)\hat{e}_x+\dots=(0-y)\hat{e}_x+(0-0)\hat{e}_y+(0-0)\hat{e}_z=-y\,\hat{e}_x.$$
>
> Un mismo $\vec\nabla=\hat{e}_i\partial/\partial x_i$ produce las tres operaciones según actúe directamente, por producto punto o por producto cruz.

---

## En qué consiste

> [!teoria]
> El operador nabla se escribe en notación independiente de coordenadas y, en cartesianas,
> $$\vec\nabla=\hat{e}_i\frac{\partial}{\partial x_i}.$$
> Combina el cálculo (derivadas parciales) con el álgebra vectorial del [[1 Algebra Lineal y Notacion/index | capítulo 1]]: actúa **directamente** sobre un escalar (gradiente), por **producto punto** sobre un vector (divergencia) o por **producto cruz** (rotor). Los operadores integrales son sus inversos en escala finita y se escriben en *forma de operador* $\int d\tau\,(\cdot)$, $\int d\vec\sigma\cdot(\cdot)$, colocados a la izquierda del integrando.

> [!info] Las tres operaciones diferenciales
> | Operador | Actúa sobre | Produce | En índices |
> |---|---|---|---|
> | Gradiente $\vec\nabla\Phi$ | escalar | vector | $\hat{e}_i\,\partial\Phi/\partial x_i$ |
> | Divergencia $\vec\nabla\cdot\vec A$ | vector | escalar | $\partial A_i/\partial x_i$ |
> | Rotor $\vec\nabla\times\vec A$ | vector | vector | $\varepsilon_{ijk}\,(\partial A_j/\partial x_i)\,\hat{e}_k$ |

## Resumen

> [!resumen]
> | Subnota | Aporta |
> |---|---|
> | [[Campos Escalares y Vectoriales]] | representación y dibujo de campos |
> | [[Operadores Integrales/index]] | integrales de línea, superficie, volumen |
> | [[Operadores Diferenciales/index]] | gradiente, divergencia, rotor, identidades |
> | [[Teoremas Integrales/index]] | Gauss, Green, Stokes, Helmholtz |

> [!corolario]
> El capítulo convierte el operador único $\vec\nabla=\hat{e}_i\partial/\partial x_i$ en las tres operaciones fundamentales del cálculo vectorial y las cierra con los teoremas integrales, que enlazan lo infinitesimal con lo macroscópico. Es la maquinaria que, escrita en notación de Einstein, se generalizará a [[Coordenadas Curvilineas/index | coordenadas curvilíneas]] y, más adelante, al [[Introduccion a Tensores/index | cálculo tensorial]].

> [!referencia]
> - Base notacional: [[1 Algebra Lineal y Notacion/index]].
> - Identidades clave ($\nabla^2$, $\vec\nabla\times\vec\nabla\times\vec v$): [[Operadores Diferenciales/Identidades Operadores]].
> - Generalización: [[Coordenadas Curvilineas/index]].
