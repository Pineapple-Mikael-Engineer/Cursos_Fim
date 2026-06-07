---
title: Sistemas Curvilíneos Generales
tags:
  - analisis-tensorial
  - teoria
  - coordenadas-curvilineas
  - factores-escala
  - index
draft: false
aliases:
  - sistemas curvilineos generales
  - coordenadas generales q1 q2 q3
  - general curvilinear coordinates
---

# Sistemas Curvilíneos Generales

> [!definicion]
> Un sistema **curvilíneo general** usa tres coordenadas genéricas $(q_1,q_2,q_3)$ con vectores base unitarios $\hat q_1,\hat q_2,\hat q_3$ **ortonormales pero variables** (dependen de la posición). Se conecta con las cartesianas mediante las transformaciones directa e inversa
> $$x_i=x_i(q_1,q_2,q_3),\qquad q_i=q_i(x_1,x_2,x_3).$$
> Cilíndricas y esféricas son casos particulares; este marco trata cualquier geometría ortogonal de una vez.

> [!info]
> Sección **3.4** del libro (Rogan & Muñoz). Generaliza los [[Sistema Cilindrico/index | cilíndricos]] y [[Sistema Esferico/index | esféricos]] del [[index | capítulo 3]] introduciendo los **factores de escala** $h_i$, con los que las operaciones vectoriales del [[Operadores en Campos/index | capítulo 2]] se reescriben en una sola forma. Se desglosa en:
> - [[Coordenadas y Vectores Base]] — construcción de $\hat q_i$ derivando $\vec r$ (cap. 3.4.1).
> - [[Factores de Escala]] — $h_i=|\partial\vec r/\partial q_i|$ y desplazamiento $d\vec r$ (cap. 3.4.1).
> - [[Geometria Diferencial Local]] — volumen y caras diferenciales (cap. 3.4.2).
> - [[Elementos Linea Superficie Volumen]] — integrales de línea, superficie y volumen (cap. 3.4.5-3.4.7).

---

## Ejemplo

> [!ejemplo]
> **Producto punto y cruz son idénticos a los cartesianos.** Por ser la base $\hat q_i$ ortonormal, $\hat q_i\cdot\hat q_j=\delta_{ij}$, así que el producto punto de dos vectores conserva su forma:
> $$\vec A\cdot\vec B=A_i\hat q_i\cdot B_j\hat q_j=A_iB_j\,\delta_{ij}=A_iB_i,$$
> donde las componentes se leen por proyección $A_i=\vec A\cdot\hat q_i$. Con la base ordenada como sistema de mano derecha, el producto cruz también mantiene la forma de Levi-Civita:
> $$\vec A\times\vec B=A_iB_j\,(\hat q_i\times\hat q_j)=\varepsilon_{ijk}\,A_iB_j\,\hat q_k.$$
> Lo único nuevo frente a las cartesianas es que la base $\hat q_i$ cambia de punto a punto; el álgebra en cada punto es la misma.

---

## En qué consiste

> [!teoria]
> La idea central es que **toda la información del sistema vive en los factores de escala** $h_i=|\partial\vec r/\partial q_i|$. Una vez conocidos los $h_i$ y la base local $\hat q_i$, el vector desplazamiento $d\vec r=h_i\,dq_i\,\hat q_i$ determina —casi mecánicamente— los elementos de arco, área y volumen y, a partir de la geometría diferencial local, los operadores gradiente, divergencia y rotor. Cartesianas, cilíndricas y esféricas se recuperan sustituyendo sus $h_i$ respectivos.

> [!info] Operaciones vectoriales en la base curvilínea
> | Operación | Forma general | Origen |
> |---|---|---|
> | Componente | $A_i=\vec A\cdot\hat q_i$ | proyección |
> | Producto punto | $\vec A\cdot\vec B=A_iB_i$ | $\hat q_i\cdot\hat q_j=\delta_{ij}$ |
> | Producto cruz | $\vec A\times\vec B=\varepsilon_{ijk}A_iB_j\hat q_k$ | mano derecha |
> | Desplazamiento | $d\vec r=h_i\,dq_i\,\hat q_i$ | factores de escala |

## Resumen

> [!resumen]
> | Subnota | Aporta |
> |---|---|
> | [[Coordenadas y Vectores Base]] | $\hat q_i=(\partial\vec r/\partial q_i)/h_i$ |
> | [[Factores de Escala]] | $h_i=\|\partial\vec r/\partial q_i\|$, $d\vec r$ |
> | [[Geometria Diferencial Local]] | $d\tau=h_1h_2h_3\,dq_1dq_2dq_3$, caras |
> | [[Elementos Linea Superficie Volumen]] | integrales en curvilíneas |

> [!corolario]
> El marco general no es una abstracción ociosa: deducir una vez las fórmulas en términos de $h_1,h_2,h_3$ evita repetir el cálculo en cada sistema. Basta sustituir $(1,\rho,1)$ para cilíndricas o $(1,r,r\operatorname{sen}\theta)$ para esféricas. La geometría diferencial local de [[Geometria Diferencial Local]] es la pieza de la que cuelgan la [[Divergencia General]] y el [[Rotor General]].

> [!referencia]
> - Casos concretos: [[Sistema Cilindrico/index]] y [[Sistema Esferico/index]].
> - Operadores cartesianos de partida: [[Operadores en Campos/index]].
> - Vector posición: [[Vector Posicion]].
