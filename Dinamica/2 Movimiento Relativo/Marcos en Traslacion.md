---
title: Marcos en Traslación
tags:
  - dinamica
  - teoria
  - movimiento-relativo
draft: false
aliases:
  - marcos en traslación
  - transformaciones de Galileo
  - relatividad de Galileo
  - sistemas inerciales
---

# Marcos en Traslación: Transformaciones de Galileo

> [!definicion]
> Cuando el marco móvil $M$ solo **traslada** respecto al fijo $F$ (no rota), sus versores son
> **constantes**, y la posición, velocidad y aceleración se transforman por las **transformaciones de
> Galileo**:
> $$\vec r=\vec R_M+\vec r\,',\qquad \vec v=\vec V_M+\vec v\,',\qquad \vec a=\vec A_M+\vec a\,',$$
> con $\vec R_M,\vec V_M,\vec A_M$ la posición, velocidad y aceleración del origen de $M$. Si además
> $\vec V_M$ es **constante** ($\vec A_M=\vec 0$), entonces $\vec a=\vec a\,'$.

> [!info]
> Primer caso del [[2 Movimiento Relativo/index | movimiento relativo]]: el sencillo, sin rotación. El
> caso con rotación añade los términos de arrastre y Coriolis → [[Operador Derivada en Base Movil]].
> Referencia: PDF *Física I* (GETI), §2.1; Taylor §1.4.

---

## Ejemplo

> [!ejemplo]
> **La pelota en el tren.**
>
> Un pasajero lanza una pelota **verticalmente** dentro de un tren que avanza a velocidad constante
> $\vec V_M=V\hat\imath$. ¿Qué trayectoria ve un observador en el andén?
>
> ![[galileo_tren.svg|520]]
>
> *En el tren ($M$) la pelota sube y baja vertical; desde el andén ($F$) describe una parábola. La aceleración —la gravedad— es la misma en ambos.*
>
> **En el tren ($M$).** Solo actúa la gravedad: $\vec a\,'=-g\hat\jmath$, y como lanza vertical,
> $\vec v\,'_0=v_0\hat\jmath$: sube y baja en **línea recta** vertical.
>
> **En el andén ($F$).** Como $\vec V_M$ es constante, $\vec A_M=\vec0$ y $\vec a=\vec a\,'=-g\hat\jmath$
> (la **misma** gravedad). Pero la velocidad inicial vista desde $F$ es $\vec v_0=\vec V_M+\vec v\,'_0=V\hat\imath+v_0\hat\jmath$:
> hay componente horizontal constante.
>
> > [!solucion]
> > Desde el andén, la pelota describe una **parábola** ($x=Vt$, $y=v_0t-\tfrac12 gt^2$); desde el tren,
> > una recta vertical. **La misma aceleración**, distinta trayectoria: depende del marco, pero $g$ no.

---

## En qué consiste

> [!teorema] Transformaciones de Galileo
> Para $M$ en pura traslación,
> $$\vec v=\vec V_M+\vec v\,',\qquad \vec a=\vec A_M+\vec a\,'.$$

> [!demostracion]
> **Paso 1 — Posición.** $\vec r=\vec R_M+\vec r\,'$.
> **Paso 2 — Velocidad.** Derivando respecto al tiempo en $F$, y como los **versores de $M$ son
> constantes** (no hay rotación), $\dfrac{d\vec r\,'}{dt}\Big|_F=\dfrac{d\vec r\,'}{dt}\Big|_M=\vec v\,'$:
> $$\vec v=\dot{\vec R}_M+\vec v\,'=\vec V_M+\vec v\,'.$$
> **Paso 3 — Aceleración.** Derivando otra vez, $\vec a=\dot{\vec V}_M+\vec a\,'=\vec A_M+\vec a\,'$.
> Si $\vec V_M=$ cte, $\vec A_M=\vec0$ y $\vec a=\vec a\,'$. $\blacksquare$

> [!proposicion] Relatividad de Galileo e invariancia de Newton
> Si $F$ es **inercial** y $M$ se mueve a **velocidad constante** respecto a $F$, entonces $M$ también
> es inercial: como $\vec a=\vec a\,'$ y la masa no cambia, $\sum\vec F=m\vec a=m\vec a\,'$ tiene la
> **misma forma** en ambos. Las leyes de la mecánica no distinguen un marco inercial de otro en
> movimiento uniforme: es el **principio de relatividad de Galileo**.

> [!warning]
> Esto vale **solo sin rotación**. Si $M$ rota, sus versores ya no son constantes y aparecen los
> términos de arrastre y de Coriolis → [[Operador Derivada en Base Movil]]. Y si $\vec A_M\neq\vec0$ (el
> origen de $M$ acelera), $M$ **no** es inercial: $\sum\vec F=m\vec a\,'$ falla salvo añadiendo la
> pseudofuerza $-m\vec A_M$.

## Resumen

> [!resumen]
> | Magnitud | Transformación (traslación) |
> |:---|:---|
> | Posición | $\vec r=\vec R_M+\vec r\,'$ |
> | Velocidad | $\vec v=\vec V_M+\vec v\,'$ |
> | Aceleración | $\vec a=\vec A_M+\vec a\,'$ |
> | $\vec V_M=$ cte | $\vec a=\vec a\,'$ (Galileo) |

> [!corolario]
> En traslación, los marcos se relacionan sumando el movimiento del origen. Los inerciales —los que se
> mueven uniformemente entre sí— comparten la misma física: ninguna experiencia mecánica detecta la
> velocidad absoluta.

> [!referencia]
> PDF *Física I* (GETI), §2.1; Taylor §1.4. Caso con rotación: [[Operador Derivada en Base Movil]].
