---
title: Elementos Activos y Pasivos
tags:
  - circuitos-electricos
  - teoria
  - resistivos
  - clasificacion
draft: false
aliases:
  - elementos activos y pasivos
  - clasificación de elementos
  - elemento lineal
  - elemento bilateral
  - active and passive elements
  - linear element
---

# Elementos Activos y Pasivos

> [!definicion]
> Todo componente de un circuito es **activo** o **pasivo** según su balance de energía. Un elemento
> **pasivo** no puede entregar más energía de la que ha recibido: la **resistencia** la disipa, el
> [[Capacitor| condensador]] y el [[Inductor| inductor]] la almacenan y la devuelven. Un elemento
> **activo** —las **fuentes**— puede entregar energía neta al circuito. El criterio formal es
> **energético**, no depende de cómo esté conectado.

---

> [!info]
> Quinta nota de [[Elementos del Circuito/index| Elementos del circuito]], en el
> [[1 Conceptos Fundamentales y Resistivos/index| capítulo 1]]. Es la nota de **clasificación**:
> usa el convenio y la potencia de [[Potencia y Energia]], y reparte el detalle de cada elemento a
> [[Resistencia y Ley de Ohm]] y [[Fuentes Independientes]].

---

## Ejemplo

> [!ejemplo] Clasificar dos elementos por su energía
> Dos elementos en convenio pasivo. ¿Cuál es activo y cuál pasivo?
>
> **Elemento A** — una resistencia $R=100\ \Omega$ con $i=0.5\ \text{A}$:
> $$p_A=Ri^2=25\ \text{W}>0\ \text{(siempre)}\ \Rightarrow\
> \int_{-\infty}^{t}p_A\,d\tau\ge0.$$
> Nunca devuelve energía: absorbe en todo instante. Es **pasivo**.
>
> **Elemento B** — una fuente de $V_s=12\ \text{V}$ con corriente $i=3\ \text{A}$ que **sale** por su
> borne $+$: su potencia en convenio pasivo es
> $$p_B=-V_s\,i=-36\ \text{W}<0,$$
> es decir, **entrega** $36\ \text{W}$ al circuito. Su integral de potencia puede hacerse negativa:
> es **activo**.
>
> El signo de $p$ instante a instante, y sobre todo el de su **integral acumulada**, es lo que separa
> ambas clases.

---

## En qué consiste

> [!teoria] El criterio energético
> La distinción no es por la forma del símbolo, sino por la **energía**. En convenio pasivo, la
> energía absorbida por un elemento hasta el instante $t$ es
> $$W(t)=\int_{-\infty}^{t}p\,d\tau=\int_{-\infty}^{t}v\,i\,d\tau.$$
>
> - Un elemento es **pasivo** si **nunca** ha entregado más de lo que recibió, es decir, si para todo
>   $t$
>   $$\int_{-\infty}^{t}p\,d\tau\ge0.$$
>   La **resistencia** lo cumple de forma trivial ($p=Ri^2\ge0$ en cada instante: solo disipa). El
>   [[Capacitor| condensador]] y el [[Inductor| inductor]] **almacenan** energía ($\tfrac12 Cv^2$,
>   $\tfrac12 Li^2$) y pueden devolverla, pero **nunca más** de la almacenada: su energía guardada es
>   no negativa, así que también son pasivos.
> - Un elemento es **activo** si puede **violar** esa desigualdad, esto es, entregar energía neta. Las
>   **fuentes** independientes y dependientes son los elementos activos del curso.

> [!proposicion] Lineal, bilateral y otros adjetivos
> Más allá de activo/pasivo, los elementos se clasifican por propiedades de su característica:
>
> - **Lineal:** su relación $v$-$i$ cumple superposición (es una recta por el origen, como
>   $v=Ri$). Si la característica se curva (diodo) el elemento es **no lineal**. Todo este capítulo es
>   de circuitos **lineales**.
> - **Bilateral:** se comporta igual en ambos sentidos de la corriente; su característica es simétrica
>   respecto al origen. La resistencia es bilateral; el diodo, **unilateral**.
> - **Concentrado (parámetros agrupados):** se modela como un punto ideal ($R$, $L$, $C$, fuente), sin
>   tener en cuenta su tamaño físico —la hipótesis de trabajo de todo el curso—.

> [!warning]
> "Pasivo" **no** significa que nunca entregue corriente: un condensador cargado puede entregar
> energía durante un rato. Significa que **a lo largo del tiempo** no entrega más de la que recibió.
> El criterio es la **integral** de la potencia, no su signo en un instante aislado.

---

## Resumen

> [!resumen] Activos vs pasivos
> | | Pasivos | Activos |
> |:---|:---:|:---:|
> | Energía neta entregada | nunca ($\int_{-\infty}^{t}p\,d\tau\ge0$) | sí puede |
> | Ejemplos | resistencia, [[Capacitor\| condensador]], [[Inductor\| inductor]] | fuentes |
> | Papel | disipan o almacenan | entregan |
> | Lo detalla | [[Resistencia y Ley de Ohm]] | [[Fuentes Independientes]] |

> [!corolario]
> El criterio $\int_{-\infty}^{t}p\,d\tau\ge0$ unifica los tres pasivos (resistencia, condensador,
> inductor) bajo una sola idea: **nunca son fuente neta de energía**. Cada elemento se desarrolla en
> su propia nota; esta solo fija el mapa.

> [!referencia]
> Fraile Mora, cap. 1, §1.3–§1.5. Índice de la sección:
> [[Elementos del Circuito/index| Elementos del circuito]].
