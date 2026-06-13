---
title: Condiciones de Ángulo y Magnitud
tags:
  - control-clasico
  - diseño
  - lugar-raices
draft: false
aliases:
  - condicion angulo
  - condicion magnitud
  - angulo y magnitud
---

# Condiciones de Ángulo y Magnitud

> [!definicion]
> Un punto $s$ del plano complejo pertenece al lugar de las raíces de $G(s)H(s)$ si y solo si cumple la **condición de ángulo**; sobre él, la **condición de magnitud** fija el valor de $K$. De $1+KG(s)H(s)=0\Rightarrow KG(s)H(s)=-1$:
> $$\boxed{\;\sum\angle(s+z_i)-\sum\angle(s+p_j)=180^\circ(2k+1)\;}\qquad\boxed{\;K=\frac{\prod\|s+p_j\|}{\prod\|s+z_i\|}\;}$$
> con $k=0,\pm1,\pm2,\dots$ La de ángulo decide **si** $s$ está en el LGR; la de magnitud, **con qué $K$**.

> [!info]
> Base operativa del [[index | lugar de las raíces]]: toda regla de trazado ([[Reglas Construccion | construcción]], [[Trayectoria eje real y Asintotas | eje real y asíntotas]], [[Puntos Ruptura | puntos de ruptura]], [[Angulos Salida Llegada | ángulos de salida/llegada]]) sale de aplicar la condición de ángulo. Los vectores $(s+p_j)$, $(s+z_i)$ van de cada polo/cero al punto de prueba $s$.

---

## Ejemplo

> [!ejemplo]
> **Verificar un punto y hallar su $K$.** Sea $G(s)H(s)=\dfrac{K}{s(s+2)}$. Comprobar si $s=-1$ pertenece al LGR y, en caso afirmativo, calcular $K$ ahí.
>
> ![[lgr_ejemplo_vectores.svg|600]]
>
> **Paso 1 — Polos y ceros.** Polos en $p_1=0$ y $p_2=2$ (es decir $s=0,\,-2$); sin ceros.
>
> **Paso 2 — Vectores hasta $s=-1$** (cada vector va del polo al punto):
> $$s+p_1=-1+0=-1\;(\text{módulo }1,\ \text{ángulo }180^\circ),\qquad s+p_2=-1+2=1\;(\text{módulo }1,\ \text{ángulo }0^\circ).$$
>
> **Paso 3 — Condición de ángulo** (sin ceros, solo restamos los de los polos):
> $$\sum\angle(s+z_i)-\sum\angle(s+p_j)=0-(180^\circ+0^\circ)=-180^\circ.$$
> $-180^\circ=180^\circ(2k+1)$ con $k=-1$ → es múltiplo impar de $180^\circ$. **$s=-1$ pertenece al LGR.** ✓
>
> **Paso 4 — Condición de magnitud** (producto de distancias a polos / a ceros; sin ceros el denominador es $1$):
> $$K=\frac{\|s+p_1\|\cdot\|s+p_2\|}{1}=\frac{1\cdot 1}{1}=1.$$
> En $s=-1$ la ganancia vale $K=1$; justo el [[Puntos Ruptura | punto de ruptura]] donde las dos ramas abandonan el eje real.
>
> **Comprobación.** La [[index | ecuación característica]] es $s^2+2s+K=0$; con $K=1$ da $(s+1)^2=0$, raíz doble en $s=-1$. Coincide. ✓
>
> ![[root_locus.gif|600]]
>
> La animación recorre $K$ de $0\to\infty$: las raíces parten de los polos $0$ y $-2$, se juntan en $s=-1$ (el punto que acabamos de verificar, $K=1$) y desde ahí suben por la vertical $\sigma=-1$ como par complejo conjugado.

> [!ejemplo]
> **Punto fuera del LGR.** Mismo $G(s)H(s)=\dfrac{K}{s(s+2)}$, probar $s=+1$.
>
> Vectores: $s+p_1=1$ (ángulo $0^\circ$), $s+p_2=3$ (ángulo $0^\circ$). Condición de ángulo:
> $$0-(0^\circ+0^\circ)=0^\circ\neq 180^\circ(2k+1).$$
> No es múltiplo impar de $180^\circ$ → **$s=1$ no pertenece al LGR**, lo que concuerda con la [[Trayectoria eje real y Asintotas | regla del eje real]] (cero polos/ceros a su derecha, paridad par).

---

## En qué consiste

> [!teoria]
> El LGR es el lugar geométrico de los **polos de lazo cerrado** cuando la ganancia $K$ recorre $0\to\infty$. Para realimentación con $G(s)$ en directa y $H(s)$ en retorno:
>
> ![[lgr_diagrama_bloques.svg|500]]
>
> $$T(s)=\frac{KG(s)}{1+KG(s)H(s)}.$$
>
> Los polos de lazo cerrado son las raíces del denominador, es decir de la **ecuación característica** $1+KG(s)H(s)=0$. En vez de resolverla para cada $K$, se traza el conjunto de todos los $s$ que pueden ser raíz para **algún** $K\ge0$.

> [!info] Recorrido de las ramas
> | $K$ | Posición de los polos de lazo cerrado |
> |---|---|
> | $K=0$ | en los **polos** de $G(s)H(s)$ |
> | $K\to\infty$ | en los **ceros** finitos de $G(s)H(s)$, o al infinito por las asíntotas |
>
> Cada rama conecta un polo de lazo abierto con un cero (finito o en infinito).

---

## Demostración

> [!teorema] De $KG(s)H(s)=-1$ a las dos condiciones
> Escribiendo $G(s)H(s)$ en forma polar $|GH|\,e^{j\angle GH}$ y usando $-1=1\cdot e^{j180^\circ(2k+1)}$.

> [!demostracion] Paso 1 — Forma polar
> $$K\,|G(s)H(s)|\,e^{j\angle G(s)H(s)}=1\cdot e^{j\,180^\circ(2k+1)}.$$

> [!demostracion] Paso 2 — Igualar módulos (condición de magnitud)
> $$K\,|G(s)H(s)|=1\;\Longrightarrow\;K=\frac{1}{|G(s)H(s)|}.$$
> Como $G(s)H(s)=\dfrac{\prod(s+z_i)}{\prod(s+p_j)}$, tomar módulos da
> $$K=\frac{\prod\|s+p_j\|}{\prod\|s+z_i\|}\quad(\text{producto de distancias a polos / a ceros}).$$

> [!demostracion] Paso 3 — Igualar argumentos (condición de ángulo)
> $$\angle G(s)H(s)=180^\circ(2k+1).$$
> Y como el ángulo de un cociente es la diferencia de ángulos:
> $$\sum_{i}\angle(s+z_i)-\sum_{j}\angle(s+p_j)=180^\circ(2k+1).$$

> [!info] Por qué $180^\circ$
> $KG(s)H(s)=-1$ exige que $KG(s)H(s)$ sea **real y negativo**. Un complejo es real negativo solo si su argumento es $180^\circ$ (módulo $360^\circ$). De ahí los múltiplos **impares** de $180^\circ$.

> [!info] Significado geométrico de los vectores
> ![[lgr_vectores_explicacion.svg|600]]
>
> Para un punto $s$: el vector $s+p_j$ va del polo $-p_j$ a $s$ (módulo $\|s+p_j\|$, ángulo $\angle(s+p_j)$); igual el vector $s+z_i$ desde el cero. La condición de ángulo suma los ángulos de los ceros y resta los de los polos; la de magnitud multiplica las distancias.

---

## Resumen

> [!resumen]
> | Condición | Decide | Fórmula |
> |---|---|---|
> | **Ángulo** | si $s\in$ LGR | $\sum\angle(s+z_i)-\sum\angle(s+p_j)=180^\circ(2k+1)$ |
> | **Magnitud** | el $K$ en ese $s$ | $K=\dfrac{\prod\|s+p_j\|}{\prod\|s+z_i\|}$ |
> | Origen | ec. característica | $1+KG(s)H(s)=0\Rightarrow GH=-1$ |
> | $K=0$ | polos de lazo cerrado en | polos de $GH$ |
> | $K\to\infty$ | polos de lazo cerrado en | ceros de $GH$ / infinito |

> [!corolario]
> La condición de ángulo es el filtro que separa los puntos del LGR del resto del plano; la de magnitud asigna a cada punto su única ganancia $K$. Todas las [[Reglas Construccion | reglas de construcción]] son atajos para no evaluar la condición de ángulo punto por punto.

> [!warning]
> 1. Las fórmulas suponen realimentación **negativa**; con $H(s)\neq1$ se usa el producto $G(s)H(s)$.
> 2. La condición de ángulo dice **si** $s$ está en el LGR, no **en qué rama**.
> 3. Con realimentación **positiva** el ángulo objetivo pasa a $360^\circ k$ (LGR complementario).

> [!referencia]
> - Marco general: [[index]].
> - Reglas que derivan de estas condiciones: [[Reglas Construccion]].
> - Eje real y asíntotas: [[Trayectoria eje real y Asintotas]].
> - Ganancia crítica en el cruce: [[Cruce Eje Imaginario]].
