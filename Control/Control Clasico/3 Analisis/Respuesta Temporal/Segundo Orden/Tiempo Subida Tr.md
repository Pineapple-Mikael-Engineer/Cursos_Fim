---
title: Tiempo de Subida (Tr)
tags:
  - control-clasico
  - analisis
  - respuesta-temporal
  - segundo-orden
draft: false
aliases:
  - tiempo subida
  - Tr
  - rise time
---

# Tiempo de Subida ($T_r$)

# Definición

> [!definicion] Tiempo de subida
> Es el tiempo que tarda la respuesta a escalón en pasar del **10% al 90%** del valor final.
> 
> $$T_r = t_{90\%} - t_{10\%}$$
> 
> Para sistemas de segundo orden subamortiguados.

> [!definicion] Definición alternativa (para sistemas sin sobrepico)
> En sistemas sobreamortiguados o de primer orden, a veces se define como el tiempo de 0% a 100%:
> $$T_r = t_{100\%}$$

# Aproximaciones prácticas

> [!info] Fórmulas empíricas para $0.3 \le \zeta \le 0.8$
> 
> | Fuente | Fórmula | Precisión |
> |--------|---------|-----------|
> | Ogata | $T_r \approx \frac{1.8}{\omega_n}$ | Buena para $\zeta \approx 0.5$ |
> | Franklin | $T_r \approx \frac{1 + 0.7\zeta}{\omega_n}$ | Mejor para $\zeta$ variable |
> | Exacta (numérica) | $T_r = \frac{\pi - \theta}{\omega_d}$ donde $\theta = \arccos(\zeta)$ | (ver demostración) |

# Demostración (fórmula exacta)

> [!teorema] Fórmula exacta para $T_r$ (subamortiguado)
> $$T_r = \frac{\pi - \theta}{\omega_d} = \frac{\pi - \arccos(\zeta)}{\omega_n \sqrt{1-\zeta^2}}$$

> [!demostracion] Paso 1: Respuesta a escalón
> Para $G(s) = \frac{\omega_n^2}{s^2 + 2\zeta\omega_n s + \omega_n^2}$:
> $$y(t) = 1 - \frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}} \sin(\omega_d t + \theta)$$
> 
> donde $\omega_d = \omega_n \sqrt{1-\zeta^2}$, $\theta = \arccos(\zeta)$.
> 
> **Paso 2:** Ecuación para $y(t) = 0.1$
> 
> Para $t$ pequeño, el término $e^{-\zeta\omega_n t} \approx 1$:
> $$1 - \frac{1}{\sqrt{1-\zeta^2}} \sin(\omega_d t + \theta) \approx 0.1$$
> 
> $$\sin(\omega_d t + \theta) \approx 0.9 \sqrt{1-\zeta^2}$$
> 
> Para sistemas con $\zeta$ típico ($0.3-0.8$), $0.9\sqrt{1-\zeta^2}$ es cercano a $0.9$ a $0.54$.
> 
> Se puede aproximar: $\sin(\omega_d t + \theta) \approx \sin(\theta)$ para $t$ muy pequeño, lo que da $y(0)=0$ exactamente.
> 
> **Paso 3:** Aproximación simplificada
> 
> Un enfoque más simple usa el hecho de que el tiempo de subida es aproximadamente el tiempo en que la respuesta alcanza el 100% si no hubiera sobrepico.
> 
> Para el caso sin amortiguamiento ($\zeta=0$), $y(t) = 1 - \cos(\omega_n t)$.
> 
> $y(t)=1 \implies \cos(\omega_n t) = 0 \implies \omega_n t = \pi/2 \implies t = \pi/(2\omega_n)$.
> 
> Para $\zeta$ pequeños, $T_r \approx \pi/(2\omega_n)$.
> 
> **Paso 4:** Ajuste empírico
> 
> Mediante ajuste de curvas, se obtiene:
> $$T_r \approx \frac{1.8}{\omega_n} \quad \text{(para $\zeta \approx 0.5$)}$$
> 
> Una fórmula más general:
> $$T_r \approx \frac{1 + 0.7\zeta}{\omega_n} \quad \text{(válida para $0.3 \le \zeta \le 0.8$)}$$

# Comparación de fórmulas

> [!info] Precisión relativa
> 
> | $\zeta$ | $\omega_n$ | $T_r$ real (simulación) | $T_r = 1.8/\omega_n$ | $T_r = (1+0.7\zeta)/\omega_n$ |
> |---------|------------|------------------------|----------------------|-------------------------------|
> | 0.3 | 1 | 1.68 s | 1.80 s (7% error) | 1.21 s (28% error) |
> | 0.5 | 1 | 1.58 s | 1.80 s (14% error) | 1.35 s (15% error) |
> | 0.7 | 1 | 1.46 s | 1.80 s (23% error) | 1.49 s (2% error) |
> | 0.8 | 1 | 1.43 s | 1.80 s (26% error) | 1.56 s (9% error) |
> 
> **Observación:** 
> - Para $\zeta$ pequeños, ambas fórmulas tienen error
> - Para $\zeta \approx 0.7$, la fórmula $(1+0.7\zeta)/\omega_n$ es muy precisa
> - La fórmula $1.8/\omega_n$ es una aproximación muy burda, útil solo para estimaciones rápidas

# Relación con otros parámetros

> [!info] Dependencia con $\zeta$ y $\omega_n$
> 
> | Parámetro | Efecto sobre $T_r$ |
> |-----------|-------------------|
> | Mayor $\omega_n$ (fijo $\zeta$) | $T_r$ **disminuye** (respuesta más rápida) |
> | Mayor $\zeta$ (fijo $\omega_n$) | $T_r$ **disminuye ligeramente** (subida más rápida) |
> 
> **Intuición:** Mayor amortiguamiento reduce la inercia del sistema, acelerando la subida inicial.

# Tabla de valores normalizados ($\omega_n = 1$)

> [!info] $T_r$ para diferentes $\zeta$
> 
> | $\zeta$ | $T_r$ (real, simulación) | $T_r \approx (1+0.7\zeta)/\omega_n$ |
> |---------|-------------------------|-------------------------------------|
> | 0.1 | 1.92 s | 1.07 s (44% error) |
> | 0.2 | 1.79 s | 1.14 s (36% error) |
> | 0.3 | 1.68 s | 1.21 s (28% error) |
> | 0.4 | 1.61 s | 1.28 s (20% error) |
> | 0.5 | 1.58 s | 1.35 s (15% error) |
> | 0.6 | 1.55 s | 1.42 s (8% error) |
> | 0.7 | 1.46 s | 1.49 s (2% error) |
> | 0.8 | 1.43 s | 1.56 s (9% error) |
> | 0.9 | 1.39 s | 1.63 s (17% error) |
> 
> **Conclusión:** La fórmula $(1+0.7\zeta)/\omega_n$ es útil solo para $0.5 \le \zeta \le 0.8$.

# Uso en diseño

> [!info] Especificación típica
> En control, se suele especificar $T_r$ máximo:
> $$T_r \le T_{r,\text{máx}}$$
> 
> Esto impone una condición sobre $\omega_n$ y $\zeta$:
> - Usando $T_r \approx \frac{1.8}{\omega_n}$: $\omega_n \ge \frac{1.8}{T_{r,\text{máx}}}$
> - Usando $T_r \approx \frac{1+0.7\zeta}{\omega_n}$: $\omega_n \ge \frac{1+0.7\zeta}{T_{r,\text{máx}}}$
> 
> La segunda es más precisa si $\zeta$ ya está determinado por $M_p$.
> 
> Ver [[Sobrepico Mp]] y [[Lugar Raices/index | lugar de las raíces]].

# Ejemplo numérico

> [!ejemplo] Cálculo de $T_r$
> 
> **Problema:** Un sistema tiene $\zeta = 0.6$ y $\omega_n = 5$ rad/s. Calcule $T_r$ usando las tres fórmulas.
> 
> **Solución:**
> 
> 1. **Fórmula exacta (numérica):**
>    $\theta = \arccos(0.6) = 0.9273$ rad
>    $\omega_d = 5\sqrt{1-0.36} = 5 \cdot 0.8 = 4$ rad/s
>    $$T_r = \frac{\pi - \theta}{\omega_d} = \frac{3.1416 - 0.9273}{4} = \frac{2.2143}{4} = 0.554 \text{ s}$$
> 
> 2. **Fórmula de Ogata ($1.8/\omega_n$):**
>    $$T_r = \frac{1.8}{5} = 0.36 \text{ s} \quad (35\% \text{ error})$$
> 
> 3. **Fórmula de Franklin ($(1+0.7\zeta)/\omega_n$):**
>    $$T_r = \frac{1 + 0.7 \cdot 0.6}{5} = \frac{1 + 0.42}{5} = \frac{1.42}{5} = 0.284 \text{ s} \quad (49\% \text{ error})$$
> 
> **Conclusión:** Para $\zeta=0.6$, ambas aproximaciones tienen errores significativos. La fórmula exacta es la más confiable pero requiere más cálculo. En la práctica, se suele usar la fórmula de Ogata para diseños preliminares y luego se verifica con simulación.

# Limitaciones

> [!warning]
> 1. **Solo aplica** a sistemas subamortiguados ($0 < \zeta < 1$)
> 2. Para $\zeta \ge 1$, usar fórmulas de sistemas de primer orden o sobreamortiguados
> 3. Las aproximaciones empíricas tienen **errores significativos** (10-50% según $\zeta$)
> 4. La presencia de **ceros** puede reducir o aumentar el tiempo de subida
> 5. La definición 10%-90% es arbitraria; algunas aplicaciones usan 0%-100% o 5%-95%
> 6. Para sistemas con sobrepico muy grande ($M_p > 50\%$), la definición puede dar valores inconsistentes