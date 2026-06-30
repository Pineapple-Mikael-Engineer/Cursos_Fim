---
title: Métodos de Análisis y Teoremas
order: 2
tags:
  - circuitos-electricos
  - teoria
  - metodos-analisis
  - index
draft: false
aliases:
  - métodos de análisis
  - teoremas de circuitos
---

# Métodos de Análisis y Teoremas

> [!definicion]
> El [[1 Conceptos Fundamentales y Resistivos/index| capítulo 1]] dio las **leyes** (Ohm y Kirchhoff); este capítulo da los **métodos** para aplicarlas de forma **sistemática** y con el **mínimo número de ecuaciones**: el **análisis de mallas** (basado en la LKV) y el **análisis de nodos** (basado en la LKC). Y añade los **teoremas** —superposición, Thévenin, Norton, máxima transferencia— que permiten resolver una parte del circuito sin plantear todo el sistema.

> [!info]
> Segundo bloque del curso (sílabo ML 140, semanas 3-4; Fraile Mora, cap. 1, §1.7 y §1.12-1.16). Construye sobre las [[Leyes de Kirchhoff/index| leyes de Kirchhoff]] y la [[Reduccion de Circuitos/index| reducción de circuitos]]. Todo lo de aquí se reutilizará tal cual en [[5 Circuitos AC Sinusoidal y Fasores/index| régimen sinusoidal]], cambiando $R$ por la impedancia $Z$.

---

## Del "a lo bruto" al método

> [!teoria] Por qué hacen falta métodos
> Una red de $b$ ramas tiene $2b$ incógnitas (una tensión y una corriente por rama). Las relaciones de los elementos ($v=Ri$) dan $b$ ecuaciones y [[Ecuaciones Independientes| Kirchhoff aporta las otras $b$]]: el sistema está determinado, pero plantear $2b$ ecuaciones es **inviable** a mano.
>
> Los métodos sistemáticos reducen drásticamente las incógnitas eligiendo **bien** las variables:
>
> - El **análisis de nodos** toma como incógnitas las **tensiones de los nodos** y aplica la LKC. Solo necesita $n-1$ ecuaciones. → [[Analisis de Nodos]].
> - El **análisis de mallas** toma como incógnitas las **corrientes de malla** y aplica la LKV. Solo necesita $b-n+1$ ecuaciones. → [[Analisis de Mallas]].
>
> ¿Cuántas ecuaciones son **realmente independientes**? Eso no depende de los valores de los elementos, sino de la **forma** en que están conectados: es una cuestión de **topología**. → [[Topologia de Redes/index| Topología de redes]].

> [!ejemplo] El ahorro, en números
> Considérese una red de $b=6$ ramas y $n=4$ nodos. El planteamiento "a lo bruto" llevaría a $2b=12$ incógnitas (una $v$ y una $i$ por rama) y $12$ ecuaciones. El **análisis de nodos** las reduce a $n-1=3$ incógnitas; el de **mallas**, a $b-n+1=3$. Pasar de $12$ a $3$ ecuaciones no es un truco de cálculo: es elegir como incógnita la variable correcta —la tensión de nodo o la corriente de malla— de modo que una de las dos leyes de Kirchhoff quede **satisfecha de antemano**.

> [!teoria] Y por qué teoremas
> A veces no interesa resolver **todo** el circuito, sino una parte: la corriente en una rama, la potencia en una carga, el efecto de una sola fuente. Los **teoremas** son atajos para eso:
> - **Superposición:** la respuesta a varias fuentes es la suma de las respuestas a cada una.
> - **Thévenin / Norton:** todo lo que ve una carga por sus dos terminales es una única fuente equivalente con una resistencia en serie (Thévenin) o en paralelo (Norton).
> - **Máxima transferencia de potencia:** cuánta potencia puede entregar una fuente real a una carga.
>
> → [[Teoremas/index| Teoremas de circuitos]].

## Mapa del capítulo

> [!info] Las tres secciones
> | Sección | Qué aporta |
> |:---|:---|
> | [[Topologia de Redes/index\| Topología de redes]] | el esqueleto: **cuántas** ecuaciones independientes hay |
> | [[Metodos de Analisis/index\| Métodos de análisis]] | mallas y nodos: cómo plantear y resolver el sistema |
> | [[Teoremas/index\| Teoremas]] | atajos: superposición, Thévenin, Norton, máxima transferencia |

> [!corolario]
> Mallas y nodos no son leyes nuevas: son la LKV y la LKC aplicadas con un criterio que **garantiza** ecuaciones independientes y mínimas. La topología justifica ese criterio; los teoremas lo complementan cuando solo interesa una parte de la red.

> [!referencia]
> Fraile Mora, cap. 1, §1.7 y §1.12-1.16. Viene de [[1 Conceptos Fundamentales y Resistivos/index| Conceptos fundamentales]]; continúa en [[3 Almacenamiento y Transitorios/index| Almacenamiento y transitorios]].
