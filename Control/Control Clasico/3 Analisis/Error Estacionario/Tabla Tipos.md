---
title: Tabla de Tipos de Sistemas
tags:
  - control-clasico
  - analisis
  - error-estacionario
draft: false
aliases:
  - tipos de sistemas
  - tabla tipos
  - tipo 0 tipo 1 tipo 2
---

# Tabla de Tipos de Sistemas

> [!definicion] Tabla maestra ($H=1$)
> Con $G(s)=\dfrac{K}{s^N}G_0(s)$, $G_0(0)=1$, el error estacionario por **tipo $N$** y entrada es:
>
> | Tipo | $K_p$ | $K_v$ | $K_a$ | **Escalón** | **Rampa** | **Parábola** |
> |---|---|---|---|---|---|---|
> | 0 | $K$ | $0$ | $0$ | $\dfrac{1}{1+K}$ | $\infty$ | $\infty$ |
> | 1 | $\infty$ | $K$ | $0$ | $0$ | $\dfrac{1}{K}$ | $\infty$ |
> | 2 | $\infty$ | $\infty$ | $K$ | $0$ | $0$ | $\dfrac{1}{K}$ |
>
> $K$ es la ganancia estática tras extraer los integradores. La diagonal marca la frontera: error **finito** donde tipo = orden de la entrada.

> [!info]
> Hija de [[index | Error Estacionario]]. Es la nota de **consulta rápida**: el "qué da" sin recalcular límites. El "por qué" está en [[Coeficientes Kp Kv Ka]] y la clasificación en [[Tipo Sistema]].

---

## Ejemplo

> [!ejemplo] Usar la tabla en tres plantas reales
> Realimentación unitaria; leer $e_{ss}$ directamente de la tabla.
>
> **(a) Mecánico con resorte (tipo 0):** $G(s)=\dfrac{1}{ms^2+bs+k}$, sin polo en $s=0$.
> $$K_p=G(0)=\frac1k\ \Rightarrow\ e_{ss}^{\text{escalón}}=\frac{1}{1+1/k}=\frac{k}{k+1};\qquad \text{rampa/parábola}:\infty.$$
> Con $k=4$: $e_{ss}=4/5=0.8$.
>
> **(b) Motor DC, salida velocidad (tipo 1):** $G(s)=\dfrac{K_t}{s(Js+b)}$, un integrador.
> $$K_v=\lim_{s\to0}sG=\frac{K_t}{b}\ \Rightarrow\ e_{ss}^{\text{rampa}}=\frac{b}{K_t};\qquad \text{escalón}:0,\ \text{parábola}:\infty.$$
> Con $K_t=2,\ b=0.5$: $e_{ss}^{\text{rampa}}=0.25$.
>
> **(c) Motor DC, salida posición (tipo 2):** $G(s)=\dfrac{K_t}{s^2(Js+b)}$, doble integrador.
> $$K_a=\lim_{s\to0}s^2G=\frac{K_t}{b}\ \Rightarrow\ e_{ss}^{\text{parábola}}=\frac{b}{K_t};\qquad \text{escalón/rampa}:0.$$
>
> En cada caso, $e_{ss}$ finito aparece **solo** en la entrada cuyo orden iguala al tipo; las de orden mayor dan $\infty$ y las menores, $0$.

> [!regla] Mnemotecnia de la tabla
> Lee la fila del tipo: ceros a la izquierda (entradas que sigue exactas), un valor finito en la diagonal, infinitos a la derecha (entradas que no puede seguir).

---

## Interpretación

> [!info] Qué significa cada tipo
> | Tipo | Sigue con error finito una... |
> |---|---|
> | 0 | **posición** constante (escalón) |
> | 1 | **velocidad** constante (rampa) |
> | 2 | **aceleración** constante (parábola) |
>
> Un sistema tipo $N$ sigue con error finito los polinomios de grado $\le N$ (error cero si el grado es $<N$).

---

## Demostración

> [!teorema] $K_p$ finito solo si $N=0$; $K_v$ solo si $N\ge1$; $K_a$ solo si $N\ge2$.

> [!demostracion]
> Sea $G(s)=\dfrac{K}{s^N}G_0(s)$ con $G_0(0)=1$.
>
> **Paso 1 — $N=0$:**
> $$K_p=\lim_{s\to0}G=K,\quad K_v=\lim_{s\to0}sK=0,\quad K_a=\lim_{s\to0}s^2K=0.$$
>
> **Paso 2 — $N=1$:**
> $$K_p=\lim_{s\to0}\frac{K}{s}G_0=\infty,\quad K_v=\lim_{s\to0}s\frac{K}{s}G_0=K,\quad K_a=\lim_{s\to0}s^2\frac{K}{s}G_0=0.$$
>
> **Paso 3 — $N=2$:**
> $$K_p=\lim_{s\to0}\frac{K}{s^2}G_0=\infty,\quad K_v=\lim_{s\to0}\frac{K}{s}G_0=\infty,\quad K_a=\lim_{s\to0}s^2\frac{K}{s^2}G_0=K.$$
>
> Sustituyendo en $e_{ss}=\frac{1}{1+K_p}$ (escalón), $\frac1{K_v}$ (rampa), $\frac1{K_a}$ (parábola) se obtiene la tabla maestra. (Deducción de esas tres fórmulas en [[Coeficientes Kp Kv Ka]].)

---

## Aumentar el tipo

> [!info]
> Agregar integradores con un controlador [[Integral I | I]]/PI o un [[Lag | compensador lag]] sube el tipo en 1 (el lag, con un polo muy cerca de $s=0$). Ver [[PID/index | PID]].

> [!warning]
> 1. Subir el tipo mejora $e_{ss}$ pero **puede desestabilizar**: cada integrador resta $90°$ de fase.
> 2. Más de 2 integradores es difícilmente estabilizable.
> 3. La tabla asume **realimentación unitaria**; si $H\neq1$ usar $G(s)H(s)$ y la fórmula de [[Formula General]].

## Resumen

> [!resumen]
> | Entrada \\ Tipo | 0 | 1 | 2 |
> |---|---|---|---|
> | Escalón | $\frac{1}{1+K}$ | $0$ | $0$ |
> | Rampa | $\infty$ | $\frac{1}{K}$ | $0$ |
> | Parábola | $\infty$ | $\infty$ | $\frac{1}{K}$ |

> [!corolario]
> La tabla condensa todo el análisis de error en régimen permanente para realimentación unitaria: basta identificar el tipo $N$ (integradores) y el orden de la entrada para leer $e_{ss}$, finito solo en la diagonal. Para justificar un valor o tratar $H\neq1$ y perturbaciones, se baja a [[Coeficientes Kp Kv Ka]] y [[Formula General]].

> [!referencia]
> - Coeficientes que la generan: [[Coeficientes Kp Kv Ka]].
> - Clasificación por integradores: [[Tipo Sistema]].
> - Caso general / perturbación: [[Formula General]].
> - Marco: [[index | Error Estacionario]].
