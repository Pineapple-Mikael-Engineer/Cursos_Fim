---
title: Teorema de Mercer
order: 2
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - fredholm
  - nucleos-simetricos
  - mercer
draft: false
aliases:
  - teorema de Mercer
  - descomposición espectral del núcleo
  - Mercer theorem
---

# Teorema de Mercer

> [!definicion]
> El **teorema de Mercer** afirma que un núcleo simétrico **continuo y definido positivo** se desarrolla en su **propia base propia**:
> $$K(x,t)=\sum_{n=1}^\infty\frac{\varphi_n(x)\,\varphi_n(t)}{\lambda_n},$$
> donde $\lambda_n$ son sus raíces características (todas positivas) y $\varphi_n$ sus funciones propias ortonormales, y la convergencia de la serie es **absoluta y uniforme** en $[a,b]\times[a,b]$. Dicho de otro modo: el núcleo **es** su descomposición espectral, igual que una matriz simétrica es $\mathsf{A}=\sum_n\mu_n\mathbf{e}_n\mathbf{e}_n^{\mathsf{T}}$.

> [!info]
> El refinamiento más fuerte de los [[Nucleos Simetricos/index| núcleos simétricos]]: mientras [[Teoria de Hilbert-Schmidt| Hilbert-Schmidt]] desarrolla $Kg$, Mercer desarrolla el **propio núcleo** $K$. Exige una hipótesis extra —definido positivo— y a cambio da convergencia uniforme y la fórmula de la **traza**. Es la herramienta que justifica los desarrollos de la [[Ecuaciones Simetricas No Homogeneas| ecuación no homogénea]].

---

## Ejemplo

> [!ejemplo] El núcleo es su propia descomposición espectral
> ![[nucleo_mercer.svg|520]]
>
> A la izquierda, un núcleo simétrico $K(x,t)$; a la derecha, su aproximación de Mercer truncada a pocos términos $\sum_{n\le N}\varphi_n(x)\varphi_n(t)/\lambda_n$: con unos pocos modos ya reproduce el núcleo, porque los $\lambda_n$ crecen y los términos altos pesan poco.

> [!ejemplo] Mercer para el núcleo de Green de $-u''$
> El núcleo de Green de $-u''$ en $[0,\pi]$ con extremos nulos,
> $$G(x,t)=\frac{1}{\pi}\begin{cases}x(\pi-t)&x\le t\\ t(\pi-x)&x>t\end{cases},$$
> es simétrico y definido positivo, con $\lambda_n=n^2$ y $\varphi_n(x)=\sqrt{2/\pi}\,\operatorname{sen}(nx)$. Mercer afirma entonces que el propio núcleo es la serie
> $$G(x,t)=\sum_{n=1}^\infty\frac{\varphi_n(x)\,\varphi_n(t)}{\lambda_n}=\frac{2}{\pi}\sum_{n=1}^\infty\frac{\operatorname{sen}(nx)\,\operatorname{sen}(nt)}{n^2},$$
> y esta serie converge **uniformemente** a la función "tienda" $G$. Puedes comprobar el caso $x=t$ evaluando la traza: $\int_0^\pi G(x,x)\,dx=\frac{2}{\pi}\sum_n\frac{1}{n^2}\int_0^\pi\operatorname{sen}^2(nx)\,dx =\sum_n\frac{1}{n^2}=\frac{\pi^2}{6}$, que coincide con el cálculo directo $\int_0^\pi\frac{x(\pi-x)}{\pi}\,dx$.

---

## En qué consiste

> [!teoria]
> La diferencia con Hilbert-Schmidt es de **objeto**: allí se desarrollaba una función $Kg$; aquí se desarrolla el núcleo, que es una función de **dos** variables. Pensando en $t$ fijo, $K(\cdot,t)$ es precisamente $K$ aplicado a una "delta en $t$", así que cabe esperar que se exprese en las $\varphi_n$. La hipótesis de **definido positivo** ($\int\int K(x,t)g(x)g(t)\ge0$, equivalente a $\lambda_n>0$) es la que garantiza que esa serie no solo converja en media, sino **absoluta y uniformemente** — y por tanto que la suma sea de verdad el núcleo continuo, punto a punto.

> [!teorema] Traza del núcleo (Mercer en la diagonal)
> Poniendo $t=x$ en la serie de Mercer e integrando, con $\int_a^b\varphi_n^2=1$,
> $$\int_a^b K(x,x)\,dx=\sum_{n=1}^\infty\frac{1}{\lambda_n}.$$
> Es el **análogo continuo** de $\operatorname{tr}\mathsf{A}=\sum_n\mu_n$ (la traza es la suma de los autovalores): aquí la "traza" $\int K(x,x)\,dx$ es la suma de los autovalores $1/\lambda_n$ del operador. Da, de paso, un criterio rápido: si $\int K(x,x)\,dx$ es finito, la serie $\sum 1/\lambda_n$ converge.

> [!demostracion] Esquema de la fórmula de la traza
> **Paso 1 — partir de Mercer.** Por el desarrollo uniforme, $K(x,t)=\sum_n\varphi_n(x)\varphi_n(t)/\lambda_n$. **Paso 2 — diagonal.** Hacer $t=x$: $K(x,x)=\sum_n\varphi_n(x)^2/\lambda_n$, serie de términos positivos (definido positivo) y uniformemente convergente, luego integrable término a término. **Paso 3 — integrar.** $\int_a^b K(x,x)\,dx=\sum_n\frac{1}{\lambda_n}\int_a^b\varphi_n(x)^2\,dx=\sum_n\frac{1}{\lambda_n}$, usando la normalización $\int\varphi_n^2=1$. $\blacksquare$

> [!warning] Mercer exige definido positivo
> La hipótesis de **definido positivo** (todos los $\lambda_n>0$) es esencial. Sin ella, la serie $\sum_n\varphi_n(x)\varphi_n(t)/\lambda_n$ puede **no converger uniformemente** al núcleo (los signos mezclados de los $\lambda_n$ destruyen la convergencia absoluta). En ese caso sigue valiendo [[Teoria de Hilbert-Schmidt| Hilbert-Schmidt]] para $Kg$ —que solo pide convergencia en media—, pero **no** el desarrollo puntual del propio núcleo.

> [!info]
> Mercer es la forma más nítida de "el núcleo simétrico es una matriz simétrica": no solo se diagonaliza, sino que **se reconstruye** desde su espectro $\{(\lambda_n,\varphi_n)\}$. Conserva su información en una lista de modos, y truncarla da la **mejor aproximación de rango bajo** del núcleo.

## Resumen

> [!resumen]
> | Concepto | Contenido |
> |---|---|
> | Hipótesis | $K$ simétrico, **continuo** y **definido positivo** ($\lambda_n>0$) |
> | Desarrollo | $K(x,t)=\sum_n\frac{\varphi_n(x)\varphi_n(t)}{\lambda_n}$ |
> | Convergencia | **absoluta y uniforme** en $[a,b]^2$ |
> | Traza | $\int_a^b K(x,x)\,dx=\sum_n\frac{1}{\lambda_n}$ ($\sim\operatorname{tr}\mathsf{A}=\sum\mu_n$) |
> | Sin def. positivo | falla la conv. uniforme; queda solo [[Teoria de Hilbert-Schmidt\|Hilbert-Schmidt]] |

> [!corolario]
> Mercer cierra la analogía matricial: un núcleo simétrico definido positivo **es** la suma de sus modos propios, con convergencia uniforme, y su traza es la suma de sus autovalores. Reconstruir el núcleo desde su espectro es lo que permite resolver la ecuación entera por desarrollo en autofunciones.

> [!referencia]
> - La base sobre la que se apoya: [[Teoria de Hilbert-Schmidt]].
> - Aplicación a resolver: [[Ecuaciones Simetricas No Homogeneas]].
> - Panorama: [[Nucleos Simetricos/index]].
