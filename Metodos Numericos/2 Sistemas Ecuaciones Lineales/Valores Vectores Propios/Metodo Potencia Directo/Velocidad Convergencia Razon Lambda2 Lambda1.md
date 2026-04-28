---
title: Velocidad Convergencia Razon Lambda2 Lambda1
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - autovalores
  - metodo-potencia
  - convergencia
draft: false
aliases:
  - Razón de convergencia
  - Factor de convergencia
---

# Velocidad de Convergencia: Razón $\lambda_2 / \lambda_1$

> [!definicion]
> Sea $A \in \mathbb{R}^{n \times n}$ diagonalizable con autovalores ordenados por módulo decreciente:
> $$|\lambda_1| > |\lambda_2| \geq |\lambda_3| \geq \cdots \geq |\lambda_n|$$
>
> La **razón de convergencia** del método de la potencia es:
> $$r = \left| \frac{\lambda_2}{\lambda_1} \right| < 1$$
>
> Este factor determina qué tan rápido la iteración $y^{(k)} = A^k y^{(0)}$ se acerca al autovector dominante $v_1$.

---

## Ejemplo

> [!ejemplo]
> **Comparación de convergencia para diferentes valores de $r$.**
>
> Sea $A$ una matriz con autovalor dominante $\lambda_1 = 1$ (normalizado) y segundo autovalor $\lambda_2 = r$. Se parte de un vector inicial con componente igual en ambas direcciones.
>
> | $r$ | Iteraciones para 3 dígitos | Iteraciones para 6 dígitos |
> |:---|:---:|:---:|
> | 0.1 | 1 | 2 |
> | 0.5 | 5 | 10 |
> | 0.9 | 29 | 58 |
> | 0.99 | 299 | 598 |
> | 0.999 | 2999 | 5998 |
>
> **Observación:** Cuando $r$ se acerca a $1$, el número de iteraciones crece drásticamente. Para $r = 0.99$, se necesitan casi $600$ iteraciones para obtener $6$ dígitos de precisión.
>
> **Ejemplo concreto:**
>
> $$A = \begin{pmatrix} 1 & 0 \\ 0 & r \end{pmatrix}, \quad y^{(0)} = \begin{pmatrix} 1 \\ 1 \end{pmatrix}$$
>
> Entonces:
> $$y^{(k)} = A^k y^{(0)} = \begin{pmatrix} 1 \\ r^k \end{pmatrix}$$
>
> El error en la dirección (desviación del autovector $(1,0)$) es proporcional a $r^k$. Para $r=0.9$, $0.9^{10} \approx 0.348$, $0.9^{50} \approx 0.005$, $0.9^{100} \approx 0.000026$.

---

## Demostración de la tasa de convergencia

> [!teorema]
> Sea $A$ diagonalizable con autovalores $|\lambda_1| > |\lambda_2| \geq \cdots \geq |\lambda_n|$. Sea $y^{(0)}$ un vector con componente no nula en la dirección de $v_1$, es decir $y^{(0)} = c_1 v_1 + c_2 v_2 + \cdots + c_n v_n$ con $c_1 \neq 0$. Entonces, para la sucesión $z^{(k)} = A^k y^{(0)}$, se cumple:
> $$\left\| \frac{z^{(k)}}{\|z^{(k)}\|} - \frac{v_1}{\|v_1\|} \right\| = O\left( \left| \frac{\lambda_2}{\lambda_1} \right|^k \right)$$

> [!demostracion]
> **Paso 1: Expresión de $z^{(k)}$ en la base de autovectores.**
>
> Como $A v_i = \lambda_i v_i$, se tiene $A^k v_i = \lambda_i^k v_i$. Por lo tanto:
> $$z^{(k)} = A^k y^{(0)} = c_1 \lambda_1^k v_1 + c_2 \lambda_2^k v_2 + \cdots + c_n \lambda_n^k v_n$$
>
> **Paso 2: Factorización del término dominante.**
>
> Factorizando $\lambda_1^k$:
> $$z^{(k)} = \lambda_1^k \left( c_1 v_1 + c_2 \left(\frac{\lambda_2}{\lambda_1}\right)^k v_2 + \cdots + c_n \left(\frac{\lambda_n}{\lambda_1}\right)^k v_n \right)$$
>
> **Paso 3: Escritura del vector normalizado.**
>
> Sea $w^{(k)} = c_1 v_1 + \sum_{i=2}^n c_i \left(\frac{\lambda_i}{\lambda_1}\right)^k v_i$. El vector normalizado es:
> $$\frac{z^{(k)}}{\|z^{(k)}\|} = \frac{w^{(k)}}{\|w^{(k)}\|}$$
>
> **Paso 4: Comportamiento asintótico de $w^{(k)}$.**
>
> Como $|\lambda_i/\lambda_1| < 1$ para $i \geq 2$, se tiene:
> $$\lim_{k \to \infty} w^{(k)} = c_1 v_1$$
>
> El término de error es:
> $$w^{(k)} - c_1 v_1 = \sum_{i=2}^n c_i \left(\frac{\lambda_i}{\lambda_1}\right)^k v_i$$
>
> Para $k$ grande, el término dominante del error es el correspondiente a $\lambda_2$ (pues $|\lambda_2/\lambda_1| \geq |\lambda_i/\lambda_1|$ para $i \geq 2$). Por lo tanto:
> $$\|w^{(k)} - c_1 v_1\| = O\left( \left| \frac{\lambda_2}{\lambda_1} \right|^k \right)$$
>
> **Paso 5: Error en la dirección.**
>
> El error en la dirección está dado por el ángulo entre $w^{(k)}$ y $v_1$. Para vectores cercanos:
> $$\left\| \frac{w^{(k)}}{\|w^{(k)}\|} - \frac{v_1}{\|v_1\|} \right\| \approx \frac{\|w^{(k)} - c_1 v_1\|}{|c_1| \|v_1\|} = O\left( \left| \frac{\lambda_2}{\lambda_1} \right|^k \right)$$

> [!corolario]
> El error en el autovector se reduce aproximadamente en un factor $r = |\lambda_2/\lambda_1|$ en cada iteración. Por lo tanto, el método de la potencia converge **linealmente** con factor de convergencia $r$.

---

## Estimación del número de iteraciones

> [!teoria]
> Para reducir el error en un factor $\varepsilon$ (es decir, lograr $\| \text{error} \| \leq \varepsilon \| \text{error inicial} \|$), se necesita un número de iteraciones $k$ tal que:
> $$r^k \leq \varepsilon$$
>
> Tomando logaritmos:
> $$k \geq \frac{\ln \varepsilon}{\ln r}$$
>
> Como $r < 1$, $\ln r$ es negativo, por lo que $k$ es positivo.
>
> **En términos de dígitos decimales:**
>
> Si se desea obtener $d$ dígitos decimales correctos, el error debe reducirse en un factor $\varepsilon = 10^{-d}$. Entonces:
> $$k \geq \frac{-d \ln 10}{\ln r} = \frac{d}{\log_{10}(1/r)}$$
>
> La cantidad $\log_{10}(1/r) = -\log_{10} r$ es el número de dígitos ganados por iteración.

> [!ejemplo]
> Para $r = 0.5$, $\log_{10}(1/0.5) = \log_{10}(2) \approx 0.301$ dígitos por iteración. Para ganar $6$ dígitos se necesitan $6 / 0.301 \approx 20$ iteraciones.
>
> Para $r = 0.9$, $\log_{10}(1/0.9) \approx 0.0458$ dígitos por iteración. Para ganar $6$ dígitos se necesitan $6 / 0.0458 \approx 131$ iteraciones (como se ve en la tabla del ejemplo).

---

## Caso de autovalores complejos

> [!warning]
> Si $\lambda_1$ y $\lambda_2$ son complejos conjugados con el mismo módulo ($|\lambda_1| = |\lambda_2|$), entonces $r = 1$ y el método de la potencia **no converge** (la iteración puede oscilar).
>
> **Ejemplo:**
> $$A = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$$
>
> Los autovalores son $\lambda = \pm i$, ambos con $|\lambda| = 1$. El método de la potencia oscila sin converger.
>
> En este caso, se requieren técnicas como el método de la potencia con desplazamiento o el método QR.

---

## Relación con el método de la potencia

> [!info]
> - Este análisis complementa a [[Metodo Potencia Directo/index]].
> - Para calcular el segundo autovalor $\lambda_2$ una vez conocido $v_1$, se utiliza la técnica de **deflación** (no cubierta en estas notas).
> - Cuando $r$ es cercano a $1$ y se desea acelerar la convergencia, se utiliza el método de la **potencia desplazada**, desarrollado en [[Variantes Metodo Potencia/Potencia Desplazada Aceleracion Convergencia]].

---

## Implicaciones prácticas

> [!info]
> **¿Cómo estimar $r$ sin conocer los autovalores?**
>
> Durante la iteración, la convergencia del cociente de Rayleigh puede monitorearse. Si $\lambda^{(k)}$ se estabiliza lentamente, es señal de que $r \approx 1$.
>
> **Estrategias cuando $r \approx 1$:**
> 1. Usar potencia desplazada (acelera convergencia, véase [[Variantes Metodo Potencia/Potencia Desplazada Aceleracion Convergencia]])
> 2. Usar método de la potencia en la matriz $(A - \mu I)^{-1}$ para targeting
> 3. Cambiar a métodos más robustos como Arnoldi o Lanczos
>
> **Conclusión práctica:**
> - Si $r < 0.5$: convergencia rápida, pocas iteraciones.
> - Si $0.5 \leq r < 0.9$: convergencia moderada.
> - Si $r \geq 0.9$: convergencia lenta, considerar aceleración.

---

## Resumen

> [!corolario]
> La velocidad de convergencia del método de la potencia está determinada por la razón $r = |\lambda_2/\lambda_1|$:
>
> - **Factor de convergencia:** $r = |\lambda_2/\lambda_1|$
> - **Tipo de convergencia:** Lineal
> - **Dígitos por iteración:** $-\log_{10} r$
> - **Iteraciones para $d$ dígitos:** $k \approx d / (-\log_{10} r)$
>
> **Regla práctica:** Si $r = 0.5$, se gana $\approx 0.3$ dígitos por iteración. Si $r = 0.9$, se gana $\approx 0.045$ dígitos por iteración (necesita $\approx 20$ veces más iteraciones que con $r=0.5$).
>
> Para acelerar la convergencia cuando $r \approx 1$, consúltese [[Variantes Metodo Potencia/Potencia Desplazada Aceleracion Convergencia]]. Para la estimación óptima del autovalor durante la iteración, véase [[Calculo Constante Normalizacion Rayleigh]].