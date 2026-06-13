---
title: Conceptos Fundamentales
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - clasificacion
draft: false
aliases:
  - conceptos fundamentales
  - clasificación de ecuaciones integrales
  - núcleo
  - especie y familia
  - fundamentals of integral equations
---

# Conceptos Fundamentales

> [!definicion]
> Una **ecuación integral** es una ecuación en la que la función incógnita $\varphi$ aparece **bajo el
> signo de una integral**. La forma lineal general es
> $$\alpha(x)\,\varphi(x)=f(x)+\lambda\int K(x,t)\,\varphi(t)\,dt,$$
> donde $K(x,t)$ es el **núcleo**, $f(x)$ el **término libre**, $\lambda$ un **parámetro** y la incógnita
> es $\varphi$. Se clasifican por **dos ejes independientes**:
> - **Familia** — según los límites de integración:
>   - **Volterra**: límite superior **variable**, $\displaystyle\int_0^x K(x,t)\varphi(t)\,dt$.
>   - **Fredholm**: límites **fijos**, $\displaystyle\int_a^b K(x,t)\varphi(t)\,dt$.
> - **Especie** — según dónde aparece $\varphi$:
>   - **Primera especie**: $\varphi$ aparece **solo dentro** de la integral, $f=\lambda\int K\varphi$.
>   - **Segunda especie**: $\varphi$ aparece **dentro y fuera**, $\varphi=f+\lambda\int K\varphi$.
>
> Se llama **homogénea** cuando $f\equiv 0$.

> [!info]
> Nota de entrada del capítulo [[3 Ecuaciones Integrales/index| Ecuaciones Integrales]]: fija el
> vocabulario que se usa en todo lo que sigue. El paralelismo con lo diferencial se desarrolla en
> [[Nexo EDO e Integrales]]; las dos familias tienen su desarrollo propio en [[Volterra/index| Volterra]]
> y [[Fredholm/index| Fredholm]]. La fuente de referencia es **Krasnov, Kiseliov, Makarenko**, *Ecuaciones
> integrales*.

---

## Ejemplo

> [!ejemplo] Clasificar cuatro ecuaciones
> Para cada ecuación identificamos **familia** (Volterra/Fredholm), **especie** (1ª/2ª) y si es
> **homogénea**.
>
> **(a)** $\displaystyle \varphi(x)=x^2+\lambda\int_0^x (x-t)\,\varphi(t)\,dt.$
> Límite superior $x$ **variable** $\Rightarrow$ **Volterra**. La $\varphi$ aparece **fuera** (a la
> izquierda) y dentro $\Rightarrow$ **segunda especie**. Como $f(x)=x^2\not\equiv0$, **no es homogénea**.
> Núcleo $K(x,t)=x-t$.
>
> **(b)** $\displaystyle \operatorname{sen}x=\int_0^1 e^{xt}\,\varphi(t)\,dt.$
> Límites $0$ y $1$ **fijos** $\Rightarrow$ **Fredholm**. La $\varphi$ aparece **solo dentro**
> $\Rightarrow$ **primera especie**. El término libre es $f(x)=\operatorname{sen}x$. Núcleo
> $K(x,t)=e^{xt}$.
>
> **(c)** $\displaystyle \varphi(x)=\lambda\int_0^{\pi}\cos(x-t)\,\varphi(t)\,dt.$
> Límites fijos $\Rightarrow$ **Fredholm**; $\varphi$ dentro y fuera $\Rightarrow$ **segunda especie**;
> $f\equiv0\Rightarrow$ **homogénea**. Es un **problema de autovalores**: se buscan los valores de
> $\lambda$ para los que existe $\varphi\not\equiv0$ (las **funciones propias**).
>
> **(d)** $\displaystyle x=\int_0^x\frac{\varphi(t)}{\sqrt{x-t}}\,dt.$
> Límite variable $\Rightarrow$ **Volterra de primera especie** con núcleo **singular** (ver
> [[Problema de Abel]]).
>
> **Resumen del ejemplo.**
> | Ecuación | Familia | Especie | $f\equiv0$ | Núcleo |
> |---|---|---|---|---|
> | (a) | Volterra | 2ª | no | $x-t$ (convolución) |
> | (b) | Fredholm | 1ª | no | $e^{xt}$ (degenerado) |
> | (c) | Fredholm | 2ª | sí (autovalores) | $\cos(x-t)$ (simétrico) |
> | (d) | Volterra | 1ª | no | $1/\sqrt{x-t}$ (singular) |

---

## En qué consiste

> [!teoria] Los dos ejes, con más detalle
> La clasificación responde a **dos preguntas independientes**, y de ellas depende **qué método** sirve.
>
> **Eje 1 — la familia (¿límites fijos o variables?).**
> - En **Volterra** el límite superior es la propia variable $x$: la integral "acumula" la información
>   desde un inicio hasta $x$, igual que un PVI acumula desde la condición inicial. Por eso una Volterra
>   de segunda especie **siempre tiene solución única** (se parece a integrar).
> - En **Fredholm** los límites $a,b$ son fijos: el valor de $\varphi$ en cada punto depende de **todo**
>   el intervalo a la vez. Es un problema **global**, como un PVF, y puede tener una, ninguna o infinitas
>   soluciones (aparece el **espectro**).
>
> **Eje 2 — la especie (¿$\varphi$ fuera de la integral?).**
> - En **segunda especie**, $\varphi=f+\lambda\int K\varphi$, la incógnita aparece "sola" fuera. El
>   operador es $(\mathbb{1}-\lambda \mathcal{K})\varphi=f$, una **perturbación de la identidad**: bien
>   condicionado, invertible salvo en valores especiales de $\lambda$.
> - En **primera especie**, $f=\lambda\int K\varphi$, hay que **deshacer** la integral. Como integrar
>   suaviza, invertir **deriva** y amplifica el ruido: es un **problema inverso** delicado.

> [!info] Tipos de núcleo $K(x,t)$
> El núcleo decide el método. Conviene reconocerlo de un vistazo.
> | Tipo | Forma | Por qué importa |
> |---|---|---|
> | **Degenerado / separable** | $K(x,t)=\sum_{i=1}^{n} a_i(x)\,b_i(t)$ | reduce la ecuación a un **sistema algebraico** $n\times n$ |
> | **Simétrico** | $K(x,t)=K(t,x)$ | espectro **real**, funciones propias **ortogonales** (teoría de Hilbert-Schmidt) |
> | **De convolución** | $K(x,t)=K(x-t)$ | se ataca con **transformada de Laplace** (Volterra) o Fourier (Fredholm) |
> | **Singular** | $K\to\infty$ en algún punto, p.ej. $1/\sqrt{x-t}$ | la integral aún converge, pero la inversión es delicada (ver [[Problema de Abel]]) |
> | **Continuo (regular)** | $K$ acotado y continuo | caso "amable": resolvente y aproximaciones sucesivas convergen |

> [!proposicion] Lineal frente a no lineal
> La ecuación es **lineal** si $\varphi$ entra de forma lineal: $\varphi$ y $\int K\varphi$ aparecen a la
> primera potencia y no compuestas con funciones no lineales. Si en cambio aparece, por ejemplo,
> $$\varphi(x)=f(x)+\lambda\int_a^b K(x,t)\,\big[\varphi(t)\big]^2\,dt
> \qquad\text{o}\qquad
> \varphi(x)=f(x)+\lambda\int_a^b K\big(x,t,\varphi(t)\big)\,dt,$$
> la ecuación es **no lineal** (ecuaciones de [[No Lineales/index| Hammerstein y Urysohn]]). Todo este
> capítulo —salvo esa sección— trata el caso **lineal**.

> [!teoria] Por qué la especie es lo que más importa
> La segunda especie suele ser **bien planteada** (well-posed): el operador $\mathbb{1}-\lambda\mathcal K$
> está "cerca" de la identidad, la solución existe, es única y depende **continuamente** de $f$. Es la
> situación de la mayoría de los métodos del capítulo (resolvente, Neumann, espectro de Fredholm).
>
> La primera especie suele ser un **problema inverso mal planteado** (ill-posed): la integral
> $\int K\varphi$ **suaviza** $\varphi$ (atenúa las oscilaciones rápidas), de modo que la operación
> inversa **amplifica** justamente esas oscilaciones. Dos términos libres $f$ casi iguales pueden provenir
> de $\varphi$ muy distintas: pequeños errores de medida en $f$ se disparan al reconstruir $\varphi$. Por
> eso requiere **regularización** (Tikhonov, truncado espectral). El caso resoluble por excelencia es la
> [[Problema de Abel| ecuación de Abel]].

> [!algoritmo] Clasificar una ecuación integral dada
> 1. **¿Dónde está $\varphi$?** Si aparece **fuera** de la integral (sola, o con un coeficiente
>    $\alpha(x)$) $\to$ **2ª especie**; si aparece **solo dentro** $\to$ **1ª especie**.
> 2. **Mira los límites.** Si el límite superior **depende de $x$** $\to$ **Volterra**; si ambos son
>    **constantes** $\to$ **Fredholm**.
> 3. **¿$f\equiv0$?** En tal caso es **homogénea** (típicamente un problema de autovalores).
> 4. **Identifica el núcleo**: ¿separable, simétrico, de convolución $K(x-t)$, singular? Eso fija el
>    método.
> 5. **¿Es lineal?** Comprueba que $\varphi$ no aparezca elevada a potencias ni dentro de funciones no
>    lineales.

> [!warning]
> No confundir los ejes: "Volterra/Fredholm" (familia) y "1ª/2ª especie" son **independientes** —existen
> las cuatro combinaciones—. Y un **límite variable** no es lo mismo que un **núcleo de convolución**:
> Volterra se refiere a los límites; convolución, a que $K$ dependa solo de $x-t$.

## Resumen

> [!resumen]
> | Eje | Opciones | Cómo reconocerlo | Consecuencia |
> |---|---|---|---|
> | Familia | Volterra / Fredholm | límite superior $x$ / límites $a,b$ fijos | local (siempre soluble) / global (espectral) |
> | Especie | 2ª / 1ª | $\varphi$ fuera y dentro / solo dentro | bien planteada / inversa mal planteada |
> | Homogeneidad | $f\not\equiv0$ / $f\equiv0$ | hay término libre / no lo hay | inhomogénea / autovalores |
> | Núcleo | degenerado / simétrico / convolución / singular | forma de $K(x,t)$ | álgebra / espectro / Laplace / regularización |
> | Linealidad | lineal / no lineal | $\varphi$ a la 1ª potencia / no | métodos del capítulo / Hammerstein-Urysohn |

> [!corolario]
> Antes de resolver, **clasificar**: familia (¿límites fijos?), especie (¿$\varphi$ fuera?) y tipo de
> núcleo. De esos tres datos se deduce casi todo: si el problema está bien planteado, si tendrá autovalores
> y qué herramienta usar. La regla de oro: **2ª especie = amable**, **1ª especie = inversa delicada**;
> **Volterra = local**, **Fredholm = global**.

> [!referencia]
> - El puente con lo diferencial: [[Nexo EDO e Integrales]].
> - La familia local: [[Volterra/index]].
> - La familia global y su espectro: [[Fredholm/index]].
> - El mapa completo del capítulo: [[3 Ecuaciones Integrales/index]].
