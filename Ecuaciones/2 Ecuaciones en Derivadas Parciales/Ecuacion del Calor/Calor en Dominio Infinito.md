---
title: Calor en Dominio Infinito
tags:
  - ecuaciones
  - edp
  - teoria
  - calor
  - fourier
draft: false
aliases:
  - calor en dominio infinito
  - núcleo de calor
  - solución fundamental del calor
  - heat kernel
  - heat equation on the line
---

# Calor en Dominio Infinito

> [!definicion]
> Cuando el calor difunde en **toda la recta** ($-\infty<x<\infty$, sin paredes que lo confinen),
> el problema
> $$u_t=\alpha^2u_{xx},\qquad u(x,0)=f(x),$$
> se resuelve con la **transformada de Fourier** en la variable $x$. La separación de variables
> ya no sirve aquí: sin fronteras no hay condiciones que cuanticen los autovalores en una serie
> discreta $\{\lambda_n\}$, sino un espectro **continuo** de modos $e^{ikx}$. El resultado final es
> una **convolución** del dato inicial con el **núcleo de calor**, una gaussiana:
> $$u(x,t)=\int_{-\infty}^{\infty}G(x-y,t)\,f(y)\,dy,\qquad
> G(x,t)=\frac{1}{\sqrt{4\pi\alpha^2t}}\;e^{-x^2/(4\alpha^2t)}.$$

> [!info]
> Es el caso **no acotado** de la [[Ecuacion del Calor/index| ecuación del calor]], complementario
> al de dominio finito que resuelven la [[Separacion Calor Dirichlet| separación con Dirichlet]] y
> sus variantes. Pertenece al [[2 Ecuaciones en Derivadas Parciales/index| capítulo de EDP]] (tipo
> **parabólico**). La ecuación misma se obtiene en [[Derivacion del Calor| la derivación del calor]];
> aquí solo cambia el dominio: la recta entera en vez de un segmento $[0,L]$.

---

## Ejemplo

> [!ejemplo] Un punto de calor concentrado
> Supongamos que en $t=0$ concentramos toda la temperatura en el origen: $u(x,0)=\delta(x)$ (una
> delta de Dirac, un "pinchazo" de calor de área unidad). Sustituyendo $f=\delta$ en la convolución
> y usando que $\int G(x-y,t)\,\delta(y)\,dy=G(x,t)$, la solución es **directamente el núcleo**:
> $$u(x,t)=G(x,t)=\frac{1}{\sqrt{4\pi\alpha^2t}}\;e^{-x^2/(4\alpha^2t)}.$$
>
> Interpretación, instante a instante:
> - En $t\to0^+$ la gaussiana es altísima y angostísima — recupera la delta inicial.
> - Para $t>0$ se **ensancha** (su desviación típica es $\sigma=\sqrt{2\alpha^2t}\sim\sqrt{t}$) y se
>   **aplana** (su altura cae como $1/\sqrt{t}$). El calor se reparte hacia los lados.
>
> Lo notable: para **cualquier** $t>0$, por pequeño que sea, $u(x,t)>0$ en **todo** $x$, incluso
> arbitrariamente lejos del origen. El calor que pusimos en un solo punto se "siente" al instante en
> todas partes (aunque exponencialmente débil). Esto es la **velocidad de propagación infinita**, el
> rasgo parabólico que distingue al calor de la [[Ecuacion de Onda/index| onda]], donde una señal
> viaja a velocidad finita y respeta un cono de luz.

## En qué consiste

> [!teoria]
> La idea es la misma que en separación de variables, pero con un espectro continuo. La transformada
> de Fourier convierte la **derivada en $x$** en una **multiplicación por $ik$**, de modo que la EDP
> en $(x,t)$ se vuelve, para cada número de onda $k$, una **EDO ordinaria en $t$** trivial de
> resolver. Una vez resuelta modo a modo, se antitransforma para volver a $x$. El milagro es que la
> antitransformada de $e^{-\alpha^2k^2t}$ vuelve a ser una gaussiana, lo que regala la fórmula
> explícita del núcleo.
>
> Conviene fijar la convención de la transformada que usaremos:
> $$\hat u(k,t)=\int_{-\infty}^{\infty}u(x,t)\,e^{-ikx}\,dx,\qquad
> u(x,t)=\frac{1}{2\pi}\int_{-\infty}^{\infty}\hat u(k,t)\,e^{ikx}\,dk.$$

> [!algoritmo] Resolver el calor en la recta por Fourier
> 1. **Transformar la EDP en $x$.** Cada $\partial_x\to ik$, así que $\partial_{xx}\to(ik)^2=-k^2$.
> 2. **Resolver la EDO resultante en $t$** (es de primer orden, separable).
> 3. **Imponer el dato inicial** transformado, $\hat u(k,0)=\hat f(k)$.
> 4. **Antitransformar.** Reconocer $e^{-\alpha^2k^2t}$ como la transformada de una gaussiana y
>    escribir la solución como **convolución** $u=G*f$.

> [!teorema] Solución por el núcleo de calor
> El problema $u_t=\alpha^2u_{xx}$ en $-\infty<x<\infty$ con $u(x,0)=f(x)$ tiene por solución
> $$u(x,t)=(G*f)(x,t)=\int_{-\infty}^{\infty}G(x-y,t)\,f(y)\,dy,\qquad
> G(x,t)=\frac{1}{\sqrt{4\pi\alpha^2t}}\,e^{-x^2/(4\alpha^2t)},$$
> donde $G$ es la **solución fundamental**: la respuesta del sistema a un dato inicial $\delta$.

> [!demostracion]
> **Paso 1 — Transformar en $x$.** Aplicando la transformada de Fourier a $u_t=\alpha^2u_{xx}$ y
> usando que $\widehat{\partial_x u}=ik\,\hat u$ (luego $\widehat{\partial_{xx}u}=(ik)^2\hat u=-k^2\hat u$),
> mientras que la derivada en $t$ pasa intacta porque la integral es en $x$:
> $$\hat u_t(k,t)=-\alpha^2k^2\,\hat u(k,t).$$
> Para cada $k$ fijo esto es una **EDO en $t$**, no una EDP. El operador difusivo en el espacio se
> ha vuelto un simple coeficiente $-\alpha^2k^2$.
>
> **Paso 2 — Resolver la EDO en $t$.** Es lineal de primer orden con coeficiente constante:
> $$\hat u(k,t)=\hat u(k,0)\,e^{-\alpha^2k^2t}=\hat f(k)\,e^{-\alpha^2k^2t},$$
> donde se usó el dato inicial $\hat u(k,0)=\hat f(k)$. El factor $e^{-\alpha^2k^2t}$ es la clave
> física: **amortigua** cada modo, y lo hace más rápido cuanto mayor es $|k|$ (modos más oscilantes
> mueren primero). Esto es el "olvido" del calor visto en el espacio de Fourier.
>
> **Paso 3 — Antitransformar.** Hay que invertir un **producto** $\hat f(k)\cdot e^{-\alpha^2k^2t}$.
> Por el **teorema de convolución**, la antitransformada de un producto es la convolución de las
> antitransformadas. La de $\hat f$ es $f$. Falta la de $e^{-\alpha^2k^2t}$: es una gaussiana en $k$,
> y la antitransformada de una gaussiana es otra gaussiana,
> $$\mathcal F^{-1}\!\big[e^{-\alpha^2k^2t}\big](x)=\frac{1}{\sqrt{4\pi\alpha^2t}}\,e^{-x^2/(4\alpha^2t)}=G(x,t).$$
> Por tanto
> $$u(x,t)=(G*f)(x,t)=\int_{-\infty}^{\infty}G(x-y,t)\,f(y)\,dy. \qquad\blacksquare$$

> [!info] El área se conserva
> El núcleo está normalizado a uno para todo $t>0$:
> $$\int_{-\infty}^{\infty}G(x,t)\,dx=1.$$
> Como consecuencia, si el dato $f$ es integrable, el **calor total** se conserva:
> $\int u(x,t)\,dx=\int\!\!\int G(x-y,t)f(y)\,dy\,dx=\int f(y)\,dy$ para todo $t$. La difusión
> **redistribuye** el calor pero no lo crea ni lo destruye: la gaussiana se ensancha y se aplana de
> modo que el área bajo ella permanece constante.

> [!proposicion] Por qué el calor suaviza al instante
> Para $t>0$ el núcleo $G(x,t)$ es $C^\infty$ (infinitamente derivable, una gaussiana). Como
> $u=G*f$ y la convolución **hereda la suavidad del factor más suave**, la solución $u(\cdot,t)$ es
> $C^\infty$ por discontinuo o anguloso que fuese el dato $f$. La difusión lima toda aspereza de
> inmediato — el reverso de esto es que el problema **hacia atrás** (calor con $t<0$) está mal
> planteado: amplifica el ruido sin control.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Dominio | recta entera $-\infty<x<\infty$ (sin fronteras) |
> | Método | transformada de Fourier en $x$ ($\partial_x\to ik$) |
> | EDP $\to$ EDO | $\hat u_t=-\alpha^2k^2\hat u$ |
> | Solución en $k$ | $\hat u(k,t)=\hat f(k)\,e^{-\alpha^2k^2t}$ |
> | Solución en $x$ | $u=G*f$, convolución con el núcleo |
> | Núcleo de calor | $G(x,t)=\dfrac{1}{\sqrt{4\pi\alpha^2t}}\,e^{-x^2/(4\alpha^2t)}$ |
> | Ancho del núcleo | $\sigma=\sqrt{2\alpha^2t}\sim\sqrt{t}$ |
> | Normalización | $\int G\,dx=1$ (calor total conservado) |

> [!corolario]
> El núcleo de calor $G$ es la **función de Green** de la ecuación del calor en la recta: conocida
> la respuesta a una delta, la respuesta a un dato arbitrario $f$ se arma por superposición continua
> $u=G*f$. La gaussiana de varianza $\sigma^2=2\alpha^2t$ encarna a la vez el suavizado (es $C^\infty$),
> la irreversibilidad ($\sqrt{t}$ no se invierte) y la velocidad infinita ($G>0$ en todo $x$).

> [!referencia]
> - De dónde sale la ecuación: [[Derivacion del Calor]].
> - El caso acotado (espectro discreto): [[Separacion Calor Dirichlet]].
> - El índice del tema: [[Ecuacion del Calor/index]].
