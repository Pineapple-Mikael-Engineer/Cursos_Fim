---
title: Derivada de Caputo
tags:
  - ecuaciones
  - difero-integrales
  - teoria
  - calculo-fraccionario
  - caputo
draft: false
aliases:
  - derivada fraccionaria de Caputo
  - derivada de Caputo
  - Caputo derivative
  - fractional derivative Caputo
---

# Derivada de Caputo $D^{\alpha}_{C}$

> [!definicion]
> La **derivada fraccionaria de Caputo** de orden $\alpha>0$, con $n=\lceil\alpha\rceil$, invierte el
> orden de las operaciones respecto a la [[Derivada de Riemann-Liouville| de Riemann-Liouville]]:
> primero se **deriva** $n$ veces de forma clásica y luego se **integra** fraccionariamente,
> $$D^{\alpha}_{C}f=I^{\,n-\alpha}\,\frac{d^{n}f}{dx^{n}}.$$
> En el caso $0<\alpha<1$ (entonces $n=1$):
> $$D^{\alpha}_{C}f(x)=\frac{1}{\Gamma(1-\alpha)}\int_0^x (x-t)^{-\alpha}\,f'(t)\,dt.$$
> Que la derivada clásica $f^{(n)}$ entre **dentro** de la integral es justo lo que hace cómodas las
> condiciones iniciales.

> [!info]
> Es la derivada **preferida en física e ingeniería** del
> [[Calculo Fraccionario/index| cálculo fraccionario]]. Se apoya en la misma
> [[Integral de Riemann-Liouville| integral fraccionaria]] $I^{n-\alpha}$ que su gemela
> [[Derivada de Riemann-Liouville| de Riemann-Liouville]], pero con el orden de derivar/integrar
> intercambiado. Es la que aparece en las ecuaciones fraccionarias resueltas con la
> [[Funcion de Mittag-Leffler| función de Mittag-Leffler]]. Capítulo:
> [[4 Ecuaciones Difero-integrales/index| Ecuaciones difero-integrales]].

---

## Ejemplo

> [!ejemplo] Caputo vs. Riemann-Liouville sobre $f=1$ y $f=x$
> Tomamos $\alpha=\tfrac12$, $n=1$, y comparamos ambas derivadas.
>
> **Sobre la constante $f(x)=1$.** Su derivada clásica es $f'=0$, luego
> $$D^{1/2}_{C}1=\frac{1}{\Gamma(1/2)}\int_0^x (x-t)^{-1/2}\cdot 0\;dt=0.$$
> En cambio, Riemann-Liouville daba $D^{1/2}1=\dfrac{x^{-1/2}}{\Gamma(1/2)}=\dfrac{1}{\sqrt{\pi x}}\neq 0$.
> La **constante tiene derivada de Caputo nula**, como en el cálculo clásico.
>
> **Sobre $f(x)=x$.** Ahora $f'=1$, y la integral fraccionaria de una constante es conocida:
> $$D^{1/2}_{C}x=I^{1/2}\,(1)=\frac{\Gamma(1)}{\Gamma(1+\tfrac12)}x^{1/2}=\frac{2}{\sqrt{\pi}}\sqrt{x}.$$
> Aquí **coincide** con Riemann-Liouville ($D^{1/2}x=\tfrac{2}{\sqrt\pi}\sqrt x$), porque $f(0)=0$ y no
> hay término de borde que las separe.
> | $f(x)$ | $D^{1/2}f$ (R-L) | $D^{1/2}_{C}f$ (Caputo) | ¿coinciden? |
> |:--:|:--:|:--:|:--:|
> | $1$ | $\dfrac{1}{\sqrt{\pi x}}$ | $0$ | no ($f(0)\neq 0$) |
> | $x$ | $\dfrac{2}{\sqrt\pi}\sqrt{x}$ | $\dfrac{2}{\sqrt\pi}\sqrt{x}$ | sí ($f(0)=0$) |

---

## En qué consiste

> [!teoria]
> El intercambio de orden tiene una consecuencia inmediata: como Caputo **deriva primero**, cualquier
> parte constante (o, en general, polinómica de grado $<n$) muere antes de integrarse. Por eso
> $D^{\alpha}_{C}$ se comporta como una derivada "de verdad" frente a las constantes, y por eso las
> condiciones iniciales que necesita son las **clásicas** $f(0),f'(0),\dots,f^{(n-1)}(0)$ —valores y
> derivadas enteras de la función, magnitudes con significado físico directo— y no derivadas
> fraccionarias evaluadas en el origen. Esa es toda su ventaja, y es decisiva en modelado.

> [!teorema] Relación Riemann-Liouville $\leftrightarrow$ Caputo
> Ambas derivadas difieren únicamente por términos que recogen los valores iniciales de $f$:
> $$D^{\alpha}f=D^{\alpha}_{C}f+\sum_{k=0}^{n-1}\frac{f^{(k)}(0)}{\Gamma(k-\alpha+1)}\,x^{k-\alpha}.$$
> En consecuencia, **coinciden** si $f(0)=f'(0)=\dots=f^{(n-1)}(0)=0$.

> [!demostracion]
> **Paso 1 — caso $0<\alpha<1$ ($n=1$).** Partimos de Riemann-Liouville,
> $D^{\alpha}f=\dfrac{d}{dx}\,I^{1-\alpha}f$, y desarrollamos $I^{1-\alpha}f$ integrando por partes,
> tratando $u=f(t)$, $dv=(x-t)^{-\alpha}dt$ (con $v=-\tfrac{(x-t)^{1-\alpha}}{1-\alpha}$):
> $$I^{1-\alpha}f(x)=\frac{1}{\Gamma(1-\alpha)}\!\left[\frac{f(0)\,x^{1-\alpha}}{1-\alpha}
> +\frac{1}{1-\alpha}\int_0^x (x-t)^{1-\alpha}f'(t)\,dt\right].$$
> **Paso 2 — derivar respecto a $x$.** Al aplicar $\dfrac{d}{dx}$, el primer término da
> $\dfrac{f(0)\,x^{-\alpha}}{\Gamma(1-\alpha)}$ y el segundo reproduce exactamente la definición de
> Caputo $D^{\alpha}_{C}f=\dfrac{1}{\Gamma(1-\alpha)}\int_0^x(x-t)^{-\alpha}f'(t)\,dt$. Por tanto
> $$D^{\alpha}f=\frac{f(0)}{\Gamma(1-\alpha)}\,x^{-\alpha}+D^{\alpha}_{C}f,$$
> que es la fórmula con el único término $k=0$. **Paso 3 — caso general.** Iterando la integración por
> partes $n$ veces aparecen los términos $k=0,\dots,n-1$ con $f^{(k)}(0)$, dando la suma del enunciado.
> $\blacksquare$

> [!info] Por qué la física la prefiere
> En las [[Ecuaciones Diferenciales Fraccionarias| ecuaciones diferenciales fraccionarias]] de la
> difusión anómala, la viscoelasticidad o los sistemas con memoria, el estado inicial del sistema es un
> dato físico: posición $f(0)$, velocidad $f'(0)$. Caputo permite imponerlos tal cual al resolver con la
> transformada de Laplace y la [[Funcion de Mittag-Leffler| función de Mittag-Leffler]]; Riemann-Liouville
> obligaría a traducirlos a derivadas fraccionarias en $0$. De ahí que estos modelos casi siempre se
> escriban con $D^{\alpha}_{C}$.

## Resumen

> [!resumen]
> | Objeto | Expresión |
> |:--|:--|
> | Definición | $D^{\alpha}_{C}f=I^{\,n-\alpha}\dfrac{d^{n}f}{dx^{n}}$ (derivar, luego integrar) |
> | Caso $0<\alpha<1$ | $D^{\alpha}_{C}f=\dfrac{1}{\Gamma(1-\alpha)}\int_0^x (x-t)^{-\alpha}f'(t)\,dt$ |
> | Constante | $D^{\alpha}_{C}1=0$ (¡sí se anula!) |
> | Cond. iniciales | clásicas: $f(0),f'(0),\dots,f^{(n-1)}(0)$ |
> | Relación con R-L | $D^{\alpha}f=D^{\alpha}_{C}f+\sum_{k=0}^{n-1}\dfrac{f^{(k)}(0)}{\Gamma(k-\alpha+1)}x^{k-\alpha}$ |
> | Coinciden si | $f^{(k)}(0)=0$ para $k=0,\dots,n-1$ |

> [!corolario]
> La derivada de Caputo es la misma idea que Riemann-Liouville con el orden de las operaciones
> invertido, y ese único cambio la hace físicamente natural: anula constantes y admite condiciones
> iniciales clásicas. Es, por eso, la herramienta estándar para escribir y resolver ecuaciones
> fraccionarias del mundo real.

> [!referencia]
> - Su gemela matemática: [[Derivada de Riemann-Liouville]].
> - El operador integral base: [[Integral de Riemann-Liouville]].
> - La exponencial que resuelve sus ecuaciones: [[Funcion de Mittag-Leffler]].
