---
title: Matriz Fundamental
tags:
  - ecuaciones
  - edo
  - teoria
  - sistemas
  - matriz-fundamental
draft: false
aliases:
  - matriz fundamental
  - wronskiano matricial
  - matriz de transición de estados
  - fundamental matrix
  - state transition matrix
---

# Matriz Fundamental

> [!definicion]
> Una **matriz fundamental** $\Phi(t)$ del sistema lineal homogéneo $\dot{\mathbf{x}}=A(t)\mathbf{x}$ es
> la matriz $n\times n$ cuyas **columnas** son $n$ soluciones linealmente independientes:
> $$\Phi(t)=\big[\,\mathbf{x}_1(t)\ \ \mathbf{x}_2(t)\ \cdots\ \mathbf{x}_n(t)\,\big].$$
> Cumple la **ecuación matricial** $\dot\Phi=A\Phi$ y $\det\Phi(t)\neq0$ (el **wronskiano matricial**).
> La solución general es $\mathbf{x}(t)=\Phi(t)\,\mathbf{c}$ con $\mathbf{c}$ constante, y el problema de
> valor inicial $\mathbf{x}(t_0)=\mathbf{x}_0$ se resuelve de un golpe:
> $$\mathbf{x}(t)=\Phi(t)\,\Phi(t_0)^{-1}\mathbf{x}_0.$$

> [!info]
> Es la forma de **empaquetar** todas las soluciones del bloque
> [[Sistemas y Dinamica/index| sistemas y dinámica]] en un solo objeto: en vez de arrastrar
> combinaciones $\sum c_i\mathbf{x}_i$, se multiplica por una matriz. Sus columnas salen del método de
> [[Sistemas Lineales Autovalores| autovalores]]; cuando se normaliza con $\Phi(t_0)=I$ coincide con la
> [[Exponencial de una Matriz| exponencial de matriz]] $e^{A(t-t_0)}$, y es el ingrediente de la
> [[Variacion de Parametros Sistemas| variación de parámetros]] para el caso no homogéneo. Pertenece al
> [[1 Ecuaciones Diferenciales Ordinarias/index| capítulo de EDO]].

---

## Ejemplo

> [!ejemplo] Construirla a partir de autovalores
> **Armar una matriz fundamental de $\dot{\mathbf{x}}=A\mathbf{x}$ con $A=\begin{pmatrix}1&2\\2&1\end{pmatrix}$.**
> **Paso 1 — modos.** De [[Sistemas Lineales Autovalores]]: $\lambda_1=3$ con $\mathbf{v}_1=(1,1)$ y $\lambda_2=-1$ con $\mathbf{v}_2=(1,-1)$. Las dos soluciones independientes son $\mathbf{v}_1e^{3t}$ y $\mathbf{v}_2e^{-t}$.
> **Paso 2 — colocarlas como columnas.**
> $$\Phi(t)=\begin{pmatrix}e^{3t}&e^{-t}\\[2pt]e^{3t}&-e^{-t}\end{pmatrix}.$$
> **Paso 3 — verificar.** $\det\Phi=-e^{3t}e^{-t}-e^{3t}e^{-t}=-2e^{2t}\neq0$ para todo $t$, así que las columnas son independientes y $\Phi$ es fundamental. La solución general es $\mathbf{x}=\Phi(t)\mathbf{c}$.
> **Paso 4 — un PVI.** Para $\mathbf{x}(0)=(2,0)$: $\Phi(0)=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$, $\Phi(0)^{-1}=\tfrac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}$, luego $\mathbf{c}=\Phi(0)^{-1}(2,0)^{\!\top}=(1,1)$ y $\mathbf{x}(t)=\Phi(t)(1,1)^{\!\top}=\big(e^{3t}+e^{-t},\ e^{3t}-e^{-t}\big)$.

---

## En qué consiste

> [!teoria]
> Una solución del sistema es un **vector que evoluciona**; la matriz fundamental reúne una **base**
> del espacio de soluciones (de dimensión $n$) en sus columnas. Como $\dot{\mathbf{x}}_i=A\mathbf{x}_i$
> para cada columna, apilando las igualdades se obtiene $\dot\Phi=A\Phi$: $\Phi$ resuelve la **misma**
> ecuación, pero matricial. La condición $\det\Phi\neq0$ es la independencia lineal de las columnas, y
> permite invertir $\Phi$ para fijar las constantes de cualquier dato inicial sin volver a resolver.

> [!teorema] Abel–Liouville (wronskiano matricial)
> El determinante $W(t)=\det\Phi(t)$ satisface la EDO escalar de primer orden
> $$\frac{d}{dt}\det\Phi=\operatorname{tr}\!\big(A(t)\big)\,\det\Phi,$$
> de donde $W(t)=W(t_0)\exp\!\Big(\int_{t_0}^{t}\operatorname{tr}A(s)\,ds\Big)$. En consecuencia
> $\det\Phi(t)$ **o es idénticamente cero, o nunca se anula**: basta comprobar la independencia en **un**
> instante para garantizarla en todos.

> [!demostracion]
> **Paso 1 — derivada de un determinante.** Para una matriz $\Phi(t)$, derivar el determinante equivale a
> sumar los determinantes obtenidos al derivar **una fila a la vez**:
> $\dfrac{d}{dt}\det\Phi=\sum_{i=1}^{n}\det\Phi^{(i)}$, donde $\Phi^{(i)}$ es $\Phi$ con su fila $i$ reemplazada por su derivada.
> **Paso 2 — usar la ecuación.** De $\dot\Phi=A\Phi$, la fila $i$ derivada es $\sum_k a_{ik}\,(\text{fila }k\text{ de }\Phi)$. Sustituyéndola, el determinante $\det\Phi^{(i)}$ recibe la fila $k=i$ con peso $a_{ii}$; los términos $k\neq i$ ponen un múltiplo de otra fila ya presente y **dan determinante nulo**.
> **Paso 3 — sumar.** Solo sobrevive el término diagonal: $\det\Phi^{(i)}=a_{ii}\det\Phi$. Sumando en $i$,
> $\dfrac{d}{dt}\det\Phi=\big(\textstyle\sum_i a_{ii}\big)\det\Phi=\operatorname{tr}(A)\det\Phi$.
> **Paso 4 — integrar.** Es una EDO lineal escalar; su solución es la exponencial de la traza. Como la exponencial nunca se anula, $W(t)$ tiene el signo de $W(t_0)$ para siempre. $\blacksquare$

> [!proposicion] No es única, pero la transición sí
> Si $\Phi$ es fundamental y $C$ es una matriz constante invertible, entonces $\Phi C$ **también** es
> fundamental (reordena/combina la base). Sin embargo, la combinación que aparece en el PVI,
> $\Phi(t)\Phi(t_0)^{-1}$, **no depende** de qué $\Phi$ se eligió: $(\Phi C)(\Phi(t_0)C)^{-1}=\Phi(t)\Phi(t_0)^{-1}$. Esa matriz tiene significado físico propio.

> [!info] Matriz de transición de estados
> La matriz $\boxed{\;\Psi(t,t_0)=\Phi(t)\,\Phi(t_0)^{-1}\;}$ se llama **matriz de transición de estados**:
> **propaga** el estado desde $t_0$ a $t$ mediante $\mathbf{x}(t)=\Psi(t,t_0)\mathbf{x}_0$. Cumple
> $\Psi(t_0,t_0)=I$ y la propiedad de semigrupo $\Psi(t_2,t_1)\Psi(t_1,t_0)=\Psi(t_2,t_0)$. Cuando $A$ es
> **constante** coincide con [[Exponencial de una Matriz| $e^{A(t-t_0)}$]]: la exponencial **es** la
> matriz fundamental normalizada con $\Phi(t_0)=I$.

## Resumen

> [!resumen]
> | Concepto | Fórmula |
> |---|---|
> | Definición | columnas = $n$ soluciones independientes |
> | Ecuación | $\dot\Phi=A\Phi$, $\det\Phi\neq0$ |
> | Solución general | $\mathbf{x}=\Phi(t)\mathbf{c}$ |
> | PVI | $\mathbf{x}=\Phi(t)\Phi(t_0)^{-1}\mathbf{x}_0$ |
> | Abel–Liouville | $\frac{d}{dt}\det\Phi=\operatorname{tr}(A)\det\Phi$ |
> | Transición | $\Psi(t,t_0)=\Phi(t)\Phi(t_0)^{-1}$; con $A$ cte $=e^{A(t-t_0)}$ |

> [!corolario]
> La matriz fundamental convierte "resolver el sistema" en "**multiplicar por una matriz**". Una vez
> conocida $\Phi$, todo PVI se contesta con un producto $\Phi(t)\Phi(t_0)^{-1}\mathbf{x}_0$, sin volver a
> integrar. El teorema de Abel garantiza que la independencia de las columnas es una propiedad de **todo
> el intervalo**, no de un instante suelto.

> [!referencia]
> - De dónde salen las columnas: [[Sistemas Lineales Autovalores]].
> - La normalizada $\Phi(t_0)=I$: [[Exponencial de una Matriz]].
> - Su uso con fuente: [[Variacion de Parametros Sistemas]].
> - Volver al mapa del bloque: [[Sistemas y Dinamica/index]].
