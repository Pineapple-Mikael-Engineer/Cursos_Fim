---
title: Fundamentos Iteracion Punto Fijo Lineal
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - sistemas-lineales
  - metodos-iterativos
  - punto-fijo
draft: false
aliases:
  - Iteración de punto fijo lineal
  - Fixed-point iteration
  - Framework unificado de métodos iterativos
---

# Fundamentos de Iteración de Punto Fijo Lineal

> [!definicion]
> Un **método iterativo de punto fijo lineal** para resolver $Ax = b$ es un esquema recurrente de la forma:
> $$y^{(k+1)} = T y^{(k)} + c, \quad k = 0, 1, 2, \dots$$
> donde:
> - $T \in \mathbb{R}^{n \times n}$ es la **matriz de iteración**,
> - $c \in \mathbb{R}^n$ es un vector constante,
> - $y^{(0)} \in \mathbb{R}^n$ es una aproximación inicial.
>
> Si la sucesión $\{y^{(k)}\}_{k=0}^{\infty}$ converge, su límite $x$ satisface la **ecuación de punto fijo**:
> $$x = T x + c$$

---

## Ejemplo numérico

> [!ejemplo]
> Resuélvase $Ax = b$ con:
> $$A = \begin{pmatrix} 4 & 1 \\ 1 & 3 \end{pmatrix}, \qquad b = \begin{pmatrix} 5 \\ 4 \end{pmatrix}$$
>
> La solución exacta es $x = (1, 1)^T$.
>
> **Construcción de la iteración.**
>
> Elíjase $M$ como la diagonal de $A$:
> $$M = \begin{pmatrix} 4 & 0 \\ 0 & 3 \end{pmatrix}$$
>
> Defínase $N = M - A$:
> $$N = \begin{pmatrix} 4 & 0 \\ 0 & 3 \end{pmatrix} - \begin{pmatrix} 4 & 1 \\ 1 & 3 \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix}$$
>
> La iteración $M y^{(k+1)} = N y^{(k)} + b$ es:
> $$\begin{pmatrix} 4 & 0 \\ 0 & 3 \end{pmatrix} y^{(k+1)} = \begin{pmatrix} 0 & -1 \\ -1 & 0 \end{pmatrix} y^{(k)} + \begin{pmatrix} 5 \\ 4 \end{pmatrix}$$
>
> Despejando componente a componente:
> $$y_1^{(k+1)} = \frac{5 - y_2^{(k)}}{4}$$
> $$y_2^{(k+1)} = \frac{4 - y_1^{(k)}}{3}$$
>
> En forma estándar $y^{(k+1)} = T y^{(k)} + c$:
> $$T = \begin{pmatrix} 0 & -1/4 \\ -1/3 & 0 \end{pmatrix}, \qquad c = \begin{pmatrix} 5/4 \\ 4/3 \end{pmatrix}$$
>
> **Iteración desde $y^{(0)} = (0, 0)^T$.**
>
> | $k$ | $y_1^{(k)}$ | $y_2^{(k)}$ | $\|y^{(k)} - x\|_\infty$ |
> |:---|:---:|:---:|:---:|
> | 0 | 0.000 | 0.000 | 1.000 |
> | 1 | 1.250 | 1.333 | 0.333 |
> | 2 | 0.917 | 0.917 | 0.083 |
> | 3 | 1.021 | 1.028 | 0.028 |
> | 4 | 0.993 | 0.993 | 0.007 |
> | 5 | 1.002 | 1.002 | 0.002 |
>
> **Verificación del criterio de convergencia.**
>
> Los autovalores de $T$ satisfacen:
> $$\det(T - \lambda I) = \lambda^2 - \frac{1}{12} = 0 \quad \Rightarrow \quad \lambda = \pm \frac{1}{\sqrt{12}} \approx \pm 0.288675$$
>
> Por lo tanto $\rho(T) = 1/\sqrt{12} \approx 0.288675 < 1$, lo que garantiza convergencia.
>
> *Observación:* La elección $M = D$ (diagonal) corresponde al método de [[Jacobi]]. Otras elecciones de $M$ producen otros métodos, como [[Gauss Seidel]].

---

## Demostración de la convergencia


> [!demostracion]
> **Paso 1: Definición de la ecuación de punto fijo.**
>
> Por construcción, la solución exacta $x = A^{-1}b$ satisface:
> $$x = T x + c$$
>
> **Paso 2: Definición del iterador.**
>
> El método iterativo se define como:
> $$y^{(k+1)} = T y^{(k)} + c$$
>
> **Paso 3: Definición del error.**
>
> Sea $z^{(k)} = y^{(k)} - x$. Restando la ecuación de punto fijo de la iteración:
> $$y^{(k+1)} - x = (T y^{(k)} + c) - (T x + c) = T(y^{(k)} - x)$$
>
> Por lo tanto:
> $$z^{(k+1)} = T z^{(k)}$$
>
> **Paso 4: Expresión del error en la iteración $k$.**
>
> Aplicando recurrentemente:
> $$z^{(1)} = T z^{(0)}$$
> $$z^{(2)} = T z^{(1)} = T^2 z^{(0)}$$
> $$\vdots$$
> $$z^{(k)} = T^k z^{(0)}$$
>
> **Paso 5: Condición de convergencia a cero.**
>
> La sucesión $y^{(k)}$ converge a $x$ si y solo si $z^{(k)} \to 0$, es decir:
> $$\lim_{k \to \infty} T^k z^{(0)} = 0 \quad \forall z^{(0)} \in \mathbb{R}^n$$
>
> Esto ocurre si y solo si $\lim_{k \to \infty} T^k = 0$, que a su vez es equivalente a $\rho(T) < 1$ ([[Criterio Radio Espectral Convergencia|teorema del radio espectral]]).

---

## Velocidad de convergencia

> [!teorema]
> Si $\rho(T) < 1$, entonces para cualquier $\varepsilon > 0$ existe $K$ tal que para todo $k \geq K$:
> $$\|z^{(k)}\| \leq (\rho(T) + \varepsilon)^k \|z^{(0)}\|$$

> [!definicion]
> La **tasa asintótica de convergencia** se mide por:
> - Factor de convergencia: $\rho(T)$
> - Tasa de convergencia lineal: $R = -\ln \rho(T)$
> - Dígitos ganados por iteración: $R_{10} = -\log_{10} \rho(T)$

> [!ejemplo]
> Para el ejemplo anterior, $\rho(T) = 1/\sqrt{12} \approx 0.288675$:
> $$R_{10} = -\log_{10}(0.288675) \approx 0.54$$
>
> Esto significa que se ganan aproximadamente $0.54$ dígitos decimales por iteración.

El análisis completo de la estimación del error se desarrolla en [[Estimacion Error y Cotas A Priori]].

---

## Error de redondeo en la implementación

En una implementación real en [[Representacion Punto Flotante IEEE 754|aritmética de punto flotante]], los cálculos se realizan con precisión finita.

> [!warning]
> Sea $\varepsilon_{\text{mach}}$ el [[Epsilon Maquina y Precision Relativa|epsilon de máquina]] ($\approx 2.2 \times 10^{-16}$ en doble precisión). En cada iteración, la operación $y^{(k+1)} = T y^{(k)} + c$ introduce un error de redondeo del orden de $\varepsilon_{\text{mach}} \|T\| \|y^{(k)}\|$.
>
> Cuando el error $z^{(k)}$ se vuelve del orden de $\varepsilon_{\text{mach}}$, la iteración entra en un régimen estacionario donde el error numérico domina sobre el error de convergencia. Reducir $\|z^{(k)}\|$ por debajo de $10^{-15}$ es generalmente imposible en doble precisión.
>
> Por esta razón, en la práctica se define una tolerancia $\text{tol} \gg \varepsilon_{\text{mach}}$ (típicamente $10^{-10}$ o $10^{-12}$) y se detiene la iteración cuando:
> $$\frac{\|y^{(k+1)} - y^{(k)}\|}{\|y^{(k+1)}\|} \leq \text{tol}$$

---

## Condiciones suficientes de convergencia

El cálculo del radio espectral puede ser costoso para matrices grandes. Existen condiciones más simples que garantizan $\rho(T) < 1$ para ciertos métodos.

> [!teorema] [Diagonal dominante estricta]
> Si $A$ es estrictamente diagonal dominante por filas:
> $$|a_{ii}| > \sum_{j \neq i} |a_{ij}| \quad \forall i$$
> entonces el método de [[Jacobi]] converge.

> [!teorema] [Matrices simétricas definidas positivas]
> Si $A$ es simétrica definida positiva, entonces el método de [[Gauss Seidel]] converge.

La demostración de estos teoremas se encuentra en [[Teorema Diagonal Dominante Estricta]].

---

## Resumen

| Paso | Descripción |
|:---|:---|
| 1. Elección de $M$ | Matriz no singular, fácil de invertir |
| 2. Definición de $N$ | $N = M - A$ |
| 3. Iteración | $M y^{(k+1)} = N y^{(k)} + b$ |
| 4. Forma estándar | $y^{(k+1)} = T y^{(k)} + c$ con $T = M^{-1}N$, $c = M^{-1}b$ |
| 5. Ecuación de punto fijo | $x = Tx + c$ |
| 6. Error | $z^{(k)} = y^{(k)} - x$, satisface $z^{(k+1)} = T z^{(k)}$, $z^{(k)} = T^k z^{(0)}$ |
| 7. Convergencia | $\rho(T) < 1$ (condición necesaria y suficiente) |

> [!corolario]
> El marco de iteración de punto fijo reduce el análisis de cualquier método iterativo a dos tareas:
> 1. Verificar que $\rho(T) < 1$ (convergencia garantizada).
> 2. Estimar $\rho(T)$ para predecir la velocidad de convergencia.
>
> Las notas [[Jacobi]] y [[Gauss Seidel]] aplican este marco a elecciones específicas de $M$. Las condiciones de convergencia se profundizan en [[Teorema Diagonal Dominante Estricta]] y [[Criterio Radio Espectral Convergencia]], mientras que [[Estimacion Error y Cotas A Priori]] desarrolla las técnicas para cuantificar la velocidad de convergencia y el [[Epsilon Maquina y Precision Relativa|error de redondeo]] en implementaciones reales.