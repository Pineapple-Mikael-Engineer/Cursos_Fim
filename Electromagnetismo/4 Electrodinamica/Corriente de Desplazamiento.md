---
title: Corriente de Desplazamiento
order: 2
tags:
  - electromagnetismo
  - teoria
  - electrodinamica
draft: false
aliases:
  - Corriente de desplazamiento
  - Término de Maxwell
---

# Corriente de Desplazamiento $\nabla\times\vec B=\mu_0\vec J+\mu_0\varepsilon_0\dfrac{\partial\vec E}{\partial t}$

> [!definicion]
> La **corriente de desplazamiento** es el término extra que Maxwell añadió a la [[Ley de Ampere | ley de Ampère]] para hacerla compatible con la **conservación de la carga** cuando los campos varían en el tiempo. Se define como la densidad de corriente "efectiva"
> $$\boxed{\ \vec J_d\equiv\varepsilon_0\,\frac{\partial\vec E}{\partial t}\ }$$
> y su flujo a través de una superficie $S$ es la **corriente de desplazamiento** $I_d=\displaystyle\int_S\vec J_d\cdot d\vec A=\varepsilon_0\dfrac{d\Phi_E}{dt}$. Sumada a la corriente de conducción $\vec J$ (flujo real de carga), corrige el rotacional del campo magnético y da la **ley de Ampère–Maxwell**, en sus dos formas equivalentes:
> $$\boxed{\ \nabla\times\vec B=\mu_0\vec J+\mu_0\varepsilon_0\,\frac{\partial\vec E}{\partial t}\ }\qquad\text{(diferencial)},$$
> $$\boxed{\ \oint_C\vec B\cdot d\vec l=\mu_0\,I_{\text{enc}}+\mu_0\varepsilon_0\,\frac{d\Phi_E}{dt}\ }\qquad\text{(integral)}.$$
> Aquí $\Phi_E=\displaystyle\int_S\vec E\cdot d\vec A$ es el flujo eléctrico a través de la superficie apoyada en $C$. El nombre es histórico: no hay carga "desplazándose", sino un **campo eléctrico variable** que actúa como fuente de $\vec B$.

---

> [!info]
> **Sección [[4 Electrodinamica/index | Electrodinámica]]** (capítulo 4 del curso). Este término es el que **cierra** el sistema de las [[Ecuaciones de Maxwell]] y, junto con la [[Ley de Faraday]], permite que los campos se autosostengan: es la pieza que hace posibles las **ondas electromagnéticas**. Parte de corregir la [[Ley de Ampere | ley de Ampère]] de la magnetostática, que solo vale para corrientes estacionarias. **Referencia.** Griffiths, *Introduction to Electrodynamics*, cap. 7.

---

## La inconsistencia de Ampère

> [!proposicion] Ampère es incompatible con la conservación de la carga
> La ley de Ampère magnetostática $\nabla\times\vec B=\mu_0\vec J$ **exige** $\nabla\cdot\vec J=0$. Pero la **ecuación de continuidad** (conservación de la carga)
> $$\nabla\cdot\vec J=-\frac{\partial\rho}{\partial t}$$
> da $\nabla\cdot\vec J\neq0$ siempre que la densidad de carga $\rho$ varíe en el tiempo. Las dos no pueden ser ciertas a la vez con cargas variables: hay una **contradicción**.

> [!demostracion]
> **Paso 1 — Tomamos la divergencia de Ampère.** Partimos de la forma diferencial magnetostática y aplicamos $\nabla\cdot$ a ambos lados:
> $$\nabla\cdot(\nabla\times\vec B)=\mu_0\,\nabla\cdot\vec J.$$
>
> **Paso 2 — La divergencia de un rotacional es nula.** Es una identidad vectorial universal: para todo campo $\vec B$ suficientemente suave,
> $$\nabla\cdot(\nabla\times\vec B)=0.$$
> Por tanto, la ley de Ampère **obliga** a que
> $$\mu_0\,\nabla\cdot\vec J=0\ \Rightarrow\ \nabla\cdot\vec J=0.$$
>
> **Paso 3 — La continuidad lo contradice.** La conservación de la carga (un principio experimental inviolable) afirma
> $$\nabla\cdot\vec J=-\frac{\partial\rho}{\partial t}.$$
> En un proceso con cargas que se acumulan o varían (por ejemplo, una placa de condensador cargándose) se tiene $\partial\rho/\partial t\neq0$, luego $\nabla\cdot\vec J\neq0$.
>
> **Paso 4 — Choque.** El paso 2 exige $\nabla\cdot\vec J=0$ y el paso 3 da $\nabla\cdot\vec J\neq0$. **No pueden coexistir**: la ley de Ampère, tal cual, es **falsa** fuera de la magnetostática. $\blacksquare$

---

## El parche de Maxwell

> [!teorema] Reparación de la ley de Ampère
> Sustituyendo $\rho=\varepsilon_0\,\nabla\cdot\vec E$ (ley de Gauss) en la continuidad, el "defecto" de divergencia de $\vec J$ se reescribe como la divergencia de $\varepsilon_0\,\partial_t\vec E$. Sumando ese término a $\vec J$ se obtiene un campo de divergencia nula, y la ley corregida es
> $$\nabla\times\vec B=\mu_0\big(\vec J+\vec J_d\big),\qquad \vec J_d=\varepsilon_0\,\frac{\partial\vec E}{\partial t}.$$

> [!demostracion]
> **Paso 1 — Partimos de la continuidad.** La conservación de la carga es
> $$\nabla\cdot\vec J+\frac{\partial\rho}{\partial t}=0.$$
>
> **Paso 2 — Eliminamos $\rho$ con la ley de Gauss.** En el vacío con cargas, [[Ley de Gauss | Gauss]] da $\rho=\varepsilon_0\,\nabla\cdot\vec E$. Sustituimos:
> $$\nabla\cdot\vec J+\frac{\partial}{\partial t}\big(\varepsilon_0\,\nabla\cdot\vec E\big)=0.$$
>
> **Paso 3 — Intercambiamos derivadas y agrupamos.** Como las derivadas espaciales y la temporal conmutan, $\partial_t(\nabla\cdot\vec E)=\nabla\cdot(\partial_t\vec E)$, y $\varepsilon_0$ es constante:
> $$\nabla\cdot\vec J+\nabla\cdot\!\left(\varepsilon_0\,\frac{\partial\vec E}{\partial t}\right)=0\ \Rightarrow\ \nabla\cdot\!\left(\vec J+\varepsilon_0\,\frac{\partial\vec E}{\partial t}\right)=0.$$
>
> **Paso 4 — Identificamos el término que faltaba.** La combinación $\vec J+\varepsilon_0\,\partial_t\vec E$ tiene divergencia **idénticamente nula**, justo lo que requiere el rotacional de $\vec B$ (paso 2 de la demostración anterior). Llamamos a la pieza nueva **corriente de desplazamiento**:
> $$\vec J_d\equiv\varepsilon_0\,\frac{\partial\vec E}{\partial t}.$$
>
> **Paso 5 — Reescribimos Ampère.** Reemplazando $\vec J$ por $\vec J+\vec J_d$ en la ley de Ampère, ahora la divergencia cuadra para todo proceso:
> $$\nabla\times\vec B=\mu_0\big(\vec J+\vec J_d\big)=\mu_0\vec J+\mu_0\varepsilon_0\,\frac{\partial\vec E}{\partial t}.$$
> En magnetostática $\partial_t\vec E=0$ y se recupera $\nabla\times\vec B=\mu_0\vec J$: el parche **no rompe** lo que ya funcionaba. $\blacksquare$

---

## El argumento del condensador

> [!proposicion] La paradoja de las dos superficies
> En un condensador cargándose, un mismo lazo amperiano $C$ admite dos superficies: $S_1$, cortada por el cable (corriente de conducción $I$), y $S_2$, que pasa **entre las placas** (sin conducción, pero con $\partial_t\vec E\neq0$). La ley de Ampère original daría **dos valores distintos** de la circulación; la corriente de desplazamiento las **iguala**.

![[desplazamiento.svg|460]]
*Condensador cargándose con corriente $I$. El lazo amperiano $C$ rodea el cable y puede taparse con la superficie plana $S_1$ (atravesada por la corriente de conducción $I$) o con la superficie abombada $S_2$, que pasa entre las placas, donde no hay carga en movimiento pero sí un campo eléctrico variable que aporta la corriente de desplazamiento $I_d=I$.*

> [!demostracion]
> **Paso 1 — La superficie $S_1$ (cortada por el cable).** El lazo $C$ rodea el alambre que alimenta la placa. La superficie plana $S_1$ es atravesada por la corriente de conducción $I$, así que la versión original de Ampère da
> $$\oint_C\vec B\cdot d\vec l=\mu_0\,I.$$
>
> **Paso 2 — La superficie $S_2$ (entre las placas).** Deformamos la superficie sin mover su borde $C$ hasta que pase **entre las placas** del condensador. Allí no hay carga moviéndose: ninguna corriente de conducción la atraviesa, $I_{\text{enc}}=0$. La ley original daría
> $$\oint_C\vec B\cdot d\vec l=\mu_0\cdot 0=0.$$
> Misma curva $C$, **dos resultados**: $\mu_0 I$ frente a $0$. Imposible.
>
> **Paso 3 — Campo entre las placas.** Sea $A$ el área de cada placa y $Q(t)$ la carga acumulada. La densidad superficial es $\sigma=Q/A$ y el campo entre placas (despreciando bordes) es uniforme:
> $$E=\frac{\sigma}{\varepsilon_0}=\frac{Q}{\varepsilon_0\,A}.$$
>
> **Paso 4 — Flujo eléctrico a través de $S_2$.** El campo solo cruza $S_2$ entre las placas, sobre el área $A$:
> $$\Phi_E=\int_{S_2}\vec E\cdot d\vec A=E\,A=\frac{Q}{\varepsilon_0}.$$
>
> **Paso 5 — Corriente de desplazamiento.** Derivando el flujo en el tiempo:
> $$I_d=\varepsilon_0\,\frac{d\Phi_E}{dt}=\varepsilon_0\,\frac{d}{dt}\!\left(\frac{Q}{\varepsilon_0}\right)=\frac{dQ}{dt}=\dot Q.$$
> Pero $\dot Q$ es justamente la corriente que carga la placa, es decir, $\dot Q=I$. Por tanto
> $$I_d=\varepsilon_0\,A\,\dot E=\dot Q=I.$$
>
> **Paso 6 — Las dos superficies coinciden.** Con la ley de Ampère–Maxwell, $S_2$ aporta $\mu_0 I_d=\mu_0 I$ en lugar de cero:
> $$\oint_C\vec B\cdot d\vec l=\mu_0\big(I_{\text{enc}}+I_d\big)=\mu_0\,(0+I)=\mu_0\,I,$$
> exactamente lo mismo que daba $S_1$. La corriente de desplazamiento **restituye la independencia de la superficie**: el campo $\vec B$ es el mismo se elija $S_1$ o $S_2$. $\blacksquare$

---

## Ejemplo

> [!ejemplo] Campo $\vec B$ dentro de un condensador de placas circulares
> Un condensador de placas planas y **circulares** de radio $a$ se carga mediante una corriente constante $I$. Hallar el campo magnético $\vec B$ en el hueco entre las placas, a una distancia $s$ del eje (con $s<a$).

> [!solucion]
> **Paso 1 — Simetría.** El campo eléctrico entre las placas, $\vec E=E(t)\,\hat z$ (eje del condensador), es uniforme y crece con el tiempo. Por la simetría cilíndrica, la corriente de desplazamiento $\vec J_d=\varepsilon_0\,\partial_t\vec E$ apunta a lo largo del eje y se distribuye uniformemente sobre el área de las placas. El campo magnético inducido es **azimutal**, $\vec B=B(s)\,\hat\varphi$, igual que el de un hilo.
>
> **Paso 2 — Lazo amperiano.** Tomamos un círculo $C$ de radio $s$ coaxial con el eje, dentro del hueco. Como $\vec B$ es tangente y constante sobre él,
> $$\oint_C\vec B\cdot d\vec l=B\,(2\pi s).$$
>
> **Paso 3 — Densidad de corriente de desplazamiento.** El campo entre placas es $E=Q/(\varepsilon_0 A)$ con $A=\pi a^2$, de modo que
> $$J_d=\varepsilon_0\,\frac{\partial E}{\partial t}=\varepsilon_0\,\frac{\dot Q}{\varepsilon_0\,A}=\frac{\dot Q}{\pi a^2}=\frac{I}{\pi a^2},$$
> donde usamos $\dot Q=I$. Está repartida uniformemente sobre toda la sección de radio $a$.
>
> **Paso 4 — "Corriente" encerrada por el lazo.** No hay conducción ($I_{\text{enc}}=0$), pero el lazo de radio $s$ encierra la fracción de corriente de desplazamiento que atraviesa el disco de área $\pi s^2$:
> $$I_{d,\text{enc}}=J_d\,(\pi s^2)=\frac{I}{\pi a^2}\,(\pi s^2)=I\,\frac{s^2}{a^2}.$$
>
> **Paso 5 — Ampère–Maxwell y despeje.** Igualamos la circulación con $\mu_0$ veces la corriente encerrada (solo de desplazamiento):
> $$B\,(2\pi s)=\mu_0\,I_{d,\text{enc}}=\mu_0\,I\,\frac{s^2}{a^2}.$$
> Despejando,
> $$\boxed{\ B=\frac{\mu_0\,I\,s}{2\pi a^2}\ }\qquad (s<a).$$
> El campo **crece linealmente** con $s$ dentro del condensador (como el de un hilo grueso de corriente uniforme), y en el borde $s=a$ vale $B=\mu_0 I/(2\pi a)$, empalmando con el campo $\mu_0 I/(2\pi s)$ del cable exterior. $\blacksquare$

---

> [!warning] Qué es (y qué no es) la corriente de desplazamiento
> - **No es un flujo de carga.** Pese al nombre, entre las placas de un condensador no hay portadores moviéndose: $\vec J_d=\varepsilon_0\,\partial_t\vec E$ es un **campo eléctrico variable**, no una corriente material. Lo único que comparte con una corriente real es que **también genera campo magnético**.
> - **Completa la simetría de Maxwell.** Con la [[Ley de Faraday]] un campo magnético variable crea $\vec E$; con la corriente de desplazamiento un campo eléctrico variable crea $\vec B$. Esa **reciprocidad** es la que permite que $\vec E$ y $\vec B$ se sostengan mutuamente y viajen como **ondas electromagnéticas** en el vacío, donde $\vec J=0$ pero $\partial_t\vec E\neq0$.
> - **No cambia la magnetostática.** Si los campos no varían en el tiempo, $\vec J_d=0$ y se recupera la [[Ley de Ampere | ley de Ampère]] original. El término solo "se enciende" con campos dependientes del tiempo.

---

## Resumen

> [!resumen]
>
> | Concepto | Expresión | Significado |
> |:---|:---|:---|
> | Densidad de desplazamiento | $\vec J_d=\varepsilon_0\,\partial_t\vec E$ | campo $\vec E$ variable que actúa como fuente de $\vec B$ |
> | Corriente de desplazamiento | $I_d=\varepsilon_0\,\dfrac{d\Phi_E}{dt}$ | flujo de $\vec J_d$ por una superficie |
> | Ampère–Maxwell (dif.) | $\nabla\times\vec B=\mu_0\vec J+\mu_0\varepsilon_0\,\partial_t\vec E$ | rotacional de $\vec B$ con divergencia nula |
> | Ampère–Maxwell (int.) | $\oint_C\vec B\cdot d\vec l=\mu_0 I_{\text{enc}}+\mu_0\varepsilon_0\,\dfrac{d\Phi_E}{dt}$ | circulación independiente de la superficie |
> | Condensador | $I_d=\varepsilon_0 A\,\dot E=\dot Q=I$ | $S_1$ y $S_2$ dan el mismo $\vec B$ |
> | Placas circulares | $B=\dfrac{\mu_0 I s}{2\pi a^2}$ | campo azimutal en el hueco, $s<a$ |
>
> donde $\Phi_E=\displaystyle\int_S\vec E\cdot d\vec A$.

> [!corolario]
> La corriente de desplazamiento es el **término de Maxwell**: la única modificación que hace falta para que las cuatro [[Ecuaciones de Maxwell]] sean mutuamente consistentes con la conservación de la carga. Nace de exigir $\nabla\cdot(\vec J+\varepsilon_0\partial_t\vec E)=0$, se verifica en el condensador con $I_d=I$, y al introducir la simetría $\partial_t\vec E\to\vec B$ frente a la $\partial_t\vec B\to\vec E$ de [[Ley de Faraday | Faraday]], **abre la puerta a las ondas electromagnéticas**. Es la pieza que convierte la electricidad y el magnetismo estáticos en el **electromagnetismo** dinámico.

> [!referencia]
> Griffiths, *Introduction to Electrodynamics*, cap. 7 ("Electrodynamics"), §7.3 ("Maxwell's Equations"), §7.3.1 ("Electrodynamics Before Maxwell") y §7.3.2 ("How Maxwell Fixed Ampère's Law"). Profundización: Jackson, cap. 6; Landau & Lifshitz, *Teoría clásica de los campos* (vol. 2).
