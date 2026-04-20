---
title: Epsilon Maquina y Precision Relativa
tags:
  - metodos-numericos
  - teoria
  - aritmetica-computacional
  - error-numerico
draft: false
aliases:
  - Unidad de redondeo
  - Machine epsilon
  - ε_mach
  - u
---

# Épsilon de Máquina y Precisión Relativa $u$

> [!definicion]
> El **épsilon de máquina**, denotado $\varepsilon_{\text{mach}}$ o simplemente $u$, se define como la distancia entre el número $1.0$ y el siguiente número representable en el sistema de [[Representacion Punto Flotante IEEE 754|punto flotante]].

En otras palabras, es el número positivo más pequeño tal que:
$$\text{fl}(1 + \varepsilon_{\text{mach}}) > 1$$

Para el formato **binary64** (precisión doble) del estándar IEEE 754:
$$u = 2^{-52} \approx 2.220446049250313 \times 10^{-16}$$

Para el formato **binary32** (precisión simple):
$$u = 2^{-23} \approx 1.1920928955078125 \times 10^{-7}$$

---

## Deducción formal

En un sistema de punto flotante con $p$ bits de precisión (incluyendo el bit implícito), el espaciado entre números consecutivos en el intervalo $[2^E, 2^{E+1})$ es:
$$\Delta x = 2^{E - (p - 1)}$$

> [!teoria]
> **Cálculo de $u$.**
> Para el intervalo $[1, 2)$, el exponente real es $E = 0$. Por tanto, el espaciado entre $1.0$ y el siguiente número representable es:
> $$u = 2^{0 - (p - 1)} = 2^{-(p - 1)}$$
> 
> En precisión doble, $p = 53$ (52 bits almacenados + 1 bit implícito), luego:
> $$u = 2^{-52}$$

> [!ejemplo]
> **Verificación conceptual de $u$ en precisión simple.**
> 
> En binary32, la fracción tiene $23$ bits. El número $1.0$ se representa como:
> - Signo: $0$
> - Exponente: $127$ ($E = 0$)
> - Fracción: $000\dots 0$
> 
> El siguiente número representable se obtiene incrementando el bit menos significativo de la fracción:
> - Fracción: $000\dots 1$ (un $1$ en la posición $2^{-23}$)
> 
> El valor de este número es $1 + 2^{-23}$. La diferencia es exactamente $2^{-23}$, que coincide con la fórmula $u = 2^{-(24-1)}$.

---

## Relación con el error relativo de redondeo

El épsilon de máquina no es meramente una curiosidad aritmética, sino la **cota superior del error relativo** cometido al representar un número real en el sistema flotante.

> [!teorema]
> **Cota del error relativo de redondeo.**
> Para cualquier número real $x$ dentro del rango normalizado del sistema flotante, existe una representación $\text{fl}(x)$ tal que:
> $$\frac{|x - \text{fl}(x)|}{|x|} \leq u$$
> 
> Equivalentemente, $\text{fl}(x) = x(1 + \delta)$ con $|\delta| \leq u$.

Esta propiedad es la piedra angular del análisis de error *forward* en métodos numéricos.

> [!ejemplo]
> **Ilustración del error relativo.**
> 
> Consideremos el número real $x = \frac{1}{3}$ en precisión doble.
> 
> La representación binaria exacta es periódica: $0.010101\dots_2$.
> 
> Al redondear a $53$ bits de precisión, el valor almacenado $\text{fl}(x)$ difiere de $x$ en aproximadamente $0.333\dots$
> 
> El error relativo es:
> $$\frac{|\frac{1}{3} - \text{fl}(\frac{1}{3})|}{\frac{1}{3}} \approx 1.1 \times 10^{-16} < u$$
> 
> Esto confirma que el error relativo nunca excede $u$, independientemente de la magnitud del número (siempre que esté en rango normalizado).

---

## Distinción crucial: $u$ vs. el menor número representable

Es común confundir el épsilon de máquina con el menor número positivo representable. Son conceptos **completamente distintos**.

| Concepto | Definición | Valor típico (doble) |
|:---|:---|:---|
| **Épsilon de máquina ($u$)** | Espaciado relativo en $[1,2)$ | $\approx 2.22 \times 10^{-16}$ |
| **Menor normalizado positivo** | Límite inferior del rango normalizado | $\approx 2.23 \times 10^{-308}$ |
| **Menor subnormal positivo** | Límite absoluto del underflow gradual | $\approx 4.94 \times 10^{-324}$ |

> [!info]
> El menor número positivo representable está determinado por el **exponente mínimo**, no por la mantisa. Para detalles sobre los límites del rango, véase [[Underflow y Numeros Subnormales]].

---

## Modelo de aritmética flotante

La propiedad $\text{fl}(x \circ y) = (x \circ y)(1 + \delta)$ con $|\delta| \leq u$ permite construir un modelo algebraico simple para analizar algoritmos.

> [!proposicion]
> **Modelo estándar para el error de redondeo.**
> Para cualquier operación básica $\circ \in \{+, -, \times, \div\}$:
> $$\text{fl}(x \circ y) = (x \circ y)(1 + \delta), \quad |\delta| \leq u$$
> Este modelo asume el [[Modos de Redondeo IEEE 754|modo de redondeo]] por defecto (*round to nearest, ties to even*).

Este modelo es la base para derivar cotas de error en:
- Suma de $n$ números (error acumulado $O(nu)$ si se ordenan adecuadamente).
- Producto matriz-vector (Ver [[Propagacion Errores Operaciones Matriciales]]).
- [[Eliminacion Gaussiana]] y [[Factorizacion LU]].

---

## Determinación numérica de $u$

El épsilon de máquina puede calcularse experimentalmente sin conocer los detalles internos del hardware, mediante un algoritmo simple.

> [!ejemplo]
> **Algoritmo para aproximar $u$ en cualquier sistema.**
> 
> ```
> u = 1.0
> mientras (1.0 + u) > 1.0:
>     u = u / 2.0
> fin mientras
> u = u * 2.0
> ```
> 
> **Explicación:**
> El bucle divide $u$ sucesivamente por $2$ hasta que $1 + u$ se redondea exactamente a $1$ (debido al espaciado finito). El valor buscado es el doble del último valor que aún produjo $1 + u > 1$.
> 
> En precisión doble, este algoritmo retorna exactamente $2^{-52}$.

---

## Implicaciones para el análisis numérico

El conocimiento de $u$ establece un **límite de expectativa realista** para cualquier cálculo numérico.

> [!warning]
> **Precisión finita como límite fundamental.**
> Ningún algoritmo puede proporcionar más de $-\log_{10}(u) \approx 16$ dígitos decimales de precisión en doble precisión. La meta del análisis numérico no es superar esta barrera, sino **evitar que el error crezca más allá de $O(u \cdot \kappa)$**, donde $\kappa$ es el [[Condicionamiento Numerico Numero Condicion|número de condición]] del problema.

Por ejemplo:
- En la [[Biseccion]], el error mínimo alcanzable está limitado por $u \cdot |r|$, donde $r$ es la raíz.
- En [[Newton Raphson]], la convergencia cuadrática se estanca cuando el error alcanza $\approx u \cdot |r|$.
- En métodos de [[Runge Kutta]], el error de truncamiento domina inicialmente, pero el error de redondeo eventualmente limita la precisión alcanzable al reducir el paso $h$.
