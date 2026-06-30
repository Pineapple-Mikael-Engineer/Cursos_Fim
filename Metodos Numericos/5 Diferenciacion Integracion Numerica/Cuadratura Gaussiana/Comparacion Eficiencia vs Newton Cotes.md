---
title: Comparación de Eficiencia frente a Newton-Cotes
order: 4
tags:
  - metodos-numericos
  - teoria
  - diferenciacion-integracion
  - cuadratura-gaussiana
draft: false
aliases:
  - Gauss vs Newton-Cotes
  - Eficiencia de cuadratura
  - Quadrature efficiency
---

# Comparación de Eficiencia frente a Newton-Cotes

> [!definicion]
> La **eficiencia** de una regla de cuadratura se mide por la precisión alcanzada en función del número de evaluaciones de $f$. La [[Cuadratura Gaussiana/index|cuadratura gaussiana]] es la más eficiente para integrandos suaves: con $n$ evaluaciones alcanza [[Grado Exactitud Polinomica 2n 1|grado de exactitud $2n-1$]], frente al $\sim n$ de [[Integracion Numerica Newton Cotes/index|Newton-Cotes]].

> [!info]
> A igualdad de evaluaciones, Gauss integra exactamente polinomios del **doble** de grado. Esto se traduce en errores mucho menores y convergencia más rápida, a cambio de nodos no equiespaciados y no reutilizables al cambiar $n$.

---

## Comparación de grado de exactitud

> [!info]
> | Evaluaciones | Newton-Cotes (grado exacto) | Gauss (grado exacto) |
> |:---:|:---:|:---:|
> | 2 | 1 (trapecio) | 3 |
> | 3 | 3 (Simpson) | 5 |
> | 4 | 3 (Simpson 3/8) | 7 |
> | 5 | 5 (Boole) | 9 |
> | $n$ | $\sim n$ | $2n-1$ |
>
> Gauss duplica el grado. Además sus [[Determinacion Nodos y Pesos Optimos|pesos son siempre positivos]], evitando la [[Inestabilidad Pesos Negativos Grado Alto|inestabilidad]] de Newton-Cotes de grado alto.

---

## Ejemplo numérico

> [!ejemplo]
> **$\int_0^1 e^x\,dx = e-1 \approx 1.7182818$**, error según número de evaluaciones:
>
> | Evaluaciones | Simpson compuesto | Gauss-Legendre |
> |:---:|:---:|:---:|
> | 2 | — | $4.0\times10^{-5}$ |
> | 3 | $5.8\times10^{-4}$ | $2.9\times10^{-7}$ |
> | 5 | $3.7\times10^{-5}$ | $5\times10^{-12}$ |
>
> Con 5 evaluaciones, Gauss da $\sim11$ dígitos correctos frente a $\sim4$ de Simpson: su elección óptima de nodos rinde mucho más por evaluación.

---

## Ventajas y limitaciones de Gauss

> [!info]
> **Ventajas.**
> - Máxima precisión por evaluación (grado $2n-1$).
> - Pesos positivos: estabilidad garantizada.
> - Convergencia espectral para integrandos analíticos.
> - Evita evaluar en los extremos (útil si $f$ tiene singularidad en bordes).

> [!warning]
> **Limitaciones.**
> - **No anidada:** cambiar $n$ recalcula *todos* los nodos; no se reutilizan evaluaciones (a diferencia del [[Trapecio Compuesto Convergencia O h2|trapecio]] o de Romberg). Las reglas de **Gauss-Kronrod** resuelven esto añadiendo nodos.
> - **Nodos irracionales:** requieren tablas o cálculo previo ([[Determinacion Nodos y Pesos Optimos|Golub-Welsch]]).
> - **Datos tabulados:** inútil si $f$ solo se conoce en puntos equiespaciados (no se puede evaluar en los nodos de Gauss).

---

## Cuándo usar cada método

> [!info]
> | Situación | Método |
> |:---|:---|
> | $f$ evaluable donde se quiera, suave | **Gauss-Legendre** |
> | Datos tabulados equiespaciados | [[Simpson Compuesto Convergencia O h4\|Simpson compuesto]] |
> | Control de error adaptativo | Gauss-Kronrod (`scipy.integrate.quad`) |
> | Refinamiento sucesivo barato | [[Extrapolacion Richardson Aceleracion Convergencia\|Romberg]] |
> | Integrando periódico | [[Trapecio Compuesto Convergencia O h2\|trapecio]] (espectral) |

> [!teoria]
> Las rutinas de integración de producción (`scipy.integrate.quad`) usan **Gauss-Kronrod adaptativo**: una regla de Gauss más nodos de Kronrod que permiten estimar el error sin recalcular, subdividiendo donde el integrando lo exige. Combina la eficiencia de Gauss con un control de error robusto.

---

## Relación con otras notas

> [!info]
> - El grado que da la ventaja: [[Grado Exactitud Polinomica 2n 1]].
> - La estabilidad de los pesos: [[Determinacion Nodos y Pesos Optimos]].
> - La alternativa para datos tabulados: [[Simpson Compuesto Convergencia O h4]].
> - El traslado a intervalos generales: [[Cambio Variable Intervalo General]].

---

## Resumen

| Aspecto | Newton-Cotes | Gauss |
|:---|:---|:---|
| Grado con $n$ nodos | $\sim n$ | $2n-1$ |
| Nodos | equiespaciados | óptimos |
| Pesos | pueden ser negativos | positivos |
| Anidada | sí (trapecio/Romberg) | no (salvo Kronrod) |
| Datos tabulados | sí | no |

> [!corolario]
> La cuadratura gaussiana es la más eficiente para integrandos suaves: con $n$ evaluaciones alcanza grado de exactitud $2n-1$, el doble de [[Integracion Numerica Newton Cotes/index|Newton-Cotes]], con pesos positivos y convergencia espectral. Su precio es no ser anidada —cambiar $n$ recalcula todo— y no servir para datos equiespaciados tabulados, donde [[Simpson Compuesto Convergencia O h4|Simpson compuesto]] sigue siendo la opción. Las reglas adaptativas de Gauss-Kronrod combinan la eficiencia gaussiana con control de error, y son el motor de las rutinas de integración modernas. El uso en intervalos arbitrarios requiere el [[Cambio Variable Intervalo General|cambio de variable]] al intervalo de referencia.
