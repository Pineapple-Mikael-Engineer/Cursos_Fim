---
title: Valores y Vectores Propios
order: 1
tags:
  - analisis-tensorial
  - teoria
  - tensores
  - diagonalizacion
  - autovalores
draft: false
aliases:
  - valores y vectores propios
  - autovalores y autovectores
  - ecuacion caracteristica
  - problema de valores propios
  - eigenvalues and eigenvectors
---

# Valores y Vectores Propios

> [!definicion]
> Un **autovalor** $\lambda_1$ y su **autovector** $\hat e'_1$ de un tensor $\overleftrightarrow{\sigma}$ cumplen
> $$\overleftrightarrow{\sigma}\cdot\hat e'_1=\lambda_1\,\hat e'_1,$$
> es decir: el tensor aplicado al autovector **no cambia su dirección**, solo su magnitud (por el factor $\lambda_1$). Los autovectores son los vectores base del sistema donde $\overleftrightarrow{\sigma}$ es diagonal, y los autovalores son los elementos de esa diagonal: $\sigma'_{11}=\lambda_1$, etc.

> [!info]
> Es el núcleo de la sección **4.4.1** del [[index | capítulo 4.4]] (libro, cap. 4.4.1). Resuelve el problema de [[index | diagonalización]]: hallar el sistema donde $\overleftrightarrow{\sigma}$ es diagonal equivale a hallar sus autovalores y autovectores. Usa el **tensor unidad** $\overleftrightarrow{1}=\delta_{ij}\hat e_i\hat e_j$ y el convenio de Einstein (ver [[../../1 Algebra Lineal y Notacion/index | notación de índices]]). La interpretación física de los autovectores se trata en [[Ejes Principales]].

---

## Ejemplo

> [!ejemplo] Ejemplo 1 — caso no degenerado
> Diagonalizar el tensor de conductividad (se ignoran las unidades)
> $$[\sigma]=\begin{pmatrix}10&0&0\\0&10&1\\0&1&10\end{pmatrix}.$$
> Es **Hermítica** (igual a su transpuesta conjugada), así que esperamos autovalores reales y autovectores ortonormales.
>
> **Paso 1 — Ecuación característica.** Imponemos $\det(\sigma_{ij}-\lambda\delta_{ij})=0$:
> $$\begin{vmatrix}10-\lambda&0&0\\0&10-\lambda&1\\0&1&10-\lambda\end{vmatrix}=0.$$
> Expandiendo por la primera columna:
> $$(10-\lambda)\big[(10-\lambda)^2-1\big]=0.$$
>
> **Paso 2 — Raíces (los tres autovalores).** El factor $(10-\lambda)=0$ da $\lambda=10$; el factor $(10-\lambda)^2-1=0$ da $(10-\lambda)=\pm1$, es decir $\lambda=9$ y $\lambda=11$. Etiquetamos
> $$\lambda_1=9,\qquad \lambda_2=11,\qquad \lambda_3=10.$$
>
> **Paso 3 — Primer autovector ($\lambda_1=9$).** Sustituimos $\lambda_1=9$ en $(\sigma_{ij}-\lambda_1\delta_{ij})a_{1j}=0$:
> $$\begin{pmatrix}1&0&0\\0&1&1\\0&1&1\end{pmatrix}\begin{pmatrix}a_{11}\\a_{12}\\a_{13}\end{pmatrix}=\begin{pmatrix}0\\0\\0\end{pmatrix}.$$
> La primera fila exige $a_{11}=0$; la segunda (y tercera, idéntica) exige $a_{12}+a_{13}=0$, o sea $a_{12}=-a_{13}$.
>
> **Paso 4 — Normalización.** La condición $a_{11}^2+a_{12}^2+a_{13}^2=1$ con $a_{11}=0$ y $a_{12}=-a_{13}$ da $2a_{12}^2=1$, luego
> $$\begin{pmatrix}a_{11}\\a_{12}\\a_{13}\end{pmatrix}=\frac1{\sqrt2}\begin{pmatrix}0\\1\\-1\end{pmatrix}\quad\Longrightarrow\quad \hat e'_1=\tfrac1{\sqrt2}\,(\hat e_2-\hat e_3).$$
>
> **Paso 5 — Los otros dos autovectores.** De forma análoga, $\lambda_2=11$ da $a_{22}=a_{23}$ y $a_{21}=0$, luego $\hat e'_2=\tfrac1{\sqrt2}(\hat e_2+\hat e_3)$; y $\lambda_3=10$ deja libre solo la dirección $1$, luego $\hat e'_3=\hat e_1$. La matriz de transformación completa es
> $$[a]=\frac1{\sqrt2}\begin{pmatrix}0&1&-1\\0&1&1\\\sqrt2&0&0\end{pmatrix}.$$
>
> **Paso 6 — Tensor diagonalizado.** En la nueva base, los elementos de $\overleftrightarrow{\sigma}$ son los autovalores:
> $$[\sigma']=\operatorname{diag}(9,11,10)=\begin{pmatrix}9&0&0\\0&11&0\\0&0&10\end{pmatrix}.$$

> [!ejemplo] Ejemplo 2 — caso degenerado
> Diagonalizar (de nuevo sin unidades)
> $$[\sigma]=\begin{pmatrix}11&-1&0\\-1&11&0\\0&0&10\end{pmatrix},$$
> también Hermítica.
>
> **Paso 1 — Ecuación característica.**
> $$\begin{vmatrix}11-\lambda&-1&0\\-1&11-\lambda&0\\0&0&10-\lambda\end{vmatrix}=0\quad\Longrightarrow\quad (10-\lambda)\big[(11-\lambda)^2-1\big]=0.$$
>
> **Paso 2 — Raíces.** El factor $(11-\lambda)^2-1=0$ da $(11-\lambda)=\pm1$, es decir $\lambda=10$ y $\lambda=12$; el factor $(10-\lambda)=0$ vuelve a dar $\lambda=10$. Hay tres raíces pero solo **dos distintas**:
> $$\lambda_1=12,\qquad \lambda_2=\lambda_3=10\ (\text{degenerado, doble}).$$
>
> **Paso 3 — Primer autovector ($\lambda_1=12$).** Sustituyendo en $(\sigma_{ij}-\lambda_1\delta_{ij})a_{1j}=0$:
> $$\begin{pmatrix}-1&-1&0\\-1&-1&0\\0&0&-2\end{pmatrix}\begin{pmatrix}a_{11}\\a_{12}\\a_{13}\end{pmatrix}=\begin{pmatrix}0\\0\\0\end{pmatrix}.$$
> Esto exige $a_{11}=-a_{12}$ y $a_{13}=0$. Con la normalización $a_{11}^2+a_{12}^2+a_{13}^2=1$:
> $$\begin{pmatrix}a_{11}\\a_{12}\\a_{13}\end{pmatrix}=\frac1{\sqrt2}\begin{pmatrix}1\\-1\\0\end{pmatrix}\quad\Longrightarrow\quad \hat e'_1=\tfrac1{\sqrt2}\,(\hat e_1-\hat e_2).$$
>
> **Paso 4 — Autovalor degenerado ($\lambda_2=\lambda_3=10$).** Sustituyendo $\lambda=10$:
> $$\begin{pmatrix}1&-1&0\\-1&1&0\\0&0&0\end{pmatrix}\begin{pmatrix}a_{21}\\a_{22}\\a_{23}\end{pmatrix}=\begin{pmatrix}0\\0\\0\end{pmatrix}.$$
> Solo queda la condición $a_{21}=a_{22}$, y $a_{23}$ **libre**. La degeneración deja **libertad** en la elección del autovector: muchos vectores la satisfacen. Imponemos que sean ortonormales.
>
> **Paso 5 — Elección ortonormal.** Fijamos $a_{23}=0$ y normalizamos: $a_{21}=a_{22}=1/\sqrt2$, de donde
> $$\hat e'_2=\tfrac1{\sqrt2}\,(\hat e_1+\hat e_2).$$
> El tercer autovector debe ser ortogonal a $\hat e'_1$ y $\hat e'_2$, que están en el plano $1$-$2$; por tanto $\hat e'_3$ apunta en la dirección $3$:
> $$\hat e'_3=\hat e_3.$$
>
> **Paso 6 — Tensor diagonalizado.** Los tres autovectores son ortonormales y forman un sistema derecho; en él
> $$[\sigma']=\operatorname{diag}(12,10,10).$$

---

## En qué consiste

> [!teoria]
> Buscamos el sistema primado donde $\overleftrightarrow{\sigma}$ es diagonal. La condición de que un vector base $\hat e'_1$ **no cambie de dirección** al actuar el tensor es exactamente $\overleftrightarrow{\sigma}\cdot\hat e'_1=\lambda_1\hat e'_1$: ahí el tensor solo **escala**. El **tensor unidad**
> $$\overleftrightarrow{1}=\delta_{ij}\hat e_i\hat e_j,\qquad \overleftrightarrow{1}\cdot\vec v=\vec v,\qquad [1]=\begin{pmatrix}1&0&0\\0&1&0\\0&0&1\end{pmatrix},$$
> permite reescribir esa condición de forma homogénea y reducirla a un problema algebraico estándar.

> [!teorema] Ecuación característica
> Los autovalores de $\overleftrightarrow{\sigma}$ son las raíces de
> $$\det(\sigma_{ij}-\lambda\delta_{ij})=0,$$
> una ecuación cúbica (en 3D) que produce **tres** autovalores $\lambda_1,\lambda_2,\lambda_3$. En la base de los autovectores, $[\sigma']=\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3)$.

> [!demostracion]
> **Paso 1 — Condición de no desviación.** Que el tensor no cambie la dirección del vector base $\hat e'_1$ es
> $$\overleftrightarrow{\sigma}\cdot\hat e'_1=\lambda_1\,\hat e'_1.$$
>
> **Paso 2 — Forma homogénea con el tensor unidad.** Usando $\hat e'_1=\overleftrightarrow{1}\cdot\hat e'_1$, pasamos todo a un lado:
> $$\big(\overleftrightarrow{\sigma}-\lambda_1\overleftrightarrow{1}\big)\cdot\hat e'_1=0.$$
>
> **Paso 3 — Notación de Einstein.** Expresando $\overleftrightarrow{\sigma}=\sigma_{ij}\hat e_i\hat e_j$ y $\overleftrightarrow{1}=\delta_{ij}\hat e_i\hat e_j$ en el sistema no primado:
> $$(\sigma_{ij}-\lambda_1\delta_{ij})\,\hat e_i\hat e_j\cdot\hat e'_1=0.$$
> Con $\hat e'_1=a_{1j}\hat e_j$ y la base ortonormal, el producto punto contrae los índices y queda
> $$\hat e_i\,(\sigma_{ij}-\lambda_1\delta_{ij})\,a_{1j}=0\quad\Longrightarrow\quad (\sigma_{ij}-\lambda_1\delta_{ij})\,a_{1j}=0.$$
> Los $a_{1j}$ son las incógnitas: tres de los elementos de la matriz de transformación $[a]$ que diagonaliza $\overleftrightarrow{\sigma}$.
>
> **Paso 4 — Sistema homogéneo.** El índice libre $i$ genera **tres** ecuaciones; en forma matricial,
> $$\begin{pmatrix}\sigma_{11}-\lambda_1&\sigma_{12}&\sigma_{13}\\\sigma_{21}&\sigma_{22}-\lambda_1&\sigma_{23}\\\sigma_{31}&\sigma_{32}&\sigma_{33}-\lambda_1\end{pmatrix}\begin{pmatrix}a_{11}\\a_{12}\\a_{13}\end{pmatrix}=\begin{pmatrix}0\\0\\0\end{pmatrix}.$$
>
> **Paso 5 — Solución no trivial.** Un sistema lineal homogéneo tiene solución distinta de cero solo si el determinante de los coeficientes se anula:
> $$\det(\sigma_{ij}-\lambda\delta_{ij})=0.$$
> Es una **cúbica** en $\lambda$ → tres autovalores. Para cada $\lambda_k$ se resuelve el sistema (con una constante libre) y se **normaliza** con $a_{k1}^2+a_{k2}^2+a_{k3}^2=1$, obteniendo el autovector $\hat e'_k=a_{kj}\hat e_j$. $\blacksquare$

> [!proposicion] Matrices Hermíticas
> Una matriz es **Hermítica** si es igual a su transpuesta conjugada, $\sigma_{ij}=\sigma^*_{ji}$. Las matrices de interés en física lo son. Dos propiedades clave:
> 1. Sus **autovalores son reales**.
> 2. Sus **autovectores son ortonormales** (o pueden elegirse así en el caso degenerado).
>
> Esto garantiza que el sistema diagonal sea un sistema de coordenadas cartesiano legítimo (base ortonormal).

> [!info] Degeneración
> Cuando dos o más autovalores coinciden ($\lambda_1\neq\lambda_2=\lambda_3$, por ejemplo) el problema es **degenerado**: los autovectores del autovalor repetido **no quedan determinados de forma única** — hay infinitas elecciones válidas. Se aprovecha esa libertad para elegirlos **ortonormales** (ver Ejemplo 2). Además queda siempre un signo global arbitrario, que se fija para que la base sea de **mano derecha**.

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Problema de autovalores | $\overleftrightarrow{\sigma}\cdot\hat e'_1=\lambda_1\hat e'_1$ |
> | Forma homogénea | $(\overleftrightarrow{\sigma}-\lambda_1\overleftrightarrow{1})\cdot\hat e'_1=0$ |
> | En índices | $(\sigma_{ij}-\lambda_1\delta_{ij})\,a_{1j}=0$ |
> | Ecuación característica | $\det(\sigma_{ij}-\lambda\delta_{ij})=0$ (cúbica → 3 autovalores) |
> | Tensor diagonal | $[\sigma']=\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3)$ |
> | Hermítica | autovalores reales, autovectores ortonormales |
> | Degeneración | autovalor repetido \| libertad en sus autovectores |

> [!corolario]
> Diagonalizar se reduce a un cálculo estándar: ecuación característica → autovalores → sustituir y normalizar → autovectores. Estos forman la matriz $[a]$ que diagonaliza el tensor, y los autovalores ocupan la diagonal de $[\sigma']$. Para matrices Hermíticas todo encaja: reales y ortonormales. La lectura física de los autovectores —los ejes donde el tensor no desvía— está en [[Ejes Principales]].

> [!referencia]
> - Marco e interpretación física: [[index | Diagonalización de Tensores]].
> - Los autovectores como ejes principales: [[Ejes Principales]].
> - Convenio de Einstein y delta de Kronecker: [[../../1 Algebra Lineal y Notacion/index]].
> - La matriz de transformación $[a]$: [[../Transformaciones entre Sistemas/Matriz de Transformacion]].
