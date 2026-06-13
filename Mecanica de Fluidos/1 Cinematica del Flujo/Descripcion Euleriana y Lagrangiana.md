---
title: Descripción Euleriana y Lagrangiana
tags:
  - fluidos
  - teoria
  - cinematica
draft: false
aliases:
  - Descripción euleriana y lagrangiana
  - Derivada material
  - Aceleración convectiva
---

# Descripción Euleriana y Lagrangiana $\dfrac{D}{Dt}=\partial_t+(\vec v\cdot\nabla)$

> [!definicion]
> Un fluido se puede mirar de dos maneras complementarias:
>
> - **Descripción lagrangiana** — se **sigue a cada partícula material** en su viaje. Se etiqueta a la partícula por su posición inicial $\vec a=\vec x(t_0)$ y se describe su **trayectoria** $\vec x=\vec x(\vec a,t)$. Toda propiedad ($F$) es función de la etiqueta y del tiempo, $F=F(\vec a,t)$. Es la mirada de la mecánica de partículas (Lagrange), pero seguir individualmente a infinitas partículas resulta inmanejable.
> - **Descripción euleriana** — se fija la atención en **puntos fijos del espacio** $\vec x$ y se observa qué fluido pasa por ellos en cada instante. La incógnita es el **campo** de velocidades $\vec v=\vec v(\vec x,t)$ (y de presión, densidad, etc.). Es la descripción que se usa casi siempre en fluidos: lo que medimos con un sensor en un punto es justamente $\vec v(\vec x,t)$.
>
> El puente entre ambas miradas es la **derivada material** (o sustancial), la tasa de cambio de una propiedad **siguiendo a la partícula** pero expresada con campos eulerianos:
> $$\boxed{\;\frac{D}{Dt}=\frac{\partial}{\partial t}+(\vec v\cdot\nabla)=\partial_t+v_j\,\partial_j\;}$$
> Su primer término ($\partial_t$) es **local** y el segundo ($v_j\partial_j$) es **convectivo**.

---

> [!info]
> **Primera nota del capítulo [[1 Cinematica del Flujo/index | Cinemática del Flujo]].** Fija el lenguaje (campo $\vec v(\vec x,t)$, convenio de suma de Einstein) con el que se escribirá todo el curso. Notas hermanas:
> - [[Lineas de Flujo]] — líneas de corriente, trayectorias y trazas; cuándo coinciden.
> - [[Tensor Gradiente de Velocidad]] — $\partial_j v_i=e_{ij}+\omega_{ij}$; velocidad relativa entre puntos vecinos.
> - [[Teorema del Transporte de Reynolds]] — derivar integrales sobre volúmenes materiales.
>
> **Referencia.** Landau-Lifshitz, Vol. 6 (*Mecánica de Fluidos*), §1; Batchelor, *An Introduction to Fluid Dynamics*, cap. 2.

---

![[euler_lagrange.svg|560]]
*Mirada **lagrangiana** (izquierda): se sigue una partícula concreta a lo largo de su trayectoria $\vec x(t)$. Mirada **euleriana** (derecha): se observa el campo $\vec v(\vec x,t)$ en puntos fijos del espacio por los que el fluido va pasando. La derivada material traduce una en la otra.*

---

> [!teoria] La derivada material: deducción
> El corazón de esta nota es relacionar "lo que le pasa a la partícula" con "lo que dicen los campos eulerianos". Sea $F(\vec x,t)$ **cualquier propiedad de campo** (un escalar como la temperatura, o una componente de la velocidad). Queremos su tasa de cambio **evaluada sobre una partícula** que en el instante $t$ ocupa el punto $\vec x(t)$, es decir, $\dfrac{d}{dt}F\big(\vec x(t),t\big)$.
>
> **Paso 1 — Regla de la cadena.** La función $t\mapsto F(\vec x(t),t)$ depende de $t$ por dos vías: directamente (último argumento) y a través de cada coordenada $x_j(t)$. Por la regla de la cadena para funciones de varias variables,
> $$\frac{d}{dt}F\big(\vec x(t),t\big)=\frac{\partial F}{\partial t}+\sum_{j}\frac{\partial F}{\partial x_j}\frac{dx_j}{dt}.$$
>
> **Paso 2 — Identificar la velocidad.** Por definición, la velocidad de la partícula es la tasa de cambio de su posición, $\dfrac{dx_j}{dt}=v_j$. Sustituyendo y usando el **convenio de suma** (índice $j$ repetido $\Rightarrow$ se suma sobre $j=1,2,3$):
> $$\frac{DF}{Dt}=\frac{\partial F}{\partial t}+v_j\,\frac{\partial F}{\partial x_j}=\partial_t F+v_j\,\partial_j F.$$
>
> **Paso 3 — Forma vectorial.** Reconociendo $v_j\,\partial_j F=(\vec v\cdot\nabla)F$, se obtiene el operador material:
> $$\frac{DF}{Dt}=\partial_t F+(\vec v\cdot\nabla)F.\qquad\blacksquare$$
>
> **Lectura de los dos términos.**
> - $\partial_t F$ — término **local** o **temporal**: cuánto cambia $F$ en un punto **fijo** del espacio porque el campo evoluciona en el tiempo.
> - $v_j\partial_j F$ — término **convectivo** (o advectivo): cuánto cambia $F$ para la partícula **porque se desplaza** a una región del espacio donde $F$ vale otra cosa, aunque el campo fuese constante en el tiempo. Es el transporte por el propio movimiento del fluido.

---

> [!proposicion] Aceleración de una partícula fluida
> Aplicando el operador material a la propia velocidad ($F\to v_i$), la **aceleración** de la partícula fluida es
> $$\vec a=\frac{D\vec v}{Dt}=\partial_t\vec v+(\vec v\cdot\nabla)\vec v,\qquad a_i=\partial_t v_i+v_j\,\partial_j v_i.$$
> El término local $\partial_t\vec v$ es lineal en $\vec v$; el término convectivo $(\vec v\cdot\nabla)\vec v$ es **cuadrático en la velocidad** —es decir, **no lineal**. Esa no linealidad es precisamente el origen de la dificultad de las ecuaciones de **Navier–Stokes** y la raíz de fenómenos como la **turbulencia**: el campo se transporta y se reorganiza a sí mismo.

> [!lema] Identidad para el término convectivo (forma de Lamb)
> Será clave para deducir Bernoulli más adelante:
> $$(\vec v\cdot\nabla)\vec v=\nabla\!\left(\tfrac12\,v^2\right)-\vec v\times(\nabla\times\vec v),\qquad v^2=\vec v\cdot\vec v.$$
>
> **Demostración (notación indicial).**
> **Paso 1 — Escribir el doble producto vectorial.** Sea $\vec\omega=\nabla\times\vec v$, de componentes $\omega_k=\epsilon_{klm}\,\partial_l v_m$. La componente $i$ de $\vec v\times\vec\omega$ es
> $$(\vec v\times\vec\omega)_i=\epsilon_{ijk}\,v_j\,\omega_k=\epsilon_{ijk}\,v_j\,\epsilon_{klm}\,\partial_l v_m.$$
>
> **Paso 2 — Identidad épsilon-delta.** Usando $\epsilon_{ijk}\epsilon_{klm}=\epsilon_{kij}\epsilon_{klm}=\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}$,
> $$(\vec v\times\vec\omega)_i=(\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl})\,v_j\,\partial_l v_m=v_j\,\partial_i v_j-v_j\,\partial_j v_i.$$
>
> **Paso 3 — Reconocer cada pieza.** El primer término es $v_j\,\partial_i v_j=\partial_i\!\big(\tfrac12 v_j v_j\big)=\partial_i\!\big(\tfrac12 v^2\big)$; el segundo es el convectivo $v_j\partial_j v_i=\big[(\vec v\cdot\nabla)\vec v\big]_i$. Por tanto
> $$\big(\vec v\times(\nabla\times\vec v)\big)_i=\partial_i\!\big(\tfrac12 v^2\big)-\big[(\vec v\cdot\nabla)\vec v\big]_i.$$
>
> **Paso 4 — Despejar.** Pasando términos,
> $$\big[(\vec v\cdot\nabla)\vec v\big]_i=\partial_i\!\big(\tfrac12 v^2\big)-\big(\vec v\times(\nabla\times\vec v)\big)_i,$$
> que en forma vectorial es la identidad buscada. $\blacksquare$

---

## Ejemplo

> [!ejemplo] Flujo estacionario en una contracción (tobera)
> Un fluido entra por un conducto que se estrecha. Por simplicidad, modelamos el flujo como **estacionario** y aproximadamente unidimensional a lo largo del eje, con
> $$\vec v=v_x(x)\,\hat{\imath},\qquad v_x(x)=U_0\,(1+\alpha x),\quad \alpha>0,$$
> de modo que el fluido **acelera** al avanzar (la sección se reduce, la velocidad crece con $x$). El campo no depende del tiempo: $\partial_t\vec v=\vec 0$. ¿Acelera una partícula fluida?

> [!solucion]
> **Paso 1 — Término local.** Como el campo es estacionario,
> $$\partial_t v_x=0.$$
>
> **Paso 2 — Término convectivo.** Con $\vec v=v_x(x)\,\hat\imath$, el único término que sobrevive de $v_j\partial_j v_x$ es $v_x\,\partial_x v_x$:
> $$a_x=\underbrace{\partial_t v_x}_{=0}+v_x\,\frac{\partial v_x}{\partial x}=v_x\,\frac{dv_x}{dx}.$$
>
> **Paso 3 — Evaluar.** Con $v_x=U_0(1+\alpha x)$ se tiene $\dfrac{dv_x}{dx}=U_0\alpha$, luego
> $$a_x=U_0(1+\alpha x)\cdot U_0\alpha=U_0^2\,\alpha\,(1+\alpha x)\neq 0.$$
>
> **Conclusión.** Aunque el campo **no cambia en el tiempo** ($\partial_t\vec v=\vec 0$), cada partícula fluida **sí acelera**: al moverse hacia $x$ mayores entra en zonas donde la velocidad del campo es mayor. La aceleración es puramente **convectiva**. (Equivalentemente, $a_x=v_x\,dv_x/dx=\tfrac12\,d(v_x^2)/dx$, consistente con la identidad de Lamb.) $\blacksquare$

> [!warning] "Estacionario" no es "sin aceleración"
> $\partial_t\vec v=\vec 0$ (flujo **estacionario**: el campo no cambia en el tiempo) **NO** implica $\vec a=\vec 0$. Una partícula puede acelerar aunque el campo esté congelado en el tiempo, por el término **convectivo** $(\vec v\cdot\nabla)\vec v$. Confundir $\partial_t\vec v$ con $\vec a$ es el error clásico al empezar en fluidos.

---

## En qué consiste

Pensar en un fluido como un sistema mecánico parece sugerir la mirada **lagrangiana**: numerar cada gotita de fluido por su posición inicial $\vec a$ y seguir su trayectoria $\vec x(\vec a,t)$, igual que en la mecánica de un punto material. Esa descripción es conceptualmente limpia —las leyes de Newton se escriben sobre la partícula—, pero **inmanejable**: un fluido tiene un continuo de partículas y rastrearlas todas es imposible en la práctica.

La alternativa **euleriana** renuncia a saber "qué partícula" está en cada sitio y se queda con el dato físicamente accesible: el **campo** $\vec v(\vec x,t)$, qué velocidad tiene el fluido que **ahora mismo** pasa por el punto $\vec x$. Es lo que mide un anemómetro o un tubo de Pitot fijo. El precio a pagar es que las leyes de Newton están escritas para partículas, no para puntos del espacio. Ahí entra la **derivada material**: es el operador que, partiendo de campos eulerianos, recupera "lo que le ocurre a la partícula que justo ahora pasa por aquí".

La fórmula $\dfrac{D}{Dt}=\partial_t+(\vec v\cdot\nabla)$ encapsula esa traducción. El término **local** $\partial_t$ captura el cambio del campo en un punto fijo (lo que vería una cámara quieta), y el término **convectivo** $(\vec v\cdot\nabla)$ añade el cambio que la partícula experimenta **por desplazarse** a otra región. Aplicada a la velocidad, esta derivada da la aceleración $\vec a=\partial_t\vec v+(\vec v\cdot\nabla)\vec v$, cuyo término convectivo —no lineal— es el que hace de la mecánica de fluidos una teoría tan difícil como rica: es lo que conecta puntos vecinos del flujo (ver [[Tensor Gradiente de Velocidad]]) y, a través de la vorticidad $\nabla\times\vec v$ que aparece en la identidad de Lamb, lo que abre la puerta a Bernoulli y a la dinámica de la rotación del fluido.

---

## Resumen

> [!resumen] Lo esencial
> | Concepto | Expresión | Lectura |
> |:---|:---|:---|
> | Lagrangiana | $\vec x=\vec x(\vec a,t)$, $\;F=F(\vec a,t)$ | seguir la partícula etiquetada por $\vec a=\vec x(t_0)$ |
> | Euleriana | $\vec v=\vec v(\vec x,t)$ | campo en puntos fijos del espacio (la usual) |
> | Derivada material | $\dfrac{D}{Dt}=\partial_t+v_j\partial_j$ | tasa de cambio siguiendo la partícula |
> | Término local | $\partial_t F$ | el campo cambia en el punto fijo |
> | Término convectivo | $v_j\partial_j F$ | la partícula se mueve a otra región |
> | Aceleración | $a_i=\partial_t v_i+v_j\partial_j v_i$ | el convectivo $v_j\partial_j v_i$ es **no lineal** |
> | Identidad de Lamb | $(\vec v\cdot\nabla)\vec v=\nabla(\tfrac12 v^2)-\vec v\times(\nabla\times\vec v)$ | separa "energía cinética" de "vorticidad" |

> [!corolario] Idea para recordar
> La **derivada material** es el único puente entre la mirada euleriana (campos) y las leyes de Newton (partículas). Su parte convectiva implica que un **flujo estacionario puede tener partículas aceleradas**, y su no linealidad es la fuente última de la complejidad de Navier–Stokes.

> [!referencia]
> Landau-Lifshitz, Vol. 6 (*Mecánica de Fluidos*), §1 — introduce el campo euleriano y la derivada material casi de inmediato. Batchelor, *An Introduction to Fluid Dynamics*, cap. 2 (§2.1–2.2) — descripciones material y espacial; aceleración convectiva.
