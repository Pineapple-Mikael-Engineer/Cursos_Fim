---
title: Fundamentos de las Transformaciones de Householder
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - autovalores
  - metodo-qr
draft: false
aliases:
  - Reflexiones de Householder
  - Householder transformations
  - Factorización QR por Householder
---

# Fundamentos de las Transformaciones de Householder

> [!definicion]
> Una **transformación de Householder** (o reflexión elemental) es una matriz ortogonal de la forma
> $$H = I - 2\,\frac{v v^T}{v^T v},$$
> donde $v \neq 0$ es el **vector de Householder**. Refleja cualquier vector respecto al hiperplano ortogonal a $v$.

> [!info]
> Las reflexiones de Householder son la herramienta estándar para construir la factorización $A = QR$ de forma numéricamente estable, anulando de golpe todas las entradas bajo la diagonal de una columna. Son la primera pieza del [[Metodo QR/index|método QR]] y de la factorización QR usada en [[Ajuste Minimos Cuadrados|mínimos cuadrados]].

---

## Propiedades

> [!proposicion]
> La matriz $H = I - 2vv^T/(v^Tv)$ satisface:
> 1. **Simétrica:** $H^T = H$.
> 2. **Ortogonal:** $H^T H = I$, luego $H^{-1} = H$ (es su propia inversa: una reflexión repetida es la identidad).
> 3. **Involutiva:** $H^2 = I$.
> 4. $\det(H) = -1$ (invierte orientación, como toda reflexión).
> 5. Preserva la norma euclídea: $\|Hx\|_2 = \|x\|_2$.

> [!demostracion]
> **Ortogonalidad.** Con $\beta = 2/(v^Tv)$:
> $$H^T H = (I - \beta vv^T)(I - \beta vv^T) = I - 2\beta vv^T + \beta^2 v(v^Tv)v^T = I - 2\beta vv^T + \beta^2 (v^Tv) vv^T.$$
> Como $\beta^2(v^Tv) = \beta\cdot\beta(v^Tv) = \beta\cdot 2 = 2\beta$, los dos últimos términos se cancelan y $H^TH = I$. La simetría es inmediata porque $vv^T$ es simétrica.

---

## Anulación de una columna

> [!teorema]
> Dado un vector $x \in \mathbb{R}^n$ con $x \neq 0$, existe una reflexión de Householder $H$ tal que
> $$Hx = \mp\|x\|_2\,e_1 = (\mp\|x\|_2,\,0,\,\dots,\,0)^T.$$
> El vector que la genera es
> $$v = x \pm \|x\|_2\, e_1,$$
> y por estabilidad se elige el signo $\operatorname{sgn}(x_1)$ para evitar cancelación:
> $$v = x + \operatorname{sgn}(x_1)\,\|x\|_2\, e_1.$$

> [!demostracion]
> Con $v = x + \alpha e_1$ y $\alpha = \operatorname{sgn}(x_1)\|x\|_2$:
> $$v^T v = \|x\|^2 + 2\alpha x_1 + \alpha^2 = 2\|x\|^2 + 2\alpha x_1 = 2(\|x\|^2 + \alpha x_1),$$
> $$v^T x = \|x\|^2 + \alpha x_1.$$
> Entonces $\beta v^T x = \dfrac{2 v^Tx}{v^Tv} = 1$, de modo que
> $$Hx = x - \beta(v^Tx)v = x - v = -\alpha e_1 = -\operatorname{sgn}(x_1)\|x\|_2\, e_1.$$
> El vector queda alineado con $e_1$, con todas las componentes inferiores anuladas.

> [!warning]
> **Elección del signo.** Si se tomara $\alpha = -\operatorname{sgn}(x_1)\|x\|$, el primer componente $v_1 = x_1 - \operatorname{sgn}(x_1)\|x\|$ restaría cantidades casi iguales cuando $x \approx \|x\|e_1$, provocando [[Perdida Significancia y Cancelacion Catastrofica|cancelación catastrófica]]. El signo $+\operatorname{sgn}(x_1)$ suma magnitudes y mantiene la [[Estabilidad Algoritmos Forward Backward|estabilidad]].

---

## Ejemplo: anular una columna

> [!ejemplo]
> **Reflejar $x = (3, 4)^T$ sobre el eje $e_1$.** Como $\|x\|_2 = 5$ y $x_1 = 3 > 0$:
> $$v = x + 5 e_1 = \begin{pmatrix} 8 \\ 4 \end{pmatrix}, \quad v^Tv = 80.$$
> $$H = I - \frac{2}{80}\begin{pmatrix} 8 \\ 4 \end{pmatrix}\begin{pmatrix} 8 & 4 \end{pmatrix} = \begin{pmatrix} 1-1.6 & -0.8 \\ -0.8 & 1-0.4 \end{pmatrix} = \begin{pmatrix} -0.6 & -0.8 \\ -0.8 & 0.6 \end{pmatrix}.$$
> Verificación:
> $$Hx = \begin{pmatrix} -0.6 & -0.8 \\ -0.8 & 0.6 \end{pmatrix}\begin{pmatrix} 3 \\ 4 \end{pmatrix} = \begin{pmatrix} -5 \\ 0 \end{pmatrix} = -\|x\|_2\, e_1.\ \checkmark$$

---

## Factorización QR por Householder

> [!algoritmo]
> **Triangularización columna a columna.** Para $A \in \mathbb{R}^{m\times n}$, aplicar reflexiones $H_1, \dots, H_n$ que anulan sucesivamente bajo la diagonal:
>
> ```
> R = A
> para j = 1 hasta n:
>     x = R[j:m, j]                       // subcolumna desde la diagonal
>     v = x + sign(x[1]) * ||x|| * e1
>     H_j = I - 2 v vᵀ / (vᵀ v)           // actuando sobre filas j:m
>     R = H_j R                           // anula R[j+1:m, j]
> Q = H_1 H_2 ... H_n                      // producto de reflexiones
> ```
>
> Resulta $A = QR$ con $Q = H_1\cdots H_n$ ortogonal y $R$ triangular superior. Coste $\approx 2n^2(m - n/3)$ flops; para $m=n$, $\frac{4}{3}n^3$.

> [!info]
> **Estabilidad y costo.** La factorización QR por Householder es **incondicionalmente estable hacia atrás** (el $Q$ ortogonal no amplifica errores, $\kappa_2(Q)=1$). Es más cara que [[Eliminacion Gaussiana|Gauss]] ($\frac{2}{3}n^3$) pero más robusta, y no requiere pivoteo para ser estable. En el método QR, $Q$ rara vez se forma explícitamente: se aplican las reflexiones directamente.

---

## Householder frente a Givens

> [!info]
> | | Householder | Givens |
> |:---|:---|:---|
> | Acción | anula una columna entera | anula una entrada |
> | Costo (denso) | menor | mayor |
> | Idóneo para | matrices densas | matrices dispersas / Hessenberg |
> | Tipo | reflexión ($\det=-1$) | rotación ($\det=+1$) |
>
> En el [[Iteracion QR Descomposicion|método QR sobre forma de Hessenberg]] se prefieren rotaciones de Givens porque solo hay una subdiagonal que anular; Householder domina la reducción densa inicial.

---

## Relación con otras notas

> [!info]
> - Uso en el algoritmo de autovalores: [[Iteracion QR Descomposicion]] y [[Metodo QR/index]].
> - La estabilidad que las hace preferibles: [[Estabilidad Algoritmos Forward Backward]].
> - La cancelación que el signo evita: [[Perdida Significancia y Cancelacion Catastrofica]].
> - Aplicación a mínimos cuadrados: [[Ajuste Minimos Cuadrados]] (factorización QR en lugar de ecuaciones normales).

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Definición | $H = I - 2vv^T/(v^Tv)$ |
| Tipo | reflexión ortogonal, simétrica, involutiva |
| Acción | $Hx = -\operatorname{sgn}(x_1)\|x\|_2 e_1$ |
| Vector | $v = x + \operatorname{sgn}(x_1)\|x\|_2 e_1$ |
| Uso | factorización $A = QR$ estable |
| Costo QR | $\frac{4}{3}n^3$ ($m=n$) |

> [!corolario]
> Las transformaciones de Householder son reflexiones ortogonales $H = I - 2vv^T/(v^Tv)$ que anulan de una vez todas las entradas bajo la diagonal de una columna, eligiendo $v = x + \operatorname{sgn}(x_1)\|x\|e_1$ para evitar cancelación. Encadenadas columna a columna producen la factorización $A = QR$ de forma incondicionalmente estable hacia atrás, sin pivoteo. Son el ladrillo ortogonal del [[Metodo QR/index|método QR]] para autovalores y de la resolución estable de [[Ajuste Minimos Cuadrados|mínimos cuadrados]]; su empleo iterado se detalla en [[Iteracion QR Descomposicion]].
