---
title: Balance de Potencias (Teorema de Tellegen)
order: 4
tags:
  - circuitos-electricos
  - teoria
  - resistivos
  - kirchhoff
  - potencia
draft: false
aliases:
  - Balance de Potencias
  - Conservación de la potencia
  - Teorema de Tellegen
  - Power balance
  - Tellegen's theorem
---

# Balance de Potencias $\sum_k v_k i_k = 0$

> [!definicion]
> En todo circuito la **potencia total entregada por las fuentes iguala la potencia total disipada o absorbida por el resto de los elementos**:
> $$\sum p_{\text{entregada}} = \sum p_{\text{absorbida}}.$$
> En convenio pasivo y sumando sobre **todas** las ramas, esto se escribe de forma compacta como
> $$\sum_{k} v_k\, i_k = 0,$$
> el **teorema de Tellegen**. Es una consecuencia conjunta de la [[Ley de Corrientes LKC]] y la [[Ley de Voltajes LKV]], y se usa sobre todo para **verificar** una solución ya obtenida.

> [!info]
> Cuarta nota de la sección [[Leyes de Kirchhoff/index| Leyes de Kirchhoff]], dentro del [[1 Conceptos Fundamentales y Resistivos/index| capítulo 1]]. La definición de $p = vi$, el convenio pasivo y la energía se tratan en [[Potencia y Energia]]; aquí se aplica a la red completa. Combina [[Ley de Corrientes LKC]] y [[Ley de Voltajes LKV]]. Fraile Mora, cap. 1, §1.10.

---

## Ejemplo

> [!ejemplo]
> **Verificar el balance en la malla serie ya resuelta.**
>
> Del circuito de la [[Ley de Voltajes LKV]]: fuente $V = 10\ \text{V}$, $R_1 = 3\ \Omega$, $R_2 = 2\ \Omega$ en serie, con solución $i = 2\ \text{A}$, $v_{R_1} = 6\ \text{V}$, $v_{R_2} = 4\ \text{V}$. Comprobar que la potencia de la fuente iguala la disipada.
>
> **Paso 1 — Potencia entregada por la fuente.** La corriente sale por el borne $+$ de la fuente (entrega energía):
> $$P_{\text{fuente}} = V\,i = 10 \cdot 2 = 20\ \text{W}.$$
>
> **Paso 2 — Potencia disipada en cada resistencia.** Con $p = Ri^2$ (convenio pasivo, absorbe):
> $$P_{R_1} = R_1 i^2 = 3 \cdot 2^2 = 12\ \text{W}, \qquad P_{R_2} = R_2 i^2 = 2 \cdot 2^2 = 8\ \text{W}.$$
>
> **Paso 3 — Balance.**
> $$P_{R_1} + P_{R_2} = 12 + 8 = 20\ \text{W} = P_{\text{fuente}}.$$
>
> > [!solucion]
> > $\sum P_{\text{absorbida}} = 20\ \text{W} = P_{\text{fuente}}$. El balance cierra: toda la potencia entregada por la fuente se disipa en las resistencias. Equivalentemente, con la fuente en convenio pasivo ($p=-20\ \text{W}$, entrega): $\sum_k v_k i_k = -20 + 12 + 8 = 0$.
>
> Comprobar también con $P_{R_k} = v_{R_k}^2 / R_k$: $6^2/3 = 12\ \text{W}$ y $4^2/2 = 8\ \text{W}$. Iguales: la solución es consistente.

---

## En qué consiste

> [!teoria] La potencia se conserva porque la carga y la energía se conservan
> El convenio pasivo asigna a cada rama $p_k = v_k i_k$: positivo si la rama **absorbe**, negativo si **entrega**. Una fuente típicamente entrega ($p<0$); una resistencia siempre absorbe ($p = Ri^2 > 0$). El teorema de Tellegen afirma que, sumando sobre **todas** las ramas, el total es cero: la energía que sale de las fuentes se reparte entre los elementos absorbentes, sin pérdidas ni creación.
>
> Lo notable es que el resultado depende **solo de la topología** (de la LKC y la LKV), no de qué elemento haya en cada rama. Por eso vale para circuitos resistivos, reactivos o no lineales, y en cualquier instante.

> [!teorema] Teorema de Tellegen
> Sean $\{v_k\}$ un conjunto de tensiones de rama que satisface la LKV y $\{i_k\}$ un conjunto de corrientes de rama que satisface la LKC, sobre el mismo grafo orientado de $b$ ramas. Entonces
> $$\sum_{k=1}^{b} v_k\, i_k = 0.$$

> [!demostracion]
> **Paso 1 — Expresar las tensiones por potenciales de nodo.** Como $\{v_k\}$ cumple la LKV, existe un potencial de nodo $V_a$ tal que la tensión de la rama $k$ entre los nodos $a$ y $b$ es $v_k = V_a - V_b$ (consecuencia de [[Ley de Voltajes LKV]]).
>
> **Paso 2 — Sustituir en la suma.**
> $$\sum_k v_k i_k = \sum_k (V_a - V_b)\, i_k = \sum_{\text{nodos } a} V_a \!\!\sum_{k \text{ inc. en } a} (\pm i_k).$$
> Al agrupar por nodos, cada potencial $V_a$ multiplica a la suma algebraica de las corrientes que inciden en ese nodo.
>
> **Paso 3 — Aplicar la LKC.** Por la [[Ley de Corrientes LKC]], la suma de corrientes en cada nodo es nula: $\sum_{k \text{ inc. en } a} (\pm i_k) = 0$.
>
> **Paso 4 — Conclusión.** Cada término del sumatorio sobre nodos es $V_a \cdot 0 = 0$, luego $\sum_k v_k i_k = 0$. La potencia total instantánea es cero: lo entregado iguala lo absorbido. $\blacksquare$

---

> [!proposicion] Uso como verificación
> El balance de potencias es la prueba de consistencia más usada tras resolver un circuito: se calcula la potencia entregada por cada fuente y la absorbida por cada elemento; si $\sum p_{\text{entregada}} \neq \sum p_{\text{absorbida}}$, hay un error en la solución. Para resistencias conviene usar las tres formas equivalentes:
> $$P_R = R i^2 = \frac{v_R^2}{R} = v_R\, i.$$

> [!warning]
> El teorema de Tellegen exige que $\{v_k\}$ e $\{i_k\}$ provengan del **mismo grafo** y cumplan respectivamente LKV y LKC, pero **no** que pertenezcan al mismo circuito ni al mismo instante: el producto $v_k i_k$ puede no tener entonces sentido físico de potencia. Para la **conservación de la potencia real**, tensiones y corrientes deben ser las del mismo circuito en el mismo instante; ese es el caso del balance de potencias ordinario.

---

## Resumen

> [!resumen]
> | Concepto | Expresión |
> |:---|:---|
> | Balance | $\sum p_{\text{entregada}} = \sum p_{\text{absorbida}}$ |
> | Tellegen (todas las ramas) | $\sum_k v_k i_k = 0$ |
> | Potencia de una resistencia | $P_R = R i^2 = v_R^2/R = v_R i$ |
> | Potencia de una fuente (entrega) | $P = V i$ (sale por $+$) |
> | Validez | cualquier instante; depende solo de LKC + LKV |
> | Uso típico | verificar una solución |

> [!corolario]
> El balance de potencias no aporta una ecuación nueva e independiente —ya está contenido en LKC y LKV—, pero es la comprobación final imprescindible: si las potencias no cuadran, la solución es errónea. Es la traducción energética de las dos leyes de Kirchhoff.

> [!referencia]
> Fraile Mora, cap. 1, §1.10 (balance de potencias). Definición de potencia y convenio pasivo: [[Potencia y Energia]]. Leyes de partida: [[Ley de Voltajes LKV]] y [[Ley de Corrientes LKC]].
