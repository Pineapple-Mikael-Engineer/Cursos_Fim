---
title: Ecuación de Euler
tags:
  - fluidos
  - teoria
  - flujo-ideal
draft: false
aliases:
  - Ecuación de Euler
  - Hidrostática
  - Fluido ideal
---

# Ecuación de Euler $\rho\,\dfrac{D\vec v}{Dt}=-\nabla p+\rho\vec g$

---

> [!definicion] Ecuación de Euler
> La **ecuación de Euler** es la ecuación de movimiento de un **fluido ideal** (no viscoso, $\mu=0$). Iguala la masa por unidad de volumen multiplicada por la aceleración material a la suma de la fuerza de presión y la fuerza másica:
> $$
> \rho\,\frac{D\vec v}{Dt}=\rho\left(\partial_t\vec v+(\vec v\cdot\nabla)\vec v\right)=-\nabla p+\rho\vec g,
> $$
> donde $\rho$ es la densidad, $\vec v$ la velocidad, $p$ la presión, $\vec g$ la aceleración másica (gravedad) y $D/Dt$ la [[Derivada Material | derivada material]]. En componentes, con convenio de suma:
> $$
> \rho\left(\partial_t v_i+v_j\,\partial_j v_i\right)=-\partial_i p+\rho\,g_i.
> $$
> Es el caso particular de las [[Ecuaciones de Navier-Stokes]] en el que se desprecian por completo los esfuerzos viscosos.

---

> [!info] Contexto
> Esta nota pertenece a la sección [[4 Flujo Ideal/index | Flujo Ideal]]. Sus **hermanas** son [[Ecuacion de Bernoulli]], [[Flujo Potencial]] y [[Vorticidad y Teoremas]]. **Viene de** [[Ecuaciones de Navier-Stokes]], de la que es el límite $\mu\to 0$. Referencia base: **Landau & Lifshitz, Vol. 6 (Mecánica de Fluidos), §§2–3**.

---

## En qué consiste

La ecuación de Euler describe un **fluido ideal**: un fluido en el que la única fuerza de superficie es la presión, isótropa y normal a cualquier elemento de área. No hay transferencia de cantidad de movimiento por fricción interna; el tensor de esfuerzos se reduce a
$$
\sigma_{ij}=-p\,\delta_{ij}.
$$

Partiendo de la **ecuación de Cauchy** $\rho\,Dv_i/Dt=\partial_j\sigma_{ij}+\rho g_i$ y sustituyendo este tensor:
$$
\partial_j\sigma_{ij}=\partial_j(-p\,\delta_{ij})=-\partial_i p\quad\Longrightarrow\quad
\rho\,\frac{D\vec v}{Dt}=-\nabla p+\rho\vec g.
$$

Equivalentemente, partiendo de las [[Ecuaciones de Navier-Stokes]] $\rho\,D\vec v/Dt=-\nabla p+\mu\nabla^2\vec v+\rho\vec g$ y haciendo $\mu=0$ se obtiene exactamente lo mismo.

> [!regla] Condición de pared: deslizamiento
> Al anular la viscosidad, la ecuación de Euler **baja de orden** (desaparece el término $\mu\nabla^2\vec v$, de segundo orden). Esto cambia la condición de contorno en una pared sólida: ya **no** se puede exigir que la velocidad tangencial coincida con la de la pared. Solo sobrevive la condición **impenetrabilidad**: la componente normal de la velocidad iguala la de la pared,
> $$
> \vec v\cdot\hat n=\vec v_{\text{pared}}\cdot\hat n,
> $$
> y la componente **tangencial queda libre** (condición de **deslizamiento**, *free slip*). Por eso el fluido ideal puede "resbalar" sobre las superficies, mientras que el fluido viscoso se adhiere (no-deslizamiento). Cerca de la pared real esto da lugar a la [[5 Flujo Viscoso/index | capa límite]].

### Forma de Lamb–Gromeka

Una reescritura muy útil del término convectivo permite conectar Euler con [[Ecuacion de Bernoulli]] y con la [[Vorticidad y Teoremas | vorticidad]].

> [!proposicion] Forma de Lamb–Gromeka
> Con la **vorticidad** $\vec\omega=\nabla\times\vec v$, la ecuación de Euler (con $\rho$ constante o, en general, $\nabla p/\rho$ explícito) se escribe
> $$
> \partial_t\vec v+\nabla\!\left(\tfrac12\,v^2\right)-\vec v\times\vec\omega=-\frac1\rho\nabla p+\vec g.
> $$

> [!demostracion]
> **Paso 1 — Identidad vectorial del término convectivo.** Para cualquier campo $\vec v$ se cumple la identidad
> $$
> \nabla\!\left(\tfrac12\,\vec v\cdot\vec v\right)=(\vec v\cdot\nabla)\vec v+\vec v\times(\nabla\times\vec v).
> $$
> Comprobémosla por componentes. El lado izquierdo es $\partial_i(\tfrac12 v_j v_j)=v_j\,\partial_i v_j$. Para el lado derecho usamos $[\vec v\times(\nabla\times\vec v)]_i=\varepsilon_{ijk}v_j(\nabla\times\vec v)_k=\varepsilon_{ijk}\varepsilon_{klm}v_j\,\partial_l v_m$. Con la identidad $\varepsilon_{ijk}\varepsilon_{klm}=\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}$:
> $$
> [\vec v\times(\nabla\times\vec v)]_i=(\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl})\,v_j\,\partial_l v_m=v_j\,\partial_i v_j-v_j\,\partial_j v_i.
> $$
> Sumando $(\vec v\cdot\nabla)v_i=v_j\,\partial_j v_i$ se cancela el segundo término y queda $v_j\,\partial_i v_j$, que es justo el lado izquierdo. $\checkmark$
>
> **Paso 2 — Despejar el término convectivo.** De la identidad anterior,
> $$
> (\vec v\cdot\nabla)\vec v=\nabla\!\left(\tfrac12\,v^2\right)-\vec v\times(\nabla\times\vec v)=\nabla\!\left(\tfrac12\,v^2\right)-\vec v\times\vec\omega.
> $$
>
> **Paso 3 — Sustituir en Euler.** Dividiendo la ecuación de Euler por $\rho$ y desarrollando $D\vec v/Dt=\partial_t\vec v+(\vec v\cdot\nabla)\vec v$:
> $$
> \partial_t\vec v+\nabla\!\left(\tfrac12\,v^2\right)-\vec v\times\vec\omega=-\frac1\rho\nabla p+\vec g.
> $$
> $\blacksquare$

Esta forma es la base de la deducción de [[Ecuacion de Bernoulli | Bernoulli]] (proyectando sobre una línea de corriente, el término $\vec v\times\vec\omega$ es ortogonal a $\vec v$) y de los [[Vorticidad y Teoremas | teoremas de Kelvin y Helmholtz]].

---

## La hidrostática como corolario ($\vec v=0$)

El caso más simple —y más exacto— de la ecuación de Euler se obtiene cuando el fluido está **en reposo**, $\vec v=\vec 0$ en todo punto y todo instante. Entonces $D\vec v/Dt=\vec 0$ y la ecuación colapsa a la **ecuación fundamental de la hidrostática**:
$$
\boxed{\;\nabla p=\rho\vec g\;}
$$
Es decir: en un fluido en reposo el gradiente de presión equilibra exactamente la fuerza másica por unidad de volumen.

![[hidrostatica.svg|420]]
*Fluido en reposo: la presión crece linealmente con la profundidad ($p=p_0+\rho g h$). Sobre un cuerpo sumergido de volumen $V$ actúa un empuje vertical $E=\rho g V$ igual al peso del fluido desplazado.*

### Fluido incompresible bajo gravedad

> [!corolario] Presión hidrostática
> Para un fluido **incompresible** ($\rho=\text{cte}$) en un campo gravitatorio uniforme $\vec g=-g\,\hat z$, la presión varía solo con la altura según
> $$
> p(z)=p_0-\rho g z,\qquad\text{o bien}\qquad p=p_0+\rho g h,
> $$
> con $h$ la **profundidad** medida hacia abajo desde el nivel de referencia donde $p=p_0$.

> [!demostracion]
> **Paso 1 — Proyectar la ecuación.** Con $\vec g=-g\,\hat z$ la relación $\nabla p=\rho\vec g$ se escribe componente a componente:
> $$
> \partial_x p=0,\qquad \partial_y p=0,\qquad \partial_z p=-\rho g.
> $$
> Las dos primeras dicen que $p$ **no depende de $x$ ni de $y$**: las superficies de presión constante (isobaras) son horizontales.
>
> **Paso 2 — Integrar en $z$.** Como $p=p(z)$, la tercera ecuación es una EDO ordinaria con $\rho$ constante:
> $$
> \frac{dp}{dz}=-\rho g\;\Longrightarrow\;\int_{p_0}^{p}dp'=-\rho g\int_{0}^{z}dz'\;\Longrightarrow\;p-p_0=-\rho g z.
> $$
> Luego $p(z)=p_0-\rho g z$.
>
> **Paso 3 — En términos de profundidad.** Definiendo la profundidad $h=-z$ (positiva hacia abajo desde el origen),
> $$
> p=p_0+\rho g h.
> $$
> La presión crece linealmente con la profundidad; cada $10\ \text{m}$ de agua añaden $\approx 1\ \text{atm}$. $\blacksquare$

### Principio de Arquímedes

> [!teorema] Principio de Arquímedes
> Sobre un cuerpo de volumen $V$ totalmente sumergido en un fluido en reposo de densidad $\rho$ actúa una fuerza de **empuje** vertical, hacia arriba, igual al peso del fluido desplazado:
> $$
> \vec E=\rho g V\,\hat z.
> $$

> [!demostracion]
> **Paso 1 — Empuje como integral de presión.** La presión actúa normal a la superficie $S$ del cuerpo, empujando hacia adentro ($-\hat n$, con $\hat n$ normal exterior). La fuerza neta de presión es
> $$
> \vec E=-\oint_S p\,\hat n\,dA.
> $$
>
> **Paso 2 — Teorema del gradiente.** El teorema del gradiente (caso vectorial del de la divergencia) afirma que $\oint_S p\,\hat n\,dA=\int_V\nabla p\,dV$. En componentes se sigue de Gauss aplicado al campo $p\,\hat e_i$: $\oint_S p\,n_i\,dA=\int_V\partial_i p\,dV$. Por tanto
> $$
> \vec E=-\int_V\nabla p\,dV.
> $$
>
> **Paso 3 — Sustituir la hidrostática.** Dentro del volumen ocupado por el cuerpo, la presión es la que tendría el fluido allí, que cumple $\nabla p=\rho\vec g=-\rho g\,\hat z$. Entonces
> $$
> \vec E=-\int_V(-\rho g\,\hat z)\,dV=\rho g\,\hat z\int_V dV=\rho g V\,\hat z.
> $$
>
> **Paso 4 — Interpretación.** $\rho g V$ es el peso del fluido que ocuparía el volumen $V$: el empuje es igual y opuesto al peso del fluido desplazado, dirigido hacia arriba. $\blacksquare$

### Atmósfera isoterma

Cuando el fluido es **compresible**, $\rho$ deja de ser constante y hay que cerrar el sistema con una ecuación de estado.

> [!corolario] Ley barométrica isoterma
> Para un **gas ideal** $p=\rho RT/M$ a temperatura $T$ constante bajo gravedad uniforme, la presión decae **exponencialmente** con la altura:
> $$
> p(z)=p_0\,e^{-Mgz/RT},
> $$
> con $M$ la masa molar y $R$ la constante de los gases.

> [!demostracion]
> **Paso 1 — Eliminar la densidad.** De la ecuación de estado $p=\rho RT/M$ despejamos $\rho=\dfrac{Mp}{RT}$. La hidrostática $dp/dz=-\rho g$ queda
> $$
> \frac{dp}{dz}=-\frac{Mg}{RT}\,p.
> $$
>
> **Paso 2 — EDO de variables separables.** Con $T$ constante, $\dfrac{dp}{p}=-\dfrac{Mg}{RT}\,dz$. Integrando desde $z=0$ (donde $p=p_0$):
> $$
> \int_{p_0}^{p}\frac{dp'}{p'}=-\frac{Mg}{RT}\int_0^z dz'\;\Longrightarrow\;\ln\frac{p}{p_0}=-\frac{Mg}{RT}\,z.
> $$
>
> **Paso 3 — Exponenciar.** Por tanto
> $$
> p(z)=p_0\,e^{-Mgz/RT}=p_0\,e^{-z/H},\qquad H=\frac{RT}{Mg},
> $$
> donde $H$ es la **altura de escala** (la altura en la que la presión cae un factor $e$). Para aire a $T\approx 288\ \text{K}$ resulta $H\approx 8{,}4\ \text{km}$. $\blacksquare$

> [!warning] Alcance del modelo
> El **flujo ideal** ($\vec v\neq 0$ con $\mu=0$) es una **idealización**: cerca de una pared la viscosidad siempre importa, por pequeña que sea, y genera la [[5 Flujo Viscoso/index | capa límite]] donde no vale la condición de deslizamiento. En cambio, la **hidrostática es exacta** para un fluido en reposo: no es una aproximación, porque al ser $\vec v=0$ también se anula el término viscoso $\mu\nabla^2\vec v=0$. Por eso $\nabla p=\rho\vec g$ rige por igual a fluidos ideales y reales mientras no haya movimiento.

---

## Ejemplo

> [!ejemplo] Presión en el fondo de una piscina
> Una piscina de agua ($\rho=1{,}00\times 10^{3}\ \text{kg/m}^3$) tiene una profundidad de $h=3{,}00\ \text{m}$. La presión atmosférica en la superficie es $p_0=1{,}013\times 10^{5}\ \text{Pa}$ y $g=9{,}81\ \text{m/s}^2$.
>
> (a) ¿Cuál es la presión absoluta en el fondo?
> (b) ¿Qué empuje sufre una boya de volumen $V=2{,}00\times 10^{-2}\ \text{m}^3$ totalmente sumergida?

> [!solucion]
> **(a) Presión en el fondo.** Aplicamos la ley hidrostática $p=p_0+\rho g h$ deducida arriba:
> $$
> p=p_0+\rho g h=1{,}013\times 10^{5}+(1{,}00\times 10^{3})(9{,}81)(3{,}00)\ \text{Pa}.
> $$
> El término hidrostático vale $\rho g h=2{,}943\times 10^{4}\ \text{Pa}$, de modo que
> $$
> p=1{,}013\times 10^{5}+0{,}2943\times 10^{5}=1{,}307\times 10^{5}\ \text{Pa}\approx 1{,}29\ \text{atm}.
> $$
> A solo $3\ \text{m}$ la presión ya supera en casi un $30\%$ a la atmosférica.
>
> **(b) Empuje sobre la boya.** Por el principio de Arquímedes, $\vec E=\rho g V\,\hat z$, con módulo
> $$
> E=\rho g V=(1{,}00\times 10^{3})(9{,}81)(2{,}00\times 10^{-2})=196\ \text{N},
> $$
> dirigido verticalmente hacia arriba. Equivale al peso de $20{,}0\ \text{kg}$ de agua, que es justo la masa de agua desplazada por la boya. $\blacksquare$

---

## Resumen

> [!resumen] Ecuación de Euler e hidrostática
>
> | Concepto | Expresión | Condición |
> |---|---|---|
> | Euler (fluido ideal) | $\rho\,D\vec v/Dt=-\nabla p+\rho\vec g$ | $\mu=0$ |
> | Lamb–Gromeka | $\partial_t\vec v+\nabla(\tfrac12 v^2)-\vec v\times\vec\omega=-\tfrac1\rho\nabla p+\vec g$ | $\vec\omega=\nabla\times\vec v$ |
> | Hidrostática | $\nabla p=\rho\vec g$ | $\vec v=0$ |
> | Presión hidrostática | $p=p_0+\rho g h$ | $\rho=\text{cte}$ |
> | Arquímedes | $\vec E=\rho g V\,\hat z$ | cuerpo sumergido |
> | Atmósfera isoterma | $p=p_0\,e^{-Mgz/RT}$ | gas ideal, $T=\text{cte}$ |
>
> Condición de pared del fluido ideal: solo $\vec v\cdot\hat n$ (deslizamiento, no adherencia).

> [!corolario] Idea central
> La ecuación de Euler es el esqueleto de la dinámica sin fricción: su forma de Lamb–Gromeka abre la puerta a [[Ecuacion de Bernoulli | Bernoulli]] y a la [[Vorticidad y Teoremas | vorticidad]], mientras que su límite estático $\vec v=0$ recupera **toda la hidrostática** (presión con la profundidad, Arquímedes, ley barométrica) como un simple corolario exacto.

> [!referencia] Bibliografía
> - **L. D. Landau y E. M. Lifshitz**, *Mecánica de Fluidos* (Curso de Física Teórica, Vol. 6), §§2–3.
> - **G. K. Batchelor**, *An Introduction to Fluid Dynamics*, cap. 1 y 3 (hidrostática y fluido ideal).
