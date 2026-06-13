---
title: Ecuaciones Homogeneas
tags:
  - ecuaciones
  - edo
  - teoria
  - primer-orden
  - homogeneas
draft: false
aliases:
  - ecuaciones homogéneas
  - homogénea grado cero
  - homogeneous equation
  - sustitución y=ux
---

# Ecuaciones Homogeneas

> [!definicion]
> Una función $f(x,y)$ es **homogénea de grado $n$** si al escalar ambos argumentos por el mismo
> factor $\lambda$ la función se reescala por $\lambda^n$:
> $$f(\lambda x,\lambda y)=\lambda^{n}\,f(x,y).$$
> Una EDO $y'=f(x,y)$ es **homogénea** cuando $f$ es homogénea de **grado cero**. Esto equivale a que
> $f$ dependa **solo del cociente** $y/x$:
> $$f(x,y)=g\!\left(\frac{y}{x}\right).$$
> Se resuelve con la sustitución $y=ux$ (con $u=y/x$), que la convierte en una ecuación de
> [[Variables Separables| variables separables]].

> [!info]
> Segundo tipo del [[Metodos de Primer Orden/index| catálogo de primer orden]] (libro, cap. 1.3.1). Es el primer ejemplo de
> **reducción por cambio de variable**: no se integra directamente, sino que un sustituto la lleva a
> [[Variables Separables| separable]]. Los [[Coeficientes Lineales| coeficientes lineales]] no
> paralelos se reducen, a su vez, a una homogénea. Para visualizar las curvas solución apóyate en el
> [[Campo de Direcciones e Isoclinas| campo de direcciones]]
> (de hecho, en una homogénea las isoclinas son **rectas por el origen** $y/x=\text{cte}$).

---

## Ejemplo

> [!ejemplo] Ejemplo 1 — solución implícita con $\arctan$
> **Resolver $y'=\dfrac{x+y}{x-y}$.**
>
> **Paso 1 — verificar homogeneidad de grado 0.** Sustituyendo $x\to\lambda x,\ y\to\lambda y$:
> $$\frac{\lambda x+\lambda y}{\lambda x-\lambda y}=\frac{\lambda(x+y)}{\lambda(x-y)}=\frac{x+y}{x-y},$$
> el $\lambda$ se cancela ($\lambda^0$): es homogénea. Dividiendo numerador y denominador por $x$,
> $$f(x,y)=\frac{1+y/x}{1-y/x}=g\!\left(\frac{y}{x}\right).$$
> (Notar que $f$ se **indefine sobre la recta** $x=y$, donde $u=1$.)
>
> **Paso 2 — sustituir $y=ux$.** Entonces $y'=u'x+u$, y la ecuación queda
> $$u'x+u=\frac{1+u}{1-u}.$$
>
> **Paso 3 — despejar y separar.** Pasamos $u$ al lado derecho:
> $$u'x=\frac{1+u}{1-u}-u=\frac{1+u-u(1-u)}{1-u}=\frac{1+u^{2}}{1-u}.$$
> Separando variables,
> $$\frac{1-u}{1+u^{2}}\,du=\frac{dx}{x}.$$
>
> **Paso 4 — integrar.** El lado izquierdo se parte en dos integrales conocidas:
> $$\int\frac{du}{1+u^{2}}-\int\frac{u\,du}{1+u^{2}}=\arctan u-\tfrac12\ln(u^{2}+1),$$
> de modo que
> $$\arctan u-\tfrac12\ln(u^{2}+1)=\ln|x|+C.$$
>
> **Paso 5 — deshacer $u=y/x$.** Sustituyendo de vuelta,
> $$\boxed{\ \arctan\!\frac{y}{x}-\tfrac12\ln\!\left(\frac{y^{2}}{x^{2}}+1\right)=\ln|x|+C\ }$$
> Es una solución **implícita**: define $y(x)$ aunque no se pueda despejar en forma elemental.

> [!ejemplo] Ejemplo 2 — PVI con solución explícita
> **Resolver el problema de valor inicial $x^{2}y'=y^{2}+xy,\ \ y(1)=1$.**
>
> **Paso 1 — forma normal y homogeneidad.** Cerca de $x=1$ podemos dividir por $x^{2}$:
> $$y'=\frac{y^{2}+xy}{x^{2}}=\left(\frac{y}{x}\right)^{2}+\frac{y}{x},$$
> que depende solo de $y/x$: es homogénea de grado 0.
>
> **Paso 2 — sustituir $y=ux$, $y'=u'x+u$:**
> $$u'x+u=u^{2}+u\ \Longrightarrow\ u'x=u^{2}.$$
>
> **Paso 3 — separar e integrar:**
> $$\frac{du}{u^{2}}=\frac{dx}{x}\ \Longrightarrow\ -\frac1u=\ln x+C\ \Longrightarrow\ u=-\frac{1}{\ln x+C}.$$
>
> **Paso 4 — deshacer $u=y/x$:**
> $$y=ux=-\frac{x}{\ln x+C}.$$
>
> **Paso 5 — imponer $y(1)=1$.** Como $\ln 1=0$:
> $$1=-\frac{1}{0+C}\ \Longrightarrow\ C=-1.$$
> La solución del PVI es
> $$\boxed{\ y=-\dfrac{x}{\ln x-1}\ }$$
> definida mientras $\ln x\neq 1$ (es decir $x\neq e$), entorno que contiene $x=1$.

---

## En qué consiste

> [!teoria]
> ¿Por qué grado cero significa "depende solo de $y/x$"? Porque la homogeneidad de grado $0$,
> $f(\lambda x,\lambda y)=f(x,y)$, vale para **todo** $\lambda$; en particular para $\lambda=1/x$:
> $$f(x,y)=f\!\left(x\cdot\tfrac1x,\ y\cdot\tfrac1x\right)=f\!\left(1,\tfrac{y}{x}\right)=:g\!\left(\tfrac{y}{x}\right).$$
> Toda la información de $f$ está en la **dirección** $y/x$, no en la escala. Por eso el cambio
> natural es $u=y/x$, que captura esa única variable relevante. Con $y=ux$ se tiene
> $y'=u'x+u$ y la ecuación se vuelve
> $$u'x+u=g(u)\ \Longrightarrow\ \frac{du}{g(u)-u}=\frac{dx}{x},$$
> que es **separable**. El término $u$ que sobra ($y'=u'x+u$, no $u'x$ a secas) es justo lo que
> permite que el $g(u)-u$ del denominador "absorba" la no linealidad.
>
> *Ejemplos de grados de homogeneidad:* la presión de un gas ideal $P=NkT/V$ es homogénea de
> **grado 0** en las variables extensivas $(N,V)$ (al duplicar gas y volumen, $P$ no cambia); la
> distancia $\sqrt{x^{2}+y^{2}}$ es de **grado 1** ($\lambda^{1}$); el área $xy$ es de **grado 2**.

> [!teorema] El cambio $y=ux$ vuelve separable toda homogénea de grado 0
> Si $f$ es homogénea de grado cero, la sustitución $y=ux$ transforma $y'=f(x,y)$ en una ecuación de
> **variables separables** en $u$ y $x$.

> [!demostracion]
> **Paso 1 — reducir $f$ a una función de $u$.** Por homogeneidad de grado $0$, con $\lambda=1/x$
> ($x>0$), $f(x,y)=f\!\left(1,\tfrac{y}{x}\right)=g(u)$ donde $u=\dfrac{y}{x}$.
>
> **Paso 2 — derivar el cambio.** De $y=ux$, con $u=u(x)$, la regla del producto da $y'=u'x+u$.
>
> **Paso 3 — sustituir en la EDO.** $y'=f(x,y)=g(u)$ se convierte en
> $$u'x+u=g(u)\ \Longrightarrow\ u'x=g(u)-u.$$
>
> **Paso 4 — separar.** Donde $g(u)\neq u$,
> $$\frac{du}{g(u)-u}=\frac{dx}{x},$$
> con $u$ a la izquierda y $x$ a la derecha: es **separable**. Integrando se obtiene $u(x)$ y, al
> deshacer $u=y/x$, la solución. Las raíces de $g(u)=u$ dan **rectas solución** $y=u_0x$ (las
> soluciones de equilibrio del cambio). $\blacksquare$

> [!algoritmo] Resolver una homogénea
> 1. **Verifica** que $f$ es homogénea de grado 0: comprueba $f(\lambda x,\lambda y)=f(x,y)$, o
>    reescribe $f$ en función de $y/x$.
> 2. **Sustituye** $y=ux$, de modo que $y'=u'x+u$.
> 3. La ecuación pasa a $u'x+u=g(u)$; **resuelve la separable** $\dfrac{du}{g(u)-u}=\dfrac{dx}{x}$.
> 4. **Deshaz** el cambio con $u=y/x$ para volver a $x,y$.

> [!warning] Cambio inverso y rectas singulares
> A veces $g(u)-u$ resulta más simple si se usa el cambio **inverso** $x=uy$ (con $u=x/y$),
> separando en $y$; conviene cuando $f$ se expresa más fácil como función de $x/y$. Además, vigila
> las **rectas donde $f$ se indefine** (en el Ejemplo 1, $x=y$): no son curvas solución obtenidas por
> integración, sino fronteras del dominio donde la EDO deja de estar definida.

## Resumen

> [!resumen]
> | Paso | Acción |
> |---|---|
> | Reconocer | $f(\lambda x,\lambda y)=f(x,y)$, o $f=g(y/x)$ |
> | Sustituir | $y=ux,\ \ y'=u'x+u$ |
> | Separar | $\dfrac{du}{g(u)-u}=\dfrac{dx}{x}$ |
> | Cerrar | integrar y deshacer $u=y/x$; fijar $C$ con la condición inicial |

> [!corolario]
> Una homogénea no se resuelve "de frente": se **reconoce la simetría de escala** ($f$ solo ve la
> dirección $y/x$) y un único cambio $y=ux$ la deposita en el caso ya resuelto de
> [[Variables Separables| variables separables]]. Es el patrón que se repite en casi todo el
> capítulo: *cambio de variable* $\to$ *separable* $\to$ *dos integrales*.

> [!referencia]
> - Destino del método: [[Variables Separables]].
> - Generalización que se reduce a esta: [[Coeficientes Lineales]] (caso de rectas no paralelas).
> - Geometría (isoclinas rectas por el origen): [[Campo de Direcciones e Isoclinas]].
> - Vuelta al catálogo: [[Metodos de Primer Orden/index]].
