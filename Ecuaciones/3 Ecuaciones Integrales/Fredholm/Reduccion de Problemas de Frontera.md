---
title: Reducción de Problemas de Frontera
order: 9
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - fredholm
  - funcion-de-green
draft: false
aliases:
  - reducción de problemas de frontera
  - PVF a ecuación integral
  - función de Green como núcleo
  - boundary value problems
  - Green function kernel
---

# Reducción de Problemas de Frontera

> [!definicion]
> Un **problema de frontera** (PVF) $Lu=f$ con condiciones de contorno **homogéneas** se reescribe como una **ecuación de Fredholm** usando la [[Funcion de Green para EDO| función de Green]] $G(x,t)$ del operador $L$:
> $$u(x)=\int_{a}^{b}G(x,t)\,f(t)\,dt.$$
> Si el problema es de **autovalores**, $Lu=\mu\,u$, la misma sustitución lo convierte en la Fredholm **homogénea**
> $$u(x)=\mu\int_{a}^{b}G(x,t)\,u(t)\,dt,$$
> cuyo núcleo es la función de Green $G$. Cuando $L$ es **autoadjunto**, ese núcleo es **simétrico**, $G(x,t)=G(t,x)$.

> [!info]
> Es el **puente** entre lo diferencial y lo integral, y la razón de ser de [[Fredholm/index| Fredholm]] dentro del [[3 Ecuaciones Integrales/index| capítulo de ecuaciones integrales]]. Explica por qué la teoría espectral de [[Sturm-Liouville/index| Sturm-Liouville]] (autovalores reales, autofunciones ortogonales) es **la misma** que la de los [[Nucleos Simetricos/index| núcleos simétricos]]: el núcleo es la función de Green. La construcción de $G$ se detalla en [[Funcion de Green para EDO| función de Green]].

---

## Ejemplo

> [!ejemplo] La función de Green como núcleo simétrico
> ![[green_kernel.svg|420]]
>
> Mapa de calor de $G(x,t)$ del operador $-u''$ en $[0,\pi]$ con extremos fijos: es **simétrico** respecto a la diagonal $x=t$ ($G(x,t)=G(t,x)$), lo que garantiza autovalores reales y autofunciones ortogonales.

> [!ejemplo] Construcción de $G$ para $-u''=\mu u$ en $[0,\pi]$
> Consideremos el problema de autovalores $-u''=\mu\,u$ con $u(0)=u(\pi)=0$. Para hallar la función de Green resolvemos $-G''=\delta(x-t)$ con las mismas condiciones de contorno.
>
> **Soluciones de la homogénea.** $-G''=0$ da rectas; las que cumplen el contorno son $u_1(x)=x$ (anula en $0$) y $u_2(x)=\pi-x$ (anula en $\pi$). Construimos $G$ por tramos:
> $$G(x,t)=\begin{cases}A\,x\,(\pi-t)&x\le t\\[2pt] A\,t\,(\pi-x)&x> t.\end{cases}$$
>
> **Salto en la derivada.** La $\delta$ impone $G'(t^{+},t)-G'(t^{-},t)=-1$ (de $-G''=\delta$). Derivando cada rama en $x=t$: $-A\,t-A(\pi-t)=-A\pi=-1$, luego $A=1/\pi$. Por tanto
> $$G(x,t)=\frac{1}{\pi}\,x\,(\pi-t)\quad(x\le t),\qquad G(x,t)=\frac{1}{\pi}\,t\,(\pi-x)\quad(x> t).$$
>
> **Verificación de la simetría.** Intercambiando $x\leftrightarrow t$, la rama $x\le t$ pasa a la rama $x> t$ con el mismo valor: $\tfrac1\pi x(\pi-t)\leftrightarrow\tfrac1\pi t(\pi-x)$. Así $G(x,t)=G(t,x)$: el núcleo es **simétrico**, como debe ser por ser $-u''$ autoadjunto. El problema queda $u=\mu\int_0^\pi G\,u\,dt$, cuyas raíces características son $\mu_n=n^2$ y funciones propias $\operatorname{sen}(nx)$.

---

## En qué consiste

> [!teoria]
> La función de Green es el **operador inverso** de $L$: resuelve $Lu=f$ a base de superponer respuestas a impulsos puntuales $\delta(x-t)$. Como $L^{-1}$ es un operador integral con núcleo $G$, todo problema diferencial lineal con contorno homogéneo se vuelve un problema integral. Y aquí está la ganancia: mientras $L$ es **no acotado** (derivar amplifica), su inverso $L^{-1}=G$ es **compacto** (integrar suaviza), de modo que se le aplica toda la teoría espectral de operadores compactos. El problema de autovalores diferencial $Lu=\mu u$ y el integral $u=\mu\int G\,u$ tienen **exactamente** el mismo espectro.

> [!teorema] Equivalencia espectral PVF ⟷ Fredholm
> Sea $L$ un operador de **Sturm-Liouville** autoadjunto con condiciones de contorno homogéneas y función de Green $G(x,t)$. Entonces:
> 1. $\mu$ es **autovalor** del PVF $Lu=\mu u$ **si y solo si** $\mu$ es **raíz característica** del núcleo $G$ en $u=\mu\int_a^b G\,u\,dt$.
> 2. Las **autofunciones** del PVF coinciden con las **funciones propias** del núcleo.
> 3. Como $G$ es **simétrico**, sus autovalores son **reales** y sus autofunciones **ortogonales**: es la teoría de [[Nucleos Simetricos/index| Hilbert-Schmidt]] aplicada a $G$.

> [!demostracion] Por qué Sturm-Liouville hereda la teoría de Hilbert-Schmidt
> **Paso 1 — invertir el operador.** Como $G$ es la función de Green, $LG(\cdot,t)=\delta(\cdot-t)$, y para cualquier $g$ la función $\int_a^b G(x,t)g(t)\,dt$ resuelve $Lu=g$ con el contorno dado. Es decir, $L^{-1}=\mathcal{G}$, el operador integral de núcleo $G$.
>
> **Paso 2 — pasar de $L$ a $\mathcal G$.** Aplicando $L^{-1}$ a $Lu=\mu u$ se obtiene $u=\mu\,\mathcal G u=\mu\int_a^b G(x,t)u(t)\,dt$. Los autovalores se relacionan: $\mu$ es autovalor de $L$ con autofunción $u$ **si y solo si** $1/\mu$ es autovalor de $\mathcal G$ con la misma $u$. El espectro es **el mismo** salvo el inverso.
>
> **Paso 3 — usar la simetría.** Para $L$ autoadjunto, la función de Green cumple $G(x,t)=G(t,x)$ (reciprocidad). Entonces $\mathcal G$ es un operador **simétrico y compacto**: por [[Nucleos Simetricos/index| Hilbert-Schmidt]] tiene autovalores **reales** y autofunciones **ortogonales** que forman base.
>
> **Paso 4 — concluir.** Traduciendo de vuelta a $L$: los autovalores $\mu_n$ del PVF son **reales** y las autofunciones $u_n$ son **ortogonales** y completas. Esto es **exactamente** el teorema de Sturm-Liouville, ahora **demostrado** como un caso de la teoría espectral de núcleos simétricos. $\blacksquare$

> [!algoritmo] Reducir un PVF a una ecuación de Fredholm
> 1. **Identifica** el operador $L$ y verifica que el contorno sea homogéneo.
> 2. **Construye la función de Green** $G(x,t)$ resolviendo $LG=\delta(x-t)$ con el contorno (continuidad de $G$ y salto unidad en la derivada).
> 3. **Reescribe**: $Lu=f\Rightarrow u=\int_a^b G f\,dt$;  $Lu=\mu u\Rightarrow u=\mu\int_a^b G\,u\,dt$.
> 4. **Aplica Fredholm**: para $G$ simétrico, usa la teoría de [[Nucleos Simetricos/index| Hilbert-Schmidt]].

> [!proposicion]
> El sentido de la simetría de $G$ es físico: $G(x,t)$ es la respuesta en $x$ a un impulso en $t$, y la **reciprocidad** $G(x,t)=G(t,x)$ dice que la respuesta en $x$ a un impulso en $t$ iguala la respuesta en $t$ a un impulso en $x$. Esa reciprocidad equivale a que $L$ sea autoadjunto.

## Resumen

> [!resumen]
> | Diferencial | Integral (Fredholm) |
> |---|---|
> | $Lu=f$, contorno homog. | $u=\int_a^b G(x,t)f(t)\,dt$ |
> | $Lu=\mu u$ (autovalores) | $u=\mu\int_a^b G(x,t)u(t)\,dt$ |
> | Operador $L$ (no acotado) | $\mathcal G=L^{-1}$ (compacto) |
> | Autovalores $\mu_n$ del PVF | raíces características de $G$ |
> | Autofunciones del PVF | funciones propias del núcleo |
> | $L$ autoadjunto | $G(x,t)=G(t,x)$ simétrico |

> [!corolario]
> Un PVF **autoadjunto** equivale exactamente a una ecuación de Fredholm con **núcleo simétrico**: lo diferencial y lo integral son dos caras del mismo problema espectral. Por eso Sturm-Liouville no es una teoría aparte, sino la teoría de [[Nucleos Simetricos/index| Hilbert-Schmidt]] vista a través de la función de Green.

> [!referencia]
> - El espectro resultante: [[Raices Caracteristicas y Funciones Propias]].
> - La teoría espectral del núcleo simétrico: [[Nucleos Simetricos/index]].
> - La construcción del núcleo: [[Funcion de Green para EDO]].
> - El PVF diferencial original: [[Sturm-Liouville/index]].
> - Vista de conjunto: [[Fredholm/index]].
