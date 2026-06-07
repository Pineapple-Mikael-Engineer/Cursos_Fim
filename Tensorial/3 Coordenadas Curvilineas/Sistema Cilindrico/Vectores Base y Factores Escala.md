---
title: Vectores Base y Factores de Escala Cilíndricos
tags:
  - analisis-tensorial
  - teoria
  - coordenadas-curvilineas
  - cilindricas
  - factores-escala
draft: false
aliases:
  - factores de escala cilindricos
  - vectores base cilindricos
  - cylindrical scale factors
---

# Vectores Base y Factores de Escala Cilíndricos

> [!definicion]
> Los **factores de escala** del sistema cilíndrico miden cuánto se desplaza $\vec r$ por unidad de cada coordenada, $h_i=\left|\partial\vec r/\partial q_i\right|$:
> $$h_\rho=1,\qquad h_\phi=\rho,\qquad h_z=1.$$
> De ellos sale el **vector desplazamiento** infinitesimal
> $$d\vec r=d\rho\,\hat e_\rho+\rho\,d\phi\,\hat e_\phi+dz\,\hat e_z.$$

> [!info]
> Subnota del [[index | sistema cilíndrico]] (libro, cap. 3.2). Aplica la receta general $h_i=|\partial\vec r/\partial q_i|$ de los [[Sistemas Curvilineos Generales/Factores de Escala | factores de escala generales]] al vector posición en cartesianas. Los $h_i$ que aquí se deducen alimentan todas las [[Operaciones Cilindricas]] y los elementos de arco, área y volumen.

---

## Ejemplo

> [!ejemplo]
> **Elemento de volumen y longitud de arco.** Con $d\vec r=d\rho\,\hat e_\rho+\rho\,d\phi\,\hat e_\phi+dz\,\hat e_z$, los tres lados de la "caja" infinitesimal son $d\rho$, $\rho\,d\phi$ y $dz$. Por ser la base ortonormal, el elemento de volumen es su producto:
> $$d\tau=h_\rho h_\phi h_z\,d\rho\,d\phi\,dz=\rho\,d\rho\,d\phi\,dz.$$
> Como aplicación, la longitud de un **arco de circunferencia** de radio $\rho=R$ fijo (con $z$ fijo) al variar $\phi$ de $0$ a $\phi_0$:
> $$s=\int_0^{\phi_0} h_\phi\,d\phi=\int_0^{\phi_0} R\,d\phi=R\,\phi_0,$$
> que es la fórmula elemental del arco. El factor $h_\phi=\rho$ es justamente lo que convierte el "ángulo puro" $d\phi$ en una **longitud**.

---

## En qué consiste

> [!teorema] Factores de escala cilíndricos
> Para el sistema cilíndrico,
> $$h_\rho=1,\qquad h_\phi=\rho,\qquad h_z=1.$$

> [!demostracion]
> **Paso 1 — Escribir $\vec r$ en cartesianas con coordenadas cilíndricas.** Sustituyendo $x=\rho\cos\phi$, $y=\rho\operatorname{sen}\phi$, $z=z$ en $\vec r=x\,\hat e_x+y\,\hat e_y+z\,\hat e_z$:
> $$\vec r=\rho\cos\phi\,\hat e_x+\rho\operatorname{sen}\phi\,\hat e_y+z\,\hat e_z.$$
> Las bases cartesianas $\hat e_x,\hat e_y,\hat e_z$ son constantes, así que solo derivamos los coeficientes.
>
> **Paso 2 — Derivar respecto a $\rho$ y tomar módulo.**
> $$\frac{\partial\vec r}{\partial\rho}=\cos\phi\,\hat e_x+\operatorname{sen}\phi\,\hat e_y,\qquad h_\rho=\left|\frac{\partial\vec r}{\partial\rho}\right|=\sqrt{\cos^2\phi+\operatorname{sen}^2\phi}=1.$$
>
> **Paso 3 — Derivar respecto a $\phi$.**
> $$\frac{\partial\vec r}{\partial\phi}=-\rho\operatorname{sen}\phi\,\hat e_x+\rho\cos\phi\,\hat e_y,$$
> $$h_\phi=\left|\frac{\partial\vec r}{\partial\phi}\right|=\sqrt{\rho^2\operatorname{sen}^2\phi+\rho^2\cos^2\phi}=\sqrt{\rho^2}=\rho.$$
>
> **Paso 4 — Derivar respecto a $z$.**
> $$\frac{\partial\vec r}{\partial z}=\hat e_z,\qquad h_z=\left|\frac{\partial\vec r}{\partial z}\right|=1.$$
>
> Por tanto $h_\rho=1,\ h_\phi=\rho,\ h_z=1$. $\blacksquare$

> [!info] Por qué $h_\phi=\rho$ y no $1$
> Las coordenadas $\rho$ y $z$ son longitudes: avanzar $d\rho$ o $dz$ mueve $\vec r$ esa misma distancia, de ahí $h_\rho=h_z=1$. Pero $\phi$ es un **ángulo** (adimensional): al girarlo $d\phi$ con $\rho$ fijo, $P$ recorre un arco de circunferencia de radio $\rho$, cuya longitud es $\rho\,d\phi$. El factor $h_\phi=\rho$ es precisamente el radio que traduce ángulo en longitud, y crece al alejarse del eje.

> [!proposicion] Vector desplazamiento, arco, área y volumen
> Como los $\hat e_i$ son unitarios, cada desplazamiento de coordenada contribuye con $h_i\,dq_i$ en su dirección:
> $$d\vec r=h_\rho\,d\rho\,\hat e_\rho+h_\phi\,d\phi\,\hat e_\phi+h_z\,dz\,\hat e_z=d\rho\,\hat e_\rho+\rho\,d\phi\,\hat e_\phi+dz\,\hat e_z.$$
>
> | Elemento | Expresión |
> |---|---|
> | Longitud $ds$ | $ds^2=d\rho^2+\rho^2\,d\phi^2+dz^2$ |
> | Área (cara $z$ cte) | $dA_z=h_\rho h_\phi\,d\rho\,d\phi=\rho\,d\rho\,d\phi$ |
> | Área (cara $\rho$ cte) | $dA_\rho=h_\phi h_z\,d\phi\,dz=\rho\,d\phi\,dz$ |
> | Volumen $d\tau$ | $h_\rho h_\phi h_z\,d\rho\,d\phi\,dz=\rho\,d\rho\,d\phi\,dz$ |

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Receta | $h_i=\left|\partial\vec r/\partial q_i\right|$ |
> | $\vec r$ en cartesianas | $\rho\cos\phi\,\hat e_x+\rho\operatorname{sen}\phi\,\hat e_y+z\,\hat e_z$ |
> | Factores | $h_\rho=1,\ h_\phi=\rho,\ h_z=1$ |
> | Desplazamiento | $d\vec r=d\rho\,\hat e_\rho+\rho\,d\phi\,\hat e_\phi+dz\,\hat e_z$ |
> | Volumen | $d\tau=\rho\,d\rho\,d\phi\,dz$ |

> [!corolario]
> Toda la peculiaridad métrica del cilíndrico se concentra en $h_\phi=\rho$: es el único factor distinto de la unidad y la fuente del $1/\rho$ y del $\partial(\rho\,\cdot)/\partial\rho$ que aparecen en el gradiente, la divergencia y el rotor de las [[Operaciones Cilindricas]]. Los $h_i$ son el puente entre la geometría del sistema y sus operadores diferenciales.

> [!referencia]
> - Definición general de los $h_i$: [[Sistemas Curvilineos Generales/Factores de Escala]].
> - Operadores que usan estos factores: [[Operaciones Cilindricas]].
> - Construcción de $\vec r$: [[Vector Posicion]] y [[index | sistema cilíndrico]].
