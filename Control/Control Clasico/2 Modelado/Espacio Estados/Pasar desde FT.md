---
title: De Función Transferencia a Espacio de Estados
tags:
  - control-clasico
  - teoria
  - espacio-estados
draft: false
aliases:
  - ft a espacio
  - transferencia a estados
  - realización
  - realizaciones canónicas
---

# De Función Transferencia a Espacio de Estados

> [!definicion]
> Una **realización** de $G(s)$ es un conjunto $\{\mathbf{A},\mathbf{B},\mathbf{C},\mathbf{D}\}$ tal que $G(s)=\mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B}+\mathbf{D}$. No es única. Para $G(s)$ estrictamente propia con denominador $s^n+a_{n-1}s^{n-1}+\dots+a_0$ y numerador $b_{n-1}s^{n-1}+\dots+b_0$, la **forma canónica controlable** coloca los $-a_i$ en la última fila de $\mathbf{A}$ y los $b_i$ en $\mathbf{C}$.

> [!info]
> Operación inversa de [[Pasar a FT]], dentro del módulo de [[index | espacio de estados]]. Aquí se construyen las realizaciones canónicas (controlable, observable, diagonal, Jordan) a partir de una FT dada.

---

## Ejemplo

> [!ejemplo] Construir $A,B,C,D$ desde una FT (forma controlable)
> $$G(s)=\frac{2s+3}{s^2+4s+5}.$$
>
> **Paso 1 — Identificar coeficientes** (estrictamente propia, $n=2$):
> $$a_1=4,\quad a_0=5,\qquad b_1=2,\quad b_0=3.$$
>
> **Paso 2 — Forma canónica controlable.** Los $-a_i$ van en la última fila de $\mathbf{A}$, $\mathbf{B}$ es el último canónico, $\mathbf{C}=[\,b_0\ b_1\,]$:
> $$\mathbf{A}=\begin{bmatrix}0&1\\-5&-4\end{bmatrix},\quad \mathbf{B}=\begin{bmatrix}0\\1\end{bmatrix},\quad \mathbf{C}=\begin{bmatrix}3&2\end{bmatrix},\quad \mathbf{D}=0.$$
>
> **Paso 3 — Verificar** ($\Delta(s)=\det(s\mathbf{I}-\mathbf{A})=s^2+4s+5$):
> $$\mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B}=\frac{2s+3}{s^2+4s+5}=G(s).\ \checkmark$$
>
> **Forma observable** del mismo $G(s)$ (transpuesta estructural):
> $$\mathbf{A}=\begin{bmatrix}0&-5\\1&-4\end{bmatrix},\quad \mathbf{B}=\begin{bmatrix}3\\2\end{bmatrix},\quad \mathbf{C}=\begin{bmatrix}0&1\end{bmatrix},\quad \mathbf{D}=0.$$

> [!ejemplo] Forma canónica controlable
> ![[ee_pasar_desde_ft.svg|620]]
>
> Realización con cadena de integradores: los coeficientes del denominador $a_i$ van en la realimentación (última fila de $\mathbf{A}$) y los del numerador $b_i$ forman la salida $\mathbf{C}$.

> [!ejemplo] Realización diagonal (polos reales distintos)
> $$G(s)=\frac{6}{(s+1)(s+2)(s+3)}.$$
> Residuos $c_i=\big[(s-p_i)G(s)\big]_{s=p_i}$:
> $$c_1=\frac{6}{(1)(2)}=3,\quad c_2=\frac{6}{(-1)(1)}=-6,\quad c_3=\frac{6}{(-2)(-1)}=3.$$
> $$\mathbf{A}=\begin{bmatrix}-1&0&0\\0&-2&0\\0&0&-3\end{bmatrix},\quad \mathbf{B}=\begin{bmatrix}1\\1\\1\end{bmatrix},\quad \mathbf{C}=\begin{bmatrix}3&-6&3\end{bmatrix},\quad \mathbf{D}=0.$$

---

## En qué consiste

> [!teorema] Condición de realizabilidad
> $G(s)$ es realizable si y solo si es **propia o estrictamente propia**: $\lim_{s\to\infty}G(s)<\infty$.
> - Numerador $<$ denominador → estrictamente propia, $\mathbf{D}=\mathbf{0}$.
> - Numerador $=$ denominador → propia, $\mathbf{D}=b_n$ tras dividir.
> - Numerador $>$ denominador → impropia, **no realizable** físicamente.

> [!definicion] Forma canónica controlable
> Para $G(s)=\dfrac{b_{n-1}s^{n-1}+\dots+b_0}{s^n+a_{n-1}s^{n-1}+\dots+a_0}$:
> $$\mathbf{A}=\begin{bmatrix}0&1&0&\dots&0\\0&0&1&\dots&0\\\vdots&&&\ddots&\vdots\\0&0&0&\dots&1\\-a_0&-a_1&-a_2&\dots&-a_{n-1}\end{bmatrix},\ \mathbf{B}=\begin{bmatrix}0\\\vdots\\0\\1\end{bmatrix},\ \mathbf{C}=\begin{bmatrix}b_0&\dots&b_{n-1}\end{bmatrix},\ \mathbf{D}=0.$$

> [!definicion] Forma canónica observable
> Es la dual; $\mathbf{A}$ es la transpuesta de la controlable con los $-a_i$ en la última columna:
> $$\mathbf{A}=\begin{bmatrix}0&0&\dots&-a_0\\1&0&\dots&-a_1\\0&1&\dots&-a_2\\\vdots&&\ddots&\vdots\\0&\dots&1&-a_{n-1}\end{bmatrix},\ \mathbf{B}=\begin{bmatrix}b_0\\b_1\\\vdots\\b_{n-1}\end{bmatrix},\ \mathbf{C}=\begin{bmatrix}0&\dots&0&1\end{bmatrix}.$$

> [!demostracion] Por qué funciona la controlable
> Con $\mathbf{A}$ en forma compañera, su polinomio característico es exactamente $\det(s\mathbf{I}-\mathbf{A})=s^n+a_{n-1}s^{n-1}+\dots+a_0$, que reproduce el denominador. El producto $\mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B}$ recombina los $b_i$ en el numerador, dando $G(s)$ por construcción. $\blacksquare$

> [!definicion] Realización diagonal (polos simples)
> Si los polos $p_i$ son distintos, expandiendo $G(s)=\sum_i \dfrac{c_i}{s-p_i}+\mathbf{D}$ con residuos $c_i$:
> $$\mathbf{A}=\operatorname{diag}(p_1,\dots,p_n),\quad \mathbf{B}=\begin{bmatrix}1\\\vdots\\1\end{bmatrix},\quad \mathbf{C}=\begin{bmatrix}c_1&\dots&c_n\end{bmatrix}.$$
> Cada modo $\dot{x}_i=p_ix_i+u$, $y_i=c_ix_i$ queda desacoplado.

> [!definicion] Forma de Jordan (polos repetidos)
> Para un polo $p$ de multiplicidad $r$ con $G=\sum_{j=1}^r \dfrac{c_j}{(s-p)^j}$, un bloque de Jordan:
> $$\mathbf{A}=\begin{bmatrix}p&1&&\\&p&\ddots&\\&&\ddots&1\\&&&p\end{bmatrix},\quad \mathbf{B}=\begin{bmatrix}0\\\vdots\\0\\1\end{bmatrix},\quad \mathbf{C}=\begin{bmatrix}c_1&\dots&c_r\end{bmatrix}.$$

> [!info] Caso propio ($\mathbf{D}\neq0$)
> Si numerador y denominador tienen igual grado, primero se divide:
> $$G(s)=\frac{2s^2+3s+1}{s^2+4s+5}=2+\frac{-5s-9}{s^2+4s+5},$$
> con $\mathbf{D}=2$; luego se realiza la parte estrictamente propia en forma controlable:
> $$\mathbf{A}=\begin{bmatrix}0&1\\-5&-4\end{bmatrix},\ \mathbf{B}=\begin{bmatrix}0\\1\end{bmatrix},\ \mathbf{C}=\begin{bmatrix}-9&-5\end{bmatrix},\ \mathbf{D}=2.$$

> [!teorema] Equivalencia por cambio de base
> Si $\{\mathbf{A},\mathbf{B},\mathbf{C},\mathbf{D}\}$ realiza $G(s)$, también lo hace $\{\mathbf{T}\mathbf{A}\mathbf{T}^{-1},\mathbf{T}\mathbf{B},\mathbf{C}\mathbf{T}^{-1},\mathbf{D}\}$ para cualquier $\mathbf{T}$ invertible. Por eso hay infinitas realizaciones (ver [[Forma General]]).

---

## Algoritmo

> [!algoritmo]
> 1. Verificar que $G(s)$ sea propia; si numerador = denominador, dividir y fijar $\mathbf{D}=b_n$.
> 2. Sobre la parte estrictamente propia, leer los coeficientes $a_i$ (denominador) y $b_i$ (numerador).
> 3. Elegir la realización según el objetivo: controlable (ubicación de polos), observable (observadores), diagonal/Jordan (análisis modal).
> 4. Colocar $a_i,b_i$ en las plantillas de $\mathbf{A},\mathbf{B},\mathbf{C}$.
> 5. Verificar con $\mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B}+\mathbf{D}=G(s)$.

> [!info] En MATLAB
> ```matlab
> num=[2 3]; den=[1 4 5];
> sys = tf(num,den);
> [A,B,C,D] = tf2ss(num,den);   % realizacion (forma controlable)
> ss(sys)                        % objeto en espacio de estados
> ```

---

## Limitaciones

> [!warning]
> 1. Las formas canónicas pueden estar **mal condicionadas** numéricamente en orden alto.
> 2. En MIMO las formas canónicas son más complejas.
> 3. La realización diagonal exige polos **distintos**; con repetidos se usa Jordan.
> 4. Las cancelaciones polo-cero indican que la realización **no es mínima**.

## Resumen

> [!resumen]
> | Realización | $\mathbf{A}$ | Uso |
> |---|---|---|
> | Controlable | compañera, $-a_i$ última fila | ubicación de polos |
> | Observable | dual (transpuesta) | observadores |
> | Diagonal | $\operatorname{diag}(p_i)$ | análisis modal (polos distintos) |
> | Jordan | bloques con 1 en la superdiagonal | polos repetidos |

> [!corolario]
> Toda FT propia admite infinitas realizaciones $\{A,B,C,D\}$; la controlable y la observable se leen directo de los coeficientes $a_i,b_i$, la diagonal de los residuos, y los términos con $D\neq0$ salen de dividir antes. La verificación siempre es $\mathbf{C}(s\mathbf{I}-\mathbf{A})^{-1}\mathbf{B}+\mathbf{D}=G(s)$, el puente inverso de [[Pasar a FT]].

> [!referencia]
> - Módulo padre: [[index]].
> - Operación inversa: [[Pasar a FT]].
> - Cambio de base y unicidad: [[Forma General]].
> - Representación origen: [[Funcion Transferencia/index]].
