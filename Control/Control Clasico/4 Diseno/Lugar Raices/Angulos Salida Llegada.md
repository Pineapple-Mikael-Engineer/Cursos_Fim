---
title: Ángulos de Salida y Llegada
tags:
  - control-clasico
  - diseno
  - lugar-raices
draft: false
aliases:
  - ángulos de salida
  - ángulos de llegada
  - departure arrival angles
---

# Ángulos de Salida y Llegada

> [!definicion]
> El **ángulo de salida** $\theta_d$ es la dirección con que una rama del [[Lugar Raices/index | lugar de raíces]] abandona un polo complejo (en $K\to0^+$); el **ángulo de llegada** $\theta_a$, con la que una rama llega a un cero complejo (en $K\to\infty$). Se obtienen aplicando la [[Condicion Angulo Magnitud | condición de ángulo]] a un punto infinitesimalmente cercano al polo/cero:
> $$\theta_d = 180^\circ + \sum_{\text{ceros}} \angle(p_i - z_j) - \sum_{\substack{\text{polos}\\ j\neq i}} \angle(p_i - p_j),\qquad \theta_a = 180^\circ - \sum_{\substack{\text{ceros}\\ j\neq i}} \angle(z_i - z_j) + \sum_{\text{polos}} \angle(z_i - p_j).$$

> [!info]
> Regla de trazado del [[Lugar Raices/index | lugar de raíces]], hermana de [[Trayectoria eje real y Asintotas]], [[Puntos Ruptura]] y [[Cruce Eje Imaginario]]. Solo hace falta en polos/ceros **complejos**; en los reales la rama sale o llega sobre el propio eje real ($0^\circ$ o $180^\circ$).

---

## Ejemplo

> [!ejemplo]
> **Polos complejos sin ceros.** $G(s)H(s)=\dfrac{K}{(s+1+j2)(s+1-j2)}$. Hallar el ángulo de salida del polo $p_1=-1+j2$.
>
> **Paso 1 — Identificar polos y ceros.** Polos $p_1=-1+j2$, $p_2=-1-j2$ (conjugados). No hay ceros.
>
> **Paso 2 — Vector desde los demás polos hasta $p_1$.** Solo está $p_2$:
> $$p_1-p_2=(-1+j2)-(-1-j2)=j4\;\Rightarrow\;\angle(p_1-p_2)=90^\circ.$$
>
> **Paso 3 — Aplicar la fórmula** (sin ceros, el sumatorio de ceros es $0$):
> $$\theta_d=180^\circ+0-\angle(p_1-p_2)=180^\circ-90^\circ=90^\circ.$$
>
> **Paso 4 — Interpretar.** La rama sale **verticalmente hacia arriba** desde $-1+j2$. Por simetría conjugada, desde $-1-j2$ sale hacia abajo ($\theta_d=-90^\circ$). Aquí coincide con el eje real porque los dos polos están alineados verticalmente; en general no es vertical.

> [!ejemplo]
> **Con un cero y un tercer polo.** $G(s)H(s)=\dfrac{K\,(s+2)}{(s+3)(s+1+j1)(s+1-j1)}$. Ángulo de salida del polo $p_1=-1+j1$.
>
> **Paso 1 — Catálogo de singularidades.** Cero $z_1=-2$; polos $p_1=-1+j1$, $p_2=-1-j1$, $p_3=-3$.
>
> **Paso 2 — Ángulo del cero hacia $p_1$:**
> $$p_1-z_1=(-1+j1)-(-2)=1+j1\;\Rightarrow\;\angle=\arctan\frac{1}{1}=45^\circ.$$
>
> **Paso 3 — Ángulos de los otros polos hacia $p_1$:**
> $$p_1-p_2=(-1+j1)-(-1-j1)=j2\;\Rightarrow\;\angle=90^\circ,$$
> $$p_1-p_3=(-1+j1)-(-3)=2+j1\;\Rightarrow\;\angle=\arctan\tfrac{1}{2}\approx26.6^\circ.$$
>
> **Paso 4 — Fórmula del ángulo de salida:**
> $$\theta_d=180^\circ+\underbrace{45^\circ}_{\text{cero}}-\underbrace{(90^\circ+26.6^\circ)}_{\text{polos}}=180^\circ+45^\circ-116.6^\circ=108.4^\circ.$$
>
> **Paso 5 — Interpretar.** La rama abandona $-1+j1$ con $108.4^\circ$ (hacia arriba y ligeramente a la izquierda): se aleja del eje real hacia el semiplano izquierdo, indicio de que el cero en $-2$ atrae el lugar y favorece la estabilidad al subir $K$.

> [!ejemplo]
> **Lectura gráfica del ángulo de salida.**
>
> ![[lgr_angulo_salida.svg|550]]
>
> Las ramas abandonan los polos complejos con el ángulo $\theta_d$ calculado, **no** horizontalmente. El vector suma de contribuciones de los demás polos/ceros fija la dirección de partida.

---

## En qué consiste

> [!teoria]
> El lugar de raíces es el conjunto de puntos $s$ que cumplen la [[Condicion Angulo Magnitud | condición de ángulo]] $\sum\angle(s-z_j)-\sum\angle(s-p_j)=\pm180^\circ(2k+1)$. Para esbozarlo cerca de un polo complejo $p_i$ basta saber **en qué dirección** arranca la rama: ese es $\theta_d$. La fórmula sale de exigir la condición de ángulo en un punto $s$ pegado a $p_i$.

> [!teorema] Ángulo de salida de un polo complejo $p_i$
> $$\theta_d = 180^\circ + \sum_{\text{ceros}} \angle(p_i - z_j) - \sum_{\substack{\text{polos}\\ j\neq i}} \angle(p_i - p_j).$$

> [!demostracion]
> **Paso 1 — Punto de prueba.** Sea $s=p_i+\varepsilon e^{j\theta_d}$ con $\varepsilon\to0^+$ un punto del lugar infinitamente cercano a $p_i$, alcanzado siguiendo la rama; el ángulo $\theta_d$ es justo la dirección de partida buscada.
>
> **Paso 2 — Condición de ángulo en $s$.**
> $$\sum_{\text{ceros}}\angle(s-z_j)-\sum_{\text{polos}}\angle(s-p_j)=\pm180^\circ.$$
>
> **Paso 3 — Separar el término propio.** El vector desde el propio polo es $s-p_i=\varepsilon e^{j\theta_d}$, cuyo ángulo es $\theta_d$. Para los demás factores, como $\varepsilon\to0$, el punto $s$ está prácticamente sobre $p_i$, así $\angle(s-z_j)\approx\angle(p_i-z_j)$ y $\angle(s-p_j)\approx\angle(p_i-p_j)$ para $j\neq i$:
> $$\sum_{\text{ceros}}\angle(p_i-z_j)-\sum_{\substack{\text{polos}\\ j\neq i}}\angle(p_i-p_j)-\theta_d=\pm180^\circ.$$
>
> **Paso 4 — Despejar.** Tomando $-180^\circ$ y reordenando:
> $$\theta_d=180^\circ+\sum_{\text{ceros}}\angle(p_i-z_j)-\sum_{\substack{\text{polos}\\ j\neq i}}\angle(p_i-p_j).\qquad\blacksquare$$

> [!teorema] Ángulo de llegada a un cero complejo $z_i$
> $$\theta_a = 180^\circ - \sum_{\substack{\text{ceros}\\ j\neq i}} \angle(z_i - z_j) + \sum_{\text{polos}} \angle(z_i - p_j).$$
> Misma deducción intercambiando el papel de polos y ceros: ahora el término propio es $\angle(s-z_i)=\theta_a$ y queda con signo opuesto.

> [!info] Por qué solo en complejos
> | Singularidad | Dirección de la rama |
> |---|---|
> | Polo/cero real | sobre el eje real ($0^\circ$ o $180^\circ$); la rama sale/llega horizontal |
> | Polo complejo | sale con $\theta_d$ (depende de los demás polos/ceros) |
> | Cero complejo | llega con $\theta_a$ |
>
> Los conjugados siempre dan $\theta_d$ (o $\theta_a$) **simétricos** respecto al eje real.

---

## Receta

> [!algoritmo]
> Para el ángulo de salida de un polo complejo $p_i$ (análogo para $\theta_a$ con un cero):
> 1. **Catalogar** todos los polos y ceros del lazo abierto $G(s)H(s)$.
> 2. **Vectores hacia $p_i$.** Calcular cada diferencia $p_i-z_j$ y $p_i-p_j$ ($j\neq i$) como número complejo.
> 3. **Ángulos.** Tomar el argumento de cada vector con $\arctan(\text{Im}/\text{Re})$, cuidando el cuadrante.
> 4. **Sumar.** $\theta_d=180^\circ+\sum\angle(\text{ceros})-\sum\angle(\text{polos})$.
> 5. **Conjugado.** El polo $\bar p_i$ sale con $-\theta_d$.

> [!info] En MATLAB
> ```matlab
> G = zpk([-2], [-3 -1+1i -1-1i], 1);
> rlocus(G)        % el trazado ya respeta los angulos de salida
> % verificacion del angulo de salida en p = -1+1i:
> p  = -1+1i;  z = -2;  pj = [-3, -1-1i];
> th = 180 + rad2deg(angle(p - z)) - sum(rad2deg(angle(p - pj)));
> mod(th,360)      % ~108.4 grados
> ```

---

## Para qué sirve

> [!info]
> El ángulo de salida indica **hacia dónde** parte la rama desde un polo complejo: ¿hacia el semiplano derecho (desestabiliza al subir $K$) o hacia la izquierda (estabiliza)? Es esencial para esbozar bien el lugar cerca de polos dominantes complejos y anticipar la evolución del [[Segundo Orden/index | amortiguamiento]].

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Salida (polo complejo $p_i$) | $\theta_d=180^\circ+\sum\angle(p_i-z_j)-\sum_{j\neq i}\angle(p_i-p_j)$ |
> | Llegada (cero complejo $z_i$) | $\theta_a=180^\circ-\sum_{j\neq i}\angle(z_i-z_j)+\sum\angle(z_i-p_j)$ |
> | Origen | [[Condicion Angulo Magnitud \| condición de ángulo]] en $s\to p_i$ |
> | Cuándo aplicarla | solo en polos/ceros complejos |
> | Conjugado | ángulo simétrico ($-\theta_d$) |

> [!corolario]
> El ángulo de salida/llegada no es más que la condición de ángulo evaluada al borde de un polo o cero complejo: $180^\circ$ más la suma de ángulos de los ceros menos la de los polos restantes. Fija la dirección de arranque de la rama y, con ella, si los polos dominantes complejos tienden hacia la estabilidad o la inestabilidad al crecer $K$.

> [!referencia]
> - Condición que los origina: [[Condicion Angulo Magnitud]].
> - Otras reglas de trazado: [[Reglas Construccion]] · [[Puntos Ruptura]] · [[Trayectoria eje real y Asintotas]].
> - Dónde la rama cruza a la inestabilidad: [[Cruce Eje Imaginario]].
