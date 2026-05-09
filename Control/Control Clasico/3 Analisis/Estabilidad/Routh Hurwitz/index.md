---
title: Criterio de Routh-Hurwitz
tags:
  - control-clasico
  - teoria
  - analisis
  - estabilidad
draft: false
aliases:
  - routh
  - routh-hurwitz
  - criterio de routh
---

# Criterio de Routh-Hurwitz

# Definición

> [!definicion] Criterio de Routh-Hurwitz
> Método algebraico para determinar el número de **polos** de un sistema (raíces del polinomio característico) con parte real positiva, **sin calcular explícitamente los polos**.
> 
> Aplica a polinomios característicos con coeficientes reales de la forma:
> $$P(s) = a_n s^n + a_{n-1} s^{n-1} + \dots + a_1 s + a_0$$

# Condición necesaria y suficiente

> [!teorema] Estabilidad por Routh-Hurwitz
> El sistema es **estable** (todos los polos con $\Re(s) < 0$) si y solo si:
> 1. **Todos los coeficientes** $a_i$ tienen el mismo signo (todos positivos o todos negativos)
> 2. **Todos los elementos de la primera columna** de la tabla de Routh tienen el mismo signo
> 
> El número de cambios de signo en la primera columna es igual al número de polos con parte real positiva.

# Construcción de la tabla de Routh

> [!info] Procedimiento
> Ver [[Construccion Tabla]] para:
> - Algoritmo paso a paso
> - Cálculo de coeficientes
> - Ejemplos numéricos
> - Interpretación de resultados

# Casos especiales

> [!info] Problemas comunes y sus soluciones
> 
> | Caso | Descripción | Ver |
> |------|-------------|-----|
> | **Caso 1** | Primer elemento de una fila es cero | [[Casos Especiales#Caso 1: Primer elemento cero]] |
> | **Caso 2** | Fila completa de ceros | [[Casos Especiales#Caso 2: Fila de ceros]] |
> 
> El **Caso 2** (fila de ceros) indica polos simétricos respecto al origen:
> - Pares reales opuestos ($s = \pm a$)
> - Pares imaginarios conjugados ($s = \pm j\omega$)
> - Cuartetos complejos ($s = \pm a \pm jb$)

# Ajuste de parámetros

> [!info] Rango de ganancia para estabilidad
> Cuando un sistema tiene un parámetro variable (ej. ganancia $K$), se puede determinar el **rango de estabilidad** imponiendo condiciones de signo en la primera columna.
> 
> Ver [[Ajuste Parametros]] para:
> - Sistemas con ganancia variable
> - Sistemas con múltiples parámetros
> - Ejemplos de diseño

# Ejemplo rápido

> [!ejemplo] Polinomio característico de tercer orden
> $$P(s) = s^3 + 6s^2 + 11s + 6$$
> 
> **Tabla de Routh:**
> 
> $$
> \begin{array}{c|cc}
> s^3 & 1 & 11 \\
> s^2 & 6 & 6 \\
> s^1 & \frac{6\cdot11 - 1\cdot6}{6} = 10 & 0 \\
> s^0 & 6 & 
> \end{array}
> $$
> 
> **Primera columna:** $1, 6, 10, 6$ (todos positivos)
> 
> **Conclusión:** Todos los polos tienen $\Re(s) < 0$ → sistema estable.

# Ventajas y desventajas

> [!info] Ventajas
> 1. No requiere calcular polos (útil para orden $\ge 3$)
> 2. Da el número exacto de polos inestables
> 3. Permite determinar rangos de parámetros para estabilidad
> 4. Fácil de implementar computacionalmente para polinomios de orden medio

> [!warning] Desventajas
> 1. Solo aplica a **polinomios** con coeficientes reales
> 2. No maneja **retardos de tiempo** ($e^{-sT}$)
> 3. No da información sobre la ubicación exacta de los polos estables
> 4. Para sistemas de orden muy alto, los cálculos pueden ser tediosos (pero automatizables)

# Limitaciones

> [!warning]
> 1. El criterio asume que el polinomio característico **no tiene polos repetidos en el eje imaginario** (casos especiales detectan esto)
> 2. Para sistemas con retardos, se requieren métodos como: aproximación de Padé, criterio de Mikhailov, o análisis frecuencial
> 3. El método no distingue entre estabilidad asintótica y marginal (se requiere análisis complementario)
> 4. Para sistemas en [[Espacio Estados/index | espacio de estados]], se pueden usar directamente los autovalores de $\mathbf{A}$ (que son los polos)