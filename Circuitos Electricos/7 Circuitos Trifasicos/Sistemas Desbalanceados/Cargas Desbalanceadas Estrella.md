---
title: Cargas Desbalanceadas en Estrella
tags:
  - circuitos-electricos
  - teoria
  - trifasico
draft: false
aliases:
  - cargas desbalanceadas estrella
  - estrella desequilibrada
  - corriente de neutro
  - unbalanced wye
---

# Cargas Desbalanceadas en Estrella

> [!definicion]
> En una **estrella desequilibrada**, las tres impedancias de fase son distintas, así que las tres corrientes difieren y **ya no suman cero**. Con **neutro** (4 hilos), cada fase es independiente, $\overline{I}_k=\overline{V}_k/Z_k$, y el neutro conduce su suma:
> $$\overline{I}_N=\overline{I}_a+\overline{I}_b+\overline{I}_c\neq0.$$
> **Sin neutro** (3 hilos), el punto común de la carga se **desplaza** y su tensión se halla por [[Teorema de Millman| Millman]].

> [!info]
> El caso desequilibrado de la [[Conexion Estrella| conexión estrella]], en [[Sistemas Desbalanceados/index| sistemas desbalanceados]] ([[7 Circuitos Trifasicos/index| capítulo 7]]). Muestra para qué sirve el neutro. Fraile Mora, cap. 3, §3.10.

---

## Ejemplo

> [!ejemplo]
> **Corriente por el neutro.**
>
> Una estrella **con neutro** a tensión de fase $230\ \text{V}$ ($\overline{V}_a=230\angle0^\circ$, $\overline{V}_b=230\angle{-}120^\circ$, $\overline{V}_c=230\angle{+}120^\circ$) alimenta tres cargas resistivas desiguales: $Z_a=23\ \Omega$, $Z_b=46\ \Omega$, $Z_c=23\ \Omega$. Hallar la corriente del neutro.
>
> **Paso 1 — Corrientes de fase** (cada una independiente):
> $$\overline{I}_a=\tfrac{230\angle0^\circ}{23}=10\angle0^\circ,\quad \overline{I}_b=\tfrac{230\angle{-}120^\circ}{46}=5\angle{-}120^\circ,\quad \overline{I}_c=\tfrac{230\angle{+}120^\circ}{23}=10\angle{+}120^\circ\ \text{A}.$$
>
> **Paso 2 — Corriente de neutro** (suma fasorial):
> $$\overline{I}_N=10\angle0^\circ+5\angle{-}120^\circ+10\angle{+}120^\circ=(2{,}5)+j(4{,}33)=5\angle60^\circ\ \text{A}.$$
>
> > [!solucion]
> > $\overline{I}_N=5\angle60^\circ\ \text{A}$. Como las cargas son desiguales, el neutro lleva corriente (sería cero si las tres $Z$ fueran iguales).

---

## En qué consiste

> [!teoria] Con neutro: tres monofásicos independientes
> El conductor neutro **fija** la tensión de cada fase de la carga en su valor (línea-neutro), aunque las impedancias difieran. Por eso cada fase se resuelve **por separado**, como un circuito monofásico, y el neutro recoge el desbalance: $\overline{I}_N=\sum\overline{I}_k$. Esa es su función —garantizar la tensión de cada carga— y por eso en distribución desequilibrada (viviendas) el neutro es imprescindible.

> [!teorema] Sin neutro: desplazamiento del punto común
> Si no hay neutro, el punto común de la carga $N'$ ya no está al potencial del neutro de la fuente $N$: aparece una tensión de desplazamiento $\overline{V}_{N'N}$, que se calcula por **Millman**:
> $$\overline{V}_{N'N}=\frac{\overline{V}_a Y_a+\overline{V}_b Y_b+\overline{V}_c Y_c}{Y_a+Y_b+Y_c},\qquad Y_k=\tfrac1{Z_k}.$$
> Conocida ella, cada corriente es $\overline{I}_k=(\overline{V}_k-\overline{V}_{N'N})\,Y_k$. → [[Teorema de Millman]].

> [!warning]
> **Sin neutro**, una carga desequilibrada recibe tensiones de fase **distintas** de las nominales (por el desplazamiento): unas se sobretensionan y otras se quedan bajas, lo que puede dañar equipos. El neutro evita ese problema. Y el equivalente **por fase no vale** aquí: hay que resolver las tres.

## Resumen

> [!resumen]
> | Caso | Cómo se resuelve |
> |:---|:---|
> | Con neutro (4 hilos) | cada fase aparte; $\overline{I}_N=\sum\overline{I}_k$ |
> | Sin neutro (3 hilos) | Millman: $\overline{V}_{N'N}$, luego $\overline{I}_k$ |
> | Corriente de neutro | $0$ solo si está equilibrado |

> [!corolario]
> En estrella desequilibrada, el neutro es el que cierra el desbalance y protege las tensiones de cada carga. Sin él, el punto común se desplaza y hay que recurrir a Millman. Es la razón física de que la distribución de baja tensión sea a **cuatro hilos**.

> [!referencia]
> Fraile Mora, cap. 3, §3.10. Equilibrado: [[Conexion Estrella]]. Herramienta: [[Teorema de Millman]]. Método general: [[Componentes Simetricas]].
