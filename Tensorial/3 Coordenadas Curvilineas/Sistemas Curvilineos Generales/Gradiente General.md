---
title: Gradiente en Coordenadas Curvilíneas
order: 5
tags:
  - analisis-tensorial
  - teoria
  - coordenadas-curvilineas
  - gradiente
draft: false
aliases:
  - gradiente general
  - gradiente curvilineo
  - nabla phi curvilineo
  - general gradient
  - curvilinear gradient
---

# Gradiente en Coordenadas Curvilíneas $\vec\nabla\Phi$

> [!definicion]
> En un sistema curvilíneo ortogonal $(q_1,q_2,q_3)$ con factores de escala $h_i$, el **gradiente** de un campo escalar $\Phi$ es
> $$\vec\nabla\Phi=\frac{1}{h_i}\frac{\partial\Phi}{\partial q_i}\,\hat q_i\qquad(\text{suma sobre }i),$$
> es decir, la componente $i$-ésima vale $(\vec\nabla\Phi)_i=\dfrac{1}{h_i}\dfrac{\partial\Phi}{\partial q_i}$. El factor $1/h_i$ convierte la derivada respecto a la coordenada en una derivada respecto a la **longitud** física a lo largo de $\hat q_i$.

> [!info]
> Sección **3.4.8** del libro, dentro de [[index | sistemas curvilíneos generales]]. Generaliza el gradiente cartesiano $\vec\nabla\Phi=(\partial\Phi/\partial x_i)\hat e_i$ del [[Operadores en Campos/index | capítulo 2]] al caso $h_i\neq1$. Se apoya en los [[Factores de Escala]] y en la forma del desplazamiento $d\vec r=h_i\,dq_i\,\hat q_i$ de [[Elementos Linea Superficie Volumen]]. Sus hermanas son la [[Divergencia General]] y el [[Rotor General]].

---

## Ejemplo

> [!ejemplo]
> **Recuperar los gradientes cilíndrico y esférico.** Basta sustituir los factores de escala en $(\vec\nabla\Phi)_i=\frac{1}{h_i}\frac{\partial\Phi}{\partial q_i}$.
>
> *Cilíndrico* $(\rho,\phi,z)$, con $h_\rho=1,\ h_\phi=\rho,\ h_z=1$:
> $$\vec\nabla\Phi=\frac{\partial\Phi}{\partial\rho}\,\hat q_\rho+\frac{1}{\rho}\frac{\partial\Phi}{\partial\phi}\,\hat q_\phi+\frac{\partial\Phi}{\partial z}\,\hat q_z.$$
> El $1/\rho$ en la componente angular sale solo: avanzar $d\phi$ recorre un arco $\rho\,d\phi$, no $d\phi$.
>
> *Esférico* $(r,\theta,\phi)$, con $h_r=1,\ h_\theta=r,\ h_\phi=r\operatorname{sen}\theta$:
> $$\vec\nabla\Phi=\frac{\partial\Phi}{\partial r}\,\hat q_r+\frac{1}{r}\frac{\partial\Phi}{\partial\theta}\,\hat q_\theta+\frac{1}{r\operatorname{sen}\theta}\frac{\partial\Phi}{\partial\phi}\,\hat q_\phi.$$
> En cartesianas ($h_i=1$) los factores desaparecen y se recupera $\vec\nabla\Phi=(\partial\Phi/\partial x_i)\hat e_i$.

---

## Demostración

> [!teorema]
> Para todo campo escalar $\Phi$ diferenciable, sus componentes curvilíneas son $(\vec\nabla\Phi)_i=\dfrac{1}{h_i}\dfrac{\partial\Phi}{\partial q_i}$.

> [!demostracion]
> Se parte de la **definición geométrica** del gradiente, válida en cualquier sistema: la variación $d\Phi$ entre dos puntos vecinos es la proyección del gradiente sobre el desplazamiento,
> $$d\Phi=\vec\nabla\Phi\cdot d\vec r.$$
>
> **Paso 1 — desplazamiento curvilíneo.** En un sistema ortogonal el desplazamiento diferencial es $d\vec r=h_j\,dq_j\,\hat q_j$ (suma sobre $j$); cada coordenada $q_j$ aporta un tramo de longitud $h_j\,dq_j$ en la dirección $\hat q_j$. Sustituyendo,
> $$d\Phi=\vec\nabla\Phi\cdot\hat q_j\,h_j\,dq_j.$$
>
> **Paso 2 — comparar con el cálculo diferencial.** Por otro lado, $\Phi$ es función de $(q_1,q_2,q_3)$ y su diferencial total es
> $$d\Phi=\frac{\partial\Phi}{\partial q_i}\,dq_i.$$
> Igualando ambas expresiones de $d\Phi$:
> $$\frac{\partial\Phi}{\partial q_i}\,dq_i=\big(\vec\nabla\Phi\cdot\hat q_j\big)\,h_j\,dq_j.$$
>
> **Paso 3 — identificar componente a componente.** Los $dq_i$ son independientes, así que la igualdad debe cumplirse término a término. El coeficiente de $dq_i$ a cada lado da
> $$\frac{\partial\Phi}{\partial q_i}=\big(\vec\nabla\Phi\cdot\hat q_i\big)\,h_i=h_i\,(\vec\nabla\Phi)_i,$$
> donde $(\vec\nabla\Phi)_i=\vec\nabla\Phi\cdot\hat q_i$ es la componente sobre $\hat q_i$. Despejando,
> $$(\vec\nabla\Phi)_i=\frac{1}{h_i}\frac{\partial\Phi}{\partial q_i}\quad\Longrightarrow\quad\vec\nabla\Phi=\frac{1}{h_i}\frac{\partial\Phi}{\partial q_i}\,\hat q_i.\qquad\blacksquare$$

---

## Resumen

> [!resumen]
> | Aspecto | Expresión |
> |---|---|
> | Componente $i$ | $(\vec\nabla\Phi)_i=\dfrac{1}{h_i}\dfrac{\partial\Phi}{\partial q_i}$ |
> | Forma compacta | $\vec\nabla\Phi=\dfrac{1}{h_i}\dfrac{\partial\Phi}{\partial q_i}\hat q_i$ |
> | Cilíndrico | $\partial_\rho\Phi\,\hat q_\rho+\tfrac1\rho\partial_\phi\Phi\,\hat q_\phi+\partial_z\Phi\,\hat q_z$ |
> | Esférico | $\partial_r\Phi\,\hat q_r+\tfrac1r\partial_\theta\Phi\,\hat q_\theta+\tfrac{1}{r\operatorname{sen}\theta}\partial_\phi\Phi\,\hat q_\phi$ |
> | Cartesiano | $h_i=1\Rightarrow\vec\nabla\Phi=\partial_{x_i}\Phi\,\hat e_i$ |

> [!corolario]
> El gradiente curvilíneo es el más simple de los tres operadores generales: la única diferencia con el cartesiano es el factor $1/h_i$ que reescala cada derivada parcial a una derivada por unidad de longitud física. Es la pieza de partida para la [[Divergencia General | divergencia]] y el [[Rotor General | rotor]], que requieren además la geometría completa de las caras del volumen.

> [!referencia]
> - Factores de escala $h_i=|\partial\vec r/\partial q_i|$: [[Factores de Escala]].
> - Desplazamiento $d\vec r=h_i\,dq_i\,\hat q_i$: [[Elementos Linea Superficie Volumen]].
> - Operadores hermanos: [[Divergencia General]], [[Rotor General]].
