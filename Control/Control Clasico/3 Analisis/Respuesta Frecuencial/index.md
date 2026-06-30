---
title: Respuesta Frecuencial
order: 5
tags:
  - control-clasico
  - analisis
  - respuesta-frecuencial
  - index
draft: false
aliases:
  - respuesta en frecuencia
  - análisis frecuencial
  - frequency response
---

# Respuesta Frecuencial

> [!definicion]
> La respuesta en frecuencia es la salida en régimen permanente de un sistema lineal estable ante una entrada senoidal, evaluando la [[Funcion Transferencia/index | función de transferencia]] sobre el eje imaginario $s=j\omega$:
> $$G(j\omega)=|G(j\omega)|\,e^{\,j\angle G(j\omega)}.$$
> La **magnitud** $|G(j\omega)|$ escala la amplitud y la **fase** $\angle G(j\omega)$ desplaza la senoide. Ante $u(t)=A\sin(\omega t)$: $\;y_{ss}(t)=A\,|G(j\omega)|\,\sin\big(\omega t+\angle G(j\omega)\big)$.

> [!info]
> Índice de la sección de análisis frecuencial (dentro de **3 Análisis**). Da las dos representaciones: [[Bode/index | Bode]] (magnitud y fase vs $\omega$) y [[Nyquist/index | Nyquist]] (lugar polar). Hermanas: [[Sistemas Fase Minima]] · [[Margenes MF MG]].

---

## Ejemplo

> [!ejemplo]
> **Filtro de primer orden $G(s)=\dfrac{10}{s+2}$ excitado a $\omega=2\ \text{rad/s}$.** Hallar la amplitud y el desfase de la salida en régimen ante $u(t)=3\sin(2t)$.
>
> **Paso 1 — Evaluar en $s=j\omega$** con $\omega=2$:
> $$G(j2)=\frac{10}{\,j2+2\,}=\frac{10}{2+j2}.$$
>
> **Paso 2 — Magnitud:**
> $$|G(j2)|=\frac{10}{\sqrt{2^2+2^2}}=\frac{10}{\sqrt{8}}=\frac{10}{2.83}\approx 3.54.$$
> En decibelios: $20\log_{10}(3.54)\approx +11.0$ dB.
>
> **Paso 3 — Fase** (numerador real positivo, denominador $2+j2$):
> $$\angle G(j2)=0-\arctan\!\frac{2}{2}=-45^\circ.$$
> El polo está justo en su frecuencia de esquina $\omega_0=2$, donde la fase vale exactamente $-45^\circ$ (ver [[Factores Basicos]]).
>
> **Paso 4 — Salida en régimen permanente:**
> $$y_{ss}(t)=3\cdot 3.54\,\sin\!\big(2t-45^\circ\big)\approx 10.6\,\sin\!\big(2t-45^\circ\big).$$
> La amplitud se amplifica $\times 3.54$ y la senoide se retrasa $45^\circ$ (un cuarto de periodo del polo). Repitiendo en varias $\omega$ se obtiene el [[Bode/index | diagrama de Bode]].

---

## En qué consiste

> [!teoria]
> El análisis frecuencial caracteriza el sistema **sin resolver la EDO** evaluando $G(j\omega)$ barriendo $\omega$. Sus ventajas:
> - Evalúa la **estabilidad de lazo cerrado** a partir de datos de **lazo abierto** ([[Criterio Nyquist]], [[Margenes MF MG | márgenes]]).
> - Trabaja con sistemas de los que solo se tiene **respuesta medida** (datos experimentales), sin modelo analítico.
> - Diseña compensadores con criterios de **margen de fase** y ancho de banda.
> - Maneja **retardos** $e^{-Ts}$, que el [[Lugar Raices/index | lugar de raíces]] trata mal.

> [!info] Las dos representaciones
> | Representación | Qué grafica | Fuerte |
> |---|---|---|
> | [[Bode/index | Bode]] | $\lvert G\rvert_{\text{dB}}$ y $\angle G$ vs $\omega$ (escala log) | construcción asintótica; lectura directa de márgenes y ancho de banda |
> | [[Nyquist/index | Nyquist]] | lugar polar de $L(j\omega)$ en el plano complejo | criterio exacto $Z=N+P$ para polos en SPD o retardos |

> [!definicion] Magnitud en decibelios
> $$|G(j\omega)|_{\text{dB}}=20\log_{10}|G(j\omega)|.$$
> La escala log convierte **productos en sumas**: $20\log|G_1G_2|=20\log|G_1|+20\log|G_2|$, lo que habilita la [[Construccion Asintotica | construcción asintótica]] sumando factores.

> [!info] Referencias rápidas dB
> | $\lvert G\rvert$ | $0.01$ | $0.1$ | $1$ | $\sqrt2$ | $2$ | $10$ | $100$ |
> |---|---|---|---|---|---|---|---|
> | dB | $-40$ | $-20$ | $0$ | $+3$ | $+6$ | $+20$ | $+40$ |

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Definición | $G(j\omega)$: evaluar $G(s)$ en $s=j\omega$ |
> | Forma polar | $\lvert G(j\omega)\rvert\,e^{j\angle G(j\omega)}$ |
> | Salida régimen | $y_{ss}=A\lvert G\rvert\sin(\omega t+\angle G)$ |
> | Magnitud en dB | $20\log_{10}\lvert G\rvert$ |
> | Representaciones | [[Bode/index \| Bode]] · [[Nyquist/index \| Nyquist]] |
> | Uso clave | estabilidad de lazo cerrado desde lazo abierto |

> [!corolario]
> La respuesta en frecuencia reduce el comportamiento dinámico a una función compleja $G(j\omega)$: magnitud (amplificación) y fase (desfase) a cada $\omega$. Sumar factores en dB y grados ([[Bode/index | Bode]]) o trazar el lugar polar ([[Nyquist/index | Nyquist]]) permite leer estabilidad y márgenes sin integrar la EDO, incluso con solo datos medidos.

> [!referencia]
> - Construcción de los diagramas: [[Bode/index]] · [[Nyquist/index]].
> - Estabilidad de lazo cerrado: [[Criterio Nyquist]] · [[Margenes MF MG]].
> - Fase y causalidad: [[Sistemas Fase Minima]].
> - Base: [[Funcion Transferencia/index]] · [[Polos Ceros]] · [[Segundo Orden/index]].
