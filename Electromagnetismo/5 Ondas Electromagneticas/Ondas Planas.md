---
title: Ondas Planas
order: 2
tags:
  - electromagnetismo
  - teoria
  - ondas
draft: false
aliases:
  - Ondas planas
  - Ondas planas monocromáticas
---

# Ondas Planas $\vec B=\dfrac{1}{c}\,\hat k\times\vec E,\quad E=cB$

---

> [!definicion] Onda plana monocromática
> Una **onda plana monocromática** es una solución de las [[Ecuaciones de Maxwell]] en el vacío que se propaga en la dirección de un vector de onda $\vec k$ con una única frecuencia angular $\omega$. En notación compleja se escribe
> $$
> \vec E(\vec r,t)=\vec E_0\,e^{i(\vec k\cdot\vec r-\omega t)},\qquad
> \vec B(\vec r,t)=\vec B_0\,e^{i(\vec k\cdot\vec r-\omega t)},
> $$
> donde solo la **parte real** tiene significado físico. Las superficies de **fase constante** $\vec k\cdot\vec r-\omega t=\text{cte}$ son planos perpendiculares a $\vec k$ (de ahí el nombre), que avanzan con la **velocidad de fase** $v=\omega/k=c$, con $c=1/\sqrt{\mu_0\varepsilon_0}$.
>
> Sus propiedades fundamentales son:
> - **Transversalidad:** $\vec E\perp\vec k$ y $\vec B\perp\vec k$.
> - **Relación E–B:** $\vec B=\dfrac{1}{c}\,\hat k\times\vec E$, de donde $\vec E\perp\vec B$, ambos en fase y con amplitudes ligadas por $E=cB$.

---

> [!info] Ubicación
> Esta nota pertenece a la sección [[5 Ondas Electromagneticas/index | Ondas Electromagnéticas]]. Sus notas hermanas son [[Ecuacion de Ondas]], [[5 Ondas Electromagneticas/Polarizacion | Polarización]] y [[Ondas en Medios]]. Se apoya en [[Ecuaciones de Maxwell]] (de donde salen todas las propiedades) y en [[Energia y Momento]] (para densidad, flujo e intensidad). Seguimos a **Griffiths, _Introduction to Electrodynamics_, cap. 9**.

---

## En qué consiste

La idea de partida es buscar soluciones de las ecuaciones de Maxwell en el vacío (sin cargas ni corrientes, $\rho=0$, $\vec J=\vec 0$) que tengan la forma más sencilla posible: una vibración sinusoidal de frecuencia única que se propaga en línea recta. Esa es la **onda plana monocromática**.

El nombre tiene dos partes:

- **Plana** porque, en cualquier instante, los puntos que comparten la misma fase forman planos infinitos perpendiculares a $\vec k$. El campo no depende de la posición dentro de ese plano: vale lo mismo en todo él.
- **Monocromática** porque hay una sola frecuencia $\omega$ (un solo «color»).

Toda la información geométrica está en cuatro vectores: $\vec k$ (dirección de avance), $\vec E_0$, $\vec B_0$ (amplitudes) y la terna ortogonal $\{\hat E,\hat B,\hat k\}$. Lo notable es que Maxwell **no permite elegirlos libremente**: la ley de Gauss obliga a que $\vec E$ y $\vec B$ sean transversales, y la ley de Faraday fija por completo $\vec B$ una vez dado $\vec E$. Esto lo demostramos abajo.

Conviene tener presente el **truco de la notación compleja**. Maxwell es lineal, así que si $\vec E_0 e^{i(\vec k\cdot\vec r-\omega t)}$ la satisface, también lo hace su parte real $\vec E_0\cos(\vec k\cdot\vec r-\omega t)$ (la física real). Trabajar con exponenciales convierte derivadas en multiplicaciones:
$$
\partial_t \;\to\; -i\omega,\qquad \nabla \;\to\; i\vec k .
$$
Esta es la herramienta que usaremos una y otra vez.

---

## Transversalidad (de la ley de Gauss)

> [!teorema] Los campos son transversales
> Para una onda plana en el vacío, $\vec k\cdot\vec E_0=0$ y $\vec k\cdot\vec B_0=0$; es decir, $\vec E\perp\vec k$ y $\vec B\perp\vec k$.

> [!demostracion]
> **Paso 1 — Ley de Gauss en el vacío.** Sin cargas, $\nabla\cdot\vec E=0$.
>
> **Paso 2 — Divergencia de la onda plana.** Calculamos la divergencia de $\vec E=\vec E_0\,e^{i(\vec k\cdot\vec r-\omega t)}$. Como $\vec E_0$ es un vector constante, solo deriva la exponencial. Para cada componente,
> $$
> \partial_j\,e^{i(\vec k\cdot\vec r-\omega t)}=\partial_j\,e^{i(k_x x+k_y y+k_z z-\omega t)}=i\,k_j\,e^{i(\vec k\cdot\vec r-\omega t)} .
> $$
> Sumando $\partial_j E_{0,j}$ sobre $j$,
> $$
> \nabla\cdot\vec E=\nabla\cdot\!\big(\vec E_0\,e^{i(\vec k\cdot\vec r-\omega t)}\big)=i\,\vec k\cdot\vec E_0\,e^{i(\vec k\cdot\vec r-\omega t)}=i\,\vec k\cdot\vec E .
> $$
>
> **Paso 3 — Imponer Gauss.** Igualando a cero, y como la exponencial nunca se anula,
> $$
> i\,\vec k\cdot\vec E_0\,e^{i(\vec k\cdot\vec r-\omega t)}=0 \;\Longrightarrow\; \vec k\cdot\vec E_0=0 .
> $$
> Por tanto $\vec E\perp\vec k$.
>
> **Paso 4 — El campo magnético.** En el vacío también $\nabla\cdot\vec B=0$. Repitiendo idénticamente los pasos con $\vec B$,
> $$
> \nabla\cdot\vec B=i\,\vec k\cdot\vec B_0\,e^{i(\vec k\cdot\vec r-\omega t)}=0 \;\Longrightarrow\; \vec k\cdot\vec B_0=0,
> $$
> luego $\vec B\perp\vec k$. Las ondas electromagnéticas son **transversales**: no hay componente de $\vec E$ ni de $\vec B$ a lo largo de la propagación. $\blacksquare$

---

## Relación entre $\vec E$ y $\vec B$ (de la ley de Faraday)

> [!teorema] Ligadura E–B
> En una onda plana en el vacío,
> $$
> \vec B=\frac{1}{c}\,\hat k\times\vec E,\qquad \omega=ck .
> $$
> En consecuencia: $\vec E\perp\vec B$, ambos campos están **en fase** y sus amplitudes cumplen $E=cB$.

> [!demostracion]
> **Paso 1 — Ley de Faraday.** $\displaystyle \nabla\times\vec E=-\,\partial_t\vec B$.
>
> **Paso 2 — Rotacional de la onda plana.** Con $\nabla\to i\vec k$ aplicado al rotacional,
> $$
> \nabla\times\vec E=\nabla\times\!\big(\vec E_0\,e^{i(\vec k\cdot\vec r-\omega t)}\big)=i\,\vec k\times\vec E_0\,e^{i(\vec k\cdot\vec r-\omega t)}=i\,\vec k\times\vec E .
> $$
> (En componentes, $[\nabla\times\vec E]_i=\varepsilon_{ijk}\,\partial_j E_k=\varepsilon_{ijk}\,(i k_j) E_k=i\,[\vec k\times\vec E]_i$.)
>
> **Paso 3 — Derivada temporal de $\vec B$.** Con $\partial_t\to -i\omega$,
> $$
> -\,\partial_t\vec B=-\,\partial_t\!\big(\vec B_0\,e^{i(\vec k\cdot\vec r-\omega t)}\big)=-(-i\omega)\,\vec B=i\omega\,\vec B .
> $$
>
> **Paso 4 — Igualar y despejar.** Faraday exige $i\,\vec k\times\vec E=i\omega\,\vec B$, es decir,
> $$
> \vec k\times\vec E_0=\omega\,\vec B_0 \;\Longrightarrow\; \vec B_0=\frac{\vec k\times\vec E_0}{\omega} .
> $$
>
> **Paso 5 — Forma con $\hat k$ y velocidad de fase.** Escribimos $\vec k=k\,\hat k$ y usamos $\omega=ck$ (que se obtiene de la [[Ecuacion de Ondas]], $k^2=\omega^2/c^2$). Entonces
> $$
> \vec B=\frac{k\,\hat k\times\vec E}{\omega}=\frac{k}{ck}\,\hat k\times\vec E=\frac{1}{c}\,\hat k\times\vec E .
> $$
>
> **Paso 6 — Consecuencias geométricas y de magnitud.** El producto $\hat k\times\vec E$ es perpendicular a $\vec E$ y a $\hat k$, así que $\vec B\perp\vec E$ y $\vec B\perp\hat k$: la terna $\{\vec E,\vec B,\hat k\}$ es un **triedro ortogonal a derechas**. Tomando módulos, y como $\vec E\perp\hat k$ implica $|\hat k\times\vec E|=E$,
> $$
> B=\frac{1}{c}\,|\hat k\times\vec E|=\frac{E}{c}\;\Longrightarrow\; \boxed{E=cB} .
> $$
> Además, $\vec E$ y $\vec B$ comparten exactamente la misma exponencial $e^{i(\vec k\cdot\vec r-\omega t)}$ sin desfase relativo: oscilan **en fase**. $\blacksquare$

La figura muestra el triedro y la oscilación sincronizada de ambos campos:

![[onda_plana.svg|480]]

*$\vec E$ (oscilando en un plano) y $\vec B$ (en el plano perpendicular) avanzan en fase a lo largo de $\hat k$; los tres vectores forman un triedro ortogonal a derechas y las amplitudes cumplen $E=cB$.*

---

## Energía e intensidad

> [!proposicion] Densidad de energía, flujo e intensidad
> Para una onda plana en el vacío,
> $$
> u=\varepsilon_0 E^2,\qquad \vec S=c\,\varepsilon_0 E^2\,\hat k,\qquad I=\langle S\rangle=\tfrac12\,c\,\varepsilon_0 E_0^2 .
> $$

> [!demostracion]
> **Paso 1 — Densidad de energía general.** De [[Energia y Momento]], la densidad de energía del campo es
> $$
> u=\frac{1}{2}\Big(\varepsilon_0 E^2+\frac{1}{\mu_0}B^2\Big).
> $$
>
> **Paso 2 — Las dos contribuciones son iguales.** Usando $B=E/c$ y $c^2=1/(\mu_0\varepsilon_0)$,
> $$
> \frac{1}{\mu_0}B^2=\frac{1}{\mu_0}\frac{E^2}{c^2}=\frac{1}{\mu_0}\,E^2\,\mu_0\varepsilon_0=\varepsilon_0 E^2 .
> $$
> La energía magnética coincide exactamente con la eléctrica: en una onda plana cada campo aporta la mitad.
>
> **Paso 3 — Densidad total.** Sustituyendo,
> $$
> u=\frac{1}{2}\big(\varepsilon_0 E^2+\varepsilon_0 E^2\big)=\varepsilon_0 E^2 .
> $$
>
> **Paso 4 — Vector de Poynting.** El flujo de energía es $\vec S=\dfrac{1}{\mu_0}\,\vec E\times\vec B$. Con $\vec B=\dfrac{1}{c}\,\hat k\times\vec E$ y $\vec E\perp\hat k$,
> $$
> \vec E\times\vec B=\frac{1}{c}\,\vec E\times(\hat k\times\vec E)
> =\frac{1}{c}\Big[(\vec E\cdot\vec E)\,\hat k-(\vec E\cdot\hat k)\,\vec E\Big]
> =\frac{E^2}{c}\,\hat k,
> $$
> donde el segundo término se anula porque $\vec E\cdot\hat k=0$. Entonces
> $$
> \vec S=\frac{1}{\mu_0}\frac{E^2}{c}\,\hat k=\frac{c^2\varepsilon_0}{c}\,E^2\,\hat k=c\,\varepsilon_0 E^2\,\hat k=c\,u\,\hat k .
> $$
> La energía viaja en la dirección $\hat k$ a velocidad $c$, como cabe esperar.
>
> **Paso 5 — Intensidad (promedio temporal).** La parte física es $E=E_0\cos(\vec k\cdot\vec r-\omega t)$, con $\langle\cos^2\rangle=\tfrac12$. La **intensidad** es el promedio temporal del módulo de $\vec S$:
> $$
> I=\langle S\rangle=c\,\varepsilon_0\,E_0^2\,\langle\cos^2(\cdots)\rangle=\frac{1}{2}\,c\,\varepsilon_0\,E_0^2 . \qquad\blacksquare
> $$

> [!info] Impedancia del vacío
> El cociente entre los módulos de $\vec E$ y $\vec H=\vec B/\mu_0$ es una constante con dimensiones de resistencia, la **impedancia del vacío**:
> $$
> Z_0=\frac{E}{H}=\sqrt{\frac{\mu_0}{\varepsilon_0}}=\mu_0 c\approx 377\ \Omega .
> $$
> Permite reescribir la intensidad como $I=\tfrac12\,E_0^2/Z_0$ y aparece de forma natural en óptica e ingeniería de antenas.

### Presión de radiación

Como la onda transporta momento (densidad $g=S/c^2$), al incidir sobre una superficie ejerce una **presión de radiación**. Para una superficie perfectamente **absorbente**, en incidencia normal,
$$
P=\frac{\langle S\rangle}{c}=\frac{I}{c}.
$$
Si la superficie es perfectamente **reflectora**, el momento se invierte y la presión se duplica, $P=2I/c$. Es un efecto diminuto en condiciones cotidianas, pero domina en velas solares y en el equilibrio de las estrellas.

---

## Ejemplo

> [!ejemplo] Onda polarizada según $\hat x$ que se propaga en $+z$
> Dada la onda plana en el vacío
> $$
> \vec E(z,t)=E_0\cos(kz-\omega t)\,\hat x,
> $$
> determina $\vec B$, comprueba que $\vec E\perp\vec B\perp\vec k$ y calcula la intensidad para $E_0=100\ \text{V/m}$.

> [!solucion]
> **Paso 1 — Identificar la geometría.** La onda avanza en $+z$, luego $\hat k=\hat z$. El campo eléctrico apunta según $\hat x$, así que $\vec E\perp\hat k$ se cumple ($\hat x\cdot\hat z=0$), consistente con la transversalidad.
>
> **Paso 2 — Calcular $\vec B$.** Aplicamos $\vec B=\dfrac{1}{c}\,\hat k\times\vec E$. Con $\hat k\times\hat x=\hat z\times\hat x=\hat y$,
> $$
> \vec B(z,t)=\frac{1}{c}\,\hat z\times\big[E_0\cos(kz-\omega t)\,\hat x\big]=\frac{E_0}{c}\cos(kz-\omega t)\,\hat y .
> $$
> El campo magnético apunta según $\hat y$, oscila **en fase** con $\vec E$ (mismo coseno) y tiene amplitud $B_0=E_0/c$.
>
> **Paso 3 — Comprobar la ortogonalidad.** $\vec E\parallel\hat x$, $\vec B\parallel\hat y$, $\vec k\parallel\hat z$. Como $\hat x\perp\hat y\perp\hat z$ y $\hat x\times\hat y=\hat z$, los tres son mutuamente perpendiculares y forman un triedro a derechas con $\hat E\times\hat B=\hat k$. Correcto.
>
> **Paso 4 — Magnitud de $\vec B$.** Con $c\approx 3{,}00\times10^{8}\ \text{m/s}$ y $E_0=100\ \text{V/m}$,
> $$
> B_0=\frac{E_0}{c}=\frac{100}{3{,}00\times10^{8}}\approx 3{,}33\times10^{-7}\ \text{T}.
> $$
> El campo magnético es minúsculo en unidades del SI: no porque «sea débil», sino por el factor $c$ que relaciona ambas unidades.
>
> **Paso 5 — Intensidad.** Con $\varepsilon_0\approx 8{,}85\times10^{-12}\ \text{F/m}$,
> $$
> I=\frac{1}{2}\,c\,\varepsilon_0\,E_0^2=\frac{1}{2}\,(3{,}00\times10^{8})(8{,}85\times10^{-12})(100)^2\ \text{W/m}^2 .
> $$
> Operando: $\tfrac12\,c\,\varepsilon_0=\tfrac12(3{,}00\times10^8)(8{,}85\times10^{-12})\approx 1{,}33\times10^{-3}$, y multiplicando por $E_0^2=10^{4}$,
> $$
> I\approx 13{,}3\ \text{W/m}^2 .
> $$
> Como referencia, la radiación solar en la superficie terrestre es del orden de $1000\ \text{W/m}^2$, que correspondería a $E_0\approx 870\ \text{V/m}$. $\blacksquare$

---

> [!warning] Idealización y notación compleja
> - La onda plana **monocromática** es una idealización: tiene extensión espacial y temporal **infinitas** y energía total infinita. No existe una onda plana pura en la naturaleza.
> - Su utilidad es que forman una **base completa**: por análisis de Fourier, cualquier onda real (un pulso láser, una señal de antena) es una **superposición** de ondas planas de distintos $\vec k$ y $\omega$. Estudiar la onda plana es estudiar el «ladrillo» de todas las demás.
> - La **notación compleja** $e^{i(\vec k\cdot\vec r-\omega t)}$ es solo un atajo de cálculo. Solo la **parte real** es física. Es válida mientras las operaciones sean lineales; al calcular cantidades cuadráticas (como $u$, $S$ o $I$) **hay que tomar primero la parte real** o usar la fórmula del promedio $\langle\,\cdot\,\rangle$, no elevar al cuadrado el campo complejo sin más.

---

## Resumen

> [!resumen] Onda plana monocromática en el vacío
> Solución $\vec E=\vec E_0\,e^{i(\vec k\cdot\vec r-\omega t)}$ con una sola frecuencia, planos de fase $\perp\vec k$ avanzando a $v=c=1/\sqrt{\mu_0\varepsilon_0}$.
>
> | Propiedad \| Resultado \| Origen |
> | :-- \| :-- \| :-- |
> | Transversalidad \| $\vec k\cdot\vec E_0=0,\ \vec k\cdot\vec B_0=0$ \| Gauss ($\nabla\cdot\vec E=0$) |
> | Relación E–B \| $\vec B=\dfrac{1}{c}\,\hat k\times\vec E$ \| Faraday |
> | Amplitudes \| $E=cB$ \| módulo de la anterior |
> | Frecuencia \| $\omega=ck$ \| ecuación de ondas |
> | Geometría \| triedro $\{\vec E,\vec B,\hat k\}$ ortogonal, en fase \| — |
> | Densidad de energía \| $u=\varepsilon_0 E^2$ \| $u_E=u_B$ |
> | Flujo \| $\vec S=c\,\varepsilon_0 E^2\,\hat k=c\,u\,\hat k$ \| Poynting |
> | Intensidad \| $I=\tfrac12\,c\,\varepsilon_0 E_0^2=\tfrac12\,E_0^2/Z_0$ \| promedio temporal |
> | Impedancia \| $Z_0=\sqrt{\mu_0/\varepsilon_0}\approx 377\ \Omega$ \| $E/H$ |
> | Presión (absorción) \| $P=I/c$ \| momento del campo |

> [!corolario] Ideas que hay que llevarse
> Maxwell fija **toda** la estructura de la onda: basta dar $\vec E_0$ y $\vec k$ y queda determinado $\vec B$, las amplitudes y la energía. La luz es un campo eléctrico y uno magnético perpendiculares, en fase, transversales a la propagación, con $E=cB$ y energía repartida por igual entre ambos. La dirección de polarización de $\vec E$ (aquí libre dentro del plano $\perp\vec k$) es el tema de [[5 Ondas Electromagneticas/Polarizacion | Polarización]].

> [!referencia] Fuentes y notas relacionadas
> - **Griffiths, _Introduction to Electrodynamics_, cap. 9** — ondas electromagnéticas en el vacío.
> - Deducción de $\omega=ck$ y la ecuación de propagación: [[Ecuacion de Ondas]].
> - Densidad de energía y vector de Poynting: [[Energia y Momento]].
> - Leyes de partida: [[Ecuaciones de Maxwell]].
> - Estados de polarización y luz no polarizada: [[5 Ondas Electromagneticas/Polarizacion | Polarización]].
> - Propagación en dieléctricos y conductores: [[Ondas en Medios]].
