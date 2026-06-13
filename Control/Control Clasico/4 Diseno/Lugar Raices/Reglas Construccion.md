---
title: Reglas de Construcción del Lugar de las Raíces
tags:
  - control-clasico
  - diseño
  - lugar-raices
draft: false
aliases:
  - reglas construccion
  - construir root locus
  - reglas lgr
---

# Reglas de Construcción del Lugar de las Raíces

> [!definicion]
> Conjunto de siete reglas que permiten trazar a mano el [[index | lugar de las raíces]] de $G(s)H(s)$ sin resolver $1+KG(s)H(s)=0$ para cada $K$. Todas derivan de la [[Condicion Angulo Magnitud | condición de ángulo]] $\sum\angle(s+z_i)-\sum\angle(s+p_j)=180^\circ(2k+1)$. Con $n$ polos y $m$ ceros: hay $n$ ramas, simétricas al eje real, sobre tramos del eje real con paridad impar a la derecha, $n-m$ asíntotas de centro $\sigma_a$, más puntos de ruptura, ángulos de salida/llegada y cruces con el eje imaginario.

> [!info]
> Receta central de la sección [[index | lugar de las raíces]]. Cada regla con detalle vive en una nota hermana: [[Trayectoria eje real y Asintotas | eje real y asíntotas]], [[Puntos Ruptura | puntos de ruptura]], [[Angulos Salida Llegada | ángulos de salida/llegada]], [[Cruce Eje Imaginario | cruce con el eje imaginario]].

---

## Ejemplo

> [!ejemplo]
> **Trazar el LGR de $G(s)H(s)=\dfrac{K}{s(s+2)(s+4)}$ aplicando las reglas en orden.**
>
> ![[root_locus_completo.gif|600]]
>
> **Regla 1 — Ramas.** Polos en $s=0,-2,-4$ (tres polos, $n=3$); sin ceros ($m=0$). → **3 ramas**, cada una nace en un polo cuando $K=0$.
>
> **Regla 2 — Simetría.** El LGR es simétrico respecto al eje real (los coeficientes de la característica son reales).
>
> **Regla 3 — Eje real.** Punto del eje real $\in$ LGR si tiene un número **impar** de polos+ceros a su derecha:
>
> | Tramo | Polos/ceros a la derecha | ¿Impar? | ¿LGR? |
> |---|---|---|---|
> | $(0,\infty)$ | 0 | No | No |
> | $(-2,0)$ | 1 ($s{=}0$) | Sí | **Sí** |
> | $(-4,-2)$ | 2 | No | No |
> | $(-\infty,-4)$ | 3 | Sí | **Sí** |
>
> **Regla 4 — Asíntotas.** Grado relativo $n-m=3$ → 3 asíntotas.
> $$\sigma_a=\frac{\sum p_j-\sum z_i}{n-m}=\frac{(0-2-4)-0}{3}=\frac{-6}{3}=-2,$$
> $$\theta_a=\frac{180^\circ(2k+1)}{3}\Rightarrow 60^\circ,\;180^\circ,\;300^\circ\quad(k=0,1,2).$$
>
> **Regla 5 — Puntos de ruptura.** $K=-s(s+2)(s+4)=-(s^3+6s^2+8s)$:
> $$\frac{dK}{ds}=-(3s^2+12s+8)=0\Rightarrow s=-2\pm\tfrac{2\sqrt3}{3}\approx-0.845,\;-3.155.$$
> Solo $s\approx-0.845$ cae en un tramo del LGR del eje real $(-2,0)$ → **breakaway** ahí. ($s\approx-3.155$ está en $(-4,-2)$, que no es LGR, y se descarta.)
>
> **Regla 7 — Cruce con el eje imaginario.** Característica $s^3+6s^2+8s+K=0$. Con $s=j\omega$, separando real/imaginaria sale $\omega^2=8$, $K=6\cdot8=48$. → cruza en $s=\pm j\sqrt8\approx\pm j2.83$ con $K_{\text{crítico}}=48$.
>
> **Síntesis del trazo.** Tres ramas parten de $0,-2,-4$; dos se acercan en $(-2,0)$, se separan en $s\approx-0.845$ hacia el plano complejo y suben siguiendo las asíntotas de $\pm60^\circ$ centradas en $\sigma_a=-2$, cruzando $j\omega$ en $\pm j2.83$ con $K=48$; la tercera escapa por la asíntota de $180^\circ$ a lo largo del eje real izquierdo.

---

## En qué consiste

> [!teoria] Las siete reglas
> Sea $G(s)H(s)=\dfrac{K\prod(s+z_i)}{\prod(s+p_j)}$ con $n$ polos y $m$ ceros.
>
> | # | Regla | Enunciado | Detalle |
> |---|---|---|---|
> | 1 | Ramas | $n$ ramas; nacen en los polos ($K=0$) y mueren en ceros finitos o en $\infty$ ($K\to\infty$). | — |
> | 2 | Simetría | El LGR es simétrico respecto al eje real (polos complejos en pares conjugados). | — |
> | 3 | Eje real | $s$ real $\in$ LGR si el nº de polos+ceros a su derecha es impar. | [[Trayectoria eje real y Asintotas]] |
> | 4 | Asíntotas | $\sigma_a=\dfrac{\sum p_j-\sum z_i}{n-m}$, $\theta_a=\dfrac{180^\circ(2k+1)}{n-m}$. | [[Trayectoria eje real y Asintotas]] |
> | 5 | Ruptura | $\dfrac{dK}{ds}=0$ con $K=-1/G(s)H(s)$. | [[Puntos Ruptura]] |
> | 6 | Salida/llegada | $\theta_{\text{sal}}=180^\circ+\sum\angle(p_j-z_i)-\sum_{i\neq j}\angle(p_j-p_i)$. | [[Angulos Salida Llegada]] |
> | 7 | Cruce $j\omega$ | $K$ y $\omega$ del cruce vía Routh-Hurwitz o $s=j\omega$. | [[Cruce Eje Imaginario]] |

> [!ejemplo] Reglas 1-3 en un caso mínimo
> $G(s)H(s)=\dfrac{K}{s(s+2)}$: polos $0,-2$ → **2 ramas** (regla 1), simétricas (regla 2).
>
> ![[lgr_ejemplo_ramas.svg|600]]
>
> Eje real (regla 3): solo el tramo $(-2,0)$ tiene un nº impar (1) de polos a la derecha → es LGR.
>
> ![[lgr_eje_real.svg|600]]

> [!ejemplo] Reglas 4 y 5 en el mismo caso
> $n-m=2$ → 2 asíntotas. $\sigma_a=\dfrac{0+(-2)}{2}=-1$; $\theta_a=90^\circ,270^\circ$ (vertical).
>
> ![[lgr_asintotas.svg|400]]
>
> Punto de ruptura: $K=-s(s+2)$, $\dfrac{dK}{ds}=-(2s+2)=0\Rightarrow s=-1$ (cae en $(-2,0)$, válido).
>
> ![[lgr_punto_ruptura.svg|500]]

---

## Receta

> [!algoritmo] Orden de aplicación
> 1. Factorizar $G(s)H(s)$; marcar polos ($\times$) y ceros ($\circ$). Contar $n$, $m$.
> 2. **Regla 1-2:** dibujar $n$ ramas, recordar la simetría.
> 3. **Regla 3:** sombrear los tramos del eje real con paridad impar a la derecha.
> 4. **Regla 4:** calcular $\sigma_a$ y los $\theta_a$; dibujar las $n-m$ asíntotas.
> 5. **Regla 5:** resolver $dK/ds=0$ y quedarse con las raíces que caen en tramos del LGR.
> 6. **Regla 6:** ángulos de salida/llegada en polos/ceros complejos.
> 7. **Regla 7:** cruces con $j\omega$ y $K_{\text{crítico}}$.

> [!info] En MATLAB
> ```matlab
> G = tf(K_unit, conv([1 0], conv([1 2],[1 4])));  % K/(s(s+2)(s+4))
> rlocus(G)            % traza el LGR completo
> [K,poles] = rlocfind(G)   % K y polos en un punto que elijas
> ```

---

## Limitaciones

> [!warning]
> 1. Las reglas suponen realimentación **negativa**; con $H(s)\neq1$ se usa $G(s)H(s)$.
> 2. Las reglas 3-7 requieren práctica; cada una tiene su nota hija.
> 3. El LGR muestra polos de lazo cerrado, no sus **ceros**.
> 4. Solo es válido para $K$ **real y positivo**.

## Resumen

> [!resumen]
> | Regla | Fórmula clave |
> |---|---|
> | 1 Ramas | $n$ (= nº de polos) |
> | 2 Simetría | eje real |
> | 3 Eje real | nº impar de polos+ceros a la derecha |
> | 4 Asíntotas | $\sigma_a=\dfrac{\sum p-\sum z}{n-m}$, $\theta_a=\dfrac{180^\circ(2k+1)}{n-m}$ |
> | 5 Ruptura | $\dfrac{dK}{ds}=0$ |
> | 6 Salida/llegada | condición de ángulo en polos/ceros complejos |
> | 7 Cruce $j\omega$ | Routh-Hurwitz o $s=j\omega$ |

> [!corolario]
> Trazar el LGR es aplicar las siete reglas en orden: contar ramas, sombrear el eje real, levantar las asíntotas desde $\sigma_a$, fijar los puntos de ruptura y los cruces con $j\omega$. Todas son consecuencia directa de la [[Condicion Angulo Magnitud | condición de ángulo]].

> [!referencia]
> - Marco: [[index]].
> - Origen de las reglas: [[Condicion Angulo Magnitud]].
> - Reglas 3-4: [[Trayectoria eje real y Asintotas]]; regla 5: [[Puntos Ruptura]]; regla 6: [[Angulos Salida Llegada]]; regla 7: [[Cruce Eje Imaginario]].
