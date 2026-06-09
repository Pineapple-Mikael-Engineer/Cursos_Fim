---
title: Método de Colocación
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - metodos-aproximados
  - colocacion
draft: false
aliases:
  - método de colocación
  - colocación
  - collocation method
---

# Método de Colocación

> [!definicion]
> El **método de colocación** es un método de **proyección por puntos**. Se busca una solución
> aproximada como combinación finita de funciones base,
> $$\varphi(x)\approx\varphi_N(x)=\sum_{i=1}^{N}c_i\,\phi_i(x),$$
> y se exige que la ecuación integral se satisfaga **exactamente en $N$ puntos prefijados**
> $x_1,\dots,x_N$ —los **nodos de colocación**—:
> $$\varphi_N(x_j)=f(x_j)+\lambda\int_a^b K(x_j,t)\,\varphi_N(t)\,dt,\qquad j=1,\dots,N.$$
> Cada una de esas $N$ condiciones es una **ecuación lineal** en los coeficientes $c_i$, de modo que la
> ecuación integral se reduce a un sistema lineal $N\times N$ para $\{c_i\}$.

> [!info]
> Una de las técnicas de **proyección** de los [[Metodos Aproximados/index| métodos aproximados]] del
> [[3 Ecuaciones Integrales/index| capítulo]]. Comparte con [[Metodo de Bubnov-Galiorkin| Galerkin]]
> la idea de buscar $\varphi$ en una base finita, pero se distingue por **cómo** impone la ecuación: en
> vez de anular el residuo en media (integrando contra las base), lo anula **exactamente en puntos**.
> Eso la hace la más simple de montar de todas y la emparenta con la [[Cuadratura y Nystrom| cuadratura]],
> que también discretiza sobre nodos.

---

## Ejemplo

> [!ejemplo] Fredholm con base $\{1,x\}$ y dos nodos $x=0,\ x=1$
> Resolvamos por colocación
> $$\varphi(x)=1+\tfrac12\int_{0}^{1}(x+t)\,\varphi(t)\,dt,$$
> es decir $f(x)=1$, $K(x,t)=x+t$, $\lambda=\tfrac12$. (La solución exacta, por
> [[Nucleo Degenerado| núcleo degenerado]], es $\varphi(x)=\tfrac{12}{7}+\tfrac{6}{7}x\approx1.714+0.857x$;
> la usaremos al final para comparar.)
>
> **Paso 1 — elige base y ansatz.** Tomamos $\phi_1=1$, $\phi_2=x$, de modo que
> $$\varphi_2(x)=c_1+c_2\,x.$$
>
> **Paso 2 — calcula la integral en función de $c_1,c_2$.** Necesitamos
> $\int_0^1\varphi_2\,dt=c_1+\tfrac12 c_2$ y $\int_0^1 t\,\varphi_2\,dt=\tfrac12 c_1+\tfrac13 c_2$. Como
> $\int_0^1(x+t)\varphi_2\,dt=x\!\int_0^1\varphi_2\,dt+\int_0^1 t\,\varphi_2\,dt$,
> $$\int_0^1(x+t)\varphi_2\,dt=x\Big(c_1+\tfrac12 c_2\Big)+\Big(\tfrac12 c_1+\tfrac13 c_2\Big).$$
> El **residuo** que queremos anular es
> $$r(x)=\varphi_2(x)-1-\tfrac12\int_0^1(x+t)\varphi_2\,dt=(c_1+c_2x)-1-\tfrac12\Big[x\big(c_1+\tfrac12 c_2\big)+\tfrac12 c_1+\tfrac13 c_2\Big].$$
>
> **Paso 3 — impón $r=0$ en los dos nodos.**
> En $x_1=0$:
> $$c_1-1-\tfrac12\Big(\tfrac12 c_1+\tfrac13 c_2\Big)=0\;\Longrightarrow\;\tfrac34 c_1-\tfrac16 c_2=1.$$
> En $x_2=1$:
> $$(c_1+c_2)-1-\tfrac12\Big[\big(c_1+\tfrac12 c_2\big)+\tfrac12 c_1+\tfrac13 c_2\Big]=0\;\Longrightarrow\;\tfrac14 c_1+\tfrac{7}{12}c_2=1.$$
>
> **Paso 4 — resuelve el sistema $2\times2$.**
> $$\begin{cases}\tfrac34 c_1-\tfrac16 c_2=1,\\[3pt]\tfrac14 c_1+\tfrac{7}{12}c_2=1.\end{cases}$$
> Multiplicando por $12$: $9c_1-2c_2=12$ y $3c_1+7c_2=12$. De la primera $c_2=\tfrac{9c_1-12}{2}$;
> sustituyendo, $3c_1+7\cdot\tfrac{9c_1-12}{2}=12\Rightarrow 6c_1+63c_1-84=24\Rightarrow 69c_1=108$, luego
> $$c_1=\frac{108}{69}=\frac{36}{23}\approx1.565,\qquad c_2=\frac{9\cdot\tfrac{36}{23}-12}{2}=\frac{\tfrac{324}{23}-\tfrac{276}{23}}{2}=\frac{48}{46}=\frac{24}{23}\approx1.043.$$
>
> **Paso 5 — solución aproximada y contraste.**
> $$\boxed{\varphi_2(x)=\tfrac{36}{23}+\tfrac{24}{23}\,x\approx1.565+1.043\,x.}$$
> Frente a la exacta $1.714+0.857x$: con solo dos nodos el ajuste ya captura el orden de magnitud y la
> pendiente. Refinando con más funciones base y más nodos (Paso siguiente natural) el error baja
> deprisa. Compárese con [[Metodo de Bubnov-Galiorkin| Galerkin]], que sobre la **misma** base $\{1,x\}$
> daría la solución exacta (porque la base contiene a la solución y Galerkin proyecta en media exacta);
> colocación, al imponer solo en dos puntos, paga un pequeño precio en precisión a cambio de no calcular
> ningún producto interno.

---

## En qué consiste

> [!teoria]
> La idea es la de **método de residuos ponderados** llevada al extremo más simple. Se define el residuo
> de la aproximación,
> $$r(x;c_1,\dots,c_N)=\varphi_N(x)-f(x)-\lambda\int_a^b K(x,t)\varphi_N(t)\,dt,$$
> que mide cuánto **falla** la ecuación. La solución exacta tendría $r\equiv0$ en todo $[a,b]$; con $N$
> coeficientes solo podemos imponer $N$ condiciones. Colocación elige las condiciones más directas
> posibles: **$r(x_j)=0$ en $N$ puntos**. Formalmente, equivale a usar como funciones de peso las
> **deltas de Dirac** $w_j(x)=\delta(x-x_j)$ en el esquema general de residuos ponderados
> $\int r(x)w_j(x)\,dx=0$ —de ahí que [[Metodo de Bubnov-Galiorkin| Galerkin]] (pesos $=\phi_j$) y
> colocación (pesos $=\delta$) sean dos caras de la misma idea.

> [!algoritmo] Resolver por colocación
> 1. **Elige la base** $\{\phi_1,\dots,\phi_N\}$ (polinomios, trigonométricas, splines…) y escribe
>    $\varphi_N=\sum_i c_i\phi_i$.
> 2. **Elige los nodos** $x_1<\dots<x_N$ en $[a,b]$ (ver el aviso de abajo).
> 3. **Calcula las integrales** $\displaystyle I_{ji}=\int_a^b K(x_j,t)\,\phi_i(t)\,dt$ para cada nodo
>    $x_j$ y cada base $\phi_i$ (analíticamente o por cuadratura).
> 4. **Monta el sistema** $\sum_i\big[\phi_i(x_j)-\lambda I_{ji}\big]c_i=f(x_j)$, esto es
>    $(\mathsf{P}-\lambda\mathsf{I})\mathbf{c}=\mathbf{f}$ con $\mathsf{P}_{ji}=\phi_i(x_j)$,
>    $\mathsf{I}_{ji}=I_{ji}$, $f_j=f(x_j)$.
> 5. **Resuelve** el sistema lineal $N\times N$ y reconstruye $\varphi_N(x)=\sum_i c_i\phi_i(x)$, válida
>    en **todo** el intervalo (no solo en los nodos).

> [!proposicion]
> Frente a [[Metodo de Bubnov-Galiorkin| Galerkin]]: colocación **no integra el residuo** contra las
> base, así que evita los $N^2$ productos internos dobles $\langle\phi_j,K\phi_i\rangle$ y solo necesita
> **evaluar** el operador en los nodos. Es por ello más barata y simple de montar, pero típicamente algo
> **menos precisa** y su sistema puede no heredar la simetría del núcleo (la matriz de Galerkin sí es
> simétrica si $K$ lo es). En resumen: colocación cambia precisión por simplicidad.

> [!warning] La elección de los nodos importa
> Con nodos **equiespaciados** y base polinómica de grado alto aparece el fenómeno de Runge: la
> aproximación oscila cerca de los extremos y la convergencia se degrada. La cura es colocar en los
> **ceros de polinomios ortogonales** (Chebyshev, Legendre): esto es la **colocación espectral**, que
> para núcleos y datos suaves recupera convergencia muy rápida. Como regla práctica, nunca uses puntos
> equiespaciados para $N$ grande; usa nodos de Chebyshev.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Ansatz | $\varphi_N=\sum_{i=1}^N c_i\phi_i$ |
> | Condición | $r(x_j)=0$ en $N$ nodos $x_1,\dots,x_N$ |
> | Pesos (residuos ponderados) | deltas $\delta(x-x_j)$ |
> | Sistema | $(\mathsf{P}-\lambda\mathsf{I})\mathbf{c}=\mathbf{f}$, $\mathsf{P}_{ji}=\phi_i(x_j)$ |
> | vs. Galerkin | más simple (sin productos internos), algo menos preciso |
> | Nodos buenos | ceros de polinomios ortogonales (colocación espectral) |

> [!corolario]
> Colocación es la forma más **literal** de aproximar una ecuación integral: "que la ecuación se cumpla
> en estos puntos". Esa literalidad la hace inmediata de programar —solo evaluaciones, sin integrales de
> ponderación— y muy competitiva si los nodos se eligen bien. Es el puente natural entre la proyección
> de [[Metodo de Bubnov-Galiorkin| Galerkin]] y la discretización por [[Cuadratura y Nystrom| cuadratura]].

> [!referencia]
> - La otra proyección, en media: [[Metodo de Bubnov-Galiorkin]].
> - La discretización por nodos y pesos: [[Cuadratura y Nystrom]].
> - Panorama de los métodos: [[Metodos Aproximados/index]].
