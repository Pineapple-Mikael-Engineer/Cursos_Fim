---
title: Diagonalizacion de Matrices
order: 5
tags:
  - analisis-tensorial
  - teoria
  - matrices
  - diagonalizacion
  - autovalores
draft: false
aliases:
  - diagonalizacion de matrices
  - transformacion de semejanza
  - similaridad
  - ecuacion secular
  - matrix diagonalization
---

# Diagonalizacion de Matrices

> [!definicion]
> **Diagonalizar** una matriz $\mathsf{A}$ es hallar una **transformación de semejanza**
> $$\mathsf{A}'=\mathsf{S}^{-1}\mathsf{A}\,\mathsf{S}$$
> que la lleve a forma diagonal $\mathsf{A}'=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$. Las columnas de $\mathsf{S}$ son los **autovectores** de $\mathsf{A}$ y la diagonal de $\mathsf{A}'$ son sus **autovalores** $\lambda_k$, raíces de la **ecuación característica** (o secular) $\det(\mathsf{A}-\lambda\mathsf{1})=0$.

> [!info]
> Sección **6.5** del [[index | capítulo 6]] (libro, cap. 6.5). Es la versión **matricial** del mismo problema que la versión geométrica (tensores, ejes principales) de [[../4 Introduccion a Tensores/Diagonalizacion de Tensores/index | Diagonalización de Tensores]]: allí se diagonaliza un tensor $\overleftrightarrow{\sigma}$ por rotación de la base; aquí se diagonaliza la matriz $\mathsf{A}$ por semejanza. El cálculo de autovalores/autovectores ya está en [[../4 Introduccion a Tensores/Diagonalizacion de Tensores/Valores y Vectores Propios | Valores y Vectores Propios]]. Para matrices **simétricas** la $\mathsf{S}$ es [[Matrices Ortogonales | ortogonal]]; para **Hermíticas**, [[Matrices Hermiticas y Unitarias | unitaria]].

---

## Ejemplo

> [!ejemplo] Diagonalizar una matriz simétrica $2\times2$
> Sea la matriz real **simétrica** ($\mathsf{A}=\tilde{\mathsf{A}}$)
> $$\mathsf{A}=\begin{pmatrix}2&1\\1&2\end{pmatrix}.$$
> Esperamos autovalores reales y autovectores ortonormales, luego una $\mathsf{S}$ **ortogonal**.
>
> **Paso 1 — Ecuación característica.** Imponemos $\det(\mathsf{A}-\lambda\mathsf{1})=0$:
> $$\begin{vmatrix}2-\lambda&1\\1&2-\lambda\end{vmatrix}=(2-\lambda)^2-1=0.$$
>
> **Paso 2 — Autovalores.** $(2-\lambda)^2=1$ da $2-\lambda=\pm1$, es decir
> $$\lambda_1=1,\qquad \lambda_2=3.$$
> La traza $2+2=4=\lambda_1+\lambda_2$ y el determinante $4-1=3=\lambda_1\lambda_2$ ya confirman las raíces.
>
> **Paso 3 — Autovector de $\lambda_1=1$.** Resolvemos $(\mathsf{A}-\mathsf{1})v=0$:
> $$\begin{pmatrix}1&1\\1&1\end{pmatrix}\begin{pmatrix}v_1\\v_2\end{pmatrix}=0\ \Rightarrow\ v_1+v_2=0\ \Rightarrow\ v=\frac1{\sqrt2}\begin{pmatrix}1\\-1\end{pmatrix}.$$
>
> **Paso 4 — Autovector de $\lambda_2=3$.** Resolvemos $(\mathsf{A}-3\mathsf{1})v=0$:
> $$\begin{pmatrix}-1&1\\1&-1\end{pmatrix}\begin{pmatrix}v_1\\v_2\end{pmatrix}=0\ \Rightarrow\ v_1-v_2=0\ \Rightarrow\ v=\frac1{\sqrt2}\begin{pmatrix}1\\1\end{pmatrix}.$$
> Los dos autovectores son **ortogonales** (producto punto $\tfrac12(1-1)=0$), como garantiza la simetría.
>
> **Paso 5 — Matriz de semejanza.** Colocamos los autovectores **como columnas**:
> $$\mathsf{S}=\frac1{\sqrt2}\begin{pmatrix}1&1\\-1&1\end{pmatrix},\qquad \mathsf{S}^{-1}=\tilde{\mathsf{S}}=\frac1{\sqrt2}\begin{pmatrix}1&-1\\1&1\end{pmatrix},$$
> que es **ortogonal** ($\mathsf{S}^{-1}=\tilde{\mathsf{S}}$, pues sus columnas son ortonormales).
>
> **Paso 6 — Verificación.** Calculamos $\mathsf{A}'=\mathsf{S}^{-1}\mathsf{A}\,\mathsf{S}$:
> $$\mathsf{S}^{-1}\mathsf{A}\,\mathsf{S}=\frac12\begin{pmatrix}1&-1\\1&1\end{pmatrix}\begin{pmatrix}2&1\\1&2\end{pmatrix}\begin{pmatrix}1&1\\-1&1\end{pmatrix}=\begin{pmatrix}1&0\\0&3\end{pmatrix}=\operatorname{diag}(\lambda_1,\lambda_2).$$
> En la base de los autovectores, $\mathsf{A}$ es diagonal y sus elementos son los autovalores.

---

## En qué consiste

> [!teoria]
> Una **transformación de semejanza** $\mathsf{A}'=\mathsf{S}^{-1}\mathsf{A}\,\mathsf{S}$ es un **cambio de base**: $\mathsf{A}$ y $\mathsf{A}'$ representan **el mismo operador lineal** en bases distintas. Diagonalizar es elegir la base —la de los autovectores— en la que el operador solo **escala** cada eje por su autovalor, sin mezclarlos. Por eso las cantidades que no dependen de la base (autovalores, traza, determinante) **se conservan**: son **invariantes** de semejanza. Para matrices simétricas reales la nueva base puede tomarse **ortonormal**, y entonces $\mathsf{S}$ es ortogonal ($\mathsf{S}^{-1}=\tilde{\mathsf{S}}$); para Hermíticas, unitaria ($\mathsf{S}^{-1}=\mathsf{S}^\dagger$).

> [!teorema] Ecuación característica (secular)
> Los autovalores de $\mathsf{A}$ son las raíces de
> $$\det(\mathsf{A}-\lambda\mathsf{1})=0,$$
> un polinomio de grado $n$ en $\lambda$. Para cada raíz $\lambda_k$, el autovector $v_k$ resuelve el sistema homogéneo $(\mathsf{A}-\lambda_k\mathsf{1})v_k=0$. Si los $n$ autovectores son linealmente independientes, la matriz $\mathsf{S}=(v_1\ v_2\ \cdots\ v_n)$ (autovectores por columnas) cumple $\mathsf{S}^{-1}\mathsf{A}\,\mathsf{S}=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$.

> [!demostracion] La semejanza conserva los autovalores
> **Paso 1 — Punto de partida.** Sea $v$ autovector de $\mathsf{A}$ con autovalor $\lambda$:
> $$\mathsf{A}\,v=\lambda\,v.$$
>
> **Paso 2 — Insertar la identidad $\mathsf{1}=\mathsf{S}\,\mathsf{S}^{-1}$.** Reescribimos $v=\mathsf{S}(\mathsf{S}^{-1}v)$:
> $$\mathsf{A}\,\mathsf{S}\,(\mathsf{S}^{-1}v)=\lambda\,v.$$
>
> **Paso 3 — Multiplicar por $\mathsf{S}^{-1}$ por la izquierda.**
> $$\mathsf{S}^{-1}\mathsf{A}\,\mathsf{S}\,(\mathsf{S}^{-1}v)=\lambda\,(\mathsf{S}^{-1}v).$$
>
> **Paso 4 — Reconocer $\mathsf{A}'$.** Como $\mathsf{A}'=\mathsf{S}^{-1}\mathsf{A}\,\mathsf{S}$, queda
> $$\mathsf{A}'\,(\mathsf{S}^{-1}v)=\lambda\,(\mathsf{S}^{-1}v).$$
> Es decir: $\mathsf{A}'$ tiene **el mismo autovalor** $\lambda$, con autovector $\mathsf{S}^{-1}v$. El espectro es invariante. $\blacksquare$

> [!demostracion] La semejanza conserva la traza (y el determinante)
> **Paso 1 — Propiedad cíclica de la traza.** Para matrices cualesquiera $\operatorname{tr}(\mathsf{X}\mathsf{Y})=\operatorname{tr}(\mathsf{Y}\mathsf{X})$. Aplicada con $\mathsf{X}=\mathsf{S}^{-1}$ e $\mathsf{Y}=\mathsf{A}\,\mathsf{S}$:
> $$\operatorname{tr}(\mathsf{A}')=\operatorname{tr}(\mathsf{S}^{-1}\mathsf{A}\,\mathsf{S})=\operatorname{tr}(\mathsf{A}\,\mathsf{S}\,\mathsf{S}^{-1}).$$
>
> **Paso 2 — Cancelar.** Como $\mathsf{S}\,\mathsf{S}^{-1}=\mathsf{1}$,
> $$\operatorname{tr}(\mathsf{A}')=\operatorname{tr}(\mathsf{A}).$$
>
> **Paso 3 — Determinante.** Por la regla del producto $|\mathsf{X}\mathsf{Y}|=|\mathsf{X}|\,|\mathsf{Y}|$ y $|\mathsf{S}^{-1}|=1/|\mathsf{S}|$:
> $$|\mathsf{A}'|=|\mathsf{S}^{-1}|\,|\mathsf{A}|\,|\mathsf{S}|=\frac{1}{|\mathsf{S}|}\,|\mathsf{A}|\,|\mathsf{S}|=|\mathsf{A}|. \qquad\blacksquare$$
> Traza, determinante y espectro son **invariantes de semejanza**; al diagonalizar, $\operatorname{tr}\mathsf{A}=\sum_k\lambda_k$ y $|\mathsf{A}|=\prod_k\lambda_k$.

> [!proposicion] Matrices simétricas y Hermíticas
> Cuando $\mathsf{A}$ es **simétrica** ($\mathsf{A}=\tilde{\mathsf{A}}$) o **Hermítica** ($\mathsf{A}=\mathsf{A}^\dagger$):
> 1. Sus autovalores son **reales**.
> 2. Sus autovectores (de autovalores distintos) son **ortogonales**, y pueden normalizarse a ortonormales.
>
> Entonces la $\mathsf{S}$ de autovectores ortonormales es **ortogonal** ($\mathsf{S}^{-1}=\tilde{\mathsf{S}}$) o **unitaria** ($\mathsf{S}^{-1}=\mathsf{S}^\dagger$), y la diagonalización es una **rotación** de la base. La generalización (qué matrices admiten $\mathsf{S}$ unitaria) está en [[Matrices Normales]].

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Semejanza | $\mathsf{A}'=\mathsf{S}^{-1}\mathsf{A}\,\mathsf{S}$ (mismo operador, otra base) |
> | $\mathsf{S}$ | columnas = autovectores de $\mathsf{A}$ |
> | Ecuación característica | $\det(\mathsf{A}-\lambda\mathsf{1})=0$ (grado $n$ → $n$ autovalores) |
> | Forma diagonal | $\mathsf{A}'=\operatorname{diag}(\lambda_1,\dots,\lambda_n)$ |
> | Invariantes | autovalores, $\operatorname{tr}\mathsf{A}=\sum_k\lambda_k$, $\|\mathsf{A}\|=\prod_k\lambda_k$ |
> | Simétrica / Hermítica | autovalores reales, autovectores ortonormales → $\mathsf{S}$ ortogonal / unitaria |

> [!corolario]
> Diagonalizar = cambiar a la base de los autovectores, donde el operador solo escala cada eje. El cálculo es el mismo de [[../4 Introduccion a Tensores/Diagonalizacion de Tensores/Valores y Vectores Propios | autovalores y autovectores]]: ecuación característica → autovalores → resolver y normalizar → columnas de $\mathsf{S}$. La semejanza conserva el espectro, la traza y el determinante, que son los **invariantes** de la matriz. Para matrices simétricas/Hermíticas la transformación es una rotación (ortogonal/unitaria); cuáles se diagonalizan así en general lo decide la normalidad ([[Matrices Normales]]).

> [!referencia]
> - Cálculo de autovalores/autovectores y casos degenerados: [[../4 Introduccion a Tensores/Diagonalizacion de Tensores/Valores y Vectores Propios]].
> - Versión geométrica (ejes principales de un tensor): [[../4 Introduccion a Tensores/Diagonalizacion de Tensores/index]].
> - Cuándo existe $\mathsf{S}$ unitaria: [[Matrices Normales]].
> - Propiedades del determinante usadas aquí ($\|\mathsf{A}\mathsf{B}\|=\|\mathsf{A}\|\|\mathsf{B}\|$): [[Determinantes]].
