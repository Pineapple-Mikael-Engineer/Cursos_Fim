---
title: Concepto y Clasificación de las Ecuaciones Integro-Diferenciales
tags:
  - ecuaciones
  - difero-integrales
  - teoria
  - integro-diferenciales
  - clasificacion
draft: false
aliases:
  - clasificación integro-diferenciales
  - ecuación integro-diferencial
  - Volterra integro-diferencial
  - Fredholm integro-diferencial
  - integro-differential equation classification
---

# Concepto y Clasificación de las Ecuaciones Integro-Diferenciales

> [!definicion]
> Una **ecuación integro-diferencial** es aquella que contiene, sobre la misma incógnita $\varphi(t)$,
> **derivadas** $\varphi',\varphi'',\dots$ **y** una **integral** $\int K\,\varphi$ de la propia
> incógnita. Reúne en una sola igualdad lo que una EDO y una ecuación integral hacen por separado:
> $$\varphi'(t)=f(t)+\lambda\int_{0}^{t}K(t,s)\,\varphi(s)\,ds.$$
> Se clasifica por **tres ejes**: el **tipo de integral** —**Volterra** ($\int_0^t$, límite superior
> variable) frente a **Fredholm** ($\int_a^b$, límites fijos)—; el **orden**, que es el de la derivada
> más alta; y por ser **lineal** o **no lineal** en $\varphi$.

> [!info]
> Nota de entrada de la sección [[Integro-Diferenciales/index| integro-diferenciales]], dentro del
> [[4 Ecuaciones Difero-integrales/index| capítulo difero-integral]]. Aquí solo se **reconoce y
> clasifica** la ecuación; cómo resolverla está en
> [[Resolucion por Transformada de Laplace| resolución por Laplace]] (núcleo de convolución) y en
> [[Reduccion a Sistemas| reducción a sistemas]] (núcleo general). Notación de Krasnov: incógnita
> $\varphi(t)$, núcleo $K$, parámetro $\lambda$.

---

## Ejemplo

> [!ejemplo] Clasificar tres ecuaciones
> Tomemos tres ecuaciones y pasémoslas por los tres ejes (tipo, orden, linealidad).
>
> **(a)** $\displaystyle \varphi'(t)=t+\lambda\int_{0}^{t}(t-s)\,\varphi(s)\,ds$, con $\varphi(0)=1$.
> - Aparece $\varphi'$ (derivada) **y** $\int\varphi$ (integral) → es **integro-diferencial**.
> - El límite superior es **variable** ($t$) → **Volterra**.
> - La derivada más alta es la primera → **orden 1**.
> - $\varphi$ y su integral entran a la primera potencia, sin productos → **lineal**.
> - Como sólo el orden vale $1$, basta **una** condición inicial: $\varphi(0)=1$.
> > **Veredicto:** integro-diferencial de **Volterra, lineal, de primer orden**.
>
> **(b)** $\displaystyle \varphi''(t)+\int_{0}^{\pi}\cos(t-s)\,\varphi(s)\,ds=\operatorname{sen}t$.
> - Hay $\varphi''$ e $\int\varphi$ → **integro-diferencial**.
> - Los límites $0$ y $\pi$ son **fijos** → **Fredholm**.
> - Derivada más alta: la segunda → **orden 2** (pide **dos** condiciones, p. ej. $\varphi(0),\varphi'(0)$).
> - Lineal en $\varphi$.
> > **Veredicto:** integro-diferencial de **Fredholm, lineal, de segundo orden**.
>
> **(c)** $\displaystyle \varphi'(t)=1+\int_{0}^{t}\varphi(s)^{2}\,ds$.
> - Integro-diferencial de Volterra, orden 1, pero $\varphi^{2}$ bajo la integral la hace **no lineal**.
> > **Veredicto:** integro-diferencial de **Volterra, no lineal, de primer orden**.

> [!info] Lo que **no** es una integro-diferencial
> | Ecuación | Por qué |
> |:---|:---|
> | $\varphi''+\varphi=0$ | sólo derivadas → es una **EDO** pura |
> | $\varphi(t)=f(t)+\lambda\int_0^t K\varphi\,ds$ | sólo integral → es una **ecuación integral** pura ([[Integro-Diferenciales/index\|Volterra]]) |
> | $\varphi'(t)=t\,\varphi(t)+f(t)$ | la integral falta → **EDO lineal** |
>
> La marca distintiva es la **coexistencia** de al menos una derivada y al menos una integral **de la
> misma incógnita** en la misma igualdad.

---

## En qué consiste

> [!teoria] La integral es "memoria"; las condiciones iniciales fijan el arranque
> Una EDO de orden $n$ necesita $n$ condiciones iniciales porque integrar $n$ veces produce $n$
> constantes. La integro-diferencial **hereda** esa cuenta: el número de condiciones iniciales que la
> determinan es igual a su **orden** (el de la derivada más alta), **no** se añade ninguna por el
> término integral. La razón es que en una integral de **Volterra** $\int_0^t K(t,s)\varphi(s)\,ds$ el
> límite inferior $0$ ya **ancla** la integral en el origen: para $t=0$ vale cero, así que no introduce
> una constante libre nueva.
>
> Lo que sí introduce la integral es **memoria**. En la EDO $\varphi'=g(t,\varphi)$ la tasa de cambio
> depende sólo del **valor presente** $\varphi(t)$. Con el término $\int_0^t K(t,s)\varphi(s)\,ds$ pasa
> a depender de **toda la historia** $\{\varphi(s):0\le s\le t\}$, ponderada por el núcleo $K$. El
> sistema "recuerda" su pasado; por eso modela materiales viscoelásticos, poblaciones con retardo o
> circuitos con elementos de memoria.

> [!algoritmo] Clasificar una ecuación integro-diferencial
> 1. **¿Es integro-diferencial?** Comprobar que aparecen a la vez **una derivada** de $\varphi$ y **una
>    integral** de $\varphi$. Si falta una, es EDO o ecuación integral pura (delegar).
> 2. **Tipo de integral.** Mirar el límite superior: si es **variable** ($t$, $x$) → **Volterra**; si
>    ambos límites son **constantes** ($a,b$) → **Fredholm**.
> 3. **Orden.** Localizar la derivada de mayor orden $\varphi^{(n)}$; ese $n$ es el orden y el número de
>    condiciones iniciales que se necesitan.
> 4. **Linealidad.** ¿Entran $\varphi$, sus derivadas y su integral sólo a la **primera potencia** y sin
>    multiplicarse entre sí? Sí → **lineal**; aparece $\varphi^2$, $\varphi\varphi'$, $\operatorname{sen}\varphi$… → **no lineal**.
> 5. **Homogeneidad** (opcional). Si el término libre $f\equiv 0$, es **homogénea**.

> [!info] Qué método elegir según el núcleo
> | Núcleo $K$ | Método recomendado |
> |:---|:---|
> | de **convolución** $K(t-s)$ (Volterra) | [[Resolucion por Transformada de Laplace\|transformada de Laplace]] → ecuación algebraica |
> | **general** $K(t,s)$ | [[Reduccion a Sistemas\|reducir a un sistema]] de EDO de primer orden |
> | núcleo **degenerado/separable** | reducir a un sistema algebraico-diferencial finito |
>
> En la práctica: si el argumento del núcleo es la **diferencia** $t-s$, intentar Laplace **siempre**
> primero; convierte derivar e integrar en multiplicar y dividir.

## Resumen

> [!resumen]
> | Eje | Opciones | Cómo se reconoce |
> |:---|:---|:---|
> | Naturaleza | integro-diferencial | hay derivada **y** integral de $\varphi$ |
> | Tipo | Volterra \| Fredholm | límite superior variable \| límites fijos |
> | Orden | $n=1,2,\dots$ | derivada más alta $\varphi^{(n)}$ |
> | Linealidad | lineal \| no lineal | $\varphi$ a la 1ª potencia \| potencias/productos |
> | Datos | $n$ condiciones iniciales | tantas como el orden, no por la integral |

> [!corolario]
> Una ecuación integro-diferencial es una **EDO con memoria**: el orden de su derivada dice cuántas
> condiciones iniciales pide, y el tipo de su integral (Volterra o Fredholm) dice qué herramienta la
> resuelve. Clasificarla bien es ya medio camino, porque cada casillero apunta a un método distinto.

> [!referencia]
> - Si el núcleo es de convolución: [[Resolucion por Transformada de Laplace]].
> - Si el núcleo es general: [[Reduccion a Sistemas]].
> - Marco de la sección: [[Integro-Diferenciales/index]].
