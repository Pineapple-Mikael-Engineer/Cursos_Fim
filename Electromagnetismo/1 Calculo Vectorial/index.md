---
title: Cálculo Vectorial
tags:
  - electromagnetismo
  - teoria
  - calculo-vectorial
  - indice
draft: false
aliases:
  - Cálculo Vectorial
  - Lenguaje del electromagnetismo
---

# Cálculo Vectorial $\nabla\cdot,\ \nabla\times,\ \nabla,\ \nabla^2$

> [!definicion]
> El **cálculo vectorial** es el lenguaje en que se escribe el electromagnetismo. Sus campos —escalares $\varphi(\vec r)$ y vectoriales $\vec F(\vec r)$— y sus tres operadores diferenciales —**gradiente, divergencia y rotacional**— bastan para enunciar las cuatro ecuaciones de Maxwell. Toda la física del curso vive en cómo un campo **varía en el espacio** (sus derivadas) y cómo se **acumula** sobre curvas, superficies y volúmenes (sus integrales), unidos por los **teoremas integrales**.

---

> [!info]
> **Capítulo 1 del curso Electromagnetismo.** Es la caja de herramientas que el resto del curso usa sin volver a deducir. Notación SI, vectores con flecha $\vec F$, **convenio de suma de Einstein** y símbolos $\delta_{ij},\epsilon_{ijk}$ para las demostraciones.
> **Referencia.** Griffiths, *Introduction to Electrodynamics*, cap. 1. Para profundidad y la versión tensorial que culmina el curso, Jackson y Landau-Lifshitz Vol. 2.

---

## La idea del capítulo

> [!teoria] Tres operadores, dos teoremas, una delta
> El campo electromagnético es un **campo vectorial** (a veces derivado de potenciales escalares/vectoriales). Para describirlo hacen falta tres derivadas direccionales del operador nabla $\nabla=\hat e_i\,\partial_i$:
>
> $$\underbrace{(\nabla\varphi)_i=\partial_i\varphi}_{\text{gradiente}}\qquad \underbrace{\nabla\cdot\vec F=\partial_i F_i}_{\text{divergencia}}\qquad \underbrace{(\nabla\times\vec F)_i=\epsilon_{ijk}\,\partial_j F_k}_{\text{rotacional}}$$
>
> El **gradiente** mide cómo crece un escalar y apunta perpendicular a sus superficies de nivel; la **divergencia** mide cuánto "mana" un campo de cada punto (fuentes y sumideros); el **rotacional** mide cuánto "circula" alrededor de cada punto (remolinos). Su composición $\nabla^2=\nabla\cdot\nabla$ es el **laplaciano**, que gobierna potenciales y ondas.
>
> ![[campos_escalar_vectorial.svg|460]]
> *Izquierda: campo escalar $\varphi$ por sus curvas de nivel. Derecha: campo vectorial $\vec F$ por sus flechas. El electromagnetismo es, esencialmente, el estudio de un campo vectorial y los escalares de los que se deriva.*

> [!teorema] Los dos teoremas que sostienen Maxwell
> El cálculo vectorial conecta lo **local** (derivadas) con lo **global** (integrales) mediante dos teoremas que son la misma idea —"la integral en una región se reduce a su frontera"— en dimensiones distintas:
> $$\oint_S\vec F\cdot d\vec A=\int_V\nabla\cdot\vec F\,dV\qquad\text{(divergencia / Gauss)}$$
> $$\oint_C\vec F\cdot d\vec l=\int_S(\nabla\times\vec F)\cdot d\vec A\qquad\text{(Stokes)}$$
> Gauss traduce la ley de Gauss y $\nabla\cdot\vec B=0$ entre forma integral y diferencial; Stokes hace lo propio con Faraday y Ampère. Además, sus corolarios —campo conservativo $\Leftrightarrow\vec F=\nabla\varphi$, campo solenoidal $\Leftrightarrow\vec F=\nabla\times\vec A$— **crean los potenciales** $V$ y $\vec A$. Se demuestran en [[Teoremas Integrales]].

> [!proposicion] Las identidades que hacen emerger la estructura
> Dos identidades, demostradas por contracción de índices con $\epsilon_{ijk}\epsilon_{ilm}=\delta_{jl}\delta_{km}-\delta_{jm}\delta_{kl}$, son la raíz de los potenciales:
> $$\nabla\times(\nabla\varphi)=\vec 0\quad\Rightarrow\quad \vec E=-\nabla V;\qquad\qquad \nabla\cdot(\nabla\times\vec F)=0\quad\Rightarrow\quad \vec B=\nabla\times\vec A.$$
> Y el **doble rotacional** $\nabla\times(\nabla\times\vec F)=\nabla(\nabla\cdot\vec F)-\nabla^2\vec F$ es el paso algebraico exacto que convierte las ecuaciones de Maxwell en la **ecuación de ondas**. Todo en [[Identidades Vectoriales]].

> [!warning] Donde el cálculo limpio se rompe
> Las identidades anteriores suponen campos **suaves**. El electromagnetismo está lleno de **fuentes puntuales**: una carga puntual genera $\vec E\propto\hat r/r^2$, cuya divergencia es nula en todas partes... salvo que su flujo vale $4\pi$. La **delta de Dirac** $\delta^3(\vec r)$ reconcilia ambas cosas: $\nabla\cdot(\hat r/r^2)=4\pi\,\delta^3(\vec r)$, de donde sale $\nabla\cdot\vec E=\rho/\varepsilon_0$. Se trata en [[Delta de Dirac y Singularidades]].

---

## Mapa del capítulo

> [!algoritmo] Notas de esta sección
> 1. **[[Campos y Operadores]]** — campos escalares/vectoriales; gradiente, divergencia, rotacional y laplaciano, con sus formas indiciales y su significado geométrico (perpendicularidad, flujo, circulación).
> 2. **[[Teoremas Integrales]]** — teorema del gradiente, de la divergencia (Gauss) y de Stokes; teorema de Green; los corolarios conservativo/solenoidal que originan los potenciales.
> 3. **[[Identidades Vectoriales]]** — $\nabla\times\nabla=0$, $\nabla\cdot(\nabla\times)=0$, BAC–CAB del nabla y reglas de producto, todas por notación indicial.
> 4. **[[Delta de Dirac y Singularidades]]** — delta 1D y 3D; la identidad clave $\nabla\cdot(\hat r/r^2)=4\pi\,\delta^3(\vec r)$ y $\nabla^2(1/r)=-4\pi\,\delta^3(\vec r)$; el nacimiento de la ley de Gauss diferencial.

> [!corolario] Qué llevarse al capítulo 2
> Con los **operadores** (qué mide cada derivada), los **teoremas integrales** (cómo pasar de integral a diferencial y de vuelta) y la **delta** (cómo tratar cargas puntuales), ya se puede construir la [[2 Electrostatica/index | Electrostática]] desde la ley de Coulomb hasta la ecuación de Poisson, sin introducir una sola herramienta matemática nueva.

> [!referencia]
> Griffiths, *Introduction to Electrodynamics*, cap. 1 ("Vector Analysis"). El mapa conceptual completo del curso (vectorial → unificación → tensorial) está en el árbol del curso.
