---
title: Generadores de Grupos Continuos
order: 1
tags:
  - analisis-tensorial
  - teoria
  - teoria-grupos
  - generadores
draft: false
aliases:
  - generadores de grupos de Lie
  - grupos de Lie
  - algebra de Lie
  - constantes de estructura
  - generators of continuous groups
  - Lie algebra
---

# Generadores de Grupos Continuos $\mathsf{R}=\exp(i\varepsilon\mathsf{S})$

> [!definicion]
> Un **grupo de Lie** es un grupo continuo cuyos parámetros son funciones analíticas. La idea de Lie es estudiar los elementos $\mathsf{R}$ cercanos a la identidad mediante la **representación exponencial**
> $$\mathsf{R}=\exp(i\varepsilon\mathsf{S}),\qquad \varepsilon\to0,$$
> donde las matrices $\mathsf{S}$ son los **generadores** del grupo. Forman un espacio lineal cuya dimensión es el **orden** del grupo. La estructura del grupo queda codificada en la **relación de clausura** $[\mathsf{S}_i,\mathsf{S}_j]=\sum_k c_{ij}^k\mathsf{S}_k$.

> [!info]
> Sección 7.2 del [[index | capítulo 7]] (libro, cap. 7.2). Es la herramienta central: reduce el estudio de un grupo continuo completo al de sus generadores cerca de la [[index | unidad]]. Da la conexión con el [[Momento Angular Orbital | momento angular]] (sus generadores son $L_x,L_y,L_z$) y organiza la física de partículas vía $SU(2)$ (spin, isospin) y $SU(3)$ (sabor). Las matrices base son [[6 Determinantes y Matrices/Matrices Ortogonales | ortogonales]] o [[6 Determinantes y Matrices/Matrices Hermiticas y Unitarias | unitarias]].

---

## Ejemplo

> [!ejemplo]
> **Obtener el generador $\mathsf{S}_z$ de las rotaciones en torno a $z$.** Las rotaciones de $SO(3)$ sobre el eje $z$ son
> $$\mathsf{R}_z(\varphi)=\begin{pmatrix}\cos\varphi&\operatorname{sen}\varphi&0\\-\operatorname{sen}\varphi&\cos\varphi&0\\0&0&1\end{pmatrix}.$$
> El generador se obtiene **derivando** la matriz en la identidad $\varphi=0$ (con un factor $-i$ que lo vuelve Hermítico):
> $$\mathsf{S}_z=-i\,\frac{d\mathsf{R}_z(\varphi)}{d\varphi}\bigg|_{\varphi=0}.$$
> **Paso 1 — derivar.** Entrada a entrada,
> $$\frac{d\mathsf{R}_z}{d\varphi}=\begin{pmatrix}-\operatorname{sen}\varphi&\cos\varphi&0\\-\cos\varphi&-\operatorname{sen}\varphi&0\\0&0&0\end{pmatrix}.$$
> **Paso 2 — evaluar en $\varphi=0$** ($\operatorname{sen}0=0$, $\cos0=1$):
> $$\frac{d\mathsf{R}_z}{d\varphi}\bigg|_{0}=\begin{pmatrix}0&1&0\\-1&0&0\\0&0&0\end{pmatrix}.$$
> **Paso 3 — multiplicar por $-i$:**
> $$\mathsf{S}_z=-i\begin{pmatrix}0&1&0\\-1&0&0\\0&0&0\end{pmatrix}=\begin{pmatrix}0&-i&0\\i&0&0\\0&0&0\end{pmatrix}.$$
> **Comprobación:** $\operatorname{tr}(\mathsf{S}_z)=0$ (porque $\det\mathsf{R}=1$) y $\mathsf{S}_z^\dagger=\mathsf{S}_z$ (porque $\mathsf{R}$ es unitaria). Reexponenciando se recupera $\mathsf{R}_z(\varphi)=\exp(i\varphi\mathsf{S}_z)$. Análogamente, derivando $\mathsf{R}_x(\psi)$ y $\mathsf{R}_y(\theta)$ se obtienen
> $$\mathsf{S}_x=\begin{pmatrix}0&0&0\\0&0&-i\\0&i&0\end{pmatrix},\qquad \mathsf{S}_y=\begin{pmatrix}0&0&-i\\0&0&0\\i&0&0\end{pmatrix}.$$

---

## En qué consiste

> [!teoria]
> La naturaleza analítica de un grupo de Lie permite reconstruir todo el grupo desde la vecindad de la identidad. Para $\mathsf{R}$ cerca de $\mathsf{1}$ se escribe $\mathsf{R}=\exp(i\varepsilon\mathsf{S})$ con $\varepsilon\to0$: la multiplicación de elementos $\mathsf{R}$ se traduce en la **suma** de los generadores $\mathsf{S}$ (igual que $\mathsf{R}(\varphi_2)\mathsf{R}(\varphi_1)=\mathsf{R}(\varphi_1+\varphi_2)$ en $SO(2)$). El número de generadores linealmente independientes es el **orden** del grupo.

> [!proposicion] Restricciones sobre los generadores
> | Condición sobre $\mathsf{R}$ | Restricción sobre $\mathsf{S}$ | Razón |
> |:---|:---|:---|
> | $\det\mathsf{R}=1$ (volumen) | traza nula, $\operatorname{tr}(\mathsf{S})=0$ | $\det\mathsf{R}=\exp(i\varepsilon\operatorname{tr}\mathsf{S})=1$ |
> | $\mathsf{R}$ unitaria, $\mathsf{R}^\dagger\mathsf{R}=\mathsf{1}$ | Hermítica, $\mathsf{S}^\dagger=\mathsf{S}$ | el factor $i$ de la exponencial |
>
> Ambas valen para $SO(n)$ y $SU(n)$.

---

> [!teorema] Relación de clausura y álgebra de Lie
> Los conmutadores de los generadores se cierran sobre el propio conjunto de generadores:
> $$[\mathsf{S}_i,\mathsf{S}_j]=\sum_k c_{ij}^k\,\mathsf{S}_k,$$
> con $c_{ij}^k$ las **constantes de estructura** del grupo, **antisimétricas** en los índices inferiores, $c_{ij}^k=-c_{ji}^k$. Tomado como regla de multiplicación, el conmutador convierte el espacio de generadores en un **álgebra de Lie**.

> [!demostracion]
> **Paso 1 — expandir a segundo orden.** Para dos generadores $\mathsf{S}_i,\mathsf{S}_j$ con parámetros pequeños $\varepsilon_i,\varepsilon_j$,
> $$\mathsf{R}_i=\exp(i\varepsilon_i\mathsf{S}_i)=\mathsf{1}+i\varepsilon_i\mathsf{S}_i-\tfrac12\varepsilon_i^2\mathsf{S}_i^2+\cdots,\qquad \mathsf{R}_i^{-1}=\mathsf{1}-i\varepsilon_i\mathsf{S}_i-\tfrac12\varepsilon_i^2\mathsf{S}_i^2+\cdots,$$
> y análogamente para $\mathsf{R}_j$. Se retiene hasta segundo orden porque los términos lineales y varios cuadráticos se cancelan en el producto.
>
> **Paso 2 — formar el producto conmutador de grupo.** Multiplicando $\mathsf{R}_i^{-1}\mathsf{R}_j^{-1}\mathsf{R}_i\mathsf{R}_j$ y conservando los términos de orden $\varepsilon_i\varepsilon_j$, los términos en $\varepsilon_i^2$ y $\varepsilon_j^2$ se cancelan y sobrevive el conmutador:
> $$\mathsf{R}_i^{-1}\mathsf{R}_j^{-1}\mathsf{R}_i\mathsf{R}_j=\mathsf{1}+\varepsilon_i\varepsilon_j\,[\mathsf{S}_j,\mathsf{S}_i]+\cdots.$$
>
> **Paso 3 — usar la clausura del grupo.** El producto de cuatro elementos del grupo es de nuevo un elemento $\mathsf{R}_{ij}$ cercano a la unidad. Por tanto su parte no trivial debe ser una **combinación lineal de los generadores** $\mathsf{S}_k$ con coeficiente proporcional a $\varepsilon_i\varepsilon_j$:
> $$\mathsf{R}_i^{-1}\mathsf{R}_j^{-1}\mathsf{R}_i\mathsf{R}_j=\mathsf{1}+\varepsilon_i\varepsilon_j\sum_k c_{ji}^k\,\mathsf{S}_k+\cdots.$$
>
> **Paso 4 — comparar.** Igualando los coeficientes de $\varepsilon_i\varepsilon_j$ de los Pasos 2 y 3 se obtiene la relación de clausura $[\mathsf{S}_i,\mathsf{S}_j]=\sum_k c_{ij}^k\mathsf{S}_k$. $\blacksquare$

> [!corolario] Identidad de Jacobi
> Los conmutadores satisfacen la **identidad de Jacobi**
> $$[[\mathsf{S}_i,\mathsf{S}_j],\mathsf{S}_k]+[[\mathsf{S}_j,\mathsf{S}_k],\mathsf{S}_i]+[[\mathsf{S}_k,\mathsf{S}_i],\mathsf{S}_j]=0,$$
> verificable directamente desde la definición de conmutador. Sustituyendo la clausura se obtiene una restricción adicional sobre las constantes de estructura, $\sum_m\{c_{ij}^m c_{mk}^n+c_{jk}^m c_{mi}^n+c_{ki}^m c_{mj}^n\}=0$. Las relaciones de clausura, antisimetría y Jacobi son la base desde la que se reconstruye el grupo de Lie cerca de su unidad.

---

> [!teoria] La aplicación a la mecánica cuántica
> Expandiendo $\mathsf{H}_R=\exp(i\varepsilon\mathsf{S})\,\mathsf{H}\exp(-i\varepsilon\mathsf{S})=\mathsf{H}+i\varepsilon[\mathsf{S},\mathsf{H}]+\cdots$ (fórmula de Baker–Hausdorff) y dividiendo por $\varepsilon\to0$, la invariancia $\mathsf{H}_R=\mathsf{H}$ implica para cualquier elemento cercano a la unidad
> $$[\mathsf{S},\mathsf{H}]=0.$$
> Si la simetría $\mathsf{S}$ **conmuta con el Hamiltoniano** $\mathsf{H}$, ambos se pueden **diagonalizar simultáneamente**: comparten autofunciones, y los **autovalores degenerados** de $\mathsf{H}$ se distinguen por los de $\mathsf{S}$. Esta es la aplicación más importante de la teoría de grupo a la mecánica cuántica.

---

## $SO(3)$: rotaciones y momento angular

> [!info]
> El grupo $SO(3)$ (rotaciones reales en 3D, $\det=+1$) tiene **orden 3**: sus generadores son $\mathsf{S}_x,\mathsf{S}_y,\mathsf{S}_z$ (obtenidos en el Ejemplo), con $\mathsf{R}_z(\varphi)=\exp(i\varphi\mathsf{S}_z)$. Rotando funciones en vez de coordenadas, las componentes del momento angular orbital $\vec L$ son los generadores, $\mathsf{R}_z(\varphi)=\exp(-i\varphi L_z)$, y satisfacen la misma álgebra:
> $$[L_i,L_j]=i\varepsilon_{ijk}L_k.$$
> Las constantes de estructura de $SO(3)$ son $c_{ij}^k=i\varepsilon_{ijk}$. El detalle de los operadores de subida/bajada se desarrolla en [[Momento Angular Orbital]].

---

## $SU(2)$ y el homomorfismo con $SO(3)$

> [!info]
> $SU(2)$ (matrices unitarias $2\times2$ con $\det=+1$) tiene **orden 3**: sus generadores son la mitad de las tres matrices de Pauli, $s_i=\sigma_i/2$. Satisfacen la **misma álgebra** que $SO(3)$:
> $$[s_i,s_j]=i\varepsilon_{ijk}s_k.$$
> Los elementos se generan como $\mathsf{U}_z(\alpha/2)=\exp(i\alpha\sigma_3/2)$, etc.

> [!proposicion] Homomorfismo $SU(2)\to SO(3)$ de 2 a 1
> La transformación unitaria $\mathsf{U}_z(\alpha/2)$ deja invariante $x^2+y^2+z^2$, luego describe una rotación: corresponde a $\mathsf{R}_z(\alpha)$ de $SO(3)$. La correspondencia **no** es uno a uno: mientras $\alpha$ recorre $0$ a $2\pi$ en $\mathsf{R}_z$, el parámetro $\alpha/2$ solo llega a $\pi$. Como
> $$\mathsf{U}_z(\alpha/2+\pi)=-\mathsf{U}_z(\alpha/2),$$
> tanto $\mathsf{U}_z(\alpha/2)$ como $-\mathsf{U}_z(\alpha/2)$ corresponden a la **misma** rotación $\mathsf{R}_z(\alpha)$. La correspondencia es de **2 a 1**: $SU(2)$ y $SO(3)$ son homomorfos. Por ello las representaciones conocidas de $SU(2)$ dan automáticamente las de $SO(3)$.

---

## $SU(3)$: el octeto de sabor

> [!info]
> $SU(3)$ (matrices unitarias $3\times3$ con $\det=+1$) tiene **orden 8**: sus generadores son las 8 **matrices de Gell-Mann** $\lambda_i$, Hermíticas $3\times3$ de traza nula. Tres de ellas contienen las matrices de Pauli del isospin en la esquina superior izquierda, $\lambda_i=\begin{pmatrix}\tau_i&0\\0&0\end{pmatrix}$. Es de **rango 2**: hay dos generadores que conmutan ($I_3$ e $Y$, con $[I_3,Y]=0$), simultáneamente diagonalizables.

> [!ejemplo]
> ![[octeto_bariones.svg|460]]
>
> **Simetría de sabor $SU(3)$ (Gell-Mann, 1961).** Los bariones de spin $\tfrac12$ se organizan, según los números cuánticos conservados **hipercarga** $Y$ e **isospin** $I_3$ (los análogos de $L^2$ y $L_z$ de $SO(3)$), en un **octeto** de ocho partículas aproximadamente degeneradas en masa:
> $$N(p,n),\quad \Sigma(\Sigma^+,\Sigma^0,\Sigma^-),\quad \Lambda,\quad \Xi(\Xi^0,\Xi^-).$$
> Independientemente, Ne'eman llegó al mismo esquema; la representación de 8 dimensiones de $SU(3)$ aloja exactamente estos bariones. El éxito predictivo de la simetría (la posterior predicción del $\Omega^-$) confirmó $SU(3)$ como la **simetría de sabor** de las interacciones fuertes.
>
> Octeto bariónico de spin 1/2: las 8 partículas en el plano hipercarga $Y$ vs isospin $I_3$, organizadas por la simetría $SU(3)$.

> [!info] Bariones del octeto (cuadro 7.1)
> | Multiplete | Partículas | $Y$ | $I$ | $I_3$ |
> |:---|:---|:---:|:---:|:---|
> | $\Xi$ | $\Xi^-,\ \Xi^0$ | $-1$ | $\tfrac12$ | $-\tfrac12,\ +\tfrac12$ |
> | $\Sigma$ | $\Sigma^-,\Sigma^0,\Sigma^+$ | $0$ | $1$ | $-1,\ 0,\ +1$ |
> | $\Lambda$ | $\Lambda$ | $0$ | $0$ | $0$ |
> | $N$ | $n,\ p$ | $+1$ | $\tfrac12$ | $-\tfrac12,\ +\tfrac12$ |

---

## Resumen

> [!resumen]
> | Grupo | Orden | Generadores | Álgebra | Física |
> |:---|:---:|:---|:---|:---|
> | $SO(3)$ | 3 | $\mathsf{S}_x,\mathsf{S}_y,\mathsf{S}_z$ | $[L_i,L_j]=i\varepsilon_{ijk}L_k$ | rotaciones, momento angular |
> | $SU(2)$ | 3 | $s_i=\sigma_i/2$ | $[s_i,s_j]=i\varepsilon_{ijk}s_k$ | spin $\tfrac12$, isospin |
> | $SU(3)$ | 8 | $\lambda_i$ (Gell-Mann) | rango 2 | sabor, octeto bariónico |
>
> Reglas generales: $\det\mathsf{R}=1\Rightarrow\operatorname{tr}(\mathsf{S})=0$; $\mathsf{R}$ unitaria $\Rightarrow\mathsf{S}^\dagger=\mathsf{S}$; clausura $[\mathsf{S}_i,\mathsf{S}_j]=\sum_k c_{ij}^k\mathsf{S}_k$ con $c_{ij}^k=-c_{ji}^k$.

> [!corolario]
> Un grupo de Lie se reconstruye desde sus **generadores**: las matrices $\mathsf{S}$ cerca de la identidad, organizadas por la relación de clausura en un **álgebra de Lie**. La misma álgebra $[s_i,s_j]=i\varepsilon_{ijk}s_k$ une $SO(3)$ y $SU(2)$ (homomorfos de 2 a 1), y su generalización $SU(3)$ organiza la materia en multipletes. El puente con la física es $[\mathsf{S},\mathsf{H}]=0$: cada simetría que conmuta con el Hamiltoniano etiqueta sus estados degenerados, y así la teoría de grupo se vuelve el idioma de las leyes de conservación.

> [!referencia]
> - Operadores de subida/bajada y $J^2=J(J+1)$: [[Momento Angular Orbital]].
> - Análogo no compacto (boosts con generador imaginario): [[Grupo Homogeneo de Lorentz]].
> - Matrices base: [[6 Determinantes y Matrices/Matrices Ortogonales]] · [[6 Determinantes y Matrices/Matrices Hermiticas y Unitarias]].
> - Marco del capítulo: [[index | Teoría de Grupo]].
