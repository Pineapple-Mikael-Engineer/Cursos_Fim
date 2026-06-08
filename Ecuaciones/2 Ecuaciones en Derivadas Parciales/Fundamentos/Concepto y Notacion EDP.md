---
title: Concepto y Notación de EDP
tags:
  - ecuaciones
  - edp
  - teoria
  - fundamentos
  - notacion
draft: false
aliases:
  - concepto de EDP
  - notación de subíndices
  - orden y linealidad de EDP
  - PDE concept and notation
  - linear quasilinear nonlinear PDE
---

# Concepto y Notación de EDP

> [!definicion]
> Una **ecuación en derivadas parciales (EDP)** es una ecuación que relaciona una función
> incógnita de **varias variables** $u=u(x,y,\dots)$ con sus **derivadas parciales**. Se usa la
> **notación de subíndices**:
> $$u_x=\frac{\partial u}{\partial x},\qquad u_{xx}=\frac{\partial^2 u}{\partial x^2},\qquad u_{xy}=\frac{\partial^2 u}{\partial x\,\partial y}.$$
> El **orden** de la EDP es el de la derivada parcial más alta que aparece. Una EDP es:
> - **lineal** si $u$ y todas sus derivadas aparecen a la **potencia 1**, sin productos entre ellas ni funciones no lineales de $u$; equivale a escribirla como $L[u]=f$ con $L$ un operador **lineal**;
> - **cuasilineal** si es lineal en las derivadas de **orden máximo**, pero sus coeficientes pueden depender de $u$ y de sus derivadas de orden menor;
> - **no lineal** en cualquier otro caso.

> [!info]
> Nota de entrada de los [[Fundamentos/index| fundamentos de EDP]]: fija el lenguaje (orden,
> linealidad, subíndices) que usan todas las demás notas. El **orden** y la **linealidad** que se
> definen aquí alimentan directamente la [[Clasificacion Segundo Orden| clasificación de segundo orden]] y deciden qué [[Tipos de Condiciones| condiciones]] cierran el problema.

---

## Ejemplo

> [!ejemplo] Resolver las EDP más simples y ver aparecer **funciones arbitrarias**
> El rasgo que distingue una EDP de una EDO es que su solución general lleva **funciones
> arbitrarias** en lugar de **constantes** arbitrarias. Lo vemos integrando tres ecuaciones de
> primer orden, tratando como **parámetro fijo** a la variable que no se deriva.
>
> **(a)** $u_x=0$, con $u=u(x,y)$. Integrar respecto a $x$ pide que $u$ no dependa de $x$: la
> "constante" de integración puede depender de $y$. Luego
> $$u(x,y)=f(y),\qquad f\ \text{arbitraria}.$$
>
> **(b)** $u_{xy}=0$. Escribimos $u_{xy}=(u_x)_y=0$: entonces $u_x$ no depende de $y$, así
> $u_x=\varphi(x)$. Integrando en $x$, $u=\int\varphi(x)\,dx+G(y)=F(x)+G(y)$. La solución general es
> $$u(x,y)=F(x)+G(y),\qquad F,G\ \text{arbitrarias}.$$
>
> **(c)** $u_x=u$. Para $y$ fijo es una EDO lineal en $x$ cuya solución es $e^x$ por una "constante"
> que puede depender de $y$:
> $$u(x,y)=f(y)\,e^{x},\qquad f\ \text{arbitraria}.$$
>
> En los tres casos, dar **condiciones** (una curva de datos, valores en la frontera) es lo que
> **selecciona** la función arbitraria concreta.

---

## En qué consiste

> [!teoria] Por qué funciones arbitrarias y no constantes
> Al integrar una EDO de orden $n$ aparecen $n$ **constantes** porque solo hay una variable
> independiente. En una EDP, cada vez que "integramos respecto a una variable", lo que queda
> indeterminado puede **variar libremente a lo largo de las otras variables**: por eso surge una
> **función** arbitraria, no un número. Geométricamente, una EDO selecciona una **curva** integral
> con unos pocos datos; una EDP de primer orden selecciona una **superficie** integral, y hace falta
> dar datos sobre toda una **curva** (no solo un punto) para fijarla. Esta es la raíz de por qué la
> teoría de EDP gira en torno a **qué** condiciones imponer, tema de
> [[Problemas Bien Planteados| problemas bien planteados]].

> [!algoritmo] Leer orden y tipo de una EDP
> 1. Identifica la función incógnita y sus variables independientes.
> 2. Localiza la derivada de **mayor orden**: ese número es el **orden**.
> 3. Mira si $u$ y sus derivadas aparecen a potencia 1 y sin productos entre sí:
>    - sí, y los coeficientes solo dependen de las variables independientes → **lineal**;
>    - sí en las derivadas de **orden máximo**, pero algún coeficiente depende de $u$ o derivadas menores → **cuasilineal**;
>    - en otro caso → **no lineal**.

> [!teorema] Principio de superposición (caso lineal **homogéneo**)
> Sea $L$ un operador diferencial **lineal**. Si $u_1$ y $u_2$ son soluciones de $L[u]=0$, entonces
> cualquier combinación lineal $c_1u_1+c_2u_2$ ($c_1,c_2$ constantes) también lo es:
> $$L[u_1]=0,\ L[u_2]=0\ \Longrightarrow\ L[c_1u_1+c_2u_2]=0.$$

> [!demostracion]
> **Paso 1 — linealidad de la derivación.** Cada derivada parcial es un operador lineal:
> $\partial_x(c_1u_1+c_2u_2)=c_1\,\partial_xu_1+c_2\,\partial_xu_2$, e igual para $\partial_{xx}$,
> $\partial_{xy}$, etc. Como $L$ es una **suma de derivadas parciales** multiplicadas por coeficientes,
> hereda esa propiedad: $L[c_1u_1+c_2u_2]=c_1L[u_1]+c_2L[u_2]$.
> **Paso 2 — usar las hipótesis.** Sustituyendo $L[u_1]=0$ y $L[u_2]=0$,
> $$L[c_1u_1+c_2u_2]=c_1\cdot 0+c_2\cdot 0=0.$$
> Luego la combinación es solución. $\blacksquare$ Este principio es la base de **construir**
> soluciones sumando piezas elementales (modos), idea central de la
> [[Tecnica de Separacion| separación de variables]].

> [!info] Clasificación de ejemplos clásicos
> | EDP | Orden | Tipo | Comentario |
> |---|:--:|---|---|
> | calor $u_t=\alpha^2 u_{xx}$ | 2 | **lineal** | coeficientes constantes; superposición vale |
> | Laplace $u_{xx}+u_{yy}=0$ | 2 | **lineal** | homogénea; modela equilibrio |
> | Burgers $u_t+u\,u_x=0$ | 1 | **cuasilineal** | lineal en $u_t,u_x$, pero el coeficiente de $u_x$ es $u$ |
> | eikonal $\lvert\nabla u\rvert=1$ | 1 | **no lineal** | $u_x^2+u_y^2=1$: las derivadas aparecen al cuadrado |

> [!warning]
> El principio de superposición **solo** se aplica a EDP **lineales y homogéneas**. En Burgers o en la
> eikonal, sumar dos soluciones **no** da otra solución: por eso aparecen ondas de choque y cáusticas
> que no existen en el mundo lineal.

## Resumen

> [!resumen]
> | Concepto | Definición operativa |
> |---|---|
> | Orden | derivada parcial más alta presente |
> | Lineal | $L[u]=f$, $L$ lineal; $u$ y derivadas a potencia 1 |
> | Cuasilineal | lineal en las derivadas de **orden máximo**; coeficientes dependen de $u$ |
> | No lineal | productos/potencias/funciones no lineales de $u$ o derivadas |
> | Solución general | lleva **funciones** arbitrarias (no constantes) |

> [!corolario]
> Antes de clasificar por tipo o elegir método, contesta dos preguntas: **¿de qué orden es?** y
> **¿es lineal?** El orden cuenta cuántos datos hacen falta; la linealidad decide si vale la
> superposición —la herramienta que hace resoluble casi toda EDP "de física".

> [!referencia]
> - El siguiente paso, clasificar por discriminante: [[Clasificacion Segundo Orden]].
> - Qué datos cierran cada EDP: [[Tipos de Condiciones]].
> - El marco general de la sección: [[Fundamentos/index]].
