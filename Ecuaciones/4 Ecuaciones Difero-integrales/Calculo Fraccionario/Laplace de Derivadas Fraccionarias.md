---
title: Laplace de Derivadas Fraccionarias
tags:
  - ecuaciones
  - difero-integrales
  - teoria
  - calculo-fraccionario
  - transformada-de-laplace
draft: false
aliases:
  - transformada de Laplace de derivadas fraccionarias
  - Laplace fraccional
  - Laplace transform of fractional derivatives
---

# Laplace de Derivadas Fraccionarias

> [!definicion]
> La **transformada de Laplace** de las derivadas fraccionarias es la herramienta para resolver
> ecuaciones fraccionarias lineales: convierte el operador no local $D^{\alpha}$ en una multiplicación
> por $s^{\alpha}$. Para la **integral fraccionaria** la regla es la más limpia,
> $$\mathcal{L}\{I^{\alpha}f\}(s)=s^{-\alpha}F(s),\qquad F(s)=\mathcal{L}\{f\}(s),$$
> generalización directa de $\mathcal{L}\Big\{\int_0^t f\Big\}=\dfrac{F(s)}{s}$ (el caso $\alpha=1$).
> Para las **derivadas** aparecen términos de frontera, distintos según se use Caputo o Riemann-Liouville.

> [!info]
> Es el **motor** de las [[Ecuaciones Diferenciales Fraccionarias| ecuaciones diferenciales fraccionarias]]: pasar a $s$, despejar algebraicamente y antitransformar con la
> [[Funcion de Mittag-Leffler| función de Mittag-Leffler]]. Vive en el capítulo
> [[4 Ecuaciones Difero-integrales/index| Ecuaciones Difero-integrales]] y se apoya en la
> [[Transformada de Laplace/index| transformada de Laplace]] ordinaria. La elección entre
> [[Derivada de Caputo| Caputo]] y [[Derivada de Riemann-Liouville| Riemann-Liouville]] se decide
> precisamente por estos términos de frontera.

---

## Ejemplo

> [!ejemplo] Transformar $D^{1/2}_{C}f$ y reconocer la Laplace de Mittag-Leffler
> Sea $0<\alpha<1$ (aquí $\alpha=\tfrac12$, con $n=1$) y consideremos la ecuación de relajación
> fraccionaria $D^{\alpha}_{C}f(t)=\lambda f(t)$, con condición inicial **clásica** $f(0)=f_0$.
>
> **Paso 1 — transformar el lado izquierdo.** Por el teorema de Caputo con $n=1$ (solo $k=0$):
> $$\mathcal{L}\{D^{\alpha}_{C}f\}=s^{\alpha}F(s)-s^{\alpha-1}f(0)=s^{\alpha}F(s)-s^{\alpha-1}f_0.$$
> Para $\alpha=\tfrac12$: $\mathcal{L}\{D^{1/2}_{C}f\}=s^{1/2}F(s)-s^{-1/2}f_0$.
>
> **Paso 2 — transformar la ecuación.** El lado derecho es $\mathcal{L}\{\lambda f\}=\lambda F(s)$, así que
> $$s^{\alpha}F(s)-s^{\alpha-1}f_0=\lambda F(s).$$
>
> **Paso 3 — despejar $F(s)$.** Agrupando $F(s)$:
> $$F(s)\big(s^{\alpha}-\lambda\big)=s^{\alpha-1}f_0\quad\Longrightarrow\quad F(s)=f_0\,\frac{s^{\alpha-1}}{s^{\alpha}-\lambda}.$$
>
> **Paso 4 — antitransformar.** El cociente $\dfrac{s^{\alpha-1}}{s^{\alpha}-\lambda}$ es **exactamente**
> la transformada de Laplace de la [[Funcion de Mittag-Leffler| función de Mittag-Leffler]],
> $\mathcal{L}\{E_\alpha(\lambda t^{\alpha})\}=\dfrac{s^{\alpha-1}}{s^{\alpha}-\lambda}$. Por tanto
> $$f(t)=f_0\,E_\alpha(\lambda t^{\alpha}).$$
> Toda la dificultad del operador no local se ha resuelto **con álgebra** en el dominio $s$: ese es el
> poder de la Laplace fraccional.

---

## En qué consiste

> [!teorema] Laplace de las derivadas fraccionarias
> Sea $n-1<\alpha\le n$ y $F(s)=\mathcal{L}\{f\}(s)$.
> - **Caputo** (condiciones iniciales **clásicas**):
> $$\mathcal{L}\{D^{\alpha}_{C}f\}(s)=s^{\alpha}F(s)-\sum_{k=0}^{n-1}s^{\alpha-1-k}\,f^{(k)}(0).$$
> - **Riemann-Liouville** (condiciones iniciales **fraccionarias**):
> $$\mathcal{L}\{D^{\alpha}f\}(s)=s^{\alpha}F(s)-\sum_{k=0}^{n-1}s^{k}\,\big[D^{\alpha-1-k}f\big]_{t=0}.$$

> [!teoria]
> Las dos fórmulas son la **misma idea** —generalizar $\mathcal{L}\{f'\}=sF-f(0)$ con $s\to s^{\alpha}$—
> pero difieren en **qué** se evalúa en $t=0$:
> - Caputo pide $f(0),f'(0),\dots,f^{(n-1)}(0)$: **derivadas enteras ordinarias**, magnitudes físicas
>   medibles (posición, velocidad inicial…). Por eso la **física e ingeniería prefieren Caputo**: el
>   problema queda bien planteado con condiciones iniciales del laboratorio.
> - Riemann-Liouville pide $\big[D^{\alpha-1-k}f\big]_{t=0}$: **derivadas fraccionarias** en el origen,
>   sin lectura física directa y a menudo singulares.
>
> Salvo por esos términos de frontera, **ambas dan $s^{\alpha}F(s)$**: el operador diferencial
> fraccionario se "diagonaliza" igual que en el caso entero.

> [!demostracion] Caputo a partir de la integral fraccionaria (caso $0<\alpha<1$, $n=1$)
> **Paso 1 — definición de Caputo.** $D^{\alpha}_{C}f=I^{1-\alpha}f'$, la integral fraccionaria de la
> derivada ordinaria, con $\mathcal{L}\{I^{\beta}g\}=s^{-\beta}G(s)$.
>
> **Paso 2 — Laplace de la integral fraccionaria.** Con $\beta=1-\alpha$ y $g=f'$:
> $$\mathcal{L}\{D^{\alpha}_{C}f\}=s^{-(1-\alpha)}\,\mathcal{L}\{f'\}=s^{\alpha-1}\,\mathcal{L}\{f'\}.$$
>
> **Paso 3 — usar la regla entera $\mathcal{L}\{f'\}=sF(s)-f(0)$.**
> $$\mathcal{L}\{D^{\alpha}_{C}f\}=s^{\alpha-1}\big(sF(s)-f(0)\big)=s^{\alpha}F(s)-s^{\alpha-1}f(0),$$
> que es la fórmula del teorema con $n=1$. El caso general $n-1<\alpha\le n$ sale igual usando
> $D^{\alpha}_{C}f=I^{n-\alpha}f^{(n)}$ y la regla de Laplace de $f^{(n)}$, que aporta la suma de términos
> $f^{(k)}(0)$. $\blacksquare$

> [!proposicion] Integral fraccionaria
> Como $I^{\alpha}=D^{-\alpha}$, su Laplace no tiene términos de frontera:
> $$\mathcal{L}\{I^{\alpha}f\}(s)=s^{-\alpha}F(s).$$
> Es el caso más simple y la razón de que se transforme la ecuación al dominio $s$: integrar y derivar
> fraccionariamente se vuelven **multiplicar y dividir por $s^{\alpha}$**.

> [!info] El patrón de solución
> Toda EDF lineal de coeficientes constantes se resuelve con el mismo guion: (1) transformar con el
> teorema de arriba, lo que mete las condiciones iniciales; (2) despejar $F(s)$, que queda como cociente
> con denominador $s^{\alpha}-\lambda$ (o un polinomio en $s^{\alpha}$); (3) antitransformar reconociendo
> $\dfrac{s^{\alpha-\beta}}{s^{\alpha}-\lambda}=\mathcal{L}\{t^{\beta-1}E_{\alpha,\beta}(\lambda t^{\alpha})\}$.
> El resultado siempre se escribe con [[Funcion de Mittag-Leffler| Mittag-Leffler]].

## Resumen

> [!resumen]
> | Operador | Transformada de Laplace |
> |---|---|
> | Integral $I^{\alpha}f$ | $s^{-\alpha}F(s)$ |
> | Caputo $D^{\alpha}_{C}f$ | $s^{\alpha}F(s)-\sum_{k=0}^{n-1}s^{\alpha-1-k}f^{(k)}(0)$ |
> | Riemann-Liouville $D^{\alpha}f$ | $s^{\alpha}F(s)-\sum_{k=0}^{n-1}s^{k}\big[D^{\alpha-1-k}f\big]_{0}$ |
> | Antitransformada clave | $\dfrac{s^{\alpha-1}}{s^{\alpha}-\lambda}\ \to\ E_\alpha(\lambda t^{\alpha})$ |
> | Caso entero $\alpha=1$ | $sF(s)-f(0)$ |

> [!corolario]
> La transformada de Laplace fraccional reduce una EDF a un problema **algebraico** en $s$, exactamente
> como en las EDO ordinarias. La elección de la derivada se reduce a sus términos de frontera: **Caputo**
> con condiciones iniciales clásicas y medibles es el estándar en aplicaciones físicas, y la
> antitransformación produce siempre [[Funcion de Mittag-Leffler| Mittag-Leffler]].

> [!referencia]
> - La función que aparece al antitransformar: [[Funcion de Mittag-Leffler]].
> - La derivada preferida en física: [[Derivada de Caputo]].
> - Lo que esta herramienta resuelve: [[Ecuaciones Diferenciales Fraccionarias]].
> - La base ordinaria: [[Transformada de Laplace/index]].
> - El capítulo: [[Calculo Fraccionario/index]].
