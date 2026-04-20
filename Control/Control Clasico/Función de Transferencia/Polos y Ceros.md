---
title: Polos y Ceros
tags:
  - control-clasico
  - modelo-matematico
  - analisis-frecuencia
draft: true
aliases:
  - Poles and Zeros
  - Raíces del Sistema
  - Polinomio Característico
---

# Polos y Ceros

> [!definicion] Polos
> Sea un sistema [[Sistemas LTI]] con [[Función de Transferencia]] racional $G(s) = N(s)/D(s)$. Los **polos** $p_i \in \mathbb{C}$ son las raíces del polinomio denominador:
> $$
> D(p_i) = 0
> $$
> 
> En forma factorizada:
> $$
> G(s) = K \frac{(s - z_1)(s - z_2)\cdots(s - z_m)}{(s - p_1)(s - p_2)\cdots(s - p_n)}
> $$
> 
> **Interpretación física:** Los polos determinan los **modos naturales** del sistema. Cada polo aporta un término en la respuesta temporal de la forma $A_i e^{p_i t}$.

> [!definicion] Ceros
> Los **ceros** $z_i \in \mathbb{C}$ son las raíces del polinomio numerador:
> $$
> N(z_i) = 0
> $$
> 
> **Interpretación física:** Los ceros **bloquean** ciertas frecuencias de entrada. Si la entrada es $u(t) = e^{z_i t}$, la salida es idénticamente cero (cancelación entrada-salida).

---

## Relación entre Polos y Respuesta Temporal

> [!teorema] Descomposición en Fracciones Parciales
> Para un sistema con polos distintos, la respuesta al impulso es:
> $$
> h(t) = \sum_{i=1}^{n} A_i e^{p_i t} \cdot \mathbf{1}(t)
> $$
> donde los residuos $A_i$ dependen de los ceros y de la ubicación de los polos.

> [!proposicion] Tipos de polos y su respuesta
> | Tipo de polo | Ubicación | Término en $h(t)$ | Comportamiento |
> |--------------|-----------|-------------------|----------------|
> | Real negativo | $\sigma < 0$, $\omega = 0$ | $A e^{\sigma t}$ | Decae a cero |
> | Real positivo | $\sigma > 0$, $\omega = 0$ | $A e^{\sigma t}$ | Crece sin límite |
> | Real cero | $\sigma = 0$, $\omega = 0$ | $A \cdot \mathbf{1}(t)$ | Constante |
> | Complejo conjugado | $\sigma < 0$, $\omega \neq 0$ | $2\|A\| e^{\sigma t} \cos(\omega t + \phi)$ | Oscila amortiguado |
> | Complejo conjugado | $\sigma = 0$, $\omega \neq 0$ | $2\|A\| \cos(\omega t + \phi)$ | Oscila sostenido |
> | Complejo conjugado | $\sigma > 0$, $\omega \neq 0$ | $2\|A\| e^{\sigma t} \cos(\omega t + \phi)$ | Oscila creciente |

---

## Estabilidad BIBO

> [!definicion] Estabilidad BIBO
> Un sistema es **BIBO estable** (Bounded Input Bounded Output) si toda entrada acotada produce una salida acotada. Ver [[Estabilidad BIBO]] para un desarrollo completo.

> [!teorema] Condición de Estabilidad vía Polos
> Un sistema [[Sistemas LTI]] causal con [[Función de Transferencia]] racional es BIBO estable si y solo si **todos los polos** tienen parte real estrictamente negativa:
> $$
> \Re(p_i) < 0, \quad \forall i
> $$

| Condición de polos | Estabilidad |
|--------------------|-------------|
| $\Re(p_i) < 0$ para todo $i$ | **Estable** |
| $\Re(p_i) \le 0$ y polos en eje imaginario simples | **Marginalmente estable** |
| Algún $\Re(p_i) > 0$ o polos múltiples en eje imaginario | **Inestable** |

> [!ejemplo] Sistema estable
> $G(s) = \dfrac{1}{s+2}$: Polo en $p = -2$ → estable.
> $h(t) = e^{-2t} \mathbf{1}(t)$ decae a cero.

> [!ejemplo] Sistema inestable
> $G(s) = \dfrac{1}{s-2}$: Polo en $p = +2$ → inestable.
> $h(t) = e^{2t} \mathbf{1}(t)$ crece sin límite.

> [!ejemplo] Sistema marginalmente estable
> $G(s) = \dfrac{1}{s^2 + \omega_0^2}$: Polos en $p = \pm j\omega_0$ → marginalmente estable.
> $h(t) = \frac{1}{\omega_0} \sin(\omega_0 t) \mathbf{1}(t)$ oscila permanentemente.

---

## Relación entre Ceros y Respuesta Temporal

> [!teoria] Efecto de los ceros
> Los ceros **no afectan la estabilidad** (no aparecen en el polinomio característico), pero modifican:
> 1. Los **residuos** $A_i$ en la expansión en fracciones parciales
> 2. La **sobreoscilación** (overshoot) en la respuesta escalón
> 3. La **respuesta inicial** $y(0^+)$

> [!proposicion] Teorema del Valor Inicial
> $$
> y(0^+) = \lim_{s \to \infty} s Y(s) = \lim_{s \to \infty} s G(s) U(s)
> $$
> - Si $G(s)$ es **estrictamente propia** ($m < n$), entonces $y(0^+) = 0$
> - Si $G(s)$ es **propia** ($m = n$), entonces $y(0^+) = K \cdot u(0^+)$ donde $K = b_m/a_n$

> [!ejemplo] Cero en semiplano izquierdo (SPI)
> $G(s) = \dfrac{s+2}{s+1}$:
> - Cero en $z = -2$, polo en $p = -1$
> - Respuesta al escalón: $y(t) = 2 - e^{-t}$ (sin sobreoscilación)

> [!ejemplo] Cero en semiplano derecho (SPD) - Fase no mínima
> $G(s) = \dfrac{s-2}{s+1}$:
> - Cero en $z = +2$ (SPD), polo en $p = -1$
> - Respuesta al escalón: $y(t) = -2 + 3e^{-t}$
> - **Suboscilación inicial (undershoot):** $y(0^+) = 1$ (valor inicial positivo), luego baja a negativo antes de subir a 2

```tikz
\begin{tikzpicture}
  \draw[->] (0,0) -- (4,0) node[right] {$t$};
  \draw[->] (0,-1.5) -- (0,2.5) node[above] {$y(t)$};
  \draw[dashed] (0,2) -- (4,2) node[right] {$y(\infty)=2$};
  \draw[domain=0:3.5, smooth, variable=\x, red] plot ({\x}, {-2+3*exp(-\x)});
  \node[red] at (2, 0.5) {Undershoot};
\end{tikzpicture}
```

---

## Diagrama de Polos y Ceros en el Plano $s$

> [!definicion] Representación Gráfica
> El **plano $s$** tiene eje real $\sigma$ (amortiguamiento) y eje imaginario $j\omega$ (frecuencia).
> - $\times$ (cruz) = polo
> - $\circ$ (círculo) = cero

```
    jω
     ↑
   3 +   × (polo)
   2 +
   1 +       ○ (cero)
     |
----+----+----+----→ σ
   -3  -2  -1   0
   1 +
   2 +
   3 +   × (polo conjugado)
```

> [!teorema] Simetría Conjugada
> Si todos los coeficientes de $G(s)$ son reales, los polos y ceros complejos aparecen en **pares conjugados**:
> $$
> \text{Si } p = \sigma + j\omega \text{ es polo, entonces } p^* = \sigma - j\omega \text{ también lo es}
> $$

> [!proposicion] Regiones del plano $s$
> - **Región de estabilidad:** Semiplano izquierdo abierto ($\sigma < 0$)
> - **Frontera:** Eje imaginario ($\sigma = 0$)
> - **Región de inestabilidad:** Semiplano derecho ($\sigma > 0$)

---

## Teoremas Fundamentales

> [!teorema] Teorema Fundamental del Álgebra
> Un polinomio de grado $n$ tiene exactamente $n$ raíces en $\mathbb{C}$ (contando multiplicidades). Por lo tanto:
> - Un sistema de orden $n$ tiene **exactamente $n$ polos**
> - Un sistema con $m \le n$ tiene **exactamente $m$ ceros**

> [!teorema] Cancelación Polo-Cero
> Si un polo y un cero coinciden exactamente ($z_i = p_j$), se cancelan algebraicamente:
> $$
> G(s) = \frac{(s - z)}{(s - z)(s - p)} = \frac{1}{s - p}
> $$

> [!warning]
> La cancelación es válida en la [[Función de Transferencia]], pero el polo cancelado puede reaparecer si las condiciones iniciales no son nulas o hay perturbaciones. **No cancelar polos inestables.**

---

## Métodos de Cálculo

> [!teoria] ¿Cómo encontrar polos y ceros?
> 1. **Desde $G(s)$:** Factorizar $N(s)$ y $D(s)$
> 2. **Desde la EDO:** $D(s)$ es el polinomio característico
> 3. **Desde $h(t)$:** Los polos son los exponentes en $h(t) = \sum A_i e^{p_i t}$
> 4. **Desde espacio de estado:** Polos = autovalores de la matriz $A$

> [!ejemplo] Cálculo desde EDO
> Dada $\ddot{y} + 5\dot{y} + 6y = \dot{u} + 2u$:
> - Laplace con C.I. nulas: $(s^2 + 5s + 6)Y(s) = (s + 2)U(s)$
> - $G(s) = \dfrac{s + 2}{s^2 + 5s + 6} = \dfrac{s + 2}{(s + 2)(s + 3)} = \dfrac{1}{s + 3}$
> - Cero en $z = -2$ cancela con polo en $p = -2$
> - Polo remanente: $p = -3$

---

## Polos y Ceros en Sistemas Discretos

> [!definicion] Caso Discreto
> Para sistemas discretos LTI con [[Función de Transferencia]] en $z$:
> $$
> H(z) = \frac{b_m z^m + \dots + b_0}{a_n z^n + \dots + a_0}
> $$
> - **Polos:** Raíces del denominador
> - **Ceros:** Raíces del numerador
> 
> **Condición de estabilidad (discreto):** Todos los polos deben satisfacer $|p_i| < 1$ (dentro del círculo unitario).

