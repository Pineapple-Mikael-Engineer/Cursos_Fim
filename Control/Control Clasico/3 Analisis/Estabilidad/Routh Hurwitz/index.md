---
title: Criterio de Routh-Hurwitz
tags:
  - control-clasico
  - teoria
  - analisis
  - estabilidad
draft: false
aliases:
  - routh
  - routh-hurwitz
  - criterio de routh
---

# Criterio de Routh-Hurwitz

> [!definicion]
> Método algebraico que cuenta los polos de $P(s)=a_n s^n+\dots+a_0$ con parte real positiva **sin calcularlos**: se construye la tabla de Routh y se cuentan los **cambios de signo** en su primera columna. El sistema es **estable** si y solo si los coeficientes comparten signo **y** toda la primera columna conserva el signo.

> [!info]
> Núcleo de la carpeta `Routh Hurwitz`, dentro de [[index | estabilidad]]. Se apoya en la [[Condicion Necesaria | condición necesaria]] como filtro previo. Detalle operativo en [[Construccion Tabla | construcción de la tabla]], [[Casos Especiales | casos especiales]] y [[Ajuste Parametros | ajuste de parámetros]].

---

## Ejemplo

> [!ejemplo] Tercer orden estable
> $$P(s)=s^3+6s^2+11s+6$$
> Coeficientes $1,6,11,6$ del mismo signo ✓ (pasa la condición necesaria). Tabla:
> $$
> \begin{array}{c|cc}
> s^3 & 1 & 11 \\
> s^2 & 6 & 6 \\
> s^1 & \frac{6\cdot11-1\cdot6}{6}=10 & 0 \\
> s^0 & 6 &
> \end{array}
> $$
> Primera columna $1,6,10,6$: todos positivos, **0 cambios de signo** → **0 polos inestables** → sistema **estable**. (De hecho $P=(s+1)(s+2)(s+3)$.)

> [!ejemplo] Tercer orden inestable que pasa el filtro
> $$P(s)=s^3+s^2+2s+8,\qquad \text{coef. }1,1,2,8>0\ ✓$$
> $$
> \begin{array}{c|cc}
> s^3 & 1 & 2 \\
> s^2 & 1 & 8 \\
> s^1 & \frac{1\cdot2-1\cdot8}{1}=-6 & 0 \\
> s^0 & 8 &
> \end{array}
> $$
> Primera columna $1,1,-6,8$: dos cambios de signo ($1\to-6$ y $-6\to8$) → **2 polos con $\Re>0$** → **inestable**. La condición necesaria no lo detectaba; Routh sí.

---

## En qué consiste

> [!teorema] Estabilidad por Routh-Hurwitz
> El sistema es estable (todos los polos con $\Re(s)<0$) **si y solo si**:
> 1. todos los coeficientes $a_i$ comparten signo, **y**
> 2. todos los elementos de la primera columna de la tabla comparten signo.
>
> El número de **cambios de signo** en la primera columna iguala el número de polos con $\Re(s)>0$.

> [!info] Equivalencia con los determinantes de Hurwitz
> La primera columna codifica los signos de los menores de Hurwitz $\Delta_1=a_{n-1}$, $\Delta_2=\det\begin{bmatrix}a_{n-1}&a_{n-3}\\a_n&a_{n-2}\end{bmatrix},\dots$ El sistema es estable si y solo si todos los $\Delta_i>0$. La tabla los calcula recursivamente sin evaluar determinantes. Demostración completa en [[Construccion Tabla | construcción de la tabla]].

---

## Mapa de la carpeta

> [!info]
> | Subnota | Qué resuelve |
> |---|---|
> | [[Construccion Tabla \| construcción de la tabla]] | algoritmo, fórmula de los elementos, ejemplos completos fila a fila |
> | [[Casos Especiales \| casos especiales]] | primer elemento cero (método $\varepsilon$), fila de ceros (polinomio auxiliar) |
> | [[Ajuste Parametros \| ajuste de parámetros]] | rango de $K$ estable, ganancia crítica y frecuencia de oscilación |
>
> Una **fila de ceros** indica polos simétricos respecto al origen: pares reales $\pm a$, imaginarios $\pm j\omega$ o cuartetos $\pm a\pm jb$.

---

## Limitaciones

> [!warning]
> 1. Solo polinomios de coeficientes **reales**; no maneja retardos $e^{-sT}$ (requieren Padé, Mikhailov o análisis frecuencial).
> 2. No da la **ubicación exacta** de los polos estables, solo cuenta los inestables.
> 3. No distingue por sí solo estabilidad asintótica de marginal (los [[Casos Especiales | casos especiales]] complementan).
> 4. En orden muy alto los cálculos se vuelven tediosos (pero automatizables). En [[Espacio Estados/index | espacio de estados]] conviene usar los autovalores de $\mathbf{A}$.

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Objetivo | contar polos con $\Re>0$ sin factorizar |
> | Entrada | $P(s)=a_n s^n+\dots+a_0$, coef. reales |
> | Criterio | coef. mismo signo **y** 1.ª columna mismo signo |
> | Conteo | #cambios de signo = #polos inestables |
> | Carácter | necesario **y** suficiente |

> [!corolario]
> Routh-Hurwitz convierte la pregunta "¿están todos los polos a la izquierda?" en un conteo de signos sobre una tabla. Es necesario y suficiente, cuenta los polos inestables y, con un parámetro variable, entrega su [[Ajuste Parametros | rango de estabilidad]]; los [[Casos Especiales | casos especiales]] cubren los ceros que rompen el algoritmo.

> [!referencia]
> - Marco de estabilidad: [[index]].
> - Filtro previo: [[Condicion Necesaria]].
> - Tabla paso a paso: [[Construccion Tabla]].
> - Anomalías de la tabla: [[Casos Especiales]].
> - Diseño con parámetro: [[Ajuste Parametros]].
