---
title: "Función de Transferencia"
tags:
  - control-clasico
  - modelo-matematico
  - transformada-laplace
  - sistemas-lineales
draft: false
aliases:
  - FT
  - Dominio de Laplace
---

# Función de Transferencia $G(s)$

> [!definicion] Definición Formal
> Sea un sistema [[Sistemas LTI]] (Lineal e Invariante en el Tiempo) con entrada $u(t)$ y salida $y(t)$. Asumiendo **condiciones iniciales nulas** ($y(0^-)=0, \dot{y}(0^-)=0, \dots$), se define:
> $$
> G(s) = \frac{\mathcal{L}\{y(t)\}}{\mathcal{L}\{u(t)\}} = \frac{Y(s)}{U(s)}
> $$
> donde $\mathcal{L}$ es la [[Transformada de Laplace|Transformada Unilateral de Laplace]].

> [!info]
> La definición no impone restricciones sobre la forma de $G(s)$. En general, $G(s)$ puede ser cualquier función compleja de variable compleja. El caso particular de sistemas modelados por ecuaciones diferenciales ordinarias con coeficientes constantes conduce a funciones racionales.

---

## Caso Particular: Sistemas con Parámetros Concentrados

> [!teoria] Sistemas Lumped
> Cuando el sistema físico se modela con parámetros concentrados (masas, resortes, resistencias, capacitancias, inductancias), su comportamiento se rige por una ecuación diferencial ordinaria lineal de coeficientes constantes:
> $$
> a_n \frac{d^n y}{dt^n} + \dots + a_0 y = b_m \frac{d^m u}{dt^m} + \dots + b_0 u
> $$

> [!demostracion] Racionalidad de $G(s)$ para sistemas lumped
> Aplicando la [[Transformada de Laplace]] con condiciones iniciales nulas ($\mathcal{L}\{d^k f/dt^k\} = s^k F(s)$):
> $$
> (a_n s^n + \dots + a_0) Y(s) = (b_m s^m + \dots + b_0) U(s)
> $$
> 
> Despejando $\frac{Y(s)}{U(s)}$:
> $$
> G(s) = \frac{b_m s^m + \dots + b_0}{a_n s^n + \dots + a_0} = \frac{N(s)}{D(s)}
> $$
> 
> **Conclusión para este caso:** $G(s)$ es una **función racional** en la variable compleja $s$. $\square$

> [!definicion] Grado Relativo y Propiedad
> - **Sistema Propio:** $m \le n$. Es físicamente realizable (no hay derivadores puros).
> - **Sistema Estrictamente Propio:** $m < n$. La salida no responde instantáneamente a la entrada.

---

## Contraejemplo: Sistemas con Parámetros Distribuidos

> [!ejemplo] Sistemas Distributed
> Líneas de transmisión, tuberías largas, procesos de difusión. Estos sistemas se rigen por ecuaciones diferenciales parciales. Su función de transferencia **no es racional**:
> 
> **Línea de transmisión sin pérdidas:**
> $$
> G(s) = e^{-s\sqrt{LC} \, d} = e^{-sT}
> $$
> donde $T$ es el tiempo de propagación. Esta función no es racional (es una función trascendente).

> [!ejemplo] Retardo puro
> $$
> G(s) = e^{-s\tau}, \quad \tau > 0
> $$
> Modela transporte, procesamiento digital, actuadores con retardo. No es representable como cociente de polinomios finitos.

---

## Componentes Fundamentales (Caso Racional)

Cuando $G(s)$ es racional (el caso más frecuente en control clásico), su dinámica queda determinada por dos estructuras algebraicas:

| Componente | Definición | Ubicación | Rol Dinámico |
|------------|------------|-----------|---------------|
| **Polos** | Raíces de $D(s)=0$ | [[Polos y Ceros]] | Determinan la estabilidad y la velocidad de respuesta transitoria |
| **Ceros** | Raíces de $N(s)=0$ | [[Polos y Ceros]] | Bloquean o acentúan frecuencias; afectan la sobreoscilación |

Para un análisis detallado de cómo polos y ceros moldean la respuesta temporal, consúltense las notas dedicadas.

---

## Estabilidad y Respuesta Temporal (Caso Racional)

> [!teorema] Condición de Estabilidad BIBO
> Un sistema [[Sistemas LTI]] causal con $G(s)$ racional es estable si y solo si todos sus polos tienen parte real estrictamente negativa:
> $$
> \Re(p_i) < 0, \quad \forall p_i \in \mathcal{P}
> $$
> 
> La justificación completa, incluyendo los casos marginalmente estables e inestables, se desarrolla en [[Estabilidad BIBO]].

> [!info] Aproximación por Polos Dominantes
> En sistemas de orden elevado con $G(s)$ racional, la respuesta transitoria está gobernada por los polos más cercanos al eje imaginario (los de menor parte real en valor absoluto). Estos se denominan **polos dominantes** y permiten reducir el orden del modelo manteniendo la esencia dinámica. Véase [[Polos Dominantes]] para el tratamiento sistemático de esta técnica.