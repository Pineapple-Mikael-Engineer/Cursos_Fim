---
title: Tiempo de Subida (Tr)
order: 5
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

> [!definicion]
> Tiempo que tarda la respuesta a escalón en pasar del **10% al 90%** del valor final (en sistemas subamortiguados). Fórmula exacta y aproximaciones empíricas:
> $$T_r=\frac{\pi-\theta}{\omega_d}=\frac{\pi-\arccos\zeta}{\omega_n\sqrt{1-\zeta^2}},\qquad T_r\approx\frac{1.8}{\omega_n}\;(\zeta\approx0.5),\qquad T_r\approx\frac{1+0.7\zeta}{\omega_n}.$$
> En sistemas sin sobrepico (sobreamortiguados / primer orden) a veces se define $0\%\to100\%$: $T_r=t_{100\%}$.

> [!info]
> Métrica de [[Segundo Orden/index | segundo orden]] derivada de la [[Formula General | respuesta $y(t)$]]; mide la **rapidez inicial**, no el régimen permanente ([[Tiempo Establecimiento Ts | $T_s$]]) ni el sobrepico ([[Sobrepico Mp | $M_p$]]). Sus aproximaciones empíricas son menos fiables que las de $T_p$ o $T_s$.

---

## Ejemplo

> [!ejemplo] $T_r$ por las tres fórmulas
> **Problema.** Un sistema tiene $\zeta=0.6$ y $\omega_n=5$ rad/s. Calcular $T_r$ con la fórmula exacta y las dos aproximaciones.
>
> **Paso 1 — Parámetros:**
> $$\theta=\arccos0.6=0.9273\ \text{rad},\qquad \omega_d=5\sqrt{1-0.36}=5(0.8)=4\ \text{rad/s}.$$
>
> **Paso 2 — Fórmula exacta:**
> $$T_r=\frac{\pi-\theta}{\omega_d}=\frac{3.1416-0.9273}{4}=\frac{2.2143}{4}=0.554\ \text{s}.$$
>
> **Paso 3 — Ogata ($1.8/\omega_n$):**
> $$T_r=\frac{1.8}{5}=0.36\ \text{s}\quad(\sim35\%\ \text{de error}).$$
>
> **Paso 4 — Franklin ($(1+0.7\zeta)/\omega_n$):**
> $$T_r=\frac{1+0.7(0.6)}{5}=\frac{1.42}{5}=0.284\ \text{s}\quad(\sim49\%\ \text{de error}).$$
>
> **Conclusión.** Para $\zeta=0.6$ ambas aproximaciones se quedan cortas; la exacta $0.554$ s es la fiable. En la práctica se usan las empíricas para diseños preliminares y se verifica con simulación.

> [!ejemplo] Tiempo de subida
> ![[resp_tiempo_subida_tr.svg|560]]
>
> $t_r$ es el tiempo en pasar del $10\%$ al $90\%$ del valor final en la primera subida.

---

## Demostración

> [!teorema] Fórmula exacta de $T_r$ (subamortiguado, $0\%\to100\%$)
> $$T_r=\frac{\pi-\theta}{\omega_d}=\frac{\pi-\arccos\zeta}{\omega_n\sqrt{1-\zeta^2}}.$$

> [!demostracion]
> **Paso 1 — Respuesta a escalón.** Para $G(s)=\frac{\omega_n^2}{s^2+2\zeta\omega_n s+\omega_n^2}$:
> $$y(t)=1-\frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}}\sin(\omega_d t+\theta),\qquad \theta=\arccos\zeta.$$
>
> **Paso 2 — Primer cruce de $y=1$.** La respuesta alcanza el valor final ($100\%$) por primera vez cuando el término oscilatorio se anula:
> $$\frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}}\sin(\omega_d t+\theta)=0\;\Rightarrow\;\sin(\omega_d t+\theta)=0\;\Rightarrow\;\omega_d t+\theta=\pi.$$
> (La exponencial nunca se anula, así que el factor que importa es el seno.)
>
> **Paso 3 — Despejar:**
> $$\omega_d t=\pi-\theta\;\Rightarrow\;T_r=\frac{\pi-\theta}{\omega_d}=\frac{\pi-\arccos\zeta}{\omega_n\sqrt{1-\zeta^2}}.$$
>
> **Paso 4 — Aproximaciones empíricas.** Para la definición $10\%\to90\%$ no hay forma cerrada; por ajuste de curvas en $0.3\le\zeta\le0.8$:
> $$T_r\approx\frac{1.8}{\omega_n}\;(\zeta\approx0.5),\qquad T_r\approx\frac{1+0.7\zeta}{\omega_n}.$$

---

## En qué consiste

> [!info] Fórmulas empíricas y su origen
> | Fuente | Fórmula | Precisión |
> |---|---|---|
> | Ogata | $T_r\approx1.8/\omega_n$ | buena para $\zeta\approx0.5$ |
> | Franklin | $T_r\approx(1+0.7\zeta)/\omega_n$ | mejor con $\zeta$ variable |
> | Exacta ($0\to100\%$) | $T_r=(\pi-\theta)/\omega_d$ | analítica |

> [!info] Comparación de precisión ($\omega_n=1$, $T_r$ real $10\%\to90\%$ simulado)
> | $\zeta$ | $T_r$ real | $1.8/\omega_n$ | $(1+0.7\zeta)/\omega_n$ |
> |---|---|---|---|
> | 0.3 | 1.68 s | 1.80 s (7%) | 1.21 s (28%) |
> | 0.5 | 1.58 s | 1.80 s (14%) | 1.35 s (15%) |
> | 0.7 | 1.46 s | 1.80 s (23%) | 1.49 s (2%) |
> | 0.8 | 1.43 s | 1.80 s (26%) | 1.56 s (9%) |
>
> La fórmula $(1+0.7\zeta)/\omega_n$ es muy precisa cerca de $\zeta\approx0.7$; $1.8/\omega_n$ es una estimación burda.

> [!info] Dependencia con $\zeta$ y $\omega_n$
> | Parámetro | Efecto sobre $T_r$ |
> |---|---|
> | Mayor $\omega_n$ (fijo $\zeta$) | $T_r$ **disminuye** (más rápido) |
> | Mayor $\zeta$ (fijo $\omega_n$) | $T_r$ **disminuye ligeramente** |

> [!regla] Uso en diseño
> Especificar $T_r\le T_{r,\text{máx}}$ impone una cota sobre $\omega_n$:
> - Ogata: $\omega_n\ge1.8/T_{r,\text{máx}}$.
> - Franklin: $\omega_n\ge(1+0.7\zeta)/T_{r,\text{máx}}$ (más precisa si $\zeta$ ya está fijado por $M_p$).
>
> Ver [[Sobrepico Mp | sobrepico]] y [[Lugar Raices/index | lugar de las raíces]].

---

## Limitaciones

> [!warning]
> 1. **Solo aplica** a sistemas subamortiguados ($0<\zeta<1$).
> 2. Para $\zeta\ge1$, usar fórmulas de primer orden / sobreamortiguado.
> 3. Las aproximaciones empíricas tienen **errores del 10–50%** según $\zeta$.
> 4. Los **ceros** pueden reducir o aumentar $T_r$.
> 5. La definición $10\%\!-\!90\%$ es arbitraria (otras usan $0\!-\!100\%$ o $5\!-\!95\%$).
> 6. Con sobrepico muy grande ($M_p>50\%$) la definición puede dar valores inconsistentes.

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Definición | $10\%\to90\%$ del valor final |
> | Exacta ($0\to100\%$) | $T_r=(\pi-\theta)/\omega_d$ |
> | Ogata | $T_r\approx1.8/\omega_n$ |
> | Franklin | $T_r\approx(1+0.7\zeta)/\omega_n$ |
> | Depende de | $\omega_n$ (y débilmente de $\zeta$) |

> [!corolario]
> El tiempo de subida mide la rapidez con que el sistema alcanza el entorno del valor final por primera vez; lo domina $\omega_n$. La fórmula exacta $(\pi-\theta)/\omega_d$ es fiable, mientras las empíricas solo sirven como estimación rápida en un rango estrecho de $\zeta$.

> [!referencia]
> - Respuesta de la que deriva: [[Formula General]].
> - Métricas relacionadas: [[Sobrepico Mp]] · [[Tiempo Pico Tp]] · [[Tiempo Establecimiento Ts]].
> - Panorama: [[Segundo Orden/index]].
> - Diseño por polos: [[Lugar Raices/index]].
