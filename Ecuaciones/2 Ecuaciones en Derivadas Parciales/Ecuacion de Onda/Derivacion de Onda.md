---
title: Derivación de la Ecuación de Onda
order: 1
tags:
  - ecuaciones
  - edp
  - teoria
  - onda
  - cuerda
draft: false
aliases:
  - derivación de onda
  - cuerda vibrante
  - wave equation derivation
  - vibrating string
---

# Derivación de la Ecuación de Onda

> [!definicion]
> La ecuación de onda $u_{tt}=c^2\,u_{xx}$ no se postula: **sale de la segunda ley de Newton** aplicada a un pequeño elemento de una **cuerda** tensa que vibra transversalmente. La función $u(x,t)$ es el desplazamiento vertical del punto $x$ en el instante $t$, y la constante $c=\sqrt{T/\rho}$ —tensión sobre densidad— resulta ser la **velocidad** con que viaja la onda.

> [!info]
> Punto de partida de la sección [[Ecuacion de Onda/index| Ecuación de Onda]], dentro del [[2 Ecuaciones en Derivadas Parciales/index| capítulo de EDP]]. Una vez deducida, la resolvemos por dos caminos: [[Separacion Onda y Modos Normales| modos normales]] en una cuerda acotada y la [[Solucion de dAlembert| solución de d'Alembert]] en la recta entera. Es el arquetipo de EDP **hiperbólica**.

---

## Ejemplo

> [!ejemplo] Modos normales de una cuerda fija
> ![[modos_onda.svg|470]]
>
> Los primeros modos $\operatorname{sen}\frac{n\pi x}{L}$ de una cuerda con extremos fijos: son **ondas estacionarias** que encajan exactamente $n$ semilongitudes de onda en la longitud $L$. El modo $n=1$ es la **fundamental** (un solo vientre); el $n=2$ tiene un nodo en el centro, el $n=3$ dos nodos, etc. Sus frecuencias son múltiplos enteros de la fundamental, $\omega_n=n\,\omega_1$, y esa es precisamente la razón física de que una cuerda suene "afinada": los armónicos caen en proporciones $1:2:3:\dots$ Estos modos son las soluciones que produce separar variables sobre la ecuación que vamos a deducir.

## En qué consiste

> [!teoria]
> Imaginemos una cuerda de guitarra: una hilera continua de masa, tensa entre dos clavijas. Cuando la desplazamos un poco de su recta de reposo, cada trocito queda **estirado** y la tensión de los vecinos tira de él hacia el equilibrio. Si la cuerda estuviera perfectamente recta, las tensiones de izquierda y derecha se cancelarían y no habría fuerza neta. Pero donde la cuerda se **curva**, la tensión de un lado apunta un poco más "hacia arriba" que la del otro, y queda una fuerza transversal neta. Esa fuerza es proporcional a la **curvatura** $u_{xx}$, y por Newton produce una aceleración $u_{tt}$. La ecuación de onda no dice más que eso: *la aceleración de cada punto es proporcional a cuánto se curva la cuerda en él*.

> [!teorema] La cuerda vibrante obedece $u_{tt}=c^2u_{xx}$
> Para una cuerda flexible de densidad lineal $\rho$ sometida a tensión constante $T$, con desplazamientos pequeños, el desplazamiento transversal $u(x,t)$ satisface
> $$u_{tt}=c^2\,u_{xx},\qquad c^2=\frac{T}{\rho}.$$

> [!demostracion]
> **Paso 1 — Aislar un elemento y calcular la fuerza transversal.** Tomamos el trozo de cuerda entre $x$ y $x+\Delta x$. La tensión $T$ es tangente a la cuerda en cada extremo; en el extremo derecho apunta con pendiente $u_x(x+\Delta x)$ y en el izquierdo con pendiente $u_x(x)$. Para **ángulos pequeños** la componente horizontal de $T$ es prácticamente la misma a ambos lados (se cancela, la cuerda no se mueve a lo largo de $x$), mientras que la componente **vertical** vale $T\sin\theta\approx T\tan\theta=T\,u_x$. La fuerza transversal neta es entonces la diferencia entre los dos extremos:
> $$F_\perp = T\,u_x(x+\Delta x,t)-T\,u_x(x,t)\;\approx\;T\,u_{xx}(x,t)\,\Delta x,$$
> donde el último paso es la definición de derivada: el incremento de $u_x$ a lo largo de $\Delta x$ es $u_{xx}\,\Delta x$.
>
> **Paso 2 — Aplicar la segunda ley de Newton.** La masa del elemento es $\rho\,\Delta x$ y su aceleración transversal es $u_{tt}$. Igualando $F=ma$:
> $$\rho\,\Delta x\,u_{tt}=T\,u_{xx}\,\Delta x.$$
>
> **Paso 3 — Simplificar y nombrar la constante.** El factor $\Delta x$ se cancela en ambos lados. Dividiendo entre $\rho$,
> $$u_{tt}=\frac{T}{\rho}\,u_{xx}=c^2\,u_{xx},\qquad c=\sqrt{\frac{T}{\rho}}.$$
> La constante $c$ tiene unidades de velocidad y, como veremos en [[Solucion de dAlembert| d'Alembert]], es **literalmente** la rapidez con que se propagan las perturbaciones. $\blacksquare$

> [!info]
> La fórmula $c=\sqrt{T/\rho}$ tiene una lectura física directa: la velocidad **aumenta** al tensar más la cuerda (más $T$) y **disminuye** con cuerdas más gruesas o pesadas (más $\rho$). Por eso al afinar una guitarra giramos la clavija para subir la tensión y elevar el tono, y por eso las cuerdas graves son las más gruesas. Lo notable es que **la misma ecuación** rige el sonido en el aire, las ondas en una membrana y las ondas electromagnéticas: solo cambia el significado de $c$ —para la luz, $c$ es la velocidad de la luz.

> [!warning]
> Toda la deducción usa la aproximación de **ángulos pequeños** ($\sin\theta\approx\tan\theta=u_x$). Si los desplazamientos son grandes, los términos no lineales reaparecen y la cuerda deja de obedecer la ecuación de onda lineal: aparecen fenómenos como el endurecimiento y la generación de armónicos adicionales. La ecuación $u_{tt}=c^2u_{xx}$ es el **régimen de pequeñas oscilaciones**.

## Resumen

> [!resumen]
> | Ingrediente | Papel en la deducción |
> |---|---|
> | Tensión $T$ | fuente de la fuerza restauradora |
> | Densidad $\rho$ | inercia del elemento de cuerda |
> | Curvatura $u_{xx}$ | mide la fuerza transversal neta $\approx T u_{xx}\Delta x$ |
> | Newton $F=ma$ | $\rho\Delta x\,u_{tt}=Tu_{xx}\Delta x$ |
> | Resultado | $u_{tt}=c^2u_{xx}$ con $c^2=T/\rho$ |

> [!corolario]
> La ecuación de onda es **la segunda ley de Newton de una cuerda**: aceleración $\propto$ curvatura. La constante de proporcionalidad $c^2=T/\rho$ no es un número arbitrario sino la velocidad de propagación al cuadrado, y eso explica de un golpe por qué tensar afina y por qué engrosar agrava.

> [!referencia]
> - Cómo se resuelve en una cuerda acotada: [[Separacion Onda y Modos Normales]].
> - Cómo se resuelve en la recta: [[Solucion de dAlembert]].
> - El panorama de la sección: [[Ecuacion de Onda/index]].
