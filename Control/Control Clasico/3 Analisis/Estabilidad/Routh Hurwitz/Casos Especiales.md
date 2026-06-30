---
title: Casos Especiales en la Tabla de Routh
order: 2
tags:
  - control-clasico
  - teoria
  - analisis
  - estabilidad
  - routh-hurwitz
draft: false
aliases:
  - casos especiales routh
  - fila de ceros
  - primer elemento cero
---

# Casos Especiales en la Tabla de Routh

> [!definicion]
> Dos anomalías detienen la construcción de la tabla de Routh. **Caso 1:** el primer elemento de una fila es $0$ con otros no nulos → se reemplaza por un infinitesimal $\varepsilon$ y se analiza el límite. **Caso 2:** una fila entera es nula → se forma el **polinomio auxiliar** $Q(s)$ de la fila superior y se sigue con $dQ/ds$; señala raíces simétricas respecto al origen.

> [!info]
> Extiende la [[Construccion Tabla | construcción de la tabla]] del criterio de [[index | Routh-Hurwitz]]. La fila de ceros remite a [[Polos Ceros | polos y ceros]] para interpretar los modos simétricos.

---

## Ejemplo

> [!ejemplo] Caso 1 — primer elemento cero (método $\varepsilon$)
> $$P(s)=s^5+2s^4+3s^3+6s^2+5s+3.$$
>
> **Paso 1 — Filas semilla.**
> $$
> \begin{array}{c|ccc}
> s^5 & 1 & 3 & 5 \\
> s^4 & 2 & 6 & 3
> \end{array}
> $$
>
> **Paso 2 — Fila $s^3$.**
> $$b_1=\frac{2\cdot3-1\cdot6}{2}=0,\qquad b_2=\frac{2\cdot5-1\cdot3}{2}=\frac{7}{2}=3.5.$$
> El primer elemento sale **cero** con un vecino no nulo → Caso 1.
>
> **Paso 3 — Sustituir $0\to\varepsilon$** ($\varepsilon\to0^+$):
> $$
> \begin{array}{c|ccc}
> s^5 & 1 & 3 & 5 \\
> s^4 & 2 & 6 & 3 \\
> s^3 & \varepsilon & 3.5 & 0
> \end{array}
> $$
>
> **Paso 4 — Fila $s^2$.**
> $$c_1=\frac{\varepsilon\cdot6-2\cdot3.5}{\varepsilon}=6-\frac{7}{\varepsilon},\qquad c_2=\frac{\varepsilon\cdot3-2\cdot0}{\varepsilon}=3.$$
> Con $\varepsilon\to0^+$: $c_1\to-\infty$.
>
> **Paso 5 — Fila $s^1$** (usando $f=(c_1,3)$, $g=(\varepsilon,3.5)$):
> $$d_1=\frac{c_1\cdot3.5-\varepsilon\cdot3}{c_1}\xrightarrow{\varepsilon\to0^+}3.5.$$
> **Fila $s^0$:** $e_1=3$.
>
> **Paso 6 — Signos en la primera columna** ($\varepsilon\to0^+$):
> $$1,\ 2,\ \varepsilon(>0),\ \underbrace{6-\tfrac{7}{\varepsilon}}_{<0},\ 3.5,\ 3 \;\Rightarrow\; +,+,+,-,+,+.$$
> **Dos cambios** ($+\to-$ y $-\to+$) → **2 polos con $\Re>0$** → **inestable**. (Con $\varepsilon\to0^-$ se obtiene el mismo conteo, confirmando que no son raíces sobre el eje.)

> [!ejemplo] Caso 2 — fila completa de ceros (polinomio auxiliar)
> $$P(s)=s^5+2s^4+2s^3+4s^2+s+2.$$
>
> **Paso 1 — Hasta la fila nula.**
> $$
> \begin{array}{c|ccc}
> s^5 & 1 & 2 & 1 \\
> s^4 & 2 & 4 & 2 \\
> s^3 & 0 & 0 & 0
> \end{array}
> $$
> La fila $s^3$ es toda ceros → Caso 2.
>
> **Paso 2 — Polinomio auxiliar** desde la fila superior $s^4$ ($2,4,2$ en $s^4,s^2,s^0$):
> $$Q(s)=2s^4+4s^2+2=2(s^2+1)^2.$$
>
> **Paso 3 — Derivar** y usar sus coeficientes ($8,8,0$) en la fila nula:
> $$\frac{dQ}{ds}=8s^3+8s.$$
> $$
> \begin{array}{c|ccc}
> s^5 & 1 & 2 & 1 \\
> s^4 & 2 & 4 & 2 \\
> s^3 & 8 & 8 & 0 \\
> s^2 & \frac{8\cdot4-2\cdot8}{8}=2 & \frac{8\cdot2-2\cdot0}{8}=2 & 0 \\
> s^1 & \frac{2\cdot8-8\cdot2}{2}=0 & 0 &
> \end{array}
> $$
>
> **Paso 4 — Nueva fila nula en $s^1$.** Auxiliar desde $s^2$: $Q_2(s)=2s^2+2$, $\dfrac{dQ_2}{ds}=4s$ → coeficientes $4,0$:
> $$
> \begin{array}{c|ccc}
> s^5 & 1 & 2 & 1 \\
> s^4 & 2 & 4 & 2 \\
> s^3 & 8 & 8 & 0 \\
> s^2 & 2 & 2 & 0 \\
> s^1 & 4 & 0 & \\
> s^0 & 2 & &
> \end{array}
> $$
>
> **Paso 5 — Leer.** Primera columna $1,2,8,2,4,2$: **sin cambios de signo** → ningún polo en $\Re>0$. Pero la fila de ceros delató raíces simétricas: $Q(s)=2(s^2+1)^2$ tiene $s=\pm j$ con **multiplicidad 2** → eje imaginario **repetido** → **inestable** (la respuesta crece como $t\sin t$).

---

## En qué consiste

> [!info] Síntomas y soluciones
> | Caso | Síntoma | Solución |
> |---|---|---|
> | 1 | primer elemento $0$, resto de la fila no nulo | reemplazar por $\varepsilon$ y analizar límites $\varepsilon\to0^\pm$ |
> | 2 | fila entera de ceros | $Q(s)$ de la fila superior, seguir con $dQ/ds$ |
>
> Una fila de ceros aparece cuando $P(s)$ tiene **raíces simétricas** respecto al origen: pares reales $\pm a$, imaginarios $\pm j\omega$ o cuartetos $\pm a\pm jb$. Esas raíces son justamente las de $Q(s)$.

> [!teorema] Caso 1 — justificación del épsilon
> Sustituir el cero por $\varepsilon$ equivale a perturbar $P(s)\to P_\varepsilon(s)=P(s)+\varepsilon R(s)$, con $P_\varepsilon\to P$ cuando $\varepsilon\to0$.

> [!demostracion]
> El signo de los elementos de la primera columna depende del de $\varepsilon$ cuando es pequeño. Si los signos coinciden para $\varepsilon\to0^+$ y $\varepsilon\to0^-$, los cambios contados son reales (polos en $\Re>0$). Si difieren, $P(s)$ tiene raíces sobre el eje imaginario que la perturbación desdobla: el sistema es a lo sumo marginal. El conteo se hace con el límite, no con $\varepsilon$ fijo. $\blacksquare$

> [!teorema] Caso 2 — justificación del polinomio auxiliar
> La fila superior a los ceros es el polinomio par $Q(s)$ que reúne los factores simétricos; sus raíces fijan el tipo de estabilidad.

> [!demostracion]
> **Paso 1.** Escribir $P(s)=Q(s)R(s)$ con $Q(s)=(s^2+\omega_1^2)^{k_1}\cdots(s^2-a_1^2)^{m_1}\cdots$, el factor de las raíces simétricas.
>
> **Paso 2.** Por ser par (solo potencias pares), $Q(s)$ ocupa la fila inmediatamente superior a la de ceros.
>
> **Paso 3.** $dQ/ds$ es **impar**; sus coeficientes rellenan la fila nula y permiten continuar.
>
> **Paso 4.** Las raíces de $Q(s)$ deciden:
> - todas **simples** en $\pm j\omega$ o $s=0$ → **marginalmente estable**;
> - alguna con **multiplicidad $\ge2$** o un par **real opuesto** $\pm a$ → **inestable**.
>
> En el ejemplo, $Q(s)=2(s^2+1)^2$ tiene $\pm j$ dobles → inestable. $\blacksquare$

---

## Limitaciones

> [!warning]
> 1. El método $\varepsilon$ exige cuidado al tomar límites por ambos lados; un signo mal evaluado falsea el conteo.
> 2. El polinomio auxiliar localiza las raíces simétricas pero no las demás; combinarlo con el resto de la primera columna.
> 3. No distingue marginal de inestable sin examinar la **multiplicidad** de las raíces de $Q(s)$.
> 4. Para sistemas con retardo el método no aplica.

## Resumen

> [!resumen]
> | Caso | Receta | Lectura final |
> |---|---|---|
> | 1: primer cero | $0\to\varepsilon$, completar, límites $\varepsilon\to0^\pm$ | cambios de signo = polos $\Re>0$ |
> | 2: fila nula | $Q(s)$ arriba, seguir con $dQ/ds$ | raíces de $Q$: simples→marginal, repetidas/reales→inestable |

> [!corolario]
> Los casos especiales no rompen el criterio: lo extienden. El $\varepsilon$ rescata una división por cero accidental; el polinomio auxiliar revela las raíces simétricas que producen la fila nula y, según su multiplicidad, separan lo marginal de lo inestable.

> [!referencia]
> - Procedimiento base: [[Construccion Tabla]].
> - Criterio general: [[index]].
> - Rango de parámetros: [[Ajuste Parametros]].
> - Raíces simétricas y modos: [[Polos Ceros]].
