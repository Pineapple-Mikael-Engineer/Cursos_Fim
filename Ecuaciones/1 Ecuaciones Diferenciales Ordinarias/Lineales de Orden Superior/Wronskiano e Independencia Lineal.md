---
title: Wronskiano e Independencia Lineal
order: 2
tags:
  - ecuaciones
  - edo
  - teoria
  - lineales
  - wronskiano
draft: false
aliases:
  - wronskiano
  - independencia lineal de soluciones
  - conjunto fundamental
  - Wronskian
  - linear independence
  - fundamental set of solutions
---

# Wronskiano e Independencia Lineal

> [!definicion]
> El **wronskiano** de $n$ funciones derivables $y_1,\dots,y_n$ es el determinante cuyas filas son las funciones y cuyas columnas son las derivadas sucesivas de orden $0,1,\dots,n-1$:
> $$W(y_1,\dots,y_n)(x)=\det\big[y_i^{(j-1)}(x)\big]_{i,j=1}^{n}=
> \begin{vmatrix} y_1 & y_1' & \cdots & y_1^{(n-1)}\\ y_2 & y_2' & \cdots & y_2^{(n-1)}\\
> \vdots & \vdots & & \vdots\\ y_n & y_n' & \cdots & y_n^{(n-1)}\end{vmatrix}.$$
> Para **dos** funciones es simplemente $W(y_1,y_2)=y_1y_2'-y_2y_1'$. Es una función de $x$ que **mide la independencia lineal** de las funciones: cuando son soluciones de una misma EDO lineal, su no anularse equivale a que sean linealmente independientes.

> [!info]
> Pieza central del bloque [[Lineales de Orden Superior/index| lineales de orden superior]]: el [[Operador Diferencial Lineal| operador $L$]] garantiza que el espacio de soluciones de la homogénea tiene dimensión $n$, y el wronskiano es el **test práctico** para saber si $n$ soluciones concretas forman una base —el **conjunto fundamental**—. Su buen comportamiento (la dicotomía "siempre $0$ o nunca $0$") proviene de la [[Formula de Abel| fórmula de Abel]]. Aparece también al construir la solución particular por [[Variacion de Parametros| variación de parámetros]]. Pertenece al **Capítulo 1 — Ecuaciones Diferenciales Ordinarias**.

---

## Ejemplo

> [!ejemplo] Dos exponenciales independientes
> Sean $y_1=e^{x}$ e $y_2=e^{-x}$, soluciones de $y''-y=0$. Entonces
> $$W=y_1y_2'-y_2y_1'=e^{x}\,(-e^{-x})-e^{-x}\,(e^{x})=-1-1=-2\neq0.$$
> Como $W\neq0$ (de hecho constante, porque $p=0$), las dos soluciones son **linealmente independientes** y $\{e^x,e^{-x}\}$ es un conjunto fundamental: la solución general es $y=c_1e^x+c_2e^{-x}$.

> [!ejemplo] Seno y coseno
> Para $y''+y=0$ con $y_1=\cos x$, $y_2=\sin x$:
> $$W=\cos x\cdot(\cos x)-\sin x\cdot(-\sin x)=\cos^2 x+\sin^2 x=1\neq0.$$
> Otra vez $W$ es constante (aquí $=1$) y las soluciones son independientes.

> [!ejemplo] Un caso dependiente
> Sean $y_1=x$ e $y_2=3x$. Geométricamente una es múltiplo de la otra, así que **no** son independientes; el wronskiano lo detecta:
> $$W=y_1y_2'-y_2y_1'=x\cdot3-3x\cdot1=3x-3x=0\quad\text{para todo }x.$$
> $W\equiv0$ y, en efecto, $y_2-3y_1\equiv0$ es una combinación lineal nula no trivial.

---

## En qué consiste

> [!teoria]
> Recordemos que $y_1,\dots,y_n$ son **linealmente independientes** en un intervalo $I$ si la única combinación lineal que se anula idénticamente,
> $$c_1y_1(x)+c_2y_2(x)+\dots+c_ny_n(x)=0\quad\forall x\in I,$$
> es la trivial $c_1=\dots=c_n=0$. Derivando esa identidad $0,1,\dots,n-1$ veces obtenemos un sistema lineal homogéneo en las incógnitas $c_i$ cuya matriz de coeficientes, evaluada en un punto $x_0$, es exactamente la del wronskiano. Por álgebra lineal, ese sistema tiene **solo** la solución trivial cuando su determinante $W(x_0)\neq0$. Esto explica por qué el wronskiano sirve de detector de independencia.

> [!algoritmo] Cómo usar el wronskiano como test
> 1. Comprueba que $y_1,\dots,y_n$ son **soluciones** de la misma EDO lineal homogénea con coeficientes continuos en $I$ (requisito imprescindible, ver el `> [!warning]`).
> 2. Forma la matriz con las funciones en filas y sus derivadas $0,\dots,n-1$ en columnas.
> 3. Calcula el determinante $W(x)$ y evalúalo en **un** punto cómodo $x_0\in I$ (por Abel basta uno).
> 4. Si $W(x_0)\neq0$ las soluciones son independientes y forman un conjunto fundamental; si $W(x_0)=0$ son dependientes.

> [!teorema] Wronskiano e independencia de soluciones
> Sean $y_1,\dots,y_n$ **soluciones** de la EDO lineal homogénea de orden $n$
> $$y^{(n)}+p_{n-1}(x)y^{(n-1)}+\dots+p_0(x)y=0,$$
> con coeficientes $p_j$ continuos en un intervalo $I$. Entonces $y_1,\dots,y_n$ son linealmente independientes en $I$ **si y solo si** $W(y_1,\dots,y_n)(x)\neq0$ en **algún** punto $x_0\in I$ (y por tanto, por la fórmula de Abel, en **todo** punto de $I$).

> [!demostracion]
> **Paso 1 — dependientes $\Rightarrow$ $W\equiv0$.** Si las soluciones son linealmente dependientes, existe una combinación nula no trivial $c_1y_1+\dots+c_ny_n\equiv0$ en $I$. Derivándola $0,1,\dots,n-1$ veces, cada columna del determinante del wronskiano cumple la misma relación lineal con coeficientes $c_i$ no todos nulos; es decir, las **filas** de la matriz $[y_i^{(j-1)}]$ son linealmente dependientes en cada $x$. Un determinante con filas dependientes vale $0$, luego $W(x)=0$ para todo $x\in I$.
>
> **Paso 2 — $W(x_0)\neq0$ $\Rightarrow$ independientes.** Supongamos $W(x_0)\neq0$ y consideremos una combinación nula $\sum_i c_iy_i\equiv0$. Derivando y evaluando en $x_0$ obtenemos el sistema lineal
> $$\big[y_i^{(j-1)}(x_0)\big]^{\!\top}\,(c_1,\dots,c_n)^{\!\top}=\mathbf 0,$$
> cuya matriz tiene determinante $W(x_0)\neq0$. Por ser invertible, la única solución es $c_1=\dots=c_n=0$: las soluciones son linealmente independientes.
>
> **Paso 3 — "algún punto = todo punto".** Por la [[Formula de Abel| fórmula de Abel]] el wronskiano de soluciones cumple $W(x)=W(x_0)\exp\!\big(-\int_{x_0}^{x}p_{n-1}\big)$, y como la exponencial nunca se anula, $W$ es **idénticamente cero** o **nunca cero** en $I$. Por eso basta verificar $W$ en un único punto, y la equivalencia de los Pasos 1–2 se extiende a todo $I$. $\blacksquare$

> [!warning] Sin la hipótesis "soluciones de una EDO lineal" la equivalencia falla
> Para funciones **arbitrarias** (no necesariamente soluciones de una misma EDO lineal), $W\equiv0$ **no** implica dependencia. El contraejemplo clásico es $y_1=x^2$ e $y_2=x\lvert x\rvert$ en $I=\mathbb R$: ambas son $C^1$, su wronskiano es idénticamente $0$, y sin embargo son linealmente **independientes** (en $x>0$ coinciden salvo signo, pero en $x<0$ una es $x^2$ y la otra $-x^2$, así que ninguna constante las relaciona en todo $\mathbb R$). La dicotomía limpia del teorema vale **solo** gracias a la fórmula de Abel, que requiere que las funciones resuelvan la misma ecuación.

> [!proposicion] Conjunto fundamental de soluciones
> Si $y_1,\dots,y_n$ son soluciones independientes de la homogénea de orden $n$ ($W\neq0$), entonces forman un **conjunto fundamental**: toda solución se escribe de manera única como $y=c_1y_1+\dots+c_ny_n$. Esto realiza la base del espacio de soluciones de dimensión $n$ garantizada por el [[Operador Diferencial Lineal| operador lineal]].

## Resumen

> [!resumen]
> | Concepto | Enunciado |
> |---|---|
> | Definición ($n=2$) | $W=y_1y_2'-y_2y_1'$ |
> | Definición general | $W=\det\big[y_i^{(j-1)}\big]$ (funciones en filas, derivadas en columnas) |
> | Test (soluciones de EDO lineal) | independientes $\iff W\neq0$ en algún punto $\iff W\neq0$ en todo $I$ |
> | Dicotomía | $W\equiv0$ o $W$ nunca $0$ (por Abel) |
> | Funciones arbitrarias | $W\equiv0$ **no** implica dependencia ($x^2$ y $x\lvert x\rvert$) |
> | Uso | detectar el conjunto fundamental; base de variación de parámetros |

> [!corolario]
> El wronskiano convierte una pregunta analítica ("¿son estas soluciones una base del espacio?") en un simple cálculo de un determinante en **un** punto. Es la herramienta que certifica que $n$ soluciones son un conjunto fundamental y, por tanto, que su combinación lineal es la solución general.

> [!referencia]
> - Por qué $W$ es siempre $0$ o nunca $0$, y cómo calcularlo sin resolver la EDO: [[Formula de Abel]].
> - El espacio de soluciones de dimensión $n$ y la superposición: [[Operador Diferencial Lineal]].
> - Construir un conjunto fundamental con coeficientes constantes: [[Coeficientes Constantes Homogenea]].
> - Donde el wronskiano se vuelve operativo para hallar $y_p$: [[Variacion de Parametros]].
