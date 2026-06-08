---
title: Variación de Parámetros (sistemas)
tags:
  - ecuaciones
  - edo
  - teoria
  - sistemas
  - no-homogenea
draft: false
aliases:
  - variacion de parametros sistemas
  - variacion de constantes
  - formula de Duhamel
  - integral de Duhamel
  - variation of parameters systems
---

# Variación de Parámetros (sistemas)

> [!definicion]
> Para el sistema **no homogéneo** $\dot{\mathbf{x}}=A\mathbf{x}+\mathbf{g}(t)$, si $\Phi(t)$ es una
> [[Matriz Fundamental| matriz fundamental]] del homogéneo asociado (sus columnas son $n$ soluciones
> independientes de $\dot{\mathbf{x}}=A\mathbf{x}$), entonces una **solución particular** es
> $$\mathbf{x}_p(t)=\Phi(t)\int\Phi^{-1}(s)\,\mathbf{g}(s)\,ds.$$
> Tomando $\Phi(t)=e^{At}$ (la [[Exponencial de una Matriz| exponencial de matriz]]) y el dato
> inicial $\mathbf{x}(0)=\mathbf{x}_0$, la solución del problema de valor inicial queda en la forma
> cerrada
> $$\boxed{\ \mathbf{x}(t)=e^{At}\mathbf{x}_0+\int_0^t e^{A(t-s)}\,\mathbf{g}(s)\,ds\ }$$
> conocida como **fórmula de variación de constantes** o **integral de Duhamel**.

> [!info]
> Cierra la parte de cálculo del bloque [[Sistemas y Dinamica/index| sistemas y dinámica]]: una vez
> que sabemos resolver el homogéneo por [[Sistemas Lineales Autovalores| autovalores]] y empaquetarlo
> en $e^{At}$, esta fórmula vence cualquier **fuente** $\mathbf{g}(t)$. Es el análogo **vectorial** de
> la [[Variacion de Parametros| variación de parámetros]] escalar: allí los coeficientes
> $c_i$ de la solución se dejaban variar; aquí dejamos variar el **vector** de constantes $\mathbf{u}(t)$
> que multiplica a la matriz fundamental. Pertenece al [[1 Ecuaciones Diferenciales Ordinarias/index| capítulo de EDO]].

---

## Ejemplo

> [!ejemplo] Oscilador forzado en resonancia, vía Duhamel
> **Resolver $\dot{\mathbf{x}}=\begin{pmatrix}0&1\\-1&0\end{pmatrix}\mathbf{x}+\begin{pmatrix}0\\ \cos t\end{pmatrix}$ con $\mathbf{x}(0)=\mathbf{0}$.**
>
> Este sistema es el oscilador $\ddot y+y=\cos t$ escrito en variables $x_1=y$, $x_2=\dot y$: la
> frecuencia natural es $\omega_0=1$ y la fuerza tiene frecuencia $1$, así que esperamos **resonancia**.
>
> **Paso 1 — la matriz fundamental.** El homogéneo es una rotación pura ($A$ antisimétrica con
> autovalores $\pm i$), de modo que
> $$e^{At}=\begin{pmatrix}\cos t&\operatorname{sen}t\\-\operatorname{sen}t&\cos t\end{pmatrix},
> \qquad e^{-As}=\begin{pmatrix}\cos s&-\operatorname{sen}s\\ \operatorname{sen}s&\cos s\end{pmatrix}.$$
>
> **Paso 2 — el integrando $e^{-As}\mathbf{g}(s)$.** Con $\mathbf{g}(s)=(0,\cos s)^{\!\top}$,
> $$e^{-As}\mathbf{g}(s)=\begin{pmatrix}\cos s&-\operatorname{sen}s\\ \operatorname{sen}s&\cos s\end{pmatrix}\begin{pmatrix}0\\ \cos s\end{pmatrix}=\begin{pmatrix}-\operatorname{sen}s\cos s\\ \cos^2 s\end{pmatrix}=\begin{pmatrix}-\tfrac12\operatorname{sen}2s\\ \tfrac12+\tfrac12\cos 2s\end{pmatrix}.$$
>
> **Paso 3 — integrar de $0$ a $t$.**
> $$\int_0^t e^{-As}\mathbf{g}(s)\,ds=\begin{pmatrix}\tfrac14(\cos 2t-1)\\[2pt] \tfrac{t}{2}+\tfrac14\operatorname{sen}2t\end{pmatrix}.$$
> Nótese el término $\tfrac{t}{2}$ en la segunda componente: **crece linealmente con $t$**, la firma de
> la resonancia.
>
> **Paso 4 — multiplicar por $e^{At}$.** $\mathbf{x}(t)=e^{At}\displaystyle\int_0^t e^{-As}\mathbf{g}(s)\,ds$.
> La primera componente (la posición $y=x_1$) resulta
> $$x_1(t)=\frac{t}{2}\,\operatorname{sen}t,$$
> exactamente la solución resonante $\propto t$ del oscilador forzado en su frecuencia natural, de acuerdo
> con [[Oscilaciones Forzadas y Resonancia| resonancia]]. La amplitud no se satura: crece sin cota.

---

## En qué consiste

> [!teoria]
> La idea es **promover las constantes a funciones**. La solución general del homogéneo es
> $\mathbf{x}_h=\Phi(t)\mathbf{c}$ con $\mathbf{c}$ un vector constante (cada componente de $\mathbf{c}$
> selecciona una combinación de las columnas de $\Phi$). Para atrapar la fuente $\mathbf{g}(t)$ dejamos
> que ese vector **varíe en el tiempo**, $\mathbf{c}\rightsquigarrow\mathbf{u}(t)$, y proponemos
> $\mathbf{x}=\Phi(t)\mathbf{u}(t)$. La condición de que esto resuelva el sistema fija $\mathbf{u}(t)$
> mediante una sola integración. Es el mismo truco que en el caso escalar, pero ahora $\Phi$ es una
> matriz y $\mathbf{u}$ un vector.

> [!teorema] Fórmula de variación de constantes
> Sea $\Phi(t)$ matriz fundamental de $\dot{\mathbf{x}}=A\mathbf{x}$ (luego $\dot\Phi=A\Phi$ y $\Phi$ es
> invertible para todo $t$). Entonces toda solución de $\dot{\mathbf{x}}=A\mathbf{x}+\mathbf{g}(t)$ es
> $$\mathbf{x}(t)=\Phi(t)\,\mathbf{c}+\Phi(t)\int \Phi^{-1}(s)\,\mathbf{g}(s)\,ds,$$
> y con $\Phi=e^{At}$ y $\mathbf{x}(0)=\mathbf{x}_0$ se reduce a
> $\mathbf{x}(t)=e^{At}\mathbf{x}_0+\int_0^t e^{A(t-s)}\mathbf{g}(s)\,ds$.

> [!demostracion]
> **Paso 1 — proponer la forma.** Buscamos la solución como $\mathbf{x}=\Phi(t)\,\mathbf{u}(t)$, con
> $\mathbf{u}(t)$ un vector de funciones a determinar (variación del vector de constantes).
>
> **Paso 2 — derivar y sustituir.** Por la regla del producto,
> $$\dot{\mathbf{x}}=\dot\Phi\,\mathbf{u}+\Phi\,\dot{\mathbf{u}}=A\Phi\,\mathbf{u}+\Phi\,\dot{\mathbf{u}},$$
> usando $\dot\Phi=A\Phi$. Igualando con $A\mathbf{x}+\mathbf{g}=A\Phi\,\mathbf{u}+\mathbf{g}$, los
> términos $A\Phi\,\mathbf{u}$ se cancelan y queda
> $$\Phi\,\dot{\mathbf{u}}=\mathbf{g}.$$
>
> **Paso 3 — despejar e integrar.** Como $\Phi$ es invertible, $\dot{\mathbf{u}}=\Phi^{-1}\mathbf{g}$,
> de donde $\mathbf{u}(t)=\int\Phi^{-1}(s)\mathbf{g}(s)\,ds$ y por tanto
> $$\mathbf{x}_p=\Phi(t)\int\Phi^{-1}(s)\,\mathbf{g}(s)\,ds.$$
> Sumando la solución homogénea $\Phi\mathbf{c}$ se obtiene la general. $\blacksquare$

> [!demostracion] De la forma general a la integral de Duhamel
> Tomemos $\Phi(t)=e^{At}$, que cumple $\Phi(0)=I$ y $\Phi^{-1}(s)=e^{-As}$. Imponiendo
> $\mathbf{x}(0)=\mathbf{x}_0$ se fija $\mathbf{c}=\mathbf{x}_0$ y se elige el límite inferior $0$ en la
> integral, así $\mathbf{x}_p(0)=\mathbf{0}$. Con la propiedad $e^{At}e^{-As}=e^{A(t-s)}$ (válida porque
> $At$ y $-As$ conmutan),
> $$\mathbf{x}(t)=e^{At}\mathbf{x}_0+e^{At}\int_0^t e^{-As}\mathbf{g}(s)\,ds=e^{At}\mathbf{x}_0+\int_0^t e^{A(t-s)}\mathbf{g}(s)\,ds.\qquad\blacksquare$$

> [!algoritmo] Resolver $\dot{\mathbf{x}}=A\mathbf{x}+\mathbf{g}(t)$, $\mathbf{x}(0)=\mathbf{x}_0$
> 1. Halla la matriz fundamental $\Phi(t)$ del homogéneo (por [[Sistemas Lineales Autovalores| autovalores]]); lo más cómodo es $\Phi=e^{At}$, que cumple $\Phi(0)=I$.
> 2. Calcula $\Phi^{-1}(s)$. Si $\Phi=e^{At}$, simplemente $\Phi^{-1}(s)=e^{-As}$.
> 3. Forma el integrando $\Phi^{-1}(s)\,\mathbf{g}(s)$ e **integra componente a componente** de $0$ a $t$.
> 4. Multiplica por la izquierda por $\Phi(t)$ para obtener $\mathbf{x}_p(t)$.
> 5. Suma la parte homogénea: $\mathbf{x}(t)=e^{At}\mathbf{x}_0+\mathbf{x}_p(t)$.

> [!proposicion] El núcleo $e^{A(t-s)}$ es un propagador
> En la forma de Duhamel, $e^{A(t-s)}$ traslada el "impulso" $\mathbf{g}(s)\,ds$ recibido en el instante
> $s$ hasta el instante de observación $t$: el estado en $t$ es la **superposición** de todos los
> empujones pasados, cada uno propagado por el flujo libre durante el lapso $t-s$. Es el principio de
> superposición de [[Operador Diferencial Lineal| sistemas lineales]] escrito con un integral, y el germen
> de la [[Funcion de Green para EDO| función de Green]].

> [!warning]
> La fórmula con $e^{A(t-s)}$ exige $A$ **constante**: solo entonces $e^{At}e^{-As}=e^{A(t-s)}$, porque
> $At$ y $-As$ conmutan. Si $A=A(t)$ depende del tiempo, esa simplificación **falla** (los $A$ en
> instantes distintos no conmutan en general) y hay que quedarse con la forma
> $\mathbf{x}=\Phi(t)\,\mathbf{c}+\Phi(t)\int\Phi^{-1}(s)\mathbf{g}(s)\,ds$ usando la matriz fundamental
> genuina $\Phi$.

## Resumen

> [!resumen]
> | Objeto | Expresión |
> |---|---|
> | Sistema | $\dot{\mathbf{x}}=A\mathbf{x}+\mathbf{g}(t)$ |
> | Propuesta | $\mathbf{x}=\Phi(t)\,\mathbf{u}(t)$ |
> | Condición | $\Phi\,\dot{\mathbf{u}}=\mathbf{g}\;\Rightarrow\;\dot{\mathbf{u}}=\Phi^{-1}\mathbf{g}$ |
> | Particular | $\mathbf{x}_p=\Phi(t)\displaystyle\int\Phi^{-1}(s)\,\mathbf{g}(s)\,ds$ |
> | Duhamel (PVI) | $\mathbf{x}(t)=e^{At}\mathbf{x}_0+\displaystyle\int_0^t e^{A(t-s)}\mathbf{g}(s)\,ds$ |

> [!corolario]
> La solución completa es **homogéneo + memoria de la fuente**: el primer término $e^{At}\mathbf{x}_0$
> propaga la condición inicial, y la integral acumula la respuesta a $\mathbf{g}$ instante por instante,
> propagada por el mismo $e^{At}$. Toda la dificultad del sistema no homogéneo se traslada a **conocer
> $e^{At}$** (o $\Phi$); lo demás es una integración.

> [!referencia]
> - El homogéneo y su solución: [[Sistemas Lineales Autovalores]].
> - El objeto $\Phi$ y su inversa: [[Matriz Fundamental]] y [[Exponencial de una Matriz]].
> - Análogo escalar: [[Variacion de Parametros]].
