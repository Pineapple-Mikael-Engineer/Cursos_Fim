---
title: Convergencia y Desplazamientos
order: 3
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - autovalores
  - metodo-qr
  - convergencia
draft: false
aliases:
  - Desplazamientos QR
  - QR shifts
  - Shift de Wilkinson
  - Convergencia del método QR
---

# Convergencia y Desplazamientos del Método QR

> [!definicion]
> Un **desplazamiento** (*shift*) en el [[Iteracion QR Descomposicion|método QR]] es un escalar $\mu_k$ que se resta antes de factorizar y se vuelve a sumar tras recomponer:
> $$A_k - \mu_k I = Q_k R_k, \qquad A_{k+1} = R_k Q_k + \mu_k I.$$
> Elegir $\mu_k$ cercano a un autovalor acelera la convergencia de lineal a **cuadrática** (o cúbica en el caso simétrico).

> [!info]
> Sin desplazamiento, la subdiagonal $(A_k)_{i+1,i}$ decae como $|\lambda_{i+1}/\lambda_i|^k$, intolerablemente lento cuando dos autovalores están próximos. El desplazamiento manipula esa razón para forzar un decaimiento rápido del último elemento subdiagonal, aislando un autovalor por vez.

---

## Por qué el desplazamiento acelera

> [!teorema]
> Con desplazamiento $\mu_k$, la entrada subdiagonal que conduce a la deflación decae según la razón de las distancias al desplazamiento:
> $$|(A_{k+1})_{n,n-1}| \approx \left|\frac{\lambda_n - \mu_k}{\lambda_{n-1} - \mu_k}\right|\,|(A_k)_{n,n-1}|.$$
> Si $\mu_k \to \lambda_n$, el numerador $|\lambda_n - \mu_k| \to 0$ y la convergencia se vuelve superlineal.

> [!demostracion]
> La iteración QR desplazada equivale a aplicar [[Potencia Inversa Valor Propio Menor Modulo|potencia inversa]] con desplazamiento $\mu_k$ a la última columna. El factor de convergencia de la potencia inversa desplazada es el cociente entre la distancia del autovalor objetivo al *shift* y la del siguiente autovalor más cercano:
> $$r_k = \left|\frac{\lambda_n - \mu_k}{\lambda_{n-1} - \mu_k}\right|.$$
> Cuando $\mu_k$ se aproxima a $\lambda_n$ en cada paso (desplazamiento adaptativo), $r_k \to 0$ y el producto $\prod_k r_k$ colapsa: la convergencia deja de ser geométrica de razón fija y pasa a cuadrática.

---

## Estrategias de desplazamiento

> [!info]
> | Estrategia | Desplazamiento $\mu_k$ | Convergencia |
> |:---|:---|:---|
> | Sin desplazamiento | $0$ | lineal, razón $|\lambda_n/\lambda_{n-1}|$ |
> | Desplazamiento de Rayleigh | $\mu_k = (A_k)_{nn}$ | cuadrática (genérico) |
> | Desplazamiento de Wilkinson | autovalor del bloque $2\times2$ inferior derecho más próximo a $(A_k)_{nn}$ | cuadrática global, robusto |
> | Doble desplazamiento (Francis) | par conjugado, en aritmética **real** | cuadrática, captura autovalores complejos |

> [!teoria]
> El **desplazamiento de Wilkinson** toma como $\mu_k$ el autovalor del bloque inferior derecho
> $$\begin{pmatrix} (A_k)_{n-1,n-1} & (A_k)_{n-1,n} \\ (A_k)_{n,n-1} & (A_k)_{n,n} \end{pmatrix}$$
> más cercano a $(A_k)_{nn}$. A diferencia del desplazamiento de Rayleigh, no falla ante autovalores de igual módulo (como $\pm\lambda$) y garantiza convergencia incluso en casos simétricos con espectro simétrico.

---

## El doble desplazamiento de Francis

> [!warning]
> Para una matriz **real** con autovalores complejos, un desplazamiento real no puede converger a ellos. El **doble desplazamiento implícito de Francis** aplica simultáneamente el par conjugado $\mu_k, \bar\mu_k$ sin salir de la aritmética real, combinando dos pasos QR en uno mediante el *bulge chasing* sobre la forma de Hessenberg. Es el algoritmo realmente implementado en LAPACK (`dhseqr`).

---

## Deflación

> [!teoria]
> Cuando una entrada subdiagonal se vuelve despreciable,
> $$|(A_k)_{i+1,i}| \leq \texttt{tol}\,\big(|(A_k)_{ii}| + |(A_k)_{i+1,i+1}|\big),$$
> se fija a cero y la matriz se **parte** en dos bloques que se procesan por separado. Cada deflación aísla un autovalor (bloque $1\times1$) o un par complejo (bloque $2\times2$), reduciendo el tamaño del problema activo. Con desplazamientos, suelen bastar $2$–$3$ iteraciones por autovalor.

---

## Ejemplo: aceleración medida

> [!ejemplo]
> **Comparación sobre $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$** (autovalores $3, 1$). Última entrada subdiagonal $(A_k)_{21}$:
>
> | $k$ | Sin desplazamiento | Con desplazamiento de Rayleigh |
> |:---:|:---:|:---:|
> | 0 | 1.000 | 1.000 |
> | 1 | 0.600 | 0.143 |
> | 2 | 0.213 | $3.1\times10^{-3}$ |
> | 3 | 0.071 | $1.5\times10^{-8}$ |
> | 4 | 0.024 | $\approx 10^{-16}$ |
>
> El desplazamiento lleva la subdiagonal a precisión de máquina en $3$–$4$ pasos (convergencia cuadrática: los exponentes se duplican), frente al decaimiento geométrico lento $(1/3)^k$ sin desplazamiento.

---

## Costo global del método QR

> [!info]
> Con reducción a Hessenberg y desplazamientos, el costo total para **todos** los autovalores es:
>
> | Operación | Costo |
> |:---|:---|
> | Reducción a Hessenberg (una vez) | $\frac{10}{3}n^3$ |
> | Iteración QR (≈ $2$–$3$ pasos/autovalor, $O(n^2)$ c/u) | $O(n^3)$ |
> | **Total autovalores** | $\sim 10\,n^3$ |
> | + autovectores (acumular $Q$) | $\sim 25\,n^3$ |
>
> Para matrices simétricas (tridiagonales), el costo baja a $O(n^2)$ para los autovalores. Esto convierte al QR desplazado en el método de referencia frente a la [[Velocidad Convergencia Razon Lambda2 Lambda1|lentitud]] del método de la potencia cuando se requiere el espectro completo.

---

## Relación con otras notas

> [!info]
> - La iteración base sobre la que actúa el desplazamiento: [[Iteracion QR Descomposicion]].
> - La conexión con la potencia inversa desplazada: [[Potencia Inversa Valor Propio Menor Modulo]] y [[Potencia Desplazada Aceleracion Convergencia]].
> - La aceleración cúbica análoga en el caso simétrico (RQI): [[Caso Simetrico Convergencia Acelerada]].
> - Panorama del algoritmo: [[Metodo QR/index]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Paso desplazado | $A_k - \mu_k I = Q_kR_k$, $A_{k+1} = R_kQ_k + \mu_k I$ |
| Factor de convergencia | $|\lambda_n - \mu_k|/|\lambda_{n-1} - \mu_k|$ |
| Rayleigh | $\mu_k = (A_k)_{nn}$, cuadrático |
| Wilkinson | autovalor del bloque $2\times2$, robusto |
| Francis (doble) | par conjugado real, captura complejos |
| Costo total | $\sim 10\,n^3$ (todos los autovalores) |

> [!corolario]
> Los desplazamientos transforman el método QR de un algoritmo de convergencia lineal —razón $|\lambda_{i+1}/\lambda_i|$— en uno de convergencia cuadrática, restando $\mu_k \approx \lambda_n$ para colapsar el factor $|\lambda_n-\mu_k|/|\lambda_{n-1}-\mu_k|$. Las estrategias de Wilkinson y el doble desplazamiento de Francis garantizan robustez incluso ante autovalores de igual módulo o complejos, y la deflación va aislando el espectro bloque a bloque. Con todo ello, el QR desplazado calcula todos los autovalores en $\sim10\,n^3$ operaciones y es el algoritmo estándar de las bibliotecas numéricas, cerrando el estudio del [[Metodo QR/index|método QR]].
