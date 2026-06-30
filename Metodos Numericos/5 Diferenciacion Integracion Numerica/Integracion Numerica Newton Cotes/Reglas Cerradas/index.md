---
title: Reglas Cerradas de Newton-Cotes
order: 2
tags:
  - metodos-numericos
  - teoria
  - diferenciacion-integracion
  - integracion-numerica
  - newton-cotes
  - index
draft: false
aliases:
  - Reglas cerradas
  - Closed Newton-Cotes
  - Trapecio y Simpson
---

# Reglas Cerradas de Newton-Cotes

> [!definicion]
> Las **reglas cerradas** de [[Integracion Numerica Newton Cotes/index|Newton-Cotes]] son las fórmulas de cuadratura cuyos nodos **incluyen los extremos** $a$ y $b$ del intervalo. Las de uso común son trapecio ($n=1$), Simpson 1/3 ($n=2$) y Simpson 3/8 ($n=3$).

> [!info]
> "Cerradas" porque evalúan $f$ en los bordes (frente a las abiertas, que no). Son las fórmulas estándar de integración; cada una integra el [[Formulacion General Pesos Newton Cotes|interpolante]] de su grado, con un error ligado a una derivada de $f$.

---

## Las reglas y su error

> [!info]
> | Regla | Fórmula | Error | Grado de exactitud |
> |:---|:---|:---|:---:|
> | [[Trapecio Error Truncamiento Segunda Derivada\|Trapecio]] | $\frac{h}{2}(f_0+f_1)$ | $-\frac{h^3}{12}f''(\xi)$ | 1 |
> | [[Simpson 1 3 Orden Precision y Error Cuarta Derivada\|Simpson 1/3]] | $\frac{h}{3}(f_0+4f_1+f_2)$ | $-\frac{h^5}{90}f^{(4)}(\xi)$ | 3 |
> | [[Simpson 3 8 y Reglas Grado Superior\|Simpson 3/8]] | $\frac{3h}{8}(f_0+3f_1+3f_2+f_3)$ | $-\frac{3h^5}{80}f^{(4)}(\xi)$ | 3 |

## El límite del grado alto

> [!warning]
> Subir el grado de Newton-Cotes **no** es viable: a partir de $n=8$ aparecen [[Inestabilidad Pesos Negativos Grado Alto|pesos negativos]] que amplifican el error de redondeo y rompen la estabilidad. Es el análogo en cuadratura del [[Fenomeno Runge y Nodos Chebyshev|fenómeno de Runge]]. La solución es subdividir ([[Metodos Compuestos/index|métodos compuestos]]), no subir el grado.

---

## Ejemplo

> [!ejemplo]
> **$\int_0^1 e^x\,dx = e-1 \approx 1.71828$.**
>
> | Regla | Aproximación | Error |
> |:---|:---:|:---:|
> | Trapecio | 1.85914 | $1.4\times10^{-1}$ |
> | Simpson 1/3 | 1.71886 | $5.8\times10^{-4}$ |
> | Simpson 3/8 | 1.71854 | $2.6\times10^{-4}$ |
>
> Simpson supera al trapecio por dos órdenes de magnitud (orden $h^5$ vs $h^3$ por panel) gracias a su mayor grado de exactitud.

---

## La sorpresa de Simpson

> [!teoria]
> Simpson 1/3 usa una **parábola** (grado 2) pero integra exactamente **cúbicas** (grado 3): tiene grado de exactitud $3$, no $2$. La razón es la simetría de los nodos, que cancela el término de error de orden $h^4$. Este "bonus de paridad" es lo que hace a Simpson tan eficiente para su costo.

---

## Resumen

| Regla | Nota |
|:---|:---|
| Trapecio | [[Trapecio Error Truncamiento Segunda Derivada]] |
| Simpson 1/3 | [[Simpson 1 3 Orden Precision y Error Cuarta Derivada]] |
| Simpson 3/8 y grado superior | [[Simpson 3 8 y Reglas Grado Superior]] |
| Inestabilidad de grado alto | [[Inestabilidad Pesos Negativos Grado Alto]] |

> [!corolario]
> Las reglas cerradas de Newton-Cotes —trapecio, Simpson 1/3, Simpson 3/8— integran el interpolante de su grado evaluando en los extremos, con errores $-\frac{h^3}{12}f''$, $-\frac{h^5}{90}f^{(4)}$ y $-\frac{3h^5}{80}f^{(4)}$ respectivamente. Simpson aventaja al trapecio por su grado de exactitud $3$ (integra cúbicas pese a usar parábolas, por simetría). Subir el grado más allá de $n=8$ introduce [[Inestabilidad Pesos Negativos Grado Alto|pesos negativos]] inestables, por lo que la estrategia correcta es la subdivisión de los [[Metodos Compuestos/index|métodos compuestos]].
