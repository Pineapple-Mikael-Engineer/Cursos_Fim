---
title: Distribución de Sumatorias con Índices Libres y Mudos
tags:
  - matemáticas
  - notación-índices
  - convenio-einstein
  - índices-libres
  - índices-mudos
  - ejercicio-resuelto
  - álgebra-lineal
draft: false
---

# Distribución de Sumatorias con Índices Libres y Mudos

> [!abstract] Resumen
> Este ejercicio resuelto muestra un error común al trabajar con la [[notación de índices]] y el [[convenio de sumación de Einstein]]: la distribución incorrecta de sumatorias cuando hay índices libres involucrados. Se analiza por qué la expresión aparentemente obvia $a_{ijk} (x_i + y_j) z_k = a_{ijk} x_i z_k + a_{ijk} y_j z_k$ es **incorrecta** en notación de Einstein debido a la ambigüedad de índices libres.

## Planteamiento

Considere la siguiente expresión en notación de Einstein (suma sobre índices repetidos):

$$
a_{ijk} (x_i + y_j) z_k
$$

¿Es cierto que:

$$
a_{ijk} (x_i + y_j) z_k = a_{ijk} x_i z_k + a_{ijk} y_j z_k \quad \text{?}
$$

> [!warning] Advertencia
> A simple vista, parece una simple distribución de la suma. Sin embargo, **no es correcta** en notación de Einstein sin una aclaración explícita sobre los índices libres.

## Análisis del Problema

### Paso 1: Reescribir con un Tensor Auxiliar

Para entender mejor la estructura de índices, definamos un tensor $b_{ij}$ como:

$$
b_{ij} = x_i + y_j
$$

Observemos que:
- $i$ e $j$ son **índices libres** en $b_{ij}$
- $b_{ij}$ representa una **matriz** (o tensor de rango 2), no un escalar

La expresión original se reescribe como:

$$
a_{ijk} (x_i + y_j) z_k = a_{ijk} b_{ij} z_k
$$

### Paso 2: Analizar los Índices en la Expresión Original

En $a_{ijk} b_{ij} z_k$:
- $i$ aparece en $a_{ijk}$ y en $b_{ij}$ → dos veces → **índice mudo** (suma sobre $i$)
- $j$ aparece en $a_{ijk}$ y en $b_{ij}$ → dos veces → **índice mudo** (suma sobre $j$)
- $k$ aparece en $a_{ijk}$ y en $z_k$ → dos veces → **índice mudo** (suma sobre $k$)

Por lo tanto, **todos los índices son mudos**. El lado izquierdo es un **escalar**.

### Paso 3: Analizar la Expresión Propuesta

Ahora examinemos el lado derecho propuesto:

$$
a_{ijk} x_i z_k + a_{ijk} y_j z_k
$$

**Primer término:** $a_{ijk} x_i z_k$
- $i$ aparece en $a_{ijk}$ y $x_i$ → dos veces → mudo (suma sobre $i$)
- $k$ aparece en $a_{ijk}$ y $z_k$ → dos veces → mudo (suma sobre $k$)
- $j$ aparece **solo en $a_{ijk}$** → **una sola vez** → **índice libre**

Este término no es un escalar, sino una expresión con índice libre $j$. Representa un **vector** (o tensor de rango 1).

**Segundo término:** $a_{ijk} y_j z_k$
- $j$ aparece en $a_{ijk}$ y $y_j$ → dos veces → mudo (suma sobre $j$)
- $k$ aparece en $a_{ijk}$ y $z_k$ → dos veces → mudo (suma sobre $k$)
- $i$ aparece **solo en $a_{ijk}$** → **una sola vez** → **índice libre**

Este término tiene índice libre $i$. También es un vector.

### Paso 4: Identificar el Problema

| Expresión | Índices mudos | Índices libres | Tipo |
|-----------|---------------|----------------|------|
| $a_{ijk} (x_i + y_j) z_k$ | $i, j, k$ | ninguno | **Escalar** |
| $a_{ijk} x_i z_k$ | $i, k$ | $j$ | **Vector** (en $j$) |
| $a_{ijk} y_j z_k$ | $j, k$ | $i$ | **Vector** (en $i$) |
| $a_{ijk} x_i z_k + a_{ijk} y_j z_k$ | mixto | $i$ y $j$ simultáneamente | **Ambiguo** |

> [!danger] Error
> $$
> a_{ijk} (x_i + y_j) z_k \neq a_{ijk} x_i z_k + a_{ijk} y_j z_k
> $$
>
> **Razón:** 
> - El lado izquierdo es un **escalar** (todos los índices están contraídos)
> - El lado derecho es la suma de un **vector en $j$** y un **vector en $i$**, lo cual es una operación mal definida (no se pueden sumar objetos con diferentes estructuras de índices libres)
>
> La igualdad sería análoga a afirmar que un número es igual a la suma de un vector y otro vector.

### Paso 5: Visualización con la Notación de $b_{ij}$

Usando $b_{ij} = x_i + y_j$, la situación se vuelve más clara:

- Lado izquierdo: $a_{ijk} b_{ij} z_k$ (contracción completa → escalar)
- Lado derecho: $a_{ijk} x_i z_k + a_{ijk} y_j z_k$

Para que la distribución fuera válida, necesitaríamos que:

$$
a_{ijk} b_{ij} z_k = a_{ijk} (x_i + y_j) z_k \stackrel{?}{=} a_{ijk} x_i z_k + a_{ijk} y_j z_k
$$

Pero esto requeriría que en $a_{ijk} x_i z_k$ el índice $j$ sea mudo (apareciendo dos veces), y en $a_{ijk} y_j z_k$ el índice $i$ sea mudo. Como no es el caso, la distribución **rompe la estructura de contracción**.

---

## La Forma Correcta

### Opción 1: Usar Sumatorias Explícitas

La forma más clara es escribir explícitamente todas las sumatorias:

$$
\sum_{i=1}^n \sum_{j=1}^n \sum_{k=1}^n a_{ijk} (x_i + y_j) z_k = \sum_{i=1}^n \sum_{j=1}^n \sum_{k=1}^n a_{ijk} x_i z_k + \sum_{i=1}^n \sum_{j=1}^n \sum_{k=1}^n a_{ijk} y_j z_k
$$

En este caso, todas las sumatorias están explícitas y no hay ambigüedad.

### Opción 2: Contraer los Índices Libres

Si queremos mantener la notación de Einstein, podemos introducir vectores que contraigan los índices libres:

Por ejemplo, introduciendo un vector $u_j$ (o $v_i$) que sume sobre el índice libre:

$$
a_{ijk} (x_i + y_j) z_k = u_j (a_{ijk} x_i z_k) = v_i (a_{ijk} y_j z_k)
$$

pero esto ya no es una distribución directa.

### Opción 3: Definir un Tensor Auxiliar (tu propuesta)

La forma más elegante es definir $b_{ij} = x_i + y_j$ y trabajar con ella:

$$
a_{ijk} (x_i + y_j) z_k = a_{ijk} b_{ij} z_k
$$

Esto deja claro que la expresión es una **contracción completa** de tres índices, y que no se puede "separar" la suma $b_{ij}$ sin perder la estructura de contracción.

---

## Ejemplo Concreto

> [!example] Caso $n=2$ para ilustrar el error
>
> Sean $n=2$, y definamos:
> - $a_{111}=1$, todos los demás $a_{ijk}=0$
> - $x_1=1$, $x_2=0$
> - $y_1=0$, $y_2=1$
> - $z_1=1$, $z_2=1$
>
> **Lado izquierdo:**
> $$
> a_{ijk} (x_i + y_j) z_k = \sum_{i=1}^2 \sum_{j=1}^2 \sum_{k=1}^2 a_{ijk} (x_i + y_j) z_k
> $$
>
> Solo $a_{111}=1$, entonces $i=1$, $j=1$, $k=1$:
> $$
> = (x_1 + y_1) z_1 = (1 + 0) \cdot 1 = 1
> $$
>
> **Lado derecho (incorrecto):**
> $$
> a_{ijk} x_i z_k + a_{ijk} y_j z_k
> $$
>
> Primer término: $a_{ijk} x_i z_k$. Con $a_{111}=1$, $i=1$, $k=1$, pero $j$ es libre:
> - Para $j=1$: $a_{111} x_1 z_1 = 1 \cdot 1 \cdot 1 = 1$
> - Para $j=2$: $a_{121} x_1 z_1 = 0$
>
> Esto da el vector $(1, 0)$ en el espacio de $j$.
>
> Segundo término: $a_{ijk} y_j z_k$. Con $a_{111}=1$, $j=1$, $k=1$, pero $i$ es libre:
> - Para $i=1$: $a_{111} y_1 z_1 = 1 \cdot 0 \cdot 1 = 0$
> - Para $i=2$: $a_{211} y_1 z_1 = 0$
>
> Esto da el vector $(0, 0)$ en el espacio de $i$.
>
> La suma de estos dos términos es $(1, 0)$ (en $j$) + $(0, 0)$ (en $i$), que **no es un escalar** sino una expresión ambigua que combina índices diferentes. No es igual a $1$.

---

## Reglas Clave para Evitar este Error

> [!teoria] Reglas de Oro en Notación de Einstein
>
> 1. **Un índice no puede aparecer más de dos veces** en un mismo término.
>
> 2. **Un índice que aparece dos veces es un índice mudo** (se suma sobre él).
>
> 3. **Un índice que aparece una sola vez es un índice libre** y debe ser el mismo en todos los términos de una ecuación.
>
> 4. **Al distribuir una suma**, hay que tener cuidado de no crear índices libres donde antes no los había.
>
> 5. **Si una expresión tiene índices libres, representa una familia de valores** (un vector, matriz, etc.), no un escalar.
>
> 6. **Una forma de evitar errores** es definir tensores auxiliares que capturen la estructura de índices, como $b_{ij} = x_i + y_j$, para visualizar claramente qué índices están libres antes de la contracción.

---

## Ejercicios Propuestos

> [!question] Ejercicio 1
> ¿Es correcta la siguiente igualdad? Justificar.
> $$
> a_{ij} (x_i + y_i) = a_{ij} x_i + a_{ij} y_i
> $$

<details>
<summary>Solución</summary>

**Sí, es correcta.** En este caso, ambos términos tienen el mismo índice libre $j$:
- $a_{ij} x_i$: suma sobre $i$, índice libre $j$
- $a_{ij} y_i$: suma sobre $i$, índice libre $j$

La suma tiene sentido porque ambos son vectores (con índice $j$).
</details>

> [!question] Ejercicio 2
> ¿Es correcta la siguiente igualdad?
> $$
> a_{ij} (x_i + y_j) = a_{ij} x_i + a_{ij} y_j
> $$

<details>
<summary>Solución</summary>

**No es correcta.** 
- Lado izquierdo: $i$ y $j$ son mudos (cada uno aparece dos veces) → escalar
- Lado derecho: primer término tiene $j$ libre, segundo término tiene $i$ libre → suma de un vector (en $j$) y un vector (en $i$), que no es un escalar.

La igualdad es incorrecta por la misma razón que el ejercicio principal.
</details>

> [!question] Ejercicio 3
> Usando la idea del tensor auxiliar $b_{ij} = x_i + y_j$, reescribir correctamente la expresión $a_{ijk} (x_i + y_j) z_k$ en notación de Einstein.

<details>
<summary>Solución</summary>

$$
a_{ijk} (x_i + y_j) z_k = a_{ijk} b_{ij} z_k
$$

donde $b_{ij} = x_i + y_j$. Esta forma deja claro que todos los índices ($i$, $j$, $k$) están contraídos y la expresión es un escalar.
</details>

> [!question] Ejercicio 4
> ¿Bajo qué condición la igualdad $a_{ijk} (x_i + y_j) z_k = a_{ijk} x_i z_k + a_{ijk} y_j z_k$ sería válida en notación de Einstein?

<details>
<summary>Solución</summary>

La igualdad sería válida si **implícitamente entendemos que en el lado derecho hay sumas sobre todos los índices**, es decir, si interpretamos $a_{ijk} x_i z_k$ como suma sobre $i,j,k$ (lo que requeriría que $j$ aparezca dos veces, pero no es el caso). Esto equivaldría a **romper el convenio de Einstein** y tratar todos los índices como mudos, lo cual no es estándar.

La forma correcta es usar sumatorias explícitas o definir $b_{ij}=x_i+y_j$ para mantener la claridad de los índices.
</details>

> [!question] Ejercicio 5
> Definir un tensor $c_{ijkl}$ tal que la expresión $a_{ijk} (x_i + y_j) z_k$ pueda escribirse como una contracción completa con $c_{ijkl}$.

<details>
<summary>Solución</summary>

Podemos definir:
$$
c_{ijkl} = a_{ijk} \delta_{il} \quad \text{(con suma sobre $i$)}
$$

Pero una forma más directa es usar $b_{ij}$ como antes. La contracción completa sería:
$$
a_{ijk} b_{ij} z_k = T
$$
donde $T$ es un escalar.
</details>

---

## Notas Relacionadas

- [[Notación de Índices en Sumatorias]]
- [[Convenio de sumación de Einstein]]
- [[Índices libres y mudos]]
- [[Derivada de una Forma Cuadrática en Notación de Índices]]
- [[Derivada de un Monomio Cuártico con Índices Repetidos]]