---
title: Teorema de Gauss
tags:
  - analisis-tensorial
  - teoria
  - calculo-vectorial
  - teoremas-integrales
  - divergencia
draft: false
aliases:
  - teorema de la divergencia
  - teorema de Gauss
  - divergence theorem
  - Gauss theorem
---

# Teorema de Gauss

> [!definicion]
> Para todo campo vectorial $\vec A$ con divergencia definida en un volumen $V$ encerrado por la superficie cerrada $S$,
> $$\int_V d\tau\,\vec\nabla\cdot\vec A=\oint_S d\vec\sigma\cdot\vec A.$$
> El **flujo** de $\vec A$ que atraviesa $S$ es igual a la integral de su divergencia sobre el volumen interior. $d\vec\sigma=\hat n\,d\sigma$ apunta hacia **afuera**.

> [!info]
> Es el *cap 2.5.1* del [[index | capítulo 2.5]] (Rogan & Muñoz). Se deduce de la [[Operadores Diferenciales/Divergencia | definición integral de la divergencia]] (cap. 2.3) y es el tronco del que se derivan el [[Teorema de Green]] y el [[Teorema de Helmholtz]]. La frontera $S$ se integra con el elemento $d\vec\sigma$ de los [[Operadores Integrales/index | operadores integrales]] (cap. 2.2).

---

## Ejemplo

> [!ejemplo]
> **Verificación para $\vec A=(x,y,z)$ en la esfera de radio $R$.** Aquí $\vec\nabla\cdot\vec A=\dfrac{\partial x}{\partial x}+\dfrac{\partial y}{\partial y}+\dfrac{\partial z}{\partial z}=3$.
>
> **Lado del volumen.** Como la divergencia es constante,
> $$\int_V d\tau\,\vec\nabla\cdot\vec A=3\int_V d\tau=3\cdot\frac{4}{3}\pi R^3=4\pi R^3.$$
>
> **Lado de la superficie.** Sobre la esfera $\vec r=R\,\hat r$ y la normal exterior es $\hat n=\hat r$, luego $\vec A\cdot\hat n=\vec r\cdot\hat r=R$. Como es constante sobre $S$,
> $$\oint_S d\vec\sigma\cdot\vec A=R\oint_S d\sigma=R\cdot 4\pi R^2=4\pi R^3.$$
>
> Ambos lados coinciden: $4\pi R^3=4\pi R^3$. (Para el campo $\vec A=\vec r$ el flujo $=3V$ para *cualquier* volumen, lo que ofrece una forma rápida de medir el volumen vía flujo.)

---

## Demostración

> [!info] Volúmenes adyacentes
> ![[gauss_volumenes.svg|380]]
>
> Al sumar dos volúmenes contiguos, las contribuciones de la cara común se cancelan ($\vec A\cdot d\vec\sigma_1+\vec A\cdot d\vec\sigma_2=0$); solo sobrevive la superficie exterior.

> [!teorema]
> $$\int_V d\tau\,\vec\nabla\cdot\vec A=\oint_S d\vec\sigma\cdot\vec A.$$

> [!demostracion]
> **Paso 1 — Definición integral de la divergencia.** La divergencia se define integrando $\vec A$ sobre una superficie cerrada infinitesimal y dividiendo por el volumen que encierra. Reescrita sin el cociente,
> $$\vec\nabla\cdot\vec A\,d\tau=\lim_{S\to0}\oint_S d\vec\sigma\cdot\vec A.$$
> Aquí $S$ rodea por completo el volumen $d\tau$, escrito infinitesimalmente.
>
> **Paso 2 — Dos celdas adyacentes.** Aplicamos la relación a dos volúmenes contiguos $d\tau_1$ y $d\tau_2$ que comparten una cara. Sumando ambas ecuaciones,
> $$\vec\nabla\cdot\vec A\,d\tau_1+\vec\nabla\cdot\vec A\,d\tau_2=\oint_{S_1}d\vec\sigma\cdot\vec A+\oint_{S_2}d\vec\sigma\cdot\vec A.$$
>
> **Paso 3 — Cancelación de la cara común.** La cara compartida pertenece a $S_1$ y a $S_2$, pero la normal exterior de cada celda la atraviesa en sentidos **opuestos**: $d\vec\sigma_1=-d\vec\sigma_2$ sobre ella. Por tanto su contribución se anula,
> $$\vec A\cdot d\vec\sigma_1+\vec A\cdot d\vec\sigma_2=0,$$
> y solo sobrevive la superficie **exterior** $S_{1+2}$ que envuelve a $d\tau_1+d\tau_2$:
> $$\vec\nabla\cdot\vec A\,d\tau_1+\vec\nabla\cdot\vec A\,d\tau_2=\oint_{S_{1+2}}d\vec\sigma\cdot\vec A.$$
>
> **Paso 4 — Acumular celdas.** Repetimos el proceso añadiendo volúmenes contiguos. Todas las caras **internas** se cancelan por parejas (cada una es compartida por dos celdas con normales opuestas); solo persiste la superficie externa $S$ que encierra el volumen total $V$. Sumando,
> $$\int_V d\tau\,\vec\nabla\cdot\vec A=\oint_S d\vec\sigma\cdot\vec A.\qquad\blacksquare$$

> [!corolario]
> Si $\vec\nabla\cdot\vec A=0$ en todo $V$ (campo **solenoidal**), entonces $\oint_S d\vec\sigma\cdot\vec A=0$: el flujo neto a través de cualquier superficie cerrada es nulo. Es la forma integral de la ley $\vec\nabla\cdot\vec B=0$ del magnetismo.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Enunciado | $\int_V d\tau\,\vec\nabla\cdot\vec A=\oint_S d\vec\sigma\cdot\vec A$ |
> | Conecta | volumen $V$ $\leftrightarrow$ superficie cerrada $S=\partial V$ |
> | Origen | definición integral de la divergencia |
> | Idea clave | las caras internas se cancelan; sobrevive la frontera externa |
> | Orientación | $d\vec\sigma=\hat n\,d\sigma$ hacia afuera |

> [!corolario]
> El teorema de Gauss iguala el flujo de $\vec A$ por la frontera con la integral de su divergencia en el interior. Es el primer teorema integral y la base del [[Teorema de Green]] (aplicándolo a $u\vec\nabla v$) y del [[Teorema de Helmholtz]].

> [!referencia]
> - Definición de origen: [[Operadores Diferenciales/Divergencia]].
> - Derivado de él: [[Teorema de Green]], [[Teorema de Helmholtz]].
> - Análogo para el rotor: [[Teorema de Stokes]].
