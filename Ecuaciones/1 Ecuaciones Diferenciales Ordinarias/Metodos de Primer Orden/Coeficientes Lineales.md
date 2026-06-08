---
title: Coeficientes Lineales
tags:
  - ecuaciones
  - edo
  - teoria
  - primer-orden
  - coeficientes-lineales
draft: false
aliases:
  - coeficientes lineales
  - ecuación con coeficientes lineales
  - linear coefficients
  - traslación al corte de rectas
---

# Coeficientes Lineales

> [!definicion]
> Una EDO tiene **coeficientes lineales** si se escribe en forma diferencial con dos expresiones
> lineales en $x,y$:
> $$(a_1x+b_1y+c_1)\,dx+(a_2x+b_2y+c_2)\,dy=0.$$
> Si $c_1=c_2=0$ ya es directamente [[Ecuaciones Homogeneas | homogénea]]. Cuando hay términos
> independientes $c_i\neq0$, el método se decide observando las **dos rectas**
> $$L_1:\ a_1x+b_1y+c_1=0,\qquad L_2:\ a_2x+b_2y+c_2=0,$$
> según se corten o sean paralelas.

> [!info]
> Tercer tipo del [[index | catálogo de primer orden]] (libro, cap. 1.3.2). Es una **extensión** de
> las [[Ecuaciones Homogeneas | homogéneas]]: los términos $c_1,c_2$ rompen la homogeneidad, y la
> idea es **recuperarla** trasladando el origen. Ambos caminos terminan en métodos ya conocidos:
> homogénea (rectas que se cortan) o [[Variables Separables | separable]] (rectas paralelas).

---

## Ejemplo

> [!ejemplo] Ejemplo 1 — rectas no paralelas (traslación al corte)
> **Resolver $(2x-y+1)\,dx+(x+y)\,dy=0$.**
>
> **Paso 1 — escribir las rectas y buscar el corte.** Aquí $c_2=0$, pero $c_1=1\neq0$, así que no es
> homogénea. Las rectas son
> $$L_1:\ 2x-y+1=0,\qquad L_2:\ x+y=0.$$
> Como $a_1/a_2=2/1\neq b_1/b_2=-1/1$, **no son paralelas**: se cortan. Resolviendo el sistema,
> sumando ambas ecuaciones $3x+1=0\Rightarrow x=-\tfrac13$, y de $L_2$, $y=-x=\tfrac13$. El corte es
> $$(h,k)=\left(-\tfrac13,\ \tfrac13\right).$$
>
> **Paso 2 — trasladar el origen al corte.** Con $\bar x=x-h=x+\tfrac13$ y $\bar y=y-k=y-\tfrac13$
> (de modo que $dx=d\bar x,\ dy=d\bar y$), los términos independientes desaparecen:
> $$(2\bar x-\bar y)\,d\bar x+(\bar x+\bar y)\,d\bar y=0.$$
> Ahora **es homogénea** en $\bar x,\bar y$. En forma normal,
> $$\frac{d\bar y}{d\bar x}=-\frac{2\bar x-\bar y}{\bar x+\bar y}=\frac{\bar y-2\bar x}{\bar x+\bar y}.$$
>
> **Paso 3 — resolver la homogénea con $\bar y=u\bar x$** ($\bar y'=u'\bar x+u$):
> $$u'\bar x+u=\frac{u-2}{1+u}\ \Longrightarrow\ u'\bar x=\frac{u-2}{1+u}-u=\frac{-(u^{2}+2)}{1+u}.$$
> Separando,
> $$\frac{1+u}{u^{2}+2}\,du=-\frac{d\bar x}{\bar x}.$$
>
> **Paso 4 — integrar.** Con $\displaystyle\int\frac{u}{u^{2}+2}du=\tfrac12\ln(u^{2}+2)$ y
> $\displaystyle\int\frac{du}{u^{2}+2}=\tfrac{1}{\sqrt2}\arctan\frac{u}{\sqrt2}$:
> $$\tfrac12\ln(u^{2}+2)+\tfrac{1}{\sqrt2}\arctan\frac{u}{\sqrt2}=-\ln|\bar x|+C.$$
>
> **Paso 5 — deshacer todo.** Con $u=\bar y/\bar x=\dfrac{y-1/3}{x+1/3}=\dfrac{3y-1}{3x+1}$ y
> $\bar x=x+\tfrac13$, la solución implícita queda
> $$\boxed{\ \tfrac12\ln\!\left(\left(\tfrac{3y-1}{3x+1}\right)^{2}+2\right)+\tfrac{1}{\sqrt2}\arctan\!\frac{3y-1}{\sqrt2\,(3x+1)}+\ln|3x+1|=C\ }$$
> válida para $x\neq-\tfrac13$ (la traslación absorbió la constante $\ln 3$ en $C$).

> [!ejemplo] Ejemplo 2 — rectas paralelas (sustitución a separable)
> **Resolver $(2x+3y-1)\,dx+(4x+6y+2)\,dy=0$.**
>
> **Paso 1 — detectar paralelismo.** Comparando coeficientes,
> $\dfrac{a_1}{a_2}=\dfrac{2}{4}=\dfrac{b_1}{b_2}=\dfrac{3}{6}=\tfrac12$: las rectas **son paralelas**
> (de hecho $4x+6y=2(2x+3y)$), no hay corte y la traslación no sirve. La clave es que **ambos**
> términos dependen del mismo bloque $2x+3y$.
>
> **Paso 2 — sustituir el bloque.** Sea $u=2x+3y-1$, entonces $du=2\,dx+3\,dy$, luego
> $dy=\dfrac{du-2\,dx}{3}$. Además $4x+6y+2=2(2x+3y)+2=2(u+1)+2=2u+4$. La ecuación pasa a estar solo
> en $u$ y $x$:
> $$u\,dx+(2u+4)\,\frac{du-2\,dx}{3}=0.$$
>
> **Paso 3 — agrupar y separar.** Multiplicando por $3$ y juntando los $dx$:
> $$\big[3u-2(2u+4)\big]\,dx+(2u+4)\,du=0\ \Longrightarrow\ (-u-8)\,dx+(2u+4)\,du=0,$$
> de donde
> $$\frac{2u+4}{u+8}\,du=dx.$$
>
> **Paso 4 — integrar.** Dividiendo, $\dfrac{2u+4}{u+8}=2-\dfrac{12}{u+8}$:
> $$\int\!\left(2-\frac{12}{u+8}\right)du=\int dx\ \Longrightarrow\ 2u-12\ln|u+8|=x+C_0.$$
>
> **Paso 5 — deshacer $u=2x+3y-1$.** Sustituyendo y reordenando (el $-8\ln$ tras simplificar la
> constante numérica), la solución implícita es
> $$\boxed{\ 2x+3y-1-8\ln|2x+3y+7|+y=C\ }$$
> con las constantes numéricas absorbidas en $C$.

---

## En qué consiste

> [!teoria]
> La idea geométrica es **quitar los términos independientes** $c_1,c_2$, que son lo único que separa
> esta ecuación de una homogénea.
>
> - **Rectas no paralelas:** se cortan en un punto $(h,k)$. La traslación $\bar x=x-h,\ \bar y=y-k$
>   lleva el origen al corte; en las nuevas coordenadas $a_i\bar x+b_i\bar y+c_i$ se convierte en
>   $a_i\bar x+b_i\bar y$ (los $c_i$ se anulan **por definición** del corte), y la ecuación queda
>   homogénea. Luego se aplica $\bar y=u\bar x$ como en [[Ecuaciones Homogeneas]].
> - **Rectas paralelas:** no hay corte, así que no existe traslación que anule ambos $c_i$. Pero el
>   paralelismo $a_1/a_2=b_1/b_2$ obliga a que $a_2x+b_2y$ sea **múltiplo** de $a_1x+b_1y$; todo
>   depende de un **único bloque lineal**. El cambio $u=a_1x+b_1y$ colapsa $x,y$ en una sola variable
>   y la ecuación se vuelve [[Variables Separables | separable]].

> [!algoritmo] Resolver coeficientes lineales
> 1. **¿Paralelas?** Compara $\dfrac{a_1}{a_2}$ con $\dfrac{b_1}{b_2}$.
> 2. **No paralelas:** halla el corte $(h,k)$ resolviendo $L_1=L_2=0$; traslada $\bar x=x-h,\ \bar
>    y=y-k$ y resuelve la **homogénea** resultante con $\bar y=u\bar x$.
> 3. **Paralelas:** sustituye $u=a_1x+b_1y$ (o $a_2x+b_2y$); la ecuación se vuelve **separable** en
>    $u$ y $x$.
> 4. En ambos casos, **deshaz** los cambios para volver a $x,y$ e impón la condición inicial.

> [!proposicion] Criterio de paralelismo
> Las rectas $L_1,L_2$ son paralelas $\iff a_1b_2-a_2b_1=0$ $\iff \dfrac{a_1}{a_2}=\dfrac{b_1}{b_2}$.
> El determinante $a_1b_2-a_2b_1$ es justo el del sistema lineal que da el corte $(h,k)$: si no se
> anula, el corte **existe y es único** (camino homogéneo); si se anula, no hay corte único (camino
> separable).

## Resumen

> [!resumen]
> | Caso | Cómo se detecta | Cambio | Reduce a |
> |---|---|---|---|
> | No paralelas | $a_1b_2-a_2b_1\neq0$ | trasladar a $(h,k)$ | [[Ecuaciones Homogeneas \| homogénea]] |
> | Paralelas | $a_1b_2-a_2b_1=0$ | $u=a_1x+b_1y$ | [[Variables Separables \| separable]] |
> | $c_1=c_2=0$ | sin términos indep. | — | ya es homogénea |

> [!corolario]
> Coeficientes lineales no es un método nuevo, sino un **pre-procesado**: con una traslación o una
> sustitución de bloque, la ecuación cae en un tipo ya resuelto. Todo el truco está en mirar las dos
> rectas y preguntarse si se cortan.

> [!referencia]
> - Caso al que reduce (no paralelas): [[Ecuaciones Homogeneas]].
> - Caso al que reduce (paralelas): [[Variables Separables]].
> - Vuelta al catálogo: [[index]].
