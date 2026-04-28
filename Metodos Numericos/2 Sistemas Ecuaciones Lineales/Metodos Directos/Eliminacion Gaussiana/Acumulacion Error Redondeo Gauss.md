---
title: Acumulacion Error Redondeo Gauss
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - sistemas-lineales
  - metodos-directos
  - error-numerico
draft: false
aliases:
  - Error de redondeo en eliminación Gaussiana
  - Propagación de error en Gauss
  - Análisis de error backward Gauss
---

# Acumulación del Error de Redondeo en Eliminación Gaussiana

> [!definicion]
> La **acumulación del error de redondeo** en la [[Eliminacion Gaussiana]] es el proceso por el cual los errores locales cometidos en cada operación aritmética de punto flotante se propagan y amplifican a lo largo del algoritmo, contaminando la solución final.

A diferencia del error de truncamiento (que proviene de aproximar procesos continuos), el error de redondeo es inherente a la [[Representacion Punto Flotante IEEE 754|aritmética finita]] y está gobernado por la [[Epsilon Maquina y Precision Relativa|unidad de redondeo]] $u$.

---

## Modelo de error local en operaciones elementales

Recordemos el modelo estándar para el error de redondeo en operaciones básicas:

> [!axioma]
> **Modelo de Wilkinson para error de redondeo.**
> Para cualquier operación $\circ \in \{+, -, \times, \div\}$ en aritmética de punto flotante con [[Epsilon Maquina y Precision Relativa|unidad de redondeo]] $u$:
> $$\text{fl}(x \circ y) = (x \circ y)(1 + \delta), \quad |\delta| \leq u$$
> 
> Este modelo asume el [[Modos de Redondeo IEEE 754|modo de redondeo]] por defecto (*round to nearest, ties to even*).

Cada operación elemental introduce un error relativo acotado por $u$. El desafío es entender cómo estos errores locales se **combinan y amplifican** a lo largo de las $O(n^3)$ operaciones de la eliminación Gaussiana.

---

## Propagación del error en la fase de eliminación

Consideremos el paso $k$ de la eliminación, donde se actualiza un elemento $a_{ij}$:

$$a_{ij}^{(k+1)} = a_{ij}^{(k)} - m_{ik} \cdot a_{kj}^{(k)}$$

En aritmética exacta, esto es una simple resta. En aritmética finita, cada operación introduce error.

> [!teoria]
> **Error local en la actualización.**
> Sean $\tilde{a}_{ij}^{(k)}$ los valores efectivamente calculados. El valor actualizado satisface:
> $$\tilde{a}_{ij}^{(k+1)} = \left( \tilde{a}_{ij}^{(k)} - \tilde{m}_{ik} \cdot \tilde{a}_{kj}^{(k)} (1 + \delta_1) \right) (1 + \delta_2)$$
> donde $|\delta_1|, |\delta_2| \leq u$.
> 
> Expandiendo y agrupando términos de orden $u$:
> $$\tilde{a}_{ij}^{(k+1)} \approx \tilde{a}_{ij}^{(k)} - \tilde{m}_{ik} \cdot \tilde{a}_{kj}^{(k)} + \text{términos de error}$$
> 
> El error absoluto acumulado en $a_{ij}$ crece con cada actualización.

El problema principal es que los errores cometidos en pasos tempranos afectan los multiplicadores $m_{ik}$ y los pivotes $a_{kk}$, que a su vez se usan en pasos posteriores, creando una **retroalimentación del error**.

---

## El factor de crecimiento $\rho$

La magnitud del error acumulado depende críticamente de cuánto crecen los elementos de la matriz durante la eliminación.

> [!definicion]
> El **factor de crecimiento** $\rho$ para la eliminación Gaussiana se define como:
> $$\rho = \frac{\max_{i,j,k} |a_{ij}^{(k)}|}{\max_{i,j} |a_{ij}|}$$
> donde $a_{ij}^{(k)}$ son los elementos generados en el paso $k$ de la eliminación, y $a_{ij}$ son los elementos de la matriz original $A$.

> [!teorema]
> **Cota de error hacia atrás para eliminación Gaussiana (Wilkinson, 1961).**
> Si se aplica eliminación Gaussiana con [[Pivoteo Parcial Total Estabilidad|pivoteo parcial]] en aritmética con unidad de redondeo $u$, los factores calculados $\tilde{L}$ y $\tilde{U}$ satisfacen:
> $$\tilde{L}\tilde{U} = A + \Delta A, \quad \|\Delta A\|_\infty \leq \rho \cdot n \cdot u \cdot \|A\|_\infty$$
> 
> El factor $\rho \cdot n \cdot u$ determina la **pérdida de dígitos** en la factorización.

> [!demostracion]
> **Idea de la demostración (Wilkinson).**
> 
> 1. Cada operación elemental introduce error $\leq u$ en valor relativo.
> 2. El error se propaga linealmente a través de las operaciones subsecuentes.
> 3. Los multiplicadores $m_{ik}$ satisfacen $|m_{ik}| \leq 1$ gracias al pivoteo parcial.
> 4. El crecimiento de los elementos $a_{ij}^{(k)}$ está acotado por $\rho \cdot \|A\|_\infty$.
> 5. Sumando las contribuciones de error a lo largo de las $O(n^3)$ operaciones, se obtiene la cota con el factor $n$ adicional.
> 
> La demostración completa es técnica y se encuentra en *Wilkinson, J.H. (1961). Error Analysis of Direct Methods of Matrix Inversion. J. ACM.*

---

## Comportamiento del factor de crecimiento $\rho$

El valor de $\rho$ determina la estabilidad práctica del algoritmo.

| Estrategia | Cota teórica de $\rho$ | Valor típico en práctica |
|:---|:---:|:---:|
| Sin pivoteo | Ilimitado | Puede ser enorme |
| [[Pivoteo Parcial Total Estabilidad\|Pivoteo parcial]] | $\leq 2^{n-1}$ | $\approx 10$ - $100$ |
| [[Pivoteo Parcial Total Estabilidad\|Pivoteo total]] | $\leq n^{1/2} [2 \cdot 3^{1/2} \cdots n^{1/(n-1)}]^{1/2}$ | $\approx 1$ - $10$ |

> [!warning]
> **¿Qué significa $\rho = 2^{n-1}$ en la práctica?**
> 
> Para $n = 1000$, $2^{999} \approx 10^{300}$. Si $\rho$ alcanzara esta cota teórica, la solución no tendría **ningún dígito correcto** en precisión doble ($u \approx 10^{-16}$).
> 
> Afortunadamente, las matrices que alcanzan esta cota son **extremadamente raras** en aplicaciones prácticas. El ejemplo patológico estándar es la [[Matriz de Wilkinson]], construida específicamente para forzar el máximo crecimiento.

> [!ejemplo]
> **Matriz de Wilkinson (caso patológico).**
> 
> $$A = \begin{pmatrix} 
> 1 & 0 & 0 & \cdots & 0 & 1 \\
> -1 & 1 & 0 & \cdots & 0 & 1 \\
> -1 & -1 & 1 & \cdots & 0 & 1 \\
> \vdots & \vdots & \vdots & \ddots & \vdots & \vdots \\
> -1 & -1 & -1 & \cdots & 1 & 1 \\
> -1 & -1 & -1 & \cdots & -1 & 1
> \end{pmatrix}$$
> 
> Para esta matriz, el pivoteo parcial **no evita** el crecimiento exponencial. Con $n = 50$, $\rho \approx 2^{49} \approx 5.6 \times 10^{14}$, causando pérdida total de precisión.
> 
> ```python
> import numpy as np
> 
> def wilkinson(n):
>     A = np.tril(-np.ones((n, n)), -1) + np.eye(n)
>     A[:, -1] = 1.0
>     return A
> 
> n = 50
> A = wilkinson(n)
> x_exacto = np.ones(n)
> b = A @ x_exacto
> 
> x_calc = np.linalg.solve(A, b)
> error = np.linalg.norm(x_calc - x_exacto, np.inf)
> 
> print(f"Error máximo: {error:.2e}")
> print(f"Número de condición κ(A): {np.linalg.cond(A, np.inf):.2e}")
> ```
> 
> Salida típica:
> ```
> Error máximo: 2.31e-04
> Número de condición κ(A): 1.12e+17
> ```
> 
> La matriz está **bien condicionada** originalmente, pero el crecimiento $\rho$ durante la eliminación destruye la precisión. El [[Pivoteo Parcial Total Estabilidad|pivoteo total]] resolvería este problema, pero a un costo $O(n^3)$ adicional.

---

## Análisis de error hacia adelante

Combinando el análisis hacia atrás con el [[Condicionamiento Numerico Numero Condicion|número de condición]], obtenemos una cota para el error en la solución.

> [!teorema]
> **Error hacia adelante para eliminación Gaussiana.**
> Sea $\tilde{x}$ la solución calculada. Bajo las mismas condiciones que el teorema anterior:
> $$\frac{\|\tilde{x} - x\|_\infty}{\|x\|_\infty} \leq \frac{\rho \cdot n \cdot u \cdot \kappa_\infty(A)}{1 - \rho \cdot n \cdot u \cdot \kappa_\infty(A)}$$
> 
> donde $\kappa_\infty(A) = \|A\|_\infty \|A^{-1}\|_\infty$ es el número de condición.

> [!corolario]
> **Estimación práctica de dígitos correctos.**
> Asumiendo $\rho \approx 10$ (típico) y $n \approx 1000$:
> $$\text{Pérdida de dígitos} \approx \log_{10}(\rho \cdot n \cdot \kappa_\infty(A))$$
> 
> Para una matriz bien condicionada ($\kappa \approx 1$):
> $$\text{Pérdida} \approx \log_{10}(10 \cdot 1000) = \log_{10}(10^4) = 4 \text{ dígitos}$$
> 
> Con precisión doble ($16$ dígitos), aún se obtienen $\approx 12$ dígitos correctos.

---

## Acumulación del error en la sustitución regresiva

La fase de sustitución regresiva también acumula error, aunque típicamente menos que la eliminación.

> [!proposicion]
> **Error en sustitución regresiva.**
> La solución $\tilde{x}$ de $Ux = c$ (con $U$ triangular superior) calculada por sustitución regresiva satisface:
> $$(U + \Delta U)\tilde{x} = c, \quad \|\Delta U\|_\infty \leq n \cdot u \cdot \|U\|_\infty + O(u^2)$$
> 
> El error es proporcional a $n \cdot u$, que para $n$ moderado es pequeño comparado con el error de la eliminación.

La combinación de errores de ambas fases da la cota global mencionada anteriormente.

---

## Efecto del pivoteo en la acumulación del error

El pivoteo es la herramienta fundamental para controlar $\rho$.

> [!teoria]
> **¿Por qué el pivoteo parcial funciona?**
> 
> 1. Al seleccionar el pivote como el máximo de la columna, todos los multiplicadores satisfacen $|m_{ik}| \leq 1$.
> 2. Esto evita que errores de pasos anteriores se **amplifiquen** por factores $> 1$ al propagarse.
> 3. El crecimiento $\rho$ ocurre solo por **suma** de términos, no por multiplicación por factores grandes.
> 4. En la práctica, la cancelación y la estructura de las matrices mantienen $\rho$ moderado.

> [!ejemplo]
> **Comparación numérica: con y sin pivoteo.**
> 
> ```python
> import numpy as np
> from scipy.linalg import lu
> 
> # Matriz mal escalada pero bien condicionada
> A = np.array([[1e-15, 1.0],
>               [1.0, 1.0]])
> x_exacto = np.array([1.0, 1.0])
> b = A @ x_exacto
> 
> # Sin pivoteo (implementación manual)
> def gauss_sin_pivoteo(A, b):
>     n = len(b)
>     for k in range(n-1):
>         for i in range(k+1, n):
>             factor = A[i, k] / A[k, k]
>             A[i, k:] -= factor * A[k, k:]
>             b[i] -= factor * b[k]
>     x = np.zeros(n)
>     for i in range(n-1, -1, -1):
>         x[i] = (b[i] - A[i, i+1:] @ x[i+1:]) / A[i, i]
>     return x
> 
> x_sin = gauss_sin_pivoteo(A.copy(), b.copy())
> 
> # Con pivoteo (NumPy)
> x_con = np.linalg.solve(A, b)
> 
> print(f"Sin pivoteo: {x_sin}")
> print(f"Con pivoteo: {x_con}")
> print(f"Exacto:      {x_exacto}")
> ```
> 
> Salida típica:
> ```
> Sin pivoteo: [0. 1.]
> Con pivoteo: [1. 1.]
> Exacto:      [1. 1.]
> ```
> 
> La diferencia es dramática: sin pivoteo, el resultado es completamente erróneo.

---

## Acumulación del error en matrices mal condicionadas

Incluso con pivoteo, si la matriz está mal condicionada ($\kappa(A)$ grande), el error puede ser significativo.

> [!warning]
> **Límite fundamental del condicionamiento.**
> Si $\kappa_\infty(A) \approx 10^{16}$ en precisión doble, **ningún algoritmo** puede dar dígitos correctos, porque el error relativo en los datos (inevitable por redondeo al almacenar $A$ y $b$) ya es del orden de $10^{-16}$, y el condicionamiento lo amplifica a $\approx 1$ (100% de error).
> 
> Este es un problema del **problema matemático**, no del algoritmo. Ver [[Condicionamiento Numerico Numero Condicion]] para más detalles.

> [!ejemplo]
> **Efecto del mal condicionamiento.**
> 
> ```python
> import numpy as np
> from scipy.linalg import hilbert
> 
> n = 12
> A = hilbert(n)  # κ ≈ 10^16
> x_exacto = np.ones(n)
> b = A @ x_exacto
> 
> x_calc = np.linalg.solve(A, b)
> error = np.linalg.norm(x_calc - x_exacto, np.inf)
> 
> kappa = np.linalg.cond(A, np.inf)
> 
> print(f"κ(A) = {kappa:.2e}")
> print(f"Error máximo = {error:.2e}")
> print(f"Dígitos correctos ≈ {-np.log10(error):.1f}")
> ```
> 
> Salida típica:
> ```
> κ(A) = 1.79e+16
> Error máximo = 1.23e+00
> Dígitos correctos ≈ -0.1
> ```
> 
> El resultado es **completamente incorrecto** a pesar de usar un algoritmo estable con pivoteo.

---

## Refinamiento iterativo

Cuando se requiere alta precisión en sistemas mal condicionados (pero no extremadamente), se puede aplicar **refinamiento iterativo**.

> [!algoritmo]
> **Refinamiento iterativo de la solución.**
> 
> 1. Resolver $Ax^{(0)} = b$ usando eliminación Gaussiana con pivoteo parcial.
> 2. Para $k = 0, 1, 2, \dots$ hasta convergencia:
>     - Calcular el residuo $r^{(k)} = b - A x^{(k)}$ en **precisión extendida** (o doble precisión si no hay otra).
>     - Resolver $A \Delta x^{(k)} = r^{(k)}$ usando la factorización LU ya calculada.
>     - Actualizar $x^{(k+1)} = x^{(k)} + \Delta x^{(k)}$.
> 
> **Costo adicional:** $O(n^2)$ por iteración (solo sustituciones).

> [!info]
> **¿Por qué funciona?**
> El cálculo del residuo $r^{(k)}$ en precisión extendida captura la información perdida por redondeo en la solución inicial. Resolver con la misma $LU$ (que ya está factorizada) es barato.
> 
> El refinamiento iterativo puede recuperar varios dígitos de precisión, incluso hasta alcanzar la precisión de la máquina si el condicionamiento no es extremo.

```python
import numpy as np
from scipy.linalg import lu_factor, lu_solve

def refinement(A, b, n_iter=5):
    lu, piv = lu_factor(A)
    x = lu_solve((lu, piv), b)
    
    for k in range(n_iter):
        r = b - A @ x
        dx = lu_solve((lu, piv), r)
        x = x + dx
        
    return x
```

---

## Resumen: Fuentes de error en eliminación Gaussiana

| Fuente | Magnitud típica | Control |
|:---|:---:|:---|
| Error de redondeo local | $\leq u \approx 10^{-16}$ | Inevitable |
| Factor de crecimiento $\rho$ | $1$ - $10^4$ | [[Pivoteo Parcial Total Estabilidad\|Pivoteo]] |
| Dimensión $n$ | Factor $n$ en cota | Inevitable para método directo |
| [[Condicionamiento Numerico Numero Condicion\|Condicionamiento]] $\kappa(A)$ | $1$ - $10^{16}$ | Reformular problema o precondicionar |
| [[Perdida Significancia y Cancelacion Catastrofica\|Cancelación catastrófica]] | Variable | Reordenar operaciones |

> [!corolario]
> **Regla de Wilkinson para eliminación Gaussiana.**
> *"La eliminación Gaussiana con pivoteo parcial es un algoritmo numéricamente estable para la gran mayoría de matrices prácticas. Cuando falla, es casi siempre debido a un mal condicionamiento del problema, no a inestabilidad del algoritmo."*
