---
title: Cauchy-Euler
tags:
  - ecuaciones
  - edo
  - teoria
  - lineales
  - cauchy-euler
draft: false
aliases:
  - ecuación de Cauchy-Euler
  - ecuación equidimensional
  - ecuación de Euler
  - Cauchy-Euler equation
  - equidimensional equation
---

# Ecuación de Cauchy-Euler

> [!definicion]
> La **ecuación de Cauchy-Euler** (o **equidimensional**) de segundo orden es
> $$x^2y''+a\,xy'+b\,y=0,$$
> y su versión de orden $n$ es análoga (cada $y^{(k)}$ acompañado de $x^k$). Tiene **coeficientes
> variables**, pero se resuelve por álgebra: se prueba $y=x^m$ y resulta la **ecuación auxiliar**
> $$m(m-1)+a\,m+b=0.$$
> De forma equivalente, el cambio $x=e^{t}$ (es decir $t=\ln x$) la transforma en una EDO de
> **coeficientes constantes**, conectándola con [[Coeficientes Constantes Homogenea]].

> [!info]
> Caso especial de coeficientes **variables** del bloque
> [[Lineales de Orden Superior/index| lineales de orden superior]] que aun así se resuelve en forma
> cerrada. Comparte los **tres casos de raíces** con [[Coeficientes Constantes Homogenea| coeficientes constantes]] (el cambio $x=e^t$ explica por qué), y su caso de raíz repetida —el $\ln x$— se justifica
> con [[Reduccion de Orden| reducción de orden]].

---

## Ejemplo

> [!ejemplo] (a) Raíces reales distintas
> **Resolver $x^2y''-2xy'+2y=0$.** Comparando con $x^2y''+axy'+by=0$: $a=-2,\ b=2$. Ecuación auxiliar:
> $$m(m-1)-2m+2=m^2-3m+2=(m-1)(m-2)=0\;\Rightarrow\;m=1,\,2.$$
> Cada raíz aporta $x^m$:
> $$\boxed{\,y=c_1x+c_2x^2\,}\qquad(x>0).$$

> [!ejemplo] (b) Raíces complejas → oscilación en $\ln x$
> **Resolver $x^2y''+xy'+y=0$.** Aquí $a=1,\ b=1$. Auxiliar:
> $$m(m-1)+m+1=m^2+1=0\;\Rightarrow\;m=\pm i\quad(\alpha=0,\ \beta=1).$$
> El par complejo $\alpha\pm i\beta$ aporta $x^\alpha\cos(\beta\ln x)$ y $x^\alpha\operatorname{sen}(\beta\ln x)$:
> $$\boxed{\,y=c_1\cos(\ln x)+c_2\operatorname{sen}(\ln x)\,}\qquad(x>0).$$
> La oscilación no es en $x$ sino en $\ln x$: es lo que predice $x=e^t$, pues en la variable $t$ habría
> $\cos t,\operatorname{sen}t$ y $t=\ln x$.

> [!ejemplo] (c) Raíz repetida → aparece $\ln x$
> **Resolver $x^2y''-xy'+y=0$.** Aquí $a=-1,\ b=1$. Auxiliar:
> $$m(m-1)-m+1=m^2-2m+1=(m-1)^2=0\;\Rightarrow\;m=1\ \text{(doble)}.$$
> Una solución es $x^1$; la segunda gana un factor $\ln x$ (el análogo del factor $x$ de coeficientes
> constantes):
> $$\boxed{\,y=(c_1+c_2\ln x)\,x\,}\qquad(x>0).$$
> Que la segunda solución sea $x\ln x$ se comprueba con [[Reduccion de Orden| reducción de orden]].

---

## En qué consiste

> [!teoria] Dos lentes para la misma ecuación
> Cauchy-Euler se puede mirar de dos modos equivalentes:
> - **Probar $y=x^m$.** Como $x^k\dfrac{d^k}{dx^k}x^m=m(m-1)\cdots(m-k+1)\,x^m$, cada término
>   $x^ky^{(k)}$ devuelve un múltiplo de $x^m$; la EDO colapsa a un **polinomio en $m$** (la auxiliar).
>   Esto funciona porque la ecuación es **equidimensional**: subir una derivada (que baja una potencia de
>   $x$) se compensa exactamente con el $x^k$ delante, de modo que $x^m$ se reproduce.
> - **Cambiar $x=e^{t}$.** Lleva la ecuación a **coeficientes constantes** en $t$. Esta lente explica por
>   qué los tres casos de raíces (reales, complejas, repetida) y sus soluciones son los **mismos** que en
>   [[Coeficientes Constantes Homogenea]], solo que con $x^m$ en lugar de $e^{rx}$ y $\ln x$ en lugar de $x$.

> [!teorema] Reducción a coeficientes constantes vía $x=e^{t}$
> Con $t=\ln x$ (para $x>0$), la ecuación $x^2y''+axy'+by=0$ se transforma en la EDO de **coeficientes
> constantes**
> $$\ddot y+(a-1)\dot y+b\,y=0,\qquad \dot{}\;=\;\frac{d}{dt},$$
> cuyas raíces de $m^2+(a-1)m+b=0$ son las mismas que las de la ecuación auxiliar $m(m-1)+am+b=0$.

> [!demostracion] El cambio de variable $x=e^{t}$
> **Paso 1 — la regla de la cadena.** Con $t=\ln x$ se tiene $\dfrac{dt}{dx}=\dfrac1x$, luego
> $$\frac{d}{dx}=\frac{dt}{dx}\frac{d}{dt}=\frac1x\frac{d}{dt}\;\Rightarrow\;x\,y'=\dot y.$$
> Así el término $xy'$ se vuelve simplemente $\dot y$.
>
> **Paso 2 — la segunda derivada.** Derivando $y'=\dfrac1x\dot y$ respecto de $x$:
> $$y''=\frac{d}{dx}\!\left(\frac1x\dot y\right)=-\frac1{x^2}\dot y+\frac1x\frac{d\dot y}{dx}
> =-\frac1{x^2}\dot y+\frac1{x^2}\ddot y=\frac{1}{x^2}\big(\ddot y-\dot y\big).$$
> Por tanto $x^2y''=\ddot y-\dot y$.
>
> **Paso 3 — sustituir en la EDO.** Reemplazando $x^2y''=\ddot y-\dot y$ y $xy'=\dot y$:
> $$(\ddot y-\dot y)+a\,\dot y+b\,y=0\;\Longrightarrow\;\ddot y+(a-1)\dot y+b\,y=0,$$
> que es de **coeficientes constantes**. Su característica $m^2+(a-1)m+b=0$ es idéntica a
> $m(m-1)+am+b=0$.
>
> **Paso 4 — deshacer el cambio.** Se resuelve en $t$ y se sustituye $t=\ln x$. Las soluciones $e^{mt}$
> pasan a $x^m$; un factor $t$ (raíz repetida) pasa a $\ln x$; y $\cos\beta t,\operatorname{sen}\beta t$
> (raíz compleja) pasan a $\cos(\beta\ln x),\operatorname{sen}(\beta\ln x)$. Esto reproduce exactamente
> los tres casos de abajo. $\blacksquare$

> [!proposicion] Los tres casos de raíces de Cauchy-Euler
> Según las raíces $m$ de la ecuación auxiliar:
> 
> | Raíces $m$ | Solución general ($x>0$) |
> |:--|:--|
> | reales distintas $m_1\neq m_2$ | $c_1x^{m_1}+c_2x^{m_2}$ |
> | complejas $m=\alpha\pm i\beta$ | $x^{\alpha}\big(c_1\cos(\beta\ln x)+c_2\operatorname{sen}(\beta\ln x)\big)$ |
> | repetida $m$ | $(c_1+c_2\ln x)\,x^{m}$ |

> [!warning] Validez en $x>0$
> El cambio $t=\ln x$ y las soluciones con $\ln x$ exigen $x>0$. Para $x<0$ se reemplaza $x$ por $|x|$
> (por ejemplo $\ln|x|$, $|x|^{m}$); el punto $x=0$ es **singular** y no pertenece a ningún intervalo de
> solución.

> [!algoritmo] Resolver una Cauchy-Euler
> 1. Reconócela: cada $y^{(k)}$ multiplicado por $x^{k}$, coeficientes constantes $a,b$.
> 2. Escribe la **ecuación auxiliar** $m(m-1)+am+b=0$ (o usa directamente $x=e^{t}$).
> 3. **Halla las raíces** $m$ con su multiplicidad.
> 4. Aplica el caso (reales / complejas / repetida) con $x^m$, $\cos(\beta\ln x)$, $\ln x$ según corresponda.
> 5. Recuerda restringir a $x>0$ (o usar $|x|$).

## Resumen

> [!resumen]
> | Elemento | Expresión |
> |---|---|
> | Forma | $x^2y''+axy'+by=0$ (equidimensional) |
> | Ansatz | $y=x^m$ |
> | Ecuación auxiliar | $m(m-1)+am+b=0$ |
> | Cambio equivalente | $x=e^{t}$ → $\ddot y+(a-1)\dot y+by=0$ (coef. constantes) |
> | reales distintas | $c_1x^{m_1}+c_2x^{m_2}$ |
> | complejas $\alpha\pm i\beta$ | $x^{\alpha}(c_1\cos(\beta\ln x)+c_2\operatorname{sen}(\beta\ln x))$ |
> | repetida $m$ | $(c_1+c_2\ln x)x^{m}$ |

> [!corolario]
> Cauchy-Euler es el puente entre coeficientes variables y constantes: aunque sus coeficientes dependen
> de $x$, el cambio $x=e^{t}$ la vuelve **constante**. Por eso hereda íntegra la estructura de
> [[Coeficientes Constantes Homogenea]] —tres casos de raíces— con el diccionario $e^{rx}\to x^m$,
> $x\to\ln x$, $\cos\beta x\to\cos(\beta\ln x)$.

> [!referencia]
> - El caso constante del que hereda los tres regímenes: [[Coeficientes Constantes Homogenea]].
> - Justificación del $\ln x$ en la raíz repetida: [[Reduccion de Orden]].
> - El bloque completo: [[Lineales de Orden Superior/index]].
