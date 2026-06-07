---
title: Geometría Diferencial Local
tags:
  - analisis-tensorial
  - teoria
  - coordenadas-curvilineas
  - factores-escala
draft: false
aliases:
  - geometria diferencial local
  - volumen diferencial curvilineo
  - differential volume element
---

# Geometría Diferencial Local

> [!definicion]
> El elemento de volumen diferencial en coordenadas curvilíneas **no es un cubo**: sus aristas miden $h_i\,dq_i$ y sus caras pueden tener curvatura. Su volumen y sus caras inferior y superior (normales a $\hat q_3$) son
> $$d\tau=h_1h_2h_3\,dq_1\,dq_2\,dq_3,$$
> $$d\vec\sigma_{\text{inf}}=-h_1h_2\,dq_1\,dq_2\,\hat q_3,\qquad d\vec\sigma_{\text{sup}}=+h_1h_2\,dq_1\,dq_2\,\hat q_3.$$

> [!info]
> Sección **3.4.2** del libro (Rogan & Muñoz). Es la **base geométrica** de la que se deducen, en curvilíneas generales, la [[Divergencia General]], el [[Rotor General]] y las [[Elementos Linea Superficie Volumen | integrales de superficie y volumen]]. Usa los [[Factores de Escala | factores de escala]] como longitudes de arista.

---

## Ejemplo

> [!ejemplo]
> **Volumen diferencial cilíndrico.** Con $(q_1,q_2,q_3)=(\rho,\phi,z)$ y factores $(h_\rho,h_\phi,h_z)=(1,\rho,1)$, las tres aristas miden $h_\rho\,d\rho=d\rho$, $h_\phi\,d\phi=\rho\,d\phi$ y $h_z\,dz=dz$. El volumen es su producto:
> $$d\tau=h_\rho h_\phi h_z\,d\rho\,d\phi\,dz=\rho\,d\rho\,d\phi\,dz.$$
> El factor $\rho$ —que viene de $h_\phi$— es lo que distingue este volumen del cubo cartesiano $dx\,dy\,dz$: la "caja" es más ancha en la dirección $\hat\phi$ cuanto más lejos del eje, y la cara normal a $\hat\rho$ es un trozo de superficie cilíndrica curva, no plana.

> [!info] El volumen diferencial curvilíneo
> ![[volumen_curvilineo.svg|460]]
>
> Volumen diferencial en coordenadas curvilíneas: aristas $h_i\,dq_i$, caras curvas.

---

## En qué consiste

> [!teoria]
> Se construye el volumen eligiendo un vértice de partida $(q_1,q_2,q_3)$ y desplazando los otros siete vértices con pequeños incrementos $dq_1,dq_2,dq_3$. En el límite diferencial, la longitud de cada arista es $dq_i$ por su factor de escala, evaluado en el conjunto de coordenadas correspondiente a su valor en ese borde. Como los $h_i$ pueden variar con la posición, las aristas opuestas tienen longitudes ligeramente distintas y las caras se curvan: el cuerpo es un "cubo deformado", no un paralelepípedo recto.

> [!teorema] Volumen y caras diferenciales
> $$d\tau=h_1h_2h_3\,dq_1\,dq_2\,dq_3\Big|_{(q_1,q_2,q_3)},$$
> $$d\vec\sigma_{\text{inf}}=-h_1h_2\,dq_1\,dq_2\,\hat q_3\Big|_{(q_1,q_2,q_3)},\qquad d\vec\sigma_{\text{sup}}=+h_1h_2\,dq_1\,dq_2\,\hat q_3\Big|_{(q_1,q_2,q_3+dq_3)}.$$

> [!demostracion]
> **Paso 1 — Aristas como $h_i\,dq_i$.** Al fijar dos coordenadas e incrementar $q_i$ en $dq_i$, la arista correspondiente del volumen tiene longitud $|h_i\,dq_i|$ (interpretación del [[Factores de Escala | factor de escala]]). Así, las tres aristas que parten del vértice $(q_1,q_2,q_3)$ miden $h_1\,dq_1$, $h_2\,dq_2$ y $h_3\,dq_3$.
>
> **Paso 2 — Volumen como producto de aristas ortogonales.** Por ser la base $\hat q_i$ ortonormal, las tres aristas son mutuamente perpendiculares en el límite diferencial, y el volumen del paralelepípedo es el producto de sus longitudes:
> $$d\tau=(h_1\,dq_1)(h_2\,dq_2)(h_3\,dq_3)=h_1h_2h_3\,dq_1\,dq_2\,dq_3,$$
> con los $h_i$ evaluados en el vértice $(q_1,q_2,q_3)$.
>
> **Paso 3 — Cara inferior (normal a $\hat q_3$).** La cara construida por las aristas $h_1\,dq_1\,\hat q_1$ y $h_2\,dq_2\,\hat q_2$ tiene área $h_1h_2\,dq_1\,dq_2$ y su normal apunta en $\pm\hat q_3$. Para la cara **inferior**, la normal saliente del volumen es **antiparalela** a $\hat q_3$, de ahí el signo menos:
> $$d\vec\sigma_{\text{inf}}=-h_1h_2\,dq_1\,dq_2\,\hat q_3,$$
> evaluada en $q_3$.
>
> **Paso 4 — Cara superior.** La cara opuesta está en $q_3+dq_3$; su normal saliente es **paralela** a $\hat q_3$, sin signo menos:
> $$d\vec\sigma_{\text{sup}}=+h_1h_2\,dq_1\,dq_2\,\hat q_3,$$
> con $h_1,h_2$ y $\hat q_3$ evaluados en $(q_1,q_2,q_3+dq_3)$. La diferencia entre las dos caras —que $h_1h_2$ y $\hat q_3$ se evalúan en planos distintos— es justo lo que, al sumar el flujo, produce la [[Divergencia General | divergencia]]. $\blacksquare$

> [!info] Por qué no es un cubo
> Dos rasgos rompen la imagen del cubo: (1) las aristas **cambian de longitud** con la posición, porque $h_i=h_i(q_1,q_2,q_3)$ (en cilíndricas, la arista $\rho\,d\phi$ crece con $\rho$); (2) las caras **se curvan**, porque las curvas coordenadas no son rectas (la cara $\rho$ constante es un trozo de cilindro). En cartesianas, con $h_i=1$ constantes y curvas coordenadas rectas, el volumen vuelve a ser el cubo $dx\,dy\,dz$.

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Arista en dirección $i$ | $h_i\,dq_i$ |
> | Volumen | $d\tau=h_1h_2h_3\,dq_1\,dq_2\,dq_3$ |
> | Cara inferior ($\perp\hat q_3$) | $-h_1h_2\,dq_1\,dq_2\,\hat q_3$ en $q_3$ |
> | Cara superior ($\perp\hat q_3$) | $+h_1h_2\,dq_1\,dq_2\,\hat q_3$ en $q_3+dq_3$ |
> | Cartesiano | cubo $dx\,dy\,dz$ ($h_i=1$) |

> [!corolario]
> Este pequeño volumen deformado es la pieza geométrica de la que cuelga todo el cálculo vectorial curvilíneo: contabilizar el flujo a través de sus seis caras da la [[Divergencia General | divergencia]], la circulación por sus bordes da el [[Rotor General | rotor]], y su volumen $h_1h_2h_3\,dq_1dq_2dq_3$ es el peso de las [[Elementos Linea Superficie Volumen | integrales de volumen]].

> [!referencia]
> - Longitud de las aristas: [[Factores de Escala]].
> - Integrales que usan estas caras y volumen: [[Elementos Linea Superficie Volumen]].
> - Operadores deducidos de esta geometría: [[Divergencia General]] y [[Rotor General]].
