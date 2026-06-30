---
title: Puntos de Ruptura (Breakaway y Break-in)
order: 3
tags:
  - control-clasico
  - diseño
  - lugar-raices
draft: false
aliases:
  - puntos ruptura
  - breakaway
  - break-in
  - punto separacion
---

# Puntos de Ruptura (Breakaway y Break-in)

> [!definicion]
> Puntos del [[index | LGR]] donde dos o más ramas se encuentran sobre el eje real y se separan hacia el plano complejo (**breakaway**) o llegan desde él al eje real (**break-in**). Se localizan resolviendo
> $$\frac{dK}{ds}=0,\qquad K=-\frac{1}{G(s)H(s)},$$
> y quedándose solo con las raíces que caen sobre un tramo del LGR. En un breakaway $K$ es máximo local; en un break-in, mínimo local.

> [!info]
> Regla 5 de [[Reglas Construccion | construcción del LGR]], sección [[index | lugar de las raíces]]. Aparecen en los tramos del eje real que sí son LGR ([[Trayectoria eje real y Asintotas | regla del eje real]]). Verificar siempre las raíces con la regla del eje real antes de aceptarlas.

---

## Ejemplo

> [!ejemplo]
> **Sistema de segundo orden: $G(s)H(s)=\dfrac{K}{s(s+2)}$.**
>
> ![[lgr_punto_ruptura.svg|600]]
>
> **Paso 1 — Despejar $K$** de $1+KG(s)H(s)=0$:
> $$K=-s(s+2)=-s^2-2s.$$
>
> **Paso 2 — Derivar e igualar a cero:**
> $$\frac{dK}{ds}=-2s-2=0\Rightarrow s=-1.$$
>
> **Paso 3 — Verificar** con la [[Trayectoria eje real y Asintotas | regla del eje real]]: $s=-1\in(-2,0)$, tramo del LGR. ✓ Es un **breakaway**.
>
> **Paso 4 — Valor de $K$** en el punto: $K=-(-1)(-1+2)=-(-1)(1)=1$.
>
> **Paso 5 — Comprobación numérica** (un mismo $K$ da dos $s$ a cada lado del breakaway):
>
> | $s$ | $K=-s(s+2)$ |
> |---|---|
> | $-0.5$ | $-(-0.5)(1.5)=0.75$ |
> | $-1.0$ | $1.00$ (máximo) |
> | $-1.5$ | $-(-1.5)(0.5)=0.75$ |
>
> $K=0.75$ aparece en $s=-0.5$ y $s=-1.5$ (las dos ramas); en $s=-1$ alcanza su máximo $K=1$ y las ramas se separan.

> [!ejemplo]
> **Tres polos reales: $G(s)H(s)=\dfrac{K}{s(s+2)(s+4)}$.**
>
> **Paso 1:** $K=-s(s+2)(s+4)=-(s^3+6s^2+8s)$.
>
> **Paso 2:** $\dfrac{dK}{ds}=-(3s^2+12s+8)=0\Rightarrow 3s^2+12s+8=0$.
>
> **Paso 3 — Resolver:**
> $$s=\frac{-12\pm\sqrt{144-96}}{6}=\frac{-12\pm\sqrt{48}}{6}=-2\pm\frac{2\sqrt3}{3}\approx-0.845,\;-3.155.$$
>
> **Paso 4 — Verificar.** LGR sobre el eje real: $(-2,0)$ y $(-\infty,-4)$.
> - $s\approx-0.845\in(-2,0)$ → **breakaway** válido.
> - $s\approx-3.155\in(-4,-2)$, que **no** es LGR → **descartar**.

> [!ejemplo]
> **Con un cero: $G(s)H(s)=\dfrac{K(s+3)}{s(s+2)}$.**
>
> **Paso 1:** $K=-\dfrac{s(s+2)}{s+3}$.
>
> **Paso 2 — Regla del cociente**, numerador de $dK/ds$ igualado a cero:
> $$(2s+2)(s+3)-s(s+2)=0\Rightarrow(2s^2+8s+6)-(s^2+2s)=s^2+6s+6=0.$$
>
> **Paso 3 — Resolver:**
> $$s=\frac{-6\pm\sqrt{36-24}}{2}=-3\pm\sqrt3\approx-1.268,\;-4.732.$$
>
> **Paso 4 — Verificar.** Polos $0,-2$; cero $-3$. LGR en $(-2,0)$ y $(-\infty,-3)$.
> - $s\approx-1.268\in(-2,0)$ → en LGR; pero el tramo $(-2,0)$ va de polo a polo y no presenta separación... aquí en realidad es el **breakaway** entre los polos $0$ y $-2$. ✓
> - $s\approx-4.732\in(-\infty,-3)$ → **break-in** (las ramas vuelven al eje real para terminar en el cero $-3$ y en $-\infty$). ✓

---

## Demostración

> [!teorema] Condición $\dfrac{dK}{ds}=0$
> En todo punto de ruptura $s_0$ del LGR sobre el eje real, $\left.\dfrac{dK}{ds}\right|_{s_0}=0$.

> [!demostracion] Paso 1 — $K$ como función de $s$
> De $1+KG(s)H(s)=0$ se despeja $K=-1/G(s)H(s)$. A lo largo de una rama, $s$ varía y $K$ varía continuamente; sobre el eje real, $K$ es real.

> [!demostracion] Paso 2 — Extremo de $K$
> En un punto de ruptura **dos ramas se encuentran**: a un mismo $K$ le corresponden dos valores de $s$. Recorriendo el eje real, $K$ crece hasta el encuentro y luego decrece (breakaway) o al revés (break-in): tiene un **extremo local**.

> [!demostracion] Paso 3 — Derivada nula
> En un extremo local de una función diferenciable, $\dfrac{dK}{ds}=0$. Equivalente: $\dfrac{ds}{dK}\to\infty$ (la trayectoria gira bruscamente para salir del eje), y $\dfrac{dK}{ds}=1/\dfrac{ds}{dK}=0$. $\blacksquare$

> [!info] Tipo de extremo
> - **Breakaway:** $K$ máximo local; las ramas dejan el eje real.
> - **Break-in:** $K$ mínimo local; las ramas regresan al eje real.

---

## Receta

> [!algoritmo] Cálculo práctico
> 1. Despejar $K=-1/G(s)H(s)=f(s)$.
> 2. Derivar e igualar: $\dfrac{dK}{ds}=0$ (con cociente, basta anular el numerador).
> 3. Resolver el polinomio resultante.
> 4. **Descartar** las raíces que no caen en un tramo del LGR (regla del eje real) o no son reales (salvo ruptura compleja).
> 5. Si interesa, evaluar $K=f(s_0)$ en cada punto válido.

> [!info] En MATLAB
> ```matlab
> syms s K
> G = 1/(s*(s+2));
> Kf = -1/G;                 % K(s)
> sol = solve(diff(Kf,s)==0, s)   % candidatos a ruptura
> ```

---

## Limitaciones

> [!warning]
> 1. $\dfrac{dK}{ds}=0$ puede dar raíces que **no** están en el LGR → verificar siempre.
> 2. No todo cero de $dK/ds$ es ruptura visible (puede ser inflexión).
> 3. En orden alto el polinomio es difícil de resolver a mano.
> 4. Puede haber rupturas **complejas** (polos/ceros complejos): la condición sigue valiendo con $s$ complejo.

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Condición | $\dfrac{dK}{ds}=0$, $K=-1/G(s)H(s)$ |
> | Breakaway | $K$ máximo local (ramas salen del eje) |
> | Break-in | $K$ mínimo local (ramas vuelven al eje) |
> | Validación | la raíz debe caer en un tramo del LGR |
> | $G=\dfrac{K}{s(s+2)}$ | $s=-1$, $K=1$ |
> | $G=\dfrac{K}{s(s+2)(s+4)}$ | $s\approx-0.845$ (el otro se descarta) |

> [!corolario]
> Los puntos de ruptura son los extremos de $K$ a lo largo del eje real: se obtienen de $dK/ds=0$ y se aceptan solo si pertenecen al LGR. Marcan dónde las ramas dejan o reencuentran el eje real, conectando la geometría del eje real con las asíntotas y el cruce por $j\omega$.

> [!referencia]
> - Contexto: [[Reglas Construccion]] y [[index]].
> - Tramos válidos del eje real: [[Trayectoria eje real y Asintotas]].
> - Origen analítico: [[Condicion Angulo Magnitud]].
