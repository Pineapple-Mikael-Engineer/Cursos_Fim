---
title: Ganancia Estática
order: 4
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

> [!definicion]
> La ganancia estática es el valor de la FT en frecuencia cero (régimen permanente DC):
> $$G(0)=\lim_{s\to 0}G(s)=\frac{b_0}{a_0}\quad(\text{si }a_0\neq 0).$$
> Para un sistema **estable** ante un escalón unitario, $G(0)$ es exactamente el **valor final** de la salida: $\lim_{t\to\infty}y(t)=G(0)$.

> [!info]
> Es uno de los parámetros básicos de la [[Funcion Transferencia/index | función de transferencia]]. Fija el valor de régimen permanente y, bajo realimentación, el [[Error Estacionario/index | error estacionario]]. Se calcula vía el [[Teorema Valor Inicial Final | teorema del valor final]].

---

## Ejemplo

> [!ejemplo] Ganancia estática como valor final
> ![[ganancia_estatica_escalon.svg|520]]
>
> $G(0)$ es el valor al que tiende la respuesta al escalón unitario. La curva arranca en $y(0^+)$ y se estabiliza en $y(\infty)=G(0)$.

> [!ejemplo] Cálculo directo desde la FT
> $$G(s)=\frac{10(s+2)}{(s+1)(s+5)}.$$
> **Paso 1 — Evaluar en $s=0$:**
> $$G(0)=\frac{10(0+2)}{(0+1)(0+5)}=\frac{20}{5}=4.$$
> **Paso 2 — Interpretar:** ante un escalón unitario, la salida estable se asienta en $y(\infty)=4$. El sistema amplifica el DC por un factor 4.

> [!ejemplo] Desde los coeficientes ($b_0/a_0$)
> $$G(s)=\frac{3s^2+2s+1}{s^3+4s^2+5s+2}\implies G(0)=\frac{b_0}{a_0}=\frac{1}{2}.$$
> Basta tomar los términos independientes de cada polinomio.

> [!ejemplo] Sistema con integrador
> $$G(s)=\frac{5}{s(s+2)}\implies G(0)=\frac{5}{0\cdot 2}=\infty.$$
> El polo en $s=0$ ($a_0=0$) hace $G(0)$ infinita: ante DC la salida crece sin límite. Ver [[Error Estacionario/index | error estacionario]].

---

## En qué consiste

> [!teorema] Cálculo desde coeficientes
> Si $G(s)=\dfrac{b_m s^m+\dots+b_0}{a_n s^n+\dots+a_0}$ con $a_0\neq 0$, entonces $G(0)=b_0/a_0$.

> [!demostracion]
> $$G(0)=\lim_{s\to 0}\frac{b_0+b_1 s+\dots+b_m s^m}{a_0+a_1 s+\dots+a_n s^n}.$$
> Cuando $s\to 0$, todos los términos con $s^k$, $k\ge1$, se anulan en numerador y denominador, quedando $b_0/a_0$. $\blacksquare$

> [!teorema] Relación con la respuesta a escalón
> Si $G(s)$ es estable (todos los polos con $\Re<0$), ante escalón unitario $\lim_{t\to\infty}y(t)=G(0)$.

> [!demostracion]
> La salida es $Y(s)=G(s)/s$. Por el [[Teorema Valor Inicial Final | teorema del valor final]] (válido por estabilidad):
> $$\lim_{t\to\infty}y(t)=\lim_{s\to 0}sY(s)=\lim_{s\to0}s\cdot G(s)\cdot\frac1s=\lim_{s\to0}G(s)=G(0).\ \blacksquare$$

> [!teorema] Ganancia estática de interconexiones
> $$\text{Serie: }G_1(0)G_2(0),\quad \text{Paralelo: }G_1(0)+G_2(0),\quad \text{Realim. unitaria: }\frac{G(0)}{1+G(0)}.$$
> Se obtienen tomando $\lim_{s\to0}$ en cada fórmula del [[Algebra Diagramas | álgebra de diagramas]].

> [!ejemplo] Interconexión numérica
> $G_1(s)=\frac{2}{s+1}$ ($G_1(0)=2$), $G_2(s)=\frac{3}{s+2}$ ($G_2(0)=1.5$). Serie: $2\cdot1.5=3$. Paralelo: $2+1.5=3.5$.

---

## Ejemplos físicos

> [!ejemplo]
> | Sistema | $G(s)$ | $G(0)$ | Lectura física |
> |---|---|---|---|
> | Masa-resorte-amort. | $\dfrac{1}{ms^2+bs+k}$ | $1/k$ | fuerza 1 N → desplazamiento $1/k$ m |
> | Motor DC (velocidad) | $\dfrac{K_t}{Js+b}$ | $K_t/b$ | voltaje 1 V → velocidad $K_t/b$ rad/s |
> | Circuito RC | $\dfrac{1}{RCs+1}$ | $1$ | en DC el capacitor es abierto, $v_o=v_i$ |

---

## Interpretación y uso

> [!info]
> - $G(0)$ finito: amplifica/atenúa señales DC por ese factor.
> - $G(0)=0$: bloquea el DC (derivador, filtro pasa-altos).
> - $G(0)=\infty$: hay integradores; la salida crece sin límite ante DC.

> [!info] En diseño de compensadores
> - [[Lead | Lead]]: no altera $G(0)$.
> - [[Lag | Lag]]: aumenta $G(0)$ por un factor $\beta>1$ (reduce error estacionario).
> - [[PID | PID]]: el término integral $K_i/s$ lleva $G(0)\to\infty$.

---

## Limitaciones

> [!warning]
> 1. $G(0)=b_0/a_0$ **solo si** $a_0\neq 0$; si $a_0=0$ hay polo(s) en $s=0$ y $G(0)=\infty$.
> 2. $\lim_{t\to\infty}y(t)=G(0)$ **solo si** el sistema es estable.
> 3. Con realimentación no unitaria, usar $G(0)H(0)$ en los coeficientes de error.

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Definición | $G(0)=\lim_{s\to0}G(s)=b_0/a_0$ |
> | Valor final | $y(\infty)=G(0)$ (escalón, sistema estable) |
> | Serie / Paralelo | $G_1(0)G_2(0)$ / $G_1(0)+G_2(0)$ |
> | Realim. unitaria | $G(0)/(1+G(0))$ |
> | $G(0)=\infty$ | integrador (polo en $0$) |

> [!corolario]
> La ganancia estática resume en un número la respuesta de régimen permanente: cuánto amplifica el sistema una entrada constante. Evaluar $b_0/a_0$ es inmediato y, junto con la estabilidad, predice el valor final de la respuesta al escalón sin resolver la EDO. Es la base de los coeficientes de [[Error Estacionario/index | error estacionario]].

> [!referencia]
> - Marco general: [[Funcion Transferencia/index]].
> - Herramienta de cálculo: [[Teorema Valor Inicial Final]].
> - Aplicación: [[Error Estacionario/index]].
> - Interconexión: [[Algebra Diagramas]].
