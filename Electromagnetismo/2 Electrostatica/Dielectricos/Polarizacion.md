---
title: Polarización
order: 1
tags:
  - electromagnetismo
  - teoria
  - dielectricos
draft: false
aliases:
  - Polarización
  - Cargas ligadas
---

# Polarización $\rho_b=-\nabla\cdot\vec P,\quad \sigma_b=\vec P\cdot\hat n$

> [!definicion]
> El **vector de polarización** $\vec P$ es el **momento dipolar por unidad de volumen** de un material. Si un pequeño elemento de volumen $d^3r'$ contiene un momento dipolar neto $d\vec p$, entonces
> $$\vec P\equiv\frac{d\vec p}{d^3r'},\qquad [\vec P]=\frac{\text{C}\cdot\text{m}}{\text{m}^3}=\frac{\text{C}}{\text{m}^2}.$$
> Describe el estado de polarización del dieléctrico: cuántos dipolos hay, cuán alineados están y en qué dirección apuntan. Toda la respuesta del material —el campo que crea y las **cargas ligadas** que aparecen— se deduce de $\vec P$.

---

> [!info]
> **Nota de la subsección [[2 Electrostatica/Dielectricos/index | Dieléctricos]]**, dentro de [[2 Electrostatica/index | Electrostática]] (curso Electromagnetismo). Aquí se construye el vector $\vec P$ y se deducen las **cargas ligadas** $\rho_b=-\nabla\cdot\vec P$ y $\sigma_b=\vec P\cdot\hat n$; la nota hermana [[Desplazamiento Electrico]] introduce $\vec D=\varepsilon_0\vec E+\vec P$ para separar carga libre y ligada. **Referencia.** Griffiths, *Introduction to Electrodynamics*, cap. 4.

---

## En qué consiste

> [!teoria] Del dipolo individual al material polarizado
> La estrategia es construir el campo del dieléctrico **sumando** los campos de todos sus dipolos. Por eso se necesitan dos ingredientes:
> 1. El **potencial de un solo dipolo** $V_{\text{dip}}$, que se calcula a continuación.
> 2. Una manera de **sumar** infinitos dipolos infinitesimales repartidos por el volumen, cada uno con momento $d\vec p=\vec P\,d^3r'$.
>
> El resultado, sorprendente y central, es que ese campo es **idéntico** al de dos densidades de carga reales: una volumétrica $\rho_b=-\nabla\cdot\vec P$ y una superficial $\sigma_b=\vec P\cdot\hat n$, llamadas **cargas ligadas**. Es decir: para calcular el campo, podemos olvidarnos de los dipolos y tratar el dieléctrico como una distribución ordinaria de carga.

> [!demostracion] Potencial de un dipolo puntual
> Sean dos cargas $+q$ y $-q$ separadas por un vector $\vec d$ (de la negativa a la positiva). El potencial en un punto $\vec r$ medido desde el centro del dipolo es
> $$V(\vec r)=\frac{1}{4\pi\varepsilon_0}\left(\frac{q}{\mathscr r_+}-\frac{q}{\mathscr r_-}\right),$$
> donde $\mathscr r_\pm$ son las distancias a las cargas $\pm q$.
>
> **Paso 1 — Distancias en el límite lejano.** Colocando $\pm q$ en $\pm\vec d/2$, la ley de los cosenos da, con $\theta$ el ángulo entre $\vec r$ y $\vec d$,
> $$\mathscr r_\pm^2=r^2\mp r\,d\cos\theta+\frac{d^2}{4}\;\xrightarrow{\,r\gg d\,}\;r^2\!\left(1\mp\frac{d}{r}\cos\theta\right).$$
>
> **Paso 2 — Desarrollo a primer orden.** Tomando la inversa de la raíz y usando $(1+x)^{-1/2}\approx 1-\tfrac12 x$,
> $$\frac{1}{\mathscr r_\pm}\approx\frac{1}{r}\left(1\pm\frac{d}{2r}\cos\theta\right).$$
>
> **Paso 3 — Diferencia.** Restando,
> $$\frac{1}{\mathscr r_+}-\frac{1}{\mathscr r_-}\approx\frac{d\cos\theta}{r^2}.$$
>
> **Paso 4 — Definición del momento dipolar.** Con $\vec p\equiv q\vec d$ y $\vec p\cdot\hat r=q\,d\cos\theta$,
> $$\boxed{\,V_{\text{dip}}(\vec r)=\frac{1}{4\pi\varepsilon_0}\frac{\vec p\cdot\hat r}{r^2}\,.}$$
> El potencial del dipolo decae como $1/r^2$ (más rápido que el $1/r$ de una carga puntual) y depende de la orientación a través de $\vec p\cdot\hat r$. $\blacksquare$

> [!demostracion] Potencial de un objeto polarizado (deducción central)
> Cada elemento de volumen $d^3r'$ del dieléctrico, situado en $\vec r\,'$, posee un momento dipolar $d\vec p=\vec P(\vec r\,')\,d^3r'$. Aplicando el potencial del dipolo, con el **vector separación** $\vec{\mathscr r}=\vec r-\vec r\,'$, $\mathscr r=|\vec r-\vec r\,'|$ y $\hat{\mathscr r}=\vec{\mathscr r}/\mathscr r$, su aporte es
> $$dV=\frac{1}{4\pi\varepsilon_0}\frac{\vec P\cdot\hat{\mathscr r}}{\mathscr r^2}\,d^3r'.$$
>
> **Paso 1 — Integrar sobre el volumen.** Sumando todos los elementos,
> $$V(\vec r)=\frac{1}{4\pi\varepsilon_0}\int_V\frac{\vec P(\vec r\,')\cdot\hat{\mathscr r}}{\mathscr r^2}\,d^3r'.$$
>
> **Paso 2 — Identidad del gradiente.** Derivando respecto de las coordenadas de la **fuente** $\vec r\,'$ (de ahí $\nabla'$),
> $$\nabla'\frac{1}{\mathscr r}=\frac{\hat{\mathscr r}}{\mathscr r^2}.$$
> El signo es $+$ porque al derivar $1/\mathscr r$ respecto de $\vec r\,'$ aparece un signo menos que cancela el de $\hat{\mathscr r}=(\vec r-\vec r\,')/\mathscr r$ apuntando de la fuente al campo. Sustituyendo,
> $$V(\vec r)=\frac{1}{4\pi\varepsilon_0}\int_V\vec P\cdot\!\left(\nabla'\frac{1}{\mathscr r}\right)d^3r'.$$
>
> **Paso 3 — Integración por partes.** Usamos la identidad $\nabla'\cdot\!\left(\dfrac{\vec P}{\mathscr r}\right)=\dfrac{1}{\mathscr r}\,\nabla'\cdot\vec P+\vec P\cdot\nabla'\dfrac{1}{\mathscr r}$, esto es,
> $$\vec P\cdot\nabla'\frac{1}{\mathscr r}=\nabla'\cdot\!\left(\frac{\vec P}{\mathscr r}\right)-\frac{1}{\mathscr r}\,\nabla'\cdot\vec P.$$
> Integrando y aplicando el **teorema de la divergencia** al primer término ($\int_V\nabla'\cdot\vec F\,d^3r'=\oint_S\vec F\cdot\hat n\,da'$),
> $$\int_V\vec P\cdot\nabla'\frac{1}{\mathscr r}\,d^3r'=\oint_S\frac{\vec P\cdot\hat n}{\mathscr r}\,da'-\int_V\frac{\nabla'\cdot\vec P}{\mathscr r}\,d^3r'.$$
>
> **Paso 4 — Reagrupar.** El potencial queda
> $$V(\vec r)=\frac{1}{4\pi\varepsilon_0}\left[\oint_S\frac{\vec P\cdot\hat n}{\mathscr r}\,da'-\int_V\frac{\nabla'\cdot\vec P}{\mathscr r}\,d^3r'\right].$$
>
> **Paso 5 — Identificar las cargas ligadas.** Ambos términos tienen exactamente la forma del potencial de una distribución de carga, $\dfrac{1}{4\pi\varepsilon_0}\displaystyle\int\dfrac{\text{carga}}{\mathscr r}$. Comparando, definimos
> $$\boxed{\;\sigma_b=\vec P\cdot\hat n,\qquad \rho_b=-\nabla\cdot\vec P\;}$$
> y entonces
> $$V(\vec r)=\frac{1}{4\pi\varepsilon_0}\left[\oint_S\frac{\sigma_b}{\mathscr r}\,da'+\int_V\frac{\rho_b}{\mathscr r}\,d^3r'\right].\qquad\blacksquare$$
>
> **Interpretación.** El potencial —y por tanto el campo $\vec E=-\nabla V$— de un dieléctrico polarizado es **exactamente** el de esas dos densidades de carga ligada: una superficial $\sigma_b$ sobre la frontera y una volumétrica $\rho_b$ en el interior. No es una aproximación: la integral de dipolos se ha reescrito sin pérdida en una integral de cargas. Por eso, una vez conocido $\vec P$, todo el problema del dieléctrico se reduce a un problema de electrostática ordinaria.

![[polarizacion.svg|440]]
*Dieléctrico polarizado: los dipolos se alinean con el campo. En el interior, la cabeza positiva de un dipolo se cancela con la cola negativa del vecino ($\rho_b=0$ si $\vec P$ es uniforme); en las caras la cancelación falla y queda carga ligada superficial $\pm\sigma_b=\pm\vec P\cdot\hat n$. Esa carga real es la fuente del campo del dieléctrico.*

---

## Ejemplo

> [!ejemplo] Esfera uniformemente polarizada
> Una esfera de radio $R$ con polarización **uniforme** $\vec P=P\hat z$. Hallar sus cargas ligadas y el campo en su interior.

> [!solucion]
> **Paso 1 — Carga ligada de volumen.** Como $\vec P=P\hat z$ es constante,
> $$\rho_b=-\nabla\cdot\vec P=-\nabla\cdot(P\hat z)=0.$$
> No hay carga ligada en el volumen: dentro, cada dipolo cancela a su vecino.
>
> **Paso 2 — Carga ligada de superficie.** En la superficie de la esfera $\hat n=\hat r$, y $\hat z\cdot\hat r=\cos\theta$, luego
> $$\sigma_b=\vec P\cdot\hat n=P\,\hat z\cdot\hat r=P\cos\theta.$$
> La carga ligada se acumula en las caras: positiva en el polo norte ($\theta=0$) y negativa en el sur ($\theta=\pi$), anulándose en el ecuador.
>
> **Paso 3 — Campo interior.** El problema se reduce ahora a una **esfera con densidad superficial** $\sigma_b=P\cos\theta$. Esta distribución es la que aparece al resolver el potencial de una esfera por armónicos; su potencial interior es
> $$V_{\text{int}}(\vec r)=\frac{P}{3\varepsilon_0}\,r\cos\theta=\frac{P}{3\varepsilon_0}\,z,$$
> un potencial **lineal en $z$**. Tomando el gradiente,
> $$\vec E=-\nabla V_{\text{int}}=-\frac{P}{3\varepsilon_0}\,\hat z=-\frac{\vec P}{3\varepsilon_0}.$$
>
> **Resultado.**
> $$\boxed{\;\vec E_{\text{int}}=-\frac{\vec P}{3\varepsilon_0}\;}$$
> El campo interior es **uniforme** y **opuesto** a $\vec P$: es el campo despolarizante creado por las cargas ligadas $\sigma_b=P\cos\theta$ de las caras, que se oponen a la polarización que las generó. $\blacksquare$

> [!warning] Las cargas ligadas son carga real
> $\sigma_b$ y $\rho_b$ **no** son un artificio de cálculo ni una "carga ficticia": son **acumulación física de carga atómica**. Cuando los dipolos se alinean, en cada cara del material queda al descubierto un exceso real de carga (los extremos no compensados de los dipolos del borde). Esa carga produce campo, atrae y repele, y se puede medir. La única diferencia con la **carga libre** es su **origen**: proviene del desplazamiento de cargas ligadas dentro de dipolos —no de electrones que viajan por el material—. Llamarla "ligada" describe de dónde viene, no que sea menos real.

---

## Resumen

> [!resumen]
> | Concepto | Expresión | Significado |
> |---|---|---|
> | Vector polarización | $\vec P=d\vec p/d^3r'$ | Momento dipolar por unidad de volumen |
> | Potencial del dipolo | $V_{\text{dip}}=\dfrac{1}{4\pi\varepsilon_0}\dfrac{\vec p\cdot\hat r}{r^2}$ | Decae como $1/r^2$ |
> | Carga ligada de volumen | $\rho_b=-\nabla\cdot\vec P$ | Nace si $\vec P$ no es uniforme |
> | Carga ligada de superficie | $\sigma_b=\vec P\cdot\hat n$ | Componente normal de $\vec P$ en la frontera |
> | Potencial del dieléctrico | $V=\dfrac{1}{4\pi\varepsilon_0}\!\left[\oint\dfrac{\sigma_b}{\mathscr r}da'+\displaystyle\int\dfrac{\rho_b}{\mathscr r}d^3r'\right]$ | Igual al de las cargas ligadas |
> | Esfera con $\vec P=P\hat z$ | $\rho_b=0,\ \sigma_b=P\cos\theta,\ \vec E_{\text{int}}=-\vec P/3\varepsilon_0$ | Campo interior uniforme |

> [!corolario] Idea para recordar
> Un dieléctrico polarizado **es** una distribución de carga ligada: el campo de sus dipolos coincide exactamente con el de $\sigma_b=\vec P\cdot\hat n$ y $\rho_b=-\nabla\cdot\vec P$. Esto traslada todo problema de medios polarizados al terreno conocido de la electrostática; el siguiente paso, [[Desplazamiento Electrico | $\vec D$]], permitirá además separar limpiamente esta carga ligada de la libre.

> [!referencia]
> Griffiths, *Introduction to Electrodynamics*, cap. 4, §4.1–4.2 ("Polarization", "The Field of a Polarized Object"). El ejemplo de la esfera uniformemente polarizada: Griffiths, ej. 4.2. Tratamiento microscópico de $\vec P$ y la polarizabilidad: Jackson, cap. 4.
