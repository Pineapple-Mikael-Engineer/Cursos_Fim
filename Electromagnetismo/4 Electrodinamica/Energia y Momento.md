---
title: Energía y Momento
order: 5
tags:
  - electromagnetismo
  - teoria
  - electrodinamica
draft: false
aliases:
  - Vector de Poynting
  - Teorema de Poynting
  - Energía del campo electromagnético
---

# Energía y Momento $\vec S=\dfrac{1}{\mu_0}\vec E\times\vec B$

---

> [!definicion] Energía, flujo y momento del campo
> El campo electromagnético **almacena energía**, **transporta energía** y **transporta momento**. Las tres magnitudes son locales (densidades de campo):
>
> **Densidad de energía** $u$ (energía por unidad de volumen, en J/m³):
> $$
> u=\frac{\varepsilon_0}{2}\,E^2+\frac{1}{2\mu_0}\,B^2,
> $$
> suma de la parte eléctrica y la magnética.
>
> **Vector de Poynting** $\vec S$ (flujo de energía por unidad de área y de tiempo, en W/m²):
> $$
> \boxed{\;\vec S=\frac{1}{\mu_0}\,\vec E\times\vec B\;}
> $$
>
> **Densidad de momento** $\vec g$ (momento por unidad de volumen, en kg·m⁻²·s⁻¹):
> $$
> \vec g=\varepsilon_0\,\vec E\times\vec B=\frac{\vec S}{c^{2}}.
> $$
>
> Ligadas por el **teorema de Poynting**, expresan la conservación de la energía del sistema campo $+$ cargas.

---

> [!info] Ubicación y conexiones
> - **Sección:** [[4 Electrodinamica/index | Electrodinámica]].
> - **Notas hermanas:** [[Ecuaciones de Maxwell]], [[Potenciales y Gauge]].
> - **Herramienta:** se apoya en la identidad $\nabla\cdot(\vec E\times\vec B)=\vec B\cdot(\nabla\times\vec E)-\vec E\cdot(\nabla\times\vec B)$ de [[Identidades Vectoriales]].
> - **Antecedente:** la densidad eléctrica $\tfrac{\varepsilon_0}{2}E^2$ ya apareció en [[Energia Electrostatica]]; aquí se le suma la magnética y se le da dinámica.
> - **Referencia base:** Griffiths, *Introduction to Electrodynamics*, capítulo 8 (Leyes de conservación).
>
> Esta nota cierra el capítulo: una vez que [[Ecuaciones de Maxwell]] están completas, sus soluciones cargan energía y momento, y eso obliga a una ley de conservación local —el teorema de Poynting— análoga a la continuidad de la carga.

---

## Demostración — Teorema de Poynting

El objetivo es escribir la conservación de la energía en **forma local**: una densidad $u$ que cambia en el tiempo, un flujo $\vec S$ que la transporta, y un sumidero $\vec J\cdot\vec E$ que es el trabajo entregado a las cargas.

Partimos de la **potencia que los campos entregan a las cargas**. La fuerza de Lorentz sobre una carga $q$ es $\vec F=q(\vec E+\vec v\times\vec B)$; la parte magnética **no trabaja** porque $\vec v\times\vec B\perp\vec v$. Para una distribución continua, la potencia mecánica entregada por unidad de volumen es $\vec J\cdot\vec E$, y sobre todo el volumen:
$$
\frac{dW}{dt}=\int_V \vec J\cdot\vec E\,d\tau.
$$

> [!demostracion] De $\frac{dW}{dt}=\int\vec J\cdot\vec E\,d\tau$ a $\partial_t u+\nabla\cdot\vec S=-\vec J\cdot\vec E$
> **Paso 1 — Despejar $\vec J$ de Ampère–Maxwell.** La cuarta ecuación de Maxwell ([[Ecuaciones de Maxwell]]) es $\nabla\times\vec B=\mu_0\vec J+\mu_0\varepsilon_0\,\partial_t\vec E$. Despejando la corriente:
> $$
> \vec J=\frac{1}{\mu_0}\nabla\times\vec B-\varepsilon_0\frac{\partial\vec E}{\partial t}.
> $$
> Multiplicando escalarmente por $\vec E$ se obtiene el integrando de la potencia:
> $$
> \vec J\cdot\vec E=\frac{1}{\mu_0}\,\vec E\cdot(\nabla\times\vec B)-\varepsilon_0\,\vec E\cdot\frac{\partial\vec E}{\partial t}.
> $$
>
> **Paso 2 — Reescribir $\vec E\cdot(\nabla\times\vec B)$ con la identidad vectorial.** Por la identidad del producto ([[Identidades Vectoriales]]):
> $$
> \nabla\cdot(\vec E\times\vec B)=\vec B\cdot(\nabla\times\vec E)-\vec E\cdot(\nabla\times\vec B),
> $$
> de donde se despeja el término buscado:
> $$
> \vec E\cdot(\nabla\times\vec B)=\vec B\cdot(\nabla\times\vec E)-\nabla\cdot(\vec E\times\vec B).
> $$
>
> **Paso 3 — Introducir Faraday.** La tercera ecuación de Maxwell es $\nabla\times\vec E=-\partial_t\vec B$ ([[Ley de Faraday]]). Sustituyéndola:
> $$
> \vec E\cdot(\nabla\times\vec B)=-\,\vec B\cdot\frac{\partial\vec B}{\partial t}-\nabla\cdot(\vec E\times\vec B).
> $$
> Llevando esto al Paso 1:
> $$
> \vec J\cdot\vec E=-\frac{1}{\mu_0}\,\vec B\cdot\frac{\partial\vec B}{\partial t}-\frac{1}{\mu_0}\,\nabla\cdot(\vec E\times\vec B)-\varepsilon_0\,\vec E\cdot\frac{\partial\vec E}{\partial t}.
> $$
>
> **Paso 4 — Reconocer las derivadas de los cuadrados.** Las dos derivadas temporales son derivadas de $E^2$ y $B^2$, pues para cualquier campo $\vec A\cdot\partial_t\vec A=\tfrac12\,\partial_t(\vec A\cdot\vec A)=\tfrac12\,\partial_t A^2$:
> $$
> \varepsilon_0\,\vec E\cdot\frac{\partial\vec E}{\partial t}=\frac{\partial}{\partial t}\!\left(\frac{\varepsilon_0}{2}E^2\right),\qquad
> \frac{1}{\mu_0}\,\vec B\cdot\frac{\partial\vec B}{\partial t}=\frac{\partial}{\partial t}\!\left(\frac{1}{2\mu_0}B^2\right).
> $$
> Sumadas, reconstruyen la densidad de energía $u$:
> $$
> \varepsilon_0\,\vec E\cdot\frac{\partial\vec E}{\partial t}+\frac{1}{\mu_0}\,\vec B\cdot\frac{\partial\vec B}{\partial t}=\frac{\partial}{\partial t}\!\left(\frac{\varepsilon_0}{2}E^2+\frac{1}{2\mu_0}B^2\right)=\frac{\partial u}{\partial t}.
> $$
>
> **Paso 5 — Identificar el vector de Poynting y reunir.** El término con divergencia es, por definición, $\nabla\cdot\vec S$ con $\vec S=\tfrac{1}{\mu_0}\vec E\times\vec B$. Reuniendo el Paso 3 reescrito con el Paso 4:
> $$
> \vec J\cdot\vec E=-\frac{\partial u}{\partial t}-\nabla\cdot\vec S.
> $$
> Pasando todo a un lado se obtiene la **forma local del teorema de Poynting**:
> $$
> \boxed{\;\frac{\partial u}{\partial t}+\nabla\cdot\vec S=-\,\vec J\cdot\vec E\;}
> $$
> $\blacksquare$

> [!corolario] Forma integral y lectura física
> Integrando sobre un volumen $V$ fijo y aplicando el teorema de la divergencia a $\nabla\cdot\vec S$:
> $$
> \frac{d}{dt}\int_V u\,d\tau+\oint_{\partial V}\vec S\cdot d\vec A=-\int_V \vec J\cdot\vec E\,d\tau.
> $$
> Lectura: la **energía del campo** dentro de $V$ disminuye por dos vías —la que **sale por la frontera** como flujo $\oint\vec S\cdot d\vec A$ y la que se **entrega a las cargas** $\int\vec J\cdot\vec E\,d\tau$ (calor Joule, energía cinética)—. La energía total (campo $+$ materia) se **conserva**, y $\vec S$ es quien la **transporta** por el espacio. Es la ecuación de continuidad de la energía electromagnética: $u$ hace de densidad, $\vec S$ de corriente, $-\vec J\cdot\vec E$ de fuente.

---

## Momento del campo

> [!proposicion] El campo transporta momento
> Si el campo lleva energía y esta viaja a velocidad finita, debe llevar también **momento** (en relatividad, energía y momento son la misma entidad). La **densidad de momento** del campo electromagnético es
> $$
> \vec g=\varepsilon_0\,\vec E\times\vec B=\varepsilon_0\mu_0\,\vec S=\frac{\vec S}{c^{2}},
> $$
> usando $c^2=1/(\varepsilon_0\mu_0)$. El momento por unidad de volumen es el flujo de energía dividido por $c^2$.

> [!teoria] Tensor de esfuerzos de Maxwell y presión de radiación
> Así como $\vec S$ es el **flujo de energía**, el **flujo de momento** del campo es un objeto de dos índices: el **tensor de esfuerzos de Maxwell**
> $$
> T_{ij}=\varepsilon_0\!\left(E_iE_j-\tfrac12\delta_{ij}E^2\right)+\frac{1}{\mu_0}\!\left(B_iB_j-\tfrac12\delta_{ij}B^2\right).
> $$
> $T_{ij}$ es la $i$-ésima componente de fuerza por unidad de área que el campo ejerce sobre una superficie orientada según $\hat e_j$. La conservación del momento se escribe localmente como
> $$
> \frac{\partial g_i}{\partial t}-\partial_j T_{ij}=-\,(\rho\,\vec E+\vec J\times\vec B)_i,
> $$
> con $\rho\vec E+\vec J\times\vec B$ la densidad de fuerza de Lorentz sobre las cargas. La cara visible de este momento es la **presión de radiación**: cuando una onda incide sobre una superficie, le transfiere su momento $\vec g$ y la empuja. Esta estructura tensorial es la antesala del tensor energía–momento $T^{\mu\nu}$ de la [[6 Formulacion Covariante/index | Formulación Covariante]].

---

## En qué consiste

La terna $\vec E$, $\vec B$, $\vec S$ es **ortogonal**: $\vec S=\tfrac{1}{\mu_0}\vec E\times\vec B$ es perpendicular a ambos campos y marca la **dirección en que fluye la energía**. Su módulo es la potencia por unidad de área que cruza un plano perpendicular a $\vec S$.

![[poynting.svg|420]]
*Terna ortogonal del campo: $\vec E$ y $\vec B$ perpendiculares entre sí, y el vector de Poynting $\vec S=\vec E\times\vec B/\mu_0$ saliendo perpendicular al plano que forman, en la dirección del flujo de energía. La densidad de energía $u=\tfrac{\varepsilon_0}{2}E^2+\tfrac{1}{2\mu_0}B^2$ llena el volumen que $\vec S$ atraviesa.*

La imagen mental correcta no es la de cargas que "empujan" corriente por un cable, sino la de **energía que viaja por el espacio entre los campos**. Tres consecuencias:

- **El campo es un depósito de energía.** Incluso en el vacío, donde no hay cargas, $u\neq0$ allí donde hay campo. Esa energía es real: puede medirse, transportarse y convertirse en trabajo.
- **La energía fluye perpendicular a los campos.** En un capacitor que se carga, $\vec S$ no entra por los cables sino **lateralmente**, por el hueco entre las placas. En una onda plana, $\vec E$, $\vec B$ y $\vec S$ avanzan juntos a velocidad $c$.
- **El campo carga momento.** Por eso la luz del Sol empuja la cola de un cometa y por eso una "vela solar" puede propulsar una nave: pura presión de radiación, $\vec g=\vec S/c^2$ transferido al impactar.

---

## Ejemplo — Flujo de Poynting en un cable con corriente

> [!ejemplo] ¿Por dónde entra la energía a un resistor?
> Un cable cilíndrico de radio $a$, longitud $\ell$ y resistencia $R$ transporta una corriente continua $I$. Entre sus extremos hay una caída de potencial $V=IR$. Demuestra que la potencia disipada $I^2R$ entra por la **superficie lateral** del cable, calculando $\vec S$ en $r=a$ y el flujo $\oint\vec S\cdot d\vec A$.

> [!solucion] Resolución
> **Paso 1 — Campo eléctrico dentro y sobre el cable.** En régimen estacionario el campo es axial y uniforme; su módulo es la caída de potencial por unidad de longitud:
> $$
> \vec E=\frac{V}{\ell}\,\hat z=\frac{IR}{\ell}\,\hat z.
> $$
>
> **Paso 2 — Campo magnético en la superficie ($r=a$).** Por la ley de Ampère, un cilindro de radio $a$ que encierra toda la corriente $I$ da
> $$
> B(a)=\frac{\mu_0 I}{2\pi a},\qquad \vec B=\frac{\mu_0 I}{2\pi a}\,\hat\varphi.
> $$
>
> **Paso 3 — Vector de Poynting en la superficie.** Con $\hat z\times\hat\varphi=-\hat r$:
> $$
> \vec S=\frac{1}{\mu_0}\,\vec E\times\vec B=\frac{1}{\mu_0}\,\frac{IR}{\ell}\,\frac{\mu_0 I}{2\pi a}\,(\hat z\times\hat\varphi)=-\frac{I^2R}{2\pi a\,\ell}\,\hat r.
> $$
> El signo $-\hat r$ indica que $\vec S$ apunta **hacia adentro**: la energía entra radialmente por los costados del cable, no por sus extremos.
>
> **Paso 4 — Flujo entrante total.** La superficie lateral tiene área $A=2\pi a\,\ell$ y $d\vec A=\hat r\,dA$ hacia afuera. La potencia que **entra** es $-\oint\vec S\cdot d\vec A$:
> $$
> P_{\text{entra}}=-\oint\vec S\cdot d\vec A=\frac{I^2R}{2\pi a\,\ell}\,(2\pi a\,\ell)=I^2R.
> $$
>
> **Resultado.** El flujo de Poynting que cruza la superficie lateral es exactamente $I^2R$, la potencia disipada por efecto Joule. La energía que calienta el resistor **viaja por el campo** que rodea al cable y entra por sus paredes; el cable solo guía los campos. $\blacksquare$

> [!corolario] Onda plana — el otro caso típico
> Para una onda electromagnética plana en el vacío, $\vec E$ y $\vec B$ son perpendiculares, $B_0=E_0/c$ y oscilan en fase. El promedio temporal del vector de Poynting (la **intensidad**) resulta
> $$
> \langle S\rangle=\frac{1}{2}\,c\,\varepsilon_0\,E_0^{2},
> $$
> el flujo medio de energía que la onda transporta por unidad de área (se deduce en detalle en [[5 Ondas Electromagneticas/index | Ondas Electromagnéticas]]).

---

> [!warning] La ambigüedad de $\vec S$ y el origen de la presión de radiación
> El vector de Poynting **no está definido de forma única**: a $\vec S$ puede sumarse cualquier campo de la forma $\nabla\times\vec F$ sin alterar la divergencia, porque $\nabla\cdot(\nabla\times\vec F)=0$, y por tanto sin cambiar el teorema de Poynting. Lo **físicamente medible** no es $\vec S$ punto a punto, sino el **flujo cerrado** $\oint\vec S\cdot d\vec A$ a través de una superficie que encierra una región: ese número sí es inequívoco. Conviene leer $\vec S=\tfrac1{\mu_0}\vec E\times\vec B$ como la elección estándar (la más simple y local), no como "la única posible".
>
> En cambio, el **momento del campo** $\vec g=\vec S/c^2$ tiene consecuencias inequívocas: la **presión de radiación** es la transferencia directa de ese momento al chocar con la materia, y se mide experimentalmente. El momento del campo es tan real como su energía.

---

## Resumen

> [!resumen] Energía y momento del campo de un vistazo
>
> | Concepto | Expresión | Significado |
> |---|---|---|
> | Densidad de energía | $u=\tfrac{\varepsilon_0}{2}E^2+\tfrac{1}{2\mu_0}B^2$ | Energía del campo por unidad de volumen [J/m³] |
> | Vector de Poynting | $\vec S=\tfrac{1}{\mu_0}\vec E\times\vec B$ | Flujo de energía por área y tiempo [W/m²] |
> | Teorema de Poynting | $\partial_t u+\nabla\cdot\vec S=-\,\vec J\cdot\vec E$ | Continuidad de la energía EM (forma local) |
> | Forma integral | $\tfrac{d}{dt}\!\int u\,d\tau+\oint\vec S\cdot d\vec A=-\!\int\vec J\cdot\vec E\,d\tau$ | Campo $+$ materia conservan energía |
> | Densidad de momento | $\vec g=\varepsilon_0\,\vec E\times\vec B=\vec S/c^2$ | Momento del campo por volumen |
> | Flujo de momento | $T_{ij}=\varepsilon_0(E_iE_j-\tfrac12\delta_{ij}E^2)+\tfrac{1}{\mu_0}(B_iB_j-\tfrac12\delta_{ij}B^2)$ | Tensor de esfuerzos de Maxwell |
> | Intensidad de onda | $\langle S\rangle=\tfrac12\,c\,\varepsilon_0\,E_0^2$ | Flujo medio de una onda plana |
>
> Donde $u$ es densidad de energía [J/m³], $\vec S$ flujo de energía [W/m²], $\vec g$ densidad de momento, $c=1/\sqrt{\mu_0\varepsilon_0}$.

> [!corolario] Ideas clave
> - El campo **almacena** energía ($u$), la **transporta** ($\vec S$) y lleva **momento** ($\vec g=\vec S/c^2$).
> - El **teorema de Poynting** $\partial_t u+\nabla\cdot\vec S=-\vec J\cdot\vec E$ es la conservación local de la energía: sale de Ampère–Maxwell $+$ Faraday $+$ la identidad de [[Identidades Vectoriales]].
> - Solo el **flujo cerrado** $\oint\vec S\cdot d\vec A$ es físicamente inequívoco; $\vec S$ admite un rotacional aditivo.
> - El momento del campo produce **presión de radiación**, real y medible; su flujo es el tensor $T_{ij}$, puente a la [[6 Formulacion Covariante/index | Formulación Covariante]].

> [!referencia] Fuentes
> - Griffiths, D. J., *Introduction to Electrodynamics*, 4.ª ed., capítulo 8 (§8.1 Energía y §8.2 Momento).
> - Jackson, J. D., *Classical Electrodynamics*, capítulo 6 (Conservation Laws).
> - Landau & Lifshitz, *Teoría Clásica de Campos*, vol. 2 (tensor energía–momento del campo).
