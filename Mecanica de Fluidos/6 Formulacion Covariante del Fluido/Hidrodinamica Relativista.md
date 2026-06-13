---
title: Hidrodinámica Relativista
tags:
  - fluidos
  - teoria
  - covariante
draft: false
aliases:
  - Hidrodinámica relativista
  - Euler relativista
  - Conservación covariante
---

# Hidrodinámica Relativista $\partial_\mu T^{\mu\nu}=0,\quad \partial_\mu(n\,u^\mu)=0$

> [!definicion] Las dos leyes covariantes del fluido perfecto
> La dinámica completa de un fluido perfecto relativista se condensa en **dos ecuaciones tensoriales**, válidas en cualquier sistema inercial sin reescribirlas:
> $$\boxed{\;\partial_\mu T^{\mu\nu}=0\;}\qquad\text{(conservación de energía–momento)}$$
> $$\boxed{\;\partial_\mu(n\,u^\mu)=0\;}\qquad\text{(conservación del número de partículas / masa)}$$
> con el **tensor energía–momento del fluido perfecto**
> $$T^{\mu\nu}=(\varepsilon+p)\,\frac{u^\mu u^\nu}{c^2}-p\,\eta^{\mu\nu}\equiv w\,\frac{u^\mu u^\nu}{c^2}-p\,\eta^{\mu\nu},\qquad w\equiv\varepsilon+p.$$
> **Convenios fijos de toda la nota:**
> - Métrica $\eta_{\mu\nu}=\mathrm{diag}(+1,-1,-1,-1)$; índices griegos $0\!-\!3$, latinos $1\!-\!3$; suma de Einstein.
> - Cuadrivelocidad $u^\mu=\gamma(c,\vec v)$, normalizada $u_\mu u^\mu=c^2$.
> - Derivadas: $\partial_0=\tfrac1c\partial_t$, $\partial^\mu=\eta^{\mu\nu}\partial_\nu$ (espacial $\partial^i=-\partial_i$).
> - $\varepsilon$ = densidad de energía propia, $p$ = presión propia, $n$ = densidad propia de partículas, $w=\varepsilon+p$ = entalpía por unidad de volumen.
> - Proyector espacial $h^{\mu\nu}=\eta^{\mu\nu}-\dfrac{u^\mu u^\nu}{c^2}$, equivalentemente $h^\alpha{}_\nu=\delta^\alpha_\nu-\dfrac{u^\alpha u_\nu}{c^2}$, con la propiedad clave $h^\alpha{}_\nu u^\nu=0$.

> [!info] Ubicación y enlaces
> Esta nota pertenece a la sección [[6 Formulacion Covariante del Fluido/index | Formulación Covariante del Fluido]]. Sus notas hermanas son [[Tensor Energia-Momento del Fluido]] (de dónde sale $T^{\mu\nu}$ y qué significa cada componente) y [[Flujo Compresible y Ondas de Choque]] (aplicación a alta velocidad).
> En el límite no relativista se recuperan las ecuaciones clásicas: [[Ecuacion de Euler]] (de la proyección $\perp u$) y [[Conservacion de Masa]] (de la continuidad covariante).
> Referencia principal: Landau & Lifshitz, *Mecánica de Fluidos* (Vol. 6), §134.

---

## Ejemplo

> [!ejemplo] Recuperar las ecuaciones clásicas como límite $v\ll c$
> El test de toda formulación covariante es que colapse a lo conocido. Verificamos las **dos** leyes por separado.
>
> **1) Continuidad clásica desde $\partial_\mu(n\,u^\mu)=0$.**
> Desarrollamos la divergencia separando índice temporal y espacial:
> $$\partial_\mu(n u^\mu)=\partial_0(n u^0)+\partial_i(n u^i)=\frac1c\partial_t\big(n\gamma c\big)+\partial_i\big(n\gamma v^i\big)=0.$$
> Con $v\ll c$ tenemos $\gamma\to 1$, y la densidad propia por partícula se vuelve la densidad de masa $\rho\equiv m\,n$ (multiplicando por la masa en reposo $m$, constante):
> $$\partial_t\rho+\partial_i(\rho v^i)=0\quad\Longleftrightarrow\quad \boxed{\;\partial_t\rho+\nabla\cdot(\rho\vec v)=0\;}$$
> que es exactamente [[Conservacion de Masa]].
>
> **2) Euler clásico desde la proyección $\perp u$.**
> Más adelante demostraremos (sección *En qué consiste*) la **ecuación de Euler relativista**
> $$\frac{\varepsilon+p}{c^2}\,u^\mu\partial_\mu u^\alpha=h^{\alpha\mu}\partial_\mu p.$$
> Tomamos la componente espacial $\alpha=i$ y aplicamos $v\ll c$, $\varepsilon\approx\rho c^2\gg p$. **Paso a paso, sin retoques de signo:**
> - *Coeficiente inercial:* $\dfrac{\varepsilon+p}{c^2}\approx\dfrac{\rho c^2}{c^2}=\rho.$
> - *Aceleración convectiva:* $u^\mu\partial_\mu u^i=\gamma\big(\tfrac1c\partial_t+v^j\partial_j\big)(\gamma v^i)\;\xrightarrow{\;\gamma\to1\;}\;\partial_t v^i+v^j\partial_j v^i=\dfrac{D v^i}{Dt}.$
> - *Lado derecho (clave del signo):* expandimos el proyector
> $$h^{i\mu}\partial_\mu p=\Big(\eta^{i\mu}-\frac{u^i u^\mu}{c^2}\Big)\partial_\mu p.$$
>   El término correctivo $\dfrac{u^i u^\mu}{c^2}\partial_\mu p\sim \dfrac{v\,\dot p}{c^2}$ es de orden $v/c^2$, despreciable. Queda solo $\eta^{i\mu}\partial_\mu p$. Como $\eta$ es diagonal, $\eta^{i\mu}\partial_\mu p=\eta^{ij}\partial_j p=-\delta_{ij}\partial_j p=-\partial_i p$.
> - *Resultado:*
> $$\boxed{\;\rho\,\frac{D v^i}{Dt}=-\partial_i p\;}\quad\Longleftrightarrow\quad \rho\,\frac{D\vec v}{Dt}=-\nabla p,$$
> que es [[Ecuacion de Euler]]. **El signo menos sale ÚNICAMENTE de $\eta^{ii}=-1$**; no se introduce ningún signo a mano. $\blacksquare$

---

## En qué consiste

Toda la hidrodinámica relativista del fluido perfecto es **una sola identidad** $\partial_\mu T^{\mu\nu}=0$ (cuatro ecuaciones, $\nu=0,1,2,3$) más la continuidad $\partial_\mu(nu^\mu)=0$. La estrategia para *leer* la física es **proyectar** $\partial_\mu T^{\mu\nu}=0$ sobre dos direcciones complementarias:

- **paralela a $u^\nu$** (contraer con $u_\nu$): da la ecuación de la **energía**;
- **ortogonal a $u^\nu$** (aplicar $h^\alpha{}_\nu$): da la ecuación del **momento** (Euler relativista).

Esta descomposición es ortogonal y completa porque $u_\nu$ y $h^\alpha{}_\nu$ separan el espacio en el eje temporal propio del fluido y su complemento espacial. Antes necesitamos un lema.

![[fluido_worldlines.svg|440]]
*Líneas de universo del fluido: la cuadrivelocidad $u^\mu$ es tangente a cada línea, la cuadriaceleración $a^\alpha=u^\mu\partial_\mu u^\alpha$ es ortogonal a ella, y el proyector $h^{\alpha\mu}$ extrae las componentes espaciales (perpendiculares a $u$) de cualquier gradiente.*

> [!lema] La cuadriaceleración es ortogonal a la cuadrivelocidad
> Partimos de la **normalización** $u_\mu u^\mu=c^2$, que es **constante** (escalar fijo). Derivamos respecto a $x^\mu$:
> $$\partial_\mu(u_\nu u^\nu)=0\;\Longrightarrow\;(\partial_\mu u_\nu)u^\nu+u_\nu(\partial_\mu u^\nu)=0.$$
> Los dos sumandos son iguales (renombrando índices mudos y subiendo/bajando con $\eta$, que es constante), de modo que
> $$2\,u_\nu\,\partial_\mu u^\nu=0\;\Longrightarrow\;\boxed{\,u_\nu\,\partial_\mu u^\nu=0\,}.$$
> Geométricamente: la cuadriaceleración $a^\alpha=u^\mu\partial_\mu u^\alpha$ es **ortogonal** a la cuadrivelocidad, $u_\alpha a^\alpha=0$. Este lema se usará una y otra vez para limpiar términos.

### Proyección paralela a $u$ — ecuación de la energía

> [!demostracion] Contracción de $\partial_\mu T^{\mu\nu}=0$ con $u_\nu$
> Multiplicamos la conservación por $u_\nu$:
> $$u_\nu\,\partial_\mu T^{\mu\nu}=u_\nu\,\partial_\mu\!\Big[w\,\frac{u^\mu u^\nu}{c^2}-p\,\eta^{\mu\nu}\Big]=0.$$
> **Término entálpico.** Aplicamos la regla del producto a $\partial_\mu(w u^\mu u^\nu/c^2)$ y contraemos con $u_\nu$:
> $$\frac{u_\nu}{c^2}\Big[\partial_\mu(w u^\mu)\,u^\nu+w u^\mu\,\partial_\mu u^\nu\Big].$$
> - En el primer sumando $u_\nu u^\nu=c^2$, que cancela el $c^2$ del denominador: queda $\partial_\mu(w u^\mu)$.
> - En el segundo, $u_\nu\,\partial_\mu u^\nu=0$ por el **lema**: se anula entero.
>
> Luego el término entálpico vale $\partial_\mu(w u^\mu)=\partial_\mu\big[(\varepsilon+p)u^\mu\big]$.
> **Término de presión.** $-u_\nu\,\partial_\mu(p\,\eta^{\mu\nu})=-u_\nu\,\eta^{\mu\nu}\partial_\mu p=-u^\mu\,\partial_\mu p$ (la métrica $\eta^{\mu\nu}$ sube el índice de $u_\nu$).
> **Sumamos e igualamos a cero:**
> $$\partial_\mu\big[(\varepsilon+p)u^\mu\big]-u^\mu\partial_\mu p=0.$$
> Desarrollando $\partial_\mu[(\varepsilon+p)u^\mu]=u^\mu\partial_\mu\varepsilon+u^\mu\partial_\mu p+(\varepsilon+p)\partial_\mu u^\mu$, el término $u^\mu\partial_\mu p$ se **cancela** con el de presión:
> $$\boxed{\,u^\mu\partial_\mu\varepsilon+(\varepsilon+p)\,\partial_\mu u^\mu=0\,}.$$
> **Lectura:** la variación de energía propia siguiendo al fluido ($u^\mu\partial_\mu\varepsilon$) equilibra el trabajo de expansión/compresión $(\varepsilon+p)\partial_\mu u^\mu$ (la divergencia $\partial_\mu u^\mu$ mide la tasa de cambio de volumen propio). Es la **primera ley de la termodinámica** en forma covariante.

### Proyección ortogonal a $u$ — Euler relativista

> [!demostracion] Aplicación de $h^\alpha{}_\nu$ a $\partial_\mu T^{\mu\nu}=0$
> Proyectamos con $h^\alpha{}_\nu=\delta^\alpha_\nu-\dfrac{u^\alpha u_\nu}{c^2}$, cuya propiedad de oro es $h^\alpha{}_\nu u^\nu=0$:
> $$h^\alpha{}_\nu\,\partial_\mu T^{\mu\nu}=h^\alpha{}_\nu\,\partial_\mu\!\Big[w\,\frac{u^\mu u^\nu}{c^2}-p\,\eta^{\mu\nu}\Big]=0.$$
>
> **Término convectivo** $h^\alpha{}_\nu\,\partial_\mu\!\big(w u^\mu u^\nu/c^2\big)$. Regla del producto sobre $u^\nu$:
> $$h^\alpha{}_\nu\,\partial_\mu\!\Big(\frac{w u^\mu u^\nu}{c^2}\Big)=h^\alpha{}_\nu\Big[\frac{\partial_\mu(w u^\mu)}{c^2}\,u^\nu+\frac{w u^\mu}{c^2}\,\partial_\mu u^\nu\Big].$$
> - El **primer** corchete contiene $h^\alpha{}_\nu u^\nu=0$: **se aniquila**.
> - En el **segundo**, $h^\alpha{}_\nu\,\partial_\mu u^\nu$. Sustituyendo $h^\alpha{}_\nu=\delta^\alpha_\nu-\dfrac{u^\alpha u_\nu}{c^2}$:
> $$h^\alpha{}_\nu\,\partial_\mu u^\nu=\partial_\mu u^\alpha-\frac{u^\alpha}{c^2}\,\underbrace{u_\nu\,\partial_\mu u^\nu}_{=\,0\ \text{(lema)}}=\partial_\mu u^\alpha.$$
>
> Por tanto el término convectivo se reduce limpiamente a $\dfrac{w}{c^2}\,u^\mu\partial_\mu u^\alpha$.
>
> **Término de presión** $-h^\alpha{}_\nu\,\partial_\mu(p\,\eta^{\mu\nu})$:
> $$-h^\alpha{}_\nu\,\partial_\mu(p\,\eta^{\mu\nu})=-h^\alpha{}_\nu\,\eta^{\mu\nu}\partial_\mu p=-h^{\alpha\mu}\partial_\mu p,$$
> donde $\eta^{\mu\nu}$ sube el índice $\nu$ de $h^\alpha{}_\nu$ produciendo $h^{\alpha\mu}$.
>
> **Sumamos los dos términos e igualamos a cero:**
> $$\frac{w}{c^2}\,u^\mu\partial_\mu u^\alpha-h^{\alpha\mu}\partial_\mu p=0,$$
> es decir, la **ecuación de Euler relativista**:
> $$\boxed{\;\frac{\varepsilon+p}{c^2}\,u^\mu\partial_\mu u^\alpha=h^{\alpha\mu}\partial_\mu p=\Big(\eta^{\alpha\mu}-\frac{u^\alpha u^\mu}{c^2}\Big)\partial_\mu p\;}.$$
> No se añade **ningún** signo menos delante: el gradiente de presión proyectado ya lleva el signo físico correcto **automáticamente**, porque la parte espacial de la métrica ($\eta^{ii}=-1$) genera el menos clásico, como se verifica en el límite no relativista.

> [!proposicion] Lectura física de Euler relativista (con su signo correcto)
> - **La presión pesa.** El coeficiente inercial no es $\rho$ sino $\dfrac{\varepsilon+p}{c^2}$: la presión **contribuye a la inercia** por unidad de volumen. En el límite clásico $\varepsilon\approx\rho c^2\gg p$ se reduce a $\rho$, pero en materia ultrarrelativista (radiación, $p=\varepsilon/3$) el factor es $\tfrac43\varepsilon/c^2$.
> - **Cuadriaceleración.** El lado izquierdo es $\dfrac{\varepsilon+p}{c^2}\,a^\alpha$ con $a^\alpha=u^\mu\partial_\mu u^\alpha$, la cuadriaceleración de la partícula de fluido.
> - **Fuerza = gradiente proyectado.** El lado derecho $h^{\alpha\mu}\partial_\mu p$ es el gradiente de presión **proyectado** al espacio ortogonal a $u$. Su parte espacial es
> $$h^{i\mu}\partial_\mu p\approx\eta^{ii}\partial_i p=-\partial_i p,$$
> es decir, **la fuerza apunta hacia presiones decrecientes**, como debe ser. El "menos" físico **vive en la métrica**; no se pone a mano.

### Continuidad covariante

> [!teorema] Conservación covariante del número de partículas
> La segunda ley, $\partial_\mu(n u^\mu)=0$, define la corriente de número $N^\mu=n u^\mu$ con divergencia nula. Separando temporal y espacial (ver *Ejemplo*) y tomando $v\ll c$, $\gamma\to1$, $\rho=mn$:
> $$\boxed{\;\partial_t\rho+\nabla\cdot(\rho\vec v)=0\;}$$
> recuperando [[Conservacion de Masa]]. En el régimen relativista esta es la ley fundamental; la "masa" clásica es solo su límite.

---

## Resumen

> [!resumen] Mapa de la hidrodinámica relativista
> | Objeto / ecuación | Forma covariante | Origen / proyección | Límite no relativista |
> |---|---|---|---|
> | Energía–momento | $T^{\mu\nu}=(\varepsilon+p)\dfrac{u^\mu u^\nu}{c^2}-p\,\eta^{\mu\nu}$ | definición | tensor de [[Tensor Energia-Momento del Fluido]] |
> | Conservación | $\partial_\mu T^{\mu\nu}=0$ | postulado | — |
> | Lema | $u_\nu\,\partial_\mu u^\nu=0$ | de $u_\mu u^\mu=c^2$ | $a\perp u$ |
> | Energía | $u^\mu\partial_\mu\varepsilon+(\varepsilon+p)\partial_\mu u^\mu=0$ | proyección $\parallel u$ (contraer $u_\nu$) | 1.ª ley termodinámica |
> | Euler relativista | $\dfrac{\varepsilon+p}{c^2}u^\mu\partial_\mu u^\alpha=h^{\alpha\mu}\partial_\mu p$ | proyección $\perp u$ (aplicar $h^\alpha{}_\nu$) | $\rho\,D\vec v/Dt=-\nabla p$ |
> | Continuidad | $\partial_\mu(n u^\mu)=0$ | postulado | $\partial_t\rho+\nabla\cdot(\rho\vec v)=0$ |
>
> Idea central: **una identidad** $\partial_\mu T^{\mu\nu}=0$ se descompone, vía las proyecciones $\parallel u$ y $\perp u$, en energía + momento; los signos cierran solos gracias a $\eta_{\mu\nu}=\mathrm{diag}(+1,-1,-1,-1)$.

> [!corolario] Cosmología FRW como caso particular
> En un universo homogéneo e isótropo (métrica de Friedmann–Robertson–Walker, factor de escala $a(t)$), la ecuación de la energía con la **divergencia covariante** $\nabla_\mu T^{\mu\nu}=0$ (que sustituye $\partial_\mu\to\nabla_\mu$ en espacio curvo) se reduce a la **ecuación del fluido cosmológico**:
> $$\boxed{\;\dot\varepsilon+3\,\frac{\dot a}{a}\,(\varepsilon+p)=0\;}.$$
> El término $3\dot a/a$ es la divergencia covariante de $u^\mu$ en FRW (expansión de Hubble); su deducción completa requiere los símbolos de Christoffel y se trata en cosmología. Se enuncia aquí solo para mostrar que **la misma proyección energética** gobierna desde una tobera supersónica hasta la evolución del universo.

> [!warning] La presión pesa: inercia, gravedad y los límites del modelo
> - **Inercia.** El coeficiente $\dfrac{\varepsilon+p}{c^2}$ muestra que la presión añade inercia: comprimir un fluido relativista lo hace más difícil de acelerar de lo que predice $\rho$ sola.
> - **Gravedad.** En Relatividad General **toda** componente de $T^{\mu\nu}$ gravita, incluida $p$. Por eso la ecuación de equilibrio estelar relativista (**Tolman–Oppenheimer–Volkoff, TOV**) contiene términos de presión que **realimentan** la gravedad: en una estrella de neutrones, aumentar la presión no siempre estabiliza, sino que puede precipitar el colapso. La presión no salva: pesa.
> - **Fluido perfecto = idealización.** $T^{\mu\nu}=(\varepsilon+p)u^\mu u^\nu/c^2-p\,\eta^{\mu\nu}$ ignora viscosidad y conducción térmica. La **hidrodinámica relativista disipativa** (añadir esos términos sin violar causalidad ni estabilidad) sigue siendo un **problema abierto**: las formulaciones ingenuas (Eckart, Landau–Lifshitz de 1.er orden) son inestables, y las modernas (Israel–Stewart, BDNK) aún se investigan activamente.

> [!referencia] Fuentes
> - L. D. Landau & E. M. Lifshitz, *Mecánica de Fluidos* (Curso de Física Teórica, Vol. 6), §134 — Hidrodinámica relativista.
> - L. D. Landau & E. M. Lifshitz, *Teoría Clásica de los Campos* (Vol. 2) — tensor energía–momento y conservación.
> - Notas relacionadas: [[Tensor Energia-Momento del Fluido]], [[Flujo Compresible y Ondas de Choque]], [[Ecuacion de Euler]], [[Conservacion de Masa]].
