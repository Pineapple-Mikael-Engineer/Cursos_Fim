---
title: Dependencia de Condiciones Iniciales y Parámetros
tags:
  - ecuaciones
  - edo
  - teoria
  - fundamentos
  - estabilidad
draft: false
aliases:
  - dependencia continua
  - dependencia de los datos iniciales
  - buen planteamiento
  - problema bien planteado
  - sensibilidad a condiciones iniciales
  - continuous dependence on initial data
  - well-posedness
  - sensitivity to initial conditions
---

# Dependencia de Condiciones Iniciales y Parámetros

> [!definicion]
> Una vez que sabemos que el PVI $y'=f(x,y),\ y(x_0)=y_0$ tiene solución única (por
> [[Existencia y Unicidad Picard| Picard]]), surge la tercera pregunta: ¿cómo cambia la solución si
> **perturbamos los datos**? Si $f$ es **Lipschitz** en $y$ con constante $L$, la solución
> $y(x;y_0,\lambda)$ depende de manera **continua** del dato inicial $y_0$ y de cualquier parámetro
> $\lambda$ que aparezca en la ecuación: cambios pequeños en los datos producen cambios pequeños en la
> solución (en cada intervalo finito). De hecho la dependencia es **cuantitativa**: dos soluciones que
> arrancan en $a$ y $b$ se separan a lo más exponencialmente,
> $$|y(x;a)-y(x;b)|\ \le\ |a-b|\,e^{L|x-x_0|},$$
> cota que es consecuencia directa de la [[Desigualdad de Gronwall| desigualdad de Gronwall]].

> [!info]
> Completa la tríada de [[Fundamentos y Teoria Cualitativa/index| preguntas fundamentales]] —existencia, unicidad y **dependencia
> continua**— que constituye el **buen planteamiento** de un problema (libro, teoría de estabilidad
> respecto a los datos). Se apoya por completo en la [[Desigualdad de Gronwall | desigualdad de Gronwall]] y prolonga el marco de [[Existencia y Unicidad Picard| Picard]]. Junto con la
> [[Prolongacion de Soluciones| prolongación]], describe el comportamiento **global** de las
> soluciones. La sensibilidad exponencial que aquí aparece es la antesala del estudio de la estabilidad
> en [[Sistemas y Dinamica/index| sistemas y dinámica]].

---

## Ejemplo

> [!ejemplo] La separación exponencial es real: $y'=y$
> Tomemos la ecuación más simple posible, $y'=y$, con $f(x,y)=y$, que es Lipschitz con **$L=1$** (su
> derivada $\partial f/\partial y=1$). Dos soluciones con datos iniciales $a$ y $b$ en $x_0=0$ son
> $y(x;a)=a\,e^{x}$ y $y(x;b)=b\,e^{x}$, de modo que su diferencia es **exactamente**
> $$|y(x;a)-y(x;b)|=|a-b|\,e^{x}.$$
> La cota general $|a-b|\,e^{L|x-x_0|}$ se alcanza aquí con **igualdad**: no es pesimista, es lo que
> realmente ocurre. Observemos la lección: aunque la dependencia es **continua** (si $a\to b$ las
> trayectorias coinciden), para $x$ grande el factor $e^{x}$ amplifica brutalmente cualquier diferencia
> inicial. Una incertidumbre de $|a-b|=10^{-6}$ en el dato se convierte en una diferencia de orden $1$
> hacia $x\approx 14$. La continuidad es una garantía *local en el tiempo*, no una promesa de que dos
> trayectorias próximas sigan próximas para siempre.

---

## En qué consiste

> [!teorema] Dependencia continua respecto al dato inicial
> Sea $f$ continua y **Lipschitz en $y$** con constante $L$ en una región que contiene a ambas
> soluciones. Sean $y(\cdot;a)$ y $y(\cdot;b)$ las soluciones del PVI con datos iniciales $a$ y $b$ en
> $x_0$. Entonces, mientras ambas existan,
> $$|y(x;a)-y(x;b)|\ \le\ |a-b|\,e^{L|x-x_0|}.$$
> En particular, $y(x;y_0)$ es una función **continua** (de hecho Lipschitz) del dato $y_0$ sobre cada
> intervalo finito: $a\to b\Rightarrow y(\cdot;a)\to y(\cdot;b)$ uniformemente.

> [!demostracion]
> Trabajamos con la **diferencia** de las dos soluciones, $w(x):=y(x;a)-y(x;b)$, y la acotamos vía
> [[Desigualdad de Gronwall| Gronwall]].
>
> **Paso 1 — forma integral de la diferencia.** Cada solución satisface la ecuación integral de
> Picard, $y(x;a)=a+\int_{x_0}^x f(t,y(t;a))\,dt$ e igual para $b$. Restando:
> $$w(x)=(a-b)+\int_{x_0}^{x}\bigl[f(t,y(t;a))-f(t,y(t;b))\bigr]\,dt.$$
>
> **Paso 2 — acotar con Lipschitz.** Tomando valor absoluto y usando que $f$ es Lipschitz-$L$ en $y$,
> $|f(t,y(t;a))-f(t,y(t;b))|\le L\,|y(t;a)-y(t;b)|=L\,|w(t)|$:
> $$|w(x)|\ \le\ |a-b|+\int_{x_0}^{x} L\,|w(t)|\,dt.$$
> Esta es exactamente la hipótesis de la desigualdad de Gronwall, con constante $|a-b|$ y factor $L$.
>
> **Paso 3 — aplicar Gronwall.** La [[Desigualdad de Gronwall| desigualdad de Gronwall]] convierte
> esa desigualdad integral implícita en la cota explícita
> $$|w(x)|\ \le\ |a-b|\,e^{L|x-x_0|}.$$
> Como el lado derecho $\to 0$ cuando $a\to b$, la dependencia es continua. $\blacksquare$

> [!info] Buen planteamiento (Hadamard)
> Las tres preguntas de los fundamentos se agrupan en un único concepto debido a **Hadamard**: un
> problema está **bien planteado** (*well-posed*) si cumple las tres condiciones a la vez:
> 1. **Existencia** — tiene al menos una solución ([[Teorema de Peano| Peano]]).
> 2. **Unicidad** — tiene a lo más una ([[Existencia y Unicidad Picard| Picard]]).
> 3. **Dependencia continua** — la solución varía con continuidad respecto a los datos (esta nota).
>
> La tercera es la que rara vez se enuncia pero más importa en la práctica: es la que garantiza que las
> **pequeñas incertidumbres de medición** en los datos iniciales no arruinan la predicción. Sin ella, el
> modelo sería inútil aunque tuviera solución única, porque jamás conocemos los datos con precisión
> infinita. Un problema que falla la tercera condición se llama **mal planteado** y exige técnicas de
> regularización.

> [!teoria] La ecuación variacional: dependencia diferenciable
> Cuando $f$ es además derivable, la dependencia no solo es continua sino **diferenciable**, y la
> sensibilidad $z(x):=\dfrac{\partial y}{\partial y_0}(x)$ se calcula resolviendo una EDO **lineal**, la
> *ecuación variacional* o **linealización** a lo largo de la trayectoria:
> $$z'(x)=\partial_y f\bigl(x,y(x)\bigr)\,z(x),\qquad z(x_0)=1.$$
> (Se obtiene derivando formalmente $y'=f(x,y)$ respecto a $y_0$ e intercambiando derivadas.) Su
> solución es $z(x)=\exp\!\Bigl(\int_{x_0}^x \partial_y f(t,y(t))\,dt\Bigr)$, que mide **cuánto se
> amplifica** una perturbación infinitesimal del dato. Para parámetros $\lambda$ el esquema es análogo:
> $\partial y/\partial\lambda$ satisface la misma EDO lineal con un término fuente $\partial_\lambda f$.
> Esta es la herramienta básica del **análisis de sensibilidad** y la puerta de entrada a la teoría de
> estabilidad de [[Sistemas y Dinamica/index| sistemas y dinámica]].

> [!proposicion] Dependencia respecto a parámetros
> Si la ecuación depende de un parámetro, $y'=f(x,y,\lambda)$, y $f$ es Lipschitz en $(y,\lambda)$
> conjuntamente, entonces la solución depende **continuamente** de $\lambda$ con la misma estructura de
> cota: una variación $|\lambda_1-\lambda_2|$ se propaga, también vía [[Desigualdad de Gronwall | Gronwall]], como $|y(x;\lambda_1)-y(x;\lambda_2)|\le C\,|\lambda_1-\lambda_2|\,e^{L|x-x_0|}$. Datos
> iniciales y parámetros se tratan, pues, con la **misma maquinaria**.

> [!warning]
> **Dependencia continua $\ne$ insensibilidad.** Que la solución dependa con continuidad de los datos
> no significa que sea *poco sensible* a ellos. La cota es $|a-b|\,e^{L|x-x_0|}$, y el factor
> exponencial puede ser **astronómico** en horizontes largos: dos trayectorias casi idénticas al inicio
> pueden volverse irreconocibles. Esa **sensibilidad a las condiciones iniciales** —compatible con un
> sistema perfectamente determinista y bien planteado— es precisamente el germen del **caos**. La
> continuidad protege en intervalos *finitos y cortos*; no promete predictibilidad a largo plazo.

## Interpretación física

> [!teoria] Por qué se puede (y no se puede) predecir
> Un modelo físico determinista y bien planteado garantiza que, *en principio*, el presente determina
> el futuro y que medidas casi iguales dan futuros casi iguales —en un horizonte corto—. Pero el factor
> $e^{L|x-x_0|}$ explica la **frontera de la predicción**: en sistemas con $L>0$ (la inmensa mayoría),
> el error de los datos se amplifica exponencialmente y existe un horizonte temporal más allá del cual
> la predicción detallada es imposible aunque el sistema sea determinista. Es la situación del clima:
> las ecuaciones están bien planteadas, pero la sensibilidad exponencial limita el pronóstico a unos
> pocos días. Determinismo y predictibilidad **no** son lo mismo; lo que los separa es justamente esta
> cota.

## Resumen

> [!resumen]
> | Concepto | Enunciado | Origen |
> |---|---|---|
> | Cota de separación | $\|y(x;a)-y(x;b)\|\le\|a-b\|\,e^{L\|x-x_0\|}$ | [[Desigualdad de Gronwall\|Gronwall]] + Lipschitz |
> | Dependencia continua | $a\to b\Rightarrow y(\cdot;a)\to y(\cdot;b)$ | la cota $\to 0$ |
> | Buen planteamiento | existencia + unicidad + dependencia continua | Hadamard |
> | Ecuación variacional | $z'=\partial_y f(x,y)\,z,\ z(x_0)=1$ | linealización; mide sensibilidad |
> | Parámetros | misma cota con $\|\lambda_1-\lambda_2\|$ | Lipschitz conjunta |
> | Caso $y'=y$ | $\|y(x;a)-y(x;b)\|=\|a-b\|e^{x}$ exacto | igualdad en la cota |

> [!corolario]
> La dependencia continua es la **tercera pata** —y la más práctica— del buen planteamiento: sin ella
> ningún modelo sería utilizable, porque nunca conocemos los datos con exactitud. Pero "continua" no es
> "robusta": el factor exponencial deja abierta la puerta a la **sensibilidad extrema** y al caos. Un
> mismo sistema puede ser, a la vez, perfectamente determinista, bien planteado e impredecible a largo
> plazo.

> [!referencia]
> - La herramienta que da la cota: [[Desigualdad de Gronwall]].
> - El teorema de existencia y unicidad de partida: [[Existencia y Unicidad Picard]].
> - El otro comportamiento global de las soluciones: [[Prolongacion de Soluciones]].
> - Hacia la estabilidad y el caos: [[Sistemas y Dinamica/index]].
> - Marco general: [[Fundamentos y Teoria Cualitativa/index]].
