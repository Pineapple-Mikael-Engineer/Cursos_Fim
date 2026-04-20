---
title: Condicionamiento Numerico Numero Condicion
tags:
  - metodos-numericos
  - teoria
  - error-numerico
  - algebra-lineal-numerica
draft: false
aliases:
  - Número de condición
  - Condicionamiento
  - κ(A)
  - Sensibilidad numérica
---

# Condicionamiento Numérico y Número de Condición $\kappa(A)$

> [!definicion]
> El **condicionamiento** de un problema matemático mide la sensibilidad de la solución ante perturbaciones infinitesimales en los datos de entrada. Un problema está **bien condicionado** si pequeños cambios en los datos producen pequeños cambios en la solución. Está **mal condicionado** si pequeñas perturbaciones se amplifican desproporcionadamente.

El condicionamiento es una propiedad **intrínseca del problema matemático**, independiente del algoritmo utilizado para resolverlo. No puede corregirse con mayor precisión aritmética ni con algoritmos más sofisticados.

---

## Número de condición para sistemas lineales $Ax = b$

Dado un sistema lineal $Ax = b$ con $A \in \mathbb{R}^{n \times n}$ no singular, interesa cuantificar cómo varía la solución $x$ cuando se perturban la matriz $A$ o el vector $b$.

> [!teorema]
> **Número de condición de una matriz.**
> Sea $\| \cdot \|$ una [[Normas Matriciales Inducidas|norma matricial inducida]]. El **número de condición** de $A$ respecto a esa norma se define como:
> $$\kappa(A) = \|A\| \cdot \|A^{-1}\|$$
> 
> Por convención, si $A$ es singular, $\kappa(A) = \infty$.

Para la norma espectral $\|\cdot\|_2$, el número de condición se expresa en términos de los [[Valores Singulares y Descomposicion SVD|valores singulares]] de $A$:
$$\kappa_2(A) = \frac{\sigma_{\max}(A)}{\sigma_{\min}(A)}$$
donde $\sigma_{\max}$ y $\sigma_{\min}$ son los valores singulares máximo y mínimo de $A$.

---

## Análisis de sensibilidad hacia adelante

Consideremos perturbaciones en el vector de términos independientes $b$.

> [!teorema]
> **Sensibilidad respecto a perturbaciones en $b$.**
> Sea $Ax = b$ y $A(x + \Delta x) = b + \Delta b$. Entonces:
> $$\frac{\|\Delta x\|}{\|x\|} \leq \kappa(A) \cdot \frac{\|\Delta b\|}{\|b\|}$$
> 
> El número de condición $\kappa(A)$ actúa como factor de amplificación del error relativo en los datos.

> [!demostracion]
> De $A\Delta x = \Delta b$, tenemos $\Delta x = A^{-1}\Delta b$.
> 
> Tomando normas:
> $$\|\Delta x\| = \|A^{-1}\Delta b\| \leq \|A^{-1}\| \cdot \|\Delta b\|$$
> 
> Por otro lado, de $Ax = b$:
> $$\|b\| = \|Ax\| \leq \|A\| \cdot \|x\| \implies \frac{1}{\|x\|} \leq \frac{\|A\|}{\|b\|}$$
> 
> Multiplicando las desigualdades:
> $$\frac{\|\Delta x\|}{\|x\|} \leq \|A^{-1}\| \cdot \|\Delta b\| \cdot \frac{\|A\|}{\|b\|} = \kappa(A) \cdot \frac{\|\Delta b\|}{\|b\|}$$

> [!teorema]
> **Sensibilidad respecto a perturbaciones en $A$.**
> Sea $(A + \Delta A)(x + \Delta x) = b$. Para perturbaciones suficientemente pequeñas tales que $\|\Delta A\| < 1 / \|A^{-1}\|$:
> $$\frac{\|\Delta x\|}{\|x\|} \leq \frac{\kappa(A)}{1 - \kappa(A)\frac{\|\Delta A\|}{\|A\|}} \cdot \frac{\|\Delta A\|}{\|A\|}$$
> 
> Para perturbaciones infinitesimales ($\|\Delta A\| \to 0$), la cota se aproxima a $\kappa(A) \cdot \frac{\|\Delta A\|}{\|A\|}$.

---

## Propiedades fundamentales

> [!proposicion]
> **Propiedades del número de condición.**
> 1. $\kappa(A) \geq 1$ para cualquier [[Normas Matriciales Inducidas|norma inducida]].
> 2. $\kappa(\alpha A) = \kappa(A)$ para cualquier escalar $\alpha \neq 0$.
> 3. Si $A$ es ortogonal ($A^T A = I$), entonces $\kappa_2(A) = 1$ (matriz perfectamente condicionada).
> 4. $\kappa_2(A)$ grande indica que $A$ está *cerca* de ser singular.
> 5. $\kappa(A)$ depende de la norma elegida, pero para cualquier par de normas $\|\cdot\|_\alpha$ y $\|\cdot\|_\beta$ en $\mathbb{R}^{n \times n}$, existen constantes $c_1, c_2 > 0$ tales que $c_1 \kappa_\alpha(A) \leq \kappa_\beta(A) \leq c_2 \kappa_\alpha(A)$.

> [!ejemplo]
> **Cálculo de $\kappa(A)$ para matrices $2 \times 2$.**
> 
> **Matriz bien condicionada:**
> $$A_1 = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \quad \kappa_2(A_1) = 1$$
> 
> **Matriz moderadamente condicionada:**
> $$A_2 = \begin{pmatrix} 10 & 0 \\ 0 & 0.1 \end{pmatrix}, \quad \kappa_2(A_2) = \frac{10}{0.1} = 100$$
> 
> **Matriz mal condicionada ([[Matriz de Hilbert]]):**
> $$H_3 = \begin{pmatrix} 1 & 1/2 & 1/3 \\ 1/2 & 1/3 & 1/4 \\ 1/3 & 1/4 & 1/5 \end{pmatrix}, \quad \kappa_2(H_3) \approx 524$$
> 
> Para $H_{10}$, $\kappa_2 \approx 1.6 \times 10^{13}$, lo que significa que un error relativo de $10^{-16}$ en los datos puede amplificarse a un error del $0.16\%$ en la solución.

---

## Interpretación geométrica

> [!teoria]
> **Interpretación mediante [[Valores Singulares y Descomposicion SVD|valores singulares]].**
> La matriz $A$ mapea la esfera unitaria en un hiperelipsoide. Los semiejes de este elipsoide tienen longitudes $\sigma_1 \geq \sigma_2 \geq \dots \geq \sigma_n > 0$.
> 
> El número de condición $\kappa_2(A) = \sigma_1 / \sigma_n$ es el cociente entre el semieje mayor y el menor.
> 
> - Si $\kappa_2(A) \approx 1$, la esfera se mapea aproximadamente en otra esfera (transformación *casi* isométrica).
> - Si $\kappa_2(A) \gg 1$, el elipsoide es muy alargado en algunas direcciones y muy aplanado en otras. Esto implica que ciertas direcciones en el espacio de entrada son amplificadas mientras otras son atenuadas drásticamente.

Esta interpretación explica por qué sistemas mal condicionados son sensibles a perturbaciones: una pequeña componente del error en la dirección del vector singular derecho asociado a $\sigma_n$ se magnifica por $1/\sigma_n$ al resolver el sistema.

---

## Ejemplo numérico ilustrativo

> [!ejemplo]
> **Efecto del mal condicionamiento en la precisión.**
> 
> ```python
> import numpy as np
> from scipy.linalg import hilbert
> 
> # Matriz mal condicionada (Hilbert 5x5)
> A = hilbert(5)
> x_exacto = np.ones(5)
> b = A @ x_exacto
> 
> # Perturbación pequeña en b
> delta_b = np.random.randn(5) * 1e-10
> b_perturbado = b + delta_b
> 
> # Resolver ambos sistemas
> x_nominal = np.linalg.solve(A, b)
> x_perturbado = np.linalg.solve(A, b_perturbado)
> 
> kappa = np.linalg.cond(A, 2)
> error_relativo_b = np.linalg.norm(delta_b, 2) / np.linalg.norm(b, 2)
> error_relativo_x = np.linalg.norm(x_perturbado - x_exacto, 2) / np.linalg.norm(x_exacto, 2)
> 
> print(f"κ₂(A) = {kappa:.2e}")
> print(f"Error relativo en b: {error_relativo_b:.2e}")
> print(f"Error relativo en x: {error_relativo_x:.2e}")
> print(f"Factor de amplificación: {error_relativo_x / error_relativo_b:.2e}")
> ```
> 
> Salida típica:
> ```
> κ₂(A) = 4.77e+05
> Error relativo en b: 2.34e-11
> Error relativo en x: 8.92e-06
> Factor de amplificación: 3.81e+05
> ```
> 
> Una perturbación minúscula en $b$ (orden $10^{-11}$) produce un error en $x$ cinco órdenes de magnitud mayor, consistente con la cota $\kappa(A)$.

---

## Relación con el error de redondeo en algoritmos de resolución

El condicionamiento determina el **límite inferior** del error que cualquier algoritmo puede alcanzar.

> [!teorema]
> **Cota de error para algoritmos estables.**
> Si se resuelve $Ax = b$ mediante un algoritmo numéricamente estable (como [[Eliminacion Gaussiana]] con [[Pivoteo Parcial Total Estabilidad|pivoteo parcial]]) en aritmética con [[Epsilon Maquina y Precision Relativa|unidad de redondeo]] $u$, la solución calculada $\tilde{x}$ satisface aproximadamente:
> $$\frac{\|\tilde{x} - x\|}{\|x\|} \lesssim \kappa(A) \cdot u \cdot \rho$$
> donde $\rho$ es el **factor de crecimiento** de los elementos durante la eliminación. Para pivoteo parcial, $\rho$ típicamente es $O(1)$ o crece lentamente con $n$.

> [!warning]
> **Regla práctica fundamental.**
> La solución numérica de un sistema lineal con aritmética de precisión $u$ tendrá aproximadamente:
> $$\text{dígitos correctos} \approx -\log_{10}(u) - \log_{10}(\kappa(A))$$
> 
> Para precisión doble ($u \approx 10^{-16}$) y $\kappa(A) = 10^8$, solo se obtienen $\approx 8$ dígitos correctos, **independientemente del algoritmo**.

---

## Estimación del número de condición

Calcular $\kappa(A)$ exactamente requiere conocer $A^{-1}$ o los valores singulares, lo cual es costoso ($O(n^3)$). En la práctica se usan **estimadores** de bajo costo.

> [!info]
> **Estimadores comunes de $\kappa(A)$:**
> - **Estimador de Hager-Higham:** Basado en resolver sistemas $A^T y = c$ y $A z = y$ iterativamente para aproximar $\|A^{-1}\|_1$.
> - **Estimador de LINPACK:** Utiliza la factorización [[Factorizacion LU|LU]] para estimar $\|A^{-1}\|_1$.
> - **Número de condición de Skeel:** $\kappa_S(A) = \| |A^{-1}| \cdot |A| \|_\infty$, que es invariante bajo escalamiento por filas.

Estos estimadores están implementados en bibliotecas como LAPACK (`?gecon`) y son fundamentales para [[Analisis Error Directos|evaluar la fiabilidad]] de una solución numérica.

---

## Número de condición para otros problemas

El concepto de condicionamiento se extiende a todos los problemas del análisis numérico.

| Problema | Definición de $\kappa$ |
|:---|:---|
| **Evaluación de función $f(x)$** | $\kappa_f(x) = \left\| \frac{x \cdot f'(x)}{f(x)} \right\|$ |
| **Raíces de $f(x)=0$** | $\kappa = 1 / \|f'(r)\|$ para raíces simples |
| **[[Interpolacion Polinomica y Matriz Vandermonde|Interpolación polinómica]]** | $\kappa \approx \text{condición de la matriz de Vandermonde}$ |
| **[[Problema Valor Inicial PVI|Problema de valor inicial EDO]]** | $\kappa \approx e^{L t}$ donde $L$ es la constante de Lipschitz |
| **[[Ajuste Minimos Cuadrados|Mínimos cuadrados]]** | $\kappa(A^T A) = [\kappa_2(A)]^2$ (peligroso) |

> [!ejemplo]
> **Condicionamiento de una raíz simple vs. múltiple.**
> 
> Para $f(x) = (x - 1)(x - 10^{-8})$, la raíz $r = 10^{-8}$ tiene:
> $$f'(r) \approx -1, \quad \kappa = 1 / |f'(r)| \approx 1$$
> 
> Está **bien condicionada**.
> 
> Para $f(x) = (x - 1)^2$, la raíz doble $r = 1$ tiene $f'(1) = 0$, luego $\kappa = \infty$. Está **mal condicionada**: una perturbación $\epsilon$ en $f$ desplaza la raíz en $O(\sqrt{\epsilon})$, no en $O(\epsilon)$. Este fenómeno afecta la [[Convergencia Lineal Raices Multiples|velocidad de convergencia]] de [[Newton Raphson]].

> [!ejemplo]
> **Condicionamiento en mínimos cuadrados.**
> 
> El problema de mínimos cuadrados $\min_x \|Ax - b\|_2$ tiene número de condición:
> $$\kappa_{\text{LS}}(A) = \kappa_2(A) + \frac{\kappa_2(A)^2 \cdot \|r\|_2}{\|A\|_2 \cdot \|x\|_2}$$
> donde $r = b - Ax$ es el residuo.
> 
> Para residuos pequeños, el problema está bien condicionado si $\kappa_2(A)$ es moderado. Para residuos grandes, el condicionamiento se degrada cuadráticamente con $\kappa_2(A)$. Esto motiva el uso de [[Factorizacion QR|factorización QR]] en lugar de las [[Ecuaciones Normales y Matriz Gram|ecuaciones normales]].

---

## Distinción crucial: Condicionamiento vs. Estabilidad

> [!warning]
> **Confusión frecuente.**
> - **Condicionamiento:** Propiedad del **problema matemático**. No se puede cambiar sin reformular el problema.
> - **Estabilidad:** Propiedad del **algoritmo numérico**. Un algoritmo es [[Estabilidad Algoritmos Forward Backward|estable]] si produce una solución cercana a la exacta para un problema bien condicionado.
> 
> Un problema mal condicionado **no tiene solución numérica precisa**, sin importar cuán estable sea el algoritmo. Un algoritmo inestable **arruina** la solución incluso para problemas bien condicionados.

> [!info]
> **Regla de Wilkinson:**
> *"Un algoritmo numéricamente estable aplicado a un problema bien condicionado produce una solución precisa. Un algoritmo inestable aplicado a un problema bien condicionado produce basura. Ningún algoritmo puede rescatar un problema mal condicionado."*

Esta distinción es fundamental para diagnosticar fuentes de error en cálculos numéricos y guía el diseño de [[Estabilidad Algoritmos Forward Backward|algoritmos estables]].

---

## Relación con el precondicionamiento

En la resolución iterativa de sistemas lineales ([[Jacobi]], [[Gauss Seidel]], [[Gradiente Conjugado]]), la velocidad de convergencia depende críticamente de $\kappa(A)$.

> [!teoria]
> **Convergencia de métodos iterativos.**
> Para el [[Gradiente Conjugado|método del gradiente conjugado]], el error en la iteración $k$ satisface:
> $$\frac{\|x_k - x^*\|_A}{\|x_0 - x^*\|_A} \leq 2 \left( \frac{\sqrt{\kappa_2(A)} - 1}{\sqrt{\kappa_2(A)} + 1} \right)^k$$
> 
> Un $\kappa_2(A)$ grande implica convergencia lenta.

Para acelerar la convergencia, se busca una matriz $M \approx A$ fácil de invertir tal que $\kappa_2(M^{-1}A) \ll \kappa_2(A)$. Este proceso se conoce como **precondicionamiento** y es esencial en la resolución de grandes sistemas dispersos provenientes de [[Diferenciacion Numerica|ecuaciones diferenciales]].
