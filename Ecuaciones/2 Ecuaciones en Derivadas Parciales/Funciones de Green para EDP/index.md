---
title: Funciones de Green para EDP
tags:
  - ecuaciones
  - edp
  - teoria
  - funcion-green
  - index
draft: false
aliases:
  - función de Green EDP
  - solución fundamental
  - Green's function PDE
---

# Funciones de Green para EDP

> [!definicion]
> La **función de Green** $G(\mathbf{x},\boldsymbol{\xi})$ de un operador $L$ es su respuesta a una
> **fuente puntual**: $L_{\mathbf{x}}G=\delta(\mathbf{x}-\boldsymbol{\xi})$ con las condiciones de
> frontera del problema. Por **superposición**, la solución de $L\,u=f$ es entonces una **integral**
> $$u(\mathbf{x})=\int G(\mathbf{x},\boldsymbol{\xi})\,f(\boldsymbol{\xi})\,d\boldsymbol{\xi}.$$
> Es la **inversa integral** de $L$: convierte resolver una EDP en **integrar** contra un núcleo.

> [!info]
> Sección transversal del [[2 Ecuaciones en Derivadas Parciales/index| capítulo de EDP]]: la misma
> idea que da la [[Calor en Dominio Infinito| solución del calor en la recta]] (núcleo de calor) o la
> [[Laplace en Disco| fórmula de Poisson]]. Generaliza la
> [[Funcion de Green para EDO| función de Green de EDO]] a varias dimensiones y conecta con las
> [[3 Ecuaciones Integrales/index| ecuaciones integrales]] (la solución es una integral con núcleo $G$).

---

## La idea: descomponer la fuente en impulsos

> [!teoria]
> Cualquier fuente $f(\mathbf{x})$ es una **superposición de fuentes puntuales**:
> $f(\mathbf{x})=\int f(\boldsymbol{\xi})\,\delta(\mathbf{x}-\boldsymbol{\xi})\,d\boldsymbol{\xi}$. Si
> conocemos la respuesta $G$ a **un** impulso $\delta$ en $\boldsymbol{\xi}$, la respuesta a $f$ es la
> suma (integral) de todas esas respuestas, ponderadas por $f(\boldsymbol{\xi})$. Eso es exactamente
> $u=\int G f$. La **linealidad** es lo que lo permite.
>
> Construir $G$ tiene dos piezas:
> 1. La **solución fundamental** $\Phi$ —la respuesta al impulso en **espacio libre**, sin
>    fronteras— ([[Solucion Fundamental| solución fundamental]]): $-\tfrac{1}{2\pi}\ln r$ (Laplace
>    2D), $\tfrac{1}{4\pi r}$ (Laplace 3D), el núcleo de calor, etc.
> 2. Una **corrección** que ajusta las **condiciones de frontera**
>    ([[Funcion de Green y Condiciones| función de Green con condiciones]]); cuando la geometría es
>    sencilla, esa corrección se obtiene con el elegante [[Metodo de las Imagenes| método de las imágenes]] (cargas espejo).

> [!info] Recorrido de la sección
> | Nota | Aporte |
> |---|---|
> | [[Solucion Fundamental\|Solución Fundamental]] | respuesta al impulso en espacio libre ($\Phi$) |
> | [[Funcion de Green y Condiciones\|Green y Condiciones]] | $G=\Phi+$ corrección armónica; simetría |
> | [[Metodo de las Imagenes\|Método de las Imágenes]] | cargas espejo para frontera plana o esférica |

## Resumen

> [!resumen]
> | Concepto | Contenido |
> |---|---|
> | Función de Green | $L_x G=\delta(x-\xi)$ + condiciones de frontera |
> | Solución | $u=\int G(x,\xi)\,f(\xi)\,d\xi$ |
> | Solución fundamental | respuesta en espacio libre ($\tfrac1{4\pi r}$, $-\tfrac1{2\pi}\ln r$, núcleo de calor) |
> | Construcción con frontera | $\Phi$ + corrección; [[Metodo de las Imagenes\|imágenes]] si hay simetría |

> [!corolario]
> La función de Green es la **inversa de un operador diferencial**: encapsula toda la información del
> problema (operador + dominio + frontera) en un núcleo, de modo que resolver para **cualquier**
> fuente se reduce a una integral. Es el puente entre las EDP y las
> [[3 Ecuaciones Integrales/index| ecuaciones integrales]].

> [!referencia]
> - La pieza de espacio libre: [[Solucion Fundamental]].
> - El truco geométrico: [[Metodo de las Imagenes]].
> - La versión 1D (EDO): [[Funcion de Green para EDO]].
