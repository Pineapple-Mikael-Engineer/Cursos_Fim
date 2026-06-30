---
title: Márgenes de Fase y Ganancia
order: 3
tags:
  - control-clasico
  - analisis
  - respuesta-frecuencial
  - estabilidad
draft: false
aliases:
  - márgenes
  - margen de fase
  - margen de ganancia
  - MF MG
  - gain phase margin
---

# Márgenes de Fase y Ganancia

> [!definicion]
> Los **márgenes** miden cuánto falta para que el lazo cerrado se vuelva inestable, como distancia del lugar de $L(j\omega)$ al punto crítico $-1$:
> $$\text{MF}=180^\circ+\angle L(j\omega_{gc}),\qquad \text{MG}_{\text{dB}}=-20\log_{10}|L(j\omega_{pc})|,$$
> donde el **cruce de ganancia** $\omega_{gc}$ cumple $|L(j\omega_{gc})|=1$ ($0$ dB) y el **cruce de fase** $\omega_{pc}$ cumple $\angle L(j\omega_{pc})=-180^\circ$. El **MG** es el factor por el que puede crecer $|L|$ y el **MF** el retardo de fase extra que tolera el lazo antes de inestabilizarse.

> [!info]
> Vive en la subcarpeta [[Nyquist/index | Nyquist]] de [[Respuesta Frecuencial/index | Respuesta Frecuencial]]. Es la lectura cuantitativa del [[Criterio Nyquist | criterio de Nyquist]] (distancia a $-1$); se leen sobre [[Bode/index | Bode]] o sobre el [[Diagrama Polar | diagrama polar]] y predicen el transitorio de [[Segundo Orden/index | segundo orden]].

---

## Ejemplo

> [!ejemplo]
> **Cálculo numérico de MF y MG para $L(s)=\dfrac{4}{s(s+1)(s+2)}$.**
>
> **Paso 1 — Margen de ganancia.** El cruce de fase $\omega_{pc}$ es donde $\angle L=-180^\circ$, que ya conocemos del [[Diagrama Polar | lugar polar]]: $\omega_{pc}=\sqrt2$ rad/s, y allí $L(j\sqrt2)=-K/6=-4/6=-0.667$. Entonces
> $$|L(j\omega_{pc})|=0.667\;\Rightarrow\;\text{MG}_{\text{dB}}=-20\log_{10}(0.667)=+3.5\ \text{dB}\quad(\text{factor }1/0.667\approx1.5).$$
> Margen positivo pero modesto: la ganancia solo puede subir $\times1.5$ antes de la inestabilidad (coherente con $K_{\text{crít}}=6$).
>
> **Paso 2 — Cruce de ganancia $\omega_{gc}$** ($|L|=1$):
> $$|L(j\omega)|=\frac{4}{\omega\sqrt{(1+\omega^2)(4+\omega^2)}}=1.$$
> Resolviendo numéricamente, $\omega_{gc}\approx1.13$ rad/s.
>
> **Paso 3 — Fase en $\omega_{gc}$:**
> $$\angle L(j\omega_{gc})=-90^\circ-\arctan(1.13)-\arctan\tfrac{1.13}{2}
> =-90^\circ-48.5^\circ-29.5^\circ=-168^\circ.$$
>
> **Paso 4 — Margen de fase:**
> $$\text{MF}=180^\circ+(-168^\circ)=+12^\circ.$$
> MF positivo → estable, pero **pequeño** (recomendado $>30^\circ$): respuesta muy oscilatoria. Con la regla $\zeta\approx\text{MF}^\circ/100\approx0.12$ se anticipa un [[Sobrepico Mp | sobrepico]] grande. Un [[Lugar Raices/index | compensador lead]] subiría el MF.

---

## Lectura gráfica

> [!ejemplo] Márgenes sobre el diagrama de Bode
> ![[bode_margenes.svg|600]]
>
> En $\omega_{gc}$ (magnitud $=0$ dB), el MF es la distancia de la fase a $-180^\circ$. En $\omega_{pc}$ (fase $=-180^\circ$), el MG es la distancia de la magnitud a $0$ dB.

> [!ejemplo] Márgenes sobre el diagrama de Nyquist
> ![[nyquist_margenes.svg|550]]
>
> El MG es el inverso de la distancia $|L|$ donde la curva cruza el eje real negativo ($\omega_{pc}$); el MF es el ángulo entre el cruce del círculo unitario ($\omega_{gc}$) y el eje real negativo.

---

## En qué consiste

> [!teorema] Frecuencias de cruce
> $$\text{Cruce de ganancia } \omega_{gc}: \quad |L(j\omega_{gc})|=1\ (0\text{ dB})$$
> $$\text{Cruce de fase } \omega_{pc}: \quad \angle L(j\omega_{pc})=-180^\circ$$
> $$\boxed{\;\text{MF}=180^\circ+\angle L(j\omega_{gc}) \qquad \text{MG}_{\text{dB}}=-20\log_{10}|L(j\omega_{pc})|\;}$$

> [!info] Interpretación geométrica
> Cuanto **más lejos** pasa el lugar de Nyquist del punto $-1$, mayores los márgenes y más robusto el sistema. Márgenes pequeños ⇒ la curva roza $-1$ ⇒ respuesta muy oscilatoria y sensible a variaciones.

> [!teorema] Estabilidad por márgenes
> Para sistemas de [[Sistemas Fase Minima | fase mínima]] y lazo abierto estable:
> $$\text{lazo cerrado estable}\iff \text{MF}>0\ \text{y}\ \text{MG}>0.$$

---

## Receta

> [!algoritmo] Procedimiento en Bode
> 1. Hallar $\omega_{gc}$: donde la magnitud cruza $0$ dB → leer la fase allí → $\text{MF}=180^\circ+\angle L$.
> 2. Hallar $\omega_{pc}$: donde la fase cruza $-180^\circ$ → leer la magnitud allí → $\text{MG}=-|L|_{\text{dB}}$.

> [!regla] Valores típicos de diseño
> | Margen | Rango recomendado |
> |---|---|
> | Margen de fase | $30^\circ$ – $60^\circ$ (robusto $\approx45^\circ$–$60^\circ$) |
> | Margen de ganancia | $>6$ dB (factor $\times2$) |

> [!info] MF y $\zeta$
> Para un sistema de [[Segundo Orden/index | segundo orden]] dominante, el margen de fase se relaciona con el amortiguamiento:
> $$\zeta\approx\frac{\text{MF}^\circ}{100}\quad(\text{regla práctica, MF}\lesssim70^\circ).$$
> Un $\text{MF}=45^\circ$ corresponde a $\zeta\approx0.45$ y un [[Sobrepico Mp | sobrepico]] moderado. Así el MF en frecuencia predice el transitorio en el tiempo — puente clave para el [[Lugar Raices/index | diseño de compensadores]] (lead aumenta MF).

> [!info] En MATLAB
> ```matlab
> K = 4;
> L = tf(K, conv([1 1 0], [1 2]));
> margin(L)                          % traza Bode con MF y MG marcados
> [Gm, Pm, Wpc, Wgc] = margin(L);    % Gm (lineal), Pm en grados
> ```

---

## Limitaciones

> [!warning] Márgenes engañosos
> En sistemas de **fase no mínima**, con múltiples cruces, o muy resonantes, MF y MG pueden no reflejar bien la robustez real. En esos casos se usa el **margen de estabilidad** (distancia mínima a $-1$) o el [[Criterio Nyquist | criterio de Nyquist]] completo.

---

## Resumen

> [!resumen]
> | Margen | Frecuencia | Fórmula | Recomendado |
> |---|---|---|---|
> | Fase (MF) | $\omega_{gc}$ ($\lvert L\rvert=1$) | $180^\circ+\angle L(j\omega_{gc})$ | $30^\circ$–$60^\circ$ |
> | Ganancia (MG) | $\omega_{pc}$ ($\angle L=-180^\circ$) | $-20\log_{10}\lvert L(j\omega_{pc})\rvert$ | $>6$ dB |
> | Ejemplo $K=4$ | — | MF $\approx12^\circ$, MG $\approx3.5$ dB | bajos (oscilatorio) |

> [!corolario]
> Los márgenes son la versión métrica del criterio de Nyquist: en vez de solo decidir estable/inestable, dicen **cuánto** margen queda. El MG mide tolerancia a cambios de ganancia y el MF a retardos de fase; un MF razonable ($\approx45^\circ$) garantiza, vía $\zeta\approx\text{MF}^\circ/100$, un transitorio bien amortiguado. Son el objetivo directo del diseño de [[Lugar Raices/index | compensadores]].

> [!referencia]
> - Distancia a $-1$ y criterio exacto: [[Criterio Nyquist]] · [[Diagrama Polar]].
> - Lectura sobre magnitud/fase: [[Bode/index]] · [[Construccion Asintotica]].
> - Conexión con el transitorio: [[Segundo Orden/index]] · [[Sobrepico Mp]].
> - Aumento de MF con compensadores: [[Lugar Raices/index]].
