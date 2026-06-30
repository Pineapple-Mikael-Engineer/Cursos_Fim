---
title: Ecuaciones Diferenciales Fraccionarias
order: 8
tags:
  - ecuaciones
  - difero-integrales
  - teoria
  - calculo-fraccionario
  - ecuaciones-fraccionarias
draft: false
aliases:
  - ecuaciones diferenciales fraccionarias
  - EDF
  - ecuación de relajación fraccionaria
  - fractional differential equations
---

# Ecuaciones Diferenciales Fraccionarias (EDF)

> [!definicion]
> Una **ecuación diferencial fraccionaria (EDF)** es aquella en la que las derivadas de orden entero se sustituyen por **derivadas fraccionarias**, por ejemplo
> $$D^{\alpha}_{C}\varphi(t)=f\big(t,\varphi(t)\big),\qquad 0<\alpha\le1\ \ (\text{o } 1<\alpha\le2),$$
> donde $D^{\alpha}_{C}$ es la [[Derivada de Caputo| derivada de Caputo]] de orden $\alpha$. Las EDF **lineales con coeficientes constantes** se resuelven aplicando la [[Laplace de Derivadas Fraccionarias| transformada de Laplace]] y antitransformando con la [[Funcion de Mittag-Leffler| función de Mittag-Leffler]] $E_\alpha$, que hace en este mundo el papel que la exponencial $e^{\lambda t}$ hace en las EDO ordinarias.

> [!info]
> Esta nota vive en [[Calculo Fraccionario/index| Cálculo Fraccionario]], dentro del capítulo [[4 Ecuaciones Difero-integrales/index| Ecuaciones Difero-integrales]]. Es la pieza que **junta** todo lo demás del capítulo: usa la [[Derivada de Caputo| derivada de Caputo]] como operador, la [[Laplace de Derivadas Fraccionarias| Laplace fraccional]] como método y la [[Funcion de Mittag-Leffler| función de Mittag-Leffler]] como solución. Para ver dónde estas ecuaciones modelan el mundo real, vaya a [[Aplicaciones Fraccionarias| aplicaciones fraccionarias]].

---

## Ejemplo

> [!ejemplo] Oscilación fraccionaria: entre relajar y oscilar ($1<\alpha<2$)
> Consideremos la **ecuación de oscilación fraccionaria**
> $$D^{\alpha}_{C}\varphi(t)=-\varphi(t),\qquad \varphi(0)=1,\quad \varphi'(0)=0,\qquad 1<\alpha<2.$$
> Como veremos en el teorema, su solución es $\varphi(t)=E_\alpha(-t^{\alpha})$. Lo interesante es lo que ocurre al **mover el orden** $\alpha$:
> - en $\alpha=1$ la ecuación es $\varphi'=-\varphi$ y da la **relajación exponencial** $e^{-t}$ (decae, no oscila);
> - en $\alpha=2$ la ecuación es $\varphi''=-\varphi$ y da la **oscilación pura** $\cos t$ (oscila, no decae);
> - para $1<\alpha<2$ la solución **interpola** entre ambos: $\varphi(t)$ **oscila** (cruza cero, tiene crestas) pero con una **amplitud que decae** lentamente, como un coseno amortiguado.
>
> Físicamente, $\alpha$ es una perilla continua entre "un sistema que solo se relaja" y "un sistema que solo vibra": las EDF describen el continuo de comportamientos intermedios que la física entera salta.

---

## En qué consiste

> [!teoria]
> La idea estructural es sencilla. En una EDO lineal de coeficientes constantes, proponer $e^{\lambda t}$ convierte derivadas en multiplicaciones por $\lambda$ y reduce la ecuación a un polinomio. En una EDF ocurre **lo mismo pero en el dominio de Laplace**: la derivada de Caputo de orden $\alpha$ se transforma multiplicando por $s^{\alpha}$ (más términos de las condiciones iniciales), de modo que la ecuación se vuelve **algebraica en $s$** —solo que con potencias **fraccionarias** $s^{\alpha}$—. Despejada $\Phi(s)$, la antitransformada de las expresiones del tipo $s^{\alpha-1}/(s^{\alpha}+\lambda)$ es exactamente una [[Funcion de Mittag-Leffler| función de Mittag-Leffler]]. Toda la teoría lineal se reduce, pues, a este triángulo: **Caputo $\to$ Laplace $\to$ Mittag-Leffler**.

> [!algoritmo] Resolver una EDF lineal de coeficientes constantes
> 1. **Transformar (Laplace).** Aplicar $\mathcal{L}$ a la ecuación usando la regla de Caputo $\mathcal{L}\{D^{\alpha}_{C}\varphi\}=s^{\alpha}\Phi(s)-\sum_{k=0}^{m-1}s^{\alpha-1-k}\varphi^{(k)}(0)$, con $m=\lceil\alpha\rceil$ (las condiciones iniciales son las **clásicas** $\varphi(0),\varphi'(0),\dots$).
> 2. **Despejar $\Phi(s)$.** Resolver algebraicamente; aparecerá el bloque característico $s^{\alpha}$.
> 3. **Antitransformar (Mittag-Leffler).** Reconocer las formas $\dfrac{s^{\alpha-\beta}}{s^{\alpha}+\lambda}$ e invertirlas con $\mathcal{L}^{-1}\!\big\{\tfrac{s^{\alpha-\beta}}{s^{\alpha}+\lambda}\big\}=t^{\beta-1}E_{\alpha,\beta}(-\lambda t^{\alpha})$.

> [!teorema] Relajación fraccionaria
> El problema de **relajación fraccionaria**
> $$D^{\alpha}_{C}\varphi(t)=-\lambda\,\varphi(t),\qquad \varphi(0)=1,\qquad 0<\alpha\le1,\ \lambda>0,$$
> tiene por solución la función de Mittag-Leffler
> $$\varphi(t)=E_\alpha(-\lambda\,t^{\alpha}).$$

> [!demostracion] Por transformada de Laplace
> **Paso 1 — transformar la ecuación.** Como $0<\alpha\le1$ se tiene $m=1$, y la regla de Caputo da $\mathcal{L}\{D^{\alpha}_{C}\varphi\}=s^{\alpha}\Phi(s)-s^{\alpha-1}\varphi(0)$. Aplicando $\mathcal{L}$ a ambos lados de $D^{\alpha}_{C}\varphi=-\lambda\varphi$ con $\varphi(0)=1$:
> $$s^{\alpha}\Phi(s)-s^{\alpha-1}=-\lambda\,\Phi(s).$$
> **Paso 2 — despejar $\Phi(s)$.** Agrupando los términos en $\Phi$:
> $$\big(s^{\alpha}+\lambda\big)\Phi(s)=s^{\alpha-1}\quad\Longrightarrow\quad \Phi(s)=\frac{s^{\alpha-1}}{s^{\alpha}+\lambda}.$$
> **Paso 3 — antitransformar.** Por la fórmula de Laplace de Mittag-Leffler $\mathcal{L}\{E_\alpha(-\lambda t^{\alpha})\}=\dfrac{s^{\alpha-1}}{s^{\alpha}+\lambda}$ (es el caso $\beta=1$ de $\mathcal{L}\{t^{\beta-1}E_{\alpha,\beta}(-\lambda t^{\alpha})\}=\tfrac{s^{\alpha-\beta}}{s^{\alpha}+\lambda}$), la inversión es inmediata:
> $$\varphi(t)=\mathcal{L}^{-1}\!\left\{\frac{s^{\alpha-1}}{s^{\alpha}+\lambda}\right\}=E_\alpha(-\lambda\,t^{\alpha}).$$
> En $\alpha=1$ esto recupera $\varphi(t)=e^{-\lambda t}$, la relajación exponencial clásica. $\blacksquare$

> [!proposicion] Estructura de la solución general lineal
> Para una EDF lineal con coeficientes constantes y término fuente, la solución se escribe como
> $$\varphi(t)=\underbrace{\sum_{k}c_k\,t^{\beta_k-1}E_{\alpha,\beta_k}(-\lambda t^{\alpha})}_{\text{respuesta libre (condiciones iniciales)}}+\underbrace{\int_0^{t}G(t-\tau)\,f(\tau)\,d\tau}_{\text{respuesta forzada (convolución)}},$$
> donde el **núcleo** $G$ es también de tipo Mittag-Leffler. La novedad frente al caso entero es que $G$ tiene **cola de ley de potencias**: el sistema "recuerda" su historia (ver [[Ecuaciones con Memoria]]).

> [!warning]
> Para EDF **no lineales** $D^{\alpha}_{C}\varphi=f(t,\varphi)$ la existencia y unicidad **no** se siguen sin más del teorema de Picard clásico: la presencia de **memoria** convierte la ecuación en una ecuación integral con núcleo singular $\sim(t-\tau)^{\alpha-1}$, y hay que rehacer el argumento de punto fijo con cuidado (condiciones de Lipschitz adaptadas, pesos en la norma). No suponga que "todo lo de las EDO traslada igual": el orden $\alpha$ cambia la teoría, no solo la fórmula.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Forma general | $D^{\alpha}_{C}\varphi=f(t,\varphi)$, $0<\alpha\le1$ o $1<\alpha\le2$ |
> | Método (lineal) | Laplace $\to$ despejar $\Phi(s)$ $\to$ Mittag-Leffler |
> | Regla de Caputo | $\mathcal{L}\{D^{\alpha}_{C}\varphi\}=s^{\alpha}\Phi-\sum_{k}s^{\alpha-1-k}\varphi^{(k)}(0)$ |
> | Relajación | $D^{\alpha}_{C}\varphi=-\lambda\varphi,\ \varphi(0)=1\Rightarrow\varphi=E_\alpha(-\lambda t^{\alpha})$ |
> | Oscilación ($1<\alpha<2$) | $E_\alpha(-t^{\alpha})$ interpola coseno $\leftrightarrow$ exponencial |
> | Cuidado | unicidad no lineal $\neq$ Picard clásico (memoria) |

> [!corolario]
> Una EDF es una EDO "con perilla": el orden $\alpha$ es un parámetro continuo que sintoniza el sistema entre regímenes que la física de orden entero solo conoce por separado (relajar en $\alpha=1$, oscilar en $\alpha=2$). Resolverlas es, casi siempre, reconocer una función de Mittag-Leffler tras una transformada de Laplace.

> [!referencia]
> - La solución universal: [[Funcion de Mittag-Leffler]].
> - El método: [[Laplace de Derivadas Fraccionarias]].
> - El operador: [[Derivada de Caputo]].
> - Dónde se usan: [[Aplicaciones Fraccionarias]].
> - Índice del tema: [[Calculo Fraccionario/index]].
