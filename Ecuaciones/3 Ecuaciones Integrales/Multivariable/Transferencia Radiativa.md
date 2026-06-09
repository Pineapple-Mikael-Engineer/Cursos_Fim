---
title: Transferencia Radiativa
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - multivariable
  - transporte
draft: false
aliases:
  - ecuación de transferencia radiativa
  - ecuación de Schwarzschild-Milne
  - transporte de radiación
  - radiative transfer equation
  - Milne equation
---

# Transferencia Radiativa

> [!definicion]
> La **ecuación de transferencia radiativa** describe cómo la **intensidad** de radiación $I$ atraviesa
> un medio que **absorbe, emite y dispersa** luz. Para una atmósfera **plana** (estratificada en capas)
> el problema se reduce a una ecuación integral de [[Fredholm Segunda Especie| Fredholm]] para la
> **función fuente** $S$, la **ecuación de Schwarzschild–Milne**:
> $$S(\tau)=(1-\omega)\,B(\tau)+\frac{\omega}{2}\int_{0}^{\infty}E_1\!\left(\lvert\tau-\tau'\rvert\right)\,S(\tau')\,d\tau',$$
> donde $\tau$ es la **profundidad óptica** (distancia medida en "cuántas veces se absorbe la luz"),
> $\omega\in[0,1]$ el **albedo de dispersión simple** (fracción dispersada frente a absorbida), $B$ la
> función de Planck (emisión térmica del medio) y $E_1$ la **integral exponencial**. La incógnita $S$
> aparece dentro y fuera de la integral: la radiación dispersada en un punto depende de la que llega de
> todos los demás.

> [!info]
> El ejemplo de transporte de la sección: una Fredholm de **convolución** con núcleo exponencial, nacida
> de promediar la radiación sobre todas las direcciones. Pertenece a
> [[Multivariable/index| Multivariable y Física]], capítulo
> [[3 Ecuaciones Integrales/index| Ecuaciones Integrales]]. Su forma original es **íntegro-diferencial**
> (lleva una derivada $\mu\,dI/d\tau$), lo que la emparenta con las
> [[Calculo Fraccionario/index| difero-integrales]].

---

## Ejemplo

> [!ejemplo] El núcleo nace de promediar sobre las direcciones
> La forma íntegro-diferencial original es $\mu\,\dfrac{dI}{d\tau}=I-S$, donde $\mu=\cos\theta$ es el
> coseno del ángulo respecto a la vertical. Integrarla **formalmente** a lo largo de cada rayo da $I$ en
> términos de $S$; al **promediar $I$ sobre todas las direcciones** $\mu$ para formar la fuente
> $S=(1-\omega)B+\tfrac{\omega}{2}\int_{-1}^{1}I\,d\mu$, las integrales angular y espacial se combinan en
> una sola integral sobre $\tau'$. El promedio direccional de $e^{-\lvert\tau-\tau'\rvert/\mu}/\mu$ sobre
> $\mu\in[0,1]$ es **justamente** $E_1$:
> $$\frac{1}{2}\int_{0}^{1}\frac{e^{-\lvert\tau-\tau'\rvert/\mu}}{\mu}\,d\mu
> \;\xrightarrow{\,s=1/\mu\,}\;\frac{1}{2}\int_{1}^{\infty}\frac{e^{-\lvert\tau-\tau'\rvert s}}{s}\,ds=\frac{1}{2}E_1\!\left(\lvert\tau-\tau'\rvert\right).$$
> Así, el núcleo $E_1$ **no es arbitrario**: codifica que la radiación viaja en línea recta atenuándose
> exponencialmente y que sumamos esa contribución desde todos los ángulos.

---

## En qué consiste

> [!teoria] El núcleo exponencial: convolución y singularidad
> El núcleo
> $$E_1(t)=\int_{1}^{\infty}\frac{e^{-ts}}{s}\,ds=\int_{t}^{\infty}\frac{e^{-r}}{r}\,dr$$
> tiene dos rasgos decisivos:
> - Es de **convolución**: depende solo de $\lvert\tau-\tau'\rvert$, así que el operador conmuta con
>   traslaciones (en el semieje $[0,\infty)$, salvo el borde). Esto permite técnicas de transformada
>   (Wiener–Hopf) para la atmósfera semi-infinita.
> - Es **débilmente singular**: cerca de $t=0$, $E_1(t)\sim-\ln t-\gamma$ (singularidad **logarítmica**,
>   con $\gamma$ la constante de Euler). El logaritmo es integrable, de modo que el operador es
>   **compacto** y vale la teoría de [[Fredholm Multidimensional| Fredholm]]; la singularidad solo
>   exige cuidado al discretizar.

> [!algoritmo] Resolución por aproximaciones sucesivas
> 1. Parte de $S^{(0)}=(1-\omega)B$ (emisión térmica sin dispersión, la **aproximación gris**).
> 2. **Itera** $S^{(m+1)}=(1-\omega)B+\dfrac{\omega}{2}\int_0^\infty E_1(\lvert\tau-\tau'\rvert)\,S^{(m)}(\tau')\,d\tau'$.
> 3. Esto es la **serie de Neumann en $\omega$**: cada iteración añade un orden de dispersión múltiple
>    (un "rebote" más del fotón). Converge porque $\omega<1$ controla la norma del operador; un fotón se
>    absorbe con probabilidad $1-\omega$ en cada interacción, así que las trayectorias muy largas pesan
>    poco. Ver [[Aproximaciones Sucesivas]].
> 4. En la práctica, se **discretiza**: el método de **ordenadas discretas** ($S_N$) reemplaza la
>    integral angular por una cuadratura en $\mu$, volviendo el sistema un conjunto de EDOs acopladas.

> [!proposicion] Lectura física del albedo $\omega$
> - $\omega\to0$ (medio **absorbente puro**): la integral desaparece, $S=B$ y la radiación es pura
>   emisión térmica local. No hay ecuación integral.
> - $\omega\to1$ (**dispersión conservativa**, sin absorción): el término integral domina, los fotones
>   rebotan indefinidamente y la convergencia de Neumann se vuelve lenta. Es el régimen de la **difusión**
>   de la luz, donde aparece el problema de Milne clásico.

> [!info] Dónde aparece la misma ecuación
> La estructura —transporte con absorción, emisión y dispersión— reaparece, con distinto nombre, en
> campos enteros:
> - **Atmósferas estelares**: el problema de **Milne** determina la temperatura de la fotosfera del Sol.
> - **Física de reactores**: el transporte de **neutrones** es la ecuación de **Boltzmann linealizada**,
>   formalmente idéntica (el albedo es la razón dispersión/absorción del material).
> - **Óptica biomédica**: difusión de luz en **tejidos** (tomografía óptica).
> - **Ciencias del clima**: balance radiativo de la atmósfera terrestre.

> [!warning] Panorama, no cierre
> La transferencia radiativa es un **campo de investigación propio**, no un mero ejercicio de ecuaciones
> integrales: métodos de **ordenadas discretas** ($S_N$), **armónicos esféricos** ($P_N$), Monte Carlo,
> Wiener–Hopf, aproximación de difusión. Esta nota da solo el puente conceptual —cómo el transporte se
> condensa en una Fredholm con núcleo $E_1$—, no la teoría completa.

## Resumen

> [!resumen]
> | Símbolo | Significado |
> |---|---|
> | $\tau$ | profundidad óptica (camino en unidades de absorción) |
> | $\omega$ | albedo de dispersión simple ($0$ absorbe, $1$ dispersa) |
> | $B(\tau)$ | función de Planck (emisión térmica) |
> | $E_1(\lvert\tau-\tau'\rvert)$ | núcleo: débilmente singular ($\sim-\ln$) y de convolución |
> | Tipo | Fredholm 2ª especie; originalmente íntegro-diferencial |
> | Solución | Neumann en $\omega$, ordenadas discretas $S_N$ |

> [!corolario]
> Promediar el transporte direccional de radiación sobre todos los ángulos colapsa una ecuación
> íntegro-diferencial en una **Fredholm de convolución** con núcleo $E_1$, débilmente singular. El albedo
> $\omega$ controla la dispersión múltiple y, con ella, la convergencia de la serie de Neumann. La misma
> ecuación gobierna estrellas, reactores nucleares, tejidos y clima: distintos medios, idéntica
> matemática.

> [!referencia]
> - El método iterativo: [[Aproximaciones Sucesivas]].
> - La hermana de dispersión de ondas: [[Ecuacion de Lippmann-Schwinger]].
> - El puente íntegro-diferencial: [[Calculo Fraccionario/index]].
> - El índice de la sección: [[Multivariable/index]].
