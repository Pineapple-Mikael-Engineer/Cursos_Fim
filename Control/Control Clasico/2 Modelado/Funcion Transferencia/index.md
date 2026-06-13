---
title: Función Transferencia
tags:
  - control-clasico
  - teoria
  - modelado
draft: false
aliases:
  - FT
  - G(s)
  - función de transferencia
---

# Función Transferencia

> [!definicion]
> La función de transferencia de un sistema **LTI** es el cociente entre la transformada de Laplace de la salida y la de la entrada, con **condiciones iniciales nulas**:
> $$G(s) = \frac{Y(s)}{U(s)}\bigg|_{\text{CI}=0}=\frac{b_m s^m + \dots + b_0}{a_n s^n + \dots + a_0},\qquad n\ge m.$$
> De una EDO $a_n y^{(n)}+\dots+a_0 y = b_m u^{(m)}+\dots+b_0 u$, los coeficientes pasan **directamente** a numerador y denominador.

> [!info]
> Es la representación central del [[Funcion Transferencia/index | modelado]] clásico. Sus parámetros se delegan a notas hijas: [[Polos Ceros | polos y ceros]] (modos y estabilidad), [[Orden | orden]] (grado y reducción), [[Ganancia Estatica | ganancia estática]] $G(0)$, [[Teorema Valor Inicial Final | valor inicial/final]] y [[Algebra Diagramas | álgebra de diagramas]] (interconexión). Es alternativa a [[Espacio Estados/index | espacio de estados]].

---

## Ejemplo

> [!ejemplo] De EDO a FT: masa-resorte-amortiguador
> Sistema $m\ddot{y}+b\dot{y}+ky=u$ con $m=1$, $b=3$, $k=2$. Hallar $G(s)$ y sus rasgos.
>
> **Paso 1 — Laplace con CI nulas** ($\mathcal{L}\{\ddot y\}=s^2Y$, $\mathcal{L}\{\dot y\}=sY$):
> $$(ms^2+bs+k)\,Y(s)=U(s).$$
>
> **Paso 2 — Despejar el cociente:**
> $$G(s)=\frac{Y(s)}{U(s)}=\frac{1}{ms^2+bs+k}=\frac{1}{s^2+3s+2}.$$
>
> **Paso 3 — Lectura inmediata de la FT:**
>
> | Rasgo | Cálculo | Resultado |
> |---|---|---|
> | Orden | grado de $D(s)$ | $2$ |
> | Polos | $s^2+3s+2=(s+1)(s+2)$ | $s=-1,\,-2$ (estable) |
> | Ceros | $N(s)=1$ | ninguno |
> | Ganancia estática | $b_0/a_0=1/2$ | $G(0)=0.5$ |
>
> Como ambos polos son reales y negativos, la respuesta es estable y sin oscilación; ante un escalón unitario, $y(\infty)=G(0)=0.5$.

> [!ejemplo] Circuito RC (primer orden)
> $RC\,\dot{v}_o+v_o=v_i$, con $R=10\ \text{k}\Omega$, $C=100\ \mu\text{F}$ ⟹ $\tau=RC=1\ \text{s}$.
> $$G(s)=\frac{1}{RCs+1}=\frac{1}{s+1}.$$
> Orden $1$, polo en $s=-1/\tau=-1$, $G(0)=1$ (en DC el capacitor es circuito abierto y $v_o=v_i$). Constante de tiempo $\tau=1\ \text{s}$. Ver [[Respuesta Temporal/Primer Orden | primer orden]].

> [!ejemplo] Motor DC (velocidad)
> $J\dot{\omega}+b\omega=K_t i_a$, entrada $i_a$, salida $\omega$:
> $$G(s)=\frac{K_t}{Js+b}.$$
> Orden $1$, polo en $s=-b/J$, ganancia estática $G(0)=K_t/b$: una corriente constante produce velocidad constante $K_t/b$.

---

## En qué consiste

> [!teoria]
> La FT existe **solo** para sistemas lineales e invariantes en el tiempo, porque se obtiene factorizando $Y(s)=G(s)U(s)$ a partir de Laplace, lo que exige CI nulas y operadores lineales de coeficientes constantes. Es una función racional propia ($n\ge m$): el denominador $D(s)$ codifica la dinámica propia (polos, modos naturales) y el numerador $N(s)$ codifica cómo la entrada excita esos modos (ceros).

> [!teorema] Forma racional desde la EDO
> Para $a_n y^{(n)}+\dots+a_0 y = b_m u^{(m)}+\dots+b_0 u$ con CI nulas:
> $$G(s)=\frac{b_m s^m+\dots+b_0}{a_n s^n+\dots+a_0}.$$

> [!demostracion]
> **Paso 1.** Por linealidad de Laplace y CI nulas, $\mathcal{L}\{f^{(k)}\}=s^k F(s)$ para cada derivada.
> **Paso 2.** Transformando ambos lados de la EDO:
> $$(a_n s^n+\dots+a_0)Y(s)=(b_m s^m+\dots+b_0)U(s).$$
> **Paso 3.** Como los paréntesis son escalares en $s$, se despeja el cociente y se obtiene $G(s)=Y(s)/U(s)$. $\blacksquare$

---

## Interconexión

> [!info] Álgebra de diagramas
> | Conexión | $G_{eq}(s)$ |
> |---|---|
> | Serie (cascada) | $G_1 G_2$ |
> | Paralelo | $G_1 + G_2$ |
> | Realimentación negativa | $\dfrac{G}{1+GH}$ |
> | Realimentación unitaria | $\dfrac{G}{1+G}$ |
>
> Reducción sistemática en [[Algebra Diagramas | álgebra de diagramas]].

---

## Relaciones con otras representaciones

> [!info] Respuesta impulsional
> $g(t)=\mathcal{L}^{-1}\{G(s)\}$ es la respuesta a $u(t)=\delta(t)$ con CI nulas. Por [[Convolucion | convolución]], $y(t)=(g*u)(t)$, es decir $Y(s)=G(s)U(s)$.

> [!info] Espacio de estados
> Dado $\dot{x}=Ax+Bu$, $y=Cx+Du$ con $x(0)=0$:
> $$G(s)=C(sI-A)^{-1}B+D.$$
> Ver [[Pasar a FT | de espacio de estados a FT]] y [[Espacio Estados/index | espacio de estados]] (admite CI no nulas, controlabilidad/observabilidad).

---

## Limitaciones

> [!warning]
> 1. **CI no nulas.** $G(s)$ supone $x(0)=0$; para CI arbitrarias usar [[Espacio Estados/index | espacio de estados]].
> 2. **Estabilidad interna.** Cancelar un polo inestable con un cero deja $G(s)$ estable pero el estado interno diverge. Ej.: $\frac{s-1}{s-1}\cdot\frac{1}{s+1}$ oculta el polo $s=1$. Ver [[Polos Ceros | polos y ceros]].
> 3. **No linealidad / variación temporal.** No existe $G(s)$; usar [[Linealizacion/index | linealización]] local.

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Definición | $G(s)=Y(s)/U(s)$ con CI$=0$ |
> | Existe para | sistemas LTI |
> | Forma | racional propia $N(s)/D(s)$, $n\ge m$ |
> | Polos | raíces de $D(s)$ → modos y estabilidad |
> | Ceros | raíces de $N(s)$ → bloqueo de modos |
> | $G(0)$ | $b_0/a_0$ → valor final a escalón |
> | Interconexión | serie $G_1G_2$, lazo $G/(1+GH)$ |

> [!corolario]
> La FT convierte una EDO lineal en un cociente de polinomios cuyos coeficientes se leen directamente: el denominador fija la dinámica (polos, estabilidad) y el numerador filtra cómo la entrada la excita (ceros). Toda la maquinaria de análisis clásico —respuesta temporal, error estacionario, lugar de raíces, frecuencia— se construye sobre esta representación.

> [!referencia]
> - Parámetros: [[Polos Ceros]], [[Orden]], [[Ganancia Estatica]].
> - Valor inicial/final: [[Teorema Valor Inicial Final]].
> - Interconexión: [[Algebra Diagramas]].
> - Representación alternativa: [[Espacio Estados/index]], [[Pasar a FT]].
