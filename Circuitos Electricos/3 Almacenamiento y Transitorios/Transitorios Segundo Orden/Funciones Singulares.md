---
title: Funciones Singulares
tags:
  - circuitos-electricos
  - teoria
  - transitorios
  - segundo-orden
  - funciones-singulares
draft: false
aliases:
  - funciones singulares
  - singularity functions
  - escalón unitario
  - impulso
  - rampa
  - step impulse ramp
---

# Funciones Singulares

> [!definicion]
> Las **funciones singulares** modelan conmutaciones (cerrar o abrir un interruptor) y sirven de
> **excitaciones de prueba** para caracterizar un circuito. Las tres básicas son:
> - **Escalón unitario** $u(t)$: vale $0$ para $t<0$ y $1$ para $t\ge0$.
> - **Impulso** o delta de Dirac $\delta(t)$: nulo salvo en $t=0$, con **área** $1$.
> - **Rampa** $r(t)=t\,u(t)$: crece linealmente desde $t=0$.
>
> Están ligadas por derivación e integración:
> $$\delta(t)=\frac{du}{dt},\qquad u(t)=\frac{dr}{dt}.$$

> [!info]
> Herramientas de los [[Transitorios Segundo Orden/index| transitorios]]
> ([[3 Almacenamiento y Transitorios/index| capítulo 3]]): el escalón modela **cerrar un
> interruptor** en $t=0$, y las tres son la entrada natural de la
> [[Solucion de Transitorios con Laplace| solución por Laplace]]. Aparecen al excitar un
> [[Circuito RLC Serie]] o al plantear la [[Respuesta Completa Primer Orden]]. Fraile Mora, cap. 4,
> §4.9.

---

## Ejemplo

> [!ejemplo]
> **Las tres funciones y su relación.**
>
> ![[funciones_singulares.svg|640]]
>
> *Escalón $u(t)$, impulso $\delta(t)$ (flecha de área $1$) y rampa $r(t)=t\,u(t)$. Derivando se sube
> en la cadena rampa→escalón→impulso; integrando se baja.*
>
> Una fuente que se **conecta en $t=0$** con valor $V_s$ se escribe simplemente $V_s\,u(t)$: vale $0$
> antes de la conmutación y $V_s$ después. Así, una entrada como $v(t)=10\,u(t)\ \text{V}$ representa una
> batería de $10\ \text{V}$ que se enchufa en el instante $t=0$. Si en cambio se inyecta una carga
> instantánea, se modela con $\delta(t)$; y si la tensión sube a ritmo constante, con $r(t)$.

---

## En qué consiste

> [!teoria] Las tres funciones
> **Escalón $u(t)$.** Es el salto de $0$ a $1$ en $t=0$. Es el modelo matemático de una **conmutación**:
> antes de $t=0$ el circuito está en un estado y a partir de $t=0$ en otro. Multiplicar una constante
> $V_s$ por $u(t)$ "enciende" esa fuente en el origen.
>
> **Impulso $\delta(t)$.** Es la **derivada del escalón**: como $u$ pasa de $0$ a $1$ de golpe, su tasa
> de cambio es infinita en $t=0$ y nula en el resto. Idealiza una **inyección instantánea** (un pulso
> muy alto y muy estrecho de **área unidad**). Su **respuesta** —la salida del circuito ante $\delta(t)$—
> caracteriza por completo al circuito: conocida la respuesta al impulso, se obtiene la respuesta a
> cualquier entrada por convolución.
>
> **Rampa $r(t)$.** Es la **integral del escalón**: como $u$ vale $1$ a partir de $t=0$, acumularla da
> una recta $r(t)=t\,u(t)$ que crece linealmente. Modela una excitación que aumenta a ritmo constante.
>
> La **cadena** de derivación/integración resume todo:
> $$r(t)\;\xrightarrow{\;d/dt\;}\;u(t)\;\xrightarrow{\;d/dt\;}\;\delta(t),$$
> y en sentido inverso, integrando, se desciende de $\delta$ a $u$ y de $u$ a $r$.

> [!proposicion] Propiedad de cribado del impulso
> El impulso **muestrea** una función en el instante donde actúa:
> $$\int_{-\infty}^{\infty} f(t)\,\delta(t-a)\,dt=f(a),$$
> y en particular su área es unitaria:
> $$\int_{-\infty}^{\infty}\delta(t)\,dt=1.$$
> Esta propiedad es la base del análisis por respuesta al impulso y de la convolución: $\delta(t-a)$
> "extrae" el valor $f(a)$ de cualquier $f$ integrable.

> [!warning]
> El impulso $\delta(t)$ es una **idealización**: no es una función ordinaria sino una **distribución**.
> Físicamente representa un pulso de **duración despreciable y área finita** (por ejemplo, una corriente
> enorme durante un tiempo brevísimo que transfiere una carga finita). Además, **no confundir el escalón
> unitario con una constante**: $u(t)$ vale $0$ **antes** de $t=0$ y $1$ después; una constante valdría
> lo mismo para todo $t$.

## Resumen

> [!resumen]
> | Función | Definición | Derivada | Integral |
> |:---|:---|:---|:---|
> | Rampa $r(t)$ | $t\,u(t)$ | $u(t)$ | $\tfrac{1}{2}t^2\,u(t)$ |
> | Escalón $u(t)$ | $0$ si $t<0$, $1$ si $t\ge0$ | $\delta(t)$ | $r(t)=t\,u(t)$ |
> | Impulso $\delta(t)$ | área $1$ en $t=0$ | $\delta'(t)$ | $u(t)$ |

> [!corolario]
> Las tres funciones singulares forman una sola **cadena** $r\to u\to\delta$ unida por derivación (e
> integración en sentido contrario). El escalón modela la conmutación, el impulso caracteriza el
> circuito por su respuesta, y la rampa representa el crecimiento lineal. Son la base para excitar los
> [[Transitorios Segundo Orden/index| transitorios]] y para la
> [[Solucion de Transitorios con Laplace| solución por Laplace]].

> [!referencia]
> Fraile Mora, cap. 4, §4.9. Aplicación: [[Circuito RLC Serie]],
> [[Respuesta Completa Primer Orden]]. Transformada: [[Solucion de Transitorios con Laplace]],
> [[Laplace en Circuitos/index]].
