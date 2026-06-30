---
title: Ejes Principales
order: 2
tags:
  - analisis-tensorial
  - teoria
  - tensores
  - diagonalizacion
  - ejes-principales
draft: false
aliases:
  - ejes principales
  - momentos principales
  - elipsoide del tensor
  - principal axes
---

# Ejes Principales

> [!definicion]
> Los **ejes principales** de un tensor $\overleftrightarrow{\sigma}$ son las direcciones de sus **autovectores** $\hat e'_1,\hat e'_2,\hat e'_3$. A lo largo de ellos el tensor **no desvía**: un vector aplicado en esa dirección sale en la misma dirección, solo escalado por el autovalor $\lambda_i$,
> $$\overleftrightarrow{\sigma}\cdot\hat e'_i=\lambda_i\,\hat e'_i.$$
> En esa base el tensor es diagonal, $[\sigma']=\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3)$. Para el **tensor de inercia**, los ejes principales son los ejes de **rotación libre** (sin vibración) y los autovalores son los **momentos principales** de inercia.

> [!info]
> Es la lectura geométrica y física de la [[index | diagonalización]] (libro, cap. 4.4). Mientras [[Valores y Vectores Propios]] da el **cómo** (resolver el problema de autovalores), esta nota da el **qué significa**: por qué esos ejes son especiales y qué representa el elipsoide asociado al tensor.
>
> ![[elipsoide_inercia.svg|420]]
>
> Elipsoide del tensor: sus semiejes coinciden con los ejes principales (autovectores); a lo largo de ellos el tensor solo escala (autovalor), no desvía.

---

## Ejemplo

> [!ejemplo] Interpretar los ejes principales del Ejemplo 1
> Para el tensor no degenerado de [[Valores y Vectores Propios]],
> $$[\sigma]=\begin{pmatrix}10&0&0\\0&10&1\\0&1&10\end{pmatrix},$$
> los autovectores hallados fueron
> $$\hat e'_1=\tfrac1{\sqrt2}(\hat e_2-\hat e_3),\qquad \hat e'_2=\tfrac1{\sqrt2}(\hat e_2+\hat e_3),\qquad \hat e'_3=\hat e_1,$$
> con autovalores $\lambda_1=9,\ \lambda_2=11,\ \lambda_3=10$.
>
> **Lectura.** El término fuera de la diagonal ($\sigma_{23}=\sigma_{32}=1$) acopla las direcciones $2$ y $3$: un campo a lo largo de $\hat e_2$ produce algo de corriente a lo largo de $\hat e_3$, es decir, **desvía**. Pero a lo largo de las diagonales del plano $2$-$3$ ese acoplamiento desaparece:
> - Aplicar el tensor a $\hat e'_1=\tfrac1{\sqrt2}(\hat e_2-\hat e_3)$ devuelve $9\,\hat e'_1$: misma dirección, escalada por $9$.
> - Aplicar a $\hat e'_2=\tfrac1{\sqrt2}(\hat e_2+\hat e_3)$ devuelve $11\,\hat e'_2$.
> - La dirección $\hat e_1$ ya estaba desacoplada: $\hat e'_3=\hat e_1$ con autovalor $10$.
>
> Esas tres direcciones son los **ejes principales**. En ellas la respuesta es pura escala (sin desvío). El **elipsoide** del tensor tiene sus semiejes a lo largo de $\hat e'_1,\hat e'_2,\hat e'_3$, con longitudes ligadas a $\lambda_1,\lambda_2,\lambda_3$.

---

## En qué consiste

> [!teoria]
> La ecuación $\overleftrightarrow{\sigma}\cdot\hat e'_i=\lambda_i\hat e'_i$ dice que sobre el autovector el tensor actúa como un **escalar** $\lambda_i$: no hay rotación de la dirección, solo cambio de magnitud. Fuera de los ejes principales, en cambio, el tensor mezcla componentes (los términos $\sigma_{ij}$ con $i\neq j$) y el vector de salida apunta en otra dirección que el de entrada. Por eso los ejes principales son las **direcciones propias** del objeto, independientes del sistema de coordenadas con que se describió originalmente.
>
> En mecánica del cuerpo rígido, $\overleftrightarrow{\sigma}$ es el **tensor de inercia** $\overleftrightarrow{I}$. Sus ejes principales son los ejes alrededor de los cuales el cuerpo gira sin generar pares de reacción ni vibraciones; los autovalores $\lambda_i$ son los **momentos principales** de inercia. Balancear una rueda es, justamente, conseguir que el eje de giro coincida con un eje principal.

> [!info] El elipsoide del tensor
> A un tensor simétrico se le asocia una superficie cuádrica, el **elipsoide del tensor**, definido por $\sigma_{ij}x_ix_j=\text{cte}$. Sus propiedades:
> 
> | Elemento del elipsoide | Significado tensorial |
> |---|---|
> | direcciones de los semiejes | ejes principales (autovectores $\hat e'_i$) |
> | longitudes de los semiejes | ligadas a los autovalores $\lambda_i$ |
> | a lo largo de un semieje | el tensor solo escala, no desvía |
>
> El elipsoide es el mismo objeto en cualquier sistema; al diagonalizar, sus ejes se **alinean** con los de coordenadas y la ecuación se reduce a $\lambda_1 x'^2_1+\lambda_2 x'^2_2+\lambda_3 x'^2_3=\text{cte}$.

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Ejes principales | direcciones de los autovectores $\hat e'_i$ |
> | Acción del tensor sobre ellos | $\overleftrightarrow{\sigma}\cdot\hat e'_i=\lambda_i\hat e'_i$ (escala, no desvía) |
> | Tensor de inercia | ejes de rotación libre; $\lambda_i$ = momentos principales |
> | Elipsoide | semiejes a lo largo de los ejes principales |
> | Invariancia | los ejes principales no dependen del sistema original |

> [!corolario]
> Los ejes principales son las direcciones propias de un tensor: a lo largo de ellas actúa como un simple escalar (el autovalor) y el elipsoide asociado tiene ahí sus semiejes. Son, físicamente, los ejes de rotación libre de un cuerpo rígido. Hallarlos es el contenido operativo de [[Valores y Vectores Propios]]; interpretarlos es el cierre de la [[index | diagonalización]].

> [!referencia]
> - Cómo se calculan (autovalores/autovectores): [[Valores y Vectores Propios]].
> - Marco de la diagonalización: [[index | Diagonalización de Tensores]].
> - El tensor como objeto independiente del sistema: [[../index | Introducción a Tensores]].
