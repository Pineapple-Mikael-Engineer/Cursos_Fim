---
title: Pseudo-escalares
tags:
  - analisis-tensorial
  - teoria
  - tensores
  - pseudo-objetos
draft: false
aliases:
  - pseudoescalar
  - pseudo-escalares
  - producto triple
  - pseudoscalar
---

# Pseudo-escalares

> [!definicion]
> Un **escalar** es invariante ante cualquier cambio de sistema. Un **pseudo-escalar** es invariante ante rotaciones pero **cambia de signo** al cambiar la orientación del sistema:
> $$S'=|a|\,S,\qquad |a|=\det[a]=\pm1.$$
> El ejemplo arquetípico es el **producto triple** $(\vec A\times\vec B)\cdot\vec C$, igual al **volumen** del paralelepípedo de aristas $\vec A,\vec B,\vec C$: positivo en un sistema derecho, negativo en uno izquierdo.

> [!info]
> Sección **4.6.2** del libro; parte de [[index | Pseudo-objetos]]. Es el caso de rango 0 de la familia: hereda el factor $|a|$ de un [[Pseudo-vectores | pseudo-vector]] (el producto cruz) al contraerlo con un vector regular. Un escalar verdadero (temperatura, $\vec A\cdot\vec B$, una traza) cumple $S'=S$.

---

## Ejemplo

> [!ejemplo]
> **El volumen es un pseudo-escalar.** El producto triple da el volumen del paralelepípedo formado por $\vec A$, $\vec B$ y $\vec C$:
> $$\text{Volumen}=(\vec A\times\vec B)\cdot\vec C.$$
>
> > [!demostracion]
> > **Paso 1 — El signo en un sistema derecho.** En un sistema de mano derecha, $\vec A\times\vec B$ apunta "hacia arriba" (regla de la mano derecha). Si $\vec C$ tiene componente en ese sentido, el producto punto es positivo:
> > $$(\vec A\times\vec B)\cdot\vec C>0\qquad\text{(sistema derecho)}.$$
> >
> > **Paso 2 — El signo en un sistema izquierdo.** Al pasar a un sistema de mano izquierda (una reflexión, $|a|=-1$), el pseudo-vector $\vec A\times\vec B$ cambia de dirección y ahora apunta "hacia abajo" respecto a los mismos vectores físicos. Su producto punto con $\vec C$ se vuelve negativo:
> > $$(\vec A\times\vec B)\cdot\vec C<0\qquad\text{(sistema izquierdo)}.$$
> >
> > **Paso 3 — El factor $|a|$.** El paralelepípedo físico es el mismo, pero el número que lo describe cambió de signo con la orientación. Eso es exactamente la ley
> > $$S'=|a|\,S,$$
> > con $|a|=+1$ (derecho, sin cambio) o $|a|=-1$ (izquierdo, signo opuesto). **Conclusión:** el volumen $(\vec A\times\vec B)\cdot\vec C$ es un pseudo-escalar.

---

## En qué consiste

> [!teoria]
> El origen del carácter pseudo-escalar es de contabilidad de factores: el producto triple contiene **un** producto cruz, que aporta un [[Pseudo-vectores | pseudo-vector]] con factor $|a|$. Al contraerlo con un vector regular $\vec C$ vía el producto punto (que no añade ni quita $|a|$), el factor sobrevive en el escalar resultante:
> $$(\vec A\times\vec B)\cdot\vec C\ \xrightarrow{\ |a|\ }\ |a|\,(\vec A\times\vec B)\cdot\vec C.$$
> En componentes, $(\vec A\times\vec B)\cdot\vec C=\varepsilon_{ijk}A_iB_jC_k$, donde $\varepsilon_{ijk}$ es el [[Pseudo-tensores | pseudo-tensor]] que carga el $|a|$. La regla general: un objeto con un número **impar** de productos cruz (o de factores $\varepsilon$) es pseudo; con un número **par**, regular.

> [!info] Escalar vs pseudo-escalar
> | | Escalar (verdadero) | Pseudo-escalar |
> |---|---|---|
> | Ley | $S'=S$ | $S'=\|a\|\,S$ |
> | Bajo rotación ($\|a\|=+1$) | invariante | invariante |
> | Bajo reflexión ($\|a\|=-1$) | invariante | cambia de signo |
> | Ejemplos | temperatura, $\vec A\cdot\vec B$, masa | volumen $(\vec A\times\vec B)\cdot\vec C$ |

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Escalar | $S'=S$ (invariante) |
> | Pseudo-escalar | $S'=\|a\|\,S$ |
> | Ejemplo estrella | volumen $(\vec A\times\vec B)\cdot\vec C$ |
> | Sistema derecho | $(\vec A\times\vec B)\cdot\vec C>0$ |
> | Sistema izquierdo | $(\vec A\times\vec B)\cdot\vec C<0$ |
> | Regla | nº impar de productos cruz $\Rightarrow$ pseudo |

> [!corolario]
> Un pseudo-escalar es un número que cambia de signo con la orientación del sistema. El producto triple $(\vec A\times\vec B)\cdot\vec C$ —el volumen orientado— lo ejemplifica: positivo en sistemas derechos, negativo en izquierdos. Hereda su factor $|a|$ del [[Pseudo-vectores | pseudo-vector]] producto cruz, controlado por el [[Pseudo-tensores | pseudo-tensor]] $\varepsilon_{ijk}$.

> [!referencia]
> - El pseudo-vector que origina el factor: [[Pseudo-vectores]].
> - El símbolo $\varepsilon_{ijk}$: [[Simbolo Levi-Civita]].
> - Marco general: [[index | Pseudo-objetos]].
