---
title: Sistemas de Fase Mínima
tags:
  - control-clasico
  - analisis
  - respuesta-frecuencial
draft: false
aliases:
  - fase mínima
  - fase no mínima
  - minimum phase
---

# Sistemas de Fase Mínima

> [!definicion]
> Un sistema es de **fase mínima** si todos sus polos y ceros están en el semiplano izquierdo (SPI), sin retardos. Si tiene algún cero o polo en el semiplano derecho (SPD), o un retardo $e^{-Ts}$, es de **fase no mínima**. Entre todos los sistemas con la **misma curva de magnitud** $|G(j\omega)|$, el de fase mínima es el de **menor desfase** posible en cada frecuencia.

> [!info]
> Vive en [[Respuesta Frecuencial/index | Respuesta Frecuencial]]. Explica por qué en fase mínima la magnitud de [[Bode/index | Bode]] basta para los [[Margenes MF MG | márgenes]], y por qué en fase no mínima hay que trazar la fase explícitamente. Hermanas: [[Polos Ceros]] · [[Criterio Nyquist]].

---

## Ejemplo

> [!ejemplo]
> **Misma magnitud, distinta fase.** Comparar el par fase mínima / fase no mínima con $z=p=10$, evaluando en $\omega=10$ y $\omega=100$:
> $$G_{\min}(s)=\frac{1+s/10}{1+s/100},\qquad G_{\text{nm}}(s)=\frac{1-s/10}{1+s/100}.$$
>
> ![[fase_minima_vs_no_minima.svg|600]]
>
> **Paso 1 — Magnitud idéntica.** El cero $1\pm s/10$ tiene magnitud $|1\pm j\omega/10|=\sqrt{1+(\omega/10)^2}$, **igual para ambos signos**. Por tanto $|G_{\min}|=|G_{\text{nm}}|$ a toda frecuencia. En $\omega=10$:
> $$|1\pm j|=\sqrt2,\quad |1+j0.1|\approx1.005\;\Rightarrow\;|G|\approx\frac{1.41}{1.005}\approx1.41\ (+3\text{ dB}).$$
>
> **Paso 2 — Fase del cero en $\omega=10$.**
> $$\angle(1+j10/10)=\angle(1+j)=+45^\circ,\qquad \angle(1-j10/10)=\angle(1-j)=-45^\circ.$$
> El cero en SPI **adelanta** $+45^\circ$; el cero en SPD **atrasa** $-45^\circ$. Diferencia de $90^\circ$ ya en la esquina.
>
> **Paso 3 — Fase del cero en $\omega=100$** (una década arriba):
> $$\angle(1+j10)=+84.3^\circ,\qquad \angle(1-j10)=-84.3^\circ.$$
> El de fase mínima tiende a $+90^\circ$; el no mínimo a $-90^\circ$. La **brecha crece** hasta casi $180^\circ$.
>
> **Paso 4 — Consecuencia.** El polo común $1/(1+s/100)$ resta lo mismo en ambos. Pero $G_{\text{nm}}$ acumula fase negativa extra: en el [[Margenes MF MG | margen de fase]] esto recorta el margen disponible y, en el tiempo, el cero en SPD produce **undershoot inicial** (la salida arranca en sentido contrario al final).

---

## En qué consiste

> [!teorema] Relación magnitud–fase (ganancia de Bode)
> Para sistemas de fase mínima, magnitud y fase **no son independientes**: una determina la otra (relación de Bode, transformada de Hilbert). La fase se aproxima por la pendiente de la magnitud:
> $$\angle G(j\omega_0)\approx 90^\circ\times\frac{1}{20}\,\frac{d\,(|G|_{\text{dB}})}{d\,(\log\omega)}.$$
> Una pendiente de $-20$ dB/dec $\Rightarrow\approx-90^\circ$ de fase; $-40$ dB/dec $\Rightarrow\approx-180^\circ$. En fase **no** mínima esta relación falla: con la misma pendiente la fase puede ser mucho más negativa.

> [!info] Consecuencia práctica
> En fase mínima, conocer la **magnitud** basta para reconstruir la fase y aplicar los [[Margenes MF MG | márgenes]]; por eso el Bode de magnitud suele bastar para el diseño. En fase no mínima hay que trazar la fase explícitamente.

> [!info] Ejemplos físicos de fase no mínima
> | Sistema | Causa de la fase no mínima |
> |---|---|
> | Retardo de transporte $e^{-Ts}$ | tubería, transmisión, tiempo de cómputo |
> | Nivel de caldera (*boiler drum*) | cero en SPD (encogimiento/hinchazón) |
> | Avión: altitud por elevador | undershoot inicial |
> | Convertidor *boost* | cero en SPD |

---

## Limitaciones

> [!warning] Limitaciones de la fase no mínima
> - **Fase extra** $\Rightarrow$ menor [[Margenes MF MG | margen de fase]] $\Rightarrow$ más difícil de estabilizar.
> - Los ceros en SPD **limitan el ancho de banda** alcanzable.
> - Los retardos imponen un tope de ganancia; se analizan mejor con [[Criterio Nyquist | Nyquist]] que con el [[Lugar Raices/index | lugar de raíces]].

> [!warning] No cancelar ceros/polos en el SPD
> Cancelar un cero en SPD con un polo del controlador (o un polo en SPD con un cero) deja un modo **inestable oculto**: incontrolable o inobservable. La cancelación solo es válida en el SPI.

---

## Resumen

> [!resumen]
> | Aspecto | Fase mínima | Fase no mínima |
> |---|---|---|
> | Polos/ceros | todos en SPI | alguno en SPD, o retardo |
> | Magnitud | — | igual a su par de fase mínima |
> | Fase | mínima posible | fase negativa extra |
> | Escalón | sin undershoot | undershoot inicial |
> | Diseño | basta la magnitud | trazar la fase aparte |

> [!corolario]
> Dos sistemas pueden compartir la misma magnitud $|G(j\omega)|$ y diferir en fase: el de fase mínima es el de menor desfase. La fase extra de la versión no mínima (cero en SPD o retardo) recorta el margen de fase, limita el ancho de banda y nunca debe cancelarse, porque dejaría un modo inestable oculto.

> [!referencia]
> - Por qué la magnitud basta (o no) para los márgenes: [[Margenes MF MG]] · [[Bode/index]].
> - Análisis de retardos: [[Criterio Nyquist]].
> - Efecto de ceros en la respuesta: [[Polos Ceros]] · [[Segundo Orden/index]].
> - Limitaciones de diseño: [[Lugar Raices/index]].
