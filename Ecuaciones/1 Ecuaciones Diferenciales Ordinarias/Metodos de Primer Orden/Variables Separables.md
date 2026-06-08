---
title: Variables Separables
tags:
  - ecuaciones
  - edo
  - teoria
  - primer-orden
  - separables
draft: false
aliases:
  - variables separables
  - ecuación separable
  - separable equation
---

# Variables Separables

> [!definicion]
> Una EDO de primer orden es de **variables separables** si puede escribirse con cada variable en
> un lado:
> $$\frac{dy}{dx}=\frac{f(x)}{g(y)}\ \Longleftrightarrow\ g(y)\,dy=f(x)\,dx.$$
> Se resuelve **integrando cada lado por separado**:
> $$\int g(y)\,dy=\int f(x)\,dx+C.$$
> Es el método más básico y el destino al que **reducen** casi todos los demás.

> [!info]
> Primer tipo del [[index | catálogo de primer orden]] (libro, cap. 1.1.2). Las
> [[Ecuaciones Homogeneas | homogéneas]] y los [[Coeficientes Lineales | coeficientes lineales]] se
> resuelven **transformándolas** en separables; la [[Lineal Primer Orden | lineal]] también acaba en
> una integral. Apóyate en el [[../Fundamentos y Teoria Cualitativa/Campo de Direcciones e Isoclinas | campo de direcciones]]
> para visualizar las soluciones.

---

## Ejemplo

> [!ejemplo]
> **Resolver $\dfrac{dy}{dx}=\dfrac{xy}{y^2+1}$.** Es separable; pasamos $y$ a la izquierda:
> $$\left(y+\frac{1}{y}\right)dy=x\,dx.$$
> Integrando ambos lados,
> $$\frac{y^2}{2}+\ln y=\frac{x^2}{2}+C.$$
> La solución queda **implícita**: define $y(x)$ sin poder despejarla en funciones elementales.
> Es perfectamente válida; para un punto inicial se fija $C$ y, por el
> [[../Fundamentos y Teoria Cualitativa/Existencia y Unicidad Picard | teorema de la función implícita]],
> hay una rama $y(x)$ bien definida donde $\partial(\cdot)/\partial y\neq0$.

> [!ejemplo]
> **PVI con solución explícita: $\dfrac{dy}{dx}=x\,y^{1/2}$ analizada con cuidado.** Separando,
> $$y^{-1/2}\,dy=x\,dx\ \Rightarrow\ 2y^{1/2}=\frac{x^2}{2}+c\ \Rightarrow\ y=\left(\frac{x^2}{4}+C\right)^{2}.$$
> Con $y(0)=0$ se obtiene la rama $y=\dfrac{x^4}{16}$ — **pero también** $y\equiv0$ resuelve el PVI.
> Hay **dos** soluciones: este es el ejemplo canónico de **pérdida de unicidad** (ver
> [[../Fundamentos y Teoria Cualitativa/Teorema de Peano | Peano]]), porque $f=xy^{1/2}$ no es
> [[../Fundamentos y Teoria Cualitativa/Existencia y Unicidad Picard | Lipschitz]] en $y=0$.

> [!warning] Las soluciones perdidas al dividir
> Al pasar de $\dfrac{dy}{dx}=\dfrac{f(x)}{g(y)}$ a $g(y)\,dy=f(x)\,dx$ **se divide por** factores en
> $y$. Cada raíz de $g(y)=0$ (o cada $y$ que anule el denominador original) da una **solución
> constante** $y=y_0$ que el método **no recupera** por integración. Hay que añadirla a mano:
> en $y'=y(1-y)$, las constantes $y=0$ y $y=1$ son soluciones de equilibrio.

---

## En qué consiste

> [!teoria]
> La idea es que si $g(y)\,dy=f(x)\,dx$, entonces al integrar aparece **una antiderivada por lado**
> más una sola constante (la diferencia de las dos). Geométricamente, la solución implícita
> $G(y)-F(x)=C$ es una **familia de curvas de nivel**; cada nivel $C$ es una curva integral del
> [[../Fundamentos y Teoria Cualitativa/Campo de Direcciones e Isoclinas | campo de direcciones]].

> [!algoritmo] Resolver una separable
> 1. Escribe $y'=f(x,y)$ y comprueba que $f$ **factoriza** como $f(x)\,h(y)$ (o $f(x)/g(y)$).
> 2. Separa: $\dfrac{dy}{h(y)}=f(x)\,dx$ — anota qué valores de $y$ anulan $h$ (**soluciones perdidas**).
> 3. Integra ambos lados; añade **una** constante $C$.
> 4. Si hay condición inicial, sustituye para fijar $C$.
> 5. Recupera las soluciones constantes descartadas en el paso 2.

> [!teorema] Una separable siempre se reduce a cuadraturas
> Si $f$ y $g$ son continuas con $g(y)\neq0$ en un entorno de $(x_0,y_0)$, el PVI
> $g(y)y'=f(x),\ y(x_0)=y_0$ tiene solución **única** dada implícitamente por
> $$\int_{y_0}^{y} g(s)\,ds=\int_{x_0}^{x} f(t)\,dt.$$

> [!demostracion]
> **Paso 1 — integrar la identidad.** Sobre una solución, $g(y(x))\,y'(x)=f(x)$. Integrando de
> $x_0$ a $x$ y usando el cambio $s=y(t)$ en el lado izquierdo ($ds=y'\,dt$):
> $$\int_{x_0}^{x} g(y(t))\,y'(t)\,dt=\int_{y_0}^{y} g(s)\,ds=\int_{x_0}^{x} f(t)\,dt.$$
>
> **Paso 2 — define $\Phi(x,y)=\int_{y_0}^{y} g - \int_{x_0}^{x} f$.** La relación anterior es
> $\Phi(x,y)=0$. Como $\partial\Phi/\partial y=g(y_0)\neq0$, el **teorema de la función implícita**
> garantiza una única rama $y=y(x)$ con $y(x_0)=y_0$ cerca del punto. $\blacksquare$

## Resumen

> [!resumen]
> | Paso | Acción |
> |---|---|
> | Reconocer | $y'=f(x)\,h(y)$ |
> | Separar | $\dfrac{dy}{h(y)}=f(x)\,dx$ (apuntar $h(y)=0$) |
> | Integrar | $\displaystyle\int\frac{dy}{h(y)}=\int f(x)\,dx+C$ |
> | Cerrar | fijar $C$ con la condición inicial; añadir soluciones constantes |

> [!corolario]
> "Separar variables" es el caso ideal: la EDO ya es **dos integrales disfrazadas**. Por eso la
> estrategia general de primer orden es *llevar la ecuación a esta forma* mediante un cambio de
> variable o un factor integrante. El único cuidado real son las **soluciones constantes** que se
> pierden al dividir.

> [!referencia]
> - Reducción a separable por cambio de variable: [[Ecuaciones Homogeneas]], [[Coeficientes Lineales]].
> - Cuándo el PVI es único: [[../Fundamentos y Teoria Cualitativa/Existencia y Unicidad Picard]].
> - Aplicación geométrica: [[Trayectorias Ortogonales e Isogonales]].
