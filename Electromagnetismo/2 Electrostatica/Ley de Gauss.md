---
title: Ley de Gauss
order: 2
tags:
  - electromagnetismo
  - teoria
  - electrostatica
draft: false
aliases:
  - Ley de Gauss
  - Teorema de Gauss eléctrico
---

# Ley de Gauss $\oint_S\vec E\cdot d\vec A=\dfrac{Q_{\text{enc}}}{\varepsilon_0}$

> [!definicion]
> La **ley de Gauss** afirma que el **flujo** del campo eléctrico $\vec E$ a través de una superficie cerrada $S$ es proporcional a la **carga total encerrada** por dicha superficie. Tiene dos formas equivalentes:
>
> **Forma integral** (válida sobre cualquier superficie cerrada $S$ que limita un volumen $V$):
> $$\oint_S\vec E\cdot d\vec A=\frac{Q_{\text{enc}}}{\varepsilon_0},\qquad Q_{\text{enc}}=\int_V\rho\,dV.$$
>
> **Forma diferencial** (válida punto a punto):
> $$\nabla\cdot\vec E=\frac{\rho}{\varepsilon_0}.$$
>
> Aquí $d\vec A=\hat n\,dA$ es el elemento de área con normal **saliente**, $\rho$ la densidad volumétrica de carga y $\varepsilon_0$ la permitividad del vacío. Es la **primera ecuación de Maxwell** y la expresión local de que *la carga es la fuente del campo eléctrico*.

---

> [!info]
> **Nota del curso [[2 Electrostatica/index | Electrostática]]** (Capítulo 2 del curso Electromagnetismo). Es hermana de [[Ley de Coulomb y Campo Electrico]] —de la que se deduce— y de [[Potencial Electrico]] —que explota la otra ecuación, $\nabla\times\vec E=\vec 0$—. Usa el **teorema de la divergencia** de [[Teoremas Integrales]] para pasar de la forma integral a la diferencial, y la identidad $\nabla\cdot(\hat r/r^2)=4\pi\,\delta^3(\vec r)$ de [[Delta de Dirac y Singularidades]] para cerrar el círculo con Coulomb. **Referencia.** Griffiths, *Introduction to Electrodynamics*, cap. 2. Unidades SI; constante de Coulomb $k=\dfrac{1}{4\pi\varepsilon_0}$.

---

## El flujo de una carga puntual

> [!teoria] El flujo solo depende de la carga encerrada
> Toda la ley de Gauss descansa en un hecho geométrico sobre el campo de Coulomb: como $\vec E$ decae como $1/r^2$ y el área de una esfera crece como $r^2$, **el flujo total se vuelve independiente del radio**. Demostrémoslo y luego generalicémoslo a cualquier superficie por **ángulo sólido**.

> [!demostracion] Flujo de una carga puntual a través de una esfera centrada
> Sea una carga puntual $q$ en el origen. Su campo es
> $$\vec E=\frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\,\hat r .$$
>
> **Paso 1 — Elegir la superficie.** Tomamos una esfera $S$ de radio $r$ centrada en la carga. Por la simetría esférica, en cada punto de $S$ el campo es **radial** y de **módulo constante** $E(r)=\frac{q}{4\pi\varepsilon_0 r^2}$.
>
> **Paso 2 — Orientar el elemento de área.** La normal saliente de la esfera es también radial: $d\vec A=\hat r\,dA$. Por tanto
> $$\vec E\cdot d\vec A=\frac{q}{4\pi\varepsilon_0 r^2}\,(\hat r\cdot\hat r)\,dA=\frac{q}{4\pi\varepsilon_0 r^2}\,dA,$$
> ya que $\hat r\cdot\hat r=1$.
>
> **Paso 3 — Integrar.** El integrando es constante sobre $S$, así que sale de la integral:
> $$\oint_S\vec E\cdot d\vec A=\frac{q}{4\pi\varepsilon_0 r^2}\oint_S dA=\frac{q}{4\pi\varepsilon_0 r^2}\,(4\pi r^2).$$
>
> **Paso 4 — Simplificar.** Los factores $4\pi r^2$ se cancelan:
> $$\oint_S\vec E\cdot d\vec A=\frac{q}{\varepsilon_0}.$$
> El radio **desapareció**: el flujo es $q/\varepsilon_0$ para *toda* esfera centrada. $\blacksquare$

> [!demostracion] Generalización a cualquier superficie cerrada (ángulo sólido)
> Queremos ver que el resultado anterior vale para una superficie cerrada $S$ **cualquiera**, no solo esferas.
>
> **Paso 1 — Flujo como ángulo sólido.** Sobre un elemento $d\vec A$ situado a distancia $r$ de la carga y con normal $\hat n$,
> $$\vec E\cdot d\vec A=\frac{q}{4\pi\varepsilon_0 r^2}\,\hat r\cdot d\vec A=\frac{q}{4\pi\varepsilon_0}\,\frac{\hat r\cdot\hat n\,dA}{r^2}.$$
> La cantidad $d\Omega=\dfrac{\hat r\cdot\hat n\,dA}{r^2}$ es precisamente el **ángulo sólido** que el elemento $dA$ subtiende desde la carga: la proyección de $dA$ sobre la dirección radial, dividida por $r^2$.
>
> **Paso 2 — Integrar el ángulo sólido.** Si $S$ **encierra** la carga, los elementos cubren toda la esfera unidad una vez, de modo que $\displaystyle\oint_S d\Omega=4\pi$. Entonces
> $$\oint_S\vec E\cdot d\vec A=\frac{q}{4\pi\varepsilon_0}\oint_S d\Omega=\frac{q}{4\pi\varepsilon_0}\,(4\pi)=\frac{q}{\varepsilon_0}.$$
>
> **Paso 3 — Carga fuera de la superficie.** Si la carga está **fuera** de $S$, todo rayo que entra por una cara vuelve a salir por otra: el ángulo sólido se cancela a pares (un signo $+$ al salir, un signo $-$ al entrar), y $\displaystyle\oint_S d\Omega=0$. Luego el flujo es $0$.
>
> **Conclusión.**
> $$\oint_S\vec E\cdot d\vec A=\begin{cases}\dfrac{q}{\varepsilon_0}, & \text{si }S\text{ encierra a }q,\\[2mm]0, & \text{si no la encierra.}\end{cases}\qquad\blacksquare$$

---

## Ley de Gauss integral por superposición

> [!teorema] Ley de Gauss (forma integral)
> Para **cualquier** distribución de cargas y **cualquier** superficie cerrada $S$,
> $$\boxed{\ \oint_S\vec E\cdot d\vec A=\frac{Q_{\text{enc}}}{\varepsilon_0}\ }$$
> donde $Q_{\text{enc}}$ es la carga total encerrada por $S$.

> [!demostracion] Por el principio de superposición
> **Paso 1 — Superponer campos.** El campo total de un conjunto de cargas $\{q_i\}$ es la suma vectorial $\vec E=\sum_i\vec E_i$, con $\vec E_i$ el campo de cada carga (esto es [[Ley de Coulomb y Campo Electrico | superposición]]). El flujo es lineal en $\vec E$, así que
> $$\oint_S\vec E\cdot d\vec A=\sum_i\oint_S\vec E_i\cdot d\vec A.$$
>
> **Paso 2 — Aplicar el resultado puntual.** Por la demostración anterior, cada término vale $q_i/\varepsilon_0$ si $q_i$ está dentro de $S$, y $0$ si está fuera. Solo sobreviven las cargas encerradas:
> $$\oint_S\vec E\cdot d\vec A=\sum_{i\,\in\,V}\frac{q_i}{\varepsilon_0}=\frac{1}{\varepsilon_0}\sum_{i\,\in\,V}q_i=\frac{Q_{\text{enc}}}{\varepsilon_0}.$$
>
> **Paso 3 — Caso continuo.** Para una densidad $\rho$, la suma pasa a integral: $Q_{\text{enc}}=\displaystyle\int_V\rho\,dV$, y el resultado se mantiene. $\blacksquare$

---

## Forma diferencial

> [!teorema] Ley de Gauss (forma diferencial)
> $$\boxed{\ \nabla\cdot\vec E=\frac{\rho}{\varepsilon_0}\ }$$

> [!demostracion] Del flujo a la divergencia (teorema de la divergencia)
> **Paso 1 — Partir de la forma integral.** Para todo volumen $V$ con frontera $S=\partial V$,
> $$\oint_S\vec E\cdot d\vec A=\frac{Q_{\text{enc}}}{\varepsilon_0}=\frac{1}{\varepsilon_0}\int_V\rho\,dV.$$
>
> **Paso 2 — Convertir el flujo en integral de volumen.** El **teorema de la divergencia** ([[Teoremas Integrales]]) transforma el flujo por la superficie cerrada en una integral de $\nabla\cdot\vec E$ sobre el volumen:
> $$\oint_S\vec E\cdot d\vec A=\int_V(\nabla\cdot\vec E)\,dV.$$
>
> **Paso 3 — Igualar los integrandos.** Combinando ambas:
> $$\int_V(\nabla\cdot\vec E)\,dV=\int_V\frac{\rho}{\varepsilon_0}\,dV\ \Longrightarrow\ \int_V\!\left(\nabla\cdot\vec E-\frac{\rho}{\varepsilon_0}\right)dV=0.$$
> Como esto vale para **todo** volumen $V$ (incluso uno arbitrariamente pequeño), el integrando debe anularse en cada punto:
> $$\nabla\cdot\vec E=\frac{\rho}{\varepsilon_0}.\qquad\blacksquare$$

> [!info] El vínculo con la delta de Dirac
> La forma diferencial es coherente con Coulomb gracias a la identidad singular $\nabla\cdot\!\left(\dfrac{\hat r}{r^2}\right)=4\pi\,\delta^3(\vec r)$ de [[Delta de Dirac y Singularidades]]. Para una carga puntual $q$ en el origen, $\vec E=\dfrac{q}{4\pi\varepsilon_0}\dfrac{\hat r}{r^2}$, así que
> $$\nabla\cdot\vec E=\frac{q}{4\pi\varepsilon_0}\,\nabla\cdot\!\left(\frac{\hat r}{r^2}\right)=\frac{q}{4\pi\varepsilon_0}\,4\pi\,\delta^3(\vec r)=\frac{q\,\delta^3(\vec r)}{\varepsilon_0}=\frac{\rho}{\varepsilon_0},$$
> ya que la densidad de una carga puntual es $\rho(\vec r)=q\,\delta^3(\vec r)$. La delta concentra toda la divergencia en el punto donde está la carga, que es justo donde el campo $1/r^2$ "nace".

---

## Cálculo de $\vec E$ por simetría

> [!warning] Cuándo sirve Gauss para *calcular*
> La ley de Gauss es **siempre válida**, pero solo permite **despejar** $\vec E$ cuando la simetría del problema garantiza que $\vec E$ tiene dirección y módulo conocidos sobre una superficie gaussiana bien elegida —de modo que pueda **salir de la integral**—. Hay tres simetrías canónicas que lo permiten: **esférica**, **cilíndrica** y **plana**. Sin esa simetría, la ecuación sigue siendo cierta pero la integral acopla todas las componentes de $\vec E$ y no es resoluble directamente; entonces se recurre a la [[Potencial Electrico | vía del potencial]].

![[gauss_simetrias.svg|620]]
*Las tres superficies gaussianas canónicas: una esfera concéntrica (simetría esférica), un cilindro coaxial al hilo (simetría cilíndrica) y una "caja de píldoras" (pillbox) que atraviesa el plano (simetría plana). En cada caso se elige $S$ para que $\vec E$ sea constante y normal sobre la parte que aporta flujo.*

> [!proposicion] Simetría esférica: esfera uniforme de carga
> Una esfera de radio $R$ con carga total $Q$ repartida uniformemente ($\rho=\dfrac{Q}{\frac43\pi R^3}$) produce
> $$E(r)=\frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2}\ \ (r\ge R),\qquad E(r)=\frac{1}{4\pi\varepsilon_0}\frac{Q\,r}{R^3}\ \ (r\le R).$$
>
> > [!demostracion]
> > **Paso 1 — Simetría.** La distribución es invariante ante rotaciones, así que $\vec E=E(r)\,\hat r$: radial y de módulo dependiente solo de $r$.
> >
> > **Paso 2 — Gaussiana.** Tomamos una esfera concéntrica de radio $r$. Sobre ella $d\vec A=\hat r\,dA$ y $E$ es constante:
> > $$\oint_S\vec E\cdot d\vec A=E(r)\,(4\pi r^2).$$
> >
> > **Paso 3 — Carga encerrada y despeje.**
> > - **Fuera** ($r\ge R$): $Q_{\text{enc}}=Q$, luego $E(r)\,4\pi r^2=\dfrac{Q}{\varepsilon_0}$, de donde $E=\dfrac{1}{4\pi\varepsilon_0}\dfrac{Q}{r^2}$. *La esfera se ve igual que una carga puntual $Q$ en su centro.*
> > - **Dentro** ($r\le R$): solo se encierra la fracción de carga $Q_{\text{enc}}=Q\,\dfrac{\frac43\pi r^3}{\frac43\pi R^3}=Q\dfrac{r^3}{R^3}$. Entonces $E(r)\,4\pi r^2=\dfrac{Q\,r^3}{\varepsilon_0 R^3}$, de donde $E=\dfrac{1}{4\pi\varepsilon_0}\dfrac{Q\,r}{R^3}$, que crece linealmente con $r$. $\blacksquare$

> [!proposicion] Simetría cilíndrica: hilo infinito
> Un hilo recto infinito con densidad lineal $\lambda$ produce un campo radial (respecto al eje)
> $$E(s)=\frac{\lambda}{2\pi\varepsilon_0\,s},$$
> donde $s$ es la distancia perpendicular al hilo.
>
> > [!demostracion]
> > **Paso 1 — Simetría.** Por invariancia ante traslaciones a lo largo del hilo y rotaciones alrededor de él, $\vec E=E(s)\,\hat s$: apunta perpendicular al hilo y solo depende de $s$.
> >
> > **Paso 2 — Gaussiana.** Tomamos un cilindro coaxial de radio $s$ y longitud $L$. El flujo por las **tapas** es nulo ($\vec E\perp\hat n$ en ellas), y por la **superficie lateral** $\vec E\parallel\hat n$ con $E$ constante:
> > $$\oint_S\vec E\cdot d\vec A=E(s)\,(2\pi s\,L).$$
> >
> > **Paso 3 — Despeje.** La carga encerrada es $Q_{\text{enc}}=\lambda L$. Por Gauss,
> > $$E(s)\,2\pi s\,L=\frac{\lambda L}{\varepsilon_0}\ \Longrightarrow\ E(s)=\frac{\lambda}{2\pi\varepsilon_0\,s}.$$
> > El factor $L$ se cancela, como debía. $\blacksquare$

> [!proposicion] Simetría plana: plano infinito
> Un plano infinito con densidad superficial $\sigma$ produce un campo **uniforme** a ambos lados,
> $$E=\frac{\sigma}{2\varepsilon_0},$$
> dirigido perpendicularmente al plano y alejándose de él (si $\sigma>0$).
>
> > [!demostracion]
> > **Paso 1 — Simetría.** Por invariancia ante traslaciones en el plano, $\vec E$ es perpendicular al plano y su módulo no depende de la posición sobre él; por simetría de reflexión apunta en sentidos opuestos a cada lado.
> >
> > **Paso 2 — Gaussiana (pillbox).** Tomamos una "caja de píldoras" cilíndrica de área transversal $A$ que atraviesa el plano, con sus dos tapas paralelas a él. El flujo por la **pared lateral** es nulo ($\vec E\perp\hat n$); cada **tapa** aporta $E\,A$, así que
> > $$\oint_S\vec E\cdot d\vec A=2\,E\,A.$$
> >
> > **Paso 3 — Despeje.** La carga encerrada es $Q_{\text{enc}}=\sigma A$. Por Gauss,
> > $$2EA=\frac{\sigma A}{\varepsilon_0}\ \Longrightarrow\ E=\frac{\sigma}{2\varepsilon_0}.$$
> > El campo es **independiente de la distancia** al plano: uniforme. $\blacksquare$

---

## Ejemplo

> [!ejemplo] Esfera uniformemente cargada: campo dentro y fuera
> Una esfera aislante de radio $R$ porta una carga total $Q$ distribuida de forma **uniforme** en su volumen. Halla $\vec E(r)$ para todo $r$, discute la continuidad en $r=R$ y describe el perfil $E(r)$.

> [!solucion]
> **Paso 1 — Densidad.** $\displaystyle\rho=\frac{Q}{\tfrac43\pi R^3}=\frac{3Q}{4\pi R^3}$, constante.
>
> **Paso 2 — Simetría y gaussiana.** Por simetría esférica $\vec E=E(r)\,\hat r$. Sobre una esfera concéntrica de radio $r$:
> $$\oint_S\vec E\cdot d\vec A=E(r)\,4\pi r^2=\frac{Q_{\text{enc}}}{\varepsilon_0}.$$
>
> **Paso 3 — Región exterior** ($r\ge R$). Toda la carga queda encerrada, $Q_{\text{enc}}=Q$:
> $$E(r)=\frac{1}{4\pi\varepsilon_0}\frac{Q}{r^2}.$$
> Idéntico al de una carga puntual $Q$ centrada.
>
> **Paso 4 — Región interior** ($r\le R$). Se encierra solo $Q_{\text{enc}}=\rho\cdot\tfrac43\pi r^3=Q\,\dfrac{r^3}{R^3}$:
> $$E(r)\,4\pi r^2=\frac{Q\,r^3}{\varepsilon_0 R^3}\ \Longrightarrow\ E(r)=\frac{1}{4\pi\varepsilon_0}\frac{Q\,r}{R^3}.$$
> Crece linealmente desde $0$ en el centro.
>
> **Paso 5 — Continuidad en $r=R$.** Evaluando ambas expresiones en la frontera:
> $$E_{\text{int}}(R)=\frac{1}{4\pi\varepsilon_0}\frac{Q\,R}{R^3}=\frac{1}{4\pi\varepsilon_0}\frac{Q}{R^2}=E_{\text{ext}}(R).$$
> El campo es **continuo** en $r=R$ —como debe ocurrir cuando solo hay carga **volumétrica** (no una capa superficial), pues una densidad superficial introduciría un salto $\sigma/\varepsilon_0$—.
>
> **Perfil $E(r)$.** El campo crece **linealmente** $E\propto r$ dentro de la esfera, alcanza su **máximo** $E_{\max}=\dfrac{Q}{4\pi\varepsilon_0 R^2}$ en la superficie, y luego **decae** como $1/r^2$ fuera:
> $$E(r)=\begin{cases}\dfrac{1}{4\pi\varepsilon_0}\dfrac{Q\,r}{R^3}, & r\le R,\\[3mm]\dfrac{1}{4\pi\varepsilon_0}\dfrac{Q}{r^2}, & r\ge R.\end{cases}$$

---

## En qué consiste

La ley de Gauss es, en el fondo, una afirmación geométrica disfrazada de ley física: como el campo de Coulomb decae exactamente como $1/r^2$ y el área crece como $r^2$, **el número de líneas de campo que atraviesa una superficie cerrada solo cuenta cuántas cargas hay dentro**, no a qué distancia ni con qué forma. Esa es la intuición de las **líneas de campo**: cada carga emite (o absorbe) un número fijo de líneas, y el flujo cuenta líneas netas.

Su valor práctico es doble. Como **principio**, $\nabla\cdot\vec E=\rho/\varepsilon_0$ es una de las cuatro ecuaciones de Maxwell y codifica que *la carga es la fuente del campo*. Como **herramienta de cálculo**, convierte un problema de integración vectorial difícil en una ecuación algebraica trivial —pero **solo cuando hay simetría suficiente**—: la simetría nos dice de antemano la dirección de $\vec E$ y que su módulo es constante sobre la gaussiana adecuada, y entonces $\vec E$ "sale" de la integral. Las tres geometrías canónicas (esférica, cilíndrica, plana) cubren la inmensa mayoría de los problemas resolubles así; fuera de ellas, hay que pasar por el [[Potencial Electrico | potencial]] o resolver [[Poisson y Laplace]].

Conviene recordar el lugar de Gauss en la estructura del capítulo: es la **forma integral** de la primera ecuación de Maxwell, equivalente a Coulomb más superposición. La otra ecuación estática, $\nabla\times\vec E=\vec 0$, da pie al potencial. Juntas determinan completamente el campo electrostático.

---

## Resumen

> [!resumen] Ley de Gauss de un vistazo
>
> | Concepto | Expresión | Observación |
> |---|---|---|
> | Forma integral | $\oint_S\vec E\cdot d\vec A=\dfrac{Q_{\text{enc}}}{\varepsilon_0}$ | Vale para toda $S$ cerrada |
> | Forma diferencial | $\nabla\cdot\vec E=\dfrac{\rho}{\varepsilon_0}$ | Por teorema de la divergencia |
> | Carga encerrada | $Q_{\text{enc}}=\displaystyle\int_V\rho\,dV$ | Solo cuenta lo de dentro |
> | Esfera uniforme $Q,R$ | $E=\dfrac{1}{4\pi\varepsilon_0}\dfrac{Q}{r^2}$ ($r\ge R$);\ $\dfrac{1}{4\pi\varepsilon_0}\dfrac{Qr}{R^3}$ ($r\le R$) | Continuo en $r=R$ |
> | Hilo infinito $\lambda$ | $E=\dfrac{\lambda}{2\pi\varepsilon_0\,s}$ | Decae como $1/s$ |
> | Plano infinito $\sigma$ | $E=\dfrac{\sigma}{2\varepsilon_0}$ | Uniforme, independiente de la distancia |
>
> *(En las celdas, $\|$ separa los dos tramos del resultado esférico.)*

> [!corolario] Ideas clave
> - El flujo de una carga por **cualquier** superficie cerrada que la encierre es $q/\varepsilon_0$ (ángulo sólido $4\pi$); $0$ si no la encierra.
> - Gauss $=$ Coulomb $+$ superposición; su forma local es $\nabla\cdot\vec E=\rho/\varepsilon_0$.
> - **Siempre válida**, pero solo **calcula** $\vec E$ con simetría esférica, cilíndrica o plana.
> - El vínculo con $\nabla\cdot(\hat r/r^2)=4\pi\,\delta^3(\vec r)$ hace que la carga puntual sea la fuente del campo $1/r^2$.

> [!referencia]
> Griffiths, *Introduction to Electrodynamics*, cap. 2 (secciones 2.2 sobre divergencia y rotacional de $\vec E$, y la ley de Gauss). Para mayor profundidad y el tratamiento del ángulo sólido: Jackson, *Classical Electrodynamics*, cap. 1.
