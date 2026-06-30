---
title: Ecuaciones Diferenciales Ordinarias
order: 1
tags:
  - ecuaciones
  - edo
  - teoria
  - index
draft: false
aliases:
  - EDO
  - ODE
  - Ordinary Differential Equations
---

# Ecuaciones Diferenciales Ordinarias

> [!definicion]
> Una **ecuación diferencial ordinaria (EDO)** relaciona una función incógnita de **una sola variable** con sus derivadas:
> $$F\!\left(x,\,y,\,y',\,\dots,\,y^{(n)}\right)=0 \qquad\text{o, en forma normal,}\qquad y^{(n)}=f\!\left(x,y,y',\dots,y^{(n-1)}\right).$$
> El **orden** es el de la derivada más alta. *Resolverla* es hallar la función $y(x)$ (y un intervalo $I$) que la satisface; casi siempre aparece una **familia** de soluciones con constantes, que un **problema de valor inicial (PVI)** fija.

> [!info]
> Primera parte del curso (la familia **diferencial**, junto con las [[2 Ecuaciones en Derivadas Parciales/index| EDP]]). El recorrido va de lo **operativo** (métodos para resolver tipos concretos) a lo **estructural** (cuándo hay solución y si es única). Las técnicas transversales —[[Transformada de Laplace/index| Laplace]], [[Sturm-Liouville/index| Sturm-Liouville]], [[Funciones Especiales/index| funciones especiales]]— viven en [[5 Herramientas Transversales/index| Herramientas]] y se enlazan desde aquí.

---

## Qué significa resolver una EDO

> [!teoria]
> Una EDO de orden $n$ fija una relación entre $y$ y sus derivadas. *Resolverla* es recuperar la función $y(x)$ a partir de esa relación, lo que **siempre involucra integrar**: por cada integración aparece una constante, así que una EDO de orden $n$ tiene una **solución general con $n$ constantes** (una familia de curvas). Esas constantes son los **grados de libertad** del sistema; se fijan con $n$ datos —**condiciones iniciales** (todas en un punto, un PVI) o **de frontera** (repartidas en los extremos, un PVF).
>
> La dificultad real es que **la mayoría de las EDO no tienen solución en funciones elementales**. Por eso el curso no busca "una fórmula mágica" sino tres lentes complementarias:

> [!info] Las tres lentes para una EDO
> | Lente | En qué consiste | Cuándo se usa |
> |---|---|---|
> | **Analítica** | hallar una fórmula cerrada $y(x)$ | solo para **tipos especiales** (separable, lineal, exacta…) |
> | **Cualitativa** | leer la geometría del [[Campo de Direcciones e Isoclinas\|campo de direcciones]] sin resolver | **siempre** disponible; da forma, equilibrios, estabilidad |
> | **Numérica / series** | aproximar (Euler, RK) o desarrollar en serie | cuando no hay fórmula pero se necesitan valores |

> [!teoria] La gran divisoria: lineal vs. no lineal
> El criterio que más ordena el campo es la **linealidad**. Una EDO es **lineal** si $y$ y sus derivadas aparecen a la potencia 1 y sin productos entre ellas:
> $$a_n(x)\,y^{(n)}+\dots+a_1(x)\,y'+a_0(x)\,y=f(x).$$
> - Las **lineales** obedecen el **principio de superposición** (la solución general es $y=y_h+y_p$, homogénea + particular) y son tratables con álgebra lineal —su solución vive en un espacio vectorial de dimensión $n$. Son las de [[Lineales de Orden Superior/index| orden superior]] y los [[Sistemas y Dinamica/index| sistemas]].
> - Las **no lineales** no superponen: pueden tener [[Prolongacion de Soluciones\|explosión en tiempo finito]], [[Solucion Singular y Envolvente\|soluciones singulares]] o caos. Casi todo lo resoluble a mano son **casos especiales** que un cambio de variable convierte en lineales o separables.

---

## Mapa del capítulo

> [!info] Las cinco caras de una EDO
> | Carpeta | Pregunta que responde | Idea central |
> |---|---|---|
> | [[Fundamentos y Teoria Cualitativa/index\|Fundamentos y Teoría Cualitativa]] | ¿Qué es y *cuándo* hay solución única? | campo de direcciones, Picard, determinismo |
> | [[Metodos de Primer Orden/index\|Métodos de Primer Orden]] | ¿Cómo resuelvo $y'=f(x,y)$? | reconocer el **tipo** y aplicar su truco |
> | [[Lineales de Orden Superior/index\|Lineales de Orden Superior]] | $y''+p y'+q y=f$ | superposición: $y=y_h+y_p$ |
> | [[Sistemas y Dinamica/index\|Sistemas y Dinámica]] | varias incógnitas acopladas | $\mathbf{x}'=A\mathbf{x}$, autovalores, fase |
> | [[Soluciones por Series/index\|Soluciones por Series]] | coeficientes variables | series de potencias y Frobenius |

---

## Por qué importan

> [!teoria]
> Casi todo modelo de un fenómeno con cambio es una EDO: la segunda ley de Newton $m\ddot{x}=F$, el enfriamiento $\dot{T}=-k(T-T_e)$, la desintegración radiactiva, un circuito $RLC$, una población. La razón de fondo: en cuanto una **cantidad física** y su **variación** aparecen juntas, surge una ecuación diferencial. Por eso dominar los **tipos resolubles** y la **teoría de existencia/unicidad** equivale a leer el comportamiento de sistemas muy distintos con un mismo lenguaje.

> [!regla] Estrategia para atacar una EDO de primer orden
> 1. Escríbela en forma normal $y'=f(x,y)$ o en forma diferencial $M\,dx+N\,dy=0$.
> 2. **Clasifícala** por su forma: ¿separable? ¿homogénea? ¿exacta? ¿lineal? ¿Bernoulli/Riccati?
> 3. Aplica el método del tipo (ver [[Metodos de Primer Orden/index| Métodos de Primer Orden]]).
> 4. Si nada encaja, recurre a lo **cualitativo** (campo de direcciones) o a series/numérico.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Objeto | $F(x,y,y',\dots,y^{(n)})=0$; forma normal $y^{(n)}=f(\dots)$ |
> | Solución | familia con $n$ constantes; un [[Concepto General de ODE\|PVI]] la fija |
> | Existencia/unicidad | [[Existencia y Unicidad Picard\|Picard]] ($f$ y $\partial f/\partial y$ continuas) |
> | Primer orden | clasificar y aplicar el método ([[Metodos de Primer Orden/index\|tabla de tipos]]) |
> | Orden superior / sistemas / series | superposición, fase, recurrencias |

> [!corolario]
> Una EDO es, antes que nada, un **campo de direcciones**: en cada punto dice hacia dónde va la solución. Los métodos algebraicos son atajos para integrar ese campo cuando tiene estructura; la teoría cualitativa garantiza que la curva existe y es única aun cuando no sepamos escribirla.

> [!referencia]
> - Empezar por [[Fundamentos y Teoria Cualitativa/index]] (qué es, geometría, existencia).
> - Catálogo de métodos: [[Metodos de Primer Orden/index]].
> - Modelo de estilo del curso: *Apuntes de Ecuaciones Diferenciales*, M. Echeverría.
