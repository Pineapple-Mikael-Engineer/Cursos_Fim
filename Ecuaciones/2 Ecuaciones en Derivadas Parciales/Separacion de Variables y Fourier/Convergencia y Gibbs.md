---
title: Convergencia y Fenómeno de Gibbs
order: 4
tags:
  - ecuaciones
  - edp
  - teoria
  - fourier
  - convergencia
draft: false
aliases:
  - convergencia de Fourier
  - teorema de Dirichlet
  - fenómeno de Gibbs
  - sobreimpulso de Gibbs
  - Fourier convergence
  - Gibbs phenomenon
---

# Convergencia de Series de Fourier y Fenómeno de Gibbs

> [!definicion]
> La serie de Fourier de una función **suave a trozos** $f$ converge —**teorema de Dirichlet**— al propio valor $f(x)$ en cada punto de **continuidad**, y al **promedio del salto**
> $$\frac{f(x^+)+f(x^-)}{2}$$
> en cada punto de **discontinuidad** (donde $f(x^\pm)$ son los límites por la derecha y por la izquierda). Cerca de un salto, las **sumas parciales** $S_N$ no se acercan ordenadamente: producen un **sobreimpulso** —el **fenómeno de Gibbs**— de aproximadamente un $\boldsymbol{9\%}$ de la altura del salto, que **no desaparece** al aumentar $N$: solo se **estrecha** y se aprieta contra la discontinuidad.

> [!info]
> Cierra el bloque sobre [[Series de Fourier]]: una vez que sabemos **construir** los coeficientes, esta nota responde **en qué sentido** la serie reproduce a $f$. Es el reverso teórico de [[Identidad de Parseval]] (convergencia en energía) y vive en [[Separacion de Variables y Fourier/index| Separación de Variables y Fourier]], dentro del capítulo de [[2 Ecuaciones en Derivadas Parciales/index| Ecuaciones en Derivadas Parciales]]. El motivo de preocuparse: al resolver una EDP con dato inicial discontinuo, la serie **siempre** convergerá en media, pero el perfil truncado mostrará oscilaciones.

---

## Ejemplo

> [!ejemplo] La onda cuadrada: Gibbs en acción
> Tomemos la función impar de período $2\pi$ con $f(x)=1$ en $(0,\pi)$ y $f(x)=-1$ en $(-\pi,0)$ —la **onda cuadrada**, de salto $2$ en $x=0$—. Su serie de Fourier es solo de senos impares:
> $$f(x)=\frac{4}{\pi}\sum_{k=0}^{\infty}\frac{\operatorname{sen}\big((2k+1)x\big)}{2k+1}
> =\frac{4}{\pi}\Big(\operatorname{sen}x+\tfrac13\operatorname{sen}3x+\tfrac15\operatorname{sen}5x+\cdots\Big).$$
> **Dónde converge.** En $x=\tfrac{\pi}{2}$ (continuidad) la serie da $1$, el valor de $f$. En $x=0$ (salto) **cada** término $\operatorname{sen}(0)=0$, así que la serie vale $0$ — exactamente el promedio $\tfrac{1+(-1)}{2}=0$. El teorema de Dirichlet se cumple punto a punto.
>
> **El sobreimpulso.** Por más armónicos que sumemos, la suma parcial $S_N$ **se pasa** del valor $1$ justo antes del salto, alcanzando un pico cercano a
> $$S_N^{\max}\approx \frac{2}{\pi}\int_0^{\pi}\frac{\operatorname{sen}t}{t}\,dt\approx 1{.}0895\cdots,$$
> es decir un **$\approx 9\%$** por encima de la altura $1$ (un $\approx 18\%$ medido sobre el salto completo de $2$). El pico se acerca cada vez más a $x=0$ al crecer $N$, pero su **altura no baja**.

---

## En qué consiste

> [!teoria] Tres modos de convergencia: no son lo mismo
> Decir "$S_N\to f$" es ambiguo; hay tres sentidos distintos, y Gibbs vive en la grieta entre ellos.
> - **Puntual (Dirichlet).** Para **cada** $x$ fijo, $S_N(x)\to f(x)$ (o al promedio en los saltos) si $f$ es suave a trozos. Es convergencia "punto por punto", y cada punto puede ir a su ritmo.
> - **Uniforme.** $\max_x|S_N(x)-f(x)|\to0$: la **peor** discrepancia tiende a cero, así que se puede dibujar una franja $\pm\varepsilon$ que la serie respeta a partir de cierto $N$. Se cumple **solo si $f$ es continua** (y suave a trozos): **sin saltos**. Donde hay un salto, el error máximo se queda anclado en el $\approx 9\%$ y **nunca** baja → **no** hay convergencia uniforme: ahí vive Gibbs.
> - **En media cuadrática ($L^2$).** $\int |S_N-f|^2\,dx\to0$: la **energía del error** tiende a cero. Se cumple **siempre** que $f$ sea de cuadrado integrable ($\int f^2<\infty$), aunque tenga saltos. El sobreimpulso de Gibbs es real pero ocupa una franja cada vez más **estrecha**, así que su contribución al **área** del error al cuadrado se desvanece.

> [!teorema] Convergencia de Dirichlet
> Sea $f$ periódica y **suave a trozos** (continua salvo en un número finito de saltos, con $f$ y $f'$ acotadas a trozos). Entonces para todo $x$:
> $$\lim_{N\to\infty}S_N(x)=\frac{f(x^+)+f(x^-)}{2}.$$
> En particular, $S_N(x)\to f(x)$ donde $f$ es continua, y converge al **punto medio** del salto donde no lo es.

> [!proposicion] Por qué el $9\%$ no se va (origen de Gibbs)
> La suma parcial puede escribirse como una convolución con el **núcleo de Dirichlet** $D_N$. Cerca del salto, al reescalar $x=\pi s/N$ alrededor de la discontinuidad, $S_N$ tiende a una curva **fija** gobernada por la **integral del seno cardinal**:
> $$\operatorname{Si}(\pi)=\int_0^{\pi}\frac{\operatorname{sen}t}{t}\,dt\approx 1{.}8519.$$
> El pico de esa curva límite vale $\tfrac{2}{\pi}\operatorname{Si}(\pi)\approx 1{.}0895$ por unidad de altura del salto. Como ese **límite no depende de $N$**, el sobreimpulso del $\approx 9\%$ es una constante universal: aumentar $N$ solo **comprime** la curva hacia el salto, sin rebajar su pico.

> [!warning]
> Gibbs **no es un error** de la serie ni un fallo de cálculo: es inevitable al truncar una serie que representa un salto. La convergencia $L^2$ **sí** se cumple (la serie es correcta "en energía"). En **procesamiento de señales** importa mucho: truncar el espectro de una señal con bordes abruptos introduce el **rizado de Gibbs** (artefactos de sobreimpulso en imágenes y audio). El remedio práctico no es sumar más términos —el pico persiste— sino **suavizar** la truncación con un *ventaneo* (factores de Fejér/Lanczos) que atenúa los armónicos altos.

## Resumen

> [!resumen]
> | Modo | Qué tiende a $0$ | Condición sobre $f$ | ¿Aguanta saltos? |
> |:--|:--|:--|:--:|
> | Puntual (Dirichlet) | $\|S_N(x)-f(x)\|$ en cada $x$ | suave a trozos | sí (→ promedio) |
> | Uniforme | $\max_x\|S_N-f\|$ | **continua** y suave a trozos | **no** (Gibbs) |
> | Media cuadrática $L^2$ | $\int\|S_N-f\|^2\,dx$ | cuadrado integrable | sí |

> [!corolario]
> Una función suave a trozos siempre tiene serie de Fourier convergente **en media**, y puntualmente al promedio en los saltos. Solo la continuidad garantiza convergencia **uniforme**; donde falta, el fenómeno de Gibbs fija un sobreimpulso del $\approx 9\%$ del salto que **ningún** número de términos elimina. Truncar no es lo mismo que aproximar bien en todos los sentidos.

> [!referencia]
> - De dónde salen los coeficientes que se suman: [[Series de Fourier]].
> - Convergencia medida en energía y completitud de la base: [[Identidad de Parseval]].
> - El método que produce estas series al resolver EDP: [[Separacion de Variables y Fourier/index]].
