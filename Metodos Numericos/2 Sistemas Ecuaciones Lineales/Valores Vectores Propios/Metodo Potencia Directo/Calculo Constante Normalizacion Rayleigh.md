---
title: Calculo Constante Normalizacion Rayleigh
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - autovalores
  - metodo-potencia
  - rayleigh
draft: false
aliases:
  - Cociente de Rayleigh
  - Rayleigh quotient
  - Estimación de autovalores
---

# Cálculo del Autovalor: Cociente de Rayleigh

> [!definicion]
> Dada una matriz $A \in \mathbb{R}^{n \times n}$ y un vector no nulo $y \in \mathbb{R}^n$, el **cociente de Rayleigh** se define como:
> $$R_A(y) = \frac{y^T A y}{y^T y}$$
>
> Si $y$ es un autovector exacto de $A$, entonces $R_A(y) = \lambda$ (el autovalor correspondiente). Si $y$ es una aproximación a un autovector, $R_A(y)$ es una estimación del autovalor.

---

## Ejemplo

> [!ejemplo]
> **Estimación del autovalor dominante durante el método de la potencia.**
>
> Para $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, los autovalores exactos son $\lambda_1 = 3$ y $\lambda_2 = 1$.
>
> Aplicando el método de la potencia desde $y^{(0)} = (1, 0)^T$ con normalización:
>
> | $k$ | $y^{(k)}$ (normalizado) | $R_A(y^{(k)}) = y^{(k)T} A y^{(k)}$ |
> |:---|:---|:---|
> | 0 | (1.000, 0.000) | 2.000 |
> | 1 | (0.894, 0.447) | 2.500 |
> | 2 | (0.780, 0.625) | 2.900 |
> | 3 | (0.732, 0.681) | 2.980 |
> | 4 | (0.716, 0.698) | 2.996 |
> | 5 | (0.708, 0.706) | 2.999 |
>
> El cociente de Rayleigh converge a $\lambda_1 = 3$ más rápido que el autovector converge. Para $k=5$, el autovector tiene error $\approx 0.001$, mientras que el autovalor tiene error $\approx 0.001$ también (similar).
>
> **Ventaja:** No es necesario calcular $\lambda$ por separado; el cociente de Rayleigh lo proporciona automáticamente en cada iteración.

---

## Propiedades fundamentales

> [!teorema]
> El cociente de Rayleigh satisface las siguientes propiedades:
>
> 1. **Homogeneidad:** $R_A(\alpha y) = R_A(y)$ para cualquier $\alpha \neq 0$. Por lo tanto, solo depende de la dirección de $y$.
>
> 2. **Rango:** Para cualquier $y \neq 0$:
>    $$\lambda_{\min} \leq R_A(y) \leq \lambda_{\max}$$
>    donde $\lambda_{\min}$ y $\lambda_{\max}$ son el menor y mayor autovalor de $A$ (si $A$ es simétrica).
>
> 3. **Estacionariedad:** Los puntos críticos de $R_A(y)$ son los autovectores de $A$, y los valores críticos son los autovalores correspondientes.

> [!demostracion]
> **Propiedad 1 (Homogeneidad):**
> $$R_A(\alpha y) = \frac{(\alpha y)^T A (\alpha y)}{(\alpha y)^T (\alpha y)} = \frac{\alpha^2 y^T A y}{\alpha^2 y^T y} = \frac{y^T A y}{y^T y} = R_A(y)$$
>
> **Propiedad 2 (Rango para $A$ simétrica):**
> Para $A$ simétrica, existe una base ortonormal de autovectores $\{v_1, \dots, v_n\}$ con autovalores $\lambda_1 \geq \lambda_2 \geq \cdots \geq \lambda_n$. Escribiendo $y = \sum_{i=1}^n c_i v_i$:
> $$R_A(y) = \frac{\sum_{i=1}^n c_i^2 \lambda_i}{\sum_{i=1}^n c_i^2}$$
>
> Esto es un promedio ponderado de los autovalores, por lo tanto:
> $$\lambda_n \leq R_A(y) \leq \lambda_1$$
>
> **Propiedad 3 (Estacionariedad):**
> El gradiente de $R_A(y)$ respecto a $y$ es:
> $$\nabla R_A(y) = \frac{2}{y^T y} \left( A y - R_A(y) y \right)$$
>
> Los puntos críticos satisfacen $\nabla R_A(y) = 0$, lo que implica $A y = R_A(y) y$, es decir, $y$ es autovector y $R_A(y)$ su autovalor.

---

## Propiedad de optimalidad

> [!teorema]
> Para una matriz simétrica $A$, el cociente de Rayleigh proporciona la mejor aproximación al autovalor en el siguiente sentido:
>
> Para cualquier vector $y \neq 0$, el escalar $\alpha$ que minimiza $\|A y - \alpha y\|_2$ es precisamente $\alpha = R_A(y)$.

> [!demostracion]
> Se busca $\alpha$ que minimice $\|A y - \alpha y\|_2^2 = (A y - \alpha y)^T (A y - \alpha y)$.
>
> Derivando respecto a $\alpha$ e igualando a cero:
> $$\frac{d}{d\alpha} \left( y^T A^T A y - 2\alpha y^T A y + \alpha^2 y^T y \right) = -2 y^T A y + 2\alpha y^T y = 0$$
>
> Despejando:
> $$\alpha = \frac{y^T A y}{y^T y} = R_A(y)$$
>
> Por lo tanto, $R_A(y)$ es el escalar que mejor aproxima $A y$ como múltiplo de $y$ en norma euclidiana.

---

## Convergencia cuadrática para matrices simétricas

> [!teorema]
> Sea $A$ simétrica y sea $y$ una aproximación al autovector $v_1$ con error $\varepsilon = \|y - v_1\|$ (con $y$ normalizado). Entonces el error en el cociente de Rayleigh satisface:
> $$|R_A(y) - \lambda_1| = O(\varepsilon^2)$$
>
> Es decir, si $y$ tiene $d$ dígitos correctos como autovector, entonces $R_A(y)$ tiene aproximadamente $2d$ dígitos correctos como autovalor.

> [!demostracion]
> Sin pérdida de generalidad, supóngase $\|v_1\| = 1$ y $\|y\| = 1$. Escríbase $y = v_1 + \delta$, donde $\delta$ es ortogonal a $v_1$ (la componente en la dirección de $v_1$ puede absorberse en la normalización). Entonces:
> $$y^T A y = (v_1 + \delta)^T A (v_1 + \delta) = v_1^T A v_1 + 2 v_1^T A \delta + \delta^T A \delta$$
>
> Como $A v_1 = \lambda_1 v_1$ y $v_1^T \delta = 0$, se tiene $v_1^T A \delta = \lambda_1 v_1^T \delta = 0$. Por lo tanto:
> $$y^T A y = \lambda_1 + \delta^T A \delta$$
>
> Además $y^T y = 1 + \delta^T \delta = 1 + \|\delta\|^2$.
>
> Entonces:
> $$R_A(y) = \frac{\lambda_1 + \delta^T A \delta}{1 + \|\delta\|^2} = (\lambda_1 + \delta^T A \delta)(1 - \|\delta\|^2 + O(\|\delta\|^4))$$
> $$= \lambda_1 - \lambda_1 \|\delta\|^2 + \delta^T A \delta + O(\|\delta\|^4)$$
>
> Como $\delta^T A \delta = O(\|\delta\|^2)$, el error $|R_A(y) - \lambda_1| = O(\|\delta\|^2) = O(\varepsilon^2)$.
>
> **Consecuencia:** Para matrices simétricas, el autovalor converge más rápido que el autovector.

> [!ejemplo]
> Para $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$, en la iteración $k=2$:
> - Error en autovector: $\|y - v_1\| \approx 0.073$ (un dígito correcto)
> - Error en autovalor: $|R_A(y) - 3| = 0.1$ (un dígito correcto)
>
> En $k=3$:
> - Error en autovector: $\approx 0.025$ (un dígito correcto)
> - Error en autovalor: $|R_A(y) - 3| = 0.02$ (dos dígitos correctos)
>
> Se observa la convergencia cuadrática del autovalor predicha por el teorema.

---

## Relación con el método de la potencia

> [!info]
> En el método de la potencia, el cociente de Rayleigh se calcula en cada iteración para estimar $\lambda_1$:
>
> ```python
> v = y0 / np.linalg.norm(y0)
> for k in range(max_iter):
>     v_new = A @ v
>     λ = np.dot(v, v_new)   # cociente de Rayleigh (v normalizado)
>     v_new = v_new / np.linalg.norm(v_new)
>     # ...
> ```
>
> Para matrices simétricas, esta estimación converge cuadráticamente, por lo que se obtiene una buena aproximación de $\lambda_1$ incluso antes de que el autovector haya convergido completamente.
>
> Para matrices no simétricas, la convergencia es lineal con factor $r = |\lambda_2/\lambda_1|$, al igual que el autovector.

---

## Aplicación en potencia inversa

> [!info]
> En el método de la potencia inversa, el cociente de Rayleigh se utiliza con la matriz $(A - \mu I)^{-1}$ para aproximar el autovalor más cercano a $\mu$:
> $$\lambda_{\text{cercano}} \approx \mu + \frac{1}{R_{(A-\mu I)^{-1}}(y)}$$
>
> Este tema se desarrolla en [[Variantes Metodo Potencia/Potencia Inversa Valor Propio Menor Modulo]].

---

## Resumen

> [!corolario]
> El cociente de Rayleigh es la herramienta estándar para estimar autovalores a partir de autovectores aproximados:
>
> | Propiedad | Descripción |
> |:---|:---|
> | Definición | $R_A(y) = \frac{y^T A y}{y^T y}$ |
> | Invarianza | $R_A(\alpha y) = R_A(y)$ |
> | Rango (simétrica) | $\lambda_{\min} \leq R_A(y) \leq \lambda_{\max}$ |
> | Optimalidad | Minimiza $\|A y - \alpha y\|$ |
> | Convergencia (simétrica) | Cuadrática: $O(\|y - v_1\|^2)$ |
> | Convergencia (general) | Lineal: $O(\|\lambda_2/\lambda_1\|^k)$ |
>
> **En la práctica:** Para matrices simétricas, el cociente de Rayleigh proporciona estimaciones muy precisas del autovalor dominante incluso con pocas iteraciones del método de la potencia. Por esta razón, es la técnica estándar en implementaciones del método de la potencia y sus variantes.
>
> Este tema complementa a [[Metodo Potencia Directo/index]] y [[Velocidad Convergencia Razon Lambda2 Lambda1]]. Para aplicaciones en la potencia inversa, véase [[Variantes Metodo Potencia/Potencia Inversa Valor Propio Menor Modulo]].