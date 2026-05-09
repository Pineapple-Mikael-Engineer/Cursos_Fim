---
title: Impulso Unitario
tags:
  - control-clasico
  - señales-prueba
  - analisis
draft: false
aliases:
  - impulso
  - delta
  - dirac
  - funcion delta
---

# Impulso Unitario

# Definición

> [!definicion] Impulso unitario $\delta(t)$ (Delta de Dirac)
> No es una función en sentido clásico, sino una **distribución** definida por:
> 
> $$\delta(t) = 0 \quad \text{para } t \neq 0$$
> $$\int_{-\infty}^{\infty} \delta(t) dt = 1$$
> 
> Y la propiedad de muestreo:
> $$\int_{-\infty}^{\infty} f(t) \delta(t - a) dt = f(a)$$

> [!definicion] Propiedad de muestreo (sifting property)
> $$\int_{-\infty}^{\infty} f(t) \delta(t - a) dt = f(a)$$
> 
> En particular, para $a=0$: $\int_{-\infty}^{\infty} f(t) \delta(t) dt = f(0)$

# Relación con el escalón

> [!info] El impulso es la derivada generalizada del escalón
> $$\delta(t) = \frac{d}{dt} u(t)$$
> $$u(t) = \int_{-\infty}^{t} \delta(\tau) d\tau$$

> [!demostracion]
> Para cualquier función de prueba $f(t)$:
> 
> $$\int_{-\infty}^{\infty} f(t) \delta(t) dt = f(0)$$
> 
> Por otro lado:
> $$\int_{-\infty}^{\infty} f(t) \frac{d}{dt} u(t) dt = -\int_{-\infty}^{\infty} f'(t) u(t) dt = -\int_{0}^{\infty} f'(t) dt = f(0) - f(\infty)$$
> 
> Para funciones que decaen en infinito ($f(\infty)=0$), se cumple la igualdad.

# Transformada de Laplace

> [!teorema] Transformada del impulso unitario
> $$\mathcal{L}\{\delta(t)\} = 1, \quad \text{para todo } s$$

> [!demostracion]
> Por definición de la transformada unilateral:
> $$\mathcal{L}\{\delta(t)\} = \int_{0^-}^{\infty} \delta(t) e^{-st} dt$$
> 
> Por la propiedad de muestreo con $a=0$ y $f(t) = e^{-st}$:
> $$\int_{0^-}^{\infty} \delta(t) e^{-st} dt = e^{-s \cdot 0} = 1$$

> [!teorema] Transformada del impulso desplazado
> $$\mathcal{L}\{\delta(t - a)\} = e^{-as}, \quad a \ge 0$$

> [!demostracion]
> Por [[Propiedades | propiedad de desplazamiento temporal]]:
> $$\mathcal{L}\{\delta(t - a)\} = e^{-as} \cdot 1 = e^{-as}$$

# Relación con otras señales

> [!info] Derivadas e integrales
> 
> **Derivada:** $\frac{d}{dt} \delta(t)$ no es una función común (doblete)
> 
> **Integral:** $\int_{-\infty}^{t} \delta(\tau) d\tau = u(t)$ ([[Escalon]])

> [!info] Otras relaciones
> - [[Escalon]]: $u(t) = \int_{-\infty}^{t} \delta(\tau) d\tau$
> - [[Rampa]]: $r(t) = \int_{-\infty}^{t} \int_{-\infty}^{\tau} \delta(\sigma) d\sigma d\tau$
> - [[Parabola]]: $p(t) = \int_{-\infty}^{t} \int_{-\infty}^{\tau} \int_{-\infty}^{\sigma} \delta(\lambda) d\lambda d\sigma d\tau$
> - **Pulso rectangular estrecho:** $\delta(t) = \lim_{\epsilon \to 0} \frac{1}{\epsilon} \left[ u(t) - u(t - \epsilon) \right]$

# Respuesta de sistemas al impulso

> [!info] Respuesta impulsional $h(t)$
> Para un sistema con función transferencia $G(s)$, la respuesta al impulso es:
> $$h(t) = \mathcal{L}^{-1}\{G(s)\}$$

> [!teorema] Relación fundamental
> $$Y(s) = G(s) U(s) \quad \xrightarrow{u(t)=\delta(t)} \quad Y(s) = G(s) \cdot 1 = G(s)$$
> 
> Por lo tanto:
> $$h(t) = \mathcal{L}^{-1}\{G(s)\} = \text{respuesta al impulso}$$

> [!ejemplo] Sistema de primer orden
> $$G(s) = \frac{K}{\tau s + 1}$$
> 
> $$h(t) = \frac{K}{\tau} e^{-t/\tau}, \quad t \ge 0$$
> 
> Ver [[Primer Orden]].

> [!ejemplo] Sistema de segundo orden (subamortiguado)
> $$G(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}, \quad 0 < \zeta < 1$$
> 
> $$h(t) = \frac{\omega_n}{\sqrt{1-\zeta^2}} e^{-\zeta\omega_n t} \sin(\omega_d t), \quad t \ge 0$$
> 
> donde $\omega_d = \omega_n\sqrt{1-\zeta^2}$
> 
> Ver [[Segundo Orden/index]].

# Propiedades de la respuesta impulsional

> [!info] Propiedades importantes
> 1. **Causalidad:** $h(t) = 0$ para $t < 0$ (sistema causal)
> 2. **Estabilidad BIBO:** $\int_0^{\infty} |h(t)| dt < \infty$
> 3. **Convolución:** $y(t) = (h * u)(t) = \int_0^t h(\tau) u(t - \tau) d\tau$
> 4. **Relación con escalón:** $h(t) = \frac{d}{dt} y_{\text{escalón}}(t)$

> [!demostracion] Relación con escalón
> La respuesta al escalón $y_{\text{escalón}}(t) = \int_0^t h(\tau) d\tau$
> 
> Derivando ambos lados: $\frac{d}{dt} y_{\text{escalón}}(t) = h(t)$

# Identificación de sistemas mediante impulso

> [!info] En teoría...
> Si se aplica un impulso ideal a un sistema, la salida es directamente $h(t)$.
> 
> **Problema:** El impulso ideal no es físicamente realizable (amplitud infinita, duración cero).

> [!ejemplo] Aproximación práctica del impulso
> En la práctica, se usa un **pulso corto** de área 1:
> $$p(t) = \frac{1}{\epsilon} \left[ u(t) - u(t - \epsilon) \right]$$
> 
> Para $\epsilon$ suficientemente pequeño (comparado con la dinámica del sistema), $p(t) \approx \delta(t)$.

# Convolución y función transferencia

> [!teorema] Teorema de convolución
> Para cualquier entrada $u(t)$:
> $$y(t) = (h * u)(t) = \int_0^t h(\tau) u(t - \tau) d\tau$$
> 
> En Laplace: $Y(s) = H(s) U(s) = G(s) U(s)$
> 
> Ver [[Convolucion]].

# Uso en control

> [!info] ¿Por qué el impulso?
> 1. **Caracterización completa del sistema:** $h(t)$ contiene toda la información del sistema LTI
> 2. **Relación con función transferencia:** $G(s) = \mathcal{L}\{h(t)\}$
> 3. **Base de la convolución:** Cualquier entrada se puede representar como superposición de impulsos
> 4. **Análisis de sistemas:** La estabilidad BIBO se verifica con $\int |h(t)| dt < \infty$
> 5. **Relación con escalón:** $h(t)$ es la derivada de la respuesta al escalón

# Comparación con otras señales

> [!info] Señales de prueba y su propósito
> 
> | Señal | Transformada | Uso principal |
> |--------|--------------|---------------|
> | [[Impulso]] $\delta(t)$ | $1$ | Obtener $h(t)$, caracterización completa |
> | [[Escalon]] $u(t)$ | $1/s$ | Evaluar respuesta transitoria y $e_{ss}$ |
> | [[Rampa]] $t \cdot u(t)$ | $1/s^2$ | Evaluar $K_v$ (error de velocidad) |
> | [[Parabola]] $\frac{t^2}{2} u(t)$ | $1/s^3$ | Evaluar $K_a$ (error de aceleración) |

> [!info] Relación entre respuestas
> $$h(t) \xrightarrow{\text{integral}} y_{\text{escalón}}(t) \xrightarrow{\text{integral}} y_{\text{rampa}}(t) \xrightarrow{\text{integral}} y_{\text{parábola}}(t)$$

# Limitaciones

> [!warning]
> 1. **No es físicamente realizable:** Impulso ideal requiere amplitud infinita
> 2. **Aproximación práctica:** Se usa un pulso corto, pero nunca es exacto
> 3. **Sensibilidad al ruido:** La derivación numérica de la respuesta al escalón amplifica ruido
> 4. **Sistemas con integradores:** $h(t)$ no tiende a cero (ej. $h(t) = 1$ para sistema $\dot{y}=u$)