---
title: "Respuesta al Impulso"
tags:
  - control-clasico
  - sistemas-lineales
  - representacion-temporal
draft: false
aliases:
  - Impulse Response
  - h(t)
  - Kernel de Convolución
---

# Respuesta al Impulso $h(t)$

> [!definicion] Definición Formal
> Sea un sistema [[Sistemas LTI]] con entrada $u(t)$ y salida $y(t)$. La **respuesta al impulso** $h(t)$ es la salida del sistema cuando la entrada es la [[Delta de Dirac]] $\delta(t)$, con **condiciones iniciales nulas**:
> $$
> h(t) = \mathcal{H}[\delta(t)]
> $$
> donde $\mathcal{H}$ es el operador del sistema.

---

## Relación con la Función de Transferencia

> [!teorema]
> Para un sistema [[Sistemas LTI]] con condiciones iniciales nulas, sea $G(s)$ la función de transferencia definida como $G(s) = Y(s)/U(s)$ para **cualquier** entrada $u(t)$. 
> 
> Si la entrada es particularmente $u(t) = \delta(t)$, entonces la salida es $y(t) = h(t)$ por definición. En este caso particular, se cumple:
> $$
> G_\delta(s) = \frac{\mathcal{L}\{h(t)\}}{\mathcal{L}\{\delta(t)\}} = \frac{\mathcal{L}\{h(t)\}}{1} = \mathcal{L}\{h(t)\}
> $$
> 
> Pero dado que $G(s)$ es la misma función de transferencia para cualquier entrada (propiedad de los sistemas LTI), se tiene $G_\delta(s) = G(s)$. Por lo tanto:
> $$
> G(s) = \mathcal{L}\{h(t)\} \quad \Longleftrightarrow \quad h(t) = \mathcal{L}^{-1}\{G(s)\}
> $$

> [!info]
> **Distinción clave:**
> - $G(s)$ es la función de transferencia **general** definida para toda entrada
> - $G_\delta(s)$ es el **caso particular** donde $u(t)=\delta(t)$, que resulta igual a $G(s)$ por la invarianza del sistema
> 
> La igualdad $G(s) = \mathcal{L}\{h(t)\}$ es una **consecuencia** de la definición general, no una definición alternativa.

> [!ejemplo] Uso práctico
> Si se desea encontrar $h(t)$ para un sistema dado, se puede:
> 1. Calcular $G(s) = Y(s)/U(s)$ con cualquier entrada (ej. escalón)
> 2. Luego $h(t) = \mathcal{L}^{-1}\{G(s)\}$
> 
> No es necesario excitar el sistema con un impulso real (físicamente difícil de generar).

> [!warning]
> Esta relación solo es válida para sistemas LTI. Para sistemas no lineales o variantes, la función de transferencia no está definida de manera única.

---

## Propiedad Fundamental: Convolución

> [!teorema] Representación Entrada-Salida
> Para cualquier entrada $u(t)$ en un sistema [[Sistemas LTI]], la salida $y(t)$ está dada por la integral de convolución:
> $$
> y(t) = (u * h)(t) = \int_{-\infty}^{\infty} u(\tau) h(t - \tau) d\tau = \int_{-\infty}^{\infty} h(\tau) u(t - \tau) d\tau
> $$

> [!demostracion]
> Por la propiedad de muestreo de la [[Delta de Dirac]], cualquier entrada puede escribirse como:
> $$
> u(t) = \int_{-\infty}^{\infty} u(\tau) \delta(t - \tau) d\tau
> $$
> Aplicando el operador $\mathcal{H}$ del sistema [[Sistemas LTI]]:
> $$
> y(t) = \mathcal{H}[u(t)] = \mathcal{H}\left[\int_{-\infty}^{\infty} u(\tau) \delta(t - \tau) d\tau\right]
> $$
> Por **linealidad** (la integral es un caso continuo de superposición):
> $$
> y(t) = \int_{-\infty}^{\infty} u(\tau) \mathcal{H}[\delta(t - \tau)] d\tau
> $$
> Por **invarianza temporal**: $\mathcal{H}[\delta(t - \tau)] = h(t - \tau)$. Sustituyendo:
> $$
> y(t) = \int_{-\infty}^{\infty} u(\tau) h(t - \tau) d\tau
> $$
> $\square$

---

## Cálculo de $h(t)$ desde la Ecuación Diferencial

> [!teoria] Método Directo
> Dada la ecuación diferencial de un sistema [[Sistemas LTI]] de orden $n$:
> $$
> a_n \frac{d^n y}{dt^n} + \dots + a_0 y = b_m \frac{d^m u}{dt^m} + \dots + b_0 u
> $$
> Para encontrar $h(t)$:
> 1. Reemplazar $u(t) = \delta(t)$ e $y(t) = h(t)$
> 2. Resolver para $t > 0$ donde $\delta(t) = 0$, obteniendo la solución homogénea
> 3. Determinar las condiciones iniciales en $t=0^+$ mediante balance de singularidades

> [!ejemplo] Sistema de primer orden
> Sea $\dot{y}(t) + a y(t) = b u(t)$. Para $u(t) = \delta(t)$:
> - Para $t > 0$: $\dot{h} + a h = 0$ $\Rightarrow$ $h(t) = C e^{-at}$
> - Integrando la ecuación desde $t=0^-$ a $t=0^+$:
>   $\int_{0^-}^{0^+} \dot{h} dt + a\int_{0^-}^{0^+} h dt = b\int_{0^-}^{0^+} \delta(t) dt$
>   $h(0^+) - h(0^-) + 0 = b \cdot 1$
> - Con condiciones iniciales nulas: $h(0^-) = 0$ $\Rightarrow$ $h(0^+) = b$
> - Evaluando $h(0^+) = C e^{0} = b$ $\Rightarrow$ $C = b$
> - Por lo tanto: $h(t) = b e^{-at} \mathbf{1}(t)$

> [!ejemplo] Sistema de segundo orden subamortiguado
> Sea $\ddot{y} + 2\zeta\omega_n\dot{y} + \omega_n^2 y = \omega_n^2 u$ (forma estándar).
> Para $u(t) = \delta(t)$:
> - Transformada de Laplace: $(s^2 + 2\zeta\omega_n s + \omega_n^2) H(s) = \omega_n^2 \cdot 1$
> - Despejando: $H(s) = \dfrac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$
> - Para $0 < \zeta < 1$ (subamortiguado):
>   $h(t) = \dfrac{\omega_n}{\sqrt{1-\zeta^2}} e^{-\zeta\omega_n t} \sin\left(\omega_n\sqrt{1-\zeta^2} \, t\right) \mathbf{1}(t)$

---

## Propiedades de $h(t)$

> [!proposicion] Causalidad
> Un sistema [[Sistemas LTI]] es **causal** si y solo si:
> $$
> h(t) = 0 \quad \forall t < 0
> $$
> Esto significa que la salida no puede depender de entradas futuras.

> [!proposicion] Estabilidad BIBO
> Un sistema [[Sistemas LTI]] es [[Estabilidad BIBO]] si y solo si:
> $$
> \int_{-\infty}^{\infty} |h(t)| \, dt < \infty
> $$
> Es decir, $h(t)$ es absolutamente integrable.

> [!ejemplo] Verificación de estabilidad
> | Sistema | $h(t)$ | $\int |h| dt$ | ¿Estable? |
> |---------|--------|---------------|------------|
> | RC pasabajos | $\frac{1}{RC}e^{-t/RC}\mathbf{1}(t)$ | $1$ | Sí |
> | Integrador | $\mathbf{1}(t)$ | $\infty$ | No |
> | Oscilador puro | $\sin(\omega_0 t)\mathbf{1}(t)$ | $\infty$ | No (marginal) |

---

## Respuesta al Impulso en Sistemas Discretos

> [!definicion] Caso Discreto
> Para sistemas discretos LTI, la respuesta al impulso $h[n]$ es la salida ante $u[n] = \delta[n]$ (delta de Kronecker). La convolución discreta es:
> $$
> y[n] = \sum_{k=-\infty}^{\infty} u[k] \, h[n-k] = (u * h)[n]
> $$
> y la [[Función de Transferencia]] en $z$ es $H(z) = \mathcal{Z}\{h[n]\}$.