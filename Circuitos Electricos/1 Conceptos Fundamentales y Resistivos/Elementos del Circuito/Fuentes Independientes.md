---
title: Fuentes Independientes
order: 2
tags:
  - circuitos-electricos
  - teoria
  - resistivos
  - fuentes
draft: false
aliases:
  - fuentes independientes
  - fuente de tensión ideal
  - fuente de corriente ideal
  - independent sources
  - ideal voltage source
  - ideal current source
---

# Fuentes Independientes: $v=V_s$ e $i=I_s$

> [!definicion]
> Una **fuente independiente** es un elemento activo que **impone** un valor —de tensión o de corriente— al circuito, fijado por sí misma y **sin depender** de ninguna otra variable. La **fuente de tensión ideal** garantiza una tensión $v=V_s$ en sus bornes sea cual sea la corriente que la atraviese; la **fuente de corriente ideal** garantiza una corriente $i=I_s$ por ella sea cual sea la tensión que aparezca en sus bornes.

---

> [!info]
> Segunda nota de [[Elementos del Circuito/index| Elementos del circuito]], en el [[1 Conceptos Fundamentales y Resistivos/index| capítulo 1]]. Es el elemento **activo** que complementa a la [[Resistencia y Ley de Ohm]]. Su versión física aparece en [[Fuentes Reales]] y su versión controlada en [[Fuentes Dependientes]].

---

## Ejemplo

> [!ejemplo] Fuente de tensión alimentando una resistencia
> Una **fuente de tensión ideal** de $V_s=12\ \text{V}$ alimenta una resistencia $R=4\ \Omega$. Determinamos la corriente del circuito.
>
> ![[simbolos_fuentes.svg|420]]
> Izq.: fuente de tensión ideal. Der.: fuente de corriente ideal.
>
> La fuente impone $v=V_s=12\ \text{V}$ en bornes de $R$. Por la ley de Ohm:
> $$i=\frac{v}{R}=\frac{12\ \text{V}}{4\ \Omega}=3\ \text{A}.$$
>
> La potencia entregada por la fuente y absorbida por la resistencia es
> $$p=V_s\,i=12\ \text{V}\times 3\ \text{A}=36\ \text{W}.$$
>
> Si la resistencia fuese $R=2\ \Omega$, la fuente **seguiría** imponiendo $12\ \text{V}$, pero ahora daría $i=6\ \text{A}$: la fuente ideal mantiene su tensión y **entrega la corriente que haga falta**.

---

## En qué consiste

> [!teoria] Dos elementos que imponen, no que reaccionan
> A diferencia de la resistencia —que **reacciona** a lo que se le aplica según $v=Ri$—, una fuente independiente **impone** una variable y deja libre la otra:
>
> - **Fuente de tensión ideal.** Fija $v=V_s$ (constante en CC, o $v=v_s(t)$ en general). La corriente que circula por ella la decide **el resto del circuito**, no la fuente. En el plano $v$-$i$ su característica es una **recta horizontal** en $v=V_s$: la tensión no cambia aunque la corriente varíe.
>
> - **Fuente de corriente ideal.** Fija $i=I_s$. La tensión en sus bornes la decide **el resto del circuito**. En el plano $v$-$i$ su característica es una **recta vertical** en $i=I_s$: la corriente no cambia aunque la tensión varíe.
>
> En símbolos, la de tensión suele dibujarse como un círculo con $+/-$ (o las barras de batería) y la de corriente como un círculo con una flecha que marca el sentido de $I_s$.

> [!proposicion] La fuente entrega potencia (signo activo)
> En convenio pasivo $p=vi>0$ significa absorber. Una fuente normalmente **entrega** energía: si la corriente sale por su borne $+$, su potencia en convenio pasivo es negativa, es decir, **entrega** $p_{ent}=V_s\,i$ al circuito. Es la razón de llamarla elemento **activo**. (Una fuente puede también absorber: una batería en carga recibe potencia del circuito.)

> [!warning]
> Las fuentes ideales describen casos límite **no físicos**:
> - **Cortocircuitar** una fuente de tensión ideal ($R=0$) exigiría corriente infinita.
> - **Dejar en circuito abierto** una fuente de corriente ideal exigiría tensión infinita.
>
> Por eso **nunca** se ponen dos fuentes de tensión ideales distintas en paralelo, ni dos de corriente ideales distintas en serie: serían contradictorias. La [[Fuentes Reales| resistencia interna]] es lo que vuelve físico el modelo.

---

## Resumen

> [!resumen] Tensión vs corriente ideal
> | | Fuente de tensión ideal | Fuente de corriente ideal |
> |:---|:---:|:---:|
> | Impone | $v=V_s$ | $i=I_s$ |
> | Variable libre | la corriente $i$ | la tensión $v$ |
> | Característica $v$-$i$ | recta **horizontal** | recta **vertical** |
> | Resistencia interna ideal | $0$ (serie) | $\infty$ (paralelo) |
> | Caso límite prohibido | cortocircuito | circuito abierto |

> [!corolario]
> Una fuente **ideal** mantiene su variable impuesta **pase lo que pase** con la carga. Esa rigidez es precisamente lo que la realidad no permite: toda fuente verdadera "cede" un poco al cargarla, y ese comportamiento se modela en [[Fuentes Reales]].

> [!referencia]
> Fraile Mora, cap. 1, §1.5. Continúa con [[Fuentes Reales]] y [[Fuentes Dependientes]].
