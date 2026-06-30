---
title: Raíces Características y Funciones Propias
order: 6
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - fredholm
  - espectro
draft: false
aliases:
  - raíces características
  - valores característicos
  - funciones propias
  - autovalores del núcleo
  - characteristic values
  - eigenfunctions
---

# Raíces Características y Funciones Propias

> [!definicion]
> La ecuación de Fredholm **homogénea**
> $$\varphi(x)=\lambda\int_{a}^{b}K(x,t)\,\varphi(t)\,dt$$
> tiene la solución trivial $\varphi\equiv0$ para casi todo $\lambda$. Los valores $\lambda=\lambda_n$ para los que existe una solución **no trivial** son las **raíces características** (o valores característicos) del núcleo, y esas soluciones $\varphi_n$ son sus **funciones propias**. Es el **espectro** del núcleo: el análogo continuo de los autovalores de una matriz.

> [!info]
> El corazón espectral de [[Fredholm/index| Fredholm]]: $\lambda_n$ es a $K$ lo que $1/\mu$ es a una matriz ($\mu$ autovalor). Decide cuándo la ecuación no homogénea tiene solución única (si $\lambda\neq\lambda_n$) o cae en la [[Alternativa de Fredholm| alternativa de Fredholm]]. Para **núcleos simétricos** el espectro es especialmente limpio ([[Nucleos Simetricos/index| Hilbert-Schmidt]]).

---

## Ejemplo

> [!ejemplo] El espectro de un núcleo de Green
> ![[autofunciones_fredholm.svg|480]]
>
> El problema de frontera $-u''=\mu\,u$ en $[0,\pi]$ con $u(0)=u(\pi)=0$ se reescribe como la ecuación integral homogénea
> $$\varphi(x)=\mu\int_0^\pi G(x,t)\,\varphi(t)\,dt,\qquad G(x,t)=\frac{1}{\pi}\begin{cases}x(\pi-t)&x\le t\\ t(\pi-x)&x> t\end{cases}$$
> (con $G$ la [[Funcion de Green para EDO| función de Green]] del operador). Sus **raíces características** son $\mu_n=n^2$ ($n=1,2,3,\dots$) y sus **funciones propias** $\varphi_n(x)=\operatorname{sen}(nx)$ — las mismas que el problema de frontera. La figura muestra las tres primeras: oscilan más al crecer $n$ y son **ortogonales** entre sí, $\int_0^\pi\operatorname{sen}(nx)\operatorname{sen}(mx)\,dx=0$ si $n\neq m$.

---

## En qué consiste

> [!teoria]
> La ecuación homogénea $\varphi=\lambda K\varphi$ dice que $\varphi$ es **autofunción** del operador integral $K$ con autovalor $1/\lambda$. Como en álgebra lineal, hay un conjunto **discreto** de valores especiales; entre ellos, la ecuación tiene "direcciones invariantes". Tres hechos clave (que se afilan para núcleos simétricos):
> 1. Las raíces características forman una sucesión $\lvert\lambda_1\rvert\le\lvert\lambda_2\rvert\le\cdots\to\infty$ (no se acumulan en finito).
> 2. A cada $\lambda_n$ le corresponde un número finito de funciones propias independientes (su **multiplicidad**).
> 3. Para un núcleo **degenerado** de rango $m$ hay a lo sumo $m$ raíces características (es una matriz $m\times m$); ver [[Nucleo Degenerado| núcleo degenerado]].

> [!teorema] Núcleos simétricos: espectro real y ortogonal
> Si el núcleo es **simétrico** ($K(x,t)=K(t,x)$) y no nulo, entonces: (a) tiene **al menos una** raíz característica; (b) todas las raíces características son **reales**; (c) las funciones propias de raíces **distintas** son **ortogonales**.

> [!demostracion] Ortogonalidad de funciones propias (núcleo simétrico)
> **Paso 1 — dos pares propios.** Sean $\varphi_n=\lambda_n K\varphi_n$ y $\varphi_m=\lambda_m K\varphi_m$. **Paso 2 — producto cruzado.** Multiplica la primera por $\varphi_m$, la segunda por $\varphi_n$, integra y resta. Usando la **simetría** $\int\varphi_m K\varphi_n=\int\varphi_n K\varphi_m$, los términos con $K$ se cancelan y queda
> $$\Big(\tfrac{1}{\lambda_n}-\tfrac{1}{\lambda_m}\Big)\int_a^b\varphi_n\varphi_m\,dx=0.$$
> **Paso 3 — concluir.** Si $\lambda_n\neq\lambda_m$, el factor no se anula, luego $\int_a^b\varphi_n\varphi_m\,dx=0$: las funciones propias son **ortogonales**. $\blacksquare$ (La realidad de los $\lambda_n$ se prueba igual, con el conjugado.)

> [!proposicion] Por qué Volterra no tiene espectro
> Una ecuación de [[Volterra/index| Volterra]] es una Fredholm con núcleo "triangular" ($K(x,t)=0$ para $t>x$). Sus núcleos iterados decaen factorialmente y la única raíz característica está en el infinito: por eso Volterra **nunca** tiene autovalores finitos y siempre es resoluble.

> [!algoritmo] Hallar raíces características y funciones propias
> 1. Plantea la homogénea $\varphi=\lambda\int_a^b K\varphi$.
> 2. Si $K$ es degenerado, redúcela a un **sistema lineal** y anula su determinante → $\lambda_n$.
> 3. Si $K$ es simétrico, usa la [[Nucleos Simetricos/index| teoría espectral]].
> 4. Normaliza las $\varphi_n$ (ortonormales) para los desarrollos.

## Resumen

> [!resumen]
> | Concepto | Contenido |
> |---|---|
> | Raíz característica $\lambda_n$ | la homogénea $\varphi=\lambda\int K\varphi$ tiene sol. no trivial |
> | Función propia $\varphi_n$ | esa solución no trivial |
> | Núcleo simétrico | $\lambda_n$ **reales**, $\varphi_n$ **ortogonales** |
> | Núcleo degenerado (rango $m$) | a lo sumo $m$ raíces |
> | Volterra | sin raíces finitas (siempre resoluble) |

> [!corolario]
> El espectro del núcleo —sus raíces características y funciones propias— es lo que vuelve a Fredholm tan rico como un problema de autovalores matricial. Cuando el núcleo es simétrico, ese espectro es real y ortogonal, y permite **diagonalizar** la ecuación: la base de la [[Nucleos Simetricos/index| teoría de Hilbert-Schmidt]].

> [!referencia]
> - La consecuencia para resolver: [[Alternativa de Fredholm]].
> - El caso simétrico (diagonalización): [[Nucleos Simetricos/index]].
> - El origen en problemas de frontera: [[Reduccion de Problemas de Frontera]].
