---
title: Ecuaciones de Restriccion
tags:
  - circuitos-electricos
  - teoria
  - metodos-analisis
  - fuentes-dependientes
draft: false
aliases:
  - ecuaciones de restricción
  - ecuación de restricción
  - constraint equation
  - variable de control
  - control variable
  - fuentes dependientes en mallas
  - dependent sources
---

# Ecuaciones de Restriccion

> [!definicion]
> Una **fuente dependiente** (o controlada: VCVS, VCCS, CCVS, CCCS — ver
> [[Fuentes Dependientes]]) tiene su valor **ligado** a otra tensión o corriente del circuito, la
> llamada **variable de control**. Al aplicar mallas o nodos, la fuente dependiente **se trata como
> una fuente normal** (con su símbolo y su signo), pero como su valor **no es un dato** sino que
> depende del propio circuito, se AÑADE una **ecuación de restricción**: la expresión de la variable
> de control ($i_x$, $v_x$) **en función de las incógnitas** del método (corrientes de malla o
> tensiones de nodo). Esa ecuación se sustituye y se resuelve el sistema.

> [!info]
> Técnica **transversal** de [[Metodos de Analisis/index| Métodos de análisis]]: vale tanto para el
> [[Analisis de Mallas]] como para el [[Analisis de Nodos]], dentro del
> [[2 Metodos de Analisis y Teoremas/index| capítulo 2]]. No es un método nuevo, sino un **paso
> adicional** que se inserta en cualquiera de ellos cuando aparecen [[Fuentes Dependientes]]. Fraile
> Mora, cap. 1, §1.12–1.13.

---

## Ejemplo

> [!ejemplo]
> **Dos mallas con una fuente dependiente CCVS en la rama derecha.**
>
> Datos: fuente **independiente** $V_s = 10\ \text{V}$ (rama izquierda); $R_1 = 2\ \Omega$ (recorrida
> por la corriente de control $i_x$), $R_2 = 2\ \Omega$ (central, compartida) y $R_3 = 2\ \Omega$
> (superior derecha). En la rama derecha hay una **fuente dependiente de tensión controlada por
> corriente (CCVS)** de valor $4\,i_x$, donde $i_x$ es la corriente por $R_1$, que **coincide con la
> corriente de malla** $i_1$. Corrientes de malla $i_1$ (izquierda) e $i_2$ (derecha), **horarias**.
>
> ![[fuente_dependiente_ejemplo.svg|470]]
>
> *La fuente dependiente vale $4\,i_x$, con $i_x = i_1$ la corriente por $R_1$: la variable de control
> se expresa en las incógnitas de malla.*
>
> **Paso 1 — Malla 1 (LKV).** Recorriendo la ventana izquierda en sentido horario:
> $$-V_s + R_1\, i_1 + R_2\,(i_1 - i_2) = 0 \;\Longrightarrow\; 4\,i_1 - 2\,i_2 = 10.$$
>
> **Paso 2 — Malla 2 (LKV).** La CCVS se trata como una fuente normal; recorrida en su sentido aporta
> el término $+4\,i_x$:
> $$R_2\,(i_2 - i_1) + R_3\, i_2 + 4\,i_x = 0.$$
>
> **Paso 3 — Ecuación de restricción.** La variable de control es la corriente por $R_1$, que es
> justamente la corriente de malla $i_1$:
> $$i_x = i_1.$$
> Sustituyendo en la malla 2 para eliminar $i_x$ de las ecuaciones:
> $$2\,(i_2 - i_1) + 2\,i_2 + 4\,i_1 = 0 \;\Longrightarrow\; 2\,i_1 + 4\,i_2 = 0.$$
>
> **Paso 4 — Resolver el sistema $2\times2$.** Con las dos ecuaciones ya en las incógnitas $i_1, i_2$:
> $$\begin{cases} 4\,i_1 - 2\,i_2 = 10 \\ 2\,i_1 + 4\,i_2 = 0 \end{cases}
> \;\Longrightarrow\; i_1 = 2\ \text{A},\quad i_2 = -1\ \text{A}.$$
>
> > [!solucion]
> > $i_1 = 2\ \text{A}$ e $i_2 = -1\ \text{A}$. Con ello, el **valor real** de la fuente dependiente es
> > $4\,i_x = 4\,i_1 = 4(2) = 8\ \text{V}$. El **signo negativo** de $i_2$ indica que su sentido real
> > es **opuesto** al horario supuesto. Observa que la matriz del sistema,
> > $\left[\begin{smallmatrix} 4 & -2 \\ 2 & 4 \end{smallmatrix}\right]$, **ya no es simétrica**: es la
> > huella que deja la fuente dependiente al sustituir la restricción.

---

## En qué consiste

> [!teoria] Por qué la fuente dependiente no añade incógnita pero sí ecuación
> Una fuente dependiente **no introduce una incógnita nueva** en el método: las incógnitas siguen
> siendo las corrientes de malla (o tensiones de nodo). Lo que ocurre es que su **valor no es un
> dato**: depende de una **variable de control** que pertenece al propio circuito. Por eso hay que
> **ligar** ese valor a las incógnitas, y eso es justo lo que hace la **ecuación de restricción**:
> escribe $i_x$ o $v_x$ en términos de las corrientes de malla o tensiones de nodo. Se añade **tantas
> ecuaciones de restricción como fuentes dependientes** haya. Al sustituirlas, la **matriz del sistema
> deja de ser simétrica** —pierde la simetría que tienen los circuitos con solo resistencias y fuentes
> independientes—, lo cual es perfectamente normal y no indica ningún error.

> [!algoritmo] Mallas o nodos con fuentes dependientes
> **Paso 1 — Plantear el método como siempre.** Escribir las ecuaciones de malla (LKV) o de nodo
> (LKC) tratando la fuente dependiente **como una fuente normal**, respetando su símbolo y su signo.
> En las ecuaciones aparecerá su valor simbólico ($k\,i_x$, $k\,v_x$, etc.).
>
> **Paso 2 — Identificar la variable de control** ($i_x$, $v_x$) y **expresarla en función de las
> incógnitas** del método (corrientes de malla o tensiones de nodo). Esa relación es la **ecuación de
> restricción**.
>
> **Paso 3 — Sustituir** la restricción en las ecuaciones para que solo queden las incógnitas del
> método.
>
> **Paso 4 — Resolver** el sistema resultante.

> [!warning]
> **No olvides la ecuación de restricción:** sin ella el sistema queda **indeterminado** (más
> incógnitas que ecuaciones, porque $i_x$/$v_x$ habría entrado como variable suelta). Cuida además el
> **signo y el sentido de la variable de control**: define con claridad en qué sentido mides $i_x$ (o
> entre qué bornes mides $v_x$) y mantén esa convención al escribir tanto el valor de la fuente como la
> restricción.

## Resumen

> [!resumen]
> | Aspecto | Ecuación de restricción |
> |:---|:---|
> | Cuándo | hay una [[Fuentes Dependientes\| fuente dependiente]] en el circuito |
> | Qué es | la variable de control ($i_x$, $v_x$) escrita en las incógnitas del método |
> | ¿Incógnita nueva? | **No**; las incógnitas siguen siendo $i$ de malla o $v$ de nodo |
> | Cuántas se añaden | una **por cada** fuente dependiente |
> | Efecto en la matriz | **pierde la simetría** tras sustituir |
> | Aplica a | [[Analisis de Mallas]] y [[Analisis de Nodos]] |
>
> En el ejemplo: la malla 2 ($2\,i_1 + 4\,i_2 = 0$, tras usar $i_x = i_1$) junto con la malla 1
> ($4\,i_1 - 2\,i_2 = 10$) dan $i_1 = 2\ \text{A}$, $i_2 = -1\ \text{A}$, y la fuente dependiente vale
> $4\,i_x = 8\ \text{V}$.

> [!corolario]
> La fuente dependiente **no encarece** el método: no suma incógnitas, solo cambia un **dato** por una
> **ecuación de restricción**. El sistema queda igual de grande que sin la fuente; lo único que se
> pierde es la simetría de la matriz, un precio cómodo a cambio de modelar la dependencia.

> [!referencia]
> Fraile Mora, cap. 1, §1.12–1.13. Concepto de las fuentes: [[Fuentes Dependientes]]. Métodos donde se
> aplica: [[Analisis de Mallas]] y [[Analisis de Nodos]]. Índice del tema:
> [[Metodos de Analisis/index]].
