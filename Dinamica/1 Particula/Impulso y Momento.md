---
title: Impulso y Momento
order: 4
tags:
  - dinamica
  - teoria
  - particula
  - momento
draft: false
aliases:
  - impulso
  - cantidad de movimiento
  - momento lineal
  - momento angular
  - coeficiente de restitución
  - impulse momentum
---

# Impulso y Momento $\;\vec{J}=\Delta\vec{p},\ \dfrac{d\vec{H}_O}{dt}=\vec{M}_O$

> [!definicion]
> La **cantidad de movimiento** (o **momento lineal**) de una partícula es el vector
> $$\vec{p}=m\vec{v}.$$
> El **impulso** de una fuerza $\vec{F}$ entre los instantes $t_1$ y $t_2$ es su integral en el tiempo,
> $$\vec{J}=\int_{t_1}^{t_2}\vec{F}\,dt.$$
> El **teorema impulso–cantidad de movimiento** afirma que el impulso **neto** iguala el cambio de momento:
> $$\vec{J}^{\text{neto}}=\Delta\vec{p}.$$
> El **momento angular** (o momento cinético) respecto a un punto fijo $O$ es
> $$\vec{H}_O=\vec{r}\times m\vec{v},$$
> y su derivada temporal es el **momento de la fuerza** respecto a $O$, $\vec{M}_O=\vec{r}\times\vec{F}$:
> $$\frac{d\vec{H}_O}{dt}=\vec{M}_O.$$

> [!info]
> Cuarta sección de la [[1 Particula/index | partícula]] ([[Dinamica/index | Dinámica]]). Es la primera integral de [[Cinetica de la Particula | Newton]] **en el tiempo**: integrando $\sum\vec{F}=d\vec{p}/dt$ en $dt$ nacen los teoremas de esta nota, igual que la integral **en el espacio** dio el teorema de [[Trabajo y Energia]]. Útil cuando la fuerza se conoce **en función del tiempo** o cuando actúan fuerzas **impulsivas** (choques). Se extiende del punto al conjunto en [[Sistemas de Particulas]]. Modelo: Taylor, cap. 3.

---

## Ejemplo

> [!ejemplo]
> **Choque frontal con restitución (1D).**
>
> Dos partículas chocan de frente sobre una recta. La primera tiene masa $m_1=2\ \text{kg}$ y velocidad $v_1=3\ \text{m/s}$; la segunda, $m_2=1\ \text{kg}$ y $v_2=0$. El coeficiente de restitución del choque es $e=0{,}5$. Hallar las velocidades finales $v_1'$ y $v_2'$.
>
> ![[choque_1d.svg|560]]
>
> *Choque frontal: se conserva la cantidad de movimiento del par y la restitución $e$ relaciona las velocidades de separación y aproximación.*
>
> Durante el choque las fuerzas son **internas** al par e **impulsivas**, de modo que la cantidad de movimiento del sistema se conserva. Esto da una ecuación; la definición de restitución da la otra:
> $$m_1v_1+m_2v_2=m_1v_1'+m_2v_2',\qquad e=\frac{v_2'-v_1'}{v_1-v_2}.$$
>
> > [!solucion]
> > **Paso 1 — Conservación de $p$.** Con los datos,
> > $$2(3)+1(0)=2v_1'+1\,v_2'\;\Longrightarrow\; 6=2v_1'+v_2'.$$
> > **Paso 2 — Restitución.** La velocidad de aproximación es $v_1-v_2=3\ \text{m/s}$, luego
> > $$v_2'-v_1'=e\,(v_1-v_2)=0{,}5\cdot 3=1{,}5\ \text{m/s}.$$
> > **Paso 3 — Resolver el sistema.** Sumando $v_2'=v_1'+1{,}5$ en la primera:
> > $$6=2v_1'+(v_1'+1{,}5)=3v_1'+1{,}5\;\Longrightarrow\; v_1'=1{,}5\ \text{m/s},$$
> > y por tanto $v_2'=1{,}5+1{,}5=3{,}0\ \text{m/s}$. **Comprobación** (conservación de $p$): $2(1{,}5)+1(3{,}0)=3+3=6\ \checkmark$.
> >
> > $$\boxed{\;v_1'=1{,}5\ \text{m/s},\qquad v_2'=3{,}0\ \text{m/s}.\;}$$
> > La partícula pesada se frena y la ligera sale despedida; como $e<1$, parte de la energía cinética se disipa en la deformación.

---

## En qué consiste

> [!teoria] Las dos primeras integrales de Newton
> La segunda ley puede escribirse $\sum\vec{F}=\dfrac{d\vec{p}}{dt}$ (con $m$ constante, $\dfrac{d\vec{p}}{dt}=m\dfrac{d\vec{v}}{dt}=m\vec{a}$). Integrarla **en el espacio** ($\cdot\,d\vec{r}$) produce el teorema trabajo–energía; integrarla **en el tiempo** ($\cdot\,dt$) produce el teorema impulso–cantidad de movimiento. Y al tomar el **momento respecto a $O$** ($\vec{r}\times$) aparece la ley del momento angular. No son principios nuevos: son Newton reescrito para las dos magnitudes —tiempo y giro— que las otras formas no destacan.

> [!teorema] Impulso–cantidad de movimiento
> El impulso neto sobre una partícula entre $t_1$ y $t_2$ iguala la variación de su cantidad de movimiento:
> $$\boxed{\;\vec{J}^{\text{neto}}=\int_{t_1}^{t_2}\sum\vec{F}\,dt=\vec{p}_2-\vec{p}_1=\Delta\vec{p}.\;}$$

> [!demostracion]
> **Paso 1 — Partir de Newton en forma de momento.** $\displaystyle\sum\vec{F}=\frac{d\vec{p}}{dt}$. **Paso 2 — Integrar en el tiempo.** Multiplicando por $dt$ e integrando entre $t_1$ y $t_2$,
> $$\int_{t_1}^{t_2}\sum\vec{F}\,dt=\int_{t_1}^{t_2}\frac{d\vec{p}}{dt}\,dt=\int_{\vec{p}_1}^{\vec{p}_2}d\vec{p}.$$
> **Paso 3 — Evaluar.** El integrando del miembro derecho es una diferencial exacta, así que
> $$\vec{J}^{\text{neto}}=\vec{p}_2-\vec{p}_1=\Delta\vec{p}.\qquad\blacksquare$$

> [!teorema] Momento angular y momento de fuerza
> La rapidez de cambio del momento angular de una partícula respecto a un punto fijo $O$ es el momento de la fuerza neta respecto a ese punto:
> $$\boxed{\;\frac{d\vec{H}_O}{dt}=\vec{M}_O,\qquad \vec{H}_O=\vec{r}\times m\vec{v},\quad \vec{M}_O=\vec{r}\times\sum\vec{F}.\;}$$

> [!demostracion]
> **Paso 1 — Derivar la definición.** Derivando $\vec{H}_O=\vec{r}\times m\vec{v}$ con la regla del producto para el producto vectorial,
> $$\frac{d\vec{H}_O}{dt}=\dot{\vec{r}}\times m\vec{v}+\vec{r}\times m\dot{\vec{v}}.$$
> **Paso 2 — Anular el primer término.** Como $\dot{\vec{r}}=\vec{v}$, ese término es $\vec{v}\times m\vec{v}=m(\vec{v}\times\vec{v})=\vec{0}$ (el producto vectorial de un vector consigo mismo es nulo). **Paso 3 — Identificar el segundo.** Por la segunda ley, $m\dot{\vec{v}}=\sum\vec{F}$, luego
> $$\frac{d\vec{H}_O}{dt}=\vec{0}+\vec{r}\times\sum\vec{F}=\vec{r}\times\sum\vec{F}=\vec{M}_O.\qquad\blacksquare$$

> [!teoria] Coeficiente de restitución
> En un choque entre dos cuerpos, el **coeficiente de restitución** $e$ mide cuánta velocidad relativa se recupera a lo largo de la **línea de impacto** (la normal de contacto). Es el cociente entre la velocidad de **separación** y la de **aproximación**, ambas medidas sobre esa línea:
> $$e=\frac{\text{velocidad de separación}}{\text{velocidad de aproximación}}=\frac{v_2'-v_1'}{v_1-v_2}\in[0,1].$$
> Los extremos clasifican el choque:
> - $e=1$ — **perfectamente elástico**: se recupera toda la velocidad relativa y se **conserva la energía cinética** $T$.
> - $e=0$ — **perfectamente plástico** (inelástico): no hay separación, los cuerpos quedan **unidos** con velocidad común.
> - $0<e<1$ — choque real, con pérdida parcial de $T$.
>
> Durante el choque la cantidad de movimiento del sistema **se conserva** —las fuerzas de contacto son internas e impulsivas, su impulso externo neto es nulo—, **aunque la energía no**. Esta es la pareja de ecuaciones que cierra cualquier problema de choque: conservación de $\vec{p}$ (vectorial) más la definición de $e$ (escalar, sobre la normal).

> [!proposicion] Leyes de conservación
> De los dos teoremas anteriores se leen de inmediato sus respectivas conservaciones:
> - **Cantidad de movimiento.** Si el impulso externo neto es nulo —en particular si $\sum\vec{F}_{ext}=\vec{0}$— entonces $\Delta\vec{p}=\vec{0}$ y $\vec{p}$ se **conserva**.
> - **Momento angular.** Si $\vec{M}_O=\vec{0}$ —caso de una **fuerza central**, paralela a $\vec{r}$, o de fuerza nula— entonces $d\vec{H}_O/dt=\vec{0}$ y $\vec{H}_O$ se **conserva**. Esta es la base de la segunda ley de **Kepler** (áreas iguales en tiempos iguales) y del movimiento bajo fuerzas centrales.

> [!warning]
> - $\vec{p}$ y $\vec{H}_O$ son **vectores**: se conservan componente a componente, y puede conservarse una componente aunque no las demás.
> - La restitución se aplica **a lo largo de la línea de impacto** (la normal de contacto), no sobre la velocidad total; la componente tangencial obedece a la fricción, no a $e$.
> - $\vec{H}_O$ depende del **punto $O$** elegido: cambiarlo cambia $\vec{r}$ y, con él, $\vec{H}_O$ y $\vec{M}_O$.
> - En un choque la energía cinética **no se conserva** salvo si $e=1$; conservar $\vec{p}$ no implica conservar $T$.

## Resumen

> [!resumen]
> | Magnitud | Definición | Ley / relación |
> |:---|:---|:---|
> | Cantidad de movimiento | $\vec{p}=m\vec{v}$ | $\sum\vec{F}=d\vec{p}/dt$ |
> | Impulso | $\vec{J}=\int_{t_1}^{t_2}\vec{F}\,dt$ | $\vec{J}^{\text{neto}}=\Delta\vec{p}$ |
> | Momento angular | $\vec{H}_O=\vec{r}\times m\vec{v}$ | $d\vec{H}_O/dt=\vec{M}_O$ |
> | Momento de fuerza | $\vec{M}_O=\vec{r}\times\vec{F}$ | anula $\dot{\vec{H}}_O$ si $\vec{M}_O=\vec0$ |
> | Restitución | $e=\dfrac{v_2'-v_1'}{v_1-v_2}$ | $e=1$ elástico, $e=0$ plástico |

> [!corolario]
> Impulso y momento son Newton integrado **en el tiempo** y proyectado sobre el **giro**. De ahí salen, sin postulados nuevos, las dos grandes conservaciones de la mecánica —la del momento lineal y la del angular— y la herramienta para tratar choques, donde $\vec{p}$ se conserva y $e$ fija cuánta energía sobrevive.

> [!referencia]
> Taylor, *Classical Mechanics*, cap. 3 (momento lineal y angular; choques). Integral gemela en el espacio: [[Trabajo y Energia]]. Origen dinámico: [[Cinetica de la Particula]]. Extensión al conjunto: [[Sistemas de Particulas]]. Vuelta al [[1 Particula/index | índice de la partícula]].
