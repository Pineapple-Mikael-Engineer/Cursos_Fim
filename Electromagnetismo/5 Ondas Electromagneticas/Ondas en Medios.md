---
title: Ondas en Medios
tags:
  - electromagnetismo
  - teoria
  - ondas
draft: false
aliases:
  - Ondas en medios
  - Reflexión y refracción
  - Índice de refracción
---

# Ondas en Medios $n=\sqrt{\varepsilon_r\mu_r}\approx\sqrt{\varepsilon_r},\quad v=\dfrac{c}{n}$

> [!definicion]
> Una **onda electromagnética en un medio** es la solución de las ecuaciones de Maxwell cuando el espacio está ocupado por materia lineal, donde $\vec D=\varepsilon\vec E$ y $\vec H=\vec B/\mu$. La onda sigue siendo transversal, pero su velocidad ya no es $c$: vale
> $$v=\frac{1}{\sqrt{\varepsilon\mu}}=\frac{c}{n},\qquad n\equiv\sqrt{\varepsilon_r\mu_r}\approx\sqrt{\varepsilon_r}.$$
> El número $n$ es el **índice de refracción** del medio: dice cuántas veces más lenta va la luz dentro del material que en el vacío. En las **interfaces** entre dos medios la onda se parte en una **reflejada** y una **transmitida (refractada)**, gobernadas por la ley de Snell y los coeficientes de Fresnel.

---

> [!info]
> **Sección del capítulo [[5 Ondas Electromagneticas/index | Ondas Electromagnéticas]].** Aquí dejamos el vacío y mandamos la onda dentro de la materia. Las hermanas de esta sección son [[Ondas Planas]] (la onda libre que ahora hacemos viajar por un dieléctrico) y [[5 Ondas Electromagneticas/Polarizacion | Polarización]] (el estado del campo que decide cuánto se refleja).
> **Apoyos.** La respuesta del medio sale de [[2 Electrostatica/Dielectricos/index | Dieléctricos]] (de ahí $\varepsilon$ y las condiciones de frontera de $\vec D$) y de [[Materiales Magneticos]] (de ahí $\mu$, casi siempre $\approx\mu_0$).
> **Referencia.** Griffiths, *Introduction to Electrodynamics*, cap. 9.

---

## En qué consiste

> [!teoria] El medio solo cambia las constantes
> Las ecuaciones de Maxwell en un medio lineal, homogéneo, sin carga ni corriente libres, son **idénticas** a las del vacío con el cambio $\varepsilon_0\to\varepsilon$, $\mu_0\to\mu$. Por eso **toda** la física de [[Ondas Planas]] se reescribe sin esfuerzo: onda transversal, $\vec E\perp\vec B\perp\vec k$, en fase, con $E=vB$ en vez de $E=cB$. Lo único nuevo y físico es:
> - la onda va **más lenta**, $v=c/n<c$;
> - en una **interfaz** la energía se reparte entre reflexión y refracción.
>
> Todo el capítulo se reduce a entender esas dos cosas.

### Ondas en un dieléctrico lineal

> [!proposicion] Velocidad e índice de refracción
> En un dieléctrico lineal cada componente del campo satisface la ecuación de ondas
> $$\nabla^2\vec E=\varepsilon\mu\,\frac{\partial^2\vec E}{\partial t^2},$$
> de donde la velocidad de propagación es $v=1/\sqrt{\varepsilon\mu}=c/n$ con
> $$n=\sqrt{\varepsilon_r\mu_r}\approx\sqrt{\varepsilon_r}\qquad(\text{pues }\mu_r\approx1).$$

> [!demostracion] De Maxwell en el medio a $v=c/n$
> **Paso 1 — Maxwell en materia.** Sin carga ni corriente libres ($\rho_{\text{lib}}=0$, $\vec J_{\text{lib}}=\vec 0$) y con $\vec D=\varepsilon\vec E$, $\vec H=\vec B/\mu$:
> $$\vec\nabla\cdot\vec E=0,\qquad \vec\nabla\cdot\vec B=0,$$
> $$\vec\nabla\times\vec E=-\frac{\partial\vec B}{\partial t},\qquad \vec\nabla\times\vec B=\varepsilon\mu\,\frac{\partial\vec E}{\partial t}.$$
> Son las de Maxwell del vacío con $\mu_0\varepsilon_0\to\mu\varepsilon$.
>
> **Paso 2 — Desacoplar tomando rotor.** Aplico $\vec\nabla\times$ a Faraday:
> $$\vec\nabla\times(\vec\nabla\times\vec E)=-\frac{\partial}{\partial t}\,(\vec\nabla\times\vec B)=-\varepsilon\mu\,\frac{\partial^2\vec E}{\partial t^2}.$$
>
> **Paso 3 — Identidad BAC–CAB.** Con [[Identidades Vectoriales]],
> $$\vec\nabla\times(\vec\nabla\times\vec E)=\vec\nabla(\underbrace{\vec\nabla\cdot\vec E}_{=\,0})-\nabla^2\vec E=-\nabla^2\vec E.$$
> Igualando con el Paso 2 queda la **ecuación de ondas en el medio**:
> $$\nabla^2\vec E=\varepsilon\mu\,\frac{\partial^2\vec E}{\partial t^2}.$$
>
> **Paso 4 — Leer la velocidad.** La ecuación de ondas $\nabla^2\vec E=\dfrac{1}{v^2}\,\partial_t^2\vec E$ identifica
> $$v=\frac{1}{\sqrt{\varepsilon\mu}}.$$
>
> **Paso 5 — Definir el índice.** Divido por la del vacío $c=1/\sqrt{\varepsilon_0\mu_0}$:
> $$\frac{c}{v}=\sqrt{\frac{\varepsilon\mu}{\varepsilon_0\mu_0}}=\sqrt{\varepsilon_r\mu_r}\;\equiv\;n.$$
> Como casi todos los materiales transparentes son no magnéticos, $\mu_r\approx1$ y $n\approx\sqrt{\varepsilon_r}$. Por tanto $v=c/n$. $\blacksquare$

### Condiciones de frontera

> [!regla] Lo que es continuo al cruzar la interfaz
> De las ecuaciones de Maxwell integradas sobre la interfaz (cajita y espira de Gauss/Ampère–Faraday), sin carga ni corriente **libres** superficiales, los campos cumplen, entre el medio 1 y el medio 2:
>
> | Componente | Condición | Origen |
> \|---\|---\|---\|
> | Tangencial de $\vec E$ | $E_\parallel^{(1)}=E_\parallel^{(2)}$ | $\vec\nabla\times\vec E=-\partial_t\vec B$ |
> | Tangencial de $\vec H$ | $H_\parallel^{(1)}=H_\parallel^{(2)}$ | $\vec\nabla\times\vec H=\partial_t\vec D$ |
> | Normal de $\vec D$ | $D_\perp^{(1)}=D_\perp^{(2)}$ | $\vec\nabla\cdot\vec D=0$ |
> | Normal de $\vec B$ | $B_\perp^{(1)}=B_\perp^{(2)}$ | $\vec\nabla\cdot\vec B=0$ |
>
> Estas son las mismas condiciones de [[2 Electrostatica/Dielectricos/index | Dieléctricos]], ahora aplicadas a campos que oscilan. **Todo** lo que sigue (Snell, Fresnel) sale de imponerlas a las ondas incidente, reflejada y transmitida.

![[reflexion_refraccion.svg|420]]
*Una onda plana incide desde el medio $n_1$ sobre la interfaz con el medio $n_2$. Parte se refleja ($\theta_R=\theta_I$) y parte se refracta hacia el medio 2 con un ángulo $\theta_T$ dado por la ley de Snell $n_1\sin\theta_I=n_2\sin\theta_T$. Los tres rayos y la normal son coplanares.*

### Leyes de la reflexión y de Snell

> [!teorema] Reflexión y refracción
> Cuando una onda plana incide sobre la interfaz entre dos medios:
> 1. los rayos incidente, reflejado y transmitido son **coplanares** (plano de incidencia);
> 2. el ángulo de reflexión iguala al de incidencia, $\theta_I=\theta_R$;
> 3. los ángulos de incidencia y transmisión cumplen la **ley de Snell**
> $$n_1\sin\theta_I=n_2\sin\theta_T.$$

> [!demostracion] Las tres leyes salen de igualar las fases
> **Paso 1 — Las tres ondas.** Sobre la interfaz coexisten
> $$\vec E_I\propto e^{i(\vec k_I\cdot\vec r-\omega t)},\quad \vec E_R\propto e^{i(\vec k_R\cdot\vec r-\omega t)},\quad \vec E_T\propto e^{i(\vec k_T\cdot\vec r-\omega t)}.$$
> La frecuencia $\omega$ es común a las tres: la impone la fuente, no el medio.
>
> **Paso 2 — Las condiciones de frontera valen en todo punto y todo instante.** Las relaciones de continuidad ($E_\parallel$, $H_\parallel$, …) deben cumplirse en **cada** punto $\vec r$ de la interfaz. Una combinación lineal de exponenciales solo puede anularse en todo punto si **todas tienen la misma fase espacial** sobre el plano. Por tanto, para $\vec r$ en la interfaz,
> $$\vec k_I\cdot\vec r=\vec k_R\cdot\vec r=\vec k_T\cdot\vec r.$$
>
> **Paso 3 — Coplanaridad.** Tomemos la normal $\hat n$ a la interfaz y el plano de incidencia el que contiene $\vec k_I$ y $\hat n$. La igualdad $\vec k_I\cdot\vec r=\vec k_R\cdot\vec r$ para todo $\vec r$ del plano obliga a que $(\vec k_I-\vec k_R)$ sea normal a la interfaz; igual con $\vec k_T$. Luego $\vec k_R$ y $\vec k_T$ no tienen componente fuera del plano de incidencia: los tres son **coplanares**.
>
> **Paso 4 — Componentes tangenciales.** Proyectando la igualdad sobre la interfaz, las componentes tangenciales de los tres vectores de onda coinciden:
> $$k_I\sin\theta_I=k_R\sin\theta_R=k_T\sin\theta_T.$$
>
> **Paso 5 — Ley de la reflexión.** Incidente y reflejada viajan en el **mismo** medio 1, así que $|\vec k_I|=|\vec k_R|=k_1=n_1\omega/c$. De $k_1\sin\theta_I=k_1\sin\theta_R$ sale
> $$\boxed{\theta_I=\theta_R.}$$
>
> **Paso 6 — Ley de Snell.** La transmitida viaja en el medio 2, $|\vec k_T|=k_2=n_2\omega/c$. De $k_1\sin\theta_I=k_2\sin\theta_T$, con $k_j=n_j\omega/c$, el factor $\omega/c$ se cancela:
> $$\boxed{n_1\sin\theta_I=n_2\sin\theta_T.}\qquad\blacksquare$$

### Coeficientes de Fresnel (incidencia normal)

> [!teorema] Reflexión y transmisión a incidencia normal
> Para una onda que incide **perpendicularmente** ($\theta_I=0$) sobre la interfaz $n_1\mid n_2$, las amplitudes reflejada y transmitida valen
> $$r=\frac{E_{0R}}{E_{0I}}=\frac{n_1-n_2}{n_1+n_2},\qquad t=\frac{E_{0T}}{E_{0I}}=\frac{2n_1}{n_1+n_2},$$
> y la energía se reparte como
> $$R=r^2=\left(\frac{n_1-n_2}{n_1+n_2}\right)^2,\qquad T=1-R.$$

> [!demostracion] Continuidad de $\vec E$ y $\vec B$ en la interfaz
> **Paso 1 — Geometría.** Pongo la interfaz en $z=0$, la onda viaja según $+z$ y $\vec E$ según $\hat x$. A la izquierda ($z<0$, medio 1) coexisten la incidente y la reflejada; a la derecha ($z>0$, medio 2) solo la transmitida. Para $z=0$ las amplitudes son $E_{0I}$, $E_{0R}$, $E_{0T}$.
>
> **Paso 2 — Campo magnético de cada onda.** En una onda plana $\vec B=\dfrac{1}{v}\,\hat k\times\vec E$, con $v=c/n$. La incidente y la transmitida viajan según $+\hat z$; la reflejada según $-\hat z$. Sus campos $\vec B$ van según $\hat y$:
> $$B_{0I}=\frac{n_1}{c}E_{0I},\qquad B_{0R}=-\frac{n_1}{c}E_{0R},\qquad B_{0T}=\frac{n_2}{c}E_{0T}.$$
> El signo de $B_{0R}$ refleja que la reflejada va en $-\hat z$.
>
> **Paso 3 — Continuidad de $E_\parallel$.** $\vec E$ es tangencial a la interfaz, luego $E_\parallel^{(1)}=E_\parallel^{(2)}$ da
> $$E_{0I}+E_{0R}=E_{0T}.\tag{1}$$
>
> **Paso 4 — Continuidad de $H_\parallel$.** Con $\mu_1\approx\mu_2\approx\mu_0$, la continuidad de $H_\parallel=B_\parallel/\mu$ es la de $B_\parallel$. $\vec B$ también es tangencial:
> $$B_{0I}+B_{0R}=B_{0T}\;\Longrightarrow\;\frac{n_1}{c}\bigl(E_{0I}-E_{0R}\bigr)=\frac{n_2}{c}E_{0T},$$
> es decir
> $$n_1\bigl(E_{0I}-E_{0R}\bigr)=n_2\,E_{0T}.\tag{2}$$
>
> **Paso 5 — Resolver (1)–(2).** Sustituyo $E_{0T}=E_{0I}+E_{0R}$ de (1) en (2):
> $$n_1(E_{0I}-E_{0R})=n_2(E_{0I}+E_{0R})\;\Longrightarrow\;(n_1-n_2)E_{0I}=(n_1+n_2)E_{0R},$$
> de donde
> $$\boxed{r=\frac{E_{0R}}{E_{0I}}=\frac{n_1-n_2}{n_1+n_2}.}$$
> Y de (1), $t=1+r$:
> $$\boxed{t=\frac{E_{0T}}{E_{0I}}=1+\frac{n_1-n_2}{n_1+n_2}=\frac{2n_1}{n_1+n_2}.}$$
>
> **Paso 6 — Coeficientes de energía.** La intensidad media es $I=\tfrac12 v\varepsilon E_0^2\propto n\,E_0^2$. La reflejada viaja en el medio 1 igual que la incidente, así que
> $$R=\frac{I_R}{I_I}=\frac{E_{0R}^2}{E_{0I}^2}=r^2=\left(\frac{n_1-n_2}{n_1+n_2}\right)^2.$$
> Por conservación de energía, lo que no se refleja se transmite:
> $$T=1-R.\qquad\blacksquare$$

> [!corolario] Incidencia oblicua y ángulo de Brewster
> En incidencia oblicua los coeficientes dependen de la **polarización** (paralela o perpendicular al plano de incidencia): son las **fórmulas de Fresnel generales**, que incluyen $\theta_I$ y $\theta_T$. Existe un ángulo, el **ángulo de Brewster** $\theta_B$ con $\tan\theta_B=n_2/n_1$, en el que la componente paralela **no se refleja**: la luz reflejada queda totalmente polarizada (base de las gafas de sol polarizadas). Ver [[5 Ondas Electromagneticas/Polarizacion | Polarización]].

### Ondas en conductores

> [!teoria] El número de onda se vuelve complejo
> En un **conductor** hay corriente libre $\vec J=\sigma\vec E$ (ley de Ohm). En la ley de Ampère–Maxwell esto añade un término disipativo, y al buscar soluciones $e^{i(kz-\omega t)}$ el número de onda $k$ deja de ser real: se vuelve **complejo**,
> $$\tilde k=k+i\kappa.$$
> La parte imaginaria $\kappa$ produce un factor $e^{-\kappa z}$: la onda **se atenúa** al penetrar en el metal. La distancia en que la amplitud cae a $1/e$ es la **profundidad de penetración** o *skin depth*
> $$\delta=\frac{1}{\kappa}\approx\sqrt{\frac{2}{\mu\sigma\omega}}\qquad(\text{buen conductor}).$$
> Por eso los metales son opacos y reflectantes, y por eso a alta frecuencia la corriente circula solo por una capa fina de la superficie (efecto piel). El caso límite $\sigma\to\infty$ recupera el conductor perfecto: $\delta\to0$ y reflexión total.

---

## Ejemplo

> [!ejemplo] Reflexión aire→vidrio a incidencia normal
> Una onda de luz pasa del aire ($n_1=1$) al vidrio ($n_2=1{,}5$) incidiendo perpendicularmente. ¿Qué fracción de la energía se refleja?

> [!solucion]
> **Paso 1 — Amplitud reflejada.** Con los coeficientes de Fresnel a incidencia normal,
> $$r=\frac{n_1-n_2}{n_1+n_2}=\frac{1-1{,}5}{1+1{,}5}=\frac{-0{,}5}{2{,}5}=-0{,}2.$$
> El signo negativo indica un desfase de $\pi$ en la reflexión (al pasar a un medio más denso ópticamente).
>
> **Paso 2 — Energía reflejada.**
> $$R=r^2=(-0{,}2)^2=0{,}04.$$
> Se refleja un **4 %** de la energía.
>
> **Paso 3 — Energía transmitida.**
> $$T=1-R=1-0{,}04=0{,}96,$$
> es decir, el **96 %** atraviesa el vidrio. Por eso una ventana se ve casi transparente pero también devuelve un reflejo tenue. $\blacksquare$
>
> *Comprobación con Snell:* si además incidiera a $\theta_I=30^\circ$, el rayo refractado saldría a $\sin\theta_T=\dfrac{n_1\sin\theta_I}{n_2}=\dfrac{1\cdot0{,}5}{1{,}5}=0{,}333$, o sea $\theta_T\approx19{,}5^\circ$: la luz se **acerca** a la normal al entrar en el medio más lento.

> [!warning] El índice depende de la frecuencia: dispersión
> $n=n(\omega)$ **no** es constante: depende de la frecuencia de la luz. Esto es la **dispersión**, y por eso un **prisma separa los colores** (cada color se refracta un ángulo distinto). Además, $v=c/n$ es la **velocidad de fase** de una onda monocromática; un pulso o paquete real viaja a la **velocidad de grupo** $v_g=d\omega/dk$, en general distinta. En medios dispersivos la velocidad de fase puede incluso superar $c$ sin violar la relatividad, porque ninguna señal viaja a esa velocidad.

---

## Resumen

> [!resumen] Ondas en medios de un vistazo
> | Concepto | Resultado | Origen |
> \|---\|---\|---\|
> | Velocidad en el medio | $v=\dfrac{1}{\sqrt{\varepsilon\mu}}=\dfrac{c}{n}$ | Ecuación de ondas con $\varepsilon,\mu$ |
> | Índice de refracción | $n=\sqrt{\varepsilon_r\mu_r}\approx\sqrt{\varepsilon_r}$ | $c/v$ |
> | Reflexión | $\theta_I=\theta_R$ | Fases iguales en la interfaz |
> | Refracción (Snell) | $n_1\sin\theta_I=n_2\sin\theta_T$ | Fases iguales en la interfaz |
> | Fresnel (normal) | $r=\dfrac{n_1-n_2}{n_1+n_2},\;\; t=\dfrac{2n_1}{n_1+n_2}$ | $E_\parallel,B_\parallel$ continuos |
> | Energía | $R=r^2,\;\; T=1-R$ | Conservación de energía |
> | Conductor | $\delta=\sqrt{2/(\mu\sigma\omega)}$ | $k$ complejo (atenuación) |

> [!corolario] La idea para llevarse
> Un medio no cambia la **forma** de las ondas de Maxwell, solo sus constantes: la luz va más lenta, $v=c/n$. Todo lo demás —Snell, Fresnel, Brewster— sale de imponer las **condiciones de frontera** a las ondas incidente, reflejada y transmitida en la interfaz. En un dieléctrico la onda se reparte; en un conductor se **apaga** en una capa de espesor $\delta$.

> [!referencia] Para seguir
> - Onda libre que aquí hacemos viajar por el medio: [[Ondas Planas]].
> - Estado del campo que decide la reflexión (Brewster): [[5 Ondas Electromagneticas/Polarizacion | Polarización]].
> - Respuesta del medio: [[2 Electrostatica/Dielectricos/index | Dieléctricos]] y [[Materiales Magneticos]].
> - Griffiths, *Introduction to Electrodynamics*, cap. 9.
