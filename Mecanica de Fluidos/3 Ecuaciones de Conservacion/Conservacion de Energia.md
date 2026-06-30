---
title: Conservación de Energía
order: 4
tags:
  - fluidos
  - teoria
  - conservacion
draft: false
aliases:
  - Conservación de energía
  - Ecuación de la energía
  - Disipación viscosa
---

# Conservación de Energía $\rho\dfrac{D}{Dt}\!\left(e+\tfrac12 v^2\right)=\nabla\cdot(\boldsymbol\sigma\cdot\vec v)+\rho\vec g\cdot\vec v-\nabla\cdot\vec q$

---

> [!definicion] Ecuación de la energía total
> Para una partícula de fluido, la tasa de cambio de su **energía total específica** $E=e+\tfrac12 v^2$ (interna $e$ más cinética $\tfrac12 v^2$) iguala la potencia de las fuerzas de superficie y másicas más el calor neto recibido por conducción:
> $$\boxed{\;\rho\,\frac{D}{Dt}\!\left(e+\tfrac12 v^2\right)=\partial_j(\sigma_{ij}v_i)+\rho\,g_i v_i-\partial_j q_j\;}$$
> donde $\sigma_{ij}$ es el tensor de esfuerzos, $g_i$ la gravedad específica, $q_j$ el flujo de calor (ley de Fourier $\vec q=-k\nabla T$) y $\dfrac{D}{Dt}=\partial_t+v_k\partial_k$ la derivada material. Convenio de suma sobre índices repetidos.

---

> [!info] Ubicación y dependencias
> Esta nota pertenece a la sección [[3 Ecuaciones de Conservacion/index | Ecuaciones de Conservación]]. Sus hermanas son [[Ecuaciones de Navier-Stokes]] y [[Conservacion de Momento]]; aquí usamos la relación constitutiva del [[Fluido Newtoniano]] para evaluar la disipación viscosa.
>
> Referencias: Landau & Lifshitz, *Fluid Mechanics* (Vol. 6), §49; Batchelor, *An Introduction to Fluid Dynamics*, cap. 3.

---

## Ejemplo

> [!ejemplo] Disipación en un flujo de Couette
> Considere un flujo plano y estacionario entre dos placas separadas una distancia $h$: la inferior fija y la superior moviéndose a velocidad $U$. El perfil es lineal,
> $$u(y)=\frac{U}{h}\,y,\qquad v=w=0.$$
> Calcule la función de disipación viscosa $\Phi$ y la potencia disipada por unidad de área.

> [!solucion] Cálculo de $\Phi$ y la potencia
> **Paso 1 — Gradiente de velocidad.** El único componente no nulo es
> $$\partial_y u=\frac{\partial u}{\partial y}=\frac{U}{h}.$$
> Por tanto, de las componentes del tensor de velocidad de deformación $e_{ij}=\tfrac12(\partial_j v_i+\partial_i v_j)$, las únicas no nulas son
> $$e_{xy}=e_{yx}=\frac12\,\frac{U}{h}.$$
> Además $e_{kk}=\nabla\cdot\vec v=0$ (incompresible).
>
> **Paso 2 — Disipación newtoniana.** Con $\Phi=2\mu\,e_{ij}e_{ij}+\lambda(e_{kk})^2$ y $e_{kk}=0$:
> $$e_{ij}e_{ij}=e_{xy}^2+e_{yx}^2=2\left(\frac{U}{2h}\right)^2=\frac{U^2}{2h^2}.$$
> $$\Phi=2\mu\cdot\frac{U^2}{2h^2}=\mu\left(\frac{U}{h}\right)^2.$$
> La disipación es **constante** en todo el canal.
>
> **Paso 3 — Potencia por unidad de área.** Integrando $\Phi$ en el espesor $h$:
> $$\dot{W}_{\text{disip}}=\int_0^h \Phi\,dy=\mu\frac{U^2}{h^2}\cdot h=\frac{\mu U^2}{h}.$$
>
> **Números.** Para agua ($\mu\approx 1{,}0\times10^{-3}\ \text{Pa·s}$), $U=1\ \text{m/s}$, $h=1\ \text{mm}=10^{-3}\ \text{m}$:
> $$\dot{W}_{\text{disip}}=\frac{(1{,}0\times10^{-3})(1)^2}{10^{-3}}=1{,}0\ \text{W/m}^2.$$
> Toda esta potencia mecánica se convierte irreversiblemente en calor. $\blacksquare$

---

## En qué consiste

La energía total específica de una partícula de fluido es
$$E=\underbrace{e}_{\text{interna}}+\underbrace{\tfrac12 v^2}_{\text{cinética}},\qquad v^2=v_i v_i.$$
La primera ley de la termodinámica aplicada a un volumen material $V(t)$ dice que la tasa de cambio de $E$ se debe a tres aportes: el trabajo de las fuerzas de superficie $\sigma_{ij}n_j$, el trabajo de las fuerzas másicas $\rho g_i$ y el calor neto entrante por conducción $-q_j n_j$.

![[disipacion_viscosa.svg|440]]
*La cizalla viscosa convierte trabajo mecánico en calor: la función de disipación $\Phi=\tau_{ij}\,\partial_j v_i\ge 0$ es siempre no negativa y calienta el fluido.*

### Energía total a partir del balance integral

> [!demostracion] Forma diferencial de la energía total
> **Paso 1 — Balance integral.** Sobre un volumen material $V(t)$,
> $$\frac{d}{dt}\int_{V}\rho\left(e+\tfrac12 v^2\right)dV=\underbrace{\int_{S}\sigma_{ij}v_i\,n_j\,dS}_{\text{potencia de superficie}}+\underbrace{\int_{V}\rho\,g_i v_i\,dV}_{\text{potencia másica}}-\underbrace{\int_{S}q_j\,n_j\,dS}_{\text{calor saliente}}.$$
>
> **Paso 2 — Lema de transporte para magnitudes específicas.** Por el teorema de transporte de Reynolds combinado con la continuidad, para cualquier campo $\psi$ por unidad de masa,
> $$\frac{d}{dt}\int_{V}\rho\,\psi\,dV=\int_{V}\rho\,\frac{D\psi}{Dt}\,dV.$$
> Con $\psi=e+\tfrac12 v^2$, el lado izquierdo del balance se vuelve $\displaystyle\int_{V}\rho\,\frac{D}{Dt}\!\left(e+\tfrac12 v^2\right)dV$.
>
> **Paso 3 — Conversión de las integrales de superficie.** Por el teorema de la divergencia,
> $$\int_{S}\sigma_{ij}v_i\,n_j\,dS=\int_{V}\partial_j(\sigma_{ij}v_i)\,dV,\qquad \int_{S}q_j\,n_j\,dS=\int_{V}\partial_j q_j\,dV.$$
>
> **Paso 4 — Forma local.** Reuniendo todo en una sola integral de volumen:
> $$\int_{V}\left[\rho\,\frac{D}{Dt}\!\left(e+\tfrac12 v^2\right)-\partial_j(\sigma_{ij}v_i)-\rho\,g_i v_i+\partial_j q_j\right]dV=0.$$
> Como $V(t)$ es arbitrario, el integrando se anula:
> $$\rho\,\frac{D}{Dt}\!\left(e+\tfrac12 v^2\right)=\partial_j(\sigma_{ij}v_i)+\rho\,g_i v_i-\partial_j q_j.\qquad\blacksquare$$

### Ecuación de la energía cinética (auxiliar)

> [!demostracion] Energía cinética a partir de Cauchy
> **Paso 1 — Ecuación de cantidad de movimiento.** La ecuación de [[Conservacion de Momento]] (Cauchy) es
> $$\rho\,\frac{D v_i}{Dt}=\partial_j\sigma_{ij}+\rho\,g_i.$$
>
> **Paso 2 — Producto escalar con $v_i$.** Multiplicamos por $v_i$ y sumamos en $i$:
> $$\rho\,v_i\,\frac{D v_i}{Dt}=v_i\,\partial_j\sigma_{ij}+\rho\,g_i v_i.$$
>
> **Paso 3 — Reconocer la energía cinética.** Como $v_i\dfrac{Dv_i}{Dt}=\dfrac{D}{Dt}\!\left(\tfrac12 v_i v_i\right)=\dfrac{D}{Dt}\!\left(\tfrac12 v^2\right)$:
> $$\boxed{\;\rho\,\frac{D}{Dt}\!\left(\tfrac12 v^2\right)=v_i\,\partial_j\sigma_{ij}+\rho\,g_i v_i\;}$$
> Esta es la **ecuación de la energía mecánica** (cinética). $\blacksquare$

### Ecuación de la energía interna y la disipación

> [!teorema] Energía interna y función de disipación
> Restando la energía cinética de la energía total se aísla la energía interna:
> $$\rho\,\frac{De}{Dt}=\sigma_{ij}\,\partial_j v_i-\partial_j q_j=-p\,\nabla\cdot\vec v+\Phi-\nabla\cdot\vec q,$$
> donde la **función de disipación viscosa** es $\Phi=\tau_{ij}\,\partial_j v_i$, con $\tau_{ij}=\sigma_{ij}+p\,\delta_{ij}$ la parte viscosa del esfuerzo.

> [!demostracion] Aislamiento de la energía interna
> **Paso 1 — Resta.** Partimos de la energía total
> $$\rho\,\frac{D}{Dt}\!\left(e+\tfrac12 v^2\right)=\partial_j(\sigma_{ij}v_i)+\rho\,g_i v_i-\partial_j q_j$$
> y restamos la cinética $\rho\,\frac{D}{Dt}(\tfrac12 v^2)=v_i\,\partial_j\sigma_{ij}+\rho\,g_i v_i$. El término másico $\rho g_i v_i$ se cancela:
> $$\rho\,\frac{De}{Dt}=\partial_j(\sigma_{ij}v_i)-v_i\,\partial_j\sigma_{ij}-\partial_j q_j.$$
>
> **Paso 2 — Regla del producto.** Desarrollamos $\partial_j(\sigma_{ij}v_i)=v_i\,\partial_j\sigma_{ij}+\sigma_{ij}\,\partial_j v_i$. Al restar $v_i\,\partial_j\sigma_{ij}$ queda
> $$\rho\,\frac{De}{Dt}=\sigma_{ij}\,\partial_j v_i-\partial_j q_j.$$
>
> **Paso 3 — Separar presión y viscosidad.** Escribimos $\sigma_{ij}=-p\,\delta_{ij}+\tau_{ij}$:
> $$\sigma_{ij}\,\partial_j v_i=-p\,\delta_{ij}\,\partial_j v_i+\tau_{ij}\,\partial_j v_i=-p\,\partial_i v_i+\tau_{ij}\,\partial_j v_i=-p\,\nabla\cdot\vec v+\Phi.$$
> Hemos usado $\delta_{ij}\,\partial_j v_i=\partial_i v_i=\nabla\cdot\vec v$. Por tanto
> $$\rho\,\frac{De}{Dt}=-p\,\nabla\cdot\vec v+\Phi-\nabla\cdot\vec q,\qquad \Phi=\tau_{ij}\,\partial_j v_i.\qquad\blacksquare$$

El término $-p\,\nabla\cdot\vec v$ es el **trabajo reversible de compresión** (cambia el volumen específico de forma recuperable), mientras que $\Phi$ es la conversión **irreversible** de energía mecánica en calor.

> [!proposicion] Forma cuadrática de $\Phi$ para fluido newtoniano
> Para un [[Fluido Newtoniano]] con $\tau_{ij}=2\mu\,e_{ij}+\lambda\,e_{kk}\,\delta_{ij}$ y $e_{ij}=\tfrac12(\partial_j v_i+\partial_i v_j)$, la disipación es la forma cuadrática
> $$\Phi=\tau_{ij}\,\partial_j v_i=2\mu\,e_{ij}e_{ij}+\lambda(e_{kk})^2.$$

> [!demostracion] Reducción a $e_{ij}$
> **Paso 1 — Simetría de $\tau_{ij}$.** El tensor viscoso newtoniano es simétrico ($\tau_{ij}=\tau_{ji}$). Descomponemos $\partial_j v_i=e_{ij}+\omega_{ij}$ en parte simétrica $e_{ij}=\tfrac12(\partial_j v_i+\partial_i v_j)$ y antisimétrica $\omega_{ij}=\tfrac12(\partial_j v_i-\partial_i v_j)$.
>
> **Paso 2 — La parte antisimétrica no contribuye.** La contracción de un tensor simétrico con uno antisimétrico es nula: $\tau_{ij}\omega_{ij}=0$. Luego
> $$\Phi=\tau_{ij}\,\partial_j v_i=\tau_{ij}\,e_{ij}.$$
>
> **Paso 3 — Sustituir la relación constitutiva.**
> $$\Phi=(2\mu\,e_{ij}+\lambda\,e_{kk}\,\delta_{ij})\,e_{ij}=2\mu\,e_{ij}e_{ij}+\lambda\,e_{kk}\,(\delta_{ij}e_{ij}).$$
> Como $\delta_{ij}e_{ij}=e_{kk}$:
> $$\Phi=2\mu\,e_{ij}e_{ij}+\lambda(e_{kk})^2.\qquad\blacksquare$$

### No negatividad de la disipación

> [!teorema] $\Phi\ge 0$ (segunda ley)
> Bajo $\mu\ge 0$ y la condición de viscosidad de volumen $\zeta=\lambda+\tfrac23\mu\ge 0$ (o la hipótesis de Stokes $\lambda=-\tfrac23\mu$, que da $\zeta=0$), la disipación viscosa es siempre no negativa:
> $$\Phi\ge 0.$$

> [!demostracion] Suma de cuadrados
> **Paso 1 — Descomposición deviatórica.** Separamos $e_{ij}$ en parte sin traza (desviadora) más parte isótropa:
> $$e_{ij}=\underbrace{\left(e_{ij}-\tfrac13 e_{kk}\,\delta_{ij}\right)}_{d_{ij},\ \ d_{kk}=0}+\tfrac13 e_{kk}\,\delta_{ij}.$$
>
> **Paso 2 — Contracción.** Usando $d_{ij}\delta_{ij}=0$ y $\delta_{ij}\delta_{ij}=3$:
> $$e_{ij}e_{ij}=d_{ij}d_{ij}+\tfrac13(e_{kk})^2.$$
>
> **Paso 3 — Reagrupar $\Phi$.** Sustituyendo en $\Phi=2\mu\,e_{ij}e_{ij}+\lambda(e_{kk})^2$:
> $$\Phi=2\mu\,d_{ij}d_{ij}+\left(\tfrac23\mu+\lambda\right)(e_{kk})^2=2\mu\,d_{ij}d_{ij}+\zeta\,(\nabla\cdot\vec v)^2.$$
>
> **Paso 4 — Signo.** $d_{ij}d_{ij}=\sum_{i,j}d_{ij}^2\ge 0$ y $(\nabla\cdot\vec v)^2\ge 0$ son sumas de cuadrados. Con $\mu\ge0$ y $\zeta\ge0$, ambos términos son no negativos:
> $$\Phi=\underbrace{2\mu\,d_{ij}d_{ij}}_{\ge0}+\underbrace{\zeta\,(\nabla\cdot\vec v)^2}_{\ge0}\ge 0.\qquad\blacksquare$$

> [!corolario] Vínculo con la entropía
> La ecuación de la entropía específica $s$ se obtiene de la energía interna; resulta
> $$\rho T\,\frac{Ds}{Dt}=\Phi-\nabla\cdot\vec q+\frac{1}{T}\,k\,\nabla T\cdot\nabla T,$$
> y la producción de entropía debida a la viscosidad es $\Phi/T\ge 0$. La condición $\mu\ge 0$ es exactamente la que garantiza el cumplimiento de la **segunda ley**: la viscosidad solo disipa energía mecánica en calor, nunca la crea.

> [!warning] Flujo incompresible: desacople térmico
> En flujo **incompresible** $\nabla\cdot\vec v=0$, de modo que el término reversible $-p\,\nabla\cdot\vec v$ se anula. La energía mecánica se desacopla de la térmica: la dinámica (velocidad y presión) puede resolverse mediante [[Ecuaciones de Navier-Stokes]] **sin** la ecuación de energía, que se integra luego como una ecuación de transporte para $T$. La disipación $\Phi=2\mu\,d_{ij}d_{ij}\ge 0$ **siempre** está presente y calienta el fluido, aun cuando no afecte al campo de velocidades.

---

## Resumen

| Concepto | Expresión | Comentario |
|---|---|---|
| Energía total | $E=e+\tfrac12 v^2$ | interna + cinética específicas |
| Energía total (local) | $\rho\dfrac{D}{Dt}(e+\tfrac12 v^2)=\partial_j(\sigma_{ij}v_i)+\rho g_i v_i-\partial_j q_j$ | 1ª ley local |
| Energía cinética | $\rho\dfrac{D}{Dt}(\tfrac12 v^2)=v_i\partial_j\sigma_{ij}+\rho g_i v_i$ | Cauchy $\cdot\,v_i$ |
| Energía interna | $\rho\dfrac{De}{Dt}=-p\,\nabla\cdot\vec v+\Phi-\nabla\cdot\vec q$ | total $-$ cinética |
| Disipación viscosa | $\Phi=\tau_{ij}\partial_j v_i=2\mu\,e_{ij}e_{ij}+\lambda(e_{kk})^2$ | newtoniano |
| No negatividad | $\Phi=2\mu\,d_{ij}d_{ij}+\zeta(\nabla\cdot\vec v)^2\ge0$ | con $\mu\ge0$, $\zeta\ge0$ |
| Conducción | $\vec q=-k\nabla T$ | ley de Fourier |
| Couette | $\Phi=\mu(U/h)^2$; \ $\dot W=\mu U^2/h$ | potencia por área |

> [!corolario] Síntesis
> La energía total se conserva localmente como trabajo de fuerzas más calor. Al separarla en partes cinética e interna aparece la **disipación viscosa** $\Phi\ge 0$: un término irreversible que transfiere energía mecánica a interna (calor). El trabajo de presión $-p\,\nabla\cdot\vec v$ es reversible y se anula si el flujo es incompresible. La condición $\mu\ge 0$ es la manifestación local de la segunda ley.

> [!referencia] Fuentes
> - L. D. Landau y E. M. Lifshitz, *Fluid Mechanics* (Course of Theoretical Physics, Vol. 6), §49 (ecuación de la energía y disipación).
> - G. K. Batchelor, *An Introduction to Fluid Dynamics*, cap. 3 (balances de energía y función de disipación).
