---
title: Integrales de Euler
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - volterra
  - euler
draft: false
aliases:
  - integrales de Euler
  - función Gamma
  - función Beta
  - Euler integrals
---

# Integrales de Euler

> [!definicion]
> Las **integrales de Euler** son dos funciones especiales que generalizan el factorial y normalizan
> los núcleos potencia. La **función Gamma** (integral de Euler de segunda especie),
> $$\Gamma(z)=\int_0^\infty t^{z-1}e^{-t}\,dt,\qquad \Gamma(n)=(n-1)!,$$
> y la **función Beta** (integral de Euler de primera especie),
> $$B(p,q)=\int_0^1 t^{p-1}(1-t)^{q-1}\,dt=\frac{\Gamma(p)\,\Gamma(q)}{\Gamma(p+q)}.$$

> [!info]
> Herramienta auxiliar de la sección [[Volterra/index| Volterra]] del [[3 Ecuaciones Integrales/index| capítulo de ecuaciones integrales]]. Aparecen al convolucionar **núcleos potencia**, lo que sustenta
> el [[Problema de Abel| problema de Abel]], las [[Ecuaciones de Convolucion| ecuaciones de convolución]] y la integral fraccionaria de [[Calculo Fraccionario/index| Riemann-Liouville]]. Fuente:
> Krasnov, *Ecuaciones integrales*, apéndice.

---

## Ejemplo

> [!ejemplo] La convolución de dos potencias
> Queremos calcular $\displaystyle\int_0^x (x-t)^{a-1}\,t^{b-1}\,dt$, con $a,b>0$. Es la convolución de
> los núcleos $t^{a-1}$ y $t^{b-1}$, omnipresente en Volterra.
>
> **Paso 1 — cambio de variable.** Ponemos $t=x\,u$, con $u\in[0,1]$ y $dt=x\,du$. Entonces
> $x-t=x(1-u)$ y
> $$\int_0^x (x-t)^{a-1}t^{b-1}\,dt=\int_0^1 \big(x(1-u)\big)^{a-1}(x u)^{b-1}\,x\,du.$$
>
> **Paso 2 — factorizar las potencias de $x$.** Sacando $x^{a-1}\,x^{b-1}\,x=x^{a+b-1}$,
> $$=x^{a+b-1}\int_0^1 (1-u)^{a-1}u^{b-1}\,du = x^{a+b-1}\,B(b,a).$$
>
> **Paso 3 — usar la simetría.** Como $B(b,a)=B(a,b)$, concluimos
> $$\boxed{\ \int_0^x (x-t)^{a-1}t^{b-1}\,dt = B(a,b)\,x^{a+b-1}.\ }$$
> La convolución de dos potencias es otra potencia, con la **Beta** como factor de normalización.

---

## En qué consiste

> [!teorema] Relación Beta–Gamma
> Para $p,q>0$,
> $$B(p,q)=\frac{\Gamma(p)\,\Gamma(q)}{\Gamma(p+q)}.$$

> [!demostracion]
> **Paso 1 — producto de dos Gamma.** Escribimos $\Gamma(p)\Gamma(q)$ como integral doble usando
> variables $u,v>0$:
> $$\Gamma(p)\Gamma(q)=\int_0^\infty u^{p-1}e^{-u}\,du\int_0^\infty v^{q-1}e^{-v}\,dv
> =\iint_{u,v>0} u^{p-1}v^{q-1}e^{-(u+v)}\,du\,dv.$$
>
> **Paso 2 — cambio a "radio y proporción".** Ponemos $u=s\,\tau$, $v=s(1-\tau)$ con $s=u+v>0$ y
> $\tau\in[0,1]$; el jacobiano es $s$. Entonces $u+v=s$ y
> $$\Gamma(p)\Gamma(q)=\int_0^\infty\!\!\int_0^1 (s\tau)^{p-1}\big(s(1-\tau)\big)^{q-1}e^{-s}\,s\,d\tau\,ds.$$
>
> **Paso 3 — separar las integrales.** Agrupando potencias de $s$ ($s^{p+q-1}$) y de $\tau$,
> $$=\underbrace{\int_0^\infty s^{p+q-1}e^{-s}\,ds}_{\Gamma(p+q)}\ \cdot\ \underbrace{\int_0^1 \tau^{p-1}(1-\tau)^{q-1}\,d\tau}_{B(p,q)}.$$
>
> **Paso 4 — despejar.** Por tanto $\Gamma(p)\Gamma(q)=\Gamma(p+q)\,B(p,q)$, es decir
> $B(p,q)=\Gamma(p)\Gamma(q)/\Gamma(p+q)$. $\blacksquare$

> [!info] Por qué aparecen en ecuaciones integrales
> La razón es la **convolución de núcleos potencia**:
> $$t^{a-1}*t^{b-1}=\int_0^x(x-t)^{a-1}t^{b-1}\,dt=B(a,b)\,x^{a+b-1}.$$
> Componer dos potencias da otra potencia y la Beta como coeficiente. Esto fundamenta dos cosas:
> los [[Problema de Abel| núcleos de Abel]] $1/\sqrt{x-t}=(x-t)^{-1/2}$ se componen entre sí
> ($a=b=\tfrac12$) dando $B(\tfrac12,\tfrac12)=\pi$, una **constante**, lo que explica por qué aplicar
> Abel dos veces integra una vez; y la integral fraccionaria de
> [[Calculo Fraccionario/index| Riemann-Liouville]] $I^\alpha f=\frac{1}{\Gamma(\alpha)}\int_0^x(x-t)^{\alpha-1}f(t)\,dt$,
> donde $\Gamma$ es el factor que **normaliza** para que $I^m$ coincida con $m$ integraciones repetidas.

> [!proposicion]
> De la definición y la relación Beta–Gamma se siguen los valores de uso frecuente:
> $$\Gamma(1)=1,\quad \Gamma\!\left(\tfrac12\right)=\sqrt{\pi},\quad \Gamma(z+1)=z\,\Gamma(z),\quad
> B\!\left(\tfrac12,\tfrac12\right)=\pi.$$
> La identidad $\Gamma(z+1)=z\Gamma(z)$ es la **recursión factorial**, base de toda la teoría.

## Resumen

> [!resumen]
> | Función | Definición | Valor clave |
> |---|---|---|
> | Gamma $\Gamma(z)$ | $\int_0^\infty t^{z-1}e^{-t}dt$ | $\Gamma(n)=(n-1)!$, $\Gamma(\tfrac12)=\sqrt\pi$ |
> | Beta $B(p,q)$ | $\int_0^1 t^{p-1}(1-t)^{q-1}dt$ | $=\dfrac{\Gamma(p)\Gamma(q)}{\Gamma(p+q)}$ |
> | Convolución | $t^{a-1}*t^{b-1}$ | $=B(a,b)\,x^{a+b-1}$ |

> [!corolario]
> Gamma y Beta son el "álgebra" de los núcleos potencia: convolucionar potencias se reduce a multiplicar
> Betas, y $\Gamma$ generaliza el factorial que normaliza la integración repetida. Por eso son la
> herramienta silenciosa detrás de Abel y del cálculo fraccionario.

> [!referencia]
> - Donde se usan como núcleo singular: [[Problema de Abel]].
> - El método de convolución asociado: [[Ecuaciones de Convolucion]].
> - La integral que normalizan: [[Calculo Fraccionario/index]].
> - Vuelta al índice: [[Volterra/index]].
