---
title: Vorticidad y Teoremas
tags:
  - fluidos
  - teoria
  - flujo-ideal
draft: false
aliases:
  - Vorticidad y teoremas
  - Teorema de Kelvin
  - Teoremas de Helmholtz
---

# Vorticidad y Teoremas $\dfrac{D\vec\omega}{Dt}=(\vec\omega\cdot\nabla)\vec v,\qquad \dfrac{D\Gamma}{Dt}=0$

> [!definicion]
> La **vorticidad** es el campo vectorial $\vec\omega=\nabla\times\vec v$, que mide la rotación local del fluido ([[Deformacion y Vorticidad]]). En un **flujo ideal** ($\mu=0$), **incompresible** ($\nabla\cdot\vec v=0$) y **barotrópico** (la densidad es función solo de la presión, de modo que $\nabla\times(\nabla p/\rho)=0$) con fuerza de cuerpo conservativa, la vorticidad obedece la **ecuación de vorticidad**
> $$\frac{D\vec\omega}{Dt}=(\vec\omega\cdot\nabla)\vec v,$$
> y la **circulación** $\Gamma=\oint_{C(t)}\vec v\cdot d\vec l$ sobre un circuito **material** se conserva: $D\Gamma/Dt=0$ (**teorema de Kelvin**). De ahí siguen los **teoremas de Helmholtz** sobre líneas y tubos de vórtice.

---

> [!info]
> **Cuarta nota de la sección [[4 Flujo Ideal/index | Flujo Ideal]].** Cierra el capítulo: tras la [[Ecuacion de Euler]], la [[Ecuacion de Bernoulli]] y el [[Flujo Potencial]], aquí se demuestra **por qué** un flujo ideal que arranca irrotacional sigue siéndolo —justificando el uso del potencial $\vec v=\nabla\phi$—. Hermanas: [[Flujo Potencial]], [[Ecuacion de Euler]]. Usa la cinemática de [[Deformacion y Vorticidad]] (definición de $\vec\omega$, tubos y líneas de vórtice).
> **Referencia.** Landau-Lifshitz, Vol. 6, §§7–8 ("Conservación de la circulación", "Flujo potencial"); Batchelor, cap. 5; Acheson, cap. 5.

---

## En qué consiste

> [!teoria] El rotacional de Euler borra la presión
> La ecuación de [[Ecuacion de Euler | Euler]] en **forma de Lamb** separa la parte gradiente de la parte rotacional:
> $$\partial_t\vec v+\nabla\!\left(\tfrac12 v^2\right)-\vec v\times\vec\omega=-\frac1\rho\nabla p+\vec g.$$
> Tomar el **rotacional** ($\nabla\times$) aniquila de un golpe los tres términos gradiente: $\nabla\times\nabla(\tfrac12 v^2)=0$, $\nabla\times(\nabla p/\rho)=0$ (barotrópico) y $\nabla\times\vec g=0$ ($\vec g=-\nabla\Phi$ conservativa). Solo sobreviven $\partial_t\vec\omega$ y $-\nabla\times(\vec v\times\vec\omega)$. La presión **desaparece**: la vorticidad evoluciona sin que la presión la afecte. Lo que queda es transporte puro más el término de **estiramiento** $(\vec\omega\cdot\nabla)\vec v$.

> [!teorema] Ecuación de la vorticidad
> Para flujo ideal, incompresible ($\nabla\cdot\vec v=0$) y barotrópico con $\vec g$ conservativa,
> $$\frac{D\vec\omega}{Dt}=\partial_t\vec\omega+(\vec v\cdot\nabla)\vec\omega=(\vec\omega\cdot\nabla)\vec v.$$

> [!demostracion]
> **Paso 1 — Rotacional de la forma de Lamb.** Aplicamos $\nabla\times$ a
> $$\partial_t\vec v+\nabla\!\left(\tfrac12 v^2\right)-\vec v\times\vec\omega=-\frac1\rho\nabla p-\nabla\Phi,\qquad \vec g=-\nabla\Phi.$$
> Como el rotacional de todo gradiente es nulo, $\nabla\times\nabla(\tfrac12 v^2)=0$ y $\nabla\times\nabla\Phi=0$. Para el término de presión, en el caso barotrópico existe la función $\mathcal P$ con $\nabla\mathcal P=\nabla p/\rho$, luego $\nabla\times(\nabla p/\rho)=\nabla\times\nabla\mathcal P=0$. En índices, con el convenio de suma, $[\nabla\times\nabla f]_i=\epsilon_{ijk}\,\partial_j\partial_k f=0$ porque $\epsilon_{ijk}$ es antisimétrico en $j,k$ y $\partial_j\partial_k f$ es simétrico. Queda
> $$\partial_t\vec\omega-\nabla\times(\vec v\times\vec\omega)=0.$$
>
> **Paso 2 — Identidad del triple producto rotacional.** Desarrollamos $\nabla\times(\vec v\times\vec\omega)$ con índices. Usando $[\vec A\times\vec B]_k=\epsilon_{klm}A_l B_m$,
> $$[\nabla\times(\vec v\times\vec\omega)]_i=\epsilon_{ijk}\,\partial_j(\epsilon_{klm}v_l\omega_m)=\epsilon_{ijk}\epsilon_{klm}\,\partial_j(v_l\omega_m).$$
> Con la identidad $\epsilon_{ijk}\epsilon_{klm}=\epsilon_{kij}\epsilon_{klm}=\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl}$,
> $$=(\delta_{il}\delta_{jm}-\delta_{im}\delta_{jl})\,\partial_j(v_l\omega_m)=\partial_j(v_i\omega_j)-\partial_j(v_j\omega_i).$$
> Aplicando la regla del producto,
> $$=\big(\omega_j\partial_j v_i+v_i\,\partial_j\omega_j\big)-\big(\omega_i\,\partial_j v_j+v_j\partial_j\omega_i\big).$$
>
> **Paso 3 — Anular las divergencias.** La vorticidad es siempre solenoidal: $\nabla\cdot\vec\omega=\partial_j\omega_j=\partial_j(\epsilon_{jkl}\partial_k v_l)=\epsilon_{jkl}\partial_j\partial_k v_l=0$ (mismo argumento de antisimetría/simetría que en el Paso 1). Y por **incompresibilidad** $\nabla\cdot\vec v=\partial_j v_j=0$. Eliminados esos dos términos,
> $$[\nabla\times(\vec v\times\vec\omega)]_i=\omega_j\partial_j v_i-v_j\partial_j\omega_i=[(\vec\omega\cdot\nabla)\vec v]_i-[(\vec v\cdot\nabla)\vec\omega]_i.$$
> En forma vectorial: $\nabla\times(\vec v\times\vec\omega)=(\vec\omega\cdot\nabla)\vec v-(\vec v\cdot\nabla)\vec\omega$.
>
> **Paso 4 — Reagrupar en derivada material.** Sustituyendo en el Paso 1,
> $$\partial_t\vec\omega-\big[(\vec\omega\cdot\nabla)\vec v-(\vec v\cdot\nabla)\vec\omega\big]=0\;\Longrightarrow\;\underbrace{\partial_t\vec\omega+(\vec v\cdot\nabla)\vec\omega}_{D\vec\omega/Dt}=(\vec\omega\cdot\nabla)\vec v.$$
> $$\frac{D\vec\omega}{Dt}=(\vec\omega\cdot\nabla)\vec v.\qquad\blacksquare$$

> [!proposicion] Estiramiento e inclinación de tubos de vórtice
> El término $(\vec\omega\cdot\nabla)\vec v$ es la **fuente** de toda la dinámica: es la derivada direccional de $\vec v$ a lo largo de $\vec\omega$. Alíneando un eje local con $\vec\omega$ (digamos $\hat z$), $\vec\omega=\omega\,\hat z$ da
> $$(\vec\omega\cdot\nabla)\vec v=\omega\,\partial_z\vec v=\omega\Big(\underbrace{\partial_z v_z}_{\text{estiramiento}}\,\hat z+\underbrace{\partial_z v_x\,\hat x+\partial_z v_y\,\hat y}_{\text{inclinación}}\Big).$$
> - **Estiramiento** ($\partial_z v_z>0$): si el fluido se acelera a lo largo del tubo de vórtice, este se **estira** y adelgaza; como su momento angular se conserva (igual que una patinadora que recoge los brazos), $\omega$ **aumenta**. Este *vortex stretching* es el motor de la cascada de la turbulencia tridimensional.
> - **Inclinación** ($\partial_z v_x,\partial_z v_y$): un gradiente transversal **reorienta** el vector $\vec\omega$ hacia otras direcciones.
> En **flujo plano** $\vec v=(v_x,v_y,0)$ se tiene $\vec\omega=\omega_z\hat z$ y $(\vec\omega\cdot\nabla)\vec v=\omega_z\partial_z\vec v=0$: el estiramiento **no existe en 2D**, donde $D\omega_z/Dt=0$ (la vorticidad se transporta como un escalar pasivo).

> [!corolario] Un flujo ideal que arranca irrotacional sigue irrotacional
> La ecuación es **homogénea** en $\vec\omega$: el lado derecho $(\vec\omega\cdot\nabla)\vec v$ se anula donde $\vec\omega=0$. Si en $t=0$ el campo es irrotacional, $\vec\omega(\vec x,0)=0$ en todo el dominio, entonces $D\vec\omega/Dt=0$ y, siguiendo cada partícula, $\vec\omega$ permanece nula para todo $t$. Por eso un flujo ideal que parte del **reposo** (o de una corriente uniforme) es irrotacional y admite potencial $\vec v=\nabla\phi$ con $\nabla^2\phi=0$ ([[Flujo Potencial]]). $\blacksquare$

---

## Teorema de circulación de Kelvin

> [!teorema] Conservación de la circulación (Kelvin)
> Sea $C(t)$ un **circuito material** (formado siempre por las mismas partículas) que se mueve con el fluido. En flujo ideal y barotrópico con $\vec g$ conservativa, la circulación
> $$\Gamma=\oint_{C(t)}\vec v\cdot d\vec l\qquad\text{cumple}\qquad \frac{D\Gamma}{Dt}=0.$$
> La circulación de un lazo que viaja con el fluido es **constante**.

![[kelvin_circulacion.svg|480]]
*Teorema de Kelvin: el circuito material se deforma y es arrastrado por el flujo, pero la circulación $\Gamma=\oint_{C}\vec v\cdot d\vec l$ se conserva en el tiempo.*

> [!demostracion]
> **Paso 1 — Derivar la integral material.** Al seguir el circuito, tanto $\vec v$ como el elemento $d\vec l$ cambian con el tiempo. Por la regla del producto bajo la derivada material,
> $$\frac{D\Gamma}{Dt}=\frac{D}{Dt}\oint_{C(t)}\vec v\cdot d\vec l=\oint_C\frac{D\vec v}{Dt}\cdot d\vec l+\oint_C\vec v\cdot\frac{D(d\vec l)}{Dt}.$$
>
> **Paso 2 — Primer término (aceleración es un gradiente).** Por la ecuación de Euler barotrópica,
> $$\frac{D\vec v}{Dt}=-\frac1\rho\nabla p+\vec g=-\nabla\mathcal P-\nabla\Phi=-\nabla(\mathcal P+\Phi),\qquad \nabla\mathcal P=\frac{\nabla p}{\rho}.$$
> La aceleración es un **gradiente puro**. Su integral sobre un lazo **cerrado** se anula, pues $\oint_C\nabla f\cdot d\vec l=\oint_C df=0$ (la función vuelve a su valor inicial). Por tanto
> $$\oint_C\frac{D\vec v}{Dt}\cdot d\vec l=-\oint_C d(\mathcal P+\Phi)=0.$$
>
> **Paso 3 — Segundo término (estiramiento del elemento de línea).** Un elemento material $d\vec l$ que une dos partículas vecinas se deforma según la diferencia de sus velocidades:
> $$\frac{D(d\vec l)}{Dt}=d\vec v.$$
> En efecto, si $d\vec l=\vec x_B-\vec x_A$, entonces $\frac{D(d\vec l)}{Dt}=\vec v_B-\vec v_A=d\vec v$. Luego
> $$\oint_C\vec v\cdot\frac{D(d\vec l)}{Dt}=\oint_C\vec v\cdot d\vec v=\oint_C d\!\left(\tfrac12 v^2\right)=0,$$
> de nuevo por ser la integral cerrada de un diferencial exacto ($\vec v\cdot d\vec v=\tfrac12\,d(v\cdot v)$).
>
> **Paso 4 — Sumar.** Ambos términos se anulan independientemente:
> $$\frac{D\Gamma}{Dt}=0+0=0.\qquad\blacksquare$$

> [!info] Kelvin ⇔ irrotacionalidad
> Kelvin es la versión integral del corolario anterior. Por **Stokes**, $\Gamma=\oint_C\vec v\cdot d\vec l=\int_S(\nabla\times\vec v)\cdot d\vec A=\int_S\vec\omega\cdot d\vec A$. Si todo circuito material conserva su $\Gamma$ y al inicio todos valen cero (flujo desde el reposo), seguirán valiendo cero, luego $\vec\omega=0$ en toda superficie: el flujo permanece irrotacional.

---

## Teoremas de Helmholtz

> [!teorema] Teoremas de Helmholtz (vórtices en flujo ideal)
> En flujo ideal, incompresible y barotrópico:
> 1. **Las líneas de vórtice son líneas materiales:** las partículas que en un instante forman una línea de vórtice la siguen formando después; los vórtices se mueven **con** el fluido.
> 2. **La intensidad de un tubo de vórtice se conserva:** el flujo de vorticidad $\Gamma=\displaystyle\int_S\vec\omega\cdot d\vec A$ a través de cualquier sección $S$ del tubo es **el mismo a lo largo del tubo** y **constante en el tiempo**.
> 3. **Un tubo de vórtice no termina en el fluido:** o se cierra sobre sí mismo (anillo de vórtice), o se apoya en una frontera del dominio.

> [!demostracion] Apoyo en Kelvin y en $\nabla\cdot\vec\omega=0$
> **(1) Líneas materiales.** Considérese una pequeña superficie $S$ tangente a las líneas de vórtice, de modo que $\vec\omega\cdot d\vec A=0$ sobre ella y $\Gamma=\oint_{\partial S}\vec v\cdot d\vec l=0$. Por **Kelvin**, $\Gamma$ se mantiene nula al avanzar el circuito material $\partial S$. Como esto vale para todo lazo apoyado en la superficie arrastrada, la superficie sigue siendo tangente a $\vec\omega$: las líneas de vórtice son transportadas por el fluido. $\blacksquare$
>
> **(2) Intensidad del tubo.** *Constancia a lo largo del tubo:* dado que $\nabla\cdot\vec\omega=0$, integrando sobre el volumen $V$ encerrado entre dos secciones $S_1,S_2$ de un mismo tubo (la pared lateral no aporta flujo, pues $\vec\omega$ es tangente a ella) y aplicando Gauss,
> $$0=\int_V\nabla\cdot\vec\omega\,dV=\oint_{\partial V}\vec\omega\cdot d\vec A=-\!\int_{S_1}\vec\omega\cdot d\vec A+\int_{S_2}\vec\omega\cdot d\vec A\;\Rightarrow\;\Gamma_1=\Gamma_2.$$
> *Constancia en el tiempo:* por (1) el borde de cada sección es un circuito material, y por **Kelvin** su $\Gamma$ no cambia. $\blacksquare$
>
> **(3) No termina en el fluido.** Si un tubo terminara abruptamente, su sección final tendría $\Gamma=0$ mientras el resto tiene $\Gamma\neq0$, contradiciendo (2). Luego debe cerrarse o alcanzar la frontera. $\blacksquare$

---

## Ejemplo

> [!ejemplo] Vortex stretching: estirar un tubo intensifica su rotación
> Un tubo de vórtice recto, de sección circular de radio $r_1$, vorticidad uniforme $\omega_1$ axial y longitud $L_1$, es estirado por el flujo hasta $L_2>L_1$ manteniéndose el fluido **incompresible**.

> [!solucion]
> **Paso 1 — Volumen constante (incompresible).** El tubo material conserva su volumen:
> $$\pi r_1^2\,L_1=\pi r_2^2\,L_2\;\Rightarrow\;r_2^2=r_1^2\,\frac{L_1}{L_2}.$$
> Al alargarse ($L_2>L_1$), la sección se **estrecha**: $r_2<r_1$.
>
> **Paso 2 — Intensidad constante (Helmholtz 2 / Kelvin).** La intensidad del tubo se conserva, $\Gamma=\omega\cdot(\text{área})=$ cte:
> $$\omega_1\,\pi r_1^2=\omega_2\,\pi r_2^2\;\Rightarrow\;\omega_2=\omega_1\,\frac{r_1^2}{r_2^2}.$$
>
> **Paso 3 — Combinar.** Sustituyendo $r_1^2/r_2^2=L_2/L_1$:
> $$\boxed{\;\omega_2=\omega_1\,\frac{L_2}{L_1}\;}$$
> La vorticidad crece en proporción directa al estiramiento. Por ejemplo, si el tubo se estira al **doble** ($L_2=2L_1$), su sección se reduce a la mitad y la vorticidad **se duplica**, $\omega_2=2\,\omega_1$. Es la misma física que la patinadora: al concentrar el momento angular en menos radio, la rotación se acelera. Este mecanismo —ausente en 2D— es la raíz de la intensificación de remolinos en la turbulencia tridimensional.

> [!ejemplo] Por qué un flujo desde el reposo es irrotacional
> Un cuerpo se mueve a través de un fluido ideal en reposo. Lejos del cuerpo $\vec v=0$, luego $\vec\omega=0$ y todo circuito material allí tiene $\Gamma=0$.

> [!solucion]
> Cada circuito material que rodea al cuerpo proviene de una región donde inicialmente $\Gamma=0$. Por **Kelvin**, $\Gamma$ se mantiene nula al ser arrastrado el circuito junto al cuerpo. Como esto vale para **todo** lazo, por Stokes $\int_S\vec\omega\cdot d\vec A=0$ sobre cualquier superficie, de donde $\vec\omega=0$ en todo el campo. El flujo es **irrotacional** y se resuelve con potencial $\vec v=\nabla\phi$, $\nabla^2\phi=0$ ([[Flujo Potencial]]). Esto **justifica** el capítulo del flujo potencial: no es una hipótesis arbitraria, sino una **consecuencia** de Kelvin para flujos que arrancan en reposo. $\blacksquare$

> [!warning] El alcance: solo flujo ideal y barotrópico
> Kelvin, Helmholtz y la permanencia de la irrotacionalidad **dependen** de tres hipótesis. Si se rompen, la vorticidad se **crea**:
> - **Viscosidad** ($\mu\neq0$): añade a la ecuación un término difusivo $\nu\nabla^2\vec\omega$, de modo que $D\vec\omega/Dt=(\vec\omega\cdot\nabla)\vec v+\nu\nabla^2\vec\omega$. La vorticidad **difunde** desde las paredes hacia el fluido (no deslizamiento), y la circulación de un circuito material **decae**. Por eso las **estelas** reales tienen vorticidad aunque la corriente entrante sea irrotacional.
> - **Baroclinicidad** ($\nabla\rho\times\nabla p\neq0$): si el flujo **no** es barotrópico, $\nabla\times(\nabla p/\rho)=\tfrac1{\rho^2}\nabla\rho\times\nabla p\neq0$ aparece como término fuente $+\tfrac1{\rho^2}\nabla\rho\times\nabla p$ en la ecuación de vorticidad. Genera rotación allí donde los gradientes de densidad y presión no son paralelos (convección, frentes atmosféricos, *baroclinic instability*).
> En el [[5 Flujo Viscoso/index | Capítulo 5]] la viscosidad reescribe esta historia cerca de las paredes.

---

## Resumen

> [!resumen]
> | Resultado | Enunciado | Hipótesis | Sirve para |
> |:---|:---|:---|:---|
> | Ecuación de vorticidad | $\dfrac{D\vec\omega}{Dt}=(\vec\omega\cdot\nabla)\vec v$ | ideal, incompresible, barotrópico, $\vec g$ conservativa | dinámica de $\vec\omega$ sin presión |
> | Vortex stretching | estirar el tubo $\Rightarrow$ $\omega\uparrow$ ($\omega_2=\omega_1 L_2/L_1$) | incompresible, 3D | cascada turbulenta |
> | Kelvin | $\dfrac{D\Gamma}{Dt}=0$, $\Gamma=\oint_{C(t)}\vec v\cdot d\vec l$ | ideal, barotrópico | conservación de circulación |
> | Helmholtz 1 | líneas de vórtice $=$ líneas materiales | ideal, barotrópico | vórtices viajan con el fluido |
> | Helmholtz 2 | intensidad del tubo $\Gamma=\int_S\vec\omega\cdot d\vec A$ constante | ideal, $\nabla\cdot\vec\omega=0$ | tubos de igual fuerza |
> | Helmholtz 3 | tubo no termina en el fluido | $\nabla\cdot\vec\omega=0$ | anillos / fronteras |

> [!corolario] La frase para recordar
> En un fluido **ideal y barotrópico**, la vorticidad es **indestructible y materialmente fiel**: no se crea ni se destruye, y los tubos de vórtice viajan congelados en el fluido conservando su intensidad. De ahí que un flujo que **parte del reposo** sea irrotacional —y se resuelva con [[Flujo Potencial | potencial]]—. La **viscosidad** y la **baroclinicidad** son las únicas que, rompiendo las hipótesis, **engendran** vorticidad: ese es el puente hacia el [[5 Flujo Viscoso/index | flujo viscoso]].

> [!referencia]
> Landau-Lifshitz, *Mecánica de Fluidos* (Vol. 6), §§7–8 ("Conservación de la circulación", "Flujo potencial"). Batchelor, *An Introduction to Fluid Dynamics*, cap. 5 ("Flow of effectively inviscid fluid"); Acheson, *Elementary Fluid Dynamics*, cap. 5 ("Vortex motion").
