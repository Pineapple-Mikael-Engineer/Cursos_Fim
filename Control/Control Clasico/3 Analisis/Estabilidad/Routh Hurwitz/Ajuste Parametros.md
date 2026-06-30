---
title: Ajuste de Parámetros con Routh-Hurwitz
order: 3
tags:
  - control-clasico
  - teoria
  - analisis
  - estabilidad
  - routh-hurwitz
draft: false
aliases:
  - rango de estabilidad
  - ajuste parametros routh
  - ganancia crítica
---

# Ajuste de Parámetros con Routh-Hurwitz

> [!definicion]
> Cuando la ecuación característica $1+G(s)H(s)=0$ depende de un parámetro $K$, la tabla de Routh se construye con elementos en función de $K$. Imponer que **toda la primera columna sea positiva** da las desigualdades cuyo intersección es el **rango de estabilidad**. En el extremo del rango, $K=K_{cr}$, una fila se anula: el polinomio auxiliar entrega los polos $\pm j\omega$ y la **frecuencia de oscilación** $\omega$.

> [!info]
> Aplicación de diseño del criterio de [[index | Routh-Hurwitz]] sobre la [[Construccion Tabla | tabla]]. La [[Condicion Necesaria | condición necesaria]] acota $K$ antes de construirla; en $K_{cr}$ aparece el Caso 2 de [[Casos Especiales | casos especiales]].

---

## Ejemplo

> [!ejemplo] Rango de ganancia estable
> ![[routh_ajuste_k_rango.svg|600]]
>
> Routh delimita el intervalo de $K$ que mantiene todos los polos en el semiplano izquierdo; al alcanzar $K_{cr}$ un par de polos cruza al eje imaginario y el sistema entra en oscilación sostenida.

> [!ejemplo] Hallar el rango, $K_{cr}$ y $\omega$
> Realimentación unitaria con $G(s)=\dfrac{K}{s(s+1)(s+2)}$.
>
> **Paso 1 — Ecuación característica.**
> $$1+G(s)=0\;\Rightarrow\; s(s+1)(s+2)+K=0\;\Rightarrow\; P(s)=s^3+3s^2+2s+K.$$
>
> **Paso 2 — Filtro de condición necesaria.** Todos los coeficientes $>0$ exige $K>0$.
>
> **Paso 3 — Tabla de Routh.**
> $$
> \begin{array}{c|cc}
> s^3 & 1 & 2 \\
> s^2 & 3 & K \\
> s^1 & \dfrac{3\cdot2-1\cdot K}{3}=\dfrac{6-K}{3} & 0 \\
> s^0 & K &
> \end{array}
> $$
>
> **Paso 4 — Condiciones de la primera columna $>0$.**
> $$\frac{6-K}{3}>0\;\Rightarrow\;K<6,\qquad K>0.$$
> **Rango de estabilidad:** $\boxed{0<K<6}$.
>
> **Paso 5 — Ganancia crítica.** El borde superior anula la fila $s^1$: $K_{cr}=6$. Allí la fila $s^1$ es cero (Caso 2).
>
> **Paso 6 — Frecuencia de oscilación.** Polinomio auxiliar de la fila $s^2$ con $K=K_{cr}=6$:
> $$Q(s)=3s^2+K\big|_{K=6}=3s^2+6=3(s^2+2)=0\;\Rightarrow\;s=\pm j\sqrt{2}.$$
> En $K_{cr}=6$ el sistema oscila de forma sostenida a $\omega=\sqrt{2}\approx1.41\ \text{rad/s}$. Para $K>6$ esos polos pasan a $\Re>0$ → inestable.

> [!ejemplo] Realimentación con ganancia (orden 2)
> $G(s)=\dfrac{1}{s(s+2)}$, $H(s)=K$.
> $$1+\frac{K}{s(s+2)}=0\;\Rightarrow\;P(s)=s^2+2s+K.$$
> $$
> \begin{array}{c|cc}
> s^2 & 1 & K \\
> s^1 & 2 & 0 \\
> s^0 & K &
> \end{array}
> $$
> Primera columna $>0$: $K>0$. No hay cota superior (orden 2 con todos los coeficientes positivos es estable), así que el rango es $K>0$ sin ganancia crítica finita.

---

## Algoritmo

> [!algoritmo] Rango de un parámetro
> 1. Formar la ecuación característica $1+G(s)H(s)=0$ y su polinomio $P(s)$ en función de $K$.
> 2. Aplicar la [[Condicion Necesaria | condición necesaria]] para una cota inicial de $K$.
> 3. Construir la [[Construccion Tabla | tabla de Routh]] con elementos dependientes de $K$.
> 4. Imponer cada elemento de la primera columna $>0$ (si $a_n>0$).
> 5. Resolver las desigualdades e **intersecar** los rangos.
> 6. En cada extremo, igualar a cero el elemento que se anula → $K_{cr}$; el polinomio auxiliar de la fila superior da los $\pm j\omega$ y la frecuencia de oscilación.

> [!info] Ganancia crítica y frecuencia
> $K_{cr}$ es el valor frontera donde el sistema es **marginalmente estable** (un par de polos sobre el eje imaginario). La frecuencia $\omega$ de esos polos es la de la oscilación sostenida que se observa justo en $K_{cr}$ —base del método de sintonía de Ziegler-Nichols por oscilación.

> [!info] En MATLAB
> ```matlab
> K = 6;                       % probar la ganancia critica
> P = [1 3 2 K];               % s^3 + 3s^2 + 2s + K
> roots(P)                     % esperar +-j*sqrt(2) y un polo real
> ```

---

## Limitaciones

> [!warning]
> 1. Supone que $P(s)$ es **lineal en $K$**; si $K$ aparece en varios coeficientes de forma no lineal, las desigualdades se complican.
> 2. Con **varios parámetros** el rango es una región en el espacio de parámetros, no un intervalo.
> 3. Da el rango de **estabilidad**, no el desempeño transitorio (sobrepico, asentamiento).
> 4. Conviene combinar con el [[Lugar Raices/index | lugar de las raíces]] para ver cómo migran los polos dentro del rango.

## Resumen

> [!resumen]
> | Magnitud | Cómo se obtiene |
> |---|---|
> | Rango de $K$ | intersección de "1.ª columna $>0$" |
> | $K_{cr}$ | valor que anula un elemento de la 1.ª columna |
> | $\omega$ de oscilación | raíces $\pm j\omega$ del aux. $Q(s)$ en $K_{cr}$ |
> | Ejemplo | $0<K<6$, $K_{cr}=6$, $\omega=\sqrt{2}$ |

> [!corolario]
> El ajuste de parámetros convierte Routh en una herramienta de diseño: cada condición de signo es una restricción sobre $K$, y su intersección es el margen seguro. La frontera $K_{cr}$ no solo marca el límite de estabilidad sino que, vía el polinomio auxiliar, regala la frecuencia exacta de la oscilación crítica.

> [!referencia]
> - Construcción base: [[Construccion Tabla]].
> - Criterio y enunciado: [[index]].
> - Fila nula en $K_{cr}$: [[Casos Especiales]].
> - Filtro previo de $K$: [[Condicion Necesaria]].
> - Migración de polos: [[Lugar Raices/index]].
