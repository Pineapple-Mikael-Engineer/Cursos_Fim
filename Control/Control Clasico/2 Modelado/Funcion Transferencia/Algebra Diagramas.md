---
title: Álgebra de Diagramas de Bloques
tags:
  - control-clasico
  - teoria
  - modelado
draft: false
aliases:
  - reducción de diagramas
  - bloques
  - diagramas de bloques
---

# Álgebra de Diagramas de Bloques

# Definición

> [!definicion] Diagrama de bloques
> Representación gráfica de un sistema de control donde:
> - **Bloques**: representan funciones transferencia $G(s)$
> - **Flechas**: representan señales (entradas, salidas, realimentaciones)
> - **Sumadores**: puntos donde se suman o restan señales (círculos con cruz)

# Conexiones básicas

> [!definicion] Serie (cascada)
> $$G_{eq}(s) = G_1(s) \cdot G_2(s)$$
> 
>![[Algebra_Bloques_02.svg|400]]

> [!definicion] Paralelo
> $$G_{eq}(s) = G_1(s) + G_2(s)$$
> 
> ![[Algebra_Bloques_03.svg|400]]

> [!definicion] Realimentación
> Lazo cerrado con realimentación $H(s)$:
> $$G_{eq}(s) = \frac{G(s)}{1 - G(s)H(s)}$$
> 
> Realimentación unitaria ($H(s)=1$):
> $$G_{eq}(s) = \frac{G(s)}{1 - G(s)}$$
> 
> ![[Algebra_Bloques_04.svg|400]]

# Demostración de realimentación

> [!teorema] Función transferencia de lazo cerrado con realimentación negativa
> $$T(s) = \frac{G(s)}{1 - G(s)H(s)}$$

> [!demostracion]
> **Paso 1:** Definir señales. Sea $E(s)$ la salida del sumador:
> $$E(s) = U(s) + H(s)Y(s)$$
> 
> **Paso 2:** La salida $Y(s)$ es:
> $$Y(s) = G(s)E(s)$$
> 
> **Paso 3:** Sustituir $E(s)$:
> $$Y(s) = G(s)[U(s) + H(s)Y(s)]$$
> 
> **Paso 4:** Despejar $Y(s)$:
> $$Y(s) = G(s)U(s) + G(s)H(s)Y(s)$$
> $$Y(s) - G(s)H(s)Y(s) = G(s)U(s)$$
> $$Y(s)[1 - G(s)H(s)] = G(s)U(s)$$
> 
> **Paso 5:** Despejar la función transferencia $T(s) = Y(s)/U(s)$:
> $$T(s) = \frac{G(s)}{1 - G(s)H(s)}$$

# Reglas de reducción

> [!info] Movimiento de sumadores
> | Operación | Equivalencia |
> |-----------|---------------|
> | Mover sumador antes de bloque | !$G$ → sumador se multiplica por $1/G$ |
> | Mover sumador después de bloque | sumador → $G$ se multiplica |
> 
> Ver reglas completas en [[Reduccion Sistematica]].

> [!info] Movimiento de puntos de bifurcación
> | Operación | Equivalencia |
> |-----------|---------------|
> | Mover bifurcación antes de bloque | se añade bloque $1/G$ |
> | Mover bifurcación después de bloque | se añade bloque $G$ |

# Ejemplos de reducción

> [!ejemplo] Realimentación con bloque en retroalimentación
> ![[Algebra_Bloques_06.svg|400]]
> 
> **Paso 1:** Reducir la realimentación interna ($G2$ con $H1$):
> $$T_1 = \frac{G_2}{1 + G_2 H_1}$$
> 
> **Paso 2:** El sistema queda:
> ![[Algebra_Bloques_08.svg|400]]
> 
> **Paso 3:** Realimentación externa:
> $$T_{eq} = \frac{G_1 T_1}{1 + G_1 T_1 H_2}$$
> 
> **Paso 4:** Sustituir $T_1$:
> $$T_{eq} = \frac{G_1 \cdot \frac{G_2}{1+G_2 H_1}}{1 + G_1 H_2 \cdot \frac{G_2}{1+G_2 H_1}} = \frac{G_1 G_2}{1 + G_2 H_1 + G_1 G_2 H_2}$$


# Simplificación de lazo cerrado

> [!teorema] Forma canónica
> Para cualquier diagrama sin lazos cruzados, la función transferencia total es:
> $$T(s) = \frac{\text{suma de productos de caminos directos}}{1 - \text{suma de productos de lazos}}$$

> [!demostracion]
> Se deduce de la [[Formula Mason | fórmula de ganancia de Mason]].
> 
> **Ejemplo:** Lazo sencillo sin camino directo alternativo:
> $$T(s) = \frac{G_1 G_2 G_3}{1 + G_1 G_2 G_3 H}$$

# Regla práctica: retroalimentación positiva

> [!info] Realimentación positiva
> Si el sumador es **positivo** ($E = U + HY$):
> $$T(s) = \frac{G(s)}{1 - G(s)H(s)}$$

> [!demostracion]
> Misma deducción pero con signo $+$:
> $$E = U + H Y$$
> $$Y = G E = G(U + H Y) = GU + GH Y$$
> $$Y - GH Y = GU$$
> $$Y(1 - GH) = GU$$
> $$T = \frac{G}{1 - GH}$$


# Limitaciones

> [!warning]
> 1. El álgebra de bloques supone que todos los bloques son **LTI**
> 2. No aplicar directamente si hay **lazos cruzados** (usar [[Formula Mason]])
> 3. Los sumadores deben ser **lineales** (no saturación, no no linealidades)