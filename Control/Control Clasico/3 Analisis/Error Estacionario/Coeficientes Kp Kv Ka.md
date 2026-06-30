---
title: Coeficientes de Error Kp, Kv, Ka
order: 1
tags:
  - control-clasico
  - analisis
  - error-estacionario
draft: false
aliases:
  - Kp
  - Kv
  - Ka
  - coeficientes de error
---

# Coeficientes de Error $K_p$, $K_v$, $K_a$

> [!definicion]
> Para **realimentación unitaria** ($H=1$), tres límites de $G(s)$ en $s\to0$ resumen todo el error estacionario:
> $$K_p=\lim_{s\to0}G(s),\qquad K_v=\lim_{s\to0}sG(s),\qquad K_a=\lim_{s\to0}s^2G(s).$$
> Con ellos, el error ante cada entrada de prueba es
> $$e_{ss}^{\text{escalón}}=\frac{1}{1+K_p},\qquad e_{ss}^{\text{rampa}}=\frac{1}{K_v},\qquad e_{ss}^{\text{parábola}}=\frac{1}{K_a}.$$

> [!info]
> Hija de [[index | Error Estacionario]]. Cuantifica el error que el [[Tipo Sistema | tipo]] solo clasifica: $K_p$ es finito solo en tipo 0, $K_v$ solo en tipo 1, $K_a$ solo en tipo 2. Tabla compacta en [[Tabla Tipos]]; deducción del límite en [[Formula General]].

---

## Ejemplo

> [!ejemplo] Calcular los tres coeficientes y el error
> Para cada planta (realimentación unitaria) calcular $K_p,K_v,K_a$ y el $e_{ss}$ relevante.
>
> **(a) Tipo 0 — $G(s)=\dfrac{10}{(s+1)(s+2)}$**
> $$K_p=\lim_{s\to0}\frac{10}{(s+1)(s+2)}=\frac{10}{1\cdot2}=5,\quad K_v=\lim_{s\to0}\frac{10s}{(s+1)(s+2)}=0,\quad K_a=0.$$
> Error ante **escalón**: $e_{ss}=\dfrac{1}{1+K_p}=\dfrac{1}{6}\approx0.167$. Ante rampa/parábola: $\infty$.
>
> **(b) Tipo 1 — $G(s)=\dfrac{10}{s(s+2)}$**
> $$K_p=\infty,\quad K_v=\lim_{s\to0}\frac{10s}{s(s+2)}=\frac{10}{2}=5,\quad K_a=\lim_{s\to0}\frac{10s^2}{s(s+2)}=0.$$
> Error ante **rampa**: $e_{ss}=\dfrac{1}{K_v}=0.2$. Ante escalón: $0$; ante parábola: $\infty$.
>
> **(c) Tipo 2 — $G(s)=\dfrac{10}{s^2(s+2)}$**
> $$K_p=\infty,\quad K_v=\infty,\quad K_a=\lim_{s\to0}\frac{10s^2}{s^2(s+2)}=\frac{10}{2}=5.$$
> Error ante **parábola**: $e_{ss}=\dfrac{1}{K_a}=0.2$. Ante escalón y rampa: $0$.

> [!ejemplo] Error estacionario por tipo de entrada
> ![[error_coef_kp_kv_ka.svg|620]]
>
> Para un sistema tipo 1: ante escalón $e_{ss}=0$ (alcanza la referencia); ante rampa $e_{ss}=1/K_v$ (desfase constante); ante parábola $e_{ss}\to\infty$ (no la sigue).

---

## Demostración

> [!teorema] Cada coeficiente sale del error de su entrada
> Con $E(s)=\dfrac{1}{1+G(s)}R(s)$ y $e_{ss}=\lim_{s\to0}sE(s)$, sustituyendo $R(s)=1/s^{k+1}$.

> [!demostracion]
> **Paso 1 — Escalón** ($R=1/s$):
> $$e_{ss}=\lim_{s\to0}\frac{s}{1+G(s)}\cdot\frac1s=\lim_{s\to0}\frac{1}{1+G(s)}=\frac{1}{1+K_p},\qquad K_p=\lim_{s\to0}G(s).$$
>
> **Paso 2 — Rampa** ($R=1/s^2$):
> $$e_{ss}=\lim_{s\to0}\frac{s}{1+G(s)}\cdot\frac1{s^2}=\lim_{s\to0}\frac{1}{s+sG(s)}=\frac{1}{\lim_{s\to0}sG(s)}=\frac{1}{K_v},\qquad K_v=\lim_{s\to0}sG(s).$$
>
> **Paso 3 — Parábola** ($R=1/s^3$):
> $$e_{ss}=\lim_{s\to0}\frac{s}{1+G(s)}\cdot\frac1{s^3}=\lim_{s\to0}\frac{1}{s^2(1+G(s))}=\frac{1}{\lim_{s\to0}s^2G(s)}=\frac{1}{K_a},\qquad K_a=\lim_{s\to0}s^2G(s).$$

> [!info] Por qué cada coeficiente "vive" en un solo tipo
> Con $G(s)=\dfrac{K}{s^N}G_0(s)$, $G_0(0)=1$:
>
> | | $K_p=\lim G$ | $K_v=\lim sG$ | $K_a=\lim s^2G$ |
> |---|---|---|---|
> | Tipo 0 | $K$ | $0$ | $0$ |
> | Tipo 1 | $\infty$ | $K$ | $0$ |
> | Tipo 2 | $\infty$ | $\infty$ | $K$ |
>
> El coeficiente "propio" del tipo vale exactamente la ganancia estática $K$; los de orden menor son $\infty$ (error $0$) y los de orden mayor son $0$ (error $\infty$).

---

## Conexión con la ganancia estática

> [!info]
> - Tipo 0: $K_p=G(0)$ (ganancia DC).
> - Tipo 1: $K_v=\lim_{s\to0}sG(s)$, constante.
> - Tipo 2: $K_a=\lim_{s\to0}s^2G(s)$, constante.
>
> Ver [[Ganancia Estatica | ganancia estática]].

---

## Limitaciones

> [!warning]
> 1. Solo tienen sentido si el lazo cerrado es **estable**.
> 2. Las fórmulas asumen **realimentación unitaria** ($H=1$).
> 3. Si $H\neq1$, usar $G(s)H(s)$ en lugar de $G(s)$ y la expresión general de [[Formula General]].

## Resumen

> [!resumen] Realimentación unitaria
> | Tipo | $K_p$ | $K_v$ | $K_a$ | Escalón | Rampa | Parábola |
> |---|---|---|---|---|---|---|
> | 0 | $K$ | $0$ | $0$ | $\frac{1}{1+K}$ | $\infty$ | $\infty$ |
> | 1 | $\infty$ | $K$ | $0$ | $0$ | $\frac{1}{K}$ | $\infty$ |
> | 2 | $\infty$ | $\infty$ | $K$ | $0$ | $0$ | $\frac{1}{K}$ |

> [!corolario]
> $K_p,K_v,K_a$ son la versión cuantitativa del tipo: un límite de $s^kG(s)$ que vale la ganancia estática justo cuando el tipo iguala al orden $k$ de la entrada, y el error es su recíproco ($1/(1+K_p)$ para escalón, $1/K_v$ y $1/K_a$ para rampa y parábola). Para no recalcular límites, la tabla por tipo está en [[Tabla Tipos]].

> [!referencia]
> - Clasificación previa: [[Tipo Sistema]].
> - Tabla de consulta: [[Tabla Tipos]].
> - Deducción del límite: [[Formula General]] · [[index | Error Estacionario]].
> - Ganancia DC: [[Ganancia Estatica]].
