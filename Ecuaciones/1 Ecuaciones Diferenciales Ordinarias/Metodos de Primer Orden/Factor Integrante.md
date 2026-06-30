---
title: Factor Integrante
order: 5
tags:
  - ecuaciones
  - edo
  - teoria
  - primer-orden
  - factor-integrante
draft: false
aliases:
  - factor integrante
  - factor de integración
  - integrating factor
---

# Factor Integrante

> [!definicion]
> Si la ecuación $M\,dx+N\,dy=0$ **no** es [[Ecuaciones Exactas| exacta]] ($\partial_yM\neq\partial_xN$), se busca una función $\mu(x,y)\neq0$ —el **factor integrante**— tal que al multiplicar
> $$\mu M\,dx+\mu N\,dy=0$$
> **sí** sea exacta. La condición que debe cumplir $\mu$ es la de exactitud de la nueva ecuación:
> $$\frac{\partial}{\partial y}\big(\mu M\big)=\frac{\partial}{\partial x}\big(\mu N\big).$$
> Hallado $\mu$, se resuelve como una [[Ecuaciones Exactas| exacta]] cualquiera.

> [!info]
> Compañera de [[Ecuaciones Exactas]] en el [[Metodos de Primer Orden/index| catálogo de primer orden]] (libro, cap. 1.3.3 y siguientes). Es el mecanismo que está **detrás de la [[Lineal Primer Orden| lineal]]**: su célebre $e^{\int p\,dx}$ es exactamente un factor integrante. El caso general es duro, pero hay **dos casos resolubles** ($\mu$ solo de $x$, o solo de $y$) que cubren la mayoría de los ejercicios. Regreso al [[Metodos de Primer Orden/index| índice de métodos]].

---

## Ejemplo

> [!ejemplo] Factor $\mu(x)$: el caso "solo $x$"
> **Resolver $(e^x-\sin y)\,dx+\cos y\,dy=0$** (libro, Ej. 10). Aquí
> $$M=e^x-\sin y,\qquad N=\cos y.$$
>
> **Paso 1 — comprobar que no es exacta.**
> $$\frac{\partial M}{\partial y}=-\cos y,\qquad \frac{\partial N}{\partial x}=0
> \ \Longrightarrow\ \partial_yM\neq\partial_xN.$$
>
> **Paso 2 — probar el cociente que da $\mu(x)$.**
> $$\frac{\partial_yM-\partial_xN}{N}=\frac{-\cos y-0}{\cos y}=-1.$$
> Sale **constante** (en particular, depende solo de $x$): existe $\mu=\mu(x)$.
>
> **Paso 3 — calcular el factor.**
> $$\mu(x)=e^{\int F(x)\,dx}=e^{\int(-1)\,dx}=e^{-x}.$$
>
> **Paso 4 — multiplicar y resolver como exacta.** La ecuación pasa a
> $$(1-e^{-x}\sin y)\,dx+e^{-x}\cos y\,dy=0,$$
> que ya es exacta. Integrando $M^\ast=1-e^{-x}\sin y$ en $x$:
> $$f=\int(1-e^{-x}\sin y)\,dx=x+e^{-x}\sin y+g(y),$$
> y $\partial_yf=e^{-x}\cos y=N^\ast$ da $g'(y)=0$. La solución es
> $$\boxed{\,x+e^{-x}\sin y=C\,}.$$

> [!ejemplo] Factor de la forma $\mu(xy)$
> **Resolver $(y^3+xy^2+y)\,dx+(x^3+x^2y+x)\,dy=0$** (libro, Ej. 11). No es exacta y los dos cocientes estándar **no** salen solo en $x$ ni solo en $y$; el truco es ensayar un factor que dependa del producto $xy$. Aquí funciona
> $$\mu=(xy)^{-3}.$$
> Multiplicando por $\mu$ la ecuación se vuelve exacta, y reconstruyendo su potencial $f$ se llega a la solución implícita
> $$\boxed{\,-\frac{1}{2}\,x^{-2}-x^{-1}y^{-1}-\frac{1}{2}\,x^{-2}y^{-2}-\frac{1}{2}\,y^{-2}=C\,}.$$
> Moraleja: cuando los dos casos simples fallan, conviene **adivinar la dependencia** de $\mu$ ($xy$, $x+y$, $x^2+y^2$, …) inspeccionando la estructura de $M$ y $N$.

---

## En qué consiste

> [!teoria]
> Un factor integrante es un **reescalado punto a punto** del campo $(M,N)$ que lo vuelve conservativo. Multiplicar por $\mu$ no cambia las curvas solución (la ecuación $\mu M\,dx+\mu N\,dy=0$ tiene las **mismas** soluciones que $M\,dx+N\,dy=0$, pues $\mu\neq0$), pero sí transforma el diferencial inexacto en uno **exacto**, y entonces podemos integrar.
>
> El problema es que la condición $\partial_y(\mu M)=\partial_x(\mu N)$ es, en general, una **EDP** para $\mu$ —tan difícil como la EDO original—. La gracia está en **restringir la forma** de $\mu$ (que dependa solo de $x$, o solo de $y$, o de $xy$…): cada restricción convierte la EDP en una EDO sencilla, resoluble cuando un cierto cociente "se simplifica" a la variable adecuada.

> [!teorema] Cuándo existe un factor $\mu(x)$ y cuándo $\mu(y)$
> Sea $M\,dx+N\,dy=0$ no exacta.
> - Si $\dfrac{\partial_yM-\partial_xN}{N}=F(x)$ depende **solo de $x$**, entonces
>   $$\mu(x)=e^{\int F(x)\,dx}.$$
> - Si $\dfrac{\partial_xN-\partial_yM}{M}=G(y)$ depende **solo de $y$**, entonces
>   $$\mu(y)=e^{\int G(y)\,dy}.$$

> [!demostracion] Fórmula del caso $\mu=\mu(x)$
> **Paso 1 — imponer exactitud con $\mu=\mu(x)$.** La condición es $\partial_y(\mu M)=\partial_x(\mu N)$. Como $\mu$ no depende de $y$, el lado izquierdo es $\mu\,\partial_yM$; en el derecho aparece la derivada de $\mu$ por la regla del producto:
> $$\mu\,\frac{\partial M}{\partial y}=\mu'(x)\,N+\mu\,\frac{\partial N}{\partial x}.$$
>
> **Paso 2 — separar variables en $\mu$.** Agrupando,
> $$\mu'\,N=\mu\,(\partial_yM-\partial_xN)
> \ \Longrightarrow\ \frac{\mu'}{\mu}=\frac{\partial_yM-\partial_xN}{N}.$$
>
> **Paso 3 — consistencia y solución.** El lado izquierdo $\mu'/\mu$ depende **solo de $x$**; por tanto la fórmula es coherente **si y solo si** el lado derecho también depende solo de $x$, llamémoslo $F(x)$. Integrando $\dfrac{\mu'}{\mu}=F(x)$ se obtiene $\ln\mu=\int F\,dx$, esto es
> $$\mu(x)=e^{\int F(x)\,dx}.\qquad\blacksquare$$
> El caso $\mu(y)$ es idéntico intercambiando los papeles de $x$ e $y$ (y el signo, por eso aparece $\partial_xN-\partial_yM$ y se divide por $M$).

> [!algoritmo] Hallar el factor integrante
> 1. ¿La ecuación es [[Ecuaciones Exactas| exacta]]? Si **sí**, no hace falta $\mu$. Si **no**, sigue.
> 2. Calcula $\dfrac{\partial_yM-\partial_xN}{N}$. Si depende **solo de $x$** $\to$ $\mu(x)=e^{\int(\cdots)\,dx}$.
> 3. Si no, calcula $\dfrac{\partial_xN-\partial_yM}{M}$. Si depende **solo de $y$** $\to$ $\mu(y)=e^{\int(\cdots)\,dy}$.
> 4. Si ninguno funciona, ensaya formas $\mu(xy)$, $\mu(x+y)$, $\mu(x^2+y^2)$… según la estructura.
> 5. Multiplica la ecuación por $\mu$ y resuélvela como [[Ecuaciones Exactas| exacta]].

> [!proposicion] La lineal es un caso particular
> La [[Lineal Primer Orden| EDO lineal]] $y'+p(x)\,y=q(x)$ se escribe $\big(p(x)\,y-q(x)\big)dx+dy=0$, con $M=py-q$, $N=1$. Entonces
> $$\frac{\partial_yM-\partial_xN}{N}=\frac{p-0}{1}=p(x),$$
> que depende solo de $x$, así que $\mu(x)=e^{\int p\,dx}$. **Ese** es el famoso factor integrante de la lineal: no es una receta aparte, sino este teorema aplicado.

> [!info] Conexión con la termodinámica
> El ejemplo físico por excelencia: el calor $\delta Q$ es un diferencial **inexacto** (depende del proceso), pero al multiplicarlo por $1/T$ se vuelve exacto y aparece una **función de estado**, la entropía:
> $$dS=\frac{\delta Q}{T}.$$
> Es decir, **$1/T$ es el factor integrante del calor**. La existencia de ese factor (garantizada por el segundo principio) es lo que permite definir la entropía como variable de estado.

> [!warning] No siempre hay forma simple
> Los casos $\mu(x)$ y $\mu(y)$ son afortunados: en general el factor integrante **existe** pero hallarlo es **tan difícil como resolver la EDO original** (su ecuación es una EDP). Si los cocientes estándar no se simplifican, hay que adivinar la dependencia de $\mu$ o recurrir a otro método de clasificación.

## Resumen

> [!resumen]
> | Caso | Condición | Factor |
> |---|---|---|
> | $\mu(x)$ | $\dfrac{\partial_yM-\partial_xN}{N}=F(x)$ solo de $x$ | $\mu=e^{\int F\,dx}$ |
> | $\mu(y)$ | $\dfrac{\partial_xN-\partial_yM}{M}=G(y)$ solo de $y$ | $\mu=e^{\int G\,dy}$ |
> | $\mu(xy)$, etc. | ensayo según estructura de $M,N$ | resolver la EDO de $\mu$ |
> | Lineal | $M=py-q,\ N=1$ | $\mu=e^{\int p\,dx}$ |

> [!corolario]
> El factor integrante es la **llave que convierte lo inexacto en exacto**. Como toda la teoría de primer orden tiende a *reducir a una integral*, $\mu$ es la herramienta universal: fabrica el diferencial total que faltaba. Su versión más usada y siempre disponible es el $e^{\int p}$ de la lineal.

> [!referencia]
> - Método al que se reduce tras multiplicar por $\mu$: [[Ecuaciones Exactas]].
> - Aplicación garantizada del factor: [[Lineal Primer Orden]] ($e^{\int p}$).
> - Lugar en el catálogo: [[Metodos de Primer Orden/index]].
