---
title: Riccati
tags:
  - ecuaciones
  - edo
  - teoria
  - primer-orden
  - riccati
draft: false
aliases:
  - ecuación de Riccati
  - Riccati
  - Riccati equation
---

# Riccati

> [!definicion]
> La **ecuación de Riccati** es la EDO cuadrática en $y$
> $$y'+p(x)\,y^{2}+q(x)\,y=r(x).$$
> Es la "siguiente" tras la lineal: añade un término $y^{2}$. Si $p\equiv0$ es
> [[Lineal Primer Orden| lineal]]; si $r\equiv0$ es de [[Bernoulli| Bernoulli]] (con $n=2$). En el
> caso general **no se resuelve por cuadraturas**: hay que **conocer una solución particular** $y_p$,
> y entonces el cambio
> $$y=y_p+\frac{1}{u}$$
> la convierte en una **lineal de primer orden en $u$**.

> [!info]
> Octavo y último tipo "estándar" del [[Metodos de Primer Orden/index| catálogo de primer orden]] (libro, cap. 2.3.2). Cierra
> la familia de **no lineales reducibles**: la [[Bernoulli| Bernoulli]] sale gratis ($r=0$) y la
> [[Lineal Primer Orden| lineal]] también ($p=0$). Su rasgo distintivo es que **necesita un dato
> extra** —una solución particular— porque, a diferencia de Bernoulli, ningún cambio universal la
> resuelve a ciegas.

---

## Ejemplo

> [!ejemplo] Ejemplo 37 — con solución particular conocida
> **Resolver $y'=2\tan x\sec x-y^{2}\sin x$ sabiendo que $y_p=\sec x$.**
>
> **Paso 1 — verificar y plantear el cambio.** Reordenada, es Riccati con
> $p=\sin x$, $q=0$, $r=2\tan x\sec x$. Tomamos
> $$y=\sec x+\frac1u,\qquad y'=\sec x\tan x-\frac{u'}{u^{2}}.$$
>
> **Paso 2 — sustituir.** El lado derecho usa
> $y^{2}=\sec^{2}x+\dfrac{2\sec x}{u}+\dfrac{1}{u^{2}}$, así que
> $$\sec x\tan x-\frac{u'}{u^{2}}
> =2\tan x\sec x-\Big(\sec^{2}x+\tfrac{2\sec x}{u}+\tfrac{1}{u^{2}}\Big)\sin x.$$
>
> **Paso 3 — cancelar los términos de $y_p$.** Como $y_p=\sec x$ resuelve la ecuación, los términos
> sin $u$ se anulan entre sí. Lo que sobrevive (multiplicando por $-u^{2}$ y usando
> $\sec x\sin x=\tan x$) es la **lineal**
> $$u'-2u\sec x\sin x=\sin x\ \Longrightarrow\ u'-2\tan x\,u=\sin x.$$
>
> **Paso 4 — factor integrante.** Con $\displaystyle\int(-2\tan x)\,dx=2\ln|\cos x|$:
> $$\mu=e^{-2\int\tan x\,dx}=\cos^{2}x.$$
>
> **Paso 5 — comprimir e integrar.** $\dfrac{d}{dx}\big(u\cos^{2}x\big)=\sin x\cos^{2}x$, y como
> $\displaystyle\int\sin x\cos^{2}x\,dx=-\tfrac13\cos^{3}x$:
> $$u\cos^{2}x=-\tfrac13\cos^{3}x+c\ \Longrightarrow\ u=\frac{-\cos^{3}x+3c}{3\cos^{2}x}.$$
>
> **Paso 6 — recomponer $y$.** Como $y=\sec x+1/u$,
> $$\boxed{\,y=\sec x+\frac{3\cos^{2}x}{-\cos^{3}x+3c}\,}.$$

---

## En qué consiste

> [!teoria] Por qué $y=y_p+1/u$ linealiza
> El término que rompe la linealidad es $p\,y^{2}$. Si ya **conocemos** una solución $y_p$, escribimos
> la incógnita como una **perturbación** de ella, $y=y_p+1/u$, midiendo la desviación con $1/u$. Al
> sustituir, el cuadrado $y^{2}=y_p^{2}+\tfrac{2y_p}{u}+\tfrac{1}{u^{2}}$ genera tres bloques: el de
> $y_p^{2}$ se **cancela** porque $y_p$ ya satisface la ecuación; el de $1/u^{2}$ se compensa con el
> $-u'/u^{2}$ que viene de derivar $1/u$; y queda solo el bloque en $1/u$, **lineal** en $u$.

> [!teorema] Riccati se linealiza con una solución conocida
> Si $y_p$ resuelve $y'+p\,y^{2}+q\,y=r$, el cambio $y=y_p+1/u$ la transforma en la lineal
> $$u'-\big(2p\,y_p+q\big)\,u=p.$$

> [!demostracion]
> **Paso 1 — sustituir.** Con $y=y_p+\dfrac1u$ y $y'=y_p'-\dfrac{u'}{u^{2}}$, la ecuación es
> $$y_p'-\frac{u'}{u^{2}}+p\Big(y_p+\tfrac1u\Big)^{2}+q\Big(y_p+\tfrac1u\Big)=r.$$
>
> **Paso 2 — expandir y usar que $y_p$ es solución.** Desarrollando el cuadrado y agrupando los
> términos **sin** $u$, aparece $y_p'+p\,y_p^{2}+q\,y_p-r=0$, que se anula por hipótesis. Queda
> $$-\frac{u'}{u^{2}}+\frac{2p\,y_p}{u}+\frac{p}{u^{2}}+\frac{q}{u}=0.$$
>
> **Paso 3 — multiplicar por $-u^{2}$.**
> $$u'-(2p\,y_p+q)\,u=p,$$
> ecuación **lineal de primer orden en $u$**. $\blacksquare$

> [!info] Panorama: Riccati ↔ lineal de segundo orden
> Toda Riccati equivale a una EDO **lineal de segundo orden**: el cambio $y=\dfrac{u'}{p\,u}$ la
> convierte en una ecuación lineal homogénea en $u$. Por eso la Riccati aparece de forma natural en
> óptica, teoría de control (ecuación algebraica de Riccati del regulador óptimo) y en la reducción de
> la ecuación de Schrödinger. Esta conexión con el
> [[Lineales de Orden Superior/index| segundo orden]] explica por qué, sin un dato extra, no cabe
> esperar una fórmula por cuadraturas.

> [!algoritmo] Resolver una Riccati
> 1. **Reconoce** la forma cuadrática $y'+p\,y^{2}+q\,y=r$.
> 2. **Consigue $y_p$**: dato del problema, o adivínala probando formas simples ($y_p=ax+b$,
>    $y_p=a/x$, $y_p=ae^{x}$, $\sec x$…).
> 3. **Cambia** $y=y_p+\dfrac1u$.
> 4. **Resuelve** la [[Lineal Primer Orden| lineal]] $u'-(2p\,y_p+q)\,u=p$ con factor integrante.
> 5. **Recompón** $y=y_p+\dfrac1u$.

> [!warning] Sin $y_p$ no hay método elemental
> A diferencia de [[Bernoulli]], la Riccati **no** tiene un cambio universal que la resuelva a ciegas:
> en general **no** se integra por cuadraturas. Si no se conoce ni se puede adivinar una solución
> particular $y_p$, la ecuación no tiene solución en términos elementales y hay que pasar al segundo
> orden o a métodos numéricos.

## Resumen

> [!resumen]
> | Caso | Condición | Reduce a |
> |---|---|---|
> | Lineal | $p\equiv0$ | [[Lineal Primer Orden\| lineal]] directa |
> | Bernoulli | $r\equiv0$ | [[Bernoulli\| Bernoulli]] con $n=2$ |
> | General | se conoce $y_p$ | lineal vía $y=y_p+1/u$ |
> | General | sin $y_p$ | segundo orden / numérico |

> [!corolario]
> La Riccati marca el **límite** de los métodos elementales de primer orden: es resoluble solo si se
> conoce una solución particular, que entonces se "promueve" a solución general resolviendo una lineal
> en $u$. Es el puente natural hacia la teoría de **segundo orden**.

> [!referencia]
> - Método al que reduce: [[Lineal Primer Orden]].
> - Caso particular $r=0$: [[Bernoulli]].
> - Linealización a segundo orden: [[Lineales de Orden Superior/index]].
> - Vuelta al catálogo: [[Metodos de Primer Orden/index]].
