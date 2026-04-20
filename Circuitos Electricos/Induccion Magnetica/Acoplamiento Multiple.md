---
title: Matriz de Voltajes en un Sistema de Inductancias Acopladas
tags:
  - inductancia
  - acoplamiento_multiple
  - matriz_voltajes
  - sistemas_lineales
draft: true
---

# Matriz de Voltajes en un Sistema de Inductores Acoplados

Considérese un sistema formado por $n$ inductores acoplados linealmente.

La relación fundamental entre flujos y corrientes es:

$$
\boldsymbol{\Phi} = \mathbf{L}\mathbf{I}
$$

donde:

- $\mathbf{L}$ es la matriz de inductancias (simétrica y definida positiva).
- $\mathbf{I}$ es el vector de corrientes.

---

# 1) Ley de Faraday

El voltaje inducido en cada inductor es:

$$
v_i = \frac{d\Phi_i}{dt}
$$

En forma vectorial:

$$
\mathbf{v} = \frac{d\boldsymbol{\Phi}}{dt}
$$

Si $\mathbf{L}$ es constante:

$$
\boxed{
\mathbf{v} = \mathbf{L}\frac{d\mathbf{I}}{dt}
}
$$

Esta es la ecuación matricial de voltajes del sistema acoplado.

---

# 2) Forma Expandida

La ecuación completa es:

$$
\begin{pmatrix}
v_1 \\
v_2 \\
\vdots \\
v_n
\end{pmatrix}
=
\begin{pmatrix}
L_{11} & L_{12} & \cdots & L_{1n} \\
L_{21} & L_{22} & \cdots & L_{2n} \\
\vdots & \vdots & \ddots & \vdots \\
L_{n1} & L_{n2} & \cdots & L_{nn}
\end{pmatrix}
\begin{pmatrix}
\dfrac{dI_1}{dt} \\
\dfrac{dI_2}{dt} \\
\vdots \\
\dfrac{dI_n}{dt}
\end{pmatrix}
$$

---

# 3) Voltaje en un Inductor Individual

Para el inductor $i$:

$$
\boxed{
v_i =
L_{ii}\frac{dI_i}{dt}
+
\sum_{j\ne i}
L_{ij}\frac{dI_j}{dt}
}
$$

Cada voltaje es la suma de:

- La contribución por autoinducción.
- Las contribuciones por inducción mutua de todos los demás inductores.

---

# 4) Estructura Operadorial del Voltaje

La ecuación fundamental del sistema es:

$$
\mathbf{v} = \mathbf{L}\frac{d\mathbf{I}}{dt}
$$

Esta expresión no debe interpretarse únicamente como una multiplicación matricial, sino como la acción de un operador lineal diferencial:

$$
\boxed{
\mathcal{Z}_L := \mathbf{L}\frac{d}{dt}
}
$$

Así, el sistema puede escribirse como:

$$
\mathbf{v} = \mathcal{Z}_L \mathbf{I}
$$

La matriz de inductancias pondera las derivadas temporales de todas las corrientes del sistema.

---

# 5) Acoplamiento Dinámico Total

Expandiendo por componente:

$$
v_i =
\sum_{j=1}^{n}
L_{ij}\frac{dI_j}{dt}
$$

Esto muestra que:

- El voltaje en una rama depende de la variación temporal de todas las corrientes.
- El acoplamiento es estrictamente dinámico: si $\frac{dI_j}{dt}=0$, no hay contribución inductiva.

El sistema es, por naturaleza, un sistema diferencial acoplado de primer orden.

---

# 6) Naturaleza del Operador

La matriz $\mathbf{L}$ es:

- Simétrica
- Definida positiva
- Independiente del tiempo (medio lineal y estacionario)

Por lo tanto:

- El operador $\mathcal{Z}_L$ es lineal.
- El sistema es causal.
- La energía almacenada es coherente con la potencia instantánea:

$$
p(t) = \mathbf{v}^T \mathbf{I}
$$

Sustituyendo:

$$
p(t)
=
\mathbf{I}^T
\mathbf{L}
\frac{d\mathbf{I}}{dt}
$$

Lo cual conduce directamente a:

$$
\frac{d}{dt}
\left(
\frac{1}{2}
\mathbf{I}^T \mathbf{L} \mathbf{I}
\right)
=
p(t)
$$

confirmando consistencia energética.

---

# 7) Interpretación Geométrica

La matriz de inductancias define una métrica cuadrática sobre el espacio de corrientes.

El voltaje es el resultado de aplicar esa métrica a la velocidad (derivada temporal) del vector de corrientes.

En este sentido:

- $\mathbf{I}$ → coordenadas en el espacio de corrientes.
- $\mathbf{L}$ → tensor métrico energético.
- $\mathbf{v}$ → covector dinámico asociado a la evolución temporal.

---

# Resultado Estructural

Un sistema de inductores acoplados no es simplemente un conjunto de elementos eléctricos.

Es un sistema dinámico lineal cuya estructura está completamente determinada por el operador:

$$
\boxed{
\mathcal{Z}_L = \mathbf{L}\frac{d}{dt}
}
$$

Toda la interacción electromagnética interna del sistema está contenida en esa estructura.
