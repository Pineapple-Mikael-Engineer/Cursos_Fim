---
title: Variables de Desviación
tags:
  - control-clasico
  - teoria
  - linealizacion
draft: false
aliases:
  - variables desviacion
  - desviacion
  - delta variables
---

# Variables de Desviación

# Definición

> [!definicion] Variables de desviación
> Dado un punto de operación $(\mathbf{x}_0, \mathbf{u}_0, \mathbf{y}_0)$:
> 
> $$\delta \mathbf{x}(t) = \mathbf{x}(t) - \mathbf{x}_0$$
> $$\delta \mathbf{u}(t) = \mathbf{u}(t) - \mathbf{u}_0$$
> $$\delta \mathbf{y}(t) = \mathbf{y}(t) - \mathbf{y}_0$$

> [!info] Propiedad fundamental
> En variables de desviación, el **punto de equilibrio se traslada al origen**:
> 
> Cuando $\mathbf{x}(t) = \mathbf{x}_0$ y $\mathbf{u}(t) = \mathbf{u}_0$, entonces $\delta \mathbf{x} = \mathbf{0}$ y $\delta \mathbf{u} = \mathbf{0}$.

# Por qué usar variables de desviación

> [!info] Ventajas
> 1. **Simplifica el análisis:** El punto de equilibrio está en el origen
> 2. **Condiciones iniciales:** $\delta \mathbf{x}(0) = \mathbf{x}(0) - \mathbf{x}_0$ representa la desviación inicial
> 3. **Linealización:** La aproximación lineal es válida para pequeñas $\delta \mathbf{x}$ y $\delta \mathbf{u}$
> 4. **Teoremas de estabilidad:** Se aplican directamente (estabilidad del origen)

# Transformación del sistema

> [!teorema] Sistema original en variables de desviación
> Dado $\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x}, \mathbf{u})$ con punto de equilibrio $(\mathbf{x}_0, \mathbf{u}_0)$:
> 
> $$\delta \dot{\mathbf{x}} = \mathbf{f}(\mathbf{x}_0 + \delta \mathbf{x}, \mathbf{u}_0 + \delta \mathbf{u})$$
> 
> con $\delta \mathbf{x}(0) = \mathbf{x}(0) - \mathbf{x}_0$.

> [!demostracion]
> Derivando $\delta \mathbf{x} = \mathbf{x} - \mathbf{x}_0$:
> 
> $$\delta \dot{\mathbf{x}} = \dot{\mathbf{x}} - \dot{\mathbf{x}}_0 = \dot{\mathbf{x}} - \mathbf{0} = \dot{\mathbf{x}}$$
> 
> Pero $\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x}, \mathbf{u}) = \mathbf{f}(\mathbf{x}_0 + \delta \mathbf{x}, \mathbf{u}_0 + \delta \mathbf{u})$.

# Sistema linealizado en variables de desviación

> [!teorema] Forma lineal
> Usando expansión de [[Serie Taylor | Taylor]] alrededor de $(\mathbf{x}_0, \mathbf{u}_0)$:
> 
> $$\delta \dot{\mathbf{x}} \approx \mathbf{A} \delta \mathbf{x} + \mathbf{B} \delta \mathbf{u}$$
> 
> donde:
> $$\mathbf{A} = \left. \frac{\partial \mathbf{f}}{\partial \mathbf{x}} \right|_{(\mathbf{x}_0, \mathbf{u}_0)}, \quad
>    \mathbf{B} = \left. \frac{\partial \mathbf{f}}{\partial \mathbf{u}} \right|_{(\mathbf{x}_0, \mathbf{u}_0)}$$

> [!demostracion]
> Sustituyendo la expansión de Taylor en $\delta \dot{\mathbf{x}} = \mathbf{f}(\mathbf{x}_0 + \delta \mathbf{x}, \mathbf{u}_0 + \delta \mathbf{u})$:
> 
> $$\mathbf{f}(\mathbf{x}_0 + \delta \mathbf{x}, \mathbf{u}_0 + \delta \mathbf{u}) = \mathbf{f}(\mathbf{x}_0, \mathbf{u}_0) + \mathbf{A} \delta \mathbf{x} + \mathbf{B} \delta \mathbf{u} + \text{SO}$$
> 
> Como $\mathbf{f}(\mathbf{x}_0, \mathbf{u}_0) = \mathbf{0}$ (punto de equilibrio):
> 
> $$\delta \dot{\mathbf{x}} = \mathbf{A} \delta \mathbf{x} + \mathbf{B} \delta \mathbf{u} + \text{SO}$$
> 
> Despreciando SO se obtiene la aproximación lineal.

# Ejemplo 1: Péndulo

> [!ejemplo] Modelo original
> $$x_1 = \theta, \quad x_2 = \dot{\theta}$$
> $$\dot{x}_1 = x_2$$
> $$\dot{x}_2 = -\frac{g}{l} \sin x_1 - \frac{b}{ml^2} x_2 + \frac{1}{ml^2} u$$
> 
> **Punto de equilibrio:** $x_{10} = 0$, $x_{20} = 0$, $u_0 = 0$
> 
> **Variables de desviación:**
> $$\delta x_1 = x_1 - 0 = \theta, \quad \delta x_2 = x_2 - 0 = \dot{\theta}, \quad \delta u = u - 0 = u$$
> 
> **Sistema linealizado en desviación:**
> $$\delta \dot{x}_1 = \delta x_2$$
> $$\delta \dot{x}_2 = -\frac{g}{l} \delta x_1 - \frac{b}{ml^2} \delta x_2 + \frac{1}{ml^2} \delta u$$
> 
> (En este caso, como $x_0 = 0$, las variables de desviación son iguales a las originales)

# Ejemplo 2: Péndulo con punto de equilibrio no nulo

> [!ejemplo] Péndulo en $\theta_0 = \pi/6$
> Punto de equilibrio: $x_{10} = \pi/6$ rad ($30^\circ$), $x_{20} = 0$, $u_0 = mgl \sin(\pi/6) = mgl \cdot 0.5$
> 
> **Variables de desviación:**
> $$\delta x_1 = x_1 - \pi/6, \quad \delta x_2 = x_2 - 0, \quad \delta u = u - 0.5 mgl$$
> 
> **Linealización:**
> $$\mathbf{A} = \begin{bmatrix} 0 & 1 \\ -\frac{g}{l} \cos(\pi/6) & -\frac{b}{ml^2} \end{bmatrix} = \begin{bmatrix} 0 & 1 \\ -\frac{g}{l} \cdot 0.866 & -\frac{b}{ml^2} \end{bmatrix}$$
> 
> $$\mathbf{B} = \begin{bmatrix} 0 \\ \frac{1}{ml^2} \end{bmatrix}$$
> 
> **Sistema linealizado en desviación:**
> $$\delta \dot{x}_1 = \delta x_2$$
> $$\delta \dot{x}_2 = -0.866\frac{g}{l} \delta x_1 - \frac{b}{ml^2} \delta x_2 + \frac{1}{ml^2} \delta u$$
> 
> **Interpretación:** La constante gravitacional efectiva es $0.866g$ (menor que en la vertical).

# Ejemplo 3: Sistema de levitación magnética

> [!ejemplo] Modelo simplificado
> $$\dot{x}_1 = x_2$$
> $$\dot{x}_2 = g - \frac{k}{m} \frac{u^2}{x_1^2}$$
> 
> donde $x_1$ es posición (positiva hacia arriba), $x_2$ velocidad, $u$ corriente.
> 
> **Punto de equilibrio:** $x_{10} = h_0$, $x_{20} = 0$, $u_0 = \sqrt{\frac{mg}{k}} h_0$
> 
> **Variables de desviación:**
> $$\delta x_1 = x_1 - h_0, \quad \delta x_2 = x_2, \quad \delta u = u - u_0$$
> 
> **Linealización (desarrollar en serie):**
> 
> Para $\frac{u^2}{x_1^2}$ alrededor de $(h_0, u_0)$:
> 
> $$\frac{u^2}{x_1^2} \approx \frac{u_0^2}{h_0^2} + \frac{2u_0}{h_0^2} \delta u - \frac{2u_0^2}{h_0^3} \delta x_1 + \text{SO}$$
> 
> Como $\frac{u_0^2}{h_0^2} = \frac{mg}{k}$:
> 
> $$\dot{x}_2 = g - \frac{k}{m}\left( \frac{mg}{k} + \frac{2u_0}{h_0^2} \delta u - \frac{2u_0^2}{h_0^3} \delta x_1 \right)$$
> 
> $$\dot{x}_2 = -\frac{2k u_0}{m h_0^2} \delta u + \frac{2k u_0^2}{m h_0^3} \delta x_1$$
> 
> **Sistema linealizado:**
> $$\delta \dot{x}_1 = \delta x_2$$
> $$\delta \dot{x}_2 = \frac{2k u_0^2}{m h_0^3} \delta x_1 - \frac{2k u_0}{m h_0^2} \delta u$$

# Ecuación de salida en variables de desviación

> [!teorema] Salida linealizada
> Dada $\mathbf{y} = \mathbf{h}(\mathbf{x}, \mathbf{u})$ con $\mathbf{y}_0 = \mathbf{h}(\mathbf{x}_0, \mathbf{u}_0)$:
> 
> $$\delta \mathbf{y} \approx \mathbf{C} \delta \mathbf{x} + \mathbf{D} \delta \mathbf{u}$$
> 
> donde:
> $$\mathbf{C} = \left. \frac{\partial \mathbf{h}}{\partial \mathbf{x}} \right|_{(\mathbf{x}_0, \mathbf{u}_0)}, \quad
>    \mathbf{D} = \left. \frac{\partial \mathbf{h}}{\partial \mathbf{u}} \right|_{(\mathbf{x}_0, \mathbf{u}_0)}$$

> [!ejemplo] Salida no lineal
> $$y = x_1^2 + x_2$$
> Con $x_{10}=1$, $x_{20}=0$:
> 
> $y_0 = 1^2 + 0 = 1$
> 
> $\frac{\partial h}{\partial x_1} = 2x_1 = 2$, $\frac{\partial h}{\partial x_2} = 1$
> 
> $\mathbf{C} = \begin{bmatrix} 2 & 1 \end{bmatrix}$
> 
> $\delta y = y - 1 \approx 2 \delta x_1 + \delta x_2$

# Relación con función transferencia

> [!info] FT en variables de desviación
> Para sistemas lineales o linealizados, la función transferencia relaciona $\delta Y(s)$ con $\delta U(s)$:
> 
> $$\delta Y(s) = G(s) \delta U(s)$$
> 
> donde $\delta Y(s) = \mathcal{L}\{\delta y(t)\}$ y $\delta U(s) = \mathcal{L}\{\delta u(t)\}$.
> 
> Esto es válido porque las condiciones iniciales son $\delta \mathbf{x}(0) = \mathbf{x}(0) - \mathbf{x}_0$.

# Propiedades importantes

> [!info] Linealidad del operador desviación
> 1. $\delta(\dot{\mathbf{x}}) = \delta \dot{\mathbf{x}}$ (derivada y desviación conmutan)
> 2. $\delta(\mathbf{x}_1 + \mathbf{x}_2) = \delta \mathbf{x}_1 + \delta \mathbf{x}_2$
> 3. $\delta(\alpha \mathbf{x}) = \alpha \delta \mathbf{x}$ para $\alpha$ constante
> 4. $\delta(\mathbf{x}_1 \mathbf{x}_2) \approx \mathbf{x}_{10} \delta \mathbf{x}_2 + \mathbf{x}_{20} \delta \mathbf{x}_1$ (linealizado)

# Limitaciones

> [!warning]
> 1. **Solo válido para pequeñas desviaciones** del punto de operación
> 2. **El punto de operación debe ser un equilibrio** ($\mathbf{f}(\mathbf{x}_0, \mathbf{u}_0) = \mathbf{0}$)
> 3. **No captura dinámicas no lineales** como saturación o histéresis
> 4. **Para sistemas con múltiples equilibrios**, se necesita una linealización por cada uno