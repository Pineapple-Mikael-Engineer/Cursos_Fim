---
title: Orden n Coeficientes Constantes
tags:
  - ecuaciones
  - edo
  - teoria
  - lineales
  - ecuacion-caracteristica
draft: false
aliases:
  - polinomio característico de grado n
  - coeficientes constantes orden n
  - multiplicidades
  - nth order constant coefficients
  - characteristic polynomial
---

# EDO de Orden $n$ con Coeficientes Constantes

> [!definicion]
> Para la EDO homogénea con **coeficientes constantes** de orden $n$
> $$a_n y^{(n)}+a_{n-1}y^{(n-1)}+\dots+a_1y'+a_0y=0,$$
> el **polinomio característico**
> $$P(r)=a_n r^{n}+a_{n-1}r^{n-1}+\dots+a_1 r+a_0=0$$
> tiene exactamente $n$ raíces (contadas **con multiplicidad** y posiblemente **complejas**). Cada raíz
> aporta soluciones **igual que en segundo orden** ([[Coeficientes Constantes Homogenea]]): la única
> novedad es bookkeeping —llevar la cuenta de raíces repetidas y de pares complejos de alta
> multiplicidad. La solución general es la combinación de las $n$ soluciones independientes.

> [!info]
> Generalización directa de la [[Coeficientes Constantes Homogenea| ecuación característica]] de
> segundo orden al bloque [[Lineales de Orden Superior/index| lineales de orden superior]]. El
> esquema "raíz → solución" no cambia; solo hay que aplicarlo a un polinomio de grado mayor. La
> aparición del factor $x$ en raíces repetidas se justifica en [[Reduccion de Orden]], y la lectura en
> términos de operadores en [[Operador Diferencial Lineal]].

---

## Ejemplo

> [!ejemplo] (a) Tercer orden con un factor cúbico que mezcla real y complejo
> **Resolver $y'''-y''+y'-y=0$.** Polinomio característico:
> $$r^3-r^2+r-1=0.$$
> Agrupamos para factorizar: $r^2(r-1)+(r-1)=(r-1)(r^2+1)=0$. Las raíces son
> $$r=1,\qquad r=\pm i.$$
> - La raíz real simple $r=1$ aporta $e^{x}$.
> - El par complejo $\alpha\pm i\beta=0\pm i\,1$ aporta $e^{0\cdot x}\cos x=\cos x$ y $\operatorname{sen}x$.
>
> $$\boxed{\,y=c_1e^{x}+c_2\cos x+c_3\operatorname{sen}x\,}$$
> Son tres soluciones independientes para una EDO de orden tres: correcto.

> [!ejemplo] (b) Cuarto orden con dos raíces reales **dobles**
> **Resolver $y''''-2y''+y=0$.** Característica:
> $$r^4-2r^2+1=(r^2-1)^2=\big[(r-1)(r+1)\big]^2=(r-1)^2(r+1)^2=0.$$
> Hay dos raíces, cada una de **multiplicidad $2$**: $r=1$ (doble) y $r=-1$ (doble). Por la regla de
> multiplicidad, cada una aporta $e^{rx}$ **y** $xe^{rx}$:
> - $r=1$ doble → $e^{x},\,xe^{x}$;
> - $r=-1$ doble → $e^{-x},\,xe^{-x}$.
>
> $$\boxed{\,y=(c_1+c_2x)e^{x}+(c_3+c_4x)e^{-x}\,}$$
> Cuatro soluciones independientes para orden cuatro.

> [!ejemplo] (c) Par complejo **repetido**
> **Resolver la EDO cuyo característico es $(r^2+1)^2=0$** (esto es $y''''+2y''+y=0$). Las raíces son
> $r=\pm i$, **cada par de multiplicidad $2$**. La regla: a las soluciones del par complejo simple
> ($\cos x,\operatorname{sen}x$, pues $\alpha=0,\beta=1$) las multiplicamos por $1$ y por $x$:
> $$\boxed{\,y=(c_1+c_2x)\cos x+(c_3+c_4x)\operatorname{sen}x\,}$$
> El factor $x$ extra es el mismo fenómeno que en las raíces reales repetidas: cuando una raíz se
> "duplica", la nueva solución gana una potencia de $x$. Físicamente, este es el caso de **resonancia
> pura**: un oscilador forzado exactamente en su frecuencia natural crece como $x\cos x$.

---

## En qué consiste

> [!teoria] Todo se hereda del segundo orden
> El [[Coeficientes Constantes Homogenea| caso de segundo orden]] ya estableció el mecanismo: $y=e^{rx}$
> convierte $L[y]=0$ en $P(r)e^{rx}=0$, y como $e^{rx}\neq0$, resolver la EDO equivale a **hallar las
> raíces de $P$**. Esa equivalencia no usa para nada que el grado sea $2$: vale para cualquier $n$. El
> [[Operador Diferencial Lineal| operador]] factoriza igual que el polinomio,
> $$L=a_n\,(D-r_1)(D-r_2)\cdots(D-r_n),$$
> y el núcleo de cada factor $(D-r_k)$ es generado por $e^{r_kx}$. Por eso **la tabla de reglas es la
> misma**; lo único nuevo es que un polinomio de grado $n$ puede tener raíces de multiplicidad mayor.

> [!teorema] Reglas raíz → solución (grado $n$)
> Sea $P(r)=0$ el característico de $a_ny^{(n)}+\dots+a_0y=0$. Entonces:
> - **Raíz real simple $r$** → aporta $e^{rx}$.
> - **Par complejo simple $\alpha\pm i\beta$** → aporta $e^{\alpha x}\cos\beta x$ y $e^{\alpha x}\operatorname{sen}\beta x$.
> - **Raíz real de multiplicidad $m$** → aporta $e^{rx},\,xe^{rx},\,x^2e^{rx},\dots,x^{m-1}e^{rx}$.
> - **Par complejo de multiplicidad $m$** → aporta las del par simple multiplicadas por $1,x,\dots,x^{m-1}$:
>   $$x^{j}e^{\alpha x}\cos\beta x,\quad x^{j}e^{\alpha x}\operatorname{sen}\beta x,\qquad j=0,1,\dots,m-1.$$
> Sumando sobre todas las raíces se obtienen **exactamente $n$** soluciones linealmente independientes.

> [!demostracion] Por qué la multiplicidad $m$ produce $e^{rx},xe^{rx},\dots,x^{m-1}e^{rx}$
> **Paso 1 — el operador factoriza.** Si $r$ es raíz de multiplicidad $m$, entonces $P(r)$ contiene el
> factor $(r-r_0)^m$, y en términos del operador $L$ aparece el bloque $(D-r_0)^m$.
>
> **Paso 2 — núcleo de $(D-r_0)^m$.** Buscamos todas las $y$ con $(D-r_0)^m y=0$. Escribimos
> $y=e^{r_0x}u(x)$. Una identidad clave es el **desplazamiento exponencial**:
> $$(D-r_0)\big[e^{r_0x}u\big]=e^{r_0x}\,Du=e^{r_0x}u'.$$
> Aplicándola $m$ veces, $(D-r_0)^m\big[e^{r_0x}u\big]=e^{r_0x}\,u^{(m)}$.
>
> **Paso 3 — resolver para $u$.** La ecuación $(D-r_0)^m y=0$ se vuelve $u^{(m)}=0$, cuya solución
> general es un polinomio de grado $m-1$:
> $$u=c_0+c_1x+c_2x^2+\dots+c_{m-1}x^{m-1}.$$
>
> **Paso 4 — leer las soluciones.** Por tanto $y=e^{r_0x}u=\big(c_0+c_1x+\dots+c_{m-1}x^{m-1}\big)e^{r_0x}$,
> es decir las $m$ funciones independientes
> $$e^{r_0x},\;xe^{r_0x},\;\dots,\;x^{m-1}e^{r_0x}.$$
> Para un par complejo de multiplicidad $m$ se repite el argumento con $(D-(\alpha+i\beta))^m$ y su
> conjugado, y al tomar partes real e imaginaria (como en el caso simple) aparecen las mismas potencias
> $x^{j}$ multiplicando a $e^{\alpha x}\cos\beta x$ y $e^{\alpha x}\operatorname{sen}\beta x$. $\blacksquare$

> [!warning] Para $n\ge5$ no hay fórmula por radicales
> El paso "hallar las raíces de $P$" es trivial en grado $2$ (fórmula cuadrática) y todavía resoluble
> en grados $3$ y $4$. Pero por el **teorema de Abel-Ruffini**, un polinomio general de grado $\ge5$ no
> tiene fórmula de sus raíces por radicales: en la práctica se hallan **numéricamente**. Esto **no
> rompe la teoría**: una vez que tienes las raíces (de donde sea), la ESTRUCTURA raíz → solución y la
> tabla de reglas son idénticas. La dificultad se traslada del cálculo simbólico al numérico.

> [!algoritmo] Resolver la homogénea de orden $n$
> 1. Escribe el **polinomio característico** $P(r)=0$ (sustituye $y^{(k)}\to r^k$).
> 2. **Factoriza / halla las raíces** de $P$, anotando cada una con su **multiplicidad** (numéricamente si $n\ge5$).
> 3. Para cada raíz, escribe sus soluciones según la tabla (real/complejo × simple/múltiple).
> 4. **Combina** las $n$ soluciones con $n$ constantes; fíjalas con las condiciones iniciales.

## Resumen

> [!resumen]
> | Raíz (con multiplicidad $m$) | Aporte a $y_h$ |
> |---|---|
> | real simple $r$ | $e^{rx}$ |
> | par complejo simple $\alpha\pm i\beta$ | $e^{\alpha x}\cos\beta x,\ e^{\alpha x}\operatorname{sen}\beta x$ |
> | real múltiple $r$ (mult. $m$) | $e^{rx},xe^{rx},\dots,x^{m-1}e^{rx}$ |
> | par complejo múltiple (mult. $m$) | $x^{j}e^{\alpha x}\cos\beta x,\ x^{j}e^{\alpha x}\operatorname{sen}\beta x$, $j=0,\dots,m-1$ |
> | total | $n$ soluciones independientes → $y_h=\sum c_iy_i$ |

> [!corolario]
> Subir de orden $2$ a orden $n$ **no introduce ideas nuevas**, solo más raíces y la posibilidad de
> multiplicidades altas. El único cambio cualitativo es algorítmico: a partir de grado $5$ las raíces
> ya no se obtienen por radicales (Abel-Ruffini) y se recurre a métodos numéricos. La forma de la
> solución sigue dictada por el **tipo de raíz**: real → exponencial, compleja → oscilación, múltiple →
> factores de potencia $x^{j}$.

> [!referencia]
> - El caso base (segundo orden) y los tres regímenes: [[Coeficientes Constantes Homogenea]].
> - De dónde sale el factor $x$ de las raíces repetidas: [[Reduccion de Orden]].
> - La factorización $L=\prod(D-r_k)$ y el desplazamiento exponencial: [[Operador Diferencial Lineal]].
> - El bloque completo: [[Lineales de Orden Superior/index]].
