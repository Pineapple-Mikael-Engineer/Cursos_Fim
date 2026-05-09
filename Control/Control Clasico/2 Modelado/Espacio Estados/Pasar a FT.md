---
title: De Espacio de Estados a Función Transferencia
tags:
  - control-clasico
  - teoria
  - espacio-estados
draft: false
aliases:
  - espacio a ft
  - espacio a transferencia
  - calcular ft desde espacio
---

# De Espacio de Estados a Función Transferencia

# Fórmula general

> [!teorema] Fórmula de transformación (SISO)
> Dado el sistema:
> $$\dot{\mathbf{x}} = \mathbf{A}\mathbf{x} + \mathbf{B}u$$
> $$y = \mathbf{C}\mathbf{x} + \mathbf{D}u$$
> 
> La función transferencia es:
> $$G(s) = \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D}$$

> [!teorema] Caso MIMO
> Para múltiples entradas y salidas:
> $$\mathbf{G}(s) = \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D}$$
> 
> donde $\mathbf{G}(s) \in \mathbb{C}^{p \times m}$ es la **matriz de transferencia**.

# Demostración operativa

> [!demostracion] Procedimiento paso a paso (SISO)
> **Paso 1:** Aplicar Laplace con CI nulas ($\mathbf{x}(0^-)=\mathbf{0}$):
> $$s\mathbf{X}(s) = \mathbf{A}\mathbf{X}(s) + \mathbf{B}U(s)$$
> 
> **Paso 2:** Reagrupar términos con $\mathbf{X}(s)$:
> $$(s\mathbf{I} - \mathbf{A})\mathbf{X}(s) = \mathbf{B}U(s)$$
> 
> **Paso 3:** Despejar $\mathbf{X}(s)$:
> $$\mathbf{X}(s) = (s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B}U(s)$$
> 
> **Paso 4:** Ecuación de salida en Laplace:
> $$Y(s) = \mathbf{C}\mathbf{X}(s) + \mathbf{D}U(s)$$
> 
> **Paso 5:** Sustituir $\mathbf{X}(s)$:
> $$Y(s) = \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B}U(s) + \mathbf{D}U(s)$$
> 
> **Paso 6:** Factorizar $U(s)$:
> $$Y(s) = \left[ \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D} \right] U(s)$$
> 
> **Paso 7:** Por definición $G(s) = Y(s)/U(s)$:
> $$G(s) = \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D}$$

# Procedimiento de cálculo

> [!info] Algoritmo práctico
> 1. Construir la matriz $s\mathbf{I} - \mathbf{A}$
> 2. Calcular su inversa: $(s\mathbf{I} - \mathbf{A})^{-1} = \frac{\text{adj}(s\mathbf{I} - \mathbf{A})}{\det(s\mathbf{I} - \mathbf{A})}$
> 3. Multiplicar: $\mathbf{C} \cdot (s\mathbf{I} - \mathbf{A})^{-1} \cdot \mathbf{B}$
> 4. Sumar $\mathbf{D}$ (si es distinta de cero)
> 5. Simplificar la expresión racional

# Ejemplo 1: Sistema de segundo orden

> [!ejemplo] Masa-resorte-amortiguador
> $$\dot{\mathbf{x}} = \begin{bmatrix} 0 & 1 \\ -\frac{k}{m} & -\frac{b}{m} \end{bmatrix} \mathbf{x} + \begin{bmatrix} 0 \\ \frac{1}{m} \end{bmatrix} u$$
> $$y = \begin{bmatrix} 1 & 0 \end{bmatrix} \mathbf{x}, \quad \mathbf{D}=0$$
> 
> **Paso 1:** $s\mathbf{I} - \mathbf{A} = \begin{bmatrix} s & -1 \\ \frac{k}{m} & s + \frac{b}{m} \end{bmatrix}$
> 
> **Paso 2:** Determinante:
> $$\Delta(s) = \det(s\mathbf{I} - \mathbf{A}) = s\left(s + \frac{b}{m}\right) + \frac{k}{m} = s^2 + \frac{b}{m}s + \frac{k}{m}$$
> 
> **Paso 3:** Inversa:
> $$(s\mathbf{I} - \mathbf{A})^{-1} = \frac{1}{\Delta(s)} \begin{bmatrix} s + \frac{b}{m} & 1 \\ -\frac{k}{m} & s \end{bmatrix}$$
> 
> **Paso 4:** Multiplicar $\mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}$:
> $$\begin{bmatrix} 1 & 0 \end{bmatrix} \begin{bmatrix} s + \frac{b}{m} & 1 \\ -\frac{k}{m} & s \end{bmatrix} \frac{1}{\Delta(s)} = \frac{1}{\Delta(s)} \begin{bmatrix} s + \frac{b}{m} & 1 \end{bmatrix}$$
> 
> **Paso 5:** Multiplicar por $\mathbf{B}$:
> $$\frac{1}{\Delta(s)} \begin{bmatrix} s + \frac{b}{m} & 1 \end{bmatrix} \begin{bmatrix} 0 \\ \frac{1}{m} \end{bmatrix} = \frac{1}{\Delta(s)} \cdot \frac{1}{m}$$
> 
> **Paso 6:** Resultado:
> $$G(s) = \frac{1/m}{s^2 + \frac{b}{m}s + \frac{k}{m}} = \frac{1}{ms^2 + bs + k}$$

# Ejemplo 2: Sistema de primer orden

> [!ejemplo] Circuito RC
> $$A = -\frac{1}{RC}, \quad B = \frac{1}{RC}, \quad C = 1, \quad D = 0$$
> 
> **Paso 1:** $sI - A = s + \frac{1}{RC}$
> 
> **Paso 2:** Inversa: $\frac{1}{s + \frac{1}{RC}}$
> 
> **Paso 3:** $G(s) = 1 \cdot \frac{1}{s + \frac{1}{RC}} \cdot \frac{1}{RC} = \frac{1/RC}{s + 1/RC} = \frac{1}{RCs + 1}$

# Ejemplo 3: Sistema con alimentación directa

> [!ejemplo] Sistema con $D \neq 0$
> $$\dot{x} = -2x + 3u$$
> $$y = 4x + 5u$$
> 
> **Paso 1:** $sI - A = s + 2$
> 
> **Paso 2:** $(sI - A)^{-1} = \frac{1}{s+2}$
> 
> **Paso 3:** $C(sI - A)^{-1}B = 4 \cdot \frac{1}{s+2} \cdot 3 = \frac{12}{s+2}$
> 
> **Paso 4:** Sumar $D$:
> $$G(s) = \frac{12}{s+2} + 5 = \frac{12 + 5(s+2)}{s+2} = \frac{5s + 22}{s+2}$$

# Ejemplo 4: Sistema MIMO 2x2

> [!ejemplo] Dos entradas, dos salidas
> $$\dot{\mathbf{x}} = \begin{bmatrix} -1 & 0 \\ 0 & -2 \end{bmatrix} \mathbf{x} + \begin{bmatrix} 1 & 0 \\ 0 & 1 \end{bmatrix} \mathbf{u}$$
> $$\mathbf{y} = \begin{bmatrix} 1 & 1 \\ 0 & 1 \end{bmatrix} \mathbf{x}, \quad \mathbf{D} = \mathbf{0}$$
> 
> **Paso 1:** $s\mathbf{I} - \mathbf{A} = \begin{bmatrix} s+1 & 0 \\ 0 & s+2 \end{bmatrix}$
> 
> **Paso 2:** $(s\mathbf{I} - \mathbf{A})^{-1} = \begin{bmatrix} \frac{1}{s+1} & 0 \\ 0 & \frac{1}{s+2} \end{bmatrix}$
> 
> **Paso 3:** $\mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1} = \begin{bmatrix} \frac{1}{s+1} & \frac{1}{s+2} \\ 0 & \frac{1}{s+2} \end{bmatrix}$
> 
> **Paso 4:** Multiplicar por $\mathbf{B}$ (identidad):
> $$\mathbf{G}(s) = \begin{bmatrix} \frac{1}{s+1} & \frac{1}{s+2} \\ 0 & \frac{1}{s+2} \end{bmatrix}$$
> 
> Interpretación: $G_{11}(s) = \frac{1}{s+1}$, $G_{12}(s) = \frac{1}{s+2}$, $G_{21}(s) = 0$, $G_{22}(s) = \frac{1}{s+2}$.

# Relación con los polos del sistema

> [!teorema] Polos = autovalores de $\mathbf{A}$
> Los polos de $G(s)$ son los **autovalores** de $\mathbf{A}$, excepto posibles cancelaciones polo-cero.
> 
> $$\text{polos} \subseteq \{\lambda_1, \lambda_2, \dots, \lambda_n\}$$
> 
> donde $\lambda_i$ son los autovalores de $\mathbf{A}$.

> [!demostracion]
> El polinomio característico es:
> $$\det(s\mathbf{I} - \mathbf{A}) = s^n + \alpha_{n-1}s^{n-1} + \dots + \alpha_0$$
> 
> Este polinomio aparece en el denominador de $G(s)$, pero factores comunes con el numerador pueden cancelarse.

# Verificación de cancelaciones

> [!info] Cancelación polo-cero
> Si $\mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B}$ tiene cancelaciones, el orden aparente de $G(s)$ es menor que $n$.
> 
> Esto indica que el sistema no es **controlable** y/o **observable**.
> 
> Ver [[Controlabilidad]] y [[Observabilidad]].

# Resumen del procedimiento

> [!info] Pasos rápidos
> 1. Calcular $\Delta(s) = \det(s\mathbf{I} - \mathbf{A})$
> 2. Calcular $\mathbf{N}(s) = \text{adj}(s\mathbf{I} - \mathbf{A})$
> 3. $G(s) = \frac{\mathbf{C} \cdot \mathbf{N}(s) \cdot \mathbf{B}}{\Delta(s)} + \mathbf{D}$
> 4. Simplificar factores comunes

# Limitaciones

> [!warning]
> 1. La inversión de matrices para sistemas de orden alto ($n > 4$) es tediosa manualmente
> 2. Para sistemas grandes, usar herramientas computacionales (MATLAB, Python)
> 3. La cancelación polo-cero puede ocultar dinámicas internas inestables