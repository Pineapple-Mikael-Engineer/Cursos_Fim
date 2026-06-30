---
title: Flujo Compresible y Ondas de Choque
order: 1
tags:
  - fluidos
  - teoria
  - covariante
draft: false
aliases:
  - Flujo compresible
  - Ondas de choque
  - Número de Mach
---

# Flujo Compresible y Ondas de Choque $\mathrm{Ma}=\dfrac{U}{c_s},\quad c_s^2=\left(\dfrac{\partial p}{\partial\rho}\right)_s$

> [!definicion] Compresibilidad, sonido y choques
> Un flujo es **compresible** cuando la densidad $\rho$ deja de ser constante y responde a las variaciones de presión. La escala que mide cuánto importa esa compresibilidad es la **velocidad del sonido**
> $$\boxed{\;c_s^2=\left(\frac{\partial p}{\partial\rho}\right)_s\;}$$
> —la rapidez con que se propagan las pequeñas perturbaciones de presión, evaluada a **entropía constante** (proceso adiabático)—. Comparándola con la velocidad característica del flujo $U$ se define el **número de Mach** $\mathrm{Ma}=U/c_s$. Cuando $\mathrm{Ma}<1$ el flujo es **subsónico**; cuando $\mathrm{Ma}>1$ es **supersónico** y aparecen fenómenos sin análogo subsónico: el **cono de Mach** y las **ondas de choque**, discontinuidades abruptas a través de las cuales saltan $\rho$, $p$ y $\vec v$.

---

> [!info] Ubicación y dependencias
> Esta nota pertenece a la sección [[6 Formulacion Covariante del Fluido/index | Formulación Covariante del Fluido]], junto a sus hermanas [[Tensor Energia-Momento del Fluido]] e [[Hidrodinamica Relativista]]. Es el **puente clásico** hacia el régimen relativista: lleva el flujo hasta velocidades comparables a una velocidad de propagación, primero $c_s$ y, en el límite, $c$. Toda la deducción se apoya en la [[Conservacion de Masa]] (continuidad) y en la [[Conservacion de Momento]] (Euler), que aquí linealizamos y, en los choques, integramos a través de la discontinuidad.
>
> **Referencias:** Landau & Lifshitz, *Mecánica de Fluidos* (Vol. 6), §64 (velocidad del sonido) y §§82–85 (ondas de choque y relaciones de Rankine–Hugoniot).

---

La compresibilidad introduce una velocidad propia del medio, $c_s$, ausente en el flujo incompresible. Todo lo demás de esta nota es geometría y balances en torno a esa velocidad: cómo se propaga una perturbación pequeña (sonido), cómo se acumulan los frentes cuando la fuente va más rápido que ellos (cono de Mach), y qué se conserva cuando el salto deja de ser pequeño (choque).

![[ondas_choque.svg|620]]

*Figura 1. (a) Cono de Mach: un objeto supersónico que viaja a velocidad $U$ emite frentes esféricos que se propagan a $c_s$ y se acumulan sobre un cono de semiángulo $\alpha$ con $\sin\alpha=c_s/U=1/\mathrm{Ma}$. (b) Choque normal: en el marco del choque el fluido entra con $(\rho_1,u_1,p_1)$ y sale con $(\rho_2,u_2,p_2)$; los flujos de masa, momento y energía se conservan a través de la discontinuidad (relaciones de Rankine–Hugoniot).*

---

## Deducción de la velocidad del sonido

> [!teorema] Ecuación de ondas para la perturbación de densidad
> Las pequeñas perturbaciones de un fluido en reposo satisfacen la **ecuación de ondas**
> $$\frac{\partial^2\rho'}{\partial t^2}=c_s^2\,\nabla^2\rho',\qquad c_s^2=\left(\frac{\partial p}{\partial\rho}\right)_s,$$
> es decir, se propagan sin deformarse a la velocidad $c_s$. Para un gas ideal con índice adiabático $\gamma$,
> $$c_s=\sqrt{\frac{\gamma p}{\rho}}=\sqrt{\frac{\gamma R T}{M}}.$$

> [!demostracion] Linealización de continuidad y Euler
> Partimos de un fluido en **reposo y uniforme**, con densidad $\rho_0$, presión $p_0$ y velocidad nula, y le superponemos perturbaciones infinitesimales:
> $$\rho=\rho_0+\rho',\qquad p=p_0+p',\qquad \vec v=\vec v\,',$$
> donde $\rho'$, $p'$ y $\vec v\,'$ son de primer orden de pequeñez. El estado base es constante, de modo que $\partial_t\rho_0=0$ y $\nabla p_0=\vec 0$.
>
> **Paso 1 — Linealizar la continuidad.** La [[Conservacion de Masa]] es $\partial_t\rho+\nabla\cdot(\rho\vec v)=0$. Sustituyendo y conservando solo los términos de primer orden (el producto $\rho'\vec v\,'$ es de segundo orden y se descarta),
> $$\frac{\partial\rho'}{\partial t}+\rho_0\,\nabla\cdot\vec v\,'=0.\tag{1}$$
>
> **Paso 2 — Linealizar Euler.** La [[Conservacion de Momento]] sin viscosidad (Euler) es $\rho\big(\partial_t\vec v+(\vec v\cdot\nabla)\vec v\big)=-\nabla p$. El término convectivo $(\vec v\,'\cdot\nabla)\vec v\,'$ es de segundo orden; a primer orden,
> $$\rho_0\,\frac{\partial\vec v\,'}{\partial t}=-\nabla p'.\tag{2}$$
>
> **Paso 3 — Cerrar con la relación adiabática.** Las perturbaciones del sonido son **adiabáticas** (no hay tiempo para que el calor difunda entre compresiones y rarefacciones), así que $p$ es función de $\rho$ a entropía constante. Desarrollando a primer orden alrededor del estado base,
> $$p'=\left(\frac{\partial p}{\partial\rho}\right)_s\rho'\equiv c_s^2\,\rho',\tag{3}$$
> lo que **define** $c_s^2=(\partial p/\partial\rho)_s$. Llevando (3) a (2),
> $$\rho_0\,\frac{\partial\vec v\,'}{\partial t}=-c_s^2\,\nabla\rho'.\tag{2'}$$
>
> **Paso 4 — Combinar para eliminar $\vec v\,'$.** Derivamos (1) respecto al tiempo,
> $$\frac{\partial^2\rho'}{\partial t^2}+\rho_0\,\nabla\cdot\frac{\partial\vec v\,'}{\partial t}=0,$$
> y sustituimos $\rho_0\,\partial_t\vec v\,'$ por (2'):
> $$\frac{\partial^2\rho'}{\partial t^2}+\nabla\cdot\big(-c_s^2\,\nabla\rho'\big)=0
> \;\;\Longrightarrow\;\;
> \frac{\partial^2\rho'}{\partial t^2}=c_s^2\,\nabla^2\rho'.$$
> Es la ecuación de ondas con velocidad de propagación $c_s$.
>
> **Paso 5 — Gas ideal.** Para un gas ideal, el proceso adiabático cumple $p\,\rho^{-\gamma}=\text{cte}$, luego $\left(\partial p/\partial\rho\right)_s=\gamma\,p/\rho$. Usando además $p=\rho R T/M$ (con $R$ constante de los gases y $M$ masa molar),
> $$c_s=\sqrt{\frac{\gamma p}{\rho}}=\sqrt{\frac{\gamma R T}{M}}.\qquad\blacksquare$$

> [!warning] El error de Newton: el sonido es adiabático, no isotermo
> Newton calculó $c_s$ suponiendo que la compresión del sonido era **isoterma**, es decir $p\propto\rho$ con $(\partial p/\partial\rho)_T=p/\rho$, y obtuvo un valor un factor $\sqrt{\gamma}\approx1{,}18$ demasiado bajo para el aire. Laplace corrigió que las oscilaciones son **adiabáticas**: tan rápidas que el calor no difunde, de modo que el índice correcto es $(\partial p/\partial\rho)_s=\gamma\,p/\rho$. Por eso $c_s^2=(\partial p/\partial\rho)_s$ lleva el subíndice $s$ (entropía constante) y el factor $\gamma$. Las **ondas de choque**, en cambio, son **irreversibles**: generan entropía, a diferencia del sonido, que es una perturbación reversible.

---

## Número de Mach y casi-incompresibilidad

> [!proposicion] Para $\mathrm{Ma}\ll1$ el flujo es prácticamente incompresible
> Si la velocidad típica del flujo es $U$ y la del sonido es $c_s$, la perturbación relativa de densidad escala como
> $$\frac{\rho'}{\rho}\sim\mathrm{Ma}^2,\qquad \mathrm{Ma}=\frac{U}{c_s}.$$
> En particular, para $\mathrm{Ma}\lesssim0{,}3$ se tiene $\rho'/\rho\lesssim0{,}09$ y la densidad puede tomarse constante: el flujo es **casi incompresible**.

> [!demostracion] Estimación de órdenes de magnitud
> **Paso 1 — Escala de la presión dinámica.** En un flujo estacionario, el balance de Euler liga las variaciones de presión con las de energía cinética (teorema de Bernoulli): un cambio de velocidad de orden $U$ produce una variación de presión
> $$p'\sim\rho\,U^2.$$
>
> **Paso 2 — Traducir presión a densidad.** Por la relación adiabática (3), $p'=c_s^2\,\rho'$, de modo que
> $$\rho'\sim\frac{p'}{c_s^2}\sim\frac{\rho\,U^2}{c_s^2}.$$
>
> **Paso 3 — Formar el número de Mach.** Dividiendo por $\rho$,
> $$\frac{\rho'}{\rho}\sim\frac{U^2}{c_s^2}=\mathrm{Ma}^2.$$
> Así, cuando $\mathrm{Ma}$ es pequeño, las variaciones de densidad son de orden $\mathrm{Ma}^2$ —doblemente pequeñas— y la hipótesis de incompresibilidad está justificada. $\blacksquare$

> [!proposicion] El cono de Mach
> Un objeto que se mueve a velocidad supersónica $U>c_s$ emite frentes de onda que se acumulan sobre un **cono** cuyo semiángulo $\alpha$ (medido desde la dirección de avance) cumple
> $$\boxed{\;\sin\alpha=\frac{c_s}{U}=\frac{1}{\mathrm{Ma}}\;}$$

> [!demostracion] Geometría de los frentes acumulados
> **Paso 1 — Posiciones en un tiempo $t$.** Sitúese el objeto en el origen en el instante $0$ y sígase un frente de onda emitido entonces. Transcurrido un tiempo $t$, ese frente es una esfera de radio $c_s\,t$ centrada en el punto de emisión, mientras que el objeto ha avanzado una distancia $U\,t$ en línea recta.
>
> **Paso 2 — Envolvente de los frentes.** Como $U>c_s$, el objeto va por delante de todos sus frentes; la **envolvente** de todas las esferas emitidas a lo largo de la trayectoria es un cono con vértice en la posición actual del objeto. El cateto opuesto al semiángulo $\alpha$ es el radio del frente, $c_s\,t$; la hipotenusa es la distancia recorrida por el objeto, $U\,t$.
>
> **Paso 3 — Relación trigonométrica.** Por el triángulo rectángulo formado,
> $$\sin\alpha=\frac{c_s\,t}{U\,t}=\frac{c_s}{U}=\frac{1}{\mathrm{Ma}}.$$
> El cono solo existe si $\mathrm{Ma}>1$ (para $\mathrm{Ma}\le1$ no hay solución real, pues los frentes no quedan atrás). Cuanto mayor el Mach, más cerrado el cono. $\blacksquare$

---

## Ondas de choque: relaciones de Rankine–Hugoniot

> [!teorema] Saltos a través de un choque normal
> En el marco de referencia que se mueve **con el choque**, el flujo es estacionario y unidimensional; los flujos de masa, momento y energía se conservan a través de la discontinuidad. Llamando $[\,\cdot\,]$ al salto (valor aguas abajo menos aguas arriba),
> $$[\rho u]=0,\qquad [\rho u^2+p]=0,\qquad \left[u\left(\tfrac12 u^2+h\right)\right]=0,$$
> con $h=e+p/\rho$ la **entalpía específica** ($e$ energía interna por unidad de masa). Estas son las **relaciones de Rankine–Hugoniot**.

> [!demostracion] Balances integrales a través del choque
> Tómese un volumen de control fino y plano, de área transversal $A$, que **atraviesa** el choque: una cara aguas arriba (estado 1) y otra aguas abajo (estado 2). En el marco del choque el régimen es estacionario, así que los flujos entrantes igualan a los salientes.
>
> **Paso 1 — Masa.** La [[Conservacion de Masa]] en estacionario dice que el flujo másico que entra por la cara 1 sale por la cara 2:
> $$\rho_1 u_1 A=\rho_2 u_2 A\;\;\Longrightarrow\;\;\rho_1 u_1=\rho_2 u_2,$$
> esto es $[\rho u]=0$. Definimos el **flujo másico** $j\equiv\rho_1 u_1=\rho_2 u_2$.
>
> **Paso 2 — Momento.** La [[Conservacion de Momento]] (Euler estacionario 1D) iguala la variación del flujo de momento a la fuerza neta de presión sobre las caras. Por unidad de área,
> $$\rho_1 u_1\cdot u_1+p_1=\rho_2 u_2\cdot u_2+p_2\;\;\Longrightarrow\;\;\rho_1 u_1^2+p_1=\rho_2 u_2^2+p_2,$$
> es decir $[\rho u^2+p]=0$. El término $\rho u^2$ es el flujo de momento convectivo y $p$ la fuerza superficial.
>
> **Paso 3 — Energía.** La conservación de la energía en flujo estacionario sin aporte de calor externo establece que el flujo de energía total (cinética más entálpica) es el mismo a ambos lados. La energía que cruza por unidad de área y tiempo es $\rho u\big(\tfrac12 u^2+e\big)$ más el trabajo de las fuerzas de presión $p\,u$; agrupando $e+p/\rho=h$,
> $$\rho_1 u_1\!\left(\tfrac12 u_1^2+h_1\right)=\rho_2 u_2\!\left(\tfrac12 u_2^2+h_2\right).$$
> Como $\rho_1 u_1=\rho_2 u_2=j\neq0$, se puede dividir por el flujo másico común y queda
> $$\tfrac12 u_1^2+h_1=\tfrac12 u_2^2+h_2\;\;\Longleftrightarrow\;\;\left[u\left(\tfrac12 u^2+h\right)\right]=0.$$
> Las tres condiciones $[\rho u]=0$, $[\rho u^2+p]=0$, $[\,u(\tfrac12 u^2+h)\,]=0$ relacionan completamente los estados 1 y 2. $\blacksquare$

> [!corolario] El choque solo puede comprimir (segunda ley)
> Las relaciones de Rankine–Hugoniot admiten matemáticamente dos soluciones: una de **compresión** (el gas se frena y se densifica) y otra de **rarefacción**. La **segunda ley de la termodinámica** exige que la entropía **aumente** a través del choque, $s_2>s_1$, y esto solo lo cumple la solución de compresión. En consecuencia, un choque siempre desacelera el flujo de supersónico a subsónico:
> $$\mathrm{Ma}_1>1>\mathrm{Ma}_2,$$
> con aumento de $\rho$, $p$ y temperatura aguas abajo. Por eso el choque es **irreversible**: a diferencia del sonido, genera entropía y disipa energía mecánica en calor.

---

## Ejemplo

> [!ejemplo] Velocidad del sonido en aire, Mach de un avión y cono de Mach
> Considérese aire a temperatura ambiente, tratado como gas ideal diatómico con $\gamma=1{,}4$, masa molar $M=0{,}029\ \text{kg/mol}$ y temperatura $T=288\ \text{K}$ ($15\ ^\circ\text{C}$); $R=8{,}314\ \text{J/(mol·K)}$.
> 1. Calcula la velocidad del sonido $c_s$.
> 2. Un avión vuela a $U=510\ \text{m/s}$. Halla su número de Mach y clasifica el régimen.
> 3. Determina el semiángulo del cono de Mach que deja tras de sí.

> [!solucion]
> **Paso 1 — Velocidad del sonido.** Con la fórmula del gas ideal,
> $$c_s=\sqrt{\frac{\gamma R T}{M}}=\sqrt{\frac{1{,}4\cdot 8{,}314\cdot 288}{0{,}029}}\ \text{m/s}.$$
> El numerador vale $1{,}4\cdot 8{,}314\cdot 288\approx 3\,352{,}2$, y dividido por $0{,}029$ da $\approx 1{,}156\times10^{5}\ \text{m}^2/\text{s}^2$. Por tanto
> $$c_s\approx\sqrt{1{,}156\times10^{5}}\approx 340\ \text{m/s},$$
> el conocido valor de $\approx 340$ m/s para el sonido en aire.
>
> **Paso 2 — Número de Mach.** Con $U=510\ \text{m/s}$,
> $$\mathrm{Ma}=\frac{U}{c_s}=\frac{510}{340}=1{,}5.$$
> Como $\mathrm{Ma}=1{,}5>1$, el vuelo es **supersónico**.
>
> **Paso 3 — Cono de Mach.** El semiángulo cumple $\sin\alpha=1/\mathrm{Ma}=1/1{,}5=0{,}667$, de donde
> $$\alpha=\arcsin(0{,}667)\approx 41{,}8^\circ.$$
> El avión arrastra un cono de choque de unos $42^\circ$ de semiángulo; al cruzar el observador la superficie del cono se percibe el **estampido sónico**. $\blacksquare$

---

## En qué consiste

La compresibilidad introduce en el fluido una velocidad propia, la del sonido $c_s=\sqrt{(\partial p/\partial\rho)_s}$, que actúa como **límite de propagación de la información mecánica** dentro del medio. Todo el comportamiento compresible se organiza en torno a la comparación entre $c_s$ y la velocidad del flujo $U$, resumida en el número de Mach $\mathrm{Ma}=U/c_s$.

Cuando $\mathrm{Ma}$ es pequeño, las perturbaciones de densidad son de orden $\mathrm{Ma}^2$ y el fluido se comporta como incompresible: el sonido viaja "infinitamente rápido" comparado con el flujo y la densidad apenas se entera de los cambios de presión. Al acercarse a $\mathrm{Ma}=1$, el flujo ya no puede avisar río arriba de lo que viene: los frentes se acumulan. En régimen supersónico esa acumulación se vuelve geométrica —el **cono de Mach**, con $\sin\alpha=1/\mathrm{Ma}$— y, cuando el salto es suficientemente brusco, una **onda de choque**: una discontinuidad delgada a través de la cual $\rho$, $p$ y $u$ saltan, conservando masa, momento y energía (Rankine–Hugoniot) pero **creando entropía**.

Esa es la razón de que esta nota sea el portal al capítulo covariante: empuja el flujo hasta velocidades comparables a una velocidad de propagación. Sustituyendo $c_s$ por $c$ y exigiendo que masa, momento y energía se conserven de forma manifiestamente invariante, los balances de Rankine–Hugoniot y la propia continuidad se reescriben como $\partial_\mu T^{\mu\nu}=0$ en el [[Tensor Energia-Momento del Fluido]] y la [[Hidrodinamica Relativista]].

---

## Resumen

> [!resumen] Tabla de resultados
> | Concepto | Expresión | Significado |
> |:---|:---|:---|
> | Velocidad del sonido | $c_s^2=\left(\partial p/\partial\rho\right)_s$ | propagación adiabática de perturbaciones |
> | Sonido en gas ideal | $c_s=\sqrt{\gamma p/\rho}=\sqrt{\gamma R T/M}$ | depende solo de $T$ (no de la presión) |
> | Número de Mach | $\mathrm{Ma}=U/c_s$ | subsónico $<1$, sónico $=1$, supersónico $>1$ |
> | Casi-incompresibilidad | $\rho'/\rho\sim\mathrm{Ma}^2$ | válida para $\mathrm{Ma}\lesssim0{,}3$ |
> | Cono de Mach | $\sin\alpha=c_s/U=1/\mathrm{Ma}$ | envolvente de frentes supersónicos |
> | Rankine–Hugoniot | $[\rho u]=0,\ [\rho u^2+p]=0,\ [\,u(\tfrac12 u^2+h)\,]=0$ | saltos de masa, momento y energía |
> | Sentido del choque | $\mathrm{Ma}_1>1>\mathrm{Ma}_2$ | solo compresión; $s_2>s_1$ |

> [!corolario] Lo esencial
> La compresibilidad se reduce a una sola comparación: $U$ frente a $c_s$. Por debajo de $\mathrm{Ma}\approx0{,}3$ el fluido es incompresible; por encima de $\mathrm{Ma}=1$ aparecen el cono de Mach y los choques. El sonido es reversible y adiabático; el choque es irreversible y comprime, frenando el flujo de supersónico a subsónico mientras genera entropía. Empujar $U$ hacia $c$ es justo lo que motiva la formulación covariante del fluido.

> [!referencia]
> Landau & Lifshitz, *Mecánica de Fluidos* (Vol. 6): §64 (velocidad del sonido), §§82–85 (ondas de choque y relaciones de Rankine–Hugoniot). Véase también Anderson, *Modern Compressible Flow*, caps. 3 y 7.
