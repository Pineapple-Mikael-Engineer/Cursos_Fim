---
title: Conexión Triángulo
tags:
  - circuitos-electricos
  - teoria
  - trifasico
draft: false
aliases:
  - conexión triángulo
  - conexión Delta
  - triángulo trifásico
  - delta connection
---

# Conexión Triángulo (Δ)

> [!definicion]
> En la **conexión triángulo (Δ)**, las tres ramas se conectan **en serie** formando un lazo cerrado, y de cada vértice sale una línea. No hay neutro. La **tensión de línea** coincide con la **de fase** ($V_L=V_F$), pero la **corriente de línea** es $\sqrt3$ veces la **de fase**:
> $$I_L=\sqrt3\,I_F.$$

> [!info]
> La otra [[Conexiones Balanceadas/index| conexión balanceada]] del [[7 Circuitos Trifasicos/index| capítulo 7]]; **dual** de la [[Conexion Estrella| estrella]]: lo que allí pasa con las tensiones, aquí pasa con las corrientes. Fraile Mora, cap. 3, §3.4.

---

## Ejemplo

> [!ejemplo]
> **De la corriente de fase a la de línea.**
>
> Una carga equilibrada en triángulo, alimentada a $V_L=400\ \text{V}$, toma una corriente de fase $I_F=10\ \text{A}$ por cada rama. Hallar la corriente de línea y la tensión de fase.
>
> ![[conexion_triangulo.svg|440]]
>
> *Las tres ramas forman un lazo. La tensión de fase $\overline{V}_F$ es la de cada rama (= la de línea); la corriente de línea $\overline{I}_L$ entra por cada vértice y se reparte en dos ramas.*
>
> **Paso 1 — Tensión de fase.** Cada rama está entre dos líneas, así que $V_F=V_L=400\ \text{V}$.
>
> **Paso 2 — Corriente de línea.**
> $$I_L=\sqrt3\,I_F=\sqrt3\cdot10\approx17{,}3\ \text{A}.$$
>
> > [!solucion]
> > $V_F=400\ \text{V}$, $I_L\approx17{,}3\ \text{A}$. La corriente de línea supera a la de fase en $\sqrt3$: por cada vértice confluyen dos ramas.

---

## En qué consiste

> [!teoria] De dónde sale el $\sqrt3$ (ahora en la corriente)
> En cada vértice, la **corriente de línea** es la **diferencia** de las dos corrientes de fase que concurren (LKC): $\overline{I}_a=\overline{I}_{ab}-\overline{I}_{ca}$. Restando dos fasores de igual módulo $I_F$ a $120^\circ$, sale módulo $\sqrt3\,I_F$ y un retraso de $30^\circ$:
> $$\overline{I}_a=\overline{I}_{ab}-\overline{I}_{ca}=\sqrt3\,I_F\angle{-}30^\circ.$$
> Es la **misma geometría** que el $\sqrt3$ de la estrella, pero aplicada a corrientes en vez de tensiones: por eso Y y Δ son **duales**. La tensión, en cambio, no cambia: cada rama está directamente entre dos líneas, $V_F=V_L$.

> [!proposicion] Sin neutro
> El triángulo es un lazo cerrado **sin punto común**: no tiene neutro ni admite cuarto conductor (es siempre a 3 hilos). Por eso se usa en cargas que no necesitan neutro (motores) y en devanados de transformador. La suma de las tres tensiones de fase alrededor del lazo es cero, así que **no** circula corriente de circulación en el triángulo equilibrado.

> [!warning]
> El $\sqrt3$ está aquí en las **corrientes** (la de línea es mayor), al revés que en la estrella. No mezclar las dos reglas: conviene escribir siempre primero qué conexión es. Y la corriente de línea **retrasa $30^\circ$** a la de fase.

## Resumen

> [!resumen]
> | Magnitud | Relación (Δ) |
> |:---|:---|
> | Tensiones | $V_L=V_F$ |
> | Corrientes | $I_L=\sqrt3\,I_F$ (línea $30^\circ$ atrás) |
> | Neutro | no hay; siempre 3 hilos |
> | Dualidad | intercambia $V\leftrightarrow I$ con la [[Conexion Estrella\| estrella]] |

> [!corolario]
> El triángulo pone el $\sqrt3$ en las corrientes y prescinde del neutro. Junto con la [[Conexion Estrella| estrella]], cubre todas las formas de conectar un sistema trifásico equilibrado; ambas se relacionan por la dualidad $V\leftrightarrow I$.

> [!referencia]
> Fraile Mora, cap. 3, §3.4. Dual: [[Conexion Estrella]]. Combinaciones: [[Sistemas Y-Y, Delta-Delta, Y-Delta]]. Equivalencia Y↔Δ de impedancias: [[Estrella Triangulo Kennelly]].
