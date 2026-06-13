---
title: Integral de Riemann-Liouville
tags:
  - ecuaciones
  - difero-integrales
  - teoria
  - calculo-fraccionario
  - riemann-liouville
draft: false
aliases:
  - integral fraccionaria de Riemann-Liouville
  - integral fraccionaria
  - media integral
  - Riemann-Liouville integral
  - fractional integral
---

# Integral de Riemann-Liouville $I^{\alpha}$

> [!definicion]
> La **integral fraccionaria de Riemann-Liouville** de orden $\alpha>0$ (con límite inferior $0$) es
> $$I^{\alpha}f(x)=\frac{1}{\Gamma(\alpha)}\int_0^x (x-t)^{\alpha-1}\,f(t)\,dt.$$
> No es más que la **integral iterada $n$ veces**, en la que se ha sustituido el factorial por la
> función Gamma: la fórmula de Cauchy $I^{n}f(x)=\dfrac{1}{(n-1)!}\int_0^x(x-t)^{n-1}f(t)\,dt$ con el
> cambio $(n-1)!\to\Gamma(\alpha)$ y permitiendo $\alpha$ **real**. Es la pieza concreta que da cuerpo
> al [[Operador Differintegral| differintegral]]: $I^{\alpha}=D^{-\alpha}$.

> [!info]
> Definición operativa del [[Calculo Fraccionario/index| cálculo fraccionario]]. De aquí parten las
> derivadas fraccionarias: la [[Derivada de Riemann-Liouville| de Riemann-Liouville]] (derivar tras
> integrar) y la [[Derivada de Caputo| de Caputo]] (derivar antes). El núcleo $(x-t)^{\alpha-1}$ es,
> salvo la constante $\Gamma(\alpha)$, exactamente el de la ecuación integral del
> [[Problema de Abel| problema de Abel]]. Segunda rama del
> [[4 Ecuaciones Difero-integrales/index| capítulo difero-integral]].

---

## Ejemplo

> [!ejemplo] La media integral de una constante
> Queremos $I^{1/2}1$, la "**media integral**" de la función constante $f(x)=1$. Como $1=x^{0}$, usamos
> la regla de las potencias con $\mu=0$ y $\alpha=\tfrac12$:
> $$I^{1/2}1=\frac{\Gamma(0+1)}{\Gamma(0+1+\tfrac12)}\,x^{0+1/2}=\frac{\Gamma(1)}{\Gamma(3/2)}\,x^{1/2}.$$
> **Paso 1 — evaluar las Gamma.** $\Gamma(1)=1$ y $\Gamma(3/2)=\tfrac12\sqrt{\pi}$, así que
> $$I^{1/2}1=\frac{x^{1/2}}{\tfrac12\sqrt{\pi}}=\frac{2\,x^{1/2}}{\sqrt{\pi}}=2\sqrt{\frac{x}{\pi}}.$$
> **Paso 2 — comprobar el sentido (semigrupo).** Aplicar $I^{1/2}$ **dos veces** debe dar la integral
> entera $I^{1}1=\int_0^x 1\,dt=x$. En efecto, $I^{1/2}\big(2\sqrt{x/\pi}\big)$ usa $\mu=\tfrac12$:
> $$I^{1/2}\!\left(\frac{2}{\sqrt\pi}x^{1/2}\right)=\frac{2}{\sqrt\pi}\cdot\frac{\Gamma(3/2)}{\Gamma(2)}\,x^{1}=\frac{2}{\sqrt\pi}\cdot\frac{\tfrac12\sqrt\pi}{1}\,x=x.\quad\checkmark$$
> Dos medias integraciones reconstruyen una integración entera: $I^{1/2}I^{1/2}1=I^{1}1=x$.

---

## En qué consiste

> [!teoria]
> La idea nace de la **fórmula de Cauchy** para la antiderivada repetida. Integrar una vez con base en
> $0$ es $I^{1}f(x)=\int_0^x f(t)\,dt$; integrar $n$ veces colapsa la integral múltiple en una sola
> gracias a un núcleo de convolución:
> $$I^{n}f(x)=\frac{1}{(n-1)!}\int_0^x (x-t)^{n-1}f(t)\,dt.$$
> El factorial $(n-1)!=\Gamma(n)$ es lo único que impide poner $n$ no entero. Reemplazándolo por
> $\Gamma(\alpha)$ se obtiene un operador definido para **todo** $\alpha>0$. Es una **convolución**
> $I^{\alpha}f=\Phi_\alpha * f$ con el núcleo causal $\Phi_\alpha(x)=\dfrac{x^{\alpha-1}}{\Gamma(\alpha)}$
> para $x>0$: por eso es **no local**, depende de toda la historia de $f$ en $[0,x]$.

> [!teorema] Regla de las potencias
> Para $\mu>-1$ y $\alpha>0$,
> $$I^{\alpha}x^{\mu}=\frac{\Gamma(\mu+1)}{\Gamma(\mu+1+\alpha)}\,x^{\mu+\alpha}.$$

> [!demostracion]
> **Paso 1 — escribir la integral.** Por definición,
> $$I^{\alpha}x^{\mu}=\frac{1}{\Gamma(\alpha)}\int_0^x (x-t)^{\alpha-1}t^{\mu}\,dt.$$
> **Paso 2 — cambio de variable $t=xu$** (con $dt=x\,du$, y $u:0\to1$). Entonces
> $x-t=x(1-u)$, de modo que $(x-t)^{\alpha-1}=x^{\alpha-1}(1-u)^{\alpha-1}$ y $t^{\mu}=x^{\mu}u^{\mu}$:
> $$I^{\alpha}x^{\mu}=\frac{1}{\Gamma(\alpha)}\int_0^1 x^{\alpha-1}(1-u)^{\alpha-1}\,x^{\mu}u^{\mu}\,x\,du
> =\frac{x^{\mu+\alpha}}{\Gamma(\alpha)}\int_0^1 u^{\mu}(1-u)^{\alpha-1}\,du.$$
> **Paso 3 — reconocer la función Beta.** La integral restante es $B(\mu+1,\alpha)$, y por la relación
> Beta-Gamma ([[Integrales de Euler]]),
> $$\int_0^1 u^{\mu}(1-u)^{\alpha-1}\,du=B(\mu+1,\alpha)=\frac{\Gamma(\mu+1)\,\Gamma(\alpha)}{\Gamma(\mu+1+\alpha)}.$$
> **Paso 4 — simplificar.** El $\Gamma(\alpha)$ se cancela con el del denominador, dejando
> $$I^{\alpha}x^{\mu}=\frac{\Gamma(\mu+1)}{\Gamma(\mu+1+\alpha)}\,x^{\mu+\alpha}.\qquad\blacksquare$$

> [!teorema] Propiedad de semigrupo
> Las integraciones fraccionarias **se suman en el orden**: para $\alpha,\beta>0$,
> $$I^{\alpha}I^{\beta}f=I^{\alpha+\beta}f.$$

> [!demostracion]
> **Paso 1 — convolución.** Como $I^{\gamma}f=\Phi_\gamma*f$ con $\Phi_\gamma(x)=x^{\gamma-1}/\Gamma(\gamma)$,
> componer dos integraciones es convolucionar los núcleos: $I^{\alpha}I^{\beta}f=(\Phi_\alpha*\Phi_\beta)*f$.
> **Paso 2 — convolución de los núcleos.** Se calcula, vía el mismo cambio $t=xu$ del teorema anterior,
> $$(\Phi_\alpha*\Phi_\beta)(x)=\frac{1}{\Gamma(\alpha)\Gamma(\beta)}\int_0^x (x-t)^{\alpha-1}t^{\beta-1}\,dt
> =\frac{x^{\alpha+\beta-1}}{\Gamma(\alpha)\Gamma(\beta)}\,B(\beta,\alpha).$$
> **Paso 3 — Beta-Gamma.** Como $B(\beta,\alpha)=\dfrac{\Gamma(\alpha)\Gamma(\beta)}{\Gamma(\alpha+\beta)}$,
> $$(\Phi_\alpha*\Phi_\beta)(x)=\frac{x^{\alpha+\beta-1}}{\Gamma(\alpha+\beta)}=\Phi_{\alpha+\beta}(x),$$
> luego $I^{\alpha}I^{\beta}f=\Phi_{\alpha+\beta}*f=I^{\alpha+\beta}f$. $\blacksquare$

> [!info] Conexión con Abel
> El núcleo $\Phi_{1/2}(x)=\dfrac{x^{-1/2}}{\Gamma(1/2)}=\dfrac{1}{\sqrt{\pi x}}$ es **el núcleo de Abel**
> salvo el factor $\Gamma(1/2)=\sqrt{\pi}$. Por eso el [[Problema de Abel| problema de Abel]]
> $\int_0^x \dfrac{f(t)}{\sqrt{x-t}}\,dt=g(x)$ es, literalmente, "$I^{1/2}f$ a menos de $\sqrt\pi$": el
> medio-cálculo apareció en física (la curva tautócrona) antes de tener nombre.

> [!warning] Depende del límite inferior
> La definición fija la base en $0$. Cambiar el extremo inferior (escribir $\int_a^x$) **cambia el
> operador**: se obtiene $\,_aI^{\alpha}$, distinto de $\,_0I^{\alpha}$ salvo casos triviales. Cuando se
> hable de "la" integral de Riemann-Liouville sin más, se entiende base $0$. Esta dependencia se hereda
> a las derivadas fraccionarias y es la razón de que las condiciones iniciales se impongan en ese punto.

## Resumen

> [!resumen]
> | Objeto | Expresión |
> |:--|:--|
> | Definición | $I^{\alpha}f(x)=\dfrac{1}{\Gamma(\alpha)}\int_0^x (x-t)^{\alpha-1}f(t)\,dt$ |
> | Origen | fórmula de Cauchy con $(n-1)!\to\Gamma(\alpha)$ |
> | Núcleo | $\Phi_\alpha(x)=\dfrac{x^{\alpha-1}}{\Gamma(\alpha)}$, convolución $I^\alpha f=\Phi_\alpha*f$ |
> | Potencias | $I^{\alpha}x^{\mu}=\dfrac{\Gamma(\mu+1)}{\Gamma(\mu+1+\alpha)}x^{\mu+\alpha}$ |
> | Semigrupo | $I^{\alpha}I^{\beta}=I^{\alpha+\beta}$ |
> | Caso medio | $I^{1/2}1=2\sqrt{x/\pi}$, y $I^{1/2}I^{1/2}1=x$ |

> [!corolario]
> La integral fraccionaria es el ladrillo de todo el edificio: un único cambio —factorial por Gamma—
> convierte la antiderivada repetida en un operador continuo en el orden, con estructura de semigrupo y
> memoria de toda la historia. Derivar fraccionariamente será, simplemente, integrar con $I^{n-\alpha}$
> y luego derivar $n$ veces.

> [!referencia]
> - La idea de orden arbitrario: [[Operador Differintegral]].
> - Las derivadas que se construyen encima: [[Derivada de Riemann-Liouville]], [[Derivada de Caputo]].
> - El precursor físico: [[Problema de Abel]].
> - La Beta y la Gamma usadas: [[Integrales de Euler]].
