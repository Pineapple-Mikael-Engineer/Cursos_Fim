---
title: El Vector Posición
tags:
  - analisis-tensorial
  - teoria
  - coordenadas-curvilineas
  - vector-posicion
draft: false
aliases:
  - vector posicion
  - position vector
  - r de P
---

# El Vector Posición

> [!definicion]
> El **vector posición** $\vec r(P)$ va del origen al punto $P$: su magnitud es la distancia origen–$P$ y su dirección apunta hacia $P$. En cartesianas,
> $$\vec r=r_i\,\hat e_i=x_i\,\hat e_i,$$
> de modo que sus componentes $(r_1,r_2,r_3)$ son las propias coordenadas $(x_1,x_2,x_3)$.

> [!info]
> Primera sección del [[index | capítulo 3]] (libro, cap. 3.1). Es la base para describir los sistemas [[Sistema Cilindrico/index | cilíndrico]] y [[Sistema Esferico/index | esférico]]: en ellos $\vec r$ tiene una forma especialmente simple. La técnica de proyectar sobre la base ($r_i=\hat e_i\cdot\vec r$) se reutiliza para hallar componentes en cualquier [[Sistemas Curvilineos Generales/index | sistema ortogonal]].

---

## Ejemplo

> [!ejemplo]
> **Componente por proyección.** La primera componente de $\vec r$ se obtiene proyectando sobre $\hat e_1$:
> $$r_1=\hat e_1\cdot\vec r=\hat e_1\cdot(x_j\hat e_j)=x_j\,(\hat e_1\cdot\hat e_j)=x_j\,\delta_{1j}=x_1.$$
> En cartesianas esto parece trivial (la componente *es* la coordenada), pero la misma técnica $r_i=\hat e_i\cdot\vec r$ **sí** es útil en sistemas donde la base no es trivial: proyectar $\vec r$ sobre cada $\hat q_i$ da sus componentes curvilíneas. (Ver [[Sistema Cilindrico/index | cilíndrico]], donde $\vec r=\rho\,\hat e_\rho+z\,\hat e_z$.)

> [!info] Dónde dibujar $\vec r$ y la base
> ![[vector_posicion.svg|520]]
>
> En curvilíneas conviene dibujar el vector y sus vectores base **emanando del mismo punto $P$** (derecha), no del origen (izquierda): así las componentes se leen como proyecciones sobre la base local. Para integrales de línea, en cambio, es mejor dibujar $\vec r$ desde el origen, porque su punta recorre el camino.

---

## En qué consiste

> [!teoria]
> En cartesianas la expresión $\vec r=x_i\hat e_i$ es intuitiva porque la base es fija. En curvilíneas surge una sutileza: los vectores base **dependen de la posición**, así que al dibujar un vector hay que tener cuidado de **dónde** se ubica. Si se dibuja $\vec r$ desde el origen pero su base desde $P$, la descomposición puede resultar ambigua.
>
> La regla práctica: para **descomponer** un vector en sus componentes, dibújalo —y a su base— partiendo del punto $P$ donde se evalúa. Las componentes son entonces las proyecciones del vector sobre cada vector base en ese punto. Esta es la idea que vuelve manejables los sistemas curvilíneos.

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Definición | $\vec r$ del origen a $P$; $|\vec r|=$ distancia |
> | Cartesianas | $\vec r=x_i\hat e_i$; $r_i=x_i$ |
> | Componente | $r_i=\hat e_i\cdot\vec r$ (proyección) |
> | Curvilíneas | dibujar $\vec r$ y base desde $P$ |
> | Cilíndrico / esférico | $\vec r=\rho\hat e_\rho+z\hat e_z$ / $\vec r=r\hat e_r$ |

> [!corolario]
> El vector posición es el objeto más simple de cada sistema y a la vez la clave para construir los demás: derivándolo respecto a las coordenadas se obtienen los vectores base y los [[Sistemas Curvilineos Generales/Factores de Escala | factores de escala]]. Su forma compacta en [[Sistema Cilindrico/index | cilíndricas]] ($\rho\hat e_\rho+z\hat e_z$) y [[Sistema Esferico/index | esféricas]] ($r\hat e_r$) anticipa la economía de elegir bien las coordenadas.

> [!referencia]
> - Construcción de la base a partir de $\vec r$: [[Sistemas Curvilineos Generales/Coordenadas y Vectores Base]].
> - $\vec r$ en cilíndricas: [[Sistema Cilindrico/index]]; en esféricas: [[Sistema Esferico/index]].
