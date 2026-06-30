---
title: Teorema Stein-Rosenberg
order: 3
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - sistemas-lineales
  - metodos-iterativos
  - convergencia
  - stein-rosenberg
draft: false
aliases:
  - Stein-Rosenberg
  - Comparación Jacobi-Gauss-Seidel
  - Teorema de comparación de convergencia
---

# Teorema de Stein-Rosenberg

> [!definicion]
> Una matriz $A \in \mathbb{R}^{n \times n}$ es una **matriz de tipo M** (o matriz de Minkowski) si:
> 1. $a_{ii} > 0$ para todo $i = 1, \dots, n$
> 2. $a_{ij} \leq 0$ para todo $i \neq j$
> 3. $A$ es no singular y $A^{-1} \geq 0$ (todas sus entradas son no negativas)

> [!info]
> La condición $A^{-1} \geq 0$ es equivalente a que $A$ sea monótona. Una condición suficiente (pero no necesaria) para que $A$ sea de tipo M es que $A$ sea estrictamente diagonal dominante con $a_{ii} > 0$ y $a_{ij} \leq 0$ para $i \neq j$.

---

## Ejemplo

> [!ejemplo]
> **Matriz de tipo M.**
>
> $$A = \begin{pmatrix} 4 & -1 & 0 \\ -1 & 4 & -1 \\ 0 & -1 & 4 \end{pmatrix}$$
>
> - $a_{ii} = 4 > 0$ para todo $i$
> - $a_{ij} \leq 0$ para $i \neq j$ (los elementos fuera de la diagonal son $-1$ o $0$)
> - $A$ es diagonal dominante estricta, por lo tanto no singular y $A^{-1} > 0$
>
> **Matriz NO es de tipo M.**
>
> $$B = \begin{pmatrix} 4 & 1 & 0 \\ -1 & 4 & -1 \\ 0 & -1 & 4 \end{pmatrix}$$
>
> El elemento $b_{12} = 1 > 0$ viola la condición $a_{ij} \leq 0$ para $i \neq j$.

---

## Teorema de Stein-Rosenberg

> [!teorema]
> Sea $A$ una matriz de tipo M. Sean $T_J$ y $T_{GS}$ las matrices de iteración de los métodos de [[Jacobi]] y [[Gauss Seidel]] respectivamente. Entonces se cumple una de las siguientes tres alternativas:
>
> 1. **Caso convergente:** $0 \leq \rho(T_{GS}) \leq \rho(T_J) < 1$
> 2. **Caso borde:** $\rho(T_{GS}) = \rho(T_J) = 1$
> 3. **Caso divergente:** $\rho(T_{GS}) \geq \rho(T_J) > 1$
>
> En particular:
> - Si $\rho(T_J) < 1$, entonces $\rho(T_{GS}) \leq \rho(T_J) < 1$ (Gauss-Seidel converge más rápido o igual que Jacobi).
> - Si $\rho(T_J) > 1$, entonces $\rho(T_{GS}) \geq \rho(T_J) > 1$ (si Jacobi diverge, Gauss-Seidel también diverge, y al menos igual de rápido).
> - Si $\rho(T_J) = 1$, entonces $\rho(T_{GS}) = 1$.

> [!corolario]
> Para matrices de tipo M, el método de [[Gauss Seidel]] converge **si y solo si** el método de [[Jacobi]] converge. Y cuando convergen, Gauss-Seidel lo hace al menos tan rápido como Jacobi:
> $$\rho(T_{GS}) \leq \rho(T_J) < 1$$

---

## Demostración

> [!lema]
> Para matrices de tipo M, las matrices de iteración $T_J$ y $T_{GS}$ son **no negativas** (todas sus entradas son $\geq 0$).

> [!demostracion]
> - $T_J = I - D^{-1}A$. Como $A$ tiene $a_{ii} > 0$ y $a_{ij} \leq 0$ para $i \neq j$, se tiene:
>   $$(T_J)_{ij} = \begin{cases} 0 & \text{si } i = j \\ -\frac{a_{ij}}{a_{ii}} \geq 0 & \text{si } i \neq j \end{cases}$$
>   Por lo tanto $T_J \geq 0$ (entradas no negativas).
>
> - $T_{GS} = (D - E)^{-1}F$. Para matrices de tipo M, se puede demostrar que $(D - E)^{-1} \geq 0$ y $F \geq 0$, por lo tanto $T_{GS} \geq 0$.

> [!demostracion]
> (Esquema de la demostración del teorema de Stein-Rosenberg)
>
> **Paso 1: Relación entre $T_J$ y $T_{GS}$.**
>
> Se puede demostrar que $T_{GS} = (I - L)^{-1}U$ donde $L = D^{-1}E$ y $U = D^{-1}F$, con $L \geq 0$, $U \geq 0$, y $L$ es estrictamente triangular inferior (nilpotente). Además $T_J = L + U$.
>
> **Paso 2: Ecuación de punto fijo.**
>
> Sea $\mu > 0$ un parámetro. Considérese la ecuación:
> $$\det(\mu I - (L + U)) = 0$$
>
> y la ecuación:
> $$\det(\mu I - (I - L)^{-1}U) = 0$$
>
> **Paso 3: Relación espectral.**
>
> Se puede demostrar que $\lambda \neq 0$ es autovalor de $T_{GS}$ si y solo si existe $\mu$ tal que $\mu$ es autovalor de $T_J$ y $\lambda$ satisface:
> $$\lambda = \frac{\mu}{1 + \mu \cdot (\dots)}$$
>
> **Paso 4: Comparación de radios espectrales.**
>
> Analizando la relación funcional entre $\rho(T_J)$ y $\rho(T_{GS})$, se obtiene que $\rho(T_{GS}) \leq \rho(T_J)$ cuando $\rho(T_J) < 1$, y la igualdad solo ocurre en casos degenerados.
>
> *La demostración completa es técnica y se omite aquí; puede encontrarse en textos de análisis numérico como Varga (1962) o Saad (2003).*

---

## Ejemplo numérico

> [!ejemplo]
> **Comparación Jacobi vs Gauss-Seidel para una matriz de tipo M.**
>
> $$A = \begin{pmatrix} 4 & -1 & 0 \\ -1 & 4 & -1 \\ 0 & -1 & 4 \end{pmatrix}$$
>
> **Matrices de iteración:**
>
> $$T_J = \begin{pmatrix} 0 & 1/4 & 0 \\ 1/4 & 0 & 1/4 \\ 0 & 1/4 & 0 \end{pmatrix}, \quad \rho(T_J) = \frac{1}{\sqrt{8}} \approx 0.3536$$
>
> $$T_{GS} = \begin{pmatrix} 0 & 1/4 & 0 \\ 0 & 1/16 & 1/4 \\ 0 & 1/64 & 1/16 \end{pmatrix}, \quad \rho(T_{GS}) = \frac{1}{8} = 0.125$$
>
> Efectivamente:
> $$\rho(T_{GS}) = 0.125 < 0.3536 = \rho(T_J) < 1$$
>
> Gauss-Seidel converge más rápido (aproximadamente el doble de dígitos por iteración).

---

## Implicaciones prácticas

> [!info]
> **¿Cuándo aplicar este teorema?**
>
> - El teorema es útil para matrices que surgen de discretizaciones de EDPs elípticas (como la ecuación de Poisson), donde los coeficientes fuera de la diagonal son negativos o cero.
> - Garantiza que si implementamos Gauss-Seidel en lugar de Jacobi, la convergencia será al menos tan rápida (y típicamente más rápida) sin necesidad de verificar condiciones adicionales.
> - Justifica teóricamente la preferencia por Gauss-Seidel sobre Jacobi para esta clase de problemas.

> [!warning]
> **Limitaciones.**
>
> - El teorema solo aplica a matrices de tipo M ($a_{ii} > 0$, $a_{ij} \leq 0$ para $i \neq j$, y $A^{-1} \geq 0$).
> - Para matrices que no cumplen estas condiciones, Gauss-Seidel puede converger más lento que Jacobi, o incluso divergir cuando Jacobi converge.
> - Existen matrices para las cuales Jacobi converge y Gauss-Seidel diverge (no son de tipo M).

---

## Relación con otros teoremas

> [!info]
> - [[Convergencia Iterativos/Teorema Diagonal Dominante Estricta|Teorema de la Diagonal Dominante Estricta]]: Si $A$ es diagonal dominante estricta con $a_{ii} > 0$ y $a_{ij} \leq 0$ para $i \neq j$, entonces $A$ es de tipo M y se aplica Stein-Rosenberg.
> - [[Criterio Radio Espectral Convergencia|Criterio del Radio Espectral]]: Proporciona la condición necesaria y suficiente para convergencia ($\rho(T) < 1$). Stein-Rosenberg compara los radios espectrales de Jacobi y Gauss-Seidel.
> - [[Gauss Seidel]]: Contiene la definición del método y su análisis básico.

---

## Resumen

> [!corolario]
> El teorema de Stein-Rosenberg establece una relación fundamental entre los métodos de Jacobi y Gauss-Seidel para matrices de tipo M:
>
> | $\rho(T_J)$ | $\rho(T_{GS})$ | Consecuencia |
> |:---|:---|:---|
> | $< 1$ | $\leq \rho(T_J) < 1$ | Ambos convergen, GS más rápido o igual |
> | $= 1$ | $= 1$ | Ambos divergen (no convergen a cero) |
> | $> 1$ | $\geq \rho(T_J) > 1$ | Ambos divergen, GS al menos igual de rápido |
>
> **Conclusión práctica:** Para la clase importante de matrices de tipo M (que incluye muchas discretizaciones de EDPs), Gauss-Seidel es **siempre preferible** a Jacobi: converge bajo las mismas condiciones y lo hace más rápido.
>
> Este teorema completa el análisis comparativo iniciado en [[Jacobi]] y [[Gauss Seidel]], y se apoya en el [[Criterio Radio Espectral Convergencia]] para la condición de convergencia.