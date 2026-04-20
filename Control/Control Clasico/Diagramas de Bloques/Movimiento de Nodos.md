---
title: "Movimiento de Nodos"
tags:
  - control-clasico
  - diagramas-de-bloques
  - transformaciones
draft: false
aliases:
  - Nodos
  - Puntos de Bifurcación
  - Sumadores
  - Reglas de Movimiento
---

# Movimiento de Nodos

> [!definicion] Nodos en Diagramas de Bloques
> En un [[Diagramas de Bloques/index|diagrama de bloques]], existen dos tipos de nodos:
> - **Sumador:** Combina varias señales mediante suma o resta.
> - **Punto de bifurcación:** Distribuye una misma señal a múltiples destinos.

La necesidad de mover nodos surge cuando se quiere reducir un diagrama de bloques a una forma canónica (serie, paralelo, realimentación) pero la configuración actual no lo permite directamente.

---

## Reglas Fundamentales

> [!teoria] Principio de Invarianza
> Al mover un nodo a través de un bloque $G(s)$, la **función de transferencia total** del sistema debe permanecer inalterada. Para ello, se introduce el bloque $G(s)$ o su inverso $G^{-1}(s)$ según corresponda.

---

## Movimiento de Puntos de Bifurcación

### 1. Mover bifurcación desde la SALIDA hacia la ENTRADA de un bloque

**Regla:** Agregar un bloque $G$ en cada rama que se bifurcaba originalmente después del bloque.

**Efecto:** El punto se mueve antes de $G$, y las señales que antes salían directamente ahora pasan por $G$.

### 2. Mover bifurcación desde la ENTRADA hacia la SALIDA de un bloque

**Regla:** Agregar un bloque $G^{-1}$ en cada rama que se bifurcaba originalmente antes del bloque.

**Efecto:** El punto se mueve después de $G$, y las señales que antes eran $u$ ahora se obtienen como $u = G^{-1} \cdot (G u)$.

> [!warning]
> El bloque inverso $G^{-1}(s)$ debe existir (sistema sin ceros en el SPD ni retardos). En caso contrario, esta transformación no es posible.

---

## Movimiento de Sumadores

### 3. Mover un sumador desde la ENTRADA hacia la SALIDA de un bloque

**Regla:** Agregar un bloque $G$ en cada rama que entra al sumador.

**Efecto:** El sumador se mueve después de $G$. Las señales que antes se sumaban y luego pasaban por $G$, ahora pasan individualmente por $G$ y luego se suman.

> [!demostracion]
> Original: $y = G(u_1 + u_2) = G u_1 + G u_2$
> Equivalente: $y = G u_1 + G u_2$ (misma expresión). $\square$

### 4. Mover un sumador desde la SALIDA hacia la ENTRADA de un bloque

**Regla:** Agregar un bloque $G^{-1}$ en la rama externa (la que no viene del bloque).

**Efecto:** El sumador se mueve antes de $G$. La señal externa se multiplica por $G^{-1}$ antes de sumarse.

> [!demostracion]
> Original: $y = G u + u_2$
> Equivalente: $y = G(u + G^{-1} u_2) = G u + u_2$ (misma expresión). $\square$

---

## Intercambio de Sumadores

> [!proposicion] Sumadores en cascada
> Dos sumadores pueden intercambiarse si no hay dependencia entre sus señales. El orden no afecta el resultado siempre que se mantengan los signos correctos.

---

## Resumen de Transformaciones

> [!teoria] Tabla de Equivalencias
| Operación | Movimiento | Bloque a agregar | Condición |
|-----------|------------|------------------|-----------|
| Bifurcación | Salida → Entrada | $G$ | Siempre |
| Bifurcación | Entrada → Salida | $G^{-1}$ | $G^{-1}$ debe existir |
| Sumador | Entrada → Salida | $G$ en cada rama | Siempre |
| Sumador | Salida → Entrada | $G^{-1}$ en rama externa | $G^{-1}$ debe existir |

> [!warning] Condiciones de Validez
> - El bloque inverso $G^{-1}(s)$ debe ser **causal y estable** para ser realizable físicamente.
> - Si $G(s)$ tiene [[Polos y Ceros|ceros en el semiplano derecho]], $G^{-1}(s)$ tendrá polos inestables → no usar.
> - En la práctica, se evita mover nodos a través de bloques con $G^{-1}$; en su lugar, se reordenan los lazos.

---

## Ejemplos de Aplicación

> [!ejemplo] Mover bifurcación para crear un lazo estándar
> 
> **Situación:** Un punto de bifurcación está entre dos bloques $G_1$ y $G_2$, y una realimentación $H$ toma la señal después de $G_2$.
> 
> **Problema:** No se puede aplicar directamente la fórmula de realimentación porque el punto de bifurcación está en medio.
> 
> **Solución:** Mover el punto de bifurcación desde la salida de $G_2$ hacia su entrada. Se agrega $G_2$ en la rama de realimentación.
> 
> **Resultado:** Ahora la realimentación toma la señal antes de $G_2$, y se tiene un lazo estándar que incluye $G_1$, $G_2$ y $H$ con un $G_2$ adicional.

> [!ejemplo] Mover sumador para combinar dos realimentaciones
> 
> **Situación:** Un sistema tiene dos lazos de realimentación $H_1$ y $H_2$ que entran a sumadores diferentes (uno antes de $G_2$ y otro después).
> 
> **Problema:** No se pueden reducir los lazos simultáneamente.
> 
> **Solución:** Mover el sumador que está después de $G_2$ hacia su entrada. Se agrega $G_2^{-1}$ en la rama de $H_1$.
> 
> **Resultado:** Ambos lazos comparten el mismo sumador y pueden reducirse secuencialmente.

---

## Relación con la Reducción de Diagramas

> [!info]
> Las reglas de Movimiento de Nodos son las herramientas fundamentales para aplicar la [[Reducción de Diagramas]]. Una vez que los nodos están en posiciones que permiten identificar conexiones serie, paralelo y realimentación, se procede a la reducción sistemática.
