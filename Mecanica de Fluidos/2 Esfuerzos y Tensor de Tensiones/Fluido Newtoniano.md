---
title: Fluido Newtoniano
order: 3
tags:
  - fluidos
  - teoria
  - esfuerzos
draft: false
aliases:
  - Fluido newtoniano
  - Relación constitutiva
  - Viscosidad
---

# Fluido Newtoniano $\tau_{ij}=2\mu\,e_{ij}+\lambda\,\delta_{ij}e_{kk}$

> [!definicion]
> Un **fluido newtoniano** es aquel cuyo **desviador viscoso** $\tau_{ij}$ (la parte del esfuerzo que no es presión, de [[Presion y Esfuerzos Viscosos]]) es una función **lineal, isótropa y sin memoria** de la **rapidez de deformación** $e_{ij}$. La forma más general que respeta esas tres exigencias es la **relación constitutiva**
> $$\boxed{\;\tau_{ij}=2\mu\,e_{ij}+\lambda\,\delta_{ij}\,e_{kk}\;},$$
> donde $\mu$ es la **viscosidad dinámica** (o de corte) y $\lambda$ el **segundo coeficiente de viscosidad**. El esfuerzo solo depende de la **velocidad** con que se deforma el elemento — no de cuánto se ha deformado (no hay memoria, a diferencia de un sólido elástico) — y depende **solo de $e_{ij}$**, nunca de la parte rotacional $\omega_{ij}$: girar como cuerpo rígido no genera esfuerzo.

---

> [!info]
> Nota de la sección [[2 Esfuerzos y Tensor de Tensiones/index | Esfuerzos y Tensor de Tensiones]] (capítulo 2). Cierra el capítulo dando la **ley material** que liga el esfuerzo con el movimiento: el tensor de esfuerzos $\sigma_{ij}$ de la hermana [[Tensor de Esfuerzos de Cauchy]] se descompone en presión y viscosidad como en [[Presion y Esfuerzos Viscosos]], y aquí fijamos cómo la viscosidad responde a la **rapidez de deformación** $e_{ij}$ definida en [[Deformacion y Vorticidad]]. Con esta relación constitutiva, sustituyendo en la ecuación de Cauchy se obtienen las ecuaciones de Navier-Stokes. Notación SI, convenio de suma de Einstein, $\delta_{ij}$. **Referencia.** Landau-Lifshitz, Vol. 6 (*Mecánica de Fluidos*), §15; Batchelor, *An Introduction to Fluid Dynamics*, §3.3; Aris, *Vectors, Tensors and the Basic Equations of Fluid Mechanics*, cap. 6.

---

## La forma constitutiva lineal-isótropa

> [!teoria] Tres hipótesis y un tensor de cuarto orden
> Postular un fluido newtoniano es postular que existe un **tensor de cuarto orden** $A_{ijkl}$ que transforma linealmente la rapidez de deformación en esfuerzo viscoso:
> $$\tau_{ij}=A_{ijkl}\,e_{kl}.$$
> Las tres hipótesis acotan $A_{ijkl}$ de forma muy fuerte:
> - **Lineal.** $A_{ijkl}$ no depende de $e_{kl}$ (son constantes del material, a temperatura y presión fijas). De ahí que $\tau_{ij}$ sea una combinación lineal de las $e_{kl}$.
> - **Isótropa.** El fluido no tiene direcciones privilegiadas: $A_{ijkl}$ debe ser un **tensor isótropo**, idéntico en todo sistema rotado.
> - **Sin memoria.** $\tau_{ij}$ depende del estado **instantáneo** $e_{kl}$, no de su historia. Además, como $\tau_{ij}$ y $e_{kl}$ son **simétricos**, basta con la parte de $A_{ijkl}$ simétrica en $(i,j)$ y en $(k,l)$.

> [!proposicion] El único tensor isótropo de cuarto orden admisible
> Todo tensor isótropo de cuarto orden con las simetrías $A_{ijkl}=A_{jikl}=A_{ijlk}$ se escribe
> $$A_{ijkl}=\mu\,(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk})+\lambda\,\delta_{ij}\delta_{kl},$$
> con $\mu,\lambda$ dos escalares. Al contraerlo con $e_{kl}$ produce exactamente $\tau_{ij}=2\mu\,e_{ij}+\lambda\,\delta_{ij}e_{kk}$.

> [!demostracion]
> **Paso 1 — Por qué solo aparecen $\delta$'s.** Un tensor **isótropo** es, por definición, invariante bajo toda rotación. Los únicos "ladrillos" invariantes bajo rotaciones (propias) con índices que construir son la delta de Kronecker $\delta_{ij}$ y el símbolo de Levi-Civita $\epsilon_{ijk}$. Para un objeto de **cuarto orden** las únicas combinaciones posibles de deltas son los tres emparejamientos de los cuatro índices:
> $$\delta_{ij}\delta_{kl},\qquad \delta_{ik}\delta_{jl},\qquad \delta_{il}\delta_{jk}.$$
> Cualquier término con $\epsilon$ exigiría dos de ellos (para tener cuatro índices libres), y $\epsilon\epsilon$ se reduce a productos de deltas; no aporta nada nuevo. Por tanto, la forma general isótropa es
> $$A_{ijkl}=a\,\delta_{ij}\delta_{kl}+b\,\delta_{ik}\delta_{jl}+c\,\delta_{il}\delta_{jk},$$
> con $a,b,c$ escalares.
>
> **Paso 2 — Imponer la simetría en $(k,l)$.** Como $e_{kl}=e_{lk}$, solo importa la parte de $A_{ijkl}$ **simétrica al intercambiar $k\leftrightarrow l$**. Intercambiando esos índices,
> $$\delta_{ij}\delta_{kl}\ \to\ \delta_{ij}\delta_{lk}=\delta_{ij}\delta_{kl}\ (\text{ya simétrico}),\qquad \delta_{ik}\delta_{jl}\ \leftrightarrow\ \delta_{il}\delta_{jk}.$$
> Los dos últimos términos se intercambian entre sí, así que en la contracción solo sobrevive su **suma simétrica**: podemos imponer $b=c$. Llamamos $b=c=\mu$ y $a=\lambda$:
> $$A_{ijkl}=\lambda\,\delta_{ij}\delta_{kl}+\mu\,(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk}).$$
>
> **Paso 3 — Contraer con $e_{kl}$, término a término.** Calculamos $\tau_{ij}=A_{ijkl}\,e_{kl}$ usando la regla de la delta $\delta_{mn}T_{n\cdots}=T_{m\cdots}$ (la delta "renombra" el índice sumado):
> $$\lambda\,\delta_{ij}\delta_{kl}\,e_{kl}=\lambda\,\delta_{ij}\,e_{kk},$$
> pues $\delta_{kl}e_{kl}=e_{kk}$ es la **traza**.
> $$\mu\,\delta_{ik}\delta_{jl}\,e_{kl}=\mu\,e_{ij}\qquad(\delta_{ik}\ \text{fija }k=i,\ \delta_{jl}\ \text{fija }l=j),$$
> $$\mu\,\delta_{il}\delta_{jk}\,e_{kl}=\mu\,e_{ji}=\mu\,e_{ij}\qquad(\delta_{il}\ \text{fija }l=i,\ \delta_{jk}\ \text{fija }k=j,\ \text{y }e_{ji}=e_{ij}).$$
>
> **Paso 4 — Sumar.** Reuniendo las tres contribuciones,
> $$\tau_{ij}=\mu\,e_{ij}+\mu\,e_{ij}+\lambda\,\delta_{ij}\,e_{kk}=2\mu\,e_{ij}+\lambda\,\delta_{ij}\,e_{kk}.$$
> Esta es la relación constitutiva buscada. El factor $2$ delante de $\mu$ nace de que **dos** de los tres emparejamientos de deltas (los simétricos en $i,j$) colapsan sobre $e_{ij}$. $\blacksquare$

---

## Separación corte / volumen (forma de Landau)

> [!proposicion] Reescritura en parte de traza nula más parte de dilatación
> La relación constitutiva es idénticamente igual a
> $$\tau_{ij}=2\mu\left(e_{ij}-\tfrac13\delta_{ij}\,e_{kk}\right)+\zeta\,\delta_{ij}\,e_{kk},\qquad \boxed{\;\zeta=\lambda+\tfrac23\mu\;},$$
> donde $\zeta$ es la **viscosidad de volumen** (bulk). El primer paréntesis es el **desviador** de $e_{ij}$ (traza nula), asociado al **cambio de forma sin cambio de volumen**; el segundo término es la **dilatación** $e_{kk}=\nabla\cdot\vec v$, asociada al **cambio de volumen sin cambio de forma**.

> [!demostracion]
> **Paso 1 — Tomar la traza nula como referencia.** Definimos el desviador de la rapidez de deformación $\hat e_{ij}=e_{ij}-\tfrac13\delta_{ij}e_{kk}$. Es de **traza nula**: $\hat e_{kk}=e_{kk}-\tfrac13\,\delta_{kk}\,e_{kk}=e_{kk}-\tfrac13\cdot 3\cdot e_{kk}=0$ (recordando $\delta_{kk}=3$ en tres dimensiones).
>
> **Paso 2 — Expandir el lado derecho propuesto.** Sustituimos:
> $$2\mu\,\hat e_{ij}+\zeta\,\delta_{ij}e_{kk}=2\mu\!\left(e_{ij}-\tfrac13\delta_{ij}e_{kk}\right)+\zeta\,\delta_{ij}e_{kk}=2\mu\,e_{ij}+\left(\zeta-\tfrac{2}{3}\mu\right)\delta_{ij}\,e_{kk}.$$
>
> **Paso 3 — Identificar el coeficiente.** Comparando con la forma original $2\mu\,e_{ij}+\lambda\,\delta_{ij}e_{kk}$, los términos $2\mu\,e_{ij}$ coinciden, y el de la dilatación exige
> $$\zeta-\tfrac23\mu=\lambda\quad\Longrightarrow\quad \zeta=\lambda+\tfrac23\mu.$$
> Las dos formas son la misma relación, reorganizada. $\blacksquare$

> [!teoria] Por qué la separación es física, no solo algebraica
> El **corte** ($2\mu\,\hat e_{ij}$) cuesta energía por **cizallar** el fluido manteniendo el volumen; lo gobierna $\mu$. El **volumen** ($\zeta\,\delta_{ij}\nabla\cdot\vec v$) cuesta energía por **comprimir o expandir** el elemento; lo gobierna $\zeta$. Son mecanismos disipativos distintos, por eso conviene escribirlos separados.

> [!corolario] Hipótesis de Stokes e incompresibilidad
> - **Hipótesis de Stokes:** se postula $\zeta=0$, es decir $\lambda=-\tfrac23\mu$. Es muy buena para gases monoatómicos y se usa por defecto en mucha aerodinámica. Bajo ella, la **presión mecánica** $-\tfrac13\sigma_{kk}$ coincide con la **presión termodinámica**, porque el término de volumen no añade presión al promediar.
> - **Flujo incompresible:** si $e_{kk}=\nabla\cdot\vec v=0$, el término de $\lambda$ (o de $\zeta$) **desaparece por completo** y la relación se reduce a
> $$\tau_{ij}=2\mu\,e_{ij}.$$
> En este caso $\lambda$ es irrelevante y la viscosidad de corte $\mu$ es el **único** parámetro material. Es la situación habitual en líquidos.

---

## Ejemplo

> [!ejemplo] Recuperar la ley de Newton y el flujo de Couette
> **(a) El cortante elemental.** Considera un flujo cortante simple $\vec v=(u(y),\,0,\,0)$. Comprueba que la relación newtoniana reproduce la **ley de viscosidad de Newton** $\tau=\mu\,\dot\gamma$.
>
> **(b) Couette plano.** En un fluido entre dos placas separadas $h$, con la inferior fija y la superior moviéndose a velocidad $U$, el perfil es $u(y)=U\,y/h$. Calcula el esfuerzo cortante para agua, $\mu=1{,}0\times 10^{-3}\ \mathrm{Pa\cdot s}$, con $U=0{,}50\ \mathrm{m/s}$ y $h=2{,}0\ \mathrm{mm}$.

> [!solucion]
> **Parte (a) — El cortante simple.** El único gradiente no nulo es $\partial_y u=\dfrac{du}{dy}$. La rapidez de deformación fuera de la diagonal es
> $$e_{xy}=\tfrac12\!\left(\partial_x v_y+\partial_y v_x\right)=\tfrac12\!\left(0+\frac{du}{dy}\right)=\frac{1}{2}\frac{du}{dy}.$$
> Como $e_{kk}=\partial_x u=0$ (la dilatación es nula: el flujo es incompresible), el término de $\lambda$ se anula y queda $\tau_{ij}=2\mu\,e_{ij}$. Por tanto
> $$\tau_{xy}=2\mu\,e_{xy}=2\mu\cdot\frac{1}{2}\frac{du}{dy}=\mu\,\frac{du}{dy}.$$
> Identificando la **rapidez de cizalla** $\dot\gamma\equiv du/dy$, se obtiene
> $$\boxed{\;\tau_{xy}=\mu\,\dot\gamma\;}$$
> que es la **ley de Newton de la viscosidad**, origen del nombre del fluido. Es justo lo que mide un **viscosímetro** de cizalla: aplica un $\dot\gamma$ conocido y lee el esfuerzo.
>
> **Parte (b) — Couette plano.** Con $u(y)=U\,y/h$, la rapidez de cizalla es **constante**:
> $$\dot\gamma=\frac{du}{dy}=\frac{U}{h}.$$
> El esfuerzo cortante es entonces uniforme en todo el hueco:
> $$\tau_{xy}=\mu\,\frac{U}{h}.$$
> Numéricamente,
> $$\tau_{xy}=\left(1{,}0\times 10^{-3}\ \mathrm{Pa\cdot s}\right)\cdot\frac{0{,}50\ \mathrm{m/s}}{2{,}0\times 10^{-3}\ \mathrm{m}}=1{,}0\times 10^{-3}\cdot 250\ \mathrm{Pa}=0{,}25\ \mathrm{Pa}.$$
> El esfuerzo es pequeño porque el agua es poco viscosa; el mismo cálculo con un aceite ($\mu\sim 0{,}1\ \mathrm{Pa\cdot s}$) daría $25\ \mathrm{Pa}$, cien veces mayor. $\blacksquare$

---

## En qué consiste

La relación constitutiva newtoniana es el puente entre la **cinemática** (cómo se mueve y deforma el fluido, capítulo 1) y la **dinámica** (qué fuerzas internas aparecen, capítulo 2). Conceptualmente:

1. **Solo la deformación cuenta.** El gradiente de velocidad se parte en $\partial_j v_i=e_{ij}+\omega_{ij}$. El esfuerzo viscoso responde **únicamente** a la parte simétrica $e_{ij}$. La parte antisimétrica $\omega_{ij}$ es rotación de cuerpo rígido y, por sí sola, no roza nada: no disipa.
2. **Lineal e isótropa $\Rightarrow$ dos constantes.** Exigir linealidad e isotropía reduce un objeto de cuarto orden (con $81$ componentes en principio) a **dos** escalares, $\mu$ y $\lambda$ (o, equivalentemente, $\mu$ y $\zeta$). Toda la riqueza del fluido cabe en dos números.
3. **Dos modos de disipar.** Cizallar cuesta $\mu$; comprimir/expandir cuesta $\zeta$. En líquidos casi siempre $\nabla\cdot\vec v=0$ y solo importa $\mu$.

El campo que **mide** los apartamientos de esta ley es la **reología**: la figura muestra qué fluidos siguen la recta newtoniana y cuáles no.

![[fluido_newtoniano.svg|460]]
*Curvas reológicas esfuerzo–rapidez de cizalla $\tau$ vs. $\dot\gamma$. El fluido **newtoniano** es la recta por el origen de pendiente $\mu$ ($\tau=\mu\dot\gamma$). El **pseudoplástico** (shear-thinning, p. ej. sangre, pintura) se aplana: su viscosidad aparente cae al cizallar. El **dilatante** (shear-thickening, p. ej. suspensiones densas de almidón) se curva hacia arriba. El plástico de **Bingham** (p. ej. pasta dental) no fluye hasta superar un esfuerzo de fluencia $\tau_0$.*

> [!warning]
> En un fluido newtoniano la viscosidad $\mu$ depende de la **temperatura** (mucho en líquidos —baja al calentar—, poco en gases —sube al calentar—) y de la presión, pero **no** de la rapidez de cizalla $\dot\gamma$: esa **constancia de $\mu$ frente a $\dot\gamma$ es la marca registrada del fluido newtoniano**. Fluidos como la **sangre**, las **pinturas** o las disoluciones de **polímeros** son **no newtonianos**: su viscosidad aparente $\mu_\text{ap}=\tau/\dot\gamma$ **cambia** con $\dot\gamma$ (y a veces con la historia del flujo), por lo que la relación $\tau_{ij}=2\mu\,e_{ij}+\lambda\,\delta_{ij}e_{kk}$ **no** los describe. Para ellos hace falta una ley constitutiva no lineal o con memoria.

---

## Resumen

> [!resumen]
> | Magnitud / forma | Expresión | Significado |
> \|---\|---\|---\|
> | Relación constitutiva | $\tau_{ij}=2\mu\,e_{ij}+\lambda\,\delta_{ij}e_{kk}$ | esfuerzo viscoso $\leftrightarrow$ rapidez de deformación |
> | Tensor isótropo de 4.º orden | $A_{ijkl}=\mu(\delta_{ik}\delta_{jl}+\delta_{il}\delta_{jk})+\lambda\,\delta_{ij}\delta_{kl}$ | $\tau_{ij}=A_{ijkl}e_{kl}$ |
> | Forma de Landau | $\tau_{ij}=2\mu\!\left(e_{ij}-\tfrac13\delta_{ij}e_{kk}\right)+\zeta\,\delta_{ij}e_{kk}$ | corte (traza nula) $+$ volumen |
> | Viscosidad de volumen | $\zeta=\lambda+\tfrac23\mu$ | resistencia a comprimir/expandir |
> | Hipótesis de Stokes | $\zeta=0\ \Leftrightarrow\ \lambda=-\tfrac23\mu$ | presión mecánica $=$ termodinámica |
> | Incompresible ($e_{kk}=0$) | $\tau_{ij}=2\mu\,e_{ij}$ | solo importa $\mu$ |
> | Ley de Newton (corte simple) | $\tau_{xy}=\mu\,\dfrac{du}{dy}=\mu\,\dot\gamma$ | origen del nombre |

> [!corolario]
> Un fluido newtoniano queda descrito por **dos** coeficientes de viscosidad ($\mu$ y $\lambda$, o $\mu$ y $\zeta$), constantes a $T$ y $p$ dadas. La hipótesis es lineal, isótropa y sin memoria; depende solo de $e_{ij}$ y, en flujo incompresible, se reduce a la sencilla $\tau_{ij}=2\mu\,e_{ij}$. Sustituida en la ecuación de Cauchy de [[Tensor de Esfuerzos de Cauchy]], produce las ecuaciones de **Navier-Stokes**.

> [!referencia]
> - **Landau-Lifshitz**, *Mecánica de Fluidos* (Vol. 6), §15 — deducción de la forma constitutiva y viscosidad de volumen.
> - **Batchelor**, *An Introduction to Fluid Dynamics*, §3.3 — fluido newtoniano y su relación de esfuerzos.
> - **Aris**, *Vectors, Tensors and the Basic Equations of Fluid Mechanics*, cap. 6 — tratamiento tensorial del tensor isótropo de cuarto orden.
> - Hermanas del capítulo: [[Tensor de Esfuerzos de Cauchy]], [[Presion y Esfuerzos Viscosos]]; usa [[Deformacion y Vorticidad]] del capítulo 1.
