---
title: Matrices Ortogonales
tags:
  - analisis-tensorial
  - teoria
  - matrices
  - rotaciones
draft: false
aliases:
  - matriz ortogonal
  - condicion de ortogonalidad
  - cosenos directores
  - angulos de Euler
  - orthogonal matrices
---

# Matrices Ortogonales $\tilde{\mathsf{A}}\mathsf{A}=\mathsf{1}$

> [!definicion]
> Una matriz real $\mathsf{A}$ es **ortogonal** si su transpuesta es su inversa:
> $$\tilde{\mathsf{A}}\mathsf{A}=\mathsf{A}\tilde{\mathsf{A}}=\mathsf{1}\qquad\Longleftrightarrow\qquad \tilde{\mathsf{A}}=\mathsf{A}^{-1}.$$
> Por componentes, la **condición de ortogonalidad** es
> $$\sum_i a_{ij}a_{ik}=\delta_{jk}\qquad(\text{también }\textstyle\sum_i a_{ji}a_{ki}=\delta_{jk}).$$
> Describe las **rotaciones reales** del espacio: $x'_i=\sum_j a_{ij}x_j$, con $a_{ij}=\hat{x}'_i\cdot\hat{x}_j$ los **cosenos directores** entre los ejes nuevos y viejos.

> [!info]
> Tercera sección del [[index | capítulo 6]] (libro, cap. 6.3). Es el análogo *real* de las [[Matrices Hermiticas y Unitarias | matrices unitarias]] y la versión matricial de la [[Introduccion a Tensores/Transformaciones entre Sistemas/Matriz de Transformacion | matriz de transformación]] entre sistemas cartesianos. Las ortogonales con $|\mathsf{A}|=+1$ forman el grupo de rotaciones $SO(3)$, base de la [[7 Teoria de Grupo/index | teoría de grupos]]. La transpuesta y la inversa se definen en [[Matrices/index | Matrices]].

---

## Ejemplo

> [!ejemplo]
> **Verificar que una matriz de rotación 3D es ortogonal.** Tomemos la rotación de $\varphi=30^\circ$ en torno al eje $x_3$:
> $$\mathsf{A}=\begin{pmatrix}\cos\varphi&\operatorname{sen}\varphi&0\\-\operatorname{sen}\varphi&\cos\varphi&0\\0&0&1\end{pmatrix}=\begin{pmatrix}\tfrac{\sqrt3}{2}&\tfrac12&0\\[2pt]-\tfrac12&\tfrac{\sqrt3}{2}&0\\[2pt]0&0&1\end{pmatrix}.$$
> **Producto $\tilde{\mathsf{A}}\mathsf{A}$** (la transpuesta intercambia el signo de los senos fuera de la diagonal):
> $$\tilde{\mathsf{A}}\mathsf{A}=\begin{pmatrix}\cos\varphi&-\operatorname{sen}\varphi&0\\\operatorname{sen}\varphi&\cos\varphi&0\\0&0&1\end{pmatrix}\begin{pmatrix}\cos\varphi&\operatorname{sen}\varphi&0\\-\operatorname{sen}\varphi&\cos\varphi&0\\0&0&1\end{pmatrix}=\begin{pmatrix}\cos^2\varphi+\operatorname{sen}^2\varphi&0&0\\0&\operatorname{sen}^2\varphi+\cos^2\varphi&0\\0&0&1\end{pmatrix}=\mathsf{1}.$$
> Luego $\tilde{\mathsf{A}}=\mathsf{A}^{-1}$: es ortogonal. Su **determinante** vale $|\mathsf{A}|=(\cos^2\varphi+\operatorname{sen}^2\varphi)\cdot1=1$, así que es una **rotación propia** (no incluye reflexión). Las columnas son vectores **unitarios** ($\tfrac34+\tfrac14=1$) y **mutuamente perpendiculares** ($\tfrac{\sqrt3}{2}\cdot\tfrac12-\tfrac12\cdot\tfrac{\sqrt3}{2}=0$): esa es justamente la lectura geométrica de $\sum_i a_{ij}a_{ik}=\delta_{jk}$.

---

## En qué consiste

> [!teoria] De la rotación a los cosenos directores
> Considérense dos sistemas cartesianos con el mismo origen pero orientación distinta: el sistema con primas está **rotado** respecto al sin primas. Proyectando cada eje nuevo sobre los viejos, un punto se transforma como
> $$x'_i=\sum_{j=1}^{3}a_{ij}x_j,\qquad a_{ij}=\cos(x'_i,x_j)=\hat{x}'_i\cdot\hat{x}_j.$$
> Los nueve $a_{ij}$ son los **cosenos directores** y forman la matriz $\mathsf{A}$. En notación de Dirac, $|x'\rangle=\mathsf{A}\,|x\rangle$. Conviene recordar que $a_{ij}$ **no** es simétrica: $\cos(x'_2,x_1)\neq\cos(x'_1,x_2)$ en general.

> [!teorema] Condición de ortogonalidad
> Que la transformación $x'_i=\sum_j a_{ij}x_j$ sea una rotación —que **conserve la longitud** $\sum_i x_i^2=\sum_i x'^2_i$ para todo punto— equivale a
> $$\boxed{\;\sum_i a_{ij}a_{ik}=\delta_{jk}\;}$$

> [!demostracion] La invariancia de la longitud $\Rightarrow$ ortogonalidad
> **Paso 1.** Exigimos que la distancia al origen sea la misma en ambos sistemas:
> $$\sum_i x_i^2=\sum_i x'^2_i.$$
> **Paso 2.** Sustituimos $x'_i=\sum_j a_{ij}x_j$ en el lado derecho. Cada $x'^2_i$ es un producto de dos sumas (renombramos los índices mudos $j$ y $k$ para no repetirlos más de dos veces):
> $$\sum_i x'^2_i=\sum_i\Big(\sum_j a_{ij}x_j\Big)\Big(\sum_k a_{ik}x_k\Big).$$
> **Paso 3.** Reordenamos las sumas dejando los $x$ fuera y agrupando los coeficientes:
> $$\sum_i x'^2_i=\sum_{j,k}x_j x_k\Big(\sum_i a_{ij}a_{ik}\Big).$$
> **Paso 4.** Igualamos con $\sum_i x_i^2=\sum_{j,k}\delta_{jk}\,x_jx_k$ (la delta selecciona $j=k$). Para que la identidad valga para **todos** los puntos $x_j,x_k$, los coeficientes de cada producto $x_jx_k$ deben coincidir:
> $$\sum_i a_{ij}a_{ik}=\delta_{jk}.\qquad\blacksquare$$
> La condición es **necesaria y suficiente**: equivale a $\tilde{\mathsf{A}}\mathsf{A}=\mathsf{1}$, y multiplicando por $\mathsf{A}^{-1}$ a la derecha da $\tilde{\mathsf{A}}=\mathsf{A}^{-1}$.

> [!info] Lecturas equivalentes de la ortogonalidad
> | Forma | Expresión | Lectura |
> |:---|:---|:---|
> | Componentes (columnas) | $\sum_i a_{ij}a_{ik}=\delta_{jk}$ | columnas ortonormales |
> | Componentes (filas) | $\sum_i a_{ji}a_{ki}=\delta_{jk}$ | filas ortonormales |
> | Matricial | $\tilde{\mathsf{A}}\mathsf{A}=\mathsf{A}\tilde{\mathsf{A}}=\mathsf{1}$ | transpuesta $=$ inversa |
> | Inversa | $\tilde{\mathsf{A}}=\mathsf{A}^{-1}$ | deshacer $=$ transponer |
> | Determinante | $\|\mathsf{A}\|=\pm1$ | $+1$ rotación, $-1$ con reflexión |

---

## Caso 2D

> [!proposicion] Rotación en el plano
> La rotación de los ejes un ángulo $\varphi$ (en el sentido horario) da $x'_1=x_1\cos\varphi+x_2\operatorname{sen}\varphi$, $x'_2=-x_1\operatorname{sen}\varphi+x_2\cos\varphi$, es decir
> $$\mathsf{A}=\begin{pmatrix}\cos\varphi&\operatorname{sen}\varphi\\-\operatorname{sen}\varphi&\cos\varphi\end{pmatrix},$$
> con $a_{11}=\cos\varphi=\cos(x'_1,x_1)$ y $a_{12}=\operatorname{sen}\varphi=\cos(\tfrac\pi2-\varphi)=\cos(x'_2,x_1)$. Para $\varphi=0$ se reduce a $\mathsf{1}$ (rotación nula).

> [!info] Comprobación directa de las dos propiedades clave
> - **Transpuesta $=$ inversa:** $\tilde{\mathsf{A}}=\begin{pmatrix}\cos\varphi&-\operatorname{sen}\varphi\\\operatorname{sen}\varphi&\cos\varphi\end{pmatrix}=\mathsf{A}(-\varphi)$, que es justo la rotación inversa $\mathsf{A}^{-1}$. La condición de ortogonalidad se reduce aquí a la identidad pitagórica:
> $$\operatorname{sen}^2\varphi+\cos^2\varphi=1,\qquad \operatorname{sen}\varphi\cos\varphi-\operatorname{sen}\varphi\cos\varphi=0.$$
> - **Determinante unitario:** $\|\mathsf{A}\|=\cos^2\varphi+\operatorname{sen}^2\varphi=1$, de modo que la rotación conserva áreas.

---

## Angulos de Euler

> [!info] Tres parámetros independientes para una rotación 3D
> La matriz $\mathsf{A}$ contiene **nueve** cosenos directores, pero la condición de ortogonalidad $\sum_i a_{ij}a_{ik}=\delta_{jk}$ impone **seis** restricciones (tres normalizaciones $j=k$ y tres ortogonalidades $j\neq k$). Quedan $9-6=3$ **parámetros independientes**: una rotación 3D tiene exactamente tres grados de libertad (dos para fijar el eje, uno para el giro en torno a él).
>
> La parametrización estándar son los **ángulos de Euler** $(\alpha,\beta,\gamma)$, que descomponen la rotación en tres giros sucesivos:
> $$\mathsf{A}(\alpha,\beta,\gamma)=\mathsf{R}_z(\gamma)\,\mathsf{R}_y(\beta)\,\mathsf{R}_z(\alpha),$$
> con $\mathsf{R}_z(\alpha)$ actuando primero. Cada factor es una rotación elemental como la del caso 2D, embebida en 3D. Estos tres parámetros reemplazan a los nueve cosenos directores redundantes y son la **base para construir el grupo de rotaciones** $SO(3)$.

---

## Resumen

> [!resumen]
> | Concepto | Resultado |
> |:---|:---|
> | Definición | $\tilde{\mathsf{A}}\mathsf{A}=\mathsf{A}\tilde{\mathsf{A}}=\mathsf{1}$, o $\tilde{\mathsf{A}}=\mathsf{A}^{-1}$ |
> | Componentes | $a_{ij}=\hat{x}'_i\cdot\hat{x}_j$ (cosenos directores) |
> | Ortogonalidad | $\sum_i a_{ij}a_{ik}=\delta_{jk}$ (columnas ortonormales) |
> | Origen | conservar la longitud $\sum x_i^2=\sum x'^2_i$ |
> | Determinante | $\|\mathsf{A}\|=+1$ (rotación) o $-1$ (con reflexión) |
> | 2D | $\mathsf{A}=\begin{psmallmatrix}\cos\varphi&\operatorname{sen}\varphi\\-\operatorname{sen}\varphi&\cos\varphi\end{psmallmatrix}$ |
> | Grados de libertad 3D | $9-6=3$ (ángulos de Euler) |

> [!corolario]
> Una matriz ortogonal es la traducción algebraica de una rotación rígida del sistema de coordenadas: conserva longitudes y ángulos porque sus columnas (los ejes rotados) son ortonormales. Que la inversa sea la transpuesta hace triviales los cálculos de rotación. En 3D bastan tres ángulos de Euler para describirla, y las de determinante $+1$ constituyen el grupo $SO(3)$.

> [!referencia]
> - Análogo complejo (que conserva la norma compleja): [[Matrices Hermiticas y Unitarias]].
> - Transpuesta, inversa y operaciones: [[Matrices/index]].
> - Como transformación tensorial: [[Introduccion a Tensores/Transformaciones entre Sistemas/Matriz de Transformacion]].
> - Grupo de rotaciones $SO(3)$ y generadores: [[7 Teoria de Grupo/index]].
