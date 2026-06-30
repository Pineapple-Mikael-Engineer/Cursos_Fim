---
title: Conexiones Balanceadas
order: 2
tags:
  - circuitos-electricos
  - teoria
  - trifasico
  - index
draft: false
aliases:
  - conexiones balanceadas
  - estrella y triángulo
  - conexión Y y Delta
---

# Conexiones Balanceadas (Y y Δ)

> [!definicion]
> Las tres fuentes (y las tres cargas) de un sistema trifásico se conectan de dos formas: en **estrella (Y)**, con un punto común —el **neutro**—, o en **triángulo (Δ)**, en serie cerrando un lazo. La distinción clave es entre magnitudes de **fase** (en cada rama) y de **línea** (entre conductores), ligadas por el factor $\sqrt3$.

> [!info]
> Segunda sección del [[7 Circuitos Trifasicos/index| capítulo 7]]. Aplica las [[Generacion de Tensiones Trifasicas| tensiones trifásicas]] a circuitos reales; es la base del cálculo de [[Potencia Trifasica/index| potencia]]. Fraile Mora, cap. 3, §3.3-3.4.

---

## Las dos conexiones y el factor √3

> [!teoria] Estrella y triángulo, lado a lado
> En **estrella** las tres ramas comparten el neutro; la **tensión de línea** (entre dos conductores) es $\sqrt3$ veces la **de fase** (de conductor a neutro), y la corriente de línea es la misma que la de fase:
>
> ![[conexion_estrella.svg|360]]
>
> En **triángulo** las ramas se conectan en serie formando un lazo; ahora es la **corriente de línea** la que vale $\sqrt3$ veces la **de fase**, y la tensión de línea coincide con la de fase:
>
> ![[conexion_triangulo.svg|360]]
>
> $$\textbf{Y:}\quad V_L=\sqrt3\,V_F,\ \ I_L=I_F;\qquad\qquad \boldsymbol{\Delta:}\quad I_L=\sqrt3\,I_F,\ \ V_L=V_F.$$
>
> El factor $\sqrt3$ y un desfase de $30^\circ$ entre fase y línea aparecen al **sumar vectorialmente** dos fasores a $120^\circ$. → [[Conexion Estrella]] y [[Conexion Triangulo]].

> [!teoria] Cuatro combinaciones y un atajo
> Fuente y carga pueden ir cada una en Y o en Δ, dando cuatro combinaciones (Y-Y, Δ-Δ, Y-Δ, Δ-Y). → [[Sistemas Y-Y, Delta-Delta, Y-Delta]]. Pero si el sistema está **equilibrado**, no hace falta resolver las tres fases: basta analizar **una sola** y multiplicar —el **equivalente monofásico por fase**—, llevando todo a Y. → [[Circuito Equivalente Monofasico]].

## Mapa de la sección

> [!info] Las notas de esta sección
> | Nota | Contenido |
> |:---|:---|
> | [[Conexion Estrella]] | Y; $V_L=\sqrt3\,V_F$; el neutro |
> | [[Conexion Triangulo]] | Δ; $I_L=\sqrt3\,I_F$; sin neutro |
> | [[Sistemas Y-Y, Delta-Delta, Y-Delta]] | las combinaciones fuente-carga |
> | [[Circuito Equivalente Monofasico]] | analizar una fase y multiplicar |

> [!corolario]
> Todo el cálculo de un sistema equilibrado se reduce a dos conexiones (Y, Δ), un factor ($\sqrt3$) y un atajo (una fase representa a las tres). Distinguir fase de línea es la única —y crucial— precaución.

> [!referencia]
> Fraile Mora, cap. 3, §3.3-3.4. Anterior: [[Fundamentos Trifasicos/index| Fundamentos]]. Siguiente: [[Potencia Trifasica/index| Potencia trifásica]].
