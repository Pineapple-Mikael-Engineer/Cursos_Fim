---
title: Condición Necesaria de Estabilidad
tags:
  - control-clasico
  - teoria
  - analisis
  - estabilidad
draft: false
aliases:
  - condicion necesaria
  - coeficientes positivos
  - condicion polinomio
---

# Condición Necesaria de Estabilidad

# Enunciado

> [!teorema] Condición necesaria (pero no suficiente)
> Sea el polinomio característico de un sistema LTI:
> $$P(s) = a_n s^n + a_{n-1} s^{n-1} + \dots + a_1 s + a_0$$
> 
> Si el sistema es **estable**, entonces:
> 1. **Todos los coeficientes** $a_i$ deben tener el **mismo signo** (todos positivos o todos negativos)
> 2. **Ningún coeficiente** puede ser cero (todos $a_i \neq 0$)

> [!warning] Esta condición es necesaria pero NO suficiente
> Que todos los coeficientes sean positivos **no garantiza** que el sistema sea estable.
> 
> Ejemplo: $s^3 + s^2 + 2s + 8 = 0$ tiene todos coeficientes positivos pero es inestable (dos polos complejos con parte real positiva).

# Demostración (caso general)

> [!demostracion] Prueba de la condición necesaria
> 
> **Paso 1:** Polinomio factorizado por polos
> 
> Sea $P(s) = a_n (s - p_1)(s - p_2)\dots(s - p_n)$, donde $p_i$ son los polos del sistema.
> 
> Si el sistema es estable, todos los polos tienen parte real negativa: $\Re(p_i) < 0$.
> 
> **Paso 2:** Factores de polos reales
> 
> Para un polo real negativo: $p_i = -\alpha_i$ con $\alpha_i > 0$.
> 
> El factor es $(s + \alpha_i)$. Todos los coeficientes de este factor son positivos.
> 
> **Paso 3:** Factores de polos complejos conjugados
> 
> Para un par complejo conjugado con parte real negativa: $p = -\sigma \pm j\omega$, $\sigma > 0$.
> 
> El factor es $(s + \sigma - j\omega)(s + \sigma + j\omega) = s^2 + 2\sigma s + (\sigma^2 + \omega^2)$.
> 
> Todos los coeficientes ($1$, $2\sigma$, $\sigma^2+\omega^2$) son positivos.
> 
> **Paso 4:** Producto de factores
> 
> El polinomio $P(s) = a_n \cdot \prod (\text{factores con coeficientes positivos})$.
> 
> El producto de polinomios con coeficientes positivos **no puede** producir coeficientes negativos o cero.
> 
> Por lo tanto, todos los $a_i$ deben tener el mismo signo que $a_n$.

# Demostración para casos particulares

> [!demostracion] Orden 1
> $$P(s) = a_1 s + a_0$$
> 
> Polo: $s = -a_0/a_1$
> 
| Condición | Conclusión |
|-----------|------------|
| $a_0/a_1 > 0$ | Polo negativo → **estable** |
| $a_0/a_1 < 0$ | Polo positivo → **inestable** |
| $a_0 = 0$ | Polo en $s=0$ → marginal |
> 
> Para primer orden, la condición es **necesaria y suficiente**.

> [!demostracion] Orden 2
> $$P(s) = a_2 s^2 + a_1 s + a_0$$
> 
> Polos: $s = \frac{-a_1 \pm \sqrt{a_1^2 - 4a_2a_0}}{2a_2}$
> 
> Para que ambos polos tengan parte real negativa:
> - $a_2, a_1, a_0$ deben tener el **mismo signo** (todos positivos o todos negativos)
> - **No hay condición adicional**
> 
> Para segundo orden, la condición es **necesaria y suficiente**.

> [!demostracion] Orden 3
> $$P(s) = a_3 s^3 + a_2 s^2 + a_1 s + a_0$$
> 
> Condiciones para estabilidad (Routh-Hurwitz):
> - Todos los coeficientes positivos ($a_3, a_2, a_1, a_0 > 0$)
> - **Condición adicional:** $a_2 a_1 > a_3 a_0$
> 
> Ejemplo donde se cumple condición necesaria pero falla la adicional:
> $$s^3 + s^2 + 2s + 8 = 0$$
> - Coeficientes: $1, 1, 2, 8 > 0$ ✓ (condición necesaria cumplida)
> - $a_2 a_1 = 1 \cdot 2 = 2$
> - $a_3 a_0 = 1 \cdot 8 = 8$
> - $2 > 8$? **No** → inestable
> 
> Ver [[Routh Hurwitz/index]] para el criterio completo.

# Contraejemplos famosos

> [!ejemplo] Coeficientes positivos pero inestable (orden 3)
> $$P(s) = s^3 + 2s^2 + s + 2$$
> $$
>\begin{array}{c|cc}
>s^3 & 1 & 1 \\
>s^2 & 2 & 2 \\
>s^1 & \frac{2\cdot1 - 1\cdot2}{2} = 0 & 0 \\
>s^0 & 2 & 
>\end{array}
>$$
> 
> Fila de $s^1$ es cero → caso especial de Routh.
> 
> Polos: $s = \pm j$ (inestable? marginal?) y $s = -2$. Hay un cambio de signo en primera columna tras resolver el caso especial → inestable.
> 
> **Conclusión:** Los coeficientes positivos no garantizan estabilidad.

> [!ejemplo] Coeficiente cero (falta el término $s$)
> $$P(s) = s^3 + 2s^2 + 3$$
> 
> Falta $s^1$ → coeficiente cero → viola condición necesaria.
> 
> Efectivamente, el sistema es inestable o marginal.
> 
> Ver [[Routh Hurwitz/Casos Especiales]] para manejo.

# Condición necesaria para sistemas con parámetros

> [!info] Aplicación en diseño
> Dado un sistema con ganancia $K$ variable, la condición necesaria da un **primer filtro**:
> 
> $$P(s) = s^3 + 3s^2 + 2s + K = 0$$
> 
> Todos los coeficientes deben ser positivos:
> - $1 > 0$ ✓
> - $3 > 0$ ✓
> - $2 > 0$ ✓
> - $K > 0$ (condición necesaria)
> 
> Luego se aplica Routh-Hurwitz para encontrar rango exacto de $K$:
> $$3 \cdot 2 > 1 \cdot K \implies K < 6$$
> 
> Rango de estabilidad: $0 < K < 6$.
> 
> Ver [[Routh Hurwitz/Ajuste Parametros]].

# Limitaciones

> [!warning]
> 1. **No suficiente:** Muchos sistemas con coeficientes positivos son inestables (especialmente orden $\ge 3$)
> 2. **No detecta** estabilidad marginal (coeficientes pueden ser positivos pero sistema oscila)
> 3. **No aplica** a sistemas con retardos ($e^{-sT}$ introduce términos no polinomiales)
> 4. **No da información** sobre el grado de estabilidad