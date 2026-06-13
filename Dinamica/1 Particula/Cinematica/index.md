---
title: Cinemática de la Partícula
tags:
  - dinamica
  - teoria
  - particula
  - cinematica
  - index
draft: false
aliases:
  - cinemática de la partícula
  - sistemas de coordenadas
  - coordenadas curvilíneas
---

# Cinemática de la Partícula

> [!definicion]
> La **cinemática** describe el movimiento sin sus causas. El estado de una partícula es su
> **posición** $\vec{r}(t)$; de ella se derivan
> $$\vec{v}=\frac{d\vec{r}}{dt},\qquad \vec{a}=\frac{d\vec{v}}{dt}=\frac{d^2\vec{r}}{dt^2}.$$
> Estas definiciones son **independientes del sistema de coordenadas**; lo que cambia con él son las
> **componentes**. Se elige el sistema según la geometría del problema.

> [!info]
> Primera sección de la [[1 Particula/index | partícula]] ([[Dinamica/index | Dinámica]]). El hilo
> técnico —las bases curvilíneas **giran**, así que sus versores tienen derivada no nula— es el caso
> particular del **[[Operador Derivada en Base Movil | operador derivada en base móvil]]** (sección 2).
> Referencia: Taylor, *Classical Mechanics*, §1.7-1.9.

---

## Los sistemas de coordenadas

> [!teoria] Cartesianas: el caso trivial
> Con base fija $\{\hat\imath,\hat\jmath,\hat k\}$ (versores **constantes**), derivar la posición es
> derivar sus componentes:
> $$\vec{r}=x\hat\imath+y\hat\jmath+z\hat k\ \Rightarrow\ \vec{v}=\dot x\hat\imath+\dot y\hat\jmath+\dot z\hat k,\quad \vec{a}=\ddot x\hat\imath+\ddot y\hat\jmath+\ddot z\hat k.$$
> Toda la riqueza de las otras descripciones nace de que **sus versores no son constantes**: una base
> ligada a la trayectoria o a un centro **gira** al moverse la partícula, y al derivar la posición hay
> que derivar también los versores.

> [!teoria] Las bases que giran
> Según qué geometría convenga, se usan tres familias de coordenadas **curvilíneas**, cada una con su
> propia nota:
>
> ![[coordenadas_cinematica.svg|680]]
>
> *Dos de las bases móviles: el triedro intrínseco $(\hat t,\hat n)$ ligado a la trayectoria
> (izquierda) y la base polar $(\hat e_r,\hat e_\theta)$ ligada a un centro (derecha).*
>
> - **Intrínsecas** $(\hat t,\hat n,\hat b)$ — ligadas a la **trayectoria**; el triedro de
>   Frenet-Serret es **tridimensional** (tangente, normal y binormal) y mide curvatura y torsión. La
>   aceleración sale $a=\dot v\,\hat t+\dfrac{v^2}{\rho}\,\hat n$. → [[Componentes Intrinsecas]].
> - **Cilíndricas** $(r,\theta,z)$ — la base polar del plano más el eje $z$; útil con simetría axial.
>   → [[Coordenadas Cilindricas]].
> - **Esféricas** $(r,\theta,\varphi)$ — ligadas a un **centro**; útiles en campos centrales.
>   → [[Coordenadas Esfericas]].

## Mapa de la sección

> [!info] Las notas de esta sección
> | Nota | Contenido |
> |:---|:---|
> | [[Componentes Intrinsecas]] | triedro de Frenet 3D ($\hat t,\hat n,\hat b$); curvatura, torsión; $a_n=v^2/\rho$ |
> | [[Coordenadas Cilindricas]] | $(r,\theta,z)$; $\vec v$, $\vec a$; término de Coriolis $2\dot r\dot\theta$ |
> | [[Coordenadas Esfericas]] | $(r,\theta,\varphi)$; $\vec v$, $\vec a$ vía la base móvil |

> [!corolario]
> La velocidad y la aceleración son únicas; cada base las **proyecta** distinto. La clave técnica común
> a todas las curvilíneas es que sus versores **giran** —derivada no nula—, el germen del operador en
> base móvil que vertebra el resto del curso.

> [!referencia]
> Taylor, §1.7-1.9. Base móvil general: [[Operador Derivada en Base Movil]]. Uso dinámico:
> [[Cinetica de la Particula]].
