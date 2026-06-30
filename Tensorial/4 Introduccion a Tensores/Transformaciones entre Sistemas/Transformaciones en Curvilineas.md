---
title: Transformaciones en Curvilíneas
order: 4
tags:
  - analisis-tensorial
  - teoria
  - tensores
  - transformaciones
  - coordenadas-curvilineas
draft: false
aliases:
  - transformaciones en curvilineas
  - matriz de transformacion curvilinea
  - transformaciones entre sistemas curvilineos
  - curvilinear transformations
---

# Transformaciones en Curvilíneas

> [!definicion]
> Las transformaciones ortonormales se extienden a bases **curvilíneas** introduciendo los factores de escala $h_j$. La matriz de transformación es
> $$a_{ij}=\frac{\partial x'_i}{h_j\,\partial q_j}\quad(\text{curvilíneo}\to\text{cartesiano}),\qquad a_{ij}=\frac{h'_i\,\partial x'_i}{h_j\,\partial q_j}\quad(\text{curvilíneo}\to\text{curvilíneo}),$$
> y, en términos de las bases, siempre vale la forma de cosenos directores
> $$a_{ij}=(\hat q'_i\cdot\hat q_j).$$

> [!info] (opcional)
> Es la sección **4.5** del libro y un complemento al [[index | capítulo 4.3]]. Generaliza la [[Matriz de Transformacion | matriz $[a]$ cartesiana]] a bases ortonormales **curvilíneas** (cilíndricas, esféricas), usando los factores de escala $h_i$ de los [[../../3 Coordenadas Curvilineas/Sistemas Curvilineos Generales/index | sistemas curvilíneos]]. Solo cambia cómo se calcula $a_{ij}$; la ley de transformación de vectores y tensores ($v'_i=a_{ij}v_j$, $T'_{lm}=T_{rs}a_{lr}a_{ms}$) es idéntica.

---

## Ejemplo

> [!ejemplo]
> **De cilíndrico a cartesiano (caso radial).** Con $(q_1,q_2,q_3)=(\rho,\phi,z)$, factores $h_\rho=1,\ h_\phi=\rho,\ h_z=1$, y las ecuaciones $x'_1=x=\rho\cos\phi$, $x'_2=y=\rho\operatorname{sen}\phi$, $x'_3=z$, los elementos $a_{ij}=\dfrac{\partial x'_i}{h_j\,\partial q_j}$ de la primera fila ($x$) son
> $$a_{11}=\frac{1}{h_\rho}\frac{\partial x}{\partial\rho}=\cos\phi,\qquad a_{12}=\frac{1}{h_\phi}\frac{\partial x}{\partial\phi}=\frac{1}{\rho}(-\rho\operatorname{sen}\phi)=-\operatorname{sen}\phi,\qquad a_{13}=\frac{\partial x}{\partial z}=0.$$
> El factor $h_\phi=\rho$ **cancela** el $\rho$ que aparece al derivar respecto de $\phi$, dejando un coseno director puro. Completando, $[a]$ es justamente la matriz que rota $\hat q_\rho,\hat q_\phi$ a $\hat e_x,\hat e_y$:
> $$[a]=\begin{pmatrix}\cos\phi&-\operatorname{sen}\phi&0\\\operatorname{sen}\phi&\cos\phi&0\\0&0&1\end{pmatrix},$$
> que coincide con $a_{ij}=(\hat e_i\cdot\hat q_j)$ y es ortogonal ($[a][a]^\dagger=[1]$), como debe ser entre bases ortonormales.

---

## En qué consiste

> [!teoria]
> En curvilíneas, los diferenciales de arco a lo largo de la coordenada $q_j$ no son $dq_j$ sino $h_j\,dq_j$ (esa es la función del factor de escala $h_j=|\partial\vec r/\partial q_j|$). Como $a_{ij}$ debe relacionar **componentes ortonormales** —medidas a lo largo de versores unitarios—, hay que dividir cada derivada $\partial x'_i/\partial q_j$ por el $h_j$ correspondiente para normalizar. De ahí
> $$a_{ij}=\frac{\partial x'_i}{h_j\,\partial q_j}.$$
> Si el sistema de destino también es curvilíneo, sus componentes se miden a lo largo de $\hat q'_i$, lo que añade un factor $h'_i$ arriba:
> $$a_{ij}=\frac{h'_i\,\partial x'_i}{h_j\,\partial q_j}.$$

> [!proposicion] El caso cartesiano se recupera
> En cartesianas todos los factores de escala valen $1$ ($h_j=1$, $h'_i=1$). Sustituyendo,
> $$a_{ij}=\frac{\partial x'_i}{h_j\,\partial q_j}\ \xrightarrow{\,h_j=1\,}\ a_{ij}=\frac{\partial x'_i}{\partial x_j},$$
> que es exactamente la expresión de la [[Matriz de Transformacion | matriz cartesiana]] (libro 4.35). La forma de cosenos directores $a_{ij}=(\hat q'_i\cdot\hat q_j)$ es válida en todos los casos, porque no depende de cómo se parametrice la base.

## Resumen

> [!resumen]
> | Caso | Matriz $a_{ij}$ |
> |---|---|
> | Curvilíneo → cartesiano | $a_{ij}=\dfrac{\partial x'_i}{h_j\,\partial q_j}$ |
> | Curvilíneo → curvilíneo | $a_{ij}=\dfrac{h'_i\,\partial x'_i}{h_j\,\partial q_j}$ |
> | Desde las bases (siempre) | $a_{ij}=(\hat q'_i\cdot\hat q_j)$ |
> | Cartesiano ($h_j=1$) | $a_{ij}=\partial x'_i/\partial x_j$ |

> [!corolario]
> Pasar a curvilíneas no cambia la **ley** de transformación de vectores y tensores, solo cómo se calcula $a_{ij}$: los factores de escala $h_j$ normalizan las derivadas para que $[a]$ siga siendo una matriz ortogonal entre bases ortonormales. La forma $a_{ij}=\hat q'_i\cdot\hat q_j$ es la receta universal; las fórmulas con $h$ son el atajo cuando solo se tienen las ecuaciones de coordenadas.

> [!referencia]
> - Versión cartesiana de la matriz: [[Matriz de Transformacion]].
> - Factores de escala y bases curvilíneas: [[../../3 Coordenadas Curvilineas/Sistemas Curvilineos Generales/index]].
> - Ley que se aplica con esta $[a]$: [[Transformaciones Tensoriales]].
