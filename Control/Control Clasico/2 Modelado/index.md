---
title: Modelado
order: 2
tags:
  - control-clasico
  - modelado
  - index
draft: false
aliases:
  - modelado
  - modelado de sistemas
  - system modeling
---

# Modelado

> [!definicion]
> **Modelar** es obtener las ecuaciones que describen la planta y llevarlas a una forma manejable para el control. El camino es: escribir las **ecuaciones diferenciales** del sistema físico, **linealizar** si hace falta, aplicar la **transformada de Laplace** para pasar del tiempo a $s$, y expresar el resultado como **función de transferencia** $G(s)$ o como **espacio de estados**. Ese modelo es la materia prima de todo el análisis y diseño posteriores.

> [!info]
> Segundo bloque del [[Control Clasico/index| Control Clásico]]. Convierte la física de la planta en un modelo matemático; sin él no hay análisis ni diseño. Ogata, cap. 2–3; Nise, cap. 2–3.

## Del sistema físico al modelo en $s$

> [!teoria] Ecuaciones, Laplace y las dos representaciones
> - **Dominios físicos**: las leyes de cada dominio (eléctrico, mecánico, fluidos, térmico…) dan la EDO de la planta; las analogías permiten un tratamiento común. → [[Dominios Fisicos/index| Dominios físicos]].
> - **Linealización**: los sistemas reales son no lineales; alrededor de un punto de operación se aproximan por su **jacobiano** para poder usar Laplace. → [[Linealizacion/index| Linealización]].
> - **Transformada de Laplace**: convierte derivadas en potencias de $s$, volviendo algebraicas las ecuaciones diferenciales. → [[Transformada Laplace/index| Transformada de Laplace]].
> - **Función de transferencia y espacio de estados**: las dos representaciones del modelo lineal —$G(s)=Y(s)/U(s)$ (entrada–salida) y $\dot{\mathbf{x}}=A\mathbf{x}+B\mathbf{u}$ (interna)—. → [[Funcion Transferencia/index| Función de transferencia]], [[Espacio Estados/index| Espacio de estados]].

## Mapa de la sección

> [!info] Las subsecciones
> | Subsección | Contenido |
> |:---|:---|
> | [[Dominios Fisicos/index\| Dominios físicos]] | ecuaciones por dominio; analogías |
> | [[Linealizacion/index\| Linealización]] | punto de operación; jacobiano |
> | [[Transformada Laplace/index\| Transformada de Laplace]] | del tiempo a $s$ |
> | [[Funcion Transferencia/index\| Función de transferencia]] | $G(s)$; polos y ceros |
> | [[Espacio Estados/index\| Espacio de estados]] | representación interna $A,B,C,D$ |

> [!corolario]
> Modelar es traducir la planta a $s$: ecuaciones del dominio → linealizar → Laplace → $G(s)$ o espacio de estados. Con ese modelo lineal, el resto del curso trabaja sobre polos, ceros y diagramas en vez de sobre ecuaciones diferenciales.

> [!referencia]
> Ogata, *Ingeniería de Control Moderna*, cap. 2–3. Nise, *Control Systems Engineering*, cap. 2–3.
