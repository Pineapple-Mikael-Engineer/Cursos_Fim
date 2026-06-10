---
title: Fasores Eléctricos
tags:
  - circuitos-electricos
  - teoria
  - fasores
draft: false
aliases:
  - fasores eléctricos
  - fasores en R L C
  - desfase en elementos
---

# Fasores Eléctricos: $v$ e $i$ en R, L y C

> [!definicion]
> En régimen sinusoidal, la tensión y la corriente de cada elemento guardan una **relación de fase
> fija**, visible al representarlas como fasores: en la **resistencia** van **en fase**; en el
> **inductor** la tensión **adelanta** $90^\circ$ a la corriente; en el **condensador** la corriente
> **adelanta** $90^\circ$ a la tensión. Ese desfase es lo que la [[Impedancia Compleja| impedancia]]
> resume en un factor $j$.

> [!info]
> Aplica la [[Representacion de Fasores| representación fasorial]] a los elementos, dentro de la
> sección [[Fasores/index| Fasores]] ([[5 Circuitos AC Sinusoidal y Fasores/index| capítulo 5]]). Es
> el puente directo hacia la [[Impedancia y Admitancia/index| impedancia]]. Fraile Mora, cap. 2, §2.6.

---

## Ejemplo

> [!ejemplo]
> **Las tres relaciones de fase.**
>
> Por los tres elementos circula la misma corriente $\overline{I}=I\angle0^\circ$. ¿Qué fase tiene la
> tensión en cada uno?
>
> ![[fasores_RLC.svg|640]]
>
> *Resistencia: $\overline{V}$ e $\overline{I}$ alineados (en fase). Inductor: $\overline{V}$ a
> $90^\circ$ por delante de $\overline{I}$. Condensador: $\overline{I}$ a $90^\circ$ por delante de
> $\overline{V}$.*
>
> **Resistencia.** $\overline{V}_R=R\,\overline{I}=RI\angle0^\circ$: misma fase que $\overline{I}$.
>
> **Inductor.** $\overline{V}_L=j\omega L\,\overline{I}=\omega L I\angle90^\circ$: el factor $j$
> **adelanta** la tensión $90^\circ$.
>
> **Condensador.** $\overline{V}_C=\dfrac{\overline{I}}{j\omega C}=\dfrac{I}{\omega C}\angle(-90^\circ)$:
> la tensión **atrasa** $90^\circ$, o sea la corriente adelanta.
>
> > [!solucion]
> > $\overline{V}_R$ en fase; $\overline{V}_L$ adelantada $90^\circ$; $\overline{V}_C$ atrasada
> > $90^\circ$ respecto a $\overline{I}$. El cociente $\overline{V}/\overline{I}$ es la
> > [[Impedancia Compleja| impedancia]] de cada elemento.

---

## En qué consiste

> [!teoria] De dónde sale cada desfase
> El desfase nace de las leyes $v$–$i$ al pasar al fasor (donde $d/dt\to j\omega$):
> - **Resistencia:** $v=Ri\Rightarrow\overline{V}=R\,\overline{I}$. No hay $j$: **en fase**.
> - **Inductor:** $v=L\dfrac{di}{dt}\Rightarrow\overline{V}=j\omega L\,\overline{I}$. El $j$ adelanta la
>   tensión $90^\circ$: la corriente "se resiste" a cambiar y va **por detrás**.
> - **Condensador:** $i=C\dfrac{dv}{dt}\Rightarrow\overline{I}=j\omega C\,\overline{V}$, luego
>   $\overline{V}=\overline{I}/(j\omega C)$: la tensión va por detrás, la **corriente adelanta**
>   $90^\circ$.

> [!regla] La regla mnemotécnica "ELI the ICE man"
> En el inductor (**L**), la tensión **E** va antes que la corriente **I**: **E-L-I**. En el
> condensador (**C**), la corriente **I** va antes que la tensión **E**: **I-C-E**. Un truco para no
> confundir quién adelanta a quién.

> [!proposicion] El desfase y la energía
> Que en R no haya desfase y en L, C sí, tiene un significado físico: la resistencia **disipa** (tensión
> y corriente "tiran a la vez"), mientras que $L$ y $C$ solo **almacenan y devuelven** energía (el
> desfase de $90^\circ$ hace que la potencia media sea cero en ellos). Esto es la semilla de la
> [[Potencia en Elementos Puros| potencia en elementos puros]].

> [!warning]
> El adelanto/atraso es **relativo** entre $v$ e $i$ del mismo elemento; depende de cuál se tome como
> referencia. Lo invariable: en $L$, $v$ e $i$ están a $90^\circ$ con la tensión delante; en $C$, a
> $90^\circ$ con la corriente delante; en $R$, a $0^\circ$.

## Resumen

> [!resumen]
> | Elemento | Relación fasorial | Desfase $v$ respecto a $i$ |
> |:---|:---|:---|
> | Resistencia | $\overline{V}=R\,\overline{I}$ | $0^\circ$ (en fase) |
> | Inductor | $\overline{V}=j\omega L\,\overline{I}$ | $+90^\circ$ ($v$ adelanta) |
> | Condensador | $\overline{V}=\dfrac{\overline{I}}{j\omega C}$ | $-90^\circ$ ($v$ atrasa) |

> [!corolario]
> Cada elemento impone un desfase fijo entre tensión y corriente: $0^\circ$, $+90^\circ$ o $-90^\circ$.
> Codificar ese desfase en un número complejo —el factor $j$— es precisamente la
> [[Impedancia Compleja| impedancia]], el siguiente paso.

> [!referencia]
> Fraile Mora, cap. 2, §2.6. Base: [[Representacion de Fasores]]. Continúa en:
> [[Impedancia Compleja]] y [[Potencia en Elementos Puros]].
