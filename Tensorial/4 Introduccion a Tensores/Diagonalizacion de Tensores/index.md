---
title: Diagonalización de Tensores
order: 5
tags:
  - analisis-tensorial
  - teoria
  - tensores
  - diagonalizacion
  - index
draft: false
aliases:
  - diagonalizacion de tensores
  - diagonalizar un tensor
  - ejes donde el tensor es diagonal
  - tensor diagonalization
---

# Diagonalización de Tensores

> [!definicion]
> **Diagonalizar** un tensor $\overleftrightarrow{\sigma}$ es hallar el sistema de coordenadas particular en el que su matriz solo tiene elementos en la **diagonal**:
> $$[\sigma']=\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3)=\begin{pmatrix}\lambda_1&0&0\\0&\lambda_2&0\\0&0&\lambda_3\end{pmatrix}.$$
> No es más que un **cambio de coordenadas**: la matriz de transformación $[a]$ que lleva del sistema original al sistema diagonal está formada por los **autovectores** $\hat e'_i$; los elementos diagonales $\lambda_i$ son los **autovalores**.

> [!info]
> Es la sección **4.4** del [[../index | capítulo 4]] (libro, cap. 4.4). Muchos estudiantes se pierden en el proceso matemático y olvidan que, en el fondo, es solo una transformación de coordenadas: se buscan los elementos de la matriz $[a]$ que diagonaliza un tensor dado. Se desglosa en:
> - [[Valores y Vectores Propios]] — el problema de autovalores/autovectores y la ecuación característica; los **dos ejemplos numéricos** resueltos (cap. 4.4.1).
> - [[Ejes Principales]] — la interpretación física: los autovectores son los ejes donde el tensor no desvía; el elipsoide asociado.

---

## Ejemplo

> [!ejemplo]
> **Por qué importa físicamente.** Un cuerpo rígido **no** experimenta vibraciones al rotar alrededor de cualquiera de tres ejes especiales: aquellos donde el [[../index | tensor]] de inercia es diagonal. Balancear una rueda de automóvil usa este hecho: cuando los ejes de giro no coinciden con esos ejes especiales, se colocan pequeños trozos de metal en la llanta para que sí coincidan y la rueda gire sin vibrar. Diagonalizar el tensor de inercia es, literalmente, encontrar esos ejes de rotación libre.

---

## En qué consiste

> [!teoria]
> Un mismo tensor $\overleftrightarrow{\sigma}$ tiene componentes distintas en cada sistema (ver [[../Transformaciones entre Sistemas/index | transformaciones]]). Entre todos los sistemas hay uno **muy especial** en el que todos los elementos fuera de la diagonal valen cero. Hallarlo equivale a resolver el problema de **valores y vectores propios**: los vectores base de ese sistema son los autovectores (no cambian de dirección al actuar el tensor sobre ellos, solo de magnitud), y los elementos diagonales son los autovalores. El procedimiento —ecuación característica, raíces, sustitución, normalización— se desarrolla en [[Valores y Vectores Propios]].
>
> Conviene recordar que diagonalizar **no** altera el tensor: es el mismo objeto geométrico visto desde una base privilegiada. Por eso los autovalores son **invariantes** bajo rotaciones, mientras que las componentes ordinarias $\sigma_{ij}$ no lo son.

## Resumen

> [!resumen]
> | Subnota | Aporta |
> |---|---|
> | [[Valores y Vectores Propios]] | ecuación característica, autovalores/autovectores, dos ejemplos resueltos |
> | [[Ejes Principales]] | interpretación física: ejes de rotación libre, momentos principales, elipsoide |

> [!corolario]
> Diagonalizar un tensor es solo cambiar de coordenadas a la base de sus **autovectores**, donde la matriz queda $\operatorname{diag}(\lambda_1,\lambda_2,\lambda_3)$. Esa base privilegiada revela la estructura intrínseca del tensor —invariante bajo rotaciones— y, en física, los ejes donde un cuerpo rígido rota sin vibrar.

> [!referencia]
> - El problema de autovalores y su resolución: [[Valores y Vectores Propios]].
> - Interpretación geométrica y física: [[Ejes Principales]].
> - Cómo cambian las componentes entre sistemas: [[../Transformaciones entre Sistemas/index]].
