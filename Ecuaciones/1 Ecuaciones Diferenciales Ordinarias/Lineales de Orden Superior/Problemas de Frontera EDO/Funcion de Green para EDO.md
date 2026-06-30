---
title: Función de Green para EDO
order: 2
tags:
  - ecuaciones
  - edo
  - teoria
  - lineales
  - problemas-frontera
  - funcion-de-green
draft: false
aliases:
  - función de Green
  - Green's function
  - inversa integral
  - núcleo de Green
---

# Función de Green para EDO

> [!definicion]
> La **función de Green** $G(x,\xi)$ de un PVF $L[y]=f$ con condiciones de frontera **homogéneas** es la solución del problema con una **fuente puntual** colocada en $\xi$:
> $$L_x\,G(x,\xi)=\delta(x-\xi),\qquad G \text{ cumple las mismas condiciones de frontera (en } x).$$
> Una vez conocida $G$, la solución del PVF para **cualquier** fuente $f$ se obtiene por **superposición** integrando las respuestas a cada fuente puntual:
> $$\boxed{\,y(x)=\int_a^b G(x,\xi)\,f(\xi)\,d\xi\,}.$$
> En otras palabras, $G$ es la **inversa integral** del operador $L$: hace por $L$ lo que $A^{-1}$ hace por una matriz, $y=L^{-1}f$.

> [!info]
> Segunda nota de [[Problemas de Frontera EDO/index| problemas de frontera]]. Resuelve el PVF **no homogéneo** de forma cerrada cuando es regular (sin autovalor de por medio). Se apoya en el [[Operador Diferencial Lineal| operador lineal]] $L$ y sus soluciones homogéneas, y conecta las EDO con las [[3 Ecuaciones Integrales/index| ecuaciones integrales]]. La versión abstracta y general vive en [[Funcion de Green/index| función de Green]] (Herramientas).

---

## Ejemplo

> [!ejemplo] La función de Green de $-y''=f$ en $[0,1]$ con $y(0)=y(1)=0$
> Queremos resolver $-y''=f(x)$ con extremos fijos a cero. Aquí $L=-\dfrac{d^2}{dx^2}$, que en forma $\tfrac{d}{dx}(p\,y')$ tiene $p(x)=-1$.
>
> **Paso 1 — soluciones homogéneas que cumplen cada extremo.** $-y''=0$ tiene general $y=A+Bx$.
> - $y_1$ debe anularse en $x=0$: tomamos $y_1(x)=x$.
> - $y_2$ debe anularse en $x=1$: tomamos $y_2(x)=1-x$.
>
> **Paso 2 — forma de $G$.** $G(x,\xi)=C\,y_1(x_<)\,y_2(x_>)$, con $x_<=\min(x,\xi)$ y $x_>=\max(x,\xi)$; es decir
> $$G(x,\xi)=\begin{cases} C\,x\,(1-\xi) & x<\xi,\\[2pt] C\,\xi\,(1-x) & x>\xi.\end{cases}$$
> Esta forma ya garantiza **continuidad** en $x=\xi$ (ambas ramas dan $C\,\xi(1-\xi)$) y las dos condiciones de frontera.
>
> **Paso 3 — fijar $C$ con el salto.** El salto de la derivada es $\partial_xG\big|_{\xi^-}^{\xi^+}=\tfrac{1}{p(\xi)}=\tfrac{1}{-1}=-1$. Derivando respecto de $x$: para $x>\xi$, $\partial_xG=C\,\xi\,(-1)=-C\xi$; para $x<\xi$, $\partial_xG=C\,(1-\xi)$. El salto es $-C\xi-C(1-\xi)=-C=-1$, luego $C=1$. Por tanto
> $$\boxed{\,G(x,\xi)=\begin{cases} x\,(1-\xi) & x<\xi,\\ \xi\,(1-x) & x>\xi.\end{cases}}$$
>
> **Paso 4 — verificar con $f=1$.** $y(x)=\displaystyle\int_0^1 G(x,\xi)\,d\xi$. Partimos en $\xi<x$ (rama $\xi(1-x)$) y $\xi>x$ (rama $x(1-\xi)$):
> $$y(x)=\int_0^x \xi(1-x)\,d\xi+\int_x^1 x(1-\xi)\,d\xi
> =(1-x)\frac{x^2}{2}+x\,\frac{(1-x)^2}{2}=\frac{x(1-x)}{2}.$$
> Comprobación: $y=\tfrac12(x-x^2)$ da $y''=-1$, luego $-y''=1=f$ ✓, y $y(0)=y(1)=0$ ✓. La función de Green resolvió el PVF de un solo golpe.

---

## En qué consiste

> [!teoria] Cómo se construye $G$ para un operador de segundo orden
> Para $L=\dfrac{d}{dx}\!\Big(p(x)\dfrac{d}{dx}\Big)+q(x)$ (forma autoadjunta; incluye $y''$ con $p\equiv1$), la receta es:
> 1. **Una solución de cada lado.** Halla $y_1$, solución de $L[y]=0$ que cumple la condición de frontera en $a$; y $y_2$, solución de $L[y]=0$ que cumple la condición en $b$.
> 2. **Estructura partida.** $G$ se construye como producto cruzado
>    $$G(x,\xi)=\begin{cases} A\,y_1(x)\,y_2(\xi) & x<\xi,\\ A\,y_1(\xi)\,y_2(x) & x>\xi,\end{cases}$$
>    o de forma compacta $G(x,\xi)=A\,y_1(x_<)\,y_2(x_>)$. Así, **para $x\neq\xi$** se tiene $L_xG=0$ (cada rama es solución homogénea) y $G$ hereda las condiciones de frontera correctas.
> 3. **Dos condiciones de empalme en $x=\xi$:**
>    - **(i) continuidad** de $G$: $G(\xi^+,\xi)=G(\xi^-,\xi)$;
>    - **(ii) salto** de la derivada: $\partial_xG\big|_{\xi^-}^{\xi^+}=\dfrac{1}{p(\xi)}$. La continuidad sale automática de la forma simétrica; el salto **fija la constante** $A$. En términos del [[Wronskiano e Independencia Lineal| wronskiano]] de $y_1,y_2$ resulta $A=\dfrac{1}{p(\xi)\,W(\xi)}$ (que es constante por la [[Formula de Abel| fórmula de Abel]] aplicada a la forma autoadjunta).

> [!demostracion] De dónde sale el salto $\partial_xG\big|_{\xi^-}^{\xi^+}=\tfrac1{p(\xi)}$
> Partimos de la ecuación definitoria $L_xG=\delta(x-\xi)$, con $L_x=\tfrac{d}{dx}\big(p\,\tfrac{d}{dx}\big)+q$.
>
> **Paso 1 — integrar a través de la singularidad.** Integramos en un entorno $(\xi-\epsilon,\xi+\epsilon)$:
> $$\int_{\xi-\epsilon}^{\xi+\epsilon}\Big[\frac{d}{dx}\big(p\,G'\big)+q\,G\Big]\,dx
> =\int_{\xi-\epsilon}^{\xi+\epsilon}\delta(x-\xi)\,dx=1.$$
>
> **Paso 2 — el término con derivada máxima da el salto.** El primer término es una derivada exacta, así que por el teorema fundamental del cálculo
> $$\int_{\xi-\epsilon}^{\xi+\epsilon}\frac{d}{dx}\big(p\,G'\big)\,dx
> =\big[p\,G'\big]_{\xi-\epsilon}^{\xi+\epsilon}
> \;\xrightarrow{\epsilon\to0}\; p(\xi)\,\big(G'(\xi^+,\xi)-G'(\xi^-,\xi)\big).$$
>
> **Paso 3 — el término sin derivada máxima se anula.** Como $G$ es **continua** (y acotada), $\displaystyle\int_{\xi-\epsilon}^{\xi+\epsilon}q\,G\,dx\to 0$ cuando $\epsilon\to0$ (es la integral de una función acotada sobre un intervalo de longitud $2\epsilon\to0$).
>
> **Paso 4 — igualar.** Queda $p(\xi)\,\big[G'\big]_{\xi^-}^{\xi^+}=1$, es decir
> $$\big[\partial_xG\big]_{\xi^-}^{\xi^+}=\frac{1}{p(\xi)}.\qquad\blacksquare$$
> Intuición: la fuente puntual $\delta$ no puede "verse" en $G$ misma (que es continua) ni en su parte regular; toda su intensidad se concentra en un **quiebre** de la pendiente, de tamaño $1/p(\xi)$.

> [!proposicion] Por qué $y=\int G\,f$ resuelve el problema
> Aplicando $L_x$ bajo la integral y usando $L_xG(x,\xi)=\delta(x-\xi)$:
> $$L_x\,y(x)=\int_a^b L_xG(x,\xi)\,f(\xi)\,d\xi=\int_a^b \delta(x-\xi)\,f(\xi)\,d\xi=f(x).$$
> Y como cada $G(\cdot,\xi)$ cumple las condiciones de frontera homogéneas, también las cumple $y$ (integrar en $\xi$ no afecta las condiciones en $x$). Así $y$ resuelve el PVF completo. La superposición de respuestas puntuales **es** la solución.

> [!warning] La función de Green existe solo si el PVF homogéneo es regular
> La construcción exige que $y_1$ y $y_2$ sean **independientes** ($W\neq0$); si fueran proporcionales, el problema homogéneo tendría solución no trivial, es decir estaríamos **en un autovalor** (ver [[Condiciones de Frontera| condiciones de frontera]]). En ese caso $G$ no existe en el sentido ordinario y el PVF no homogéneo o no tiene solución o tiene infinitas (alternativa de Fredholm). La función de Green es la herramienta del caso **regular**.

---

## Resumen

> [!resumen]
> | Ingrediente | Qué es |
> |---|---|
> | Definición | $L_xG(x,\xi)=\delta(x-\xi)$ con condiciones de frontera homogéneas |
> | Solución del PVF | $y(x)=\int_a^b G(x,\xi)\,f(\xi)\,d\xi$ |
> | Construcción | $G=A\,y_1(x_<)\,y_2(x_>)$; $y_1$ cumple frontera en $a$, $y_2$ en $b$ |
> | Empalme (i) | **continuidad** en $x=\xi$ |
> | Empalme (ii) | **salto** $\partial_xG\big\|_{\xi^-}^{\xi^+}=\tfrac{1}{p(\xi)}$ → fija $A$ |
> | Ejemplo modelo | $-y''=f$, $[0,1]$, $y(0)=y(1)=0$ → $G=x(1-\xi)$ si $x<\xi$, $\xi(1-x)$ si $x>\xi$ |

> [!corolario]
> La función de Green es la **inversa del operador diferencial** hecha explícita: convierte el PVF $L[y]=f$ en una simple integral $y=\int G f$. Concentra toda la dificultad —el operador y las condiciones de frontera— en un único objeto $G(x,\xi)$ que se calcula **una vez** y sirve para toda fuente $f$. Esa es su potencia: separa "el problema" (en $G$) de "el dato" (en $f$).

> [!referencia]
> - Cuándo NO existe $G$ (autovalores): [[Condiciones de Frontera]].
> - El operador que se invierte: [[Operador Diferencial Lineal]].
> - La conexión con núcleos integrales: [[3 Ecuaciones Integrales/index]].
> - La versión general (EDP y dimensiones superiores): [[Funcion de Green/index]].
> - Vista de conjunto de la sección: [[Problemas de Frontera EDO/index]].
