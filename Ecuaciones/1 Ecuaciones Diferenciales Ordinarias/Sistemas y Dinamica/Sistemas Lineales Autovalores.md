---
title: Sistemas Lineales por Autovalores
tags:
  - ecuaciones
  - edo
  - teoria
  - sistemas
  - autovalores
draft: false
aliases:
  - sistemas lineales autovalores
  - autovalores y autovectores
  - eigenvalue method
  - linear systems
---

# Sistemas Lineales por Autovalores

> [!definicion]
> Para el sistema lineal homogéneo $\dot{\mathbf{x}}=A\mathbf{x}$ ($A$ matriz constante $n\times n$),
> se prueba $\mathbf{x}=\mathbf{v}\,e^{\lambda t}$ y resulta el **problema de autovalores**
> $$(A-\lambda I)\mathbf{v}=\mathbf{0}.$$
> Cada **autovalor** $\lambda$ (raíz de $\det(A-\lambda I)=0$) con su **autovector** $\mathbf{v}$ da
> un modo $\mathbf{v}\,e^{\lambda t}$. Si $A$ es diagonalizable, la solución general es
> $\mathbf{x}=\sum_i c_i\,\mathbf{v}_i\,e^{\lambda_i t}$.

> [!info]
> El método de cálculo del bloque [[Sistemas y Dinamica/index| sistemas y dinámica]]. Es el análogo
> vectorial de la [[Coeficientes Constantes Homogenea| ecuación característica]] escalar: allí
> $e^{rt}$, aquí $\mathbf{v}\,e^{\lambda t}$. Los autovalores fijan también el **tipo de equilibrio**
> en el [[Puntos de Equilibrio y Plano de Fase| plano de fase]], y se empaquetan en la
> [[Exponencial de una Matriz| exponencial de matriz]].

---

## Ejemplo

> [!ejemplo] Autovalores reales distintos (una silla)
> **Resolver $\dot{\mathbf{x}}=\begin{pmatrix}1&2\\2&1\end{pmatrix}\mathbf{x}$.**
> **Paso 1 — autovalores:** $\det(A-\lambda I)=(1-\lambda)^2-4=0\Rightarrow\lambda=3,\,-1$.
> **Paso 2 — autovectores:** para $\lambda=3$, $(A-3I)\mathbf{v}=\begin{pmatrix}-2&2\\2&-2\end{pmatrix}\mathbf{v}=0\Rightarrow\mathbf{v}_1=(1,1)$; para $\lambda=-1$, $\mathbf{v}_2=(1,-1)$.
> **Paso 3 — solución general:**
> $$\mathbf{x}=c_1\begin{pmatrix}1\\1\end{pmatrix}e^{3t}+c_2\begin{pmatrix}1\\-1\end{pmatrix}e^{-t}.$$
> Como los autovalores tienen **signos opuestos**, el equilibrio es una **silla**: las trayectorias
> entran por la dirección de $\mathbf{v}_2$ ($e^{-t}$, decae) y salen por la de $\mathbf{v}_1$.

> [!ejemplo] Autovalores complejos (un foco/espiral)
> **Resolver $\dot{\mathbf{x}}=\begin{pmatrix}-1&-2\\2&-1\end{pmatrix}\mathbf{x}$.** Autovalores:
> $(-1-\lambda)^2+4=0\Rightarrow\lambda=-1\pm 2i$. Un autovector para $\lambda=-1+2i$ es
> $\mathbf{v}=(1,\,-i)$, así $\mathbf{x}=(1,-i)\,e^{(-1+2i)t}$. Tomando partes real e imaginaria
> (ambas son soluciones reales), con $e^{2it}=\cos2t+i\operatorname{sen}2t$:
> $$\mathbf{x}=e^{-t}\!\left[c_1\begin{pmatrix}\cos2t\\ \operatorname{sen}2t\end{pmatrix}+c_2\begin{pmatrix}\operatorname{sen}2t\\ -\cos2t\end{pmatrix}\right].$$
> Parte real $-1<0$ → **espiral que entra** (foco estable); la parte imaginaria $2$ da la rotación.

> [!ejemplo] Autovalor repetido deficiente (autovector generalizado)
> **Resolver $\dot{\mathbf{x}}=\begin{pmatrix}2&1\\0&2\end{pmatrix}\mathbf{x}$.** $\lambda=2$ doble,
> pero solo **un** autovector $\mathbf{v}=(1,0)$. Se busca un **autovector generalizado** $\mathbf{w}$
> con $(A-2I)\mathbf{w}=\mathbf{v}$: $\begin{pmatrix}0&1\\0&0\end{pmatrix}\mathbf{w}=(1,0)\Rightarrow\mathbf{w}=(0,1)$. La segunda solución gana un factor $t$:
> $$\mathbf{x}=c_1\begin{pmatrix}1\\0\end{pmatrix}e^{2t}+c_2\left[\begin{pmatrix}1\\0\end{pmatrix}t+\begin{pmatrix}0\\1\end{pmatrix}\right]e^{2t}.$$

---

## En qué consiste

> [!teorema] La sustitución $\mathbf{v}e^{\lambda t}$ y el problema de autovalores
> $\mathbf{x}=\mathbf{v}\,e^{\lambda t}$ (con $\mathbf{v}\neq\mathbf{0}$) resuelve
> $\dot{\mathbf{x}}=A\mathbf{x}$ **si y solo si** $\lambda$ es autovalor de $A$ y $\mathbf{v}$ un
> autovector asociado.

> [!demostracion]
> **Paso 1 — derivar.** $\dot{\mathbf{x}}=\lambda\mathbf{v}\,e^{\lambda t}$.
> **Paso 2 — sustituir.** $\dot{\mathbf{x}}=A\mathbf{x}$ exige $\lambda\mathbf{v}\,e^{\lambda t}=A\mathbf{v}\,e^{\lambda t}$; como $e^{\lambda t}\neq0$, $A\mathbf{v}=\lambda\mathbf{v}$, esto es $(A-\lambda I)\mathbf{v}=\mathbf{0}$.
> **Paso 3 — no trivialidad.** Para que exista $\mathbf{v}\neq\mathbf{0}$ hace falta $\det(A-\lambda I)=0$ (el **polinomio característico** de $A$). $\blacksquare$

> [!proposicion] Lectura de los casos (2×2)
> | Autovalores | Solución | Equilibrio |
> |:--|:--|:--|
> | reales mismo signo | $c_1\mathbf{v}_1e^{\lambda_1t}+c_2\mathbf{v}_2e^{\lambda_2t}$ | **nodo** (estable si $<0$) |
> | reales signo opuesto | íd. | **silla** (inestable) |
> | complejos $\alpha\pm i\beta$, $\alpha\neq0$ | $e^{\alpha t}(\dots\cos,\dots\operatorname{sen})$ | **foco/espiral** |
> | imaginarios puros $\pm i\beta$ | oscilación sin decaer | **centro** |
> | repetido deficiente | con autovector generalizado ($t\,e^{\lambda t}$) | nodo impropio |

> [!demostracion] Caso complejo: extraer soluciones reales
> Si $\lambda=\alpha+i\beta$ con autovector $\mathbf{v}=\mathbf{a}+i\mathbf{b}$, entonces
> $\mathbf{z}(t)=\mathbf{v}\,e^{\lambda t}$ es una solución **compleja**. Como $A$ es real, sus partes
> real e imaginaria, $\mathrm{Re}\,\mathbf{z}$ e $\mathrm{Im}\,\mathbf{z}$, son cada una solución
> **real** e independiente. Desarrollando con $e^{\lambda t}=e^{\alpha t}(\cos\beta t+i\operatorname{sen}\beta t)$ se obtienen las dos soluciones reales del ejemplo. $\blacksquare$

> [!demostracion] Caso repetido deficiente: el autovector generalizado
> Si $\lambda$ es doble pero solo hay un autovector $\mathbf{v}$, se prueba
> $\mathbf{x}_2=(\mathbf{v}\,t+\mathbf{w})e^{\lambda t}$. Sustituyendo en $\dot{\mathbf{x}}=A\mathbf{x}$
> y agrupando potencias de $t$: el término en $t$ pide $A\mathbf{v}=\lambda\mathbf{v}$ (ya se cumple) y
> el término constante pide $(A-\lambda I)\mathbf{w}=\mathbf{v}$. Ese $\mathbf{w}$ es el **autovector
> generalizado**; siempre existe para una raíz doble deficiente. $\blacksquare$

> [!algoritmo] Resolver $\dot{\mathbf{x}}=A\mathbf{x}$
> 1. Autovalores: $\det(A-\lambda I)=0$.
> 2. Para cada $\lambda$, autovector(es) de $(A-\lambda I)\mathbf{v}=\mathbf{0}$.
> 3. Modos: real → $\mathbf{v}e^{\lambda t}$; complejo → partes real/imaginaria; deficiente →
>    autovector generalizado con factor $t$.
> 4. Combina con $n$ constantes; fíjalas con $\mathbf{x}(0)=\mathbf{x}_0$.

## Resumen

> [!resumen]
> | Paso | Acción |
> |---|---|
> | Autovalores | $\det(A-\lambda I)=0$ |
> | Autovectores | $(A-\lambda I)\mathbf{v}=\mathbf{0}$ |
> | Complejo | partes real e imaginaria de $\mathbf{v}e^{\lambda t}$ |
> | Repetido deficiente | $(A-\lambda I)\mathbf{w}=\mathbf{v}$, factor $t$ |
> | General | $\mathbf{x}=\sum c_i\mathbf{x}_i$ |

> [!corolario]
> Los **autovalores de $A$ son el sistema**: su parte real dice si los modos crecen o decaen, su
> parte imaginaria si rotan, y su patrón de signos clasifica el equilibrio (nodo, silla, foco,
> centro). Diagonalizar $A$ es desacoplar el sistema en $n$ ecuaciones escalares independientes.

> [!referencia]
> - Empaquetar la solución: [[Matriz Fundamental]] y [[Exponencial de una Matriz]].
> - Qué dibujan los autovalores: [[Puntos de Equilibrio y Plano de Fase]].
> - Análogo escalar: [[Coeficientes Constantes Homogenea]].
