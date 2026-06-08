---
title: Problemas de Frontera EDO
tags:
  - ecuaciones
  - edo
  - teoria
  - lineales
  - problemas-frontera
  - index
draft: false
aliases:
  - problemas de valores de frontera
  - PVF
  - boundary value problem
  - BVP
---

# Problemas de Frontera EDO

> [!definicion]
> Un **problema de valores de frontera (PVF)** consiste en una EDO lineal acompañada de condiciones
> impuestas en **dos puntos distintos**: los extremos $a$ y $b$ de un intervalo $[a,b]$. El caso
> típico es
> $$y''+p(x)\,y'+q(x)\,y=f(x),\qquad y(a)=\alpha,\quad y(b)=\beta.$$
> Esto contrasta con el **problema de valores iniciales (PVI)**, donde todas las condiciones
> ($y(a)=\alpha,\ y'(a)=\gamma$) se dan en **un solo punto**. Mover una de las condiciones del punto
> $a$ al punto $b$ parece un cambio menor, pero altera por completo la naturaleza del problema.

> [!info]
> Última sección del bloque [[Lineales de Orden Superior/index | lineales de orden superior]], dentro
> del [[1 Ecuaciones Diferenciales Ordinarias/index | capítulo de EDO]]. Aquí la EDO ya no se resuelve
> "hacia adelante" desde un punto, sino que debe **ajustarse simultáneamente en ambos extremos**. De
> esta tensión nacen los **autovalores**, que son el puente hacia [[Sturm-Liouville/index |
> Sturm-Liouville]] y la separación de variables en [[2 Ecuaciones en Derivadas Parciales/index |
> EDP]]. Esta sección se organiza en dos notas:
> - [[Problemas de Frontera EDO/Condiciones de Frontera]] — los tipos (Dirichlet, Neumann, Robin,
>   periódicas) y el fenómeno de los **problemas de autovalores**.
> - [[Problemas de Frontera EDO/Funcion de Green para EDO]] — cómo resolver el PVF no homogéneo
>   $L[y]=f$ mediante la **inversa integral** del operador.

---

## Ejemplo

> [!ejemplo] Un mismo operador, tres destinos distintos
> Tomemos $y''+y=0$, cuya solución general es $y=c_1\cos x+c_2\operatorname{sen}x$, y veamos qué pasa
> según dónde y cómo pongamos las condiciones.
>
> **(a) Como PVI** ($y(0)=0,\ y'(0)=1$): $y(0)=c_1=0$ y $y'(0)=c_2=1$, así que
> $$y=\operatorname{sen}x,$$
> **única** solución. Es lo que garantiza siempre el PVI.
>
> **(b) Como PVF con solución única** ($y(0)=0,\ y(\tfrac\pi2)=3$): $c_1=0$ y
> $c_2\operatorname{sen}\tfrac\pi2=c_2=3$, luego $y=3\operatorname{sen}x$. Única, pero el mecanismo es
> distinto: dos ecuaciones algebraicas en $c_1,c_2$.
>
> **(c) Como PVF degenerado** ($y(0)=0,\ y(\pi)=0$): $c_1=0$ y $c_2\operatorname{sen}\pi=0$, que se
> cumple **para todo** $c_2$. Hay **infinitas** soluciones $y=c_2\operatorname{sen}x$.
>
> El mismo operador pasa de tener solución única a tener infinitas con solo cambiar el punto y el
> valor de la segunda condición. Esa fragilidad es justamente lo interesante.

---

## En qué consiste

> [!teoria] Por qué el PVF rompe el determinismo del PVI
> En el PVI, el [[Existencia y Unicidad Picard | teorema de Picard]] garantiza una **única** solución:
> dado el estado completo en un punto ($y$ y $y'$ en $x=a$), la EDO determina el futuro sin
> ambigüedad. Es el **determinismo** de la física clásica: presente $\Rightarrow$ trayectoria.
>
> El PVF reparte la información entre dos puntos, y eso lo cambia todo. Resolverlo equivale a tomar la
> solución general $y=c_1y_1+c_2y_2$ (que ya tiene los $n$ grados de libertad del espacio homogéneo)
> e imponer las condiciones de frontera, lo que produce un **sistema lineal** en las constantes
> $c_1,c_2$:
> $$\begin{cases} c_1\,y_1(a)+c_2\,y_2(a)=\alpha,\\ c_1\,y_1(b)+c_2\,y_2(b)=\beta.\end{cases}$$
> Y un sistema lineal puede tener **una, ninguna o infinitas** soluciones, según el determinante de
> su matriz de coeficientes:
> - determinante $\neq 0$ → **única** solución (caso genérico);
> - determinante $=0$ → o bien **ninguna** (sistema incompatible), o bien **infinitas** (compatible
>   indeterminado).
>
> Por eso un PVF puede no tener solución, o tener un continuo de ellas. No es una patología rara: es
> el régimen donde aparece la física más rica.

> [!teoria] De los PVF a los autovalores (la idea central)
> El caso degenerado —cuando el determinante se anula— no es un accidente que haya que evitar, sino el
> objeto que **da nombre** a toda esta teoría. Consideremos el PVF **homogéneo** con un parámetro:
> $$y''+\lambda y=0,\qquad y(0)=0,\ y(L)=0.$$
> Para casi todo $\lambda$, la única solución es la trivial $y\equiv0$. Pero para ciertos valores
> especiales $\lambda=\lambda_n$ —los **autovalores**— aparecen soluciones no triviales
> $y_n$ —las **autofunciones**—. Esos $\lambda_n$ son exactamente los $\lambda$ que anulan el
> determinante del sistema de frontera.
>
> Esto es la versión continua del problema de autovalores del [[Determinantes y Matrices/index |
> álgebra lineal]] $A\vec v=\lambda\vec v$: el operador diferencial $-\tfrac{d^2}{dx^2}$ con esas
> condiciones de frontera juega el papel de la matriz $A$. Las autofunciones $y_n$ son las que, al
> aplicarles el operador, se reproducen multiplicadas por $\lambda_n$. Y resultan ser una **base
> ortogonal** del espacio de funciones —el germen de las series de Fourier y de la separación de
> variables en EDP—. La nota [[Problemas de Frontera EDO/Condiciones de Frontera]] resuelve este
> problema modelo en detalle.

> [!teoria] La herramienta del PVF no homogéneo: la función de Green
> Cuando el PVF **es** resoluble (determinante $\neq 0$) y hay una fuente $f$, queremos no una sino
> **la** solución, y de forma explícita. La herramienta universal es la **función de Green**
> $G(x,\xi)$: una vez construida, la solución de $L[y]=f$ con condiciones de frontera homogéneas se
> escribe de un golpe como una integral
> $$y(x)=\int_a^b G(x,\xi)\,f(\xi)\,d\xi.$$
> $G$ es, literalmente, la **inversa integral** del operador $L$ (igual que $A^{-1}$ resuelve
> $A\vec x=\vec b$). Su construcción y su interpretación como "respuesta a una fuente puntual"
> $\delta(x-\xi)$ están en [[Problemas de Frontera EDO/Funcion de Green para EDO]].

> [!warning] PVF y PVI no son intercambiables
> No traslade la intuición del PVI al PVF. Que una EDO tenga solución general con dos constantes
> **no** garantiza que un PVF dado sobre ella tenga solución, ni que sea única. Antes de "resolver",
> conviene comprobar el determinante de frontera: si se anula, el problema o es imposible o admite
> infinitas soluciones, y eso suele ser una señal de que está cerca de un **autovalor**.

---

## Mapa de la sección

> [!info]
> | Nota | Rol |
> |---|---|
> | [[Problemas de Frontera EDO/Condiciones de Frontera\|Condiciones de Frontera]] | tipos (Dirichlet/Neumann/Robin/periódicas); existencia y unicidad; problema de autovalores |
> | [[Problemas de Frontera EDO/Funcion de Green para EDO\|Función de Green para EDO]] | resolver $L[y]=f$ con la inversa integral de $L$; fuente puntual $\delta$ |

## Resumen

> [!resumen]
> | Aspecto | PVI | PVF |
> |---|---|---|
> | Condiciones | todas en un punto $x=a$ | repartidas entre $a$ y $b$ |
> | Existencia/unicidad | siempre **única** ([[Existencia y Unicidad Picard\|Picard]]) | una, **ninguna** o **infinitas** |
> | Naturaleza | determinismo (evolución) | sistema lineal en las constantes |
> | Fenómeno propio | — | **autovalores** y autofunciones |
> | Resolver el no homogéneo | integración directa | **función de Green** $y=\int G\,f$ |

> [!corolario]
> El PVF no es "un PVI con las condiciones movidas": es una clase de problemas cualitativamente
> distinta. Su rasgo definitorio —que la solubilidad dependa de un sistema lineal en las constantes—
> hace emerger los **problemas de autovalores**, columna vertebral de [[Sturm-Liouville/index |
> Sturm-Liouville]] y de la física matemática de las EDP. La **función de Green** es la contraparte
> constructiva: la inversa del operador que resuelve el caso no homogéneo.

> [!referencia]
> - El contraste fundamental, la unicidad del PVI: [[Existencia y Unicidad Picard]].
> - Tipos de condiciones y el problema de autovalores: [[Problemas de Frontera EDO/Condiciones de Frontera]].
> - Resolver el no homogéneo: [[Problemas de Frontera EDO/Funcion de Green para EDO]].
> - Hacia dónde lleva esto: [[Sturm-Liouville/index]].
> - El bloque que la contiene: [[Lineales de Orden Superior/index]].
