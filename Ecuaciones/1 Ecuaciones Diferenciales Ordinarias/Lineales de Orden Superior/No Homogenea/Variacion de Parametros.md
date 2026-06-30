---
title: Variación de Parámetros
order: 2
tags:
  - ecuaciones
  - edo
  - teoria
  - lineales
  - no-homogenea
  - variacion-de-parametros
draft: false
aliases:
  - variación de parámetros
  - método de variación de parámetros
  - variation of parameters
  - method of variation of parameters
---

# Método de Variación de Parámetros

> [!definicion]
> Método **universal** para hallar una particular $y_p$ de $L[y]=f$. Dado un conjunto fundamental $y_1,y_2$ de la homogénea, se permite que las **constantes** $c_1,c_2$ de $c_1y_1+c_2y_2$ se vuelvan **funciones** $u_1(x),u_2(x)$ (de ahí "variación de parámetros") y se busca
> $$y_p=u_1(x)\,y_1+u_2(x)\,y_2.$$
> Para la ecuación normalizada $y''+p(x)y'+q(x)y=f(x)$ resulta
> $$u_1'=-\frac{y_2\,f}{W},\qquad u_2'=\frac{y_1\,f}{W},$$
> con $W=y_1y_2'-y_2y_1'$ el [[Wronskiano e Independencia Lineal| wronskiano]] de $y_1,y_2$. Integrando,
> $$y_p=-y_1\!\int\!\frac{y_2 f}{W}\,dx+y_2\!\int\!\frac{y_1 f}{W}\,dx.$$
> Funciona para **cualquier** $f$ continua e incluso con **coeficientes variables**, a cambio de tener que integrar.

> [!info]
> La hija **universal** de [[No Homogenea/index| no homogénea]]. A diferencia de [[Coeficientes Indeterminados| coeficientes indeterminados]] —limitado a $f$ de "buena forma" y coeficientes constantes—, aquí $f$ es arbitraria y los coeficientes pueden depender de $x$ (siempre que se conozcan $y_1,y_2$). Requiere el [[Wronskiano e Independencia Lineal| wronskiano]]. Capítulo: [[1 Ecuaciones Diferenciales Ordinarias/index| EDO]].

---

## Ejemplo

> [!ejemplo] Una fuente imposible para coeficientes indeterminados
> **Resolver $y''-3y'+2y=\operatorname{sen}(e^{-x})$.** La fuente $\operatorname{sen}(e^{-x})$ **no** es de "buena forma" (no se reproduce al derivar), así que coeficientes indeterminados no sirve.
>
> **Paso 1 — homogénea y wronskiano.** Raíces $1,2$ → $y_1=e^{x}$, $y_2=e^{2x}$. El wronskiano:
> $$W=\begin{vmatrix} e^{x} & e^{2x}\\ e^{x} & 2e^{2x}\end{vmatrix}=2e^{3x}-e^{3x}=e^{3x}.$$
>
> **Paso 2 — las derivadas $u_i'$.** Con $f=\operatorname{sen}(e^{-x})$:
> $$u_1'=-\frac{y_2 f}{W}=-\frac{e^{2x}\operatorname{sen}(e^{-x})}{e^{3x}}=-e^{-x}\operatorname{sen}(e^{-x}),$$
> $$u_2'=\frac{y_1 f}{W}=\frac{e^{x}\operatorname{sen}(e^{-x})}{e^{3x}}=e^{-2x}\operatorname{sen}(e^{-x}).$$
>
> **Paso 3 — integrar** (sustitución $u=e^{-x}$, $du=-e^{-x}\,dx$):
> $$u_1=-\!\int e^{-x}\operatorname{sen}(e^{-x})\,dx=\int \operatorname{sen}(u)\,du=-\cos(e^{-x}),$$
> $$u_2=\int e^{-2x}\operatorname{sen}(e^{-x})\,dx=-\!\int u\operatorname{sen}u\,du=u\cos u-\operatorname{sen}u
> = e^{-x}\cos(e^{-x})-\operatorname{sen}(e^{-x}).$$
>
> **Paso 4 — armar $y_p=u_1y_1+u_2y_2$.**
> $$y_p=-e^{x}\cos(e^{-x})+e^{2x}\big[e^{-x}\cos(e^{-x})-\operatorname{sen}(e^{-x})\big]
> =-e^{2x}\operatorname{sen}(e^{-x}),$$
> donde los dos términos en $\cos(e^{-x})$ se cancelan. Por tanto
> $$\boxed{\,y=c_1e^{x}+c_2e^{2x}-e^{2x}\operatorname{sen}(e^{-x})\,}.$$

---

## En qué consiste

> [!teorema] Las fórmulas de variación de parámetros
> Sea $y''+p(x)y'+q(x)y=f(x)$ con conjunto fundamental $y_1,y_2$ de la homogénea y wronskiano $W=y_1y_2'-y_2y_1'\neq0$. Entonces $y_p=u_1y_1+u_2y_2$ es solución particular si
> $$u_1'=-\frac{y_2 f}{W},\qquad u_2'=\frac{y_1 f}{W}.$$

> [!demostracion]
> **Paso 1 — proponer e imponer una condición.** Buscamos $y_p=u_1y_1+u_2y_2$ con $u_1,u_2$ por determinar. Derivando,
> $$y_p'=u_1'y_1+u_2'y_2+u_1y_1'+u_2y_2'.$$
> Tenemos **dos** funciones incógnita y solo **una** ecuación ($L[y_p]=f$): hay libertad. La usamos imponiendo la **condición**
> $$u_1'y_1+u_2'y_2=0,$$
> que mata los términos con $u_i'$ y evita que aparezcan **segundas** derivadas de los $u_i$.
>
> **Paso 2 — derivar de nuevo.** Con esa condición $y_p'=u_1y_1'+u_2y_2'$, y
> $$y_p''=u_1'y_1'+u_2'y_2'+u_1y_1''+u_2y_2''.$$
>
> **Paso 3 — sustituir en $L[y_p]=f$.** Agrupando,
> $$L[y_p]=u_1\underbrace{(y_1''+py_1'+qy_1)}_{=0}+u_2\underbrace{(y_2''+py_2'+qy_2)}_{=0}+u_1'y_1'+u_2'y_2'.$$
> Como $y_1,y_2$ resuelven la homogénea, los paréntesis se anulan ($L[y_i]=0$) y queda
> $$u_1'y_1'+u_2'y_2'=f.$$
>
> **Paso 4 — resolver el sistema por Cramer.** Tenemos
> $$\begin{cases} u_1'y_1+u_2'y_2=0\\ u_1'y_1'+u_2'y_2'=f \end{cases}$$
> cuyo determinante es el wronskiano $W=y_1y_2'-y_2y_1'$. Por Cramer,
> $$u_1'=\frac{\begin{vmatrix}0 & y_2\\ f & y_2'\end{vmatrix}}{W}=-\frac{y_2 f}{W},\qquad
> u_2'=\frac{\begin{vmatrix}y_1 & 0\\ y_1' & f\end{vmatrix}}{W}=\frac{y_1 f}{W}.$$
> Integrando se obtienen $u_1,u_2$ y con ellos $y_p=u_1y_1+u_2y_2$. $\blacksquare$

> [!info] Cuándo preferir variación de parámetros
> Úsalo cuando **falla** [[Coeficientes Indeterminados| coeficientes indeterminados]], es decir:
> - la fuente $f$ **no** es de "buena forma": $\operatorname{sen}(e^{-x})$, $\sec x$, $\tan x$, $\ln x$, $\dfrac{1}{x}$, etc. (no se reproducen al derivar, no hay propuesta finita que adivinar);
> - los **coeficientes son variables** ($p,q$ dependen de $x$), con tal de **conocer** un conjunto fundamental $y_1,y_2$ (a menudo obtenido por [[Reduccion de Orden| reducción de orden]] o [[Cauchy-Euler| Cauchy-Euler]]).
>
> Precio a pagar: hay que **integrar** $\int \tfrac{y_2 f}{W}dx$ y $\int \tfrac{y_1 f}{W}dx$, que pueden ser difíciles. Si $f$ encaja en la tabla de coeficientes indeterminados, aquel método es más rápido.

> [!algoritmo] Aplicar variación de parámetros
> 1. **Normaliza** la EDO a $y''+p(x)y'+q(x)y=f(x)$ (coeficiente líder $1$; cuidado: $f$ es ya el lado derecho normalizado).
> 2. Resuelve la **homogénea**: obtén un conjunto fundamental $y_1,y_2$.
> 3. Calcula el **wronskiano** $W=y_1y_2'-y_2y_1'$.
> 4. Forma $u_1'=-\dfrac{y_2 f}{W}$ y $u_2'=\dfrac{y_1 f}{W}$.
> 5. **Integra** para obtener $u_1,u_2$ (constantes de integración a $0$: se absorben en $y_h$).
> 6. Escribe $y_p=u_1y_1+u_2y_2$ y la general $y=c_1y_1+c_2y_2+y_p$.

> [!warning]
> Antes de aplicar las fórmulas, **normaliza** la ecuación: $f$ debe ser el término independiente con el coeficiente líder igual a $1$. Si la EDO es $a(x)y''+\dots=g(x)$, primero divide por $a(x)$, de modo que $f=g/a$. Olvidarlo introduce un factor $a(x)$ erróneo en $u_i'$.

## Resumen

> [!resumen]
> | Paso | Fórmula |
> |---|---|
> | Propuesta | $y_p=u_1y_1+u_2y_2$ |
> | Condición impuesta | $u_1'y_1+u_2'y_2=0$ |
> | Wronskiano | $W=y_1y_2'-y_2y_1'$ |
> | Derivadas | $u_1'=-\dfrac{y_2 f}{W},\quad u_2'=\dfrac{y_1 f}{W}$ |
> | Particular | $y_p=-y_1\!\int\!\tfrac{y_2 f}{W}dx+y_2\!\int\!\tfrac{y_1 f}{W}dx$ |

> [!corolario]
> Variación de parámetros es el método **general** para la no homogénea: solo necesita un conjunto fundamental de la homogénea y una integral. Su universalidad (cualquier $f$ continua, coeficientes variables) lo hace el complemento natural de [[Coeficientes Indeterminados| coeficientes indeterminados]]: este es rápido pero restringido; aquel es lento pero siempre funciona.

> [!referencia]
> - El método rápido para $f$ de "buena forma": [[Coeficientes Indeterminados]].
> - El wronskiano que aparece en las fórmulas: [[Wronskiano e Independencia Lineal]].
> - De dónde sale el conjunto fundamental: [[Coeficientes Constantes Homogenea]].
> - Vuelta al mapa del bloque: [[No Homogenea/index]].
