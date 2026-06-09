---
title: Solucion Fundamental
tags:
  - ecuaciones
  - edp
  - teoria
  - funcion-green
  - solucion-fundamental
draft: false
aliases:
  - solución fundamental
  - respuesta al impulso en espacio libre
  - fundamental solution
  - free-space Green's function
---

# Solución Fundamental

> [!definicion]
> La **solución fundamental** $\Phi$ de un operador lineal $L$ es su **respuesta al impulso en
> espacio libre** (todo $\mathbb{R}^n$, sin fronteras):
> $$L\,\Phi(\mathbf{x})=\delta(\mathbf{x}),$$
> donde $\delta$ es la delta de Dirac concentrada en el origen. Para el **laplaciano** $L=-\nabla^2$,
> la solución fundamental es exactamente el **potencial de una carga puntual**:
> $$\Phi(\mathbf{x})=-\frac{1}{2\pi}\ln\lvert\mathbf{x}\rvert\quad\text{(2D)},\qquad
> \Phi(\mathbf{x})=\frac{1}{4\pi\,\lvert\mathbf{x}\rvert}\quad\text{(3D)}.$$
> Es la pieza más básica de toda la teoría: la respuesta a **un** impulso, sin paredes que la
> distorsionen. Todo lo demás se construye encima de ella.

> [!info]
> Es la primera pieza de la sección [[Funciones de Green para EDP/index| Funciones de Green para EDP]],
> dentro del [[2 Ecuaciones en Derivadas Parciales/index| capítulo de EDP]]. Cuando el dominio tiene
> fronteras hay que **corregirla** sumándole una parte armónica: ese es el contenido de
> [[Funcion de Green y Condiciones]], y en geometrías simples la corrección se obtiene con el
> [[Metodo de las Imagenes]]. Su análogo evolutivo es el núcleo de calor de
> [[Calor en Dominio Infinito]].

---

## Ejemplo

> [!ejemplo] El potencial de una carga puntual resuelve Poisson
> Una carga puntual de magnitud unidad en el origen crea (en unidades de Gauss, con
> $\varepsilon_0=1$) el potencial
> $$u(\mathbf{x})=\Phi(\mathbf{x})=\frac{1}{4\pi r},\qquad r=\lvert\mathbf{x}\rvert.$$
> Afirmamos que este potencial resuelve la **ecuación de Poisson con fuente puntual**
> $$-\nabla^2 u=\delta(\mathbf{x}).$$
> Comprobémoslo en dos partes, que es justo lo que hará la demostración de abajo:
> - **Fuera del origen** ($r>0$): un cálculo directo da $\nabla^2(1/r)=0$, de modo que $-\nabla^2u=0$,
>   coherente con que ahí no hay carga.
> - **En el origen**: $1/r$ explota, así que toda la "fuente" se concentra en $\mathbf{x}=\mathbf{0}$.
>   Midiendo cuánto, mediante el flujo a través de una esfera diminuta, sale exactamente $-1$, es
>   decir una delta de peso $1$.
>
> Físicamente esto es la **ley de Coulomb** (o la de Newton, idéntica en forma): el campo
> $\mathbf{E}=-\nabla u=\dfrac{\hat{\mathbf{r}}}{4\pi r^2}$ decae como $1/r^2$ y su flujo total
> a través de cualquier esfera cerrada vale $1$, sin importar el radio. Eso es el teorema de Gauss
> diciéndonos que dentro hay una carga unidad.
>
> El **mismo papel** lo juega, para la ecuación del calor, el núcleo gaussiano
> $G(x,t)=\frac{1}{\sqrt{4\pi\alpha^2 t}}\,e^{-x^2/(4\alpha^2 t)}$: es la respuesta a un dato inicial
> $\delta$, la solución fundamental del operador del calor (ver [[Calor en Dominio Infinito]]). En
> ambos casos: una sola respuesta al impulso, y todo lo demás por superposición.

## En qué consiste

> [!teoria]
> ¿Por qué la solución fundamental es tan central? Porque cualquier fuente $f$ se descompone en una
> **superposición continua de impulsos**,
> $$f(\mathbf{x})=\int f(\boldsymbol{\xi})\,\delta(\mathbf{x}-\boldsymbol{\xi})\,d\boldsymbol{\xi},$$
> y si conocemos la respuesta $\Phi$ a **un** impulso, la respuesta a $f$ se arma sumando todas esas
> respuestas (esto es la convolución, al final de la nota). La solución fundamental es así la
> "unidad de construcción" con la que se levanta toda solución.
>
> La forma concreta de $\Phi$ está fijada por dos exigencias:
> 1. ser **armónica** ($\nabla^2\Phi=0$) en todas partes salvo el origen, porque fuera de la carga
>    no hay fuente;
> 2. tener en el origen una **singularidad** del tamaño justo para que el flujo total valga $-1$,
>    que es lo que codifica la delta.
>
> En 3D la función $1/r$ cumple ambas; en 2D el papel lo hace $\ln r$ (la singularidad logarítmica
> es más suave porque "hay menos espacio" hacia donde escapar el flujo).

> [!teorema] $-\nabla^2\Phi=\delta$ en 3D
> La función $\Phi(\mathbf{x})=\dfrac{1}{4\pi r}$, con $r=\lvert\mathbf{x}\rvert$, satisface en el
> sentido de las distribuciones
> $$-\nabla^2\Phi=\delta(\mathbf{x}).$$

> [!demostracion]
> **Paso 1 — $\Phi$ es armónica para $r>0$.** En coordenadas esféricas, para una función que solo
> depende de $r$, el laplaciano se reduce a
> $$\nabla^2\Phi=\frac{1}{r^2}\frac{d}{dr}\!\left(r^2\frac{d\Phi}{dr}\right).$$
> Con $\Phi=\frac{1}{4\pi r}$ se tiene $\dfrac{d\Phi}{dr}=-\dfrac{1}{4\pi r^2}$, luego
> $r^2\dfrac{d\Phi}{dr}=-\dfrac{1}{4\pi}$ es **constante** y su derivada en $r$ es nula. Por tanto
> $\nabla^2\Phi=0$ para todo $r>0$: fuera del origen no hay fuente, como debe ser.
>
> **Paso 2 — Medir la singularidad por el flujo.** Integramos $\nabla^2\Phi$ sobre una bola pequeña
> $B_\varepsilon$ de radio $\varepsilon$ centrada en el origen y aplicamos el **teorema de la
> divergencia** ($\int_{B_\varepsilon}\nabla^2\Phi=\oint_{\partial B_\varepsilon}\nabla\Phi\cdot\hat n\,dS$,
> con $\hat n=\hat{\mathbf{r}}$ y $\nabla\Phi\cdot\hat n=\partial_r\Phi$):
> $$\int_{B_\varepsilon}\nabla^2\Phi\,dV
> =\oint_{\partial B_\varepsilon}\partial_r\Phi\,dS
> =\left(-\frac{1}{4\pi\varepsilon^2}\right)\cdot\underbrace{4\pi\varepsilon^2}_{\text{área de }\partial B_\varepsilon}
> =-1.$$
> El resultado es $-1$ **para cualquier** $\varepsilon$, por pequeño que sea: el aporte no se diluye
> al encoger la bola.
>
> **Paso 3 — Identificar la delta.** Tenemos una función que vale $0$ en todas partes salvo el
> origen, pero cuya integral sobre cualquier entorno del origen vale $-1$. Eso es, por definición,
> una **delta de Dirac de peso $-1$**: $\nabla^2\Phi=-\delta(\mathbf{x})$. Cambiando de signo,
> $$-\nabla^2\Phi=\delta(\mathbf{x}). \qquad\blacksquare$$
>
> En 2D el cálculo es idéntico salvo geometría: con $\Phi=-\frac{1}{2\pi}\ln r$ se obtiene
> $\partial_r\Phi=-\frac{1}{2\pi r}$ y el perímetro del círculo es $2\pi\varepsilon$, de nuevo con
> producto $-1$. El factor de normalización ($\frac1{2\pi}$ o $\frac1{4\pi}$) no es más que el
> "área de la esfera unidad" en cada dimensión.

> [!info] La solución de Poisson es una convolución
> Una vez que se tiene $\Phi$, la solución de la ecuación de Poisson **en espacio libre**
> $-\nabla^2 u=f$ se obtiene por superposición de impulsos: cada elemento de fuente
> $f(\boldsymbol{\xi})\,d\boldsymbol{\xi}$ contribuye con $\Phi(\mathbf{x}-\boldsymbol{\xi})$, y se suma
> todo,
> $$u(\mathbf{x})=(\Phi*f)(\mathbf{x})=\int_{\mathbb{R}^n}\Phi(\mathbf{x}-\boldsymbol{\xi})\,f(\boldsymbol{\xi})\,d\boldsymbol{\xi}.$$
> En 3D esto es la conocida fórmula del potencial
> $u(\mathbf{x})=\dfrac{1}{4\pi}\displaystyle\int\dfrac{f(\boldsymbol{\xi})}{\lvert\mathbf{x}-\boldsymbol{\xi}\rvert}\,d\boldsymbol{\xi}$:
> el potencial creado por una distribución continua de carga $f$. La solución fundamental es, pues,
> el **núcleo** de la convolución que invierte el laplaciano.

> [!warning] La convolución resuelve el espacio libre, no un dominio acotado
> La fórmula $u=\Phi*f$ vale en **todo $\mathbb{R}^n$**, donde la única condición es que $u$ decaiga
> en el infinito. En un dominio con fronteras ($u=g$ en $\partial\Omega$) esta $u$ **no** cumplirá,
> en general, el dato de frontera: hay que añadirle una corrección armónica. Esa es exactamente la
> diferencia entre la **solución fundamental** $\Phi$ y la **función de Green** $G$ del dominio,
> tema de [[Funcion de Green y Condiciones]].

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Definición | $L\,\Phi=\delta$ en espacio libre (sin fronteras) |
> | Laplace 2D | $\Phi=-\dfrac{1}{2\pi}\ln\lvert\mathbf{x}\rvert$ |
> | Laplace 3D | $\Phi=\dfrac{1}{4\pi\,\lvert\mathbf{x}\rvert}$ |
> | Interpretación | potencial de una carga puntual (Coulomb / Newton) |
> | Armónica salvo origen | $\nabla^2\Phi=0$ para $r>0$ |
> | Singularidad | flujo $=-1$ en cualquier bola $\Rightarrow\ -\nabla^2\Phi=\delta$ |
> | Solución de Poisson | $u=\Phi*f$ (convolución en espacio libre) |
> | Análogo del calor | núcleo gaussiano $G(x,t)$ |

> [!corolario]
> La solución fundamental encapsula la **respuesta universal al impulso**: una vez conocida, resolver
> $-\nabla^2u=f$ en espacio libre es una simple integral $u=\Phi*f$. Es el bloque mínimo a partir del
> cual se levantan las funciones de Green de dominios concretos, sumándole una corrección que ajuste
> la frontera.

> [!referencia]
> - Corrección para fronteras: [[Funcion de Green y Condiciones]].
> - Construirla por simetría: [[Metodo de las Imagenes]].
> - El análogo evolutivo (núcleo de calor): [[Calor en Dominio Infinito]].
> - El índice de la sección: [[Funciones de Green para EDP/index]].
