---
title: Conductores
tags:
  - electromagnetismo
  - teoria
  - electrostatica
draft: false
aliases:
  - Conductores
  - Conductor en equilibrio electrostático
---

# Conductores $\vec E_{\text{int}}=\vec 0,\quad \sigma=\varepsilon_0 E_\perp$

---

> [!definicion] Conductor en equilibrio electrostático
> Un **conductor** es un material que contiene una densidad apreciable de **cargas libres** (los electrones de conducción en un metal) que pueden desplazarse a través de todo su volumen bajo la acción de un campo eléctrico. Se dice que el conductor está en **equilibrio electrostático** cuando, transcurrido un tiempo muy breve tras aplicar las fuentes externas, **ninguna carga se mueve de forma macroscópica**: las cargas se han redistribuido hasta una configuración estacionaria. En ese estado, y en el interior del material conductor,
> $$\boxed{\;\vec E_{\text{int}}=\vec 0\;}$$
> y toda carga neta reside en la **superficie**, con densidad superficial $\sigma$ ligada al campo exterior por
> $$\boxed{\;\sigma=\varepsilon_0\,E_\perp\;}$$
> donde $E_\perp$ es la componente normal del campo justo afuera de la superficie. El conductor es además un **volumen equipotencial** ($V=\text{cte}$) y el campo en su exterior incide **perpendicularmente** a la superficie.

---

> [!info] Ubicación en el curso
> Esta nota pertenece al curso de **Electromagnetismo**, sección [[2 Electrostatica/index | Electrostática]]. Sus notas hermanas son [[Poisson y Laplace]] (las ecuaciones $\nabla^2 V=-\rho/\varepsilon_0$ que gobiernan $V$ en las regiones vacías entre conductores) y [[2 Electrostatica/Dielectricos/index | Dieléctricos]] (el comportamiento dual: materiales que **no** conducen pero se polarizan). La herramienta central para deducir casi todas las propiedades es [[Ley de Gauss]]. Referencia principal: **Griffiths, *Introduction to Electrodynamics*, cap. 2**.

---

## En qué consiste

La física de un conductor en electrostática se resume en una sola idea: **las cargas libres se reacomodan hasta que dejan de sentir fuerza**. Como la fuerza sobre una carga libre es $\vec F=q\,\vec E$, "no sentir fuerza" significa $\vec E=\vec 0$ en el lugar donde están las cargas, es decir, en todo el material. De esta única condición se desprenden, una tras otra, todas las propiedades de la sección [[#Demostraciones de las propiedades]].

Conviene tener clara la imagen mental: ante un campo externo, los electrones de conducción se desplazan en sentido contrario a $\vec E$ acumulándose en una cara y dejando carga positiva descubierta en la opuesta. Esa **carga inducida** crea un campo interno que se opone al externo. El movimiento cesa exactamente cuando los dos campos se cancelan en el interior. El proceso es prácticamente instantáneo (escala de tiempos $\sim 10^{-19}\ \mathrm{s}$ en buenos metales), por lo que en electrostática siempre suponemos ya alcanzado el equilibrio.

> [!teoria] Las seis propiedades del conductor
> 1. $\vec E=\vec 0$ en el interior del material.
> 2. $\rho=0$ en el interior: toda carga neta vive en la superficie.
> 3. El conductor es **equipotencial**: $V=\text{cte}$ en todo el volumen y la superficie.
> 4. Justo afuera, $\vec E$ es **perpendicular** a la superficie.
> 5. La densidad superficial cumple $\sigma=\varepsilon_0\,E_\perp$.
> 6. Una **cavidad vacía** está libre de campo (apantallamiento, jaula de Faraday).

---

## Demostraciones de las propiedades

> [!teorema] $\vec E=\vec 0$ en el interior de un conductor
> En equilibrio electrostático, el campo eléctrico es nulo en todo punto del interior del material conductor.

> [!demostracion]
> **Paso 1 — Hipótesis por reducción al absurdo.** Supongamos que en algún punto interior $\vec E\neq\vec 0$.
>
> **Paso 2 — Consecuencia sobre las cargas libres.** Sobre cada carga libre $q$ (electrón de conducción) actuaría la fuerza $\vec F=q\,\vec E\neq\vec 0$. Como las cargas libres pueden desplazarse sin restricción por el material, comenzarían a moverse, generando una corriente.
>
> **Paso 3 — Contradicción con el equilibrio.** El estado de equilibrio electrostático se define precisamente como aquel en que **no hay movimiento macroscópico de carga**. La existencia de corriente contradice esa hipótesis.
>
> **Paso 4 — Conclusión.** El sistema solo se detiene cuando $\vec E=\vec 0$ en todo punto donde haya cargas libres, esto es, en todo el interior:
> $$\vec E_{\text{int}}=\vec 0.\qquad\blacksquare$$

> [!teorema] $\rho=0$ en el interior; la carga reside en la superficie
> La densidad volumétrica de carga neta es nula en el interior del conductor; cualquier carga neta del cuerpo se distribuye sobre su superficie.

> [!demostracion]
> **Paso 1 — Ley de Gauss diferencial.** En forma diferencial, [[Ley de Gauss]] establece
> $$\nabla\cdot\vec E=\frac{\rho}{\varepsilon_0}.$$
>
> **Paso 2 — Uso de $\vec E=\vec 0$.** En el interior acabamos de probar que $\vec E=\vec 0$ idénticamente, luego también su divergencia es nula:
> $$\nabla\cdot\vec E=0\quad\Longrightarrow\quad \frac{\rho}{\varepsilon_0}=0\quad\Longrightarrow\quad \rho=0.$$
>
> **Paso 3 — Localización de la carga.** El razonamiento solo es válido en puntos **interiores**, donde $\vec E=\vec 0$. La discontinuidad del campo (de $\vec 0$ a un valor no nulo) ocurre en la superficie, único lugar donde puede alojarse carga neta. Si el conductor tiene carga total $Q$, ésta reside en la superficie con densidad $\sigma$. $\qquad\blacksquare$

> [!teorema] El conductor es equipotencial y $\vec E\perp$ superficie
> El potencial $V$ toma el mismo valor en todo el conductor (volumen y superficie), y el campo eléctrico inmediatamente exterior es perpendicular a la superficie.

> [!demostracion]
> **Paso 1 — Equipotencialidad.** El potencial entre dos puntos cualesquiera $A$ y $B$ del conductor se obtiene de [[Potencial Electrico]]:
> $$V_B-V_A=-\int_A^B \vec E\cdot d\vec\ell.$$
> Tomando un camino que vaya íntegramente por el interior, donde $\vec E=\vec 0$, la integral se anula:
> $$V_B-V_A=0\quad\Longrightarrow\quad V_A=V_B.$$
> Como $A$ y $B$ son arbitrarios, $V=\text{cte}$ en todo el conductor. En particular, **la superficie es una equipotencial**.
>
> **Paso 2 — Perpendicularidad.** Sobre la superficie descompongamos el campo exterior en una parte tangencial $\vec E_\parallel$ y una normal $\vec E_\perp\hat n$. Si existiera $\vec E_\parallel\neq\vec 0$, ejercería fuerza tangente sobre las cargas superficiales (también libres), que se desplazarían a lo largo de la superficie: de nuevo se rompería el equilibrio.
>
> **Paso 3 — Conclusión.** Por tanto $\vec E_\parallel=\vec 0$ y el campo justo afuera solo tiene componente normal:
> $$\vec E_{\text{ext}}=E_\perp\,\hat n.\qquad\blacksquare$$

> [!teorema] Carga superficial inducida $\sigma=\varepsilon_0 E_\perp$
> La densidad superficial de carga de un conductor en equilibrio está relacionada con el campo justo afuera por $\sigma=\varepsilon_0\,E_\perp$.

> [!demostracion]
> **Paso 1 — Superficie gaussiana tipo pastilla.** Construyamos una **pastilla** (pillbox) cilíndrica muy chata de área de base $A$, atravesando la superficie del conductor: una cara dentro del metal y la otra justo afuera, con altura $\to 0$.
>
> **Paso 2 — Flujo cara interior.** La cara interior está en el metal, donde $\vec E=\vec 0$; su flujo es nulo.
>
> **Paso 3 — Flujo cara exterior y lateral.** La cara exterior tiene $\vec E=E_\perp\hat n$, paralelo a su normal, con flujo $E_\perp A$. La superficie lateral, de altura despreciable, no aporta flujo.
>
> **Paso 4 — Ley de Gauss.** La carga encerrada es $\sigma A$. Igualando flujo y carga,
> $$\oint \vec E\cdot d\vec A = E_\perp A = \frac{\sigma A}{\varepsilon_0}.$$
>
> **Paso 5 — Conclusión.** Cancelando $A$,
> $$\sigma=\varepsilon_0\,E_\perp,\qquad\text{equivalentemente}\qquad E_\perp=\frac{\sigma}{\varepsilon_0}.\qquad\blacksquare$$

> [!warning] Efecto punta
> La densidad superficial $\sigma$ **no es uniforme**: se acumula más carga donde la superficie es más **curva** (puntas, aristas) y menos donde es plana. Como $E_\perp=\sigma/\varepsilon_0$, el campo justo afuera es **mucho mayor en las puntas**. Por eso los pararrayos terminan en punta (el campo intenso ioniza el aire y descarga el rayo) y por eso los conductores de alta tensión se rematan con superficies redondeadas para evitar la descarga corona.

---

## Cavidades

> [!teorema] Cavidad vacía: apantallamiento (jaula de Faraday)
> Si dentro de un conductor hay una **cavidad sin carga**, el campo eléctrico es nulo en toda la cavidad, sea cual sea el campo aplicado desde el exterior.

> [!demostracion]
> **Paso 1 — Equipotencialidad de la pared.** Toda la pared de la cavidad pertenece al conductor, que es equipotencial: la pared está a un único potencial $V_0$.
>
> **Paso 2 — No pueden nacer líneas de campo en la cavidad.** Supongamos, por absurdo, que $\vec E\neq\vec 0$ en algún punto de la cavidad. Las líneas de campo no pueden cerrarse sobre sí mismas en electrostática (el campo es conservativo, $\nabla\times\vec E=\vec 0$), ni pueden nacer/morir en el vacío de la cavidad (allí $\rho=0$, $\nabla\cdot\vec E=0$). Por tanto una línea de campo tendría que **empezar y terminar en la pared**.
>
> **Paso 3 — Contradicción energética.** Recorriendo esa línea de campo de un extremo a otro de la pared,
> $$V_{\text{fin}}-V_{\text{inicio}}=-\int \vec E\cdot d\vec\ell < 0,$$
> pues $\vec E$ y $d\vec\ell$ son paralelos a lo largo de una línea de campo. Pero ambos extremos están en la pared, donde $V=V_0$, así que esa diferencia debe ser **cero**. Contradicción.
>
> **Paso 4 — Vía unicidad.** Formalmente: en la cavidad $V$ satisface la [[Poisson y Laplace | ecuación de Laplace]] $\nabla^2V=0$ con condición de contorno $V=V_0$ en toda la pared. La solución es única y es $V=V_0$ constante, luego $\vec E=-\nabla V=\vec 0$.
>
> **Paso 5 — Conclusión.** El interior de la cavidad está **apantallado** del exterior: $\vec E=\vec 0$. Esto es la **jaula de Faraday**. $\qquad\blacksquare$

> [!teorema] Carga $q$ dentro de una cavidad
> Si se coloca una carga puntual $q$ dentro de la cavidad de un conductor neutro, la pared de la cavidad adquiere una carga inducida $-q$ y la superficie exterior del conductor adquiere $+q$.

> [!demostracion]
> **Paso 1 — Gauss en una superficie dentro del metal.** Rodeamos la cavidad con una superficie gaussiana $S$ trazada **íntegramente por el interior del material** conductor. Allí $\vec E=\vec 0$, de modo que
> $$\oint_S \vec E\cdot d\vec A=0=\frac{Q_{\text{enc}}}{\varepsilon_0}\quad\Longrightarrow\quad Q_{\text{enc}}=0.$$
>
> **Paso 2 — Carga inducida en la pared.** La carga encerrada por $S$ es la suma de la carga $q$ y la carga $q_{\text{pared}}$ depositada en la pared de la cavidad:
> $$Q_{\text{enc}}=q+q_{\text{pared}}=0\quad\Longrightarrow\quad q_{\text{pared}}=-q.$$
>
> **Paso 3 — Conservación de la carga.** El conductor es neutro en total. Si en la pared interior hay $-q$, en la **superficie exterior** debe haber su opuesto para que la suma sea cero:
> $$q_{\text{ext}}=+q.$$
>
> **Paso 4 — Campo exterior.** La superficie exterior "olvida" la posición de $q$ dentro de la cavidad: por ser el conductor equipotencial, $q_{\text{ext}}=+q$ se distribuye en la superficie exterior **según la forma de ésta**, no según dónde esté $q$. Si el conductor exterior es una esfera, el campo afuera es el de una carga $+q$ centrada, $\vec E=\dfrac{q}{4\pi\varepsilon_0 r^2}\hat r$, **independientemente** de la posición de $q$ en la cavidad. $\qquad\blacksquare$

---

## Presión electrostática

> [!proposicion] Presión sobre la superficie de un conductor
> Cada elemento de la superficie de un conductor cargado sufre una fuerza por unidad de área dirigida hacia afuera de valor
> $$P=\frac{\sigma^2}{2\varepsilon_0}=\frac{\varepsilon_0}{2}\,E^2.$$

> [!demostracion]
> **Paso 1 — Campo que actúa sobre $\sigma$.** El campo total justo afuera es $E=\sigma/\varepsilon_0$, pero un elemento de superficie **no puede ejercer fuerza sobre sí mismo**. El campo que actúa sobre el parche es el creado por el **resto** de la distribución, $E_{\text{otros}}$.
>
> **Paso 2 — Descomposición.** Cerca del parche, el campo total es la suma del campo del propio parche ($\sigma/2\varepsilon_0$ a cada lado, apuntando hacia afuera del parche) y el del resto:
> - Afuera: $E_{\text{otros}}+\dfrac{\sigma}{2\varepsilon_0}=\dfrac{\sigma}{\varepsilon_0}$.
> - Adentro (en el metal): $E_{\text{otros}}-\dfrac{\sigma}{2\varepsilon_0}=0$.
>
> **Paso 3 — Despejar $E_{\text{otros}}$.** Sumando ambas o despejando de cualquiera,
> $$E_{\text{otros}}=\frac{\sigma}{2\varepsilon_0}.$$
>
> **Paso 4 — Fuerza por unidad de área.** La fuerza sobre el parche es la carga $\sigma\,dA$ por el campo del resto:
> $$P=\frac{dF}{dA}=\sigma\,E_{\text{otros}}=\sigma\cdot\frac{\sigma}{2\varepsilon_0}=\frac{\sigma^2}{2\varepsilon_0}=\frac{\varepsilon_0}{2}E^2.$$
> La presión es siempre **hacia afuera** (tiende a hinchar el conductor), independientemente del signo de $\sigma$. $\qquad\blacksquare$

---

## Ejemplo

> [!ejemplo] Carga $q$ en el centro de una cavidad esférica de un conductor neutro
> Un conductor esférico **neutro** tiene radio exterior $b$ y una cavidad esférica concéntrica de radio $a$ ($a<b$). En el centro se coloca una carga puntual $q$. Determina:
> 1. La densidad superficial $\sigma$ en la pared de la cavidad ($r=a$) y en la superficie exterior ($r=b$).
> 2. El campo eléctrico $\vec E$ en las tres regiones: $r<a$, $a<r<b$ y $r>b$.

> [!solucion]
> **Paso 1 — Carga inducida en cada superficie.** Por el teorema de la carga en la cavidad, la pared interior adquiere $-q$ y, por neutralidad del conductor, la superficie exterior adquiere $+q$.
>
> **Paso 2 — Densidades superficiales.** Por simetría esférica las cargas se reparten uniformemente:
> $$\sigma_a=\frac{-q}{4\pi a^2},\qquad \sigma_b=\frac{+q}{4\pi b^2}.$$
> Nótese que $\sigma_a<0$ (carga inducida negativa atraída por $q$) y $\sigma_b>0$.
>
> **Paso 3 — Región $r<a$ (cavidad).** Aplicando [[Ley de Gauss]] a una esfera de radio $r<a$, la carga encerrada es solo $q$:
> $$E\,(4\pi r^2)=\frac{q}{\varepsilon_0}\quad\Longrightarrow\quad \vec E=\frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\,\hat r.$$
>
> **Paso 4 — Región $a<r<b$ (metal).** Estamos dentro del material conductor:
> $$\vec E=\vec 0.$$
> Comprobación por Gauss: la esfera de radio $r$ encierra $q+(-q)=0$. Coherente.
>
> **Paso 5 — Región $r>b$ (exterior).** La esfera de radio $r>b$ encierra $q+(-q)+(+q)=q$:
> $$E\,(4\pi r^2)=\frac{q}{\varepsilon_0}\quad\Longrightarrow\quad \vec E=\frac{1}{4\pi\varepsilon_0}\frac{q}{r^2}\,\hat r.$$
> El campo exterior es **idéntico** al de una carga puntual $q$ en el centro: el conductor apantalla los detalles internos pero no la carga neta encerrada.

![[conductor_cavidad.svg|420]]
> **Figura.** Conductor con una carga $+q$ alojada en una cavidad. En la pared de la cavidad se induce $-q$, en la superficie exterior aparece $+q$, y en el espesor del metal $\vec E=\vec 0$. El campo exterior es el de una carga $+q$ centrada, sin memoria de la posición exacta de $q$ dentro de la cavidad.

---

## Resumen

> [!resumen] Conductor en equilibrio electrostático
>
> | Propiedad | Enunciado | Origen |
> |---|---|---|
> | Campo interior | $\vec E_{\text{int}}=\vec 0$ | Las cargas libres se mueven hasta anularlo |
> | Carga volumétrica | $\rho=0$ dentro | Gauss: $\nabla\cdot\vec E=\rho/\varepsilon_0=0$ |
> | Ubicación de la carga | toda en la superficie | consecuencia de $\rho=0$ |
> | Potencial | $V=\text{cte}$ (equipotencial) | $V_B-V_A=-\int\vec E\cdot d\vec\ell=0$ |
> | Campo exterior | $\vec E\perp$ superficie | $\vec E_\parallel$ movería carga |
> | Carga superficial | $\sigma=\varepsilon_0 E_\perp$ | Gauss en una pastilla |
> | Cavidad vacía | $\vec E=\vec 0$ adentro | unicidad / apantallamiento |
> | Carga $q$ en cavidad | $-q$ en pared, $+q$ afuera | Gauss en el metal + conservación |
> | Presión | $P=\dfrac{\sigma^2}{2\varepsilon_0}=\dfrac{\varepsilon_0}{2}E^2$ | campo del resto $\times\,\sigma$ |
>
> El campo en las puntas crece como $1/\text{radio de curvatura}$ (**efecto punta**).

> [!corolario] Lectura geométrica
> Un conductor "absorbe" en su superficie justo la carga inducida necesaria para volver nulo el campo en su interior. Para el observador exterior, una cavidad con carga $q$ y un conductor con carga superficial $+q$ son indistinguibles: solo importa la **carga neta encerrada** y la **forma de la superficie externa**. Esto convierte a los conductores en el ingrediente de los problemas de contorno de [[Poisson y Laplace]] y en la base de los **condensadores**.

> [!referencia] Para profundizar
> - **Griffiths**, *Introduction to Electrodynamics*, cap. 2 (Conductores, §2.5).
> - Notas relacionadas: [[Ley de Gauss]], [[Potencial Electrico]], [[Poisson y Laplace]], [[2 Electrostatica/Dielectricos/index | Dieléctricos]].
