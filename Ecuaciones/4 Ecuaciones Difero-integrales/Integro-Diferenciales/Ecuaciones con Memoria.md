---
title: Ecuaciones con Memoria
tags:
  - ecuaciones
  - difero-integrales
  - teoria
  - integro-diferenciales
  - memoria
draft: false
aliases:
  - ecuaciones con memoria
  - memory equations
  - nucleo de memoria
  - memory kernel
  - ecuaciones hereditarias
---

# Ecuaciones con Memoria

> [!definicion]
> Una ecuación tiene **memoria** cuando la tasa de cambio actual de la incógnita no depende solo de
> su valor presente, sino de **toda su historia** a través de un **núcleo de memoria** $K(t-s)$:
> $$\varphi'(t)=f(t)+\int_{0}^{t}K(t-s)\,\varphi(s)\,ds.$$
> El núcleo es el corazón físico de la ecuación: $K(t-s)$ dice **cuánto pesa** sobre el instante
> presente $t$ lo que ocurrió hace un tiempo $t-s$. Toda la integral es una **suma ponderada del
> pasado**, y la forma de $K$ decide si el sistema es de memoria corta o de memoria larga.

> [!info]
> Cuarta nota de la rama integro-diferencial, dentro de [[Integro-Diferenciales/index| Ecuaciones Integro-Diferenciales]],
> en el [[4 Ecuaciones Difero-integrales/index| capítulo difero-integral]]. Aquí se da el
> **significado físico** del término integral que aparece en [[Concepto y Clasificacion| Concepto y Clasificación]]; sus aplicaciones se recorren en [[Aplicaciones Integro-Diferenciales| Aplicaciones]]
> y su generalización vive en el [[Calculo Fraccionario/index| cálculo fraccionario]].

---

## Ejemplo

> [!ejemplo] Viscoelasticidad: el esfuerzo como integral hereditaria
> Estire un trozo de goma y suéltelo: no recupera su forma de golpe ni se queda donde estaba, sino
> que **relaja** poco a poco. El material **recuerda** cómo fue deformado. La descripción de Boltzmann
> de un sólido viscoelástico lineal escribe el esfuerzo $\sigma(t)$ como una **integral hereditaria**
> de la velocidad de deformación $\dot\varepsilon(s)$:
> $$\sigma(t)=\int_{0}^{t}G(t-s)\,\dot\varepsilon(s)\,ds,$$
> donde $G(t-s)$ es el **módulo de relajación**: la tensión que sobrevive a un tiempo $t-s$ de haber
> aplicado un escalón de deformación. El módulo es justo el **núcleo de memoria** de este problema.
>
> - Un **sólido elástico ideal** (ley de Hooke) tiene $G(t)=E$ **constante**: no olvida ni recuerda,
>   responde solo al valor instantáneo $\varepsilon(t)$ — **sin memoria**.
> - Un **material viscoelástico** tiene $G(t)$ **decreciente**: el peso de la deformación antigua se
>   desvanece con el tiempo. La rapidez con que se desvanece distingue los dos regímenes siguientes.
>
> > [!ejemplo] Memoria corta (exponencial) vs memoria larga (ley de potencias)
> > ![[memoria_viscoelasticidad.svg|470]]
> >
> > Módulo de relajación $G(t)$: el decaimiento **exponencial** (Maxwell) olvida el pasado rápido; el
> > de **ley de potencias** $t^{-\alpha}$ tiene una **cola larga** —memoria que persiste—, propia de
> > los modelos fraccionarios.

## En qué consiste

> [!teoria] El núcleo decide el tipo de memoria
> Toda la física del sistema con memoria está codificada en la forma del núcleo $K(t-s)$. Dos
> regímenes opuestos organizan el panorama y conviene tenerlos siempre en mente.
>
> **1. Memoria corta — núcleo exponencial.**
> $$K(t-s)=\frac{1}{\tau}\,e^{-(t-s)/\tau}.$$
> El peso del pasado **cae exponencialmente**: lo ocurrido hace mucho más que un tiempo
> característico $\tau$ resulta ya **irrelevante**. El sistema "vive en el presente reciente".
> El límite $\tau\to 0$ es revelador: la exponencial se concentra en una **delta**,
> $K(t-s)\to\delta(t-s)$, y la integral colapsa a $\varphi(t)$ — la ecuación pierde la memoria y se
> vuelve una **EDO ordinaria, markoviana**, sin historia. La memoria corta es, en este sentido, una
> pequeña corrección con respecto al caso sin memoria.
>
> **2. Memoria larga — núcleo de ley de potencias.**
> $$K(t-s)=\frac{C}{(t-s)^{\alpha}},\qquad 0<\alpha<1.$$
> Aquí no hay tiempo característico: el peso decae **lentamente**, como una potencia, y la **cola
> nunca se desprende**. El pasado remoto sigue contando indefinidamente; no existe un $\tau$ tras el
> cual "ya se olvidó". Esta memoria de **ley de potencias** es exactamente la que define a las
> derivadas fraccionarias y conduce al [[Calculo Fraccionario/index| cálculo fraccionario]].

> [!proposicion] Por qué la exponencial "no tiene memoria" y la potencia sí
> La diferencia profunda es la **escala**. La exponencial $e^{-(t-s)/\tau}$ posee una escala temporal
> propia $\tau$ y es **sin memoria en sentido estricto** ($e^{-(a+b)}=e^{-a}e^{-b}$, la propiedad de
> ausencia de memoria de la distribución exponencial). La ley de potencias $(t-s)^{-\alpha}$ es
> **autosemejante**: no tiene escala, se ve igual en todos los tiempos, y por eso reparte peso a todas
> las épocas del pasado por igual (salvo el factor potencial). Memoria sin escala = memoria larga.

> [!info] La ecuación de renovación
> Una hermana muy cercana de las ecuaciones con memoria es la **ecuación de renovación**, puramente
> integral (sin la derivada):
> $$\varphi(t)=f(t)+\int_{0}^{t}K(t-s)\,\varphi(s)\,ds.$$
> El valor presente $\varphi(t)$ se compone de un término de fuente $f(t)$ más una **realimentación**
> del pasado a través de $K$. Aparece en **demografía** (la tasa de nacimientos hoy depende de los
> nacimientos de generaciones anteriores ponderados por la fertilidad por edad), en **teoría de
> riesgo** (procesos de ruina con reclamaciones acumuladas) y en los **procesos de renovación** de la
> probabilidad. Si $K$ es de convolución, esta ecuación se resuelve de un golpe con la
> [[Transformada de Laplace/index| transformada de Laplace]].

> [!warning] La condición inicial no basta
> En una EDO ordinaria, conocer $\varphi(0)$ fija el futuro. En una ecuación con memoria **no es así**:
> el término integral $\int_0^t K(t-s)\varphi(s)\,ds$ arrastra **toda la trayectoria** $\varphi(s)$
> para $0\le s\le t$. Por eso la solución no se "olvida" de su pasado y, en problemas con núcleo
> singular ($\alpha\to 1$), hay que prescribir información sobre la historia previa, no solo un dato en
> $t=0$.

## Resumen

> [!resumen]
> | Aspecto | Memoria corta | Memoria larga |
> |---|---|---|
> | Núcleo $K(t-s)$ | $\dfrac{1}{\tau}e^{-(t-s)/\tau}$ | $\dfrac{C}{(t-s)^{\alpha}}$ |
> | Escala temporal | $\tau$ finito | **ninguna** (autosemejante) |
> | Peso del pasado remoto | despreciable | **persiste** (cola larga) |
> | Límite notable | $\tau\to 0$: **sin memoria** (markoviano) | $\to$ derivada **fraccionaria** |
> | Modelo viscoelástico | Maxwell (relajación exp.) | módulo $G(t)\sim t^{-\alpha}$ |

> [!corolario]
> La memoria corta es una corrección del caso sin memoria; en el límite recupera una EDO ordinaria. La
> memoria de **ley de potencias**, en cambio, es el **puente natural hacia las derivadas
> fraccionarias**: una memoria sin escala que nunca se olvida y que solo el cálculo fraccionario sabe
> escribir compactamente.

> [!referencia]
> - Dónde se usa todo esto: [[Aplicaciones Integro-Diferenciales]].
> - La generalización de la memoria larga: [[Calculo Fraccionario/index]].
> - Vuelta al índice de la rama: [[Integro-Diferenciales/index]].
