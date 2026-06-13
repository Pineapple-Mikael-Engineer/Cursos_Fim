---
title: Exponencial de una Matriz
tags:
  - ecuaciones
  - edo
  - teoria
  - sistemas
  - exponencial-matriz
draft: false
aliases:
  - exponencial de una matriz
  - matrix exponential
  - e^{At}
---

# Exponencial de una Matriz $e^{At}$

> [!definicion]
> La **exponencial de una matriz** $A$ se define por la misma serie que la exponencial escalar:
> $$e^{At}:=\sum_{k=0}^{\infty}\frac{(At)^k}{k!}=I+At+\frac{(At)^2}{2!}+\dots$$
> (converge para toda $A$). Resuelve el PVI lineal homogéneo de un tirón:
> $$\dot{\mathbf{x}}=A\mathbf{x},\ \mathbf{x}(0)=\mathbf{x}_0\ \Longrightarrow\ \mathbf{x}(t)=e^{At}\mathbf{x}_0.$$
> Es el análogo vectorial del factor $e^{rt}$ escalar.

> [!info]
> Cierra la maquinaria de cálculo del bloque [[Sistemas y Dinamica/index| sistemas y dinámica]]. Es
> la [[Matriz Fundamental| matriz fundamental]] **normalizada** con $\Phi(0)=I$, y la pieza que la
> [[Variacion de Parametros Sistemas| variación de parámetros]] usa en la fórmula de Duhamel. Se
> calcula con los [[Sistemas Lineales Autovalores| autovalores]] de $A$.

---

## Ejemplo

> [!ejemplo] Caso diagonalizable
> **Calcular $e^{At}$ para $A=\begin{pmatrix}1&2\\2&1\end{pmatrix}$.** Autovalores $\lambda=3,-1$ con
> autovectores $\mathbf{v}_1=(1,1),\mathbf{v}_2=(1,-1)$, así $A=PDP^{-1}$ con
> $P=\begin{pmatrix}1&1\\1&-1\end{pmatrix}$, $D=\operatorname{diag}(3,-1)$, $P^{-1}=\tfrac12\begin{pmatrix}1&1\\1&-1\end{pmatrix}$.
> Entonces
> $$e^{At}=P\,e^{Dt}P^{-1}=P\begin{pmatrix}e^{3t}&0\\0&e^{-t}\end{pmatrix}P^{-1}=\frac12\begin{pmatrix}e^{3t}+e^{-t}&e^{3t}-e^{-t}\\ e^{3t}-e^{-t}&e^{3t}+e^{-t}\end{pmatrix}.$$
> La solución del PVI es $\mathbf{x}(t)=e^{At}\mathbf{x}_0$.

> [!ejemplo] Caso deficiente (forma de Jordan)
> **Calcular $e^{At}$ para $A=\begin{pmatrix}2&1\\0&2\end{pmatrix}$.** Se escribe $A=2I+N$ con
> $N=\begin{pmatrix}0&1\\0&0\end{pmatrix}$ **nilpotente** ($N^2=0$). Como $2I$ y $N$ **conmutan**,
> $$e^{At}=e^{2It}\,e^{Nt}=e^{2t}\,(I+Nt)=e^{2t}\begin{pmatrix}1&t\\0&1\end{pmatrix}.$$
> El factor $t$ es la huella del autovalor **repetido deficiente** (mismo origen que en
> [[Sistemas Lineales Autovalores| el autovector generalizado]]). La serie se **corta** porque $N$
> es nilpotente: $e^{Nt}=I+Nt$ exacto.

---

## En qué consiste

> [!teorema] $e^{At}$ resuelve el sistema
> La función $t\mapsto e^{At}$ cumple $\dfrac{d}{dt}e^{At}=A\,e^{At}$ y $e^{A\cdot0}=I$. Por tanto
> $\mathbf{x}(t)=e^{At}\mathbf{x}_0$ es la **única** solución de $\dot{\mathbf{x}}=A\mathbf{x}$ con
> $\mathbf{x}(0)=\mathbf{x}_0$.

> [!demostracion]
> **Paso 1 — derivar la serie término a término** (converge uniformemente en compactos):
> $$\frac{d}{dt}e^{At}=\frac{d}{dt}\sum_{k\ge0}\frac{A^kt^k}{k!}=\sum_{k\ge1}\frac{A^kt^{k-1}}{(k-1)!}=A\sum_{j\ge0}\frac{A^jt^j}{j!}=A\,e^{At}.$$
> **Paso 2 — verificar el PVI.** Con $\mathbf{x}=e^{At}\mathbf{x}_0$: $\dot{\mathbf{x}}=Ae^{At}\mathbf{x}_0=A\mathbf{x}$ y $\mathbf{x}(0)=I\mathbf{x}_0=\mathbf{x}_0$. La unicidad la da [[Existencia y Unicidad Picard| Picard]]. $\blacksquare$

> [!proposicion] Propiedades
> | Propiedad | Enunciado |
> |---|---|
> | Identidad | $e^{A\cdot0}=I$ |
> | Derivada | $\dfrac{d}{dt}e^{At}=Ae^{At}=e^{At}A$ |
> | Suma (si $AB=BA$) | $e^{A+B}=e^Ae^B$ |
> | Inversa | $(e^{At})^{-1}=e^{-At}$ |
> | Semigrupo | $e^{A(t+s)}=e^{At}e^{As}$ |

> [!warning]
> En general $e^{A+B}\neq e^Ae^B$ **si $A$ y $B$ no conmutan**. Por eso no se puede "separar" la
> exponencial de una suma de matrices arbitrarias.

> [!algoritmo] Calcular $e^{At}$
> 1. **Diagonalizable** ($n$ autovectores): $e^{At}=P\,\operatorname{diag}(e^{\lambda_it})\,P^{-1}$.
> 2. **Deficiente**: descompón $A=S+N$ (semisimple + nilpotente que conmutan, forma de Jordan) y usa
>    $e^{At}=e^{St}e^{Nt}$ con $e^{Nt}=\sum_{j<m}\frac{(Nt)^j}{j!}$ (serie finita).
> 3. Alternativa: $e^{At}=\mathcal{L}^{-1}\{(sI-A)^{-1}\}$ (transformada de Laplace).

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Definición | $e^{At}=\sum (At)^k/k!$ |
> | Resuelve | $\dot{\mathbf{x}}=A\mathbf{x}\Rightarrow\mathbf{x}=e^{At}\mathbf{x}_0$ |
> | Diagonalizable | $P\,e^{Dt}P^{-1}$ |
> | Deficiente | $e^{St}e^{Nt}$ (Jordan; serie finita en $N$) |
> | Relación | matriz fundamental con $\Phi(0)=I$ |

> [!corolario]
> $e^{At}$ comprime toda la dinámica lineal en un solo objeto: **propaga** el estado inicial al
> instante $t$. Sus autovalores ($e^{\lambda_it}$) reproducen modo a modo el crecimiento, el
> decaimiento y la rotación que predicen los [[Sistemas Lineales Autovalores| autovalores]] de $A$.

> [!referencia]
> - De dónde salen los autovalores: [[Sistemas Lineales Autovalores]].
> - Versión sin normalizar: [[Matriz Fundamental]].
> - Sistema con fuente: [[Variacion de Parametros Sistemas]].
