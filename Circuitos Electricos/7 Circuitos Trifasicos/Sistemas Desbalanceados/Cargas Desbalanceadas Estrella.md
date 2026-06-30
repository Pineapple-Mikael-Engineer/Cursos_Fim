---
title: Cargas Desbalanceadas en Estrella
order: 1
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
> En una **estrella desequilibrada**, las tres impedancias de fase son distintas, así que las tres corrientes difieren y **ya no suman cero**. Lo que pasa depende de **cómo se una el neutro de la carga $N'$ con el de la fuente $N$**:
> - **Con neutro (4 hilos)** —el caso **normal y útil** en distribución—: el conductor neutro fuerza $\overline{V}_{N'N}=0$, **fija** la tensión de cada fase en su valor nominal y recoge el desbalance, $\overline{I}_N=\overline{I}_a+\overline{I}_b+\overline{I}_c\neq0$. Cada fase se resuelve como un monofásico independiente.
> - **Caso general**: $N'$ se une a $N$ por una **impedancia de neutro** $Z_N$ (la del propio conductor, nunca nula). El neutro ideal ($Z_N=0$) y el caso **sin neutro** ($Z_N\to\infty$, 3 hilos) son sus dos **extremos**; en ambos y en el intermedio, el desplazamiento $\overline{V}_{N'N}$ sale por [[Teorema de Millman| Millman]].

> [!info]
> El caso desequilibrado de la [[Conexion Estrella| conexión estrella]], en [[Sistemas Desbalanceados/index| sistemas desbalanceados]] ([[7 Circuitos Trifasicos/index| capítulo 7]]). Muestra **para qué sirve el neutro** —y qué pasa cuando falta o se rompe—. Fraile Mora, cap. 3, §3.10.

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

> [!teoria] Con neutro (4 hilos): el caso útil de la distribución
> Este es el montaje **real** de la red de baja tensión que alimenta cargas desiguales (viviendas, oficinas). El conductor neutro une $N'$ con $N$ y, al ser de muy baja impedancia, **fija** la tensión de cada fase de la carga en su valor nominal línea-neutro **aunque las impedancias difieran**. Por eso cada fase se resuelve **por separado**, como un monofásico: $\overline{I}_k=\overline{V}_k/Z_k$. Las tres corrientes ya no se cancelan, y su desbalance **retorna por el neutro**:
> $$\overline{I}_N=\overline{I}_a+\overline{I}_b+\overline{I}_c\neq0.$$
> Esa es la función del neutro y por qué es **imprescindible** en distribución desequilibrada: garantiza que cada carga reciba sus $230\ \text{V}$ pase lo que pase en las otras dos fases. Cuanto mayor el desbalance, más corriente de neutro.

> [!teoria] El caso general: neutro a través de una impedancia $Z_N$
> En realidad el neutro **nunca** tiene impedancia nula (el conductor tiene su resistencia, y a veces se intercala una $Z_N$ deliberada). El montaje general une $N'$ y $N$ por una admitancia $Y_N=1/Z_N$, y el desplazamiento del neutro de la carga se obtiene por **Millman** incluyendo ese término:
> $$\overline{V}_{N'N}=\frac{\overline{V}_a Y_a+\overline{V}_b Y_b+\overline{V}_c Y_c}{Y_a+Y_b+Y_c+Y_N},\qquad Y_k=\tfrac1{Z_k}.$$
> Conocida $\overline{V}_{N'N}$, cada corriente es $\overline{I}_k=(\overline{V}_k-\overline{V}_{N'N})\,Y_k$ y por el neutro circula $\overline{I}_N=\overline{V}_{N'N}\,Y_N$. Los dos casos típicos son **límites** de esta fórmula:
> - **Neutro ideal** ($Z_N\to0$, $Y_N\to\infty$): $\overline{V}_{N'N}\to0$ → tensiones fijas e $\overline{I}_N=\sum\overline{I}_k$ (el caso de 4 hilos de arriba).
> - **Sin neutro** ($Z_N\to\infty$, $Y_N=0$): desaparece el término $Y_N$ y queda el Millman a 3 hilos. → [[Teorema de Millman]].
> - **$Z_N$ finita**: el neutro reduce el desplazamiento pero no lo anula del todo; es el caso real de un neutro con resistencia apreciable.

> [!teorema] Sin neutro o neutro roto: el punto común se desplaza
> Si no hay neutro ($Y_N=0$) —o si **se rompe** el conductor de neutro—, el punto común de la carga $N'$ deja de estar al potencial de $N$ y "flota":
> $$\overline{V}_{N'N}=\frac{\overline{V}_a Y_a+\overline{V}_b Y_b+\overline{V}_c Y_c}{Y_a+Y_b+Y_c}.$$
> ¿Cuándo es esto **útil de verdad**? En dos situaciones muy reales: (1) los sistemas a **3 hilos** sin neutro (alimentación entre transformadores, líneas de transporte, [[Motores Electricos Trifasicos| motores]] trifásicos —cuyo punto estrella flota por diseño—); y (2) el análisis de **averías**: una carga equilibrada con el neutro **roto** se vuelve, de hecho, una estrella desequilibrada a 3 hilos. Por eso este caso no es académico: es el que predice qué pasa cuando el neutro falla.

> [!warning]
> El **neutro roto** es un peligro real, no un ejercicio: al perderse, las tensiones de las cargas se **desplazan** (unas suben muy por encima de su valor nominal, otras caen), lo que **quema** los equipos sobretensionados. Por eso el neutro se protege y nunca se le pone fusible. Dos avisos de cálculo: con neutro ideal el equivalente **por fase no vale** (hay que resolver las tres por separado); y sin neutro, antes de las corrientes hay que hallar siempre $\overline{V}_{N'N}$ por Millman.

## Resumen

> [!resumen]
> | Caso | Neutro | Cómo se resuelve |
> |:---|:---|:---|
> | 4 hilos (ideal) | $Z_N=0$ | cada fase aparte; $\overline{I}_N=\sum\overline{I}_k$ |
> | General | $Z_N$ finita | Millman con $Y_N$: $\overline{V}_{N'N}$, luego $\overline{I}_k$ |
> | 3 hilos / neutro roto | $Z_N\to\infty$ | Millman sin $Y_N$; $N'$ flota |
> | Corriente de neutro | — | $0$ solo si está equilibrado |

> [!corolario]
> Todo se resume en un único método —el **desplazamiento de neutro de Millman** con la admitancia $Y_N$— del que los casos habituales son límites: con neutro ideal ($Y_N\to\infty$) las tensiones quedan fijas y solo importa $\overline{I}_N=\sum\overline{I}_k$; sin neutro ($Y_N=0$) el punto común flota. El neutro es lo que cierra el desbalance y protege la tensión de cada carga: esa es la razón física de que la distribución de baja tensión sea a **cuatro hilos** —y de que su rotura sea peligrosa—.

> [!referencia]
> Fraile Mora, cap. 3, §3.10. Equilibrado: [[Conexion Estrella]]. Herramienta: [[Teorema de Millman]]. Método general: [[Componentes Simetricas]].
