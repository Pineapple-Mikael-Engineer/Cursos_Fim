---
title: Estabilidad de Sistemas
tags:
  - control-clasico
  - teoria
  - analisis
  - estabilidad
draft: false
aliases:
  - estabilidad
  - estabilidad BIBO
  - estabilidad interna
  - estabilidad asintotica
---

# Estabilidad de Sistemas

# Definiciones fundamentales

> [!definicion] Estabilidad BIBO (Bounded Input Bounded Output)
> Un sistema es **BIBO estable** si toda entrada acotada produce una salida acotada.
> 
> $$|u(t)| \le M_u < \infty \quad \forall t \implies |y(t)| \le M_y < \infty \quad \forall t$$

> [!definicion] Estabilidad asintótica (entrada nula)
> Un sistema es **asintóticamente estable** si, con condiciones iniciales arbitrarias y entrada nula, el estado tiende a cero:
> $$\lim_{t \to \infty} \|x(t)\| = 0$$
> 
> Para sistemas LTI, esto equivale a que todos los polos (autovalores) tengan parte real negativa.

> [!definicion] Estabilidad marginal
> Un sistema es **marginalmente estable** si, con entrada nula, la respuesta permanece acotada pero **no tiende a cero**:
> - Oscilaciones sostenidas (ej. polos en $\pm j\omega$)
> - Respuesta constante (polo en $s=0$ simple)

> [!definicion] Inestabilidad
> Un sistema es **inestable** si existe alguna condición inicial que produce una respuesta **no acotada**.
> 
> Causas típicas:
> - Polos con parte real positiva
> - Polos en el eje imaginario con multiplicidad $\ge 2$

# Clasificación según polos (sistemas LTI)

> [!info] Resumen
> 
> | Ubicación de polos | Estabilidad | Respuesta característica |
> |--------------------|-------------|--------------------------|
> | Todos $\Re(p_i) < 0$ | **Asintóticamente estable** | $e^{\sigma t}$ con $\sigma < 0$ |
> | Polos en $s=0$ simples, resto $\Re < 0$ | **Marginalmente estable** | constante o rampa |
> | Polos en $s=\pm j\omega$ simples, resto $\Re < 0$ | **Marginalmente estable** | $\sin(\omega t)$ |
> | Algún $\Re(p_i) > 0$ | **Inestable** | $e^{\sigma t}$ con $\sigma > 0$ |
> | Polos en eje imaginario con multiplicidad $\ge 2$ | **Inestable** | $t\sin(\omega t)$ o $t$ |
> 
> Ver [[Polos Ceros]] para análisis de modos naturales.

# Relación entre estabilidad BIBO y estabilidad asintótica

> [!teorema] Para sistemas LTI sin cancelaciones polo-cero
> - **Estabilidad asintótica** (todos los polos con $\Re < 0$) $\implies$ **BIBO estable**
> - **BIBO estable** $\implies$ todos los polos con $\Re \le 0$, y los de $\Re = 0$ deben ser simples
> 
> La diferencia es el tratamiento de los polos en el eje imaginario.

> [!ejemplo] Diferencia práctica
> $G(s) = \frac{1}{s^2 + 1}$ (polos $\pm j$):
> - **BIBO estable?** Sí (entrada acotada → salida acotada, ej. $\sin(t)$)
> - **Asintóticamente estable?** No (no tiende a cero, oscila)
> 
> $G(s) = \frac{1}{s(s+1)}$ (polos $0, -1$):
> - **BIBO estable?** No (escalón produce $t$, no acotado)

# Estabilidad interna vs externa

> [!definicion] Estabilidad externa (BIBO)
> Se refiere únicamente a la relación **entrada–salida** del sistema.
> Un sistema es BIBO estable si toda entrada acotada produce una salida acotada.
> 
> Ver [[Funcion Transferencia/index | función transferencia]].

> [!definicion] Estabilidad interna (asintótica)
> Se refiere al comportamiento de **todos los modos del sistema**, incluidos aquellos que pueden no aparecer en la función de transferencia.

> [!warning] Cancelaciones pueden ocultar inestabilidad interna
> Considere un sistema cuya función de transferencia es:
> 
> $$
> G(s) = \frac{s-1}{(s-1)(s+2)}
> $$
> 
> Se observa una cancelación del factor $(s-1)$, lo que deja:
> 
> $$
> G(s) = \frac{1}{s+2}
> $$
> 
> Desde la función de transferencia, el sistema parece BIBO estable (polo en $s=-2$).
> 
> Sin embargo, la cancelación indica que existe un modo interno asociado al polo $s=1$ que no es visible en la relación entrada–salida.
> 
> Ese modo puede crecer sin acotarse internamente, aunque la salida permanezca estable.
> 
> **Conclusión:** la estabilidad BIBO depende de la función de transferencia simplificada, mientras que la estabilidad interna depende de todos los polos del sistema antes de cancelaciones.

# Criterios para determinar estabilidad

> [!info] Herramientas principales
> 
> | Método | Aplica a | Ventaja | Ver |
> |--------|----------|---------|-----|
> | Cálculo directo de polos | Sistemas de orden bajo | Exacto | [[Polos Ceros]] |
> | Routh-Hurwitz | Sistemas de cualquier orden | No requiere factorizar | [[Routh Hurwitz/index]] |
> | Lugar de las raíces | Sistemas con un parámetro variable | Muestra tendencia | [[Lugar Raices/index]] |
> | Diagrama de Nyquist | Sistemas con realimentación | Da márgenes | [[Nyquist]] |
> | Autovalores de A | Espacio de estados | Da estabilidad interna | [[Espacio Estados/index]] |

# Condición necesaria de estabilidad

> [!teorema] Condición necesaria (pero no suficiente)
> Para que un sistema sea estable, **todos los coeficientes** del polinomio característico deben tener el **mismo signo** y **ninguno puede ser cero**.
> 
> Ver [[Condicion Necesaria]] para:
> - Demostración
> - Contraejemplos (coeficientes positivos pero inestable)
> - Sistemas de orden 1, 2 y 3

# Estabilidad y especificaciones de diseño

> [!info] Diseño de controladores
> 1. **Estabilización:** Llevar polos inestables al semiplano izquierdo
> 2. **Margen de estabilidad:** Asegurar que los polos no estén demasiado cerca del eje imaginario (ver [[Diseno/Lead | lead]], [[Diseno/Lag | lag]])
> 3. **Robustez:** Mantener estabilidad ante variaciones paramétricas (ver [[Lugar Raices/index | lugar de las raíces]])

# Ejemplos prácticos

> [!ejemplo] Sistema inestable clásico
> Péndulo invertido:
> $$G(s) = \frac{1}{s^2 - \frac{g}{l}}$$
> 
> Polos: $s = \pm \sqrt{g/l}$. Un polo positivo → inestable.

> [!ejemplo] Sistema marginalmente estable
> Oscilador armónico sin amortiguamiento:
> $$G(s) = \frac{1}{s^2 + \omega_0^2}$$
> 
> Polos: $s = \pm j\omega_0$ → oscilación sostenida.

# Limitaciones

> [!warning]
> 1. El análisis por polos **no aplica** a sistemas no lineales o variantes en el tiempo
> 2. La condición necesaria (coeficientes positivos) es débil: muchos sistemas la cumplen y son inestables
> 3. Routh-Hurwitz no maneja retardos de tiempo ($e^{-sT}$) directamente
> 4. La estabilidad BIBO puede ser engañosa si hay cancelaciones