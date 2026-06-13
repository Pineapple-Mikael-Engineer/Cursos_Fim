---
title: Operadores Integrales
tags:
  - analisis-tensorial
  - teoria
  - calculo-vectorial
  - operadores-integrales
  - index
draft: false
aliases:
  - operadores integrales
  - notacion de operador integral
  - integral operators
---

# Operadores Integrales

> [!definicion]
> Un **operador integral** es una integral escrita en *forma de operador*: en vez de mezclar el signo $\int$ con el integrando, se agrupa $\int dx\,(\cdot)$ como un símbolo que **opera** sobre lo que tiene a su derecha, igual que $\vec\nabla$ opera sobre un campo. Las tres variantes geométricas son la integral de **línea** $\int_C d\vec r$, la de **superficie** $\int_S d\vec\sigma$ y la de **volumen** $\int_V d\tau$.

> [!info]
> Sección **2.2** del [[index | capítulo 2]] (Rogan & Muñoz). Es la contraparte integral de los [[Operadores Diferenciales/index | operadores diferenciales]] (cap. 2.3); ambos quedan ligados por los [[Teoremas Integrales/index | teoremas integrales]] (cap. 2.5). Se desglosa en:
> - [[Integral de Linea]] — $\int_C d\vec r$, trabajo y circulación (cap. 2.2.2).
> - [[Integral de Superficie]] — $\int_S d\vec\sigma$, flujo a través de una superficie (cap. 2.2.3).
> - [[Integral de Volumen]] — $\int_V d\tau$, integración sobre una región (cap. 2.2.4).

---

## Ejemplo

> [!ejemplo]
> **Pasar a forma de operador y factorizar.** El gradiente se escribe $\vec\nabla\Phi$: el operador $\vec\nabla$ a la izquierda actúa sobre $\Phi$. La integral, en cambio, suele escribirse mezclada, $\int f(x)\,dx$. Reordenando se obtiene la **forma de operador**
> $$\int dx\,f(x),$$
> donde $\int dx\,(\cdot)$ es un símbolo que opera sobre $f(x)$. En la práctica, el operador integral **pasa a través de todo factor que no dependa de la variable de integración**. Por ejemplo, con la variable $x$ y un integrando $x^2(x+y)y^2$:
> $$\int dx\,x^2(x+y)\,y^2=y^2\int dx\,x^2(x+y),$$
> porque $y^2$ es constante respecto de $x$. Evaluemos ahora el factor restante entre $x=0$ y $x=1$:
> $$\int_0^1 x^2(x+y)\,dx=\int_0^1\big(x^3+x^2y\big)\,dx=\Big[\tfrac{x^4}{4}+\tfrac{x^3}{3}y\Big]_0^1=\frac14+\frac{y}{3}.$$
> Por tanto
> $$\int_0^1 dx\,x^2(x+y)\,y^2=y^2\Big(\frac14+\frac{y}{3}\Big)=\frac{y^2}{4}+\frac{y^3}{3}.$$
> El factor $y^2$ salió íntegro fuera del operador antes de integrar en $x$.

---

## En qué consiste

> [!teoria]
> Que el gradiente, la divergencia y el rotor sean *operadores* significa que un símbolo ($\vec\nabla$) actúa sobre un operando ($\Phi$, $\vec A$). La integral admite la misma lectura: escrita como $\int dx\,(\cdot)$, el bloque $\int dx$ es el operador y lo que sigue es el operando. La regla operativa es que **el operador atraviesa los factores constantes respecto de la variable de integración**, exactamente como una derivada respeta los factores constantes. Como $d\vec r$, $d\vec\sigma$ y $d\tau$ están escritos en notación vectorial, las definiciones valen en cualquier sistema de coordenadas; en cartesianas se desarrollan con $d\vec r=dx_i\hat{e}_i$, $d\vec\sigma=d\sigma_i\hat{e}_i$ y $d\tau=dx\,dy\,dz$.

> [!info] Las tres integrales geométricas
> | Operador | Diferencial | Sobre escalar $\Phi$ | Sobre vector $\vec v$ |
> |---|---|---|---|
> | Línea $\int_C$ | $d\vec r=dx_i\hat{e}_i$ | $\int_C d\vec r\,\Phi$ (vector) | $\int_C d\vec r\cdot\vec v$ (escalar) |
> | Superficie $\int_S$ | $d\vec\sigma=d\sigma_i\hat{e}_i$ | $\int_S d\vec\sigma\,\Phi$ (vector) | $\int_S d\vec\sigma\cdot\vec v$ (escalar) |
> | Volumen $\int_V$ | $d\tau=dx\,dy\,dz$ | $\int_V d\tau\,\Phi$ (escalar) | $\int_V d\tau\,\vec v$ (vector) |

## Resumen

> [!resumen]
> | Subnota | Aporta | Forma núcleo |
> |---|---|---|
> | [[Integral de Linea]] | trabajo, circulación | $W=\int_C d\vec r\cdot\vec F=\int_C dx_i\,F_i$ |
> | [[Integral de Superficie]] | flujo | $\int_S d\vec\sigma\cdot\vec v=\int_S d\sigma_i\,v_i$ |
> | [[Integral de Volumen]] | masa, carga, totales | $\int_V d\tau\,\Phi$ |

> [!corolario]
> La notación de operador unifica las integrales con $\vec\nabla$: ambos son símbolos que actúan a la izquierda de su operando y atraviesan los factores constantes. Esta lectura es la que permite enunciar de forma limpia los [[Teoremas Integrales/index | teoremas de Gauss, Green y Stokes]], que igualan un operador integral en el borde con un operador diferencial en el interior.

> [!referencia]
> - Contraparte diferencial: [[Operadores Diferenciales/index]].
> - Conexión borde–interior: [[Teoremas Integrales/index]].
> - Campos que se integran: [[Campos Escalares y Vectoriales]].
