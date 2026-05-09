---
title: Espacio de Estados
tags:
  - control-clasico
  - teoria
  - modelado
draft: false
aliases:
  - espacio estados
  - representación en estados
  - variables de estado
---

# Espacio de Estados

# Definición

> [!definicion] Representación en espacio de estados
> Para un sistema dinámico de orden $n$, con $m$ entradas y $p$ salidas:
> 
> **Ecuación de estado:**
> $$\dot{\mathbf{x}}(t) = \mathbf{A} \mathbf{x}(t) + \mathbf{B} \mathbf{u}(t)$$
> 
> **Ecuación de salida:**
> $$\mathbf{y}(t) = \mathbf{C} \mathbf{x}(t) + \mathbf{D} \mathbf{u}(t)$$
> 
> donde:
> - $\mathbf{x}(t) \in \mathbb{R}^n$: vector de **estados**
> - $\mathbf{u}(t) \in \mathbb{R}^m$: vector de **entradas**
> - $\mathbf{y}(t) \in \mathbb{R}^p$: vector de **salidas**
> - $\mathbf{A} \in \mathbb{R}^{n \times n}$: matriz de **dinámica**
> - $\mathbf{B} \in \mathbb{R}^{n \times m}$: matriz de **entrada**
> - $\mathbf{C} \in \mathbb{R}^{p \times n}$: matriz de **salida**
> - $\mathbf{D} \in \mathbb{R}^{p \times m}$: matriz de **transmisión directa**

> [!info] Caso SISO
> Para sistemas SISO (una entrada, una salida):
> - $u(t)$ es escalar, $\mathbf{B}$ es vector columna $n \times 1$
> - $y(t)$ es escalar, $\mathbf{C}$ es vector fila $1 \times n$
> - $\mathbf{D}$ es escalar

# Por qué espacio de estados

> [!info] Ventajas sobre función transferencia
> 1. **Condiciones iniciales:** se incorporan naturalmente
> 2. **Sistemas MIMO:** maneja múltiples entradas y salidas
> 3. **Sistemas no lineales:** base para linealización
> 4. **Sistemas variantes en el tiempo:** permite $\mathbf{A}(t), \mathbf{B}(t), \mathbf{C}(t), \mathbf{D}(t)$
> 5. **Análisis interno:** controlabilidad, observabilidad, estabilidad interna

> [!warning] Limitaciones de función transferencia
> La función transferencia $G(s)$:
> - Solo describe relación entrada-salida con CI nulas
> - No revela estabilidad interna si hay cancelaciones
> - No permite analizar controlabilidad/observabilidad
> 
> Ver [[Funcion Transferencia/index | función transferencia]].

# Ejemplo: masa-resorte-amortiguador

> [!ejemplo] Modelado en espacio de estados
> $$m\ddot{y} + b\dot{y} + ky = u$$
> 
> **Paso 1:** Elegir variables de estado:
> $$x_1 = y \quad \text{(posición)}$$
> $$x_2 = \dot{y} \quad \text{(velocidad)}$$
> 
> **Paso 2:** Escribir ecuaciones:
> $$\dot{x}_1 = x_2$$
> $$\dot{x}_2 = \frac{1}{m}(-b x_2 - k x_1 + u)$$
> 
> **Paso 3:** Forma matricial:
> $$\dot{\mathbf{x}} = \begin{bmatrix} 0 & 1 \\ -\frac{k}{m} & -\frac{b}{m} \end{bmatrix} \mathbf{x} + \begin{bmatrix} 0 \\ \frac{1}{m} \end{bmatrix} u$$
> 
> $$y = \begin{bmatrix} 1 & 0 \end{bmatrix} \mathbf{x} + \begin{bmatrix} 0 \end{bmatrix} u$$

# Relación con función transferencia

> [!teorema] De espacio de estados a FT (caso SISO)
> Para sistemas SISO, la función transferencia es:
> $$G(s) = \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D}$$
> 
> donde $G(s)$ es un **escalar**.

> [!teorema] Caso MIMO
> Para sistemas MIMO, la matriz de transferencia es:
> $$\mathbf{G}(s) = \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} + \mathbf{D}$$
> 
> donde $\mathbf{G}(s) \in \mathbb{C}^{p \times m}$.

> [!demostracion] Demostración (caso SISO)
> Aplicando Laplace a las ecuaciones con CI nulas ($\mathbf{x}(0^-)=\mathbf{0}$):
> 
> $$s\mathbf{X}(s) = \mathbf{A}\mathbf{X}(s) + \mathbf{B}U(s)$$
> 
> Reagrupando:
> $$(s\mathbf{I} - \mathbf{A})\mathbf{X}(s) = \mathbf{B}U(s)$$
> 
> Despejando $\mathbf{X}(s)$:
> $$\mathbf{X}(s) = (s\mathbf{I} - \mathbf{A})^{-1} \mathbf{B} U(s)$$
> 
> La ecuación de salida en Laplace:
> $$Y(s) = \mathbf{C}\mathbf{X}(s) + \mathbf{D} U(s)$$
> 
> Sustituyendo $\mathbf{X}(s)$:
> $$Y(s) = \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1} \mathbf{B} U(s) + \mathbf{D} U(s)$$
> 
> Factorizando $U(s)$:
> $$Y(s) = \left[ \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1} \mathbf{B} + \mathbf{D} \right] U(s)$$
> 
> Por definición de función transferencia $G(s) = Y(s)/U(s)$:
> $$G(s) = \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1} \mathbf{B} + \mathbf{D}$$

> [!ejemplo] Del ejemplo anterior
> $$\mathbf{A} = \begin{bmatrix} 0 & 1 \\ -k/m & -b/m \end{bmatrix}, \quad 
>    \mathbf{B} = \begin{bmatrix} 0 \\ 1/m \end{bmatrix}, \quad 
>    \mathbf{C} = \begin{bmatrix} 1 & 0 \end{bmatrix}, \quad 
>    \mathbf{D} = 0$$
> 
> $$s\mathbf{I} - \mathbf{A} = \begin{bmatrix} s & -1 \\ k/m & s + b/m \end{bmatrix}$$
> 
> $$(s\mathbf{I} - \mathbf{A})^{-1} = \frac{1}{s^2 + (b/m)s + k/m} \begin{bmatrix} s + b/m & 1 \\ -k/m & s \end{bmatrix}$$
> 
> $$G(s) = \mathbf{C}(s\mathbf{I} - \mathbf{A})^{-1}\mathbf{B} = 
>    \frac{1}{ms^2 + bs + k}$$
> 
> Ver [[Pasar a FT]] para más ejemplos.

# Diagrama de bloques

> [!info] Representación en diagrama de bloques
> 
> ![[espacio_estados_diagrama.svg|600]]
> 
> donde:
> - $u(t)$ se bifurca en la entrada
> - $\mathbf{B}$ escala la entrada
> - El sumador combina $\mathbf{B}u$ con $\mathbf{A}\mathbf{x}$
> - El integrador $\frac{1}{s}$ convierte $\dot{\mathbf{x}}$ en $\mathbf{x}$
> - $\mathbf{x}(t)$ se bifurca: va a $\mathbf{C}$ y a $\mathbf{A}$
> - $\mathbf{C}$ produce $\mathbf{C}\mathbf{x}$
> - $\mathbf{D}$ produce $\mathbf{D}u$ (alimentación directa)
> - El sumador final combina $\mathbf{C}\mathbf{x} + \mathbf{D}u$ para formar $y(t)$

# Formas canónicas

> [!info] Realizaciones comunes
> | Forma | Característica | Uso |
> |-------|----------------|-----|
> | [[Forma Canónica Controlable]] | Controlabilidad explícita | Diseño por ubicación de polos |
> | [[Forma Canónica Observable]] | Observabilidad explícita | Diseño de observadores |
> | [[Forma Diagonal]] | Polos en diagonal (sistema desacoplado) | Análisis modal |
> | [[Forma de Jordan]] | Polos repetidos | Sistemas con valores propios múltiples |

# Estabilidad en espacio de estados

> [!definicion] Estabilidad interna
> El sistema $\dot{\mathbf{x}} = \mathbf{A}\mathbf{x}$ es **asintóticamente estable** si y solo si todos los **valores propios** de $\mathbf{A}$ tienen parte real negativa:
> $$\Re(\lambda_i(\mathbf{A})) < 0 \quad \forall i$$
> 
> Esto es equivalente a que todos los polos de $\mathbf{G}(s)$ tengan $\Re(p_i) < 0$, **si no hay cancelaciones polo-cero**.

# Conceptos avanzados

> [!info] Controlabilidad
> Un sistema es controlable si existe una entrada $\mathbf{u}(t)$ que lleva el estado de $\mathbf{x}(0)$ a cualquier $\mathbf{x}(t_f)$ en tiempo finito.
> 
> Criterio de controlabilidad: $\text{rango}[\mathbf{B} \ \mathbf{AB} \ \mathbf{A}^2\mathbf{B} \ \dots \ \mathbf{A}^{n-1}\mathbf{B}] = n$.

> [!info] Observabilidad
> Un sistema es observable si se puede determinar $\mathbf{x}(0)$ a partir de $\mathbf{u}(t)$ e $\mathbf{y}(t)$ en un intervalo finito.
> 
> Criterio de observabilidad: $\text{rango}[\mathbf{C} \ \mathbf{CA} \ \mathbf{CA}^2 \ \dots \ \mathbf{CA}^{n-1}]^T = n$.

# Limitaciones

> [!warning]
> 1. Para sistemas de orden alto, las matrices $\mathbf{A}, \mathbf{B}, \mathbf{C}, \mathbf{D}$ pueden ser grandes
> 2. Elegir buenas variables de estado es clave para simplificar el modelo
> 3. La transformación a formas canónicas puede ser numéricamente sensible