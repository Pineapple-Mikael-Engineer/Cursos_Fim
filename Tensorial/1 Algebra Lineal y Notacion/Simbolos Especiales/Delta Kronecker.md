---
title: Delta de Kronecker
tags:
  - analisis-tensorial
  - teoria
  - notacion-indices
  - delta-kronecker
draft: false
aliases:
  - delta de kronecker
  - propiedad de sustitucion
  - Kronecker delta
---

# Delta de Kronecker $\delta_{ij}$

> [!definicion]
> La **delta de Kronecker** es el arreglo de índices
> $$\delta_{ij}=\begin{cases}1 & i=j\\[2pt] 0 & i\neq j\end{cases}$$
> Es simétrica ($\delta_{ij}=\delta_{ji}$) y, en cartesianas ortonormales, da el producto de los vectores base: $\hat{e}_i\cdot\hat{e}_j=\delta_{ij}$. Su uso central es la **propiedad de sustitución** $A_i\delta_{ij}=A_j$: sumar contra una delta **renombra** el índice.

> [!info]
> Vive en [[index | Símbolos Especiales]] del [[../index | capítulo 1]] (libro, cap. 1.2.2). Usa la [[Notacion Indices Sumatorias | notación de Einstein]]. Su pareja en el producto cruz es [[Simbolo Levi-Civita]]; el producto de dos $\varepsilon$ se reduce a deltas en [[Identidad Epsilon-Delta]].

---

## Ejemplo

> [!ejemplo]
> **Producto punto vía $\delta_{ij}$.** Partiendo de $\vec{A}=A_i\hat{e}_i$ y $\vec{B}=B_j\hat{e}_j$:
> $$\vec{A}\cdot\vec{B}=A_iB_j\,(\hat{e}_i\cdot\hat{e}_j)=A_iB_j\,\delta_{ij}=A_iB_i.$$
> La delta **contrae** $i$ con $j$: de la doble suma sobre $i,j$ sobreviven solo los términos $i=j$, dejando $A_iB_i=A_1B_1+A_2B_2+A_3B_3$, el producto escalar. La base ortonormal es lo único que se usó.

> [!ejemplo]
> **Verificación numérica de la sustitución.** Comprobar $\delta_{2j}a_j=a_2$ en $n=3$, expandiendo la suma sobre $j$:
> $$\delta_{2j}a_j=\delta_{21}a_1+\delta_{22}a_2+\delta_{23}a_3=0\cdot a_1+1\cdot a_2+0\cdot a_3=a_2.$$
> Solo sobrevive el término con $j=2$ (donde $\delta_{2j}=1$). La delta "filtra" la componente cuyo índice iguala al libre: por eso $A_i\delta_{ij}=A_j$.

> [!ejemplo]
> **Traza de una matriz.** La traza de $[A]$ se escribe contrayendo el índice consigo mismo, o equivalentemente con una delta:
> $$\operatorname{tr}(A)=A_{ii}=A_{11}+A_{22}+A_{33}=\delta_{ij}A_{ij}.$$
> En la última forma $\delta_{ij}$ selecciona los elementos diagonales $A_{ij}$ con $i=j$. Como caso particular, la traza de la identidad es $\delta_{ii}=n=3$ en 3D.

---

## En qué consiste

> [!teoria]
> En cartesianas la base es ortonormal: $\hat{e}_i\cdot\hat{e}_j$ vale $1$ si los índices coinciden y $0$ si no, exactamente $\delta_{ij}$. Toda la utilidad operativa de la delta sale de aquí: al expandir cualquier producto punto $A_iB_j(\hat{e}_i\cdot\hat{e}_j)$ aparece $\delta_{ij}$, que colapsa la doble suma a una sola. Como arreglo, $\delta_{ij}$ **son** las componentes de la matriz identidad, $[\delta]=I$.

> [!proposicion] Propiedad de sustitución
> Sumar una cantidad contra $\delta_{ij}$ sobre un índice repetido **renombra** ese índice:
> $$A_i\delta_{ij}=A_j,\qquad T_{ik}\delta_{kj}=T_{ij}.$$
> La delta actúa como un "cambia-índice": consume el índice mudo y lo reemplaza por el otro índice de la delta. Es la manipulación más frecuente con $\delta$ y el paso final de casi toda reducción con la [[Identidad Epsilon-Delta | identidad $\varepsilon$-$\delta$]].

> [!teorema] Propiedades de $\delta_{ij}$
> 1. **Simetría:** $\delta_{ij}=\delta_{ji}$.
> 2. **Sustitución:** $A_i\delta_{ij}=A_j$.
> 3. **Contracción total:** $\delta_{ii}=n$ ($=3$ en 3D).
> 4. **Producto de deltas:** $\delta_{ij}\delta_{jk}=\delta_{ik}$.
> 5. **Identidad:** $[\delta]=I$, es decir $\delta_{ij}=I_{ij}$.

> [!demostracion]
> **Producto de deltas, $\delta_{ij}\delta_{jk}=\delta_{ik}$.**
> *Paso 1.* Por sustitución, $\delta_{jk}$ aplicada a $\delta_{ij}$ renombra el índice mudo $j\to k$ en el segundo subíndice: $\delta_{ij}\delta_{jk}=\delta_{ik}$.
> *Paso 2 (verificación directa).* La suma sobre $j$ tiene un único término no nulo, $j=k$ (donde $\delta_{jk}=1$). Entonces $\delta_{ij}\delta_{jk}=\delta_{ik}\cdot 1=\delta_{ik}$.
> *Corolario.* Contrayendo de nuevo con $\delta_{ki}$: $\delta_{ij}\delta_{jk}\delta_{ki}=\delta_{ik}\delta_{ki}=\delta_{ii}=n$.

## Resumen

> [!resumen]
> | Propiedad | Fórmula | Lectura |
> |---|---|---|
> | Definición | $\delta_{ij}=1$ si $i=j$, $0$ si no | filtro de igualdad |
> | Base | $\hat{e}_i\cdot\hat{e}_j=\delta_{ij}$ | ortonormalidad cartesiana |
> | Sustitución | $A_i\delta_{ij}=A_j$ | renombra el índice |
> | Contracción total | $\delta_{ii}=n=3$ | dimensión del espacio |
> | Producto | $\delta_{ij}\delta_{jk}=\delta_{ik}$ | composición de filtros |
> | Matriz | $[\delta]=I$ | matriz identidad |

> [!corolario]
> $\delta_{ij}$ es el producto punto y la identidad a la vez. En la práctica funciona como un operador de renombrado: cada vez que aparece sumada contra algo, **borra un índice mudo y lo sustituye**. Esa es la operación que cierra toda reducción de índices.

> [!referencia]
> - Símbolo dual (producto cruz): [[Simbolo Levi-Civita]].
> - Producto de dos $\varepsilon$ en términos de $\delta$: [[Identidad Epsilon-Delta]].
> - Notación base: [[Notacion Indices Sumatorias]].
