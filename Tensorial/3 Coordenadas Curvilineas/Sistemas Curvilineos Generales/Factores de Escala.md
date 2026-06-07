---
title: Factores de Escala
tags:
  - analisis-tensorial
  - teoria
  - coordenadas-curvilineas
  - factores-escala
draft: false
aliases:
  - factores de escala
  - h_i
  - scale factors
---

# Factores de Escala $h_i$

> [!definicion]
> El **factor de escala** $h_i$ es el módulo de la derivada del vector posición respecto a la coordenada $q_i$:
> $$h_i=\left|\frac{\partial\vec r}{\partial q_i}\right|=\sqrt{\left(\frac{\partial x_1}{\partial q_i}\right)^2+\left(\frac{\partial x_2}{\partial q_i}\right)^2+\left(\frac{\partial x_3}{\partial q_i}\right)^2}.$$
> Mide **cuánto se desplaza $\vec r$ por unidad de coordenada**: al variar $q_i$ en $dq_i$, el punto se mueve una distancia $|h_i\,dq_i|$. El **vector desplazamiento** queda
> $$d\vec r=h_i\,dq_i\,\hat q_i\quad(\text{suma sobre }i).$$

> [!info]
> Sección **3.4.1** del libro (Rogan & Muñoz). Los $h_i$ son el corazón del marco [[index | curvilíneo general]]: traducen incrementos de coordenada en longitudes reales y, con ellos, todo elemento de arco, área y volumen ([[Geometria Diferencial Local]]) y los operadores diferenciales quedan determinados. Aparecen al normalizar los [[Coordenadas y Vectores Base | vectores base]].

---

## Ejemplo

> [!ejemplo]
> **Factores de escala cilíndricos $(1,\rho,1)$.** Con $x=\rho\cos\phi$, $y=\rho\operatorname{sen}\phi$, $z=z$, derivamos $\vec r=\rho\cos\phi\,\hat e_x+\rho\operatorname{sen}\phi\,\hat e_y+z\,\hat e_z$ y tomamos módulos:
> $$h_\rho=\left|\frac{\partial\vec r}{\partial\rho}\right|=\sqrt{\cos^2\phi+\operatorname{sen}^2\phi}=1,$$
> $$h_\phi=\left|\frac{\partial\vec r}{\partial\phi}\right|=\sqrt{(-\rho\operatorname{sen}\phi)^2+(\rho\cos\phi)^2}=\sqrt{\rho^2}=\rho,$$
> $$h_z=\left|\frac{\partial\vec r}{\partial z}\right|=1.$$
> Resultado $(h_\rho,h_\phi,h_z)=(1,\rho,1)$.

> [!ejemplo]
> **Factores de escala esféricos $(1,r,r\operatorname{sen}\theta)$.** Con $x=r\operatorname{sen}\theta\cos\phi$, $y=r\operatorname{sen}\theta\operatorname{sen}\phi$, $z=r\cos\theta$:
> $$\vec r=r\operatorname{sen}\theta\cos\phi\,\hat e_x+r\operatorname{sen}\theta\operatorname{sen}\phi\,\hat e_y+r\cos\theta\,\hat e_z.$$
>
> **Respecto a $r$:**
> $$\frac{\partial\vec r}{\partial r}=\operatorname{sen}\theta\cos\phi\,\hat e_x+\operatorname{sen}\theta\operatorname{sen}\phi\,\hat e_y+\cos\theta\,\hat e_z,$$
> $$h_r=\sqrt{\operatorname{sen}^2\theta(\cos^2\phi+\operatorname{sen}^2\phi)+\cos^2\theta}=\sqrt{\operatorname{sen}^2\theta+\cos^2\theta}=1.$$
>
> **Respecto a $\theta$:**
> $$\frac{\partial\vec r}{\partial\theta}=r\cos\theta\cos\phi\,\hat e_x+r\cos\theta\operatorname{sen}\phi\,\hat e_y-r\operatorname{sen}\theta\,\hat e_z,$$
> $$h_\theta=\sqrt{r^2\cos^2\theta(\cos^2\phi+\operatorname{sen}^2\phi)+r^2\operatorname{sen}^2\theta}=\sqrt{r^2\cos^2\theta+r^2\operatorname{sen}^2\theta}=r.$$
>
> **Respecto a $\phi$:**
> $$\frac{\partial\vec r}{\partial\phi}=-r\operatorname{sen}\theta\operatorname{sen}\phi\,\hat e_x+r\operatorname{sen}\theta\cos\phi\,\hat e_y,$$
> $$h_\phi=\sqrt{r^2\operatorname{sen}^2\theta(\operatorname{sen}^2\phi+\cos^2\phi)}=r\operatorname{sen}\theta.$$
> Resultado $(h_r,h_\theta,h_\phi)=(1,r,r\operatorname{sen}\theta)$. El $h_\phi=r\operatorname{sen}\theta$ es el radio del paralelo a latitud $\theta$: se anula en los polos, donde $\phi$ deja de mover el punto.

---

## En qué consiste

> [!teoria]
> Cada $h_i$ traduce el "ángulo o coordenada pura" $dq_i$ en una **longitud física** $h_i\,dq_i$. La interpretación: imaginemos fijas dos coordenadas y variemos solo $q_i$ en $dq_i$; el punto $P$ recorre una curva (la *curva coordenada* de $q_i$) y avanza una distancia $|h_i\,dq_i|$. Sumando las tres contribuciones, como la base $\hat q_i$ es ortonormal, se obtiene el vector desplazamiento.

> [!proposicion] Vector desplazamiento
> Partiendo de $d\vec r=(\partial\vec r/\partial q_i)\,dq_i$ y usando $\partial\vec r/\partial q_i=h_i\hat q_i$ (de la normalización de la base):
> $$d\vec r=\frac{\partial\vec r}{\partial q_i}\,dq_i=h_i\,dq_i\,\hat q_i\qquad(\text{suma sobre }i).$$
> Aquí **sí** hay suma sobre $i$, porque el índice no aparece libre en el lado izquierdo. Explícitamente $d\vec r=h_1\,dq_1\,\hat q_1+h_2\,dq_2\,\hat q_2+h_3\,dq_3\,\hat q_3$.

> [!info] Caso cartesiano y componente física vs coordenada
> En cartesianas $q_i=x_i$, $\hat q_i=\hat e_i$ y $\partial x_j/\partial x_i=\delta_{ij}$, de modo que **todos los $h_i=1$** y $d\vec r=dx_i\,\hat e_i$. Cuando algún $h_i\neq1$ surge la distinción clave: la **coordenada** $q_i$ (p. ej. el ángulo $\phi$, adimensional) no es lo mismo que la **componente física** del desplazamiento en esa dirección, que es $h_i\,dq_i$ (p. ej. la longitud de arco $\rho\,d\phi$). Las componentes que se miden con regla son las físicas, $h_i\,dq_i$, no los $dq_i$.

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Definición | $h_i=\left|\partial\vec r/\partial q_i\right|$ |
> | Fórmula | $\sqrt{(\partial x_1/\partial q_i)^2+(\partial x_2/\partial q_i)^2+(\partial x_3/\partial q_i)^2}$ |
> | Interpretación | $\vec r$ se desplaza $|h_i\,dq_i|$ al variar $q_i$ |
> | Desplazamiento | $d\vec r=h_i\,dq_i\,\hat q_i$ (suma sobre $i$) |
> | Cilíndricas | $(1,\rho,1)$ |
> | Esféricas | $(1,r,r\operatorname{sen}\theta)$ |
> | Cartesianas | $(1,1,1)$ |

> [!corolario]
> Toda la geometría del sistema se condensa en $h_1,h_2,h_3$. La distinción entre coordenada $q_i$ y componente física $h_i\,dq_i$ explica de dónde salen los factores $\rho$ y $r\operatorname{sen}\theta$ en áreas, volúmenes y operadores. La siguiente nota, [[Geometria Diferencial Local]], los usa para construir el volumen diferencial.

> [!referencia]
> - Normalización de la base con $h_i$: [[Coordenadas y Vectores Base]].
> - Volumen y caras diferenciales: [[Geometria Diferencial Local]].
> - Integrales que pesan con los $h_i$: [[Elementos Linea Superficie Volumen]].
