---
title: Metodos Iterativos
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - sistemas-lineales
  - metodos-iterativos
  - index
draft: false
aliases:
  - Métodos iterativos
  - Iterative methods
  - Resolución iterativa de sistemas
---

# Métodos Iterativos para Sistemas de Ecuaciones Lineales

> [!definicion]
> Un **método iterativo** para resolver $Ax = b$ genera una sucesión de vectores $\{y^{(k)}\}_{k=0}^{\infty}$ mediante una regla de recurrencia de la forma:
> $$y^{(k+1)} = T y^{(k)} + c$$
> donde $T$ es la **matriz de iteración** y $c$ un vector constante. Si la sucesión converge, su límite es la solución exacta $x = A^{-1}b$.

A diferencia de los [[Eliminacion Gaussiana|métodos directos]], que transforman $A$ en una matriz triangular y resuelven en un número fijo de operaciones, los métodos iterativos **no modifican** la matriz $A$ y generan aproximaciones sucesivas que se acercan cada vez más a la solución. Solo requieren productos matriz-vector y operaciones vectoriales.

---

## Un ejemplo con Gauss-Seidel

Para ver un método iterativo en acción, apliquemos Gauss-Seidel a un sistema pequeño.

> [!ejemplo]
> **Resolver $Ax = b$ con Gauss-Seidel.**
> 
> $$A = \begin{pmatrix} 4 & -1 & 0 \\ -1 & 4 & -1 \\ 0 & -1 & 4 \end{pmatrix}, \quad b = \begin{pmatrix} 6 \\ 2 \\ 14 \end{pmatrix}$$
> 
> La solución exacta es $x = (2, 2, 4)^T$. Partimos de $y^{(0)} = (0, 0, 0)^T$.
> 
> **Iteración 1:**
> - $y_1^{(1)} = (6 - (-1)\cdot 0 - 0\cdot 0) / 4 = 6/4 = 1.5$
> - $y_2^{(1)} = (2 - (-1)\cdot 1.5 - (-1)\cdot 0) / 4 = (2 + 1.5) / 4 = 3.5 / 4 = 0.875$
> - $y_3^{(1)} = (14 - 0\cdot 1.5 - (-1)\cdot 0.875) / 4 = 14.875 / 4 = 3.71875$
> 
> **Iteración 2:**
> - $y_1^{(2)} = (6 - (-1)\cdot 0.875 - 0\cdot 3.71875) / 4 = 6.875 / 4 = 1.71875$
> - $y_2^{(2)} = (2 - (-1)\cdot 1.71875 - (-1)\cdot 3.71875) / 4 = (2 + 1.71875 + 3.71875) / 4 = 7.4375 / 4 = 1.859375$
> - $y_3^{(2)} = (14 - 0\cdot 1.71875 - (-1)\cdot 1.859375) / 4 = 15.859375 / 4 = 3.96484375$
> 
> **Iteración 3:**
> - $y_1^{(3)} = (6 - (-1)\cdot 1.859375 - 0\cdot 3.96484375) / 4 = 7.859375 / 4 = 1.96484375$
> - $y_2^{(3)} = (2 - (-1)\cdot 1.96484375 - (-1)\cdot 3.96484375) / 4 = (2 + 1.96484375 + 3.96484375) / 4 = 7.9296875 / 4 = 1.982421875$
> - $y_3^{(3)} = (14 - 0\cdot 1.96484375 - (-1)\cdot 1.982421875) / 4 = 15.982421875 / 4 = 3.99560546875$
> 
> **Iteración 4:**
> - $y_1^{(4)} = (6 - (-1)\cdot 1.982421875 - 0\cdot 3.99560546875) / 4 = 7.982421875 / 4 = 1.99560546875$
> - $y_2^{(4)} = (2 - (-1)\cdot 1.99560546875 - (-1)\cdot 3.99560546875) / 4 = (2 + 1.99560546875 + 3.99560546875) / 4 = 7.9912109375 / 4 = 1.997802734375$
> - $y_3^{(4)} = (14 - 0\cdot 1.99560546875 - (-1)\cdot 1.997802734375) / 4 = 15.997802734375 / 4 = 3.99945068359375$
> 
> **Iteración 5:**
> - $y_1^{(5)} = (6 - (-1)\cdot 1.997802734375 - 0\cdot 3.99945068359375) / 4 = 7.997802734375 / 4 = 1.99945068359375$
> - $y_2^{(5)} = (2 - (-1)\cdot 1.99945068359375 - (-1)\cdot 3.99945068359375) / 4 = (2 + 1.99945068359375 + 3.99945068359375) / 4 = 7.9989013671875 / 4 = 1.999725341796875$
> - $y_3^{(5)} = (14 - 0\cdot 1.99945068359375 - (-1)\cdot 1.999725341796875) / 4 = 15.999725341796875 / 4 = 3.99993133544921875$
> 
> Observamos que la sucesión se acerca gradualmente a $(2, 2, 4)^T$. Después de $20$ iteraciones se alcanzan $4$ decimales correctos.

---

## Idea fundamental: Iteración de punto fijo

La clave está en descomponer $A$ en dos matrices, una de ellas fácil de invertir.

Se elige una matriz $M$ no singular y se escribe $A = M - N$. El sistema $Ax = b$ se reescribe como:
$$Mx = Nx + b$$

Esto sugiere la iteración:
$$M y^{(k+1)} = N y^{(k)} + b \quad \implies \quad y^{(k+1)} = M^{-1}N y^{(k)} + M^{-1}b$$

Definiendo $T = M^{-1}N$ y $c = M^{-1}b$, se obtiene la forma estándar $y^{(k+1)} = T y^{(k)} + c$.

La solución exacta $x$ satisface $x = Tx + c$ (es un punto fijo de la iteración). Restando:
$$\varepsilon^{(k+1)} = T \varepsilon^{(k)}$$
donde $\varepsilon^{(k)} = y^{(k)} - x$ es el error.

El desarrollo riguroso de este marco, incluyendo la clasificación de las descomposiciones y el análisis de la matriz de iteración, se estudia en [[Fundamentos Iteracion Punto Fijo Lineal]].

---

## Los dos métodos clásicos

A partir de la partición natural de $A = D - E - F$, cada método elige una $M$ distinta.

### Método de Jacobi

Toma $M = D$ (la diagonal). Invierte $D$ trivialmente. Actualiza todas las componentes a la vez usando solo valores de la iteración anterior.

> [!info]
> La derivación completa se desarrolla en [[Jacobi]]. El análisis de la matriz de iteración $T_J = D^{-1}(E + F)$ y su radio espectral se estudia en [[Jacobi]].

### Método de Gauss-Seidel

Toma $M = D - E$ (parte triangular inferior). Usa los valores recién calculados en cuanto están disponibles, lo que acelera la convergencia.

> [!info]
> La derivación completa se desarrolla en [[Gauss Seidel]]. La comparación de su velocidad de convergencia con Jacobi, incluyendo el teorema de Stein-Rosenberg, se estudia en [[Gauss Seidel]].


---

## Convergencia

No todos los sistemas convergen con estos métodos. Se requieren condiciones sobre $A$ o sobre $T$.

> [!info]
> El análisis riguroso de convergencia se distribuye en tres notas:
> - [[Convergencia Iterativos/Teorema Diagonal Dominante Estricta|Teorema Diagonal Dominante Estricta]]: Condición suficiente basada en la estructura de $A$.
> - [[Convergencia Iterativos/Criterio Radio Espectral Convergencia|Criterio Radio Espectral Convergencia]]: Condición necesaria y suficiente $\rho(T) < 1$.
> - [[Convergencia Iterativos/Estimacion Error y Cotas A Priori|Estimacion Error y Cotas A Priori]]: Cuántas iteraciones se necesitan para una tolerancia dada.

---

## Criterios de parada

En la práctica se detiene la iteración cuando el residuo o la diferencia entre iteraciones es suficientemente pequeña.

> [!definicion]
> $$\frac{\|b - A y^{(k)}\|}{\|b\|} \leq \text{tol} \quad \text{o} \quad \frac{\|y^{(k+1)} - y^{(k)}\|}{\|y^{(k+1)}\|} \leq \text{tol}$$

> [!warning]
> Un residuo pequeño **no implica** error pequeño si la matriz está mal condicionada. La relación entre ambos y el [[Condicionamiento Numerico Numero Condicion|número de condición]] se detalla en [[Convergencia Iterativos/Estimacion Error y Cotas A Priori]].

---

## Motivación: ¿Por qué métodos iterativos?

Aunque secundaria para el uso diario de la nota, es importante entender qué problema resuelven estos métodos.

Los métodos directos como la [[Factorizacion LU]] tienen costo $O(n^3)$ y producen **relleno** en matrices dispersas. Una matriz de $10^5 \times 10^5$ con solo $10^6$ elementos no nulos puede llenarse por completo durante la eliminación, requiriendo $80$ GB de memoria.

Los métodos iterativos evitan esto porque:
- **Nunca modifican $A$**: solo calculan productos matriz-vector.
- **Costo por iteración**: $O(\text{nnz})$ para matrices dispersas.
- **Sin relleno**: la memoria es solo la de $A$ más unos pocos vectores auxiliares.

**Análisis de velocidad: ¿Por qué $O(\text{nnz})$ por iteración?**

Para una matriz dispersa almacenada en formato CSR (Compressed Sparse Row), el producto matriz-vector $A y^{(k)}$ requiere recorrer cada elemento no nulo exactamente una vez. Si $\text{nnz}$ es el número de elementos no nulos, entonces:
- El producto matriz-vector cuesta $\Theta(\text{nnz})$ operaciones.
- En Jacobi, cada iteración requiere calcular $D^{-1}((L+U)y^{(k)} + b) = y^{(k)} + D^{-1}(b - A y^{(k)})$, que es esencialmente un producto matriz-vector más $O(n)$ operaciones.
- En Gauss-Seidel, aunque la implementación ingenua parece $O(n^2)$, una implementación eficiente para matrices dispersas también cuesta $O(\text{nnz})$ por iteración.

**Comparación numérica concreta.**

Para una matriz tridiagonal de $n = 10^6$ (como la que surge de discretizar una EDO en 1D):
- $\text{nnz} \approx 3 \times 10^6$
- Costo por iteración $\approx 3 \times 10^6$ operaciones.
- Si se requieren $k = 500$ iteraciones para converger: $1.5 \times 10^9$ operaciones totales.
- Un método directo para matriz tridiagonal (algoritmo de Thomas) cuesta $\approx 8n = 8 \times 10^6$ operaciones, que es mucho menor. **Para matrices tridiagonales, los métodos directos ganan.**

Para una matriz dispersa 2D de $n = 10^6$ (malla $1000 \times 1000$ con diferencias finitas):
- $\text{nnz} \approx 5 \times 10^6$ (5 puntos por nodo)
- El costo de un método directo (factorización LU dispersa) puede ser del orden de $O(n^{3/2}) \approx 10^9$ a $O(n^2) \approx 10^{12}$ operaciones dependiendo del ancho de banda y el relleno.
- Jacobi con $k = 1000$ iteraciones: $\approx 5 \times 10^9$ operaciones, similar o menor que el método directo, pero con mucha menos memoria.
- Para mallas 3D ($n = 10^6$, malla $100 \times 100 \times 100$ con 7 puntos por nodo, $\text{nnz} \approx 7 \times 10^6$), los métodos directos sufren relleno catastrófico (el ancho de banda crece como $n^{2/3}$, la factorización puede ser $O(n^{7/3}) \approx 10^{14}$). Los métodos iterativos siguen siendo $O(k \cdot \text{nnz})$.

**Conclusión práctica:**
- Matrices pequeñas ($n < 10^4$ densas, o $n < 10^5$ con perfil de banda estrecho): métodos directos.
- Matrices grandes y dispersas ($n > 10^5$ con estructura 2D/3D): métodos iterativos.
- La ventaja de los métodos iterativos crece con la dimensión del problema.

Para sistemas dispersos de gran escala (especialmente en 2D y 3D), los métodos iterativos son la única opción viable por razones de memoria y tiempo computacional.

---

## Resumen comparativo

| Método | $M$ | $T$ | Paralelismo |
|:---|:---|:---|:---|
| **Jacobi** | $D$ | $D^{-1}(E+F)$ | Fácil |
| **Gauss-Seidel** | $D - E$ | $(D-E)^{-1}F$ | Difícil |

> [!conclusion]
> Los métodos iterativos clásicos son simples en concepto pero su análisis de convergencia es profundo. El punto de partida es entender la iteración de punto fijo en [[Fundamentos Iteracion Punto Fijo Lineal]]. A partir de ahí, cada método se estudia en sus notas correspondientes: [[Jacobi]] y [[Gauss Seidel]]. Las condiciones de convergencia se formalizan en [[Convergencia Iterativos/Teorema Diagonal Dominante Estricta|Teorema Diagonal Dominante Estricta]], [[Convergencia Iterativos/Criterio Radio Espectral Convergencia|Criterio Radio Espectral Convergencia]] y [[Convergencia Iterativos/Estimacion Error y Cotas A Priori|Estimacion Error y Cotas A Priori]].