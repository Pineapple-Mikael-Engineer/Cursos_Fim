---
title: Ecuaciones en Derivadas Parciales
tags:
  - ecuaciones
  - edp
  - teoria
  - index
draft: false
aliases:
  - EDP
  - PDE
  - Partial Differential Equations
---

# Ecuaciones en Derivadas Parciales

> [!definicion]
> Una **ecuación en derivadas parciales (EDP)** relaciona una función incógnita de **varias
> variables** con sus derivadas parciales, p. ej. $u=u(x,t)$ y
> $$F\!\left(x,t,\,u,\,u_x,\,u_t,\,u_{xx},\,u_{xt},\dots\right)=0.$$
> A diferencia de una [[1 Ecuaciones Diferenciales Ordinarias/index| EDO]], la solución general
> involucra **funciones arbitrarias** (no solo constantes), y las **condiciones de frontera e
> iniciales** son las que seleccionan la solución física. Las tres EDP lineales de segundo orden
> —**calor**, **onda** y **Laplace**— son el corazón de la física matemática.

> [!info]
> Segunda parte de la familia **diferencial** (junto a las EDO). Reúne herramientas transversales:
> [[Series de Fourier| Fourier]], [[Sturm-Liouville/index| Sturm-Liouville]] y
> [[Funciones Especiales/index| funciones especiales]] (Bessel, Legendre) — que nacieron justo de
> resolver estas ecuaciones por [[Tecnica de Separacion| separación de variables]].

---

## El mapa de las EDP de segundo orden

> [!teoria]
> Las EDP lineales de segundo orden se **clasifican** en tres tipos —elíptica, parabólica e
> hiperbólica— según el signo de un discriminante (igual que las cónicas), y **cada tipo tiene su
> propia física, sus condiciones bien planteadas y su método**:
> 
> | Tipo | Prototipo | Física | Datos típicos |
> |---|---|---|---|
> | **Parabólica** | calor $u_t=\alpha^2 u_{xx}$ | difusión, suavizado irreversible | inicial + frontera |
> | **Hiperbólica** | onda $u_{tt}=c^2u_{xx}$ | propagación a velocidad finita | inicial ($u,u_t$) + frontera |
> | **Elíptica** | Laplace $\nabla^2u=0$ | equilibrio, estado estacionario | solo frontera |
>
> No es una taxonomía vacía: el **tipo decide qué condiciones hacen el problema bien planteado** y
> cómo se comporta la solución (¿se suaviza? ¿se propaga en frentes? ¿alcanza su máximo en la
> frontera?). Por eso el capítulo empieza por la **clasificación**.

> [!teoria] Los dos grandes métodos
> 1. **Separación de variables + Fourier** (el método maestro para dominios acotados): se busca
>    $u=X(x)\,T(t)$, lo que parte la EDP en EDO acopladas por un **problema de autovalores**
>    ([[Sturm-Liouville/index| Sturm-Liouville]]), y la condición inicial se ajusta con un
>    **desarrollo en serie** de las autofunciones ([[Series de Fourier| Fourier]]).
> 2. **Características** (para primer orden y la onda): se transportan los datos a lo largo de curvas
>    especiales donde la EDP se vuelve una EDO. Da la [[Solucion de dAlembert| solución de d'Alembert]] de la onda y explica la propagación a velocidad finita.

---

## Mapa del capítulo

> [!info]
> | Sección | Contenido |
> |---|---|
> | [[Fundamentos/index\|Fundamentos]] | notación, **clasificación**, formas canónicas, buen planteamiento, condiciones |
> | [[Primer Orden y Caracteristicas/index\|Primer Orden y Características]] | método de características, leyes de conservación, choques |
> | [[Separacion de Variables y Fourier/index\|Separación de Variables y Fourier]] | el método maestro y la base ortogonal |
> | [[Ecuacion del Calor/index\|Ecuación del Calor]] | difusión (parabólica): Dirichlet, Neumann, dominio infinito |
> | [[Ecuacion de Onda/index\|Ecuación de Onda]] | propagación (hiperbólica): modos, d'Alembert, energía |
> | [[Ecuacion de Laplace y Poisson/index\|Laplace y Poisson]] | equilibrio (elíptica): disco, esfera, principio del máximo |
> | [[Funciones de Green para EDP/index\|Funciones de Green]] | solución fundamental, método de imágenes |
> | [[Teoria Avanzada/index\|Teoría Avanzada]] | distribuciones, Sobolev, no lineales (panorama) |

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Objeto | $F(x,t,u,u_x,u_t,u_{xx},\dots)=0$ (varias variables) |
> | Clasificación | elíptica / parabólica / hiperbólica (discriminante) |
> | Método maestro | [[Tecnica de Separacion\|separación]] $u=X(x)T(t)$ + [[Series de Fourier\|Fourier]] |
> | Método de transporte | [[Metodo de las Caracteristicas\|características]] |
> | Datos | iniciales y/o de frontera según el **tipo** |

> [!corolario]
> La gran idea del capítulo: el **tipo** de una EDP (elíptica/parabólica/hiperbólica) no es un
> tecnicismo, es lo que dicta su física, sus condiciones bien planteadas y su método de solución.
> Difusión que suaviza, ondas que propagan, equilibrios que promedian: tres comportamientos, tres
> ecuaciones, un mismo lenguaje.

> [!referencia]
> - Punto de partida: [[Fundamentos/index]] (clasificación y buen planteamiento).
> - El método que se usará una y otra vez: [[Separacion de Variables y Fourier/index]].
> - De dónde vienen las herramientas: [[1 Ecuaciones Diferenciales Ordinarias/index]] (las EDO de la separación).
