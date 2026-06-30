---
title: Regiones de Estabilidad Absoluta y A-Estabilidad
order: 5
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - valor-inicial
  - estabilidad
draft: false
aliases:
  - Estabilidad absoluta
  - Región de estabilidad
  - A-estabilidad
  - Absolute stability
---

# Regiones de Estabilidad Absoluta y A-Estabilidad

> [!definicion]
> La **región de estabilidad absoluta** de un método es el conjunto de valores $z = h\lambda$ (en el plano complejo) para los cuales la solución numérica de la **ecuación de prueba** $y' = \lambda y$ permanece **acotada**:
> $$y_{n+1} = R(z)\,y_n, \qquad \text{región} = \{z\in\mathbb{C} : |R(z)| \leq 1\},$$
> donde $R(z)$ es el **factor de amplificación** del método.

> [!info]
> La estabilidad absoluta determina el **paso máximo seguro**: para que la simulación no explote, $h\lambda$ debe caer dentro de la región. Es independiente de la precisión —un método puede ser preciso pero inestable si $h$ es grande—. Es la propiedad clave para entender la [[Rigidez Stiffness Problemas Ingenieria|rigidez]].

---

## La ecuación de prueba y el factor de amplificación

> [!teorema]
> Aplicando cada método a $y'=\lambda y$ se obtiene $y_{n+1} = R(z)y_n$ con $z=h\lambda$:
>
> | Método | $R(z)$ | Región de estabilidad |
> |:---|:---|:---|
> | [[Euler Explicito Orden 1 Interpretacion Geometrica\|Euler explícito]] | $1 + z$ | disco $|1+z|\leq1$ (centro $-1$, radio 1) |
> | [[Euler Implicito Estabilidad Incondicional\|Euler implícito]] | $\dfrac{1}{1-z}$ | exterior del disco $|1-z|\geq1$ (todo $\operatorname{Re}z<0$) |
> | Trapezoidal (Crank-Nicolson) | $\dfrac{1+z/2}{1-z/2}$ | todo el semiplano $\operatorname{Re}z\leq0$ |
> | [[RK4 Clasico Tabla Butcher y Orden Cuatro\|RK4]] | $1+z+\tfrac{z^2}{2}+\tfrac{z^3}{6}+\tfrac{z^4}{24}$ | región acotada (llega a $z\approx-2.78$ en el eje real) |

> [!info]
> Para $y'=\lambda y$ con $\operatorname{Re}(\lambda)<0$ (decaimiento físico), la solución exacta decae. El método es estable si $|R(z)|\leq1$: replica el decaimiento sin explotar. Los métodos explícitos tienen regiones **acotadas**, limitando $h$; los implícitos pueden cubrir todo el semiplano.

---

## A-estabilidad

> [!definicion]
> Un método es **A-estable** si su región de estabilidad contiene **todo** el semiplano izquierdo $\{z : \operatorname{Re}(z) \leq 0\}$. Entonces es estable para **cualquier** $h>0$ en problemas disipativos.

> [!teorema]
> **Barrera de Dahlquist.** Ningún método explícito es A-estable, y ningún método lineal multipaso A-estable tiene orden $>2$. La A-estabilidad de orden alto exige métodos **implícitos** (RK implícitos de Gauss, BDF).

> [!info]
> [[Euler Implicito Estabilidad Incondicional|Euler implícito]] y el trapezoidal son A-estables; ambos implícitos. Esta barrera explica por qué los problemas [[Rigidez Stiffness Problemas Ingenieria|rígidos]] **obligan** a métodos implícitos: no hay alternativa explícita estable con paso grande.

---

## Ejemplo: el límite de paso de RK4

> [!ejemplo]
> **$y' = -100y$ (decaimiento rápido, $\lambda=-100$).** RK4 es estable solo si $z=h\lambda$ está en su región, que en el eje real negativo llega hasta $z\approx-2.78$:
> $$|h\lambda| \leq 2.78 \;\Rightarrow\; h \leq \frac{2.78}{100} = 0.0278.$$
>
> | $h$ | $z=h\lambda$ | ¿estable? |
> |:---:|:---:|:---:|
> | 0.02 | $-2.0$ | sí |
> | 0.0278 | $-2.78$ | límite |
> | 0.04 | $-4.0$ | **no (explota)** |
>
> Aunque la solución $e^{-100t}$ es trivial (decae a 0 al instante), RK4 explota si $h>0.0278$: la **estabilidad**, no la precisión, fija el paso. Con [[Euler Implicito Estabilidad Incondicional|Euler implícito]] cualquier $h$ sirve.

---

## Estabilidad vs precisión

> [!warning]
> Son propiedades **distintas**:
> - **Precisión** (orden): cuán fielmente se aproxima la solución para $h$ pequeño.
> - **Estabilidad**: para qué $h$ la solución numérica no explota.
>
> Un método de alto orden con región pequeña (RK4) puede ser inútil en problemas rígidos pese a su precisión. Un método de orden 1 A-estable (Euler implícito) los resuelve. **Para rigidez, la estabilidad domina.**

---

## Relación con otras notas

> [!info]
> - El método explícito de región mínima: [[Euler Explicito Orden 1 Interpretacion Geometrica]].
> - El A-estable de referencia: [[Euler Implicito Estabilidad Incondicional]].
> - El problema donde esto es decisivo: [[Rigidez Stiffness Problemas Ingenieria]].
> - El teorema que une estabilidad y convergencia: [[Consistencia Estabilidad Convergencia Lax]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Ecuación de prueba | $y'=\lambda y$, $z=h\lambda$ |
| Factor | $y_{n+1}=R(z)y_n$ |
| Región | $\{z : |R(z)|\leq1\}$ |
| Euler explícito | disco radio 1 |
| RK4 | región acotada ($z\gtrsim-2.78$) |
| A-estable | semiplano izq. completo (solo implícitos) |
| Barrera de Dahlquist | no hay explícitos A-estables |

> [!corolario]
> La región de estabilidad absoluta —los $z=h\lambda$ con $|R(z)|\leq1$— fija el paso máximo seguro de cada método, independientemente de su precisión. Los métodos explícitos tienen regiones acotadas (RK4 hasta $z\approx-2.78$), limitando $h$; la A-estabilidad, que cubre todo el semiplano izquierdo, solo la alcanzan los implícitos ([[Euler Implicito Estabilidad Incondicional|Euler implícito]], trapezoidal), como impone la barrera de Dahlquist. Esta distinción entre estabilidad y precisión es la clave para entender por qué los problemas [[Rigidez Stiffness Problemas Ingenieria|rígidos]] exigen métodos implícitos, y es un ingrediente del [[Consistencia Estabilidad Convergencia Lax|teorema de convergencia de Lax]].
