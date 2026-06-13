---
title: No Resueltas en y prima
tags:
  - ecuaciones
  - edo
  - teoria
  - primer-orden
  - no-resueltas
  - index
draft: false
aliases:
  - ecuaciones no resueltas en y'
  - no resueltas respecto a la derivada
  - equations not solved for the derivative
---

# No Resueltas en $y'$

> [!definicion]
> Una EDO de primer orden está **no resuelta respecto a $y'$** cuando la derivada aparece de forma
> **no lineal** dentro de la ecuación $F(x,y,y')=0$ —con potencias $(y')^2,(y')^3,\dots$, raíces o
> funciones de $y'$— de modo que **no se puede despejar $y'$ de manera única** (o despejarla produce
> varias ramas). Los casos clásicos que sí tienen método cerrado son la **ecuación de Lagrange**
> $$y=x\,\varphi(y')+\psi(y'),$$
> y su caso particular, la **ecuación de Clairaut**
> $$y=x\,y'+\psi(y').$$

> [!info]
> Última familia del [[Metodos de Primer Orden/index| catálogo de primer orden]] (libro, caps. 2.1 y 2.3). A diferencia de
> los métodos anteriores, aquí **no** se empieza despejando $y'=f(x,y)$: la ecuación lo impide. La idea
> es transformar el problema **derivando** e introduciendo $p=y'$ como variable auxiliar. Aparece aquí
> un fenómeno nuevo y propio de este capítulo: las **soluciones singulares** (envolventes), que no
> existen en los tipos lineales. Hijas: [[Lagrange]], [[Clairaut]],
> [[Solucion Singular y Envolvente]].

---

## En qué consiste

> [!teoria]
> El obstáculo es claro: si $y'$ aparece, por ejemplo, como $(y')^2$, no hay una pendiente única en
> cada punto sino **varias**, y los métodos de los tipos anteriores —que asumen $y'=f(x,y)$ explícito—
> no se aplican. El **truco común** a todos estos casos es:
>
> **Derivar la ecuación respecto a $x$ e introducir $p=y'$ como nueva variable.** Al derivar
> $F(x,y,y')=0$ aparece $y''$, pero como ahora tratamos a $p=y'$ como una **incógnita más** ligada a
> $x$, lo que obtenemos es una **relación entre $x$, $p$ y $\dfrac{dp}{dx}$**. En los casos de Lagrange
> y Clairaut esa relación resulta ser una EDO **lineal en $x(p)$** (¡el papel de variable
> independiente pasa a $p$!). Se resuelve para $x=x(p)$, se sustituye de vuelta en la ecuación
> original para obtener $y=y(p)$, y la solución queda en **forma paramétrica**
> $$x=x(p),\qquad y=y(p),$$
> con $p$ recorriendo los valores admisibles. No siempre se puede eliminar $p$ para volver a $y(x)$
> explícito; la forma paramétrica es la respuesta natural.
>
> Hay un **precio** por derivar: derivar **sube el orden** del problema, y al subirlo podemos introducir
> soluciones que la ecuación original no tenía (**soluciones espurias**) y, sobre todo, puede aparecer
> una **solución singular** que **no** pertenece a la familia de soluciones generales. La intuición
> geométrica es la siguiente: la solución general es una **familia de curvas** (una por cada valor de la
> constante de integración). Su **envolvente** —una curva tangente a todos los miembros de la familia a
> la vez— también satisface la EDO, porque en cada punto comparte pendiente con un miembro de la
> familia; pero **no es ninguno** de esos miembros, no se obtiene fijando la constante. Esa envolvente
> es la solución singular. La profundizan [[Clairaut]] (donde la solución general es un haz de rectas y
> la singular su envolvente) y [[Solucion Singular y Envolvente]] (qué es exactamente una envolvente y
> cómo calcularla).

> [!info] Mapa de las hijas
> | Nota | Ecuación | Idea clave |
> |---|---|---|
> | [[Lagrange]] | $y=x\,\varphi(y')+\psi(y')$ | derivar → **lineal en $x(p)$**; solución paramétrica |
> | [[Clairaut]] | $y=x\,y'+\psi(y')$ | familia de **rectas** + **solución singular** |
> | [[Solucion Singular y Envolvente]] | — | qué es una **envolvente**; c-discriminante |

> [!algoritmo] Esquema general
> 1. **Deriva** la ecuación $F(x,y,y')=0$ respecto a $x$.
> 2. **Pon** $p=y'$ (y $y''=\dfrac{dp}{dx}$); reagrupa.
> 3. **Resuelve** la EDO resultante (en Lagrange/Clairaut suele ser **lineal en $x(p)$**).
> 4. **Escribe** la solución en forma **paramétrica** $x=x(p),\ y=y(p)$ (sustituyendo en la original).
> 5. **Busca la solución singular** eliminando $p$ del sistema
>    $$\{\,F(x,y,p)=0,\quad \partial F/\partial p=0\,\}.$$

## Resumen

> [!resumen]
> | Aspecto | Tipos resueltos en $y'$ | No resueltos en $y'$ |
> |---|---|---|
> | Forma | $y'=f(x,y)$ | $F(x,y,y')=0$ no lineal en $y'$ |
> | Pendiente en un punto | única | varias ramas |
> | Estrategia | integrar / cambio de variable | derivar y poner $p=y'$ |
> | Forma de la solución | $y(x)$ o implícita | a menudo **paramétrica** |
> | Solución singular | no aparece | **envolvente** de la familia |

> [!corolario]
> Lo distintivo de este bloque es doble: la **técnica** (derivar respecto a $x$ y tomar $p=y'$ como
> variable, lo que linealiza el problema en $x(p)$) y el **fenómeno** (la aparición de soluciones
> singulares como envolventes, ausentes en todos los tipos anteriores).

> [!referencia]
> - Caso general: [[Lagrange]].
> - Caso particular y más visual: [[Clairaut]].
> - Concepto de envolvente y su cálculo: [[Solucion Singular y Envolvente]].
> - Vuelta al catálogo: [[Metodos de Primer Orden/index]].
