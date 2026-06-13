---
title: Potencial Eléctrico
tags:
  - electromagnetismo
  - teoria
  - electrostatica
draft: false
aliases:
  - Potencial eléctrico
  - Voltaje
---

# Potencial Eléctrico $\vec E=-\nabla V,\quad V=\dfrac{1}{4\pi\varepsilon_0}\displaystyle\int\dfrac{\rho}{\mathscr r}\,d^3r'$

> [!definicion]
> El **potencial eléctrico** $V(\vec r)$ es el campo **escalar** del que deriva el campo eléctrico mediante
> $$\boxed{\ \vec E=-\nabla V\ }$$
> Físicamente, $V(\vec r)$ es el **trabajo por unidad de carga** necesario para traer una carga de prueba desde un punto de **referencia** hasta $\vec r$ contra el campo:
> $$V(\vec r)=-\int_{\text{ref}}^{\vec r}\vec E\cdot d\vec l.$$
> Su existencia se debe a que en electrostática $\nabla\times\vec E=\vec 0$: el campo es **conservativo**. Para una distribución de carga $\rho$,
> $$V(\vec r)=\frac{1}{4\pi\varepsilon_0}\int\frac{\rho(\vec r\,')}{\mathscr r}\,d^3r',\qquad \mathscr r\equiv|\vec r-\vec r\,'|,$$
> una **única integral escalar** —frente a las tres componentes de $\vec E$—. Se mide en voltios ($1\ \text{V}=1\ \text{J/C}$); de ahí el alias **voltaje**.

---

> [!info]
> **Sección [[2 Electrostatica/index | Electrostática]]** (capítulo 2). Esta nota desarrolla la segunda ecuación estática, $\nabla\times\vec E=\vec 0$, y su consecuencia: el potencial.
> **Notas hermanas.** [[Ley de Gauss]] (la otra ecuación, $\nabla\cdot\vec E=\rho/\varepsilon_0$), [[Poisson y Laplace]] (qué EDP cumple $V$) y [[Energia Electrostatica]] (energía en términos de $V$).
> **Herramientas.** Usa [[Identidades Vectoriales]] (rotacional de un gradiente, teorema del gradiente) y [[Teoremas Integrales]] (Stokes).
> **Referencia.** Griffiths, *Introduction to Electrodynamics*, cap. 2. Unidades SI; constante $k=\dfrac{1}{4\pi\varepsilon_0}$.

---

## Existencia del potencial

> [!teorema] Como $\nabla\times\vec E=\vec 0$, existe $V$ con $\vec E=-\nabla V$
> En electrostática el campo es **irrotacional**, $\nabla\times\vec E=\vec 0$. Entonces:
> 1. la **circulación** de $\vec E$ por cualquier curva cerrada es nula, $\displaystyle\oint\vec E\cdot d\vec l=0$;
> 2. la integral de línea $\displaystyle\int_{\text{ref}}^{\vec r}\vec E\cdot d\vec l$ **no depende del camino**;
> 3. existe un campo escalar $V$, definido salvo una constante, tal que $\vec E=-\nabla V$ (el signo $-$ es convenio).

> [!demostracion] De $\nabla\times\vec E=\vec 0$ a $\vec E=-\nabla V$
> **Paso 1 — Circulación nula.** Tomemos una curva cerrada $\Gamma$ que bordea una superficie $S$. Por el teorema de Stokes ([[Teoremas Integrales]]),
> $$\oint_\Gamma\vec E\cdot d\vec l=\int_S(\nabla\times\vec E)\cdot d\vec A=\int_S\vec 0\cdot d\vec A=0.$$
> La circulación de $\vec E$ a lo largo de **cualquier** lazo cerrado es cero.
>
> **Paso 2 — Independencia del camino.** Sean dos caminos $C_1$ y $C_2$ que van del punto $a$ al punto $b$. Recorrer $C_1$ hacia adelante y $C_2$ hacia atrás forma un lazo cerrado, así que por el Paso 1
> $$\int_{C_1}\vec E\cdot d\vec l-\int_{C_2}\vec E\cdot d\vec l=\oint\vec E\cdot d\vec l=0\ \Longrightarrow\ \int_{C_1}\vec E\cdot d\vec l=\int_{C_2}\vec E\cdot d\vec l.$$
> La integral solo depende de los extremos. Podemos, por tanto, **definir** la función
> $$V(\vec r)\equiv-\int_{\text{ref}}^{\vec r}\vec E\cdot d\vec l,$$
> sin ambigüedad de trayectoria (el signo $-$ es el convenio elegido).
>
> **Paso 3 — Recuperar el campo: teorema del gradiente.** Por el teorema fundamental para gradientes ([[Identidades Vectoriales]]),
> $$V(\vec r+d\vec l)-V(\vec r)=\nabla V\cdot d\vec l.$$
> Pero por la propia definición de $V$,
> $$V(\vec r+d\vec l)-V(\vec r)=-\vec E\cdot d\vec l.$$
> Igualando para todo desplazamiento $d\vec l$ arbitrario:
> $$\nabla V\cdot d\vec l=-\vec E\cdot d\vec l\quad\forall\,d\vec l\ \Longrightarrow\ \boxed{\vec E=-\nabla V}.$$
>
> **Coherencia (recíproco).** Que un campo así definido es irrotacional es inmediato, pues el rotacional de un gradiente es siempre nulo ([[Identidades Vectoriales]]):
> $$\nabla\times\vec E=\nabla\times(-\nabla V)=\vec 0.\qquad\blacksquare$$

---

## Potencial de una carga puntual

> [!proposicion] $V=\dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r}$, con referencia en el infinito
> El potencial de una carga puntual $q$ situada en el origen, tomando $V(\infty)=0$, es
> $$V(r)=\frac{1}{4\pi\varepsilon_0}\frac{q}{r}=k\,\frac{q}{r}.$$

> [!demostracion] Integrando $\vec E$ desde el infinito
> **Paso 1 — Campo de Coulomb.** El campo de la carga puntual es radial, $\displaystyle\vec E=k\,\frac{q}{r^2}\,\hat r$ ([[Ley de Coulomb y Campo Electrico]]).
>
> **Paso 2 — Camino radial.** Como la integral no depende del camino (Paso 2 del teorema anterior), elegimos el más simple: una recta radial desde $\infty$ hasta $r$, con $d\vec l=dr'\,\hat r$. Entonces $\vec E\cdot d\vec l=k\,q\,dr'/r'^2$ y
> $$V(r)=-\int_\infty^{r}\vec E\cdot d\vec l=-\int_\infty^{r}k\,\frac{q}{r'^2}\,dr'=-k\,q\left[-\frac{1}{r'}\right]_\infty^{r}.$$
>
> **Paso 3 — Evaluar.**
> $$V(r)=-k\,q\left(-\frac{1}{r}+\frac{1}{\infty}\right)=k\,\frac{q}{r}=\frac{1}{4\pi\varepsilon_0}\frac{q}{r}.\qquad\blacksquare$$
>
> La elección $V(\infty)=0$ es la que hace finita y natural esta expresión; es la referencia estándar para distribuciones acotadas.

---

## Superposición: la fórmula integral

> [!teorema] $V=\dfrac{1}{4\pi\varepsilon_0}\displaystyle\int\dfrac{\rho(\vec r\,')}{\mathscr r}\,d^3r'$
> Para una distribución continua de carga $\rho$, el potencial en $\vec r$ es la suma (integral) de las contribuciones puntuales:
> $$V(\vec r)=\frac{1}{4\pi\varepsilon_0}\int\frac{\rho(\vec r\,')}{\mathscr r}\,d^3r',\qquad \mathscr r=|\vec r-\vec r\,'|.$$

> [!demostracion] Sumar potenciales escalares
> **Paso 1 — Superposición.** El campo cumple el principio de superposición, $\vec E=\sum_i\vec E_i$. Como $\vec E_i=-\nabla V_i$ y el gradiente es lineal,
> $$\vec E=-\nabla\Big(\textstyle\sum_i V_i\Big)\ \Longrightarrow\ V=\sum_i V_i.$$
> El potencial total es la **suma escalar** de los potenciales individuales.
>
> **Paso 2 — Carga puntual a distancia $\mathscr r$.** El aporte de una carga $q_i$ en $\vec r_i$ a un punto a distancia $\mathscr r_i=|\vec r-\vec r_i|$ es $V_i=k\,q_i/\mathscr r_i$.
>
> **Paso 3 — Continuo.** Sustituyendo $q_i\to\rho(\vec r\,')\,d^3r'$ y la suma por integral:
> $$V(\vec r)=\frac{1}{4\pi\varepsilon_0}\int\frac{\rho(\vec r\,')}{\mathscr r}\,d^3r'.\qquad\blacksquare$$

> [!regla] La ventaja del potencial
> Calcular $V$ exige **una sola integral escalar**; calcular $\vec E$ directamente exige **tres** (una por componente) y vigilar las direcciones de cada $\hat{\mathscr r}$. Por eso la estrategia general es: hallar $V$, y luego derivar $\vec E=-\nabla V$. El precio es barato: una derivada frente a tres integrales.

---

## Conexión con Poisson

> [!teorema] $\nabla^2 V=-\rho/\varepsilon_0$
> Combinando la ley de Gauss diferencial con la definición del potencial, $V$ satisface la **ecuación de Poisson**.

> [!demostracion] Insertar $\vec E=-\nabla V$ en la ley de Gauss
> **Paso 1 — Las dos ecuaciones.** De [[Ley de Gauss]], $\nabla\cdot\vec E=\rho/\varepsilon_0$. De esta nota, $\vec E=-\nabla V$.
>
> **Paso 2 — Sustituir.**
> $$\nabla\cdot\vec E=\nabla\cdot(-\nabla V)=-\nabla^2 V.$$
>
> **Paso 3 — Igualar.**
> $$-\nabla^2 V=\frac{\rho}{\varepsilon_0}\ \Longrightarrow\ \boxed{\nabla^2 V=-\frac{\rho}{\varepsilon_0}}.$$
> En las regiones sin carga ($\rho=0$) se reduce a la **ecuación de Laplace** $\nabla^2 V=0$. El estudio de estas EDP, con sus condiciones de frontera, se continúa en [[Poisson y Laplace]]. $\blacksquare$

---

## Energía, equipotenciales y geometría

> [!proposicion] Energía potencial $U=qV$ y trabajo $W=q[V(b)-V(a)]$
> Una carga puntual $q$ en un punto de potencial $V$ tiene energía potencial $U=qV$. El trabajo que hace el campo al llevar $q$ de $a$ a $b$ es
> $$W=-\Delta U=q\big[V(a)-V(b)\big],$$
> y el que hace un agente externo (sin energía cinética neta) es $W_{\text{ext}}=q\big[V(b)-V(a)\big]$. Esto conecta con [[Energia Electrostatica]].

> [!proposicion] Las superficies equipotenciales son $\perp$ a $\vec E$
> Sobre una superficie de $V$ constante, todo desplazamiento $d\vec l$ tangente cumple $dV=0$. Pero
> $$dV=\nabla V\cdot d\vec l=-\vec E\cdot d\vec l.$$
> Luego $\vec E\cdot d\vec l=0$ para todo $d\vec l$ tangente: $\vec E$ es **perpendicular** a la superficie equipotencial. Además, como $\vec E=-\nabla V$ y el gradiente apunta hacia $V$ **creciente**, el campo $\vec E$ apunta hacia $V$ **decreciente** (de mayor a menor potencial).

![[equipotenciales.svg|420]]
*Líneas de campo $\vec E$ (con flecha, de $V$ alto a $V$ bajo) cortando perpendicularmente a las superficies equipotenciales (curvas de $V$ constante). Donde las equipotenciales se aprietan, $\vec E$ es más intenso.*

> [!warning] $V$ está definido salvo una constante
> El potencial depende del punto de **referencia**: cambiarlo suma una constante a $V$ en todos lados. Esa constante no afecta al campo, pues $\nabla(V+C)=\nabla V$, ni a las diferencias $V(b)-V(a)$. **Solo las diferencias de potencial tienen sentido físico**; el "valor absoluto" de $V$ es convencional (para cargas acotadas se fija $V(\infty)=0$).

---

## Ejemplo

> [!ejemplo] Potencial en el eje de un disco uniformemente cargado
> Un disco de radio $R$ tiene densidad superficial de carga uniforme $\sigma$. Halla $V(z)$ en un punto del **eje** (a distancia $z$ del centro, perpendicular al disco) y, a partir de él, recupera $E_z$.

> [!solucion]
> **Paso 1 — Elemento de carga.** Usamos coordenadas polares en el disco. Un anillo de radio $s$ y grosor $ds$ tiene área $dA=2\pi s\,ds$ y carga $dq=\sigma\,2\pi s\,ds$.
>
> **Paso 2 — Distancia al punto del eje.** Todos los puntos del anillo están a la **misma** distancia del punto del eje:
> $$\mathscr r=\sqrt{s^2+z^2}.$$
> Esta es la gran ventaja de trabajar con el escalar $V$: no hay que descomponer en componentes; basta la distancia.
>
> **Paso 3 — Integral escalar.** Sumando los aportes $dV=k\,dq/\mathscr r$:
> $$V(z)=\frac{1}{4\pi\varepsilon_0}\int_0^{R}\frac{\sigma\,2\pi s\,ds}{\sqrt{s^2+z^2}}=\frac{\sigma}{2\varepsilon_0}\int_0^{R}\frac{s\,ds}{\sqrt{s^2+z^2}}.$$
>
> **Paso 4 — Resolver la integral.** Con $u=s^2+z^2$, $du=2s\,ds$:
> $$\int_0^{R}\frac{s\,ds}{\sqrt{s^2+z^2}}=\Big[\sqrt{s^2+z^2}\,\Big]_0^{R}=\sqrt{R^2+z^2}-\sqrt{z^2}=\sqrt{R^2+z^2}-|z|.$$
> Por tanto
> $$\boxed{\,V(z)=\frac{\sigma}{2\varepsilon_0}\left(\sqrt{R^2+z^2}-|z|\right)\,}.$$
>
> **Paso 5 — Recuperar el campo $E_z=-\partial_z V$.** Para $z>0$ es $|z|=z$, y
> $$E_z=-\frac{\partial V}{\partial z}=-\frac{\sigma}{2\varepsilon_0}\left(\frac{z}{\sqrt{R^2+z^2}}-1\right)=\frac{\sigma}{2\varepsilon_0}\left(1-\frac{z}{\sqrt{R^2+z^2}}\right).$$
> Hemos obtenido $E_z$ con **una derivada**, sin volver a integrar. $\blacksquare$
>
> **Comprobaciones (límites).**
> - **Plano infinito** ($R\to\infty$): $E_z\to\dfrac{\sigma}{2\varepsilon_0}$, el campo constante de un plano cargado (ver [[Ley de Gauss]]).
> - **Lejos** ($z\gg R$): desarrollando $\sqrt{R^2+z^2}\approx z\big(1+\tfrac{R^2}{2z^2}\big)$ resulta $V\approx\dfrac{\sigma R^2}{4\varepsilon_0 z}=\dfrac{1}{4\pi\varepsilon_0}\dfrac{Q}{z}$ con $Q=\sigma\pi R^2$: el disco se ve como una **carga puntual**, como debe ser.

---

## En qué consiste

> [!teoria] La idea en una frase
> Como en electrostática $\nabla\times\vec E=\vec 0$, el campo vectorial $\vec E$ —tres funciones— puede comprimirse en un **único campo escalar** $V$ tal que $\vec E=-\nabla V$. Calcular ese escalar (una integral) y derivar es mucho más barato que atacar $\vec E$ de frente (tres integrales). El potencial, además, traduce la ley de Gauss en una EDP limpia ($\nabla^2V=-\rho/\varepsilon_0$) y conecta el campo con la energía ($U=qV$).

> [!regla] Cuándo usar el potencial
> - **Para calcular $\vec E$ de una distribución conocida** sin simetría suficiente para Gauss: integra $V$ y deriva.
> - **Para problemas con fronteras** (conductores, regiones de carga desconocida): resuelve $\nabla^2V=-\rho/\varepsilon_0$ con condiciones de contorno (ver [[Poisson y Laplace]]).
> - **Para energía y trabajo**: $U=qV$, $W=q\,\Delta V$.
> - Recuerda fijar **una referencia** y trabajar con diferencias.

---

## Resumen

> [!resumen]
> | Concepto | Expresión | Comentario |
> | --- | --- | --- |
> | Definición | $\vec E=-\nabla V$ | $V$ escalar; signo $-$ por convenio |
> | Integral de línea | $V(\vec r)=-\displaystyle\int_{\text{ref}}^{\vec r}\vec E\cdot d\vec l$ | bien definida porque $\oint\vec E\cdot d\vec l=0$ |
> | Existencia | $\nabla\times\vec E=\vec 0\Rightarrow\exists\,V$ | $\vec E$ conservativo (electrostática) |
> | Carga puntual | $V=\dfrac{1}{4\pi\varepsilon_0}\dfrac{q}{r}$ | referencia $V(\infty)=0$ |
> | Distribución | $V=\dfrac{1}{4\pi\varepsilon_0}\displaystyle\int\dfrac{\rho}{\mathscr r}\,d^3r'$ | una integral escalar, no tres |
> | Poisson | $\nabla^2V=-\dfrac{\rho}{\varepsilon_0}$ | Laplace $\nabla^2V=0$ si $\rho=0$ |
> | Energía / trabajo | $U=qV$, $\ W=q\,\Delta V$ | solo diferencias importan |
> | Equipotenciales | $\vec E\perp\{V=\text{cte}\}$ | $\vec E$ hacia $V$ decreciente |
> | Disco (eje) | $V(z)=\dfrac{\sigma}{2\varepsilon_0}\big(\sqrt{R^2+z^2}-\|z\|\big)$ | $E_z=-\partial_z V$ |
>
> **Corolario.** El potencial reduce todo el problema vectorial de la electrostática a un **único escalar** que cumple una EDP de segundo orden; resolverla con las condiciones de frontera adecuadas es el contenido de [[Poisson y Laplace]], y derivar $V$ da el campo de [[Ley de Coulomb y Campo Electrico]] sin nuevas integrales.

> [!referencia]
> Griffiths, *Introduction to Electrodynamics*, cap. 2 (secciones 2.3–2.4). Notas relacionadas: [[2 Electrostatica/index | Electrostática]], [[Ley de Gauss]], [[Poisson y Laplace]], [[Energia Electrostatica]], [[Identidades Vectoriales]], [[Teoremas Integrales]].
