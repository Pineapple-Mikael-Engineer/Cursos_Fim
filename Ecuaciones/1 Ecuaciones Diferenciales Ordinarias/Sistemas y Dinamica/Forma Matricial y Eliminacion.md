---
title: Forma Matricial y Eliminación
tags:
  - ecuaciones
  - edo
  - teoria
  - sistemas
  - forma-matricial
draft: false
aliases:
  - forma matricial y eliminación
  - reducción a sistema
  - método de eliminación
  - matrix form and elimination
  - operator method
---

# Forma Matricial y Eliminación

> [!definicion]
> Un **sistema lineal de primer orden** se escribe en forma matricial como
> $$\dot{\mathbf{x}}=A\mathbf{x}+\mathbf{g}(t),\qquad \mathbf{x}=(x_1,\dots,x_n)^{\!\top},$$
> donde $A$ es la matriz de coeficientes y $\mathbf{g}(t)$ el término de fuente. Hay un **diccionario
> en dos direcciones**: toda EDO de orden $n$ se convierte en un sistema de $n$ ecuaciones de primer
> orden tomando como variables $x_1=y,\ x_2=y',\ \dots,\ x_n=y^{(n-1)}$; y a la inversa, **eliminando**
> variables un sistema de $n$ ecuaciones de primer orden se reduce a **una sola** EDO de orden $n$.

> [!info]
> Es la nota de **traducción** del bloque [[Sistemas y Dinamica/index| sistemas y dinámica]]: nos deja
> pasar libremente entre el lenguaje de **una ecuación de orden alto** y el de **un sistema vectorial**.
> Una vez en forma matricial, la maquinaria de [[Sistemas Lineales Autovalores| autovalores]], la
> [[Matriz Fundamental| matriz fundamental]] y la [[Exponencial de una Matriz| exponencial de matriz]]
> resuelven el sistema; en sentido inverso, la **eliminación** reduce el problema a la ya conocida
> [[Coeficientes Constantes Homogenea| ecuación característica]] escalar. Pertenece al
> [[1 Ecuaciones Diferenciales Ordinarias/index| capítulo de EDO]].

---

## Ejemplo

> [!ejemplo] De orden superior a sistema
> **Convertir $y''-3y'+2y=0$ en un sistema de primer orden.**
> **Paso 1 — nombrar las derivadas como variables.** Sea $x_1=y$ y $x_2=y'$. Entonces $\dot x_1=y'=x_2$.
> **Paso 2 — despejar la derivada más alta.** De la ecuación, $y''=3y'-2y=3x_2-2x_1$, es decir $\dot x_2=-2x_1+3x_2$.
> **Paso 3 — apilar en forma matricial.**
> $$\dot{\mathbf{x}}=\begin{pmatrix}\dot x_1\\\dot x_2\end{pmatrix}=\begin{pmatrix}0&1\\-2&3\end{pmatrix}\begin{pmatrix}x_1\\x_2\end{pmatrix}=A\mathbf{x}.$$
> La última fila de $A$ son **los coeficientes de la ecuación con signo cambiado** (la fila $(-a_0,-a_1)$ para $y''+a_1y'+a_0y=0$): aquí $a_1=-3,\ a_0=2$, así que la fila es $(-2,\,3)$. Esa estructura —unos en la subdiagonal y los coeficientes abajo— se llama **matriz compañera**.

> [!ejemplo] De sistema a una sola EDO (eliminación)
> **Resolver el sistema $\dot x=4x-y,\quad \dot y=2x+y$.**
> **Paso 1 — derivar una ecuación.** Derivo la primera: $\ddot x=4\dot x-\dot y$.
> **Paso 2 — usar la otra ecuación.** Sustituyo $\dot y=2x+y$: $\ddot x=4\dot x-(2x+y)$.
> **Paso 3 — eliminar la variable sobrante.** De la primera ecuación, $y=4x-\dot x$. Lo meto arriba:
> $$\ddot x=4\dot x-2x-(4x-\dot x)=5\dot x-6x\ \Longrightarrow\ \ddot x-5\dot x+6x=0.$$
> **Paso 4 — resolver la EDO escalar.** Ecuación característica $r^2-5r+6=(r-2)(r-3)=0$, luego
> $$x(t)=c_1e^{2t}+c_2e^{3t}.$$
> **Paso 5 — recuperar la otra variable.** Con $\dot x=2c_1e^{2t}+3c_2e^{3t}$ y $y=4x-\dot x$:
> $$y(t)=4(c_1e^{2t}+c_2e^{3t})-(2c_1e^{2t}+3c_2e^{3t})=2c_1e^{2t}+c_2e^{3t}.$$
> No aparecen constantes nuevas: $y$ queda **determinada** por $x$, como debe ser en un sistema $2\times2$ con dos constantes en total.

---

## En qué consiste

> [!teoria]
> Las dos direcciones son **inversas** la una de la otra y descansan en la misma idea: **derivar
> introduce información** y **una variable por cada orden de derivada**.
> - **Subir de dimensión (orden $\to$ sistema):** una ecuación de orden $n$ esconde $n$ datos iniciales
>   ($y,y',\dots,y^{(n-1)}$). Si los promovemos a $n$ variables, el orden cae a $1$ pero la dimensión
>   sube a $n$. El total de constantes ($n$) se conserva.
> - **Bajar de dimensión (sistema $\to$ orden):** $n$ ecuaciones de primer orden también guardan $n$
>   constantes. Derivando una de ellas y sustituyendo las demás, eliminamos variables hasta quedarnos
>   con una sola incógnita y su EDO de orden $n$.

> [!algoritmo] Orden superior → sistema
> Para $y^{(n)}+a_{n-1}y^{(n-1)}+\dots+a_1y'+a_0y=f(t)$:
> 1. Define $x_1=y,\ x_2=y',\ \dots,\ x_n=y^{(n-1)}$.
> 2. Las primeras $n-1$ ecuaciones son inmediatas: $\dot x_1=x_2,\ \dot x_2=x_3,\ \dots,\ \dot x_{n-1}=x_n$.
> 3. La última despeja $y^{(n)}$: $\dot x_n=-a_0x_1-a_1x_2-\dots-a_{n-1}x_n+f(t)$.
> 4. Apila: $\dot{\mathbf{x}}=A\mathbf{x}+\mathbf{g}(t)$ con $A$ la **matriz compañera** y $\mathbf{g}=(0,\dots,0,f)^{\!\top}$.

> [!algoritmo] Sistema → una sola EDO
> Para un sistema lineal $2\times2$ (la idea generaliza a $n$):
> 1. Elige una variable, p. ej. $x$, y deriva su ecuación: obtienes $\ddot x$ en términos de las derivadas de las demás.
> 2. Sustituye esas derivadas usando las **otras** ecuaciones del sistema.
> 3. Elimina la variable sobrante despejándola de la ecuación original.
> 4. Queda una EDO de orden $n$ en una sola incógnita; resuélvela con su [[Coeficientes Constantes Homogenea| ecuación característica]].
> 5. Recupera las demás variables por sustitución, **sin** añadir constantes nuevas.

> [!info] El método de operadores $D$
> Escribiendo $D=\dfrac{d}{dt}$, el sistema del ejemplo es
> $$(D-4)x+y=0,\qquad -2x+(D-1)y=0.$$
> Se tratan los **operadores como coeficientes** y se elimina por combinación lineal, igual que en un
> sistema algebraico. Multiplicando la primera por $(D-1)$ y restando la segunda se cancela $y$ y aparece
> directamente el **operador característico** $\big[(D-4)(D-1)+2\big]x=(D^2-5D+6)x=0$, que es justo
> $\ddot x-5\dot x+6x=0$. Es la misma eliminación, pero contable como álgebra de polinomios en $D$.

> [!warning]
> Al eliminar, **no inventes constantes nuevas** al integrar las variables recuperadas: cada constante
> espuria debe fijarse sustituyendo de vuelta en una de las ecuaciones originales. Un sistema $n\times n$
> tiene **exactamente $n$** constantes arbitrarias en total. Además la eliminación puede fallar o
> complicarse si $A$ no es de coeficientes constantes; entonces conviene quedarse en forma matricial.

> [!proposicion] El polinomio característico es el mismo
> La EDO escalar que produce la eliminación tiene por polinomio característico exactamente
> $\det(A-\lambda I)$, el **polinomio característico de la matriz**. En el ejemplo,
> $\det\!\begin{pmatrix}4-\lambda&-1\\2&1-\lambda\end{pmatrix}=(4-\lambda)(1-\lambda)+2=\lambda^2-5\lambda+6$,
> que coincide con $r^2-5r+6$. Por eso eliminar y diagonalizar dan **los mismos exponentes** $e^{\lambda t}$.

## Resumen

> [!resumen]
> | Dirección | Construcción | Resultado |
> |---|---|---|
> | Orden $n$ → sistema | $x_k=y^{(k-1)}$ | $\dot{\mathbf{x}}=A\mathbf{x}+\mathbf{g}$, $A$ compañera |
> | Sistema → orden $n$ | derivar + eliminar | una EDO escalar de orden $n$ |
> | Operadores $D$ | tratar $D$ como coeficiente | operador característico $p(D)x=0$ |
> | Característica | $\det(A-\lambda I)=0$ | **mismos** exponentes $e^{\lambda t}$ |

> [!corolario]
> Sistema de primer orden y ecuación de orden superior son **dos caras de lo mismo**: cambian la
> dimensión por el orden pero conservan el número de constantes y, sobre todo, el **espectro**. Por eso
> elegimos la cara más cómoda: forma matricial para usar álgebra lineal, ecuación escalar para usar la
> característica clásica.

> [!referencia]
> - Resolver ya en forma matricial: [[Sistemas Lineales Autovalores]].
> - Empaquetar las soluciones: [[Matriz Fundamental]].
> - El análogo escalar de la eliminación: [[Coeficientes Constantes Homogenea]].
> - Volver al mapa del bloque: [[Sistemas y Dinamica/index]].
