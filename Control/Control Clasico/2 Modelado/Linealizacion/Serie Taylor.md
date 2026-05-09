---
title: Serie de Taylor para Linealización
tags:
  - control-clasico
  - teoria
  - linealizacion
draft: false
aliases:
  - serie taylor
  - expansion taylor
  - aproximacion lineal
---

# Serie de Taylor para Linealización

# Definición

> [!definicion] Serie de Taylor (caso escalar)
> Dada una función $f(x)$ infinitamente diferenciable alrededor de $x_0$:
> 
> $$f(x) = f(x_0) + f'(x_0)(x - x_0) + \frac{f''(x_0)}{2!}(x - x_0)^2 + \frac{f'''(x_0)}{3!}(x - x_0)^3 + \dots$$
> 
> La **aproximación lineal** (primer orden) es:
> $$f(x) \approx f(x_0) + f'(x_0)(x - x_0)$$

> [!definicion] Serie de Taylor (caso vectorial)
> Dada $\mathbf{f}(\mathbf{x})$ con $\mathbf{x} \in \mathbb{R}^n$:
> 
> $$\mathbf{f}(\mathbf{x}) = \mathbf{f}(\mathbf{x}_0) + \left. \frac{\partial \mathbf{f}}{\partial \mathbf{x}} \right|_{\mathbf{x}_0} (\mathbf{x} - \mathbf{x}_0) + \text{términos de orden superior}$$
> 
> donde $\frac{\partial \mathbf{f}}{\partial \mathbf{x}}$ es la [[Jacobiano | matriz Jacobiana]].

# Demostración del teorema de linealización

> [!teorema] Linealización de un sistema no lineal
> Dado $\dot{\mathbf{x}} = \mathbf{f}(\mathbf{x}, \mathbf{u})$ con punto de equilibrio $(\mathbf{x}_0, \mathbf{u}_0)$ tal que $\mathbf{f}(\mathbf{x}_0, \mathbf{u}_0) = \mathbf{0}$, el sistema linealizado alrededor de ese punto es:
> 
> $$\delta \dot{\mathbf{x}} = \mathbf{A} \delta \mathbf{x} + \mathbf{B} \delta \mathbf{u}$$
> 
> donde $\mathbf{A} = \left. \frac{\partial \mathbf{f}}{\partial \mathbf{x}} \right|_0$, $\mathbf{B} = \left. \frac{\partial \mathbf{f}}{\partial \mathbf{u}} \right|_0$.

> [!demostracion] Paso 1: Expansión de Taylor
> Expandimos $\mathbf{f}(\mathbf{x}, \mathbf{u})$ alrededor de $(\mathbf{x}_0, \mathbf{u}_0)$:
> 
> $$\mathbf{f}(\mathbf{x}, \mathbf{u}) = \mathbf{f}(\mathbf{x}_0, \mathbf{u}_0) + \left. \frac{\partial \mathbf{f}}{\partial \mathbf{x}} \right|_0 (\mathbf{x} - \mathbf{x}_0) + \left. \frac{\partial \mathbf{f}}{\partial \mathbf{u}} \right|_0 (\mathbf{u} - \mathbf{u}_0) + \text{SO}$$
> 
> donde $\text{SO}$ (términos de segundo orden y superiores) incluye:
> - Términos cuadráticos: $(\mathbf{x} - \mathbf{x}_0)^2$, $(\mathbf{u} - \mathbf{u}_0)^2$, $(\mathbf{x} - \mathbf{x}_0)(\mathbf{u} - \mathbf{u}_0)$
> - Términos cúbicos y superiores
> 
> **Paso 2:** Evaluar en el punto de equilibrio
> 
> Por definición de punto de equilibrio: $\mathbf{f}(\mathbf{x}_0, \mathbf{u}_0) = \mathbf{0}$
> 
> **Paso 3:** Introducir variables de desviación
> 
> Sea $\delta \mathbf{x} = \mathbf{x} - \mathbf{x}_0$, $\delta \mathbf{u} = \mathbf{u} - \mathbf{u}_0$. Entonces $\dot{\mathbf{x}} = \delta \dot{\mathbf{x}}$ (pues $\mathbf{x}_0$ es constante).
> 
> Sustituyendo:
> 
> $$\delta \dot{\mathbf{x}} = \mathbf{A} \delta \mathbf{x} + \mathbf{B} \delta \mathbf{u} + \text{SO}$$
> 
> **Paso 4:** Despreciar términos de orden superior
> 
> Si $\delta \mathbf{x}$ y $\delta \mathbf{u}$ son **pequeños**, entonces $\text{SO}$ es despreciable (ej. si $\delta x = 0.01$, entonces $(\delta x)^2 = 0.0001$).
> 
> Por lo tanto:
> 
> $$\delta \dot{\mathbf{x}} \approx \mathbf{A} \delta \mathbf{x} + \mathbf{B} \delta \mathbf{u}$$

# Condiciones de validez de la aproximación

> [!info] ¿Cuándo es válida?
> 1. **La función debe ser diferenciable** en el punto de operación
> 2. **Las desviaciones deben ser pequeñas**: $\|\delta \mathbf{x}\| \ll 1$, $\|\delta \mathbf{u}\| \ll 1$
> 3. **El punto de operación debe ser un punto de equilibrio** ($\mathbf{f}(\mathbf{x}_0, \mathbf{u}_0) = \mathbf{0}$)
> 4. **Los términos de orden superior deben ser acotados** en la región de interés

# Error de la aproximación

> [!teorema] Teorema del resto (forma de Lagrange)
> Para el caso escalar, existe $\xi$ entre $x$ y $x_0$ tal que:
> 
> $$f(x) = f(x_0) + f'(x_0)(x - x_0) + \frac{f''(\xi)}{2}(x - x_0)^2$$
> 
> El error de la aproximación lineal es:
> $$E = \frac{f''(\xi)}{2}(x - x_0)^2$$
> 
> Por lo tanto, el error es **proporcional a $(x - x_0)^2$**.

> [!ejemplo] Error en la linealización del péndulo
> Para $\sin \theta \approx \theta$, el error es:
> $$E(\theta) = \sin \theta - \theta = -\frac{\theta^3}{6} - \frac{\theta^5}{120} - \dots$$
> 
> | $\theta$ (rad) | $\sin \theta$ | $\theta$ | Error relativo |
> |----------------|---------------|----------|----------------|
> | $0.1$ | $0.09983$ | $0.1$ | $0.17\%$ |
> | $0.2$ | $0.19867$ | $0.2$ | $0.67\%$ |
> | $0.5$ | $0.47943$ | $0.5$ | $4.3\%$ |
> | $1.0$ | $0.84147$ | $1.0$ | $18.8\%$ |
> 
> Regla práctica: $\theta < 0.5$ rad ($\approx 30^\circ$) para error $< 5\%$.

# Ejemplos de expansión de funciones no lineales

> [!ejemplo] Función seno
> $f(\theta) = \sin \theta$ alrededor de $\theta=0$:
> 
> $$f(0) = 0, \quad f'(0) = \cos 0 = 1$$
> 
> Aproximación lineal: $\sin \theta \approx \theta$
> 
> Expansión completa: $\sin \theta = \theta - \frac{\theta^3}{3!} + \frac{\theta^5}{5!} - \dots$

> [!ejemplo] Función coseno
> $f(\theta) = \cos \theta$ alrededor de $\theta=0$:
> 
> $$f(0) = 1, \quad f'(0) = -\sin 0 = 0$$
> 
> Aproximación lineal: $\cos \theta \approx 1$
> 
> (El primer término no lineal es de segundo orden: $\cos \theta = 1 - \frac{\theta^2}{2} + \dots$)

> [!ejemplo] Función exponencial
> $f(x) = e^{x}$ alrededor de $x=0$:
> 
> $$f(0) = 1, \quad f'(0) = 1$$
> 
> Aproximación lineal: $e^{x} \approx 1 + x$
> 
> Expansión completa: $e^{x} = 1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \dots$

> [!ejemplo] Función cuadrática (término no lineal puro)
> $f(x) = x^2$ alrededor de $x=0$:
> 
> $$f(0) = 0, \quad f'(0) = 0$$
> 
> Aproximación lineal: $x^2 \approx 0$ (¡pierde toda la dinámica!)
> 
> **Conclusión:** Para sistemas donde la dinámica depende de términos cuadráticos, la linealización alrededor de $x_0=0$ es **insuficiente**. Se necesita linealizar alrededor de otro punto o usar análisis no lineal.

# Ejemplo completo: péndulo

> [!ejemplo] Linealización paso a paso con Taylor
> Sistema: $\dot{x}_1 = x_2$, $\dot{x}_2 = -\frac{g}{l} \sin x_1$
> 
> Punto de equilibrio: $x_{10} = 0$, $x_{20} = 0$
> 
> **Expansión de $\sin x_1$:**
> $$\sin x_1 = x_1 - \frac{x_1^3}{6} + \frac{x_1^5}{120} - \dots$$
> 
> **Sustituir en $\dot{x}_2$:**
> $$\dot{x}_2 = -\frac{g}{l}\left(x_1 - \frac{x_1^3}{6} + \dots\right) = -\frac{g}{l}x_1 + \frac{g}{l}\frac{x_1^3}{6} + \dots$$
> 
> **Aproximación lineal:** despreciar $x_1^3$ y superiores
> $$\dot{x}_2 \approx -\frac{g}{l}x_1$$
> 
> **Sistema linealizado:**
> $$\dot{x}_1 = x_2$$
> $$\dot{x}_2 = -\frac{g}{l}x_1$$

# Relación con la linealización por Jacobianos

> [!info] Equivalencia
> El método de Jacobiano es exactamente la **aproximación de Taylor de primer orden**:
> 
> - $\frac{\partial f_i}{\partial x_j}$ son las derivadas parciales (coeficientes lineales)
> - Los términos de orden superior se desprecian
> - El punto de operación determina dónde se evalúan las derivadas

# Limitaciones

> [!warning]
> 1. La aproximación lineal **fracasa** si el sistema opera lejos del punto de equilibrio
> 2. **No captura bifurcaciones**: cambios cualitativos en la dinámica al variar parámetros
> 3. **No captura ciclos límite** (oscilaciones autosostenidas)
> 4. Para funciones con derivada nula en el punto de operación, el comportamiento dominante puede ser **cuadrático** (ej. $x^2$ cerca de $x=0$)