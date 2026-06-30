---
title: Definiciones Topológicas
tags:
  - circuitos-electricos
  - teoria
  - metodos-analisis
  - topologia
draft: false
aliases:
  - definiciones topológicas
  - grafo de un circuito
  - árbol y eslabones
  - nodo rama lazo malla
---

# Definiciones Topológicas

> [!definicion]
> El vocabulario de la topología de circuitos. Un **nodo** es un punto de unión de elementos; una **rama**, un elemento (o grupo) entre dos nodos; un **lazo**, un camino cerrado de ramas; una **malla**, un lazo que no encierra a ningún otro (una "ventana"). El **grafo** es el dibujo simplificado donde cada rama es un segmento; un **árbol** es un subconjunto de ramas que conecta todos los nodos sin formar lazos, y los **eslabones** son las ramas restantes.

> [!info]
> Vocabulario base de la [[Topologia de Redes/index| topología de redes]], en el [[2 Metodos de Analisis y Teoremas/index| capítulo 2]]. Con estos términos se cuenta, en [[Ramas y Mallas Independientes]], cuántas ecuaciones independientes hacen falta. Fraile Mora, cap. 1, §1.7.1.

---

## Ejemplo

> [!ejemplo]
> **Del circuito a su grafo.**
>
> El circuito de la izquierda tiene **cuatro nodos** ($A$, $B$, $C$ y el central $O$) y **seis ramas** (la fuente $u_1$, las resistencias del triángulo exterior y las tres del interior). Al quedarnos solo con la **estructura** —cada rama un segmento, cada nodo un punto— obtenemos su **grafo**, a la derecha:
>
> ![[circuito_grafo.svg|620]]
>
> *El grafo conserva las conexiones y olvida los valores. Tiene los mismos $n=4$ nodos y $b=6$ ramas que el circuito; sobre él se definen árbol, lazos y mallas.*
>
> Sobre este grafo: un **lazo** es, por ejemplo, $A\!-\!B\!-\!O\!-\!A$; las **mallas** (ventanas) son las tres regiones interiores $AOB$, $BOC$, $COA$. La red es **plana** porque se dibuja sin que se crucen ramas.

---

## En qué consiste

> [!teoria] El vocabulario, término a término
> Todas las definiciones se refieren a la conectividad, no a los valores:
>
> - **Nodo:** punto de unión de elementos. Si concurren **tres o más** ramas es un **nodo principal**; si solo **dos** (una conexión en serie), es un **nodo secundario** y no aporta ecuación nueva.
> - **Rama:** un elemento, o un grupo de elementos en serie, comprendido entre dos nodos. Lleva una sola corriente.
> - **Lazo:** conjunto de ramas que forman una línea cerrada, tal que al quitar cualquiera de ellas el camino queda abierto.
> - **Malla:** un lazo que **no contiene ningún otro lazo en su interior**. Solo tiene sentido en circuitos **planos**; hay tantas mallas como **ventanas** tiene la red.
> - **Red plana:** la que puede dibujarse sobre un plano sin que **se cruce** ninguna rama.
> - **Grafo:** dibujo simplificado en que cada rama es un segmento y cada nodo un punto. Es **orientado** si se marca el sentido de referencia de cada rama.
> - **Árbol:** subconjunto de ramas que **conecta todos los nodos sin formar lazos**. Sus ramas se llaman *ramas de árbol*.
> - **Eslabones** (o **cuerdas**): las ramas del grafo **no** incluidas en el árbol. Cada eslabón, al añadirse al árbol, cierra exactamente un lazo.

> [!info] Nodo principal vs. secundario
> Distinguirlos importa para contar ecuaciones: en un **nodo secundario** la LKC dice simplemente que "la corriente que entra es la que sale" (es la misma rama), lo cual no añade información. Por eso, al aplicar el [[Analisis de Nodos| método de nodos]], solo cuentan los **nodos principales**.

> [!info] Un poco de historia
> La topología nació con Leonhard **Euler** y el problema de los **siete puentes de Königsberg** (1736): ¿se puede recorrer la ciudad cruzando cada puente una sola vez? Euler lo resolvió abstrayendo el mapa a un **grafo**, y demostró que era imposible. **Kirchhoff** aplicó estas ideas a los circuitos eléctricos en 1847, justo para elegir ecuaciones independientes.

> [!warning]
> **Malla** y **lazo** no son sinónimos: toda malla es un lazo, pero no todo lazo es una malla. En el grafo del ejemplo, $A\!-\!B\!-\!C\!-\!A$ (el triángulo exterior) es un **lazo** que **no** es malla, porque encierra al nodo $O$ y a tres mallas en su interior.

## Resumen

> [!resumen]
> | Término | Definición breve |
> |:---|:---|
> | Nodo | unión de elementos; principal ($\geq 3$ ramas) o secundario ($2$) |
> | Rama | elemento(s) en serie entre dos nodos; lleva una corriente |
> | Lazo | camino cerrado de ramas |
> | Malla | lazo sin lazos interiores (ventana); solo en redes planas |
> | Red plana | dibujable sin cruces de ramas |
> | Grafo | esqueleto: cada rama un segmento, cada nodo un punto |
> | Árbol | ramas que conectan todos los nodos sin lazos ($n-1$ ramas) |
> | Eslabón | rama fuera del árbol; cierra un lazo ($b-n+1$ en total) |

> [!corolario]
> Reducir un circuito a su grafo separa lo que importa para **contar ecuaciones** (la conectividad) de lo que importa para **calcular valores** (los elementos). Sobre el grafo, el árbol y los eslabones dan directamente el número de ecuaciones independientes: ese es el tema de [[Ramas y Mallas Independientes]].

> [!referencia]
> Fraile Mora, cap. 1, §1.7.1. Continúa en [[Ramas y Mallas Independientes]].
