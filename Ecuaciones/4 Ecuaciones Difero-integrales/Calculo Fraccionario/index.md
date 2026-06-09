---
title: Cálculo Fraccionario
tags:
  - ecuaciones
  - difero-integrales
  - teoria
  - calculo-fraccionario
  - index
draft: false
aliases:
  - cálculo fraccionario
  - fractional calculus
  - differintegral
  - derivada fraccionaria
---

# Cálculo Fraccionario

> [!definicion]
> El **cálculo fraccionario** generaliza la derivada y la integral a **orden arbitrario** $q\in
> \mathbb{R}$ (o $\mathbb{C}$): un único operador, el **differintegral** $D^{q}$, tal que $D^{1}$ es la
> derivada, $D^{2}$ la segunda derivada, $D^{-1}$ la integral, $D^{-2}$ la doble integral… y $D^{1/2}$
> una "**media derivada**" que, aplicada dos veces, da la derivada entera.

> [!info]
> Segunda rama del [[4 Ecuaciones Difero-integrales/index| capítulo difero-integral]] y su corazón
> conceptual. Nació de una pregunta de l'Hôpital a Leibniz ("¿y si $n=1/2$?") y de la inversión del
> [[Problema de Abel| problema de Abel]] (que es exactamente una media integración). Hoy modela la
> **difusión anómala** y los materiales con **memoria de ley de potencias**.

---

## La idea: un continuo de órdenes

> [!teoria]
> Iterar la integral $n$ veces tiene una fórmula cerrada (Cauchy):
> $$I^{n}f(x)=\frac{1}{(n-1)!}\int_0^x (x-t)^{n-1}f(t)\,dt.$$
> El paso genial es **reemplazar el factorial por la función Gamma** ($\,(n-1)!=\Gamma(n)$) y permitir
> $n$ **no entero**: así nace la [[Integral de Riemann-Liouville| integral fraccionaria de Riemann-Liouville]] $I^{\alpha}$, y derivando $\lceil\alpha\rceil$ veces, la
> [[Derivada de Riemann-Liouville| derivada fraccionaria]]. Hay **varias definiciones** que coinciden
> para funciones suaves, cada una con su ventaja:
> - **Riemann-Liouville** — la más matemática (deriva *después* de integrar).
> - **[[Derivada de Caputo| Caputo]]** — la **física**: deriva *antes*, de modo que las condiciones
>   iniciales son las habituales $\varphi(0),\varphi'(0),\dots$
> - **Grünwald-Letnikov** — como límite de diferencias finitas; base de los métodos **numéricos**.
>
> La "exponencial" de este mundo es la [[Funcion de Mittag-Leffler| función de Mittag-Leffler]]
> $E_\alpha$: igual que $e^{\lambda t}$ resuelve $\varphi'=\lambda\varphi$, $E_\alpha(\lambda t^\alpha)$
> resuelve la ecuación fraccionaria $D^{\alpha}\varphi=\lambda\varphi$.

> [!info] Recorrido de la sección
> | Nota | Aporte |
> |---|---|
> | [[Operador Differintegral\|Operador Differintegral]] | la idea de orden arbitrario $D^{q}$ |
> | [[Integral de Riemann-Liouville\|Integral de Riemann-Liouville]] | $I^\alpha$ desde la fórmula de Cauchy |
> | [[Derivada de Riemann-Liouville\|Derivada de Riemann-Liouville]] | derivar tras integrar |
> | [[Derivada de Caputo\|Derivada de Caputo]] | la versión con condiciones iniciales físicas |
> | [[Derivada de Grunwald-Letnikov\|Grünwald-Letnikov]] | límite de diferencias; numérico |
> | [[Funcion de Mittag-Leffler\|Función de Mittag-Leffler]] | la exponencial fraccionaria |
> | [[Laplace de Derivadas Fraccionarias\|Laplace Fraccional]] | $\mathcal{L}\{D^\alpha\varphi\}=s^\alpha\Phi-\dots$ |
> | [[Ecuaciones Diferenciales Fraccionarias\|EDF]] | resolverlas con Laplace y Mittag-Leffler |
> | [[Aplicaciones Fraccionarias\|Aplicaciones]] | difusión anómala, viscoelasticidad, memoria |

## Resumen

> [!resumen]
> | Concepto | Contenido |
> |---|---|
> | Differintegral | $D^{q}$, $q\in\mathbb{R}$; interpola derivar/integrar |
> | Integral fraccionaria | $I^\alpha f=\frac{1}{\Gamma(\alpha)}\int_0^x (x-t)^{\alpha-1}f\,dt$ |
> | Derivadas | Riemann-Liouville / Caputo / Grünwald-Letnikov |
> | "Exponencial" | Mittag-Leffler $E_\alpha$ |
> | Aplicación | difusión anómala, memoria de ley de potencias |

> [!corolario]
> El cálculo fraccionario disuelve la frontera entre derivar e integrar: ambos son casos de un único
> operador $D^{q}$ con $q$ deslizándose por la recta real. No es una curiosidad: la memoria de ley de
> potencias de la naturaleza —viscoelasticidad, difusión en medios complejos— se escribe en su lenguaje.

> [!referencia]
> - La idea fundacional: [[Operador Differintegral]] y [[Integral de Riemann-Liouville]].
> - La exponencial del campo: [[Funcion de Mittag-Leffler]].
> - El precursor: [[Problema de Abel]].
