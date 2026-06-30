---
title: Solución de Transitorios con Laplace
tags:
  - circuitos-electricos
  - teoria
  - transitorios
  - laplace
draft: false
aliases:
  - solución de transitorios con Laplace
  - método de Laplace para transitorios
  - transient solution by Laplace
  - transient analysis by Laplace
---

# Solución de Transitorios con Laplace

> [!definicion]
> Es el **método sistemático** para resolver transitorios: (1) **transformar el circuito al dominio de $s$** —cada elemento por su impedancia $Z(s)$ y cada condición inicial por su fuente equivalente—; (2) **despejar algebraicamente** la incógnita $X(s)$ como en un circuito resistivo; (3) **antitransformar** (normalmente por fracciones parciales) para obtener $x(t)$. El método entrega de una vez la **respuesta natural y la forzada**, con las condiciones iniciales ya incorporadas.

> [!info]
> Es el método **completo** de [[Laplace en Circuitos/index| Laplace en circuitos]] ([[3 Almacenamiento y Transitorios/index| capítulo 3]]); reúne la [[Transformada de Laplace]] y los [[Circuitos en el Dominio de s]] en un solo procedimiento. Reproduce sin esfuerzo los resultados del [[Circuito RC]] y los de los sistemas de segundo orden, pero sin resolver ninguna ecuación diferencial. Fraile Mora, cap. 4, §4.9.

---

## Ejemplo

> [!ejemplo]
> **Carga del condensador en un RC, resuelta por Laplace.**
>
> Datos: $V_s=10\ \text{V}$ aplicada como **escalón** ($v(t)=V_s\,u(t)$, de modo que $\mathcal{L}\{V_s\,u(t)\}=V_s/s$), $R=2\ \text{k}\Omega$, $C=1\ \mu\text{F}$ y **condensador descargado** $v_C(0)=0$. La constante de tiempo es $\tau=RC=2\ \text{ms}$.
>
> ![[laplace_flujo.svg|600]]
>
> *El método: pasar al dominio de $s$, despejar $V_C(s)$ y antitransformar.*
>
> **Paso 1 — Plantear en $s$ (divisor de tensión).** Con la fuente transformada $V_s/s$ y las impedancias $Z_R=R$, $Z_C=1/sC$, la salida en el condensador es un simple divisor:
> $$V_C(s)=\frac{V_s}{s}\cdot\frac{1/sC}{R+1/sC}=\frac{V_s}{s\,(1+sRC)}.$$
> Como $v_C(0)=0$, **no** hace falta añadir ninguna fuente de condición inicial.
>
> **Paso 2 — Fracciones parciales.** Se separan los dos polos, en $s=0$ y en $s=-1/RC$:
> $$\frac{V_s}{s\,(1+sRC)}=V_s\!\left(\frac{1}{s}-\frac{1}{s+1/RC}\right).$$
>
> **Paso 3 — Antitransformar término a término** (cada uno está en la tabla: $1/s\to u(t)$ y $1/(s+a)\to e^{-at}$):
> $$v_C(t)=V_s\big(1-e^{-t/RC}\big)=10\big(1-e^{-t/2\,\text{ms}}\big)\ \text{V}.$$
>
> > [!solucion]
> > $$v_C(t)=10\big(1-e^{-t/2\,\text{ms}}\big)\ \text{V}.$$
> > Es el **mismo** resultado que en el [[Circuito RC]], pero obtenido de forma **sistemática**, sin plantear ni resolver la ecuación diferencial. El polo en $s=0$ fija el valor final $10\ \text{V}$ (régimen permanente) y el polo en $s=-1/RC$ genera la exponencial $e^{-t/RC}$ (respuesta natural).

---

## En qué consiste

> [!teoria] Por qué funciona
> Al transformar, la **ecuación diferencial** que gobierna el circuito se convierte en una **ecuación algebraica en $s$**, que se despeja exactamente como un circuito resistivo (con $Z$ en lugar de $R$). La **antitransformada por fracciones parciales** separa $X(s)$ en sus polos, y cada polo aporta su propio modo:
> - un **polo real** $s=-a$ da una **exponencial** $e^{-at}$;
> - un **par de polos complejos** $s=-\sigma\pm j\omega_d$ da una **oscilación amortiguada** $e^{-\sigma t}\cos(\omega_d t+\varphi)$.
>
> La gran ventaja: las **condiciones iniciales** (vía las fuentes equivalentes) y el **régimen permanente** (vía los polos de la entrada, p. ej. el $1/s$ del escalón) salen **juntos**, en un solo cálculo.

> [!algoritmo] Resolver un transitorio por Laplace
> **Paso 1 —** Transformar las **fuentes** (escalón $\to V_s/s$, impulso $\to 1$, rampa $\to 1/s^2$, etc.; ver [[Funciones Singulares]]) y los **elementos** por sus impedancias, añadiendo las fuentes de las **condiciones iniciales** de inductores y condensadores. **Paso 2 —** Resolver para $X(s)$ con **cualquier método resistivo** (divisores, mallas, nodos, Thévenin) sobre los [[Circuitos en el Dominio de s]]. **Paso 3 —** Descomponer $X(s)$ en **fracciones parciales** (un término por polo). **Paso 4 —** **Antitransformar** término a término con la tabla de la [[Transformada de Laplace]]. Comprobar con los teoremas del **valor inicial** $\big(x(0^+)=\lim_{s\to\infty}sX(s)\big)$ y del **valor final** $\big(x(\infty)=\lim_{s\to0}sX(s)\big)$.

> [!warning]
> Hay que **incluir las fuentes de condiciones iniciales** cuando los almacenadores **no** parten de cero; omitirlas falsea el transitorio. Y cuidar el **orden numerador/denominador** y la forma de las fracciones parciales: los **polos repetidos** exigen términos $\frac{A}{(s+a)^2}+\frac{B}{s+a}$ y los **polos complejos** se agrupan para reconstruir senos y cosenos amortiguados, no exponenciales reales.

## Resumen

> [!resumen]
> | Paso | Acción | Resultado |
> |:---|:---|:---|
> | 1 | Transformar fuentes y elementos (+ fuentes de C.I.) | Circuito en $s$ |
> | 2 | Resolver con método resistivo | $X(s)$ |
> | 3 | Fracciones parciales | Un término por polo |
> | 4 | Antitransformar con la tabla | $x(t)$ |

> [!corolario]
> Laplace unifica el análisis de transitorios: en lugar de resolver una EDO con sus constantes de integración, basta con **álgebra en $s$ + antitransformada**. La respuesta natural y la forzada aparecen juntas, y cada polo de $X(s)$ se lee directamente como un modo de la respuesta $x(t)$.

> [!referencia]
> Fraile Mora, cap. 4, §4.9. Reúne: [[Transformada de Laplace]], [[Circuitos en el Dominio de s]] y [[Funciones Singulares]]. Reproduce: [[Circuito RC]].
