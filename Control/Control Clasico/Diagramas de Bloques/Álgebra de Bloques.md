---
title: "Álgebra de Bloques"
tags:
  - control-clasico
  - diagramas-de-bloques
  - algebra
draft: false
aliases:
  - Block Diagram Algebra
  - Conexión de Bloques
  - Combinación de Bloques
---

# Álgebra de Bloques

> [!definicion] Representación en Bloques
> Un **diagrama de bloques** es una representación gráfica de un [[Sistemas LTI|sistema de control]] donde:
> - **Bloques** representan [[Función de Transferencia/index|funciones de transferencia]] $G(s)$
> - **Flechas** representan señales (entradas, salidas, variables intermedias)
> - **Sumadores** (nodos suma) combinan señales con signo $+$ o $-$
> - **Puntos de bifurcación** (nodos) distribuyen una señal a múltiples destinos


Ejemplo de bloque básico:

![[Algebra_Bloques_01.svg|500]]



---

## Conexiones Fundamentales

> [!teoria] Tres Conexiones Básicas
> A partir de estas tres conexiones, puede construirse cualquier [[Diagramas de Bloques/index|diagrama de bloques]] complejo. Son los "átomos" del álgebra de bloques.

### 1. Conexión en Serie (Cascada)

> [!definicion] Serie
> Dos bloques $G_1(s)$ y $G_2(s)$ en serie, donde la salida del primero es la entrada del segundo.

![[Algebra_Bloques_02.svg|500]]

> [!teorema] Función de Transferencia Equivalente
> $$
> G_{\text{eq}}(s) = G_1(s) \cdot G_2(s)
> $$

> [!demostracion]
> Sean $y_1 = G_1 u$ y $y = G_2 y_1$. Sustituyendo: $y = G_2 (G_1 u) = (G_2 G_1) u$. 
> 
> Como el producto de [[Función de Transferencia/index|funciones de transferencia]] conmuta (son funciones complejas), $G_2 G_1 = G_1 G_2$. Por lo tanto $G_{\text{eq}} = G_1 G_2$. $\square$

> [!ejemplo] Sistema de dos filtros en cascada
> Sean $G_1(s) = \dfrac{1}{s+1}$ y $G_2(s) = \dfrac{2}{s+2}$:
> $$
> G_{\text{eq}}(s) = \frac{1}{s+1} \cdot \frac{2}{s+2} = \frac{2}{(s+1)(s+2)}
> $$
> 
> El sistema equivalente es un sistema de segundo orden (ver [[Polos y Ceros]]).

> [!warning]
> La conexión en serie es válida en [[Función de Transferencia/index|funciones de transferencia]] ideales. En [[Sistemas LTI|sistemas físicos reales]], debe verificarse que la impedancia de salida de $G_1$ sea despreciable frente a la impedancia de entrada de $G_2$ (efecto de carga).

### 2. Conexión en Paralelo

> [!definicion] Paralelo
> Dos bloques $G_1(s)$ y $G_2(s)$ en paralelo comparten la misma entrada y sus salidas se suman.

![[Algebra_Bloques_03.svg|500]]

> [!teorema] Función de Transferencia Equivalente
> $$
> G_{\text{eq}}(s) = G_1(s) + G_2(s)
> $$

> [!demostracion]
> Sean $y_1 = G_1 u$ e $y_2 = G_2 u$. La salida total es $y = y_1 + y_2 = G_1 u + G_2 u = (G_1 + G_2) u$. $\square$

> [!ejemplo] Controlador PID en paralelo
> Un [[Controlador PID]] tiene tres acciones en paralelo:
> $$
> G_{\text{PID}}(s) = K_p + \frac{K_i}{s} + K_d s
> $$
> 
> Cada término actúa sobre la misma señal de error y sus salidas se suman.

### 3. Conexión en Realimentación (Feedback)

> [!definicion] Realimentación
> Un sistema con realimentación tiene un bloque $G(s)$ en la trayectoria directa y un bloque $H(s)$ en la trayectoria de realimentación.

![[Algebra_Bloques_04.svg|500]]

> [!teorema] Función de Transferencia en Lazo Cerrado
> - **Realimentación negativa** (signo $-$ en el sumador, el más común en [[Control Clásico|control]]):
>   $$
>   G_{\text{lc}}(s) = \frac{G(s)}{1 + G(s)H(s)}
>   $$
> 
> - **Realimentación positiva** (signo $+$ en el sumador, usado en [[Osciladores]]):
>   $$
>   G_{\text{lc}}(s) = \frac{G(s)}{1 - G(s)H(s)}
>   $$

> [!demostracion] (Caso negativo)
> Sean:
> - $e = u - y_f$ (señal de error)
> - $y = G e$
> - $y_f = H y$
> 
> Sustituyendo: $y = G(u - H y) = G u - G H y$
> 
> Despejando $y$: $y + G H y = G u \Rightarrow y(1 + G H) = G u$
> 
> Por lo tanto: $\dfrac{y}{u} = \dfrac{G}{1 + G H}$ $\square$

> [!ejemplo] Sistema de primer orden con realimentación unitaria
> Sea $G(s) = \dfrac{K}{s + a}$ y $H(s) = 1$:
> $$
> G_{\text{lc}}(s) = \frac{\frac{K}{s+a}}{1 + \frac{K}{s+a}} = \frac{K}{s + a + K}
> $$
> 
> El [[Polos y Ceros|polo]] del sistema en lazo cerrado es $p = -(a + K)$. Aumentar $K$ acelera la respuesta.

> [!ejemplo] Sistema con realimentación no unitaria
> Sea $G(s) = \dfrac{1}{s}$ (integrador) y $H(s) = K$ (ganancia constante):
> $$
> G_{\text{lc}}(s) = \frac{\frac{1}{s}}{1 + \frac{1}{s} \cdot K} = \frac{1}{s + K}
> $$
> 
> El sistema integrador puro se convierte en un sistema de primer orden [[Estabilidad BIBO|estable]].

---

## Función de Transferencia en Lazo Cerrado con Perturbaciones

> [!teoria] Sistema con Entrada de Perturbación
> En [[Sistemas de Control|sistemas de control reales]], además de la referencia $R(s)$, existen perturbaciones $D(s)$ que afectan la salida.

![[Algebra_Bloques_05.svg|500]]


> [!teorema] Salida Total por Superposición
> Dado que el [[Sistemas LTI|sistema es lineal]], la salida es la suma de los efectos de cada entrada:
> $$
> Y(s) = \underbrace{\frac{G_1 G_2}{1 + G_1 G_2 H}}_{\text{Referencia}} R(s) + \underbrace{\frac{G_2}{1 + G_1 G_2 H}}_{\text{Perturbación}} D(s) - \underbrace{\frac{G_1 G_2 H}{1 + G_1 G_2 H}}_{\text{Ruido}} N(s)
> $$

> [!info] Interpretación
> - **Referencia $R(s)$:** La [[Función de Transferencia/index|función de transferencia]] deseada
> - **Perturbación $D(s)$:** Se atenúa con alta ganancia $G_1 G_2$ (ver [[Sensibilidad]])
> - **Ruido $N(s)$:** Se amplifica con alta ganancia (trade-off fundamental)

---

## Sistemas con Múltiples Lazos

> [!teoria] Reducción Sistemática
> Para sistemas con múltiples lazos de realimentación anidados:
> 1. Identificar los lazos internos (los que no contienen otros lazos dentro)
> 2. Reducir cada lazo interno usando $G_{\text{lc}} = G/(1+GH)$
> 3. Repetir el proceso hasta obtener un solo lazo
> 4. Aplicar la fórmula de realimentación final

> [!ejemplo] Dos lazos anidados (realimentación doble)
> 
> ![[Algebra_Bloques_06.svg|500]]
> 
> **Solución paso a paso:**
> 1. Reducir el lazo interno (alrededor de $G_2$):
>    $$
>    G_{\text{int}} = \frac{G_2}{1 + G_2 H_1}
>    $$
> 2. El sistema se reduce a $G_1$ en serie con $G_{\text{int}}$ con realimentación $H_2$:
>    $$
>    G_{\text{total}} = \frac{G_1 \cdot G_{\text{int}}}{1 + G_1 \cdot G_{\text{int}} \cdot H_2}
>    $$
> 3. Sustituyendo $G_{\text{int}}$:
>    $$
>    G_{\text{total}} = \frac{G_1 G_2}{1 + G_2 H_1 + G_1 G_2 H_2}
>    $$

> [!ejemplo] Sistema con realimentación y alimentación directa (feedforward)
> 
> ![[Algebra_Bloques_07.svg|500]]
> 
> La señal $u$ también pasa por $G_3$ y se suma antes de $G_2$. Este tipo de configuraciones requieren mover bloques o aplicar reglas de transformación (ver [[Movimiento de Nodos]] y [[Reducción de Diagramas]]).
