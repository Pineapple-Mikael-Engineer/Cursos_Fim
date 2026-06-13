---
title: Fórmula General del Error Estacionario
tags:
  - control-clasico
  - analisis
  - error-estacionario
draft: false
aliases:
  - formula general error
  - error con perturbaciones
  - error no unitario
---

# Fórmula General del Error Estacionario

> [!definicion]
> El error es $E(s)=R(s)-Y(s)$ y su valor en régimen permanente se obtiene con el [[Teorema Valor Inicial Final | teorema del valor final]]:
> $$e_{ss}=\lim_{t\to\infty}e(t)=\lim_{s\to0}sE(s).$$
> Según la realimentación, $E(s)$ vale (lazo abierto / unitario / general):
> $$[1-G]R,\qquad \frac{1}{1+G}R,\qquad \frac{1+GH-G}{1+GH}R.$$

> [!info]
> Hija de [[index | Error Estacionario]]. Esta nota es el caso **general**: realimentación no unitaria y **perturbaciones**. Para el caso unitario tabulado ver [[Coeficientes Kp Kv Ka]] y [[Tabla Tipos]]; la clasificación por integradores en [[Tipo Sistema]].

---

## Ejemplo

> [!ejemplo] Realimentación no unitaria ante escalón
> $$G(s)=\frac{2}{(s+1)(s+2)},\qquad H(s)=\frac{1}{s+3},\qquad R(s)=\frac1s,\;D(s)=0.$$
>
> **Paso 1 — Lazo abierto:**
> $$L(s)=G(s)H(s)=\frac{2}{(s+1)(s+2)(s+3)}.$$
>
> **Paso 2 — Error (no unitario):** como $H\neq1$, el error verdadero $R-Y$ es
> $$E(s)=\frac{1+GH-G}{1+GH}R(s).$$
>
> **Paso 3 — Evaluar en $s=0$:**
> $$G(0)=\frac{2}{1\cdot2}=1,\qquad G(0)H(0)=\frac{2}{1\cdot2\cdot3}=\frac13.$$
>
> **Paso 4 — TVF** (el $s$ cancela el $1/s$ del escalón):
> $$e_{ss}=\frac{1+G(0)H(0)-G(0)}{1+G(0)H(0)}=\frac{1+\tfrac13-1}{1+\tfrac13}=\frac{\tfrac13}{\tfrac43}=\frac14=0.25.$$
>
> Aunque $G$ tiene ganancia DC $1$ (que en caso unitario daría $e_{ss}=\tfrac{1}{1+1}=0.5$), la realimentación no unitaria $H(0)=\tfrac13$ cambia el resultado a $0.25$: **no** se puede usar la fórmula de $K_p$ directamente.

> [!ejemplo] Error ante perturbación escalón (tipo 0)
> ![[sistema_perturbacion.svg|500]]
>
> $$G_1(s)=K_1,\quad G_2(s)=\frac{K_2}{s+1},\quad H(s)=1,\quad D(s)=\frac1s,\quad R(s)=0.$$
>
> Por superposición, la salida debida solo a $D$ es $Y_D=\dfrac{G_2}{1+G_1G_2H}D$, y como $R=0$ el error es $E=-Y_D$:
> $$e_{ss}=\lim_{s\to0}s\left[-\frac{K_2/(s+1)}{1+K_1K_2/(s+1)}\cdot\frac1s\right]=-\frac{K_2}{1+K_1K_2}.$$
>
> La perturbación deja error **no nulo** salvo que $G_1$ aporte un integrador (que haría $\to\infty$ el denominador y anularía el error). Con $K_1=K_2=10$: $e_{ss}=-10/101\approx-0.099$.

---

## En qué consiste

> [!teoria]
> El error verdadero es siempre $R-Y$. Lo que cambia entre configuraciones es $Y(s)$:
>
> | Configuración | $Y(s)$ | $E(s)=R-Y$ |
> |---|---|---|
> | Lazo abierto | $G\,R$ | $[1-G]R$ |
> | Cerrado unitario | $\frac{G}{1+G}R$ | $\frac{1}{1+G}R$ |
> | Cerrado general | $\frac{G}{1+GH}R$ | $\frac{1+GH-G}{1+GH}R$ |
>
> En el caso general **no** hay cancelación de $G$ en el numerador, por eso el error no se reduce a $1/(1+GH)$.

> [!warning] Error en el comparador ≠ error real
> La señal a la entrada de $G$ es
> $$E_{\text{comp}}(s)=\frac{1}{1+G(s)H(s)}R(s),$$
> que **solo** coincide con $R-Y$ cuando $H=1$. Confundirlos es el error típico en sistemas con sensor dinámico.

> [!teorema] Sistema con perturbación (superposición)
> Con $G=G_1G_2$ y perturbación $D$ entrando entre $G_1$ y $G_2$:
> $$Y(s)=\underbrace{\frac{G_1G_2}{1+G_1G_2H}}_{\text{de }R}R(s)+\underbrace{\frac{G_2}{1+G_1G_2H}}_{\text{de }D}D(s).$$
> Entonces
> $$E(s)=\frac{1+G_1G_2H-G_1G_2}{1+G_1G_2H}R(s)-\frac{G_2}{1+G_1G_2H}D(s).$$
> El segundo término es el error por perturbación; lo anula un integrador **antes** del punto donde entra $D$ (en $G_1$).

---

## Receta

> [!algoritmo] Calcular $e_{ss}$ en cualquier configuración
> 1. Escribir $Y(s)$ y formar $E(s)=R(s)-Y(s)$ en términos de $R,D,G,H$.
> 2. Verificar que el lazo cerrado es **estable** (si no, $e_{ss}$ no existe).
> 3. Aplicar el [[Teorema Valor Inicial Final | TVF]]: $e_{ss}=\lim_{s\to0}sE(s)$.
> 4. Si $H=1$ y solo hay $R$, atajar con $K_p,K_v,K_a$ ([[Coeficientes Kp Kv Ka]]).
>
> ```matlab
> G = tf(2,conv([1 1],[1 2]));  H = tf(1,[1 3]);
> Ecl = minreal((1+G*H-G)/(1+G*H));   % E(s)/R(s), no unitario
> ess = dcgain(Ecl)                    % escalon: lim s*E*(1/s)=E(0)
> ```

---

## Casos particulares (lazo cerrado unitario)

> [!info] Para $H=1$ y solo referencia, el error se reduce a
> | Entrada | $R(s)$ | $e_{ss}$ |
> |---|---|---|
> | [[Escalon \| escalón]] | $1/s$ | $\dfrac{1}{1+\lim_{s\to0}G}=\dfrac{1}{1+K_p}$ |
> | [[Rampa \| rampa]] | $1/s^2$ | $\dfrac{1}{\lim_{s\to0}sG}=\dfrac{1}{K_v}$ |
> | [[Parabola \| parábola]] | $1/s^3$ | $\dfrac{1}{\lim_{s\to0}s^2G}=\dfrac{1}{K_a}$ |
>
> Generalización con coeficientes en [[Coeficientes Kp Kv Ka]] y [[Tabla Tipos]].

---

## Limitaciones

> [!warning]
> 1. El TVF **solo** aplica si el lazo cerrado es estable; si diverge, $e_{ss}$ no está definido.
> 2. La expresión no unitaria es **distinta** de la unitaria: no usar $K_p$ con $H\neq1$.
> 3. No confundir el error real $R-Y$ con el error del comparador $\frac{1}{1+GH}R$.
> 4. El error por perturbación depende de **dónde** entra $D$ respecto a los integradores.

## Resumen

> [!resumen]
> | Configuración | $E(s)$ | $e_{ss}$ |
> |---|---|---|
> | Lazo abierto | $[1-G]R$ | $\lim_{s\to0}s[1-G]R$ |
> | Unitario | $\frac{1}{1+G}R$ | $\frac{1}{1+K_p}$, $\frac1{K_v}$, $\frac1{K_a}$ |
> | General | $\frac{1+GH-G}{1+GH}R$ | $\lim_{s\to0}s\,E(s)$ |
> | Perturbación | $-\frac{G_2}{1+G_1G_2H}D$ | $-\frac{G_2(0)}{1+G_1G_2H|_0}$ (si tipo 0) |

> [!corolario]
> Todo $e_{ss}$ es el mismo límite $\lim_{s\to0}sE(s)$; la única dificultad es armar bien $E(s)=R-Y$, que cambia con la realimentación y con el punto de entrada de la perturbación. El atajo de $K_p,K_v,K_a$ vale solo en el caso unitario sin perturbación; fuera de él, hay que pasar por la fórmula general.

> [!referencia]
> - Caso unitario tabulado: [[Coeficientes Kp Kv Ka]] · [[Tabla Tipos]].
> - Clasificación por integradores: [[Tipo Sistema]].
> - Marco general: [[index | Error Estacionario]].
> - Herramienta base: [[Teorema Valor Inicial Final]].
