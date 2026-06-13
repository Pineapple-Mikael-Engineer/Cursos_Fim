---
title: Inercia
tags:
  - dinamica
  - teoria
  - inercia
  - index
draft: false
aliases:
  - inercia
  - tensor de inercia
  - momento de inercia
---

# Inercia

> [!definicion]
> El **tensor de inercia** $\mathbf I$ es la propiedad que codifica **cómo se distribuye la masa** de un
> cuerpo rígido respecto a un punto: es el análogo rotacional de la masa. De una sola integral de
> segundo momento,
> $$\mathbf I=\int(r^2\,\mathbb 1-\vec r\,\vec r^{\,T})\,dm,\qquad I_{ij}=\int(r^2\delta_{ij}-r_i r_j)\,dm,$$
> salen las tres magnitudes rotacionales del sólido: el **momento angular** $\vec H=\mathbf I\vec\omega$,
> la **energía cinética** $T=\tfrac12\vec\omega\cdot\mathbf I\vec\omega$ y el **torque**
> $\vec\tau=\mathbf I\vec\alpha+\vec\omega\times(\mathbf I\vec\omega)$.

> [!info]
> Tercer bloque del curso de [[Dinamica/index | Dinámica]], **antes** del [[4 Cuerpo Rigido/index| cuerpo rígido]] porque es su prerrequisito. Se construye sobre la velocidad de un punto del sólido
> $\vec v_p=\vec v_c+\vec\omega\times\vec r$, que viene del
> [[Operador Derivada en Base Movil | operador en base móvil]]. Referencia: Goldstein, cap. 5.

---

## La distribución de masa, hecha tensor

> [!teoria] Una integral, tres consecuencias
> El sólido es un sistema continuo de masa; integrando $\vec v_p=\vec v_c+\vec\omega\times\vec r$ sobre
> el cuerpo aparece **siempre** la misma estructura, el **segundo momento** $Q_{ij}=\int r_i r_j\,dm$,
> y con él el tensor de inercia $\mathbf I=\mathrm{Tr}(\mathbf Q)\,\mathbb 1-\mathbf Q$. De ahí, desde
> primeros principios, se deducen las tres magnitudes del sólido:
>
> ![[cuerpo_inercia.svg|520]]
>
> *Cada elemento de masa $dm$ a posición $\vec r$ contribuye al tensor; integrando sobre todo el
> cuerpo $N$ se obtiene $\mathbf I$.*
>
> - **Momento angular:** $\vec H=\mathbf I\vec\omega$. → [[Deduccion del Momento Angular]].
> - **Torque (ecuación de Euler):** $\vec\tau=\mathbf I\vec\alpha+\vec\omega\times(\mathbf I\vec\omega)$.
>   → [[Deduccion del Torque]].
> - **Energía cinética:** $T=\tfrac12 m v_c^2+\tfrac12\vec\omega\cdot\mathbf I\vec\omega$.
>   → [[Deduccion de la Energia Cinetica]].
>
> Las tres viven en la subcarpeta [[Deducciones/index | Deducciones]].

> [!teoria] Qué hay que saber del tensor
> El tensor de inercia tiene estructura propia, que ocupa el resto de la sección:
> - **Definición y componentes:** momentos (diagonal) y productos (fuera); es **simétrico** y
>   **definido positivo**. Fijar **una** convención de signo. → [[Tensor de Inercia]].
> - **Ejes principales:** al diagonalizarlo ($\mathbf I\vec v=\lambda\vec v$) desaparecen los
>   productos; sus autovalores son los momentos principales. → [[Ejes Principales de Inercia]].
> - **Cambio de punto:** el **teorema del eje paralelo** lo traslada del CM a otro punto.
>   → [[Teorema del Eje Paralelo]].
> - **Cuerpos comunes:** tabla de momentos (varilla, disco, esfera…) y la distinción masa/área.
>   → [[Momentos de Inercia de Figuras]].

## Mapa de la sección

> [!info] Las notas de esta sección
> | Nota | Contenido |
> |:---|:---|
> | [[Tensor de Inercia]] | $I_{ij}=\int(r^2\delta_{ij}-r_ir_j)dm$; componentes; convención de signo |
> | [[Ejes Principales de Inercia]] | autovalores $\mathbf I\vec v=\lambda\vec v$; forma diagonal |
> | [[Teorema del Eje Paralelo]] | $\mathbf I_O=\mathbf I_G+m[(d^2)\mathbb 1-\vec d\vec d^{\,T}]$ |
> | [[Momentos de Inercia de Figuras]] | tabla de cuerpos; masa ($dm$) vs área ($dA$); radio de giro |
> | [[Deducciones/index]] | $\vec H$, $\vec\tau$, $T$ desde primeros principios |

> [!corolario]
> El tensor de inercia es a la rotación lo que la masa a la traslación: una sola integral que, aplicada
> a $\vec\omega$, da el momento angular, la energía y el torque. Construirlo bien —y entender sus ejes
> principales— es la llave de toda la dinámica del cuerpo rígido.

> [!referencia]
> Goldstein, cap. 5; Taylor, cap. 10. Viene de [[2 Movimiento Relativo/index | Movimiento relativo]];
> se aplica en [[4 Cuerpo Rigido/index| Cuerpo rígido]].
