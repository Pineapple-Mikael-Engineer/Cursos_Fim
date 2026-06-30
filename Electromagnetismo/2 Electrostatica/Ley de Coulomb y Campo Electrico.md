---
title: Ley de Coulomb y Campo Eléctrico
order: 1
tags:
  - electromagnetismo
  - teoria
  - electrostatica
draft: false
aliases:
  - Ley de Coulomb
  - Campo eléctrico
---

# Ley de Coulomb y Campo Eléctrico $\vec E=\dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r^2}\hat r$

---

> [!definicion] Ley de Coulomb y campo eléctrico
> La fuerza electrostática que una carga puntual $q'$ situada en $\vec r\,'$ ejerce sobre otra carga $q$ situada en $\vec r$ es, en el vacío,
> $$\vec F=\frac{1}{4\pi\varepsilon_0}\,\frac{q\,q'}{\mathscr r^{2}}\,\hat{\mathscr r},\qquad \hat{\mathscr r}=\frac{\vec r-\vec r\,'}{|\vec r-\vec r\,'|},\qquad \mathscr r=|\vec r-\vec r\,'|,$$
> dirigida a lo largo de la recta que une ambas cargas. El **campo eléctrico** creado por una distribución de fuente se define como la fuerza por unidad de carga de prueba positiva,
> $$\vec E(\vec r)=\lim_{q_0\to 0}\frac{\vec F}{q_0},$$
> de modo que la fuerza sobre una carga $q$ inmersa en el campo es $\vec F=q\,\vec E$. Para una sola carga puntual en el origen,
> $$\boxed{\;\vec E(\vec r)=\frac{1}{4\pi\varepsilon_0}\,\frac{q}{r^{2}}\,\hat r\;}$$

---

> [!info] Ubicación en el curso
> Esta nota pertenece al curso de **Electromagnetismo**, sección [[2 Electrostatica/index | Electrostática]]. Es la base de las notas hermanas [[Ley de Gauss]] (forma integral y diferencial de $\nabla\cdot\vec E$) y [[Potencial Electrico]] (el campo como gradiente $\vec E=-\nabla V$). Para el tratamiento riguroso de la divergencia del campo de una carga puntual y de las densidades singulares se usa [[Delta de Dirac y Singularidades]]. Referencia principal: **Griffiths, *Introduction to Electrodynamics*, cap. 2**.

---

## Ejemplo

> [!ejemplo] Fuerza entre dos cargas puntuales
> Dos cargas $q_1=+2{,}0\ \mathrm{nC}$ y $q_2=-3{,}0\ \mathrm{nC}$ se separan una distancia $\mathscr r=5{,}0\ \mathrm{cm}$. ¿Cuál es la magnitud y el carácter (atractivo o repulsivo) de la fuerza entre ellas?

> [!solucion]
> Con $k=\dfrac{1}{4\pi\varepsilon_0}=8{,}99\times10^{9}\ \mathrm{N\,m^2/C^2}$,
> $$|\vec F|=k\,\frac{|q_1 q_2|}{\mathscr r^{2}}=8{,}99\times10^{9}\cdot\frac{(2{,}0\times10^{-9})(3{,}0\times10^{-9})}{(5{,}0\times10^{-2})^{2}}\ \mathrm{N}.$$
> El numerador vale $6{,}0\times10^{-18}\ \mathrm{C^2}$ y el denominador $2{,}5\times10^{-3}\ \mathrm{m^2}$, así que
> $$|\vec F|=8{,}99\times10^{9}\cdot\frac{6{,}0\times10^{-18}}{2{,}5\times10^{-3}}\ \mathrm{N}\approx 2{,}2\times10^{-5}\ \mathrm{N}.$$
> Como el producto $q_1 q_2<0$, el factor de signo es negativo: la fuerza apunta de cada carga **hacia** la otra. Es **atractiva**, de magnitud $\approx 22\ \mathrm{\mu N}$.

---

## En qué consiste

La interacción electrostática entre cargas en reposo se rige por dos ideas centrales: la **ley de Coulomb** (acción directa entre cargas) y el **campo eléctrico** (intermediario local que reemplaza a la acción a distancia). Todo lo demás de la electrostática se deriva de estas dos.

![[coulomb_fuerza.svg|420]]
*Fuerza de Coulomb entre dos cargas: el vector separación $\hat{\mathscr r}$ apunta de la fuente al punto de campo; cargas del mismo signo se repelen, de signo opuesto se atraen.*

> [!teoria] La constante $\varepsilon_0$ y el signo de la fuerza
> La constante $\varepsilon_0=8{,}854\times10^{-12}\ \mathrm{C^2/(N\,m^2)}$ es la **permitividad del vacío**; fija la intensidad de la interacción eléctrica en el SI. Se agrupa en
> $$k=\frac{1}{4\pi\varepsilon_0}=8{,}99\times10^{9}\ \mathrm{N\,m^2/C^2}.$$
> El factor $4\pi$ "racionaliza" las ecuaciones: aparece aquí para que **no** aparezca en la ley de Gauss. El **signo** de la fuerza lo lleva el producto $q\,q'$:
> - $q\,q'>0$ (cargas iguales) $\Rightarrow$ $\vec F$ paralela a $\hat{\mathscr r}$: **repulsiva**.
> - $q\,q'<0$ (cargas opuestas) $\Rightarrow$ $\vec F$ antiparalela a $\hat{\mathscr r}$: **atractiva**.
>
> La fuerza decae como $1/\mathscr r^{2}$, igual que la gravitación de Newton, pero es enormemente más intensa y puede ser de ambos signos.

> [!proposicion] Principio de superposición de fuerzas
> La fuerza total sobre una carga $q$ debida a un conjunto de cargas $\{q_i'\}$ es la **suma vectorial** de las fuerzas individuales, cada una calculada como si las demás no existieran:
> $$\vec F=\sum_i \vec F_i=\frac{q}{4\pi\varepsilon_0}\sum_i \frac{q_i'}{\mathscr r_i^{2}}\,\hat{\mathscr r}_i.$$
> Esta linealidad es un hecho experimental y es la propiedad que hace tratable toda la electrostática.

> [!teoria] El campo eléctrico y sus líneas
> Sacando la carga de prueba $q$ del principio de superposición, lo que queda es una propiedad **del espacio** generada por las fuentes: el campo eléctrico. Para una colección de cargas,
> $$\vec E(\vec r)=\frac{1}{4\pi\varepsilon_0}\sum_i \frac{q_i}{\mathscr r_i^{2}}\,\hat{\mathscr r}_i.$$
> Se usa una **carga de prueba** $q_0\to 0$ para no perturbar la distribución fuente al medir. Las **líneas de campo** son curvas tangentes a $\vec E$ en cada punto; nacen en las cargas positivas y mueren en las negativas, su densidad mide la intensidad del campo, y **nunca se cruzan** (el campo es univaluado).

![[campo_cargas.svg|460]]
*Líneas de campo: una carga puntual positiva (radiales hacia afuera) y un dipolo (de la carga positiva a la negativa). La densidad de líneas indica la magnitud del campo.*

> [!teorema] Campo de una distribución continua de carga
> En el límite continuo, la suma sobre cargas puntuales se convierte en una integral sobre la distribución. Para una densidad volumétrica $\rho(\vec r\,')$,
> $$\vec E(\vec r)=\frac{1}{4\pi\varepsilon_0}\int \frac{\hat{\mathscr r}}{\mathscr r^{2}}\,\rho(\vec r\,')\,d^{3}r',$$
> con las versiones análogas para densidad lineal $\lambda$ y superficial $\sigma$.

> [!demostracion] Paso de la suma discreta a la integral
> **Paso 1 — Partición de la fuente.** Dividimos la distribución continua en $N$ elementos de volumen $\Delta V_i$ centrados en $\vec r_i'$. Cada elemento contiene una carga
> $$\Delta q_i=\rho(\vec r_i')\,\Delta V_i.$$
>
> **Paso 2 — Superposición.** Por el principio de superposición, el campo total es la suma de los campos de cada elemento, tratado como carga puntual $\Delta q_i$:
> $$\vec E(\vec r)\approx\frac{1}{4\pi\varepsilon_0}\sum_{i=1}^{N}\frac{\Delta q_i}{\mathscr r_i^{2}}\,\hat{\mathscr r}_i=\frac{1}{4\pi\varepsilon_0}\sum_{i=1}^{N}\frac{\hat{\mathscr r}_i}{\mathscr r_i^{2}}\,\rho(\vec r_i')\,\Delta V_i.$$
>
> **Paso 3 — Límite del continuo.** Hacemos $N\to\infty$ y $\Delta V_i\to 0$. La suma de Riemann converge a la integral de volumen sobre la región fuente $\mathcal V'$:
> $$\vec E(\vec r)=\frac{1}{4\pi\varepsilon_0}\int_{\mathcal V'} \frac{\hat{\mathscr r}}{\mathscr r^{2}}\,\rho(\vec r\,')\,d^{3}r',\qquad \hat{\mathscr r}=\frac{\vec r-\vec r\,'}{\mathscr r},\ \ \mathscr r=|\vec r-\vec r\,'|.$$
>
> **Paso 4 — Densidades inferiores.** Si la carga se reparte sobre una superficie ($\sigma$, $\mathrm{C/m^2}$) o sobre una curva ($\lambda$, $\mathrm{C/m}$), el mismo argumento da
> $$\vec E(\vec r)=\frac{1}{4\pi\varepsilon_0}\int_{\mathcal S'} \frac{\hat{\mathscr r}}{\mathscr r^{2}}\,\sigma(\vec r\,')\,da',\qquad \vec E(\vec r)=\frac{1}{4\pi\varepsilon_0}\int_{\mathcal L'} \frac{\hat{\mathscr r}}{\mathscr r^{2}}\,\lambda(\vec r\,')\,d\ell'. \qquad\blacksquare$$

> [!demostracion] Campo de un anillo cargado en su eje
> Un anillo de radio $R$ con carga total $Q$ uniformemente distribuida ($\lambda=Q/2\pi R$) está en el plano $z=0$ centrado en el origen. Buscamos $\vec E$ en el punto $P=(0,0,z)$ del eje.
>
> **Paso 1 — Elemento de carga y separación.** Un elemento $d\ell'=R\,d\phi'$ lleva carga $dq=\lambda\,R\,d\phi'$. Su distancia al punto $P$ es la misma para todos los elementos:
> $$\mathscr r=\sqrt{R^{2}+z^{2}}.$$
>
> **Paso 2 — Simetría: cancelación de las componentes radiales.** Cada $dq$ produce un $d\vec E$ con una componente a lo largo del eje ($z$) y una componente perpendicular al eje (radial, hacia el eje). Para cada elemento existe el diametralmente opuesto, cuya componente radial es **igual y opuesta**: al integrar sobre todo el anillo, las componentes radiales se cancelan exactamente. Solo sobrevive la componente $z$.
>
> **Paso 3 — Componente axial.** La proyección sobre el eje introduce el factor $\cos\theta=z/\mathscr r=z/\sqrt{R^{2}+z^{2}}$:
> $$dE_z=\frac{1}{4\pi\varepsilon_0}\,\frac{dq}{\mathscr r^{2}}\cos\theta=\frac{1}{4\pi\varepsilon_0}\,\frac{\lambda R\,d\phi'}{R^{2}+z^{2}}\cdot\frac{z}{\sqrt{R^{2}+z^{2}}}.$$
>
> **Paso 4 — Integración.** El integrando no depende de $\phi'$, luego $\int_0^{2\pi}d\phi'=2\pi$, y $\lambda\,R\,(2\pi)=Q$:
> $$E_z=\frac{1}{4\pi\varepsilon_0}\,\frac{z}{(R^{2}+z^{2})^{3/2}}\,\underbrace{\lambda R\,(2\pi)}_{=\,Q}=\frac{1}{4\pi\varepsilon_0}\,\frac{Q\,z}{(R^{2}+z^{2})^{3/2}}.$$
> $$\boxed{\;\vec E(0,0,z)=\frac{1}{4\pi\varepsilon_0}\,\frac{Q\,z}{(R^{2}+z^{2})^{3/2}}\,\hat z\;}$$
>
> **Paso 5 — Límite lejano $z\gg R$.** Si $z\gg R$, entonces $(R^{2}+z^{2})^{3/2}\approx z^{3}$, de modo que
> $$E_z\approx\frac{1}{4\pi\varepsilon_0}\,\frac{Q\,z}{z^{3}}=\frac{1}{4\pi\varepsilon_0}\,\frac{Q}{z^{2}}=\frac{kQ}{z^{2}},$$
> el campo de una **carga puntual** $Q$: a gran distancia el anillo se ve como un punto, como debe ser. $\blacksquare$

> [!proposicion] Campo de un hilo recto infinito
> Un hilo infinito a lo largo del eje $x$ con densidad lineal uniforme $\lambda$ produce, a distancia perpendicular $s$, un campo radial (perpendicular al hilo) de magnitud
> $$E=\frac{\lambda}{2\pi\varepsilon_0\,s}.$$

> [!demostracion] Hilo infinito por integración directa
> Colocamos el hilo sobre el eje $x$ y evaluamos $\vec E$ en el punto $P=(0,s,0)$ a distancia $s$.
>
> **Paso 1 — Elemento y separación.** Un elemento en $(x,0,0)$ tiene carga $dq=\lambda\,dx$. La separación al punto $P$ es
> $$\mathscr r=\sqrt{x^{2}+s^{2}}.$$
>
> **Paso 2 — Simetría.** Para cada elemento en $+x$ existe su simétrico en $-x$: sus componentes a lo largo del hilo ($x$) se cancelan, y solo sobrevive la componente perpendicular (radial), con factor de proyección $\cos\theta=s/\mathscr r=s/\sqrt{x^{2}+s^{2}}$.
>
> **Paso 3 — Componente perpendicular.**
> $$dE_\perp=\frac{1}{4\pi\varepsilon_0}\,\frac{\lambda\,dx}{x^{2}+s^{2}}\cdot\frac{s}{\sqrt{x^{2}+s^{2}}}=\frac{\lambda s}{4\pi\varepsilon_0}\,\frac{dx}{(x^{2}+s^{2})^{3/2}}.$$
>
> **Paso 4 — La integral clave.** Integramos sobre todo el hilo, $x\in(-\infty,\infty)$. Usando
> $$\int_{-\infty}^{\infty}\frac{dx}{(x^{2}+s^{2})^{3/2}}=\left[\frac{x}{s^{2}\sqrt{x^{2}+s^{2}}}\right]_{-\infty}^{\infty}=\frac{1}{s^{2}}\big(1-(-1)\big)=\frac{2}{s^{2}},$$
> (el corchete se obtiene con la sustitución $x=s\tan\theta$, $dx=s\sec^2\theta\,d\theta$, que reduce el integrando a $\cos\theta/s^2$).
>
> **Paso 5 — Resultado.**
> $$E=\frac{\lambda s}{4\pi\varepsilon_0}\cdot\frac{2}{s^{2}}=\frac{\lambda}{2\pi\varepsilon_0\,s}.$$
> $$\boxed{\;\vec E=\frac{\lambda}{2\pi\varepsilon_0\,s}\,\hat s\;}$$
> El campo decae como $1/s$ (no como $1/s^2$), reflejo de la geometría infinita de la fuente. Este mismo resultado se obtiene en **una sola línea** con la [[Ley de Gauss]] usando un cilindro coaxial: la integración directa es laboriosa; Gauss la vuelve trivial cuando hay simetría. $\blacksquare$

> [!warning] Divergencia en $r\to 0$
> El campo de una carga puntual $\vec E=\dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r^{2}}\hat r$ **diverge** cuando $r\to 0$. Esto no es un defecto físico evitable de la electrostática elemental: la **energía propia** de una carga puntual también diverge. El tratamiento riguroso de esta singularidad —y de la divergencia $\nabla\cdot\vec E$ concentrada en el punto— requiere la **delta de Dirac**, $\nabla\cdot\left(\frac{\hat r}{r^2}\right)=4\pi\,\delta^{3}(\vec r)$; ver [[Delta de Dirac y Singularidades]].

---

## Resumen

> [!resumen] Fórmulas clave
> | Concepto | Expresión | Notas |
> |---|---|---|
> | Fuerza de Coulomb | $\vec F=\dfrac{1}{4\pi\varepsilon_0}\dfrac{q\,q'}{\mathscr r^{2}}\,\hat{\mathscr r}$ | signo lo da $q\,q'$ |
> | Campo (definición) | $\vec E=\lim_{q_0\to0}\vec F/q_0$ | $\vec F=q\,\vec E$ |
> | Carga puntual | $\vec E=\dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r^{2}}\,\hat r$ | diverge en $r\to0$ |
> | Distribución $\rho$ | $\vec E=\dfrac{1}{4\pi\varepsilon_0}\displaystyle\int\dfrac{\hat{\mathscr r}}{\mathscr r^{2}}\rho\,d^3r'$ | $\lambda,\sigma$ análogas |
> | Anillo (eje) | $E_z=\dfrac{1}{4\pi\varepsilon_0}\dfrac{Qz}{(R^2+z^2)^{3/2}}$ | $\to kQ/z^2$ si $z\gg R$ |
> | Hilo infinito | $E=\dfrac{\lambda}{2\pi\varepsilon_0\,s}$ | decae como $1/s$ |

> [!corolario] Ideas para recordar
> - La ley de Coulomb y la **linealidad** (superposición) generan toda la electrostática: el campo de cualquier distribución es una integral de campos de carga puntual.
> - La **simetría** elimina componentes antes de integrar (radiales en el anillo, longitudinales en el hilo): identificarla simplifica el cálculo.
> - Cuando hay simetría suficiente, conviene pasar a [[Ley de Gauss]]; cuando no, se integra directamente con la ley de Coulomb.

> [!referencia] Fuentes
> - **D. J. Griffiths**, *Introduction to Electrodynamics*, 4.ª ed., cap. 2 (Electrostática).
> - **J. D. Jackson**, *Classical Electrodynamics*, cap. 1.
> - Notas relacionadas: [[Ley de Gauss]], [[Potencial Electrico]], [[Delta de Dirac y Singularidades]], [[2 Electrostatica/index | Electrostática]].
