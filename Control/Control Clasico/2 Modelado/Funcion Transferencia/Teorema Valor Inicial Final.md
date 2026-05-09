---
title: Teoremas del Valor Inicial y Final
tags:
  - control-clasico
  - teoria
  - analisis
draft: false
aliases:
  - TVI
  - TVF
  - valor final
  - valor inicial
---

# Teoremas del Valor Inicial y Final

# Definiciones

> [!definicion] Teorema del valor final (TVF)
> Si $f(t)$ es una función con transformada $F(s)$ y todos los polos de $sF(s)$ tienen parte real negativa (excepto posiblemente un polo simple en $s=0$), entonces:
> $$\lim_{t \to \infty} f(t) = \lim_{s \to 0} s F(s)$$

> [!definicion] Teorema del valor inicial (TVI)
> Si existe el límite $\lim_{t \to 0^+} f(t)$, entonces:
> $$f(0^+) = \lim_{t \to 0^+} f(t) = \lim_{s \to \infty} s F(s)$$
> 
> No requiere condiciones de estabilidad.

# Demostración del TVF

> [!teorema] Teorema del valor final
> Bajo las condiciones enunciadas, $\lim_{t \to \infty} f(t) = \lim_{s \to 0} sF(s)$.

> [!demostracion]
> **Paso 1:** Partir de la definición de la transformada de Laplace de la derivada:
> $$\mathcal{L}\left\{\frac{df}{dt}\right\} = \int_0^\infty \frac{df}{dt} e^{-st} dt = sF(s) - f(0^-)$$
> 
> **Paso 2:** Tomar límite cuando $s \to 0^+$:
> $$\lim_{s \to 0} \int_0^\infty \frac{df}{dt} e^{-st} dt = \lim_{s \to 0} [sF(s) - f(0^-)]$$
> 
> **Paso 3:** Intercambiar límite e integral (válido por convergencia uniforme, garantizada por las hipótesis):
> $$\int_0^\infty \frac{df}{dt} \left( \lim_{s \to 0} e^{-st} \right) dt = \int_0^\infty \frac{df}{dt} dt = \lim_{t \to \infty} f(t) - f(0^-)$$
> 
> **Paso 4:** Igualar:
> $$\lim_{t \to \infty} f(t) - f(0^-) = \lim_{s \to 0} sF(s) - f(0^-)$$
> 
> **Paso 5:** Cancelar $f(0^-)$:
> $$\lim_{t \to \infty} f(t) = \lim_{s \to 0} sF(s)$$

# Demostración del TVI

> [!teorema] Teorema del valor inicial
> $$f(0^+) = \lim_{s \to \infty} sF(s)$$

> [!demostracion]
> **Paso 1:** De la misma identidad:
> $$\int_0^\infty \frac{df}{dt} e^{-st} dt = sF(s) - f(0^-)$$
> 
> **Paso 2:** Tomar límite cuando $s \to \infty$:
> $$\lim_{s \to \infty} \int_0^\infty \frac{df}{dt} e^{-st} dt = \lim_{s \to \infty} [sF(s) - f(0^-)]$$
> 
> **Paso 3:** Cuando $s \to \infty$, $e^{-st} \to 0$ para todo $t > 0$:
> $$\lim_{s \to \infty} \int_0^\infty \frac{df}{dt} e^{-st} dt = 0$$
> 
> **Paso 4:** Por lo tanto:
> $$0 = \lim_{s \to \infty} sF(s) - f(0^-)$$
> 
> **Paso 5:** Como $f(0^-) = f(0^+)$ para funciones sin discontinuidad en el origen (o se define adecuadamente):
> $$f(0^+) = \lim_{s \to \infty} sF(s)$$

# Ejemplos de TVF

> [!ejemplo] Sistema estable de primer orden
> $$F(s) = \frac{2}{s+1} \cdot \frac{1}{s} = \frac{2}{s(s+1)}$$
> 
> $sF(s) = \frac{2}{s+1}$ tiene polo en $s=-1$ (parte real negativa). Aplicando TVF:
> $$\lim_{t \to \infty} f(t) = \lim_{s \to 0} \frac{2}{s+1} = 2$$
> 
> Verificación: $f(t) = 2(1 - e^{-t}) \to 2$.

> [!ejemplo] Sistema con polo en el origen
> $$F(s) = \frac{1}{s^2}$$
> 
> $sF(s) = \frac{1}{s}$ tiene polo en $s=0$ (viola hipótesis de TVF porque el polo en $0$ no es simple en $sF(s)$? En realidad es simple pero el enunciado requiere que sea el único y el resto con $\Re<0$; aquí no hay resto. El TVF da:
> $$\lim_{t \to \infty} f(t) = \lim_{s \to 0} s \cdot \frac{1}{s^2} = \lim_{s \to 0} \frac{1}{s} = \infty$$
> 
> Esto es correcto: $f(t) = t \to \infty$.

> [!ejemplo] Sistema inestable
> $$F(s) = \frac{1}{s-1} \cdot \frac{1}{s} = \frac{1}{s(s-1)}$$
> 
> $sF(s) = \frac{1}{s-1}$ tiene polo en $s=1$ (parte real positiva). **No aplicar TVF.** La respuesta crece exponencialmente, no hay límite finito.

# Ejemplos de TVI

> [!ejemplo] Sistema con discontinuidad inicial
> $$F(s) = \frac{2}{s+1}$$
> 
> $$\lim_{s \to \infty} s \cdot \frac{2}{s+1} = \lim_{s \to \infty} \frac{2s}{s+1} = 2$$
> 
> Verificación: $f(t) = 2e^{-t}$, $f(0^+) = 2$.

> [!ejemplo] Función con salto
> $$F(s) = \frac{1 - e^{-sT}}{s}$$
> 
> $$\lim_{s \to \infty} s \cdot \frac{1 - e^{-sT}}{s} = \lim_{s \to \infty} (1 - e^{-sT}) = 1$$
> 
> La función es un pulso de altura 1 y duración $T$; $f(0^+)=1$.

# Condiciones de validez

> [!warning] TVF
> No aplicar si:
> - $sF(s)$ tiene polos con parte real $\ge 0$ excepto posiblemente un polo simple en $s=0$
> - El sistema es inestable
> - Hay polos en eje imaginario (excepto simple en $0$)
> 
> Ejemplo donde **falla**:
> $$F(s) = \frac{1}{s^2 + \omega^2} \quad (\text{seno})$$
> 
> $sF(s) = \frac{s}{s^2 + \omega^2}$ tiene polos $s = \pm j\omega$ (parte real cero, no simples en $sF(s)$? Son simples pero el TVF requiere que todos los polos excepto posible $s=0$ tengan $\Re<0$). El TVF daría $\lim_{s \to 0} \frac{s}{s^2+\omega^2} = 0$, pero $\lim_{t \to \infty} \sin(\omega t)$ no existe.

> [!warning] TVI
> - El límite $\lim_{s \to \infty} sF(s)$ debe existir
> - Si $f(t)$ tiene un impulso en $t=0$, el TVI da el área del impulso

# Aplicación en control

> [!info] Uso típico
> - **TVF:** calcular error estacionario $e_{ss} = \lim_{s \to 0} sE(s)$
> - **TVI:** verificar condiciones iniciales de sistemas
> 
> Ver [[Ganancia Estatica | ganancia estática]] y [[Error Estacionario/index | error estacionario]].

> [!ejemplo] Error estacionario a escalón
> $$E(s) = \frac{1}{1+G(s)} \cdot \frac{1}{s}$$
> 
> $$e_{ss} = \lim_{s \to 0} sE(s) = \lim_{s \to 0} \frac{1}{1+G(s)} = \frac{1}{1+G(0)}$$
> 
> Válido si el lazo cerrado es estable.

# Contraejemplos famosos

> [!ejemplo] TVF no aplica (seno)
> $$f(t) = \sin(t) \implies F(s) = \frac{1}{s^2+1}$$
> 
> $sF(s) = \frac{s}{s^2+1}$, polos $s = \pm j$. TVF daría $0$, pero no hay límite cuando $t \to \infty$.

> [!ejemplo] TVF no aplica (exponencial creciente)
> $$f(t) = e^{t} \implies F(s) = \frac{1}{s-1}$$
> 
> $sF(s) = \frac{s}{s-1}$, polo en $s=1$ (parte real positiva). TVF daría $\lim_{s \to 0} \frac{s}{s-1} = 0$, pero $f(t) \to \infty$.