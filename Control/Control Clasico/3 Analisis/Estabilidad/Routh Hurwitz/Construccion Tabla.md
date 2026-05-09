---
title: Construcción de la Tabla de Routh
tags:
  - control-clasico
  - teoria
  - analisis
  - estabilidad
  - routh-hurwitz
draft: false
aliases:
  - tabla de routh
  - construir tabla routh
  - algoritmo routh
---

# Construcción de la Tabla de Routh

# Algoritmo general

> [!definicion] Procedimiento paso a paso
> Dado el polinomio característico:
> $$P(s) = a_n s^n + a_{n-1} s^{n-1} + a_{n-2} s^{n-2} + \dots + a_1 s + a_0$$
> 
> **Paso 1:** Verificar condición necesaria (todos los coeficientes $a_i$ deben tener el mismo signo y ser no nulos). Si no se cumple, el sistema es inestable.
> 
> **Paso 2:** Construir las dos primeras filas de la tabla:
> 
> $$\begin{array}{c|cccc} \\
> s ^{n} & a_{n} & a_{n-2} & a_{n-4} & \dots \\
> s ^{n-1} & a_{n-1}  & a_{n-3} & a_{n-5} & \dots	
> \end{array}$$
> 
> **Paso 3:** Calcular las filas siguientes usando:
> 
> $$b_1 = \frac{a_{n-1} \cdot a_{n-2} - a_n \cdot a_{n-3}}{a_{n-1}}$$
> $$b_2 = \frac{a_{n-1} \cdot a_{n-4} - a_n \cdot a_{n-5}}{a_{n-1}}$$
> $$b_3 = \frac{a_{n-1} \cdot a_{n-6} - a_n \cdot a_{n-7}}{a_{n-1}}$$
> 
> **Paso 4:** Continuar hasta obtener una fila con un solo elemento diferente de cero.

# Fórmula general para elementos

> [!info] Regla de cálculo
> Para cualquier fila $k$ (con elementos $c_1, c_2, c_3, \dots$) y dos filas superiores ($f_1, f_2, f_3, \dots$ y $g_1, g_2, g_3, \dots$):
> 
> $$c_i = \frac{g_1 \cdot f_{i+1} - f_1 \cdot g_{i+1}}{g_1}$$
> 
> donde $f_1$ es el primer elemento de la fila superior, $g_1$ es el primer elemento de la fila dos filas arriba.

# Ejemplo 1: Sistema de tercer orden

> [!ejemplo] Polinomio $P(s) = s^3 + 6s^2 + 11s + 6$
> 
> **Paso 1:** Coeficientes: $1, 6, 11, 6$ (todos positivos) ✓
> 
> **Paso 2:** Dos primeras filas:
> 
> $$
> \begin{array}{c|cc}
> s^3 & 1 & 11 \\
> s^2 & 6 & 6
> \end{array}
> $$
> 
> **Paso 3:** Calcular $s^1$:
> 
> $b_1 = \frac{6 \cdot 11 - 1 \cdot 6}{6} = \frac{66 - 6}{6} = \frac{60}{6} = 10$
> 
> $b_2 = \frac{6 \cdot 0 - 1 \cdot 0}{6} = 0$
> 
> $$
> \begin{array}{c|cc}
> s^3 & 1 & 11 \\
> s^2 & 6 & 6 \\
> s^1 & 10 & 0
> \end{array}
> $$
> 
> **Paso 4:** Calcular $s^0$:
> 
> $c_1 = \frac{10 \cdot 6 - 6 \cdot 0}{10} = \frac{60}{10} = 6$
> 
> $$
> \begin{array}{c|cc}
> s^3 & 1 & 11 \\
> s^2 & 6 & 6 \\
> s^1 & 10 & 0 \\
> s^0 & 6 & 
> \end{array}
> $$
> 
> **Primera columna:** $1, 6, 10, 6$ (todos positivos)
> 
> **Conclusión:** Sistema estable.

# Ejemplo 2: Sistema inestable (coeficientes positivos)

> [!ejemplo] Polinomio $P(s) = s^3 + s^2 + 2s + 8$
> 
> **Paso 1:** Coeficientes: $1, 1, 2, 8$ (todos positivos) ✓ (condición necesaria cumplida)
> 
> **Paso 2:** Dos primeras filas:
> 
> $$
> \begin{array}{c|cc}
> s^3 & 1 & 2 \\
> s^2 & 1 & 8
> \end{array}
> $$
> 
> **Paso 3:** Calcular $s^1$:
> 
> $b_1 = \frac{1 \cdot 2 - 1 \cdot 8}{1} = \frac{2 - 8}{1} = -6$
> 
> $b_2 = \frac{1 \cdot 0 - 1 \cdot 0}{1} = 0$
> 
> $$
> \begin{array}{c|cc}
> s^3 & 1 & 2 \\
> s^2 & 1 & 8 \\
> s^1 & -6 & 0
> \end{array}
> $$
> 
> **Paso 4:** Calcular $s^0$:
> 
> $c_1 = \frac{(-6) \cdot 8 - 1 \cdot 0}{-6} = \frac{-48}{-6} = 8$
> 
> $$
> \begin{array}{c|cc}
> s^3 & 1 & 2 \\
> s^2 & 1 & 8 \\
> s^1 & -6 & 0 \\
> s^0 & 8 & 
> \end{array}
> $$
> 
> **Primera columna:** $1, 1, -6, 8$ (dos cambios de signo: $1 \to -6$, $-6 \to 8$)
> 
> **Conclusión:** Dos polos con parte real positiva (inestable).

# Ejemplo 3: Sistema de cuarto orden

> [!ejemplo] Polinomio $P(s) = s^4 + 2s^3 + 3s^2 + 4s + 5$
> 
> **Paso 1:** Coeficientes: $1, 2, 3, 4, 5$ (todos positivos) ✓
> 
> **Paso 2:** Dos primeras filas:
> 
> $$
> \begin{array}{c|ccc}
> s^4 & 1 & 3 & 5 \\
> s^3 & 2 & 4 & 0
> \end{array}
> $$
> 
> **Paso 3:** Calcular $s^2$:
> 
> $b_1 = \frac{2 \cdot 3 - 1 \cdot 4}{2} = \frac{6 - 4}{2} = \frac{2}{2} = 1$
> 
> $b_2 = \frac{2 \cdot 5 - 1 \cdot 0}{2} = \frac{10}{2} = 5$
> 
> $b_3 = 0$
> 
> $$
> \begin{array}{c|ccc}
> s^4 & 1 & 3 & 5 \\
> s^3 & 2 & 4 & 0 \\
> s^2 & 1 & 5 & 0
> \end{array}
> $$
> 
> **Paso 4:** Calcular $s^1$:
> 
> $c_1 = \frac{1 \cdot 4 - 2 \cdot 5}{1} = \frac{4 - 10}{1} = -6$
> 
> $c_2 = \frac{1 \cdot 0 - 2 \cdot 0}{1} = 0$
> 
> $$
> \begin{array}{c|ccc}
> s^4 & 1 & 3 & 5 \\
> s^3 & 2 & 4 & 0 \\
> s^2 & 1 & 5 & 0 \\
> s^1 & -6 & 0 & 0
> \end{array}
> $$
> 
> **Paso 5:** Calcular $s^0$:
> 
> $d_1 = \frac{(-6) \cdot 5 - 1 \cdot 0}{-6} = \frac{-30}{-6} = 5$
> 
> $$
> \begin{array}{c|ccc}
> s^4 & 1 & 3 & 5 \\
> s^3 & 2 & 4 & 0 \\
> s^2 & 1 & 5 & 0 \\
> s^1 & -6 & 0 & 0 \\
> s^0 & 5 &   & 
> \end{array}
> $$
> 
> **Primera columna:** $1, 2, 1, -6, 5$ (dos cambios de signo: $1 \to -6$, $-6 \to 5$)
> 
> **Conclusión:** Dos polos con parte real positiva (inestable).

# Interpretación de resultados

> [!info] Primera columna
> | Condición | Significado |
> |-----------|-------------|
> | Todos los elementos tienen el **mismo signo** | Sistema estable |
> | **Cambios de signo** | Hay tantos polos inestables como cambios |
> | **Ceros** en primera columna | Ver [[Casos Especiales]] |

> [!ejemplo] Conteo de cambios
> Primera columna: $1, 3, -2, 4, -1$
> 
> Cambios:
> - $3 \to -2$ (cambio)
> - $-2 \to 4$ (cambio)
> - $4 \to -1$ (cambio)
> 
> Total: **3 cambios** → 3 polos con parte real positiva.

# Simplificaciones para polinomios pares e impares

> [!info] Polinomios con términos faltantes
> Si el polinomio tiene **términos faltantes** (coeficientes cero), ya es un indicador de posibles problemas.
> 
> Ejemplo: $s^5 + 2s^3 + s$ (faltan $s^4$, $s^2$, término constante)
> 
> Ver [[Casos Especiales| Primer elemento cero]] para manejo.

# Limitaciones

> [!warning]
> 1. El algoritmo **fracasa** si $a_{n-1} = 0$ (primer elemento de la segunda fila es cero), requiere manejo especial
> 2. Para polinomios de grado muy alto, los cálculos pueden ser largos (recomendable automatizar)
> 3. El método no da información sobre ubicación exacta de polos estables, solo cuenta inestables
> 4. No aplica a sistemas con retardos

# Demostración del método de Routh-Hurwitz

> [!teorema] Justificación fundamental
> El criterio de Routh-Hurwitz determina el número de raíces con parte real positiva analizando los coeficientes del polinomio mediante una **transformación conforme** que mapea el semiplano izquierdo en el interior del círculo unitario.

> [!demostracion] Paso 1: Transformación bilineal
> 
> Sea la transformación:
> 
> $$z = \frac{1 + s}{1 - s} \quad \Longleftrightarrow \quad s = \frac{z - 1}{z + 1}$$
> 
> Esta transformación **mapea**:
> - El semiplano izquierdo $\Re(s) < 0$ → interior del círculo unitario $|z| < 1$
> - El eje imaginario $s = j\omega$ → círculo unitario $|z| = 1$
> - El semiplano derecho $\Re(s) > 0$ → exterior del círculo unitario $|z| > 1$

> [!demostracion] Paso 2: Aplicación al polinomio
> 
> Dado $P(s) = a_n s^n + a_{n-1} s^{n-1} + \dots + a_0$, sustituimos $s = \frac{z-1}{z+1}$:
> 
> $$P\left(\frac{z-1}{z+1}\right) = \frac{Q(z)}{(z+1)^n}$$
> 
> donde $Q(z)$ es un polinomio en $z$ de grado $n$.
> 
> Las raíces de $P(s)$ con $\Re(s) < 0$ corresponden a raíces de $Q(z)$ con $|z| < 1$.

> [!demostracion] Paso 3: Aplicación del criterio de Schur-Cohn
> 
> El criterio de Schur-Cohn determina cuántas raíces de $Q(z)$ están dentro del círculo unitario.
> 
> Routh aplicó un **algoritmo recursivo** sobre los coeficientes de $P(s)$ que es **equivalente** a aplicar Schur-Cohn sobre $Q(z)$, pero trabajando directamente con $P(s)$.

> [!demostracion] Paso 4: Algoritmo recursivo de Routh
> 
> La tabla de Routh se construye con:
> 
> $$c_{i,j} = \frac{c_{i-2,1} \cdot c_{i-1,j+1} - c_{i-1,1} \cdot c_{i-2,j+1}}{c_{i-1,1}}$$
> 
> Este algoritmo es **equivalente** a realizar la transformación bilineal implícitamente y contar los cambios de signo en la primera columna.
> 
> El **teorema de Sturm** garantiza que el número de cambios de signo es igual al número de raíces de $Q(z)$ fuera del círculo unitario, que a su vez corresponde al número de raíces de $P(s)$ con $\Re(s) > 0$.

> [!demostracion] Paso 5: Principio del argumento (justificación conceptual)
> 
> Sea $P(s)$ un polinomio. El número de ceros en el semiplano derecho es:
> 
> $$N = \frac{1}{2\pi j} \oint_{\Gamma} \frac{P'(s)}{P(s)} ds$$
> 
> donde $\Gamma$ es el contorno de Nyquist (eje imaginario + semicírculo infinito).
> 
> Routh-Hurwitz evita esta integral compleja mediante **álgebra de coeficientes**, utilizando los **determinantes de Hurwitz**:
> 
> $$\Delta_1 = a_{n-1}, \quad \Delta_2 = \det\begin{bmatrix} a_{n-1} & a_{n-3} \\ a_n & a_{n-2} \end{bmatrix}, \quad \Delta_3 = \det\begin{bmatrix} a_{n-1} & a_{n-3} & a_{n-5} \\ a_n & a_{n-2} & a_{n-4} \\ 0 & a_{n-1} & a_{n-3} \end{bmatrix}, \dots$$
> 
> El sistema es estable si y solo si **todos** $\Delta_i > 0$.

> [!referencia] Conclusión
> La tabla de Routh es un **algoritmo eficiente** para calcular los signos de los determinantes de Hurwitz sin evaluar determinantes explícitamente. Los cambios de signo en la primera columna indican cuántos determinantes cambian de signo, lo que equivale al número de raíces con parte real positiva.