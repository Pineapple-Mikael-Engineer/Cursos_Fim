---
title: Análisis de Mallas
tags:
  - circuitos-electricos
  - teoria
  - metodos-analisis
  - mallas
draft: false
aliases:
  - análisis de mallas
  - método de mallas
  - corrientes de malla
  - mesh analysis
---

# Análisis de Mallas

> [!definicion]
> El **análisis de mallas** asigna una **corriente de malla** —una corriente ficticia que circula por cada ventana de la red— y plantea la **LKV** en cada una. Como cada corriente de malla entra y sale de todos los nodos que recorre, la **LKC queda satisfecha de antemano**; solo hay que imponer la LKV. Para un circuito plano de $b$ ramas y $n$ nodos resultan $b-n+1$ ecuaciones, el mínimo.

> [!info]
> Método central de [[Metodos de Analisis/index| Métodos de análisis]] ([[2 Metodos de Analisis y Teoremas/index| capítulo 2]]). Es la [[Ley de Voltajes LKV| LKV]] aplicada de forma sistemática; su dual es el [[Analisis de Nodos]]. Cuando hay una fuente de corriente compartida se recurre a la [[Mallas con Fuentes de Corriente| supermalla]]. Fraile Mora, cap. 1, §1.12.

---

## Ejemplo

> [!ejemplo]
> **El circuito de dos mallas, ahora por corrientes de malla.**
>
> Es el mismo circuito que resolvimos con la [[Ley de Voltajes LKV| LKV]] rama a rama ($U_{s1}=8\ \text{V}$, $U_{s2}=13\ \text{V}$, $R_1=1\ \Omega$, $R_2=2\ \Omega$, $R_3=3\ \Omega$). Allí hicieron falta **tres** ecuaciones (dos de malla y una de nodo); aquí bastan **dos**.
>
> ![[circuito_dos_mallas.svg|470]]
>
> *Corrientes de malla $i_a$ (ventana izquierda) e $i_b$ (derecha), ambas horarias. La rama central $R_2$ es recorrida por las dos: su corriente es $i_a-i_b$.*
>
> **Paso 1 — Asignar corrientes de malla.** $i_a$ e $i_b$, horarias. La LKC ya está cubierta: solo resta la LKV.
>
> **Paso 2 — LKV en la malla $a$.** Las resistencias propias de la malla suman su corriente; la compartida $R_2$ ve la **diferencia** $i_a-i_b$:
> $$-U_{s1} + R_1 i_a + R_2 (i_a - i_b) = 0 \;\Longrightarrow\; 3\,i_a - 2\,i_b = 8.$$
>
> **Paso 3 — LKV en la malla $b$.**
> $$R_2 (i_b - i_a) + R_3 i_b + U_{s2} = 0 \;\Longrightarrow\; -2\,i_a + 5\,i_b = 13.$$
>
> **Paso 4 — Resolver el sistema $2\times2$.**
> $$\begin{pmatrix} 3 & -2 \\ -2 & 5 \end{pmatrix}\!\begin{pmatrix} i_a \\ i_b \end{pmatrix}=\begin{pmatrix} 8 \\ 13 \end{pmatrix}\;\Longrightarrow\; i_a = 6\ \text{A},\quad i_b = 5\ \text{A}.$$
>
> > [!solucion]
> > $i_a = 6\ \text{A}$, $i_b = 5\ \text{A}$. Las corrientes de rama se recuperan al instante: $i_1 = i_a = 6\ \text{A}$ (por $R_1$), $i_3 = i_b = 5\ \text{A}$ (por $R_3$) y $i_{R_2} = i_a - i_b = 1\ \text{A}$ (por la central). Coinciden con las del método LKV, pero con **una ecuación menos**.

---

## En qué consiste

> [!teoria] Por qué la LKC se cumple sola
> Una corriente de malla es un lazo cerrado de corriente. Al recorrer un nodo, **entra por una rama y sale por otra**: su aporte neto a la LKC de ese nodo es cero. Por eso, si todas las corrientes son de malla, la LKC se satisface en **todos** los nodos automáticamente, y solo queda imponer la LKV en cada ventana. La corriente real de una rama es la **suma algebraica** de las corrientes de malla que la atraviesan: en una rama compartida por dos mallas, su diferencia.

> [!algoritmo] Método de mallas (circuito plano, fuentes de tensión)
> **Paso 1 — Identificar las mallas** (ventanas) y asignar a cada una una corriente, todas en el mismo sentido (por convención, **horario**).
>
> **Paso 2 — LKV en cada malla.** Recorriéndola, sumar las caídas: la resistencia $R_k$ **propia** de la malla aporta $R_k i_{\text{malla}}$; una resistencia **compartida** con la malla vecina aporta $R_k\,(i_{\text{malla}} - i_{\text{vecina}})$. Las fuentes de tensión entran con su signo.
>
> **Paso 3 — Resolver** el sistema lineal para las corrientes de malla.
>
> **Paso 4 — Corrientes de rama.** Cada una es la suma algebraica de las corrientes de malla que la recorren.

> [!proposicion] La matriz de resistencias (atajo por inspección)
> Con todas las corrientes horarias, el sistema $R\,\mathbf{i} = \mathbf{u}$ se escribe **por inspección**:
> $$\begin{cases} R_{kk} = \text{suma de las resistencias de la malla } k \\ R_{jk} = -\,(\text{resistencia compartida entre las mallas } j \text{ y } k) \\ u_k = \text{suma de subidas de tensión de las fuentes en la malla } k \end{cases}$$
> La matriz $R$ es **simétrica** ($R_{jk}=R_{kj}$) si no hay fuentes dependientes. En el ejemplo, $R_{11}=R_1+R_2=3$, $R_{22}=R_2+R_3=5$, $R_{12}=R_{21}=-R_2=-2$.

> [!warning]
> El término de acoplamiento es $-R_{\text{compartida}}$ **solo** si las dos corrientes de malla se definen en el **mismo** sentido (ambas horarias). Si se mezclan sentidos, los signos cambian. Y el método de mallas, tal cual, exige un circuito **plano** y fuentes de **tensión**; con una fuente de corriente compartida hay que usar la [[Mallas con Fuentes de Corriente| supermalla]].

## Resumen

> [!resumen]
> | Aspecto | Mallas |
> |:---|:---|
> | Incógnita | corriente de malla $i_k$ |
> | Ley impuesta | LKV ($\sum v = 0$ por ventana) |
> | Ley automática | LKC |
> | Nº de ecuaciones | $b-n+1$ |
> | Sistema | $R\,\mathbf{i}=\mathbf{u}$, $R$ simétrica |
> | Resistencia propia / compartida | $R_{kk}=\sum R_{\text{malla}}$ / $R_{jk}=-R_{\text{compartida}}$ |

> [!corolario]
> El análisis de mallas reduce el circuito a un sistema lineal pequeño y **escribible por inspección**. Resolver el mismo circuito con menos ecuaciones que rama a rama es justo lo que prometía la [[Ramas y Mallas Independientes| topología]].

> [!referencia]
> Fraile Mora, cap. 1, §1.12. Dual: [[Analisis de Nodos]]. Caso especial: [[Mallas con Fuentes de Corriente]]. Con fuentes dependientes: [[Ecuaciones de Restriccion]].
