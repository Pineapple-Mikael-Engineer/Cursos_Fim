---
title: Simetría en Circuitos
tags:
  - circuitos-electricos
  - teoria
  - resistivos
  - simetria
draft: false
aliases:
  - simetría en circuitos
  - nodos equipotenciales
  - plano de simetría
  - circuit symmetry
  - equipotential nodes
---

# Simetría en Circuitos $V_i=V_j\Rightarrow$ unir o separar

> [!definicion]
> Explotar la **simetría** consiste en reconocer, antes de calcular nada, que ciertos nodos de la red están al **mismo potencial** por la geometría del circuito y la simetría de la excitación. Dos nodos equipotenciales pueden **unirse** (cortocircuitarse) o **separarse** sin alterar ninguna tensión ni corriente, porque entre ellos no circula corriente. Esta observación reduce drásticamente el número de ramas independientes y convierte cálculos imposibles a mano en sumas inmediatas de serie y paralelo.

---

> [!info]
> Nota de la sección [[Reduccion de Circuitos/index| Reducción de circuitos]], dentro del [[1 Conceptos Fundamentales y Resistivos/index| capítulo 1]]. Es el **Paso 3** del método [[RINCE]]: buscar simetrías antes de reducir. Complementa a [[Resistencias en Serie y Paralelo]] (lo que se aplica una vez simplificado) y a [[Estrella Triangulo Kennelly]] (la otra forma de destrabar redes sin serie ni paralelo evidentes).

---

## Ejemplo

> [!ejemplo] Resistencia entre vértices opuestos de un cubo de $12$ resistencias
> El problema clásico: un **cubo** cuyas $12$ aristas son resistencias iguales de valor $R$. Buscamos $R_{eq}$ entre dos **vértices opuestos** $a$ y $b$ (los extremos de la diagonal del cubo). A mano, sin simetría, exigiría resolver un sistema grande. Con simetría, se hace en tres pasos.
>
> **Paso 1 — Inyectar corriente y clasificar nodos.** Hacemos entrar una corriente $i$ por $a$ y salir por $b$. Por la simetría triple del cubo respecto a la diagonal $a$-$b$:
> - Los **tres** vértices vecinos de $a$ son equivalentes: están al **mismo potencial**. Llamémoslos grupo $A$.
> - Los **tres** vértices vecinos de $b$ son equivalentes entre sí: grupo $B$, todos al mismo potencial.
>
> **Paso 2 — Unir los equipotenciales.** Como dentro de $A$ todos los nodos están al mismo potencial, podemos **unirlos** en un solo nodo (no circula corriente entre ellos); igual con $B$. El cubo se aplana en tres tramos en serie:
> - de $a$ al nodo $A$: las $3$ aristas que salen de $a$ están en **paralelo**, $\dfrac{R}{3}$;
> - de $A$ a $B$: las $6$ aristas centrales en **paralelo**, $\dfrac{R}{6}$;
> - de $B$ a $b$: las $3$ aristas que llegan a $b$ en **paralelo**, $\dfrac{R}{3}$.
>
> **Paso 3 — Sumar en serie.**
> $$R_{eq}=\frac{R}{3}+\frac{R}{6}+\frac{R}{3}=\frac{2R+R+2R}{6}=\frac{5R}{6}.$$
>
> > [!solucion]
> > $R_{eq}=\dfrac{5}{6}R$ entre vértices opuestos del cubo. La simetría reduce $12$ resistencias a tres paralelos en serie: $\frac{R}{3}+\frac{R}{6}+\frac{R}{3}$.

---

## En qué consiste

> [!teoria] Por qué un nodo equipotencial se puede tocar sin que pase nada
> La corriente por una resistencia es $i=(V_i-V_j)/R$. Si dos nodos están al **mismo potencial**, $V_i=V_j$, entonces **no circula corriente** por ninguna conexión que se establezca entre ellos. Por eso hay total libertad para **unirlos** con un cortocircuito (un cable de $0\ \Omega$ no transporta nada si sus extremos están al mismo potencial) o para **separarlos** (cortar una rama que no lleva corriente no cambia nada). Ambas operaciones dejan **invariantes** todas las tensiones y corrientes del resto del circuito, así que el equivalente $R_{eq}$ no cambia.

> [!teorema] Criterio de simetría
> Si una transformación geométrica del circuito (reflexión respecto a un **plano de simetría**, rotación, permutación de ramas) deja **invariantes** tanto la topología de la red como la posición de la excitación (los terminales por donde entra y sale la corriente), entonces los nodos que se **intercambian** entre sí bajo esa transformación están al **mismo potencial**.

> [!demostracion]
> **Paso 1 — La simetría aplica al circuito completo.** Sea $S$ una simetría que deja invariantes la red y la fuente. Aplicada a la **solución** (el conjunto de potenciales nodales), produce otra solución del mismo problema.
>
> **Paso 2 — Unicidad.** Una red resistiva con excitación dada tiene solución **única** de potenciales. Como $S$ transforma una solución en una solución del mismo problema, ambas deben coincidir.
>
> **Paso 3 — Igualdad de potenciales.** Por tanto, si $S$ lleva el nodo $i$ al nodo $j$, la unicidad obliga a $V_i=V_j$. Esos nodos son equipotenciales y pueden unirse o separarse. $\blacksquare$

> [!proposicion] Plano de simetría: cuándo unir y cuándo separar
> Sobre el **plano de simetría** que pasa entre los dos terminales pueden caer ramas o nodos:
> - Un nodo que el plano deja **a un lado** tiene su espejo al otro lado, al mismo potencial → se pueden **unir**.
> - Una rama que el plano **cruza por su mitad** y conecta dos nodos espejo no lleva corriente neta a través del plano → en problemas antisimétricos puede **separarse** (abrirse) sin alterar nada. Saber cuál de las dos operaciones aplicar depende de si la excitación es simétrica o antisimétrica respecto al plano.

> [!warning] Condición indispensable
> La simetría debe cumplirse **a la vez** en la red **y** en la excitación. Una red perfectamente simétrica deja de poder simplificarse así si la corriente entra y sale por terminales que **rompen** esa simetría. Comprobar siempre las dos cosas antes de unir o separar nodos; en caso de duda, asignar potenciales literales $V_i$ y verificar la igualdad.

---

## Resumen

> [!resumen] Simetría de un vistazo
> | Situación | Operación | Justificación |
> |:---|:---|:---|
> | $V_i=V_j$ (nodos espejo) | unir (cortocircuitar) | no circula corriente entre ellos |
> | Rama cruzada por el plano, caso antisimétrico | separar (abrir) | no lleva corriente neta |
> | Cubo, vértices opuestos | $R_{eq}=\dfrac{R}{3}+\dfrac{R}{6}+\dfrac{R}{3}$ | grupos equipotenciales $A$, $B$ |
> | Resultado del cubo | $R_{eq}=\dfrac{5}{6}R$ | tres paralelos en serie |

> [!corolario]
> La simetría no calcula $R_{eq}$ por sí sola, pero **prepara el terreno**: tras unir o separar los nodos equipotenciales, lo que quedaba como una maraña irreducible se convierte casi siempre en una cadena de [[Resistencias en Serie y Paralelo]] inmediata. Por eso es el primer reflejo dentro de [[RINCE]].

> [!referencia]
> Fraile Mora, cap. 1, §1.10. Se combina con [[RINCE]], [[Resistencias en Serie y Paralelo]] y [[Estrella Triangulo Kennelly]].
