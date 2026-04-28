---
title: Variantes Metodo Potencia
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - autovalores
  - metodo-potencia
  - potencia-inversa
  - potencia-desplazada
  - index
draft: false
aliases:
  - Variantes del método de la potencia
  - Power method variants
  - Inverse power method
  - Shifted power method
---

# Variantes del Método de la Potencia

> [!definicion]
> Las variantes del método de la potencia son extensiones del [[Metodo Potencia Directo/index|método de la potencia directo]] que permiten calcular autovalores distintos al dominante, aplicando el mismo principio a matrices transformadas.

> [!info]
> Mientras que el método de la potencia directo calcula el autovalor de mayor módulo $|\lambda_1|$, las variantes inversa y desplazada permiten acceder a cualquier autovalor del espectro, incluyendo el de menor módulo y autovalores interiores.

---

## Ejemplo

> [!ejemplo]
> **Cálculo del autovalor de menor módulo mediante potencia inversa.**
>
> Sea $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, con autovalores $\lambda_1 = 3$ y $\lambda_2 = 1$. El autovalor de menor módulo es $\lambda_2 = 1$.
>
> Aplicando el método de la potencia a $A^{-1}$:
> $$A^{-1} = \frac{1}{3} \begin{pmatrix} 2 & -1 \\ -1 & 2 \end{pmatrix} \approx \begin{pmatrix} 0.6667 & -0.3333 \\ -0.3333 & 0.6667 \end{pmatrix}$$
>
> Los autovalores de $A^{-1}$ son $1/\lambda_1 = 1/3 \approx 0.3333$ y $1/\lambda_2 = 1$. El dominante de $A^{-1}$ es $1$, correspondiente a $\lambda_2 = 1$.
>
> Partiendo de $y^{(0)} = (1, 0)^T$ y aplicando el método de la potencia a $A^{-1}$:
>
> | $k$ | $y^{(k)}$ (normalizado) | $\lambda^{(k)} = 1 / R_{A^{-1}}(y^{(k)})$ |
> |:---|:---|:---|
> | 0 | (1.000, 0.000) | — |
> | 1 | (0.894, -0.447) | 1.667 |
> | 2 | (0.780, -0.625) | 1.190 |
> | 3 | (0.732, -0.681) | 1.048 |
> | 4 | (0.716, -0.698) | 1.012 |
> | 5 | (0.708, -0.706) | 1.003 |
>
> El autovector converge a $(1/\sqrt{2}, -1/\sqrt{2})$, el autovector de $\lambda_2 = 1$. El autovalor estimado converge a $1$.
>
> **Observación:** La potencia inversa requiere resolver un sistema lineal $(A - \mu I)z = y$ en cada iteración, lo que es más costoso que el simple producto matriz-vector del método directo.

---

## Demostración general

> [!teorema]
> Sea $A \in \mathbb{R}^{n \times n}$ diagonalizable con autovalores $\lambda_1, \lambda_2, \dots, \lambda_n$ y autovectores $v_1, v_2, \dots, v_n$. Sea $\mu \in \mathbb{R}$ tal que $A - \mu I$ es no singular. Entonces:
>
> 1. Los autovalores de $(A - \mu I)^{-1}$ son $1/(\lambda_i - \mu)$.
> 2. Los autovectores de $(A - \mu I)^{-1}$ son los mismos que los de $A$.
> 3. Aplicando el método de la potencia a $(A - \mu I)^{-1}$ se obtiene convergencia al autovalor $\lambda_i$ más cercano a $\mu$.

> [!demostracion]
> **Paso 1: Relación espectral.**
>
> Si $A v_i = \lambda_i v_i$, entonces:
> $$(A - \mu I) v_i = (\lambda_i - \mu) v_i$$
>
> Inviertiendo (si $\lambda_i - \mu \neq 0$):
> $$(A - \mu I)^{-1} v_i = \frac{1}{\lambda_i - \mu} v_i$$
>
> Por lo tanto, los autovectores de $(A - \mu I)^{-1}$ son los mismos que los de $A$, y sus autovalores son $1/(\lambda_i - \mu)$.
>
> **Paso 2: Orden de convergencia.**
>
> Sea $\lambda_j$ el autovalor más cercano a $\mu$, es decir, $|\lambda_j - \mu|$ es mínimo. Entonces $1/|\lambda_j - \mu|$ es el autovalor de mayor módulo de $(A - \mu I)^{-1}$.
>
> Aplicando el método de la potencia a $(A - \mu I)^{-1}$, se obtiene convergencia a $v_j$ (autovector asociado) y el autovalor dominante de $(A - \mu I)^{-1}$ es $1/(\lambda_j - \mu)$. Por lo tanto:
> $$\lambda_j = \mu + \frac{1}{\text{autovalor dominante de } (A - \mu I)^{-1}}$$
>
> **Paso 3: Razón de convergencia.**
>
> La razón de convergencia está dada por:
> $$r = \left| \frac{\text{segundo autovalor en módulo de } (A - \mu I)^{-1}}{\text{primer autovalor en módulo de } (A - \mu I)^{-1}} \right| = \left| \frac{1/|\lambda_k - \mu|}{1/|\lambda_j - \mu|} \right| = \left| \frac{\lambda_j - \mu}{\lambda_k - \mu} \right|$$
>
> donde $\lambda_k$ es el autovalor más cercano a $\mu$ después de $\lambda_j$.
>
> **Caso particular (potencia inversa sin desplazamiento):**
>
> Si $\mu = 0$, entonces $(A - 0I)^{-1} = A^{-1}$. Los autovalores de $A^{-1}$ son $1/\lambda_i$, y el dominante es $1/\lambda_n$ si $\lambda_n$ es el de menor módulo. Por lo tanto, la potencia inversa converge al autovalor de menor módulo $\lambda_n$ con razón $r = |\lambda_n / \lambda_{n-1}|$.

> [!info]
> **Interpretación:** Cuanto mejor sea el desplazamiento $\mu$ (más cercano a $\lambda_j$), mayor será $1/|\lambda_j - \mu|$ y más rápida la convergencia. En el límite $\mu \to \lambda_j$, la convergencia es instantánea (una iteración), pero en la práctica $\lambda_j$ no se conoce de antemano.

---

## Variantes

### Potencia inversa

> [!info]
> Aplica el método de la potencia a $A^{-1}$ para calcular el autovalor de menor módulo $|\lambda_n|$.
>
> **Operación principal por iteración:** Resolver $A z = y^{(k)}$.
>
> Desarrollado en [[Potencia Inversa Valor Propio Menor Modulo]].

### Potencia desplazada

> [!info]
> Aplica el método de la potencia a $(A - \mu I)^{-1}$ para calcular el autovalor más cercano a $\mu$, con aceleración de convergencia mediante una buena elección de $\mu$.
>
> **Operación principal por iteración:** Resolver $(A - \mu I) z = y^{(k)}$.
>
> Desarrollado en [[Potencia Desplazada Aceleracion Convergencia]].

---

## Relación con el método de la potencia directo

> [!info]
> | Método | Matriz transformada | Objetivo | Razón de convergencia |
> |:---|:---|:---|:---|
> | Potencia directa | $A$ | $\lambda_1$ (mayor módulo) | $\|\lambda_2/\lambda_1\|$ |
> | Potencia inversa | $A^{-1}$ | $\lambda_n$ (menor módulo) | $\|\lambda_n/\lambda_{n-1}\|$ |
> | Potencia desplazada | $(A - \mu I)^{-1}$ | $\lambda$ más cercano a $\mu$ | $\left\| \frac{\lambda_j - \mu}{\lambda_k - \mu} \right\|$ |

---

## Resumen

> [!corolario]
> Las variantes del método de la potencia extienden su utilidad a cualquier autovalor del espectro:
>
> - **Potencia inversa:** Calcula el autovalor de menor módulo resolviendo $A z = y$ por iteración.
> - **Potencia desplazada:** Calcula el autovalor más cercano a $\mu$ resolviendo $(A - \mu I) z = y$.
>
> La razón de convergencia mejora al elegir $\mu$ cercano al autovalor deseado, lo que motiva técnicas de desplazamiento adaptativo (véase [[Potencia Desplazada Aceleracion Convergencia]]).
>
> Para los fundamentos del método de la potencia, véase [[Metodo Potencia Directo/index]]; para el cálculo del autovalor mediante cociente de Rayleigh, véase [[Calculo Constante Normalizacion Rayleigh]].