---
title: Derivada de un Monomio Cuártico con Índices Repetidos
tags:
  - matemáticas
  - cálculo
  - notación-índices
  - derivadas-parciales
  - delta-kronecker
  - ejercicio-resuelto
  - monomio
draft: false
---

# Derivada de un Monomio Cuártico con Índices Repetidos

> [!abstract] Resumen
> Este ejercicio resuelto muestra cómo calcular la derivada parcial de un monomio de cuarto orden $M = x_i x_j x_i x_j$ con respecto a una variable $x_k$ usando la [[notación de índices]] y el [[convenio de sumación de Einstein]]. Se presentan dos enfoques: uno directo usando la regla del producto, y otro riguroso introduciendo [[Delta de Kronecker|deltas de Kronecker]] desde el inicio para explicitar la estructura de la suma.

## Planteamiento

Calcular la siguiente derivada parcial:

$$
\frac{\partial}{\partial x_k} \left( x_i x_j x_i x_j \right)
$$

donde:
- Se usa el [[convenio de sumación de Einstein]]: suma sobre índices repetidos $i$ y $j$
- $x_i$ son las variables independientes ($i = 1, \dots, n$)
- El monomio $x_i x_j x_i x_j$ tiene índices repetidos: $i$ aparece dos veces, $j$ aparece dos veces

> [!warning] Interpretación
> La expresión $x_i x_j x_i x_j$ es equivalente a:
> $$
> x_i x_j x_i x_j = \left( \sum_{i=1}^n x_i^2 \right) \left( \sum_{j=1}^n x_j^2 \right) = |\mathbf{x}|^2 |\mathbf{x}|^2 = |\mathbf{x}|^4
> $$
> Por lo tanto, esperamos que la derivada sea $4 |\mathbf{x}|^2 x_k$.

## Herramientas Fundamentales

> [!teoria] Relaciones Básicas
> 1. **Derivada de una variable**: 
>    $$
>    \frac{\partial x_p}{\partial x_q} = \delta_{pq}
>    $$
>
> 2. **Regla del producto generalizada**:
>    $$
>    \frac{\partial}{\partial x_k} (abcd) = \frac{\partial a}{\partial x_k} bcd + a \frac{\partial b}{\partial x_k} cd + ab \frac{\partial c}{\partial x_k} d + abc \frac{\partial d}{\partial x_k}
>    $$
>
> 3. **Propiedad de sustitución** de la [[Delta de Kronecker]]:
>    $$
>    \delta_{ij} a_j = a_i, \quad \delta_{ij} a_i = a_j
>    $$

---

## Método 1: Expansión Directa (Enfoque Intuitivo)

Este método reconoce que $x_i x_i = |\mathbf{x}|^2$ y simplifica el problema.

### Paso 1: Simplificar la Expresión

Observamos que los índices $i$ y $j$ son mudos e independientes:

$$
x_i x_j x_i x_j = (x_i x_i)(x_j x_j) = |\mathbf{x}|^2 |\mathbf{x}|^2 = |\mathbf{x}|^4
$$

### Paso 2: Derivar

$$
\frac{\partial}{\partial x_k} |\mathbf{x}|^4 = 4 |\mathbf{x}|^3 \frac{\partial |\mathbf{x}|}{\partial x_k}
$$

Sabemos que $\frac{\partial |\mathbf{x}|}{\partial x_k} = \frac{x_k}{|\mathbf{x}|}$ (para $\mathbf{x} \neq \mathbf{0}$).

### Paso 3: Resultado

$$
\frac{\partial}{\partial x_k} |\mathbf{x}|^4 = 4 |\mathbf{x}|^3 \cdot \frac{x_k}{|\mathbf{x}|} = 4 |\mathbf{x}|^2 x_k
$$

### Paso 4: Expresar en Notación de Índices

Como $|\mathbf{x}|^2 = x_i x_i$, tenemos:

$$
\boxed{\frac{\partial}{\partial x_k} (x_i x_j x_i x_j) = 4 x_k x_i x_i}
$$

> [!success] Resultado Clave
> $$
> \frac{\partial}{\partial x_k} (x_i x_j x_i x_j) = 4 x_k x_i x_i
> $$
> donde se entiende suma sobre $i$ en el último término.

---

## Método 2: Regla del Producto Directa (Enfoque Explícito)

Este método aplica la regla del producto directamente a los cuatro factores sin simplificar primero.

### Paso 1: Identificar los Factores

Escribimos el monomio como producto de cuatro factores:

$$
M = x_i \cdot x_j \cdot x_i \cdot x_j
$$

### Paso 2: Aplicar la Regla del Producto

Derivamos con respecto a $x_k$:

$$
\frac{\partial M}{\partial x_k} = \frac{\partial x_i}{\partial x_k} x_j x_i x_j + x_i \frac{\partial x_j}{\partial x_k} x_i x_j + x_i x_j \frac{\partial x_i}{\partial x_k} x_j + x_i x_j x_i \frac{\partial x_j}{\partial x_k}
$$

### Paso 3: Introducir la Delta de Kronecker

Usamos $\frac{\partial x_p}{\partial x_q} = \delta_{pq}$:

$$
\frac{\partial M}{\partial x_k} = \delta_{ik} x_j x_i x_j + x_i \delta_{jk} x_i x_j + x_i x_j \delta_{ik} x_j + x_i x_j x_i \delta_{jk}
$$

### Paso 4: Aplicar la Propiedad de Sustitución

**Primer término:** $\delta_{ik} x_j x_i x_j = x_j x_k x_j = x_k x_j x_j$

**Segundo término:** $x_i \delta_{jk} x_i x_j = x_i x_i x_k$

**Tercer término:** $x_i x_j \delta_{ik} x_j = x_k x_j x_j$

**Cuarto término:** $x_i x_j x_i \delta_{jk} = x_i x_k x_i = x_k x_i x_i$

### Paso 5: Sumar Todos los Términos

$$
\frac{\partial M}{\partial x_k} = x_k x_j x_j + x_i x_i x_k + x_k x_j x_j + x_k x_i x_i
$$

Observamos que:
- $x_j x_j = x_i x_i = |\mathbf{x}|^2$
- El primer y tercer término son iguales: $x_k |\mathbf{x}|^2 + x_k |\mathbf{x}|^2 = 2 x_k |\mathbf{x}|^2$
- El segundo y cuarto término son iguales: $x_k |\mathbf{x}|^2 + x_k |\mathbf{x}|^2 = 2 x_k |\mathbf{x}|^2$

### Paso 6: Resultado Final

$$
\frac{\partial M}{\partial x_k} = 4 x_k |\mathbf{x}|^2 = 4 x_k x_i x_i
$$

$$
\boxed{\frac{\partial}{\partial x_k} (x_i x_j x_i x_j) = 4 x_k x_i x_i}
$$

---

## Método 3: Introducción de Deltas desde el Inicio (Enfoque Riguroso)

Este método es el más riguroso. Es útil cuando la expresión tiene múltiples repeticiones de índices y se quiere evitar cualquier ambigüedad.

### Paso 1: Reescribir con Deltas

Para explicitar la suma sobre $i$ y $j$, introducimos deltas:

$$
x_i x_j x_i x_j = \delta_{ip} \delta_{jq} x_i x_j x_p x_q
$$

Esto es válido porque $\delta_{ip}$ fuerza $i=p$ y $\delta_{jq}$ fuerza $j=q$, recuperando la expresión original.

### Paso 2: Aplicar la Derivada

$$
\frac{\partial}{\partial x_k} (x_i x_j x_i x_j) = \delta_{ip} \delta_{jq} \frac{\partial}{\partial x_k} (x_i x_j x_p x_q)
$$

### Paso 3: Derivar el Producto de Cuatro Factores

Aplicamos la regla del producto generalizada:

$$
\begin{aligned}
\frac{\partial}{\partial x_k} (x_i x_j x_p x_q) = &\quad \frac{\partial x_i}{\partial x_k} x_j x_p x_q \\
&+ x_i \frac{\partial x_j}{\partial x_k} x_p x_q \\
&+ x_i x_j \frac{\partial x_p}{\partial x_k} x_q \\
&+ x_i x_j x_p \frac{\partial x_q}{\partial x_k}
\end{aligned}
$$

Introducimos deltas:

$$
= \delta_{ik} x_j x_p x_q + x_i \delta_{jk} x_p x_q + x_i x_j \delta_{pk} x_q + x_i x_j x_p \delta_{qk}
$$

### Paso 4: Sustituir en la Expresión Original

$$
\frac{\partial M}{\partial x_k} = \delta_{ip} \delta_{jq} \left( \delta_{ik} x_j x_p x_q + x_i \delta_{jk} x_p x_q + x_i x_j \delta_{pk} x_q + x_i x_j x_p \delta_{qk} \right)
$$

### Paso 5: Aplicar la Propiedad de Sustitución Paso a Paso

**Primer término:**
$$
\delta_{ip} \delta_{jq} \delta_{ik} x_j x_p x_q
$$
- $\delta_{ip} \delta_{ik} = \delta_{pk}$ (ya que $i$ se contrae)
- Queda: $\delta_{jq} \delta_{pk} x_j x_p x_q = \delta_{pk} x_j x_p x_j = \delta_{pk} x_j x_j x_p = x_k x_j x_j$

**Segundo término:**
$$
\delta_{ip} \delta_{jq} x_i \delta_{jk} x_p x_q = \delta_{ip} \delta_{jk} x_i x_p x_k = \delta_{ip} x_i x_p x_k = x_i x_i x_k
$$

**Tercer término:**
$$
\delta_{ip} \delta_{jq} x_i x_j \delta_{pk} x_q = \delta_{ik} \delta_{jq} x_i x_j x_q = \delta_{ik} x_i x_j x_j = x_k x_j x_j
$$

**Cuarto término:**
$$
\delta_{ip} \delta_{jq} x_i x_j x_p \delta_{qk} = \delta_{ip} \delta_{jk} x_i x_j x_p = \delta_{jk} x_i x_j x_i = x_i x_i x_k
$$

### Paso 6: Sumar Todos los Términos

$$
\frac{\partial M}{\partial x_k} = x_k x_j x_j + x_i x_i x_k + x_k x_j x_j + x_i x_i x_k = 4 x_k x_i x_i
$$

### Paso 7: Resultado Final

$$
\boxed{\frac{\partial}{\partial x_k} (x_i x_j x_i x_j) = 4 x_k x_i x_i}
$$

---

## Comparación de los Tres Métodos

| Aspecto                 | Método 1 (Expansión Directa)     | Método 2 (Regla del Producto)          | Método 3 (Deltas desde Inicio)            |
| ----------------------- | -------------------------------- | -------------------------------------- | ----------------------------------------- |
| **Enfoque**             | Reconoce $\|\mathbf{x}\|^4$            | Aplica regla del producto a 4 factores | Introduce deltas explícitamente           |
| **Complejidad**         | Muy baja                         | Media                                  | Alta                                      |
| **Pasos**               | 4                                | 6                                      | 7                                         |
| **Riesgo de error**     | Muy bajo                         | Bajo                                   | Moderado                                  |
| **Claridad conceptual** | Excelente                        | Buena                                  | Excelente (muestra cada suma)             |
| **Utilidad pedagógica** | Ideal para entender el resultado | Útil para practicar regla del producto | Útil para entender el papel de las deltas |

> [!tip] Recomendación
> El **Método 1** es el más eficiente para este caso particular. Sin embargo, el **Método 3** es invaluable para entender cómo las deltas de Kronecker gestionan las sumas múltiples y para generalizar a expresiones más complejas.

---

## Verificación con un Ejemplo Concreto

> [!example] Ejemplo Numérico: $n=3$, $k=2$
> Sea $\mathbf{x} = (x_1, x_2, x_3) = (1, 2, 3)$.
>
> Calculamos $M = x_i x_j x_i x_j = |\mathbf{x}|^4 = (1^2 + 2^2 + 3^2)^2 = (1 + 4 + 9)^2 = 14^2 = 196$
>
> Derivamos analíticamente usando la fórmula: $\frac{\partial M}{\partial x_2} = 4 x_2 |\mathbf{x}|^2 = 4 \cdot 2 \cdot 14 = 112$
>
> Ahora verificamos numéricamente con una aproximación de diferencia finita (con $h = 0.001$):
> - $M(x_2 + h) = (1^2 + (2.001)^2 + 3^2)^2 = (1 + 4.004001 + 9)^2 = (14.004001)^2 = 196.112056$
> - $M(x_2 - h) = (1^2 + (1.999)^2 + 3^2)^2 = (1 + 3.996001 + 9)^2 = (13.996001)^2 = 195.888056$
> - $\frac{M(x_2 + h) - M(x_2 - h)}{2h} \approx \frac{0.224}{0.002} = 112$ ✅

---


## Generalización

> [!teoria] Patrón General
> La expresión $x_i x_j x_i x_j$ es un caso particular de un patrón más general: un producto donde cada índice aparece exactamente dos veces.

### Caso 1: Producto de Bloques Repetidos

Sean $i_1, i_2, \dots, i_m$ índices (pueden ser iguales o diferentes). Definimos:

$$
M_m = \left( \prod_{r=1}^m x_{i_r} \right) \left( \prod_{r=1}^m x_{i_r} \right) = \left( \prod_{r=1}^m x_{i_r} \right)^2
$$

**Derivada:**
$$
\frac{\partial M_m}{\partial x_k} = 2 \left( \prod_{r=1}^m x_{i_r} \right) \cdot \frac{\partial}{\partial x_k} \left( \prod_{r=1}^m x_{i_r} \right)
$$

donde:
$$
\frac{\partial}{\partial x_k} \left( \prod_{r=1}^m x_{i_r} \right) = \sum_{r=1}^m \left( \delta_{i_r k} \prod_{\substack{s=1 \\ s \neq r}}^m x_{i_s} \right)
$$

### Caso 2: Todos los Índices Distintos

Si los $m$ índices $i_1, \dots, i_m$ son todos distintos, entonces para un $k$ dado:

$$
\frac{\partial}{\partial x_k} \left( \prod_{r=1}^m x_{i_r} \right) = \begin{cases}
\displaystyle \prod_{\substack{r=1 \\ i_r \neq k}}^m x_{i_r} & \text{si } k = i_r \text{ para algún } r \\
0 & \text{si } k \text{ no aparece entre los } i_r
\end{cases}
$$

Por lo tanto:
$$
\frac{\partial M_m}{\partial x_k} = 2 x_k \prod_{\substack{r=1 \\ i_r \neq k}}^m x_{i_r}^2
$$

### Caso 3: Extensión a Potencias Mayores

Para una expresión más general como:
$$
M = \prod_{r=1}^m x_{i_r}^{p_r}
$$

donde cada $i_r$ es un índice (con posible repetición) y $p_r \in \mathbb{N}$, la derivada es:

$$
\frac{\partial M}{\partial x_k} = \sum_{r=1}^m p_r \left( \delta_{i_r k} \cdot x_{i_r}^{p_r - 1} \prod_{\substack{s=1 \\ s \neq r}}^m x_{i_s}^{p_s} \right)
$$

### Ejemplo: Caso Particular $m=2$, $i_1 = i$, $i_2 = j$, $p_1 = p_2 = 2$

$$
M = x_i^2 x_j^2
$$

Derivada:
$$
\frac{\partial M}{\partial x_k} = 2 \delta_{ik} x_i x_j^2 + 2 \delta_{jk} x_i^2 x_j = 2 \delta_{ik} x_k x_j^2 + 2 \delta_{jk} x_i^2 x_k
$$

Si $k = i$: $\frac{\partial M}{\partial x_i} = 2 x_i x_j^2$
Si $k = j$: $\frac{\partial M}{\partial x_j} = 2 x_i^2 x_j$
Si $k$ es otro índice: $\frac{\partial M}{\partial x_k} = 0$

Esto coincide con la derivada directa de $(x_i^2 x_j^2)$.


---
## Ejercicios Propuestos

> [!question] Ejercicio 1
> Calcular $\frac{\partial}{\partial x_k} (x_i x_j x_i x_j)$ usando el Método 2 (regla del producto) pero agrupando los términos de manera diferente.

> [!question] Ejercicio 2
> Calcular $\frac{\partial}{\partial x_k} (x_i x_j x_i x_j x_p x_p)$.
>
> <details>
> <summary>Solución</summary>
>
> $$
> \frac{\partial}{\partial x_k} (x_i x_j x_i x_j x_p x_p) = 6 x_k x_i  x_i  x_j x_j
> $$
> </details>

> [!question] Ejercicio 3
> Usando el Método 3, demostrar que $\frac{\partial}{\partial x_k} (x_i x_j x_i x_j) = 4 x_k x_i x_i$ con una elección diferente de deltas (por ejemplo, $\delta_{im} \delta_{jn} x_i x_j x_m x_n$).

---

## Notas Relacionadas

- [[Derivada de un Monomio Cuártico con Índices Repetidos]]
- [[Delta de Kronecker]]
- [[Derivada de una Forma Cuadrática en Notación de Índices]]
- [[Convenio de sumación de Einstein]]
- [[Regla del producto]]
