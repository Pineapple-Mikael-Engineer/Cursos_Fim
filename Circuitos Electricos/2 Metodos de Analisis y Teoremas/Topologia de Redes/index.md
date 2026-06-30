---
title: Topología de Redes
tags:
  - circuitos-electricos
  - teoria
  - metodos-analisis
  - topologia
  - index
draft: false
aliases:
  - topología de redes
  - topología de circuitos
---

# Topología de Redes

> [!definicion]
> La **topología** estudia la **estructura de conexión** de un circuito —qué nodo se une con qué— con independencia de los valores de los elementos. Su utilidad es muy concreta: dice **cuántas ecuaciones independientes** hacen falta para resolver la red y **cuáles** elegir. Reduciendo el circuito a su **grafo** y escogiendo un **árbol**, el número de ecuaciones de nodo ($n-1$) y de malla ($b-n+1$) se lee de un vistazo.

> [!info]
> Primera sección del [[2 Metodos de Analisis y Teoremas/index | capítulo 2]]. Es el cimiento del [[Analisis de Mallas]] y el [[Analisis de Nodos]]: antes de plantear ecuaciones conviene saber cuántas serán independientes. Fraile Mora, cap. 1, §1.7.

---

## El esqueleto: el grafo

> [!teoria] Quedarse con la forma, olvidar los valores
> Para **contar** ecuaciones no hace falta saber cuánto vale cada resistencia: basta saber **cómo está conectado** el circuito. Si sustituimos cada rama por un simple segmento y cada nodo por un punto, obtenemos el **grafo** de la red: su esqueleto. Dos circuitos con elementos completamente distintos pero igual grafo se resuelven con el **mismo** número y tipo de ecuaciones.
>
> Sobre el grafo se nombran las piezas (lo detalla [[Definiciones Topologicas]]): el **nodo** (unión de ramas), la **rama** (un camino entre dos nodos, que lleva una sola corriente), el **lazo** (un camino cerrado) y la **malla** (un lazo que no encierra a ningún otro: una "ventana" de la red). El número de nodos $n$ y de ramas $b$ es todo lo que necesitamos para el conteo.

## Árbol y eslabones: el conteo

> [!teoria] La idea central de toda la sección
> Elijamos en el grafo un **árbol**: un conjunto de ramas que **conecte todos los nodos sin cerrar ningún lazo**. Al construirlo, el primer nodo no necesita rama y cada rama nueva engancha **exactamente un nodo más**; por tanto, un árbol de $n$ nodos tiene siempre
> $$\boxed{\;n-1\;}\quad\text{ramas de árbol.}$$
> Las ramas que **sobran** —las que no entran en el árbol— se llaman **eslabones** (o cuerdas), y hay
> $$\boxed{\;b-(n-1)=b-n+1\;}\quad\text{eslabones.}$$
> Aquí está la potencia del método: **cada rama de árbol corresponde a una ecuación de nodo (LKC) independiente**, y **cada eslabón, al cerrarse sobre el árbol, define un lazo y una ecuación de malla (LKV) independiente**. Es decir:
> $$n-1\ \text{ecuaciones de nodo}\quad+\quad b-n+1\ \text{ecuaciones de malla}\;=\;b,$$
> exactamente las $b$ ecuaciones que Kirchhoff debe aportar para las $b$ corrientes de rama. La demostración de este conteo y su uso están en [[Ramas y Mallas Independientes]].

> [!ejemplo] Un conteo de cabeza
> Una red con $n=4$ nodos y $b=6$ ramas tiene $n-1=3$ ecuaciones de nodo y $b-n+1=3$ de malla. Sin mirar un solo valor de resistencia ya sabemos que habrá **tres** incógnitas de nodo o **tres** de malla —y que ambos caminos cuestan lo mismo aquí—.

> [!teoria] Dualidad nodo ↔ malla
> El conteo revela una simetría profunda entre los dos métodos del capítulo. El [[Analisis de Nodos]] usa $n-1$ incógnitas (las **tensiones** de los nodos) y la LKC; el [[Analisis de Mallas]] usa $b-n+1$ incógnitas (las **corrientes** de malla) y la LKV. Tensión ↔ corriente, nodo ↔ malla, LKC ↔ LKV: cada afirmación sobre uno tiene su gemela sobre el otro. Por eso conviene **elegir el método con menos ecuaciones**: nodos si $n-1<b-n+1$, mallas en caso contrario.

## Mapa de la sección

> [!info] Qué profundiza cada hija
> | Nota | Qué añade a lo anterior |
> |:---|:---|
> | [[Definiciones Topologicas]] | el **vocabulario** completo (nodo principal/secundario, lazo vs. malla, red plana, grafo orientado, árbol, eslabón) con sus casos finos |
> | [[Ramas y Mallas Independientes]] | la **demostración** del conteo $n-1$/$b-n+1$, su independencia, y el **algoritmo** para elegir las ecuaciones y el método más corto |

> [!corolario]
> La topología convierte una pregunta difícil —"¿cuántas ecuaciones independientes necesito y cuáles elijo?"— en un conteo inmediato sobre el grafo: $n-1$ de nodo y $b-n+1$ de malla. Sin ella, los [[Metodos de Analisis/index | métodos de mallas y nodos]] serían recetas sin fundamento; con ella, son la consecuencia directa de la estructura del circuito.

> [!referencia]
> Fraile Mora, cap. 1, §1.7. Profundizan: [[Definiciones Topologicas]] y [[Ramas y Mallas Independientes]]. Siguiente sección: [[Metodos de Analisis/index | Métodos de análisis]].
