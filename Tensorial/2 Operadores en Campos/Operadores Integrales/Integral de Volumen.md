---
title: Integral de Volumen
tags:
  - analisis-tensorial
  - teoria
  - calculo-vectorial
  - operadores-integrales
  - integral-de-volumen
draft: false
aliases:
  - integral de volumen
  - integral triple
  - masa
  - volume integral
---

# Integral de Volumen $\int_V d\tau$

> [!definicion]
> La **integral de volumen** suma una cantidad sobre una región $V$ con el elemento de volumen $d\tau=dx\,dy\,dz$. Es el operador integral más simple, porque la variable de integración es **escalar**. Sobre un escalar produce un escalar,
> $$\int_V d\tau\,\Phi=\int_V \Phi\,dx\,dy\,dz,$$
> y sobre un vector produce un vector, $\int_V d\tau\,\vec v=\hat{e}_i\int_V d\tau\,v_i$.

> [!info]
> Sección **2.2.4** del libro; tercera hija de [[index | Operadores Integrales]] (cap. 2.2). El integrando es un [[Campos Escalares y Vectoriales | campo]] escalar (densidad, energía) o vectorial. Es el lado de volumen del [[Teoremas Integrales/Teorema de Gauss | teorema de Gauss]], que lo iguala al flujo de la [[Operadores Diferenciales/Divergencia | divergencia]] a través del borde.

---

## Ejemplo

> [!ejemplo]
> **Masa de un cubo con densidad $\rho=xyz$.** Sea el cubo unidad $V=[0,1]\times[0,1]\times[0,1]$ con densidad de masa $\rho(x,y,z)=xyz$. La masa es el escalar
> $$M=\int_V d\tau\,\rho=\int_0^1\!\!\int_0^1\!\!\int_0^1 xyz\,\,dx\,dy\,dz.$$
> Como el integrando **se factoriza** y cada factor depende de una sola variable, el operador integral atraviesa los factores constantes y la triple se separa en tres simples:
> $$M=\left(\int_0^1 x\,dx\right)\left(\int_0^1 y\,dy\right)\left(\int_0^1 z\,dz\right).$$
> Cada factor vale $\int_0^1 x\,dx=\big[\tfrac{x^2}{2}\big]_0^1=\tfrac12$, de modo que
> $$M=\frac12\cdot\frac12\cdot\frac12=\frac18=0{,}125.$$
> Si en cambio quisiéramos integrar paso a paso sin separar, integrando primero en $x$:
> $$\int_0^1 xyz\,dx=yz\Big[\tfrac{x^2}{2}\Big]_0^1=\tfrac12 yz,\qquad\int_0^1\tfrac12 yz\,dy=\tfrac12 z\Big[\tfrac{y^2}{2}\Big]_0^1=\tfrac14 z,$$
> $$\int_0^1\tfrac14 z\,dz=\tfrac14\Big[\tfrac{z^2}{2}\Big]_0^1=\frac18,$$
> mismo resultado, $M=1/8$.

---

## En qué consiste

> [!teoria]
> La integral de volumen se escribe en forma de operador $\int_V d\tau\,(\cdot)$, con $d\tau$ el volumen diferencial y $V$ la región total. En cartesianas $d\tau=dx_1\,dx_2\,dx_3=dx\,dy\,dz$, de modo que
> $$\int_V d\tau\,\Phi=\int_V dx_1\,dx_2\,dx_3\,\Phi.$$
> Como la variable de integración es escalar, **no hay producto punto ni cruz**: el operador actúa directamente. Sobre un campo vectorial $\vec v=v_i\hat{e}_i$ los versores salen de la integral (base cartesiana independiente de la posición) y queda una integral de volumen por componente:
> $$\int_V d\tau\,\vec v=\hat{e}_i\int_V d\tau\,v_i.$$

> [!info] Cómo se evalúa
> Una integral de volumen es una **integral triple** iterada: se integra en una variable a la vez, tratando las otras como constantes. Si el integrando se factoriza como $\Phi=f(x)g(y)h(z)$ y la región es un caja, la triple se separa en el producto de tres integrales simples (como en el ejemplo). Para densidades $\rho(\vec r)$, $\int_V d\tau\,\rho$ es la masa; para densidades de carga, la carga total.

## Resumen

> [!resumen]
> | Operación | Forma | Resultado |
> |---|---|---|
> | Sobre escalar | $\int_V d\tau\,\Phi=\int_V \Phi\,dx\,dy\,dz$ | escalar |
> | Sobre vector | $\int_V d\tau\,\vec v=\hat{e}_i\int_V d\tau\,v_i$ | vector |
> | Elemento | $d\tau=dx\,dy\,dz$ | — |
> | Físico típico | $M=\int_V\rho\,d\tau$ | masa / carga total |

> [!corolario]
> La integral de volumen es la más sencilla porque integra sobre una variable escalar: no hay normal ni tangente que fijar. Se evalúa como una triple iterada y, cuando el integrando y la región se factorizan, se reduce a un producto de integrales simples (la masa del cubo con $\rho=xyz$ dio $1/8$). Es el miembro de volumen del [[Teoremas Integrales/Teorema de Gauss | teorema de Gauss]].

> [!referencia]
> - Forma de operador y reglas: [[index | Operadores Integrales]].
> - Hermanas: [[Integral de Linea]], [[Integral de Superficie]].
> - Divergencia y Gauss: [[Operadores Diferenciales/Divergencia]], [[Teoremas Integrales/Teorema de Gauss]].
