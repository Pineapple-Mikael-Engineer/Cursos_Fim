---
title: Fuentes Reales
order: 4
tags:
  - circuitos-electricos
  - teoria
  - resistivos
  - fuentes
draft: false
aliases:
  - fuentes reales
  - resistencia interna
  - recta de carga
  - tensión en vacío
  - corriente de cortocircuito
  - real sources
  - internal resistance
  - load line
---

# Fuentes Reales (con resistencia interna)

> [!definicion]
> Una **fuente real** es el modelo físico de un generador: una fuente ideal acompañada de una **resistencia interna** que limita lo que puede entregar. Una **fuente de tensión real** es una fuente ideal $V_s$ **en serie** con una resistencia $R_s$, de modo que su tensión en bornes **cae** al aumentar la corriente
> $$v=V_s-R_s\,i.$$
> Una **fuente de corriente real** es una fuente ideal $I_s$ **en paralelo** con una resistencia $R_p$.

---

> [!info]
> Cuarta nota de [[Elementos del Circuito/index| Elementos del circuito]], en el [[1 Conceptos Fundamentales y Resistivos/index| capítulo 1]]. Vuelve físicas a las [[Fuentes Independientes]] ideales; las dos formas (serie / paralelo) son intercambiables por [[Transformacion de Fuentes]] y fijan el contexto de la [[Maxima Transferencia de Potencia]].

---

## Ejemplo

> [!ejemplo] Una batería cargada
> Una batería de tensión ideal $V_s=12\ \text{V}$ tiene resistencia interna $R_s=0.5\ \Omega$ y alimenta una carga $R_L=5.5\ \Omega$. ¿Qué corriente circula y qué tensión aparece en los bornes?
>
> **Paso 1 — un solo lazo en serie.** La fuente ideal, $R_s$ y $R_L$ están en serie, así que la misma corriente recorre todo. Por Kirchhoff de tensiones:
> $$V_s=R_s\,i+R_L\,i=(R_s+R_L)\,i.$$
>
> **Paso 2 — corriente.**
> $$i=\frac{V_s}{R_s+R_L}=\frac{12\ \text{V}}{0.5\ \Omega+5.5\ \Omega}
> =\frac{12}{6}=2\ \text{A}.$$
>
> **Paso 3 — tensión en bornes** (la que "ve" la carga):
> $$v_{term}=V_s-R_s\,i=12\ \text{V}-0.5\ \Omega\times 2\ \text{A}=12-1=11\ \text{V}.$$
>
> La batería **no** entrega sus $12\ \text{V}$ nominales: al circular corriente, $1\ \text{V}$ se pierde en su resistencia interna y a la carga llegan $11\ \text{V}$. Cuanto más se la exige (menor $R_L$, mayor $i$), más cae su tensión en bornes.

---

## En qué consiste

> [!teoria] Resistencia interna y recta de carga
> Ninguna fuente real mantiene su variable impuesta pase lo que pase; al cargarla, "cede" un poco. Ese comportamiento se captura con una **resistencia interna**:
>
> - **Fuente de tensión real:** ideal $V_s$ **en serie** con $R_s$. Su característica en bornes es
>   $$v=V_s-R_s\,i,$$
>   una **recta de carga** descendente: la tensión disponible disminuye linealmente con la corriente. Cuanto menor sea $R_s$, más se parece a la ideal (recta más plana).
> - **Fuente de corriente real:** ideal $I_s$ **en paralelo** con $R_p$. Parte de su corriente se desvía por $R_p$, de modo que la corriente entregada es
>   $$i=I_s-\frac{v}{R_p}.$$
>   Cuanto mayor sea $R_p$, menos corriente se fuga y más se parece a la ideal.

> [!proposicion] Vacío y cortocircuito: los dos extremos
> Dos puntos especiales de la recta de carga de la fuente de tensión real:
>
> - **Tensión en vacío** ($i=0$, carga desconectada): no circula corriente, no hay caída en $R_s$, y
>   $$v_{oc}=V_s.$$
>   Medir la fuente "en vacío" da directamente la tensión ideal $V_s$.
> - **Corriente de cortocircuito** ($v=0$, bornes unidos): toda la tensión cae en $R_s$, y
>   $$i_{sc}=\frac{V_s}{R_s}.$$
>   Es la **máxima** corriente que la fuente puede dar; finita gracias a $R_s$ (en la ideal sería infinita).
>
> Estos dos puntos —$(0,V_s)$ y $(i_{sc},0)$— determinan por completo la recta de carga, y de su cociente se lee la resistencia interna: $R_s=v_{oc}/i_{sc}$.

> [!warning]
> La caída interna **no es despreciable** cuando la corriente es alta o $R_s$ comparable a $R_L$: es la causa de que las luces del coche "bajen" al arrancar el motor (gran $i$, gran caída en $R_s$). Modelar la fuente como ideal en esos casos da tensiones equivocadas.

---

## Resumen

> [!resumen] Las dos fuentes reales
> | | Tensión real | Corriente real |
> |:---|:---:|:---:|
> | Estructura | $V_s$ **en serie** con $R_s$ | $I_s$ **en paralelo** con $R_p$ |
> | Característica | $v=V_s-R_s\,i$ | $i=I_s-v/R_p$ |
> | En vacío ($i=0$) | $v_{oc}=V_s$ | $v_{oc}=I_s R_p$ |
> | En cortocircuito ($v=0$) | $i_{sc}=V_s/R_s$ | $i_{sc}=I_s$ |
> | Ideal cuando | $R_s\to 0$ | $R_p\to\infty$ |

> [!corolario]
> Las dos formas son **equivalentes** vistas desde sus bornes si $V_s=I_s R_p$ y $R_s=R_p$: esa identidad es la base de la [[Transformacion de Fuentes]] y permite cambiar una por otra según convenga al análisis.

> [!referencia]
> Fraile Mora, cap. 1, §1.9. Continúa con [[Transformacion de Fuentes]] y [[Maxima Transferencia de Potencia]].
