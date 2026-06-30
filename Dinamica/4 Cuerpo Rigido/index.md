---
title: Cuerpo Rígido
order: 4
tags:
  - dinamica
  - teoria
  - cuerpo-rigido
  - index
draft: false
aliases:
  - cuerpo rígido
  - sólido rígido
  - dinámica del cuerpo rígido
---

# Cuerpo Rígido

> [!definicion]
> Un **cuerpo rígido** es un sistema de partículas cuyas **distancias mutuas no cambian**. Su configuración necesita solo seis números (tres de posición del centro de masa $G$, tres de orientación), y su movimiento se descompone en **traslación** de $G$ más **rotación** con velocidad angular $\vec\omega$. La velocidad de cualquier punto es
> $$\vec v_P=\vec v_G+\vec\omega\times\vec r_{P/G}.$$

> [!info]
> Cuarto bloque del curso de [[Dinamica/index | Dinámica]]. **Aplica** la [[3 Inercia/index | inercia]] (que ya da $\vec H$, $T$, $\vec\tau$) y el [[Operador Derivada en Base Movil | operador en base móvil]] (que da $\vec v_P,\vec a_P$), y extiende los teoremas de [[Sistemas de Particulas | sistemas de partículas]]. Referencia: Goldstein cap. 5; Taylor cap. 10.

---

## El programa del cuerpo rígido

![[velocidad_solido.svg|460]]

*La velocidad de un punto del sólido: traslación del CM más rotación, $\vec v_P=\vec v_G+\vec\omega\times\vec r_{P/G}$.*

> [!teoria] Cinemática y luego cinética
> Igual que en la partícula, primero se **describe** y luego se **explica**:
> - **Cinemática** — cómo se mueven los puntos del sólido. En el **plano**: rotación de eje fijo, velocidad y aceleración relativas, centro instantáneo de rotación, rodadura. → [[Cinematica Plana]]. En **3D**: $\vec v_P=\vec v_G+\vec\omega\times\vec r$, $\vec a_P=\vec a_G+\vec\alpha\times\vec r+\vec\omega\times(\vec\omega\times\vec r)$ (del operador). → [[Cinematica en 3D]].
> - **Cinética** — las ecuaciones de Newton-Euler. En el **plano** ($\vec\omega\parallel\hat k$, sin término giroscópico) basta $\sum\vec F=m\vec a_G$ y $\sum M_G=I_G\alpha$. → [[Dinamica Plana 2D]]. En **3D** aparece $\sum\vec M=\mathbf I\vec\alpha+\vec\omega\times(\mathbf I\vec\omega)$, las **ecuaciones de Euler**. → [[Ecuaciones de Euler 3D]].

> [!teoria] El efecto estrella: el giróscopo
> El término giroscópico $\vec\omega\times(\mathbf I\vec\omega)$ —ausente en 2D— produce la **precesión**: un cuerpo que gira rápido responde a un torque moviéndose **perpendicular** a él, no en su dirección. Es la dinámica más contraintuitiva del curso. → [[Movimiento Giroscopico]].

## Mapa del capítulo

> [!info] Las notas de este capítulo
> | Nota | Contenido |
> |:---|:---|
> | [[Cinematica Plana]] | rotación, velocidad/aceleración relativa, CIR, rodadura |
> | [[Cinematica en 3D]] | $\vec v_P,\vec a_P$ vía el operador en base móvil |
> | [[Dinamica Plana 2D]] | Newton-Euler 2D; energía e impulso-momento |
> | [[Ecuaciones de Euler 3D]] | $\sum\vec M=\mathbf I\vec\alpha+\vec\omega\times(\mathbf I\vec\omega)$ |
> | [[Movimiento Giroscopico]] | precesión estacionaria; giróscopo |

> [!corolario]
> El cuerpo rígido no introduce principios nuevos: combina la cinemática del operador en base móvil con la cinética que el tensor de inercia ya entregó. Traslación de $G$ más rotación con $\vec\omega$ es todo lo que hay —pero en 3D esa rotación esconde el giróscopo—.

> [!referencia]
> Goldstein cap. 5; Taylor cap. 10. Viene de [[3 Inercia/index | Inercia]]; precede a [[5 Vibraciones/index | Vibraciones]].
