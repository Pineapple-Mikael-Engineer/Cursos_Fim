---
title: RINCE
order: 6
tags:
  - circuitos-electricos
  - teoria
  - resistivos
  - equivalente
draft: false
aliases:
  - RINCE
  - ramas independientes para el cálculo del equivalente
  - método del equivalente resistivo
  - equivalent resistance method
---

# RINCE $R_{eq}=\dfrac{v}{i}\Big|_{a\,b}$

> [!definicion]
> **RINCE** (*Ramas Independientes para el Cálculo del Equivalente*) es el método sistemático del curso ML 140 para hallar la **resistencia equivalente** $R_{eq}$ vista desde dos terminales $a$-$b$ de una red puramente resistiva. La idea: identificar las **ramas independientes** —tramos de resistencia que no comparten más nodos que sus extremos— y **colapsarlas** una a una mediante reducciones sucesivas (serie, paralelo, estrella-triángulo) y simetrías, hasta que entre $a$ y $b$ queda una **única** resistencia. Por definición, $R_{eq}=v/i$, el cociente entre la tensión aplicada en $a$-$b$ y la corriente que entra.

---

> [!info]
> Nota de la sección [[Reduccion de Circuitos/index| Reducción de circuitos]], dentro del [[1 Conceptos Fundamentales y Resistivos/index| capítulo 1]]. Es el **procedimiento paraguas** que orquesta a [[Resistencias en Serie y Paralelo]], [[Estrella Triangulo Kennelly]] y [[Simetria en Circuitos]]. Cuando el método se atasca (no quedan asociaciones ni transformaciones), se recurre a inyectar una fuente de prueba y resolver por [[Analisis de Mallas]].

---

## Ejemplo

> [!ejemplo] Red en escalera reducida con RINCE
> Queremos $R_{eq}$ entre $a$ y $b$ de una **escalera** de tres peldaños, todas las resistencias de $2\ \Omega$: tres resistencias "horizontales" en serie por la rama superior y dos "verticales" (peldaños) que cuelgan hacia el nodo inferior común. La estrategia de RINCE es **empezar por el extremo más alejado** de los terminales y avanzar hacia $a$-$b$, colapsando ramas independientes una a una.
>
> **Paso 1 — Identificar ramas independientes.** Numeramos los nodos de la rama superior. El peldaño más lejano (vertical, $2\ \Omega$) queda en serie con la horizontal que lo precede; ese tramo es una rama independiente porque solo toca la red por sus dos extremos.
>
> **Paso 2 — Colapsar el extremo.** La horizontal final ($2\ \Omega$) está en **serie** con el peldaño vertical final ($2\ \Omega$):
> $$R=2+2=4\ \Omega.$$
> Esos $4\ \Omega$ quedan en **paralelo** con el siguiente peldaño vertical ($2\ \Omega$):
> $$R=\frac{4\cdot 2}{4+2}=\frac{8}{6}=\frac{4}{3}\ \Omega.$$
>
> **Paso 3 — Subir un peldaño.** El resultado anterior está en **serie** con la siguiente horizontal:
> $$R=\frac{4}{3}+2=\frac{10}{3}\ \Omega.$$
>
> **Paso 4 — Último colapso hacia $a$-$b$.** Ese tramo queda en **serie** con la horizontal de entrada,
> $$R_{eq}=\frac{10}{3}+2=\frac{16}{3}\approx 5{,}33\ \Omega.$$
>
> > [!solucion]
> > $R_{eq}=\dfrac{16}{3}\ \Omega\approx 5{,}33\ \Omega$. La escalera se resuelve sin escribir una sola ecuación de mallas: basta alternar serie y paralelo desde el extremo libre hacia los terminales.

---

## En qué consiste

> [!teoria] Qué es una "rama independiente" y por qué se colapsa
> Una **rama independiente** entre dos nodos es un camino de elementos que **no comparte nodos intermedios** con el resto del circuito: solo se conecta por sus dos extremos. Por eso puede sustituirse por su resistencia total sin afectar a nada de lo demás —es la base de la equivalencia vista desde dos terminales—. RINCE consiste en **iterar** este reemplazo: cada paso reduce el número de nodos o de ramas en una unidad, y como la red es finita, el proceso **termina** con una sola resistencia entre $a$ y $b$.

> [!algoritmo] Procedimiento RINCE
> **Paso 1 — Marcar terminales.** Etiquetar los dos bornes $a$ y $b$ desde los que se mide $R_{eq}$.
>
> **Paso 2 — Limpiar.** Eliminar ramas que no conducen: resistencias en serie con un **circuito abierto** (no aportan) y cortocircuitar las que están en paralelo con un **cortocircuito**.
>
> **Paso 3 — Buscar simetrías.** Antes de calcular, comprobar si hay nodos al **mismo potencial** (→ [[Simetria en Circuitos]]): unirlos o separarlos suele eliminar varias ramas de golpe.
>
> **Paso 4 — Reducir serie/paralelo.** Recorrer la red desde el extremo más alejado de $a$-$b$ colapsando toda asociación serie o paralelo que aparezca (→ [[Resistencias en Serie y Paralelo]]).
>
> **Paso 5 — Destrabar con Kennelly.** Si no queda ninguna serie ni paralelo (típico de puentes), aplicar una transformación estrella-triángulo (→ [[Estrella Triangulo Kennelly]]) y volver al Paso 4.
>
> **Paso 6 — Cerrar.** Repetir hasta que entre $a$ y $b$ quede una única resistencia: esa es $R_{eq}$. Si el proceso se estanca, inyectar una fuente de prueba de $1\ \text{V}$ (o $1\ \text{A}$) y obtener $R_{eq}=v/i$ por [[Analisis de Mallas]]. $\blacksquare$

> [!proposicion] La fuente de prueba como red de seguridad
> Cualquier red resistiva tiene $R_{eq}$ bien definida, aunque ninguna reducción elemental la simplifique. Conectando una fuente de tensión de prueba $v$ entre $a$ y $b$ y calculando la corriente $i$ que entra,
> $$R_{eq}=\frac{v}{i},$$
> se obtiene el equivalente **siempre**. RINCE prefiere las reducciones porque son más rápidas, pero la fuente de prueba garantiza que el problema nunca queda sin solución.

> [!warning] Dónde se equivoca uno
> - **Reducir mirando solo el dibujo.** Dos resistencias parecen "en serie" pero comparten un nodo con una tercera rama: entonces **no** lo están. Verificar siempre que el nodo intermedio no tenga más ramas.
> - **Olvidar las simetrías al principio.** Buscarlas **antes** de calcular ahorra la mayor parte del trabajo en redes regulares (cubos, mallas, puentes equilibrados).
> - **Mantener ramas muertas.** Una resistencia en serie con un extremo abierto no transporta corriente: se elimina antes de empezar.

---

## Resumen

> [!resumen] El método en cinco gestos
> | Gesto | Herramienta | Resultado |
> |:---|:---|:---|
> | Limpiar | abiertos/cortocircuitos | menos ramas |
> | Simetría | nodos equipotenciales | unir/separar nodos |
> | Serie/paralelo | $R_{eq}=\sum R$, $1/R_{eq}=\sum 1/R$ | colapsar ramas |
> | Kennelly | Y ↔ Δ | destrabar puentes |
> | Fuente de prueba | $R_{eq}=v/i$ | garantía final |

> [!corolario]
> RINCE no es una fórmula sino una **disciplina de orden**: empezar lejos de los terminales, limpiar, mirar la simetría, reducir, y solo recurrir a mallas si todo lo demás falla. Bien aplicado, convierte redes intimidantes en sumas y paralelos de bachillerato.

> [!referencia]
> Fraile Mora, cap. 1, §1.10–§1.11. Apoyado en [[Resistencias en Serie y Paralelo]], [[Estrella Triangulo Kennelly]] y [[Simetria en Circuitos]]; respaldo de cálculo en [[Analisis de Mallas]].
