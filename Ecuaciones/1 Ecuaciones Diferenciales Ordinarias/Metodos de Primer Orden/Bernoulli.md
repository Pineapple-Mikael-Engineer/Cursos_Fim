---
title: Bernoulli
tags:
  - ecuaciones
  - edo
  - teoria
  - primer-orden
  - bernoulli
draft: false
aliases:
  - ecuación de Bernoulli
  - Bernoulli
  - Bernoulli equation
---

# Bernoulli

> [!definicion]
> La **ecuación de Bernoulli** es la EDO no lineal
> $$y'+p(x)\,y=q(x)\,y^{n},\qquad n\in\mathbb{R}.$$
> Es "casi lineal": coincide con una [[Lineal Primer Orden| lineal]] salvo por el factor $y^{n}$ del
> lado derecho. Si $n=0$ o $n=1$ **ya es lineal** (no hay nada que hacer). Para $n\neq0,1$ el cambio
> de variable
> $$u=y^{1-n}$$
> la transforma en una **ecuación lineal de primer orden en $u$**, que se resuelve con factor
> integrante.

> [!info]
> Séptimo tipo del [[Metodos de Primer Orden/index| catálogo de primer orden]] (libro, cap. 2.3.1). Es la primera de las
> **no lineales reducibles**: no se ataca de frente, sino que un cambio la lleva a
> [[Lineal Primer Orden| lineal]]. Comparte familia con la [[Riccati| ecuación de Riccati]] (que es
> Bernoulli cuando su término independiente $r=0$). Una vez en forma lineal, todo el peso recae en el
> [[Lineal Primer Orden| factor integrante]].

---

## Ejemplo

> [!ejemplo] Ejemplo 36 — exponente negativo
> **Resolver $y'+x\,y=x\,y^{-3}$.**
>
> **Paso 1 — identificar $n$ y el cambio.** Aquí $p=x$, $q=x$ y $n=-3$. El cambio es
> $$u=y^{1-n}=y^{1-(-3)}=y^{4},\qquad du=4y^{3}\,dy.$$
>
> **Paso 2 — preparar la ecuación.** Dividimos todo por $y^{n}=y^{-3}$ (equivalente a multiplicar por
> $y^{3}$) para que aparezca $y^{3}y'$:
> $$y^{3}y'+x\,y^{4}=x.$$
> Como $u'=4y^{3}y'$, se tiene $y^{3}y'=\tfrac14 u'$ y $y^{4}=u$, luego
> $$\tfrac14 u'+x\,u=x\ \Longrightarrow\ u'+4x\,u=4x.$$
> Esta es **lineal en $u$**.
>
> **Paso 3 — factor integrante.**
> $$\mu=e^{\int 4x\,dx}=e^{2x^{2}}.$$
>
> **Paso 4 — comprimir e integrar.** $\dfrac{d}{dx}\big(u\,e^{2x^{2}}\big)=4x\,e^{2x^{2}}$, y como
> $\displaystyle\int 4x\,e^{2x^{2}}\,dx=e^{2x^{2}}$:
> $$u\,e^{2x^{2}}=e^{2x^{2}}+c\ \Longrightarrow\ u=1+c\,e^{-2x^{2}}.$$
>
> **Paso 5 — deshacer $u=y^{4}$.**
> $$\boxed{y^{4}=1+c\,e^{-2x^{2}}}.$$

---

## En qué consiste

> [!teoria] Por qué $u=y^{1-n}$ linealiza
> El estorbo es el factor $y^{n}$ del lado derecho. La maniobra es **dividir por $y^{n}$** para
> dejar todo en términos de la combinación $y^{1-n}$, que es justo la que tiene derivada limpia:
> $$\frac{d}{dx}\,y^{1-n}=(1-n)\,y^{-n}\,y'.$$
> Tras dividir, el lado izquierdo de la ecuación contiene $y^{-n}y'$ y $y^{1-n}$, ambos expresables
> en $u=y^{1-n}$ y $u'$. El término $y^{n}$ desaparece y queda algo lineal.

> [!teorema] Bernoulli se linealiza con $u=y^{1-n}$
> Para $n\neq1$, la ecuación $y'+p\,y=q\,y^{n}$ es equivalente, bajo $u=y^{1-n}$, a la lineal
> $$u'+(1-n)\,p\,u=(1-n)\,q.$$

> [!demostracion]
> **Paso 1 — dividir por $y^{n}$.** Suponiendo $y\neq0$,
> $$y^{-n}y'+p\,y^{1-n}=q.$$
>
> **Paso 2 — introducir $u=y^{1-n}$.** Derivando, $u'=(1-n)\,y^{-n}y'$, de donde
> $y^{-n}y'=\dfrac{u'}{1-n}$. Además $y^{1-n}=u$. Sustituyendo:
> $$\frac{1}{1-n}\,u'+p\,u=q.$$
>
> **Paso 3 — limpiar.** Multiplicando por $(1-n)$:
> $$u'+(1-n)\,p\,u=(1-n)\,q,$$
> que es **lineal de primer orden en $u$**. $\blacksquare$

> [!algoritmo] Resolver una Bernoulli
> 1. **Identifica $n$** (exponente de $y$ en el lado derecho). Si $n=0$ o $1$, trátala como
>    [[Lineal Primer Orden| lineal]] directamente.
> 2. **Cambia** $u=y^{1-n}$.
> 3. **Reescribe** como la lineal $u'+(1-n)\,p\,u=(1-n)\,q$.
> 4. **Resuelve** con [[Lineal Primer Orden| factor integrante]] $\mu=e^{\int(1-n)p\,dx}$.
> 5. **Deshaz** el cambio: vuelve a $y$ mediante $y^{1-n}=u$.

> [!warning] La solución $y\equiv0$
> Al dividir por $y^{n}$ en el Paso 1 se **excluye** $y=0$. Cuando $n>0$, la función $y\equiv0$ es una
> solución de equilibrio (sustituye y comprueba) que el cambio **no recupera**; añádela aparte si el
> problema la admite, igual que las soluciones perdidas en [[Variables Separables]].

## Resumen

> [!resumen]
> | Paso | Acción |
> |---|---|
> | Forma | $y'+p\,y=q\,y^{n}$ |
> | Casos triviales | $n=0,1$ → ya es lineal |
> | Cambio | $u=y^{1-n}$, $u'=(1-n)y^{-n}y'$ |
> | Lineal resultante | $u'+(1-n)\,p\,u=(1-n)\,q$ |
> | Resolver | factor integrante $\mu=e^{\int(1-n)p\,dx}$ |
> | Cerrar | deshacer $y^{1-n}=u$; revisar $y\equiv0$ |

> [!corolario]
> Bernoulli no es un método nuevo, sino un **disfraz** de la lineal: el exponente $y^{n}$ se elimina
> con un único cambio de potencia. Reconocer $n$ y aplicar $u=y^{1-n}$ devuelve el problema a terreno
> conocido — el factor integrante.

> [!referencia]
> - Método al que reduce: [[Lineal Primer Orden]].
> - Generalización cuadrática: [[Riccati]] (Bernoulli con $r\neq0$).
> - Soluciones perdidas al dividir: [[Variables Separables]].
> - Vuelta al catálogo: [[Metodos de Primer Orden/index]].
