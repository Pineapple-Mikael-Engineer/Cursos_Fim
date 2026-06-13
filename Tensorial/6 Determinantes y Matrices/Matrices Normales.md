---
title: Matrices Normales
tags:
  - analisis-tensorial
  - teoria
  - matrices
  - diagonalizacion
draft: false
aliases:
  - matrices normales
  - matriz normal
  - teorema espectral
  - normal matrices
---

# Matrices Normales

> [!definicion]
> Una matriz $\mathsf{A}$ es **normal** si **conmuta con su adjunta**:
> $$\mathsf{A}\,\mathsf{A}^\dagger=\mathsf{A}^\dagger\mathsf{A}\qquad\Longleftrightarrow\qquad [\mathsf{A},\mathsf{A}^\dagger]=0,$$
> donde $\mathsf{A}^\dagger=\tilde{\mathsf{A}}^{\,*}$ es la transpuesta conjugada. Es la clase **exacta** de matrices diagonalizables por una transformación **unitaria**.

> [!info]
> Sección **6.6** del [[index | capítulo 6]] (libro, cap. 6.6). Generaliza la [[Diagonalizacion de Matrices | diagonalización]] del cap. 6.5 (limitada a simétricas/Hermíticas) a la mayor clase posible bajo transformaciones unitarias. Engloba como casos particulares las matrices [[Matrices Hermiticas y Unitarias | Hermíticas, anti-Hermíticas y unitarias]], y las [[Matrices Ortogonales | ortogonales]]. Aparece en problemas físicos como los **modos normales de vibración** y el diagnóstico de **matrices patológicas**.

---

## Ejemplo

> [!ejemplo] Una matriz normal que **no** es Hermítica ni unitaria
> Sea
> $$\mathsf{A}=\begin{pmatrix}1&1\\-1&1\end{pmatrix}.$$
> No es Hermítica ($\mathsf{A}^\dagger=\begin{pmatrix}1&-1\\1&1\end{pmatrix}\neq\mathsf{A}$) ni unitaria ($\mathsf{A}^\dagger\mathsf{A}=2\mathsf{1}\neq\mathsf{1}$). Pero **sí es normal**:
>
> **Paso 1 — Adjunta.** Real, así que $\mathsf{A}^\dagger=\tilde{\mathsf{A}}=\begin{pmatrix}1&-1\\1&1\end{pmatrix}$.
>
> **Paso 2 — Producto $\mathsf{A}\mathsf{A}^\dagger$.**
> $$\mathsf{A}\,\mathsf{A}^\dagger=\begin{pmatrix}1&1\\-1&1\end{pmatrix}\begin{pmatrix}1&-1\\1&1\end{pmatrix}=\begin{pmatrix}2&0\\0&2\end{pmatrix}.$$
>
> **Paso 3 — Producto $\mathsf{A}^\dagger\mathsf{A}$.**
> $$\mathsf{A}^\dagger\mathsf{A}=\begin{pmatrix}1&-1\\1&1\end{pmatrix}\begin{pmatrix}1&1\\-1&1\end{pmatrix}=\begin{pmatrix}2&0\\0&2\end{pmatrix}.$$
>
> **Paso 4 — Comparar.** $\mathsf{A}\mathsf{A}^\dagger=\mathsf{A}^\dagger\mathsf{A}=2\mathsf{1}$, luego $[\mathsf{A},\mathsf{A}^\dagger]=0$: es **normal**. Por el teorema, es diagonalizable por una transformación unitaria, con autovalores **complejos** $\lambda=1\pm i$ (raíces de $(1-\lambda)^2+1=0$) y autovectores ortonormales.

---

## En qué consiste

> [!teorema] Diagonalización unitaria $\Leftrightarrow$ normalidad
> Una matriz $\mathsf{A}$ es diagonalizable por una transformación **unitaria** ($\mathsf{A}'=\mathsf{U}^\dagger\mathsf{A}\,\mathsf{U}$ diagonal, con $\mathsf{U}^\dagger\mathsf{U}=\mathsf{1}$) **si y solo si** es **normal** ($\mathsf{A}\mathsf{A}^\dagger=\mathsf{A}^\dagger\mathsf{A}$). En tal caso sus autovectores forman una base **ortonormal**, y la $\mathsf{U}$ se construye con ellos como columnas.

> [!teoria]
> La idea (cap. 6.6) es: para una matriz normal $\mathsf{A}$, su adjunta $\mathsf{A}^\dagger$ tiene **los mismos autovectores** que $\mathsf{A}$ (con autovalores complejos conjugados $\lambda^*$). Eso fuerza que autovectores de autovalores distintos sean **ortogonales** —igual que en el caso Hermítico, pero ahora con autovalores posiblemente complejos—. Esos autovectores ortonormales construyen la $\mathsf{U}$ unitaria que diagonaliza. La recíproca es directa: si $\mathsf{A}=\mathsf{U}\,\mathsf{D}\,\mathsf{U}^\dagger$ con $\mathsf{D}$ diagonal, entonces $\mathsf{A}$ y $\mathsf{A}^\dagger$ conmutan porque las diagonales $\mathsf{D}$ y $\mathsf{D}^\dagger$ conmutan.

> [!proposicion] Las clases físicas son todas normales
> Las matrices [[Matrices Hermiticas y Unitarias | Hermíticas]], anti-Hermíticas y unitarias —y las [[Matrices Ortogonales | ortogonales]] reales— son **todas normales**, luego todas diagonalizables por transformación unitaria:
>
> | Clase | Definición | $\mathsf{A}\mathsf{A}^\dagger$ vs $\mathsf{A}^\dagger\mathsf{A}$ | Autovalores |
> |---|---|---|---|
> | Hermítica | $\mathsf{A}^\dagger=\mathsf{A}$ | $\mathsf{A}^2=\mathsf{A}^2$ | reales |
> | Anti-Hermítica | $\mathsf{A}^\dagger=-\mathsf{A}$ | $-\mathsf{A}^2=-\mathsf{A}^2$ | imaginarios puros (o $0$) |
> | Unitaria | $\mathsf{A}^\dagger=\mathsf{A}^{-1}$ | $\mathsf{A}\mathsf{A}^{-1}=\mathsf{A}^{-1}\mathsf{A}=\mathsf{1}$ | magnitud uno |
> | **Normal** | $\mathsf{A}\mathsf{A}^\dagger=\mathsf{A}^\dagger\mathsf{A}$ | (por definición) | complejos cualesquiera |
>
> En las tres primeras la igualdad es inmediata; por eso son casos particulares de normal. El recíproco no vale: hay normales que no son ninguna de las tres (ver Ejemplo).

> [!demostracion] Hermítica $\Rightarrow$ normal, y unitaria $\Rightarrow$ normal
> **Paso 1 — Caso Hermítico.** Si $\mathsf{A}^\dagger=\mathsf{A}$, sustituimos $\mathsf{A}^\dagger$ por $\mathsf{A}$ en ambos productos:
> $$\mathsf{A}\,\mathsf{A}^\dagger=\mathsf{A}\,\mathsf{A}=\mathsf{A}^2,\qquad \mathsf{A}^\dagger\mathsf{A}=\mathsf{A}\,\mathsf{A}=\mathsf{A}^2.$$
> Son iguales, luego $[\mathsf{A},\mathsf{A}^\dagger]=0$: **normal**. (Lo mismo con anti-Hermítica: $\mathsf{A}^\dagger=-\mathsf{A}$ da $-\mathsf{A}^2$ en ambos lados.)
>
> **Paso 2 — Caso unitario.** Si $\mathsf{A}^\dagger=\mathsf{A}^{-1}$, entonces
> $$\mathsf{A}\,\mathsf{A}^\dagger=\mathsf{A}\,\mathsf{A}^{-1}=\mathsf{1},\qquad \mathsf{A}^\dagger\mathsf{A}=\mathsf{A}^{-1}\mathsf{A}=\mathsf{1}.$$
> Ambos productos valen $\mathsf{1}$, luego conmutan: **normal**. $\blacksquare$

> [!demostracion] Por qué $\mathsf{A}^\dagger$ comparte autovectores con $\mathsf{A}$ (núcleo del teorema)
> **Paso 1 — Definir $\mathsf{B}$.** Sea $\mathsf{A}\,|x\rangle=\lambda|x\rangle$, es decir $(\mathsf{A}-\lambda\mathsf{1})|x\rangle=0$. Llamamos $\mathsf{B}=\mathsf{A}-\lambda\mathsf{1}$, que **también es normal** ($[\mathsf{B},\mathsf{B}^\dagger]=[\mathsf{A},\mathsf{A}^\dagger]=0$).
>
> **Paso 2 — Norma de $\mathsf{B}^\dagger|x\rangle$.** Como $\mathsf{B}|x\rangle=0$, formamos
> $$\langle x|\mathsf{B}^\dagger\mathsf{B}|x\rangle=0\ \overset{[\mathsf{B},\mathsf{B}^\dagger]=0}{=}\ \langle x|\mathsf{B}\mathsf{B}^\dagger|x\rangle=\big(\mathsf{B}^\dagger|x\rangle\big)^\dagger\big(\mathsf{B}^\dagger|x\rangle\big)=0.$$
>
> **Paso 3 — Conclusión.** Una norma nula implica el vector nulo, $\mathsf{B}^\dagger|x\rangle=0$, es decir
> $$(\mathsf{A}^\dagger-\lambda^*\mathsf{1})|x\rangle=0\quad\Longrightarrow\quad \mathsf{A}^\dagger|x\rangle=\lambda^*|x\rangle.$$
> Mismo autovector $|x\rangle$, autovalor conjugado $\lambda^*$.
>
> **Paso 4 — Ortogonalidad.** Con dos autovectores $\mathsf{A}|x_i\rangle=\lambda_i|x_i\rangle$, $\mathsf{A}|x_j\rangle=\lambda_j|x_j\rangle$, se multiplica la segunda por $\langle x_i|$ y se usa el Paso 3 ($\langle x_i|\mathsf{A}=\lambda_i\langle x_i|$):
> $$\lambda_i\langle x_i|x_j\rangle=\lambda_j\langle x_i|x_j\rangle\ \Rightarrow\ (\lambda_i-\lambda_j)\langle x_i|x_j\rangle=0.$$
> Para $\lambda_i\neq\lambda_j$ queda $\langle x_i|x_j\rangle=0$: autovectores **ortogonales**. Construyen la $\mathsf{U}$ unitaria. $\blacksquare$

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Normal | $\mathsf{A}\mathsf{A}^\dagger=\mathsf{A}^\dagger\mathsf{A}$, $\ [\mathsf{A},\mathsf{A}^\dagger]=0$ |
> | Teorema | normal $\Leftrightarrow$ diagonalizable por $\mathsf{U}$ unitaria |
> | $\mathsf{A}^\dagger$ | mismos autovectores que $\mathsf{A}$, autovalor $\lambda^*$ |
> | Autovectores | ortogonales (de autovalores distintos) |
> | Casos particulares | Hermítica, anti-Hermítica, unitaria, ortogonal |
> | No al revés | hay normales que no son ninguna (ver Ejemplo) |

> [!corolario]
> Normal es **el nombre exacto** de "diagonalizable por una rotación generalizada": conmutar con la adjunta basta y sobra para que los autovectores sean ortonormales y exista una $\mathsf{U}$ unitaria que diagonalice. Las matrices de la física —Hermíticas (observables), unitarias (evolución), anti-Hermíticas— caen todas dentro de esta clase, que es estrictamente mayor. La diagonalización ortogonal de las simétricas reales en [[Diagonalizacion de Matrices]] es el caso real de este resultado.

> [!referencia]
> - El procedimiento de diagonalización y la semejanza: [[Diagonalizacion de Matrices]].
> - Definiciones de Hermítica, anti-Hermítica y unitaria: [[Matrices Hermiticas y Unitarias]].
> - Matrices ortogonales (caso real): [[Matrices Ortogonales]].
> - Cálculo de autovalores/autovectores: [[../4 Introduccion a Tensores/Diagonalizacion de Tensores/Valores y Vectores Propios]].
