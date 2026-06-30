---
title: Simpson 3/8 y Reglas de Grado Superior
order: 3
tags:
  - metodos-numericos
  - teoria
  - diferenciacion-integracion
  - integracion-numerica
  - newton-cotes
draft: false
aliases:
  - Simpson 3/8
  - Regla de Boole
  - Newton-Cotes de grado superior
  - Simpson 3/8 rule
---

# Simpson 3/8 y Reglas de Grado Superior

> [!definicion]
> La **regla de Simpson 3/8** integra la **cúbica** que pasa por cuatro nodos equiespaciados. Con $h = \frac{b-a}{3}$ y nodos $x_0,\dots,x_3$:
> $$\int_a^b f(x)\,dx \approx \frac{3h}{8}\big(f_0 + 3f_1 + 3f_2 + f_3\big).$$

> [!info]
> Es la regla de [[Reglas Cerradas/index|Newton-Cotes]] de grado $3$. Tiene el mismo orden de error que [[Simpson 1 3 Orden Precision y Error Cuarta Derivada|Simpson 1/3]] ($f^{(4)}$), pero su principal utilidad es **completar** integraciones compuestas con un número de paneles no divisible por $2$.

---

## Error y grado de exactitud

> [!teorema]
> Si $f \in C^4[a,b]$:
> $$\int_a^b f\,dx = \frac{3h}{8}(f_0 + 3f_1 + 3f_2 + f_3) - \frac{3h^5}{80}f^{(4)}(\xi), \qquad h = \frac{b-a}{3}.$$
> Grado de exactitud $3$ (igual que Simpson 1/3), pero con constante de error algo mayor por panel.

> [!info]
> **¿Por qué usarla entonces?** Simpson 1/3 exige número **par** de subintervalos. Si el total es impar, se aplica Simpson 1/3 a la mayoría y **Simpson 3/8 a los últimos 3 paneles**, recuperando un esquema de orden $4$ sobre todo el dominio. Es su rol principal.

---

## Ejemplo: combinación 1/3 + 3/8

> [!ejemplo]
> **Integrar con $n = 5$ subintervalos** (impar, incompatible con Simpson 1/3 solo): se divide en
> - Simpson 1/3 sobre los primeros $2$ paneles $[x_0, x_2]$,
> - Simpson 3/8 sobre los últimos $3$ paneles $[x_2, x_5]$.
>
> $$\int_{x_0}^{x_5} f \approx \frac{h}{3}(f_0 + 4f_1 + f_2) + \frac{3h}{8}(f_2 + 3f_3 + 3f_4 + f_5).$$
>
> Así se integra con orden $O(h^4)$ pese al número impar de paneles.

---

## Reglas de grado superior

> [!info]
> | $n$ | Regla | Error | Grado de exactitud |
> |:---:|:---|:---|:---:|
> | 1 | Trapecio | $-\frac{h^3}{12}f''$ | 1 |
> | 2 | Simpson 1/3 | $-\frac{h^5}{90}f^{(4)}$ | 3 |
> | 3 | Simpson 3/8 | $-\frac{3h^5}{80}f^{(4)}$ | 3 |
> | 4 | Boole | $-\frac{8h^7}{945}f^{(6)}$ | 5 |
>
> La regla de **Boole** ($n=4$) alcanza grado $5$ con error $O(h^7)$. Pero subir más el grado es contraproducente.

---

## El muro del grado alto

> [!warning]
> A partir de $n = 8$, las fórmulas de Newton-Cotes desarrollan **pesos negativos** de magnitud creciente, que amplifican el redondeo y rompen la estabilidad (ver [[Inestabilidad Pesos Negativos Grado Alto]]). Por eso, en la práctica **no** se usan reglas de grado $\geq 5$: para mayor precisión se subdivide ([[Metodos Compuestos/index|compuestas]]) o se cambia a [[Cuadratura Gaussiana/index|cuadratura gaussiana]].

---

## Relación con otras notas

> [!info]
> - La regla hermana de número par de paneles: [[Simpson 1 3 Orden Precision y Error Cuarta Derivada]].
> - La inestabilidad que limita el grado: [[Inestabilidad Pesos Negativos Grado Alto]].
> - La alternativa eficiente: [[Cuadratura Gaussiana/index]].
> - La deducción general de los pesos: [[Formulacion General Pesos Newton Cotes]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Fórmula | $\frac{3h}{8}(f_0+3f_1+3f_2+f_3)$ |
| Error | $-\frac{3h^5}{80}f^{(4)}(\xi)$ |
| Grado de exactitud | 3 |
| Uso principal | completar paneles impares con Simpson 1/3 |
| Grado superior | Boole ($n=4$, $O(h^7)$); $n\geq8$ inestable |

> [!corolario]
> La regla de Simpson 3/8 integra una cúbica por $4$ nodos, $\frac{3h}{8}(f_0+3f_1+3f_2+f_3)$ con error $-\frac{3h^5}{80}f^{(4)}$ y grado de exactitud $3$, igual que Simpson 1/3 pero con constante mayor; su valor real es **completar** integraciones compuestas con número impar de paneles. Reglas de mayor grado como Boole ($O(h^7)$) existen, pero el [[Inestabilidad Pesos Negativos Grado Alto|muro de los pesos negativos]] a partir de $n=8$ las hace inviables: para más precisión se recurre a la subdivisión [[Metodos Compuestos/index|compuesta]] o a la [[Cuadratura Gaussiana/index|cuadratura gaussiana]].
