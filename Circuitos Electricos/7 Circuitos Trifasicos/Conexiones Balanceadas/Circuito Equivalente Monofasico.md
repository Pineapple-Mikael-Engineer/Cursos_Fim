---
title: Circuito Equivalente Monofásico
tags:
  - circuitos-electricos
  - teoria
  - trifasico
draft: false
aliases:
  - equivalente por fase
  - circuito por fase
  - per-phase analysis
  - per-phase equivalent circuit
---

# Circuito Equivalente Monofásico (por fase)

> [!definicion]
> En un sistema trifásico **equilibrado**, las tres fases son idénticas salvo un desfase de $120^\circ$, de modo que **no hace falta resolver las tres**: basta analizar **una sola fase** —el **circuito equivalente monofásico** o **por fase**— y obtener las otras dos rotando $\mp120^\circ$. Se toma la fase $a$ con su retorno por el neutro, llevando todo a estrella:
> $$\overline{I}_a=\frac{\overline{V}_{an}}{Z},\qquad \overline{I}_b=\overline{I}_a\angle{-}120^\circ,\qquad \overline{I}_c=\overline{I}_a\angle{+}120^\circ.$$

> [!info]
> Es el **atajo de cálculo** de las [[Conexiones Balanceadas/index| conexiones balanceadas]] del [[7 Circuitos Trifasicos/index| capítulo 7]]: convierte cualquier [[Sistemas Y-Y, Delta-Delta, Y-Delta| combinación Y/Δ]] en un circuito monofásico simple. Es la base del cálculo de [[Potencia en Sistemas Balanceados| potencia trifásica]]. Fraile Mora, cap. 3, §3.5.

---

## Ejemplo

> [!ejemplo]
> **Corriente de línea por el equivalente por fase.**
>
> Un sistema equilibrado Y-Y tiene tensión de fase $\overline{V}_{an}=230\angle0^\circ\ \text{V}$ y carga por fase $Z=10+j10=14{,}14\angle45^\circ\ \Omega$ (impedancia de línea despreciable). Hallar la corriente de línea.
>
> **Paso 1 — Pasar a Y.** Ya está en estrella; no hay nada que convertir.
>
> **Paso 2 — Equivalente por fase.** Una sola malla fase-neutro:
> $$\overline{I}_a=\frac{\overline{V}_{an}}{Z}=\frac{230\angle0^\circ}{14{,}14\angle45^\circ}=16{,}3\angle{-}45^\circ\ \text{A}.$$
>
> **Paso 3 — Las otras dos fases.** Mismas magnitudes, desfasadas $\mp120^\circ$:
> $$\overline{I}_b=16{,}3\angle{-}165^\circ\ \text{A},\qquad \overline{I}_c=16{,}3\angle75^\circ\ \text{A}.$$
>
> > [!solucion]
> > $\overline{I}_a=16{,}3\angle{-}45^\circ\ \text{A}$; basta una fase para conocer las tres. Las demás salen sumando $-120^\circ$ (fase $b$) y $+120^\circ$ (fase $c$) sin recalcular nada.

---

## En qué consiste

> [!teoria] Por qué basta una fase
> Por la simetría del sistema equilibrado, las tres corrientes tienen igual módulo y están separadas $120^\circ$:
> $$\overline{I}_b=\overline{I}_a\angle{-}120^\circ,\qquad \overline{I}_c=\overline{I}_a\angle{+}120^\circ.$$
> Su suma es **nula**, así que el neutro **no lleva corriente** y su tensión es la misma en ambos extremos. Eso permite "cortar" el circuito por el neutro —imaginar un conductor ideal de impedancia nula entre los dos neutros— y quedarse con **una sola malla fase-neutro**. Toda carga o fuente en Δ se pasa antes a su equivalente en Y ($Z_Y=Z_\Delta/3$). El equivalente por fase usa **siempre** tensión de **fase** (línea-neutro) e impedancia de **fase** en Y.

> [!algoritmo] Método de la fase única
> 1. **Pasar todo a Y.** Convertir cargas y fuentes en triángulo: $Z_\Delta\to Z_\Delta/3$.
> 2. **Dibujar una sola fase.** Fuente de fase $\overline{V}_{an}$, impedancia de línea $Z_L$ y de carga $Z_Y$ en serie, retorno por el neutro.
> 3. **Resolver esa malla.** $\overline{I}_a=\dfrac{\overline{V}_{an}}{Z_{\text{total}}}$, con $Z_{\text{total}}=Z_L+Z_Y$.
> 4. **Obtener las otras fases** con $\mp120^\circ$ y, si se pide, pasar a magnitudes de **línea** o a las ramas reales del Δ con el factor $\sqrt3$.

> [!proposicion] Alcance del método
> El equivalente por fase **solo** es válido bajo **equilibrio** (tensiones de fuente y cargas iguales en las tres fases). A cambio, reduce el problema trifásico a uno monofásico, **dividiendo el trabajo por tres**: una sola ecuación en lugar de tres mallas acopladas.

> [!warning]
> Usar tensión de **fase** (no de línea) y la impedancia en **Y** (convertir Δ antes con $Z_Y=Z_\Delta/3$). El resultado del equivalente da magnitudes **por fase**; para pasarlas a línea se aplica el factor $\sqrt3$ según la conexión. **No** aplicar este método si el sistema está [[Sistemas Y-Y, Delta-Delta, Y-Delta| desequilibrado]]: ahí el neutro lleva corriente y las tres fases deben resolverse por separado.

## Resumen

> [!resumen]
> | Paso | Acción |
> |:---|:---|
> | Condición | Sistema **equilibrado** (única hipótesis) |
> | Reducir | Pasar todo a Y ($Z_\Delta\to Z_\Delta/3$) |
> | Tomar | Fase $a$-$n$ con retorno por el neutro |
> | Resolver | $\overline{I}_a=\overline{V}_{an}/Z$ (tensión e impedancia de **fase**) |
> | Completar | Otras fases a $\mp120^\circ$; a línea con $\sqrt3$ |

> [!corolario]
> El circuito equivalente monofásico es la herramienta de trabajo de todo sistema trifásico equilibrado: resuelve una malla fase-neutro y rota $\mp120^\circ$ para las demás. Conviene la [[Conexion Estrella]] porque expone directamente el neutro; cualquier [[Sistemas Y-Y, Delta-Delta, Y-Delta| combinación Y/Δ]] se reduce a este caso, y sobre él se monta el cálculo de [[Potencia en Sistemas Balanceados| potencia trifásica]].

> [!referencia]
> Fraile Mora, cap. 3, §3.5. Conexión base: [[Conexion Estrella]]. Combinaciones: [[Sistemas Y-Y, Delta-Delta, Y-Delta]]. Aplicación: [[Potencia en Sistemas Balanceados]]. Índices: [[Conexiones Balanceadas/index]], [[7 Circuitos Trifasicos/index]].
