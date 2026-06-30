---
title: Conexión Estrella
tags:
  - circuitos-electricos
  - teoria
  - trifasico
draft: false
aliases:
  - conexión estrella
  - conexión Y
  - estrella trifásica
  - wye connection
---

# Conexión Estrella (Y)

> [!definicion]
> En la **conexión estrella (Y)**, las tres ramas (fuentes o cargas) se unen en un punto común, el **neutro** $N$, y el otro extremo de cada una va a una línea ($a$, $b$, $c$). La **corriente de línea** es igual a la **de fase** ($I_L=I_F$), pero la **tensión de línea** (entre dos conductores) es $\sqrt3$ veces la **de fase** (de conductor a neutro):
> $$V_L=\sqrt3\,V_F.$$

> [!info]
> Una de las dos [[Conexiones Balanceadas/index| conexiones balanceadas]] del [[7 Circuitos Trifasicos/index| capítulo 7]]; **dual** del [[Conexion Triangulo| triángulo]]. Su neutro permite el sistema a 4 hilos. Fraile Mora, cap. 3, §3.3.

---

## Ejemplo

> [!ejemplo]
> **De la tensión de fase a la de línea.**
>
> Una carga equilibrada en estrella tiene tensión de fase $V_F=230\ \text{V}$ (de conductor a neutro). Hallar la tensión de línea y la relación entre corrientes.
>
> ![[conexion_estrella.svg|420]]
>
> *Las tres ramas comparten el neutro $N$. La tensión de fase $\overline{V}_F$ va de un conductor al neutro; la de línea $\overline{V}_L$, entre dos conductores. La corriente de línea es la de la propia rama.*
>
> **Paso 1 — Tensión de línea.**
> $$V_L=\sqrt3\,V_F=\sqrt3\cdot230\approx400\ \text{V}.$$
>
> **Paso 2 — Corrientes.** Como cada línea es la prolongación de una rama, $I_L=I_F$.
>
> > [!solucion]
> > $V_L\approx400\ \text{V}$, $I_L=I_F$. Es la red doméstica habitual: $230\ \text{V}$ entre fase y neutro (monofásico) y $400\ \text{V}$ entre dos fases (trifásico).

---

## En qué consiste

> [!teoria] De dónde sale el $\sqrt3$
> La tensión de línea es la **diferencia** de dos tensiones de fase: $\overline{V}_{ab}=\overline{V}_a-\overline{V}_b$. Restando dos fasores de igual módulo $V_F$ separados $120^\circ$, el resultado tiene módulo $\sqrt3\,V_F$ y está adelantado $30^\circ$ respecto a $\overline{V}_a$:
> $$\overline{V}_{ab}=\overline{V}_a-\overline{V}_b=\sqrt3\,V_F\angle30^\circ.$$
> El $\sqrt3=2\cos30^\circ$ es pura geometría de la resta de dos vectores a $120^\circ$. La corriente, en cambio, no se reparte: la que sale de la rama es la misma que va por la línea, $I_L=I_F$.

> [!proposicion] El neutro y los cuatro hilos
> El punto común permite sacar un **cuarto conductor**, el **neutro**. Con carga **equilibrada**, la corriente del neutro es **cero** ($\overline{I}_a+\overline{I}_b+\overline{I}_c=0$), así que puede suprimirse (sistema a 3 hilos). Si la carga se **desequilibra**, el neutro lleva corriente y conviene mantenerlo. → [[Cargas Desbalanceadas Estrella]].

> [!info] Tensiones de la red
> En España/Europa, la red de baja tensión es $230/400\ \text{V}$: $230\ \text{V}$ de fase (alimenta cargas monofásicas) y $400\ \text{V}$ de línea ($=\sqrt3\cdot230$, para cargas trifásicas). Es exactamente una estrella con neutro.

> [!warning]
> No confundir **fase** con **línea**: en estrella el $\sqrt3$ está en las **tensiones** (la de línea es mayor), no en las corrientes. Y la tensión de línea **adelanta $30^\circ$** a la de fase: el factor $\sqrt3$ va siempre acompañado de ese desfase.

## Resumen

> [!resumen]
> | Magnitud | Relación (Y) |
> |:---|:---|
> | Tensiones | $V_L=\sqrt3\,V_F$ (línea $30^\circ$ adelante) |
> | Corrientes | $I_L=I_F$ |
> | Neutro | punto común; corriente $0$ si equilibrado |
> | Hilos | 3 o 4 (con neutro) |

> [!corolario]
> La estrella pone el $\sqrt3$ en las tensiones y ofrece un neutro. Es la conexión de la distribución de baja tensión (dos niveles, $230$ y $400\ \text{V}$, en la misma red). Su dual, el [[Conexion Triangulo| triángulo]], lo pone en las corrientes.

> [!referencia]
> Fraile Mora, cap. 3, §3.3. Dual: [[Conexion Triangulo]]. Combinaciones: [[Sistemas Y-Y, Delta-Delta, Y-Delta]]. Desequilibrio: [[Cargas Desbalanceadas Estrella]].
