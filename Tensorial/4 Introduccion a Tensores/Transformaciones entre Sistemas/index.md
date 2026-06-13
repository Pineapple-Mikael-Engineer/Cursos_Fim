---
title: Transformaciones entre Sistemas
tags:
  - analisis-tensorial
  - teoria
  - tensores
  - transformaciones
  - index
draft: false
aliases:
  - transformaciones entre sistemas
  - ley de transformacion tensorial
  - cambio de sistema de coordenadas
  - coordinate transformations
---

# Transformaciones entre Sistemas

> [!definicion]
> Al cambiar de sistema de coordenadas las **componentes** de un vector o tensor cambian, aunque el objeto físico sea el mismo. La ley que rige ese cambio es lo que **define** a un tensor: un objeto es un tensor si, y solo si, sus componentes transforman como
> $$v'_i=a_{ij}v_j,\qquad T'_{ij\dots}=T_{rs\dots}\,a_{ir}a_{js}\dots$$
> con un factor $a_{ij}$ por cada índice. La **matriz de transformación** entre dos sistemas cartesianos ortonormales es
> $$a_{ij}=(\hat e'_i\cdot\hat e_j)=\frac{\partial x'_i}{\partial x_j}.$$

> [!info]
> Es la sección **4.3** del [[../index | capítulo 4]] (libro, cap. 4.3). Solo se tratan transformaciones entre sistemas **ortonormales**; primero cartesianos y luego curvilíneos. Es la sección que da sentido al [[../index | tensor]] como objeto independiente del sistema. Se desglosa en:
> - [[Transformaciones Vectoriales Cartesianas]] — la rotación de un sistema un ángulo $\theta_0$ (cap. 4.3.1).
> - [[Matriz de Transformacion]] — cómo obtener $[a]$ y sus propiedades ortonormales (cap. 4.3.2).
> - [[Transformaciones Tensoriales]] — la ley para tensores de rango $r$; la **definición operativa** (cap. 4.3.4).
> - [[Transformaciones en Curvilineas]] — generalización a bases curvilíneas (cap. 4.5, opcional).

---

## Ejemplo

> [!ejemplo]
> **Mismo vector, distintas componentes.** Un vector $\vec v$ con componentes $(v_1,v_2)=(2,0)$ en un sistema cartesiano se ve, en un sistema rotado $90^\circ$ ($\theta_0=90^\circ$), con componentes
> $$v'_1=v_1\cos 90^\circ+v_2\operatorname{sen}90^\circ=0,\qquad v'_2=-v_1\operatorname{sen}90^\circ+v_2\cos 90^\circ=-2,$$
> es decir $(v'_1,v'_2)=(0,-2)$. El vector apunta a la misma flecha en el espacio; lo único que cambió fue su descripción numérica, porque cambió la base. Esa es toda la idea del capítulo: separar el **objeto** (invariante) de sus **componentes** (dependientes del sistema), y caracterizar la regla $a_{ij}$ que las conecta.

---

## En qué consiste

> [!teoria]
> Muchos textos **definen** un tensor como "un objeto que transforma como un tensor". La frase parece circular, pero es precisa: dado un arreglo de números, no se sabe si es un tensor hasta comprobar que, al rotar el sistema, sus valores cambian según la ley $T'_{ij\dots}=T_{rs\dots}a_{ir}a_{js}\dots$. La notación diádica $T_{ij\dots}\hat e_i\hat e_j\dots$ vuelve **mecánica** esa comprobación: como las bases también transforman, basta sustituir $\hat e_i=a_{ji}\hat e'_j$ y reordenar.
>
> Toda la sección se apoya en una única matriz $[a]$ de **cosenos directores** entre las dos bases. Sus propiedades (ortonormalidad, inversa = transpuesta) se demuestran en [[Matriz de Transformacion]] y se reutilizan para vectores y tensores por igual.

> [!info] Las cuatro ecuaciones de transformación (cartesianas)
> | Objeto | Sistema primado | Sistema no primado |
> |:---|:---|:---|
> | Componentes | $v'_i=a_{ij}v_j$ | $v_i=a_{ji}v'_j$ |
> | Base | $\hat e'_i=a_{ij}\hat e_j$ | $\hat e_i=a_{ji}\hat e'_j$ |
>
> con $a_{ij}=(\hat e'_i\cdot\hat e_j)=\partial x'_i/\partial x_j$. **Patrón:** al pasar del sistema **no primado al primado** se suma sobre el **segundo** índice de $a$; al volver (primado → no primado) se suma sobre el **primero**.

## Resumen

> [!resumen]
> | Subnota | Aporta |
> |---|---|
> | [[Transformaciones Vectoriales Cartesianas]] | rotación $\theta_0$; componentes y matriz $[a]$ |
> | [[Matriz de Transformacion]] | $[a]$ desde bases y desde coordenadas; ortonormalidad |
> | [[Transformaciones Tensoriales]] | ley para rango $r$; definición operativa de tensor |
> | [[Transformaciones en Curvilineas]] | generalización a curvilíneas (opcional) |

> [!corolario]
> La ley de transformación —un factor $a_{ij}$ por índice— es la **marca de identidad** de un tensor y lo que lo vuelve un objeto geométrico de coordenadas independientes. Todo lo demás (matriz de cosenos directores, ortonormalidad, inversa = transpuesta) son herramientas para aplicar esa ley. La [[../Diagonalizacion de Tensores/index | diagonalización]] es, de hecho, buscar el sistema particular donde esa ley deja al tensor en forma diagonal.

> [!referencia]
> - Caso introductorio (rotación 2D): [[Transformaciones Vectoriales Cartesianas]].
> - La matriz $[a]$ y sus propiedades: [[Matriz de Transformacion]].
> - Tensores de cualquier rango: [[Transformaciones Tensoriales]].
> - El objeto que se transforma: [[../index | Introducción a Tensores]].
