---
title: Formulación General y Pesos de Newton-Cotes
tags:
  - metodos-numericos
  - teoria
  - diferenciacion-integracion
  - integracion-numerica
  - newton-cotes
draft: false
aliases:
  - Pesos de Newton-Cotes
  - Formulación general de cuadratura
  - Newton-Cotes weights
---

# Formulación General y Pesos de Newton-Cotes

> [!definicion]
> Una **fórmula de cuadratura** aproxima $\int_a^b f(x)\,dx \approx \sum_{i=0}^n w_i f(x_i)$. En **Newton-Cotes**, los nodos son equiespaciados ($x_i = a + ih$, $h = \frac{b-a}{n}$) y los pesos son las integrales de los [[Formulacion Polinomios Cardinales L i x|polinomios cardinales de Lagrange]]:
> $$w_i = \int_a^b L_i(x)\,dx.$$

> [!info]
> La construcción es directa: se interpola $f$ por $p_n$ y se integra $p_n$ en lugar de $f$. Como la integración es lineal, $\int p_n = \sum_i f(x_i)\int L_i = \sum_i w_i f(x_i)$. Los pesos dependen solo de los nodos, no de $f$: se calculan una vez.

---

## Deducción de los pesos

> [!teorema]
> Sea $p_n$ el interpolante de $f$ en $x_0,\dots,x_n$. Entonces
> $$\int_a^b f(x)\,dx \approx \int_a^b p_n(x)\,dx = \int_a^b \sum_{i=0}^n f(x_i)L_i(x)\,dx = \sum_{i=0}^n f(x_i)\underbrace{\int_a^b L_i(x)\,dx}_{w_i}.$$

> [!demostracion]
> Por la forma de Lagrange $p_n(x) = \sum_i f(x_i)L_i(x)$ y la linealidad de la integral, $\int p_n = \sum_i f(x_i)\int L_i$. Definiendo $w_i = \int_a^b L_i$, se obtiene la fórmula. El error de cuadratura es la integral del [[Error Interpolacion Formula Cauchy|error de interpolación]]:
> $$\int_a^b f - \int_a^b p_n = \int_a^b \frac{f^{(n+1)}(\xi_x)}{(n+1)!}\prod_i(x-x_i)\,dx.$$

---

## Pesos de las reglas básicas

> [!info]
> Calculando $w_i = \int L_i$ (forma cerrada en $[a,b]$ con $h = (b-a)/n$):
>
> | $n$ | Regla | Fórmula | Pesos $(w_i)$ |
> |:---:|:---|:---|:---|
> | 1 | [[Trapecio Error Truncamiento Segunda Derivada\|Trapecio]] | $\frac{h}{2}(f_0 + f_1)$ | $\frac{h}{2}(1, 1)$ |
> | 2 | [[Simpson 1 3 Orden Precision y Error Cuarta Derivada\|Simpson 1/3]] | $\frac{h}{3}(f_0 + 4f_1 + f_2)$ | $\frac{h}{3}(1, 4, 1)$ |
> | 3 | [[Simpson 3 8 y Reglas Grado Superior\|Simpson 3/8]] | $\frac{3h}{8}(f_0 + 3f_1 + 3f_2 + f_3)$ | $\frac{3h}{8}(1,3,3,1)$ |
> | 4 | Boole | $\frac{2h}{45}(7f_0 + 32f_1 + 12f_2 + 32f_3 + 7f_4)$ | $\frac{2h}{45}(7,32,12,32,7)$ |

---

## Propiedades estructurales

> [!proposicion]
> 1. **Consistencia (suma de pesos):** $\sum_i w_i = b - a$, pues la regla integra exactamente $f\equiv1$.
> 2. **Simetría:** $w_i = w_{n-i}$ (nodos simétricos respecto al centro).
> 3. **Grado de exactitud:** $n$ si $n$ impar; $n+1$ si $n$ par (Simpson integra cúbicas exactamente pese a usar una parábola).
> 4. **Exactitud polinómica:** la regla integra exactamente todo polinomio de grado $\leq$ su grado de exactitud.

> [!demostracion]
> **Propiedad 1.** Para $f\equiv1$, $p_n\equiv1$ (interpola exactamente), así que $\sum_i w_i\cdot1 = \int_a^b 1\,dx = b-a$. Es la condición mínima de consistencia: una regla que no integre bien las constantes es inútil.

---

## Ejemplo

> [!ejemplo]
> **Pesos de Simpson 1/3 en $[0, 2]$** ($n=2$, $h=1$, nodos $0,1,2$). Calculando $w_1 = \int_0^2 L_1\,dx$ con $L_1(x) = -x(x-2)$:
> $$w_1 = \int_0^2 (-x^2 + 2x)\,dx = \left[-\tfrac{x^3}{3} + x^2\right]_0^2 = -\tfrac{8}{3} + 4 = \tfrac{4}{3} = \tfrac{h}{3}\cdot4.$$
> Análogamente $w_0 = w_2 = \tfrac13 = \tfrac{h}{3}\cdot1$. La fórmula resultante $\frac{h}{3}(f_0+4f_1+f_2)$ coincide con la tabla; $\sum w_i = 2 = b-a$. ✓

---

## Relación con otras notas

> [!info]
> - La base de Lagrange que se integra: [[Formulacion Polinomios Cardinales L i x]].
> - El error como integral del error de interpolación: [[Error Interpolacion Formula Cauchy]].
> - Las reglas concretas: [[Reglas Cerradas/index]].
> - La alternativa con nodos óptimos: [[Determinacion Nodos y Pesos Optimos]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Forma | $\int_a^b f \approx \sum_i w_i f(x_i)$ |
| Pesos | $w_i = \int_a^b L_i(x)\,dx$ |
| Nodos | equiespaciados $x_i = a+ih$ |
| Consistencia | $\sum_i w_i = b-a$ |
| Grado de exactitud | $n$ (impar) o $n+1$ (par) |

> [!corolario]
> Las fórmulas de Newton-Cotes se obtienen integrando el polinomio interpolante: los pesos $w_i = \int L_i$ son las integrales de los polinomios cardinales, calculables una sola vez por ser independientes de $f$. Cumplen $\sum w_i = b-a$ (consistencia), son simétricos, y su grado de exactitud es $n$ o $n+1$ según la paridad —razón por la que Simpson integra cúbicas exactamente—. El error es la integral del [[Error Interpolacion Formula Cauchy|error de interpolación]], lo que conecta cada regla con la derivada correspondiente de $f$ y se concreta en las [[Reglas Cerradas/index|reglas cerradas]].
