---
title: Componentes Simétricas
tags:
  - circuitos-electricos
  - teoria
  - trifasico
draft: false
aliases:
  - componentes simétricas
  - teorema de Fortescue
  - secuencias positiva negativa homopolar
  - symmetrical components
---

# Componentes Simétricas

> [!definicion]
> El **teorema de Fortescue** afirma que **cualquier** conjunto de tres fasores desequilibrados se
> descompone, de forma única, en la **suma** de tres conjuntos **equilibrados**: la secuencia
> **positiva** (orden $abc$), la **negativa** (orden $acb$) y la **homopolar** o cero (las tres en
> fase). Con el operador de giro $a=1\angle120^\circ$,
> $$\overline{V}_a=\overline{V}_{a0}+\overline{V}_{a1}+\overline{V}_{a2}.$$

> [!info]
> La herramienta general para [[Sistemas Desbalanceados/index| sistemas desbalanceados]]
> ([[7 Circuitos Trifasicos/index| capítulo 7]]): convierte un problema asimétrico en tres simétricos.
> Base del análisis de faltas en sistemas de potencia. Fraile Mora, cap. 3, §3.11.

---

## Ejemplo

> [!ejemplo]
> **Descomponer una tensión de una sola fase.**
>
> Un caso extremo de desequilibrio: $\overline{V}_a=30\angle0^\circ\ \text{V}$ y
> $\overline{V}_b=\overline{V}_c=0$. Hallar sus componentes simétricas.
>
> ![[componentes_simetricas.svg|660]]
>
> *Las tres secuencias: positiva ($abc$), negativa ($acb$) y homopolar (en fase). El fasor real es la
> suma de las tres en cada fase.*
>
> **Paso 1 — Fórmulas** (con $a=1\angle120^\circ$):
> $$\overline{V}_{a0}=\tfrac13(\overline{V}_a+\overline{V}_b+\overline{V}_c),\ \ \overline{V}_{a1}=\tfrac13(\overline{V}_a+a\overline{V}_b+a^2\overline{V}_c),\ \ \overline{V}_{a2}=\tfrac13(\overline{V}_a+a^2\overline{V}_b+a\overline{V}_c).$$
>
> **Paso 2 — Sustituir** ($\overline{V}_b=\overline{V}_c=0$):
> $$\overline{V}_{a0}=\overline{V}_{a1}=\overline{V}_{a2}=\tfrac13\cdot30=10\angle0^\circ\ \text{V}.$$
>
> > [!solucion]
> > Las tres componentes valen $10\angle0^\circ\ \text{V}$: una tensión de una sola fase se reparte por
> > igual entre las tres secuencias. (Comprobación: en la fase $a$ suman $30\ \text{V}$; en $b$ y $c$ se
> > cancelan.)

---

## En qué consiste

> [!teoria] El operador $a$ y las tres secuencias
> El operador $a=1\angle120^\circ$ gira un fasor $120^\circ$; cumple $a^2=1\angle240^\circ=1\angle{-}120^\circ$
> y $1+a+a^2=0$. Con él, los tres conjuntos equilibrados son:
> - **Positiva** ($\overline{V}_{a1}$): $\overline{V}_{b1}=a^2\overline{V}_{a1}$, $\overline{V}_{c1}=a\overline{V}_{a1}$ (gira $abc$, como el sistema sano).
> - **Negativa** ($\overline{V}_{a2}$): $\overline{V}_{b2}=a\overline{V}_{a2}$, $\overline{V}_{c2}=a^2\overline{V}_{a2}$ (gira $acb$).
> - **Homopolar** ($\overline{V}_{a0}$): las tres iguales, $\overline{V}_{a0}=\overline{V}_{b0}=\overline{V}_{c0}$.
>
> Sumando las tres se reconstruye el original; cada secuencia se analiza **por separado** en su propia
> red de secuencia, y al final se superponen.

> [!proposicion] Qué dice cada secuencia
> - Un sistema **equilibrado** de secuencia directa tiene **solo** componente **positiva** ($V_{a2}=V_{a0}=0$).
> - La componente **negativa** mide el **desequilibrio** entre fases (calienta los motores, los frena).
> - La **homopolar** solo circula si hay **retorno** (neutro o tierra), pues $\overline{I}_{a0}+\overline{I}_{b0}+\overline{I}_{c0}=3\overline{I}_{a0}\neq0$ necesita un camino común.

> [!warning]
> La homopolar requiere un **camino de retorno**: en triángulo o en estrella sin neutro **no** puede
> circular corriente homopolar. El factor $\tfrac13$ va en la **descomposición** (no al recomponer). Y
> $a$ es $1\angle120^\circ$, **no** la unidad imaginaria $j$.

## Resumen

> [!resumen]
> | Secuencia | Definición | Presencia |
> |:---|:---|:---|
> | Positiva ($V_{a1}$) | equilibrada, orden $abc$ | sistema sano |
> | Negativa ($V_{a2}$) | equilibrada, orden $acb$ | desequilibrio |
> | Homopolar ($V_{a0}$) | las tres en fase | solo con neutro/tierra |
> | Recomposición | $\overline{V}_a=\overline{V}_{a0}+\overline{V}_{a1}+\overline{V}_{a2}$ | — |

> [!corolario]
> Fortescue convierte cualquier desequilibrio en tres sistemas equilibrados independientes, mucho más
> fáciles de analizar. Es la herramienta que cierra el estudio del trifásico: del caso ideal
> equilibrado al real asimétrico, todo queda cubierto.

> [!referencia]
> Fraile Mora, cap. 3, §3.11. Contexto: [[Sistemas Desbalanceados/index| Sistemas desbalanceados]].
> Aplicación: [[Cargas Desbalanceadas Estrella]].
