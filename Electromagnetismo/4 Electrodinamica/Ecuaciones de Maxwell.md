---
title: Ecuaciones de Maxwell
order: 3
tags:
  - electromagnetismo
  - teoria
  - electrodinamica
draft: false
aliases:
  - Ecuaciones de Maxwell
  - Maxwell
---

# Ecuaciones de Maxwell $\nabla\cdot\vec E=\rho/\varepsilon_0,\ \nabla\cdot\vec B=0,\ \nabla\times\vec E=-\partial_t\vec B,\ \nabla\times\vec B=\mu_0\vec J+\mu_0\varepsilon_0\partial_t\vec E$

---

> [!definicion] Las cuatro ecuaciones de Maxwell y la fuerza de Lorentz
> En el vacío, los campos eléctrico $\vec E(\vec r,t)$ y magnético $\vec B(\vec r,t)$ obedecen, en **forma diferencial**:
>
> $$
> \begin{aligned}
> \nabla\cdot\vec E &= \frac{\rho}{\varepsilon_0} && \text{(Gauss eléctrico)}\\[4pt]
> \nabla\cdot\vec B &= 0 && \text{(Gauss magnético)}\\[4pt]
> \nabla\times\vec E &= -\frac{\partial \vec B}{\partial t} && \text{(Faraday)}\\[4pt]
> \nabla\times\vec B &= \mu_0\,\vec J + \mu_0\varepsilon_0\,\frac{\partial \vec E}{\partial t} && \text{(Ampère–Maxwell)}
> \end{aligned}
> $$
>
> con $\rho$ la densidad de carga y $\vec J$ la densidad de corriente. La **fuerza de Lorentz** cierra la teoría diciendo cómo los campos actúan sobre una carga $q$ con velocidad $\vec v$:
>
> $$
> \vec F = q\left(\vec E + \vec v\times\vec B\right).
> $$
>
> Constantes: $\varepsilon_0 = 8{,}854\times10^{-12}\ \mathrm{F/m}$ (permitividad del vacío), $\mu_0 = 4\pi\times10^{-7}\ \mathrm{H/m}$ (permeabilidad del vacío), con $c = 1/\sqrt{\mu_0\varepsilon_0} \approx 2{,}998\times10^{8}\ \mathrm{m/s}$.

---

> [!info] Ubicación y vecindad
> Esta nota pertenece a [[4 Electrodinamica/index | Electrodinámica]]. Sus hermanas son [[Ley de Faraday]], [[Corriente de Desplazamiento]], [[Potenciales y Gauge]] y [[Energia y Momento]]. Las cuatro ecuaciones reúnen y completan todo lo construido en electrostática y magnetostática; el ingrediente nuevo —la corriente de desplazamiento $\mu_0\varepsilon_0\,\partial_t\vec E$— es lo que las cierra y hace aparecer las ondas. Seguimos a Griffiths, *Introduction to Electrodynamics*, cap. 7.

---

## En qué consiste

Las ecuaciones de Maxwell son el resumen de **todos** los hechos experimentales del electromagnetismo clásico en cuatro ecuaciones de campo, más la fuerza de Lorentz que traduce campos en fuerzas. Cada una codifica una ley física distinta, y cada una tiene una **forma diferencial** (puntual, local) y una **forma integral** (global, sobre regiones o superficies). Las dos versiones son equivalentes gracias a los teoremas de la [[1 Calculo Vectorial/index | divergencia y de Stokes]].

### Gauss eléctrico — las cargas son fuentes de $\vec E$

$$
\nabla\cdot\vec E = \frac{\rho}{\varepsilon_0}
\qquad\Longleftrightarrow\qquad
\oint_{\partial V}\vec E\cdot d\vec A = \frac{Q_{\text{enc}}}{\varepsilon_0}.
$$

El flujo de $\vec E$ a través de una superficie cerrada mide la carga encerrada: las líneas de campo **nacen** en cargas positivas y **mueren** en negativas. La divergencia es la versión puntual de ese mismo enunciado.

### Gauss magnético — no hay monopolos

$$
\nabla\cdot\vec B = 0
\qquad\Longleftrightarrow\qquad
\oint_{\partial V}\vec B\cdot d\vec A = 0.
$$

El flujo magnético neto a través de cualquier superficie cerrada es nulo: las líneas de $\vec B$ **no tienen principio ni fin**, siempre se cierran sobre sí mismas. No existe la "carga magnética" aislada.

### Faraday — un $\vec B$ variable genera $\vec E$ rotacional

$$
\nabla\times\vec E = -\frac{\partial\vec B}{\partial t}
\qquad\Longleftrightarrow\qquad
\oint_{\partial S}\vec E\cdot d\vec\ell = -\frac{d}{dt}\int_S\vec B\cdot d\vec A = -\frac{d\Phi_B}{dt}.
$$

La fuerza electromotriz inducida en un circuito es menos la tasa de cambio del flujo magnético que lo atraviesa (ver [[Ley de Faraday]]). El signo menos es la [[Ley de Faraday | ley de Lenz]]: la inducción se opone al cambio.

### Ampère–Maxwell — corrientes y $\vec E$ variable generan $\vec B$

$$
\nabla\times\vec B = \mu_0\vec J + \mu_0\varepsilon_0\frac{\partial\vec E}{\partial t}
\quad\Longleftrightarrow\quad
\oint_{\partial S}\vec B\cdot d\vec\ell = \mu_0 I_{\text{enc}} + \mu_0\varepsilon_0\frac{d}{dt}\int_S\vec E\cdot d\vec A.
$$

El término $\mu_0\varepsilon_0\,\partial_t\vec E$ es la [[Corriente de Desplazamiento | corriente de desplazamiento]]: la pieza que Maxwell **añadió** a la ley de Ampère y que vuelve la teoría consistente (lo demostramos abajo) y predictiva de ondas.

> [!resumen] Diccionario diferencial ↔ integral
>
> | Ley | Forma diferencial | Forma integral |
> |---|---|---|
> | Gauss eléctrico | $\nabla\cdot\vec E=\rho/\varepsilon_0$ | $\oint\vec E\cdot d\vec A=Q_{\text{enc}}/\varepsilon_0$ |
> | Gauss magnético | $\nabla\cdot\vec B=0$ | $\oint\vec B\cdot d\vec A=0$ |
> | Faraday | $\nabla\times\vec E=-\partial_t\vec B$ | $\oint\vec E\cdot d\vec\ell=-d\Phi_B/dt$ |
> | Ampère–Maxwell | $\nabla\times\vec B=\mu_0\vec J+\mu_0\varepsilon_0\,\partial_t\vec E$ | $\oint\vec B\cdot d\vec\ell=\mu_0 I_{\text{enc}}+\mu_0\varepsilon_0\,d\Phi_E/dt$ |

![[maxwell_acoplamiento.svg|460]]

**Figura.** El bucle de retroalimentación de Maxwell. Por **Faraday**, un campo magnético $\vec B$ que varía en el tiempo genera un campo eléctrico $\vec E$ con rotacional. Por **Ampère–Maxwell**, ese $\vec E$ variable genera a su vez un $\vec B$ con rotacional. Cada campo se "regenera" del otro: el acoplamiento se autosostiene y se propaga por el espacio como una **onda electromagnética**, sin necesidad de cargas ni corrientes.

---

## Conservación de la carga como consecuencia

Un test de consistencia interna: las ecuaciones de Maxwell **no son independientes** de la conservación de la carga. La continuidad

$$
\nabla\cdot\vec J + \frac{\partial\rho}{\partial t} = 0
$$

no hay que postularla aparte; ya está **contenida** en las ecuaciones.

> [!teorema] Maxwell implica la ecuación de continuidad
> De Gauss eléctrico y Ampère–Maxwell se deduce $\nabla\cdot\vec J+\partial_t\rho=0$.

> [!demostracion]
> **Paso 1 — Tomar la divergencia de Ampère–Maxwell.** Aplicamos $\nabla\cdot$ a ambos lados de
> $$
> \nabla\times\vec B = \mu_0\vec J + \mu_0\varepsilon_0\frac{\partial\vec E}{\partial t},
> $$
> obteniendo
> $$
> \nabla\cdot(\nabla\times\vec B) = \mu_0\,\nabla\cdot\vec J + \mu_0\varepsilon_0\,\nabla\cdot\frac{\partial\vec E}{\partial t}.
> $$
>
> **Paso 2 — El lado izquierdo se anula.** La divergencia de un rotacional es idénticamente cero (ver [[Identidades Vectoriales]]):
> $$
> \nabla\cdot(\nabla\times\vec B) = 0.
> $$
>
> **Paso 3 — Intercambiar derivadas y usar Gauss.** Como las derivadas espaciales y la temporal conmutan,
> $$
> \nabla\cdot\frac{\partial\vec E}{\partial t} = \frac{\partial}{\partial t}\big(\nabla\cdot\vec E\big) = \frac{\partial}{\partial t}\left(\frac{\rho}{\varepsilon_0}\right) = \frac{1}{\varepsilon_0}\frac{\partial\rho}{\partial t},
> $$
> donde en el penúltimo paso usamos **Gauss eléctrico** $\nabla\cdot\vec E=\rho/\varepsilon_0$.
>
> **Paso 4 — Sustituir y simplificar.** Reemplazando en la igualdad del Paso 1:
> $$
> 0 = \mu_0\,\nabla\cdot\vec J + \mu_0\varepsilon_0\cdot\frac{1}{\varepsilon_0}\frac{\partial\rho}{\partial t}
> = \mu_0\left(\nabla\cdot\vec J + \frac{\partial\rho}{\partial t}\right).
> $$
> Como $\mu_0\neq 0$, dividimos y obtenemos
> $$
> \nabla\cdot\vec J + \frac{\partial\rho}{\partial t} = 0. \qquad\blacksquare
> $$

> [!corolario] Por qué hacía falta la corriente de desplazamiento
> Sin el término $\mu_0\varepsilon_0\,\partial_t\vec E$, la ley de Ampère sería $\nabla\times\vec B=\mu_0\vec J$, y su divergencia daría $0=\mu_0\nabla\cdot\vec J$, es decir $\nabla\cdot\vec J=0$ **siempre**. Eso contradice la conservación de la carga en situaciones no estacionarias (por ejemplo, un condensador cargándose). El término de Maxwell repara exactamente esa inconsistencia.

---

## Las ondas emergen

Esta es la deducción estelar: combinando las cuatro ecuaciones **en el vacío** ($\rho=0$, $\vec J=0$), los campos satisfacen una ecuación de ondas. La electrodinámica predice la luz.

> [!teorema] Ecuación de ondas para los campos en el vacío
> En una región sin cargas ni corrientes, cada componente de $\vec E$ y $\vec B$ satisface
> $$
> \nabla^2\vec E = \mu_0\varepsilon_0\,\frac{\partial^2\vec E}{\partial t^2},
> \qquad
> \nabla^2\vec B = \mu_0\varepsilon_0\,\frac{\partial^2\vec B}{\partial t^2},
> $$
> que son ecuaciones de onda con velocidad de propagación $c = 1/\sqrt{\mu_0\varepsilon_0}$.

> [!demostracion]
> **Paso 1 — Aplicar el rotacional a Faraday.** En el vacío, Faraday sigue siendo $\nabla\times\vec E=-\partial_t\vec B$. Tomamos $\nabla\times$ a ambos lados:
> $$
> \nabla\times(\nabla\times\vec E) = \nabla\times\left(-\frac{\partial\vec B}{\partial t}\right) = -\frac{\partial}{\partial t}\big(\nabla\times\vec B\big).
> $$
>
> **Paso 2 — Sustituir Ampère–Maxwell.** Con $\vec J=0$, la cuarta ecuación es $\nabla\times\vec B=\mu_0\varepsilon_0\,\partial_t\vec E$. Insertándola:
> $$
> \nabla\times(\nabla\times\vec E) = -\frac{\partial}{\partial t}\left(\mu_0\varepsilon_0\frac{\partial\vec E}{\partial t}\right) = -\mu_0\varepsilon_0\,\frac{\partial^2\vec E}{\partial t^2}.
> $$
>
> **Paso 3 — Desarrollar el doble rotacional (BAC–CAB).** La identidad vectorial (ver [[Identidades Vectoriales]]) dice
> $$
> \nabla\times(\nabla\times\vec E) = \nabla(\nabla\cdot\vec E) - \nabla^2\vec E.
> $$
> En el vacío, **Gauss eléctrico** da $\nabla\cdot\vec E=\rho/\varepsilon_0=0$, de modo que el primer término desaparece:
> $$
> \nabla\times(\nabla\times\vec E) = -\nabla^2\vec E.
> $$
>
> **Paso 4 — Igualar y ordenar.** Combinando el Paso 2 con el Paso 3:
> $$
> -\nabla^2\vec E = -\mu_0\varepsilon_0\,\frac{\partial^2\vec E}{\partial t^2}
> \quad\Longrightarrow\quad
> \boxed{\;\nabla^2\vec E = \mu_0\varepsilon_0\,\frac{\partial^2\vec E}{\partial t^2}\;}
> $$
>
> **Paso 5 — Análogo para $\vec B$.** Repitiendo el argumento partiendo de Ampère–Maxwell ($\nabla\times\vec B=\mu_0\varepsilon_0\,\partial_t\vec E$), aplicando $\nabla\times$ y usando Faraday y $\nabla\cdot\vec B=0$, se obtiene idénticamente
> $$
> \nabla^2\vec B = \mu_0\varepsilon_0\,\frac{\partial^2\vec B}{\partial t^2}. \qquad\blacksquare
> $$

> [!corolario] La luz es electromagnetismo
> Comparando con la ecuación de ondas estándar $\nabla^2 f = \dfrac{1}{v^2}\partial_t^2 f$, la velocidad de propagación es
> $$
> c = \frac{1}{\sqrt{\mu_0\varepsilon_0}} = \frac{1}{\sqrt{(4\pi\times10^{-7})(8{,}854\times10^{-12})}} \approx 2{,}998\times10^{8}\ \mathrm{m/s},
> $$
> que coincide con la velocidad medida de la luz. Maxwell concluyó que **la luz es una onda electromagnética**. El desarrollo completo de estas soluciones está en [[5 Ondas Electromagneticas/index | Ondas Electromagnéticas]].

---

## Maxwell en medios materiales

Dentro de la materia conviene separar cargas y corrientes **libres** de las **ligadas** (polarización $\vec P$ y magnetización $\vec M$). Definiendo los campos auxiliares
$$
\vec D = \varepsilon_0\vec E + \vec P,
\qquad
\vec H = \frac{1}{\mu_0}\vec B - \vec M,
$$
las ecuaciones adoptan la forma macroscópica:

$$
\begin{aligned}
\nabla\cdot\vec D &= \rho_{\text{libre}}, &
\nabla\cdot\vec B &= 0,\\[4pt]
\nabla\times\vec E &= -\frac{\partial\vec B}{\partial t}, &
\nabla\times\vec H &= \vec J_{\text{libre}} + \frac{\partial\vec D}{\partial t}.
\end{aligned}
$$

En **medios lineales, homogéneos e isótropos** se cumplen las relaciones constitutivas
$$
\vec D = \varepsilon\,\vec E,
\qquad
\vec H = \frac{\vec B}{\mu},
$$
con $\varepsilon=\varepsilon_0\varepsilon_r$ la permitividad y $\mu=\mu_0\mu_r$ la permeabilidad del medio (ver [[2 Electrostatica/Dielectricos/index | Dieléctricos]] y [[Materiales Magneticos]]). Las ecuaciones recuperan la misma forma que en el vacío con la sustitución $\varepsilon_0\to\varepsilon$, $\mu_0\to\mu$; en particular la velocidad de las ondas en el medio es $v=1/\sqrt{\mu\varepsilon}=c/n$, con $n=\sqrt{\varepsilon_r\mu_r}$ el índice de refracción.

---

## Ejemplo

> [!ejemplo] Una onda plana satisface Maxwell en el vacío
> Verificar que los campos
> $$
> \vec E(z,t) = E_0\cos(kz-\omega t)\,\hat x,
> \qquad
> \vec B(z,t) = \frac{E_0}{c}\cos(kz-\omega t)\,\hat y,
> $$
> satisfacen las cuatro ecuaciones de Maxwell en el vacío ($\rho=0$, $\vec J=0$) **si y solo si** $\omega = ck$.

> [!solucion]
> Llamemos $u \equiv \cos(kz-\omega t)$. Sus derivadas útiles son
> $$
> \frac{\partial u}{\partial z} = -k\sin(kz-\omega t),
> \qquad
> \frac{\partial u}{\partial t} = \omega\sin(kz-\omega t).
> $$
>
> **Paso 1 — Gauss eléctrico.** Como $\vec E$ solo tiene componente $x$ y depende solo de $z$ y $t$:
> $$
> \nabla\cdot\vec E = \frac{\partial E_x}{\partial x} = 0 = \frac{\rho}{\varepsilon_0}. \checkmark
> $$
>
> **Paso 2 — Gauss magnético.** Análogamente, $\vec B$ solo tiene componente $y$ dependiente de $z,t$:
> $$
> \nabla\cdot\vec B = \frac{\partial B_y}{\partial y} = 0. \checkmark
> $$
>
> **Paso 3 — Faraday.** El rotacional de $\vec E=E_x\,\hat x$ (con $E_x$ función de $z,t$) es
> $$
> \nabla\times\vec E = \frac{\partial E_x}{\partial z}\,\hat y = -E_0 k\sin(kz-\omega t)\,\hat y.
> $$
> Por otro lado,
> $$
> -\frac{\partial\vec B}{\partial t} = -\frac{E_0}{c}\,\omega\sin(kz-\omega t)\,\hat y.
> $$
> Igualando componentes $\hat y$:
> $$
> -E_0 k = -\frac{E_0\omega}{c}\quad\Longrightarrow\quad \omega = ck. \checkmark
> $$
>
> **Paso 4 — Ampère–Maxwell.** El rotacional de $\vec B=B_y\,\hat y$ (con $B_y$ función de $z,t$) es
> $$
> \nabla\times\vec B = -\frac{\partial B_y}{\partial z}\,\hat x = \frac{E_0 k}{c}\sin(kz-\omega t)\,\hat x.
> $$
> El lado derecho, con $\vec J=0$, es
> $$
> \mu_0\varepsilon_0\frac{\partial\vec E}{\partial t} = \mu_0\varepsilon_0\,E_0\,\omega\sin(kz-\omega t)\,\hat x = \frac{\omega E_0}{c^2}\sin(kz-\omega t)\,\hat x,
> $$
> donde usamos $\mu_0\varepsilon_0=1/c^2$. Igualando los factores $\hat x$:
> $$
> \frac{E_0 k}{c} = \frac{\omega E_0}{c^2}\quad\Longrightarrow\quad \omega = ck. \checkmark
> $$
>
> **Conclusión.** Las cuatro ecuaciones se cumplen exactamente cuando $\boxed{\omega = ck}$, la **relación de dispersión** del vacío. La onda viaja en $+\hat z$ con $\vec E\perp\vec B\perp\hat z$ y $|\vec B|=|\vec E|/c$. $\blacksquare$

---

> [!warning] Toda la electrodinámica clásica cabe aquí
> Las **cuatro ecuaciones de Maxwell más la fuerza de Lorentz** constituyen la totalidad de la electrodinámica clásica. Todo lo demás —la propagación de ondas, la radiación de cargas aceleradas, la óptica, la teoría de circuitos, las guías de onda— se **deduce** de ellas; no hay leyes electromagnéticas adicionales. Si un resultado parece contradecirlas, el error está en el resultado, no en Maxwell.

---

## Resumen

> [!resumen] Lo esencial
>
> | Concepto | Expresión | Significado |
> |---|---|---|
> | Gauss eléctrico | $\nabla\cdot\vec E=\rho/\varepsilon_0$ | la carga es fuente de $\vec E$ |
> | Gauss magnético | $\nabla\cdot\vec B=0$ | no hay monopolos magnéticos |
> | Faraday | $\nabla\times\vec E=-\partial_t\vec B$ | $\vec B$ variable induce $\vec E$ |
> | Ampère–Maxwell | $\nabla\times\vec B=\mu_0\vec J+\mu_0\varepsilon_0\,\partial_t\vec E$ | corriente y $\vec E$ variable inducen $\vec B$ |
> | Lorentz | $\vec F=q(\vec E+\vec v\times\vec B)$ | acción de los campos sobre la carga |
> | Continuidad | $\nabla\cdot\vec J+\partial_t\rho=0$ | consecuencia, no postulado |
> | Onda en vacío | $\nabla^2\vec E=\mu_0\varepsilon_0\,\partial_t^2\vec E$ | con $c=1/\sqrt{\mu_0\varepsilon_0}$ |
> | En medios | $\nabla\cdot\vec D=\rho_{\text{lib}},\ \nabla\times\vec H=\vec J_{\text{lib}}+\partial_t\vec D$ | $\vec D=\varepsilon\vec E,\ \vec H=\vec B/\mu$ |

> [!corolario] Idea para recordar
> Maxwell unifica electricidad, magnetismo y óptica en una sola estructura **autoconsistente** (implica la conservación de la carga) y **predictiva** (predice ondas a velocidad $c$). La corriente de desplazamiento es la pieza que cierra el círculo: sin ella no hay consistencia ni ondas.

> [!referencia] Fuentes y conexiones
> - Griffiths, *Introduction to Electrodynamics*, cap. 7 (Electrodinámica) y §9 (Ondas).
> - Jackson, *Classical Electrodynamics*, cap. 6.
> - Landau & Lifshitz, *Teoría clásica de campos* (vol. 2).
> - Notas relacionadas: [[Ley de Faraday]], [[Corriente de Desplazamiento]], [[Potenciales y Gauge]], [[Energia y Momento]], [[5 Ondas Electromagneticas/index | Ondas Electromagnéticas]], [[Identidades Vectoriales]], [[2 Electrostatica/Dielectricos/index | Dieléctricos]], [[Materiales Magneticos]].
