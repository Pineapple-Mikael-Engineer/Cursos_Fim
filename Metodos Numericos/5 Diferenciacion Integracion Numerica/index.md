---
title: Diferenciación e Integración Numérica
tags:
  - metodos-numericos
  - teoria
  - diferenciacion-integracion
  - index
draft: false
aliases:
  - Diferenciación e integración numérica
  - Cuadratura
  - Numerical calculus
---

# Diferenciación e Integración Numérica

> [!definicion]
> La **diferenciación** y la **integración numérica** aproximan derivadas $f'(x)$ e integrales $\int_a^b f(x)\,dx$ a partir de evaluaciones de $f$ en puntos discretos, cuando no se dispone de fórmula analítica o $f$ solo se conoce por una tabla de datos.

> [!info]
> Ambas se construyen sobre la [[Interpolacion Polinomica/index|interpolación]]: se reemplaza $f$ por un polinomio interpolante y se deriva o integra este. La diferencia de comportamiento es radical: la **integración numérica es estable** (promedia errores), mientras que la **diferenciación numérica es inestable** (amplifica el ruido).

---

## Diferenciación numérica

> [!info]
> Aproxima derivadas por [[Aproximacion Diferencias Finitas Serie Taylor|diferencias finitas]] derivadas de la serie de Taylor, con [[Orden Error Progresiva Regresiva Centrada|distinto orden]] según el esquema, aceleradas por [[Extrapolacion Richardson Aceleracion Convergencia|extrapolación de Richardson]]. Su talón de Aquiles es la [[Inestabilidad Error Redondeo Paso h|inestabilidad respecto al paso $h$]]. Se estudia en [[Diferenciacion Numerica/index]].

## Integración por Newton-Cotes

> [!info]
> Integra el polinomio interpolante en nodos **equiespaciados**, dando los pesos de [[Integracion Numerica Newton Cotes/index|Newton-Cotes]] (trapecio, Simpson). Las versiones compuestas son las de uso práctico. Se estudia en [[Integracion Numerica Newton Cotes/index]].

## Cuadratura gaussiana

> [!info]
> Elige **nodos y pesos óptimos** (no equiespaciados) para maximizar el grado de exactitud: con $n$ nodos integra exactamente polinomios de grado $2n-1$. Se estudia en [[Cuadratura Gaussiana/index]].

---

## Ejemplo

> [!ejemplo]
> **Aproximar $\int_0^1 e^x\,dx = e - 1 \approx 1.71828$** con distintos métodos (mismo número de evaluaciones $\sim 3$):
>
> | Método | Aproximación | Error |
> |:---|:---:|:---:|
> | Trapecio simple | 1.85914 | $1.4\times10^{-1}$ |
> | Simpson 1/3 | 1.71886 | $5.8\times10^{-4}$ |
> | Gauss-Legendre (2 nodos) | 1.71832 | $4.0\times10^{-5}$ |
>
> Con el mismo coste, Gauss supera a Newton-Cotes por su elección óptima de nodos. La estabilidad de la integración contrasta con la fragilidad de la derivación.

---

## Integrar es estable, derivar no

> [!warning]
> | | Integración | Diferenciación |
> |:---|:---|:---|
> | Efecto sobre el error | promedia (suaviza) | amplifica (ruido $\times 1/h$) |
> | Paso $h \to 0$ | mejora hasta precisión de máquina | mejora y luego **empeora** |
> | Condicionamiento | bien condicionada | mal condicionada |
>
> La integración acumula contribuciones con signo coherente; la diferenciación resta cantidades casi iguales ([[Perdida Significancia y Cancelacion Catastrofica|cancelación]]).

---

## Resumen

| Familia | Subdirectorio |
|:---|:---|
| Diferenciación numérica | [[Diferenciacion Numerica/index]] |
| Integración de Newton-Cotes | [[Integracion Numerica Newton Cotes/index]] |
| Cuadratura gaussiana | [[Cuadratura Gaussiana/index]] |

> [!corolario]
> La diferenciación e integración numéricas se obtienen derivando o integrando un [[Interpolacion Polinomica/index|polinomio interpolante]], pero su carácter difiere por completo: la integración es estable y converge hasta precisión de máquina, mientras que la [[Diferenciacion Numerica/index|diferenciación]] amplifica el ruido y se degrada al reducir $h$. En integración, [[Integracion Numerica Newton Cotes/index|Newton-Cotes]] usa nodos equiespaciados y la [[Cuadratura Gaussiana/index|cuadratura gaussiana]] nodos óptimos que duplican el grado de exactitud. Estas técnicas alimentan la resolución de [[6 Ecuaciones Diferenciales Ordinarias/index|ecuaciones diferenciales]].
