---
title: Notación Tensorial y Terminología
tags:
  - analisis-tensorial
  - teoria
  - tensores
  - notacion-diadica
draft: false
aliases:
  - notacion diadica
  - rango de un tensor
  - producto diadico
  - tensor notation
  - dyadic product
---

# Notación Tensorial y Terminología

> [!definicion]
> Un **tensor** de rango $n$ se escribe en **notación diádica** como sus componentes acompañadas de $n$ vectores base yuxtapuestos:
> $$\overleftrightarrow{T}=T_{ijk\dots}\,\hat e_i\hat e_j\hat e_k\dots$$
> El **rango** (u orden) es el número de índices = número de vectores base. Un **escalar** es rango 0 (sin índices), un **vector** es rango 1 ($\vec A=A_i\hat e_i$). La **dimensión** del espacio fija el rango de valores de cada índice (en 3D: $i,j,k\dots=1,2,3$), de modo que un tensor de rango $n$ tiene $3^n$ componentes.

> [!info]
> Es la **notación** del [[index | capítulo 4]] (libro, cap. 4.2), continuación de [[Tensor Conductividad y Ley de Ohm]]. Aquí se fija el vocabulario —rango, base diádica, producto externo— que usan [[Operaciones con Tensores]] y [[Transformaciones entre Sistemas/index | transformaciones]]. La yuxtaposición de bases $\hat e_i\hat e_j$ son "cajones" (no operan entre sí) y se apoya en la [[1 Algebra Lineal y Notacion/Notacion Indices Sumatorias | convención de Einstein]].

---

## Ejemplo

> [!ejemplo]
> **Producto diádico de dos vectores concretos.** Sean $\vec A=(2,0,1)$ y $\vec B=(1,3,0)$ en 3D. El **producto diádico** (externo) $\vec A\vec B$ es un tensor de rango 2 cuyas componentes son $T_{ij}=A_iB_j$:
> $$\vec A\vec B=A_i\hat e_i\,B_j\hat e_j=A_iB_j\,\hat e_i\hat e_j.$$
> La matriz $[T]$ se obtiene multiplicando columna por fila:
> $$[T]=\begin{pmatrix}A_1\\A_2\\A_3\end{pmatrix}\begin{pmatrix}B_1&B_2&B_3\end{pmatrix}=\begin{pmatrix}2\\0\\1\end{pmatrix}\begin{pmatrix}1&3&0\end{pmatrix}=\begin{pmatrix}2&6&0\\0&0&0\\1&3&0\end{pmatrix}.$$
> Por ejemplo $T_{12}=A_1B_2=2\cdot3=6$ y $T_{31}=A_3B_1=1\cdot1=1$. Nótese que $T_{ij}\neq T_{ji}$ en general: la diádica $\vec A\vec B\neq\vec B\vec A$ (el orden de las bases importa). Esta matriz tiene **rango algebraico 1** (filas proporcionales), reflejo de que nace de dos solos vectores.

> [!ejemplo]
> **Clasificar objetos por rango.** Dado el número de índices se lee el rango (y con él, el número de componentes en 3D):
>
> | Objeto | Notación | Índices | Rango | Componentes (3D) |
> |---|---|---|---|---|
> | temperatura $\Phi$ | $\Phi$ | 0 | 0 | 1 |
> | campo $\vec E$ | $E_i\hat e_i$ | 1 | 1 | 3 |
> | conductividad $\overleftrightarrow{\sigma}$ | $\sigma_{ij}\hat e_i\hat e_j$ | 2 | 2 | 9 |
> | diádica $\vec A\vec B$ | $A_iB_j\hat e_i\hat e_j$ | 2 | 2 | 9 |
> | rigidez elástica $\overleftrightarrow{C}$ | $C_{ijkl}\hat e_i\hat e_j\hat e_k\hat e_l$ | 4 | 4 | 81 |
>
> La regla operativa: **cuenta los índices libres** (o, equivalentemente, los vectores base). El producto triple $(\vec A\times\vec B)\cdot\vec C$ no tiene índices libres (todos sumados) $\Rightarrow$ rango 0, un escalar.

---

## En qué consiste

> [!teoria]
> La notación diádica **yuxtapone** vectores base sin ningún operador entre ellos: en $\hat e_i\hat e_j$ las dos bases son cajones que registran *con qué pareja de direcciones* va asociada la componente $T_{ij}$. No se multiplican ni con punto ni con cruz; simplemente se ordenan. Esto consigue dos cosas: (1) la notación **carga la base**, así que las ecuaciones pueden mezclar sistemas de coordenadas; (2) el **rango** queda visible como el número de cajones. La matriz $[T]$ es solo el arreglo de componentes $T_{ij}$ **sin** la información de la base.

> [!definicion] Producto externo (diádico)
> El **producto externo** de dos tensores yuxtapone sus componentes y concatena sus bases. Para dos vectores produce un tensor de rango 2:
> $$\vec A\vec B=A_i\hat e_i\,B_j\hat e_j=A_iB_j\,\hat e_i\hat e_j,\qquad (\vec A\vec B)_{ij}=A_iB_j.$$
> En general, el producto externo de un tensor de rango $p$ por uno de rango $q$ da un tensor de **rango $p+q$**:
> $$T_{ij\dots}\,U_{kl\dots}\,\hat e_i\hat e_j\dots\hat e_k\hat e_l\dots,\qquad \text{rango}=p+q.$$

> [!teorema] El producto externo suma los rangos
> Si $\overleftrightarrow{T}$ tiene rango $p$ y $\overleftrightarrow{U}$ tiene rango $q$, su producto externo $\overleftrightarrow{T}\,\overleftrightarrow{U}$ tiene rango $p+q$.

> [!demostracion]
> **Paso 1.** Escribir cada factor en notación diádica con índices distintos para no violar la regla de oro (ningún índice más de dos veces):
> $$\overleftrightarrow{T}=T_{i_1\dots i_p}\,\hat e_{i_1}\dots\hat e_{i_p},\qquad \overleftrightarrow{U}=U_{j_1\dots j_q}\,\hat e_{j_1}\dots\hat e_{j_q}.$$
>
> **Paso 2.** El producto externo es la yuxtaposición: se multiplican las componentes (todos índices **libres**, ninguno se repite) y se concatenan las bases en orden:
> $$\overleftrightarrow{T}\,\overleftrightarrow{U}=T_{i_1\dots i_p}\,U_{j_1\dots j_q}\;\hat e_{i_1}\dots\hat e_{i_p}\,\hat e_{j_1}\dots\hat e_{j_q}.$$
>
> **Paso 3.** Contar: el resultado tiene $p+q$ índices libres y $p+q$ vectores base. Como el rango es el número de bases, el rango es $p+q$. $\blacksquare$
>
> Caso particular ($p=q=1$): dos vectores dan un tensor de rango $1+1=2$, la diádica del ejemplo.

> [!info] Terminología
> | Término | Significado |
> |---|---|
> | **rango** (orden) | nº de índices = nº de vectores base |
> | **componente** | $T_{ij\dots}$, un número; el arreglo es la matriz $[T]$ |
> | **base diádica** | $\hat e_i\hat e_j\dots$, yuxtaposición sin operador ("cajones") |
> | **diádica** | tensor de rango 2 formado por $\vec A\vec B$ |
> | **producto externo** | yuxtaposición; rangos se **suman** |
> | **dimensión** | nº de valores por índice ($=3$ en 3D) $\Rightarrow$ $3^n$ componentes |

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Notación diádica | $\overleftrightarrow{T}=T_{ijk\dots}\hat e_i\hat e_j\hat e_k\dots$ |
> | Rango $n$ | nº de índices = nº de bases |
> | Escalar / vector | rango 0 / rango 1 |
> | Componentes en 3D | $3^n$ |
> | Producto diádico | $\vec A\vec B=A_iB_j\hat e_i\hat e_j$ (rango 2) |
> | Producto externo | rango$(p)$ + rango$(q)$ = $p+q$ |

> [!corolario]
> El rango es el invariante combinatorio que organiza todo el formalismo: cuenta índices y bases a la vez. El **producto externo** es la operación que *sube* el rango (suma los rangos de los factores) y, partiendo de dos vectores, fabrica la primera diádica. Su operación inversa —que *baja* el rango— es la **contracción**, y junto con la suma constituyen el álgebra tensorial de [[Operaciones con Tensores]].

> [!referencia]
> - Operaciones (suma, contracción, producto interno): [[Operaciones con Tensores]].
> - Motivación física de la diádica: [[Tensor Conductividad y Ley de Ohm]].
> - Convención de índices y suma de Einstein: [[1 Algebra Lineal y Notacion/Notacion Indices Sumatorias | notación de índices]].
