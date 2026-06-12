---
title: Delta de Dirac y Singularidades
tags:
  - electromagnetismo
  - teoria
  - calculo-vectorial
draft: false
aliases:
  - Delta de Dirac
  - Función delta tridimensional
  - div(r̂/r²)=4π δ³(r)
---

# Delta de Dirac y Singularidades $\nabla\cdot\dfrac{\hat r}{r^2}=4\pi\,\delta^3(\vec r)$

> [!definicion]
> La **delta de Dirac** $\delta(x)$ es la "función" nula en todo punto salvo el origen, con área unidad:
> $$\delta(x)=0\ \ (x\neq0),\qquad \int_{-\infty}^{\infty}\delta(x)\,dx=1,\qquad \int_{-\infty}^{\infty}f(x)\,\delta(x-a)\,dx=f(a).$$
> Su versión **tridimensional** $\delta^3(\vec r)=\delta(x)\,\delta(y)\,\delta(z)$ cumple $\int_{\text{todo}}\delta^3(\vec r)\,d^3r=1$ y $\int f(\vec r)\,\delta^3(\vec r-\vec a)\,d^3r=f(\vec a)$. Es el objeto que describe una **carga puntual** como densidad: $\rho(\vec r)=q\,\delta^3(\vec r-\vec a)$.

---

> [!info]
> **Ubicación.** Curso Electromagnetismo · sección [[1 Calculo Vectorial/index | Cálculo Vectorial]]. Hermanas: [[Campos y Operadores]] (operadores), [[Teoremas Integrales]] (Gauss, que aquí se usa), [[Identidades Vectoriales]] (las identidades nulas fallan justo en la singularidad que estudia esta nota).
> **Referencia.** Griffiths, *Introduction to Electrodynamics*, §1.5. El resultado central $\nabla\cdot(\hat r/r^2)=4\pi\,\delta^3(\vec r)$ —equivalente a $\nabla^2(1/r)=-4\pi\,\delta^3(\vec r)$— es la **piedra angular** de la electrostática: hace consistentes la ley de Gauss diferencial y la de Coulomb.

---

## Ejemplo

> [!ejemplo] La paradoja del campo $\hat r/r^2$
> El campo $\vec F=\hat r/r^2$ (la forma del campo de una carga puntual) parece tener divergencia nula en todas partes, y sin embargo su flujo por cualquier esfera centrada en el origen vale $4\pi$. ¿Cómo se reconcilia esto?
>
> ![[campo_puntual.svg|360]]
> *Campo radial $\vec F=\hat r/r^2$: diverge desde el origen. Toda la "fuente" está concentrada en $r=0$.*
>
> > [!solucion]
> > **Divergencia fuera del origen.** En esféricas $\nabla\cdot\vec F=\dfrac{1}{r^2}\dfrac{\partial}{\partial r}\big(r^2 F_r\big)$ con $F_r=1/r^2$:
> > $$\nabla\cdot\vec F=\frac{1}{r^2}\frac{\partial}{\partial r}\!\left(r^2\cdot\frac{1}{r^2}\right)=\frac{1}{r^2}\frac{\partial}{\partial r}(1)=0\qquad(r\neq0).$$
> > **Flujo por una esfera de radio $R$.** Con $d\vec A=R^2\sin\theta\,d\theta\,d\phi\,\hat r$ y $F_r(R)=1/R^2$:
> > $$\oint_S\vec F\cdot d\vec A=\int_0^{2\pi}\!\!\int_0^{\pi}\frac{1}{R^2}\,R^2\sin\theta\,d\theta\,d\phi=\int_0^{2\pi}d\phi\int_0^{\pi}\sin\theta\,d\theta=2\pi\cdot2=4\pi.$$
> > El flujo es $4\pi$ **independiente de $R$**, pero la divergencia es $0$ en todo el interior salvo en $r=0$. Por el teorema de la divergencia, $\int_V\nabla\cdot\vec F\,dV=4\pi$ aunque el integrando sea nulo en casi todo punto: la divergencia es una **delta** concentrada en el origen. Eso resuelve la paradoja.

---

## En qué consiste

> [!teoria] La delta como límite y como distribución
> $\delta(x)$ no es una función ordinaria: es una **distribución**, definida por cómo actúa bajo la integral (su "propiedad de cribado" $\int f\,\delta=f(0)$). Se la puede ver como límite de funciones cada vez más picudas y estrechas de área $1$ —p. ej. gaussianas $\frac{1}{\sqrt{2\pi}\,\sigma}e^{-x^2/2\sigma^2}$ con $\sigma\to0$, o un pulso rectangular de ancho $\varepsilon$ y altura $1/\varepsilon$—. Propiedades útiles:
> $$\delta(-x)=\delta(x),\qquad \delta(ax)=\frac{1}{|a|}\delta(x),\qquad x\,\delta(x)=0,\qquad \delta(x)=\frac{d}{dx}\,\Theta(x),$$
> donde $\Theta$ es el escalón de Heaviside. La derivada $\delta'(x)$ se define por $\int f\,\delta'=-f'(0)$ (integración por partes).

> [!teorema] Identidad fundamental de la electrostática
> En sentido distribucional,
> $$\nabla\cdot\!\left(\frac{\hat r}{r^2}\right)=4\pi\,\delta^3(\vec r),\qquad\text{equivalentemente}\qquad \nabla^2\!\left(\frac{1}{r}\right)=-4\pi\,\delta^3(\vec r).$$
>
> > [!demostracion]
> > **Paso 1 — Fuera del origen vale $0$.** Para $r\neq0$, el cálculo del ejemplo da $\nabla\cdot(\hat r/r^2)=0$. La equivalencia con el laplaciano sale de $\nabla(1/r)=-\hat r/r^2$ (pues $\partial_r(1/r)=-1/r^2$), luego $\nabla^2(1/r)=\nabla\cdot\nabla(1/r)=-\nabla\cdot(\hat r/r^2)$, que también es $0$ para $r\neq0$.
> > **Paso 2 — Pero la integral vale $4\pi$.** Para *cualquier* volumen $V$ que contenga al origen, con frontera $S$, el teorema de la divergencia ([[Teoremas Integrales]]) y el flujo del ejemplo dan
> > $$\int_V\nabla\cdot\!\left(\frac{\hat r}{r^2}\right)dV=\oint_S\frac{\hat r}{r^2}\cdot d\vec A=4\pi,$$
> > donde el último paso usa que el flujo de $\hat r/r^2$ por **cualquier** superficie cerrada que rodee al origen es $4\pi$ (ángulo sólido total; no depende de la forma de $S$). Si $V$ **no** contiene al origen, $\nabla\cdot\vec F=0$ en todo $V$ y la integral es $0$.
> > **Paso 3 — Conclusión: es una delta.** Tenemos una densidad que es nula en todo punto salvo el origen pero cuya integral sobre cualquier región que incluya el origen es $4\pi$ (y $0$ si no lo incluye). Esa es exactamente la definición de $4\pi\,\delta^3(\vec r)$:
> > $$\int_V\nabla\cdot\!\left(\frac{\hat r}{r^2}\right)dV=4\pi\int_V\delta^3(\vec r)\,dV\ \ \forall V\ \Longrightarrow\ \nabla\cdot\!\left(\frac{\hat r}{r^2}\right)=4\pi\,\delta^3(\vec r).\qquad\blacksquare$$
>
> > [!warning]
> > La identidad nula $\nabla\cdot\vec F=0$ del ejemplo **solo es válida fuera del origen**. El cálculo ingenuo en esféricas "pierde" la delta porque $1/r^2$ no es diferenciable en $r=0$. Lección general: las identidades de [[Identidades Vectoriales]] valen donde los campos son suaves; en las **singularidades** (cargas puntuales, hilos, planos) aparecen deltas que solo el argumento de flujo detecta.

> [!proposicion] Forma trasladada (carga en $\vec r\,'$)
> Para una fuente en el punto $\vec r\,'$, con $\vec{\mathscr r}=\vec r-\vec r\,'$ y $\mathscr r=|\vec r-\vec r\,'|$:
> $$\nabla\cdot\!\left(\frac{\hat{\mathscr r}}{\mathscr r^2}\right)=4\pi\,\delta^3(\vec r-\vec r\,'),\qquad \nabla^2\!\left(\frac{1}{|\vec r-\vec r\,'|}\right)=-4\pi\,\delta^3(\vec r-\vec r\,').$$
> El operador $\nabla$ actúa sobre la coordenada de campo $\vec r$. Esta es la versión que se usa al integrar sobre distribuciones de carga.

> [!corolario] De aquí sale la ley de Gauss diferencial
> El campo de Coulomb de una carga puntual $q$ en el origen es $\vec E=\dfrac{q}{4\pi\varepsilon_0}\dfrac{\hat r}{r^2}$. Tomando divergencia y usando el teorema:
> $$\nabla\cdot\vec E=\frac{q}{4\pi\varepsilon_0}\,\nabla\cdot\!\left(\frac{\hat r}{r^2}\right)=\frac{q}{4\pi\varepsilon_0}\,4\pi\,\delta^3(\vec r)=\frac{q\,\delta^3(\vec r)}{\varepsilon_0}=\frac{\rho(\vec r)}{\varepsilon_0},$$
> ya que $\rho(\vec r)=q\,\delta^3(\vec r)$. Es decir, $\boxed{\nabla\cdot\vec E=\rho/\varepsilon_0}$: la **ley de Gauss en forma diferencial** nace de esta identidad. Sin la delta, la divergencia del campo de Coulomb parecería nula en todas partes y la ley de Gauss sería contradictoria.

---

## Resumen

> [!resumen] Lo esencial
>
> | Objeto | Propiedad |
> |:---|:---|
> | $\delta(x)$ | $0$ salvo en $0$; $\int\delta\,dx=1$; $\int f\,\delta(x-a)\,dx=f(a)$ |
> | $\delta^3(\vec r)$ | $\delta(x)\delta(y)\delta(z)$; $\int\delta^3 d^3r=1$; carga puntual $\rho=q\,\delta^3(\vec r)$ |
> | $\nabla\cdot(\hat r/r^2)$ | $=4\pi\,\delta^3(\vec r)$ — nulo salvo en el origen, flujo $4\pi$ |
> | $\nabla^2(1/r)$ | $=-4\pi\,\delta^3(\vec r)$ — la "función de Green" del laplaciano |
> | Consecuencia | $\nabla\cdot\vec E=\rho/\varepsilon_0$ (Gauss diferencial) sale de aquí |

> [!corolario] Por qué cierra el capítulo
> El cálculo vectorial "limpio" ([[Campos y Operadores]], [[Teoremas Integrales]], [[Identidades Vectoriales]]) supone campos suaves. El electromagnetismo está lleno de **fuentes puntuales y singularidades**, y la delta es el lenguaje que las incorpora sin romper el formalismo: convierte "el campo diverge en un punto" en una ecuación local exacta. Con esto, el capítulo entrega las tres herramientas que la electrostática usará sin parar: los **operadores**, los **teoremas integrales** y la **delta**.

> [!referencia]
> Griffiths, *Introduction to Electrodynamics*, §1.5 (especialmente §1.5.3, la divergencia de $\hat r/r^2$). Para la delta como distribución y la función de Green del laplaciano: Jackson, *Classical Electrodynamics*, cap. 1.
