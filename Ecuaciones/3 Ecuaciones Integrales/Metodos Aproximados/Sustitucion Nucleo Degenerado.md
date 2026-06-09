---
title: Sustitución del Núcleo por uno Degenerado
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - metodos-aproximados
  - nucleo-degenerado
draft: false
aliases:
  - sustitución del núcleo degenerado
  - aproximación por núcleo degenerado
  - aproximación por núcleo separable
  - degenerate kernel approximation
  - kernel approximation method
---

# Sustitución del Núcleo por uno Degenerado

> [!definicion]
> El método consiste en **aproximar un núcleo general** $K(x,t)$ por uno **degenerado**
> $$K_N(x,t)=\sum_{i=1}^{N} a_i(x)\,b_i(t),$$
> obtenido por **desarrollo de Taylor**, **serie de Fourier** o **interpolación** del núcleo. Una vez
> reemplazado $K\to K_N$, la ecuación de Fredholm se convierte en un **sistema lineal $N\times N$
> exacto** —ya no aproximado—, resoluble por el procedimiento estándar del [[Nucleo Degenerado]]. La
> única aproximación está en sustituir $K$ por $K_N$; todo lo demás es álgebra lineal finita.

> [!info]
> Es la **traducción práctica** del [[Nucleo Degenerado| núcleo degenerado]] a núcleos cualesquiera, y
> el primer método de la sección [[Metodos Aproximados/index| Métodos Aproximados]] del
> [[3 Ecuaciones Integrales/index| capítulo de ecuaciones integrales]]. Frente a la
> [[Cuadratura y Nystrom| cuadratura de Nyström]] (que discretiza la integral), aquí se discretiza el
> **núcleo**: se aprovecha cualquier estructura analítica ($e^{xt}$, $\cos(x-t)$, $\frac{1}{1-xt}$, …)
> para truncar una serie conocida.

---

## Ejemplo

> [!ejemplo] Núcleo $K(x,t)=e^{xt}$ en $[0,1]$ aproximado por Taylor
> Resolvamos, para $f(x)=1$ y $\lambda$ pequeño,
> $$\varphi(x)=1+\lambda\int_0^1 e^{xt}\,\varphi(t)\,dt.$$
> El núcleo $e^{xt}$ **no** es degenerado (es una suma infinita), pero su serie de Taylor sí separa las
> variables término a término.
>
> **Paso 1 — desarrolla el núcleo.** Usando $e^{u}=\sum_{k\ge 0}u^k/k!$ con $u=xt$:
> $$e^{xt}=\sum_{k=0}^{\infty}\frac{(xt)^k}{k!}=\sum_{k=0}^{\infty}\frac{x^k}{\;}\cdot\frac{t^k}{k!}.$$
> Truncando en $N$ términos, $K_N(x,t)=\sum_{k=0}^{N-1}\dfrac{x^k t^k}{k!}$, que **es** degenerado de
> rango $N$ con $a_k(x)=x^k$ y $b_k(t)=t^k/k!$.
>
> **Paso 2 — toma $N=2$.** $K_2(x,t)=1+xt$. La ecuación aproximada es
> $$\varphi(x)=1+\lambda\int_0^1\big(1+xt\big)\,\varphi(t)\,dt.$$
> Separando, $a_1=1,\ b_1=1,\ a_2=x,\ b_2=t$, e introduciendo las constantes
> $$c_1=\int_0^1\varphi(t)\,dt,\qquad c_2=\int_0^1 t\,\varphi(t)\,dt,$$
> la solución tiene la forma $\varphi(x)=1+\lambda\,(c_1+c_2\,x)$.
>
> **Paso 3 — arma el sistema $2\times 2$.** Sustituye esa $\varphi$ en las definiciones de $c_1,c_2$,
> con $\int_0^1 1=1$, $\int_0^1 t=\tfrac12$, $\int_0^1 t^2=\tfrac13$:
> $$c_1=\int_0^1\big(1+\lambda(c_1+c_2 t)\big)dt=1+\lambda\big(c_1+\tfrac12 c_2\big),$$
> $$c_2=\int_0^1 t\big(1+\lambda(c_1+c_2 t)\big)dt=\tfrac12+\lambda\big(\tfrac12 c_1+\tfrac13 c_2\big).$$
> En forma $(\mathsf{I}-\lambda\mathsf{A})\mathbf{c}=\mathbf{f}$,
> $$\mathsf{A}=\begin{pmatrix}1&\tfrac12\\[2pt]\tfrac12&\tfrac13\end{pmatrix},\qquad
> \mathbf{f}=\begin{pmatrix}1\\[2pt]\tfrac12\end{pmatrix},\qquad
> \begin{cases}(1-\lambda)c_1-\tfrac{\lambda}{2}c_2=1,\\[4pt]-\tfrac{\lambda}{2}c_1+\big(1-\tfrac{\lambda}{3}\big)c_2=\tfrac12.\end{cases}$$
>
> **Paso 4 — resuelve (con $\lambda=\tfrac12$).** El determinante es
> $\Delta=(1-\lambda)(1-\tfrac{\lambda}{3})-\tfrac{\lambda^2}{4}$; en $\lambda=\tfrac12$,
> $\Delta=\tfrac12\cdot\tfrac56-\tfrac{1}{16}=\tfrac{5}{12}-\tfrac{1}{16}=\tfrac{17}{48}$. Por Cramer,
> $$c_1=\frac{1}{\Delta}\Big(1\cdot\tfrac56-\tfrac12\cdot\tfrac14\Big)=\frac{\tfrac56-\tfrac18}{\,17/48\,}=\frac{17/24}{17/48}=2,\qquad
> c_2=\frac{1}{\Delta}\Big(\tfrac12\cdot\tfrac12-\tfrac14\cdot 1\Big)=\frac{0}{\Delta}=0.$$
> Luego $\varphi(x)=1+\tfrac12(2+0\cdot x)=2$. La solución aproximada es **constante**, $\varphi\approx 2$.
>
> **Paso 5 — refina con $N=3$.** Con $K_3=1+xt+\tfrac{x^2t^2}{2}$ aparece un tercer término $a_3=x^2$,
> $b_3=t^2/2$ y el sistema pasa a $3\times 3$; la corrección sobre $\varphi\approx 2$ es del orden del
> término omitido $\tfrac{x^2t^2}{2}\le\tfrac12$ en $[0,1]$, de modo que dos términos ya dan buena
> precisión para $\lambda$ moderado. Aumentar $N$ acerca $K_N\to K$ y $\varphi_N\to\varphi$.

---

## En qué consiste

> [!teoria]
> La idea es **prestar** a un núcleo cualquiera la maquinaria exacta del [[Nucleo Degenerado]]. Hay
> tres maneras naturales de fabricar el desarrollo $K_N=\sum a_i b_i$:
> - **Taylor** (cuando $K$ es analítico en $xt$ o en $x-t$): se trunca la serie de potencias y cada
>   potencia $x^k t^k$ ya viene separada.
> - **Fourier** (cuando $K$ es periódico o se define en un intervalo): $K\approx\sum_{k} \alpha_k(x)\cos kt+\beta_k(x)\sin kt$
>   separa $x$ de $t$ término a término.
> - **Interpolación** (cuando solo se conoce $K$ por valores): se interpola en $t$ con funciones base
>   $\ell_j(t)$, $K(x,t)\approx\sum_j K(x,t_j)\,\ell_j(t)$, con $a_j(x)=K(x,t_j)$ y $b_j(t)=\ell_j(t)$.
> Cualquiera de ellas convierte el operador integral de **dimensión infinita** en una matriz $N\times N$.

> [!algoritmo] Sustitución del núcleo degenerado
> 1. **Desarrolla** $K(x,t)\approx K_N=\sum_{i=1}^N a_i(x)b_i(t)$ (Taylor, Fourier o interpolación),
>    eligiendo $N$ términos.
> 2. **Monta y resuelve** el sistema finito del [[Nucleo Degenerado| núcleo degenerado]]:
>    $(\mathsf{I}-\lambda\mathsf{A})\mathbf{c}=\mathbf{f}$ con $\alpha_{ji}=\int_a^b b_j a_i$,
>    $f_j=\int_a^b b_j f$, y $\varphi_N=f+\lambda\sum_i c_i a_i$.
> 3. **Refina** $N$: repite con un término más y compara; detente cuando $\varphi_N$ deje de cambiar
>    dentro de la tolerancia.

> [!teorema] Convergencia de la solución aproximada
> Si $K$ es **continuo** en $[a,b]\times[a,b]$ y $K_N\to K$ **uniformemente**, entonces para todo
> $\lambda$ que no sea raíz característica de $K$, la solución aproximada $\varphi_N$ (la del núcleo
> truncado) **converge a la solución exacta** $\varphi$ cuando $N\to\infty$:
> $$\lVert\varphi-\varphi_N\rVert\xrightarrow[N\to\infty]{}0.$$

> [!demostracion]
> **Paso 1 — operadores cercanos.** Sea $\mathcal{K}\varphi=\int_a^b K(x,t)\varphi\,dt$ y
> $\mathcal{K}_N$ el operador con núcleo $K_N$. La convergencia uniforme $K_N\to K$ implica, en norma
> de operador sobre funciones continuas,
> $$\lVert\mathcal{K}-\mathcal{K}_N\rVert\le (b-a)\max_{x,t}\lvert K(x,t)-K_N(x,t)\rvert\xrightarrow[N\to\infty]{}0.$$
>
> **Paso 2 — resolvente acotada.** Si $\lambda$ no es raíz característica, $(\mathsf{I}-\lambda\mathcal{K})^{-1}$
> existe y es acotado. Por continuidad de la inversión de operadores, para $N$ grande
> $(\mathsf{I}-\lambda\mathcal{K}_N)^{-1}$ también existe y está **uniformemente acotado**.
>
> **Paso 3 — diferencia de soluciones.** Restando $\varphi=f+\lambda\mathcal{K}\varphi$ y
> $\varphi_N=f+\lambda\mathcal{K}_N\varphi_N$,
> $$\varphi-\varphi_N=\lambda\,(\mathsf{I}-\lambda\mathcal{K}_N)^{-1}(\mathcal{K}-\mathcal{K}_N)\varphi.$$
> Tomando normas,
> $$\lVert\varphi-\varphi_N\rVert\le\lvert\lambda\rvert\,\big\lVert(\mathsf{I}-\lambda\mathcal{K}_N)^{-1}\big\rVert\,\lVert\mathcal{K}-\mathcal{K}_N\rVert\,\lVert\varphi\rVert.$$
> Como el primer factor está acotado y $\lVert\mathcal{K}-\mathcal{K}_N\rVert\to 0$ por el Paso 1, el
> miembro derecho tiende a $0$. $\blacksquare$

> [!warning]
> El desarrollo elegido debe **converger** sobre todo el cuadrado $[a,b]\times[a,b]$: un Taylor de
> radio de convergencia insuficiente, o un Fourier de un núcleo discontinuo (fenómeno de Gibbs), pueden
> hacer que $K_N$ **no** se acerque a $K$ y arruinar la aproximación. Verifica siempre el residuo
> $\max\lvert K-K_N\rvert$ antes de confiar en $\varphi_N$.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Idea | reemplazar $K$ por $K_N=\sum_{i=1}^N a_i(x)b_i(t)$ |
> | Cómo se obtiene $K_N$ | Taylor, Fourier o interpolación de $K$ |
> | Resultado | sistema $(\mathsf{I}-\lambda\mathsf{A})\mathbf{c}=\mathbf{f}$ **exacto** para $K_N$ |
> | Solución | $\varphi_N=f+\lambda\sum_i c_i a_i$ |
> | Convergencia | $K_N\to K$ uniforme $\Rightarrow \varphi_N\to\varphi$ |
> | Riesgo | desarrollo que no converge en todo el cuadrado |

> [!corolario]
> Cualquier núcleo continuo es, a efectos prácticos, **un núcleo degenerado más un resto pequeño**.
> Sustituirlo por su truncamiento traslada todo el problema al terreno exacto y finito del núcleo
> separable, con el único cuidado de controlar el error del desarrollo. Es el método a elegir cuando el
> núcleo tiene **estructura analítica** que regalar; si no la tiene, conviene la
> [[Cuadratura y Nystrom| cuadratura de Nyström]].

> [!referencia]
> - El motor algebraico exacto: [[Nucleo Degenerado]].
> - La alternativa por discretización de la integral: [[Cuadratura y Nystrom]].
> - Panorama de la sección: [[Metodos Aproximados/index]].
