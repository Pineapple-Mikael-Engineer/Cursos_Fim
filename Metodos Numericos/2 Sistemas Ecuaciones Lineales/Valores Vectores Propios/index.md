---
title: Valores Vectores Propios
order: 3
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - autovalores
  - autovectores
  - index
draft: false
aliases:
  - Eigenvalues
  - Eigenvectors
  - Teoría espectral
---

# Valores y Vectores Propios

> [!definicion]
> Dada una matriz $A \in \mathbb{R}^{n \times n}$, un **valor propio** (autovalor) es un escalar $\lambda \in \mathbb{C}$ para el cual existe un vector no nulo $v \in \mathbb{C}^n$, llamado **vector propio** (autovector), que satisface:
> $$A v = \lambda v$$

> [!info]
> El par $(\lambda, v)$ representa una dirección $v$ que $A$ no rota, solo escala por factor $\lambda$.

---

## Polinomio característico

> [!teorema]
> $\lambda$ es autovalor de $A$ si y solo si $\det(A - \lambda I) = 0$.
>
> El polinomio $p(\lambda) = \det(A - \lambda I)$ es el **polinomio característico** de $A$, de grado $n$.

> [!ejemplo]
> Para $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$:
> $$p(\lambda) = \det \begin{pmatrix} 2-\lambda & 1 \\ 1 & 2-\lambda \end{pmatrix} = (2-\lambda)^2 - 1 = \lambda^2 - 4\lambda + 3 = (\lambda - 3)(\lambda - 1)$$
> Autovalores: $\lambda_1 = 3$, $\lambda_2 = 1$.

---

## Propiedades fundamentales

> [!proposicion]
> 1. La suma de los autovalores (contando multiplicidades) es la **traza**:
>    $$\sum_{i=1}^n \lambda_i = \operatorname{tr}(A) = \sum_{i=1}^n a_{ii}$$
>
> 2. El producto de los autovalores es el **determinante**:
>    $$\prod_{i=1}^n \lambda_i = \det(A)$$
>
> 3. Si $A$ es simétrica ($A^T = A$), todos sus autovalores son **reales**.
>
> 4. Si $A$ es definida positiva ($x^T A x > 0$ para $x \neq 0$), todos sus autovalores son **positivos**.
>
> 5. Los autovalores de $A^{-1}$ son $1/\lambda_i$ (si $A$ es no singular).
>
> 6. Los autovalores de $A^k$ son $\lambda_i^k$.

---

## Multiplicidades

> [!definicion]
> - **Multiplicidad algebraica:** la multiplicidad de $\lambda$ como raíz del polinomio característico.
> - **Multiplicidad geométrica:** la dimensión del autoespacio $\{v : A v = \lambda v\}$.
>
> Siempre se cumple: $1 \leq \text{mult. geométrica} \leq \text{mult. algebraica}$.

> [!warning]
> Una matriz es **diagonalizable** si y solo si la multiplicidad geométrica de cada autovalor coincide con su multiplicidad algebraica.

---

## Diagonalización

> [!teorema]
> Si $A$ tiene $n$ autovectores linealmente independientes $v_1, \dots, v_n$, entonces:
> $$A = V \Lambda V^{-1}$$
> donde $V = [v_1 \cdots v_n]$ y $\Lambda = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$.

> [!corolario]
> $A^k = V \Lambda^k V^{-1}$. Si $|\lambda_1| > |\lambda_2| \geq \cdots \geq |\lambda_n|$, entonces para $k$ grande:
> $$A^k \approx \lambda_1^k v_1 w_1^T$$
> donde $w_1^T$ es la primera fila de $V^{-1}$. Esta es la base del [[Metodo Potencia Directo/Fundamentos Valor Propio Dominante|método de la potencia]].

---

## Localización de autovalores: Círculos de Gershgorin

> [!teorema]
> Todo autovalor $\lambda$ de $A$ satisface:
> $$|\lambda - a_{ii}| \leq \sum_{j \neq i} |a_{ij}| \quad \text{para algún } i$$
>
> Es decir, cada autovalor pertenece a al menos uno de los discos de Gershgorin:
> $$D_i = \left\{ z \in \mathbb{C} : |z - a_{ii}| \leq \sum_{j \neq i} |a_{ij}| \right\}$$

> [!ejemplo]
> Para $A = \begin{pmatrix} 4 & -1 & 0 \\ -1 & 4 & -1 \\ 0 & -1 & 4 \end{pmatrix}$:
> - Disco 1: centro $4$, radio $1$ → $[3, 5]$
> - Disco 2: centro $4$, radio $2$ → $[2, 6]$
> - Disco 3: centro $4$, radio $1$ → $[3, 5]$
>
> Los autovalores reales están en $[2, 6]$ (de hecho son $\lambda \approx 4 \pm \sqrt{2}$ y $4$).

---

## Métodos numéricos para calcular autovalores

No existe un método directo finito para autovalores (teorema de Abel-Ruffini). Todos los métodos son iterativos.

### Método de la potencia

Calcula el autovalor de mayor módulo ($|\lambda_1|$) y su autovector.

> [!info]
> Desarrollado en [[Metodo Potencia Directo/index]].


### Potencia inversa

Calcula el autovalor de menor módulo o el más cercano a un valor $\mu$.

>  [!info]
> Desarrollado en [[Variantes Metodo Potencia/index]].

### Potencia desplazada

Aceleración de convergencia mediante desplazamiento óptimo $\mu$.

> [!info]
> Desarrollado en [[Variantes Metodo Potencia/index]].

---

## Ejemplo completo

> [!ejemplo]
> **Matriz:**
> $$A = \begin{pmatrix} 2 & -1 & 0 \\ -1 & 2 & -1 \\ 0 & -1 & 2 \end{pmatrix}$$
>
> **Polinomio característico:**
> $$p(\lambda) = (2-\lambda)[(2-\lambda)^2 - 1] - (-1)[(-1)(2-\lambda)] = (2-\lambda)^3 - 2(2-\lambda)$$
> $$= (2-\lambda)[(2-\lambda)^2 - 2] = (2-\lambda)(\lambda^2 - 4\lambda + 2)$$
>
> **Autovalores:**
> $$\lambda_1 = 2 + \sqrt{2} \approx 3.414, \quad \lambda_2 = 2, \quad \lambda_3 = 2 - \sqrt{2} \approx 0.586$$
>
> **Autovectores:**
> $$v_1 = (1, \sqrt{2}, 1)^T, \quad v_2 = (1, 0, -1)^T, \quad v_3 = (1, -\sqrt{2}, 1)^T$$
>
> **Verificación:**
> - $\operatorname{tr}(A) = 2+2+2 = 6 = \lambda_1+\lambda_2+\lambda_3 = 3.414 + 2 + 0.586$
> - $\det(A) = 2(4-1) + 1(-2) = 6 - 2 = 4 = \lambda_1 \lambda_2 \lambda_3 = 3.414 \times 2 \times 0.586 \approx 4$

---

## Relación con estabilidad de sistemas

> [!teoria]
> En sistemas dinámicos lineales $y^{(k+1)} = A y^{(k)}$:
> - El estado tiende a $0$ si $\rho(A) < 1$ (todos los autovalores dentro del círculo unitario)
> - El estado crece si $\rho(A) > 1$
> - El autovalor dominante determina el comportamiento asintótico
>
> Por esto, el [[Metodo Potencia Directo/Fundamentos Valor Propio Dominante|método de la potencia]] es fundamental en análisis de estabilidad.

---

## Resumen

> [!corolario]
> Los valores y vectores propios son herramientas centrales del álgebra lineal con aplicaciones en estabilidad, vibraciones, optimización y reducción de dimensionalidad. Su cálculo numérico requiere métodos iterativos como el método de la potencia (autovalor dominante), potencia inversa (autovalor menor módulo) y potencia desplazada (aceleración). Las propiedades espectrales (traza, determinante, círculos de Gershgorin) permiten estimar y validar resultados numéricos.