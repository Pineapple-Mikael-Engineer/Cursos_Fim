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

> [!ejemplo] Caso escalar — masa
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

## Ejemplo

> [!ejemplo] Caso vectorial — corriente total
> **Corriente total $\vec I=\int_V d\tau\,\vec J$ en una caja.** Sea la caja $V=[0,1]\times[0,2]\times[0,1]$ recorrida por la densidad de corriente $\vec J=(y,\,z,\,2x)$. La integral vectorial se hace **componente a componente** (los $\hat{e}_i$ son constantes y salen de la integral):
> $$\vec I=\int_V d\tau\,\vec J=\hat{e}_i\int_V d\tau\,J_i.$$
>
> **Componente $x$:** $\displaystyle I_x=\int_V y\,d\tau=\int_0^1\!\!dx\int_0^2\!\!y\,dy\int_0^1\!\!dz=(1)\Big[\tfrac{y^2}{2}\Big]_0^2(1)=(1)(2)(1)=2.$
>
> **Componente $y$:** $\displaystyle I_y=\int_V z\,d\tau=\int_0^1\!\!dx\int_0^2\!\!dy\int_0^1\!\!z\,dz=(1)(2)\Big[\tfrac{z^2}{2}\Big]_0^1=(1)(2)\big(\tfrac12\big)=1.$
>
> **Componente $z$:** $\displaystyle I_z=\int_V 2x\,d\tau=\int_0^1\!\!2x\,dx\int_0^2\!\!dy\int_0^1\!\!dz=\Big[x^2\Big]_0^1(2)(1)=(1)(2)(1)=2.$
>
> Por tanto $\vec I=(2,\,1,\,2)$. Cada componente es una integral de volumen **escalar** independiente; el carácter vectorial sólo reapareció al reensamblar $\vec I=I_x\hat{e}_x+I_y\hat{e}_y+I_z\hat{e}_z$.
>
> *(El mismo esquema da el numerador del centro de masa $\int_V\vec r\,\rho\,d\tau$: una integral escalar por cada coordenada $x_i$.)*

---

## En qué consiste

> [!teoria]
> La integral de volumen se escribe en forma de operador $\int_V d\tau\,(\cdot)$, con $d\tau$ el volumen diferencial y $V$ la región total. En cartesianas $d\tau=dx_1\,dx_2\,dx_3=dx\,dy\,dz$, de modo que
> $$\int_V d\tau\,\Phi=\int_V dx_1\,dx_2\,dx_3\,\Phi.$$
> Como la variable de integración es escalar, **no hay producto punto ni cruz**: el operador actúa directamente. Sobre un campo vectorial $\vec v=v_i\hat{e}_i$ los versores salen de la integral (base cartesiana independiente de la posición) y queda una integral de volumen por componente:
> $$\int_V d\tau\,\vec v=\hat{e}_i\int_V d\tau\,v_i.$$

> [!proposicion] La integral vectorial es componente a componente
> $$\int_V d\tau\,\vec v=\hat{e}_i\int_V d\tau\,v_i,$$
> es decir, integrar un campo vectorial sobre $V$ equivale a integrar cada una de sus tres componentes escalares por separado y reensamblar el vector.

> [!demostracion]
> **Paso 1 — desarrollar el integrando en la base.** Escribimos el campo en cartesianas,
> $$\vec v(\vec r)=v_i(\vec r)\,\hat{e}_i=v_1\hat{e}_1+v_2\hat{e}_2+v_3\hat{e}_3.$$
>
> **Paso 2 — usar la linealidad de la integral.** El operador $\int_V d\tau\,(\cdot)$ es lineal, así que la integral de la suma es la suma de las integrales:
> $$\int_V d\tau\,\vec v=\int_V d\tau\,(v_1\hat{e}_1+v_2\hat{e}_2+v_3\hat{e}_3)=\sum_i\int_V d\tau\,(v_i\,\hat{e}_i).$$
>
> **Paso 3 — sacar los versores constantes.** Los vectores base cartesianos $\hat{e}_i$ **no dependen de la posición** $\vec r$ (a diferencia de las bases curvilíneas $\hat{q}_i$), de modo que son constantes respecto de la integración en $d\tau$ y salen del integrando:
> $$\int_V d\tau\,(v_i\,\hat{e}_i)=\hat{e}_i\int_V d\tau\,v_i.$$
>
> **Paso 4 — reensamblar.** Reuniendo las tres direcciones,
> $$\int_V d\tau\,\vec v=\hat{e}_i\int_V d\tau\,v_i=\hat{e}_1\!\int_V v_1\,d\tau+\hat{e}_2\!\int_V v_2\,d\tau+\hat{e}_3\!\int_V v_3\,d\tau.$$
> Cada $\int_V v_i\,d\tau$ es una integral de volumen **escalar** ordinaria. $\blacksquare$
>
> > [!warning]
> > Este paso de "sacar el versor" **sólo es válido en coordenadas cartesianas**. En curvilíneas (cilíndricas, esféricas) los $\hat{q}_i$ varían con el punto y **no** pueden extraerse de la integral; hay que proyectar antes sobre una base fija.

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
