---
title: Ley de Voltajes de Kirchhoff (LKV)
tags:
  - circuitos-electricos
  - teoria
  - resistivos
  - kirchhoff
  - mallas
draft: false
aliases:
  - Ley de Voltajes LKV
  - Ley de Tensiones de Kirchhoff
  - Segundo lema de Kirchhoff
  - Kirchhoff's Voltage Law
  - KVL
---

# Ley de Voltajes de Kirchhoff $\sum_k v_k=0$

> [!definicion]
> La **ley de voltajes de Kirchhoff (LKV)** —segundo lema— establece que al recorrer una **malla** (camino cerrado) de un circuito, la suma algebraica de las tensiones es nula en cada instante:
> $$\sum_{k} v_k = 0.$$
> Equivalentemente, **la suma de las subidas de tensión (fuentes) iguala la suma de las caídas** (elementos pasivos). Es consecuencia directa de la **conservación de la energía**: la energía por unidad de carga recobra su valor al volver al punto de partida.

> [!info]
> Segundo lema de la sección [[Leyes de Kirchhoff/index| Leyes de Kirchhoff]], dentro del [[1 Conceptos Fundamentales y Resistivos/index| capítulo 1]]. Lema dual de la [[Ley de Corrientes LKC]] (suma de corrientes en un nodo). Es el fundamento del [[Analisis de Mallas]] y, aplicada a un divisor, justifica el [[Divisor de Voltaje]]. Fraile Mora, cap. 1, §1.8.

---

## Ejemplo

> [!ejemplo]
> **Una malla es una "ventana": la LKV en un circuito de dos mallas.**
>
> El circuito tiene dos fuentes, $U_{s1} = 8\ \text{V}$ y $U_{s2} = 13\ \text{V}$, y tres resistencias, $R_1 = 1\ \Omega$, $R_2 = 2\ \Omega$, $R_3 = 3\ \Omega$. Posee **dos mallas** —las dos ventanas $a$ y $b$, que comparten la rama central $R_2$— y la LKV se cumple **en cada una**. Hallar las corrientes de rama $i_1$, $i_2$, $i_3$.
>
> ![[circuito_dos_mallas.svg|470]]
>
> *Una malla no es un lazo aislado: es cada ventana de la red. Aquí hay dos ($a$ y $b$) y la LKV vale alrededor de ambas.*
>
> **Paso 1 — Corrientes y recorrido.** Se asignan $i_1$, $i_2$, $i_3$ con los sentidos del dibujo y se recorre cada malla en sentido **horario**. En convenio pasivo, cada resistencia recorrida a favor de su corriente aporta una **caída** $-R\,i$.
>
> **Paso 2 — LKV en la malla $a$** (ventana izquierda: $U_{s1}$, $R_1$, $R_2$):
> $$-U_{s1} + R_1 i_1 + R_2 i_2 = 0 \;\Longrightarrow\; 1\,i_1 + 2\,i_2 = 8.$$
>
> **Paso 3 — LKV en la malla $b$** (ventana derecha: $R_2$, $R_3$, $U_{s2}$):
> $$R_2 i_2 + R_3 i_3 + U_{s2} = 0 \;\Longrightarrow\; 2\,i_2 + 3\,i_3 = -13.$$
>
> **Paso 4 — LKC en el nodo $A$** (cierra el sistema): lo que entra iguala a lo que sale,
> $$i_1 + i_3 = i_2.$$
>
> **Paso 5 — Resolver.** Sustituyendo $i_2 = i_1 + i_3$ en las dos ecuaciones de malla:
> $$i_1 = 6\ \text{A}, \qquad i_2 = 1\ \text{A}, \qquad i_3 = -5\ \text{A}.$$
>
> > [!solucion]
> > $i_1 = 6\ \text{A}$, $i_2 = 1\ \text{A}$, $i_3 = -5\ \text{A}$. El signo negativo de $i_3$ avisa de que su sentido real es el opuesto al dibujado. Verificación de la LKV en la malla $a$: $R_1 i_1 + R_2 i_2 = 6 + 2 = 8\ \text{V} = U_{s1}$. La resolución sistemática de estas ecuaciones es el [[Analisis de Mallas]]; el reparto de potencias de este mismo circuito está en [[Balance de Potencias]].

---

## En qué consiste

> [!teoria] La energía por unidad de carga es de circulación nula
> Una **malla** es un camino cerrado de ramas que no encierra otras ramas. La tensión $v_k$ de un elemento es la energía que gana o pierde la unidad de carga al atravesarlo. Al completar el lazo y regresar al punto inicial, la carga recupera su potencial original: lo ganado en las fuentes (subidas) se ha gastado en los elementos pasivos (caídas). La suma de todos los $v_k$, con su signo, es por tanto cero.
>
> ![[kirchhoff_malla.svg|540]]
>
> *Una malla cualquiera dentro de una red mayor: se recorre el lazo cerrado $A\to B\to C\to D\to A$ con elementos de cualquier tipo, y los **muñones** de cada nodo son las demás ramas de la red, que no intervienen en esta LKV. Al completar el recorrido, $\sum_k u_k = 0$.*
>
> Como la LKC, la ley es **lineal** y **no depende del tipo de elemento**: rige igual en circuitos resistivos, con almacenamiento de energía o en régimen sinusoidal. Solo cambia la relación $v$–$i$ de cada rama (Ohm, $L\,di/dt$, $1/C\!\int i\,dt$, o $Z$ fasorial).

> [!algoritmo] Aplicar la LKV en una malla
> **Paso 1 — Elegir el sentido de recorrido.** Por convención, **horario**. Mantenerlo en todas las mallas del circuito.
>
> **Paso 2 — Asignar sentidos de corriente.** Suponer una corriente de malla; con convenio pasivo, la tensión de una resistencia recorrida a favor de $i$ es una **caída** $-Ri$.
>
> **Paso 3 — Recorrer y sumar.** Al cruzar cada elemento, sumar su tensión con signo:
> - **subida** ($-$ a $+$, típicamente una fuente que aporta energía): $+v_k$;
> - **caída** ($+$ a $-$, un elemento que absorbe): $-v_k$.
>
> **Paso 4 — Igualar a cero.** $\sum_k v_k = 0$. Resolver para las corrientes de malla. De un circuito de $b$ ramas y $n$ nodos solo $b-n+1$ mallas son independientes; ver [[Ecuaciones Independientes]].

> [!teorema] Forma de conservación de la energía
> Para cualquier camino cerrado (malla) de un circuito de parámetros concentrados,
> $$\oint v \;=\; \sum_k v_k = 0.$$

> [!demostracion]
> **Paso 1 — Potencial de nodo.** En un circuito de parámetros concentrados cada nodo tiene un potencial bien definido $V_a$. La tensión de la rama entre los nodos $a$ y $b$ es la diferencia de potencial $v_{ab} = V_a - V_b$.
>
> **Paso 2 — Recorrer la malla.** Sea la malla la secuencia de nodos $a \to b \to c \to \cdots \to a$. Sumando las tensiones de rama a lo largo del lazo:
> $$\sum_k v_k = (V_a - V_b) + (V_b - V_c) + \cdots + (V_z - V_a).$$
>
> **Paso 3 — Cancelación telescópica.** Cada potencial de nodo aparece una vez con signo $+$ y otra con signo $-$, de modo que la suma colapsa a $V_a - V_a = 0$.
>
> **Paso 4 — Conclusión.** Por tanto $\sum_k v_k = 0$ a lo largo de toda malla. La existencia de un potencial de nodo único es la expresión circuital de la conservación de la energía. $\blacksquare$

---

> [!proposicion] La LKV genera el divisor de tensión
> En una malla serie con una sola fuente y **sin ramas intermedias** (todas las resistencias comparten la misma corriente $i = V/\sum_j R_j$), la LKV reparte la tensión total proporcionalmente a cada resistencia: $v_{R_k} = V \dfrac{R_k}{\sum_j R_j}$. Es el [[Divisor de Voltaje]].

> [!warning]
> El signo de cada $v_k$ depende del **sentido de recorrido** y de la **polaridad** $\pm$ marcada en el elemento, no de su valor. Hay que fijar el recorrido antes de sumar. Una corriente o tensión negativa en la solución indica solo que el sentido o la polaridad reales son los opuestos a los supuestos.

---

## Resumen

> [!resumen]
> | Concepto | Expresión |
> |:---|:---|
> | Ley (forma de malla) | $\sum_k v_k = 0$ |
> | Subidas vs. caídas | $\sum v_{\text{subida}} = \sum v_{\text{caída}}$ |
> | Origen físico | conservación de la energía (potencial de nodo único) |
> | Convención | recorrido horario; subida $+$, caída $-$ |
> | Serie ($R_1,\dots$) | $i = V / \sum_j R_j$; $v_{R_k} = R_k i$ |
> | Mallas independientes | $b - n + 1$ para $b$ ramas y $n$ nodos |

> [!corolario]
> La LKV traduce cada lazo del circuito en una ecuación de tensiones. Junto con la [[Ley de Corrientes LKC]] y la ley de Ohm $v = Ri$, cierra el sistema que resuelve toda red resistiva. Su aplicación sistemática es el [[Analisis de Mallas]].

> [!referencia]
> Fraile Mora, cap. 1, §1.8 (segundo lema de Kirchhoff). Lema dual: [[Ley de Corrientes LKC]]. Aplicación inmediata: [[Divisor de Voltaje]].
