---
title: Ecuaciones de Navier-Stokes
tags:
  - fluidos
  - teoria
  - conservacion
draft: false
aliases:
  - Ecuaciones de Navier-Stokes
  - Navier-Stokes
---

# Ecuaciones de Navier-Stokes $\rho\dfrac{D\vec v}{Dt}=-\nabla p+\mu\nabla^2\vec v+\rho\vec g$

> [!definicion]
> Las **ecuaciones de Navier–Stokes** son las ecuaciones de movimiento de un fluido viscoso newtoniano. Se obtienen al insertar la **relación constitutiva newtoniana** en la **ecuación de Cauchy** del momento, y expresan la segunda ley de Newton para una partícula fluida: su inercia $\rho\,D\vec v/Dt$ iguala la suma de las fuerzas por unidad de volumen —gradiente de presión, fricción viscosa y gravedad—. En su forma **incompresible** ($\nabla\cdot\vec v=0$) son
> $$\boxed{\;\rho\Big(\partial_t\vec v+(\vec v\cdot\nabla)\vec v\Big)=-\nabla p+\mu\nabla^2\vec v+\rho\vec g\;}\qquad \nabla\cdot\vec v=0.$$
> Junto con la continuidad forman un sistema cerrado de **cuatro ecuaciones** (continuidad + tres componentes de momento) para **cuatro incógnitas**: el campo de velocidad $\vec v$ y la presión $p$.

---

> [!info]
> Nota central de la sección [[3 Ecuaciones de Conservacion/index | Ecuaciones de Conservación]]. Sus hermanas son [[Conservacion de Momento]] (de donde toma la ecuación de Cauchy), [[Conservacion de Masa]] (que aporta la continuidad $\nabla\cdot\vec v=0$) y [[Conservacion de Energia]]. La pieza que cierra la deducción es la relación constitutiva de un [[Fluido Newtoniano]]. Esta ecuación prepara los dos capítulos siguientes: el límite $\mu=0$ da el [[4 Flujo Ideal/index | Flujo Ideal]] (Euler, Bernoulli) y el caso $\mu\neq0$ da el [[5 Flujo Viscoso/index | Flujo Viscoso]] (Reynolds, capa límite).
> **Referencia.** Landau-Lifshitz, Vol. 6, §15; Batchelor, *An Introduction to Fluid Dynamics*, cap. 3.

---

## Derivación

> [!teoria] El punto de partida y la receta
> Tenemos dos ingredientes. El primero es la **ecuación de Cauchy** del momento ([[Conservacion de Momento]]), la segunda ley de Newton local para el fluido, escrita con índices ($i,j=1,2,3$, convenio de suma de Einstein):
> $$\rho\,\frac{Dv_i}{Dt}=\partial_j\sigma_{ij}+\rho g_i.$$
> El segundo es la **relación constitutiva newtoniana** ([[Fluido Newtoniano]]), que liga el tensor de esfuerzos $\sigma_{ij}$ con el tensor de velocidad de deformación $e_{ij}=\tfrac12(\partial_i v_j+\partial_j v_i)$:
> $$\sigma_{ij}=-p\,\delta_{ij}+2\mu\,e_{ij}+\lambda\,\delta_{ij}\,e_{kk},$$
> donde $\mu$ es la viscosidad dinámica y $\lambda$ la segunda viscosidad (de volumen). La derivación consiste en **calcular la divergencia $\partial_j\sigma_{ij}$** término a término y sustituirla en Cauchy.

> [!demostracion] De Cauchy a Navier–Stokes (forma compresible)
> Tomamos $\mu$ y $\lambda$ constantes y calculamos $\partial_j\sigma_{ij}$ sumando las contribuciones de los tres sumandos.
>
> **Paso 1 — Término de presión.** Aplicamos $\partial_j$ a $-p\,\delta_{ij}$. La delta de Kronecker $\delta_{ij}$ selecciona $j=i$ al contraer, de modo que
> $$\partial_j(-p\,\delta_{ij})=-\delta_{ij}\,\partial_j p=-\partial_i p.$$
> Es decir, la parte isótropa del esfuerzo produce exactamente el gradiente de presión $-\nabla p$.
>
> **Paso 2 — Término viscoso desviador.** Aplicamos $\partial_j$ a $2\mu\,e_{ij}$ con $\mu$ constante:
> $$\partial_j(2\mu\,e_{ij})=\mu\,\partial_j(\partial_i v_j+\partial_j v_i)=\mu\big(\partial_i(\partial_j v_j)+\partial_j\partial_j v_i\big).$$
> Hemos usado que las derivadas parciales conmutan, $\partial_j\partial_i=\partial_i\partial_j$. Ahora reconocemos $\partial_j v_j=\nabla\cdot\vec v$ y $\partial_j\partial_j=\nabla^2$ (laplaciano), luego
> $$\partial_j(2\mu\,e_{ij})=\mu\,\partial_i(\nabla\cdot\vec v)+\mu\,\nabla^2 v_i.$$
>
> **Paso 3 — Término de viscosidad de volumen.** Aplicamos $\partial_j$ a $\lambda\,\delta_{ij}\,e_{kk}$, con $e_{kk}=\partial_k v_k=\nabla\cdot\vec v$ (la traza es la dilatación). La delta vuelve a contraer $j=i$:
> $$\partial_j(\lambda\,\delta_{ij}\,e_{kk})=\lambda\,\delta_{ij}\,\partial_j(\nabla\cdot\vec v)=\lambda\,\partial_i(\nabla\cdot\vec v).$$
>
> **Paso 4 — Reunir.** Sumamos los tres pasos para obtener la divergencia completa:
> $$\partial_j\sigma_{ij}=-\partial_i p+\mu\,\nabla^2 v_i+(\mu+\lambda)\,\partial_i(\nabla\cdot\vec v).$$
> Sustituyendo en la ecuación de Cauchy $\rho\,Dv_i/Dt=\partial_j\sigma_{ij}+\rho g_i$ llegamos a la **forma compresible** de Navier–Stokes:
> $$\rho\,\frac{Dv_i}{Dt}=-\partial_i p+\mu\,\nabla^2 v_i+(\mu+\lambda)\,\partial_i(\nabla\cdot\vec v)+\rho g_i.$$
> $\blacksquare$

> [!proposicion] Forma incompresible
> Para un flujo **incompresible**, la conservación de masa ([[Conservacion de Masa]]) impone $\nabla\cdot\vec v=0$. Entonces el término $(\mu+\lambda)\,\partial_i(\nabla\cdot\vec v)$ se anula idénticamente, y la ecuación compresible se reduce a
> $$\rho\,\frac{Dv_i}{Dt}=-\partial_i p+\mu\,\nabla^2 v_i+\rho g_i.$$
> Escribiendo la derivada material $D/Dt=\partial_t+(\vec v\cdot\nabla)$ en notación vectorial:
> $$\boxed{\;\rho\Big(\partial_t\vec v+(\vec v\cdot\nabla)\vec v\Big)=-\nabla p+\mu\nabla^2\vec v+\rho\vec g\;}.$$
> Acompañada de $\nabla\cdot\vec v=0$, constituye un **sistema cerrado**: 4 ecuaciones escalares para las 4 incógnitas $(\vec v,p)$. La viscosidad de volumen $\lambda$ desaparece —en un fluido incompresible solo importa $\mu$—.

---

## En qué consiste

![[navier_stokes.svg|480]]
*La ecuación maestra de la mecánica de fluidos: la inercia de la partícula fluida ($\rho\,D\vec v/Dt$) iguala la suma de las fuerzas por unidad de volumen —el gradiente de presión $-\nabla p$, la fricción viscosa $\mu\nabla^2\vec v$ y la gravedad $\rho\vec g$—. Es a los fluidos lo que las ecuaciones de Maxwell son al electromagnetismo.*

> [!teoria] Significado de cada término
> Leyendo la ecuación de izquierda a derecha, cada sumando tiene una interpretación física directa:
> - $\rho\,\partial_t\vec v$ — **inercia local**: cómo cambia la velocidad en un punto fijo del espacio con el tiempo.
> - $\rho(\vec v\cdot\nabla)\vec v$ — **inercia convectiva**: la partícula acelera al moverse hacia regiones con otra velocidad. Es el único término **no lineal**.
> - $-\nabla p$ — **fuerza de presión**: el fluido es empujado de las zonas de alta a las de baja presión.
> - $\mu\nabla^2\vec v$ — **fricción viscosa**: difusión de momento entre capas vecinas, que tiende a uniformar el perfil de velocidad.
> - $\rho\vec g$ — **gravedad** (o cualquier fuerza de cuerpo por unidad de volumen).

> [!corolario] Viscosidad cinemática y forma reducida
> Dividiendo la forma incompresible por $\rho$ aparece la **viscosidad cinemática** $\nu=\mu/\rho$ (unidades de $\mathrm{m^2/s}$, las de un coeficiente de difusión):
> $$\frac{D\vec v}{Dt}=-\frac1\rho\nabla p+\nu\,\nabla^2\vec v+\vec g.$$
> En esta forma se ve que $\nu$ es la **difusividad del momento**: el término $\nu\nabla^2\vec v$ es estructuralmente idéntico al de la ecuación del calor, y describe cómo el momento se reparte por difusión a través del fluido.

> [!teorema] El término no lineal y el problema del milenio
> El sumando convectivo $(\vec v\cdot\nabla)\vec v$ es **cuadrático** en $\vec v$: ahí reside toda la dificultad. Matemáticamente, impide aplicar superposición y hace que la existencia y unicidad de soluciones suaves en tres dimensiones sea un **problema abierto** —uno de los siete *Problemas del Milenio*—. Físicamente, es el responsable de la **turbulencia**: cuando domina sobre la fricción viscosa, el flujo se vuelve caótico y multiescalar. La razón entre inercia convectiva y fricción se cuantifica con el número de Reynolds del [[5 Flujo Viscoso/index | Flujo Viscoso]].

> [!regla] Condición de no deslizamiento
> Sobre una **pared sólida**, un fluido viscoso satisface la condición de **no deslizamiento**:
> $$\vec v=\vec v_{\text{pared}}\quad\text{(en la pared)}.$$
> La componente normal expresa impenetrabilidad (la pared no deja pasar fluido), pero la novedad es la **componente tangencial**: la viscosidad obliga al fluido a quedar adherido y moverse con la pared. Esto se debe a que $\mu\neq0$ acopla por fricción las capas contiguas hasta la última, la que toca el sólido. En el [[4 Flujo Ideal/index | flujo ideal]] ($\mu=0$) esta condición desaparece —el laplaciano se va y solo se exige impenetrabilidad—, y por eso el fluido ideal **sí desliza** sobre las paredes. La discrepancia se concentra en una **capa límite** delgada.

---

## Ejemplo

> [!ejemplo] Flujo plano unidireccional (Couette / Poiseuille)
> Reduzcamos Navier–Stokes a un caso resoluble: flujo **estacionario**, **incompresible** y **unidireccional** entre dos placas planas horizontales, con
> $$\vec v=(u(y),\,0,\,0).$$
> Despreciamos la gravedad (o la absorbemos en la presión). Queremos hallar el perfil $u(y)$.

> [!solucion]
> **Paso 1 — Continuidad.** $\nabla\cdot\vec v=\partial_x u(y)=0$ se cumple automáticamente, pues $u$ no depende de $x$. El campo es admisible.
>
> **Paso 2 — Anular el término convectivo.** La componente $x$ del término no lineal es
> $$(\vec v\cdot\nabla)u=u\,\partial_x u+0\cdot\partial_y u+0\cdot\partial_z u=u\,\partial_x u=0,$$
> ya que $u=u(y)$ no depende de $x$. **El término no lineal se anula**: este es justo el tipo de simetría que vuelve la ecuación tratable.
>
> **Paso 3 — Componente $x$ de Navier–Stokes.** Con $\partial_t\vec v=0$ (estacionario) y el convectivo nulo, la ecuación en $x$ queda lineal:
> $$0=-\partial_x p+\mu\,\frac{\partial^2 u}{\partial y^2}\quad\Longrightarrow\quad \mu\,u''(y)=\partial_x p.$$
> La componente $y$ da $\partial_y p=0$, así que $p=p(x)$ y $\partial_x p\equiv -G$ es una constante (el gradiente de presión impuesto).
>
> **Paso 4 — Integrar.** Como $u''(y)=-G/\mu$ es constante, integramos dos veces:
> $$u(y)=-\frac{G}{2\mu}\,y^2+C_1\,y+C_2.$$
> Las constantes $C_1,C_2$ se fijan con la condición de **no deslizamiento** en ambas placas. Si $G=0$ y una placa se mueve, el perfil es lineal (**flujo de Couette**); si las placas están fijas y $G\neq0$, el perfil es parabólico (**flujo de Poiseuille plano**). $\blacksquare$
>
> Estos perfiles se desarrollan en detalle en [[Soluciones Viscosas Exactas]].

> [!warning]
> Navier–Stokes es un sistema de **EDP no lineales acopladas**. Salvo en presencia de simetrías especiales —como la del ejemplo, donde el término convectivo se anula— **no admite solución analítica**. Por eso casi todo el resto del curso consiste en estudiar **límites** donde sí se puede resolver: $\mu=0$ ([[4 Flujo Ideal/index | flujo ideal]]), $\mathrm{Re}\ll1$ (flujo reptante) o la aproximación de **capa límite**. La ecuación completa, con su no linealidad intacta, solo se ataca numéricamente.

---

## Resumen

> [!resumen]
> | Concepto \| Expresión \| Significado |
> |---|---|---|
> | Ecuación de Cauchy \| $\rho\,Dv_i/Dt=\partial_j\sigma_{ij}+\rho g_i$ \| Punto de partida (2ª ley de Newton) |
> | Relación newtoniana \| $\sigma_{ij}=-p\,\delta_{ij}+2\mu e_{ij}+\lambda\,\delta_{ij}e_{kk}$ \| Cierra la incógnita $\sigma_{ij}$ |
> | N–S compresible \| $\rho\,Dv_i/Dt=-\partial_i p+\mu\nabla^2 v_i+(\mu+\lambda)\partial_i(\nabla\cdot\vec v)+\rho g_i$ \| Forma general |
> | N–S incompresible \| $\rho(\partial_t\vec v+(\vec v\cdot\nabla)\vec v)=-\nabla p+\mu\nabla^2\vec v+\rho\vec g$ \| Con $\nabla\cdot\vec v=0$ |
> | Forma cinemática \| $D\vec v/Dt=-\tfrac1\rho\nabla p+\nu\nabla^2\vec v+\vec g$ \| $\nu=\mu/\rho$ difusividad del momento |
> | Término no lineal \| $(\vec v\cdot\nabla)\vec v$ \| Turbulencia; problema del milenio |
> | Frontera viscosa \| $\vec v=\vec v_{\text{pared}}$ \| No deslizamiento |

> [!corolario] La idea en una frase
> Navier–Stokes es la **ecuación maestra** del curso: Cauchy más la ley newtoniana, un sistema cerrado de 4 ecuaciones para $(\vec v,p)$. Su término convectivo no lineal la hace, en general, irresoluble salvo numéricamente o en límites simétricos; de esos límites nacen el [[4 Flujo Ideal/index | Flujo Ideal]] ($\mu=0$) y el [[5 Flujo Viscoso/index | Flujo Viscoso]] ($\mathrm{Re}$ y capa límite).

> [!referencia]
> Landau-Lifshitz, *Mecánica de Fluidos* (Vol. 6 del Curso de Física Teórica), §15 (ecuaciones del movimiento de un fluido viscoso). Batchelor, *An Introduction to Fluid Dynamics*, cap. 3.
