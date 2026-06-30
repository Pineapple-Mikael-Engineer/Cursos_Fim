---
title: Nodos con Fuentes de Voltaje
tags:
  - circuitos-electricos
  - teoria
  - metodos-analisis
  - nodos
draft: false
aliases:
  - supernodo
  - nodos con fuentes de tensión
  - método del supernodo
  - supernode
---

# Nodos con Fuentes de Voltaje

> [!definicion]
> Cuando una **fuente de tensión** une dos nodos directamente (sin resistencia en serie), **no** se puede escribir la [[Ley de Corrientes LKC| LKC]] de cada nodo por separado: la corriente que atraviesa la fuente es una **incógnita** y no se expresa con la ley de Ohm. La técnica del **supernodo** engloba ambos nodos en una **superficie cerrada** y aplica la LKC al **conjunto** (donde esa corriente desconocida no aparece), añadiendo la **restricción** $V_1-V_2=V_s$ que impone la fuente.

> [!info]
> Caso especial del [[Analisis de Nodos]], dentro de [[Metodos de Analisis/index| Métodos de análisis]] del [[2 Metodos de Analisis y Teoremas/index| capítulo 2]]. Es el **dual** de la [[Mallas con Fuentes de Corriente| supermalla]]. La restricción es un caso de las [[Ecuaciones de Restriccion| ecuaciones de restricción]]. Fraile Mora, cap. 1, §1.13.

---

## Ejemplo

> [!ejemplo]
> **Supernodo con dos fuentes de corriente.**
>
> Hallar $V_1$ y $V_2$. Los nodos $1$ y $2$ están unidos por una fuente de tensión $V_s=2\ \text{V}$ (terminal $+$ en el nodo $1$). A masa cuelgan $R_1=1\ \Omega$ (nodo $1$) y $R_2=1\ \Omega$ (nodo $2$). Inyectan corriente las fuentes $I_{s1}=3\ \text{A}$ (entra al nodo $1$) e $I_{s2}=1\ \text{A}$ (entra al nodo $2$).
>
> ![[supernodo.svg|470]]
>
> *La fuente $V_s$ une los nodos 1 y 2: se engloban en un supernodo (a trazos) y se aplica la LKC al conjunto.*
>
> **Paso 1 — Restricción de la fuente.** El terminal $+$ está en el nodo $1$, luego la fuente fija la diferencia de potenciales:
> $$V_1 - V_2 = V_s = 2.$$
>
> **Paso 2 — LKC del supernodo.** Englobando ambos nodos en una superficie cerrada, la corriente por la fuente queda **interna** y se cancela. La corriente **inyectada** por las fuentes iguala a la que **sale** por las dos resistencias a masa:
> $$I_{s1}+I_{s2} = \frac{V_1}{R_1} + \frac{V_2}{R_2} \;\Longrightarrow\; 3+1 = V_1 + V_2
> \;\Longrightarrow\; V_1 + V_2 = 4.$$
>
> **Paso 3 — Resolver.** Sumando y restando $V_1-V_2=2$ y $V_1+V_2=4$:
> $$V_1 = 3\ \text{V}, \qquad V_2 = 1\ \text{V}.$$
>
> > [!solucion]
> > $V_1 = 3\ \text{V}$, $V_2 = 1\ \text{V}$. Comprobación de la restricción: $V_1-V_2=3-1=2=V_s$. La corriente por la fuente (incógnita que evitamos) se recupera ahora con la LKC de un nodo aislado: en el nodo $2$, $I_{s2} + i_{V_s} = V_2/R_2 \Rightarrow i_{V_s}=1-1=0\ \text{A}$.

---

## En qué consiste

> [!teoria] Por qué falla la LKC nodo a nodo y por qué el supernodo la salva
> En el análisis de nodos cada corriente de rama se escribe con la ley de Ohm a partir de las tensiones de nodo, $(V_j-V_k)/R$. Una **fuente de tensión** rompe esa receta: fija la diferencia $V_1-V_2$ pero **no** la corriente que la atraviesa, que pasa a ser una incógnita extra. Si se escribiera la LKC del nodo $1$ por separado, esa corriente desconocida $i_{V_s}$ aparecería y no podría despejarse. La solución es **englobar** los dos nodos en una superficie cerrada (el supernodo): la corriente de la fuente entra y sale de la misma región, es **interna**, y la LKC del conjunto **no la contiene**. Perdemos una ecuación (ya no hay dos LKC independientes, sino una), pero la **restricción** $V_1-V_2=V_s$ que aporta la fuente la repone: el cómputo de incógnitas y ecuaciones vuelve a cuadrar.
>
> Si **un terminal** de la fuente es la **masa**, no hace falta supernodo: el otro nodo queda con tensión **conocida** directamente ($V=\pm V_s$) y deja de ser incógnita.

> [!algoritmo] Método del supernodo
> **Paso 1 — Detectar.** Localizar toda **fuente de tensión entre dos nodos no-referencia** (sin resistencia en serie).
>
> **Paso 2 — Restricción.** Escribir $V_1 - V_2 = V_s$, con el signo según qué terminal ($+$) toca cada nodo.
>
> **Paso 3 — LKC del supernodo.** Trazar una superficie cerrada que englobe **ambos** nodos y plantear la LKC del conjunto: corriente inyectada por las fuentes $=$ corriente que sale por todas las resistencias que cruzan la frontera. La corriente de la fuente interna no aparece.
>
> **Paso 4 — Resolver** el sistema (restricción + LKC del supernodo + LKC del resto de nodos).

> [!warning]
> No escribas la LKC de un nodo individual **atravesado** por la fuente de tensión: introducirías la corriente desconocida de la fuente. Usa siempre el **supernodo**. Si la fuente está **en serie con una resistencia**, conviene una [[Transformacion de Fuentes| transformación de fuente]] previa que la convierte en fuente de corriente y elimina la necesidad del supernodo.

## Resumen

> [!resumen]
> | Aspecto | Supernodo |
> |:---|:---|
> | Problema | fuente de $V$ entre dos nodos: $i_{V_s}$ desconocida |
> | Idea | englobar ambos nodos en una superficie cerrada |
> | LKC del conjunto | $\sum I_{s} = \sum V_k/R$ (la $i_{V_s}$ es interna) |
> | Ecuación que falta | restricción $V_1 - V_2 = V_s$ |
> | Si un terminal es masa | el otro nodo tiene $V$ conocida; sin supernodo |
> | Dual | [[Mallas con Fuentes de Corriente\| supermalla]] |

> [!corolario]
> El supernodo y la supermalla son la **misma idea por dualidad**: una variable de rama queda impuesta por la fuente (tensión en nodos, corriente en mallas) mientras su conjugada (corriente por la fuente, tensión sobre ella) se vuelve incógnita; agrupar elementos elimina esa incógnita y la fuente repone la ecuación con su restricción.

> [!referencia]
> Fraile Mora, cap. 1, §1.13. Caso general: [[Analisis de Nodos]]. Dual: [[Mallas con Fuentes de Corriente]]. La restricción, en [[Ecuaciones de Restriccion]].
