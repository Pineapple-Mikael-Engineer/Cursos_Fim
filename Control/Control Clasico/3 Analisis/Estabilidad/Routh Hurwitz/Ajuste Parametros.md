---
title: Ajuste de Parámetros con Routh-Hurwitz
tags:
  - control-clasico
  - teoria
  - analisis
  - estabilidad
  - routh-hurwitz
draft: false
aliases:
  - rango de estabilidad
  - ajuste parametros routh
  - ganancia crítica
---

# Ajuste de Parámetros con Routh-Hurwitz

# Definición

> [!definicion] Problema típico
> Dado un sistema con realimentación unitaria y función transferencia de lazo abierto $G(s)$ que contiene un parámetro $K$ en el **denominador**, determinar el **rango de valores** de $K$ para el cual el sistema en lazo cerrado es estable.
>
> La ecuación característica es:
> $$1 + G(s) = 0$$

# Procedimiento general

> [!info] Pasos
> 1. Obtener la ecuación característica $1 + G(s) = 0$
> 2. Escribir el polinomio característico $P(s)$
> 3. Construir la tabla de Routh con coeficientes que dependen de $K$
> 4. Imponer que **todos los elementos de la primera columna** sean $> 0$ (si $a_n > 0$)
> 5. Resolver las desigualdades resultantes
> 6. Encontrar la intersección de todos los rangos

# Ejemplo 1: Parámetro en el denominador

> [!ejemplo] $G(s) = \frac{1}{s(s+1)(s+2) + K}$
>
> **Paso 1:** Ecuación característica
> $$1 + \frac{1}{s(s+1)(s+2) + K} = 0$$
>
> **Paso 2:** Polinomio característico
> $$s(s+1)(s+2) + K + 1 = 0$$
>
> $$P(s) = s^3 + 3s^2 + 2s + (K+1) = 0$$

> **Paso 3:** Tabla de Routh
> $$
> \begin{array}{c|cc}
> s^3 & 1 & 2 \\
> s^2 & 3 & K+1 \\
> s^1 & \frac{3 \cdot 2 - 1 \cdot (K+1)}{3} = \frac{6 - K - 1}{3} = \frac{5 - K}{3} & 0 \\
> s^0 & K+1 & 
> \end{array}
> $$

> **Paso 4:** Condiciones de estabilidad
> $$1 > 0,\quad 3 > 0,\quad \frac{5 - K}{3} > 0,\quad K+1 > 0$$
>
> $$5 - K > 0 \implies K < 5$$
> $$K + 1 > 0 \implies K > -1$$
>
> $$-1 < K < 5$$

> **Paso 5:** Ganancia crítica
> $K_{\text{crítica}} = 5$ (sistema marginalmente estable)

# Ejemplo 2: Otro parámetro en el denominador

> [!ejemplo] $G(s) = \frac{1}{s^3 + 2s^2 + 3s + K}$
>
> **Paso 1:** Ecuación característica
> $$1 + \frac{1}{s^3 + 2s^2 + 3s + K} = 0$$
>
> **Paso 2:** Polinomio característico
> $$s^3 + 2s^2 + 3s + K + 1 = 0$$
>
> $$P(s) = s^3 + 2s^2 + 3s + (K+1) = 0$$

> **Paso 3:** Tabla de Routh
> $$
> \begin{array}{c|cc}
> s^3 & 1 & 3 \\
> s^2 & 2 & K+1 \\
> s^1 & \frac{2 \cdot 3 - 1 \cdot (K+1)}{2} = \frac{6 - K - 1}{2} = \frac{5 - K}{2} & 0 \\
> s^0 & K+1 & 
> \end{array}
> $$

> **Paso 4:** Condiciones de estabilidad
> $$2 > 0,\quad \frac{5 - K}{2} > 0,\quad K+1 > 0$$
>
> $$K < 5,\quad K > -1$$
>
> $$-1 < K < 5$$

# Ejemplo 3: Sistema con realimentación no unitaria (parámetro en la realimentación)

> [!ejemplo] $G(s) = \frac{1}{s(s+2)}$, $H(s) = K$ (realimentación con ganancia)
>
> **Paso 1:** Ecuación característica
> $$1 + G(s)H(s) = 1 + \frac{K}{s(s+2)} = 0$$
>
> **Paso 2:** Polinomio característico
> $$s(s+2) + K = 0$$
>
> $$P(s) = s^2 + 2s + K = 0$$

> **Paso 3:** Tabla de Routh
> $$
> \begin{array}{c|cc}
> s^2 & 1 & K \\
> s^1 & 2 & 0 \\
> s^0 & K & 
> \end{array}
> $$

> **Paso 4:** Condiciones de estabilidad
> $$1 > 0,\quad 2 > 0,\quad K > 0$$
>
> $$K > 0$$

# Ganancia crítica

> [!definicion] Ganancia crítica ($K_{\text{crítico}}$)
> Es el valor de $K$ en el límite de la estabilidad, donde el sistema es **marginalmente estable** (polos en el eje imaginario).

> [!info] Obtención desde la tabla
> Para el Ejemplo 1, la ganancia crítica ocurre cuando $\frac{5 - K}{3} = 0 \implies K = 5$.
>
> En este punto, la fila $s^1$ se anula y el polinomio auxiliar se extrae de la fila $s^2$:
> $$Q(s) = 3s^2 + (K+1)\big|_{K=5} = 3s^2 + 6 = 3(s^2 + 2)$$
>
> Los polos en el eje imaginario son $s = \pm j\sqrt{2}$.

# Limitaciones

> [!warning]
> 1. El método asume que el parámetro $K$ aparece de forma que el polinomio característico es lineal en $K$
> 2. Para sistemas con múltiples parámetros, las condiciones se vuelven más complejas
> 3. El método da el rango de estabilidad, **no** el desempeño transitorio
> 4. Ver [[Construccion Tabla]] y [[Casos Especiales]] para la construcción de la tabla