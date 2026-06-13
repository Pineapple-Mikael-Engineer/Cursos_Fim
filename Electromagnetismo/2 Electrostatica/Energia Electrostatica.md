---
title: Energía Electrostática
tags:
  - electromagnetismo
  - teoria
  - electrostatica
draft: false
aliases:
  - Energía electrostática
  - Energía del campo eléctrico
---

# Energía Electrostática $W=\dfrac{\varepsilon_0}{2}\displaystyle\int E^2\,dV$

---

> [!definicion] Energía electrostática
> La **energía electrostática** $W$ de una configuración de cargas es el trabajo que cuesta ensamblarla, trayendo cada carga desde el infinito (donde no interactúan) hasta su posición final, venciendo las fuerzas eléctricas de las cargas ya colocadas. Para un conjunto de cargas puntuales,
> $$W=\frac{1}{4\pi\varepsilon_0}\sum_{i<j}\frac{q_i\,q_j}{r_{ij}}=\frac12\sum_i q_i\,V_i,$$
> donde $V_i$ es el potencial creado en la posición de $q_i$ por **todas las demás** cargas. En el límite continuo, con densidad $\rho$ y potencial $V$,
> $$W=\frac12\int\rho\,V\,d^3r.$$
> Esta misma energía puede atribuirse al **campo** que llena el espacio, con densidad de energía $u=\tfrac{\varepsilon_0}{2}E^2$:
> $$\boxed{\;W=\frac{\varepsilon_0}{2}\int E^2\,dV\;}$$

---

> [!info] Ubicación en el curso
> Esta nota pertenece al curso de **Electromagnetismo**, sección [[2 Electrostatica/index | Electrostática]]. Se apoya directamente en el [[Potencial Electrico | potencial eléctrico]] $V$ (la energía es trabajo $=$ carga $\times$ potencial) y prepara el estudio de [[Conductores]] (energía almacenada en un sistema de conductores y condensadores). El paso de $\rho$ al campo usa la divergencia de la [[Ley de Gauss | ley de Gauss]] en forma diferencial. Referencia principal: **Griffiths, *Introduction to Electrodynamics*, cap. 2**.

---

## Ejemplo

> [!ejemplo] Energía de una esfera uniformemente cargada
> Una esfera de radio $R$ tiene carga total $Q$ repartida **uniformemente** en su volumen (densidad $\rho=\dfrac{Q}{\frac43\pi R^{3}}$). Calcular la energía electrostática almacenada por el **método del campo**, integrando $u=\tfrac{\varepsilon_0}{2}E^2$ en todo el espacio.

> [!solucion]
> **Paso 1 — Campo dentro y fuera.** Por la [[Ley de Gauss | ley de Gauss]] con simetría esférica, el campo es radial y vale (encerrando carga $Q_{\text{enc}}$ en una esfera de radio $r$):
> $$E(r)=\frac{1}{4\pi\varepsilon_0}\frac{Q}{R^{3}}\,r\quad(r\le R),\qquad E(r)=\frac{1}{4\pi\varepsilon_0}\frac{Q}{r^{2}}\quad(r\ge R).$$
> Dentro, $Q_{\text{enc}}=Q\,(r/R)^3$ da el crecimiento lineal $E\propto r$; fuera, toda la carga actúa como puntual, $E\propto 1/r^2$.
>
> **Paso 2 — Densidad de energía e integración por capas.** Con simetría esférica $dV=4\pi r^{2}\,dr$, de modo que
> $$W=\frac{\varepsilon_0}{2}\int_0^{\infty} E^2\,4\pi r^{2}\,dr=2\pi\varepsilon_0\int_0^{\infty}E^2\,r^{2}\,dr.$$
>
> **Paso 3 — Contribución interior $(0\le r\le R)$.** Sustituyendo $E=\dfrac{1}{4\pi\varepsilon_0}\dfrac{Q}{R^{3}}r$,
> $$W_{\text{int}}=2\pi\varepsilon_0\int_0^{R}\left(\frac{1}{4\pi\varepsilon_0}\frac{Q}{R^{3}}\right)^{2}r^{2}\cdot r^{2}\,dr=2\pi\varepsilon_0\,\frac{Q^2}{16\pi^2\varepsilon_0^2 R^{6}}\int_0^{R}r^{4}\,dr.$$
> Como $\displaystyle\int_0^{R}r^4\,dr=\frac{R^5}{5}$,
> $$W_{\text{int}}=\frac{Q^2}{8\pi\varepsilon_0 R^{6}}\cdot\frac{R^5}{5}=\frac{1}{4\pi\varepsilon_0}\frac{Q^2}{R}\cdot\frac{1}{10}.$$
>
> **Paso 4 — Contribución exterior $(r\ge R)$.** Con $E=\dfrac{1}{4\pi\varepsilon_0}\dfrac{Q}{r^{2}}$,
> $$W_{\text{ext}}=2\pi\varepsilon_0\int_R^{\infty}\left(\frac{1}{4\pi\varepsilon_0}\frac{Q}{r^{2}}\right)^{2}r^{2}\,dr=2\pi\varepsilon_0\,\frac{Q^2}{16\pi^2\varepsilon_0^2}\int_R^{\infty}\frac{dr}{r^{2}}.$$
> Como $\displaystyle\int_R^{\infty}\frac{dr}{r^2}=\frac{1}{R}$,
> $$W_{\text{ext}}=\frac{Q^2}{8\pi\varepsilon_0}\cdot\frac{1}{R}=\frac{1}{4\pi\varepsilon_0}\frac{Q^2}{R}\cdot\frac{1}{2}.$$
>
> **Paso 5 — Suma.** Sumando interior y exterior,
> $$W=\frac{1}{4\pi\varepsilon_0}\frac{Q^2}{R}\left(\frac{1}{10}+\frac{1}{2}\right)=\frac{1}{4\pi\varepsilon_0}\frac{Q^2}{R}\cdot\frac{6}{10},$$
> $$\boxed{\;W=\frac{3}{5}\,\frac{1}{4\pi\varepsilon_0}\frac{Q^2}{R}\;}$$
> El campo exterior, aunque ocupa una región infinita, almacena la mayor parte ($5/6$) de la energía; el interior aporta solo $1/6$. $\blacksquare$

---

## En qué consiste

La energía electrostática es el **coste energético de tener cargas juntas**. Dos preguntas equivalentes la responden: ¿cuánto trabajo costó traer las cargas desde el infinito? (visión de partículas) y ¿cuánta energía hay guardada en el campo que ahora llena el espacio? (visión de campo). Ambas dan el mismo número para distribuciones extensas, pero **localizan** la energía de forma distinta.

![[energia_ensamblaje.svg|460]]
*Ensamblaje de una configuración trayendo las cargas una a una desde el infinito: cada nueva carga hace trabajo contra el potencial de las ya presentes. El total es $W=\frac12\sum_i q_iV_i=\frac{\varepsilon_0}{2}\int E^2\,dV$.*

> [!demostracion] Energía de cargas puntuales y el factor $\tfrac12$
> **Paso 1 — Ensamblaje carga a carga.** Traer la primera carga $q_1$ al espacio vacío no cuesta trabajo: $W_1=0$. Para traer $q_2$ desde el infinito hasta su sitio, trabajamos contra el potencial $V_{12}$ que $q_1$ crea allí:
> $$W_2=q_2\,V_{12}=\frac{1}{4\pi\varepsilon_0}\frac{q_1 q_2}{r_{12}}.$$
> Al traer $q_3$ trabajamos contra el potencial de $q_1$ **y** $q_2$:
> $$W_3=q_3\big(V_{13}+V_{23}\big)=\frac{1}{4\pi\varepsilon_0}\left(\frac{q_1 q_3}{r_{13}}+\frac{q_2 q_3}{r_{23}}\right),$$
> y así sucesivamente.
>
> **Paso 2 — Suma sobre pares.** El trabajo total es la suma, en la que cada **par** $\{i,j\}$ aparece **una sola vez** (cuando la segunda de las dos llega):
> $$W=\frac{1}{4\pi\varepsilon_0}\sum_{i<j}\frac{q_i\,q_j}{r_{ij}}.$$
> La condición $i<j$ garantiza contar cada pareja exactamente una vez. Nota que $W$ no depende del orden de ensamblaje (la energía es función de estado).
>
> **Paso 3 — Forma simétrica con potencial.** Reescribimos la suma restringida $\sum_{i<j}$ como media de la suma libre $\sum_{i\ne j}$ (cada par $\{i,j\}$ aparece dos veces, como $(i,j)$ y $(j,i)$):
> $$W=\frac{1}{4\pi\varepsilon_0}\sum_{i<j}\frac{q_iq_j}{r_{ij}}=\frac12\cdot\frac{1}{4\pi\varepsilon_0}\sum_{i\ne j}\frac{q_iq_j}{r_{ij}}.$$
> El factor $\tfrac12$ corrige justamente ese **doble conteo** de pares.
>
> **Paso 4 — Identificar el potencial en cada carga.** Factorizamos $q_i$ y reconocemos que la suma sobre $j\ne i$ es el potencial $V_i$ creado en la posición de $q_i$ por todas las demás:
> $$W=\frac12\sum_i q_i\underbrace{\left(\frac{1}{4\pi\varepsilon_0}\sum_{j\ne i}\frac{q_j}{r_{ij}}\right)}_{\displaystyle V_i}=\frac12\sum_i q_i\,V_i.$$
> Se excluye $j=i$: la carga **no** contribuye a su propio potencial en este conteo (queda fuera la autoenergía). $\blacksquare$

> [!teorema] Energía de una distribución continua
> Para una densidad volumétrica de carga $\rho(\vec r\,)$ con su potencial $V(\vec r\,)$, la suma discreta $\tfrac12\sum_i q_i V_i$ se convierte en
> $$W=\frac12\int\rho\,V\,d^3r,$$
> extendida a la región donde $\rho\ne0$ (o, equivalentemente, a todo el espacio, donde $\rho=0$ no aporta).

> [!demostracion] Energía en el campo: $W=\dfrac{\varepsilon_0}{2}\displaystyle\int E^2\,dV$
> Partimos de $W=\dfrac12\displaystyle\int\rho\,V\,dV$ y eliminamos $\rho$ a favor del campo.
>
> **Paso 1 — Sustituir $\rho$ por la divergencia del campo.** La [[Ley de Gauss | ley de Gauss]] diferencial dice $\nabla\cdot\vec E=\rho/\varepsilon_0$, es decir $\rho=\varepsilon_0\,\nabla\cdot\vec E$. Entonces
> $$W=\frac12\int\rho\,V\,dV=\frac{\varepsilon_0}{2}\int(\nabla\cdot\vec E)\,V\,dV.$$
>
> **Paso 2 — Identidad del producto.** Para un escalar $V$ y un vector $\vec E$ vale la regla
> $$\nabla\cdot(V\vec E)=V\,(\nabla\cdot\vec E)+\vec E\cdot(\nabla V),$$
> de donde despejamos el integrando:
> $$V\,(\nabla\cdot\vec E)=\nabla\cdot(V\vec E)-\vec E\cdot\nabla V.$$
>
> **Paso 3 — Integrar por partes.** Sustituyendo,
> $$W=\frac{\varepsilon_0}{2}\int\Big[\nabla\cdot(V\vec E)-\vec E\cdot\nabla V\Big]\,dV=\frac{\varepsilon_0}{2}\left[\int\nabla\cdot(V\vec E)\,dV-\int\vec E\cdot\nabla V\,dV\right].$$
> Por el **teorema de la divergencia**, la primera integral se convierte en flujo a través de la superficie $S$ que encierra el volumen:
> $$\int_{\mathcal V}\nabla\cdot(V\vec E)\,dV=\oint_S V\,\vec E\cdot d\vec A,$$
> de modo que
> $$W=\frac{\varepsilon_0}{2}\left[\oint_S V\,\vec E\cdot d\vec A-\int\vec E\cdot\nabla V\,dV\right].$$
>
> **Paso 4 — Usar $\nabla V=-\vec E$.** Como el campo deriva del potencial ([[Potencial Electrico]]), $\vec E=-\nabla V$, luego $\nabla V=-\vec E$ y $\vec E\cdot\nabla V=-E^{2}$:
> $$W=\frac{\varepsilon_0}{2}\left[\oint_S V\,\vec E\cdot d\vec A+\int E^{2}\,dV\right].$$
>
> **Paso 5 — Extender a todo el espacio: el término de superficie se anula.** La energía no cambia si integramos sobre una región mayor (donde $\rho=0$ no aporta). Tomamos $S$ como una esfera de radio $r\to\infty$. Para una distribución acotada, lejos $V\sim 1/r$ y $E\sim 1/r^{2}$, mientras el área crece $S\sim r^{2}$:
> $$\oint_S V\,\vec E\cdot d\vec A\ \sim\ \frac1r\cdot\frac{1}{r^{2}}\cdot r^{2}=\frac1r\ \xrightarrow[r\to\infty]{}\ 0.$$
> El integrando del flujo decae como $1/r$, así que la integral de superficie tiende a cero. Queda solo el término de volumen, extendido a **todo el espacio**:
> $$\boxed{\;W=\frac{\varepsilon_0}{2}\int_{\text{todo el espacio}} E^{2}\,dV\;},\qquad u=\frac{\varepsilon_0}{2}E^{2}\ \text{(densidad de energía)}.$$
> La energía queda **localizada en el campo**, con densidad $u=\tfrac{\varepsilon_0}{2}E^2$ por unidad de volumen, allí donde haya campo. $\blacksquare$

> [!warning] Autoenergía y divergencia de la carga puntual
> Las dos expresiones de la energía **no son idénticas** para cargas puntuales. La forma $\tfrac12\sum_i q_iV_i$ **excluye** la autointeracción de cada carga consigo misma, mientras que $\tfrac{\varepsilon_0}{2}\int E^2\,dV$ la **incluye**. Esa diferencia es la **energía propia** de cada carga puntual, que **diverge**: el campo de una carga puntual $E\sim 1/r^2$ hace que
> $$\frac{\varepsilon_0}{2}\int E^2\,dV\ \sim\ \int_0^{R}\frac{1}{r^{4}}\,r^{2}\,dr=\int_0^{R}\frac{dr}{r^{2}}\ \xrightarrow[R\to0]{}\ \infty.$$
> La fórmula del campo $\tfrac{\varepsilon_0}{2}\int E^2$ es siempre **positiva** (integral de un cuadrado); la suma de pares puede ser negativa (cargas opuestas se atraen). Para distribuciones **continuas** acotadas no hay paradoja: la autoenergía es finita y ambas visiones coinciden numéricamente. El problema es exclusivo de la idealización puntual; su tratamiento riguroso aparece en [[Ley de Coulomb y Campo Electrico]] y [[Delta de Dirac y Singularidades]].

---

## Resumen

> [!resumen] Fórmulas clave
> | Concepto | Expresión | Notas |
> |---|---|---|
> | Cargas puntuales (pares) | $W=\dfrac{1}{4\pi\varepsilon_0}\displaystyle\sum_{i<j}\dfrac{q_iq_j}{r_{ij}}$ | excluye autoenergía |
> | Forma con potencial | $W=\dfrac12\displaystyle\sum_i q_i V_i$ | el $\tfrac12$ corrige doble conteo |
> | Distribución continua | $W=\dfrac12\displaystyle\int\rho\,V\,d^3r$ | límite continuo |
> | Energía en el campo | $W=\dfrac{\varepsilon_0}{2}\displaystyle\int E^2\,dV$ | siempre $\ge 0$ |
> | Densidad de energía | $u=\dfrac{\varepsilon_0}{2}E^2$ | energía por unidad de volumen |
> | Esfera uniforme $Q,R$ | $W=\dfrac{3}{5}\dfrac{1}{4\pi\varepsilon_0}\dfrac{Q^2}{R}$ | $5/6$ en el campo exterior |

> [!corolario] Ideas para recordar
> - La energía electrostática es **trabajo de ensamblaje**: $W=\tfrac12\sum q_iV_i$, con el $\tfrac12$ por contar cada par una sola vez.
> - La integración por partes con $\rho=\varepsilon_0\nabla\cdot\vec E$ y $\vec E=-\nabla V$ traslada la energía **de las cargas al campo**: $W=\tfrac{\varepsilon_0}{2}\int E^2\,dV$, con densidad $u=\tfrac{\varepsilon_0}{2}E^2$.
> - La forma del campo es **siempre positiva** e incluye la autoenergía; la de pares puede ser negativa y la excluye. Para una carga puntual ideal la autoenergía **diverge**.

> [!referencia] Fuentes
> - **D. J. Griffiths**, *Introduction to Electrodynamics*, 4.ª ed., cap. 2 (Trabajo y energía en electrostática).
> - **J. D. Jackson**, *Classical Electrodynamics*, cap. 1.
> - Notas relacionadas: [[Potencial Electrico]], [[Conductores]], [[Ley de Coulomb y Campo Electrico]], [[Ley de Gauss]], [[2 Electrostatica/index | Electrostática]].
