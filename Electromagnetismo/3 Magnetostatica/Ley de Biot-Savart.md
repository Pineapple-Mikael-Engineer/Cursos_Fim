---
title: Ley de Biot-Savart
order: 2
tags:
  - electromagnetismo
  - teoria
  - magnetostatica
draft: false
aliases:
  - Ley de Biot-Savart
  - Campo de una corriente
---

# Ley de Biot-Savart $\vec B=\dfrac{\mu_0}{4\pi}\displaystyle\int\dfrac{\vec J\times\hat{\mathscr r}}{\mathscr r^2}\,d^3r'$

> [!definicion] Ley de Biot–Savart
> El campo magnético $\vec B(\vec r)$ producido por una distribución estacionaria de corriente se obtiene sumando (integrando) la contribución de cada elemento de corriente fuente. En sus tres formas equivalentes:
>
> - **Filiforme** (corriente $I$ por un hilo):
> $$\vec B(\vec r)=\frac{\mu_0}{4\pi}\int\frac{I\,d\vec l\,'\times\hat{\mathscr r}}{\mathscr r^{2}}$$
> - **Superficial** (densidad $\vec K$):
> $$\vec B(\vec r)=\frac{\mu_0}{4\pi}\int\frac{\vec K(\vec r\,')\times\hat{\mathscr r}}{\mathscr r^{2}}\,da'$$
> - **Volumétrica** (densidad $\vec J$):
> $$\vec B(\vec r)=\frac{\mu_0}{4\pi}\int\frac{\vec J(\vec r\,')\times\hat{\mathscr r}}{\mathscr r^{2}}\,d^3r'$$
>
> Aquí $\vec r$ es el **punto de campo** (donde medimos $\vec B$), $\vec r\,'$ el **punto fuente** (donde está la corriente), y el vector separación fuente→campo es
> $$\hat{\mathscr r}=\frac{\vec r-\vec r\,'}{|\vec r-\vec r\,'|},\qquad \mathscr r=|\vec r-\vec r\,'|.$$
> La constante $\mu_0=4\pi\times10^{-7}\ \mathrm{T\cdot m/A}$ es la **permeabilidad del vacío**. El producto vectorial $\times$ es el rasgo distintivo: el campo de cada elemento es **perpendicular** a la corriente y a la línea fuente→campo.

---

> [!info] Ubicación y contexto
> Esta nota pertenece a la sección [[3 Magnetostatica/index | Magnetostática]]. Sus notas hermanas son [[Fuerza de Lorentz]], [[Ley de Ampere]] y [[Potencial Vector]]. La referencia base es **Griffiths, *Introduction to Electrodynamics*, cap. 5**.
>
> La Ley de Biot–Savart es a la magnetostática lo que la [[Ley de Coulomb]] es a la electrostática: una receta integral para hallar el campo directamente a partir de sus fuentes. Cuando la simetría lo permite, la [[Ley de Ampere]] suele ser más cómoda; pero Biot–Savart funciona **siempre**.

---

> [!teoria] El paralelismo con Coulomb
> Conviene escribir ambas leyes lado a lado para ver qué comparten y qué las separa.
>
> | Aspecto | Electrostática (Coulomb) | Magnetostática (Biot–Savart) |
> |---|---|---|
> | Fuente | carga $\rho$ | corriente $\vec J$ |
> | Ley integral | $\vec E=\dfrac{1}{4\pi\varepsilon_0}\displaystyle\int\dfrac{\rho\,\hat{\mathscr r}}{\mathscr r^{2}}\,d^3r'$ | $\vec B=\dfrac{\mu_0}{4\pi}\displaystyle\int\dfrac{\vec J\times\hat{\mathscr r}}{\mathscr r^{2}}\,d^3r'$ |
> | Dependencia con la distancia | $1/\mathscr r^{2}$ | $1/\mathscr r^{2}$ |
> | Dirección de la contribución | **radial** ($\parallel\hat{\mathscr r}$) | **transversal** ($\perp$ a $\vec J$ y a $\hat{\mathscr r}$) |
> | Constante | $1/4\pi\varepsilon_0$ | $\mu_0/4\pi$ |
>
> Ambas decaen como $1/\mathscr r^{2}$ y son lineales en la fuente. La diferencia esencial es el **producto vectorial**: mientras $\vec E$ apunta a lo largo de $\hat{\mathscr r}$, $\vec B$ apunta perpendicular a $\hat{\mathscr r}$, lo que genera líneas de campo cerradas que rodean a la corriente (no líneas que emanan de un punto).

---

> [!info] El elemento de campo $d\vec B$
> La estructura geométrica de cada contribución se ve mejor en un diagrama: el elemento de corriente $I\,d\vec l\,'$ apunta en el sentido del flujo, el vector $\hat{\mathscr r}$ va de la fuente al punto de campo, y $d\vec B$ sale **fuera del plano** que ambos forman.
>
> ![[biot_savart.svg|440]]
>
> *Figura 1. Un elemento de corriente $I\,d\vec l\,'$ sobre el hilo y el vector separación fuente→campo $\hat{\mathscr r}$ generan una contribución $d\vec B=\frac{\mu_0}{4\pi}\frac{I\,d\vec l\,'\times\hat{\mathscr r}}{\mathscr r^{2}}$, perpendicular a ambos (regla de la mano derecha).*

---

## Ejemplo

> [!ejemplo] Hilo recto infinito
> Un hilo recto infinito sobre el eje $x$ transporta una corriente estacionaria $I$. Halla el campo magnético a una distancia perpendicular $s$ del hilo, integrando directamente la Ley de Biot–Savart.

> [!solucion] Integración directa para el hilo
> **Paso 1 — Geometría y parametrización.** Colocamos el hilo a lo largo del eje $x$, con la corriente en sentido $+x$. El punto de campo $P$ está a distancia perpendicular $s$. Un elemento genérico de corriente está en la posición $x$ a lo largo del hilo:
> $$I\,d\vec l\,'=I\,dx\,\hat x.$$
> El vector que va del elemento fuente al punto de campo tiene módulo
> $$\mathscr r=\sqrt{x^{2}+s^{2}},$$
> y forma un ángulo $\theta$ con el hilo.
>
> **Paso 2 — El producto vectorial.** Sea $\theta$ el ángulo entre $d\vec l\,'$ y $\hat{\mathscr r}$. Entonces
> $$|d\vec l\,'\times\hat{\mathscr r}|=dx\,\sin\theta.$$
> La dirección de $d\vec l\,'\times\hat{\mathscr r}$ es la misma para **todos** los elementos: sale del plano (sentido azimutal $\hat\phi$ alrededor del hilo). Por eso todas las contribuciones se suman como escalares, sin cancelaciones direccionales:
> $$dB=\frac{\mu_0 I}{4\pi}\frac{\sin\theta\,dx}{\mathscr r^{2}}=\frac{\mu_0 I}{4\pi}\frac{\sin\theta\,dx}{x^{2}+s^{2}}.$$
>
> **Paso 3 — Cambio a una sola variable.** Conviene usar el ángulo $\theta$ medido desde $+\hat x$ hacia $\hat{\mathscr r}$. De la geometría:
> $$x=-\frac{s}{\tan\theta}=-s\cot\theta\ \Rightarrow\ dx=\frac{s}{\sin^{2}\theta}\,d\theta,$$
> $$s=\mathscr r\,\sin\theta\ \Rightarrow\ \frac{1}{\mathscr r^{2}}=\frac{\sin^{2}\theta}{s^{2}}.$$
> Sustituyendo en $dB$:
> $$dB=\frac{\mu_0 I}{4\pi}\,\sin\theta\cdot\frac{\sin^{2}\theta}{s^{2}}\cdot\frac{s}{\sin^{2}\theta}\,d\theta=\frac{\mu_0 I}{4\pi s}\,\sin\theta\,d\theta.$$
>
> **Paso 4 — Integración sobre todo el hilo.** Cuando $x$ recorre $-\infty\to+\infty$, el ángulo $\theta$ recorre $0\to\pi$:
> $$B=\frac{\mu_0 I}{4\pi s}\int_{0}^{\pi}\sin\theta\,d\theta=\frac{\mu_0 I}{4\pi s}\Big[-\cos\theta\Big]_{0}^{\pi}=\frac{\mu_0 I}{4\pi s}\,(1-(-1)).$$
>
> **Paso 5 — Resultado.**
> $$\boxed{\,B=\frac{\mu_0 I}{2\pi s}\,}$$
> El campo es **azimutal**: rodea al hilo en círculos concéntricos, con sentido dado por la regla de la mano derecha (pulgar a lo largo de $I$, los dedos siguen $\vec B$). $\blacksquare$
>
> **Comprobación equivalente (forma cartesiana).** El mismo resultado sale de la integral
> $$B=\frac{\mu_0 I}{4\pi}\int_{-\infty}^{\infty}\frac{s\,dx}{(x^{2}+s^{2})^{3/2}}=\frac{\mu_0 I}{4\pi}\cdot\frac{s}{s^{2}}\left[\frac{x}{\sqrt{x^{2}+s^{2}}}\right]_{-\infty}^{\infty}=\frac{\mu_0 I}{4\pi s}\,(1-(-1))=\frac{\mu_0 I}{2\pi s},$$
> usando $\sin\theta=s/\mathscr r=s/(x^{2}+s^{2})^{1/2}$ en el paso 2.

> [!proposicion] Campo en el eje de una espira circular
> Una espira circular de radio $R$ porta corriente $I$. En un punto del eje a distancia $z$ del centro, el campo es axial y vale
> $$B_z=\frac{\mu_0 I R^{2}}{2\,(R^{2}+z^{2})^{3/2}}.$$

> [!demostracion] Espira en su eje
> **Paso 1 — Simetría: solo sobrevive $B_z$.** Tomamos la espira en el plano $xy$ centrada en el origen y el punto de campo en $(0,0,z)$. Para un elemento $I\,d\vec l\,'$ sobre la espira, el vector separación $\hat{\mathscr r}$ apunta del aro al punto del eje, con
> $$\mathscr r=\sqrt{R^{2}+z^{2}}\quad(\text{igual para todo el aro}).$$
> Como $d\vec l\,'\perp\hat{\mathscr r}$ (el elemento es tangente al aro y $\hat{\mathscr r}$ vive en un plano que lo contiene), el módulo de la contribución es
> $$dB=\frac{\mu_0 I}{4\pi}\frac{dl'}{R^{2}+z^{2}}.$$
> Cada $d\vec B$ forma un cono alrededor del eje. Por simetría de rotación, al recorrer toda la espira las **componentes perpendiculares al eje se cancelan** por pares diametralmente opuestos; solo sobrevive la componente $z$.
>
> **Paso 2 — Proyección sobre el eje.** El ángulo $\alpha$ entre $d\vec B$ y el eje cumple
> $$\cos\alpha=\frac{R}{\mathscr r}=\frac{R}{\sqrt{R^{2}+z^{2}}},$$
> de modo que la componente útil es
> $$dB_z=dB\,\cos\alpha=\frac{\mu_0 I}{4\pi}\frac{1}{R^{2}+z^{2}}\cdot\frac{R}{\sqrt{R^{2}+z^{2}}}\,dl'.$$
>
> **Paso 3 — Integración sobre el aro.** Todo el integrando es constante a lo largo de la espira; basta con $\oint dl'=2\pi R$:
> $$B_z=\frac{\mu_0 I}{4\pi}\frac{R}{(R^{2}+z^{2})^{3/2}}\oint dl'=\frac{\mu_0 I}{4\pi}\frac{R}{(R^{2}+z^{2})^{3/2}}\,(2\pi R).$$
>
> **Paso 4 — Resultado.**
> $$\boxed{\,B_z=\frac{\mu_0 I R^{2}}{2\,(R^{2}+z^{2})^{3/2}}\,}$$
> En el centro ($z=0$) se reduce al útil $B_z=\dfrac{\mu_0 I}{2R}$. $\blacksquare$
>
> ![[espira_eje.svg|360]]
>
> *Figura 2. Espira circular de radio $R$ y el campo $B_z$ sobre su eje; las componentes radiales de $d\vec B$ se cancelan por simetría y solo persiste la componente axial.*

> [!corolario] Límite lejano: el dipolo magnético
> Para $z\gg R$ se desprecia $R^{2}$ frente a $z^{2}$ en el denominador:
> $$B_z=\frac{\mu_0 I R^{2}}{2\,(R^{2}+z^{2})^{3/2}}\xrightarrow{\ z\gg R\ }\frac{\mu_0 I R^{2}}{2\,z^{3}}=\frac{\mu_0}{4\pi}\frac{2\,(I\pi R^{2})}{z^{3}}.$$
> Definiendo el **momento dipolar magnético** $m=I\,\pi R^{2}=I\,A$ (corriente por área),
> $$B\approx\frac{\mu_0}{4\pi}\frac{2m}{z^{3}}.$$
> Es la forma del campo de un dipolo magnético sobre su eje: decae como $1/z^{3}$, igual que un dipolo eléctrico. Toda espira pequeña, vista de lejos, se comporta como un dipolo de momento $\vec m=I\vec A$ — el punto de partida del [[Potencial Vector]] de un dipolo y de la teoría de imanes. $\blacksquare$

> [!warning] Coulomb vs. Biot–Savart: cuidado con la intuición
> A diferencia del campo de Coulomb, en Biot–Savart $\vec B$ es **perpendicular** tanto a la corriente como a $\hat{\mathscr r}$ (es un producto vectorial). Consecuencias:
> - $\vec B$ **no** apunta de la fuente al punto de campo; le da la vuelta a la corriente.
> - Las líneas de campo magnético son **cerradas** (lazos que envuelven la corriente), no radiales. Esto refleja $\nabla\cdot\vec B=0$: no hay "cargas magnéticas" de las que broten o mueran líneas.
> - El signo y la orientación dependen de la **regla de la mano derecha**; un error de orientación invierte todo el campo.

---

## En qué consiste

La Ley de Biot–Savart responde a la pregunta operativa: *dada una corriente, ¿cuánto vale el campo magnético en cada punto?* Su lógica es la misma que la del principio de superposición en electrostática, pero con un giro geométrico:

1. **Trocea la corriente.** Divides la distribución en elementos infinitesimales: trozos $I\,d\vec l\,'$ de hilo, parches $\vec K\,da'$ de superficie o celdas $\vec J\,d^3r'$ de volumen.
2. **Cada trozo aporta un $d\vec B$.** La contribución decae como $1/\mathscr r^{2}$ (como Coulomb) pero apunta en la dirección $\vec J\times\hat{\mathscr r}$: perpendicular al flujo y a la línea fuente→campo.
3. **Suma vectorialmente.** Integras todas las contribuciones. La simetría del problema decide qué componentes se cancelan (como las radiales en la espira) y cuáles se refuerzan.

La gran ventaja es que **siempre** es aplicable, sin importar la simetría. La desventaja es práctica: la integral vectorial puede ser difícil. Cuando hay simetría suficiente (hilos, solenoides, planos), la [[Ley de Ampere]] da el mismo resultado con mucho menos trabajo; Biot–Savart queda como el método general de fuerza bruta y como la base conceptual de toda la magnetostática.

---

## Resumen

> [!resumen] Fórmulas clave
>
> | Situación | Campo $\vec B$ |
> |---|---|
> | Forma general (volumen) | $\vec B=\dfrac{\mu_0}{4\pi}\displaystyle\int\dfrac{\vec J\times\hat{\mathscr r}}{\mathscr r^{2}}\,d^3r'$ |
> | Corriente filiforme | $\vec B=\dfrac{\mu_0}{4\pi}\displaystyle\int\dfrac{I\,d\vec l\,'\times\hat{\mathscr r}}{\mathscr r^{2}}$ |
> | Hilo recto infinito | $B=\dfrac{\mu_0 I}{2\pi s}$ (azimutal) |
> | Espira circular (eje) | $B_z=\dfrac{\mu_0 I R^{2}}{2(R^{2}+z^{2})^{3/2}}$ |
> | Centro de la espira | $B_z=\dfrac{\mu_0 I}{2R}$ |
> | Dipolo lejano ($z\gg R$) | $B\approx\dfrac{\mu_0}{4\pi}\dfrac{2m}{z^{3}},\ m=I\pi R^{2}$ |

> [!corolario] Ideas para recordar
> - Biot–Savart es el **análogo magnético de Coulomb**: misma ley $1/\mathscr r^{2}$, pero con producto vectorial $\vec J\times\hat{\mathscr r}$.
> - El producto vectorial hace que $\vec B$ sea **transversal**: líneas cerradas que envuelven la corriente, nunca radiales.
> - Es de aplicación **universal**; cuando hay simetría, la [[Ley de Ampere]] es el atajo.
> - Una espira pequeña vista de lejos $=$ **dipolo magnético** de momento $\vec m=I\vec A$, con campo $\sim 1/z^{3}$.

> [!referencia] Para profundizar
> - **Griffiths, *Introduction to Electrodynamics*, cap. 5** (Magnetostática; Biot–Savart y ejemplos del hilo y la espira).
> - **Jackson, *Classical Electrodynamics*, cap. 5** (formulación general y desarrollo multipolar magnético).
> - Notas relacionadas: [[Fuerza de Lorentz]], [[Ley de Ampere]], [[Potencial Vector]], y la sección [[3 Magnetostatica/index | Magnetostática]].
