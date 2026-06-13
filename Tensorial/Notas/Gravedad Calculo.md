# Reducción de la integral gravitacional mediante el teorema de Gauss

La fuerza gravitacional ejercida sobre un cuerpo homogéneo sometido a un campo gravitatorio externo puede expresarse como:

$$
\vec{F} = \rho \int_V \vec{g}(\vec{r}) \, d\tau
$$

donde:

- $\rho$ es la densidad uniforme del cuerpo.
- $\vec{g}(\vec{r})$ es el campo gravitatorio externo.
- $V$ es el volumen ocupado por el cuerpo.

Descomponiendo la fuerza en componentes cartesianas:

$$
\vec{F} = F_i \hat{e}_i
$$

se obtiene:

$$
F_i = \rho \int_V g_i(\vec{r}) \, d\tau
$$

## Relación entre el campo gravitatorio y el potencial

El campo gravitatorio puede expresarse en términos del potencial gravitatorio $p$ mediante:

$$
\vec{g} = -\nabla p
$$

o, en notación indicial:

$$
g_i = -\frac{\partial p}{\partial x_i}
$$

Definimos el tensor de segundo orden:

$$
h_{ij} = -p \delta_{ij}
$$

donde $\delta_{ij}$ es el delta de Kronecker.

Calculando su divergencia:

$$
\frac{\partial h_{ij}}{\partial x_j}
=
\frac{\partial}{\partial x_j}
\left(
-p \delta_{ij}
\right)
$$

Dado que $\delta_{ij}$ es constante:

$$
\frac{\partial h_{ij}}{\partial x_j}
=
-\delta_{ij}
\frac{\partial p}{\partial x_j}
$$

Utilizando la propiedad del delta de Kronecker:

$$
\delta_{ij}
\frac{\partial p}{\partial x_j}
=
\frac{\partial p}{\partial x_i}
$$

obtenemos:

$$
\frac{\partial h_{ij}}{\partial x_j}
=
-\frac{\partial p}{\partial x_i}
=
g_i
$$

Por lo tanto:

$$
g_i
=
\frac{\partial h_{ij}}{\partial x_j}
$$

## Aplicación del teorema de la divergencia

Sustituyendo la expresión anterior en la definición de la fuerza:

$$
F_i
=
\rho
\int_V
\frac{\partial h_{ij}}{\partial x_j}
\, d\tau
$$

Aplicando el teorema de la divergencia:

$$
F_i
=
\rho
\oint_S
h_{ij} n_j
\, dS
$$

donde:

- $S$ es la superficie cerrada que delimita el volumen.
- $n_j$ son las componentes de la normal unitaria exterior.

Sustituyendo la definición de $h_{ij}$:

$$
F_i
=
\rho
\oint_S
(-p \delta_{ij}) n_j
\, dS
$$

Reordenando términos:

$$
F_i
=
-\rho
\oint_S
p \delta_{ij} n_j
\, dS
$$

Aplicando nuevamente la propiedad del delta de Kronecker:

$$
\delta_{ij} n_j = n_i
$$

se obtiene:

$$
F_i
=
-\rho
\oint_S
p n_i
\, dS
$$

Finalmente, escribiendo la expresión en forma vectorial:

$$
\vec{F}
=
-\rho
\oint_S
p \, d\vec{S}
$$

donde:

$$
d\vec{S}
=
\hat{n} \, dS
$$

es el elemento diferencial de superficie orientado hacia el exterior.

## Interpretación

La formulación original requiere una integración sobre todo el volumen del cuerpo:

$$
\vec{F}
=
\rho
\int_V
\vec{g}
\, d\tau
$$

La expresión obtenida permite reescribir el problema como una integral únicamente sobre la superficie:

$$
\vec{F}
=
-\rho
\oint_S
p
\, d\vec{S}
$$

reduciendo la dimensionalidad del problema de tres a dos dimensiones.

Este resultado es válido para cualquier cuerpo homogéneo, independientemente de su geometría, siempre que el potencial gravitatorio externo pueda evaluarse sobre la superficie del objeto.

## Motivación computacional

La implementación directa de:

$$
\vec{F}
=
\rho
\int_V
\vec{g}
\, d\tau
$$

requiere una integración tridimensional sobre el volumen del cuerpo.

La formulación equivalente:

$$
\vec{F}
=
-\rho
\oint_S
p
\, d\vec{S}
$$

requiere únicamente una integración sobre la frontera del dominio.

Esta reducción constituye la motivación teórica detrás de la implementación utilizada en este proyecto para el cálculo de fuerzas gravitacionales sobre cuerpos extendidos homogéneos.