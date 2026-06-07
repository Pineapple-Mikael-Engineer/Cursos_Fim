---
title: Vectores Base y Factores de Escala Esféricos
tags:
  - analisis-tensorial
  - teoria
  - coordenadas-curvilineas
  - esfericas
  - factores-escala
draft: false
aliases:
  - factores de escala esfericos
  - vectores base esfericos
  - spherical scale factors
---

# Vectores Base y Factores de Escala Esféricos

> [!definicion]
> Los **factores de escala** del sistema esférico miden cuánto se desplaza $\vec r$ por unidad de cada coordenada, $h_i=\left|\partial\vec r/\partial q_i\right|$:
> $$h_r=1,\qquad h_\theta=r,\qquad h_\phi=r\operatorname{sen}\theta.$$
> De ellos sale el **vector desplazamiento** infinitesimal
> $$d\vec r=dr\,\hat e_r+r\,d\theta\,\hat e_\theta+r\operatorname{sen}\theta\,d\phi\,\hat e_\phi.$$

> [!info]
> Subnota del [[index | sistema esférico]] (libro, cap. 3.3). Aplica la receta general $h_i=|\partial\vec r/\partial q_i|$ de los [[Sistemas Curvilineos Generales/Factores de Escala | factores de escala generales]] al vector posición en cartesianas. Los $h_i$ que aquí se deducen alimentan todas las [[Operaciones Esfericas]] y los elementos de arco, área y volumen.

---

## Ejemplo

> [!ejemplo]
> **Elemento de volumen y volumen de la esfera.** Con $d\vec r=dr\,\hat e_r+r\,d\theta\,\hat e_\theta+r\operatorname{sen}\theta\,d\phi\,\hat e_\phi$, los tres lados de la "caja" infinitesimal son $dr$, $r\,d\theta$ y $r\operatorname{sen}\theta\,d\phi$. Por ser la base ortonormal, el elemento de volumen es su producto:
> $$d\tau=h_r h_\theta h_\phi\,dr\,d\theta\,d\phi=r^2\operatorname{sen}\theta\,dr\,d\theta\,d\phi.$$
> Como verificación, el **volumen de una esfera** de radio $R$ se obtiene integrando $r\in[0,R]$, $\theta\in[0,\pi]$, $\phi\in[0,2\pi]$:
> $$V=\int_0^{2\pi}\!\!\int_0^{\pi}\!\!\int_0^{R} r^2\operatorname{sen}\theta\,dr\,d\theta\,d\phi=\underbrace{\int_0^{R}r^2\,dr}_{R^3/3}\;\underbrace{\int_0^{\pi}\operatorname{sen}\theta\,d\theta}_{2}\;\underbrace{\int_0^{2\pi}d\phi}_{2\pi}=\frac{R^3}{3}\cdot 2\cdot 2\pi=\frac{4}{3}\pi R^3.$$
> Se recupera la fórmula clásica. El factor $r^2\operatorname{sen}\theta$ —producto de $h_\theta h_\phi=r\cdot r\operatorname{sen}\theta$— es el **jacobiano** del cambio de coordenadas: sin él la integral daría un resultado sin sentido dimensional.

---

## En qué consiste

> [!teorema] Factores de escala esféricos
> Para el sistema esférico,
> $$h_r=1,\qquad h_\theta=r,\qquad h_\phi=r\operatorname{sen}\theta.$$

> [!demostracion]
> **Paso 1 — Escribir $\vec r$ en cartesianas con coordenadas esféricas.** Sustituyendo $x=r\operatorname{sen}\theta\cos\phi$, $y=r\operatorname{sen}\theta\operatorname{sen}\phi$, $z=r\cos\theta$ en $\vec r=x\,\hat e_x+y\,\hat e_y+z\,\hat e_z$:
> $$\vec r=r\operatorname{sen}\theta\cos\phi\,\hat e_x+r\operatorname{sen}\theta\operatorname{sen}\phi\,\hat e_y+r\cos\theta\,\hat e_z.$$
> Las bases cartesianas $\hat e_x,\hat e_y,\hat e_z$ son constantes, así que solo derivamos los coeficientes.
>
> **Paso 2 — Derivar respecto a $r$ y tomar módulo.**
> $$\frac{\partial\vec r}{\partial r}=\operatorname{sen}\theta\cos\phi\,\hat e_x+\operatorname{sen}\theta\operatorname{sen}\phi\,\hat e_y+\cos\theta\,\hat e_z,$$
> $$h_r=\left|\frac{\partial\vec r}{\partial r}\right|=\sqrt{\operatorname{sen}^2\theta\cos^2\phi+\operatorname{sen}^2\theta\operatorname{sen}^2\phi+\cos^2\theta}=\sqrt{\operatorname{sen}^2\theta+\cos^2\theta}=1.$$
>
> **Paso 3 — Derivar respecto a $\theta$.**
> $$\frac{\partial\vec r}{\partial\theta}=r\cos\theta\cos\phi\,\hat e_x+r\cos\theta\operatorname{sen}\phi\,\hat e_y-r\operatorname{sen}\theta\,\hat e_z,$$
> $$h_\theta=\left|\frac{\partial\vec r}{\partial\theta}\right|=\sqrt{r^2\cos^2\theta\cos^2\phi+r^2\cos^2\theta\operatorname{sen}^2\phi+r^2\operatorname{sen}^2\theta}=\sqrt{r^2\cos^2\theta+r^2\operatorname{sen}^2\theta}=r.$$
>
> **Paso 4 — Derivar respecto a $\phi$.**
> $$\frac{\partial\vec r}{\partial\phi}=-r\operatorname{sen}\theta\operatorname{sen}\phi\,\hat e_x+r\operatorname{sen}\theta\cos\phi\,\hat e_y,$$
> $$h_\phi=\left|\frac{\partial\vec r}{\partial\phi}\right|=\sqrt{r^2\operatorname{sen}^2\theta\operatorname{sen}^2\phi+r^2\operatorname{sen}^2\theta\cos^2\phi}=\sqrt{r^2\operatorname{sen}^2\theta}=r\operatorname{sen}\theta.$$
>
> Por tanto $h_r=1,\ h_\theta=r,\ h_\phi=r\operatorname{sen}\theta$. $\blacksquare$

> [!info] Lectura geométrica de $h_\theta$ y $h_\phi$
> La coordenada $r$ es una longitud: avanzar $dr$ mueve $\vec r$ esa misma distancia, de ahí $h_r=1$. Los otros dos son **ángulos** (adimensionales) y necesitan un factor que los traduzca en longitud de arco:
> - Al variar $\theta$ con $r$ fijo, $P$ recorre un **meridiano** (circunferencia de radio $r$): el arco es $r\,d\theta$, luego $h_\theta=r$.
> - Al variar $\phi$ con $r,\theta$ fijos, $P$ recorre un **paralelo**. El radio de ese paralelo no es $r$ sino su proyección sobre el plano $xy$, que vale $r\operatorname{sen}\theta$; el arco es $r\operatorname{sen}\theta\,d\phi$, luego $h_\phi=r\operatorname{sen}\theta$.
>
> Por eso $h_\phi$ se anula en el eje ($\theta=0,\pi$): allí el paralelo degenera en un punto y un giro en $\phi$ no desplaza a $P$.

> [!proposicion] Vector desplazamiento, arco, área y volumen
> Como los $\hat e_i$ son unitarios, cada desplazamiento de coordenada contribuye con $h_i\,dq_i$ en su dirección:
> $$d\vec r=h_r\,dr\,\hat e_r+h_\theta\,d\theta\,\hat e_\theta+h_\phi\,d\phi\,\hat e_\phi=dr\,\hat e_r+r\,d\theta\,\hat e_\theta+r\operatorname{sen}\theta\,d\phi\,\hat e_\phi.$$
>
> | Elemento | Expresión |
> |---|---|
> | Longitud $ds$ | $ds^2=dr^2+r^2\,d\theta^2+r^2\operatorname{sen}^2\theta\,d\phi^2$ |
> | Área (cara $r$ cte) | $dA_r=h_\theta h_\phi\,d\theta\,d\phi=r^2\operatorname{sen}\theta\,d\theta\,d\phi$ |
> | Área (cara $\theta$ cte) | $dA_\theta=h_r h_\phi\,dr\,d\phi=r\operatorname{sen}\theta\,dr\,d\phi$ |
> | Volumen $d\tau$ | $h_r h_\theta h_\phi\,dr\,d\theta\,d\phi=r^2\operatorname{sen}\theta\,dr\,d\theta\,d\phi$ |
>
> El área $dA_r=r^2\operatorname{sen}\theta\,d\theta\,d\phi$ sobre una esfera de radio fijo es el **elemento de ángulo sólido** $r^2\,d\Omega$, con $d\Omega=\operatorname{sen}\theta\,d\theta\,d\phi$.

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Receta | $h_i=\left|\partial\vec r/\partial q_i\right|$ |
> | $\vec r$ en cartesianas | $r\operatorname{sen}\theta\cos\phi\,\hat e_x+r\operatorname{sen}\theta\operatorname{sen}\phi\,\hat e_y+r\cos\theta\,\hat e_z$ |
> | Factores | $h_r=1,\ h_\theta=r,\ h_\phi=r\operatorname{sen}\theta$ |
> | Desplazamiento | $d\vec r=dr\,\hat e_r+r\,d\theta\,\hat e_\theta+r\operatorname{sen}\theta\,d\phi\,\hat e_\phi$ |
> | Volumen | $d\tau=r^2\operatorname{sen}\theta\,dr\,d\theta\,d\phi$ |
> | Ángulo sólido | $d\Omega=\operatorname{sen}\theta\,d\theta\,d\phi$ |

> [!corolario]
> Toda la peculiaridad métrica del esférico se concentra en $h_\theta=r$ y $h_\phi=r\operatorname{sen}\theta$: son los factores distintos de la unidad y la fuente de los $1/r$, $1/(r\operatorname{sen}\theta)$ y de las derivadas $\partial(r^2\,\cdot)/\partial r$ y $\partial(\operatorname{sen}\theta\,\cdot)/\partial\theta$ que aparecen en el gradiente, la divergencia y el rotor de las [[Operaciones Esfericas]]. Los $h_i$ son el puente entre la geometría del sistema y sus operadores diferenciales.

> [!referencia]
> - Definición general de los $h_i$: [[Sistemas Curvilineos Generales/Factores de Escala]].
> - Operadores que usan estos factores: [[Operaciones Esfericas]].
> - Construcción de $\vec r$: [[Vector Posicion]] y [[index | sistema esférico]].
> - Versión cilíndrica: [[Sistema Cilindrico/Vectores Base y Factores Escala]].
