---
title: "Convolución"
tags:
  - control-clasico
  - sistemas-lineales
  - representacion-temporal
draft: false
aliases:
  - Convolution
  - Integral de Convolución
  - Producto de Convolución
---

# Convolución

> [!definicion] Definición Formal
> Dadas dos funciones $f(t)$ y $g(t)$, su **convolución** $(f * g)(t)$ se define como:
> $$
> (f * g)(t) = \int_{-\infty}^{\infty} f(\tau) g(t - \tau) d\tau = \int_{-\infty}^{\infty} f(t - \tau) g(\tau) d\tau
> $$
> La segunda igualdad se obtiene mediante el cambio de variable $\sigma = t - \tau$.

---

## Propiedades de la Convolución

> [!proposicion] Conmutatividad
> $$
> f * g = g * f
> $$

> [!proposicion] Asociatividad
> $$
> (f * g) * h = f * (g * h)
> $$

> [!proposicion] Distributividad
> $$
> f * (g + h) = f * g + f * h
> $$

> [!proposicion] Elemento Identidad (Delta de Dirac)
> $$
> f * \delta = \delta * f = f
> $$
> donde $\delta(t)$ es la [[Delta de Dirac]].

> [!proposicion] Desplazamiento Temporal
> Si $g_\tau(t) = g(t - \tau)$, entonces:
> $$
> (f * g_\tau)(t) = (f * g)(t - \tau)
> $$

---

## Convolución en Sistemas LTI

> [!teorema] Representación Entrada-Salida
> Para un sistema [[Sistemas LTI]] con respuesta al impulso $h(t)$ y entrada $u(t)$, la salida $y(t)$ está dada por:
> $$
> y(t) = (u * h)(t) = \int_{-\infty}^{\infty} u(\tau) h(t - \tau) d\tau
> $$

> [!demostracion]
> Por la propiedad de muestreo de la [[Delta de Dirac]]:
> $$
> u(t) = \int_{-\infty}^{\infty} u(\tau) \delta(t - \tau) d\tau
> $$
> 
> Aplicando el operador $\mathcal{H}$ del sistema [[Sistemas LTI]]:
> $$
> y(t) = \mathcal{H}[u(t)] = \mathcal{H}\left[\int_{-\infty}^{\infty} u(\tau) \delta(t - \tau) d\tau\right]
> $$
> 
> Por **linealidad**:
> $$
> y(t) = \int_{-\infty}^{\infty} u(\tau) \mathcal{H}[\delta(t - \tau)] d\tau
> $$
> 
> Por **invarianza temporal**: $\mathcal{H}[\delta(t - \tau)] = h(t - \tau)$. Por lo tanto:
> $$
> y(t) = \int_{-\infty}^{\infty} u(\tau) h(t - \tau) d\tau
> $$
> $\square$

---

## Convolución en el Dominio de Laplace

> [!teorema] Teorema de Convolución en Laplace
> La transformada de Laplace de una convolución es el producto de las transformadas individuales:
> $$
> \mathcal{L}\{(f * g)(t)\} = F(s) \cdot G(s)
> $$
> donde $F(s) = \mathcal{L}\{f(t)\}$ y $G(s) = \mathcal{L}\{g(t)\}$, siempre que las transformadas existan.

> [!demostracion]
> Por definición:
> $$
> \mathcal{L}\{(f * g)(t)\} = \int_{0^-}^{\infty} \left[ \int_{0^-}^{\infty} f(\tau) g(t - \tau) d\tau \right] e^{-st} dt
> $$
> 
> Invirtiendo el orden de integración (Teorema de Fubini):
> $$
> = \int_{0^-}^{\infty} f(\tau) \left[ \int_{0^-}^{\infty} g(t - \tau) e^{-st} dt \right] d\tau
> $$
> 
> Cambio de variable $\sigma = t - \tau$ en la integral interna:
> $$
> = \int_{0^-}^{\infty} f(\tau) \left[ \int_{0^-}^{\infty} g(\sigma) e^{-s(\sigma + \tau)} d\sigma \right] d\tau
> $$
> 
> Separando exponenciales:
> $$
> = \int_{0^-}^{\infty} f(\tau) e^{-s\tau} \left[ \int_{0^-}^{\infty} g(\sigma) e^{-s\sigma} d\sigma \right] d\tau
> $$
> 
> La integral entre corchetes es $G(s)$, independiente de $\tau$:
> $$
> = \left[ \int_{0^-}^{\infty} f(\tau) e^{-s\tau} d\tau \right] G(s) = F(s) \cdot G(s)
> $$
> $\square$

> [!corolario] Aplicación a Sistemas LTI
> Para un sistema [[Sistemas LTI]] con respuesta al impulso $h(t)$ y función de transferencia $G(s)$:
> $$
> Y(s) = \mathcal{L}\{y(t)\} = \mathcal{L}\{(u * h)(t)\} = U(s) \cdot H(s) = U(s) \cdot G(s)
> $$
> Esto justifica la relación $Y(s) = G(s) U(s)$.

---

## Ejemplos de Cálculo

> [!ejemplo] Convolución de funciones exponenciales
> Sean $f(t) = e^{-at} \mathbf{1}(t)$ y $g(t) = e^{-bt} \mathbf{1}(t)$ con $a \neq b$:
> $$
> (f * g)(t) = \int_{0}^{t} e^{-a\tau} e^{-b(t-\tau)} d\tau = e^{-bt} \int_{0}^{t} e^{-(a-b)\tau} d\tau
> $$
> $$
> = e^{-bt} \left[ \frac{e^{-(a-b)\tau}}{-(a-b)} \right]_{0}^{t} = e^{-bt} \cdot \frac{1 - e^{-(a-b)t}}{a-b}
> $$
> $$
> = \frac{e^{-bt} - e^{-at}}{a-b} \cdot \mathbf{1}(t)
> $$

> [!ejemplo] Convolución con escalón
> Sea $f(t) = e^{-at} \mathbf{1}(t)$ y $g(t) = \mathbf{1}(t)$:
> $$
> (f * g)(t) = \int_{0}^{t} e^{-a\tau} d\tau = \left[ -\frac{1}{a} e^{-a\tau} \right]_{0}^{t} = \frac{1 - e^{-at}}{a} \cdot \mathbf{1}(t)
> $$

> [!ejemplo] Convolución de dos rectángulos
> Sean $f(t) = \text{rect}(t/T)$ y $g(t) = \text{rect}(t/T)$:
> - El resultado es una función triangular
> - Para $|t| \le T$: $(f * g)(t) = T - |t|$
> - Para $|t| > T$: $(f * g)(t) = 0$

---

## Convolución en Tiempo Discreto

> [!definicion] Convolución Discreta
> Para secuencias $f[n]$ y $g[n]$, la convolución discreta se define como:
> $$
> (f * g)[n] = \sum_{k=-\infty}^{\infty} f[k] \, g[n-k] = \sum_{k=-\infty}^{\infty} f[n-k] \, g[k]
> $$

> [!proposicion] Transformada Z
> La transformada Z de una convolución discreta es el producto de las transformadas individuales:
> $$
> \mathcal{Z}\{(f * g)[n]\} = F(z) \cdot G(z)
> $$

> [!ejemplo] Convolución discreta
> Sean $f[n] = a^n \mathbf{1}[n]$ y $g[n] = b^n \mathbf{1}[n]$ con $a \neq b$:
> $$
> (f * g)[n] = \sum_{k=0}^{n} a^k b^{n-k} = b^n \sum_{k=0}^{n} \left(\frac{a}{b}\right)^k = b^n \cdot \frac{1 - (a/b)^{n+1}}{1 - a/b} = \frac{b^{n+1} - a^{n+1}}{b - a} \cdot \mathbf{1}[n]
> $$

---

## Relación con la Correlación

> [!definicion] Correlación Cruzada
> La correlación cruzada entre $f(t)$ y $g(t)$ se define como:
> $$
> (f \star g)(t) = \int_{-\infty}^{\infty} f^*(\tau) g(t + \tau) d\tau
> $$
> donde $f^*$ denota el conjugado complejo. A diferencia de la convolución, la correlación no es conmutativa y no involucra inversión temporal de una de las funciones.

La correlación se utiliza en procesamiento de señales para medir similitud entre señales, mientras que la convolución modela la respuesta de sistemas LTI.