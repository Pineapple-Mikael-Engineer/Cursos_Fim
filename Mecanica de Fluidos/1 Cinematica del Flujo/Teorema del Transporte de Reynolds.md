---
title: Teorema del Transporte de Reynolds
order: 5
tags:
  - fluidos
  - teoria
  - cinematica
draft: false
aliases:
  - Teorema del transporte de Reynolds
  - Reynolds transport theorem
---

# Teorema del Transporte de Reynolds $\dfrac{d}{dt}\!\int_{V(t)}\phi\,dV=\int_V\partial_t\phi\,dV+\oint_S\phi\,(\vec v\cdot\hat n)\,dA$

> [!definicion]
> El **teorema del transporte de Reynolds** es la regla de Leibniz para derivar respecto al tiempo una integral sobre un **volumen material** $V(t)$ —una porción de fluido cuyas fronteras $S(t)$ **viajan con el propio fluido** a la velocidad $\vec v$—. Para cualquier campo escalar $\phi(\vec x,t)$ (densidad, energía por unidad de volumen, una componente de cantidad de movimiento, etc.):
> $$\boxed{\;\frac{d}{dt}\int_{V(t)}\phi\,dV=\underbrace{\int_{V}\frac{\partial\phi}{\partial t}\,dV}_{\text{cambio local}}+\underbrace{\oint_{S}\phi\,(\vec v\cdot\hat n)\,dA}_{\text{flujo por la frontera}}\;}$$
> Aplicando el **teorema de la divergencia** al término de superficie, adopta la **forma diferencial**:
> $$\frac{d}{dt}\int_{V(t)}\phi\,dV=\int_V\left[\frac{\partial\phi}{\partial t}+\nabla\cdot(\phi\,\vec v)\right]dV.$$
> Y reagrupando con la **derivada material**:
> $$\frac{d}{dt}\int_{V(t)}\phi\,dV=\int_V\left[\frac{D\phi}{Dt}+\phi\,\nabla\cdot\vec v\right]dV.$$
> El teorema traduce la tasa de cambio de una **propiedad de la materia** (mirada lagrangiana) en operaciones sobre **campos eulerianos**: es la pieza que convierte las leyes de conservación de la mecánica en ecuaciones diferenciales de campo.

---

> [!info]
> **Cierra el capítulo [[1 Cinematica del Flujo/index | Cinemática del Flujo]].** Necesita el lenguaje de la [[Descripcion Euleriana y Lagrangiana]] (campo $\vec v(\vec x,t)$, derivada material $D/Dt$) y se apoya en la cinemática local de la [[Deformacion y Vorticidad]] (la divergencia $\nabla\cdot\vec v$ como tasa de dilatación). La herramienta matemática clave es el **teorema de la divergencia** (Gauss). Este teorema **prepara** las [[3 Ecuaciones de Conservacion/index | Ecuaciones de Conservación]]: aplicado a la masa da continuidad, a la cantidad de movimiento da Cauchy/Navier–Stokes, y a la energía la primera ley.
>
> **Referencia.** Landau-Lifshitz, Vol. 6 (*Mecánica de Fluidos*), §1; Batchelor, *An Introduction to Fluid Dynamics*, cap. 2.

---

![[volumen_control.svg|420]]
*Volumen material $V(t)$ y su frontera $S(t)$ moviéndose con el fluido. El cambio de $\int_V\phi\,dV$ tiene dos causas: que $\phi$ varíe en el tiempo **dentro** del volumen, y que la frontera **barra** volumen nuevo a velocidad $\vec v$, dejando entrar o salir el flujo $\phi\,(\vec v\cdot\hat n)$ a través de $S(t)$.*

---

> [!teorema] Teorema del transporte de Reynolds
> Sea $V(t)$ un volumen material (sus puntos frontera se mueven con la velocidad del fluido $\vec v(\vec x,t)$) y $\phi(\vec x,t)$ un campo escalar suave. Entonces
> $$\frac{d}{dt}\int_{V(t)}\phi\,dV=\int_{V}\frac{\partial\phi}{\partial t}\,dV+\oint_{S}\phi\,(\vec v\cdot\hat n)\,dA=\int_V\left[\frac{\partial\phi}{\partial t}+\nabla\cdot(\phi\,\vec v)\right]dV,$$
> con $\hat n$ la normal exterior a $S=\partial V$.

> [!demostracion] Las dos contribuciones al cambio
> El obstáculo es que en $\dfrac{d}{dt}\int_{V(t)}\phi\,dV$ **el dominio de integración cambia con el tiempo**: no se puede meter la derivada dentro de la integral sin más, porque derivaríamos $\phi$ olvidando que $V(t)$ se mueve y deforma. Separamos las dos causas físicas del cambio.
>
> **Paso 1 — Plantear la derivada como límite.** Por definición,
> $$\frac{d}{dt}\int_{V(t)}\phi\,dV=\lim_{\Delta t\to 0}\frac{1}{\Delta t}\left[\int_{V(t+\Delta t)}\phi(\vec x,t+\Delta t)\,dV-\int_{V(t)}\phi(\vec x,t)\,dV\right].$$
> Sumamos y restamos el término puente $\displaystyle\int_{V(t)}\phi(\vec x,t+\Delta t)\,dV$, que integra el campo **nuevo** sobre el dominio **viejo**:
> $$\frac{d}{dt}\int_{V(t)}\phi\,dV=\underbrace{\lim_{\Delta t\to 0}\int_{V(t)}\frac{\phi(\vec x,t+\Delta t)-\phi(\vec x,t)}{\Delta t}\,dV}_{(\mathrm{I})}+\underbrace{\lim_{\Delta t\to 0}\frac{1}{\Delta t}\left[\int_{V(t+\Delta t)}-\int_{V(t)}\right]\phi(\vec x,t+\Delta t)\,dV}_{(\mathrm{II})}.$$
>
> **Paso 2 — Término (I): el campo cambia en el volumen.** El dominio está **fijo** en $V(t)$, así que el límite entra y deriva solo a $\phi$ en el tiempo:
> $$(\mathrm{I})=\int_{V(t)}\frac{\partial\phi}{\partial t}\,dV.$$
> Es el cambio **local**: aunque el volumen estuviese quieto, $\phi$ evoluciona dentro de él.
>
> **Paso 3 — Término (II): la frontera barre volumen nuevo.** La diferencia $V(t+\Delta t)\setminus V(t)$ es la cáscara delgada que la frontera $S(t)$ recorre en el tiempo $\Delta t$. Un elemento $dA$ de la superficie, con normal exterior $\hat n$, se desplaza $\vec v\,\Delta t$, generando un volumen elemental
> $$dV_{\text{barrido}}=(\vec v\,\Delta t)\cdot\hat n\,dA=(\vec v\cdot\hat n)\,\Delta t\,dA,$$
> positivo donde el fluido sale ($\vec v\cdot\hat n>0$) y negativo donde entra. Integrando $\phi$ sobre esa cáscara y dividiendo por $\Delta t$ (en el límite, $\phi(\vec x,t+\Delta t)\to\phi(\vec x,t)$):
> $$(\mathrm{II})=\oint_{S(t)}\phi\,(\vec v\cdot\hat n)\,dA.$$
> Es el **flujo** de $\phi$ a través de la frontera móvil.
>
> **Paso 4 — Sumar las dos contribuciones.** Reuniendo (I) y (II) se obtiene la forma integral:
> $$\frac{d}{dt}\int_{V(t)}\phi\,dV=\int_{V}\frac{\partial\phi}{\partial t}\,dV+\oint_{S}\phi\,(\vec v\cdot\hat n)\,dA.$$
>
> **Paso 5 — Forma diferencial (teorema de la divergencia).** El campo vectorial $\phi\,\vec v$ es suave, así que el teorema de la divergencia (Gauss) convierte el flujo de superficie en una integral de volumen:
> $$\oint_{S}\phi\,(\vec v\cdot\hat n)\,dA=\oint_{S}(\phi\,\vec v)\cdot\hat n\,dA=\int_{V}\nabla\cdot(\phi\,\vec v)\,dV.$$
> Sustituyendo,
> $$\frac{d}{dt}\int_{V(t)}\phi\,dV=\int_V\left[\frac{\partial\phi}{\partial t}+\nabla\cdot(\phi\,\vec v)\right]dV.\qquad\blacksquare$$

---

> [!proposicion] Forma con la derivada material
> El teorema de Reynolds también se escribe
> $$\frac{d}{dt}\int_{V(t)}\phi\,dV=\int_V\left[\frac{D\phi}{Dt}+\phi\,\nabla\cdot\vec v\right]dV.$$
>
> **Demostración.** **Paso 1 — Expandir la divergencia del producto.** Por la regla del producto para la divergencia de "escalar por vector",
> $$\nabla\cdot(\phi\,\vec v)=\phi\,\nabla\cdot\vec v+\vec v\cdot\nabla\phi.$$
>
> **Paso 2 — Sustituir en la forma diferencial.** Partiendo del Paso 5 anterior,
> $$\frac{\partial\phi}{\partial t}+\nabla\cdot(\phi\,\vec v)=\frac{\partial\phi}{\partial t}+\vec v\cdot\nabla\phi+\phi\,\nabla\cdot\vec v.$$
>
> **Paso 3 — Reconocer la derivada material.** Los dos primeros términos son exactamente $\dfrac{D\phi}{Dt}=\partial_t\phi+\vec v\cdot\nabla\phi$ (ver [[Descripcion Euleriana y Lagrangiana]]). Por tanto
> $$\frac{\partial\phi}{\partial t}+\nabla\cdot(\phi\,\vec v)=\frac{D\phi}{Dt}+\phi\,\nabla\cdot\vec v,$$
> e integrando sobre $V(t)$ se obtiene la forma buscada. $\blacksquare$
>
> **Lectura.** El cambio total de $\int\phi\,dV$ se reparte en: $\dfrac{D\phi}{Dt}$, cuánto cambia $\phi$ **siguiendo a cada partícula**, y $\phi\,\nabla\cdot\vec v$, cuánto cambia por **dilatación o compresión** del volumen material (recordar que $\nabla\cdot\vec v$ es la tasa de cambio relativo de volumen, ver [[Deformacion y Vorticidad]]).

---

> [!corolario] Aplicación inmediata: conservación de la masa
> Tomemos $\phi=\rho$, la densidad. La masa de un volumen **material** es, por definición, **constante** (no entra ni sale materia: las fronteras viajan con el fluido):
> $$\frac{d}{dt}\int_{V(t)}\rho\,dV=0.$$
>
> **Paso 1 — Aplicar Reynolds (forma diferencial).** Con $\phi=\rho$,
> $$0=\frac{d}{dt}\int_{V(t)}\rho\,dV=\int_V\left[\frac{\partial\rho}{\partial t}+\nabla\cdot(\rho\,\vec v)\right]dV.$$
>
> **Paso 2 — Localizar (argumento del volumen arbitrario).** La igualdad vale para **cualquier** volumen material $V(t)$. Si una función continua tiene integral nula sobre todo volumen, la función es idénticamente nula. Por tanto el integrando se anula punto a punto:
> $$\boxed{\;\frac{\partial\rho}{\partial t}+\nabla\cdot(\rho\,\vec v)=0\;}$$
> que es la **ecuación de continuidad**.
>
> **Paso 3 — Forma material.** Usando $\nabla\cdot(\rho\vec v)=\rho\nabla\cdot\vec v+\vec v\cdot\nabla\rho$ y $\dfrac{D\rho}{Dt}=\partial_t\rho+\vec v\cdot\nabla\rho$:
> $$\frac{D\rho}{Dt}+\rho\,\nabla\cdot\vec v=0.\qquad\blacksquare$$
> Es el **primer fruto** del teorema y la primera de las [[3 Ecuaciones de Conservacion/index | Ecuaciones de Conservación]].

---

## Ejemplo

> [!ejemplo] El caso incompresible: el volumen material se conserva
> Tomemos $\phi=1$ (campo constante igual a $1$): entonces $\displaystyle\int_{V(t)}\phi\,dV=\int_{V(t)}dV=\mathrm{Vol}\big(V(t)\big)$ es literalmente el **volumen** de la porción de fluido. Queremos su tasa de cambio para un flujo **incompresible**, definido por $\nabla\cdot\vec v=0$.

> [!solucion]
> **Paso 1 — Aplicar Reynolds.** Con $\phi=1$ se tiene $\partial_t\phi=0$ y $\nabla\cdot(\phi\,\vec v)=\nabla\cdot\vec v$, así que la forma diferencial da
> $$\frac{d}{dt}\,\mathrm{Vol}\big(V(t)\big)=\frac{d}{dt}\int_{V(t)}dV=\int_V\big[\,0+\nabla\cdot\vec v\,\big]\,dV=\int_V\nabla\cdot\vec v\,dV.$$
>
> **Paso 2 — Imponer incompresibilidad.** Si $\nabla\cdot\vec v=0$ en todo el dominio,
> $$\frac{d}{dt}\,\mathrm{Vol}\big(V(t)\big)=0.$$
>
> **Conclusión.** En un flujo incompresible, **toda porción material de fluido conserva su volumen** mientras se mueve y se deforma (puede estirarse en una dirección y comprimirse en otra, pero su volumen total no cambia). Coherentemente, la continuidad $\frac{D\rho}{Dt}+\rho\nabla\cdot\vec v=0$ se reduce a $\frac{D\rho}{Dt}=0$: la densidad de cada partícula es constante a lo largo de su trayectoria. $\blacksquare$

> [!warning] Volumen material vs. volumen de control fijo
> No confundir dos dominios distintos:
> - **Volumen material** $V(t)$ — sus fronteras **viajan con el fluido** (velocidad $\vec v$). Siempre contiene **las mismas partículas**; no cruza materia por su frontera. Es donde se escriben las leyes de Newton/conservación (mirada **lagrangiana**).
> - **Volumen de control fijo** $V_0$ — sus fronteras están **quietas** en el espacio. El fluido lo **atraviesa**; sí hay flujo neto de masa, momento y energía por su frontera (mirada **euleriana**).
>
> El teorema de Reynolds es justamente **el puente** entre ambos: toma una ley válida sobre la materia ($\frac{d}{dt}\!\int_{V(t)}\phi\,dV=\dots$) y la reescribe con campos eulerianos integrables sobre cualquier región. (Para un volumen de control fijo, el término de la frontera móvil $\vec v\cdot\hat n$ se reinterpreta como flujo a través de fronteras quietas; el de Reynolds, con frontera móvil a $\vec v$, es el caso material.)

---

## En qué consiste

Las leyes fundamentales de la física —conservación de masa, de cantidad de movimiento, de energía— se enuncian de forma natural **sobre la materia**: "la masa de *esta* porción de fluido no cambia", "la tasa de cambio del momento de *esta* porción es igual a la fuerza sobre ella". Eso es lenguaje **lagrangiano**, escrito sobre un **volumen material** $V(t)$ que se mueve y deforma arrastrado por el propio fluido. Pero la mecánica de fluidos trabaja con **campos eulerianos** $\phi(\vec x,t)$ definidos sobre puntos fijos del espacio. El teorema del transporte de Reynolds es la máquina que traduce de un lenguaje al otro.

El problema técnico es que derivar $\dfrac{d}{dt}\int_{V(t)}\phi\,dV$ no es derivar bajo el signo integral: el **dominio mismo cambia con el tiempo**. La idea de la demostración es separar limpiamente las dos razones por las que esa integral cambia. Primera, que el campo $\phi$ evoluciona **dentro** del volumen: aunque congelásemos las fronteras, $\int\partial_t\phi\,dV$ ya sería distinto de cero. Segunda, que la frontera **se mueve** y barre volumen nuevo: cada trozo de superficie $dA$ avanza $\vec v\,\Delta t$ e incorpora (o expulsa) material, lo que aporta el flujo $\oint\phi\,(\vec v\cdot\hat n)\,dA$. La suma de ambas es la forma integral del teorema.

A partir de ahí, el **teorema de la divergencia** convierte ese flujo de frontera en una integral de volumen, dando la forma diferencial $\int_V[\partial_t\phi+\nabla\cdot(\phi\vec v)]\,dV$; y reagrupando con la derivada material se obtiene $\int_V[\frac{D\phi}{Dt}+\phi\,\nabla\cdot\vec v]\,dV$, que distingue el cambio "siguiendo a la partícula" del cambio "por dilatación del volumen". La potencia del teorema está en lo que viene después: como la igualdad vale para **cualquier** volumen material, el **argumento del volumen arbitrario** permite borrar las integrales y quedarse con ecuaciones **diferenciales de campo**. Con $\phi=\rho$ sale la continuidad; ese mismo mecanismo, aplicado al momento y a la energía, genera el resto de las [[3 Ecuaciones de Conservacion/index | Ecuaciones de Conservación]]. Es, en una sola identidad, el motor que convierte la física de la materia en las ecuaciones de la dinámica de fluidos.

---

## Resumen

> [!resumen] Lo esencial
> | Concepto | Expresión | Lectura |
> |:---|:---|:---|
> | Forma integral | $\dfrac{d}{dt}\!\int_{V(t)}\phi\,dV=\int_V\partial_t\phi\,dV+\oint_S\phi(\vec v\cdot\hat n)\,dA$ | cambio local $+$ flujo por la frontera móvil |
> | Forma diferencial | $=\int_V\big[\partial_t\phi+\nabla\cdot(\phi\vec v)\big]\,dV$ | vía teorema de la divergencia |
> | Forma material | $=\int_V\big[\tfrac{D\phi}{Dt}+\phi\,\nabla\cdot\vec v\big]\,dV$ | "seguir la partícula" $+$ dilatación |
> | Volumen material | $V(t)$, frontera a velocidad $\vec v$ | mismas partículas; mirada lagrangiana |
> | Volumen de control | $V_0$ fijo | el fluido lo atraviesa; mirada euleriana |
> | Continuidad ($\phi=\rho$) | $\partial_t\rho+\nabla\cdot(\rho\vec v)=0$ | masa material constante $\Rightarrow$ primer fruto |
> | Incompresible | $\nabla\cdot\vec v=0$ | el volumen material se conserva |

> [!corolario] Idea para recordar
> Reynolds es la **regla de Leibniz para dominios que se mueven con el fluido**: el cambio de $\int_{V(t)}\phi\,dV$ es lo que cambia $\phi$ **dentro** más lo que la frontera **deja entrar/salir**. Combinado con el **argumento del volumen arbitrario**, transforma las leyes de conservación lagrangianas en las ecuaciones diferenciales eulerianas del fluido —empezando por la ecuación de continuidad.

> [!referencia]
> Landau-Lifshitz, Vol. 6 (*Mecánica de Fluidos*), §1 — deduce la continuidad a partir del balance de masa sobre un volumen. Batchelor, *An Introduction to Fluid Dynamics*, cap. 2 (§2.2) — teorema del transporte y derivación de las ecuaciones de conservación.
