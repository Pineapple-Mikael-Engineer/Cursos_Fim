---
title: Inestabilidad de Pesos Negativos en Grado Alto
tags:
  - metodos-numericos
  - teoria
  - diferenciacion-integracion
  - integracion-numerica
  - newton-cotes
  - error-numerico
draft: false
aliases:
  - Pesos negativos
  - Inestabilidad de Newton-Cotes
  - Runge en cuadratura
---

# Inestabilidad de Pesos Negativos en Grado Alto

> [!definicion]
> A partir de $n = 8$, las fórmulas de [[Integracion Numerica Newton Cotes/index|Newton-Cotes]] desarrollan **pesos negativos** de magnitud creciente. Esto destruye su estabilidad: los errores de redondeo en las evaluaciones de $f$ se amplifican en vez de promediarse, y la regla deja de converger.

> [!info]
> Es la manifestación, en cuadratura, del [[Fenomeno Runge y Nodos Chebyshev|fenómeno de Runge]]: el polinomio interpolante de grado alto sobre nodos equiespaciados oscila, y al integrarlo aparecen pesos de signos alternados. La cura es la misma: no subir el grado, sino subdividir ([[Metodos Compuestos/index|compuestas]]) o usar nodos óptimos ([[Cuadratura Gaussiana/index|Gauss]]).

---

## Aparición de los pesos negativos

> [!teorema]
> Los pesos de Newton-Cotes $w_i = \int L_i$ son todos positivos para $n \leq 7$. Para $n \geq 8$ (cerradas), algunos $w_i < 0$, y
> $$\sum_i |w_i| \to \infty \quad (n\to\infty),$$
> mientras que $\sum_i w_i = b-a$ permanece fijo. La suma de **valores absolutos** diverge, lo que mide la amplificación del error.

> [!info]
> **Estabilidad y condicionamiento.** El error de redondeo de una regla de cuadratura se acota por $u\sum_i|w_i|\max|f|$. Si todos los pesos son positivos, $\sum|w_i| = \sum w_i = b-a$ (acotado, estable). Con pesos negativos, $\sum|w_i| \gg b-a$ crece sin límite: la regla amplifica el ruido.

---

## Ejemplo: pesos de Newton-Cotes

> [!ejemplo]
> **Pesos normalizados** (factor común extraído) por grado:
>
> | $n$ | Pesos | ¿Negativos? |
> |:---:|:---|:---:|
> | 2 (Simpson 1/3) | $(1, 4, 1)$ | no |
> | 4 (Boole) | $(7, 32, 12, 32, 7)$ | no |
> | 7 | $(751, 3577, 1323, 2989, 2989, 1323, 3577, 751)$ | no |
> | 8 | $(989, 5888, -928, 10496, -4540, 10496, -928, 5888, 989)$ | **sí** |
> | 10 | magnitudes crecientes, signos alternados | sí |
>
> En $n=8$ aparecen los primeros pesos negativos ($-928, -4540$); para $n$ mayor, su magnitud explota.

---

## Consecuencia práctica

> [!warning]
> **No usar Newton-Cotes de grado $\geq 8$.** Aunque el grado de exactitud crece, la inestabilidad numérica arruina el resultado: para integrandos con cualquier ruido (o en aritmética finita), el error de redondeo domina. Es inútil aumentar el grado para ganar precisión.

> [!teoria]
> **El paralelo con Runge.** La integral de un interpolante de grado alto en nodos equiespaciados hereda las oscilaciones de [[Fenomeno Runge y Nodos Chebyshev|Runge]]. Los pesos negativos son la firma de esas oscilaciones: regiones donde el interpolante va por debajo de cero contribuyen "área negativa". Con nodos de Chebyshev (cuadratura de Clenshaw-Curtis) los pesos permanecen positivos.

---

## Soluciones

> [!info]
> | Estrategia | Idea |
> |:---|:---|
> | [[Metodos Compuestos/index\|Compuestas]] | grado bajo + muchos paneles; pesos siempre positivos |
> | [[Cuadratura Gaussiana/index\|Gauss-Legendre]] | nodos óptimos; pesos **siempre positivos**, grado $2n-1$ |
> | Clenshaw-Curtis | nodos de Chebyshev; pesos positivos |
> | Adaptativas | subdividir donde el integrando lo exige |
>
> Todas evitan el problema manteniendo pesos positivos: estabilidad garantizada.

---

## Relación con otras notas

> [!info]
> - El fenómeno de interpolación subyacente: [[Fenomeno Runge y Nodos Chebyshev]].
> - La estrategia correcta de subdivisión: [[Metodos Compuestos/index]].
> - La cuadratura con pesos siempre positivos: [[Determinacion Nodos y Pesos Optimos]].
> - La amplificación de redondeo en general: [[Propagacion Errores Operaciones Matriciales]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Umbral | $n \geq 8$ (cerradas) |
| Síntoma | pesos $w_i < 0$ |
| Medida | $\sum|w_i| \to \infty$ |
| Causa | oscilación tipo Runge del interpolante |
| Solución | compuestas, Gauss, Clenshaw-Curtis |

> [!corolario]
> A partir de $n=8$, Newton-Cotes desarrolla pesos negativos cuya suma de valores absolutos diverge, amplificando el error de redondeo y destruyendo la estabilidad: es el [[Fenomeno Runge y Nodos Chebyshev|fenómeno de Runge]] trasladado a la cuadratura. Por eso no se usan reglas de grado alto; la precisión se obtiene subdividiendo en [[Metodos Compuestos/index|reglas compuestas]] de grado bajo —que conservan pesos positivos— o con [[Cuadratura Gaussiana/index|cuadratura gaussiana]], cuyos pesos son siempre positivos y cuyo grado de exactitud $2n-1$ supera con creces lo que Newton-Cotes podría ofrecer establemente.
