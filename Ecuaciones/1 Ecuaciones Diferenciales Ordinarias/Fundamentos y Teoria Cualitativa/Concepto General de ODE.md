---
title: Concepto General de ODE
order: 1
tags:
  - ecuaciones
  - edo
  - teoria
  - fundamentos
  - concepto-general
draft: false
aliases:
  - concepto general de ode
  - ecuación diferencial ordinaria
  - ordinary differential equation
  - forma normal
  - problema de valor inicial
---

# Concepto General de ODE

> [!definicion]
> Una **ecuación diferencial** relaciona una función incógnita con sus derivadas. Es **ordinaria** (EDO) si todas las derivadas son respecto a **una sola** variable; es **parcial** (EDP) si hay varias. Escribiendo $y^{(n)}\equiv d^n y/dx^n$, su forma más general (**implícita**) es
> $$F\big(x,\,y,\,y',\,\dots,\,y^{(n)}\big)=0,$$
> y, cuando se despeja la derivada mayor, su **forma normal**
> $$\frac{d^n y}{dx^n}=f\big(x,\,y,\,y',\,\dots,\,y^{(n-1)}\big).$$
> El **orden** es el de la derivada más alta; el **grado** es la potencia a la que aparece esa derivada (una vez racionalizada).

> [!info]
> Es la nota de entrada al curso: fija vocabulario y notación (libro, cap. 1.2). De aquí salen la lectura geométrica del [[Campo de Direcciones e Isoclinas| campo de direcciones]], las [[Curvas Integrales y Soluciones| curvas integrales]] y el teorema de [[Existencia y Unicidad Picard| existencia y unicidad]]. El primer método concreto para resolver es [[Variables Separables| variables separables]]. Índice del bloque: [[Fundamentos y Teoria Cualitativa/index]].

---

## Ejemplo

> [!ejemplo]
> **Verificar que $y=\cos x$ resuelve $y''=-y$ en $\mathbb{R}$.** Derivando dos veces,
> $$y=\cos x\ \Rightarrow\ y'=-\sin x\ \Rightarrow\ y''=-\cos x=-y.$$
> La igualdad se cumple en **todo** $x\in\mathbb{R}$, así que $y=\cos x$ es solución sobre el intervalo $I=(-\infty,\infty)$. Es una EDO de **orden 2** (aparece $y''$) y de **grado 1** (esa derivada aparece a la primera potencia).

> [!ejemplo]
> **No toda EDO tiene solución: $\left(\dfrac{d^3x}{dt^3}\right)^2+x^2=-1$.** El lado izquierdo es suma de dos cuadrados reales, luego $\ge 0$; el derecho vale $-1<0$. No existe ninguna función real $x(t)$ que la satisfaga: el conjunto solución es **vacío**. Escribir una ecuación diferencial no garantiza que tenga solución.

> [!ejemplo]
> **Solución implícita de una separable: $y'=\dfrac{xy}{y^2+1}$.** La ecuación es [[Variables Separables| separable]]; pasamos $y$ a la izquierda,
> $$\left(y+\frac{1}{y}\right)dy=x\,dx,$$
> e integramos cada lado:
> $$\frac{y^2}{2}+\ln y=\frac{x^2}{2}+C.$$
> No se puede despejar $y(x)$ en funciones elementales. Aun así es una **solución legítima**: por el **teorema de la función implícita** (ver más abajo), como $\partial g/\partial y=y+1/y\neq0$ donde $y>0$, la relación $g(x,y)=\tfrac{y^2}{2}+\ln y-\tfrac{x^2}{2}-C=0$ define una rama $y(x)$ que satisface la EDO.

---

## En qué consiste

> [!teoria]
> Una EDO no es más que una **restricción** sobre la pendiente (y curvaturas, etc.) de la incógnita. Resolverla es hallar **todas** las funciones que la cumplen sobre un intervalo. Cuatro ideas organizan el resto del curso:
> 1. **Implícita vs. normal**: $F(\dots)=0$ es la forma cruda; despejar $y^{(n)}=f(\dots)$ (forma normal) es lo que permite aplicar teoremas y métodos numéricos.
> 2. **Orden y grado** clasifican la dificultad: el orden cuenta cuántas constantes tendrá la [[Curvas Integrales y Soluciones| solución general]].
> 3. **Solución implícita**: muchas veces lo mejor que se obtiene es $g(x,y)=0$, válida si define $y(x)$ localmente.
> 4. **PVI**: añadir condiciones iniciales selecciona **una** solución entre la familia.

> [!definicion] Solución sobre un intervalo
> Una función $y:\,I=(a,b)\to\mathbb{R}$, derivable hasta orden $n$, es **solución** de la EDO en $I$ si al sustituirla la igualdad se cumple para **todo** $x\in I$. El intervalo importa: la misma fórmula puede ser solución en un tramo y no en otro (p. ej. donde se anula un denominador).

> [!definicion] Solución implícita
> Una relación $g(x,y)=0$ es **solución implícita** si, por el **teorema de la función implícita** ($g$ de clase $C^1$ y $\partial g/\partial y\neq0$ en un punto $(x_0,y_0)$ de la curva), define una función derivable $y(x)$ en un entorno de $x_0$, y esa $y(x)$ satisface la EDO. Se verifica **derivando implícitamente** $g(x,y)=0$ sin despejar $y$.

> [!definicion] Problema de valor inicial (PVI)
> El **PVI** de primer orden es el par
> $$\begin{cases}\dfrac{dx}{dt}=f(t,x),\\[4pt] x(t_0)=x_0.\end{cases}$$
> La ecuación fija la familia de soluciones (con una constante libre); la **condición inicial** $x(t_0)=x_0$ fija esa constante y, cuando hay unicidad, selecciona **una** solución.

> [!teorema] Existencia y unicidad (caso escalar)
> Sea $f(t,x)$ **continua** en un rectángulo alrededor de $(t_0,x_0)$ y supongamos que $\partial f/\partial x$ **existe y es continua** ahí. Entonces el PVI $\dot x=f(t,x),\ x(t_0)=x_0$ tiene una solución $x(t)$ y es **única** en algún intervalo $(t_0-h,\,t_0+h)$ con $h>0$.

> [!demostracion]
> La prueba constructiva (iteración de Picard) se desarrolla en [[Existencia y Unicidad Picard]]; aquí solo registramos las **dos hipótesis clave** y su papel: continuidad de $f$ $\Rightarrow$ **existencia**; control del cociente incremental en $x$ (continuidad de $\partial f/\partial x$, condición de **Lipschitz**) $\Rightarrow$ **unicidad**. Si falla la segunda hipótesis, la unicidad puede perderse, como muestra el ejemplo siguiente. $\blacksquare$

> [!ejemplo] Pérdida de unicidad: $\dot y=x\,y^{1/2},\ y(0)=0$
> Aquí $f(x,y)=x\,y^{1/2}$ es continua, pero
> $$\frac{\partial f}{\partial y}=\frac{x}{2\sqrt{y}}$$
> **no existe** en $(0,0)$: se viola la hipótesis del teorema. Como consecuencia, el PVI tiene **dos** soluciones distintas que pasan por $(0,0)$:
> $$y\equiv 0 \qquad\text{y}\qquad y=\frac{x^4}{16}.$$
> (En efecto, separando $y^{-1/2}dy=x\,dx$ se llega a $2\sqrt y=x^2/4+c$, y con $y(0)=0$ queda $y=x^4/16$; pero la constante $y\equiv0$ también resuelve la ecuación.) Físicamente esto **rompe el determinismo**: las mismas condiciones iniciales no fijan el futuro.

### Reducción a un sistema de primer orden

> [!teoria]
> **Toda EDO de orden $n$ equivale a un sistema de $n$ ecuaciones de primer orden.** Se introducen como nuevas incógnitas la función y sus derivadas sucesivas; cada derivada pasa a ser una variable y su evolución, una ecuación. Esto unifica la teoría (basta estudiar sistemas $\dot{\mathbf{x}}= \mathbf{f}(t,\mathbf{x})$) y es lo que usan todos los métodos numéricos.

> [!algoritmo] Pasar de orden $n$ a sistema
> 1. Dada $y^{(n)}=f(x,y,y',\dots,y^{(n-1)})$, define $x_1=y,\ x_2=y',\ \dots,\ x_n=y^{(n-1)}$.
> 2. Entonces $\dot x_1=x_2,\ \dot x_2=x_3,\ \dots,\ \dot x_{n-1}=x_n$.
> 3. La última: $\dot x_n=f(t,x_1,\dots,x_n)$.
> 4. Escribe todo como $\dot{\mathbf{x}}=\mathbf{f}(t,\mathbf{x})$ con $\mathbf{x}=(x_1,\dots,x_n)^T$.

> [!ejemplo] El sistema acoplado del libro
> Dadas las ecuaciones de segundo orden acopladas
> $$\frac{d^2x}{dt^2}-3xy+\frac{dx}{dt}=t,\qquad \frac{d^2y}{dt^2}+y=3,$$
> introducimos $x_1=x,\ x_2=\dot x,\ x_3=y,\ x_4=\dot y$. Despejando las derivadas mayores ($\ddot x=3xy-\dot x+t$, $\ddot y=3-y$) queda el sistema de **primer orden**
> $$\dot{\mathbf{x}}=\mathbf{f}(t,\mathbf{x}),\qquad
> \mathbf{f}=\begin{pmatrix} x_2\\ 3x_1x_3-x_2+t\\ x_4\\ 3-x_3\end{pmatrix}.$$
> Cuatro ecuaciones de primer orden reemplazan a dos de segundo orden.

> [!definicion] Punto de equilibrio
> Un **punto de equilibrio** (o crítico) del sistema autónomo $\dot{\mathbf{x}}=\mathbf{f}(\mathbf{x})$ es un $\mathbf{x}_c$ con
> $$\mathbf{f}(\mathbf{x}_c)=\mathbf{0}.$$
> Allí todas las derivadas se anulan: si el sistema arranca en $\mathbf{x}_c$, permanece ahí. Son la base del estudio cualitativo de estabilidad.

> [!warning]
> No confundas **orden** con **grado**. En $\big(y''\big)^2+xy=0$ el orden es $2$ (deriva más alta $y''$) y el grado es $2$ (esa derivada al cuadrado). Una EDO **lineal** siempre tiene grado $1$, pero grado $1$ no implica linealidad ($y'+y^2=x$ tiene grado $1$ y **no** es lineal por el $y^2$).

## Resumen

> [!resumen]
> | Concepto | Definición | Detalle |
> |---|---|---|
> | EDO vs. EDP | derivadas respecto a una / varias variables | aquí solo EDO |
> | Forma implícita | $F(x,y,\dots,y^{(n)})=0$ | forma cruda |
> | Forma normal | $y^{(n)}=f(x,y,\dots,y^{(n-1)})$ | se despeja la derivada mayor |
> | Orden / grado | derivada más alta / su potencia | clasifican la EDO |
> | Solución | $y(x)$ cumple la EDO en $I$ | depende del intervalo |
> | Solución implícita | $g(x,y)=0$ con $\partial g/\partial y\neq0$ | define $y(x)$ localmente |
> | PVI | $\dot x=f(t,x),\ x(t_0)=x_0$ | la C.I. fija la constante |
> | Equilibrio | $\mathbf{f}(\mathbf{x}_c)=\mathbf{0}$ | solución constante |

> [!corolario]
> Toda la teoría se reduce a un objeto: el sistema de primer orden $\dot{\mathbf{x}}= \mathbf{f}(t,\mathbf{x})$. Si $\mathbf{f}$ es suave (continua y con derivadas continuas en $\mathbf{x}$), por cada punto pasa **una** trayectoria: existencia + unicidad = **determinismo**. Cuando $\mathbf{f}$ pierde suavidad ($y^{1/2}$ en $y=0$), pueden coexistir varias soluciones.

> [!referencia]
> - Lectura geométrica de $y'=f(x,y)$: [[Campo de Direcciones e Isoclinas]].
> - Qué dibujan las soluciones: [[Curvas Integrales y Soluciones]].
> - Demostración del teorema: [[Existencia y Unicidad Picard]].
> - Primer método de resolución: [[Variables Separables]].
> - Índice del bloque: [[Fundamentos y Teoria Cualitativa/index]].
