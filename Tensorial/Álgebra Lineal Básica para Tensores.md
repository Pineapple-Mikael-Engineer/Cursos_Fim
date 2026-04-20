---
title: Álgebra Lineal Básica para Tensores
tags:
  - matemáticas
  - álgebra-lineal
  - tensores
  - notación-índices
  - transformaciones-lineales
  - geometría
  - cálculo-tensorial
  - producto-interno
  - métrica
draft: false
---

# Álgebra Lineal Básica para Tensores

> [!abstract] Resumen
> Esta nota establece los fundamentos del álgebra lineal en notación de índices, conectando conceptos clásicos (matrices, vectores, determinantes) con su representación tensorial. Es la base para comprender el [[cálculo tensorial]] y sus aplicaciones en [[geometría diferencial]], [[mecánica del continuo]] y [[relatividad general]].

---

## Notación de Tensor para Matrices, Vectores y Determinantes

### Convención de Índices y Notación

En notación tensorial, utilizamos:
- **Índices superiores** (contravariantes): $a^i$ — transforman de manera opuesta a la base
- **Índices inferiores** (covariantes): $a_i$ — transforman como la base
- **Índices mixtos**: $a^i_{\,j}$ — un índice arriba, uno abajo

> [!info] Convenio de Einstein
> Se suma sobre todo índice que aparece repetido (una vez arriba y una vez abajo):
> $$
> a^i b_i = \sum_{i=1}^n a^i b_i
> $$

> [!warning] Distinción entre Objeto Geométrico y Componentes
> En álgebra lineal y cálculo tensorial es fundamental distinguir:
> 
> | Objeto | Notación | Descripción |
> |--------|----------|-------------|
> | **Vector** | $\vec{v}$ o $\mathbf{v}$ | Entidad geométrica independiente de coordenadas |
> | **Tensor** | $\overset{\leftrightarrow}{A}$ o $\mathbf{A}$ | Entidad geométrica de rango superior |
> | **Matriz** | $[a^i_{\,j}]$ | Representación de un tensor en una base (componentes) |
> | **Componentes** | $a^i_{\,j}$, $v^i$, $v_i$ | Números que dependen de la base elegida |
>
> La relación fundamental es:
> $$
> \vec{v} = v^i \vec{e}_i \quad \text{(suma sobre $i$)}
> $$
> donde $\vec{e}_i$ son los vectores base. La **flecha** ($\vec{v}$) indica el objeto geométrico; las **componentes** ($v^i$) son solo números que adquieren significado en el contexto de una base.

### Representación de Matrices

Una matriz (como objeto algebraico) representa las componentes de un tensor de rango 2 en una base específica.

#### Matriz con Índices Mixtos (Forma Estándar)

Una matriz $A$ de dimensión $m \times n$ se representa como:

$$
[a^i_{\,j}]_{m \times n} = 
\begin{bmatrix}
a^1_{\,1} & a^1_{\,2} & a^1_{\,3} & \dots & a^1_{\,n} \\
a^2_{\,1} & a^2_{\,2} & a^2_{\,3} & \dots & a^2_{\,n} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
a^m_{\,1} & a^m_{\,2} & a^m_{\,3} & \dots & a^m_{\,n}
\end{bmatrix}
$$

- $i$ (superior) = índice de fila
- $j$ (inferior) = índice de columna

#### Matriz con Índices Superiores (Contravariante)

Para una matriz con ambos índices arriba (tensor contravariante de rango 2):

$$
[a^{ij}]_{m \times n} = 
\begin{bmatrix}
a^{11} & a^{12} & a^{13} & \dots & a^{1n} \\
a^{21} & a^{22} & a^{23} & \dots & a^{2n} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
a^{m1} & a^{m2} & a^{m3} & \dots & a^{mn}
\end{bmatrix}
$$

#### Matriz con Índices Inferiores (Covariante)

Para una matriz con ambos índices abajo (tensor covariante de rango 2):

$$
[a_{ij}]_{m \times n} = 
\begin{bmatrix}
a_{11} & a_{12} & a_{13} & \dots & a_{1n} \\
a_{21} & a_{22} & a_{23} & \dots & a_{2n} \\
\vdots & \vdots & \vdots & \ddots & \vdots \\
a_{m1} & a_{m2} & a_{m3} & \dots & a_{mn}
\end{bmatrix}
$$

> [!example] Ejemplo 1: Matriz $2 \times 2$
> Para una matriz $A = \begin{pmatrix} 2 & 3 \\ 5 & 7 \end{pmatrix}$:
> - Notación mixta: $a^1_{\,1}=2$, $a^1_{\,2}=3$, $a^2_{\,1}=5$, $a^2_{\,2}=7$
> - Notación contravariante: $a^{11}=2$, $a^{12}=3$, $a^{21}=5$, $a^{22}=7$
> - Notación covariante: $a_{11}=2$, $a_{12}=3$, $a_{21}=5$, $a_{22}=7$

### Vectores

#### Vector como Objeto Geométrico

Un vector $\vec{v}$ es una entidad geométrica independiente de coordenadas. En una base $\{\vec{e}_i\}$ se expresa como:

$$
\vec{v} = v^i \vec{e}_i
$$

donde $v^i$ son sus **componentes contravariantes**.

#### Representación Matricial de un Vector

En una base fija, un vector se representa como una **matriz columna** con sus componentes:

$$
[\vec{v}]_{\mathcal{B}} = [v^i]_{n \times 1} = 
\begin{bmatrix}
v^1 \\
v^2 \\
\vdots \\
v^n
\end{bmatrix}
$$

En notación simplificada (cuando la base está implícita), a veces se escribe $\vec{v} = (v^1, v^2, \dots, v^n)$.

> [!warning] Notación Simplificada vs. Rigurosa
> La expresión $\vec{v} = (v^i)$ es una **simplificación** que identifica al vector con sus componentes. Esto solo es válido cuando:
> 1. Se trabaja en una base ortonormal fija (como la cartesiana estándar)
> 2. No hay necesidad de distinguir entre el objeto y sus coordenadas
>
> En cálculo tensorial, la forma correcta es $\vec{v} = v^i \vec{e}_i$, donde la suma sobre $i$ está implícita por el convenio de Einstein.

#### Vector Fila (1-Forma o Covariante)

Una **1-forma** (funcional lineal) $\tilde{\omega}$ se representa como un vector fila con componentes covariantes:

$$
[\tilde{\omega}]_{\mathcal{B}} = [\omega_i]_{1 \times n} = 
\begin{bmatrix}
\omega_1 & \omega_2 & \dots & \omega_n
\end{bmatrix}
$$

En términos de base dual $\{\vec{\varepsilon}^i\}$ (definida por $\vec{\varepsilon}^i(\vec{e}_j) = \delta^i_{\,j}$):

$$
\tilde{\omega} = \omega_i \vec{\varepsilon}^i
$$

La acción de una 1-forma sobre un vector es:

$$
\tilde{\omega}(\vec{v}) = \omega_i v^i
$$

> [!example] Ejemplo 2: Vector en $\mathbb{R}^3$
> Para $\vec{v} = 3\vec{e}_1 - \vec{e}_2 + 2\vec{e}_3$ en base cartesiana:
> - Componentes contravariantes: $v^1 = 3$, $v^2 = -1$, $v^3 = 2$
> - Representación matricial: $\begin{bmatrix} 3 \\ -1 \\ 2 \end{bmatrix}$
> - Notación simplificada: $\vec{v} = (3, -1, 2)$

### Bases Duales y el Producto Interno

El **producto interno** (producto punto) es una operación que toma dos vectores y devuelve un escalar. En términos de vectores abstractos:

$$
\vec{u} \cdot \vec{v} = \text{escalar}
$$

Al expandir en una base, aparecen los **vectores base** $\vec{e}_i$ y la **base dual** $\vec{\varepsilon}^j$:

$$
\vec{u} \cdot \vec{v} = (u^i \vec{e}_i) \cdot (v^j \vec{e}_j) = u^i v^j (\vec{e}_i \cdot \vec{e}_j)
$$

Definimos el **tensor métrico** (covariante) como:

$$
g_{ij} = \vec{e}_i \cdot \vec{e}_j
$$

Por lo tanto:

$$
\vec{u} \cdot \vec{v} = g_{ij} u^i v^j
$$

#### Relación entre Componentes Covariantes y Contravariantes

La métrica permite "bajar" y "subir" índices:

- **Bajar un índice**: $v_i = g_{ij} v^j$
- **Subir un índice**: $v^i = g^{ij} v_j$

donde $g^{ij}$ es la inversa de $g_{ij}$ ($g^{ik} g_{kj} = \delta^i_{\,j}$).

#### En Base Ortonormal (Cartesiana)

En coordenadas cartesianas con base ortonormal:

$$
g_{ij} = \delta_{ij} \quad \text{(matriz identidad)}
$$

Por lo tanto:

$$
v_i = \delta_{ij} v^j = v^i
$$

Es decir, **no hay diferencia** entre componentes covariantes y contravariantes. Esta es la razón por la que en muchos textos introductorios se ignora la distinción.

#### Producto Interno como Tensor de Rango 2

El producto interno es un tensor de rango 2 (0,2) cuyas componentes son $g_{ij}$:

$$
\vec{u} \cdot \vec{v} = g_{ij} u^i v^j
$$

> [!example] Ejemplo 3: Producto interno en coordenadas polares
> En coordenadas polares $(r, \theta)$ en $\mathbb{R}^2$:
> - La métrica es: $g_{rr} = 1$, $g_{\theta\theta} = r^2$, $g_{r\theta} = g_{\theta r} = 0$
> - Para $\vec{u} = u^r \vec{e}_r + u^\theta \vec{e}_\theta$, $\vec{v} = v^r \vec{e}_r + v^\theta \vec{e}_\theta$:
> $$
> \vec{u} \cdot \vec{v} = u^r v^r + r^2 u^\theta v^\theta
> $$
>
> Si $\vec{u} = (1, 0)$ en componentes contravariantes ($u^r=1$, $u^\theta=0$) y $\vec{v} = (0, 1)$ ($v^r=0$, $v^\theta=1$):
> $$
> \vec{u} \cdot \vec{v} = 1 \cdot 0 + r^2 \cdot 0 \cdot 1 = 0
> $$
> (son ortogonales, como esperamos)

### Covariante vs. Contravariante (Ampliación)

La posición del índice (arriba o abajo) indica cómo se transforman las componentes ante un cambio de base:

- **Contravariante** ($v^i$): las componentes se transforman **inversamente** a la base
  - Si la base se estira, las componentes se encogen
  - Ejemplo: las componentes de un vector de posición

- **Covariante** ($v_i$): las componentes se transforman **como** la base
  - Si la base se estira, las componentes también se estiran
  - Ejemplo: las componentes del gradiente de una función

La relación entre ambas está dada por la métrica:

$$
v_i = g_{ij} v^j \quad \text{(bajar índice)}
$$
$$
v^i = g^{ij} v_j \quad \text{(subir índice)}
$$

> [!info] En Coordenadas Cartesianas
> En coordenadas cartesianas con base ortonormal, $g_{ij} = \delta_{ij}$, por lo tanto:
> $$
> v^i = v_i
> $$
> Por eso en muchos textos introductorios se ignora la distinción. La diferencia se vuelve crucial en [[coordenadas curvilíneas]] y en [[relatividad general]].

### Operaciones Básicas

#### Suma de Matrices

En notación de índices:
$$
c^i_{\,j} = a^i_{\,j} + b^i_{\,j}
$$

> [!example] Ejemplo 4: Suma de matrices
> $$
> \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} + \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix} = \begin{pmatrix} 6 & 8 \\ 10 & 12 \end{pmatrix}
> $$
> En índices: $c^1_{\,1}=1+5=6$, $c^1_{\,2}=2+6=8$, $c^2_{\,1}=3+7=10$, $c^2_{\,2}=4+8=12$

#### Multiplicación Escalar

$$
c^i_{\,j} = \lambda \, a^i_{\,j}
$$

> [!example] Ejemplo 5: Multiplicación escalar
> $$
> 3 \cdot \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix} = \begin{pmatrix} 3 & 6 \\ 9 & 12 \end{pmatrix}
> $$

---

## Fórmulas Básicas en Notación de Índices

### Multiplicación de Matrices

El producto $C = A \cdot B$ (con $A$ de $m \times p$, $B$ de $p \times n$) se escribe:

$$
c^i_{\,j} = a^i_{\,k} \, b^k_{\,j}
$$

donde $k$ es un índice mudo (se suma sobre $k=1,\dots,p$).

> [!example] Ejemplo 6: Multiplicación de matrices
> $$
> A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}, \quad
> B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}
> $$
> $$
> C = AB = \begin{pmatrix} 1\cdot5+2\cdot7 & 1\cdot6+2\cdot8 \\ 3\cdot5+4\cdot7 & 3\cdot6+4\cdot8 \end{pmatrix} = \begin{pmatrix} 19 & 22 \\ 43 & 50 \end{pmatrix}
> $$
>
> En índices:
> - $c^1_{\,1} = a^1_{\,k} b^k_{\,1} = a^1_{\,1}b^1_{\,1} + a^1_{\,2}b^2_{\,1} = 1\cdot5 + 2\cdot7 = 19$
> - $c^1_{\,2} = a^1_{\,k} b^k_{\,2} = 1\cdot6 + 2\cdot8 = 22$
> - $c^2_{\,1} = a^2_{\,k} b^k_{\,1} = 3\cdot5 + 4\cdot7 = 43$
> - $c^2_{\,2} = a^2_{\,k} b^k_{\,2} = 3\cdot6 + 4\cdot8 = 50$

### Matriz Identidad

La [[matriz identidad]] $I_n$ se representa con la [[Delta de Kronecker]]:

$$
\delta^i_{\,j} = \begin{cases} 1 & \text{si } i = j \\ 0 & \text{si } i \neq j \end{cases}
$$

Propiedades:
- $\delta^i_{\,j} v^j = v^i$ (contracción)
- $\delta^i_{\,j} \omega_i = \omega_j$
- $\delta^i_{\,j} \delta^j_{\,k} = \delta^i_{\,k}$

### Matriz Transpuesta

La [[matriz transpuesta]] de $A = [a^i_{\,j}]$ es $(A^T)^i_{\,j} = a^j_{\,i}$.

> [!example] Ejemplo 7: Transpuesta
> $$
> A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \end{pmatrix}, \quad
> A^T = \begin{pmatrix} 1 & 4 \\ 2 & 5 \\ 3 & 6 \end{pmatrix}
> $$
> En índices: $(A^T)^1_{\,1}=a^1_{\,1}=1$, $(A^T)^1_{\,2}=a^2_{\,1}=4$, etc.

### Matriz Inversa

Para una matriz cuadrada $A$ con $\det(A) \neq 0$, su [[matriz inversa]] $A^{-1} = [ (A^{-1})^i_{\,j} ]$ satisface:

$$
a^i_{\,k} (A^{-1})^k_{\,j} = \delta^i_{\,j}, \quad (A^{-1})^i_{\,k} a^k_{\,j} = \delta^i_{\,j}
$$

En términos de la matriz de cofactores:

$$
(A^{-1})^i_{\,j} = \frac{1}{\det(A)} \tilde{a}^{\,i}_{j}
$$

donde $\tilde{a}^{\,i}_{j}$ es la matriz de cofactores transpuesta.

> [!example] Ejemplo 8: Inversa de una matriz $2 \times 2$
> Para $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$:
> $$
> A^{-1} = \frac{1}{ad - bc} \begin{pmatrix} d & -b \\ -c & a \end{pmatrix}
> $$
> En índices: $(A^{-1})^1_{\,1} = \frac{d}{\det A}$, $(A^{-1})^1_{\,2} = \frac{-b}{\det A}$, etc.

### Símbolo de Permutación (Símbolo de Levi-Civita)

El [[símbolo de Levi-Civita]] $\varepsilon_{ijk}$ (en 3D) es un tensor completamente antisimétrico:

$$
\varepsilon_{ijk} = \begin{cases}
+1 & \text{si } (i,j,k) \text{ es una permutación par de } (1,2,3) \\
-1 & \text{si } (i,j,k) \text{ es una permutación impar de } (1,2,3) \\
0 & \text{si hay índices repetidos}
\end{cases}
$$

> [!example] Ejemplo 9: Valores del símbolo de Levi-Civita
> - $\varepsilon_{123} = 1$ (permutación par)
> - $\varepsilon_{132} = -1$ (permutación impar)
> - $\varepsilon_{112} = 0$ (índice repetido)

### Determinante de una Matriz Cuadrada

El [[determinante]] de una matriz $A = [a^i_{\,j}]$ se expresa como:

$$
\det(A) = \varepsilon_{i_1 i_2 \dots i_n} a^{i_1}_{\,1} a^{i_2}_{\,2} \cdots a^{i_n}_{\,n}
$$

o equivalentemente:

$$
\det(A) = \frac{1}{n!} \varepsilon_{i_1 \dots i_n} \varepsilon_{j_1 \dots j_n} a^{i_1}_{\,j_1} \cdots a^{i_n}_{\,j_n}
$$

Para $n=3$:
$$
\det(A) = \varepsilon_{ijk} a^i_{\,1} a^j_{\,2} a^k_{\,3}
$$

> [!example] Ejemplo 10: Determinante $2 \times 2$
> Para $A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$:
> $$
> \det(A) = \varepsilon_{ij} a^i_{\,1} a^j_{\,2}
> $$
> Sumando sobre $i,j$:
> - $i=1,j=2$: $\varepsilon_{12}=1$, término $a^1_{\,1}a^2_{\,2} = ad$
> - $i=2,j=1$: $\varepsilon_{21}=-1$, término $-a^2_{\,1}a^1_{\,2} = -bc$
> - Total: $ad - bc$

### Expansión de Laplace del Determinante

La [[expansión de Laplace]] por cofactores:

$$
\det(A) = a^i_{\,j} C^j_{\,i}
$$

donde $C^j_{\,i} = (-1)^{i+j} M^j_{\,i}$ es el [[cofactor]], y $M^j_{\,i}$ es el [[menor (álgebra lineal)|menor]].

En notación de índices:

$$
\det(A) = \frac{1}{n} a^i_{\,j} \frac{\partial \det(A)}{\partial a^i_{\,j}}
$$

### Matriz Jacobiana

La [[matriz jacobiana]] de una transformación $\bar{x}^i = T^i(x^1, \dots, x^n)$ es:

$$
J^i_{\,j} = \frac{\partial \bar{x}^i}{\partial x^j}
$$

Su determinante, el [[jacobiano]], indica el cambio de volumen bajo la transformación.

> [!example] Ejemplo 11: Jacobiana de coordenadas polares
> Para la transformación $x = r\cos\theta$, $y = r\sin\theta$:
> $$
> J = \begin{pmatrix} \frac{\partial x}{\partial r} & \frac{\partial x}{\partial \theta} \\ \frac{\partial y}{\partial r} & \frac{\partial y}{\partial \theta} \end{pmatrix} = \begin{pmatrix} \cos\theta & -r\sin\theta \\ \sin\theta & r\cos\theta \end{pmatrix}
> $$
> $\det(J) = r$

### Producto Escalar de Vectores (Producto Interno)

En espacio euclidiano con métrica $g_{ij}$:

$$
\vec{u} \cdot \vec{v} = g_{ij} u^i v^j
$$

En coordenadas cartesianas ($g_{ij} = \delta_{ij}$):

$$
\vec{u} \cdot \vec{v} = u^i v_i = u^i \delta_{ij} v^j = \sum_{i=1}^n u^i v^i
$$

> [!example] Ejemplo 12: Producto escalar en $\mathbb{R}^3$
> $\vec{u} = (1,2,3)$, $\vec{v} = (4,5,6)$:
> $$
> \vec{u} \cdot \vec{v} = 1\cdot4 + 2\cdot5 + 3\cdot6 = 4 + 10 + 18 = 32
> $$

#### Norma de un Vector

$$
\|\vec{v}\| = \sqrt{\vec{v} \cdot \vec{v}} = \sqrt{g_{ij} v^i v^j}
$$

En cartesianas: $\|\vec{v}\| = \sqrt{v^i v_i} = \sqrt{\delta_{ij} v^i v^j}$

#### Ángulo entre Vectores

$$
\cos \theta = \frac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \|\vec{v}\|} = \frac{g_{ij} u^i v^j}{\sqrt{g_{ij} u^i u^j} \sqrt{g_{ij} v^i v^j}}
$$

### Producto Vectorial en $\mathbb{R}^3$ (Producto Cruz)

El [[producto vectorial]] $\vec{w} = \vec{u} \times \vec{v}$ se escribe:

$$
w^i = \varepsilon^{ijk} u_j v_k
$$

o con índices covariantes:

$$
w_i = \varepsilon_{ijk} u^j v^k
$$

> [!example] Ejemplo 13: Producto vectorial
> $\vec{u} = (1,0,0)$, $\vec{v} = (0,1,0)$:
> - $w^1 = \varepsilon^{123} u_2 v_3 + \varepsilon^{132} u_3 v_2 = 1\cdot0\cdot0 + (-1)\cdot0\cdot1 = 0$
> - $w^2 = \varepsilon^{213} u_1 v_3 + \varepsilon^{231} u_3 v_1 = (-1)\cdot1\cdot0 + 1\cdot0\cdot0 = 0$
> - $w^3 = \varepsilon^{312} u_1 v_2 + \varepsilon^{321} u_2 v_1 = 1\cdot1\cdot1 + (-1)\cdot0\cdot0 = 1$
>
> Resultado: $\vec{w} = (0,0,1)$

---

## Expresión Matricial para Sistemas y Formas Cuadráticas

### Sistemas de Ecuaciones Lineales

Un sistema $A\vec{x} = \vec{b}$ se escribe:

$$
a^i_{\,j} x^j = b^i
$$

> [!example] Ejemplo 14: Sistema $2 \times 2$
> $$
> \begin{cases} 2x + 3y = 5 \\ 4x + 6y = 7 \end{cases}
> $$
> En notación de índices: $a^1_{\,1}x^1 + a^1_{\,2}x^2 = b^1$, $a^2_{\,1}x^1 + a^2_{\,2}x^2 = b^2$
> donde $a^1_{\,1}=2$, $a^1_{\,2}=3$, $a^2_{\,1}=4$, $a^2_{\,2}=6$, $b^1=5$, $b^2=7$.

### Formas Cuadráticas

Una [[forma cuadrática]] se escribe como:

$$
Q(\vec{x}) = \vec{x}^T A \vec{x} = a_{ij} x^i x^j
$$

donde $a_{ij}$ son los coeficientes (usualmente simétricos: $a_{ij} = a_{ji}$).

> [!example] Ejemplo 15: Forma cuadrática en $\mathbb{R}^2$
> Para $A = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}$:
> $$
> Q(x,y) = 2x^2 + 2xy + 3y^2 = a_{11}x^1x^1 + a_{12}x^1x^2 + a_{21}x^2x^1 + a_{22}x^2x^2
> $$

---

## Transformación Lineal

Una [[transformación lineal]] $T: \mathbb{R}^n \to \mathbb{R}^m$ se representa como:

$$
\bar{x}^i = a^i_{\,j} x^j
$$

donde $a^i_{\,j}$ son las componentes de la matriz asociada.

> [!example] Ejemplo 16: Rotación en $\mathbb{R}^2$
> Rotación por ángulo $\theta$:
> $$
> \bar{x}^1 = (\cos\theta) x^1 - (\sin\theta) x^2
> $$
> $$
> \bar{x}^2 = (\sin\theta) x^1 + (\cos\theta) x^2
> $$
> Matriz asociada: $a^1_{\,1} = \cos\theta$, $a^1_{\,2} = -\sin\theta$, $a^2_{\,1} = \sin\theta$, $a^2_{\,2} = \cos\theta$

### Composición de Transformaciones

Si $T_1: \mathbb{R}^n \to \mathbb{R}^p$ y $T_2: \mathbb{R}^p \to \mathbb{R}^m$, entonces $T = T_2 \circ T_1$ tiene componentes:

$$
c^i_{\,j} = b^i_{\,k} a^k_{\,j}
$$

### Distancia en un Sistema Coordenado Cartesiano

En coordenadas cartesianas, la distancia entre dos puntos $\vec{x}$ e $\vec{y}$ es:

$$
d(\vec{x}, \vec{y}) = \sqrt{(\vec{x} - \vec{y})^T (\vec{x} - \vec{y})} = \sqrt{\delta_{ij} \Delta x^i \Delta x^j}
$$

#### Transformación de Coordenadas

Consideremos una transformación lineal $\bar{\vec{x}} = A \vec{x}$ (con $\det A \neq 0$). La distancia en coordenadas transformadas se relaciona con:

$$
d(\bar{\vec{x}}, \bar{\vec{y}}) = \sqrt{(\bar{\vec{x}} - \bar{\vec{y}})^T G (\bar{\vec{x}} - \bar{\vec{y}})} = \sqrt{g_{ij} \Delta \bar{x}^i \Delta \bar{x}^j}
$$

donde:

$$
[g_{ij}]_{n \times n} \equiv G = (A A^T)^{-1}
$$

y $\Delta \bar{x}^i = \bar{x}^i - \bar{y}^i$.

> [!example] Ejemplo 17: Transformación lineal con métrica inducida
> Sea $A = \begin{pmatrix} 2 & 0 \\ 0 & 1 \end{pmatrix}$ (escalamiento en $x$).
> $$
> A A^T = \begin{pmatrix} 4 & 0 \\ 0 & 1 \end{pmatrix}, \quad G = (A A^T)^{-1} = \begin{pmatrix} 1/4 & 0 \\ 0 & 1 \end{pmatrix}
> $$
> La distancia en coordenadas transformadas:
> $$
> d^2 = \frac{1}{4}(\Delta \bar{x}^1)^2 + (\Delta \bar{x}^2)^2
> $$

### Casos Especiales

#### Rotación de Ejes

Para una rotación pura, $A$ es ortogonal: $A A^T = I$, por lo tanto $G = I$. La distancia es invariante:

$$
d(\bar{\vec{x}}, \bar{\vec{y}}) = \sqrt{(\Delta \bar{x}^1)^2 + (\Delta \bar{x}^2)^2 + \dots + (\Delta \bar{x}^n)^2}
$$

#### Escalamiento

Para $A = \text{diag}(\lambda_1, \lambda_2, \dots, \lambda_n)$:

$$
g_{ij} = \frac{1}{\lambda_i^2} \delta_{ij} \quad \text{(sin suma sobre $i$)}
$$

---

## Transformación de Coordenadas Generalizada

### Transformaciones No Lineales

Una transformación de coordenadas generalizada (posiblemente no lineal) se escribe:

$$
\bar{x}^i = T^i(x^1, x^2, \dots, x^N), \quad i = 1, \dots, N
$$

o en forma vectorial:

$$
\bar{\vec{x}} = \mathbf{T}(\vec{x})
$$

> [!example] Ejemplo 18: Coordenadas polares
> En $\mathbb{R}^2$, transformación de cartesianas a polares:
> $$
> \bar{x}^1 = r = \sqrt{(x^1)^2 + (x^2)^2}
> $$
> $$
> \bar{x}^2 = \theta = \arctan\left(\frac{x^2}{x^1}\right)
> $$

### Coordenadas Curvilíneas

Cuando la transformación no es lineal, las coordenadas $\bar{x}^i$ se denominan [[coordenadas curvilíneas]]. Ejemplos:

- **Coordenadas polares**: $(r, \theta)$
- **Coordenadas cilíndricas**: $(r, \theta, z)$
- **Coordenadas esféricas**: $(r, \theta, \phi)$

### Biyecciones y Cambio de Coordenadas

Para que la transformación sea un cambio de coordenadas válido, $\mathbf{T}$ debe ser una [[biyección]] (al menos localmente) con $\det \left( \frac{\partial \bar{x}^i}{\partial x^j} \right) \neq 0$.

---

## Regla de la Cadena en Derivadas Parciales

### Transformación de Derivadas

Bajo un cambio de coordenadas $x \mapsto \bar{x}(x)$, las derivadas parciales se transforman mediante la [[regla de la cadena]]:

$$
\frac{\partial}{\partial x^j} = \frac{\partial \bar{x}^i}{\partial x^j} \frac{\partial}{\partial \bar{x}^i}
$$

### Matriz Jacobiana

La [[matriz jacobiana]] de la transformación es:

$$
J^i_{\,j} = \frac{\partial \bar{x}^i}{\partial x^j}
$$

Su inversa satisface:

$$
\frac{\partial x^i}{\partial \bar{x}^j} = (J^{-1})^i_{\,j}
$$

### Transformación de Vectores

Un vector contravariante $\vec{v}$ con componentes $v^i$ se transforma como:

$$
\bar{v}^i = \frac{\partial \bar{x}^i}{\partial x^j} v^j
$$

Un vector covariante (1-forma) $\tilde{\omega}$ con componentes $\omega_i$ se transforma como:

$$
\bar{\omega}_i = \frac{\partial x^j}{\partial \bar{x}^i} \omega_j
$$

> [!example] Ejemplo 19: Gradiente en coordenadas polares
> En coordenadas cartesianas, el gradiente es $\nabla f = \left( \frac{\partial f}{\partial x}, \frac{\partial f}{\partial y} \right)$.
>
> En coordenadas polares $(r,\theta)$:
> $$
> \frac{\partial}{\partial x} = \cos\theta \frac{\partial}{\partial r} - \frac{\sin\theta}{r} \frac{\partial}{\partial \theta}
> $$
> $$
> \frac{\partial}{\partial y} = \sin\theta \frac{\partial}{\partial r} + \frac{\cos\theta}{r} \frac{\partial}{\partial \theta}
> $$
>
> Las componentes del gradiente en coordenadas polares son:
> $$
> (\nabla f)_r = \frac{\partial f}{\partial r}, \quad (\nabla f)_\theta = \frac{1}{r} \frac{\partial f}{\partial \theta}
> $$

### Transformación de Tensores

Un tensor de rango $(p,q)$ (con $p$ índices arriba y $q$ abajo) se transforma como:

$$
\bar{T}^{i_1 \dots i_p}_{\,j_1 \dots j_q} = \frac{\partial \bar{x}^{i_1}}{\partial x^{k_1}} \cdots \frac{\partial \bar{x}^{i_p}}{\partial x^{k_p}} \frac{\partial x^{l_1}}{\partial \bar{x}^{j_1}} \cdots \frac{\partial x^{l_q}}{\partial \bar{x}^{j_q}} T^{k_1 \dots k_p}_{\,l_1 \dots l_q}
$$

---

## Tabla de Correspondencias

| Concepto | Notación Matricial | Notación de Índices |
|----------|-------------------|---------------------|
| Vector abstracto | $\vec{v}$ | $\vec{v} = v^i \vec{e}_i$ |
| Vector columna | $[\vec{v}] = [v^i]$ | $v^i$ |
| Vector fila (1-forma) | $[\tilde{\omega}] = [\omega_i]$ | $\omega_i$ |
| Producto interno | $\vec{u}^T \vec{v}$ (cartesiano) | $g_{ij} u^i v^j$ |
| Métrica | $G = [g_{ij}]$ | $g_{ij}$ |
| Multiplicación matriz-vector | $A\vec{v}$ | $a^i_{\,j} v^j$ |
| Producto de matrices | $C = AB$ | $c^i_{\,j} = a^i_{\,k} b^k_{\,j}$ |
| Traza | $\operatorname{tr}(A)$ | $a^i_{\,i}$ |
| Determinante ($n=3$) | $\det(A)$ | $\varepsilon_{ijk} a^i_{\,1} a^j_{\,2} a^k_{\,3}$ |
| Producto vectorial ($\mathbb{R}^3$) | $\vec{u} \times \vec{v}$ | $\varepsilon^{ijk} u_j v_k$ |
| Matriz identidad | $I$ | $\delta^i_{\,j}$ |
| Transformación lineal | $\bar{\vec{x}} = A\vec{x}$ | $\bar{x}^i = a^i_{\,j} x^j$ |
| Jacobiana | $J = \frac{\partial \bar{x}}{\partial x}$ | $J^i_{\,j} = \frac{\partial \bar{x}^i}{\partial x^j}$ |
| Regla de la cadena | $\nabla_{\bar{x}} = J \nabla_x$ | $\frac{\partial}{\partial x^j} = \frac{\partial \bar{x}^i}{\partial x^j} \frac{\partial}{\partial \bar{x}^i}$ |

---

## Ejercicios Propuestos

> [!question] Ejercicio 1
> Dadas las matrices $A = \begin{pmatrix} 1 & 2 \\ 3 & 4 \end{pmatrix}$ y $B = \begin{pmatrix} 5 & 6 \\ 7 & 8 \end{pmatrix}$, calcular $C = AB$ en notación de índices.

<details>
<summary>Solución</summary>

$c^i_{\,j} = a^i_{\,k} b^k_{\,j}$.
- $c^1_{\,1} = a^1_{\,1}b^1_{\,1} + a^1_{\,2}b^2_{\,1} = 1\cdot5 + 2\cdot7 = 19$
- $c^1_{\,2} = a^1_{\,1}b^1_{\,2} + a^1_{\,2}b^2_{\,2} = 1\cdot6 + 2\cdot8 = 22$
- $c^2_{\,1} = a^2_{\,1}b^1_{\,1} + a^2_{\,2}b^2_{\,1} = 3\cdot5 + 4\cdot7 = 43$
- $c^2_{\,2} = a^2_{\,1}b^1_{\,2} + a^2_{\,2}b^2_{\,2} = 3\cdot6 + 4\cdot8 = 50$
</details>

> [!question] Ejercicio 2
> Demostrar que $\varepsilon_{ijk} \varepsilon_{ilm} = \delta_{jl}\delta_{km} - \delta_{jm}\delta_{kl}$.

<details>
<summary>Pista</summary>

Esta es la identidad fundamental del símbolo de Levi-Civita. Verificar caso por caso o usar propiedades de antisimetría.
</details>

> [!question] Ejercicio 3
> Calcular el determinante de $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 5 & 6 \\ 7 & 8 & 9 \end{pmatrix}$ usando la notación de índices con $\varepsilon_{ijk}$.

<details>
<summary>Solución</summary>

$\det(A) = \varepsilon_{ijk} a^i_{\,1} a^j_{\,2} a^k_{\,3}$.
Sumando sobre todas las permutaciones:
- Permutación par (123): $1\cdot5\cdot9 = 45$
- Permutación par (231): $2\cdot6\cdot7 = 84$
- Permutación par (312): $3\cdot4\cdot8 = 96$
- Permutación impar (132): $-1\cdot6\cdot8 = -48$
- Permutación impar (213): $-2\cdot4\cdot9 = -72$
- Permutación impar (321): $-3\cdot5\cdot7 = -105$
Total: $45+84+96-48-72-105 = 0$
</details>

> [!question] Ejercicio 4
> Expresar la norma de un vector $\vec{v} = (v^1, v^2, v^3)$ en notación de índices.

<details>
<summary>Solución</summary>

$\|\vec{v}\| = \sqrt{v^i v_i} = \sqrt{\delta_{ij} v^i v^j} = \sqrt{(v^1)^2 + (v^2)^2 + (v^3)^2}$
</details>

> [!question] Ejercicio 5
> Dada la transformación lineal $\bar{x}^1 = 2x^1 + x^2$, $\bar{x}^2 = x^1 + 3x^2$, encontrar la matriz $G$ para la distancia en coordenadas transformadas.

<details>
<summary>Solución</summary>

$A = \begin{pmatrix} 2 & 1 \\ 1 & 3 \end{pmatrix}$, $A A^T = \begin{pmatrix} 5 & 5 \\ 5 & 10 \end{pmatrix}$, $G = (A A^T)^{-1} = \frac{1}{25} \begin{pmatrix} 10 & -5 \\ -5 & 5 \end{pmatrix} = \begin{pmatrix} 2/5 & -1/5 \\ -1/5 & 1/5 \end{pmatrix}$
</details>

> [!question] Ejercicio 6
> Dado el vector $\vec{v} = 2\vec{e}_1 - 3\vec{e}_2 + \vec{e}_3$ en la base cartesiana, escribir sus componentes $v^i$ y su representación matricial.

<details>
<summary>Solución</summary>

$v^1 = 2$, $v^2 = -3$, $v^3 = 1$
Representación matricial: $\begin{bmatrix} 2 \\ -3 \\ 1 \end{bmatrix}$
</details>

> [!question] Ejercicio 7
> Explica por qué la notación $\vec{v} = (v^1, v^2, v^3)$ es una simplificación y cuál es la forma rigurosa de escribir un vector en notación de índices.

<details>
<summary>Solución</summary>

La notación $\vec{v} = (v^1, v^2, v^3)$ identifica el vector con sus componentes, lo cual solo es válido en una base fija (generalmente la cartesiana ortonormal). La forma rigurosa es $\vec{v} = v^i \vec{e}_i$, donde $\vec{e}_i$ son los vectores base y hay suma sobre $i$. Esta forma deja explícita la dependencia de la base.
</details>

> [!question] Ejercicio 8
> En coordenadas polares, la métrica es $g_{rr}=1$, $g_{\theta\theta}=r^2$, $g_{r\theta}=g_{\theta r}=0$. Dado un vector $\vec{v} = v^r \vec{e}_r + v^\theta \vec{e}_\theta$, calcular sus componentes covariantes $v_r$ y $v_\theta$.

<details>
<summary>Solución</summary>

$v_r = g_{rr} v^r + g_{r\theta} v^\theta = 1 \cdot v^r + 0 \cdot v^\theta = v^r$
$v_\theta = g_{\theta r} v^r + g_{\theta\theta} v^\theta = 0 \cdot v^r + r^2 \cdot v^\theta = r^2 v^\theta$
</details>

---

## Notas Relacionadas

- [[Notación de Índices en Sumatorias]]
- [[Delta de Kronecker]]
- [[Símbolo de Levi-Civita]]
- [[Derivada de una Forma Cuadrática en Notación de Índices]]
- [[Coordenadas Curvilíneas]]
- [[Cálculo Tensorial]]
- [[Geometría Diferencial]]
- [[Espacio Dual y 1-Formas]]
- [[Tensor Métrico]]
- [[Matriz Jacobiana]]
- [[Determinante]]
- [[Matriz Inversa]]
- [[Matriz Transpuesta]]
- [[Producto Vectorial]]
- [[Forma Cuadrática]]
- [[Transformación Lineal]]
- [[Regla de la Cadena]]
