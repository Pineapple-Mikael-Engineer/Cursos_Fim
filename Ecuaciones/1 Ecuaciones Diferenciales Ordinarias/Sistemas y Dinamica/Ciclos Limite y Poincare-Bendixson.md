---
title: Ciclos Límite y Poincaré-Bendixson
order: 9
tags:
  - ecuaciones
  - edo
  - teoria
  - sistemas
  - ciclos-limite
draft: false
aliases:
  - ciclo límite
  - teorema de Poincaré-Bendixson
  - oscilador de Van der Pol
  - limit cycle
---

# Ciclos Límite y Poincaré-Bendixson

> [!definicion]
> Un **ciclo límite** es una órbita **cerrada aislada** del plano de fase: una oscilación periódica hacia la que (o desde la que) **espiralan** las trayectorias vecinas. A diferencia de los [[Puntos de Equilibrio y Plano de Fase| centros]] —rodeados de un continuo de órbitas cerradas no aisladas—, un ciclo límite es una oscilación **autosostenida** con amplitud propia, fijada por la dinámica y no por las condiciones iniciales.

> [!info]
> Cierre cualitativo del bloque [[Sistemas y Dinamica/index| sistemas y dinámica]] (nota de panorama). Responde qué comportamientos son **posibles** en el plano de fase una vez clasificados los equilibrios ([[Estabilidad de Lyapunov| estabilidad]], [[Linealizacion y Hartman-Grobman| linealización]]) y por qué el **caos** está prohibido en 2D.

---

## Ejemplo

> [!ejemplo] El oscilador de Van der Pol
> $$\ddot x-\mu\,(1-x^2)\,\dot x+x=0\qquad(\mu>0).$$
> El término de amortiguamiento $-\mu(1-x^2)\dot x$ cambia de signo: para amplitudes **pequeñas** ($|x|<1$) es **negativo** —inyecta energía y **amplifica** la oscilación—; para amplitudes **grandes** ($|x|>1$) es **positivo** —**disipa** y la frena—. El equilibrio en el origen es inestable (las trayectorias se alejan) pero las lejanas se acercan: ambas tendencias se equilibran en una **única órbita cerrada estable**, el ciclo límite, de amplitud bien definida ($\approx 2$ para $\mu$ pequeño). Cualquier condición inicial (salvo el origen exacto) **converge** a esa misma oscilación: es un reloj robusto.

---

## En qué consiste

> [!teorema] Poincaré-Bendixson
> Sea $\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x})$ un sistema **autónomo en el plano** ($\mathbf{x}\in\mathbb{R}^2$, $\mathbf{f}$ suave). Si una trayectoria permanece **acotada** en una región cerrada que **no contiene equilibrios** (o no tiende a ninguno), entonces su conjunto límite es una **órbita cerrada** (un ciclo límite). En el plano, una trayectoria acotada solo puede acabar en un equilibrio o en un ciclo.

> [!corolario] No hay caos en 2D autónomo
> El teorema **excluye** el comportamiento caótico en sistemas autónomos del plano: las únicas "atracciones" posibles son puntos de equilibrio y órbitas cerradas. El caos requiere al menos **tres** dimensiones de espacio de fase (de ahí Lorenz, $n=3$) o forzamiento dependiente del tiempo.

> [!info] Cómo se usa en la práctica (región de atrapamiento)
> Para **probar** que existe un ciclo límite se construye una **región anular** (un "trampa") en la que el campo $\mathbf{f}$ apunta hacia adentro en ambos bordes y que no encierra equilibrios: por Poincaré-Bendixson, toda trayectoria que entra queda atrapada y debe enrollarse en un ciclo cerrado dentro del anillo.

> [!warning]
> Es un resultado de **panorama**: la demostración completa se apoya en el teorema de la curva de Jordan y queda fuera del curso. Aquí interesa el enunciado y su consecuencia (2D ⇒ sin caos).

## Resumen

> [!resumen]
> | Concepto | Idea |
> |---|---|
> | Ciclo límite | órbita cerrada **aislada**; oscilación autosostenida |
> | vs. centro | el centro tiene órbitas cerradas **no** aisladas (no robustas) |
> | Poincaré-Bendixson | en 2D, trayectoria acotada → equilibrio o ciclo |
> | Consecuencia | **no hay caos** en 2D autónomo |
> | Ejemplo | Van der Pol (ciclo límite estable único) |

> [!corolario]
> En el plano, la dinámica a largo plazo es **simple**: o se va a un equilibrio o se enrolla en un ciclo límite. Los ciclos límite explican las **oscilaciones robustas** de la naturaleza (latido cardíaco, osciladores electrónicos, ritmos biológicos), cuya amplitud no depende del arranque.

> [!referencia]
> - Clasificación de equilibrios: [[Puntos de Equilibrio y Plano de Fase]].
> - Estabilidad local: [[Estabilidad de Lyapunov]], [[Linealizacion y Hartman-Grobman]].
> - Marco del bloque: [[Sistemas y Dinamica/index]].
