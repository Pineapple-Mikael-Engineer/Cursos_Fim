---
title: Lineal Primer Orden
tags:
  - ecuaciones
  - edo
  - teoria
  - primer-orden
  - lineal
draft: false
aliases:
  - lineal de primer orden
  - ecuación lineal de primer orden
  - factor integrante lineal
  - first order linear ODE
---

# Lineal Primer Orden

> [!definicion]
> Una EDO es **lineal de primer orden** si la incógnita $x$ y su derivada $\dot x$ aparecen **a la
> potencia 1** (sin productos $x\dot x$, sin $x^2$, sin $\sin x$…), de modo que puede escribirse en la
> **forma estándar**
> $$\dot x+p(t)\,x=q(t).$$
> El lado izquierdo $\dot x+p(t)x$ es **el sistema** (su dinámica interna); el lado derecho $q(t)$ es
> el **input** o **fuente** que lo excita. Se resuelve multiplicando toda la ecuación por el
> **factor integrante**
> $$\mu(t)=e^{\int p(t)\,dt},$$
> que convierte el lado izquierdo en la derivada de un producto y permite **integrar directamente**.

> [!info]
> Método **estrella** del [[index | catálogo de primer orden]] (libro, cap. 2.1.1) y el más
> reutilizado de toda la teoría. Su factor integrante reaparece al resolver [[Bernoulli]] y
> [[Riccati]] (que se reducen a esta forma) y en las
> [[../Lineales de Orden Superior/index | lineales de orden superior]]. Cuando $q\equiv0$ la ecuación
> es además [[Variables Separables | separable]], lo que sirve de puente conceptual. La técnica
> general de "multiplicar por $\mu$ para fabricar un diferencial total" es la misma del
> [[Factor Integrante]] para ecuaciones inexactas.

---

## Ejemplo

> [!ejemplo] Ejemplo 12 — homogénea, lectura directa
> **Resolver $\dot x-2t\,x=0$.** Está en forma estándar con $p(t)=-2t$ y $q(t)=0$. El factor
> integrante es
> $$\mu=e^{\int(-2t)\,dt}=e^{-t^{2}}.$$
> Multiplicando, el lado izquierdo se vuelve $\dfrac{d}{dt}\!\big(x\,e^{-t^{2}}\big)=0$, luego
> $x\,e^{-t^{2}}=C$ y por tanto
> $$\boxed{x=C\,e^{t^{2}}}.$$
> (Al ser $q=0$, se podría haber separado $\dfrac{dx}{x}=2t\,dt$ y obtener lo mismo.)

> [!ejemplo] Ejemplo 13 — PVI, fijar la constante
> **Resolver $y'+\dfrac{3}{x}\,y=0$ con $y(1)=1$.** Aquí $p=3/x$, $q=0$ y
> $$\mu=e^{\int 3/x\,dx}=e^{3\ln|x|}=x^{3}.$$
> Entonces $\dfrac{d}{dx}(y\,x^{3})=0\Rightarrow y\,x^{3}=C\Rightarrow y=Cx^{-3}$. Imponiendo
> $y(1)=1$ se obtiene $C=1$, de modo que
> $$\boxed{y=\frac{1}{x^{3}}}.$$

> [!ejemplo] Ejemplo 14 — llevar a forma estándar e integrar por partes
> **Resolver $t\,\dfrac{dx}{dt}-4x=t^{6}e^{t}$.**
>
> **Paso 1 — forma estándar.** Dividimos entre $t$ para dejar el coeficiente de $\dot x$ igual a $1$:
> $$\frac{dx}{dt}-\frac{4}{t}\,x=t^{5}e^{t},\qquad p=-\frac4t,\quad q=t^{5}e^{t}.$$
>
> **Paso 2 — factor integrante.**
> $$\mu=e^{-4\int dt/t}=e^{-4\ln|t|}=t^{-4}.$$
>
> **Paso 3 — comprimir el lado izquierdo.** Multiplicando por $t^{-4}$,
> $$\frac{d}{dt}\!\big(x\,t^{-4}\big)=t^{-4}\cdot t^{5}e^{t}=t\,e^{t}.$$
>
> **Paso 4 — integrar (por partes).** Con $\displaystyle\int t\,e^{t}\,dt=t\,e^{t}-e^{t}$:
> $$x\,t^{-4}=t\,e^{t}-e^{t}+c.$$
>
> **Paso 5 — despejar.** Multiplicando por $t^{4}$:
> $$\boxed{x=t^{5}e^{t}-t^{4}e^{t}+c\,t^{4}}.$$
> Nótese que esta solución es **válida incluso en $t=0$** (no quedan denominadores), aunque la forma
> estándar dividía por $t$: la división se "deshizo" al final.

> [!ejemplo] Ejemplo 15 — lineal en $x$, no en $y$
> **Resolver $\dfrac{dy}{dx}=\dfrac{1}{x+y^{2}}$.** En $y$ **no** es lineal (aparece $y^{2}$). Pero
> **invirtiendo** la derivada y mirando $x$ como función de $y$:
> $$\frac{dx}{dy}=x+y^{2}\ \Longrightarrow\ \frac{dx}{dy}-x=y^{2},$$
> que **sí** es lineal en $x$, con $p=-1$ y $q=y^{2}$ (variable independiente $y$).
>
> **Paso 1 — factor integrante.** $\mu=e^{\int(-1)\,dy}=e^{-y}$.
>
> **Paso 2 — comprimir.** $\dfrac{d}{dy}\big(x\,e^{-y}\big)=e^{-y}y^{2}$.
>
> **Paso 3 — integrar dos veces por partes.**
> $\displaystyle\int e^{-y}y^{2}\,dy=-e^{-y}(y^{2}+2y+2)$, luego
> $$x\,e^{-y}=-e^{-y}(y^{2}+2y+2)+c.$$
>
> **Paso 4 — despejar.**
> $$\boxed{x=-y^{2}-2y-2+c\,e^{y}}.$$

> [!ejemplo] Ejemplo 40 — aplicación: mezcla en un tanque
> **Un tanque de capacidad $100$ L contiene $10$ kg de sal disueltos en $60$ L de agua. Entra
> salmuera a $5$ L/min con concentración $0{,}1$ kg/L; la mezcla, bien agitada, sale a $3$ L/min.
> ¿Cuánta sal hay cuando el tanque se llena?**
>
> **Paso 1 — volumen y balance de masa.** El volumen crece $5-3=2$ L/min, así que
> $V(t)=60+2t$. Llamando $m(t)$ a la masa de sal,
> $$\dot m=\underbrace{(0{,}1)(5)}_{\text{entra}}-\underbrace{\frac{m}{V}\cdot 3}_{\text{sale}}
> =0{,}5-\frac{3m}{60+2t}.$$
>
> **Paso 2 — forma estándar (lineal en $m$).**
> $$\dot m+\frac{3}{60+2t}\,m=0{,}5.$$
>
> **Paso 3 — factor integrante.** Con $\displaystyle\int\frac{3\,dt}{60+2t}=\frac32\ln(60+2t)$:
> $$\mu=e^{\frac32\ln(60+2t)}=(60+2t)^{3/2}.$$
>
> **Paso 4 — integrar.** $\dfrac{d}{dt}\big[m(60+2t)^{3/2}\big]=0{,}5\,(60+2t)^{3/2}$, y con
> $\displaystyle\int 0{,}5\,(60+2t)^{3/2}\,dt=\frac{1}{10}(60+2t)^{5/2}$:
> $$m(60+2t)^{3/2}=\frac{1}{10}(60+2t)^{5/2}+c
> \ \Longrightarrow\ m(t)=\frac{60+2t}{10}+c\,(60+2t)^{-3/2}.$$
>
> **Paso 5 — condición inicial y respuesta.** Con $m(0)=10$ y $V(0)=60$:
> $10=6+c\,60^{-3/2}\Rightarrow c=4\cdot 60^{3/2}$. El tanque se llena cuando $V=100$, es decir
> $60+2t=100\Rightarrow t=20$ min. Sustituyendo,
> $$m(20)=\frac{100}{10}+4\cdot 60^{3/2}\cdot 100^{-3/2}=10+4\left(\frac{60}{100}\right)^{3/2}
> \approx 10+4(0{,}6)^{1{,}5}\approx \boxed{11{,}86\ \text{kg}}.$$

---

## En qué consiste

> [!teoria] La idea: fabricar la derivada de un producto
> El truco entero descansa en una observación de la **regla del producto**. Para cualquier
> antiderivada $\int p\,dt$,
> $$\frac{d}{dt}\Big(x\,e^{\int p\,dt}\Big)
> =e^{\int p\,dt}\,\dot x+x\,e^{\int p\,dt}\,p
> =e^{\int p\,dt}\big(\dot x+p\,x\big).$$
> ¡El paréntesis final es exactamente el lado izquierdo de la ecuación! Por eso, si **multiplicamos**
> $\dot x+p\,x=q$ por $\mu=e^{\int p\,dt}$, el lado izquierdo se **colapsa** en una sola derivada:
> $$\frac{d}{dt}\big(x\,\mu\big)=\mu\,q.$$
> Esto ya es **integrable de golpe**: $x\,\mu=\int\mu\,q\,dt+c$, de donde
> $$x=e^{-\int p\,dt}\left(\int e^{\int p\,dt}\,q\,dt+c\right).$$
> En el caso **homogéneo** $q=0$ queda $x=C\,e^{-\int p\,dt}$, que también sale de
> [[Variables Separables | separar]] $\dfrac{dx}{x}=-p\,dt$.

> [!info] Principio de superposición
> Como el operador $L[x]=\dot x+p\,x$ es **lineal** ($L[c_1x_1+c_2x_2]=c_1L[x_1]+c_2L[x_2]$), las
> soluciones de la homogénea $\dot x+p\,x=0$ forman un espacio vectorial: si $x_1,x_2$ la resuelven,
> toda combinación $c_1x_1+c_2x_2$ también. En consecuencia, la **solución general** se escribe como
> $$x=x_h+x_p,$$
> una solución particular $x_p$ de la completa más la solución general $x_h=C\,e^{-\int p\,dt}$ de la
> homogénea. Esta estructura es la que se generaliza a las
> [[../Lineales de Orden Superior/index | lineales de orden superior]].

> [!algoritmo] Resolver una lineal de primer orden
> 1. **Forma estándar.** Reescribe como $\dot x+p(t)\,x=q(t)$ (coeficiente de $\dot x$ igual a $1$).
> 2. **Factor integrante.** Calcula $\mu=e^{\int p\,dt}$ (sin constante de integración).
> 3. **Comprimir.** Reconoce que el lado izquierdo, tras multiplicar por $\mu$, es
>    $\dfrac{d}{dt}(\mu\,x)$.
> 4. **Integrar.** $\mu\,x=\displaystyle\int\mu\,q\,dt+c$.
> 5. **Despejar.** $x=\dfrac{1}{\mu}\left(\displaystyle\int\mu\,q\,dt+c\right)$; impón la condición
>    inicial si la hay.

> [!teorema] Existencia, unicidad y fórmula cerrada
> Si $p,q$ son continuas en un intervalo $I$ que contiene a $t_0$, el PVI
> $\dot x+p\,x=q,\ x(t_0)=x_0$ tiene **solución única** en todo $I$, dada por
> $$x(t)=e^{-\int_{t_0}^{t}p}\left(x_0+\int_{t_0}^{t}e^{\int_{t_0}^{s}p}\,q(s)\,ds\right).$$

> [!demostracion]
> **Paso 1 — el factor integrante nunca se anula.** Como $\mu=e^{\int p}$ es una exponencial,
> $\mu(t)>0$ para todo $t\in I$; por tanto multiplicar por $\mu$ es una operación **reversible** y no
> introduce ni pierde soluciones.
>
> **Paso 2 — la ecuación se vuelve exacta.** Por la regla del producto,
> $\mu(\dot x+p\,x)=\dfrac{d}{dt}(\mu\,x)$, luego la ecuación equivale a
> $\dfrac{d}{dt}(\mu\,x)=\mu\,q$.
>
> **Paso 3 — integrar entre $t_0$ y $t$.**
> $$\mu(t)\,x(t)-\mu(t_0)\,x_0=\int_{t_0}^{t}\mu(s)\,q(s)\,ds.$$
> Tomando $\mu(t)=e^{\int_{t_0}^{t}p}$ (de modo que $\mu(t_0)=1$) y dividiendo por $\mu(t)$ se obtiene
> la fórmula. Es **única** porque cada paso fue una equivalencia. $\blacksquare$

> [!warning] ¿Lineal en $x$ aunque no en $y$?
> Una ecuación puede **no** ser lineal en $y$ pero **sí** serlo si intercambias los papeles y miras
> $x=x(y)$ (Ejemplo 15). Ante un $y^{2}$, $\sqrt{y}$, $e^{y}$… que estorba, **invierte la derivada**
> $\dfrac{dy}{dx}\to\dfrac{dx}{dy}$ y revisa si quedó lineal en $x$ antes de descartar el método.

## Resumen

> [!resumen]
> | Paso | Acción |
> |---|---|
> | Reconocer | $\dot x$ y $x$ a la potencia 1 → forma estándar $\dot x+p\,x=q$ |
> | Factor | $\mu=e^{\int p\,dt}$ (siempre $>0$) |
> | Comprimir | lado izq. $=\dfrac{d}{dt}(\mu\,x)$ |
> | Integrar | $\mu\,x=\int\mu\,q\,dt+c$ |
> | Despejar | $x=\dfrac{1}{\mu}\left(\int\mu\,q\,dt+c\right)$ |
> | General | $x=x_h+x_p$ (superposición) |

> [!corolario]
> La lineal es el método **más robusto** de primer orden: su factor integrante $e^{\int p}$ **siempre
> existe** y da una fórmula cerrada, a diferencia de los métodos que dependen de adivinar un cambio.
> Por eso la estrategia frente a una no lineal ([[Bernoulli]], [[Riccati]]) es **transformarla** en
> una lineal y caer en esta nota.

> [!referencia]
> - Generaliza la técnica de $\mu$: [[Factor Integrante]] (para ecuaciones inexactas).
> - No lineales que reducen a esta: [[Bernoulli]], [[Riccati]].
> - Caso homogéneo como separable: [[Variables Separables]].
> - Estructura $x_h+x_p$ en dimensión mayor: [[../Lineales de Orden Superior/index]].
> - Vuelta al catálogo: [[index]].
