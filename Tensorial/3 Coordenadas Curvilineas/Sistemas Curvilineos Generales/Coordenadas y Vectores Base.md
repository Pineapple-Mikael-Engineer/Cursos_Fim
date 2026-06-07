---
title: Coordenadas y Vectores Base
tags:
  - analisis-tensorial
  - teoria
  - coordenadas-curvilineas
  - factores-escala
draft: false
aliases:
  - vectores base curvilineos
  - construccion de q_i
  - curvilinear base vectors
---

# Coordenadas y Vectores Base $\hat q_i$

> [!definicion]
> El **vector base unitario** asociado a la coordenada $q_i$ se construye derivando el vector posición respecto a $q_i$ y normalizando:
> $$\hat q_i=\frac{\partial\vec r/\partial q_i}{h_i},\qquad \frac{\partial\vec r}{\partial q_i}=\frac{\partial x_j}{\partial q_i}\,\hat e_j,$$
> con $h_i=\left|\partial\vec r/\partial q_i\right|$ el [[Factores de Escala | factor de escala]]. El vector $\partial\vec r/\partial q_i$ apunta en la dirección en que se mueve $P$ al aumentar $q_i$; dividir por $h_i$ lo vuelve unitario.

> [!info]
> Sección **3.4.1** del libro (Rogan & Muñoz). Es el primer paso del marco [[index | curvilíneo general]]: una vez se tiene $\hat q_i$, las componentes de cualquier vector se obtienen por proyección $A_i=\vec A\cdot\hat q_i$. La misma derivación, particularizada, da las bases [[Sistema Cilindrico/index | cilíndrica]] y [[Sistema Esferico/index | esférica]]. El módulo de $\partial\vec r/\partial q_i$ se trata aparte en [[Factores de Escala]].

---

## Ejemplo

> [!ejemplo]
> **Bases cilíndricas $\hat e_\rho,\hat e_\phi$ derivando $\vec r$.** Partimos del vector posición escrito en cartesianas con coordenadas cilíndricas, $x=\rho\cos\phi$, $y=\rho\operatorname{sen}\phi$, $z=z$:
> $$\vec r=\rho\cos\phi\,\hat e_x+\rho\operatorname{sen}\phi\,\hat e_y+z\,\hat e_z.$$
>
> **Derivar respecto a $\rho$** (las bases $\hat e_x,\hat e_y$ son constantes):
> $$\frac{\partial\vec r}{\partial\rho}=\cos\phi\,\hat e_x+\operatorname{sen}\phi\,\hat e_y,\qquad h_\rho=\left|\frac{\partial\vec r}{\partial\rho}\right|=\sqrt{\cos^2\phi+\operatorname{sen}^2\phi}=1.$$
> Como $h_\rho=1$, el vector base ya es unitario:
> $$\hat e_\rho=\cos\phi\,\hat e_x+\operatorname{sen}\phi\,\hat e_y.$$
>
> **Derivar respecto a $\phi$:**
> $$\frac{\partial\vec r}{\partial\phi}=-\rho\operatorname{sen}\phi\,\hat e_x+\rho\cos\phi\,\hat e_y,\qquad h_\phi=\sqrt{\rho^2\operatorname{sen}^2\phi+\rho^2\cos^2\phi}=\rho.$$
> Normalizando por $h_\phi=\rho$:
> $$\hat e_\phi=\frac{1}{\rho}\left(-\rho\operatorname{sen}\phi\,\hat e_x+\rho\cos\phi\,\hat e_y\right)=-\operatorname{sen}\phi\,\hat e_x+\cos\phi\,\hat e_y.$$
> Se comprueba $\hat e_\rho\cdot\hat e_\phi=-\cos\phi\operatorname{sen}\phi+\operatorname{sen}\phi\cos\phi=0$: la base es ortonormal, como pedía el marco general. Nótese que ambas dependen de $\phi$: la base **gira** con la posición.

> [!info] La base local emana del punto $P$
> ![[base_curvilinea.svg|380]]
>
> Los vectores base $\hat q_1,\hat q_2,\hat q_3$ emanan del punto $P(q_1,q_2,q_3)$ y cambian de dirección con la posición.

---

## En qué consiste

> [!teorema] Construcción del vector base
> $$\hat q_i=\frac{1}{h_i}\,\frac{\partial\vec r}{\partial q_i},\qquad \frac{\partial\vec r}{\partial q_i}=\frac{\partial x_j}{\partial q_i}\,\hat e_j,\qquad h_i=\left|\frac{\partial\vec r}{\partial q_i}\right|.$$

> [!demostracion]
> **Paso 1 — Incrementar la coordenada $q_i$.** Mantenemos fijas las otras dos coordenadas y aumentamos $q_i$ en $dq_i$. El punto $P$ se desplaza y el vector posición cambia en $d\vec r=(\partial\vec r/\partial q_i)\,dq_i$. La dirección de este desplazamiento —la dirección en que avanza $P$ al crecer $q_i$— **define** la dirección del vector base $\hat q_i$.
>
> **Paso 2 — Expresar $\vec r$ por sus componentes cartesianas.** Como la base cartesiana es fija, escribimos $\vec r=x_j(q_1,q_2,q_3)\,\hat e_j$ con los $x_j$ dependiendo de las curvilíneas. Derivando solo los coeficientes (la regla de la cadena recae sobre los $x_j$, no sobre los $\hat e_j$):
> $$\frac{\partial\vec r}{\partial q_i}=\frac{\partial x_j}{\partial q_i}\,\hat e_j.$$
> Este vector apunta en la dirección de $\hat q_i$, pero **no** es unitario: su módulo es el factor de escala.
>
> **Paso 3 — Calcular el módulo (factor de escala).** Por ser $\hat e_j$ ortonormal,
> $$h_i=\left|\frac{\partial\vec r}{\partial q_i}\right|=\sqrt{\left(\frac{\partial x_1}{\partial q_i}\right)^2+\left(\frac{\partial x_2}{\partial q_i}\right)^2+\left(\frac{\partial x_3}{\partial q_i}\right)^2}.$$
>
> **Paso 4 — Normalizar.** Dividir el vector del Paso 2 por su módulo del Paso 3 da el vector base unitario:
> $$\hat q_i=\frac{\partial\vec r/\partial q_i}{h_i}.$$
> Aquí el índice $i$ es **libre** (aparece en ambos lados): no hay suma sobre $i$ pese a repetirse, porque la repetición está implícita en la notación de $h_i$. $\blacksquare$

> [!info] Por qué los $\hat q_i$ son variables
> Las derivadas $\partial x_j/\partial q_i$ son, en general, funciones de las coordenadas (en cilíndricas aparecen $\cos\phi$, $\operatorname{sen}\phi$). Por eso $\hat q_i$ cambia de dirección de un punto a otro: es la diferencia esencial con la base cartesiana fija y la razón de dibujar siempre la base **partiendo de $P$** (ver [[Vector Posicion]]).

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Dirección de $\hat q_i$ | sentido en que avanza $P$ al crecer $q_i$ |
> | Vector tangente | $\partial\vec r/\partial q_i=(\partial x_j/\partial q_i)\,\hat e_j$ |
> | Normalización | $\hat q_i=(\partial\vec r/\partial q_i)/h_i$ |
> | Ortonormalidad | $\hat q_i\cdot\hat q_j=\delta_{ij}$ |
> | Componente de $\vec A$ | $A_i=\vec A\cdot\hat q_i$ |

> [!corolario]
> El vector posición es el generador de toda la maquinaria: derivándolo se obtienen las direcciones de la base y, con su módulo, los [[Factores de Escala | factores de escala]]. Una vez fijada la base local $\hat q_i$, las operaciones vectoriales (punto, cruz, proyección) recuperan su forma cartesiana en cada punto, según se ve en el [[index | marco general]].

> [!referencia]
> - Módulo de $\partial\vec r/\partial q_i$: [[Factores de Escala]].
> - Vector posición de partida: [[Vector Posicion]].
> - Bases concretas: [[Sistema Cilindrico/index]] y [[Sistema Esferico/index]].
