---
title: Estrella-Triángulo (Kennelly)
tags:
  - circuitos-electricos
  - teoria
  - resistivos
  - estrella-triangulo
draft: false
aliases:
  - estrella triángulo
  - transformación Y-Δ
  - teorema de Kennelly
  - wye-delta transform
  - star-delta transformation
---

# Estrella-Triángulo (Kennelly) $R_\Delta=3R_Y$

> [!definicion]
> El **teorema de Kennelly** establece que toda terna de resistencias conectada en **estrella** (Y) entre
> tres nodos $a$, $b$, $c$ es **equivalente**, vista desde esos tres terminales, a otra terna conectada en
> **triángulo** (Δ), y viceversa. La conversión **Δ→Y** reparte cada resistencia de la estrella como
> $$R_a=\frac{R_{ab}\,R_{ca}}{R_{ab}+R_{bc}+R_{ca}}$$
> (y sus cíclicas para $R_b$ y $R_c$), y la conversión **Y→Δ** las recombina como
> $$R_{ab}=\frac{R_aR_b+R_bR_c+R_cR_a}{R_c}$$
> (y sus cíclicas). Es la herramienta que **desbloquea** las redes —puentes, escaleras irregulares— que
> no presentan ninguna asociación serie ni paralelo a la vista.

---

> [!info]
> Nota de la sección [[Reduccion de Circuitos/index| Reducción de circuitos]], dentro del
> [[1 Conceptos Fundamentales y Resistivos/index| capítulo 1]]. Es el recurso al que se acude cuando
> [[Resistencias en Serie y Paralelo]] se queda corto. Se integra en el método sistemático [[RINCE]] y
> convive con [[Simetria en Circuitos]]. Cuando ni Kennelly ni la simetría bastan, se pasa a
> [[Analisis de Mallas]].

---

## Ejemplo

> [!ejemplo] Puente con red en Δ: pasar a estrella para hallar $R_{eq}$
> ![[estrella_triangulo.svg|460]]
>
> *Equivalencia estrella (Y) ↔ triángulo (Δ) entre los nodos $a$, $b$, $c$.*
>
> Consideremos un **puente de Wheatstone** en el que el triángulo superior está formado por tres
> resistencias **iguales** $R_{ab}=R_{bc}=R_{ca}=9\ \Omega$ entre los nodos $a$, $b$, $c$. Como ninguna de
> ellas está en serie ni en paralelo con otra (comparten nodos de tres en tres), no podemos reducir el
> puente directamente. La salida es **convertir el triángulo en estrella**.
>
> **Paso 1 — Denominador común.** La suma de las tres resistencias del triángulo es
> $$R_{ab}+R_{bc}+R_{ca}=9+9+9=27\ \Omega.$$
>
> **Paso 2 — Cada brazo de la estrella.** Aplicando la fórmula Δ→Y a cada nodo,
> $$R_a=\frac{R_{ab}\,R_{ca}}{27}=\frac{9\cdot 9}{27}=\frac{81}{27}=3\ \Omega,$$
> y por la simetría del caso equilibrado $R_b=R_c=3\ \Omega$. Es decir, $R_Y=3\ \Omega$, lo que confirma
> la regla del caso equilibrado $R_\Delta=3R_Y$ (en efecto $9=3\cdot 3$).
>
> **Paso 3 — Circuito ya reducible.** Sustituido el triángulo por la estrella, aparece un nodo central
> conectado a $a$, $b$, $c$ por tres resistencias de $3\ \Omega$. Ahora **sí** hay asociaciones serie y
> paralelo: el brazo $R_a$ queda en serie con la rama que sale de $a$, el brazo $R_b$ en serie con la de
> $b$, esas dos ramas en paralelo entre sí, y el resultado en serie con $R_c$. Con esa cadena ya se
> obtiene $R_{eq}$ entre los terminales del puente con simples sumas y productos.
>
> > [!solucion]
> > El triángulo de $9\ \Omega$ equivale a una estrella de $R_Y=3\ \Omega$ por brazo. La conversión
> > convierte un puente irresoluble por serie/paralelo en una red escalonada que ya se reduce paso a paso.

---

## En qué consiste

> [!teoria] Por qué dos redes distintas son indistinguibles desde fuera
> Una caja con tres terminales $a$, $b$, $c$ y solo resistencias dentro queda **completamente
> caracterizada** por las tres resistencias que se miden entre cada par de bornes (con el tercero al
> aire). Si dos redes —una en Y, otra en Δ— dan los **mismos tres pares** de resistencias, ningún
> experimento externo las distingue: son **equivalentes**. Kennelly es, simplemente, la solución del
> sistema de tres ecuaciones que impone esa igualdad. La estrella tiene un **nodo interno** (el centro)
> que el triángulo no posee; ese nodo desaparece al pasar a Δ y reaparece al pasar a Y.

> [!teorema] Fórmulas de Kennelly
> Sean $R_a,R_b,R_c$ las resistencias de la estrella (cada una entre un terminal y el nodo central) y
> $R_{ab},R_{bc},R_{ca}$ las del triángulo (cada una entre dos terminales).
>
> **Triángulo → Estrella** (cada brazo = producto de las dos Δ adyacentes, dividido por la suma de las tres):
> $$R_a=\frac{R_{ab}R_{ca}}{R_{ab}+R_{bc}+R_{ca}},\quad
> R_b=\frac{R_{ab}R_{bc}}{R_{ab}+R_{bc}+R_{ca}},\quad
> R_c=\frac{R_{bc}R_{ca}}{R_{ab}+R_{bc}+R_{ca}}.$$
>
> **Estrella → Triángulo** (cada lado = suma de productos por pares, dividida por la $R_Y$ opuesta):
> $$R_{ab}=\frac{R_aR_b+R_bR_c+R_cR_a}{R_c},\quad
> R_{bc}=\frac{R_aR_b+R_bR_c+R_cR_a}{R_a},\quad
> R_{ca}=\frac{R_aR_b+R_bR_c+R_cR_a}{R_b}.$$

> [!demostracion]
> **Paso 1 — Resistencia entre dos bornes en cada red.** En el **triángulo**, la resistencia entre $a$ y
> $b$ (con $c$ al aire) es $R_{ab}$ en paralelo con la serie $R_{bc}+R_{ca}$:
> $$R_{ab}^{\Delta}=\frac{R_{ab}\,(R_{bc}+R_{ca})}{R_{ab}+R_{bc}+R_{ca}}.$$
> En la **estrella**, entre $a$ y $b$ (con $c$ al aire) solo conducen los brazos $R_a$ y $R_b$ en serie:
> $$R_{ab}^{Y}=R_a+R_b.$$
>
> **Paso 2 — Igualar par a par.** La equivalencia exige $R_a+R_b=R_{ab}^{\Delta}$, y análogamente para
> los pares $b$-$c$ y $c$-$a$. Se obtiene un sistema de tres ecuaciones con incógnitas $R_a,R_b,R_c$.
>
> **Paso 3 — Resolver.** Sumando las tres y dividiendo, restando convenientemente las ecuaciones, despejan
> $$R_a=\frac{R_{ab}R_{ca}}{R_{ab}+R_{bc}+R_{ca}}$$
> y sus cíclicas. Invirtiendo el sistema (despejando las $R_{\Delta}$ en función de las $R_Y$) se llega a
> $R_{ab}=(R_aR_b+R_bR_c+R_cR_a)/R_c$ y sus cíclicas. $\blacksquare$

> [!proposicion] Caso equilibrado
> Si las tres resistencias del triángulo son iguales, $R_{ab}=R_{bc}=R_{ca}=R_\Delta$, las de la estrella
> también lo son y valen un tercio:
> $$R_Y=\frac{R_\Delta\cdot R_\Delta}{3R_\Delta}=\frac{R_\Delta}{3}\quad\Longleftrightarrow\quad R_\Delta=3R_Y.$$
> Es el caso más frecuente en problemas de examen y conviene memorizarlo: **el triángulo equilibrado vale
> el triple que la estrella equilibrada equivalente.**

> [!warning] Errores típicos
> - **No confundir las dos direcciones.** En Δ→Y se divide por la **suma** de las tres del triángulo; en
>   Y→Δ se divide por la **$R_Y$ del brazo opuesto**. Son fórmulas distintas, no inversas término a término.
> - **Cuidar las adyacencias.** En $R_a$ aparecen las dos resistencias del triángulo que **tocan** el nodo
>   $a$ (esto es, $R_{ab}$ y $R_{ca}$), no $R_{bc}$.
> - La transformación es **exacta y reversible**; no introduce aproximación alguna.

---

## Resumen

> [!resumen] Las dos conversiones de un vistazo
> | Sentido | Fórmula (un término) | Divisor | Regla mnemotécnica |
> |:---|:---|:---|:---|
> | Δ → Y | $R_a=\dfrac{R_{ab}R_{ca}}{R_{ab}+R_{bc}+R_{ca}}$ | suma de las tres $R_\Delta$ | producto de las dos adyacentes / suma |
> | Y → Δ | $R_{ab}=\dfrac{R_aR_b+R_bR_c+R_cR_a}{R_c}$ | $R_Y$ del brazo opuesto | suma de productos por pares / $R_Y$ opuesta |
> | Equilibrado | $R_\Delta=3R_Y$ | — | el triángulo vale el triple |

> [!corolario]
> Kennelly es la pieza que falta para que el método [[RINCE]] sea completo: cuando una red no exhibe ni
> serie ni paralelo, una sola transformación Y-Δ casi siempre **destraba** la reducción y permite seguir
> con las herramientas elementales hasta llegar a $R_{eq}$.

> [!referencia]
> Fraile Mora, cap. 1, §1.11. Relacionado con [[Resistencias en Serie y Paralelo]], [[RINCE]] y
> [[Simetria en Circuitos]]; alternativa de cálculo en [[Analisis de Mallas]].
