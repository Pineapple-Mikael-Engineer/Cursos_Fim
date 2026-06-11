---
title: Deducciones (Tensor de Inercia)
tags:
  - dinamica
  - teoria
  - inercia
  - index
draft: false
aliases:
  - deducciones del tensor de inercia
  - integrales útiles
---

# Deducciones desde Primeros Principios

> [!definicion]
> Esta subcarpeta **deduce**, integrando sobre el cuerpo, las tres magnitudes rotacionales del sólido a
> partir de la velocidad de un punto $\vec v_p=\vec v_c+\vec\omega\times\vec r_{p/c}$ y de la definición
> del tensor de inercia. Son las "integrales útiles": el **momento angular** $\vec H$, el **torque**
> $\vec\tau$ (ecuación de Euler) y la **energía cinética** $T$.

> [!info]
> Núcleo deductivo de la [[3 Inercia/index | inercia]] ([[Dinamica/index | Dinámica]]): justifica de
> dónde sale que $\vec H=\mathbf I\vec\omega$, etc. Usa la cinemática del
> [[Operador Derivada en Base Movil | sólido]]. Referencia: Goldstein §5.

---

## El método común

> [!teoria] Tres pasos que se repiten
> Las tres deducciones siguen el **mismo patrón**:
> 1. Escribir la magnitud como **integral sobre $dm$** del aporte de cada elemento.
> 2. Sustituir $\vec v_p=\vec v_c+\vec\omega\times\vec r_{p/c}$ (y $\vec a_p$ para el torque).
> 3. Separar términos: los que llevan $\int\vec r_{p/c}\,dm=\vec0$ (propiedad del **centro de masa**)
>    **se anulan**, y los que sobreviven, vía la identidad $\vec r\times(\vec\omega\times\vec r)=\vec\omega\,r^2-\vec r(\vec r\cdot\vec\omega)$
>    (o $\epsilon_{ijk}\epsilon_{mnk}=\delta_{im}\delta_{jn}-\delta_{in}\delta_{jm}$), hacen aparecer el
>    segundo momento $Q_{ij}=\int r_ir_j\,dm$ y, con él, $\mathbf I=\mathrm{Tr}(\mathbf Q)\mathbb 1-\mathbf Q$.
>
> Así, sin postular nada, el tensor de inercia emerge como la estructura que conecta $\vec\omega$ con
> $\vec H$, $\vec\tau$ y $T$.

## Mapa de la sección

> [!info] Las deducciones
> | Nota | Resultado |
> |:---|:---|
> | [[Deduccion del Momento Angular]] | $\vec H^o=\mathbf I_c\vec\omega+m\,\vec r_{c/o}\times\vec v_c$ |
> | [[Deduccion del Torque]] | $\vec\tau^o=\mathbf I_c\vec\alpha+\vec\omega\times(\mathbf I_c\vec\omega)+\vec r_{c/o}\times\vec F$ |
> | [[Deduccion de la Energia Cinetica]] | $T=\tfrac12 m v_c^2+\tfrac12\,\vec\omega\cdot\mathbf I_c\vec\omega$ |

> [!corolario]
> Las tres magnitudes del sólido no son axiomas: se **integran** desde la cinemática rígida, y todas
> destilan el mismo tensor de inercia. En el centro de masa ($O=C$) toman su forma más limpia, base de
> las [[Ecuaciones de Euler 3D | ecuaciones de Euler]].

> [!referencia]
> Goldstein §5. Tensor: [[Tensor de Inercia]]. Aplicación: [[Ecuaciones de Euler 3D]].
