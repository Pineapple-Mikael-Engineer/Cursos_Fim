---
title: Trapecio Compuesto y Convergencia O(h²)
tags:
  - metodos-numericos
  - teoria
  - diferenciacion-integracion
  - integracion-numerica
  - newton-cotes
  - convergencia
draft: false
aliases:
  - Trapecio compuesto
  - Composite trapezoidal
  - Regla del trapecio compuesta
---

# Trapecio Compuesto y Convergencia $O(h^2)$

> [!definicion]
> El **trapecio compuesto** divide $[a,b]$ en $n$ subintervalos iguales de paso $h = \frac{b-a}{n}$ y aplica la [[Trapecio Error Truncamiento Segunda Derivada|regla del trapecio]] en cada uno:
> $$\int_a^b f(x)\,dx \approx h\left(\frac{f_0}{2} + f_1 + f_2 + \cdots + f_{n-1} + \frac{f_n}{2}\right) = \frac{h}{2}\Big(f_0 + 2\sum_{i=1}^{n-1}f_i + f_n\Big).$$

> [!info]
> Los nodos internos cuentan con peso doble (compartidos por dos paneles); los extremos, peso simple. Su error global es $O(h^2)$, y su expansión de error —solo potencias pares de $h$— lo hace base ideal de la extrapolación de [[Extrapolacion Richardson Aceleracion Convergencia|Romberg]].

---

## Error global

> [!teorema]
> Si $f \in C^2[a,b]$, el error del trapecio compuesto es
> $$\int_a^b f\,dx - T_n = -\frac{(b-a)h^2}{12}f''(\xi), \qquad \xi\in(a,b),$$
> es decir $O(h^2)$: global, no por panel.

> [!demostracion]
> El error por panel $[x_{i}, x_{i+1}]$ es $-\frac{h^3}{12}f''(\xi_i)$ ([[Trapecio Error Truncamiento Segunda Derivada|regla simple]]). Sumando los $n$ paneles:
> $$E = -\frac{h^3}{12}\sum_{i=0}^{n-1}f''(\xi_i) = -\frac{h^3}{12}\,n\,\overline{f''} = -\frac{h^3}{12}\cdot\frac{b-a}{h}\,\overline{f''} = -\frac{(b-a)h^2}{12}\overline{f''},$$
> donde $\overline{f''} = \frac{1}{n}\sum f''(\xi_i)$ es un valor medio, igual a $f''(\xi)$ por el teorema del valor intermedio (continuidad). Se pierde una potencia de $h$ al sumar $n = (b-a)/h$ paneles: de $O(h^3)$ por panel a $O(h^2)$ global.

---

## Ejemplo

> [!ejemplo]
> **$\int_0^1 e^x\,dx = e-1 \approx 1.718282$**, trapecio compuesto:
>
> | $n$ | $h$ | $T_n$ | error | factor |
> |:---:|:---:|:---:|:---:|:---:|
> | 1 | 1 | 1.859141 | $1.4\times10^{-1}$ | — |
> | 2 | 0.5 | 1.753931 | $3.6\times10^{-2}$ | 3.9 |
> | 4 | 0.25 | 1.727222 | $8.9\times10^{-3}$ | 4.0 |
> | 8 | 0.125 | 1.720519 | $2.2\times10^{-3}$ | 4.0 |
>
> Halvar $h$ divide el error por $\approx 4 = 2^2$, confirmando $O(h^2)$.

---

## Fórmula de Euler-Maclaurin

> [!teoria]
> El error del trapecio compuesto admite la expansión de **Euler-Maclaurin**, que solo contiene potencias **pares** de $h$:
> $$\int_a^b f - T_n = -\frac{h^2}{12}\big[f'(b)-f'(a)\big] - \frac{h^4}{720}\big[f'''(b)-f'''(a)\big] - \cdots$$
> Dos consecuencias clave:
> 1. La estructura en potencias pares hace que la extrapolación de [[Extrapolacion Richardson Aceleracion Convergencia|Romberg]] suba de $O(h^2)$ a $O(h^4)$ de golpe.
> 2. Si $f$ es **periódica** con período $b-a$, los términos de borde $f^{(k)}(b)-f^{(k)}(a)$ se anulan: el trapecio converge **espectralmente** (más rápido que cualquier potencia de $h$).

---

## Cálculo incremental

> [!info]
> Al duplicar $n$, las evaluaciones previas se **reutilizan**:
> $$T_{2n} = \frac{1}{2}T_n + h_{2n}\sum_{\text{nodos nuevos}} f(x_i),$$
> donde los nodos nuevos son los puntos medios de los paneles anteriores. Esto hace eficiente el refinamiento sucesivo (clave en Romberg y métodos adaptativos): solo se evalúa $f$ en los puntos añadidos.

---

## Relación con otras notas

> [!info]
> - La regla simple que se repite: [[Trapecio Error Truncamiento Segunda Derivada]].
> - Su aceleración a $O(h^4)$ y más: [[Extrapolacion Richardson Aceleracion Convergencia]] (Romberg).
> - La regla compuesta de mayor orden: [[Simpson Compuesto Convergencia O h4]].
> - El contraste con la inestabilidad de grado alto: [[Inestabilidad Pesos Negativos Grado Alto]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Fórmula | $\frac{h}{2}(f_0 + 2\sum f_i + f_n)$ |
| Error global | $-\frac{(b-a)h^2}{12}f''(\xi)$ |
| Orden | $O(h^2)$ |
| Expansión | Euler-Maclaurin (potencias pares) |
| Refinamiento | incremental ($T_{2n} = \frac12 T_n + \cdots$) |
| Periódicas | convergencia espectral |

> [!corolario]
> El trapecio compuesto suma trapecios sobre $n$ paneles, dando $\frac{h}{2}(f_0 + 2\sum f_i + f_n)$ con error global $-\frac{(b-a)h^2}{12}f''(\xi) = O(h^2)$: se pierde una potencia de $h$ al sumar $(b-a)/h$ paneles. Su expansión de Euler-Maclaurin, en potencias pares, lo hace base ideal de [[Extrapolacion Richardson Aceleracion Convergencia|Romberg]] (sube a $O(h^4)$) y explica su convergencia espectral para integrandos periódicos. El refinamiento incremental reutiliza evaluaciones, haciéndolo eficiente. Para mayor orden directo se usa [[Simpson Compuesto Convergencia O h4|Simpson compuesto]].
