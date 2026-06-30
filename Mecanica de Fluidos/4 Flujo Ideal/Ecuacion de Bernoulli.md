---
title: Ecuación de Bernoulli
order: 2
tags:
  - fluidos
  - teoria
  - flujo-ideal
draft: false
aliases:
  - Ecuación de Bernoulli
  - Teorema de Bernoulli
---

# Ecuación de Bernoulli $\tfrac12 v^2+\dfrac{p}{\rho}+gz=\text{cte}$

> [!definicion]
> La **ecuación de Bernoulli** afirma que, en un **flujo ideal, estacionario e incompresible**, la cantidad
> $$B=\tfrac12 v^2+\frac{p}{\rho}+gz$$
> —la **energía mecánica por unidad de masa**— se mantiene **constante a lo largo de cada línea de corriente**. Si además el flujo es **irrotacional** ($\vec\omega=\nabla\times\vec v=\vec 0$), la constante es la **misma en todo el campo**. Es la integral primera de la [[Ecuacion de Euler]] cuando se proyecta sobre la dirección del movimiento, y traduce la conservación de la energía a un balance entre velocidad, presión y altura.

---

> [!info]
> **Sección [[4 Flujo Ideal/index | Flujo Ideal]] (Capítulo 4).** Es el segundo gran fruto de la [[Ecuacion de Euler]]: la integral del campo de fuerzas a lo largo de una línea de corriente. Notas hermanas: [[Ecuacion de Euler]] (de donde se deduce) y [[Flujo Potencial]] (donde Bernoulli vale en todo el campo). **Referencia.** Landau-Lifshitz, Vol. 6, §5 ("Ecuación de Bernoulli").

---

## En qué consiste

> [!teoria] Una integral primera de Euler
> La ecuación de Euler para un flujo ideal, escrita en la **forma de Lamb** (usando la identidad vectorial $(\vec v\cdot\nabla)\vec v=\nabla(\tfrac12 v^2)-\vec v\times\vec\omega$, con $\vec\omega=\nabla\times\vec v$ la **vorticidad**), es:
> $$\partial_t\vec v+\nabla\!\left(\tfrac12 v^2\right)-\vec v\times\vec\omega=-\frac{1}{\rho}\nabla p+\vec g.$$
> Bernoulli es lo que queda cuando esta ecuación se vuelve **integrable**: en régimen estacionario el término $\partial_t\vec v$ desaparece, en flujo incompresible $\tfrac1\rho\nabla p=\nabla(p/\rho)$, y la gravedad deriva de un potencial $\vec g=-\nabla(gz)$. Todo se agrupa bajo un único gradiente, y solo sobrevive el término rotacional $\vec v\times\vec\omega$, que es **perpendicular a $\vec v$**. Por eso la cantidad $B$ no cambia **a lo largo del flujo**.

La función $B=\tfrac12 v^2+p/\rho+gz$ se llama **función de Bernoulli** o **trinomio de Bernoulli**. Cada término es una energía por unidad de masa: cinética ($\tfrac12 v^2$), de presión ($p/\rho$, el trabajo que el fluido aguas arriba ejerce empujando) y potencial gravitatoria ($gz$). Multiplicando por $\rho$ se obtiene la forma en **presiones**:
$$\underbrace{p}_{\text{estática}}+\underbrace{\tfrac12\rho v^2}_{\text{dinámica}}+\underbrace{\rho g z}_{\text{hidrostática}}=\text{cte}.$$
La suma se llama **presión total** o **de estancamiento**: lo que un manómetro leería si frenara el fluido hasta el reposo sin pérdidas.

---

> [!demostracion] Deducción de Bernoulli desde Euler
> Partimos de la **forma de Lamb** de la [[Ecuacion de Euler]] para un flujo ideal.
>
> **Paso 1 — Hipótesis.** Imponemos las tres condiciones del teorema:
> - **Estacionario:** $\partial_t\vec v=\vec 0$.
> - **Incompresible:** $\rho=\text{cte}$, luego $\tfrac1\rho\nabla p=\nabla\!\left(\dfrac{p}{\rho}\right)$.
> - **Gravedad conservativa:** $\vec g=-\nabla(gz)$, con $z$ la altura.
>
> Sustituyendo en Euler:
> $$\nabla\!\left(\tfrac12 v^2\right)-\vec v\times\vec\omega=-\nabla\!\left(\frac{p}{\rho}\right)-\nabla(gz).$$
>
> **Paso 2 — Agrupar bajo un gradiente.** Pasamos todo a la izquierda. Los tres gradientes se reúnen en uno solo:
> $$\nabla\!\left(\tfrac12 v^2+\frac{p}{\rho}+gz\right)=\vec v\times\vec\omega.$$
> El miembro izquierdo es $\nabla B$ con $B=\tfrac12 v^2+p/\rho+gz$. Esta es la **forma de Bernoulli de la ecuación de Euler**: exacta, sin más hipótesis que las del Paso 1.
>
> **Paso 3 — Proyectar sobre la línea de corriente.** Una **línea de corriente** es, en cada punto, tangente a $\vec v$. La variación de $B$ siguiendo esa curva es su derivada direccional a lo largo de $\vec v$, esto es $\vec v\cdot\nabla B$. Proyectamos la ecuación del Paso 2 multiplicando escalarmente por $\vec v$:
> $$\vec v\cdot\nabla B=\vec v\cdot(\vec v\times\vec\omega).$$
>
> **Paso 4 — El término rotacional se anula.** El producto mixto $\vec v\cdot(\vec v\times\vec\omega)$ tiene **dos factores iguales** ($\vec v$ repetido), luego es cero: $\vec v\times\vec\omega\perp\vec v$. Por tanto:
> $$\vec v\cdot\nabla B=0.$$
> La derivada de $B$ en la dirección del movimiento es nula: $B$ **no varía a lo largo de una línea de corriente**. Como el flujo es estacionario, las líneas de corriente coinciden con las trayectorias de las partículas, así que cada partícula conserva su $B$:
> $$\boxed{\;\tfrac12 v^2+\frac{p}{\rho}+gz=\text{cte sobre cada línea de corriente}.\;}$$
> $\blacksquare$

> [!corolario] Caso irrotacional: una sola constante en todo el campo
> Si el flujo es además **irrotacional**, $\vec\omega=\vec 0$, el miembro derecho de la ecuación del Paso 2 se anula por completo:
> $$\nabla B=\vec 0\quad\Longrightarrow\quad B=\tfrac12 v^2+\frac{p}{\rho}+gz=\text{cte en TODO el dominio}.$$
> No hace falta seguir una línea de corriente: la constante es **única para todo el campo**. Esta es la situación del [[Flujo Potencial]] ($\vec v=\nabla\phi$), y por eso allí Bernoulli relaciona dos puntos cualesquiera, estén o no sobre la misma línea de corriente. Hay que distinguir bien los dos casos:
> - **Rotacional:** $B$ constante **sobre cada** línea de corriente (puede cambiar de una a otra).
> - **Irrotacional:** $B$ constante **en todas partes** (un solo valor).

> [!proposicion] Bernoulli no estacionario (flujo potencial)
> Si el flujo es **potencial** pero **no estacionario**, $\vec v=\nabla\phi$ y $\partial_t\vec v=\nabla(\partial_t\phi)$. El término temporal entra también bajo el gradiente, y la integración da:
> $$\partial_t\phi+\tfrac12 v^2+\frac{p}{\rho}+gz=f(t),$$
> donde $f(t)$ es una función **del tiempo**, igual en todo el espacio (puede absorberse redefiniendo $\phi$). Recupera el caso estacionario cuando $\partial_t\phi=0$ y $f=\text{cte}$. Es la forma usada en ondas de superficie y oscilaciones.

> [!teoria] Lectura energética
> $B$ es la **energía mecánica por unidad de masa** transportada por una partícula: cinética más de presión más potencial. Bernoulli es, literalmente, la **conservación de la energía mecánica** de la partícula de fluido **en ausencia de fricción**: sin viscosidad no hay disipación, así que la energía solo se intercambia entre sus tres formas. Donde el fluido acelera ($v\uparrow$), debe ceder presión ($p\downarrow$) o altura; donde frena, la recupera. Esta es la base intuitiva del efecto Venturi y de la sustentación.

---

> [!demostracion] Tres aplicaciones clásicas
> **(a) Teorema de Torricelli — vaciado por un orificio.** Un depósito grande y abierto tiene un orificio pequeño a profundidad $h$ bajo la superficie libre. Tomamos una línea de corriente desde la superficie (punto 1) hasta el chorro de salida (punto 2). Ambos están a presión atmosférica, $p_1=p_2=p_{\text{atm}}$. El depósito es grande, así que la superficie baja muy despacio: $v_1\approx 0$. Situamos el orificio en $z_2=0$ y la superficie en $z_1=h$. Bernoulli da:
> $$\tfrac12 v_1^2+\frac{p_{\text{atm}}}{\rho}+g h=\tfrac12 v_2^2+\frac{p_{\text{atm}}}{\rho}+0.$$
> Cancelando $p_{\text{atm}}/\rho$ y con $v_1\approx0$:
> $$g h=\tfrac12 v_2^2\quad\Longrightarrow\quad \boxed{\,v_2=\sqrt{2gh}\,.}$$
> La velocidad de salida es la **misma que la de caída libre** desde la altura $h$. $\blacksquare$
>
> **(b) Tubo de Pitot — medida de velocidad.** Un tubo de Pitot enfrenta al flujo un orificio que **frena** el fluido hasta el reposo (punto de **estancamiento**, $v_0=0$, presión $p_0$) y compara con una toma lateral que mide la presión estática $p$ del flujo libre, de velocidad $v$. Sobre una línea de corriente horizontal ($z$ constante, se cancela $gz$):
> $$\tfrac12\rho v^2+p=\underbrace{\tfrac12\rho\,v_0^2}_{=0}+p_0.$$
> Despejando la velocidad:
> $$\boxed{\,v=\sqrt{\dfrac{2\,(p_0-p)}{\rho}}\,.}$$
> Midiendo la diferencia $p_0-p$ (presión dinámica) se obtiene la velocidad: así miden su velocidad los aviones. $\blacksquare$
>
> **(c) Efecto Venturi — estrangulamiento de un tubo.** En una tubería horizontal que se estrecha de área $A_1$ a $A_2<A_1$, la **continuidad** (conservación de masa, flujo incompresible) impone $A_1 v_1=A_2 v_2$, de modo que en la garganta $v_2>v_1$. Bernoulli horizontal ($gz$ se cancela):
> $$p_1+\tfrac12\rho v_1^2=p_2+\tfrac12\rho v_2^2.$$
> Como $v_2>v_1$, necesariamente $p_2<p_1$: **donde el fluido acelera, la presión baja**. Eliminando $v_1=(A_2/A_1)v_2$:
> $$p_1-p_2=\tfrac12\rho\,v_2^2\left[1-\left(\frac{A_2}{A_1}\right)^{2}\right]>0.\qquad\blacksquare$$

![[bernoulli_venturi.svg|480]]
*Efecto Venturi: en la garganta el área disminuye, la velocidad sube y la presión baja, manteniéndose $\tfrac12 v^2+p/\rho+gz$ constante a lo largo de la línea de corriente. La caída de presión $p_1-p_2$ se visualiza en las columnas manométricas.*

---

## Ejemplo

> [!ejemplo] Caudal con un medidor de Venturi
> Por una tubería horizontal circula agua ($\rho=1\,000\ \text{kg/m}^3$). Un medidor de Venturi tiene área de entrada $A_1=20\ \text{cm}^2$ y garganta $A_2=8\ \text{cm}^2$. Los manómetros indican una diferencia de presión $p_1-p_2=4\,500\ \text{Pa}$ entre la entrada y la garganta. Hallar el **caudal volumétrico** $Q$.

> [!solucion]
> **Paso 1 — Datos en el SI.** $A_1=20\ \text{cm}^2=20\cdot10^{-4}\ \text{m}^2=2,0\cdot10^{-3}\ \text{m}^2$; $A_2=8\ \text{cm}^2=8,0\cdot10^{-4}\ \text{m}^2$; $\Delta p=p_1-p_2=4\,500\ \text{Pa}$.
>
> **Paso 2 — Continuidad.** El caudal es el mismo en ambas secciones: $Q=A_1 v_1=A_2 v_2$. Despejamos las velocidades en función de $Q$:
> $$v_1=\frac{Q}{A_1},\qquad v_2=\frac{Q}{A_2}.$$
>
> **Paso 3 — Bernoulli horizontal.** Con $z_1=z_2$:
> $$p_1+\tfrac12\rho v_1^2=p_2+\tfrac12\rho v_2^2\;\Longrightarrow\;\Delta p=\tfrac12\rho\left(v_2^2-v_1^2\right)=\tfrac12\rho\,Q^2\left(\frac{1}{A_2^2}-\frac{1}{A_1^2}\right).$$
>
> **Paso 4 — Despejar el caudal.**
> $$Q=A_2\sqrt{\dfrac{2\,\Delta p}{\rho\left[1-\left(A_2/A_1\right)^2\right]}}.$$
>
> **Paso 5 — Numérico.** La relación de áreas: $A_2/A_1=8/20=0,4$, luego $1-(0,4)^2=1-0,16=0,84$. El radicando:
> $$\frac{2\cdot4\,500}{1\,000\cdot 0,84}=\frac{9\,000}{840}=10,71\ \text{m}^2/\text{s}^2,\qquad \sqrt{10,71}=3,27\ \text{m/s}.$$
> Entonces:
> $$Q=8,0\cdot10^{-4}\cdot 3,27=2,62\cdot10^{-3}\ \text{m}^3/\text{s}\approx 2,6\ \text{L/s}.$$
>
> **Comprobación.** Las velocidades resultan $v_1=Q/A_1=1,31\ \text{m/s}$ y $v_2=Q/A_2=3,27\ \text{m/s}$, coherentes con $v_2>v_1$ y con $\Delta p=\tfrac12\rho(v_2^2-v_1^2)=\tfrac12\cdot1\,000\cdot(10,69-1,72)\approx4\,500\ \text{Pa}$. $\blacksquare$

---

> [!warning] Cuándo NO se puede usar Bernoulli
> La ecuación exige **todas** estas condiciones:
> - **Flujo ideal** (sin viscosidad): no hay pérdidas por fricción ni en las paredes ni en estelas.
> - **Estacionario** (salvo la variante potencial con $\partial_t\phi$).
> - **Incompresible** o, al menos, **barotrópico** ($p=p(\rho)$, sustituyendo $p/\rho$ por $\int dp/\rho$).
> - **A lo largo de una misma línea de corriente**, a menos que el flujo sea **irrotacional** (entonces vale en todo el campo).
>
> En particular, **NO** se aplica al cruzar una **estela** o una **capa de cortadura** (líneas de corriente distintas con $B$ distinto y disipación viscosa), al atravesar una **bomba o turbina** (aportan o extraen energía: $B$ salta), ni a través de un **salto hidráulico** o una **onda de choque** (hay disipación). En esos casos hay que usar balances de energía con términos de pérdida o de trabajo.

---

## Resumen

> [!resumen]
> | Forma / caso | Expresión | Validez |
> |:---|:---|:---|
> | Energía por unidad de masa | $\tfrac12 v^2+\dfrac{p}{\rho}+gz=\text{cte}$ | línea de corriente |
> | En presiones | $p+\tfrac12\rho v^2+\rho gz=\text{cte}$ | línea de corriente |
> | Forma de Euler (Lamb) | $\nabla B=\vec v\times\vec\omega$ | flujo ideal estacionario |
> | Irrotacional | $B=\text{cte}$ en todo el campo | $\vec\omega=\vec 0$ |
> | No estacionario potencial | $\partial_t\phi+\tfrac12 v^2+\dfrac{p}{\rho}+gz=f(t)$ | $\vec v=\nabla\phi$ |
> | Torricelli | $v=\sqrt{2gh}$ | orificio a profundidad $h$ |
> | Pitot | $v=\sqrt{2(p_0-p)/\rho}$ | presión de estancamiento |
> | Venturi + continuidad | $A_1v_1=A_2v_2,\; v\uparrow\Rightarrow p\downarrow$ | tubo horizontal |

> [!corolario]
> Bernoulli es la **integral primera de Euler a lo largo del flujo**: la energía mecánica por unidad de masa se conserva sobre cada línea de corriente (y en todo el campo si es irrotacional). Es el puente entre la dinámica de [[Ecuacion de Euler]] y la cinemática del [[Flujo Potencial]], y la herramienta de cálculo más usada en flujo ideal. Su límite es el mismo del modelo: **vale donde la fricción es despreciable**.

> [!referencia]
> Landau-Lifshitz, *Mecánica de Fluidos* (Vol. 6), §5 ("Ecuación de Bernoulli"). Batchelor, *An Introduction to Fluid Dynamics*, §3.5; Acheson, *Elementary Fluid Dynamics*, cap. 1.
