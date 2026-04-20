---
title: "Reducción de Diagramas"
tags:
  - control-clasico
  - diagramas-de-bloques
  - reduccion
draft: false
aliases:
  - Block Diagram Reduction
  - Reducción Sistemática
  - Fórmula de Mason
---

# Reducción de Diagramas

> [!definicion] Objetivo
> La **reducción de diagramas de bloques** es el proceso de transformar un diagrama complejo en una única [[Función de Transferencia/index|función de transferencia]] equivalente $G(s) = Y(s)/U(s)$, combinando las reglas de [[Álgebra de Bloques]] y [[Movimiento de Nodos]].

---

## Estrategia General

> [!teoria] Procedimiento Sistemático
> 1. **Identificar** las conexiones fundamentales (serie, paralelo, realimentación)
> 2. **Mover nodos** (bifurcaciones o sumadores) para exponer estas conexiones
> 3. **Reducir** cada conexión a un bloque equivalente
> 4. **Repetir** hasta obtener un solo bloque

```
Diagrama original → Mover nodos → Identificar conexiones → Reducir → Diagrama reducido → Repetir
```

---

## Reducción de Conexiones Básicas

> [!teoria] Bloque Único Equivalente

| Conexión | Configuración | Función equivalente |
|----------|---------------|---------------------|
| **Serie** | $G_1$ seguido de $G_2$ | $G_{\text{eq}} = G_1 \cdot G_2$ |
| **Paralelo** | $G_1$ y $G_2$ con misma entrada | $G_{\text{eq}} = G_1 + G_2$ |
| **Realimentación negativa** | $G$ con $H$ en retroalimentación | $G_{\text{eq}} = \dfrac{G}{1 + G H}$ |
| **Realimentación positiva** | $G$ con $H$ en retroalimentación | $G_{\text{eq}} = \dfrac{G}{1 - G H}$ |

---

## Casos Comunes de Reducción

### Caso 1: Realimentación con bloque en la rama de retroalimentación

**Configuración:**
- Trayectoria directa: $G$
- Rama de retroalimentación: $H$
- Sumador: resta en la entrada

**Resultado:** $G_{\text{lc}} = \dfrac{G}{1 + G H}$

### Caso 2: Realimentación unitaria ($H = 1$)

**Configuración:**
- Trayectoria directa: $G$
- Rama de retroalimentación: directa (sin bloque)

**Resultado:** $G_{\text{lc}} = \dfrac{G}{1 + G}$

### Caso 3: Sistema con realimentación interna y externa

**Procedimiento:**
1. Reducir primero el lazo interno (más cercano a la salida)
2. El resultado se convierte en un bloque en serie con otros
3. Reducir el lazo externo

### Caso 4: Sistema con múltiples entradas (referencia, perturbación, ruido)

**Procedimiento:**
- Aplicar superposición (sistema lineal)
- Reducir cada entrada por separado considerando las demás nulas
- Sumar los resultados parciales

---

## Fórmula de Mason (Método Alternativo)

> [!definicion] Ganancia de Mason
> Para sistemas complejos con múltiples lazos, la **fórmula de Mason** permite obtener la función de transferencia sin reducción paso a paso:
> $$
> G(s) = \frac{\sum_{k} P_k \Delta_k}{\Delta}
> $$
> 
> donde:
> - $P_k$ = ganancia de la $k$-ésima trayectoria directa
> - $\Delta = 1 - \sum L_i + \sum L_i L_j - \sum L_i L_j L_k + \dots$
> - $L_i$ = ganancia de cada lazo individual
> - $L_i L_j$ = producto de lazos que no se tocan
> - $\Delta_k$ = valor de $\Delta$ eliminando lazos que tocan la $k$-ésima trayectoria

> [!ejemplo] Aplicación de Mason
> Para un sistema con:
> - Trayectorias directas: $P_1 = G_1 G_2$, $P_2 = G_3$
> - Lazos: $L_1 = -G_1 H_1$, $L_2 = -G_2 H_2$, $L_3 = -G_1 G_2 H_3$
> - Lazos que no se tocan: $L_1$ y $L_2$ (si no comparten nodos)
> 
> Se calcula $\Delta$ y luego $G(s)$.

> [!info]
> La fórmula de Mason es útil para sistemas muy complejos, pero la reducción paso a paso es más didáctica y menos propensa a errores en sistemas de tamaño moderado.

---

## Errores Comunes en la Reducción

> [!warning] Errores a Evitar
> 1. **Mover un sumador sin agregar el bloque correcto** (olvidar $G$ o $G^{-1}$)
> 2. **Cambiar el orden de sumadores** sin verificar que las señales son independientes
> 3. **Cancelar polos inestables** al simplificar (válido en FT, peligroso en lazo cerrado)
> 4. **Ignorar el efecto de carga** en conexiones serie (en sistemas físicos reales)
> 5. **Aplicar realimentación cuando el lazo no está aislado** (hay señales que entran o salen del lazo)

---

## Ejemplo Paso a Paso

> [!ejemplo] Reducción completa de un sistema
> 
> **Paso 1:** Identificar lazos internos.
> 
> **Paso 2:** Mover nodos si es necesario (bifurcaciones o sumadores).
> 
> **Paso 3:** Reducir el lazo más interno usando $G_{\text{lc}} = G/(1+GH)$.
> 
> **Paso 4:** El resultado se combina en serie con los bloques adyacentes.
> 
> **Paso 5:** Reducir el siguiente lazo (ahora más externo).
> 
> **Paso 6:** Si quedan múltiples trayectorias (paralelo), sumar.
> 
> **Paso 7:** Verificar que la función de transferencia final tiene sentido (orden, polos, ceros).

---

## Verificación de Resultados

> [!teoria] Comprobaciones Rápidas
> - **Ganancia estática:** Evaluar $G(0)$ debe coincidir con el sentido físico
> - **Orden del sistema:** El grado del denominador debe ser $\le$ suma de órdenes individuales
> - **Polos en lazo cerrado:** Deben moverse hacia la izquierda respecto a lazo abierto (realimentación negativa estabiliza)

---

## Relación con Otras Técnicas

> [!info]
> - La [[Álgebra de Bloques]] provee las reglas para combinar bloques
> - El [[Movimiento de Nodos]] permite reordenar el diagrama
> - La **Reducción de Diagramas** integra ambas para obtener la función de transferencia
> - Para sistemas muy complejos, conviene usar [[Fórmula de Mason]] o pasar a representación en [[Espacio de Estado]]
