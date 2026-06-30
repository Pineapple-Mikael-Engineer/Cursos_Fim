---
title: Circuitos en el Dominio de s
order: 2
tags:
  - circuitos-electricos
  - teoria
  - transitorios
  - laplace
  - impedancia-operacional
draft: false
aliases:
  - circuitos en el dominio de s
  - impedancia operacional
  - impedancia en s
  - s-domain circuit
---

# Circuitos en el Dominio de $s$

> [!definicion]
> En el dominio de $s$, cada elemento se sustituye por su **impedancia** $Z(s)$ y se cumple la **ley de Ohm generalizada** $V(s)=Z(s)\,I(s)$:
> $$Z_R=R,\qquad Z_L=sL,\qquad Z_C=\frac{1}{sC}.$$
> Las **condiciones iniciales** se incorporan como **fuentes** añadidas. Hecho esto, el circuito se resuelve con **todas** las técnicas resistivas (serie/paralelo, divisores, mallas, nodos, Thévenin), pero algebraicamente.

> [!info]
> El paso operativo de [[Laplace en Circuitos/index| Laplace en circuitos]] ([[3 Almacenamiento y Transitorios/index| capítulo 3]]). Convierte el análisis dinámico en uno **resistivo** en $s$; sobre él se definen la [[Funcion de Transferencia]] y la [[Solucion de Transitorios con Laplace| solución de transitorios]]. Fraile Mora, cap. 4, §4.7.

---

## Ejemplo

> [!ejemplo]
> **Los tres elementos y un divisor en $s$.**
>
> Cada elemento del tiempo pasa a una impedancia en $s$:
>
> ![[impedancias_s.svg|580]]
>
> *$R\to R$, $L\to sL$, $C\to 1/sC$. Derivar (en $L$) multiplica por $s$; integrar (en $C$) divide por $s$.*
>
> Con ellas, un **RC** es un simple **divisor de tensión** en $s$: si $V_s$ alimenta $R$ en serie con $C$ y se toma la salida en $C$,
> $$\frac{V_C(s)}{V_s(s)}=\frac{Z_C}{Z_R+Z_C}=\frac{1/sC}{R+1/sC}=\frac{1}{1+sRC}.$$
>
> > [!solucion]
> > El [[Divisor de Voltaje| divisor de tensión]] del capítulo 1 vale **igual** en $s$, con $Z$ en vez de $R$. El polo en $s=-1/RC$ anticipa la exponencial $e^{-t/RC}$ del [[Circuito RC]].

---

## En qué consiste

> [!teoria] La ley de Ohm generalizada
> Las leyes de los elementos, transformadas (con condiciones iniciales nulas), son multiplicaciones:
> - **Resistencia:** $v=Ri \Rightarrow V(s)=R\,I(s)$, $Z_R=R$.
> - **Inductor:** $v=L\dfrac{di}{dt} \Rightarrow V(s)=sL\,I(s)$, $Z_L=sL$ (derivar $\to \times s$).
> - **Condensador:** $i=C\dfrac{dv}{dt} \Rightarrow I(s)=sC\,V(s)$, luego $Z_C=1/sC$ (integrar $\to \div s$).
>
> Como todas tienen la forma $V=Z\,I$, **Kirchhoff y todos los métodos** del análisis resistivo se aplican sin cambios, ahora con números complejos en $s$.

> [!teoria] Las condiciones iniciales son fuentes
> Si el almacenador no parte de cero, su modelo en $s$ incluye una **fuente** que representa la energía inicial:
> - **Inductor** con $i_L(0)$: $\;V(s)=sL\,I(s)-L\,i_L(0)$ → una $sL$ en serie con una **fuente de tensión** $L\,i_L(0)$ (o, equivalente, $sL$ en paralelo con una fuente de corriente $i_L(0)/s$).
> - **Condensador** con $v_C(0)$: $\;V(s)=\dfrac{I(s)}{sC}+\dfrac{v_C(0)}{s}$ → una $1/sC$ en serie con una **fuente de tensión** $v_C(0)/s$.
>
> Por eso las condiciones iniciales entran **automáticamente** en el planteamiento, sin tratarlas aparte.

> [!algoritmo] Analizar un circuito en $s$
> **Paso 1 —** Sustituir cada elemento por su impedancia $Z(s)$ y añadir las fuentes de las condiciones iniciales. **Paso 2 —** Resolver el circuito en $s$ con cualquier método resistivo (divisores, mallas, nodos, [[Teorema de Thevenin| Thévenin]]) para la incógnita $X(s)$. **Paso 3 —** Antitransformar $X(s)$ (normalmente por fracciones parciales) para obtener $x(t)$.

> [!warning]
> $Z(s)$ depende de $s$ (a diferencia de $R$): el inductor "pesa" más a $s$ grande ($sL$) y el condensador a $s$ pequeño ($1/sC$). Y **no** olvidar las fuentes de condiciones iniciales si los almacenadores no parten de cero, o el transitorio saldrá mal.

## Resumen

> [!resumen]
> | Elemento | $Z(s)$ | Con condición inicial |
> |:---|:---|:---|
> | Resistencia | $R$ | — |
> | Inductor | $sL$ | $sL$ + fuente $L\,i_L(0)$ |
> | Condensador | $1/sC$ | $1/sC$ + fuente $v_C(0)/s$ |
> | Ley de Ohm | $V(s)=Z(s)I(s)$ | Kirchhoff y métodos, igual |

> [!corolario]
> Pasar al dominio de $s$ convierte un circuito dinámico en uno **resistivo** con impedancias: todo lo aprendido en los capítulos 1 y 2 se reutiliza. Es lo que hace de Laplace un método tan económico, y la base de la [[Funcion de Transferencia]].

> [!referencia]
> Fraile Mora, cap. 4, §4.7. Define: [[Transformada de Laplace]]. Continúa en: [[Funcion de Transferencia]] y [[Solucion de Transitorios con Laplace]].
