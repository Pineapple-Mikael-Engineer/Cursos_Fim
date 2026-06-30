---
title: Ecuación de Ondas
order: 1
tags:
  - electromagnetismo
  - teoria
  - ondas
draft: false
aliases:
  - Ecuación de ondas
  - Ecuación de d'Alembert
---

# Ecuación de Ondas $\nabla^2\vec E=\dfrac{1}{c^2}\dfrac{\partial^2\vec E}{\partial t^2}$

> [!definicion]
> La **ecuación de ondas** electromagnética es la ecuación diferencial en derivadas parciales que satisfacen, en el vacío y en ausencia de fuentes ($\rho=0$, $\vec J=\vec 0$), cada componente del campo eléctrico $\vec E$ y del campo magnético $\vec B$:
> $$\nabla^2\vec E=\frac{1}{c^2}\frac{\partial^2\vec E}{\partial t^2},\qquad \nabla^2\vec B=\frac{1}{c^2}\frac{\partial^2\vec B}{\partial t^2}.$$
> Es una ecuación **hiperbólica** de segundo orden que describe perturbaciones que se propagan en el espacio a velocidad finita $c$. Definiendo el **operador de d'Alembert** (o **dalambertiano**)
> $$\Box\equiv\nabla^2-\frac{1}{c^2}\frac{\partial^2}{\partial t^2},$$
> ambas ecuaciones se escriben de forma compacta como $\Box\vec E=\vec 0$ y $\Box\vec B=\vec 0$. La velocidad de propagación es
> $$c=\frac{1}{\sqrt{\mu_0\varepsilon_0}},$$
> es decir, queda fijada **únicamente** por las constantes electromagnéticas del vacío.

> [!info]
> Pertenece a la sección [[5 Ondas Electromagneticas/index | Ondas Electromagnéticas]]. Sus notas hermanas son [[Ondas Planas]] (la solución particular más importante de esta ecuación) y [[Ondas en Medios]] (cómo cambian $c$, $\lambda$ y la amplitud al propagarse en materia). La deducción parte de las [[Ecuaciones de Maxwell]] y se apoya en las [[Identidades Vectoriales]] (en particular la identidad BAC–CAB para el doble rotacional). Referencia: Griffiths, *Introduction to Electrodynamics*, cap. 9.

---

## Deducción desde las ecuaciones de Maxwell

> [!teorema]
> En el vacío sin fuentes ($\rho=0$, $\vec J=\vec 0$), los campos $\vec E$ y $\vec B$ satisfacen la ecuación de ondas con velocidad $c=1/\sqrt{\mu_0\varepsilon_0}$.

Las [[Ecuaciones de Maxwell]] en el vacío sin fuentes son:

$$
\begin{aligned}
\nabla\cdot\vec E&=0 &&\text{(Gauss eléctrica)},\\
\nabla\cdot\vec B&=0 &&\text{(Gauss magnética)},\\
\nabla\times\vec E&=-\frac{\partial\vec B}{\partial t} &&\text{(Faraday)},\\
\nabla\times\vec B&=\mu_0\varepsilon_0\,\frac{\partial\vec E}{\partial t} &&\text{(Ampère–Maxwell)}.
\end{aligned}
$$

> [!demostracion]
> Buscamos una ecuación que involucre **solo** a $\vec E$. La estrategia es eliminar a $\vec B$ tomando un segundo rotacional.
>
> **Paso 1 — Aplicar $\nabla\times$ a la ley de Faraday.** Tomamos el rotacional de ambos lados de $\nabla\times\vec E=-\partial_t\vec B$:
> $$\nabla\times(\nabla\times\vec E)=\nabla\times\left(-\frac{\partial\vec B}{\partial t}\right)=-\frac{\partial}{\partial t}\big(\nabla\times\vec B\big),$$
> donde hemos intercambiado el rotacional espacial con la derivada temporal (los operadores actúan sobre variables independientes).
>
> **Paso 2 — Sustituir Ampère–Maxwell en el lado derecho.** Como $\nabla\times\vec B=\mu_0\varepsilon_0\,\partial_t\vec E$:
> $$\nabla\times(\nabla\times\vec E)=-\frac{\partial}{\partial t}\left(\mu_0\varepsilon_0\,\frac{\partial\vec E}{\partial t}\right)=-\mu_0\varepsilon_0\,\frac{\partial^2\vec E}{\partial t^2}.$$
>
> **Paso 3 — Desarrollar el lado izquierdo con BAC–CAB.** La identidad del doble rotacional ([[Identidades Vectoriales]]) establece
> $$\nabla\times(\nabla\times\vec E)=\nabla(\nabla\cdot\vec E)-\nabla^2\vec E.$$
> Pero la ley de Gauss en el vacío da $\nabla\cdot\vec E=0$, de modo que el primer término se anula:
> $$\nabla\times(\nabla\times\vec E)=-\nabla^2\vec E.$$
>
> **Paso 4 — Igualar ambas expresiones.** Combinando los Pasos 2 y 3:
> $$-\nabla^2\vec E=-\mu_0\varepsilon_0\,\frac{\partial^2\vec E}{\partial t^2}\;\Longrightarrow\;\boxed{\;\nabla^2\vec E=\mu_0\varepsilon_0\,\frac{\partial^2\vec E}{\partial t^2}\;}$$
>
> **Paso 5 — El campo magnético cumple lo mismo.** El argumento es idéntico cambiando los papeles. Tomamos $\nabla\times$ de Ampère–Maxwell:
> $$\nabla\times(\nabla\times\vec B)=\mu_0\varepsilon_0\,\frac{\partial}{\partial t}\big(\nabla\times\vec E\big)=\mu_0\varepsilon_0\,\frac{\partial}{\partial t}\left(-\frac{\partial\vec B}{\partial t}\right)=-\mu_0\varepsilon_0\,\frac{\partial^2\vec B}{\partial t^2}.$$
> Con BAC–CAB y $\nabla\cdot\vec B=0$ se tiene $\nabla\times(\nabla\times\vec B)=-\nabla^2\vec B$, y por tanto
> $$\nabla^2\vec B=\mu_0\varepsilon_0\,\frac{\partial^2\vec B}{\partial t^2}.$$
>
> **Paso 6 — Identificar la velocidad.** Comparando con la forma canónica $\nabla^2 u=\frac{1}{c^2}\partial_t^2 u$, la constante que multiplica a la derivada temporal debe ser $1/c^2$. Luego
> $$\mu_0\varepsilon_0=\frac{1}{c^2}\;\Longrightarrow\;c=\frac{1}{\sqrt{\mu_0\varepsilon_0}}.\qquad\blacksquare$$

> [!teoria] Evaluación numérica de $c$
> Con $\mu_0=4\pi\times10^{-7}\ \mathrm{T\,m/A}$ y $\varepsilon_0=8{,}854\times10^{-12}\ \mathrm{C^2/(N\,m^2)}$:
> $$c=\frac{1}{\sqrt{(4\pi\times10^{-7})(8{,}854\times10^{-12})}}\approx 3{,}00\times10^{8}\ \mathrm{m/s}.$$
> Este número coincide con la velocidad de la luz medida ópticamente: fue la pista que llevó a Maxwell a concluir que la luz **es** una onda electromagnética.

---

## Solución general de d'Alembert

Reducimos el problema a una dimensión espacial. Sea $u(z,t)$ una componente cartesiana cualquiera del campo (por ejemplo $E_x$) que depende solo de $z$ y $t$. La ecuación de ondas se reduce a

$$\frac{\partial^2 u}{\partial z^2}=\frac{1}{c^2}\frac{\partial^2 u}{\partial t^2}.$$

> [!proposicion]
> La solución general de la ecuación de ondas unidimensional es
> $$u(z,t)=f(z-ct)+g(z+ct),$$
> con $f$ y $g$ funciones **arbitrarias** (dos veces derivables). El término $f(z-ct)$ representa un pulso que viaja hacia $+z$ y $g(z+ct)$ uno que viaja hacia $-z$, ambos a velocidad $c$ y **sin deformarse**.

> [!demostracion]
> **Paso 1 — Cambio de variables característico.** Introducimos las **coordenadas características**
> $$\xi=z-ct,\qquad \eta=z+ct.$$
> Por la regla de la cadena, las derivadas respecto de $z$ y $t$ se reescriben en términos de $\xi,\eta$. Como $\partial\xi/\partial z=1$, $\partial\eta/\partial z=1$, $\partial\xi/\partial t=-c$, $\partial\eta/\partial t=+c$:
> $$\frac{\partial}{\partial z}=\frac{\partial}{\partial\xi}+\frac{\partial}{\partial\eta},\qquad \frac{\partial}{\partial t}=-c\,\frac{\partial}{\partial\xi}+c\,\frac{\partial}{\partial\eta}.$$
>
> **Paso 2 — Segundas derivadas.** Aplicando dos veces:
> $$\frac{\partial^2 u}{\partial z^2}=\left(\partial_\xi+\partial_\eta\right)^2 u=u_{\xi\xi}+2u_{\xi\eta}+u_{\eta\eta},$$
> $$\frac{\partial^2 u}{\partial t^2}=c^2\left(-\partial_\xi+\partial_\eta\right)^2 u=c^2\left(u_{\xi\xi}-2u_{\xi\eta}+u_{\eta\eta}\right).$$
>
> **Paso 3 — Sustituir en la ecuación.** La ecuación $\partial_z^2 u=\frac{1}{c^2}\partial_t^2 u$ se convierte en
> $$u_{\xi\xi}+2u_{\xi\eta}+u_{\eta\eta}=u_{\xi\xi}-2u_{\xi\eta}+u_{\eta\eta}.$$
> Cancelando $u_{\xi\xi}$ y $u_{\eta\eta}$ y reordenando queda $4u_{\xi\eta}=0$, es decir
> $$\frac{\partial^2 u}{\partial\xi\,\partial\eta}=0.$$
>
> **Paso 4 — Integrar la ecuación desacoplada.** Que $\partial_\xi(\partial_\eta u)=0$ significa que $\partial_\eta u$ no depende de $\xi$: $\partial_\eta u=G(\eta)$ para alguna función $G$. Integrando en $\eta$:
> $$u=\int G(\eta)\,d\eta+f(\xi)=g(\eta)+f(\xi),$$
> donde $g$ es una primitiva de $G$ y $f(\xi)$ es la "constante" de integración (que puede depender de $\xi$). Deshaciendo el cambio:
> $$u(z,t)=f(z-ct)+g(z+ct).\qquad\blacksquare$$
>
> **Interpretación física.** En $f(z-ct)$, el perfil es constante a lo largo de las líneas $z-ct=\text{cte}$, es decir $z=z_0+ct$: el punto donde el perfil vale un valor dado se desplaza con velocidad $+c$. El pulso conserva exactamente su forma porque su único argumento es $z-ct$. Análogamente, $g(z+ct)$ viaja a $-c$.

La siguiente figura ilustra un perfil $f(z-ct)$ que avanza a velocidad $c$ manteniendo intacta su forma:

![[onda_viajera.svg|460]]

*Figura 1. Un pulso $f(z-ct)$ en tres instantes sucesivos: la forma se traslada rígidamente hacia $+z$ a velocidad $c$, sin deformarse ni cambiar de amplitud.*

---

## Ondas monocromáticas como caso particular

Entre todas las soluciones $f(z-ct)$, las **sinusoidales** son las más útiles, porque cualquier pulso se descompone en ellas (análisis de Fourier). Tomamos

$$u(z,t)=A\cos(kz-\omega t),$$

que es de la forma $f(z-ct)$ siempre que el argumento sea proporcional a $z-ct$. En efecto,

$$kz-\omega t=k\left(z-\frac{\omega}{k}\,t\right),$$

de modo que el perfil viaja a velocidad $\omega/k$. Para que sea solución de la ecuación de ondas, esa velocidad debe ser $c$, lo que impone la **relación de dispersión**:

> [!regla] Relación de dispersión en el vacío
> $$\omega=c\,k.$$
> El campo de una onda monocromática queda descrito por:
> $$k=\frac{2\pi}{\lambda}\ \text{(número de onda)},\qquad \omega=2\pi f\ \text{(frecuencia angular)},$$
> y de $\omega=ck$ se deduce la relación entre longitud de onda y frecuencia:
> $$c=\lambda f.$$
> Que $\omega$ sea proporcional a $k$ (dispersión **lineal**) es lo que garantiza que *todas* las frecuencias viajen a la misma velocidad $c$, y por eso un pulso no se deforma en el vacío.

---

## Ejemplo

> [!ejemplo]
> Verifica explícitamente que la onda plana
> $$\vec E(z,t)=E_0\cos(kz-\omega t)\,\hat x$$
> satisface la ecuación de ondas, y determina la condición sobre $\omega$ y $k$.

> [!solucion]
> **Paso 1 — Calcular $\nabla^2\vec E$.** Como $\vec E$ solo tiene componente $x$ y depende únicamente de $z$, el laplaciano se reduce a la segunda derivada respecto de $z$:
> $$\nabla^2\vec E=\frac{\partial^2}{\partial z^2}\big[E_0\cos(kz-\omega t)\big]\,\hat x.$$
> Derivando dos veces respecto de $z$:
> $$\frac{\partial}{\partial z}\cos(kz-\omega t)=-k\sin(kz-\omega t),$$
> $$\frac{\partial^2}{\partial z^2}\cos(kz-\omega t)=-k^2\cos(kz-\omega t).$$
> Por tanto:
> $$\nabla^2\vec E=-k^2 E_0\cos(kz-\omega t)\,\hat x=-k^2\,\vec E.$$
>
> **Paso 2 — Calcular $\partial_t^2\vec E$.** Derivando dos veces respecto de $t$:
> $$\frac{\partial}{\partial t}\cos(kz-\omega t)=+\omega\sin(kz-\omega t),$$
> $$\frac{\partial^2}{\partial t^2}\cos(kz-\omega t)=-\omega^2\cos(kz-\omega t).$$
> Por tanto:
> $$\frac{\partial^2\vec E}{\partial t^2}=-\omega^2 E_0\cos(kz-\omega t)\,\hat x=-\omega^2\,\vec E.$$
>
> **Paso 3 — Imponer la ecuación de ondas.** Sustituyendo en $\nabla^2\vec E=\frac{1}{c^2}\partial_t^2\vec E$:
> $$-k^2\,\vec E=\frac{1}{c^2}\,(-\omega^2\,\vec E)\;\Longrightarrow\; k^2=\frac{\omega^2}{c^2}.$$
> Como $\omega,k,c>0$, tomamos la raíz positiva:
> $$\boxed{\;\omega=c\,k\;}$$
>
> **Conclusión.** La onda plana es solución de la ecuación de ondas **si y solo si** se cumple la relación de dispersión $\omega=ck$. La amplitud $E_0$ y la fase quedan libres: la ecuación de ondas no las fija. $\blacksquare$

---

## En qué consiste

La idea profunda de esta nota es que las **ondas electromagnéticas no son un postulado**: emergen de las [[Ecuaciones de Maxwell]] como una consecuencia matemática inevitable. Maxwell unió la electricidad y el magnetismo en cuatro ecuaciones; al manipularlas para despejar un solo campo, el resultado fue, por sorpresa, la ecuación de una onda. Y la velocidad de esa onda no era un parámetro ajustable: salía de combinar dos constantes medidas en el laboratorio con experimentos de electrostática y magnetostática, $\mu_0$ y $\varepsilon_0$. El número resultante, $\approx 3{,}00\times10^8$ m/s, coincidía con la velocidad de la luz. Esa coincidencia fue la prueba de que **la luz es electromagnetismo**.

El mecanismo físico es un baile mutuo entre los campos. Un campo eléctrico que cambia en el tiempo genera, por Ampère–Maxwell, un campo magnético; ese campo magnético variable genera, por Faraday, un campo eléctrico; y así sucesivamente. Esta retroalimentación se sostiene a sí misma y se propaga por el espacio sin necesidad de cargas ni corrientes: una perturbación que, una vez lanzada, viaja indefinidamente a velocidad $c$.

La solución de d'Alembert revela la estructura cinemática: cualquier forma de pulso $f(z-ct)$ se traslada rígidamente. La ecuación no selecciona *qué* forma, solo *cómo* se mueve. Las ondas monocromáticas $\cos(kz-\omega t)$ son el ladrillo elemental con el que, vía Fourier, se construye cualquier pulso, y la relación lineal $\omega=ck$ asegura que todas viajen al unísono. Esto conecta directamente con las [[Ondas Planas]], que añaden la información sobre la **dirección** de $\vec E$, $\vec B$ y la propagación, y con las [[Ondas en Medios]], donde $\mu_0,\varepsilon_0$ se reemplazan por $\mu,\varepsilon$ y la velocidad baja a $c/n$.

> [!warning] Dos sutilezas conceptuales
> - **La ecuación de ondas es una consecuencia, no un axioma.** No se postula que existan ondas: se deducen de Maxwell. Si las ecuaciones de Maxwell son correctas, las ondas electromagnéticas *deben* existir.
> - **La velocidad $c$ no menciona ningún observador.** En la deducción, $c=1/\sqrt{\mu_0\varepsilon_0}$ surge de constantes del vacío, sin referencia a un sistema de referencia respecto del cual se mida. Esta ausencia —¿velocidad $c$ respecto de qué?— es precisamente la semilla de la que brotaría la relatividad especial: la luz tiene la misma velocidad $c$ para todos los observadores.

---

## Resumen

> [!resumen]
> | Concepto | Expresión | Comentario |
> |---|---|---|
> | Ecuación de ondas (campo $\vec E$) | $\nabla^2\vec E=\dfrac{1}{c^2}\dfrac{\partial^2\vec E}{\partial t^2}$ | Idéntica para $\vec B$ |
> | Operador de d'Alembert | $\Box=\nabla^2-\dfrac{1}{c^2}\partial_t^2$ | Forma compacta $\Box\vec E=\vec 0$ |
> | Velocidad de propagación | $c=\dfrac{1}{\sqrt{\mu_0\varepsilon_0}}\approx 3{,}00\times10^8\ \mathrm{m/s}$ | Fijada por las constantes del vacío |
> | Solución general 1D | $u=f(z-ct)+g(z+ct)$ | Pulsos a $\pm c$ sin deformarse |
> | Onda monocromática | $u=A\cos(kz-\omega t)$ | Caso particular sinusoidal |
> | Relación de dispersión | $\omega=ck$ | Equivale a $c=\lambda f$ |

> [!corolario]
> - En el vacío, $\vec E$ y $\vec B$ obedecen **la misma** ecuación de ondas con **la misma** velocidad $c$: viajan juntos.
> - La onda plana $E_0\cos(kz-\omega t)\,\hat x$ es solución $\iff$ $\omega=ck$; la amplitud y la fase quedan libres.
> - La existencia de las ondas y el valor de $c$ se siguen exclusivamente de las [[Ecuaciones de Maxwell]]; ningún ingrediente adicional es necesario.

> [!referencia]
> - Griffiths, D. J. *Introduction to Electrodynamics*, 4ª ed., cap. 9 (The wave equation; electromagnetic waves in vacuum).
> - Jackson, J. D. *Classical Electrodynamics*, cap. 7.
> - Landau & Lifshitz, *The Classical Theory of Fields* (vol. 2), cap. 6.
