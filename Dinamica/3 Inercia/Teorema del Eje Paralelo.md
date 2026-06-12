---
title: Teorema del Eje Paralelo
tags:
  - dinamica
  - teoria
  - inercia
draft: false
aliases:
  - teorema de Steiner
  - eje paralelo
  - parallel axis theorem
  - Steiner's theorem
---

# Teorema del Eje Paralelo $\mathbf I_O=\mathbf I_G+m[d^2\mathbb 1-\vec d\,\vec d^{\,T}]$

> [!definicion]
> El **teorema del eje paralelo** (o **teorema de Steiner**), en su forma **tensorial**, relaciona el tensor de inercia respecto a un punto $O$ con el tensor respecto al **centro de masa** $G$:
> $$\mathbf I_O=\mathbf I_G+m\big[(\vec d\cdot\vec d)\,\mathbb 1-\vec d\,\vec d^{\,T}\big],$$
> donde $m$ es la masa del cuerpo, $\mathbb 1$ es el tensor identidad y $\vec d=\vec r_{G/O}$ es el vector que va de $O$ a $G$ (su módulo $d=|\vec d|$ es la distancia entre ambos puntos).
>
> En **componentes**:
> $$I_{O,ij}=I_{G,ij}+m\big(d^2\delta_{ij}-d_i\,d_j\big).$$
> Restringido a un **único eje**, recupera la forma escalar clásica:
> $$I_O=I_G+m\,d^2.$$

![[eje_paralelo.svg|440]]

*Dos ejes paralelos: el del CM ($G$) y otro por $O$, separados $\vec d$. El término $m[d^2\mathbb 1-\vec d\vec d^{\,T}]$ traslada el tensor.*

> [!info]
> El teorema **traslada** el [[Tensor de Inercia]] entre dos puntos del cuerpo, una operación central en la [[3 Inercia/index | inercia]]. Es **imprescindible** para reutilizar la [[Momentos de Inercia de Figuras | tabla de figuras]] —cuyos valores están tabulados **en el centro de masa**— sobre cualquier otro eje de rotación. La masa $m$ aparece como factor de un término puramente **geométrico** que solo depende de la separación $\vec d$. Cf. Goldstein §5.3.

---

## Ejemplo

Considérese una **varilla delgada** homogénea de masa $m$ y longitud $L$. Su momento de inercia respecto a un eje perpendicular que pasa por su **centro** es
$$I_G=\tfrac{1}{12}\,mL^2.$$
Para obtener el momento respecto a un eje perpendicular que pasa por un **extremo**, el extremo dista del centro de masa
$$d=\frac{L}{2},$$
de modo que el teorema da
$$I_O=I_G+m\,d^2=\tfrac{1}{12}\,mL^2+m\left(\frac{L}{2}\right)^2=\tfrac{1}{12}\,mL^2+\tfrac{1}{4}\,mL^2.$$

> [!solucion]
> $$I_{\text{extremo}}=\tfrac{1}{12}\,mL^2+\tfrac{3}{12}\,mL^2=\boxed{\tfrac{1}{3}\,mL^2}.$$
> El momento se **cuadruplica menos un factor**: pasar de $\tfrac{1}{12}$ a $\tfrac{1}{3}$ es multiplicar por $4$. La razón física es que la masa, al alejarse del eje, **pesa con el cuadrado de la distancia**: desplazar el eje al extremo añade $m\,d^2=\tfrac14 mL^2$, tres veces el valor central.

---

## En qué consiste

> [!teoria]
> El tensor de inercia mide cómo se distribuye la masa **alrededor** de un punto. Al cambiar el punto de referencia de $G$ a $O$, cada elemento de masa $dm$ ve modificada su posición en el mismo vector constante $\vec d$. El teorema cuantifica el efecto de ese desplazamiento uniforme: el tensor original $\mathbf I_G$ más un término que se comporta como el de una **masa puntual** $m$ situada en $G$, vista desde $O$. La estructura $d^2\mathbb 1-\vec d\,\vec d^{\,T}$ es precisamente el tensor de inercia de un punto material respecto al origen.

> [!teorema]
> Sea un cuerpo de masa $m$ y centro de masa $G$. Para cualquier punto $O$, con $\vec d=\vec r_{G/O}$, se cumple
> $$I_{O,ij}=I_{G,ij}+m\big(d^2\delta_{ij}-d_i\,d_j\big).$$

> [!demostracion]
> Partimos de la definición del tensor de inercia respecto a $O$,
> $$I_{O,ij}=\int\big(r_O^2\,\delta_{ij}-r_{O,i}\,r_{O,j}\big)\,dm,$$
> donde $\vec r_{p/O}$ es la posición del elemento $dm$ respecto a $O$. Usamos la descomposición
> $$\vec r_{p/O}=\vec r_{p/G}+\vec d.$$
>
> **Paso 1 — Sustituir.** Para el módulo al cuadrado,
> $$r_O^2=\vec r_{p/O}\cdot\vec r_{p/O}=r_G^2+2\,\vec r_{p/G}\cdot\vec d+d^2,$$
> y para el producto de componentes,
> $$r_{O,i}\,r_{O,j}=(r_{G,i}+d_i)(r_{G,j}+d_j)=r_{G,i}r_{G,j}+r_{G,i}d_j+d_i r_{G,j}+d_i d_j.$$
>
> **Paso 2 — Anular los términos lineales.** Al integrar, todos los términos **lineales** en $\vec r_{p/G}$ contienen el factor
> $$\int\vec r_{p/G}\,dm=\vec 0,$$
> que se anula por la **definición de centro de masa** ($G$ es el punto respecto al cual la posición media de la masa es nula). Desaparecen así el término $2(\vec r_{p/G}\cdot\vec d)\delta_{ij}$ y los cruzados $r_{G,i}d_j+d_i r_{G,j}$.
>
> **Paso 3 — Recolectar.** Sobreviven dos contribuciones. La del **centro de masa**,
> $$\int\big(r_G^2\,\delta_{ij}-r_{G,i}r_{G,j}\big)\,dm=I_{G,ij},$$
> y la **constante**, que sale de la integral por no depender de $dm$,
> $$\int\big(d^2\,\delta_{ij}-d_i d_j\big)\,dm=m\big(d^2\,\delta_{ij}-d_i d_j\big).$$
> Sumando ambas,
> $$\boxed{\,\mathbf I_O=\mathbf I_G+m\big[d^2\,\mathbb 1-\vec d\,\vec d^{\,T}\big]\,}.\qquad\blacksquare$$

> [!proposicion]
> El término añadido $m\big[d^2\mathbb 1-\vec d\,\vec d^{\,T}\big]$ es **semidefinido positivo**: para cualquier eje unitario $\hat n$,
> $$\hat n^{\,T}\big(d^2\mathbb 1-\vec d\,\vec d^{\,T}\big)\hat n=d^2-(\vec d\cdot\hat n)^2=d_\perp^2\ge 0,$$
> donde $d_\perp$ es la componente de $\vec d$ **perpendicular** al eje. En consecuencia, el momento de inercia respecto a un eje de dirección dada es **mínimo** cuando el eje pasa por el **centro de masa**. Para un eje concreto, esto se lee como
> $$I_O=I_G+m\,d_\perp^2\ge I_G.$$

> [!warning]
> **Uno de los dos puntos debe ser el centro de masa.** El teorema NO conecta directamente dos puntos arbitrarios $O_1$ y $O_2$: para trasladar de $O_1$ a $O_2$ hay que **pasar por $G$** (restar para llegar a $G$, sumar para alejarse). El vector $\vec d$ va de $O$ a $G$; su módulo es la distancia. El resultado vale para el **tensor completo** —incluidos los productos de inercia fuera de la diagonal—, no solo para un eje aislado.

---

## Resumen

> [!resumen]
> | Forma | Expresión |
> |---|---|
> | Tensorial | $\mathbf I_O=\mathbf I_G+m\big[d^2\mathbb 1-\vec d\,\vec d^{\,T}\big]$ |
> | Componentes | $I_{O,ij}=I_{G,ij}+m(d^2\delta_{ij}-d_i d_j)$ |
> | Un eje | $I_O=I_G+m\,d^2$ |
> | Mínimo | alcanzado en el **centro de masa** $G$ |
>
> El término sumado es el tensor de una **masa puntual** $m$ en $G$ vista desde $O$; siempre **incrementa** el momento de inercia.

> [!corolario]
> Conocido $\mathbf I_G$ y la tabla de [[Momentos de Inercia de Figuras]] (tabulada en el CM), el tensor respecto a **cualquier** punto del cuerpo se obtiene con una sola suma geométrica. Para combinar varios cuerpos, se traslada el tensor de cada uno al punto común antes de sumar.

> [!referencia]
> - [[Tensor de Inercia]] — el objeto que se traslada.
> - [[Momentos de Inercia de Figuras]] — valores en el CM listos para Steiner.
> - [[3 Inercia/index]] — contexto en la inercia.
> - Goldstein, *Classical Mechanics*, §5.3.
