---
title: Sistemas de Coordenadas Curvilíneos
tags:
  - analisis-tensorial
  - teoria
  - coordenadas-curvilineas
  - index
draft: false
aliases:
  - coordenadas curvilineas
  - capitulo 3 tensorial
  - cilindricas esfericas
  - curvilinear coordinates
---

# Sistemas de Coordenadas Curvilíneos

> [!definicion]
> Un sistema de coordenadas es **curvilíneo** si sus vectores base $\hat{q}_1,\hat{q}_2,\hat{q}_3$ son ortonormales pero **dependen de la posición** (sus direcciones cambian de un punto a otro). Los casos más comunes son el **cilíndrico** $(\rho,\phi,z)$ y el **esférico** $(r,\theta,\phi)$; ambos son casos particulares de un marco general gobernado por los **factores de escala** $h_i$.

> [!info]
> Es el **capítulo 3** del libro (Rogan & Muñoz, Parte I). Generaliza los [[Operadores en Campos/index | operadores del capítulo 2]] a geometrías que respetan la simetría del problema. Se desglosa en:
> - [[Vector Posicion]] — cómo se dibuja y descompone $\vec r$.
> - [[Sistema Cilindrico/index | Sistema Cilíndrico]] — $(\rho,\phi,z)$.
> - [[Sistema Esferico/index | Sistema Esférico]] — $(r,\theta,\phi)$.
> - [[Sistemas Curvilineos Generales/index | Sistemas Curvilíneos Generales]] — $(q_1,q_2,q_3)$, factores de escala $h_i$, y grad/div/rot generales.

---

## Ejemplo

> [!ejemplo]
> **Por qué cambiar de coordenadas: el campo de una carga puntual.** En cartesianas, el campo de una carga $q$ en el origen es
> $$\vec E=q\,\frac{x\,\hat x+y\,\hat y+z\,\hat z}{(x^2+y^2+z^2)^{3/2}},$$
> una expresión engorrosa que esconde la simetría. En **esféricas**, donde la base $\hat e_r$ apunta radialmente, el mismo campo es
> $$\vec E=\frac{q}{r^2}\,\hat e_r.$$
> La física —campo radial que decae como $1/r^2$— queda a la vista. Elegir las coordenadas que respetan la simetría del problema es la razón de ser de este capítulo.

> [!info] Los tres sistemas de un vistazo
> ![[coordenadas_comparacion.svg|620]]
>
> Cartesiano (base fija), cilíndrico $(\rho,\phi,z)$ y esférico $(r,\theta,\phi)$: en los curvilíneos los vectores base giran al moverse el punto $P$.

---

## En qué consiste

> [!teoria]
> En cartesianas la base $\hat e_i$ es fija: el mismo $\hat e_1$ en todo el espacio. En curvilíneas, cada vector base apunta en la dirección en la que se mueve $P$ al **aumentar** su coordenada; como $P$ se mueve, esas direcciones cambian. Por eso un vector y su base deben dibujarse **emanando del mismo punto $P$** (no del origen), o las componentes pierden sentido.
>
> Todo el aparato del [[Operadores en Campos/index | capítulo 2]] (gradiente, divergencia, rotor, integrales) se reescribe en curvilíneas introduciendo los **factores de escala** $h_i=|\partial\vec r/\partial q_i|$, que miden cuánto se desplaza $\vec r$ por unidad de coordenada. Con ellos, las fórmulas cartesianas se recuperan como el caso $h_i=1$.

> [!info] Comparación de los tres sistemas
> | Sistema | Coordenadas | Factores de escala | Base |
> |---|---|---|---|
> | Cartesiano | $(x,y,z)$ | $1,1,1$ | $\hat e_x,\hat e_y,\hat e_z$ (fija) |
> | Cilíndrico | $(\rho,\phi,z)$ | $1,\rho,1$ | $\hat e_\rho,\hat e_\phi,\hat e_z$ |
> | Esférico | $(r,\theta,\phi)$ | $1,r,r\operatorname{sen}\theta$ | $\hat e_r,\hat e_\theta,\hat e_\phi$ |

## Resumen

> [!resumen]
> | Subnota | Aporta |
> |---|---|
> | [[Vector Posicion]] | $\vec r$ y su descomposición |
> | [[Sistema Cilindrico/index]] | $(\rho,\phi,z)$, base y operaciones |
> | [[Sistema Esferico/index]] | $(r,\theta,\phi)$, base y operaciones |
> | [[Sistemas Curvilineos Generales/index]] | $h_i$, grad/div/rot generales |

> [!corolario]
> Las coordenadas curvilíneas no cambian la física, cambian su descripción: eligiendo la base que sigue la simetría del problema, las expresiones se simplifican. El precio es que la base ya no es fija, lo que obliga a introducir los factores de escala $h_i$. Con ellos, el [[Sistemas Curvilineos Generales/Gradiente General | gradiente]], la [[Sistemas Curvilineos Generales/Divergencia General | divergencia]] y el [[Sistemas Curvilineos Generales/Rotor General | rotor]] adoptan una forma única válida para cilíndricas, esféricas y cualquier otra geometría ortogonal.

> [!referencia]
> - Operadores en cartesianas (base): [[Operadores en Campos/index]].
> - Marco general y factores de escala: [[Sistemas Curvilineos Generales/index]].
> - Aplicación de tensores en curvilíneas: [[Introduccion a Tensores/index]].
