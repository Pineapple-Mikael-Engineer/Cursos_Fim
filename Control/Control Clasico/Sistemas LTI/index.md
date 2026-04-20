---
title: "Sistemas LTI"
tags:
  - control-clasico
  - sistemas-lineales
  - fundamentos
draft: false
aliases:
  - LTI
  - Linear Time-Invariant Systems
  - Sistemas Lineales e Invariantes en el Tiempo
---

# Sistemas LTI

> [!definicion] Definición
> Un sistema **LTI** (Lineal e Invariante en el Tiempo) es aquel que satisface simultáneamente dos propiedades fundamentales:
> 1. [[Linealidad]]: Principio de superposición (homogeneidad + aditividad)
> 2. [[Invarianza Temporal]]: Un desplazamiento en la entrada produce el mismo desplazamiento en la salida

---

## Importancia de la Clase LTI

> [!teoria] ¿Por qué estudiar sistemas LTI?
> La combinación de linealidad e invarianza temporal permite:
> - Caracterizar completamente el sistema mediante la [[Respuesta al Impulso]] $h(t)$
> - Calcular la salida mediante [[Convolución]]: $y(t) = (u * h)(t)$
> - Trabajar en el dominio de Laplace con la [[Control/Control Clasico/Función de Transferencia/index|index]] $G(s)$
> - Multiplicar en frecuencia: $Y(s) = G(s) U(s)$

---

## Propiedades Fundamentales de los Sistemas LTI

### 1. Caracterización por Respuesta al Impulso

> [!teorema]
> Para un sistema LTI, la respuesta al impulso $h(t)$ contiene toda la información dinámica del sistema. Conocida $h(t)$, la salida ante cualquier entrada $u(t)$ es:
> $$
> y(t) = \int_{-\infty}^{\infty} u(\tau) h(t - \tau) d\tau
> $$

### 2. Representación en el Dominio de Laplace

> [!teorema]
> Aplicando la [[Transformada de Laplace]] con condiciones iniciales nulas:
> $$
> Y(s) = G(s) U(s), \quad \text{donde} \quad G(s) = \frac{Y(s)}{U(s)}
> $$
> $G(s)$ es la [[Control/Control Clasico/Función de Transferencia/index|index]] del sistema.

### 3. Convolución como Operador Fundamental

> [!proposicion]
> La convolución es el operador que describe la relación entrada-salida en un sistema LTI:
> $$
> y = u * h
> $$
> Esta operación es conmutativa, asociativa y distributiva.

---

## Clasificación de Sistemas LTI

| Propiedad | Condición | Consecuencia |
|-----------|-----------|--------------|
| **Causalidad** | $h(t) = 0$ para $t < 0$ | La salida no depende de entradas futuras |
| **Estabilidad BIBO** | $\int_{-\infty}^{\infty} \|h(t)\| dt < \infty$ | Entrada acotada $\Rightarrow$ salida acotada |
| **Memoria** | $h(t) \neq k \cdot \delta(t)$ | La salida depende de entradas pasadas |

---

## Relaciones Clave

> [!teorema] Resumen de Equivalencias
> Para un sistema LTI con condiciones iniciales nulas, los siguientes objetos son equivalentes (se determinan mutuamente):
> 
> | Representación | Dominio | Operación |
> |----------------|---------|-----------|
> | Respuesta al impulso $h(t)$ | Temporal | $y = u * h$ |
> | Función de transferencia $G(s)$ | Laplace | $Y = G \cdot U$ |
> | Ecuación diferencial | Temporal | Coeficientes constantes |
> | Polos y ceros | $s$ | $G(s) = N(s)/D(s)$ |

---

## Limitaciones de los Sistemas LTI

> [!warning]
> La mayoría de los sistemas físicos reales son **no lineales** y/o **variantes en el tiempo**. El modelo LTI es una **aproximación** válida en ciertas condiciones:
> - Pequeñas señales alrededor de un punto de operación (linealización)
> - Sistemas con parámetros que varían lentamente (cuasi-invariantes)
> - Sistemas diseñados para operar en régimen lineal

Para sistemas no lineales, se requieren técnicas avanzadas como control no lineal, control adaptativo o control robusto.

---

## Notas Hijas

- [[Linealidad]]
- [[Invarianza Temporal]]
- [[Respuesta al Impulso]]
- [[Convolución]]