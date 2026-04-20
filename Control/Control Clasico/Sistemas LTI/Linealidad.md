---
title: "Linealidad"
tags:
  - control-clasico
  - sistemas-lineales
  - propiedades
draft: false
aliases:
  - Principio de Superposición
  - Homogeneidad
  - Aditividad
---

# Linealidad

> [!definicion] Definición Formal
> Un sistema [[Sistemas LTI]] es **lineal** si y solo si satisface el **principio de superposición**, que consta de dos propiedades:

---

## 1. Homogeneidad (Escalamiento)

**Homogeneidad:** Si la entrada $u(t)$ produce la salida $y(t)$, entonces una entrada escalada $\alpha u(t)$ produce una salida escalada $\alpha y(t)$ para cualquier constante $\alpha \in \mathbb{C}$:
$$
u(t) \to y(t) \quad \Longrightarrow \quad \alpha u(t) \to \alpha y(t)
$$

**Interpretación:** Multiplicar la entrada por un factor constante multiplica la salida por el mismo factor.

---

## 2. Aditividad (Superposición de entradas)

**Aditividad:** Si $u_1(t) \to y_1(t)$ y $u_2(t) \to y_2(t)$, entonces:
$$
u_1(t) + u_2(t) \to y_1(t) + y_2(t)
$$

**Interpretación:** La respuesta a la suma de dos entradas es la suma de las respuestas individuales.

---

## Propiedad Unificada: Superposición

> [!teorema] Principio de Superposición (Forma completa)
> Combinando homogeneidad y aditividad, para cualquier combinación lineal de entradas:
> $$
> \sum_{i=1}^{n} \alpha_i u_i(t) \quad \longrightarrow \quad \sum_{i=1}^{n} \alpha_i y_i(t)
> $$
> donde $y_i(t)$ es la respuesta a $u_i(t)$.

---

## Consecuencias para la Función de Transferencia

> [!teoria] Base del Análisis en Laplace
> La linealidad es lo que permite trabajar en el dominio de Laplace. Sin ella:
> - No podría definirse la [[Función de Transferencia]] como $G(s) = Y(s)/U(s)$.
> - No sería válido aplicar [[Transformada de Laplace]] para convertir ecuaciones diferenciales en algebraicas.
> - El análisis de [[Sistemas LTI]] colapsaría por completo.

**Relación con Invarianza Temporal:** La linealidad por sí sola no garantiza que un sistema sea manejable con herramientas de Laplace. Se requiere también **invarianza temporal** (ver [[Invarianza Temporal]]). Juntas definen la clase [[Sistemas LTI]].

---

## Ejemplos en Diferentes Contextos

> [!ejemplo] Circuitos Eléctricos
> **Lineal:** Resistor $v(t) = R \cdot i(t)$
> - Homogeneidad: $R \cdot (\alpha i) = \alpha (R i)$
> - Aditividad: $R(i_1+i_2) = R i_1 + R i_2$
> 
> **No lineal:** Diodo $i(t) = I_s (e^{v(t)/V_T} - 1)$
> - $e^{\alpha v}/V_T \neq \alpha e^{v/V_T}$ — viola homogeneidad

> [!ejemplo] Mecánica
> **Lineal:** Resorte ideal $F = k \cdot x$ (Ley de Hooke)
> - El doble de desplazamiento produce el doble de fuerza
> 
> **No lineal:** Péndulo real $\ddot{\theta} + \frac{g}{L} \sin(\theta) = 0$
> - $\sin(\theta) \approx \theta$ solo para ángulos pequeños (linealización)
> - Para $\theta$ grandes, el sistema es no lineal

> [!ejemplo] Procesamiento de Señales
> **Lineal:** Filtro promedio móvil $y[n] = \frac{1}{3}(x[n-1] + x[n] + x[n+1])$
> - La salida escala linealmente con la entrada
> 
> **No lineal:** Mediana móvil $y[n] = \text{mediana}(x[n-1], x[n], x[n+1])$
> - El escalado de la entrada no escala la mediana de forma lineal

> [!ejemplo] Sistemas Térmicos
> **Lineal:** Enfriamiento newtoniano $\dot{T} = -k(T - T_{\text{amb}})$
> - Ecuación diferencial lineal en $T$
> 
> **No lineal:** Radiación térmica $P = \sigma \varepsilon A T^4$ (Ley de Stefan-Boltzmann)
> - La potencia emitida es proporcional a $T^4$, no lineal en la temperatura

> [!ejemplo] Control y Automatización
> **Lineal:** Amplificador operacional en zona lineal $V_{\text{out}} = A \cdot (V_+ - V_-)$
> 
> **No lineal:** Control on-off (termostato, relé)
> $$
> u(t) = \begin{cases} U_{\text{max}} & \text{si } e(t) > 0 \\ U_{\text{min}} & \text{si } e(t) < 0 \end{cases}
> $$
> - No hay relación lineal entre el error $e(t)$ y la acción de control

---

**Limitación de los Sistemas Lineales:** La mayoría de sistemas físicos reales son **no lineales** en algún rango de operación. La práctica común en control clásico es **linealizar** alrededor de un punto de equilibrio mediante expansión en serie de Taylor (primer orden), permitiendo aplicar teoría de [[Sistemas LTI]] localmente.