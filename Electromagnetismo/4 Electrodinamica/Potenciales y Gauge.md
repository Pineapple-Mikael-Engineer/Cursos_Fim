---
title: Potenciales y Gauge
tags:
  - electromagnetismo
  - teoria
  - electrodinamica
draft: false
aliases:
  - Potenciales electromagnéticos
  - Gauge de Lorenz
  - Invariancia de gauge
---

# Potenciales y Gauge $\vec E=-\nabla V-\partial_t\vec A,\quad \vec B=\nabla\times\vec A$

> [!definicion]
> Los **potenciales electromagnéticos** son un campo escalar $V(\vec r,t)$ y un campo vectorial $\vec A(\vec r,t)$ a partir de los cuales se construyen los campos físicos:
> $$\boxed{\;\vec B=\nabla\times\vec A,\qquad \vec E=-\nabla V-\frac{\partial\vec A}{\partial t}\;}$$
> Con ellos, **dos** de las cuatro ecuaciones de Maxwell ($\nabla\cdot\vec B=0$ y $\nabla\times\vec E=-\partial_t\vec B$) quedan satisfechas **automáticamente**, y el problema entero se reduce a hallar $V$ y $\vec A$. La elección de $(V,\vec A)$ **no es única**: dos pares distintos pueden dar el mismo $(\vec E,\vec B)$. A esa libertad se la llama **libertad de gauge**.

---

> [!info]
> **Nota de la sección [[4 Electrodinamica/index | Electrodinámica]].** Sus hermanas son [[Ecuaciones de Maxwell]] (las cuatro leyes que aquí reescribimos) y [[Energia y Momento]] (Poynting, momento del campo). La construcción de $\vec A$ ya se discutió en estática en [[Potencial Vector]]; el álgebra usa el desarrollo BAC–CAB y demás de [[Identidades Vectoriales]].
> **Referencia.** Griffiths, *Introduction to Electrodynamics*, cap. 10 (formulación con potenciales) y cap. 7 (electrodinámica). Operador d'Alembertiano: $\Box=\nabla^2-\dfrac{1}{c^2}\partial_t^2$, con $c^2=1/(\mu_0\varepsilon_0)$.

---

## En qué consiste

La idea es cambiar de **incógnitas**. En lugar de resolver para los seis campos $\vec E,\vec B$ atados por las cuatro ecuaciones de Maxwell, se introducen $V$ (un escalar) y $\vec A$ (un vector) —cuatro funciones— de modo que **dos** de las ecuaciones se cumplan por construcción. Las dos restantes (Gauss eléctrica y Ampère–Maxwell) se convierten en ecuaciones para $V$ y $\vec A$.

El precio es una **redundancia**: hay infinitos pares $(V,\vec A)$ que producen los mismos $(\vec E,\vec B)$. Lejos de ser un defecto, esa redundancia es una herramienta. Eligiendo bien —**fijando un gauge**— las ecuaciones se simplifican drásticamente. El gauge de **Lorenz** las vuelve dos ecuaciones de onda independientes; el gauge de **Coulomb** convierte a $V$ en un Poisson instantáneo.

![[gauge.svg|460]]
*Los campos medibles $\vec E,\vec B$ se **derivan** de los potenciales $V,\vec A$. Una transformación de gauge mueve $(V,\vec A)$ a lo largo de la fibra punteada sin alterar $(\vec E,\vec B)$: por eso los potenciales no son únicos, pero los campos sí.*

---

## Las dos ecuaciones que se cumplen solas

> [!proposicion] $\vec B$ desde un potencial vector
> Como **siempre** $\nabla\cdot\vec B=0$ (no hay monopolos), $\vec B$ es solenoidal y admite un potencial vector:
> $$\vec B=\nabla\times\vec A.$$
> En efecto, $\nabla\cdot(\nabla\times\vec A)=0$ es una identidad ([[Identidades Vectoriales]]), así que $\nabla\cdot\vec B=0$ queda garantizado para **cualquier** $\vec A$. Ver [[Potencial Vector]].

> [!demostracion] Existencia del potencial escalar $V$
> Buscamos reescribir $\vec E$ usando que $\nabla\times\vec E=-\partial_t\vec B$ (Faraday).
>
> **Paso 1 — Sustituir $\vec B=\nabla\times\vec A$ en Faraday.**
> $$\nabla\times\vec E=-\frac{\partial}{\partial t}\bigl(\nabla\times\vec A\bigr).$$
>
> **Paso 2 — Conmutar $\partial_t$ con $\nabla\times$.** Las derivadas espaciales y la temporal conmutan, luego $\partial_t(\nabla\times\vec A)=\nabla\times(\partial_t\vec A)$. Pasando todo a un lado:
> $$\nabla\times\vec E+\nabla\times\frac{\partial\vec A}{\partial t}=0\ \Longrightarrow\ \nabla\times\!\left(\vec E+\frac{\partial\vec A}{\partial t}\right)=0.$$
>
> **Paso 3 — Un rotacional nulo es un gradiente.** Todo campo irrotacional deriva de un potencial escalar ([[Identidades Vectoriales]]): existe $V$ tal que
> $$\vec E+\frac{\partial\vec A}{\partial t}=-\nabla V,$$
> donde el signo menos es convención (recupera $\vec E=-\nabla V$ en estática). Despejando:
> $$\boxed{\;\vec E=-\nabla V-\frac{\partial\vec A}{\partial t}\;}$$
> Así, **Faraday** queda satisfecha por construcción para todo $V,\vec A$. $\blacksquare$

Con esto, $\nabla\cdot\vec B=0$ y $\nabla\times\vec E=-\partial_t\vec B$ ya no son ecuaciones a resolver: son **identidades**. Sólo quedan las dos con fuentes.

---

## Las dos ecuaciones dinámicas en términos de potenciales

> [!teorema] Maxwell en $(V,\vec A)$
> Insertando $\vec E=-\nabla V-\partial_t\vec A$ y $\vec B=\nabla\times\vec A$ en las dos ecuaciones con fuente se obtiene el par **acoplado**
> $$\nabla^2 V+\frac{\partial}{\partial t}\bigl(\nabla\cdot\vec A\bigr)=-\frac{\rho}{\varepsilon_0},$$
> $$\nabla^2\vec A-\frac{1}{c^2}\frac{\partial^2\vec A}{\partial t^2}-\nabla\!\left(\nabla\cdot\vec A+\frac{1}{c^2}\frac{\partial V}{\partial t}\right)=-\mu_0\vec J.$$

> [!demostracion] Ecuación para $V$ (desde Gauss eléctrica)
> **Paso 1 — Partir de $\nabla\cdot\vec E=\rho/\varepsilon_0$** y sustituir $\vec E$:
> $$\nabla\cdot\!\left(-\nabla V-\frac{\partial\vec A}{\partial t}\right)=\frac{\rho}{\varepsilon_0}.$$
>
> **Paso 2 — Distribuir la divergencia.** Usando $\nabla\cdot(\nabla V)=\nabla^2 V$ y conmutando $\nabla\cdot$ con $\partial_t$:
> $$-\nabla^2 V-\frac{\partial}{\partial t}\bigl(\nabla\cdot\vec A\bigr)=\frac{\rho}{\varepsilon_0}.$$
>
> **Paso 3 — Cambiar de signo:**
> $$\nabla^2 V+\frac{\partial}{\partial t}\bigl(\nabla\cdot\vec A\bigr)=-\frac{\rho}{\varepsilon_0}.\qquad\blacksquare$$

> [!demostracion] Ecuación para $\vec A$ (desde Ampère–Maxwell)
> **Paso 1 — Partir de $\nabla\times\vec B=\mu_0\vec J+\mu_0\varepsilon_0\,\partial_t\vec E$** y sustituir $\vec B=\nabla\times\vec A$, $\vec E=-\nabla V-\partial_t\vec A$:
> $$\nabla\times(\nabla\times\vec A)=\mu_0\vec J+\mu_0\varepsilon_0\frac{\partial}{\partial t}\!\left(-\nabla V-\frac{\partial\vec A}{\partial t}\right).$$
>
> **Paso 2 — Desarrollar el doble rotacional con BAC–CAB.** La identidad $\nabla\times(\nabla\times\vec A)=\nabla(\nabla\cdot\vec A)-\nabla^2\vec A$ ([[Identidades Vectoriales]]) da en el lado izquierdo:
> $$\nabla(\nabla\cdot\vec A)-\nabla^2\vec A.$$
>
> **Paso 3 — Desarrollar el lado derecho.** Con $\mu_0\varepsilon_0=1/c^2$:
> $$\mu_0\vec J-\frac{1}{c^2}\nabla\frac{\partial V}{\partial t}-\frac{1}{c^2}\frac{\partial^2\vec A}{\partial t^2}.$$
>
> **Paso 4 — Igualar y agrupar.** Llevando todos los términos en $\vec A$ y $V$ a la izquierda:
> $$\nabla(\nabla\cdot\vec A)-\nabla^2\vec A+\frac{1}{c^2}\nabla\frac{\partial V}{\partial t}+\frac{1}{c^2}\frac{\partial^2\vec A}{\partial t^2}=\mu_0\vec J.$$
>
> **Paso 5 — Reordenar** aislando el término de onda $\nabla^2\vec A-\tfrac{1}{c^2}\partial_t^2\vec A$ y juntando los dos gradientes:
> $$\nabla^2\vec A-\frac{1}{c^2}\frac{\partial^2\vec A}{\partial t^2}-\nabla\!\left(\nabla\cdot\vec A+\frac{1}{c^2}\frac{\partial V}{\partial t}\right)=-\mu_0\vec J.\qquad\blacksquare$$

Las dos ecuaciones están **acopladas**: en la de $V$ aparece $\nabla\cdot\vec A$, y en la de $\vec A$ aparece $V$. El término molesto en ambas es justamente la combinación
$$\nabla\cdot\vec A+\frac{1}{c^2}\frac{\partial V}{\partial t}.$$
Si pudiéramos anularla, las ecuaciones se separarían. Aquí entra la libertad de gauge.

---

## Libertad de gauge

> [!teorema] Transformación de gauge
> Los campos $\vec E$ y $\vec B$ son **invariantes** bajo la transformación
> $$\vec A\ \longrightarrow\ \vec A\,'=\vec A+\nabla\lambda,\qquad V\ \longrightarrow\ V'=V-\frac{\partial\lambda}{\partial t},$$
> para **cualquier** función escalar $\lambda(\vec r,t)$.

> [!demostracion] Invariancia de $\vec B$ y de $\vec E$
> **Paso 1 — Verificar $\vec B$.** El nuevo campo magnético es
> $$\vec B'=\nabla\times\vec A\,'=\nabla\times(\vec A+\nabla\lambda)=\nabla\times\vec A+\nabla\times(\nabla\lambda).$$
> Pero $\nabla\times(\nabla\lambda)=0$ (el rotacional de un gradiente es nulo, [[Identidades Vectoriales]]), así que
> $$\vec B'=\nabla\times\vec A=\vec B.$$
>
> **Paso 2 — Verificar $\vec E$.** El nuevo campo eléctrico es
> $$\vec E'=-\nabla V'-\frac{\partial\vec A\,'}{\partial t}=-\nabla\!\left(V-\frac{\partial\lambda}{\partial t}\right)-\frac{\partial}{\partial t}\bigl(\vec A+\nabla\lambda\bigr).$$
>
> **Paso 3 — Distribuir y cancelar.**
> $$\vec E'=-\nabla V+\nabla\frac{\partial\lambda}{\partial t}-\frac{\partial\vec A}{\partial t}-\frac{\partial}{\partial t}\nabla\lambda.$$
> Los términos $\nabla\partial_t\lambda$ y $\partial_t\nabla\lambda$ son iguales (las derivadas conmutan) y de signo opuesto: se **cancelan**. Queda
> $$\vec E'=-\nabla V-\frac{\partial\vec A}{\partial t}=\vec E.$$
> Ambos campos quedan intactos. $\blacksquare$

La función $\lambda$ es completamente libre: es la "perilla" que mueve $(V,\vec A)$ sobre la fibra de la figura sin tocar la física. **Fijar el gauge** es elegir $\lambda$ (o una condición sobre $V,\vec A$) que simplifique las ecuaciones.

---

## Gauge de Lorenz: las ecuaciones se desacoplan

> [!definicion] Condición de Lorenz
> Se llama **gauge de Lorenz** a la elección de potenciales que satisfacen
> $$\boxed{\;\nabla\cdot\vec A+\frac{1}{c^2}\frac{\partial V}{\partial t}=0\;}$$
> Es precisamente la combinación que aparecía como término de acoplamiento. Siempre puede alcanzarse: dado un par cualquiera, una $\lambda$ que resuelva $\Box\lambda=-\bigl(\nabla\cdot\vec A+\tfrac{1}{c^2}\partial_t V\bigr)$ lleva al nuevo par a cumplir la condición.

> [!teorema] Ecuaciones de onda con fuente
> En el gauge de Lorenz, los potenciales obedecen **dos ecuaciones de onda independientes y simétricas**:
> $$\boxed{\;\Box V=-\frac{\rho}{\varepsilon_0},\qquad \Box\vec A=-\mu_0\vec J\;},\qquad \Box=\nabla^2-\frac{1}{c^2}\frac{\partial^2}{\partial t^2}.$$

> [!demostracion] Desacoplamiento
> **Paso 1 — Ecuación de $\vec A$.** En la dinámica de $\vec A$, el paréntesis es exactamente la condición de Lorenz, que se **anula**:
> $$\nabla^2\vec A-\frac{1}{c^2}\frac{\partial^2\vec A}{\partial t^2}-\nabla\underbrace{\left(\nabla\cdot\vec A+\frac{1}{c^2}\frac{\partial V}{\partial t}\right)}_{=\,0}=-\mu_0\vec J\ \Longrightarrow\ \Box\vec A=-\mu_0\vec J.$$
>
> **Paso 2 — Ecuación de $V$.** En la dinámica de $V$ aparece $\partial_t(\nabla\cdot\vec A)$. Usando Lorenz, $\nabla\cdot\vec A=-\tfrac{1}{c^2}\partial_t V$, luego
> $$\frac{\partial}{\partial t}(\nabla\cdot\vec A)=-\frac{1}{c^2}\frac{\partial^2 V}{\partial t^2}.$$
> Sustituyendo en $\nabla^2 V+\partial_t(\nabla\cdot\vec A)=-\rho/\varepsilon_0$:
> $$\nabla^2 V-\frac{1}{c^2}\frac{\partial^2 V}{\partial t^2}=-\frac{\rho}{\varepsilon_0}\ \Longrightarrow\ \Box V=-\frac{\rho}{\varepsilon_0}.$$
>
> **Paso 3 — Lectura.** $V$ depende sólo de $\rho$ y $\vec A$ sólo de $\vec J$: el sistema **se separó**. Además ambas tienen la **misma** forma —una onda que viaja a $c$ con un término fuente—, lo que exhibe la simetría profunda entre carga y corriente. $\blacksquare$

> [!regla] Gauge de Coulomb (alternativa)
> Otra elección común es el **gauge de Coulomb** $\nabla\cdot\vec A=0$. Entonces la ecuación de $V$ se reduce a $\nabla^2 V=-\rho/\varepsilon_0$ (Poisson **instantáneo**: $V$ se obtiene de $\rho$ como en electrostática, sin retardo), mientras que $\vec A$ conserva un término extra con $\partial_t V$. Es cómodo en problemas sin radiación y en mecánica cuántica; Lorenz, en cambio, es **relativistamente covariante** y natural para la radiación.

---

## Ejemplo

> [!ejemplo] Invariancia de gauge con una $\lambda$ concreta, y Poisson como límite estático
> **(a)** Sea un par de potenciales $(V,\vec A)$ y la función $\lambda=k\,t$ con $k$ constante. La transformación da
> $$\vec A\,'=\vec A+\nabla(kt)=\vec A,\qquad V'=V-\frac{\partial(kt)}{\partial t}=V-k.$$
> Es decir, **sumar una constante al potencial** $V$ es una transformación de gauge.

> [!solucion]
> **Paso 1 — Campo magnético.** Como $\vec A\,'=\vec A$, trivialmente $\vec B'=\nabla\times\vec A\,'=\nabla\times\vec A=\vec B$.
>
> **Paso 2 — Campo eléctrico.** $\vec A$ no cambió y $V$ bajó una constante, cuyo gradiente es cero:
> $$\vec E'=-\nabla(V-k)-\frac{\partial\vec A}{\partial t}=-\nabla V-\frac{\partial\vec A}{\partial t}=\vec E.$$
> Recuperamos el hecho conocido de electrostática: **el cero de potencial es arbitrario**; sólo importan las diferencias. Es el caso más simple de invariancia de gauge.
>
> **(b) Límite estático en gauge de Lorenz.** Si nada depende del tiempo, $\partial_t V=0$ y $\partial_t^2 V=0$, de modo que $\Box V=\nabla^2 V$. La ecuación de Lorenz $\Box V=-\rho/\varepsilon_0$ colapsa a
> $$\nabla^2 V=-\frac{\rho}{\varepsilon_0},$$
> la **ecuación de Poisson** de la [[2 Electrostatica/index | Electrostática]]. La formulación con potenciales **contiene** la estática como caso particular, como debe ser. $\blacksquare$

---

> [!warning] Los potenciales no son únicos
> $V$ y $\vec A$ **no son cantidades físicas medibles** en electrodinámica clásica: dependen del gauge elegido, y dos observadores con gauges distintos asignan potenciales distintos a la misma situación. Sólo $\vec E$ y $\vec B$ —invariantes de gauge— son medibles. Elegir un gauge no es física, es comodidad de cálculo. Esta **invariancia de gauge** no es un mero truco: reaparece como el principio organizador de las teorías de campo modernas (electrodinámica cuántica y el modelo estándar), donde la simetría de gauge **dicta** la forma de las interacciones.

---

## Resumen

> [!resumen]
> | Objeto | Expresión | Comentario |
> |---|---|---|
> | Campos desde potenciales | $\vec B=\nabla\times\vec A,\ \ \vec E=-\nabla V-\partial_t\vec A$ | satisface $\nabla\cdot\vec B=0$ y Faraday por construcción |
> | Ecuación de $V$ (general) | $\nabla^2 V+\partial_t(\nabla\cdot\vec A)=-\rho/\varepsilon_0$ | desde Gauss eléctrica |
> | Ecuación de $\vec A$ (general) | $\nabla^2\vec A-\tfrac{1}{c^2}\partial_t^2\vec A-\nabla\!\bigl(\nabla\cdot\vec A+\tfrac{1}{c^2}\partial_t V\bigr)=-\mu_0\vec J$ | desde Ampère–Maxwell (BAC–CAB) |
> | Transformación de gauge | $\vec A\to\vec A+\nabla\lambda,\ \ V\to V-\partial_t\lambda$ | deja $\vec E,\vec B$ invariantes |
> | Gauge de Lorenz | $\nabla\cdot\vec A+\tfrac{1}{c^2}\partial_t V=0$ | desacopla: $\Box V=-\rho/\varepsilon_0,\ \Box\vec A=-\mu_0\vec J$ |
> | Gauge de Coulomb | $\nabla\cdot\vec A=0$ | $\nabla^2 V=-\rho/\varepsilon_0$ (Poisson instantáneo) |

> [!corolario]
> Introducir $V,\vec A$ reduce las cuatro ecuaciones de Maxwell a **dos** —y, en el gauge de Lorenz, a dos ecuaciones de onda **simétricas** $\Box V=-\rho/\varepsilon_0$, $\Box\vec A=-\mu_0\vec J$. La libertad de gauge es la redundancia que lo permite; los potenciales no son medibles, pero su invariancia de gauge es el germen de la física de partículas moderna.

> [!referencia]
> - Griffiths, *Introduction to Electrodynamics*, cap. 10 (potenciales y gauge) y cap. 7.
> - Hermanas: [[Ecuaciones de Maxwell]], [[Energia y Momento]]. Sección: [[4 Electrodinamica/index | Electrodinámica]].
> - Prerrequisitos: [[Potencial Vector]], [[Identidades Vectoriales]].
