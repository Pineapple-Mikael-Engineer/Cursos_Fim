---
title: Extrapolación de Richardson y Aceleración de Convergencia
order: 3
tags:
  - metodos-numericos
  - teoria
  - diferenciacion-integracion
  - diferenciacion-numerica
  - convergencia
draft: false
aliases:
  - Extrapolación de Richardson
  - Richardson extrapolation
  - Aceleración de convergencia
  - Romberg
---

# Extrapolación de Richardson y Aceleración de Convergencia

> [!definicion]
> La **extrapolación de Richardson** combina dos aproximaciones de orden $p$ calculadas con pasos $h$ y $h/2$ para **cancelar** el término de error dominante, produciendo una aproximación de orden $p+q$ (mayor). Se aplica a [[Orden Error Progresiva Regresiva Centrada|diferenciación]], integración ([[Simpson Compuesto Convergencia O h4|Romberg]]) y cualquier proceso con expansión de error conocida.

> [!info]
> La idea: si se conoce *cómo* depende el error de $h$ (su potencia), se puede eliminar algebraicamente. No requiere evaluar más allá de los dos pasos; explota la **estructura** del error, no más datos.

---

## Fórmula de extrapolación

> [!teorema]
> Sea $A(h)$ una aproximación de un valor exacto $A$ con expansión de error
> $$A(h) = A + c_p h^p + c_{p+q} h^{p+q} + \cdots.$$
> Entonces la combinación
> $$A^{\text{ext}}(h) = \frac{2^p A(h/2) - A(h)}{2^p - 1} = A + O(h^{p+q})$$
> elimina el término $c_p h^p$ y tiene orden $p+q$.

> [!demostracion]
> Escríbase $A(h) = A + c_p h^p + O(h^{p+q})$ y $A(h/2) = A + c_p (h/2)^p + O(h^{p+q}) = A + c_p 2^{-p}h^p + O(h^{p+q})$. Multiplicando la segunda por $2^p$ y restando la primera:
> $$2^p A(h/2) - A(h) = (2^p - 1)A + \big(c_p h^p - c_p h^p\big) + O(h^{p+q}) = (2^p-1)A + O(h^{p+q}).$$
> Dividiendo entre $2^p - 1$ se cancela $c_p h^p$ y queda orden $p+q$.

---

## Ejemplo: diferenciación centrada

> [!ejemplo]
> **Derivada centrada de $f(x)=e^x$ en $x=0$** ($p=2$, $q=2$ porque la expansión solo tiene potencias pares). Con $D(h) = \frac{f(h)-f(-h)}{2h}$:
>
> | $h$ | $D(h)$ | $D^{\text{ext}} = \frac{4D(h/2)-D(h)}{3}$ |
> |:---:|:---:|:---:|
> | 0.2 | 1.0066800 | — |
> | 0.1 | 1.0016675 | 1.0000... |
> | 0.05 | 1.0004168 | 1.00000003 |
>
> $D(h)$ tiene error $\sim1.7\times10^{-3}$ con $h=0.1$; la extrapolada $D^{\text{ext}}$ alcanza $\sim10^{-8}$ con los mismos datos: salta de orden $2$ a orden $4$.

---

## Extrapolación repetida e integración de Romberg

> [!teoria]
> La extrapolación se **itera**: tras obtener orden $p+q$, se combinan dos valores extrapolados para alcanzar $p+2q$, y así sucesivamente, formando una tabla triangular. Aplicada a la [[Trapecio Compuesto Convergencia O h2|regla del trapecio compuesta]] (que tiene expansión solo en potencias pares de $h$), genera el **método de Romberg**:
> $$R_{k,0} = \text{trapecio con } 2^k \text{ intervalos}, \qquad R_{k,j} = \frac{4^j R_{k,j-1} - R_{k-1,j-1}}{4^j - 1}.$$
> La primera columna es $O(h^2)$ (trapecio); la segunda $O(h^4)$ (coincide con [[Simpson Compuesto Convergencia O h4|Simpson]]); la tercera $O(h^6)$, etc. Convergencia muy rápida para integrandos suaves.

---

## Algoritmo

> [!algoritmo]
> **Tabla de Romberg en Python.**
>
> ```python
> import numpy as np
>
> def romberg(f, a, b, niveles=6):
>     R = np.zeros((niveles, niveles))
>     h = b - a
>     R[0, 0] = 0.5 * h * (f(a) + f(b))            # trapecio, 1 intervalo
>     for k in range(1, niveles):
>         h *= 0.5
>         # trapecio compuesto reusando evaluaciones previas
>         suma = sum(f(a + (2*i - 1)*h) for i in range(1, 2**(k-1) + 1))
>         R[k, 0] = 0.5 * R[k-1, 0] + h * suma
>         for j in range(1, k + 1):
>             R[k, j] = (4**j * R[k, j-1] - R[k-1, j-1]) / (4**j - 1)
>     return R[niveles-1, niveles-1]
> ```

---

## Relación con otras notas

> [!info]
> - Los esquemas base que se aceleran: [[Orden Error Progresiva Regresiva Centrada]].
> - El límite que impone el redondeo a la extrapolación: [[Inestabilidad Error Redondeo Paso h]].
> - La regla del trapecio que Romberg refina: [[Trapecio Compuesto Convergencia O h2]] y [[Simpson Compuesto Convergencia O h4]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Idea | cancelar el término de error dominante |
| Fórmula | $\frac{2^p A(h/2) - A(h)}{2^p - 1}$ |
| Resultado | orden $p \to p+q$ |
| Iterada | tabla de Romberg ($O(h^2)\to O(h^4)\to\cdots$) |
| Requisito | conocer la potencia del error |

> [!corolario]
> La extrapolación de Richardson cancela algebraicamente el término de error dominante combinando $A(h)$ y $A(h/2)$ con pesos $\frac{2^p A(h/2)-A(h)}{2^p-1}$, elevando el orden de $p$ a $p+q$ sin más evaluaciones que las de los dos pasos. Iterada sobre la [[Trapecio Compuesto Convergencia O h2|regla del trapecio]] produce el método de Romberg, cuya tabla asciende $O(h^2)\to O(h^4)\to O(h^6)$ y converge velozmente para integrandos suaves. Su único requisito es conocer la potencia del error; su límite, la [[Inestabilidad Error Redondeo Paso h|barrera del redondeo]].
