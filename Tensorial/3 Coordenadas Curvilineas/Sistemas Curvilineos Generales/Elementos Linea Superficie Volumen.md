---
title: Elementos de Línea, Superficie y Volumen
order: 4
tags:
  - analisis-tensorial
  - teoria
  - coordenadas-curvilineas
  - factores-escala
draft: false
aliases:
  - integrales en curvilineas
  - elementos de linea superficie volumen
  - line surface volume elements
---

# Elementos de Línea, Superficie y Volumen

> [!definicion]
> Con el desplazamiento $d\vec r=h_i\,dq_i\,\hat q_i$ y el volumen $d\tau=h_1h_2h_3\,dq_1dq_2dq_3$, las tres integrales de un campo en coordenadas curvilíneas son
> $$\int_C d\vec r\cdot\vec v=\int dq_j\,h_j\,v_j,$$
> $$\int_S d\vec\sigma\cdot\vec V=\int\pm dq_1dq_2\,h_1h_2\,V_3\pm dq_2dq_3\,h_2h_3\,V_1\pm dq_1dq_3\,h_1h_3\,V_2,$$
> $$\int_V d\tau\,\rho=\int dq_1dq_2dq_3\,h_1h_2h_3\,\rho.$$
> Los [[Factores de Escala | factores de escala]] $h_i$ son el peso que convierte coordenadas en longitudes, áreas y volúmenes reales.

> [!info]
> Secciones **3.4.5 a 3.4.7** del libro (Rogan & Muñoz). Aplican el desplazamiento de [[Factores de Escala]] y las caras de [[Geometria Diferencial Local]] al cálculo de integrales. Particularizando los $h_i$ se obtienen las integrales [[Sistema Cilindrico/index | cilíndricas]] y [[Sistema Esferico/index | esféricas]] habituales.

---

## Ejemplo

> [!ejemplo]
> **Volumen de un cilindro (integral de volumen).** En cilíndricas $h_1h_2h_3=\rho$, así que $d\tau=\rho\,d\rho\,d\phi\,dz$. Para un cilindro de radio $R$ y altura $L$ con $\rho=1$:
> $$V=\int_V d\tau=\int_0^L\!\!\int_0^{2\pi}\!\!\int_0^R \rho\,d\rho\,d\phi\,dz=\left(\int_0^R\rho\,d\rho\right)\!\left(\int_0^{2\pi}d\phi\right)\!\left(\int_0^L dz\right)=\frac{R^2}{2}\cdot2\pi\cdot L=\pi R^2 L.$$
> El factor $\rho=h_\phi$ es lo que hace aparecer el $R^2/2$ y, con ello, el área $\pi R^2$ de la base.

> [!ejemplo]
> **Volumen de una esfera (integral de volumen).** En esféricas $h_1h_2h_3=h_r h_\theta h_\phi=1\cdot r\cdot r\operatorname{sen}\theta=r^2\operatorname{sen}\theta$, luego $d\tau=r^2\operatorname{sen}\theta\,dr\,d\theta\,d\phi$. Para una esfera de radio $R$:
> $$V=\int_0^{2\pi}\!\!\int_0^{\pi}\!\!\int_0^R r^2\operatorname{sen}\theta\,dr\,d\theta\,d\phi=\left(\int_0^R r^2\,dr\right)\!\left(\int_0^{\pi}\operatorname{sen}\theta\,d\theta\right)\!\left(\int_0^{2\pi}d\phi\right).$$
> Evaluando: $\dfrac{R^3}{3}\cdot[-\cos\theta]_0^{\pi}\cdot2\pi=\dfrac{R^3}{3}\cdot2\cdot2\pi=\dfrac{4}{3}\pi R^3.$

> [!ejemplo]
> **Área lateral de un cilindro (integral de superficie).** La cara $\rho=R$ constante tiene normal $\hat q_1=\hat e_\rho$; su elemento de área es $h_\phi h_z\,d\phi\,dz=R\,d\phi\,dz$ (el término $h_2h_3$ de la fórmula general). El área lateral de un cilindro de radio $R$ y altura $L$:
> $$A=\int_0^L\!\!\int_0^{2\pi} R\,d\phi\,dz=R\cdot2\pi\cdot L=2\pi R L.$$

---

## En qué consiste

> [!teorema] Integral de línea
> Insertando $d\vec r=h_j\,dq_j\,\hat q_j$ y $\vec v=v_i\hat q_i$, con $\hat q_i\cdot\hat q_j=\delta_{ij}$:
> $$\int_C d\vec r\cdot\vec v=\int dq_j\,h_j\,\hat q_j\cdot v_i\hat q_i=\int dq_j\,h_j\,v_i\,\delta_{ij}=\int dq_j\,h_j\,v_j.$$
> Cada tramo del camino pesa con su factor de escala: la componente $v_j$ se integra contra la longitud física $h_j\,dq_j$.

> [!teorema] Integral de superficie
> Recordando las caras de [[Geometria Diferencial Local]], el elemento $d\vec\sigma$ normal a $\hat q_3$ es $\pm h_1h_2\,dq_1dq_2\,\hat q_3$, y análogamente para las otras dos orientaciones. El flujo de $\vec V=V_i\hat q_i$ es
> $$\int_S d\vec\sigma\cdot\vec V=\int\pm dq_1dq_2\,h_1h_2\,V_3\pm dq_2dq_3\,h_2h_3\,V_1\pm dq_1dq_3\,h_1h_3\,V_2,$$
> donde cada signo $\pm$ se elige según el signo de $d\vec\sigma\cdot\hat q_i$ (orientación de la cara respecto a la normal saliente).

> [!teorema] Integral de volumen
> Con el elemento $d\tau=h_1h_2h_3\,dq_1dq_2dq_3$, la integral de una densidad $\rho(\vec r)$ sobre un volumen $V$ es
> $$\int_V d\tau\,\rho=\int dq_1dq_2dq_3\,h_1h_2h_3\,\rho(q_1,q_2,q_3).$$
> El producto $h_1h_2h_3$ es el **jacobiano** del cambio de coordenadas para sistemas ortogonales.

> [!info] Las tres integrales de un vistazo
> | Integral | Peso | Forma |
> |---|---|---|
> | Línea | $h_j$ | $\int dq_j\,h_j\,v_j$ |
> | Superficie ($\perp\hat q_k$) | $h_ih_j$ | $\int\pm dq_idq_j\,h_ih_j\,V_k$ |
> | Volumen | $h_1h_2h_3$ | $\int dq_1dq_2dq_3\,h_1h_2h_3\,\rho$ |

---

## Resumen

> [!resumen]
> | Sistema | $h_1h_2h_3$ ($d\tau$) | Elemento de volumen |
> |---|---|---|
> | Cartesiano | $1$ | $dx\,dy\,dz$ |
> | Cilíndrico | $\rho$ | $\rho\,d\rho\,d\phi\,dz$ |
> | Esférico | $r^2\operatorname{sen}\theta$ | $r^2\operatorname{sen}\theta\,dr\,d\theta\,d\phi$ |

> [!corolario]
> Toda integral en curvilíneas se reduce a colocar el peso correcto: $h_j$ para línea, $h_ih_j$ para superficie y $h_1h_2h_3$ para volumen. Deducidas una vez en el [[index | marco general]], las fórmulas valen para cualquier sistema ortogonal; los volúmenes de cilindro y esfera salen de sustituir sus $h_i$. La misma geometría de [[Geometria Diferencial Local]] da, por flujo y circulación, la [[Divergencia General | divergencia]] y el [[Rotor General | rotor]].

> [!referencia]
> - Desplazamiento $d\vec r$ y factores: [[Factores de Escala]].
> - Caras y volumen diferenciales: [[Geometria Diferencial Local]].
> - Casos concretos: [[Sistema Cilindrico/index]] y [[Sistema Esferico/index]].
