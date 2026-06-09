---
title: Método de Wiener-Hopf
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - singulares
  - analisis-complejo
draft: false
aliases:
  - método de Wiener-Hopf
  - técnica de Wiener-Hopf
  - factorización de Wiener-Hopf
  - Wiener-Hopf method
  - ecuación de convolución en el semieje
---

# Método de Wiener-Hopf

> [!definicion]
> El **método de Wiener-Hopf** es la técnica para resolver **ecuaciones de convolución sobre el semieje**
> $[0,\infty)$, esto es, ecuaciones de la forma
> $$\varphi(x)=f(x)+\int_0^{\infty} K(x-t)\,\varphi(t)\,dt,\qquad x>0,$$
> (o su versión de primera especie). Aunque el núcleo $K(x-t)$ es de **convolución** —lo que invitaría a
> usar [[Transformada de Fourier| Fourier]]—, el **semieje** rompe el teorema de convolución: la integral
> no recorre toda la recta, así que $\widehat{K\!*\!\varphi}\neq\hat K\hat\varphi$ globalmente. La idea de
> Wiener y Hopf es **extender** el problema a toda la recta introduciendo una incógnita auxiliar y
> resolverlo por **factorización en el plano complejo**.

> [!info]
> Sección [[Singulares/index| Singulares]] del capítulo
> [[3 Ecuaciones Integrales/index| Ecuaciones Integrales]]. Es el primo de la
> [[Nucleo de Cauchy y Riemann-Hilbert| ecuación singular de Cauchy]] cuando el contorno es la **recta
> real** y el núcleo es de convolución: la factorización $G=X^+/X^-$ de Riemann-Hilbert se vuelve aquí
> la factorización en semiplanos. Emparenta con las [[Ecuaciones de Convolucion| ecuaciones de convolución]] sobre toda la recta (resolubles con Fourier sin más). Fuente: **Krasnov, Kiseliov,
> Makarenko**, *Ecuaciones integrales* (panorama).

---

## Ejemplo

> [!ejemplo] Factorización en semiplanos del plano complejo
> ![[wiener_hopf.svg|470]]
>
> El plano complejo de la variable de Fourier $\xi$ se **parte** en dos semiplanos. La función
> $G_+(\xi)$ es analítica y no nula en el **semiplano superior** $\operatorname{Im}\xi>0$ (allí donde es
> analítica la transformada de algo soportado en $x>0$), y $G_-(\xi)$ lo es en el **inferior**
> $\operatorname{Im}\xi<0$. Ambas coinciden en una **franja común** que contiene al eje real. La
> factorización $1-\hat K(\xi)=G_+(\xi)\,G_-(\xi)$ separa la incógnita en sus partes analíticas
> "arriba" y "abajo"; el teorema de Liouville las pega en una función entera (un polinomio), y de ahí se
> despeja la solución.

---

## En qué consiste

> [!teoria] La factorización (idea central)
> **Paso 1 — Extender a toda la recta.** La ecuación solo vale para $x>0$; el miembro derecho no está
> definido para $x<0$. Definimos ahí una **incógnita auxiliar** $\varphi_-(x)$ (lo que "falta" para que la
> identidad valga en toda la recta) y partimos $\varphi=\varphi_+ +\varphi_-$, con $\varphi_+$ soportada
> en $x>0$ y $\varphi_-$ en $x<0$. Ahora la ecuación rige en **toda** $\mathbb{R}$.
>
> **Paso 2 — Transformar.** Tomando Fourier, la convolución sí se vuelve producto. Aparece la **ecuación
> de Wiener-Hopf en el plano de frecuencias**
> $$\Phi_+(\xi)\,\big[1-\hat K(\xi)\big]+\Phi_-(\xi)=F(\xi),$$
> donde $\Phi_+$ es analítica en el semiplano **superior** (transformada de algo en $x>0$) y $\Phi_-$ en
> el **inferior** (algo en $x<0$). El reto: una sola ecuación con dos incógnitas analíticas en mitades
> distintas del plano.
>
> **Paso 3 — Factorizar el símbolo.** La clave del método es escribir
> $$1-\hat K(\xi)=G_+(\xi)\,G_-(\xi),$$
> con $G_+$ analítica y **sin ceros** en el semiplano superior, y $G_-$ análoga en el inferior. Tal
> factorización existe (vía la integral de Cauchy del logaritmo, igual que en
> [[Nucleo de Cauchy y Riemann-Hilbert| Riemann-Hilbert]]) siempre que $1-\hat K$ no se anule en el eje
> real y tenga **índice cero**.
>
> **Paso 4 — Separar y aplicar Liouville.** Dividiendo por $G_-$ y descomponiendo el término libre
> $F/G_-=[\,\cdot\,]_+ +[\,\cdot\,]_-$ en sus partes analíticas arriba/abajo, se reordena la ecuación
> hasta que **un lado es analítico en el semiplano superior y el otro en el inferior**, y ambos coinciden
> en la franja común. Definen entonces una **única función entera**; por el comportamiento en el infinito
> (Liouville), esa función es un **polinomio** (a menudo $0$). Igualándola se **despeja $\Phi_+$**, y
> $\varphi$ se recupera por transformada inversa.

> [!info] Aplicaciones célebres
> Wiener-Hopf nació en astrofísica (transporte radiativo) y es hoy una herramienta canónica:
> - **Difracción de Sommerfeld**: la difracción de una onda por el **borde de una pantalla**
>   semiinfinita es el ejemplo histórico que dio fama al método (Copson, Jones).
> - **Teoría de colas y de riesgo**: la probabilidad de ruina y la distribución estacionaria de la cola
>   $G/G/1$ se obtienen factorizando el símbolo de un paseo aleatorio en el semieje.
> - **Fractura y contacto**: problemas de grieta y de contacto elástico semiinfinito.

> [!proposicion] Relación con Riemann-Hilbert
> Wiener-Hopf **es** el problema de Riemann-Hilbert con contorno $L=\mathbb{R}$ y símbolo de **convolución**
> $G(\xi)=1-\hat K(\xi)$. La factorización en semiplanos $G=G_+G_-$ es la versión recta de
> $G=X^+/X^-$, y el **índice** (número de giro de $G$ a lo largo del eje real) decide de nuevo el número
> de soluciones y condiciones de solubilidad. Lo que en Riemann-Hilbert era "dentro/fuera del contorno"
> aquí es "semiplano superior/inferior".

> [!warning] Panorama, no algoritmo universal
> La factorización **explícita** $1-\hat K=G_+G_-$ solo es sencilla en casos especiales (símbolos
> racionales, ciertos núcleos exponenciales). En general $G_\pm$ se da por una **integral de Cauchy del
> logaritmo** que rara vez se evalúa en forma cerrada, y si el **índice** no es cero hay que extraer
> primero factores $(\xi\pm i)^{\kappa}$. Por eso Wiener-Hopf es más un **marco conceptual** —reducir a
> factorización de funciones analíticas en semiplanos— que una receta cerrada de aplicación automática.

## Resumen

> [!resumen]
> | Objeto | Expresión | Papel |
> |---|---|---|
> | Ecuación | $\varphi(x)=f(x)+\displaystyle\int_0^{\infty}\!K(x-t)\varphi(t)\,dt$ | convolución en el semieje |
> | Obstrucción | semieje rompe $\widehat{K\!*\!\varphi}=\hat K\hat\varphi$ | Fourier sola no basta |
> | Extensión | $\varphi=\varphi_+ +\varphi_-$, auxiliar en $x<0$ | ecuación en toda $\mathbb{R}$ |
> | En frecuencias | $\Phi_+[1-\hat K]+\Phi_-=F$ | dos analíticas, semiplanos opuestos |
> | Factorización | $1-\hat K=G_+G_-$ | $G_+$ analítica arriba, $G_-$ abajo |
> | Cierre | Liouville $\Rightarrow$ polinomio | despejar $\Phi_+$, antitransformar |

> [!corolario]
> El método de Wiener-Hopf resuelve convoluciones en el **semieje** extendiendo a la recta y
> **factorizando el símbolo** $1-\hat K=G_+G_-$ en partes analíticas en semiplanos opuestos; tras separar,
> Liouville pega ambas en un polinomio y se despeja la solución. Es la encarnación de
> [[Nucleo de Cauchy y Riemann-Hilbert| Riemann-Hilbert]] sobre la recta con núcleo de convolución, y
> brilla en difracción, colas y fractura —aunque la factorización explícita rara vez sea elemental.

> [!referencia]
> - El marco complejo general: [[Nucleo de Cauchy y Riemann-Hilbert]].
> - El caso fácil (recta completa): [[Ecuaciones de Convolucion]].
> - El mapa de la sección: [[Singulares/index]].
