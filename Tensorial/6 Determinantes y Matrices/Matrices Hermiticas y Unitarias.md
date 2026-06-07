---
title: Matrices Hermiticas y Unitarias
tags:
  - analisis-tensorial
  - teoria
  - matrices
  - mecanica-cuantica
draft: false
aliases:
  - matriz hermitica
  - matriz unitaria
  - matriz adjunta
  - autoadjunta
  - matrices de Pauli
  - hermitian and unitary matrices
---

# Matrices Hermiticas y Unitarias $\mathsf{A}^\dagger=\mathsf{A}$, $\mathsf{U}^\dagger\mathsf{U}=\mathsf{1}$

> [!definicion]
> Para matrices **complejas** se usa la **adjunta** (transpuesta conjugada)
> $$\mathsf{A}^\dagger=(\tilde{\mathsf{A}})^*=\widetilde{\mathsf{A}^*},\qquad (a^\dagger)_{ij}=a^*_{ji}.$$
> - **Hermítica** (o autoadjunta): $\mathsf{A}^\dagger=\mathsf{A}$, es decir $a_{ij}=a^*_{ji}$. Es el análogo complejo de **simétrica**.
> - **Unitaria:** $\mathsf{U}^\dagger\mathsf{U}=\mathsf{U}\mathsf{U}^\dagger=\mathsf{1}$, es decir $\mathsf{U}^\dagger=\mathsf{U}^{-1}$. Es el análogo complejo de **ortogonal**.

> [!info]
> Cuarta sección del [[index | capítulo 6]] (libro, cap. 6.4). Generaliza al campo complejo las [[Matrices Ortogonales]] (caso real). Son centrales en mecánica cuántica: las **hermíticas** representan observables (autovalores reales) y las **unitarias** describen evoluciones y simetrías (conservan la norma compleja $\langle x|x\rangle$). La adjunta combina la transpuesta de [[Matrices/index | Matrices]] con la conjugación compleja. Las normales ($\mathsf{A}\mathsf{A}^\dagger=\mathsf{A}^\dagger\mathsf{A}$) las engloban a ambas: [[Matrices Normales]].

---

## Ejemplo

> [!ejemplo]
> **Las matrices de Pauli son hermíticas.** Introducidas para el espín $\tfrac12$:
> $$\sigma_1=\begin{pmatrix}0&1\\1&0\end{pmatrix},\quad \sigma_2=\begin{pmatrix}0&-i\\i&0\end{pmatrix},\quad \sigma_3=\begin{pmatrix}1&0\\0&-1\end{pmatrix}.$$
> Para $\sigma_2$: la transpuesta intercambia $-i$ e $i$, y la conjugación los devuelve a su sitio,
> $$\sigma_2^\dagger=(\tilde{\sigma_2})^*=\begin{pmatrix}0&i\\-i&0\end{pmatrix}^*=\begin{pmatrix}0&-i\\i&0\end{pmatrix}=\sigma_2.$$
> Las tres cumplen $\sigma_k^\dagger=\sigma_k$ (los elementos diagonales son reales y los de fuera complejos conjugados cruzados), por eso sus autovalores $\pm1$ son **reales**, como debe ser para un observable. Además $(\sigma_k)^2=\mathsf{1}$, así que también son **unitarias**: las de Pauli son a la vez hermíticas y unitarias.

> [!ejemplo]
> **Una matriz de fase es unitaria.** Sea, con $\theta_1,\theta_2\in\mathbb{R}$,
> $$\mathsf{U}=\operatorname{diag}\!\big(e^{i\theta_1},e^{i\theta_2}\big)=\begin{pmatrix}e^{i\theta_1}&0\\0&e^{i\theta_2}\end{pmatrix}.$$
> Su adjunta conjuga las fases (la diagonal no cambia al transponer): $\mathsf{U}^\dagger=\operatorname{diag}(e^{-i\theta_1},e^{-i\theta_2})$. Entonces
> $$\mathsf{U}^\dagger\mathsf{U}=\operatorname{diag}\!\big(e^{-i\theta_1}e^{i\theta_1},\,e^{-i\theta_2}e^{i\theta_2}\big)=\operatorname{diag}(1,1)=\mathsf{1}.$$
> Luego $\mathsf{U}^\dagger=\mathsf{U}^{-1}$: es unitaria. No es hermítica salvo que las fases sean $0$ o $\pi$ (autovalores reales). Multiplicar un vector por $\mathsf{U}$ solo rota fases, dejando $\langle x|x\rangle$ inalterado.

---

## En qué consiste

> [!teoria] La adjunta y las dos clases complejas
> La adjunta $\mathsf{A}^\dagger=(\tilde{\mathsf{A}})^*$ es la operación natural en espacios complejos, donde el cuadrado de la norma de $x=(x_1,\dots,x_n)$ es $x^\dagger x=\sum_i x_i^* x_i=\sum_i|x_i|^2$. Propiedades útiles:
> - $(\mathsf{A}\mathsf{B})^\dagger=\mathsf{B}^\dagger\mathsf{A}^\dagger$ (invierte el orden, como la transpuesta).
> - Si $\mathsf{A}$ es **real**, $\mathsf{A}^\dagger=\tilde{\mathsf{A}}$: hermítica $\to$ simétrica, unitaria $\to$ ortogonal.
>
> Una transformación de coordenadas $y=\mathsf{U}x$ conserva la distancia compleja si $x^\dagger x=y^\dagger y=(\mathsf{U}x)^\dagger(\mathsf{U}x)=x^\dagger\mathsf{U}^\dagger\mathsf{U}x$ para todo $x$, lo que obliga a $\mathsf{U}^\dagger\mathsf{U}=\mathsf{1}$: ahí nace la **unitariedad**. Es la generalización exacta de "la ortogonal conserva la longitud real".

> [!teorema] Los autovalores de una matriz hermítica son reales
> Si $\mathsf{A}^\dagger=\mathsf{A}$ y $\mathsf{A}|x\rangle=\lambda|x\rangle$ con $|x\rangle\neq0$, entonces $\lambda=\lambda^*\in\mathbb{R}$.

> [!demostracion] $\lambda=\lambda^*$ a partir de $\mathsf{A}=\mathsf{A}^\dagger$
> **Paso 1.** Partimos de la ecuación de autovalores y la multiplicamos por la izquierda por el bra $\langle x|$:
> $$\mathsf{A}|x\rangle=\lambda|x\rangle\ \Longrightarrow\ \langle x|\mathsf{A}|x\rangle=\lambda\,\langle x|x\rangle.$$
> **Paso 2.** Tomamos la **adjunta** de $\mathsf{A}|x\rangle=\lambda|x\rangle$. Como $(\mathsf{A}|x\rangle)^\dagger=\langle x|\mathsf{A}^\dagger$ y $(\lambda|x\rangle)^\dagger=\lambda^*\langle x|$:
> $$\langle x|\mathsf{A}^\dagger=\lambda^*\langle x|.$$
> **Paso 3.** Usamos la hipótesis $\mathsf{A}^\dagger=\mathsf{A}$ y multiplicamos por la derecha por el ket $|x\rangle$:
> $$\langle x|\mathsf{A}|x\rangle=\lambda^*\,\langle x|x\rangle.$$
> **Paso 4.** Restamos este resultado del Paso 1. El lado izquierdo $\langle x|\mathsf{A}|x\rangle$ es el mismo en ambos, así que se cancela:
> $$(\lambda-\lambda^*)\,\langle x|x\rangle=0.$$
> **Paso 5.** Como $|x\rangle\neq0$, la norma $\langle x|x\rangle=\sum_i|x_i|^2>0$. Por tanto $\lambda-\lambda^*=0$, es decir $\lambda=\lambda^*$: el autovalor es **real**. $\blacksquare$
>
> Un argumento análogo con dos autovalores distintos muestra que los **autovectores** correspondientes son **ortogonales**; normalizándolos se obtiene una base **ortonormal**. Por eso las matrices hermíticas representan observables: valores medidos reales y estados propios ortogonales.

---

## Real vs. complejo

> [!info] Diccionario entre el caso real y el complejo
> | Operación / clase | Caso real | Caso complejo |
> |:---|:---:|:---:|
> | Operación base | transpuesta $\tilde{\mathsf{A}}$ | adjunta $\mathsf{A}^\dagger=(\tilde{\mathsf{A}})^*$ |
> | "Igual a sí misma" | simétrica $\tilde{\mathsf{A}}=\mathsf{A}$ | hermítica $\mathsf{A}^\dagger=\mathsf{A}$ |
> | "Inversa $=$ adjunta" | ortogonal $\tilde{\mathsf{A}}=\mathsf{A}^{-1}$ | unitaria $\mathsf{U}^\dagger=\mathsf{U}^{-1}$ |
> | Conserva | longitud real $\sum x_i^2$ | norma compleja $\sum\|x_i\|^2$ |
> | Autovalores (simétrica/herm.) | reales | reales |
> | Aparece en | rotaciones, ejes principales | observables, evolución cuántica |
>
> Si la matriz es real, cada celda derecha colapsa en la izquierda: una hermítica real **es** simétrica y una unitaria real **es** ortogonal. El grupo de Lorentz es un caso de unitarias de especial interés en física.

---

## Resumen

> [!resumen]
> | Concepto | Resultado |
> |:---|:---|
> | Adjunta | $\mathsf{A}^\dagger=(\tilde{\mathsf{A}})^*$, $(a^\dagger)_{ij}=a^*_{ji}$ |
> | Hermítica | $\mathsf{A}^\dagger=\mathsf{A}$ (análogo de simétrica) |
> | Unitaria | $\mathsf{U}^\dagger\mathsf{U}=\mathsf{1}$, $\mathsf{U}^\dagger=\mathsf{U}^{-1}$ (análogo de ortogonal) |
> | Producto | $(\mathsf{A}\mathsf{B})^\dagger=\mathsf{B}^\dagger\mathsf{A}^\dagger$ |
> | Autovalores herm. | reales; autovectores ortonormales |
> | Ejemplo herm. | matrices de Pauli $\sigma_1,\sigma_2,\sigma_3$ |
> | Ejemplo unit. | fase $\operatorname{diag}(e^{i\theta_1},e^{i\theta_2})$ |

> [!corolario]
> La adjunta es la transpuesta correcta en el campo complejo. Las hermíticas (autovalores reales, autovectores ortonormales) son los observables de la mecánica cuántica; las unitarias (norma invariante) son sus rotaciones y evoluciones. Real es a complejo lo que simétrica/ortogonal es a hermítica/unitaria; ambas son casos particulares de matrices normales y, por ello, diagonalizables.

> [!referencia]
> - Caso real correspondiente: [[Matrices Ortogonales]].
> - Clase que las engloba ($\mathsf{A}\mathsf{A}^\dagger=\mathsf{A}^\dagger\mathsf{A}$): [[Matrices Normales]].
> - Diagonalización por autovalores: [[Diagonalizacion de Matrices]].
> - Transpuesta y operaciones de partida: [[Matrices/index]].
