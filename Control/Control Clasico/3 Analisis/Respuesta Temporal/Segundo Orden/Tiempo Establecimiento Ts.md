---
title: Tiempo de Establecimiento (Ts)
order: 4
tags:
  - control-clasico
  - analisis
  - respuesta-temporal
  - segundo-orden
draft: false
aliases:
  - tiempo establecimiento
  - Ts
  - settling time
---

# Tiempo de Establecimiento ($T_s$)

> [!definicion]
> Tiempo que tarda la respuesta a escalón en **entrar y permanecer** dentro de una banda porcentual alrededor del valor final. Aproximaciones para sistema subamortiguado:
> $$T_s(2\%)\approx\frac{4}{\zeta\omega_n},\qquad T_s(5\%)\approx\frac{3}{\zeta\omega_n}.$$
> El producto $\sigma=\zeta\omega_n$ es la **parte real** de los polos: gobierna la velocidad de decaimiento de la envolvente.

> [!info]
> Métrica de [[Segundo Orden/index | segundo orden]] derivada de la **envolvente** de la [[Formula General | respuesta $y(t)$]]. Fija el producto $\zeta\omega_n$ en diseño (complementa a [[Sobrepico Mp | $M_p$]], que fija $\zeta$). Distinta del [[Tiempo Pico Tp | tiempo de pico]] (transitorio) y del [[Tiempo Subida Tr | tiempo de subida]] (rapidez inicial).

---

## Ejemplo

> [!ejemplo] Cálculo de $T_s$ aproximado y exacto
> **Problema.** Un sistema tiene $\zeta=0.5$ y $\omega_n=10$ rad/s. Calcular $T_s(2\%)$ aproximado y compararlo con el real.
>
> **Paso 1 — Aproximación estándar:**
> $$T_s(2\%)\approx\frac{4}{\zeta\omega_n}=\frac{4}{0.5\cdot10}=\frac{4}{5}=0.8\ \text{s}.$$
>
> **Paso 2 — Envolvente exacta.** La respuesta es $y(t)=1-\frac{e^{-5t}}{\sqrt{0.75}}\sin(8.66t+\arccos0.5)$. Su envolvente alcanza el $2\%$ cuando:
> $$\frac{e^{-5t}}{0.866}=0.02\;\Rightarrow\;e^{-5t}=0.0173\;\Rightarrow\;t=\frac{-\ln0.0173}{5}=\frac{4.06}{5}=0.81\ \text{s}.$$
>
> **Paso 3 — Comparar.** El último cruce real de la banda $\pm2\%$ (resuelto numéricamente) es $\approx0.78$ s. La aproximación $0.8$ s tiene error de solo $\sim2.5\%$.
>
> **Paso 4 — Especificación inversa.** Si se exige $T_s\le0.5$ s, hace falta $\zeta\omega_n\ge4/0.5=8$; con $\zeta=0.5$ implica $\omega_n\ge16$ rad/s.

> [!ejemplo] Banda de establecimiento
> ![[resp_tiempo_establecimiento_ts.svg|560]]
>
> La salida entra y permanece dentro de la banda $\pm2\%$ del valor final a partir de $t_s\approx4/\zeta\omega_n$.

---

## Demostración

> [!teorema] Fórmula de $T_s(2\%)$ para sistema subamortiguado
> $$T_s(2\%)\approx\frac{4}{\zeta\omega_n}.$$

> [!demostracion]
> **Paso 1 — Acotar por la envolvente.** Para $y(t)=1-\frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}}\sin(\omega_d t+\theta)$, como $|\sin|\le1$:
> $$1-\frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}}\le y(t)\le 1+\frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}}.$$
>
> **Paso 2 — Condición de entrada en la banda.** Para permanecer dentro de $\pm2\%$, la envolvente debe ser $\le0.02$:
> $$\frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}}\le0.02.$$
> Para $\zeta$ típicos ($0.3\le\zeta\le0.8$), $\sqrt{1-\zeta^2}\in[0.6,0.95]$; la aproximación común ignora ese factor: $e^{-\zeta\omega_n t}\le0.02$.
>
> **Paso 3 — Despejar $t$:**
> $$-\zeta\omega_n t\le\ln0.02\approx-3.912\;\Rightarrow\;\zeta\omega_n t\ge3.912\;\Rightarrow\;t\ge\frac{3.912}{\zeta\omega_n}.$$
>
> **Paso 4 — Redondear.** Se aproxima $3.912\to4$ (margen de seguridad):
> $$T_s(2\%)\approx\frac{4}{\zeta\omega_n}.$$

> [!info] Análogo para $T_s(5\%)$
> $$\frac{e^{-\zeta\omega_n t}}{\sqrt{1-\zeta^2}}\le0.05\;\Rightarrow\;-\zeta\omega_n t\le\ln0.05\approx-2.996\;\Rightarrow\;t\ge\frac{2.996}{\zeta\omega_n}\approx\frac{3}{\zeta\omega_n}.$$

---

## En qué consiste

> [!info] Dependencia con $\zeta$ y $\omega_n$
> | Parámetro | Efecto sobre $T_s$ |
> |---|---|
> | Mayor $\omega_n$ (fijo $\zeta$) | $T_s$ **disminuye** (más rápido) |
> | Mayor $\zeta$ (fijo $\omega_n$) | $T_s$ **disminuye** (menos oscilaciones) |
> | Producto $\zeta\omega_n$ | constante de amortiguamiento (inverso de $T_s$) |

> [!info] Fórmula más precisa (para $\zeta$ pequeño)
> Incluyendo el factor $1/\sqrt{1-\zeta^2}$:
> $$\frac{e^{-\zeta\omega_n T_s}}{\sqrt{1-\zeta^2}}=0.02\;\Rightarrow\;T_s=\frac{-\ln(0.02\sqrt{1-\zeta^2})}{\zeta\omega_n}.$$
> - $\zeta=0.3$: $-\ln(0.02\cdot0.954)=-\ln0.0191=3.96\approx4$.
> - $\zeta=0.1$: $-\ln(0.02\cdot0.995)=-\ln0.0199=3.92\approx4$.
>
> La aproximación $4/\zeta\omega_n$ funciona muy bien para $0.1\le\zeta\le0.9$.

> [!info] $T_s$ normalizado ($\omega_n=1$ rad/s)
> | $\zeta$ | $T_s(2\%)$ real | $T_s(2\%)$ aprox. | Error |
> |---|---|---|---|
> | 0.1 | 40.0 s | 40.0 s | 0% |
> | 0.3 | 13.3 s | 13.3 s | 0% |
> | 0.5 | 8.0 s | 8.0 s | 0% |
> | 0.7 | 5.7 s | 5.7 s | 0% |
> | 0.9 | 4.5 s | 4.4 s | 2% |

> [!regla] Uso en diseño
> Especificar $T_s\le T_{s,\text{máx}}$ impone una cota sobre la parte real de los polos:
> $$\frac{4}{\zeta\omega_n}\le T_{s,\text{máx}}\;\Rightarrow\;\zeta\omega_n\ge\frac{4}{T_{s,\text{máx}}}.$$
> $\zeta\omega_n$ es la distancia de los polos al eje imaginario. Combinado con $M_p$: p. ej. $M_p\le10\%$ y $T_s\le2$ s dan $\zeta\ge0.59$ y $\omega_n\ge4/(0.59\cdot2)\approx3.4$ rad/s. Ver [[Lugar Raices/index | lugar de las raíces]].

---

## Limitaciones

> [!warning]
> 1. La fórmula $4/\zeta\omega_n$ es una **aproximación**: desprecia $1/\sqrt{1-\zeta^2}$ y usa la cota superior de la envolvente.
> 2. **Solo aplica** a sistemas subamortiguados ($0<\zeta<1$); para $\zeta$ muy pequeño no es válida.
> 3. Para $\zeta\ge1$ el establecimiento es más largo (fórmula conservadora).
> 4. Los **ceros** pueden extender $T_s$.
> 5. Asume **realimentación unitaria** y 2.º orden sin ceros; en orden superior usar polos dominantes.
> 6. El criterio $\pm2\%$ es arbitrario; elegir según la aplicación.

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Definición | entrar y permanecer en banda $\pm x\%$ |
> | $T_s(2\%)$ | $\approx4/\zeta\omega_n$ |
> | $T_s(5\%)$ | $\approx3/\zeta\omega_n$ |
> | Depende de | $\zeta\omega_n$ (parte real de los polos) |
> | Diseño | $\zeta\omega_n\ge4/T_{s,\text{máx}}$ |

> [!corolario]
> El establecimiento lo gobierna la envolvente exponencial $e^{-\zeta\omega_n t}$: su constante de tiempo $1/(\zeta\omega_n)$ fija cuándo el *ringing* cae bajo la banda. Por eso $T_s$ se traduce directamente en una cota sobre la parte real de los polos, mientras $M_p$ fija $\zeta$: juntos determinan $(\zeta,\omega_n)$.

> [!referencia]
> - Respuesta y envolvente: [[Formula General]].
> - Métrica complementaria que fija $\zeta$: [[Sobrepico Mp]].
> - Otras métricas: [[Tiempo Pico Tp]] · [[Tiempo Subida Tr]].
> - Panorama: [[Segundo Orden/index]].
