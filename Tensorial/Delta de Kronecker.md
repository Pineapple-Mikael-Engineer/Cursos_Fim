---
title: Delta de Kronecker
tags:
  - matemáticas
  - álgebra-lineal
  - notación-índices
  - cálculo-tensorial
draft: false
---

# Delta de Kronecker

> [!definicion] Definición
> La **Delta de Kronecker** se define como:
> $$
> \delta_{ij} = \begin{cases} 
> 1 & \text{si } i = j \\ 
> 0 & \text{si } i \neq j 
> \end{cases}
> $$

## Interpretaciones Equivalentes

> [!abstract] Matriz Identidad
> En álgebra lineal, $\delta_{ij}$ representa las componentes de la [[Matriz Identidad]] $I$:
> $$
> I = \begin{pmatrix}
> 1 & 0 & \cdots & 0 \\
> 0 & 1 & \cdots & 0 \\
> \vdots & \vdots & \ddots & \vdots \\
> 0 & 0 & \cdots & 1
> \end{pmatrix}, \quad I_{ij} = \delta_{ij}
> $$

## Propiedades Fundamentales

### 1. Propiedad de Sustitución (Sifting Property)
Esta es la propiedad más importante:
$$
\delta_{ij} a_j = a_i \quad \text{(sumando sobre j)}
$$

> [!example] Ejemplo
> $$
> \delta_{1j} a_j = \delta_{11}a_1 + \delta_{12}a_2 + \dots + \delta_{1n}a_n = 1 \cdot a_1 + 0 \cdot a_2 + \dots = a_1
> $$

### 2. Traza
$$
\delta_{ii} = n \quad \text{(donde $n$ es la dimensión)}
$$

### 3. Simetría
$$
\delta_{ij} = \delta_{ji}
$$

### 4. Producto de Deltas
$$
\delta_{ij} \delta_{jk} = \delta_{ik}
$$

## Manipulación Algebraica

> [!teorema] Reglas de Contracción
> Al trabajar con sumatorias y la delta de Kronecker:
> - $\delta_{ij} \delta_{ij} = n$
> - $\delta_{ij} \delta_{jk} \delta_{ki} = n$
> - $a_i \delta_{ij} = a_j$

## Relación con Otros Conceptos

### Con el [[Símbolo de Levi-Civita]]
$$
\varepsilon_{ijk} \varepsilon_{ilm} = \delta_{jl}\delta_{km} - \delta_{jm}\delta_{kl}
$$

### Con el [[Tensor Métrico]]
En espacios euclidianos con coordenadas cartesianas, $g_{ij} = \delta_{ij}$.

## Problemas Resueltos

> [!example] Problema 1: Simplificar $a_i b_j \delta_{ij}$
> 
> **Solución:** 
> $$
> a_i b_j \delta_{ij} = a_i b_i = \sum_{i} a_i b_i = \vec{a} \cdot \vec{b}
> $$
> La delta "contrae" los índices $i$ y $j$, resultando en el [[Producto Escalar]].

> [!example] Problema 2: Calcular $\delta_{ij} \delta_{jk} \delta_{ki}$
> 
> **Solución:** 
> $$
> \delta_{ij} \delta_{jk} \delta_{ki} = \delta_{ik} \delta_{ki} = \delta_{ii} = n
> $$

## Notas Relacionadas

- [[Notación de Índices en Sumatorias]]
- [[Símbolo de Levi-Civita]]
- [[Producto Escalar]]
- [[Matriz Identidad]]
- [[Convenio de Sumación de Einstein]]