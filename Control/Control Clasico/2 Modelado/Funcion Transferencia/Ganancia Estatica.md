---
title: Ganancia Estática
tags:
  - control-clasico
  - teoria
  - modelado
draft: false
aliases:
  - ganancia DC
  - G(0)
---

# Ganancia Estática

# Definición

> [!definicion] Ganancia estática
> $$G(0) = \lim_{s \to 0} G(s)$$
> 
> Es el valor de la función transferencia en frecuencia cero (régimen permanente DC).

> [!ejemplo]
> $$G(s) = \frac{10(s+2)}{(s+1)(s+5)} \implies G(0) = \frac{10 \cdot 2}{1 \cdot 5} = 4$$

> [!ejemplo]
> $$G(s) = \frac{5}{s(s+2)} \implies G(0) = \infty$$
> 
> Sistemas con integradores tienen $G(0)$ infinito. Ver [[Error Estacionario/index | error estacionario]].

---

# Teorema 1: Cálculo desde coeficientes

> [!teorema]
> Dada $G(s) = \dfrac{b_m s^m + b_{m-1} s^{m-1} + \dots + b_0}{a_n s^n + a_{n-1} s^{n-1} + \dots + a_0}$ con $a_0 \neq 0$, entonces:
> $$G(0) = \frac{b_0}{a_0}$$

> [!demostracion]
> Por definición, $G(0) = \lim_{s \to 0} G(s)$. Sustituyendo:
> 
> $$G(0) = \lim_{s \to 0} \frac{b_0 + b_1 s + b_2 s^2 + \dots + b_m s^m}{a_0 + a_1 s + a_2 s^2 + \dots + a_n s^n}$$
> 
> Cuando $s \to 0$, todos los términos $b_k s^k$ con $k \ge 1$ tienden a $0$. Lo mismo para el denominador. Por lo tanto:
> 
> $$G(0) = \frac{b_0}{a_0}$$

> [!ejemplo]
> $$G(s) = \frac{3s^2 + 2s + 1}{s^3 + 4s^2 + 5s + 2} \implies G(0) = \frac{1}{2}$$

---

# Teorema 2: Relación con respuesta a escalón

> [!teorema]
> Sea $G(s)$ con todos los polos en $\Re(s) < 0$ (sistema estable). Para entrada escalón unitario $u(t)=1(t)$:
> $$\lim_{t \to \infty} y(t) = G(0)$$

> [!demostracion]
> La salida en Laplace es $Y(s) = G(s) \cdot \frac{1}{s}$.
> 
> Aplicando el [[Teorema Valor Inicial Final | teorema del valor final]] (válido por la hipótesis de estabilidad):
> 
> $$\lim_{t \to \infty} y(t) = \lim_{s \to 0} s Y(s) = \lim_{s \to 0} s \cdot G(s) \cdot \frac{1}{s} = \lim_{s \to 0} G(s) = G(0)$$

> [!ejemplo]
> $$G(s) = \frac{2}{s+2} \implies G(0)=1$$
> 
> La respuesta a escalón estabiliza en $y(\infty)=1$.

---

# Teorema 3: Conexión de sistemas

> [!teorema]
> Para sistemas interconectados:
> - **Serie:** $G_{eq}(0) = G_1(0) \cdot G_2(0)$
> - **Paralelo:** $G_{eq}(0) = G_1(0) + G_2(0)$
> - **Realimentación unitaria:** $G_{eq}(0) = \dfrac{G(0)}{1 + G(0)}$, si $G(0) \neq -1$

> [!demostracion]
> **Serie:** $G_{eq}(s) = G_1(s) G_2(s) \implies \lim_{s \to 0} G_{eq}(s) = \lim_{s \to 0} G_1(s) \cdot \lim_{s \to 0} G_2(s) = G_1(0) G_2(0)$
> 
> **Paralelo:** $G_{eq}(s) = G_1(s) + G_2(s) \implies \lim_{s \to 0} G_{eq}(s) = G_1(0) + G_2(0)$
> 
> **Realimentación:** $G_{eq}(s) = \dfrac{G(s)}{1+G(s)} \implies G_{eq}(0) = \dfrac{G(0)}{1+G(0)}$

> [!ejemplo]
> $$G_1(s) = \frac{2}{s+1}, \quad G_2(s) = \frac{3}{s+2}$$
> 
> - Serie: $G_{eq}(0) = 2 \cdot 1.5 = 3$
> - Paralelo: $G_{eq}(0) = 2 + 1.5 = 3.5$

---

# Ejemplos físicos

> [!ejemplo] Masa-resorte amortiguador
> $$G(s) = \frac{1}{ms^2 + bs + k} \implies G(0) = \frac{1}{k}$$
> 
> Fuerza constante de 1 N produce desplazamiento constante de $1/k$ metros.

> [!ejemplo] Motor DC velocidad
> $$G(s) = \frac{K_t}{Js + b} \implies G(0) = \frac{K_t}{b}$$
> 
> Voltaje constante de 1 V produce velocidad angular constante de $K_t/b$ rad/s.

> [!ejemplo] Circuito RC
> $$G(s) = \frac{1}{RCs + 1} \implies G(0) = 1$$
> 
> El capacitor se comporta como circuito abierto en DC; $v_o = v_i$.

---

# Interpretación

> [!info]
> - $G(0)$ finito: el sistema amplifica/atenúa señales DC
> - $G(0) = 0$: bloquea señales DC (derivador, filtro pasa altos)
> - $G(0) = \infty$: tiene integradores; salida crece sin límite ante DC (o se satura)

> [!info] Uso en diseño
> - [[Lead | Lead]]: no afecta $G(0)$
> - [[Lag | Lag]]: aumenta $G(0)$ por factor $\beta > 1$
> - [[PID | PID]]: término integral $\frac{K_i}{s}$ hace $G(0) \to \infty$

---

# Limitaciones

> [!warning]
> 1. $G(0) = b_0/a_0$ solo si $a_0 \neq 0$. Si $a_0 = 0$ hay polo(s) en $s=0$.
> 2. $\lim_{t \to \infty} y(t) = G(0)$ solo si el sistema es **estable**.
> 3. Para sistemas con realimentación no unitaria, usar $G(0)H(0)$ en los coeficientes de error.