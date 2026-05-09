---
title: Casos Especiales en la Tabla de Routh
tags:
  - control-clasico
  - teoria
  - analisis
  - estabilidad
  - routh-hurwitz
draft: false
aliases:
  - casos especiales routh
  - fila de ceros
  - primer elemento cero
---

# Casos Especiales en la Tabla de Routh

# Introducción

> [!info] Dos problemas típicos
> Durante la construcción de la tabla de Routh pueden ocurrir dos situaciones anómalas:
> 
> | Caso | Descripción | Solución |
> |------|-------------|----------|
> | **Caso 1** | El primer elemento de una fila es **cero** | Reemplazar por $\varepsilon$ (épsilon) |
> | **Caso 2** | Una fila completa es **cero** | Usar polinomio auxiliar |

Ver [[Construccion Tabla]] para el procedimiento base.

---

# Caso 1: Primer elemento de una fila es cero

> [!definicion] Síntoma
> En alguna fila, el primer coeficiente es $0$, pero hay al menos otro coeficiente no nulo en la misma fila.

> [!ejemplo] Polinomio $P(s) = s^5 + 2s^4 + 3s^3 + 6s^2 + 5s + 3$
> 
> **Paso 1:** Construir las dos primeras filas:
> 
> $$
> \begin{array}{c|cccc}
> s^5 & 1 & 3 & 5 \\
> s^4 & 2 & 6 & 3
> \end{array}
> $$
> 
> **Paso 2:** Calcular $s^3$:
> 
> $b_1 = \frac{2 \cdot 3 - 1 \cdot 6}{2} = \frac{6 - 6}{2} = 0$
> 
> $b_2 = \frac{2 \cdot 5 - 1 \cdot 3}{2} = \frac{10 - 3}{2} = \frac{7}{2} = 3.5$
> 
> $b_3 = 0$
> 
> $$
> \begin{array}{c|cccc}
> s^5 & 1 & 3 & 5 \\
> s^4 & 2 & 6 & 3 \\
> s^3 & 0 & 3.5 & 0
> \end{array}
> $$
> 
> El primer elemento de la fila $s^3$ es **cero** (Caso 1).

> [!solucion] Solución: Método del épsilon ($\varepsilon$)
> 
> **Paso 1:** Reemplazar el $0$ por $\varepsilon$:
> 
> $$
> \begin{array}{c|cccc}
> s^5 & 1 & 3 & 5 \\
> s^4 & 2 & 6 & 3 \\
> s^3 & \varepsilon & 3.5 & 0
> \end{array}
> $$
> 
> **Paso 2:** Calcular $s^2$:
> 
> $c_1 = \frac{\varepsilon \cdot 6 - 2 \cdot 3.5}{\varepsilon} = \frac{6\varepsilon - 7}{\varepsilon} = 6 - \frac{7}{\varepsilon}$
> 
> $c_2 = \frac{\varepsilon \cdot 3 - 2 \cdot 0}{\varepsilon} = 3$
> 
> $$
> \begin{array}{c|cccc}
> s^5 & 1 & 3 & 5 \\
> s^4 & 2 & 6 & 3 \\
> s^3 & \varepsilon & 3.5 & 0 \\
> s^2 & 6 - \frac{7}{\varepsilon} & 3 & 0
> \end{array}
> $$
> 
> **Paso 3:** Calcular $s^1$ y $s^0$ (omitido por brevedad).
> 
> **Paso 4:** Analizar signos cuando $\varepsilon \to 0^+$ y $\varepsilon \to 0^-$:
> 
> | Fila | $\varepsilon \to 0^+$ | $\varepsilon \to 0^-$ |
> |------|----------------------|----------------------|
> | $s^5$ | $1 > 0$ | $1 > 0$ |
> | $s^4$ | $2 > 0$ | $2 > 0$ |
> | $s^3$ | $\varepsilon > 0$ | $\varepsilon < 0$ |
> | $s^2$ | $6 - \frac{7}{\varepsilon} \to -\infty$ | $6 - \frac{7}{\varepsilon} \to +\infty$ |
> 
> **Conclusión:** 
> - $\varepsilon > 0$: dos cambios de signo ($2 \to \varepsilon$? en realidad $s^3$ positivo, $s^2$ negativo → un cambio; luego negativo a positivo → otro cambio) → **inestable**
> - $\varepsilon < 0$: también hay cambios → **inestable**
> 
> El sistema es **inestable**.

---

# Caso 2: Fila completa de ceros

> [!definicion] Síntoma
> Toda una fila de la tabla de Routh está compuesta por ceros.

> [!ejemplo] Polinomio $P(s) = s^5 + 2s^4 + 2s^3 + 4s^2 + s + 2$ (ejemplo clásico)
> 
> **Paso 1:** Construir tabla:
> 
> $$
> \begin{array}{c|cccc}
> s^5 & 1 & 2 & 1 \\
> s^4 & 2 & 4 & 2 \\
> s^3 & 0 & 0 & 0
> \end{array}
> $$
> 
> Fila $s^3$ es **completa de ceros** (Caso 2).

> [!solucion] Solución: Polinomio auxiliar
> 
> **Paso 1:** Tomar la fila **inmediatamente superior** a la fila de ceros (fila $s^4$).
> 
> **Paso 2:** Construir el **polinomio auxiliar** $Q(s)$:
> 
> Coeficientes de $s^4$: $2, 4, 2$ corresponden a $s^4, s^2, s^0$:
> 
> $$Q(s) = 2s^4 + 4s^2 + 2 = 2(s^4 + 2s^2 + 1) = 2(s^2 + 1)^2$$
> 
> **Paso 3:** Derivar $Q(s)$:
> 
> $$\frac{dQ(s)}{ds} = 8s^3 + 8s$$
> 
> **Paso 4:** Reemplazar la fila de ceros con los coeficientes de $dQ/ds$ ($8, 8, 0$):
> 
> $$
> \begin{array}{c|cccc}
> s^5 & 1 & 2 & 1 \\
> s^4 & 2 & 4 & 2 \\
> s^3 & 8 & 8 & 0 \\
> s^2 & \frac{8\cdot4 - 2\cdot8}{8} = 2 & \frac{8\cdot2 - 2\cdot0}{8} = 2 & 0 \\
> s^1 & \frac{2\cdot8 - 8\cdot2}{2} = 0 & 0 & \\
> s^0 & \text{(nueva fila de ceros)} & &
> \end{array}
> $$
> 
> **Paso 5:** Aplicar nuevamente el método (fila $s^1$ es cero):
> 
> Polinomio auxiliar desde fila $s^2$: $Q_2(s) = 2s^2 + 2$
> 
> $$\frac{dQ_2(s)}{ds} = 4s$$
> 
> Reemplazar fila $s^1$ con $4, 0$:
> 
> $$
> \begin{array}{c|cccc}
> s^5 & 1 & 2 & 1 \\
> s^4 & 2 & 4 & 2 \\
> s^3 & 8 & 8 & 0 \\
> s^2 & 2 & 2 & 0 \\
> s^1 & 4 & 0 & \\
> s^0 & 2 & &
> \end{array}
> $$
> 
> **Primera columna:** $1, 2, 8, 2, 4, 2$ (todos positivos)
> 
> **Conclusión:** Sin cambios de signo, pero hay raíces en el eje imaginario (de $Q(s)$: $\pm j$ dobles). Como son **múltiples** → **inestable**.

> [!info] Significado de la fila de ceros
> Una fila de ceros indica la presencia de **raíces simétricas** respecto al origen:
> - Pares reales opuestos: $s = \pm a$
> - Pares imaginarios conjugados: $s = \pm j\omega$
> - Cuartetos complejos: $s = \pm a \pm jb$
> 
> Ver [[Polos Ceros]] para más detalles sobre modos naturales.

---

# Demostración

> [!teorema] Demostración del método del épsilon (Caso 1)

> [!demostracion]
> Sea $P(s)$ un polinomio con un coeficiente nulo en la posición que causa el cero en la tabla.
> 
> Considérese la familia perturbada:
> $$P_\varepsilon(s) = P(s) + \varepsilon \cdot R(s)$$
> 
> donde $R(s)$ se elige para que el primer elemento de la fila problemática sea $\varepsilon$.
> 
> Cuando $\varepsilon \to 0$, $P_\varepsilon(s) \to P(s)$.
> 
> El signo de los elementos de la primera columna depende del signo de $\varepsilon$ cuando $\varepsilon$ es pequeño.
> 
> Si los signos de la primera columna son **consistentes** para $\varepsilon > 0$ y $\varepsilon < 0$, el sistema es marginalmente estable.
> 
> Si los signos **cambian** para un signo de $\varepsilon$, entonces $P(s)$ tiene raíces en el eje imaginario que al perturbarse se vuelven inestables.

> [!teorema] Demostración del polinomio auxiliar (Caso 2)

> [!demostracion]
> **Paso 1:** Sea $P(s) = Q(s) \cdot R(s)$, donde $Q(s)$ contiene todos los **factores pares** (simétricos):
> $$Q(s) = (s^2 + \omega_1^2)^{k_1} (s^2 + \omega_2^2)^{k_2} \cdots (s^2 - a_1^2)^{m_1} \cdots$$
> 
> **Paso 2:** En la tabla de Routh, los coeficientes de $Q(s)$ aparecen en la fila superior a la fila de ceros, porque $Q(s)$ es **par** (solo potencias pares).
> 
> **Paso 3:** Derivando $Q(s)$:
> $$\frac{dQ(s)}{ds} = \sum \text{términos donde cada factor $(s^2 + \omega^2)$ se convierte en $2s$}$$
> 
> **Paso 4:** El polinomio $dQ/ds$ es **impar** y no tiene raíces en el eje imaginario (excepto posiblemente $s=0$). Por lo tanto, estabiliza la tabla.
> 
> **Paso 5:** Las raíces de $Q(s)$ determinan la estabilidad:
> - Si todas las raíces de $Q(s)$ son **simples** y están en $\pm j\omega$ o $s=0$ → **marginalmente estable**
> - Si alguna raíz tiene **multiplicidad $\ge 2$** o hay raíces **reales opuestas** → **inestable**

> [!ejemplo] Aplicación de la demostración al ejemplo
> 
> $Q(s) = 2(s^2 + 1)^2$ tiene raíces $\pm j$ con multiplicidad $2$ → **inestable**.

---

# Resumen

> [!info] Caso 1: Primer elemento cero
> 1. Reemplazar $0$ por $\varepsilon$
> 2. Completar tabla
> 3. Analizar signos para $\varepsilon \to 0^+$ y $\varepsilon \to 0^-$
> 4. Si hay cambio de signo → inestable; si no hay cambio → marginal

> [!info] Caso 2: Fila de ceros
> 1. Identificar fila superior
> 2. Construir $Q(s)$
> 3. Derivar $dQ/ds$
> 4. Reemplazar fila de ceros con coeficientes de $dQ/ds$
> 5. Continuar tabla
> 6. Analizar raíces de $Q(s)$ para determinar tipo de estabilidad

# Limitaciones

> [!warning]
> 1. Ver [[Construccion Tabla]] para el procedimiento base
> 2. Ver [[Ajuste Parametros]] para rangos de estabilidad con parámetros
> 3. Ver [[Polos Ceros]] para interpretación de raíces simétricas
> 4. Ver [[Estabilidad/index | estabilidad]] para definiciones de estabilidad marginal