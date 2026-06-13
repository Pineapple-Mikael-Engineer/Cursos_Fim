---
title: Correcciones del Diagrama de Bode
tags:
  - control-clasico
  - analisis
  - respuesta-frecuencial
  - bode
draft: false
aliases:
  - correcciones de Bode
  - error asintótico
  - pico resonante
---

# Correcciones del Diagrama de Bode

> [!definicion]
> Las [[Construccion Asintotica | asíntotas]] son rectas idealizadas; la curva real se desvía cerca de las **frecuencias de esquina** y en torno a las **resonancias**. Las correcciones ajustan el trazo asintótico a la respuesta verdadera: $\mp3$ dB en la esquina de un polo/cero simple y el pico $M_r$ de un par de 2.º orden subamortiguado.

> [!info]
> Cierra la subsección [[index | Bode]] de [[Respuesta Frecuencial/index | Respuesta Frecuencial]]: afina lo trazado en [[Construccion Asintotica]] con los factores de [[Factores Basicos]]. El pico resonante conecta con [[Segundo Orden/index]] y el [[Sobrepico Mp | sobrepico]] temporal.

---

## Ejemplo

> [!ejemplo]
> **Corregir la esquina de $G(s)=\dfrac{1}{1+s/10}$ (polo simple, $\omega_0=10$).** Comparar asíntota y curva real en tres frecuencias.
>
> ![[bode_correccion_esquina.svg|550]]
>
> La magnitud real es $|G|_{\text{dB}}=-20\log\sqrt{1+(\omega/10)^2}$; la asíntota es $0$ dB hasta $\omega_0$ y luego $-20$ dB/dec.
>
> | $\omega$ | $\omega/\omega_0$ | Asíntota (dB) | Real $-20\log\sqrt{1+(\omega/\omega_0)^2}$ | Corrección |
> |---|---|---|---|---|
> | $5$ | $0.5$ | $0$ | $-20\log\sqrt{1.25}=-0.97$ | $-1.0$ dB |
> | $10$ | $1$ | $0$ | $-20\log\sqrt{2}=-3.01$ | $-3.0$ dB |
> | $20$ | $2$ | $-6.0$ | $-20\log\sqrt{5}=-6.99$ | $-1.0$ dB |
>
> **Fase en la esquina:** $\angle G(j10)=-\arctan(10/10)=-45^\circ$ exactos. La mayor corrección de magnitud ($-3$ dB) cae justo en $\omega_0$ y decae a $\approx\mp1$ dB a una octava. Para un **cero** los mismos valores con signo $+$.

> [!ejemplo]
> **Pico resonante de un par de 2.º orden con $\zeta=0.3$, $\omega_n=1$.** La asíntota ($0$ dB hasta $\omega_n$, luego $-40$ dB/dec) ignora el pico.
>
> ![[bode_pico_resonante.svg|550]]
>
> **Altura del pico:**
> $$M_r=\frac{1}{2\zeta\sqrt{1-\zeta^2}}=\frac{1}{2(0.3)\sqrt{1-0.09}}=\frac{1}{0.6\cdot0.954}\approx1.75\;\Rightarrow\;20\log1.75\approx+4.8\text{ dB}.$$
> **Frecuencia del pico:**
> $$\omega_r=\omega_n\sqrt{1-2\zeta^2}=\sqrt{1-0.18}\approx0.905\ \text{rad/s}.$$
> La corrección añade $+4.8$ dB sobre la asíntota en $\omega_r\approx0.9$, ligeramente por debajo de $\omega_n$.

---

## En qué consiste

> [!teorema] Desviación de $\pm3$ dB en la esquina
> En la frecuencia de esquina $\omega_0$ de un polo o cero simple, la magnitud real difiere de la asíntota en:
> $$|G(j\omega_0)|_{\text{dB}}-\text{asíntota}=\mp3\text{ dB}$$
> ($-3$ dB para polo, $+3$ dB para cero). A **una octava** de la esquina la desviación es $\approx\mp1$ dB.

> [!info] Corrección de fase
> La fase real de un polo simple es $\arctan(-\omega/\omega_0)$: $-45^\circ$ exactos en $\omega_0$, aproximándose suavemente a $0^\circ$/$-90^\circ$. La aproximación lineal (recta de $\mp45^\circ$/dec entre $0.1\omega_0$ y $10\omega_0$) tiene error máximo $\approx6^\circ$ cerca de los extremos del tramo.

> [!teorema] Magnitud del pico resonante (segundo orden)
> Para el par de [[Segundo Orden/index | segundo orden]] con $\zeta<0.707$, la asíntota ($0$ dB hasta $\omega_n$) **subestima** el máximo. El pico real es
> $$M_r=\frac{1}{2\zeta\sqrt{1-\zeta^2}}\quad\text{en}\quad\omega_r=\omega_n\sqrt{1-2\zeta^2}.$$

> [!info] Pico según $\zeta$
> | $\zeta$ | $M_r$ (dB) | Comentario |
> |---|---|---|
> | $0.05$ | $+20$ | resonancia muy aguda |
> | $0.1$ | $+14$ | |
> | $0.3$ | $+4.8$ | |
> | $0.5$ | $+1.2$ | pico apenas visible |
> | $0.707$ | $0$ | sin pico (límite) |
> | $>0.707$ | — | magnitud monótona decreciente |

---

## Limitaciones

> [!warning] Relación con el dominio temporal
> Un pico resonante alto ($\zeta$ bajo) corresponde a un [[Sobrepico Mp | sobrepico]] grande en la respuesta al escalón: ambos miden el **amortiguamiento**. $\omega_r\approx\omega_n$ y $M_r$ crece al disminuir $\zeta$, igual que $M_p$. Para $\zeta\geq0.707$ no hay pico y la corrección se reduce a los $\mp3$ dB de las esquinas simples.

---

## Resumen

> [!resumen]
> | Corrección | Dónde | Magnitud |
> |---|---|---|
> | Polo simple | esquina $\omega_0$ | $-3$ dB |
> | Cero simple | esquina $\omega_0$ | $+3$ dB |
> | A una octava | $0.5\omega_0$ o $2\omega_0$ | $\mp1$ dB |
> | Fase (recta) | extremos del tramo | error $\approx6^\circ$ |
> | Par 2.º orden | $\omega_r=\omega_n\sqrt{1-2\zeta^2}$ | $M_r=\frac{1}{2\zeta\sqrt{1-\zeta^2}}$ |

> [!corolario]
> La asíntota acierta lejos de las esquinas y yerra cerca de ellas: en cada esquina simple corrige $\mp3$ dB y la fase pasa por $\mp45^\circ$; en un par subamortiguado añade el pico $M_r$ en $\omega_r$. Cuanto menor el $\zeta$, mayor el pico y mayor el sobrepico temporal asociado.

> [!referencia]
> - El trazo asintótico que se corrige: [[Construccion Asintotica]].
> - Origen del pico: [[Segundo Orden/index]] · [[Factores Basicos]].
> - Conexión con el transitorio: [[Sobrepico Mp]].
> - Lectura de márgenes sobre la curva corregida: [[Margenes MF MG]].
