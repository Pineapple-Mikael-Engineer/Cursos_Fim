---
title: Conservación de Masa
tags:
  - fluidos
  - teoria
  - conservacion
draft: false
aliases:
  - Conservación de masa
  - Ecuación de continuidad
---

# Conservación de Masa $\partial_t\rho+\nabla\cdot(\rho\vec v)=0$

> [!definicion] Ecuación de continuidad
> La **conservación de masa** establece que la masa de un fluido no se crea ni se destruye. En forma local (diferencial) se expresa mediante la **ecuación de continuidad**:
> $$\boxed{\;\frac{\partial\rho}{\partial t}+\nabla\cdot(\rho\vec v)=0\;}$$
> donde $\rho(\vec x,t)$ es la densidad y $\vec v(\vec x,t)$ el campo de velocidades. El término $\rho\vec v$ es la **densidad de flujo másico** (kg·m⁻²·s⁻¹): la cantidad de masa que atraviesa la unidad de área por unidad de tiempo. La ecuación dice que la densidad solo aumenta en un punto si converge flujo másico hacia él ($\nabla\cdot(\rho\vec v)<0$).

---

> [!info] Ubicación y dependencias
> Esta nota pertenece a la sección [[3 Ecuaciones de Conservacion/index | Ecuaciones de Conservación]], junto a sus hermanas [[Conservacion de Momento]] y [[Ecuaciones de Navier-Stokes]]. La deducción se apoya en el [[Teorema del Transporte de Reynolds]] para pasar del enunciado integral sobre un volumen material a la forma diferencial.
>
> **Referencias:** Landau & Lifshitz, *Mecánica de Fluidos* (Vol. 6) §1; Batchelor, *An Introduction to Fluid Dynamics*, cap. 3.

---

La idea física es un simple **balance de inventario**: la masa que se acumula en una región es igual a la que entra menos la que sale por su frontera. La figura ilustra ese balance sobre un volumen de control fijo.

![[flujo_masa.svg|420]]

*Figura 1. Balance de flujo másico en un volumen de control fijo $dx\,dy\,dz$: la tasa de acumulación interior $\partial_t\rho\,dV$ iguala la diferencia entre el flujo másico entrante y el saliente a través de las caras.*

---

## Deducción de la ecuación de continuidad

Presentamos las **dos** rutas clásicas: la lagrangiana (volumen material + transporte de Reynolds) y la euleriana (volumen de control fijo + balance cara a cara). Ambas conducen a la misma ecuación.

> [!teorema] Ecuación de continuidad
> Para todo campo de densidad $\rho$ y velocidad $\vec v$ suficientemente regulares, la conservación de la masa equivale a
> $$\frac{\partial\rho}{\partial t}+\nabla\cdot(\rho\vec v)=0.$$

### Ruta 1 — Volumen material y Teorema del Transporte de Reynolds

> [!demostracion] Vía lagrangiana
> Considérese un **volumen material** $V(t)$: una porción de fluido formada siempre por las mismas partículas, cuya frontera se mueve con la velocidad local $\vec v$. Como ninguna partícula entra ni sale de él por definición, su masa es constante en el tiempo:
> $$\frac{d}{dt}\int_{V(t)}\rho\,dV=0.$$
>
> **Paso 1 — Aplicar el Teorema del Transporte de Reynolds.** El teorema ([[Teorema del Transporte de Reynolds]]) permite intercambiar la derivada temporal con la integral sobre un volumen móvil. Para la propiedad por unidad de volumen $\rho$,
> $$\frac{d}{dt}\int_{V(t)}\rho\,dV=\int_{V(t)}\!\left[\frac{\partial\rho}{\partial t}+\nabla\cdot(\rho\vec v)\right]dV.$$
>
> **Paso 2 — Imponer la conservación.** Igualando a cero el miembro izquierdo,
> $$\int_{V(t)}\!\left[\frac{\partial\rho}{\partial t}+\nabla\cdot(\rho\vec v)\right]dV=0.$$
>
> **Paso 3 — Arbitrariedad del volumen.** La igualdad vale para **cualquier** volumen material $V(t)$, por pequeño que sea y dondequiera que se ubique. Si el integrando fuese, digamos, positivo en algún punto $\vec x_0$, por continuidad lo sería en una bola alrededor de $\vec x_0$, y eligiendo $V(t)$ contenido en esa bola la integral resultaría positiva, contradiciendo que es nula. Luego el integrando debe anularse en todo punto:
> $$\frac{\partial\rho}{\partial t}+\nabla\cdot(\rho\vec v)=0.\qquad\blacksquare$$

### Ruta 2 — Volumen de control fijo (balance de flujos)

> [!demostracion] Vía euleriana, cara a cara
> Fíjese en el espacio un pequeño paralelepípedo fijo de aristas $dx$, $dy$, $dz$ centrado en $(x,y,z)$, con volumen $dV=dx\,dy\,dz$. Escribimos $\vec v=(u,v,w)=(v_1,v_2,v_3)$.
>
> **Paso 1 — Tasa de acumulación.** La masa contenida es $\rho\,dV$, y como el volumen es fijo, su variación temporal es
> $$\frac{\partial}{\partial t}(\rho\,dV)=\frac{\partial\rho}{\partial t}\,dx\,dy\,dz.$$
>
> **Paso 2 — Flujo neto en la dirección $x$.** Por la cara izquierda (en $x-\tfrac{dx}{2}$, área $dy\,dz$) **entra** masa a razón de $(\rho u)\big|_{x-\frac{dx}{2}}\,dy\,dz$; por la cara derecha (en $x+\tfrac{dx}{2}$) **sale** $(\rho u)\big|_{x+\frac{dx}{2}}\,dy\,dz$. Desarrollando ambas con Taylor a primer orden,
> $$(\rho u)\Big|_{x\pm\frac{dx}{2}}=(\rho u)\big|_x\pm\frac{\partial(\rho u)}{\partial x}\frac{dx}{2}.$$
> El flujo neto entrante (entra − sale) en $x$ es
> $$\Big[(\rho u)\big|_{x-\frac{dx}{2}}-(\rho u)\big|_{x+\frac{dx}{2}}\Big]dy\,dz=-\frac{\partial(\rho u)}{\partial x}\,dx\,dy\,dz.$$
>
> **Paso 3 — Las otras dos direcciones.** Idénticamente, por las caras perpendiculares a $y$ y a $z$:
> $$-\frac{\partial(\rho v)}{\partial y}\,dx\,dy\,dz,\qquad -\frac{\partial(\rho w)}{\partial z}\,dx\,dy\,dz.$$
>
> **Paso 4 — Balance.** La acumulación iguala el flujo neto entrante total:
> $$\frac{\partial\rho}{\partial t}\,dx\,dy\,dz=-\left[\frac{\partial(\rho u)}{\partial x}+\frac{\partial(\rho v)}{\partial y}+\frac{\partial(\rho w)}{\partial z}\right]dx\,dy\,dz.$$
> Dividiendo por $dV=dx\,dy\,dz\neq 0$ y usando el convenio de suma $\partial_i(\rho v_i)=\nabla\cdot(\rho\vec v)$,
> $$\frac{\partial\rho}{\partial t}=-\partial_i(\rho v_i)=-\nabla\cdot(\rho\vec v),$$
> es decir $\partial_t\rho+\nabla\cdot(\rho\vec v)=0$. $\blacksquare$

---

## Forma con derivada material

> [!proposicion] Continuidad en forma lagrangiana
> La ecuación de continuidad equivale a
> $$\frac{D\rho}{Dt}+\rho\,\nabla\cdot\vec v=0,$$
> donde $\dfrac{D}{Dt}=\dfrac{\partial}{\partial t}+\vec v\cdot\nabla$ es la **derivada material** (la tasa de cambio siguiendo a la partícula).

> [!demostracion]
> **Paso 1 — Expandir la divergencia del producto.** Por la regla del producto, con $\partial_i(\rho v_i)=v_i\,\partial_i\rho+\rho\,\partial_i v_i$,
> $$\nabla\cdot(\rho\vec v)=\rho\,\nabla\cdot\vec v+\vec v\cdot\nabla\rho.$$
>
> **Paso 2 — Sustituir en la ecuación de continuidad.**
> $$\frac{\partial\rho}{\partial t}+\rho\,\nabla\cdot\vec v+\vec v\cdot\nabla\rho=0.$$
>
> **Paso 3 — Reagrupar la derivada material.** Los términos $\partial_t\rho+\vec v\cdot\nabla\rho$ son exactamente $\dfrac{D\rho}{Dt}$. Por tanto
> $$\frac{D\rho}{Dt}+\rho\,\nabla\cdot\vec v=0.\qquad\blacksquare$$

Esta forma se lee así: la densidad de una partícula cambia ($D\rho/Dt$) solo si el campo de velocidades comprime o dilata su entorno ($\nabla\cdot\vec v$). Un $\nabla\cdot\vec v>0$ (expansión local) hace caer la densidad de la partícula.

---

## Flujo incompresible

> [!definicion] Flujo incompresible
> Un flujo es **incompresible** cuando la densidad de cada partícula no varía a lo largo de su trayectoria:
> $$\frac{D\rho}{Dt}=0.$$
> No exige que $\rho$ sea uniforme en el espacio, solo que se conserve siguiendo a cada partícula.

> [!proposicion] Equivalencia $\;D\rho/Dt=0\iff\nabla\cdot\vec v=0$
> En un flujo incompresible el campo de velocidades es **solenoidal**: $\nabla\cdot\vec v=0$.

> [!demostracion]
> **Paso 1 — Partir de la forma material.** La continuidad da siempre $\dfrac{D\rho}{Dt}+\rho\,\nabla\cdot\vec v=0$.
>
> **Paso 2 — Imponer incompresibilidad.** Por definición $\dfrac{D\rho}{Dt}=0$, luego
> $$\rho\,\nabla\cdot\vec v=0.$$
>
> **Paso 3 — Eliminar $\rho$.** Como $\rho>0$ en un fluido real, se concluye
> $$\nabla\cdot\vec v=0.$$
> Recíprocamente, si $\nabla\cdot\vec v=0$ entonces $\rho\,\nabla\cdot\vec v=0$ y la continuidad obliga a $\dfrac{D\rho}{Dt}=0$. La equivalencia queda establecida. $\blacksquare$

> [!warning] Incompresible ≠ densidad constante
> La incompresibilidad es una propiedad del **flujo**, no únicamente del fluido. Significa $\nabla\cdot\vec v=0$, es decir, que las partículas no cambian su densidad. Esto **no** implica densidad uniforme: el océano o la atmósfera pueden fluir de forma incompresible aun estando **estratificados** ($\rho$ distinta a distintas alturas), siempre que cada partícula conserve su propia densidad.
>
> Por eso un **gas** —compresible por naturaleza— fluye casi incompresiblemente cuando el número de Mach es pequeño ($\mathrm{Ma}\ll 1$): las variaciones relativas de densidad escalan como $\mathrm{Ma}^2$ y se vuelven despreciables. El caso particular de **densidad constante** ($\rho=\text{cte}$ en todo el campo) da directamente $\nabla\cdot\vec v=0$ desde $\partial_t\rho+\nabla\cdot(\rho\vec v)=0$, pues $\partial_t\rho=0$ y $\nabla\rho=\vec 0$ dejan $\rho\,\nabla\cdot\vec v=0$.

---

## Caudal en un tubo de corriente

> [!corolario] Conservación del caudal
> En un flujo **estacionario** ($\partial_t(\cdot)=0$) e **incompresible**, el caudal volumétrico
> $$Q=\int_A \vec v\cdot d\vec A$$
> es constante a lo largo de un **tubo de corriente**. Para secciones $A_1$ y $A_2$ con velocidades medias normales $v_1$, $v_2$:
> $$A_1\,v_1=A_2\,v_2.$$

> [!demostracion]
> **Paso 1 — Volumen de control.** Tómese como volumen de control un tramo del tubo de corriente limitado por dos secciones transversales $A_1$ (entrada) y $A_2$ (salida) y por la pared lateral del tubo.
>
> **Paso 2 — Forma integral estacionaria.** Integrando la continuidad sobre el volumen fijo $V$ y aplicando el teorema de la divergencia, con $\partial_t\rho=0$:
> $$\int_V \nabla\cdot(\rho\vec v)\,dV=\oint_{\partial V}\rho\,\vec v\cdot d\vec A=0.$$
>
> **Paso 3 — Anular la pared lateral.** Sobre la superficie lateral del tubo, $\vec v$ es tangente a la pared (las líneas de corriente no la cruzan), de modo que $\vec v\cdot d\vec A=0$ ahí. Solo contribuyen las dos secciones extremas:
> $$\int_{A_2}\rho\,\vec v\cdot d\vec A-\int_{A_1}\rho\,\vec v\cdot d\vec A=0,$$
> con el signo del primer término saliente (normal exterior) y el segundo entrante.
>
> **Paso 4 — Incompresibilidad.** Con $\rho$ constante a lo largo del tubo sale del integrando y se cancela:
> $$\int_{A_2}\vec v\cdot d\vec A=\int_{A_1}\vec v\cdot d\vec A\;\Longrightarrow\;A_2 v_2=A_1 v_1.\qquad\blacksquare$$

La consecuencia es intuitiva: al **estrechar** la sección, el fluido debe **acelerar** para que pase el mismo caudal.

---

## Ejemplo

> [!ejemplo] Campos solenoidales y una contracción
> **(a)** Determina si el campo $\vec v=(2x,\,-y,\,-z)$ corresponde a un flujo incompresible.
>
> **(b)** Agua circula en régimen estacionario por una tubería que se contrae de un diámetro $D_1=10\ \text{cm}$ a $D_2=5\ \text{cm}$. Si en la sección ancha la velocidad media es $v_1=1,5\ \text{m/s}$, halla la velocidad media $v_2$ en la sección estrecha.

> [!solucion]
> **(a) Divergencia del campo.** Con el convenio de suma, $\nabla\cdot\vec v=\partial_x v_1+\partial_y v_2+\partial_z v_3$:
> $$\nabla\cdot\vec v=\frac{\partial(2x)}{\partial x}+\frac{\partial(-y)}{\partial y}+\frac{\partial(-z)}{\partial z}=2+(-1)+(-1)=0.$$
> Como $\nabla\cdot\vec v=0$, el flujo **es incompresible** (campo solenoidal).
>
> *Contraejemplo de control:* el campo $\vec v=(2x,\,-y,\,0)$ daría $\nabla\cdot\vec v=2-1+0=1\neq 0$, es decir **compresible**: el entorno de cada partícula se dilata.
>
> **(b) Conservación del caudal.** Para una sección circular, $A=\dfrac{\pi D^2}{4}$. De $A_1 v_1=A_2 v_2$:
> $$v_2=v_1\,\frac{A_1}{A_2}=v_1\left(\frac{D_1}{D_2}\right)^{2}=1,5\cdot\left(\frac{10}{5}\right)^{2}\ \text{m/s}=1,5\cdot 4\ \text{m/s}=6,0\ \text{m/s}.$$
> Al reducir el diámetro a la mitad, el área cae a la cuarta parte y la velocidad se cuadruplica: $v_2=6,0\ \text{m/s}$.

---

## En qué consiste

La conservación de masa es el primer principio físico que cierra el sistema de ecuaciones de un fluido. Su contenido se puede resumir en cuatro lecturas equivalentes de un mismo hecho —la masa ni aparece ni desaparece—:

- **Local euleriana:** $\partial_t\rho+\nabla\cdot(\rho\vec v)=0$. La densidad en un punto fijo sube si converge flujo másico hacia él. Es la forma que se discretiza en los métodos numéricos.
- **Lagrangiana:** $\dfrac{D\rho}{Dt}+\rho\,\nabla\cdot\vec v=0$. Siguiendo a la partícula, su densidad cambia solo si el flujo comprime o dilata su entorno.
- **Integral:** $\dfrac{d}{dt}\displaystyle\int_{V(t)}\rho\,dV=0$ sobre un volumen material; o el balance entrada−salida sobre un volumen de control fijo.
- **Incompresible:** cuando $D\rho/Dt=0$, la cinemática se simplifica a $\nabla\cdot\vec v=0$, una restricción puramente geométrica sobre $\vec v$ que es la hipótesis de trabajo de la hidráulica y de buena parte de la aerodinámica subsónica.

Conceptualmente, la divergencia $\nabla\cdot\vec v$ mide la **tasa de dilatación volumétrica** del fluido: positiva si se expande, negativa si se comprime, nula si es incompresible. La ecuación de continuidad es, en el fondo, la traducción de "no se pierde masa" a una afirmación sobre cómo esa dilatación debe acoplarse con los cambios de densidad.

---

## Resumen

> [!resumen] Formas de la conservación de masa
> | Forma | Expresión | Hipótesis |
> |---|---|---|
> | Local (euleriana) | $\partial_t\rho+\nabla\cdot(\rho\vec v)=0$ | general |
> | Material (lagrangiana) | $\dfrac{D\rho}{Dt}+\rho\,\nabla\cdot\vec v=0$ | general |
> | Integral (vol. material) | $\dfrac{d}{dt}\!\int_{V(t)}\rho\,dV=0$ | general |
> | Incompresible | $\nabla\cdot\vec v=0$ | $D\rho/Dt=0$ |
> | Densidad constante | $\nabla\cdot\vec v=0$ | $\rho=\text{cte}$ |
> | Caudal en tubo | $A_1 v_1=A_2 v_2$ | estacionario e incompresible |

> [!corolario] Claves
> - La continuidad sale de "la masa se conserva" por dos vías equivalentes: transporte de Reynolds sobre un volumen material, y balance de flujos en un volumen de control fijo.
> - **Incompresible** $\iff$ $\nabla\cdot\vec v=0$, una propiedad del flujo; no equivale a densidad uniforme (admite estratificación) ni se limita a líquidos (un gas con $\mathrm{Ma}\ll 1$ fluye casi incompresiblemente).
> - En flujo estacionario incompresible el caudal se conserva: estrechar la sección acelera el fluido.

> [!referencia] Fuentes
> - L. D. Landau y E. M. Lifshitz, *Mecánica de Fluidos* (Curso de Física Teórica, Vol. 6), §1 «La ecuación de continuidad».
> - G. K. Batchelor, *An Introduction to Fluid Dynamics*, cap. 3.
> - Notas relacionadas: [[Teorema del Transporte de Reynolds]], [[Conservacion de Momento]], [[Ecuaciones de Navier-Stokes]].
