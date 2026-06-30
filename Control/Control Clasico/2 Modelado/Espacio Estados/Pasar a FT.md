---
title: De Espacio de Estados a Función Transferencia
order: 2
tags:
  - control-clasico
  - teoria
  - espacio-estados
draft: false
aliases:
  - espacio a ft
  - espacio a transferencia
  - calcular ft desde espacio
---

# De Espacio de Estados a Función Transferencia

> [!definicion]
> Dado un sistema $\dot{\mathbf{x}}=\mathbf{A}\mathbf{x}+\mathbf{B}u$, $y=\mathbf{C}\mathbf{x}+\mathbf{D}u$, su función transferencia se obtiene por
> $$G(s)=\mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B}+\mathbf{D}.$$
> En MIMO el resultado es la matriz $\mathbf{G}(s)\in\mathbb{C}^{p\times m}$. El denominador es $\det(s\mathbf{I}-\mathbf{A})$, cuyas raíces (autovalores de $\mathbf{A}$) son los polos.

> [!info]
> Puente del [[index | espacio de estados]] hacia la [[Funcion Transferencia/index | función transferencia]]. La operación inversa (de una FT a una realización $A,B,C,D$) está en [[Pasar desde FT]].

---

## Ejemplo

> [!ejemplo] Calcular la FT desde $A,B,C,D$ numéricos
> Sea
> $$\mathbf{A}=\begin{bmatrix}0&1\\-2&-3\end{bmatrix},\quad \mathbf{B}=\begin{bmatrix}0\\1\end{bmatrix},\quad \mathbf{C}=\begin{bmatrix}1&0\end{bmatrix},\quad \mathbf{D}=0.$$
>
> **Paso 1 — Construir $s\mathbf{I}-\mathbf{A}$:**
> $$s\mathbf{I}-\mathbf{A}=\begin{bmatrix}s&-1\\2&s+3\end{bmatrix}.$$
>
> **Paso 2 — Determinante:** $\Delta(s)=\det(s\mathbf{I}-\mathbf{A})=s(s+3)+2=s^2+3s+2$.
>
> **Paso 3 — Inversa** (adjunta sobre determinante):
> $$(s\mathbf{I}-\mathbf{A})^{-1}=\frac{1}{\Delta(s)}\begin{bmatrix}s+3&1\\-2&s\end{bmatrix}.$$
>
> **Paso 4 — Multiplicar $\mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}$:**
> $$\begin{bmatrix}1&0\end{bmatrix}\frac{1}{\Delta(s)}\begin{bmatrix}s+3&1\\-2&s\end{bmatrix}=\frac{1}{\Delta(s)}\begin{bmatrix}s+3&1\end{bmatrix}.$$
>
> **Paso 5 — Multiplicar por $\mathbf{B}$ y sumar $\mathbf{D}=0$:**
> $$G(s)=\frac{1}{\Delta(s)}\begin{bmatrix}s+3&1\end{bmatrix}\begin{bmatrix}0\\1\end{bmatrix}=\frac{1}{s^2+3s+2}.$$
>
> Los polos $-1,-2$ coinciden con los autovalores de $\mathbf{A}$.

> [!ejemplo] De estados a función de transferencia
> ![[ee_pasar_a_ft.svg|640]]
>
> Tomando Laplace con $x(0)=0$ se despeja $X=(sI-A)^{-1}BU$ y se sustituye en $Y=CX+DU$ para obtener $G(s)=C(sI-A)^{-1}B+D$.

> [!ejemplo] Con alimentación directa $D\neq0$
> $\dot{x}=-2x+3u$, $y=4x+5u$ → $A=-2,B=3,C=4,D=5$.
> $$G(s)=4\cdot\frac{1}{s+2}\cdot3+5=\frac{12}{s+2}+5=\frac{5s+22}{s+2}.$$
> Como $D\neq0$, el grado del numerador iguala al del denominador (bipropio).

---

## En qué consiste

> [!teorema] Fórmula de transformación
> Para SISO, $G(s)=\mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B}+\mathbf{D}$ es escalar; para MIMO, $\mathbf{G}(s)=\mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B}+\mathbf{D}$ es la matriz de transferencia $p\times m$.

> [!demostracion] Paso a paso (SISO)
> **Paso 1 — Laplace con CI nulas** ($\mathbf{x}(0^-)=\mathbf{0}$): $s\mathbf{X}(s)=\mathbf{A}\mathbf{X}(s)+\mathbf{B}U(s)$.
>
> **Paso 2 — Reagrupar:** $(s\mathbf{I}-\mathbf{A})\mathbf{X}(s)=\mathbf{B}U(s)$.
>
> **Paso 3 — Despejar:** $\mathbf{X}(s)=(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B}U(s)$.
>
> **Paso 4 — Salida en Laplace:** $Y(s)=\mathbf{C}\mathbf{X}(s)+\mathbf{D}U(s)$.
>
> **Paso 5 — Sustituir y factorizar $U(s)$:**
> $$Y(s)=\big[\mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B}+\mathbf{D}\big]U(s).$$
>
> **Paso 6 — Por definición** $G(s)=Y(s)/U(s)$:
> $$G(s)=\mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B}+\mathbf{D}.\qquad\blacksquare$$

> [!teorema] Polos = autovalores de $\mathbf{A}$
> Como $(s\mathbf{I}-\mathbf{A})^{-1}=\dfrac{\operatorname{adj}(s\mathbf{I}-\mathbf{A})}{\det(s\mathbf{I}-\mathbf{A})}$, el denominador de $G(s)$ es el polinomio característico $\det(s\mathbf{I}-\mathbf{A})$. Por tanto:
> $$\text{polos}\subseteq\{\lambda_1,\dots,\lambda_n\}\ \text{(autovalores de }\mathbf{A}),$$
> con posibles **cancelaciones** polo-cero que reducen el orden aparente.

> [!warning] Cancelaciones polo-cero
> Si $\mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B}$ presenta cancelaciones, el orden de $G(s)$ es menor que $n$: el sistema **no es controlable y/o no observable**, y $G(s)$ puede ocultar dinámica interna inestable.

---

## Algoritmo

> [!algoritmo]
> 1. Construir $s\mathbf{I}-\mathbf{A}$.
> 2. Calcular $\Delta(s)=\det(s\mathbf{I}-\mathbf{A})$ y $\operatorname{adj}(s\mathbf{I}-\mathbf{A})$.
> 3. Formar $(s\mathbf{I}-\mathbf{A})^{-1}=\operatorname{adj}/\Delta$.
> 4. Multiplicar $\mathbf{C}\,(s\mathbf{I}-\mathbf{A})^{-1}\,\mathbf{B}$ y sumar $\mathbf{D}$.
> 5. Simplificar factores comunes (vigilar cancelaciones).

> [!info] En MATLAB
> ```matlab
> A=[0 1; -2 -3]; B=[0;1]; C=[1 0]; D=0;
> sys = ss(A,B,C,D);
> G   = tf(sys);     % 1/(s^2+3s+2)
> eig(A)             % polos = autovalores de A
> ```

---

## Limitaciones

> [!warning]
> 1. Invertir $s\mathbf{I}-\mathbf{A}$ a mano es tedioso para $n>4$.
> 2. Para sistemas grandes conviene usar herramientas (MATLAB, Python).
> 3. Las cancelaciones polo-cero pueden ocultar modos internos inestables.

## Resumen

> [!resumen]
> | Paso | Operación |
> |---|---|
> | Fórmula | $G(s)=\mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B}+\mathbf{D}$ |
> | Denominador | $\Delta(s)=\det(s\mathbf{I}-\mathbf{A})$ |
> | Numerador | $\mathbf{C}\,\operatorname{adj}(s\mathbf{I}-\mathbf{A})\,\mathbf{B}+\mathbf{D}\,\Delta(s)$ |
> | Polos | autovalores de $\mathbf{A}$ (salvo cancelaciones) |
> | $\mathbf{D}=0$ | estrictamente propio |

> [!corolario]
> La FT se obtiene siempre con $G(s)=\mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B}+\mathbf{D}$: el determinante de $s\mathbf{I}-\mathbf{A}$ fija el denominador y sus raíces son los polos. Una cancelación polo-cero delata pérdida de controlabilidad u observabilidad. La construcción inversa está en [[Pasar desde FT]].

> [!referencia]
> - Módulo padre: [[index]].
> - Operación inversa: [[Pasar desde FT]].
> - Forma general y cambio de base: [[Forma General]].
> - Representación destino: [[Funcion Transferencia/index]].
