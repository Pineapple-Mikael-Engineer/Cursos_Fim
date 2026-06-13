---
title: Contravarianza y Covarianza de Derivadas Parciales
tags:
  - analisis-tensorial
  - teoria
  - coordenadas-no-ortogonales
  - covarianza
draft: false
aliases:
  - derivada parcial covariante
  - gradiente contravariante
  - partial derivatives covariant contravariant
---

# Contravarianza y Covarianza de Derivadas Parciales

> [!definicion]
> Una derivada parcial respecto a una coordenada **contravariante** $\partial/\partial x^i$ produce una cantidad **covariante**: el superíndice "en el denominador" actúa como **subíndice**.
> $$\frac{\partial}{\partial x^i}\ \longrightarrow\ \text{transforma como cantidad covariante }(\,\cdot\,)_i.$$
> Simétricamente, derivar respecto a una coordenada covariante daría una cantidad contravariante. Es la regla que fija la posición de los índices de $\vec\nabla$.

> [!info]
> Es el cap. 5.2.7 del libro (Rogan & Muñoz). Completa la maquinaria de [[Covarianza Contravarianza en Tensores]] aplicándola al **operador derivada**. Las matrices de cambio son $t^i{}_j=\partial x'^i/\partial x^j$ y $g^j{}_i=\partial x^j/\partial x'^i$ (ver [[Transformaciones Contravariantes]] · [[Transformaciones Covariantes]]). Ver el [[index | índice del capítulo 5]].
>
> **Notación.** Contravariante = superíndice, covariante = subíndice. La regla del "denominador": un superíndice en el denominador de una derivada cuenta como **subíndice** (y viceversa), por lo que $\partial/\partial x^i$ es un objeto **covariante**.

---

## Ejemplo

> [!ejemplo] El campo eléctrico $\vec E=-\vec\nabla\varphi$
> Un campo eléctrico estático se obtiene del gradiente de un potencial escalar:
> $$\vec E=-\vec\nabla\varphi.$$
>
> **Paso 1 — El gradiente sale en base contravariante.** El gradiente se define por $d\varphi=\vec\nabla\varphi\cdot d\vec r$, con el desplazamiento $d\vec r=dx^i\,\hat g_i$ ($dx^i$ es contravariante). Para que la contracción funcione, $\vec\nabla\varphi$ debe escribirse sobre la **base dual** $\hat g^i$:
> $$\vec\nabla\varphi=\frac{\partial\varphi}{\partial x^i}\,\hat g^i.$$
>
> **Paso 2 — Verificación.** Sustituyendo en $\vec\nabla\varphi\cdot d\vec r$ y usando $\hat g^i\cdot\hat g_j=\delta^i{}_j$:
> $$\vec\nabla\varphi\cdot d\vec r=\frac{\partial\varphi}{\partial x^i}\,\hat g^i\cdot dx^j\,\hat g_j
> =\frac{\partial\varphi}{\partial x^i}\,dx^j\,\delta^i{}_j
> =\frac{\partial\varphi}{\partial x^i}\,dx^i
> =d\varphi.\ ✓$$
>
> **Paso 3 — Componentes covariantes del campo.** De $\vec E=-\vec\nabla\varphi$, las componentes son
> $$E_i=-\frac{\partial\varphi}{\partial x^i},$$
> que son **covariantes** (subíndice, porque el denominador lleva el superíndice $x^i$) y por tanto transforman como
> $$E'_i=g^j{}_i\,E_j.$$

---

## En qué consiste

> [!teoria] La regla del "denominador"
> En las matrices de transformación, la componente con superíndice en el **denominador** de la derivada actúa como un subíndice (ej. $t^i{}_j=\partial x'^i/\partial x^j$, $g^i{}_j=\partial x^i/\partial x'^j$). Esto es una propiedad general: una derivada parcial respecto a una **cantidad contravariante** produce un **resultado covariante**, y respecto a una cantidad covariante produce un resultado contravariante. Para mantener la consistencia de la notación arriba/abajo, se impone como **regla**: un superíndice en el denominador cuenta abajo, un subíndice en el denominador cuenta arriba.

> [!teorema] $\partial/\partial x^i$ transforma como cantidad covariante
> El operador $\partial/\partial x^i$ es covariante: bajo cambio de coordenadas sigue la misma ley que las componentes covariantes de un vector.

> [!demostracion]
> **Paso 1 — Regla de la cadena.** Sean $x^i$ y $x'^i$ las coordenadas contravariantes de dos sistemas. El cálculo exige
> $$\frac{\partial}{\partial x'^i}=\frac{\partial x^j}{\partial x'^i}\,\frac{\partial}{\partial x^j},$$
> con suma implícita sobre $j$.
>
> **Paso 2 — Identificar la matriz.** El factor $\partial x^j/\partial x'^i$ es **exactamente** la definición de $g^j{}_i$ (la matriz de transformación covariante). Por tanto
> $$\frac{\partial}{\partial x'^i}=g^j{}_i\,\frac{\partial}{\partial x^j}.$$
>
> **Paso 3 — Comparar.** Esta es **idéntica** a la ley de transformación de una cantidad covariante $v'_i=g^j{}_i\,v_j$ (ver [[Transformaciones Covariantes]]). Luego la operación $\partial/\partial x^i$ transforma como un objeto covariante: lleva subíndice. $\blacksquare$
>
> **Caso recíproco.** Análogamente, $\dfrac{\partial}{\partial x'_i}=\dfrac{\partial x_j}{\partial x'_i}\,\dfrac{\partial}{\partial x_j}=t^i{}_j\,\dfrac{\partial}{\partial x_j}$, que es la ley **contravariante**: derivar respecto a una coordenada covariante da una cantidad contravariante.

---

## Resumen

> [!resumen]
> | Operación | Naturaleza | Ley de transformación |
> |---|---|---|
> | $\partial/\partial x^i$ (denom. contravariante) | covariante | $\dfrac{\partial}{\partial x'^i}=g^j{}_i\dfrac{\partial}{\partial x^j}$ |
> | $\partial/\partial x_i$ (denom. covariante) | contravariante | $\dfrac{\partial}{\partial x'_i}=t^i{}_j\dfrac{\partial}{\partial x_j}$ |
> | Gradiente | base dual $\hat g^i$ | $\vec\nabla\varphi=\dfrac{\partial\varphi}{\partial x^i}\hat g^i$ |
> | Campo eléctrico | componentes covariantes | $E_i=-\dfrac{\partial\varphi}{\partial x^i}$, $\ E'_i=g^j{}_i E_j$ |

> [!corolario]
> El operador derivada invierte la posición del índice: $\partial/\partial x^i$ es covariante porque el superíndice del denominador cuenta como subíndice. De ahí que el gradiente $\vec\nabla\varphi=(\partial\varphi/\partial x^i)\hat g^i$ viva en la base dual y que las componentes del campo $E_i=-\partial\varphi/\partial x^i$ sean covariantes, transformando con $g^j{}_i$.

> [!referencia]
> - Tensores con índices co/contra y la métrica que los conecta: [[Covarianza Contravarianza en Tensores]].
> - Las matrices $t$ y $g$: [[Transformaciones Contravariantes]] · [[Transformaciones Covariantes]].
> - La base dual $\hat g^i$ del gradiente: [[Metrica/Tensor Metrico]].
