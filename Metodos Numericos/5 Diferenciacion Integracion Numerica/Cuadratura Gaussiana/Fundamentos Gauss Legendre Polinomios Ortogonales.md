---
title: Fundamentos de Gauss-Legendre y Polinomios Ortogonales
order: 1
tags:
  - metodos-numericos
  - teoria
  - diferenciacion-integracion
  - cuadratura-gaussiana
draft: false
aliases:
  - Polinomios de Legendre
  - Fundamentos de Gauss-Legendre
  - Polinomios ortogonales
  - Orthogonal polynomials
---

# Fundamentos de Gauss-Legendre y Polinomios Ortogonales


> [!definicion]
> Los **polinomios de Legendre** $\{P_n\}$ son la familia de polinomios ortogonales en $[-1,1]$ con peso $w(x)=1$:
> $$\int_{-1}^1 P_m(x)P_n(x)\,dx = 0 \quad (m\neq n).$$
> Los **nodos** de la [[Cuadratura Gaussiana/index|cuadratura de Gauss-Legendre]] de orden $n$ son los $n$ ceros de $P_n$.


> [!teoria]
> La ortogonalidad de los polinomios depende del **producto interno** que se utilice. En lugar del producto punto entre vectores, se define
> $$
> \langle p,q\rangle
> =
> \int_a^b p(x)\,q(x)\,w(x)\,dx,
> $$
> donde $w(x)>0$ se denomina **función de peso**.
>
> La función de peso determina qué regiones del intervalo tienen mayor influencia en el producto interno. Si $w(x)$ es grande cerca de cierto punto, los valores de los polinomios en esa zona "pesan más" al medir su ortogonalidad.


> [!info]
> La clave de la cuadratura gaussiana es elegir como nodos los ceros de un polinomio ortogonal. La ortogonalidad es precisamente lo que permite que $n$ nodos integren exactamente polinomios de grado $2n-1$ (ver [[Grado Exactitud Polinomica 2n 1]]).

---

## Polinomios de Legendre

> [!info]
> Primeros polinomios de Legendre (normalizados con $P_n(1)=1$):
>
> | $n$ | $P_n(x)$ | Ceros (nodos de Gauss) |
> |:---:|:---|:---|
> | 0 | $1$ | — |
> | 1 | $x$ | $0$ |
> | 2 | $\frac{1}{2}(3x^2-1)$ | $\pm1/\sqrt3 \approx \pm0.5774$ |
> | 3 | $\frac{1}{2}(5x^3-3x)$ | $0,\ \pm\sqrt{3/5} \approx \pm0.7746$ |
> | 4 | $\frac{1}{8}(35x^4-30x^2+3)$ | $\pm0.3400,\ \pm0.8611$ |
>
> Satisfacen la **recurrencia de tres términos**:
> $$(n+1)P_{n+1}(x) = (2n+1)\,x\,P_n(x) - n\,P_{n-1}(x).$$

---

## Propiedades clave de los polinomios ortogonales

> [!proposicion]
> 1. **Ortogonalidad:** $\int_{-1}^1 P_m P_n\,dx = \frac{2}{2n+1}\delta_{mn}$.
> 2. **Ceros reales y simples:** $P_n$ tiene exactamente $n$ ceros reales distintos, todos en $(-1,1)$.
> 3. **Ortogonalidad a grados menores:** $\int_{-1}^1 P_n(x)\,q(x)\,dx = 0$ para todo polinomio $q$ de grado $< n$.
> 4. **Entrelazado:** los ceros de $P_n$ y $P_{n+1}$ se entrelazan.

> [!demostracion]
> Las cuatro propiedades son consecuencia de la construcción de los polinomios de Legendre como una familia de polinomios ortogonales respecto al producto interno
> $$
> \langle p,q\rangle
> =
> \int_{-1}^{1}p(x)q(x)\,dx.
> $$
>
> **1. Ortogonalidad.**  
> Por definición, cada polinomio $P_n$ se construye ortogonal a todos los de menor grado. En consecuencia,
> $$
> \int_{-1}^{1}P_m(x)P_n(x)\,dx=0,
> \qquad m\neq n.
> $$
> Además, la normalización habitual $P_n(1)=1$ fija la constante
> $$
> \int_{-1}^{1}P_n^2(x)\,dx
> =
> \frac{2}{2n+1},
> $$
> por lo que
> $$
> \int_{-1}^{1}P_mP_n\,dx
> =
> \frac{2}{2n+1}\delta_{mn}.
> $$
>
> **2. Ortogonalidad frente a polinomios de menor grado.**  
> Todo polinomio $q$ con
> $$
> \deg(q)<n
> $$
> puede escribirse como combinación lineal de los primeros polinomios de Legendre:
> $$
> q(x)
> =
> a_0P_0(x)+a_1P_1(x)+\cdots+a_{n-1}P_{n-1}(x).
> $$
> Entonces
> $$
> \int_{-1}^{1}P_n(x)q(x)\,dx
> =
> \sum_{k=0}^{n-1}
> a_k
> \int_{-1}^{1}P_nP_k\,dx
> =
> 0,
> $$
> porque cada integral es nula por la propiedad anterior.
>
> **3. Ceros reales y simples.**  
> Supóngase que $P_n$ tuviera solamente $k<n$ cambios de signo en $(-1,1)$, localizados en
> $$
> r_1,\dots,r_k.
> $$
> Construimos el polinomio
> $$
> q(x)
> =
> \prod_{j=1}^{k}(x-r_j),
> $$
> cuyo grado es $k<n$.
>
> El producto
> $$
> P_n(x)q(x)
> $$
> no cambia de signo en $[-1,1]$, por lo que
> $$
> \int_{-1}^{1}P_n(x)q(x)\,dx\neq0.
> $$
> Esto contradice la propiedad anterior. Luego $P_n$ debe poseer al menos $n$ cambios de signo.
>
> Como $P_n$ tiene grado exactamente $n$, no puede tener más de $n$ raíces. Se concluye que posee exactamente $n$ raíces reales distintas, todas situadas en $(-1,1)$.
>
> **4. Entrelazado de los ceros.**  
> Sean
> $$
> x_1<\cdots<x_n
> $$
> las raíces de $P_n$. Entre dos raíces consecutivas de $P_n$, este polinomio mantiene signo constante.
>
> Si $P_{n+1}$ no tuviera una raíz en alguno de esos intervalos, también conservaría el mismo signo allí. Entonces el producto
> $$
> P_n(x)P_{n+1}(x)
> $$
> mantendría signo constante en dicho intervalo y su integral no podría anularse, contradiciendo la ortogonalidad
> $$
> \int_{-1}^{1}P_nP_{n+1}\,dx=0.
> $$
> Por tanto, entre cada par de raíces consecutivas de $P_n$ debe existir exactamente una raíz de $P_{n+1}$. Como $P_{n+1}$ posee una raíz adicional, ésta se sitúa cerca de cada extremo del intervalo, obteniéndose el entrelazado de las raíces.

---

## Por qué los ceros ortogonales son óptimos

> [!teoria]
> Sea $p(x)$ un polinomio de grado $\leq 2n-1$. Dividiéndolo por $P_n$: $p = q\,P_n + r$, con $q, r$ de grado $\leq n-1$. Entonces
> $$\int_{-1}^1 p\,dx = \underbrace{\int_{-1}^1 q P_n\,dx}_{=0\ \text{(ortogonalidad)}} + \int_{-1}^1 r\,dx = \int_{-1}^1 r\,dx.$$
> El término con $P_n$ **se anula** por ortogonalidad. Y en los nodos $x_i$ (ceros de $P_n$), $p(x_i) = r(x_i)$ porque $P_n(x_i)=0$. Como una regla con $n$ nodos integra exactamente $r$ (grado $\leq n-1$), integra exactamente $p$ (grado $\leq 2n-1$). Esta es la idea central, formalizada en [[Grado Exactitud Polinomica 2n 1]].

---

## Ejemplo

> [!ejemplo]
> **Verificar ortogonalidad $P_1 \perp P_2$:**
> $$\int_{-1}^1 P_1 P_2\,dx = \int_{-1}^1 x\cdot\tfrac{1}{2}(3x^2-1)\,dx = \tfrac{1}{2}\int_{-1}^1 (3x^3 - x)\,dx = \tfrac{1}{2}\cdot 0 = 0,$$
> pues el integrando es impar. Los ceros de $P_2$, $\pm1/\sqrt3$, son los nodos de Gauss de 2 puntos.

---

## Otras familias (otras funciones de peso)

> [!info]
> Cada función de peso $w(x)$ y dominio define una familia ortogonal y su cuadratura:
>
> | Familia | Intervalo | Peso $w(x)$ | Uso |
> |:---|:---|:---|:---|
> | Legendre | $[-1,1]$ | $1$ | integrales generales |
> | Chebyshev | $[-1,1]$ | $1/\sqrt{1-x^2}$ | integrandos con singularidad en bordes |
> | Laguerre | $[0,\infty)$ | $e^{-x}$ | integrales semiinfinitas |
> | Hermite | $(-\infty,\infty)$ | $e^{-x^2}$ | integrales con peso gaussiano |
>
> La construcción es idéntica: nodos = ceros del polinomio ortogonal de la familia.

---

## Relación con otras notas

> [!info]
> - El cálculo concreto de nodos y pesos: [[Determinacion Nodos y Pesos Optimos]].
> - La demostración del grado $2n-1$: [[Grado Exactitud Polinomica 2n 1]].
> - El traslado a $[a,b]$: [[Cambio Variable Intervalo General]].
> - El contraste con nodos fijos: [[Formulacion General Pesos Newton Cotes]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Nodos de Gauss | ceros de $P_n$ |
| Ortogonalidad | $\int_{-1}^1 P_m P_n = \frac{2}{2n+1}\delta_{mn}$ |
| Ceros | $n$ reales, simples, en $(-1,1)$ |
| Recurrencia | $(n+1)P_{n+1} = (2n+1)xP_n - nP_{n-1}$ |
| Idea clave | división por $P_n$ + ortogonalidad anula medio polinomio |

> [!corolario]
> Los nodos de la cuadratura de Gauss-Legendre son los ceros de los polinomios de Legendre, la familia ortogonal en $[-1,1]$. La ortogonalidad —$\int P_n q = 0$ para $q$ de grado menor— es lo que hace óptimos esos nodos: al dividir cualquier polinomio de grado $\leq 2n-1$ por $P_n$, la parte con $P_n$ se anula y solo queda un resto de grado $\leq n-1$ que $n$ nodos integran exactamente. Sus ceros son reales, simples e interiores, calculables por la [[Determinacion Nodos y Pesos Optimos|recurrencia de tres términos]], y la misma construcción con otras funciones de peso (Chebyshev, Laguerre, Hermite) genera cuadraturas para dominios e integrandos especiales.
