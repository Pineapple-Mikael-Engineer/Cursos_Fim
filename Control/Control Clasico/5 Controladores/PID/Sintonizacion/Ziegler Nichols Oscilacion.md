---
title: Ziegler-Nichols — Oscilación Sostenida
tags:
  - control-clasico
  - controladores
  - pid
  - sintonizacion
draft: false
aliases:
  - Ziegler-Nichols oscilación
  - método de la ganancia última
  - ganancia crítica
  - segundo método de Z-N
---

# Ziegler-Nichols: Oscilación Sostenida

> [!definicion]
> Método de sintonización en **lazo cerrado**: con control solo proporcional se sube $K_p$ hasta que la salida oscila con amplitud constante; ese $K_p$ es la **ganancia última** $K_u$ (también $K_{cr}$) y el periodo de la oscilación es el **periodo último** $P_u$ (también $T_{cr}$). Con ambos se calculan $K_p$, $T_i$, $T_d$ por la tabla de Ziegler-Nichols.
> $$\text{PID:}\qquad K_p=0.6\,K_u,\qquad T_i=\frac{P_u}{2},\qquad T_d=\frac{P_u}{8}.$$

> [!info]
> Vive en [[Sintonizacion/index | sintonización del PID]], junto a su hermana en lazo abierto [[Ziegler Nichols Curva Reaccion | curva de reacción]]. La ganancia última $K_u$ coincide con el límite de estabilidad de [[Routh Hurwitz/index | Routh-Hurwitz]] y con el cruce del eje imaginario del [[Lugar Raices/index | lugar de raíces]].

---

## Ejemplo

> [!ejemplo]
> **De $K_u$, $P_u$ al PID, y verificación analítica.** Una planta $G(s)=\dfrac{1}{(s+1)^3}$ en lazo cerrado con ganancia proporcional $K_p$. Hallar $K_u$ y $P_u$ y sintonizar un PID.
>
> ![[zn_oscilacion_sostenida.svg|550]]
>
> **Paso 1 — Ecuación característica** del lazo $1+K_p\,G(s)=0$:
> $$(s+1)^3+K_p=0\;\Longrightarrow\; s^3+3s^2+3s+(1+K_p)=0.$$
>
> **Paso 2 — Límite de estabilidad por Routh.** La fila $s^1$ se anula cuando el producto de extremos iguala al de medios:
> $$3\cdot 3 = 1\cdot(1+K_p)\;\Longrightarrow\; 9 = 1+K_p\;\Longrightarrow\; \boxed{K_u=8}.$$
>
> **Paso 3 — Frecuencia de oscilación.** En $K_u$ los polos están en $\pm j\omega$; de la fila auxiliar $3s^2+(1+K_u)=0$:
> $$3s^2+9=0\;\Longrightarrow\; s^2=-3\;\Longrightarrow\; \omega_{pc}=\sqrt{3}\approx 1.732\ \text{rad/s}.$$
>
> **Paso 4 — Periodo último:**
> $$P_u=\frac{2\pi}{\omega_{pc}}=\frac{2\pi}{\sqrt{3}}\approx 3.63\ \text{s}.$$
>
> **Paso 5 — Tabla ZN para PID** ($K_p=0.6K_u$, $T_i=P_u/2$, $T_d=P_u/8$):
> $$K_p=0.6\cdot 8=4.8,\qquad T_i=\frac{3.63}{2}=1.81\ \text{s},\qquad T_d=\frac{3.63}{8}=0.45\ \text{s}.$$
>
> **Paso 6 — Ganancias en forma paralela** ($K_i=K_p/T_i$, $K_d=K_p T_d$):
> $$K_i=\frac{4.8}{1.81}=2.65\ \text{s}^{-1},\qquad K_d=4.8\cdot 0.45=2.18\ \text{s}.$$
> Con un PI saldría $K_p=0.45K_u=3.6$ y $T_i=P_u/1.2=3.02\ \text{s}$. Son ganancias **iniciales**: el sobrepico $\sim25\%$ pide ajuste fino.

---

## En qué consiste

> [!teoria]
> Con las acciones I y D anuladas ($T_i=\infty$, $T_d=0$) el lazo queda solo proporcional. Al subir $K_p$, los polos de lazo cerrado se desplazan hacia el semiplano derecho; existe un valor crítico $K_u$ para el cual **un par de polos cae justo sobre el eje imaginario** $\pm j\omega_{pc}$. Ahí la respuesta es una oscilación sostenida (ni crece ni decae) de periodo $P_u=2\pi/\omega_{pc}$. Ese par $(K_u,P_u)$ caracteriza la dinámica de la planta en su frecuencia crítica y basta para fijar el PID — sin necesidad de modelo si el ensayo es experimental.

> [!algoritmo]
> 1. Anular las acciones I y D ($T_i=\infty$, $T_d=0$): control **solo proporcional**.
> 2. Aumentar $K_p$ gradualmente hasta que la salida oscile con **amplitud constante**.
> 3. Registrar la **ganancia última** $K_u=K_p$ y el **periodo último** $P_u$ de la oscilación.
> 4. Sustituir $K_u$ y $P_u$ en la **tabla de Ziegler-Nichols**.

> [!info] Tabla de Ziegler-Nichols (oscilación sostenida)
> | Controlador | $K_p$ | $T_i$ | $T_d$ |
> |---|---|---|---|
> | P | $0.5\,K_u$ | $\infty$ | $0$ |
> | PI | $0.45\,K_u$ | $P_u/1.2$ | $0$ |
> | PID | $0.6\,K_u$ | $P_u/2$ | $P_u/8$ |
>
> Recordar $K_i=K_p/T_i$ y $K_d=K_p T_d$.

> [!teorema] $K_u$ y $P_u$ son el límite de estabilidad
> La ganancia última $K_u$ es exactamente el $K_p$ que sitúa los polos de lazo cerrado **sobre el eje imaginario** — el mismo valor que dan [[Routh Hurwitz/index | Routh-Hurwitz]] (anulación de la primera columna) y el [[Lugar Raices/index | cruce del eje imaginario]] del lugar de raíces. El periodo se liga a la frecuencia de cruce:
> $$P_u=\frac{2\pi}{\omega_{pc}},$$
> donde $\omega_{pc}$ es también la frecuencia de [[Margenes MF MG | cruce de fase]] ($-180^\circ$) del Nyquist.

---

## Limitaciones

> [!warning]
> 1. **Peligroso:** llevar el proceso a oscilación sostenida puede ser inviable o dañino en plantas críticas o costosas.
> 2. **Sobrepico alto:** apunta a decaimiento de $1/4$ de amplitud, $\sim25\%$ de sobrepico; requiere ajuste fino.
> 3. **No siempre existe $K_u$:** plantas de primer o segundo orden puro no oscilan ($K_u$ infinito); para esos casos usar la [[Ziegler Nichols Curva Reaccion | curva de reacción]].
> 4. **Ventaja:** no necesita modelo de la planta; basta el ensayo experimental.

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Ensayo | $K_p$ creciente en **lazo cerrado** |
> | Se leen | $K_u$ (ganancia última), $P_u$ (periodo último) |
> | Relación | $P_u=2\pi/\omega_{pc}$, con polos en $\pm j\omega_{pc}$ |
> | PID | $K_p=0.6K_u$, $T_i=P_u/2$, $T_d=P_u/8$ |
> | Equivale a | límite de Routh-Hurwitz / cruce del eje imaginario |
> | Precisión | baja (sobrepico $\sim25\%$) |

> [!corolario]
> El método reduce toda la sintonización a un único par de números $(K_u,P_u)$ medibles en lazo cerrado, que es el límite de estabilidad de la planta. Es directo y no requiere modelo, pero lleva el proceso al borde de la inestabilidad y deja un sobrepico elevado; cuando ese riesgo no es aceptable, la [[Ziegler Nichols Curva Reaccion | curva de reacción]] en lazo abierto es la alternativa.

> [!referencia]
> - Método alternativo en lazo abierto: [[Ziegler Nichols Curva Reaccion]].
> - $K_u$ como límite de estabilidad: [[Routh Hurwitz/index]] · [[Lugar Raices/index]] · [[Criterio Nyquist]].
> - Frecuencia de cruce de fase: [[Margenes MF MG]].
> - Marco y ajuste posterior: [[Sintonizacion/index]] · [[PID]].
