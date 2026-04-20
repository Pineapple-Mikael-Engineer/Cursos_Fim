---
title: Derivada de una Forma Cuadrática en Notación de Índices
tags:
  - matemáticas
  - cálculo
  - álgebra-lineal
  - notación-índices
  - derivadas-parciales
  - formas-cuadráticas
  - delta-kronecker
draft: false
---

# Derivada de una Forma Cuadrática en Notación de Índices

> [!abstract] Contexto
> Este ejercicio muestra cómo calcular la derivada parcial de una [[forma cuadrática]] $Q = a_{ij} x_i x_j$ con respecto a una variable $x_k$ usando la [[notación de índices]] y el [[convenio de sumación de Einstein|convenio de Einstein]].

## Planteamiento del Problema

Calcular la siguiente derivada parcial:

$$
\frac{\partial}{\partial x_k} \left( a_{ij} x_i x_j \right)
$$

donde:
- $a_{ij}$ son coeficientes constantes (no dependen de $\mathbf{x}$)
- Se usa el [[convenio de sumación de Einstein]]: suma sobre índices repetidos $i$ y $j$
- $x_i$ son las variables independientes

## Herramientas Fundamentales

Antes de resolver, recordemos dos herramientas clave:

> [!teoria] Regla del Producto y Delta de Kronecker
> 1. **Regla del producto** para derivadas parciales:
>    $$
>    \frac{\partial}{\partial x_k} (x_i x_j) = x_i \frac{\partial x_j}{\partial x_k} + x_j \frac{\partial x_i}{\partial x_k}
>    $$
>
> 2. **Relación fundamental** con la [[Delta de Kronecker]]:
>    $$
>    \frac{\partial x_p}{\partial x_q} = \delta_{pq}
>    $$
>    donde $\delta_{pq}$ vale 1 si $p = q$ y 0 en caso contrario.

---

## Método 1: Expansión Directa de la Sumatoria (Enfoque Didáctico)

Este método muestra explícitamente cómo se comportan los términos de la suma.

### Paso 1: Descomposición de la Sumatoria Doble

Primero, escribimos explícitamente la suma sobre todos los pares $(i,j)$:

$$
S = \sum_{i=1}^{n} \sum_{j=1}^{n} a_{ij} x_i x_j
$$

Para derivar con respecto a $x_k$, debemos identificar los términos que contienen $x_k$. Estos son:

1. **Términos con $i = k$, $j \neq k$**: $x_k$ aparece solo en $x_i$
2. **Términos con $i \neq k$, $j = k$**: $x_k$ aparece solo en $x_j$
3. **Término con $i = k$, $j = k$**: $x_k$ aparece como $x_k \cdot x_k = x_k^2$

Visualmente, podemos separar la suma en cuatro regiones:

$$
\sum_{i,j} a_{ij}x_ix_j = 
\underbrace{\sum_{\substack{i=k \\ j \neq k}} a_{ij}x_ix_j}_{\text{1. solo } x_k \text{ en } x_i} +
\underbrace{\sum_{\substack{i \neq k \\ j=k}} a_{ij}x_ix_j}_{\text{2. solo } x_k \text{ en } x_j} +
\underbrace{\sum_{\substack{i=k \\ j=k}} a_{ij}x_ix_j}_{\text{3. } x_k \text{ aparece dos veces}} +
\underbrace{\sum_{\substack{i \neq k \\ j \neq k}} a_{ij}x_ix_j}_{\text{4. no contiene } x_k}
$$

> [!example] Ejemplo numérico para $n=3$, $k=2$
> La matriz $a_{ij}$ tiene 9 términos. Para $k=2$, los términos que contienen $x_2$ son:
> - $i=2$, $j=1$: $a_{21}x_2x_1$
> - $i=2$, $j=3$: $a_{23}x_2x_3$
> - $i=1$, $j=2$: $a_{12}x_1x_2$
> - $i=3$, $j=2$: $a_{32}x_3x_2$
> - $i=2$, $j=2$: $a_{22}x_2^2$
>
> El resto ($i=1,j=1$, $i=1,j=3$, $i=3,j=1$, $i=3,j=3$) no contienen $x_2$.

### Paso 2: Reexpresión de Cada Término

#### Término 1: $i = k$, $j \neq k$

Cuando $i=k$, tenemos $x_i = x_k$. El término se escribe como:

$$
\sum_{\substack{i=k \\ j \neq k}} a_{ij}x_ix_j = \left( \sum_{j \neq k} a_{kj} x_j \right) x_k
$$

#### Término 2: $i \neq k$, $j = k$

Cuando $j=k$, tenemos $x_j = x_k$:

$$
\sum_{\substack{i \neq k \\ j=k}} a_{ij}x_ix_j = \left( \sum_{i \neq k} a_{ik} x_i \right) x_k
$$

#### Término 3: $i = k$, $j = k$

Cuando ambos índices son $k$:

$$
\sum_{\substack{i=k \\ j=k}} a_{ij}x_ix_j = a_{kk} (x_k)^2
$$

#### Término 4: No contiene $x_k$

Este término es constante con respecto a $x_k$:

$$
C = \sum_{\substack{i \neq k \\ j \neq k}} a_{ij}x_ix_j
$$

### Paso 3: Suma de Todos los Términos

Agrupando todo:

$$
S = C + \left( \sum_{j \neq k} a_{kj} x_j \right) x_k + \left( \sum_{i \neq k} a_{ik} x_i \right) x_k + a_{kk} (x_k)^2
$$

### Paso 4: Derivación con Respecto a $x_k$

Ahora derivamos término por término:

1. $\displaystyle \frac{\partial}{\partial x_k}(C) = 0$

2. $\displaystyle \frac{\partial}{\partial x_k} \left[ \left( \sum_{j \neq k} a_{kj} x_j \right) x_k \right] = \sum_{j \neq k} a_{kj} x_j$

3. $\displaystyle \frac{\partial}{\partial x_k} \left[ \left( \sum_{i \neq k} a_{ik} x_i \right) x_k \right] = \sum_{i \neq k} a_{ik} x_i$

4. $\displaystyle \frac{\partial}{\partial x_k} \left[ a_{kk} (x_k)^2 \right] = 2 a_{kk} x_k$

Sumando:

$$
\frac{\partial S}{\partial x_k} = \sum_{j \neq k} a_{kj} x_j + \sum_{i \neq k} a_{ik} x_i + 2 a_{kk} x_k
$$

### Paso 5: Expansión a Sumatorias Completas

Observemos que:
- $\displaystyle \sum_{j \neq k} a_{kj} x_j + a_{kk} x_k = \sum_{j=1}^{n} a_{kj} x_j$
- $\displaystyle \sum_{i \neq k} a_{ik} x_i + a_{kk} x_k = \sum_{i=1}^{n} a_{ik} x_i$

Por lo tanto:

$$
\frac{\partial S}{\partial x_k} = \left( \sum_{j=1}^{n} a_{kj} x_j \right) + \left( \sum_{i=1}^{n} a_{ik} x_i \right)
$$

### Paso 6: Resultado Final (Método 1)

Renombrando el índice mudo en la segunda suma ($i \to j$):

$$
\boxed{\frac{\partial}{\partial x_k} (a_{ij} x_i x_j) = a_{kj} x_j + a_{jk} x_j}
$$

O equivalentemente:

$$
\frac{\partial}{\partial x_k} (a_{ij} x_i x_j) = (a_{ik} + a_{ki}) x_i
$$

---

## Método 2: Manipulación Algebraica con Delta de Kronecker (Enfoque Elegante)

Este método utiliza directamente la [[Delta de Kronecker]] y la regla del producto, resultando en un cálculo más conciso y elegante.

### Paso 1: Aplicar la Regla del Producto

Como los coeficientes $a_{ij}$ son constantes:

$$
\frac{\partial}{\partial x_k} (a_{ij} x_i x_j) = a_{ij} \frac{\partial}{\partial x_k} (x_i x_j)
$$

Aplicamos la [[regla del producto]]:

$$
\frac{\partial}{\partial x_k} (x_i x_j) = x_i \frac{\partial x_j}{\partial x_k} + x_j \frac{\partial x_i}{\partial x_k}
$$

### Paso 2: Introducir la Delta de Kronecker

Usamos la relación fundamental $\frac{\partial x_p}{\partial x_q} = \delta_{pq}$:

$$
\frac{\partial}{\partial x_k} (x_i x_j) = x_i \delta_{jk} + x_j \delta_{ik}
$$

> [!example] Verificación con un ejemplo concreto
> Para $n=3$, $k=2$, $i=1$, $j=3$:
> $$
> \frac{\partial}{\partial x_2}(x_1 x_3) = x_1 \underbrace{\frac{\partial x_3}{\partial x_2}}_{=\delta_{32}=0} + x_3 \underbrace{\frac{\partial x_1}{\partial x_2}}_{=\delta_{12}=0} = 0
> $$
> Correcto, porque $x_1 x_3$ no contiene $x_2$.

### Paso 3: Sustituir en la Expresión Original

$$
\frac{\partial}{\partial x_k} (a_{ij} x_i x_j) = a_{ij} (x_i \delta_{jk} + x_j \delta_{ik})
$$

Distribuimos:

$$
= a_{ij} x_i \delta_{jk} + a_{ij} x_j \delta_{ik}
$$

### Paso 4: Aplicar la Propiedad de Sustitución de la Delta

Recordemos que la [[Delta de Kronecker]] tiene la **propiedad de sustitución**:

- $\delta_{jk}$ "activa" el término cuando $j = k$: $a_{ij} x_i \delta_{jk} = a_{ik} x_i$
- $\delta_{ik}$ "activa" el término cuando $i = k$: $a_{ij} x_j \delta_{ik} = a_{kj} x_j$

Por lo tanto:

$$
\frac{\partial}{\partial x_k} (a_{ij} x_i x_j) = a_{ik} x_i + a_{kj} x_j
$$

### Paso 5: Renombrar Índices Mudos

En el primer término, $i$ es un índice mudo; en el segundo, $j$ es mudo. Podemos renombrar ambos a $i$ para unificar la expresión:

$$
\frac{\partial}{\partial x_k} (a_{ij} x_i x_j) = a_{ik} x_i + a_{ki} x_i
$$

Factorizando:

$$
\boxed{\frac{\partial}{\partial x_k} (a_{ij} x_i x_j) = (a_{ik} + a_{ki}) x_i}
$$

> [!success] Resultado Final (Método 2)
> $$
> \frac{\partial}{\partial x_k} (a_{ij} x_i x_j) = (a_{ik} + a_{ki}) x_i
> $$
> donde se entiende suma sobre $i$ (índice mudo).

---

## Comparación de Métodos

| Aspecto                 | Método 1 (Expansión Directa)                       | Método 2 (Delta de Kronecker)                |
| ----------------------- | -------------------------------------------------- | -------------------------------------------- |
| **Enfoque**             | Didáctico, muestra cada término                    | Algebraico, conciso                          |
| **Complejidad**         | Más pasos, requiere manejo cuidadoso de sumatorias | Menos pasos, requiere familiaridad con delta |
| **Riesgo de error**     | Mayor por la expansión explícita                   | Menor, pero requiere dominio de la notación  |
| **Utilidad pedagógica** | Excelente para entender qué ocurre                 | Ideal para cálculos rápidos                  |

> [!tip] Recomendación
> Es recomendable **aprender ambos métodos**. El primero desarrolla la intuición sobre el comportamiento de las sumatorias, mientras que el segundo es más eficiente para cálculos avanzados en [[cálculo tensorial]] y [[física matemática]].

---

## Casos Especiales

### Caso 1: Matriz Simétrica ($a_{ij} = a_{ji}$)

Si $a_{ij}$ es una [[matriz simétrica]]:

$$
\frac{\partial}{\partial x_k} (a_{ij} x_i x_j) = 2 a_{ki} x_i
$$

En forma vectorial, si $Q(\mathbf{x}) = \mathbf{x}^T A \mathbf{x}$ con $A$ simétrica:

$$
\nabla Q = 2A\mathbf{x}
$$

### Caso 2: Matriz Antisimétrica ($a_{ij} = -a_{ji}$)

Si $a_{ij}$ es antisimétrica, entonces $a_{ik} + a_{ki} = a_{ik} - a_{ik} = 0$:

$$
\frac{\partial}{\partial x_k} (a_{ij} x_i x_j) = 0
$$

Esto tiene sentido porque $a_{ij} x_i x_j = 0$ para matrices antisimétricas (el producto $x_i x_j$ es simétrico).

### Caso 3: Matriz General

Para una matriz general (no simétrica ni antisimétrica), el resultado es la suma de las partes simétrica y antisimétrica:

$$
(a_{ik} + a_{ki}) x_i = 2 \cdot \frac{a_{ik} + a_{ki}}{2} x_i = 2 \cdot (A_{\text{sym}})_{ik} x_i
$$

Donde $A_{\text{sym}} = \frac{A + A^T}{2}$ es la parte simétrica de $A$. Esto confirma que **solo la parte simétrica de la matriz contribuye al gradiente** de la forma cuadrática.

---

## Verificación con un Ejemplo Concreto

> [!example] Ejemplo Numérico: $n=2$, $k=1$
> Sea $a_{ij}$ una matriz $2 \times 2$:
> $$
> A = \begin{pmatrix} a_{11} & a_{12} \\ a_{21} & a_{22} \end{pmatrix}
> $$
> La forma cuadrática es:
> $$
> Q = a_{11}x_1^2 + a_{12}x_1x_2 + a_{21}x_2x_1 + a_{22}x_2^2
> $$
>
> **Método 1** (derivación directa):
> $$
> \frac{\partial Q}{\partial x_1} = 2a_{11}x_1 + a_{12}x_2 + a_{21}x_2
> $$
>
> **Método 2** (fórmula):
> $$
> \frac{\partial Q}{\partial x_1} = (a_{11} + a_{11})x_1 + (a_{12} + a_{21})x_2 = 2a_{11}x_1 + (a_{12} + a_{21})x_2
> $$
>
> ✅ Ambos métodos coinciden perfectamente.

---

## Aplicaciones

Esta derivada aparece frecuentemente en:

| Campo                       | Aplicación                                                                        |
| --------------------------- | --------------------------------------------------------------------------------- |
| [[Optimización]]            | Gradiente de funciones objetivo cuadráticas en [[mínimos cuadrados]]              |
| [[Machine Learning]]        | Derivadas de funciones de costo como el [[error cuadrático medio]]                |
| [[Mecánica clásica]]        | Derivadas de la [[energía cinética]] $T = \frac{1}{2} m_{ij} \dot{q}_i \dot{q}_j$ |
| [[Análisis de estabilidad]] | Linealización de sistemas no lineales alrededor de puntos de equilibrio           |
| [[Geometría diferencial]]   | Derivadas de [[métricas]] en coordenadas locales                                  |

---

## Ejercicios Propuestos

> [!question] Ejercicio 1
> Calcular $\frac{\partial}{\partial x_k} (b_i x_i)$, donde $b_i$ son constantes.
> 
> <details>
> <summary>Solución</summary>
> 
> $$
> \frac{\partial}{\partial x_k} (b_i x_i) = b_i \frac{\partial x_i}{\partial x_k} = b_i \delta_{ik} = b_k
> $$
> </details>

> [!question] Ejercicio 2
> Calcular $\frac{\partial}{\partial x_k} (a_{ij} b_{pq} x_i x_j x_p x_q)$, con $a_{ij}$ y $b_{pq}$ constantes.
> 
> <details>
> <summary>Pista</summary>
> 
> Aplicar la regla del producto generalizada y usar la delta de Kronecker. Cada término tendrá cuatro contribuciones, una por cada factor $x$.
> </details>

> [!question] Ejercicio 3
> Demostrar que $\frac{\partial}{\partial x_k} (x_i x_j x_i x_j) = 4 x_k x_i x_i$ (sumando sobre índices repetidos).
>
> <details>
> <summary>Solución</summary>
> 
> $$
> \frac{\partial}{\partial x_k} (x_i x_j x_i x_j) = \frac{\partial}{\partial x_k} (x_i x_i x_j x_j) = \frac{\partial}{\partial x_k} (|\mathbf{x}|^4) = 4 |\mathbf{x}|^2 x_k
> $$
> </details>

---

## Notas Relacionadas

- [[Notación de Índices en Sumatorias]]
- [[Delta de Kronecker]]
- [[Forma cuadrática]]
- [[Gradiente de una función]]
- [[Matriz Hessiana]]
- [[Convenio de sumación de Einstein]]
- [[Símbolo de Levi-Civita]]
- [[Regla del producto]]
- [[Derivación en notación de índices]]