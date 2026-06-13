---
title: Pseudo-vectores
tags:
  - analisis-tensorial
  - teoria
  - tensores
  - pseudo-objetos
draft: false
aliases:
  - pseudovector
  - vector axial
  - pseudo-vectores
  - axial vector
---

# Pseudo-vectores

> [!definicion]
> Un **pseudo-vector** (o **vector axial**) transforma como un vector regular **salvo por un factor $|a|$ extra**:
> $$\text{vector regular: } v'_r=v_i\,a_{ri}\qquad\Longleftrightarrow\qquad\text{pseudo-vector: } v'_r=|a|\,v_i\,a_{ri},$$
> con $|a|=\det[a]=\pm1$. El producto cruz $\vec A\times\vec B$ de dos vectores regulares es un pseudo-vector: bajo una **reflexión** ($|a|=-1$) cambia de signo respecto a lo que daría la transformación regular.

> [!info]
> Sección **4.6.1** del libro; parte de [[index | Pseudo-objetos]]. El carácter axial proviene de que el [[Producto Cruz]] se define con la regla de la mano derecha, una convención de orientación. Los vectores regulares se llaman **polares**. Usa la transformación regular de vectores ([[Transformaciones entre Sistemas/index]]) y el [[Simbolo Levi-Civita]].

---

## Ejemplo

> [!ejemplo]
> **El producto cruz transforma con un signo extra.** Se demuestra examinando $\vec A\times\vec B$ en un sistema derecho y en su imagen reflejada.
>
> > [!demostracion]
> > **Paso 1 — Sistema derecho.** Toma $\vec A=A_0\hat e_1$ y $\vec B=B_0\hat e_2$. Con el determinante,
> > $$\vec A\times\vec B=\begin{vmatrix}\hat e_1&\hat e_2&\hat e_3\\A_0&0&0\\0&B_0&0\end{vmatrix}=A_0B_0\,\hat e_3,$$
> > o con Levi-Civita, $(\vec A\times\vec B)_k=\varepsilon_{ijk}A_iB_j$ da $A_0B_0\hat e_3$. La dirección sigue la regla de la mano derecha.
> >
> > **Paso 2 — La reflexión.** Aplica $x'_1=-x_1,\ x'_2=x_2,\ x'_3=x_3$ (inversión simple del eje 1; equivale a reflejar el sistema derecho sobre el plano $x_2x_3$). La matriz de transformación es
> > $$[a]=\begin{pmatrix}-1&0&0\\0&1&0\\0&0&1\end{pmatrix},\qquad |a|=\det[a]=-1.$$
> > El sistema primado es **izquierdo**.
> >
> > **Paso 3 — Transformar el resultado como vector regular.** Aplicando $[a]$ a las componentes de $\vec A\times\vec B=(0,0,A_0B_0)$:
> > $$\begin{pmatrix}-1&0&0\\0&1&0\\0&0&1\end{pmatrix}\begin{pmatrix}0\\0\\A_0B_0\end{pmatrix}=\begin{pmatrix}0\\0\\A_0B_0\end{pmatrix}\ \Longrightarrow\ +A_0B_0\,\hat e'_3.$$
> >
> > **Paso 4 — Recalcular el cruz en el sistema primado.** En el sistema izquierdo, $\vec A=-A_0\hat e'_1$ y $\vec B=B_0\hat e'_2$ (las componentes vienen de aplicar $[a]$ a cada vector). El determinante da
> > $$\vec A\times\vec B=\begin{vmatrix}\hat e'_1&\hat e'_2&\hat e'_3\\-A_0&0&0\\0&B_0&0\end{vmatrix}=-A_0B_0\,\hat e'_3.$$
> >
> > **Paso 5 — La contradicción y su resolución.** El Paso 3 da $+A_0B_0\hat e'_3$ y el Paso 4 da $-A_0B_0\hat e'_3$: **difieren en un signo**. El producto cruz no transforma como un vector regular. Si se incluye el factor $|a|=-1$ en la ley de transformación,
> > $$v'_r=|a|\,v_i\,a_{ri}=(-1)(+A_0B_0)\,\hat e'_3=-A_0B_0\,\hat e'_3,$$
> > coincide con el cálculo directo. **Conclusión:** $\vec A\times\vec B$ es un pseudo-vector.

---

## En qué consiste

> [!teoria]
> La distinción se resume en una sola línea: un vector **regular** (polar) transforma sin $|a|$, un **pseudo-vector** (axial) con $|a|$.
> $$v'_r=v_i\,a_{ri}\quad(\text{regular}),\qquad v'_r=|a|\,v_i\,a_{ri}\quad(\text{pseudo}).$$
> Mientras la transformación sea una rotación o traslación rígida ($|a|=+1$) los dos se comportan igual. Solo bajo una **reflexión** ($|a|=-1$) el pseudo-vector invierte su signo respecto a lo que esperaría un vector polar. La raíz es la regla de la mano derecha del [[Producto Cruz]]: al reflejar el sistema, esa regla deja de aplicar y aparece el signo.

> [!info] Ejemplos físicos de pseudo-vectores
> | Pseudo-vector | Construcción | Por qué es axial |
> |---|---|---|
> | Momento angular $\vec L$ | $\vec L=\vec r\times\vec p$ | producto cruz de dos vectores polares |
> | Torque $\vec\tau$ | $\vec\tau=\vec r\times\vec F$ | ídem |
> | Campo magnético $\vec B$ | $\vec F=q\,\vec v\times\vec B$ | aparece en/como producto cruz |
> | Velocidad angular $\vec\omega$ | $\vec v=\vec\omega\times\vec r$ | ídem |

> [!info] Violación de paridad
> Es tentador ver el factor $|a|$ como un mero artificio de notación del producto cruz, y en muchos casos lo es (al definir $\vec B$ o $\vec L$ se elige implícitamente la orientación del sistema). Pero hay física genuina: existen procesos cuya imagen especular **no** ocurre en la naturaleza. El experimento de **Wu** (1957) mostró que el Cobalto-60 emite partículas beta con preferencia direccional bajo la interacción débil, rompiendo la simetría especular. El análisis de **Lee y Yang** de esta **violación de paridad** —contraria a la lógica común— les valió el premio Nobel.

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Vector regular (polar) | $v'_r=v_i a_{ri}$ |
> | Pseudo-vector (axial) | $v'_r=\|a\|\,v_i a_{ri}$ |
> | Origen | producto cruz $\vec A\times\vec B$ (regla mano derecha) |
> | Bajo rotación ($\|a\|=+1$) | idéntico a un vector regular |
> | Bajo reflexión ($\|a\|=-1$) | cambia de signo |
> | Ejemplos | $\vec B$, $\vec L$, $\vec\tau$, $\vec\omega$ |

> [!corolario]
> El producto cruz de dos vectores polares es un pseudo-vector: arrastra un factor $|a|$ que solo se manifiesta al reflejar el sistema de coordenadas. La física confirma que esto no es pura convención —la violación de paridad (Wu, Lee-Yang) prueba que el universo distingue izquierda de derecha en la interacción débil. La generalización a otros rangos da los [[Pseudo-escalares]] y [[Pseudo-tensores]].

> [!referencia]
> - Producto cruz y su definición: [[Producto Cruz]].
> - Símbolo $\varepsilon_{ijk}$: [[Simbolo Levi-Civita]].
> - Marco general: [[index | Pseudo-objetos]].
