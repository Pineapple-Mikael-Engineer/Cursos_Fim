---
title: Orden del Sistema
tags:
  - control-clasico
  - teoria
  - modelado
draft: false
aliases:
  - orden
  - grado del sistema
---

# Orden del Sistema

> [!definicion]
> El orden de un sistema es el grado del polinomio denominador de $G(s)$ **después de cancelar** los factores comunes con el numerador:
> $$G(s)=\frac{N(s)}{D(s)}\implies\text{orden}=\deg(D(s))\text{ tras cancelación}.$$
> Equivale al número de polos, de modos naturales y de condiciones iniciales independientes del sistema.

> [!info]
> Es un parámetro de la [[Funcion Transferencia/index | función de transferencia]] ligado a [[Polos Ceros | polos y ceros]] (cada polo = un modo). Coincide con la dimensión del estado en [[Espacio Estados/index | espacio de estados]]. La reducción de orden aproxima sistemas altos por uno de 1.º o 2.º orden vía polos dominantes.

---

## Ejemplo

> [!ejemplo] La cancelación reduce el orden
> $$G(s)=\frac{(s+1)}{(s+1)(s+2)(s+3)}=\frac{1}{(s+2)(s+3)}.$$
> **Paso 1 — Denominador original:** grado 3.
> **Paso 2 — Cancelar el factor común $(s+1)$.**
> **Paso 3 — Denominador efectivo:** $(s+2)(s+3)$, grado 2.
> **Orden = 2.** El sistema tiene solo dos modos observables: $e^{-2t}$ y $e^{-3t}$.

> [!ejemplo] Reducción 3.º → 1.er orden (polos dominantes)
> $$G(s)=\frac{10}{(s+1)(s+10)(s+20)}.$$
> Polos: $-1$ (lento, dominante), $-10$ y $-20$ (rápidos, $|\Re|\ge 10$). Los rápidos decaen ≥10× más rápido; se evalúan en $s=0$ dentro de sus factores:
> $$G(s)\approx\frac{10}{(s+1)(0+10)(0+20)}=\frac{0.05}{s+1}.$$
> Se conserva la ganancia estática $G(0)=10/200=0.05$ y el polo dominante.

> [!ejemplo] Reducción 3.º → 2.º orden (par complejo dominante)
> $$G(s)=\frac{100}{(s^2+2s+100)(s+20)}.$$
> Par complejo $-1\pm j9.95$ ($\zeta=0.1$, $\omega_n=10$) dominante; polo real $-20$ rápido. Evaluando el factor rápido en $s=0$:
> $$G(s)\approx\frac{100/20}{s^2+2s+100}=\frac{5}{s^2+2s+100}.$$
> Conserva $G(0)=100/(100\cdot20)=0.05$ y la dinámica oscilatoria dominante.

---

## Por qué importa el orden

> [!teoria]
> El orden fija el número de polos (modos) y de condiciones iniciales. La dinámica cualitativa depende de él:
>
> | Orden | Polos / modos | Respuesta típica |
> |---|---|---|
> | 1 | un polo, $e^{-t/\tau}$ | monótona, sin sobrepico |
> | 2 | dos polos (reales o complejos) | sobrepico si $\zeta<1$ |
> | $\ge 3$ | $n$ polos, $n$ modos | a menudo gobernada por [[Polos Ceros | polos dominantes]] |

> [!ejemplo] Órdenes canónicos
> Primer orden $G(s)=\dfrac{K}{\tau s+1}$ (orden 1). Segundo orden $G(s)=\dfrac{\omega_n^2}{s^2+2\zeta\omega_n s+\omega_n^2}$ (orden 2).

---

## Reducción de orden

> [!regla] Aproximación por polos dominantes
> Si hay polos con parte real mucho más negativa que el resto ($|\Re(p_\text{rápido})|\ge5\,|\Re(p_\text{lento})|$), los rápidos decaen casi al instante y se eliminan **conservando la ganancia estática** $G(0)$. El sistema de orden $n$ se aproxima por uno de orden 1 o 2.

> [!algoritmo] Receta de reducción
> 1. Hallar los polos y separar lentos (dominantes) de rápidos.
> 2. Verificar el factor 5× entre $|\Re|$ de rápidos y lentos.
> 3. Eliminar los factores rápidos $(s+p_\text{rápido})$ **evaluándolos en $s=0$** (es decir, sustituir $s+p\to p$).
> 4. Comprobar que $G(0)$ se mantiene; ajustar la constante si hace falta.
>
> ```matlab
> G = tf(10,[conv([1 1],conv([1 10],[1 20]))]);
> Gr = reduce(G,1);   % o balred para orden reducido
> step(G,'b',Gr,'r--')
> ```

> [!ejemplo] Sistema completo: planta + actuador
> $$G(s)=\frac{1}{(ms^2+bs+k)(\tau s+1)}.$$
> Orden 3. Si el actuador es rápido ($\tau$ pequeño, polo $-1/\tau$ lejano), se desprecia conservando su ganancia DC unitaria:
> $$G(s)\approx\frac{1}{ms^2+bs+k},$$
> de nuevo un segundo orden.

---

## Sistemas de orden superior

> [!info]
> - Par complejo dominante → comportamiento tipo segundo orden.
> - Polo real dominante → comportamiento tipo primer orden.
> - Polos múltiples dominantes → respuesta más lenta (factor $t^{r-1}$).

> [!warning]
> Reducir orden por cancelación polo-cero es válido **solo en la FT**. El sistema interno puede mantener modos no observables o no controlables. Ver [[Polos Ceros | polos y ceros]] y [[Espacio Estados/index | espacio de estados]].

---

## Relación con espacio de estados

> [!info]
> En [[Espacio Estados/index | espacio de estados]] el orden es la dimensión del vector de estado $x\in\mathbb{R}^n$. La FT $G(s)=C(sI-A)^{-1}B+D$ tiene denominador de grado $\le n$; las cancelaciones reducen el orden aparente.

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Orden | $\deg(D)$ tras cancelar |
> | Significado | nº de polos = modos = CI |
> | Cancelación | reduce orden aparente (cuidado interno) |
> | Reducción | despreciar polos rápidos, conservar $G(0)$ |
> | Estado | orden = $\dim(x)$ |

> [!corolario]
> El orden cuenta los modos que pueden manifestarse en la respuesta. Reducirlo —por cancelación legítima o por polos dominantes— simplifica el análisis sin perder lo esencial, siempre que se conserve la ganancia estática y se respete la salvedad de los modos internos no observables.

> [!referencia]
> - Definición base: [[Funcion Transferencia/index]].
> - Modos y dominancia: [[Polos Ceros]].
> - Dimensión del estado: [[Espacio Estados/index]].
