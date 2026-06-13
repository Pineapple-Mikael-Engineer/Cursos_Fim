---
title: Número de Reynolds y Adimensionalización
tags:
  - fluidos
  - teoria
  - flujo-viscoso
draft: false
aliases:
  - Número de Reynolds
  - Adimensionalización
  - Semejanza dinámica
---

# Número de Reynolds y Adimensionalización $\mathrm{Re}=\dfrac{\rho U L}{\mu}=\dfrac{UL}{\nu}$

---

> [!definicion] Número de Reynolds
> El **número de Reynolds** es el parámetro adimensional que mide el peso relativo de los efectos inerciales frente a los efectos viscosos en un flujo. Dadas una velocidad característica $U$, una longitud característica $L$, la densidad $\rho$, la viscosidad dinámica $\mu$ y la viscosidad cinemática $\nu=\mu/\rho$, se define
> $$\boxed{\;\mathrm{Re}=\frac{\rho U L}{\mu}=\frac{U L}{\nu}\;}$$
> Al **adimensionalizar** las [[Ecuaciones de Navier-Stokes]] con estas escalas, $\mathrm{Re}$ emerge como el **único** parámetro que gobierna la dinámica de un flujo incompresible de geometría dada. Dos flujos con el mismo $\mathrm{Re}$ y la misma geometría son, una vez reescalados, **idénticos** (semejanza dinámica).

---

> [!info] Ubicación y contexto
> Esta nota pertenece a la sección [[5 Flujo Viscoso/index | Flujo Viscoso]]. Sus notas hermanas son [[Soluciones Viscosas Exactas]], [[Capa Limite]] y [[Flujo de Stokes]]. El desarrollo central parte de las [[Ecuaciones de Navier-Stokes]] y constituye el lenguaje común con el que se clasifican todos los regímenes viscosos.
>
> Referencia principal: **Landau & Lifshitz, _Mecánica de Fluidos_ (Vol. 6), §19** ("Semejanza"). La adimensionalización es la herramienta que justifica por qué basta un parámetro para describir una familia entera de flujos.

---

## En qué consiste

La ecuación de Navier–Stokes incompresible mezcla densidad, viscosidad, velocidades, presiones y tamaños. A simple vista parece que para resolver un problema concreto hay que fijar cinco o seis cantidades dimensionales. La **adimensionalización** demuestra que eso es ilusorio: si reescalamos cada variable por su valor típico, todas las constantes dimensionales se agrupan en un solo número, $\mathrm{Re}$.

La idea física es comparar **órdenes de magnitud**. En un flujo con velocidad típica $U$ que varía sobre una distancia $L$:

- El término inercial $\rho(\vec v\cdot\vec\nabla)\vec v$ es del orden de $\rho U^2/L$: representa el transporte de cantidad de movimiento por la propia corriente.
- El término viscoso $\mu\,\nabla^2\vec v$ es del orden de $\mu U/L^2$: representa la difusión de cantidad de movimiento por fricción interna.

Su cociente es justamente $\mathrm{Re}$, y dice quién manda. Cuando $\mathrm{Re}\ll1$ la viscosidad domina y el flujo es ordenado, reversible, "pegajoso" (mundo de [[Flujo de Stokes]], de las bacterias). Cuando $\mathrm{Re}\gg1$ la inercia domina, la viscosidad se confina a una delgada [[Capa Limite]] junto a las paredes, y al crecer aún más aparece la turbulencia.

A continuación lo demostramos: primero la deducción rigurosa de la ecuación adimensional, luego la interpretación de $\mathrm{Re}$ como cociente de fuerzas, y por último el principio de semejanza dinámica que sostiene todo el ensayo con modelos a escala.

---

### Adimensionalización de Navier–Stokes

> [!teorema] Forma adimensional de Navier–Stokes
> Para un flujo incompresible con escalas características $L$ (longitud), $U$ (velocidad), $T=L/U$ (tiempo convectivo) y $P=\rho U^2$ (presión dinámica), la ecuación de Navier–Stokes adopta la forma universal
> $$\frac{D\vec v^{\,*}}{Dt^{*}}=-\vec\nabla^{*}p^{*}+\frac{1}{\mathrm{Re}}\,\nabla^{*2}\vec v^{\,*},\qquad \mathrm{Re}=\frac{\rho U L}{\mu},$$
> donde los asteriscos denotan variables adimensionales. **Toda la física dimensional queda concentrada en el único parámetro $\mathrm{Re}$.**

> [!demostracion] Deducción paso a paso
> Partimos de la [[Ecuaciones de Navier-Stokes | ecuación de Navier–Stokes]] incompresible:
> $$\rho\left(\frac{\partial\vec v}{\partial t}+(\vec v\cdot\vec\nabla)\vec v\right)=-\vec\nabla p+\mu\,\nabla^2\vec v. \tag{1}$$
>
> **Paso 1 — Definir las variables adimensionales.** Reescalamos cada cantidad por su valor característico:
> $$\vec x^{\,*}=\frac{\vec x}{L},\quad \vec v^{\,*}=\frac{\vec v}{U},\quad t^{*}=\frac{t\,U}{L},\quad p^{*}=\frac{p}{\rho U^2}.$$
> Todas las variables con asterisco son números puros de orden $1$. Despejando las dimensionales:
> $$\vec x=L\,\vec x^{\,*},\qquad \vec v=U\,\vec v^{\,*},\qquad t=\frac{L}{U}\,t^{*},\qquad p=\rho U^2\,p^{*}.$$
>
> **Paso 2 — Transformar los operadores diferenciales.** Como $\vec x=L\,\vec x^{\,*}$, el gradiente escala con $1/L$:
> $$\vec\nabla=\frac{\partial}{\partial\vec x}=\frac{1}{L}\frac{\partial}{\partial\vec x^{\,*}}=\frac{1}{L}\,\vec\nabla^{*}\quad\Longrightarrow\quad \vec\nabla^{*}=L\,\vec\nabla.$$
> Aplicándolo dos veces, el laplaciano escala con $1/L^2$:
> $$\nabla^2=\frac{1}{L^2}\,\nabla^{*2}.$$
> Para la derivada temporal, con $t=(L/U)\,t^{*}$:
> $$\frac{\partial}{\partial t}=\frac{U}{L}\frac{\partial}{\partial t^{*}}.$$
>
> **Paso 3 — Sustituir cada término de (1).** Lo hacemos término a término.
>
> Derivada local:
> $$\rho\,\frac{\partial\vec v}{\partial t}=\rho\cdot\frac{U}{L}\frac{\partial}{\partial t^{*}}\big(U\,\vec v^{\,*}\big)=\frac{\rho U^2}{L}\,\frac{\partial\vec v^{\,*}}{\partial t^{*}}.$$
>
> Término convectivo:
> $$\rho\,(\vec v\cdot\vec\nabla)\vec v=\rho\,\big(U\vec v^{\,*}\cdot\tfrac{1}{L}\vec\nabla^{*}\big)\big(U\vec v^{\,*}\big)=\frac{\rho U^2}{L}\,(\vec v^{\,*}\cdot\vec\nabla^{*})\vec v^{\,*}.$$
>
> Gradiente de presión:
> $$-\vec\nabla p=-\frac{1}{L}\vec\nabla^{*}\big(\rho U^2 p^{*}\big)=-\frac{\rho U^2}{L}\,\vec\nabla^{*}p^{*}.$$
>
> Término viscoso:
> $$\mu\,\nabla^2\vec v=\mu\cdot\frac{1}{L^2}\nabla^{*2}\big(U\vec v^{\,*}\big)=\frac{\mu U}{L^2}\,\nabla^{*2}\vec v^{\,*}.$$
>
> **Paso 4 — Reescribir la ecuación completa.** Reuniendo los cuatro términos:
> $$\frac{\rho U^2}{L}\frac{\partial\vec v^{\,*}}{\partial t^{*}}+\frac{\rho U^2}{L}(\vec v^{\,*}\cdot\vec\nabla^{*})\vec v^{\,*}=-\frac{\rho U^2}{L}\vec\nabla^{*}p^{*}+\frac{\mu U}{L^2}\nabla^{*2}\vec v^{\,*}.$$
>
> **Paso 5 — Dividir por $\rho U^2/L$.** Este es el factor común de los términos inerciales y de presión; lo usamos como referencia:
> $$\frac{\partial\vec v^{\,*}}{\partial t^{*}}+(\vec v^{\,*}\cdot\vec\nabla^{*})\vec v^{\,*}=-\vec\nabla^{*}p^{*}+\frac{\mu U/L^2}{\rho U^2/L}\,\nabla^{*2}\vec v^{\,*}.$$
>
> **Paso 6 — Simplificar el coeficiente viscoso.** El prefactor del término viscoso es
> $$\frac{\mu U/L^2}{\rho U^2/L}=\frac{\mu U}{L^2}\cdot\frac{L}{\rho U^2}=\frac{\mu}{\rho U L}=\frac{1}{\mathrm{Re}}.$$
> Reconociendo además la derivada material $\dfrac{D}{Dt^{*}}=\dfrac{\partial}{\partial t^{*}}+(\vec v^{\,*}\cdot\vec\nabla^{*})$, concluimos:
> $$\frac{D\vec v^{\,*}}{Dt^{*}}=-\vec\nabla^{*}p^{*}+\frac{1}{\mathrm{Re}}\,\nabla^{*2}\vec v^{\,*}.$$
>
> La ecuación de continuidad incompresible $\vec\nabla\cdot\vec v=0$ se transforma simplemente en $\vec\nabla^{*}\cdot\vec v^{\,*}=0$, sin introducir parámetros nuevos. Por tanto el flujo queda determinado por un **solo** número, $\mathrm{Re}$ (más la geometría y las condiciones de frontera adimensionales). $\blacksquare$

---

### Interpretación: cociente de fuerzas

> [!proposicion] $\mathrm{Re}$ como razón inercia/viscosidad
> El número de Reynolds es el cociente entre la magnitud típica de la fuerza inercial por unidad de volumen y la de la fuerza viscosa por unidad de volumen.

> [!demostracion]
> **Paso 1 — Orden de magnitud de la fuerza inercial.** El término convectivo $\rho(\vec v\cdot\vec\nabla)\vec v$ tiene dimensiones de fuerza por unidad de volumen. Con velocidad típica $U$ y variaciones sobre la distancia $L$:
> $$F_{\text{iner}}\sim\rho\,U\,\frac{U}{L}=\frac{\rho U^2}{L}.$$
>
> **Paso 2 — Orden de magnitud de la fuerza viscosa.** El término $\mu\nabla^2\vec v$ involucra dos derivadas espaciales:
> $$F_{\text{visc}}\sim\mu\,\frac{U}{L^2}.$$
>
> **Paso 3 — Tomar el cociente.**
> $$\frac{F_{\text{iner}}}{F_{\text{visc}}}\sim\frac{\rho U^2/L}{\mu U/L^2}=\frac{\rho U^2}{L}\cdot\frac{L^2}{\mu U}=\frac{\rho U L}{\mu}=\mathrm{Re}.$$
>
> Así, $\mathrm{Re}\gg1$ significa "inercia ≫ viscosidad" y $\mathrm{Re}\ll1$ significa "viscosidad ≫ inercia". El mismo cociente apareció en la demostración anterior como prefactor $1/\mathrm{Re}$ del término viscoso, lo que confirma la coherencia de ambas lecturas. $\blacksquare$

---

### Semejanza dinámica

> [!teorema] Principio de semejanza dinámica
> Dos flujos **geométricamente semejantes** (misma forma, distintas escalas) gobernados por Navier–Stokes incompresible son **dinámicamente semejantes** —es decir, sus campos adimensionales coinciden— si y solo si tienen el **mismo número de Reynolds**.

> [!demostracion]
> **Paso 1 — La ecuación no distingue los dos flujos.** Por el teorema de adimensionalización, ambos flujos obedecen literalmente la misma ecuación:
> $$\frac{D\vec v^{\,*}}{Dt^{*}}=-\vec\nabla^{*}p^{*}+\frac{1}{\mathrm{Re}}\,\nabla^{*2}\vec v^{\,*},\qquad \vec\nabla^{*}\cdot\vec v^{\,*}=0.$$
> El único coeficiente que figura es $\mathrm{Re}$. Si $\mathrm{Re}_1=\mathrm{Re}_2$, las dos ecuaciones son **idénticas**.
>
> **Paso 2 — Las condiciones de frontera también coinciden.** La semejanza geométrica garantiza que el dominio adimensional (la forma del obstáculo o conducto medido en unidades de $L$) es el mismo, y la condición de no deslizamiento $\vec v^{\,*}=0$ en las paredes más la corriente lejana $\vec v^{\,*}\to\hat e$ son las mismas en variables adimensionales.
>
> **Paso 3 — Unicidad.** Misma ecuación + mismo dominio + mismas condiciones de frontera $\Rightarrow$ la solución adimensional $\vec v^{\,*}(\vec x^{\,*},t^{*})$, $p^{*}(\vec x^{\,*},t^{*})$ es **una y la misma** para ambos flujos. Al deshacer el reescalado se recuperan los campos dimensionales de cada uno. Los flujos son, salvo factores de escala, el mismo flujo. $\blacksquare$

**Consecuencia práctica — modelos a escala.** Cualquier magnitud adimensional medible es entonces una función *solo* de $\mathrm{Re}$ (y de la geometría). En particular el **coeficiente de arrastre**:
$$C_D=\frac{F_D}{\tfrac12\,\rho U^2 A}=f(\mathrm{Re}),$$
donde $F_D$ es la fuerza de arrastre y $A$ un área de referencia. Esto justifica los **túneles de viento**: para predecir el arrastre de un avión real basta ensayar una maqueta a escala igualando el $\mathrm{Re}$; entonces $C_D$ medido en el modelo es el del prototipo.

---

### Regímenes según $\mathrm{Re}$

La forma adimensional permite leer el comportamiento directamente del valor de $\mathrm{Re}$:

- **$\mathrm{Re}\ll1$ (flujo reptante / Stokes).** El prefactor $1/\mathrm{Re}$ del término viscoso es enorme: la viscosidad domina y la inercia es despreciable. La ecuación se linealiza a $\vec\nabla^{*}p^{*}=\tfrac{1}{\mathrm{Re}}\nabla^{*2}\vec v^{\,*}$, base del [[Flujo de Stokes]]. Flujo reversible, sin estela, simétrico.
- **$\mathrm{Re}\gg1$ (flujo inercial).** El término viscoso $\tfrac{1}{\mathrm{Re}}\nabla^{*2}\vec v^{\,*}$ casi se anula, salvo en una delgada región cerca de las paredes donde los gradientes son grandes: la [[Capa Limite]]. Fuera de ella el flujo es prácticamente ideal.
- **Transición a turbulencia.** Al superar un $\mathrm{Re}$ crítico el flujo laminar se desestabiliza y se vuelve caótico. En una tubería el valor crítico ronda $\mathrm{Re}_{\text{cr}}\approx 2300$ (basado en el diámetro); por encima aparece la turbulencia plenamente desarrollada.

---

### Otros números adimensionales

El mismo procedimiento de adimensionalización, aplicado a ecuaciones más generales (compresibles, con gravedad, no estacionarias forzadas), hace aparecer otros grupos adimensionales. Cada uno mide el peso de un efecto físico frente a la inercia:

| Número | Definición | Compara | Relevante cuando |
| :--- | :---: | :--- | :--- |
| Reynolds | $\mathrm{Re}=\dfrac{\rho U L}{\mu}$ | inercia / viscosidad | siempre en flujo viscoso |
| Mach | $\mathrm{Ma}=\dfrac{U}{c_s}$ | velocidad / vel. del sonido | compresibilidad ($\mathrm{Ma}\gtrsim 0{,}3$) |
| Froude | $\mathrm{Fr}=\dfrac{U}{\sqrt{gL}}$ | inercia / gravedad | olas, superficie libre |
| Euler | $\mathrm{Eu}=\dfrac{\Delta p}{\rho U^2}$ | presión / inercia | cavitación, pérdidas |
| Strouhal | $\mathrm{St}=\dfrac{fL}{U}$ | tiempo convectivo / periodo | desprendimiento de vórtices |

Aquí $c_s$ es la velocidad del sonido, $g$ la gravedad y $f$ una frecuencia característica. Cuando dos fenómenos coexisten (p. ej. olas alrededor de un casco de barco) hay que igualar **varios** números simultáneamente para tener semejanza completa.

---

## Ejemplo

> [!ejemplo] Tres flujos y un ensayo a escala
> **(a)** Agua fluyendo por una tubería de diámetro $D=5\ \text{cm}$ a $U=1\ \text{m/s}$. Datos del agua: $\rho=1000\ \text{kg/m}^3$, $\mu=1{,}0\times10^{-3}\ \text{Pa·s}$ (equivalente a $\nu=1{,}0\times10^{-6}\ \text{m}^2/\text{s}$). Clasifica el régimen.
>
> **(b)** Una bacteria de tamaño $L=2\ \mu\text{m}$ nadando en agua a $U=30\ \mu\text{m/s}$. Clasifica el régimen.
>
> **(c)** Túnel de viento: se ensaya una maqueta de ala a escala $1:10$ de una cuerda real $c=2\ \text{m}$. ¿A qué velocidad de aire $U_m$ hay que soplar para igualar el $\mathrm{Re}$ del vuelo real a $U_r=60\ \text{m/s}$? (Misma densidad y viscosidad del aire en ambos casos.)

> [!solucion]
> **(a) Agua en tubería.** Usamos $L=D$ como escala (convención para conductos):
> $$\mathrm{Re}=\frac{U D}{\nu}=\frac{(1)(0{,}05)}{1{,}0\times10^{-6}}=5{,}0\times10^{4}.$$
> Como $\mathrm{Re}\approx 50\,000\gg 2300$, el flujo es **turbulento**, plenamente inercial.
>
> **(b) Bacteria.** Convertimos a unidades SI: $L=2\times10^{-6}\ \text{m}$, $U=3{,}0\times10^{-5}\ \text{m/s}$.
> $$\mathrm{Re}=\frac{U L}{\nu}=\frac{(3{,}0\times10^{-5})(2\times10^{-6})}{1{,}0\times10^{-6}}=6{,}0\times10^{-5}.$$
> Como $\mathrm{Re}\approx 6\times10^{-5}\ll1$, la bacteria vive en pleno régimen de [[Flujo de Stokes]]: la viscosidad domina por completo, no hay inercia, el nado es reversible.
>
> **(c) Semejanza en el túnel.** La maqueta tiene cuerda $c_m=c/10=0{,}2\ \text{m}$; el ala real $c_r=2\ \text{m}$. Igualamos los números de Reynolds:
> $$\mathrm{Re}_m=\mathrm{Re}_r\;\Longrightarrow\;\frac{U_m\,c_m}{\nu}=\frac{U_r\,c_r}{\nu}.$$
> La viscosidad cinemática se cancela (mismo fluido), luego
> $$U_m=U_r\,\frac{c_r}{c_m}=60\cdot\frac{2}{0{,}2}=60\cdot 10=600\ \text{m/s}.$$
> El modelo es $10$ veces menor, así que hay que soplar $10$ veces más rápido: $U_m=600\ \text{m/s}$. (En la práctica eso supera la velocidad del sonido y rompe la igualdad de $\mathrm{Ma}$; por eso los túneles reales usan aire presurizado para subir $\rho$ y bajar $\nu$, o aceptan semejanza parcial. Aquí ilustra el principio puro.) $\blacksquare$

---

![[reynolds_regimenes.svg|560]]

*Comparación de regímenes alrededor de un cilindro: a bajo $\mathrm{Re}$ el flujo es laminar, adherido y simétrico aguas arriba y aguas abajo (dominio viscoso); a alto $\mathrm{Re}$ la capa límite se desprende y se forma una estela ancha y turbulenta detrás del cuerpo (dominio inercial).*

---

## Resumen

> [!resumen] Lo esencial
>
> | Concepto | Expresión | Lectura |
> | :--- | :---: | :--- |
> | Definición | $\mathrm{Re}=\dfrac{\rho U L}{\mu}=\dfrac{U L}{\nu}$ | inercia / viscosidad |
> | N–S adimensional | $\dfrac{D\vec v^{\,*}}{Dt^{*}}=-\vec\nabla^{*}p^{*}+\dfrac{1}{\mathrm{Re}}\nabla^{*2}\vec v^{\,*}$ | un solo parámetro gobierna |
> | Escalas usadas | $L,\;U,\;T=L/U,\;P=\rho U^2$ | longitud, velocidad, tiempo, presión |
> | Semejanza | mismo $\mathrm{Re}$ + misma geometría | mismo flujo (modelos a escala) |
> | Coeficiente típico | $C_D=\dfrac{F_D}{\tfrac12\rho U^2 A}=f(\mathrm{Re})$ | base del ensayo en túnel |
> | Régimen viscoso | $\mathrm{Re}\ll1$ | [[Flujo de Stokes]], reversible |
> | Régimen inercial | $\mathrm{Re}\gg1$ | [[Capa Limite]] delgada |
> | Turbulencia | $\mathrm{Re}>\mathrm{Re}_{\text{cr}}$ ($\sim 2300$ en tubería) | flujo caótico |

> [!corolario] Por qué importa
> La adimensionalización reduce un problema con seis cantidades dimensionales a **una sola variable de control**, $\mathrm{Re}$. Esto: (1) permite predecir flujos reales a partir de maquetas; (2) explica por qué la naturaleza microscópica (bacterias, $\mathrm{Re}\ll1$) y la macroscópica (peces, aviones, $\mathrm{Re}\gg1$) son cualitativamente distintas; y (3) organiza toda la sección de [[5 Flujo Viscoso/index | Flujo Viscoso]] en torno a los dos límites $\mathrm{Re}\to 0$ y $\mathrm{Re}\to\infty$.

> [!warning] La escala $L$ debe declararse
> El valor de $\mathrm{Re}$ depende de **qué longitud característica $L$ se elige**: diámetro de la tubería, cuerda del perfil, longitud de la placa, radio de la esfera… No es lícito comparar dos números de Reynolds sin saber sobre qué escala se calcularon. Por la misma razón, un único flujo puede ser "viscoso" a escala pequeña e "inercial" a escala grande: por eso una bacteria de micras vive en $\mathrm{Re}\ll1$ mientras que un pez de decímetros nada en $\mathrm{Re}\gg1$, aun moviéndose ambos en el mismo agua.

> [!referencia] Fuentes
> - **L. D. Landau & E. M. Lifshitz**, _Mecánica de Fluidos_ (Curso de Física Teórica, Vol. 6), §19 "Semejanza".
> - **G. K. Batchelor**, _An Introduction to Fluid Dynamics_, cap. 4 (número de Reynolds y semejanza dinámica).
> - **F. M. White**, _Fluid Mechanics_, cap. 5 (análisis dimensional y semejanza).
> - Notas relacionadas: [[Ecuaciones de Navier-Stokes]], [[Flujo de Stokes]], [[Capa Limite]], [[Soluciones Viscosas Exactas]].
