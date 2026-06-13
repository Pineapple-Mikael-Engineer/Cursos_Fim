---
title: Ley de Corrientes de Kirchhoff (LKC)
tags:
  - circuitos-electricos
  - teoria
  - resistivos
  - kirchhoff
  - nodos
draft: false
aliases:
  - Ley de Corrientes LKC
  - Primer lema de Kirchhoff
  - Kirchhoff's Current Law
  - KCL
---

# Ley de Corrientes de Kirchhoff $\sum_k i_k=0$

> [!definicion]
> La **ley de corrientes de Kirchhoff (LKC)** —primer lema— establece que en todo **nodo** de un
> circuito la suma algebraica de las corrientes es nula en cada instante:
> $$\sum_{k} i_k = 0.$$
> Dicho de otro modo, **la suma de corrientes que entran al nodo es igual a la suma de las que
> salen**. Es consecuencia directa de la **conservación de la carga**: en el nodo no se acumula ni
> se crea carga.

> [!info]
> Primer lema de la sección [[Leyes de Kirchhoff/index| Leyes de Kirchhoff]], dentro del
> [[1 Conceptos Fundamentales y Resistivos/index| capítulo 1]]. Complementa a la
> [[Ley de Voltajes LKV]] (suma de tensiones en una malla). Es el fundamento del
> [[Analisis de Nodos]]; el número de ecuaciones LKC útiles lo fija
> [[Ecuaciones Independientes]]. Fraile Mora, cap. 1, §1.8.

---

## Ejemplo

> [!ejemplo]
> **Nodo con cuatro ramas; tres corrientes conocidas, hallar la cuarta.**
>
> A un nodo llegan $i_1 = 3\ \text{A}$ e $i_2 = 2\ \text{A}$ (entrantes) y sale $i_3 = 4\ \text{A}$.
> Se desconoce $i_4$, dibujada como saliente. Determinar $i_4$.
>
> ![[kirchhoff_nodo.svg|360]]
>
> *Nodo con corrientes entrantes y salientes: $i_1+i_2=i_3+i_4$.*
>
> **Paso 1 — Convención de signos.** Se toman como **positivas las entrantes** y negativas las
> salientes. La LKC exige
> $$\sum_k i_k = 0 \;\Longrightarrow\; i_1 + i_2 - i_3 - i_4 = 0.$$
>
> **Paso 2 — Despejar la incógnita.**
> $$i_4 = i_1 + i_2 - i_3 = 3 + 2 - 4 = 1\ \text{A}.$$
>
> > [!solucion]
> > $i_4 = 1\ \text{A}$, **saliente** (el signo positivo confirma el sentido supuesto). Se verifica
> > el balance: entra $i_1+i_2=5\ \text{A}$, sale $i_3+i_4=4+1=5\ \text{A}$. Lo que entra, sale.
>
> Si el resultado hubiese salido negativo, el sentido real de $i_4$ sería el opuesto al dibujado; el
> método funciona igual y el signo lo corrige automáticamente.

---

## En qué consiste

> [!teoria] La carga no se acumula en un nodo
> Un **nodo** es un punto de conexión de dos o más ramas. La corriente es el flujo de carga,
> $i = \dfrac{dq}{dt}$. Si en el nodo se acumulara carga, su potencial crecería sin límite; en un
> conductor ideal eso no ocurre, de modo que la carga que entra por unidad de tiempo debe igualar a
> la que sale. Esa igualdad de flujos, instante a instante, es exactamente la LKC.
>
> La ley es **lineal** y **no depende de los elementos** conectados: vale igual con resistencias,
> condensadores, inductores o en régimen sinusoidal. Solo se afirma algo sobre las **corrientes** en
> el nodo, no sobre qué hay en cada rama.

> [!algoritmo] Aplicar la LKC en un nodo
> **Paso 1 — Fijar la convención.** Elegir un signo para las corrientes entrantes (p. ej. $+$) y el
> opuesto para las salientes ($-$). Mantenerla en todo el circuito.
>
> **Paso 2 — Asignar sentidos.** Dibujar una flecha de sentido supuesto en cada rama incidente. El
> sentido puede ser arbitrario; el signo del resultado lo corregirá.
>
> **Paso 3 — Escribir la suma.** Sumar con su signo cada corriente del nodo e igualar a cero:
> $\sum_k i_k = 0$.
>
> **Paso 4 — Repetir** en los nodos necesarios. De un circuito con $n$ nodos solo $n-1$ ecuaciones
> LKC son independientes (la del último nodo es combinación de las demás); ver
> [[Ecuaciones Independientes]].

> [!teorema] Forma de conservación de la carga
> Para cualquier superficie cerrada $S$ que no encierre acumulación de carga, la corriente neta que
> la atraviesa es nula:
> $$\sum_{k \,\in\, S} i_k = 0.$$

> [!demostracion]
> **Paso 1 — Conservación de la carga.** La carga total $q_S$ encerrada por $S$ cumple, por
> continuidad, $\dfrac{dq_S}{dt} = -\,i_{\text{neta, saliente}}$, donde $i_{\text{neta, saliente}}$
> es la corriente que sale por $S$.
>
> **Paso 2 — Régimen sin acumulación.** En los nudos de un circuito de parámetros concentrados la
> carga no se almacena ($q_S$ constante), luego $\dfrac{dq_S}{dt}=0$.
>
> **Paso 3 — Conclusión.** Entonces $i_{\text{neta, saliente}}=0$, es decir, la suma algebraica de
> las corrientes que cruzan $S$ es cero. Tomando $S$ alrededor de un único nodo se recupera
> $\sum_k i_k = 0$. $\blacksquare$

---

> [!proposicion] Supernodo: la LKC sobre una superficie cerrada
> La LKC no se limita a un punto: vale para **cualquier superficie cerrada** que englobe varios
> nodos. Esa superficie se llama **supernodo**. Toda la región interior se trata como un único nodo,
> y la suma de las corrientes que cruzan su frontera es cero. Es la herramienta para nodos unidos por
> una fuente de tensión en el [[Analisis de Nodos]], donde la rama interior queda oculta dentro del
> supernodo.

> [!warning]
> El signo de cada corriente depende del **sentido supuesto en su flecha**, no de su valor. Antes de
> sumar hay que fijar qué sentido se considera entrante. Un valor negativo en la solución no es un
> error: significa que el sentido real es contrario al dibujado.

---

## Resumen

> [!resumen]
> | Concepto | Expresión |
> |:---|:---|
> | Ley (forma nodal) | $\sum_k i_k = 0$ |
> | Entrantes vs. salientes | $\sum i_{\text{entra}} = \sum i_{\text{sale}}$ |
> | Origen físico | conservación de la carga, $i=dq/dt$ |
> | Convención | entrantes $+$ / salientes $-$ (o al revés, consistente) |
> | Supernodo | $\sum i_k = 0$ sobre una superficie cerrada |
> | Ecuaciones independientes | $n-1$ para $n$ nodos |

> [!corolario]
> La LKC convierte la topología de un circuito en ecuaciones: una por nodo (menos uno). Junto con la
> [[Ley de Voltajes LKV]] y la ley de Ohm $v=Ri$, basta para resolver cualquier red resistiva. Su
> aplicación sistemática es, precisamente, el [[Analisis de Nodos]].

> [!referencia]
> Fraile Mora, cap. 1, §1.8 (primer lema de Kirchhoff). Lema dual:
> [[Ley de Voltajes LKV]]. Conteo de ecuaciones: [[Ecuaciones Independientes]].
