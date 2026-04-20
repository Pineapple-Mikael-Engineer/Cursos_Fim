---
title: Ejercicios de Notación de Índices y Álgebra Lineal Tensorial
tags:
  - matemáticas
  - ejercicios
  - notación-índices
  - álgebra-lineal
  - tensores
  - práctica
draft: false
---

# Ejercicios de Notación de Índices y Álgebra Lineal Tensorial

> [!abstract] Instrucciones
> Resuelve cada ejercicio justificando cada paso. Presta especial atención a:
> - La diferencia entre **índices libres** e **índices mudos**
> - La distinción entre **vector abstracto** ($\vec{v}$) y **componentes** ($v^i$)
> - El papel de la **métrica** $g_{ij}$ en el producto interno
> - El **convenio de Einstein** (suma sobre índices repetidos)
>
> No uses calculadora. Los ejercicios están diseñados para ser resueltos con manipulación algebraica.

---

## Ejercicio 1: Distinción entre Vector y Componentes

Indica si cada expresión es un **escalar**, un **vector** (con índice libre), o una **expresión ambigua/incorrecta**. Justifica.

1. $v^i$
2. $\vec{v}$
3. $v_i$
4. $v^i \vec{e}_i$
5. $v^i v_i$
6. $v^i \vec{e}_j$
7. $v^i \vec{e}_i + w^j \vec{e}_j$
8. $(v^i + w^i) \vec{e}_i$
9. $a_{ij} v^i$
10. $a_{ij} v^i v^j$

> [!question] Ejercicio 1
>
> **Solución:**
>
> 1. $v^i$ → **Vector** (componentes contravariantes, índice $i$ libre)
> 2. $\vec{v}$ → **Vector abstracto** (objeto geométrico)
> 3. $v_i$ → **Vector** (componentes covariantes, índice $i$ libre)
> 4. $v^i \vec{e}_i$ → **Vector abstracto** (todos los índices contraídos, resulta en un vector)
> 5. $v^i v_i$ → **Escalar** (contracción completa, índice $i$ mudo)
> 6. $v^i \vec{e}_j$ → **Expresión ambigua** (tiene índice $i$ mudo pero $j$ libre, y $\vec{e}_j$ es vector base → es un vector en dirección $j$)
> 7. $v^i \vec{e}_i + w^j \vec{e}_j$ → **Vector abstracto** (suma de dos vectores, índices mudos independientes)
> 8. $(v^i + w^i) \vec{e}_i$ → **Vector abstracto** (componentes sumadas, índice $i$ mudo)
> 9. $a_{ij} v^i$ → **Vector** (suma sobre $i$, índice $j$ libre)
> 10. $a_{ij} v^i v^j$ → **Escalar** (suma sobre $i$ y $j$)

---

## Ejercicio 2: Índices Libres y Mudos

Identifica los índices libres y mudos en cada expresión. Determina el rango (número de índices libres) del tensor resultante.

1. $a_{ijk} b^{jk}$
2. $a_{ij} b_{jk} c^{kl}$
3. $a_{i} b_{j} c_{k} d^{ijk}$
4. $a_{ij} b_{kl} c^{ik} d^{jl}$
5. $a_{i} b^{j} \delta^{i}_{j}$

> [!question] Ejercicio 2
>
> **Solución:**
>
> 1. $a_{ijk} b^{jk}$: $i$ libre, $j$ y $k$ mudos → rango 1
> 2. $a_{ij} b_{jk} c^{kl}$: $i$ libre, $l$ libre, $j$ y $k$ mudos → rango 2
> 3. $a_{i} b_{j} c_{k} d^{ijk}$: todos los índices ($i,j,k$) mudos → rango 0 (escalar)
> 4. $a_{ij} b_{kl} c^{ik} d^{jl}$: todos los índices ($i,j,k,l$) mudos → rango 0 (escalar)
> 5. $a_{i} b^{j} \delta^{i}_{j}$: $i$ y $j$ mudos (por $\delta^{i}_{j}$) → rango 0 (escalar)

---

## Ejercicio 3: Producto Interno y Métrica

En un espacio con métrica $g_{ij}$, responde:

1. Expresa el producto interno $\vec{u} \cdot \vec{v}$ en notación de índices usando **componentes contravariantes**.
2. Expresa el mismo producto interno usando **componentes covariantes**.
3. ¿Qué relación existe entre $g_{ij}$ y $g^{ij}$?
4. Si $g_{ij} = \delta_{ij}$ (cartesiano), ¿qué forma toma el producto interno?
5. En coordenadas polares, $g_{rr}=1$, $g_{\theta\theta}=r^2$, $g_{r\theta}=g_{\theta r}=0$. Calcula $\vec{u} \cdot \vec{v}$ si $u^r=2$, $u^\theta=1$, $v^r=3$, $v^\theta=4$.

> [!question] Ejercicio 3
>
> **Solución:**
>
> 1. $\vec{u} \cdot \vec{v} = g_{ij} u^i v^j$
> 2. $\vec{u} \cdot \vec{v} = u_i v^i = u^i v_i$ (también $g^{ij} u_i v_j$)
> 3. $g^{ij}$ es la inversa de $g_{ij}$: $g^{ik} g_{kj} = \delta^i_{\,j}$
> 4. $\vec{u} \cdot \vec{v} = \delta_{ij} u^i v^j = u^i v_i = u^1 v^1 + u^2 v^2 + \dots + u^n v^n$
> 5. $\vec{u} \cdot \vec{v} = g_{rr} u^r v^r + g_{\theta\theta} u^\theta v^\theta = 1 \cdot 2 \cdot 3 + r^2 \cdot 1 \cdot 4 = 6 + 4r^2$

---

## Ejercicio 4: Subir y Bajar Índices

Dada la métrica $g_{ij} = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}$ en $\mathbb{R}^2$:

1. Calcula $g^{ij}$ (la inversa).
2. Dado un vector con componentes contravariantes $u^i = (1, 2)$, encuentra sus componentes covariantes $u_i$.
3. Dado un vector con componentes covariantes $v_i = (3, 4)$, encuentra sus componentes contravariantes $v^i$.
4. Verifica que $u^i u_i = g_{ij} u^i u^j$ con los valores anteriores.
5. ¿Cuál es la norma al cuadrado de $u$?

> [!question] Ejercicio 4
>
> **Solución:**
>
> 1. $\det(g) = 2\cdot3 - 1\cdot1 = 5$, $g^{11} = 3/5$, $g^{12} = g^{21} = -1/5$, $g^{22} = 2/5$
>    $$
>    g^{ij} = \frac{1}{5} \begin{pmatrix} 3 & -1 \\ -1 & 2 \end{pmatrix}
>    $$
>
> 2. $u_i = g_{ij} u^j$:
>    - $u_1 = g_{11}u^1 + g_{12}u^2 = 2\cdot1 + 1\cdot2 = 4$
>    - $u_2 = g_{21}u^1 + g_{22}u^2 = 1\cdot1 + 3\cdot2 = 7$
>    Por lo tanto $u_i = (4, 7)$
>
> 3. $v^i = g^{ij} v_j$:
>    - $v^1 = g^{11}v_1 + g^{12}v_2 = \frac{3}{5}\cdot3 + \frac{-1}{5}\cdot4 = \frac{9 - 4}{5} = 1$
>    - $v^2 = g^{21}v_1 + g^{22}v_2 = \frac{-1}{5}\cdot3 + \frac{2}{5}\cdot4 = \frac{-3 + 8}{5} = 1$
>    Por lo tanto $v^i = (1, 1)$
>
> 4. $u^i u_i = 1\cdot4 + 2\cdot7 = 4 + 14 = 18$
>    $g_{ij} u^i u^j = 2\cdot1\cdot1 + 1\cdot1\cdot2 + 1\cdot2\cdot1 + 3\cdot2\cdot2 = 2 + 2 + 2 + 12 = 18$ ✅
>
> 5. $\|u\|^2 = g_{ij} u^i u^j = 18$

---

## Ejercicio 5: Convenio de Einstein y Expansión Explícita

Escribe explícitamente la suma (con $\sum$) para cada expresión, asumiendo $n=3$ (índices de 1 a 3).

1. $a_{ij} x^i x^j$
2. $a_{ijk} b^{jk}$
3. $c_{ij} \delta^{ij}$
4. $\varepsilon_{ijk} a^i b^j c^k$
5. $v^i w_i$

> [!question] Ejercicio 5
>
> **Solución:**
>
> 1. $a_{ij} x^i x^j = \sum_{i=1}^3 \sum_{j=1}^3 a_{ij} x^i x^j$
>    - Expansión: $a_{11}x^1x^1 + a_{12}x^1x^2 + a_{13}x^1x^3 + a_{21}x^2x^1 + a_{22}x^2x^2 + a_{23}x^2x^3 + a_{31}x^3x^1 + a_{32}x^3x^2 + a_{33}x^3x^3$
>
> 2. $a_{ijk} b^{jk} = \sum_{j=1}^3 \sum_{k=1}^3 a_{ijk} b^{jk}$ (para cada $i$)
>    - Para $i=1$: $a_{111}b^{11} + a_{112}b^{12} + a_{113}b^{13} + a_{121}b^{21} + a_{122}b^{22} + a_{123}b^{23} + a_{131}b^{31} + a_{132}b^{32} + a_{133}b^{33}$
>    - Análogo para $i=2$ e $i=3$
>
> 3. $c_{ij} \delta^{ij} = \sum_{i=1}^3 \sum_{j=1}^3 c_{ij} \delta^{ij} = c_{11} + c_{22} + c_{33}$ (solo términos con $i=j$)
>
> 4. $\varepsilon_{ijk} a^i b^j c^k = \sum_{i=1}^3 \sum_{j=1}^3 \sum_{k=1}^3 \varepsilon_{ijk} a^i b^j c^k$
>    - Solo sobreviven permutaciones: $i,j,k$ distintos
>    - $= a^1b^2c^3 + a^2b^3c^1 + a^3b^1c^2 - a^1b^3c^2 - a^2b^1c^3 - a^3b^2c^1$
>
> 5. $v^i w_i = \sum_{i=1}^3 v^i w_i = v^1 w_1 + v^2 w_2 + v^3 w_3$

---

## Ejercicio 6: Multiplicación de Matrices en Notación de Índices

Sean $A = [a^i_{\,j}]$ y $B = [b^i_{\,j}]$ matrices $3 \times 3$. Escribe explícitamente (con sumas) las componentes de:

1. $C = AB$
2. $D = A^T$
3. $E = A + B$
4. $F = A^{-1}$ (en términos de cofactores)
5. La traza de $A$

> [!question] Ejercicio 6
>
> **Solución:**
>
> 1. $c^i_{\,j} = a^i_{\,k} b^k_{\,j} = \sum_{k=1}^3 a^i_{\,k} b^k_{\,j}$
>    - Ejemplo $c^1_{\,1} = a^1_{\,1}b^1_{\,1} + a^1_{\,2}b^2_{\,1} + a^1_{\,3}b^3_{\,1}$
>
> 2. $(A^T)^i_{\,j} = a^j_{\,i}$
>
> 3. $e^i_{\,j} = a^i_{\,j} + b^i_{\,j}$
>
> 4. $(A^{-1})^i_{\,j} = \frac{1}{\det(A)} \tilde{a}^{\,i}_{j}$ donde $\tilde{a}^{\,i}_{j}$ es el cofactor transpuesto
>
> 5. $\operatorname{tr}(A) = a^i_{\,i} = a^1_{\,1} + a^2_{\,2} + a^3_{\,3}$

---

## Ejercicio 7: Identidad con Levi-Civita

Verifica que $\varepsilon_{ijk} \varepsilon_{ilm} = \delta_{jl}\delta_{km} - \delta_{jm}\delta_{kl}$ para un caso específico.

Elige $j=2$, $l=2$, $k=3$, $m=3$ y calcula ambos lados.

> [!question] Ejercicio 7
>
> **Solución:**
>
> Lado izquierdo: $\varepsilon_{i23} \varepsilon_{i23}$ suma sobre $i$ (de 1 a 3)
>
> - $i=1$: $\varepsilon_{123}=1$, $\varepsilon_{123}=1$ → $1\cdot1 = 1$
> - $i=2$: $\varepsilon_{223}=0$ → $0$
> - $i=3$: $\varepsilon_{323}=0$ → $0$
>
> Total: $1$
>
> Lado derecho: $\delta_{22}\delta_{33} - \delta_{23}\delta_{32} = 1\cdot1 - 0\cdot0 = 1$
>
> ✅ Se cumple.

---

## Ejercicio 8: Errores Comunes en Distribución

Indica si cada igualdad es correcta o incorrecta. Justifica.

1. $a_{ij} (x_i + y_j) = a_{ij} x_i + a_{ij} y_j$
2. $a_{ij} (x_i + y_i) = a_{ij} x_i + a_{ij} y_i$
3. $(a_{ij} + b_{ij}) x^i x^j = a_{ij} x^i x^j + b_{ij} x^i x^j$
4. $a_{ij} (x^i + y^i) = a_{ij} x^i + a_{ij} y^i$
5. $\vec{u} \cdot \vec{v} = u^i v^i$ (en coordenadas cartesianas)

> [!question] Ejercicio 8
>
> **Solución:**
>
> 1. **Incorrecta**. Lado izquierdo: $i$ y $j$ son mudos → escalar. Lado derecho: primer término tiene $j$ libre, segundo tiene $i$ libre. No es una igualdad válida.
>
> 2. **Correcta**. $i$ es mudo en ambos términos, $j$ es libre en todos. La suma tiene sentido.
>
> 3. **Correcta**. Distribución válida porque $i$ y $j$ son mudos en todos los términos.
>
> 4. **Correcta**. $i$ es mudo, $j$ libre. La distribución es válida.
>
> 5. **Correcta en coordenadas cartesianas**. En cartesianas $g_{ij}=\delta_{ij}$, entonces $u^i v_i = u^i v^i$.

---

## Ejercicio 9: Transformación de Coordenadas Lineal

En $\mathbb{R}^2$, se define la transformación lineal $\bar{x}^1 = 2x^1 + x^2$, $\bar{x}^2 = x^1 + x^2$.

1. Escribe la matriz $A$ de la transformación ($\bar{x}^i = a^i_{\,j} x^j$).
2. Calcula la matriz $G = (A A^T)^{-1}$.
3. ¿Cómo se expresa la distancia $d(\bar{x}, \bar{y})$ en coordenadas transformadas?
4. Si $\bar{x} - \bar{y} = (1, 0)$, ¿cuál es la distancia?

> [!question] Ejercicio 9
>
> **Solución:**
>
> 1. $a^1_{\,1}=2$, $a^1_{\,2}=1$, $a^2_{\,1}=1$, $a^2_{\,2}=1$
>    $$
>    A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}
>    $$
>
> 2. $A A^T = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix} = \begin{pmatrix} 5 & 3 \\ 3 & 2 \end{pmatrix}$
>    $\det(AA^T) = 5\cdot2 - 3\cdot3 = 10 - 9 = 1$
>    $$
>    G = (A A^T)^{-1} = \begin{pmatrix} 2 & -3 \\ -3 & 5 \end{pmatrix}
>    $$
>
> 3. $d^2 = g_{ij} \Delta \bar{x}^i \Delta \bar{x}^j = 2(\Delta \bar{x}^1)^2 - 6 \Delta \bar{x}^1 \Delta \bar{x}^2 + 5(\Delta \bar{x}^2)^2$
>
> 4. $\Delta \bar{x}^1 = 1$, $\Delta \bar{x}^2 = 0$ → $d^2 = 2\cdot1^2 = 2$ → $d = \sqrt{2}$

---

## Ejercicio 10: Composición de Transformaciones

Sean dos transformaciones lineales:
- $T_1: \bar{x}^i = a^i_{\,j} x^j$ con $a^1_{\,1}=1$, $a^1_{\,2}=2$, $a^2_{\,1}=0$, $a^2_{\,2}=1$
- $T_2: \hat{x}^i = b^i_{\,j} \bar{x}^j$ con $b^1_{\,1}=1$, $b^1_{\,2}=0$, $b^2_{\,1}=3$, $b^2_{\,2}=1$

1. Encuentra la matriz de $T_1$ y $T_2$.
2. Encuentra la matriz de la composición $T = T_2 \circ T_1$ (primero $T_1$, luego $T_2$).
3. Escribe las componentes $c^i_{\,j}$ de la transformación compuesta.
4. Aplica $T$ al vector $x = (1, 1)$.

> [!question] Ejercicio 10
>
> **Solución:**
>
> 1. $A = \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix}$, $B = \begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix}$
>
> 2. $C = B A = \begin{pmatrix} 1 & 0 \\ 3 & 1 \end{pmatrix} \begin{pmatrix} 1 & 2 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 & 2 \\ 3 & 7 \end{pmatrix}$
>
> 3. $c^1_{\,1}=1$, $c^1_{\,2}=2$, $c^2_{\,1}=3$, $c^2_{\,2}=7$
>
> 4. $\hat{x}^1 = 1\cdot1 + 2\cdot1 = 3$, $\hat{x}^2 = 3\cdot1 + 7\cdot1 = 10$ → $\hat{x} = (3, 10)$

---

## Ejercicio 11: Simplificación de Expresiones

Simplifica las siguientes expresiones usando propiedades de la delta de Kronecker y el símbolo de Levi-Civita.

1. $\delta_{ij} \delta_{jk}$
2. $\delta_{ij} \delta_{ij}$
3. $\varepsilon_{ijk} \varepsilon_{ijk}$
4. $\varepsilon_{ijk} \varepsilon_{ijl}$
5. $a_i \delta_{ij}$
6. $a_{ij} \delta_{jk}$

> [!question] Ejercicio 11
>
> **Solución:**
>
> 1. $\delta_{ij} \delta_{jk} = \delta_{ik}$ (suma sobre $j$)
> 2. $\delta_{ij} \delta_{ij} = \delta_{ii} = n$ (en $n$ dimensiones)
> 3. $\varepsilon_{ijk} \varepsilon_{ijk} = 6$ (para $n=3$)
> 4. $\varepsilon_{ijk} \varepsilon_{ijl} = \delta_{jj}\delta_{kl} - \delta_{jl}\delta_{kj} = 3\delta_{kl} - \delta_{kl} = 2\delta_{kl}$
> 5. $a_i \delta_{ij} = a_j$
> 6. $a_{ij} \delta_{jk} = a_{ik}$

---

## Ejercicio 12: Vector en Base No Ortonormal

En $\mathbb{R}^2$ se define una base $\{\vec{e}_1, \vec{e}_2\}$ con:
- $\vec{e}_1 \cdot \vec{e}_1 = 2$
- $\vec{e}_1 \cdot \vec{e}_2 = 1$
- $\vec{e}_2 \cdot \vec{e}_2 = 3$

1. Escribe la métrica $g_{ij}$.
2. Un vector $\vec{v}$ tiene componentes contravariantes $v^1=1$, $v^2=2$. Encuentra $\vec{v}$ en la base $\{\vec{e}_i\}$.
3. Calcula la norma de $\vec{v}$.
4. Encuentra las componentes covariantes $v_i$.

> [!question] Ejercicio 12
>
> **Solución:**
>
> 1. $g_{11}=2$, $g_{12}=1$, $g_{21}=1$, $g_{22}=3$
>    $$
>    g_{ij} = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}
>    $$
>
> 2. $\vec{v} = v^1 \vec{e}_1 + v^2 \vec{e}_2 = 1\vec{e}_1 + 2\vec{e}_2$
>
> 3. $\|\vec{v}\|^2 = g_{ij} v^i v^j = 2\cdot1\cdot1 + 1\cdot1\cdot2 + 1\cdot2\cdot1 + 3\cdot2\cdot2 = 2 + 2 + 2 + 12 = 18$
>    $\|\vec{v}\| = \sqrt{18} = 3\sqrt{2}$
>
> 4. $v_i = g_{ij} v^j$:
>    $v_1 = 2\cdot1 + 1\cdot2 = 4$
>    $v_2 = 1\cdot1 + 3\cdot2 = 7$
>    $v_i = (4, 7)$

---

## Ejercicio 13: Producto Vectorial en Notación de Índices

En $\mathbb{R}^3$, dados los vectores $\vec{u} = (1, 2, 3)$ y $\vec{v} = (4, 5, 6)$:

1. Calcula $\vec{w} = \vec{u} \times \vec{v}$ usando la fórmula $w^i = \varepsilon^{ijk} u_j v_k$.
2. Verifica que $\vec{w}$ es ortogonal a $\vec{u}$ y $\vec{v}$ (producto escalar cero).
3. ¿Cuál es la norma de $\vec{w}$?

> [!question] Ejercicio 13
>
> **Solución:**
>
> 1. $w^1 = \varepsilon^{123} u_2 v_3 + \varepsilon^{132} u_3 v_2 = 1\cdot2\cdot6 + (-1)\cdot3\cdot5 = 12 - 15 = -3$
>    $w^2 = \varepsilon^{213} u_1 v_3 + \varepsilon^{231} u_3 v_1 = (-1)\cdot1\cdot6 + 1\cdot3\cdot4 = -6 + 12 = 6$
>    $w^3 = \varepsilon^{312} u_1 v_2 + \varepsilon^{321} u_2 v_1 = 1\cdot1\cdot5 + (-1)\cdot2\cdot4 = 5 - 8 = -3$
>    $\vec{w} = (-3, 6, -3)$
>
> 2. $\vec{w} \cdot \vec{u} = (-3)\cdot1 + 6\cdot2 + (-3)\cdot3 = -3 + 12 - 9 = 0$
>    $\vec{w} \cdot \vec{v} = (-3)\cdot4 + 6\cdot5 + (-3)\cdot6 = -12 + 30 - 18 = 0$ ✅
>
> 3. $\|\vec{w}\| = \sqrt{(-3)^2 + 6^2 + (-3)^2} = \sqrt{9 + 36 + 9} = \sqrt{54} = 3\sqrt{6}$

---

## Ejercicio 14: Forma Cuadrática y su Gradiente

Dada la forma cuadrática $Q(\vec{x}) = a_{ij} x^i x^j$ con $a_{ij}$ constante y simétrica ($a_{ij}=a_{ji}$):

1. Expresa $Q(\vec{x})$ en forma matricial.
2. Calcula $\frac{\partial Q}{\partial x^k}$ en notación de índices.
3. Si $a_{ij} = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}$ y $\vec{x} = (1, 2)$, encuentra $\nabla Q$.

> [!question] Ejercicio 14
>
> **Solución:**
>
> 1. $Q(\vec{x}) = \vec{x}^T A \vec{x}$ con $A = [a_{ij}]$
>
> 2. $\frac{\partial Q}{\partial x^k} = (a_{ik} + a_{ki}) x^i = 2a_{ki} x^i$ (por simetría)
>
> 3. $a_{11}=2$, $a_{12}=1$, $a_{21}=1$, $a_{22}=3$
>    $\frac{\partial Q}{\partial x^1} = 2a_{11}x^1 + 2a_{12}x^2 = 2\cdot2\cdot1 + 2\cdot1\cdot2 = 4 + 4 = 8$
>    $\frac{\partial Q}{\partial x^2} = 2a_{21}x^1 + 2a_{22}x^2 = 2\cdot1\cdot1 + 2\cdot3\cdot2 = 2 + 12 = 14$
>    $\nabla Q = (8, 14)$

---

## Ejercicio 15: Contracción de Tensores

Dados los tensores $A^{ij}$ y $B_{jk}$, encuentra la expresión contraída $C^i = A^{ij} B_{jk}$.

1. Escribe explícitamente la suma para $n=2$.
2. Si $A^{ij} = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ y $B_{jk} = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$, calcula $C^i$.

> [!question] Ejercicio 15
>
> **Solución:**
>
> 1. $C^i = A^{ij} B_{jk} = \sum_{j=1}^2 \sum_{k=1}^2 A^{ij} B_{jk}$ (suma sobre $j$ y $k$)
>    - $C^1 = A^{11}B_{11} + A^{11}B_{12} + A^{12}B_{21} + A^{12}B_{22}$
>    - $C^2 = A^{21}B_{11} + A^{21}B_{12} + A^{22}B_{21} + A^{22}B_{22}$
>
> 2. $C^1 = 1\cdot5 + 1\cdot6 + 2\cdot7 + 2\cdot8 = 5 + 6 + 14 + 16 = 41$
>    $C^2 = 3\cdot5 + 3\cdot6 + 4\cdot7 + 4\cdot8 = 15 + 18 + 28 + 32 = 93$
>    $C^i = (41, 93)$

---

> [!summary] Resumen de Conceptos Clave
> - **Índice mudo**: aparece dos veces → se suma
> - **Índice libre**: aparece una vez → representa un tensor
> - **Métrica $g_{ij}$**: define el producto interno y relaciona componentes covariantes y contravariantes
> - **Convenio de Einstein**: se suma sobre índices repetidos (uno arriba, uno abajo)
> - **Delta de Kronecker $\delta^i_j$**: matriz identidad, propiedad de sustitución
> - **Símbolo de Levi-Civita $\varepsilon_{ijk}$**: antisimétrico, define producto vectorial y determinante

---

## Notas Relacionadas

- [[Notación de Índices en Sumatorias]]
- [[Álgebra Lineal Básica para Tensores]]
- [[Delta de Kronecker]]
- [[Símbolo de Levi-Civita]]
- [[Derivada de una Forma Cuadrática en Notación de Índices]]
- [[Producto Interno y Métrica]]