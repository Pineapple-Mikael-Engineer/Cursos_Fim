---
title: Notación de Índices en Sumatorias
tags:
  - matemáticas
  - álgebra-lineal
  - notación
  - sumatorias
  - cálculo-tensorial
draft: false
---

# Notación de Índices en Sumatorias

La [[notación de índices]] (o notación de Einstein) es un sistema poderoso para trabajar con sumatorias múltiples, especialmente en [[álgebra lineal]] y [[cálculo tensorial]].

## Índices Mudos y Libres

Cuando se representa una suma de variables, por lo general se acostumbra a usar el [[Símbolo de sumatoria|Sigma]] (∑) para la representación de una serie:

$$
a_{1}x_{1} + a_{2}x_{2} + a_{3}x_{3} + \dots + a_{n}x_{n} = \sum_{i = 1} ^{n} a_{i}x_{i}
$$

En el segundo miembro, la expresión queda simplemente como $a_{i} x_{i}$, donde $1 \leq i \leq n$. Este índice $i$ es un *[[índice mudo]]* que recorre todos los valores posibles.

> [!teoria] Definición: Índices Libres y Mudos
> En una expresión con sumatorias:
> - Un **[[índice mudo]]** (dummy index) aparece **repetido** en un mismo término y sobre él se realiza la sumatoria.
> - Un **índice libre** (free index) aparece **una sola vez** en cada término y debe tomar el mismo valor en todos los términos de una ecuación.

> [!example] Ejemplo 1: Distinguiendo índices
> En la expresión $S = a_{i} x_{i}$:
> - $i$ es **mudo** — aparece dos veces, indicando suma sobre $i$
> - El resultado $S$ no tiene índices libres (es un [[escalar]])
>
> En la ecuación $b_{j} = a_{ji} x_{i}$:
> - $j$ es **libre** — aparece una vez, generando $n$ ecuaciones ($j=1,2,\dots,n$)
> - $i$ es **mudo** — aparece dos veces en el lado derecho

> [!example] Ejemplo 2: Sistema de ecuaciones lineales
> El sistema:
> $$
> \begin{cases}
> 2x_1 + 3x_2 = 5 \\
> 4x_1 + 6x_2 = 7
> \end{cases}
> $$
> Puede escribirse como $A_{ij}x_j = b_i$, donde:
> - $i$ es **libre** ($i=1,2$ representa cada ecuación)
> - $j$ es **mudo** (suma sobre $j=1,2$)
>
> Explícitamente: $A_{1j}x_j = A_{11}x_1 + A_{12}x_2 = 2x_1 + 3x_2 = b_1$

> [!remark] Observación 1: Renombramiento de índices mudos
> Un índice mudo puede renombrarse a cualquier otra letra que no esté siendo utilizada:
> $$
> \sum_{i=1}^{n} a_i x_i = \sum_{k=1}^{n} a_k x_k
> $$
> Esto es análogo a renombrar la variable de integración en una [[integral definida]]: $\int_a^b f(x)dx = \int_a^b f(t)dt$.

> [!remark] Observación 2: [[Convenio de sumación de Einstein|Convenio de Einstein]]
> En la notación de Einstein (o convenio de sumación), se omite el símbolo de la sumatoria y se asume la suma sobre todo índice que aparece repetido en un mismo término. Por ejemplo, $a_i x_i$ implica sumatoria sobre $i$.

## Doble Suma

La suma sobre dos índices, uno para $x$ y otro para $y$, se expande como:

$$
\begin{aligned}
a_{ij} x_{i} y_{j} &= a_{1j}x_{1}y_{j} + a_{2j}x_{2}y_{j} + a_{3j}x_{3}y_{j} + \dots + a_{nj}x_{n}y_{j} \\
& = \left( a_{11}x_{1}y_{1} + a_{12}x_{1}y_{2}  + \dots + a_{1n}x_{1}y_{n} \right)\\
&+ \left( a_{21}x_{2}y_{1} + a_{22}x_{2}y_{2} + \dots + a_{2n}x_{2}y_{n} \right) \\
&+ \left( a_{31}x_{3}y_{1} + a_{32}x_{3}y_{2} + \dots + a_{3n}x_{3}y_{n} \right) \\
&+ \dots \\
&+ \left( a_{n1}x_{n}y_{1} + a_{n2}x_{n}y_{2} + \dots + a_{nn}x_{n}y_{n} \right)
\end{aligned}
$$

En notación de sumatoria compacta:

$$
\sum_{i=1}^{n} \sum_{j=1}^{n} a_{ij} x_i y_j
$$

> [!example] Ejemplo 3: Doble suma numérica
> Sean $n=2$, $a_{ij} = i+j$, $x_i = i$, $y_j = j$:
> $$
> \sum_{i=1}^{2} \sum_{j=1}^{2} (i+j) \cdot i \cdot j
> $$
> Expandimos:
> - $i=1$: $(1+1)\cdot1\cdot1 + (1+2)\cdot1\cdot2 = 2 + 6 = 8$
> - $i=2$: $(2+1)\cdot2\cdot1 + (2+2)\cdot2\cdot2 = 6 + 16 = 22$
> Total: $8 + 22 = 30$

> [!example] Ejemplo 4: Forma cuadrática
> Una [[forma cuadrática]] $Q(\mathbf{x}) = \mathbf{x}^T A \mathbf{x}$ se escribe como $Q = a_{ij} x_i x_j$. Para $n=2$:
> $$
> a_{ij}x_i x_j = a_{11}x_1^2 + a_{12}x_1x_2 + a_{21}x_2x_1 + a_{22}x_2^2
> $$
> Si $A$ es [[matriz simétrica]] ($a_{12}=a_{21}$), esto se simplifica a:
> $$
> a_{11}x_1^2 + 2a_{12}x_1x_2 + a_{22}x_2^2
> $$

## Sustituciones y Cambio de Índices

> [!teorema] Cambio de Índice en una Expresión
> Al realizar una sustitución, es crucial evitar la duplicación accidental de índices mudos. El procedimiento correcto es el siguiente:

### Paso 1: Identificar el conflicto
Definimos la expresión y la sustitución:
$$
Q = b_{ij} y_{i} x_{j}, \qquad y_{i} = a_{ij} x_{j}
$$
**Problema:** El índice $j$ aparece como mudo tanto en $Q$ como en la ecuación para $y_i$, lo que puede llevar a confusión.

### Paso 2: Renombrar el índice mudo
Cambiamos el índice mudo en la sustitución:
$$
y_{i} = a_{ir} x_{r}
$$
(Aquí, $r$ es un nuevo índice mudo).

### Paso 3: Restituir y simplificar
Sustituimos en la expresión original:
$$
Q = b_{ij} (a_{ir} x_{r}) x_{j}
$$
Reordenamos los términos:
$$
Q = (b_{ij} a_{ir}) x_{r} x_{j}
$$

> [!example] Ejemplo 5: Composición de transformaciones lineales
> Sean $T: \mathbb{R}^n \to \mathbb{R}^m$ con componentes $T(\mathbf{x})_i = A_{ij}x_j$ y $S: \mathbb{R}^m \to \mathbb{R}^p$ con componentes $S(\mathbf{y})_k = B_{ki} y_i$.
>
> La composición $S \circ T: \mathbb{R}^n \to \mathbb{R}^p$ es:
> $$
> (S \circ T)(\mathbf{x})_k = B_{ki} (A_{ij}x_j) = (B_{ki}A_{ij})x_j
> $$
> Por lo tanto, la [[multiplicación de matrices]] es $(BA)_{kj} = B_{ki}A_{ij}$.

> [!example] Ejemplo 6: Error común y su corrección
> **Incorrecto:** Sustituir $y_i = a_{ij}x_j$ en $Q = b_{ij}y_i x_j$ sin renombrar:
> $$
> Q \stackrel{?}{=} b_{ij}(a_{ij}x_j)x_j
> $$
> Esto es ambiguo: ¿sobre qué índice se suma? ¿$j$ aparece 4 veces?
>
> **Correcto:** Renombrar primero:
> $$
> Q = b_{ij}(a_{ir}x_r)x_j
> $$
> Ahora los índices son claros: $i$ libre, $j$ y $r$ mudos.

> [!tip] Regla de oro
> Un índice no debe aparecer más de dos veces en un mismo término. Si aparece más, hay un conflicto que debe resolverse renombrando.

## Delta de Kronecker

> [!teoria] Definición: [[Delta de Kronecker]]
> La **Delta de Kronecker**, denotada como $\delta_{ij}$, es una función de dos variables que vale 1 si los índices son iguales y 0 si son distintos:
> $$
> \delta_{ij} = \begin{cases} 1 & \text{si } i = j \\ 0 & \text{si } i \neq j \end{cases}
> $$
>
> Es equivalente a la [[matriz identidad]] $I$, donde $(I)_{ij} = \delta_{ij}$.

> [!example] Ejemplo 7: Propiedad de sustitución
> La propiedad más importante: $\delta_{ij} a_j = a_i$ (sumando sobre $j$).
>
> Para $n=3$, verificamos:
> $$
> \delta_{2j} a_j = \delta_{21}a_1 + \delta_{22}a_2 + \delta_{23}a_3 = 0\cdot a_1 + 1\cdot a_2 + 0\cdot a_3 = a_2
> $$

> [!example] Ejemplo 8: Producto escalar
> El [[producto escalar]] (o producto punto) se expresa elegantemente con la delta:
> $$
> \mathbf{u} \cdot \mathbf{v} = u_i v_i = \delta_{ij} u_i v_j
> $$
> Ya que $\delta_{ij}$ "contrae" los índices $i$ y $j$.

> [!example] Ejemplo 9: Traza de una matriz
> La [[traza (álgebra lineal)|traza]] de una matriz $A$ es:
> $$
> \operatorname{tr}(A) = A_{ii} = \delta_{ij} A_{ij}
> $$
> Para $n=2$, $\operatorname{tr}(A) = A_{11} + A_{22}$.

> [!example] Ejemplo 10: Relación con el símbolo de Levi-Civita
> En [[cálculo vectorial]] y [[álgebra tensorial]], la delta de Kronecker se relaciona con el [[símbolo de Levi-Civita]] $\varepsilon_{ijk}$ mediante la identidad:
> $$
> \varepsilon_{ijk} \varepsilon_{ilm} = \delta_{jl}\delta_{km} - \delta_{jm}\delta_{kl}
> $$
> Esta identidad es fundamental para demostrar identidades vectoriales como $\nabla \times (\nabla \times \mathbf{F}) = \nabla(\nabla \cdot \mathbf{F}) - \nabla^2 \mathbf{F}$.

> [!info] Propiedades Clave de la Delta de Kronecker
> - **Propiedad de sustitución:** $\delta_{ij} a_j = a_i$
> - **Traza:** $\delta_{ii} = n$ (suma sobre $i$)
> - **Producto de deltas:** $\delta_{ij} \delta_{jk} = \delta_{ik}$
> - **Simetría:** $\delta_{ij} = \delta_{ji}$

## Resumen y Próximos Pasos

> [!summary] Conceptos Clave
> - **Índice mudo:** Aparece dos veces, se suma sobre él
> - **Índice libre:** Aparece una vez, representa ecuaciones múltiples
> - **Convenio de Einstein:** Se omite el símbolo ∑
> - **Delta de Kronecker:** $\delta_{ij}$ actúa como matriz identidad

### Notas Relacionadas
- [[Convenio de sumación de Einstein]]
- [[Delta de Kronecker]] — Nota detallada con más ejemplos
- [[Símbolo de Levi-Civita]]
- [[Multiplicación de matrices]]
- [[Producto escalar]]
- [[Forma cuadrática]]
- [[Cálculo tensorial]]