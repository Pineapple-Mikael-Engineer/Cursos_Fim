---
title: Condicionamiento de las Ecuaciones Normales
order: 3
tags:
  - metodos-numericos
  - teoria
  - aproximacion-funciones
  - minimos-cuadrados
  - error-numerico
draft: false
aliases:
  - Condicionamiento de mínimos cuadrados
  - Ecuaciones normales mal condicionadas
  - QR vs ecuaciones normales
---

# Condicionamiento de las Ecuaciones Normales

> [!definicion]
> El **condicionamiento de las ecuaciones normales** describe la pérdida de precisión al resolver $A^TAc = A^Ty$ por formación explícita de la [[Ecuaciones Normales y Matriz Gram|matriz de Gram]]. El defecto central es que el [[Condicionamiento Numerico Numero Condicion|número de condición]] se **eleva al cuadrado**:
> $$\kappa_2(A^TA) = \kappa_2(A)^2.$$

> [!info]
> Resolver las ecuaciones normales pierde el **doble** de dígitos que un método que trabaje directamente con $A$. Para $A$ moderadamente mal condicionada, esto es desastroso; la solución estándar es la **factorización QR**, que evita formar $A^TA$.

---

## El cuadrado del número de condición

> [!teorema]
> Para $A \in \mathbb{R}^{m\times n}$ de rango completo, con valores singulares $\sigma_1 \geq \cdots \geq \sigma_n > 0$:
> $$\kappa_2(A) = \frac{\sigma_1}{\sigma_n}, \qquad \kappa_2(A^TA) = \frac{\sigma_1^2}{\sigma_n^2} = \kappa_2(A)^2.$$

> [!demostracion]
> Los autovalores de $A^TA$ son los cuadrados de los valores singulares de $A$ (por la descomposición SVD $A = U\Sigma V^T$, se tiene $A^TA = V\Sigma^2 V^T$). Entonces los valores singulares de $A^TA$ —al ser simétrica definida positiva— son sus autovalores $\sigma_i^2$, y
> $$\kappa_2(A^TA) = \frac{\sigma_{\max}^2}{\sigma_{\min}^2} = \left(\frac{\sigma_1}{\sigma_n}\right)^2 = \kappa_2(A)^2.$$

> [!warning]
> **Regla de los dígitos perdidos.** Con [[Epsilon Maquina y Precision Relativa|unidad de redondeo]] $u$, la solución por ecuaciones normales tiene error relativo $\sim \kappa_2(A)^2\,u$, mientras que un método estable basado en $A$ logra $\sim \kappa_2(A)\,u$. En doble precisión con $\kappa_2(A) = 10^8$: las ecuaciones normales dan **0 dígitos** correctos; QR da **8**.

---

## Ejemplo: pérdida medida

> [!ejemplo]
> **Matriz de diseño con columnas casi colineales** (ajuste polinómico de grado alto, base de monomios):
>
> | $\kappa_2(A)$ | $\kappa_2(A^TA)$ | Dígitos: ec. normales | Dígitos: QR |
> |:---:|:---:|:---:|:---:|
> | $10^2$ | $10^4$ | 12 | 14 |
> | $10^4$ | $10^8$ | 8 | 12 |
> | $10^6$ | $10^{12}$ | 4 | 10 |
> | $10^8$ | $10^{16}$ | 0 | 8 |
>
> Para $\kappa_2(A) = 10^8$ las ecuaciones normales son inservibles en doble precisión, mientras QR aún conserva 8 dígitos. La diferencia se agrava con la base de monomios (ligada al [[Matriz Vandermonde Mal Condicionamiento|mal condicionamiento de Vandermonde]]).

---

## Alternativa: factorización QR

> [!teorema]
> Sea $A = QR$ con $Q \in \mathbb{R}^{m\times n}$ de columnas ortonormales ($Q^TQ = I$) y $R$ triangular superior. El minimizador de $\|Ac - y\|_2$ resuelve
> $$R\,c = Q^T y,$$
> un sistema triangular bien condicionado **sin** formar $A^TA$.

> [!demostracion]
> Como $Q$ tiene columnas ortonormales, preserva la norma: $\|Ac - y\|_2 = \|QRc - y\|_2$. Descomponiendo $y$ en su parte en $\operatorname{col}(Q)$ y ortogonal,
> $$\|Ac - y\|_2^2 = \|Rc - Q^Ty\|_2^2 + \|(I - QQ^T)y\|_2^2.$$
> El segundo término es independiente de $c$; el primero se anula resolviendo $Rc = Q^Ty$. Como $\kappa_2(R) = \kappa_2(A)$ (no su cuadrado), el método es estable.

> [!info]
> La factorización QR se construye con [[Fundamentos Transformaciones Householder|reflexiones de Householder]], [[Estabilidad Algoritmos Forward Backward|incondicionalmente estables]]. Es el método **por defecto** para mínimos cuadrados (`numpy.linalg.lstsq`, `\` de MATLAB).

---

## Cuándo usar cada método

> [!info]
> | Método | Costo | Condicionamiento | Cuándo |
> |:---|:---|:---|:---|
> | Ecuaciones normales (Cholesky) | $mn^2 + \frac{n^3}{3}$ | $\kappa(A)^2$ | $A$ bien condicionada, $m \gg n$, rapidez |
> | **QR (Householder)** | $2mn^2 - \frac{2n^3}{3}$ | $\kappa(A)$ | uso general, estabilidad |
> | SVD | $\sim mn^2$ (mayor constante) | $\kappa(A)$, robusto a rango deficiente | $A$ casi singular, rango incierto |

> [!warning]
> Las ecuaciones normales **no** son siempre malas: si $\kappa_2(A) \lesssim 10^4$ y se prioriza la velocidad (por ejemplo, $m \gg n$ con $A$ bien condicionada), son aceptables y más rápidas. La regla es: **si hay duda sobre el condicionamiento, usar QR.**

---

## Relación con otras notas

> [!info]
> - El sistema que se evita formar: [[Ecuaciones Normales y Matriz Gram]].
> - La medida de amplificación de error: [[Condicionamiento Numerico Numero Condicion]].
> - La factorización estable alternativa: [[Fundamentos Transformaciones Householder]].
> - El mismo fenómeno en interpolación: [[Matriz Vandermonde Mal Condicionamiento]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Defecto | $\kappa_2(A^TA) = \kappa_2(A)^2$ |
| Dígitos (ec. normales) | $-\log_{10}u - 2\log_{10}\kappa(A)$ |
| Dígitos (QR) | $-\log_{10}u - \log_{10}\kappa(A)$ |
| Alternativa | $Rc = Q^Ty$ (QR) |
| Más robusto aún | SVD |
| Regla | duda ⇒ QR |

> [!corolario]
> Resolver mínimos cuadrados por las ecuaciones normales eleva al cuadrado el número de condición, $\kappa_2(A^TA) = \kappa_2(A)^2$, duplicando los dígitos perdidos respecto a un método basado directamente en $A$. La factorización QR resuelve $Rc = Q^Ty$ con $\kappa_2(R) = \kappa_2(A)$, sin formar $A^TA$, y es estable e idónea como método por defecto; la SVD añade robustez ante rango deficiente. Las ecuaciones normales siguen siendo útiles cuando $A$ está bien condicionada y prima la velocidad, pero ante la duda se prefiere QR. Es el mismo aviso que el [[Matriz Vandermonde Mal Condicionamiento|mal condicionamiento de Vandermonde]] da en interpolación: la representación importa tanto como el problema.
