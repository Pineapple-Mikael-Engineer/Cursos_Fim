---
title: Desplazamiento Eléctrico
order: 2
tags:
  - electromagnetismo
  - teoria
  - dielectricos
draft: false
aliases:
  - Desplazamiento eléctrico
  - Campo D
  - Permitividad
---

# Desplazamiento Eléctrico $\vec D=\varepsilon_0\vec E+\vec P,\quad \nabla\cdot\vec D=\rho_{\text{libre}}$

> [!definicion]
> El **desplazamiento eléctrico** $\vec D$ es el campo auxiliar
> $$\vec D=\varepsilon_0\vec E+\vec P,$$
> combinación del campo total $\vec E$ y de la polarización $\vec P$ del medio. Su rasgo característico es que **su fuente es únicamente la carga libre**: la carga ligada queda absorbida dentro de $\vec D$. Por eso satisface una **ley de Gauss limpia**, sin cargas inducidas,
> $$\nabla\cdot\vec D=\rho_{\text{libre}}\qquad\Longleftrightarrow\qquad \oint_S\vec D\cdot d\vec A=Q_{\text{libre,enc}}.$$
>
> En **medios lineales** la relación con $\vec E$ es proporcional, $\vec D=\varepsilon\,\vec E$, con $\varepsilon=\varepsilon_0\varepsilon_r$ la **permitividad** del material y $\varepsilon_r=1+\chi_e$ la **constante dieléctrica**. Unidades SI: $[\vec D]=[\vec P]=\text{C}/\text{m}^2$, mientras que $[\vec E]=\text{V}/\text{m}$ y $[\varepsilon]=\text{C}^2/(\text{N}\cdot\text{m}^2)$.

---

> [!info]
> **Nota de la subsección [[2 Electrostatica/Dielectricos/index | Dieléctricos]]**, dentro del capítulo [[2 Electrostatica/index | Electrostática]] (curso Electromagnetismo). Es **hermana** de [[2 Electrostatica/Dielectricos/Polarizacion | Polarización]] —de donde tomamos la carga ligada $\rho_b=-\nabla\cdot\vec P$, ingrediente clave de la deducción— y prolonga la [[Ley de Gauss]] del vacío a la materia, reemplazando $\vec E$ por $\vec D$ y $\rho$ por $\rho_{\text{libre}}$. **Referencia.** Griffiths, *Introduction to Electrodynamics*, cap. 4. Unidades SI; $\varepsilon_0=8{,}854\times10^{-12}\ \text{C}^2/(\text{N}\cdot\text{m}^2)$.

---

## Ley de Gauss para $\vec D$

> [!teoria] La idea: separar la carga que controlamos de la que no
> En un dieléctrico hay dos clases de carga. La **libre** $\rho_{\text{libre}}$ —la que ponemos a mano en placas, electrodos o por inyección— y la **ligada** $\rho_b$ —los extremos de los dipolos polarizados, que no controlamos porque dependen del propio campo—. La ley de Gauss usual $\nabla\cdot\vec E=\rho/\varepsilon_0$ las mezcla a las dos. La maniobra consiste en **mover la carga ligada al otro lado de la ecuación** y empaquetarla junto a $\vec E$ en un nuevo campo $\vec D$, de manera que la fuente que queda a la vista sea solo $\rho_{\text{libre}}$.

> [!demostracion] De la ley de Gauss para $\vec E$ a la ley para $\vec D$
> **Paso 1 — Partir de Gauss con la carga total.** La forma diferencial de la [[Ley de Gauss]] es exacta para el campo total $\vec E$ y la **carga total** $\rho$:
> $$\nabla\cdot\vec E=\frac{\rho}{\varepsilon_0}\qquad\Longrightarrow\qquad \varepsilon_0\,\nabla\cdot\vec E=\rho.$$
>
> **Paso 2 — Descomponer la carga total.** Toda la carga del medio es la suma de la libre y la ligada:
> $$\rho=\rho_{\text{libre}}+\rho_b,\qquad \rho_b=-\,\nabla\cdot\vec P,$$
> donde la expresión de $\rho_b$ se deduce en [[2 Electrostatica/Dielectricos/Polarizacion | Polarización]] (la divergencia de la polarización es, salvo signo, la densidad de carga ligada). Sustituyendo:
> $$\varepsilon_0\,\nabla\cdot\vec E=\rho_{\text{libre}}-\nabla\cdot\vec P.$$
>
> **Paso 3 — Reunir las divergencias.** Pasamos el término $-\nabla\cdot\vec P$ a la izquierda y usamos la linealidad del operador divergencia, $\nabla\cdot\vec a+\nabla\cdot\vec b=\nabla\cdot(\vec a+\vec b)$:
> $$\varepsilon_0\,\nabla\cdot\vec E+\nabla\cdot\vec P=\rho_{\text{libre}}\qquad\Longrightarrow\qquad \nabla\cdot\big(\varepsilon_0\vec E+\vec P\big)=\rho_{\text{libre}}.$$
>
> **Paso 4 — Bautizar el campo.** Definimos el desplazamiento eléctrico como el contenido del paréntesis,
> $$\boxed{\;\vec D=\varepsilon_0\vec E+\vec P\;},$$
> con lo cual la ecuación anterior se lee
> $$\boxed{\;\nabla\cdot\vec D=\rho_{\text{libre}}\;}.$$
> La carga ligada **desapareció** de la fuente: quedó absorbida en $\vec D$. $\blacksquare$

> [!corolario] Forma integral
> Integrando $\nabla\cdot\vec D=\rho_{\text{libre}}$ sobre un volumen $V$ encerrado por la superficie $S$ y aplicando el **teorema de la divergencia** $\displaystyle\int_V\nabla\cdot\vec D\,dV=\oint_S\vec D\cdot d\vec A$:
> $$\oint_S\vec D\cdot d\vec A=\int_V\rho_{\text{libre}}\,dV=Q_{\text{libre,enc}}.$$
> El **flujo de $\vec D$** a través de una superficie cerrada cuenta exactamente la **carga libre encerrada**, ignorando por completo la carga ligada. Esta es la herramienta práctica: con simetría suficiente, despeja $\vec D$ sabiendo solo dónde está la carga que pusimos nosotros.

---

## Medios lineales y permitividad

> [!proposicion] En un dieléctrico lineal, $\vec D=\varepsilon\vec E$
> Un medio es **lineal, isótropo y homogéneo** (l.i.h.) cuando la polarización responde de forma proporcional al campo:
> $$\vec P=\varepsilon_0\,\chi_e\,\vec E,$$
> con $\chi_e$ la **susceptibilidad eléctrica** (adimensional, $\chi_e\ge 0$, constante en el material). Entonces $\vec D$ y $\vec E$ son proporcionales.

> [!demostracion] Cálculo de la permitividad
> **Paso 1 — Sustituir $\vec P$ en la definición.** Partimos de $\vec D=\varepsilon_0\vec E+\vec P$ e insertamos $\vec P=\varepsilon_0\chi_e\vec E$:
> $$\vec D=\varepsilon_0\vec E+\varepsilon_0\chi_e\vec E.$$
>
> **Paso 2 — Factorizar $\varepsilon_0\vec E$.** Como ambos términos comparten $\varepsilon_0\vec E$:
> $$\vec D=\varepsilon_0\,(1+\chi_e)\,\vec E.$$
>
> **Paso 3 — Definir la permitividad y la constante dieléctrica.** Llamamos
> $$\varepsilon\equiv\varepsilon_0(1+\chi_e),\qquad \varepsilon_r\equiv\frac{\varepsilon}{\varepsilon_0}=1+\chi_e,$$
> de modo que
> $$\boxed{\;\vec D=\varepsilon\,\vec E=\varepsilon_0\varepsilon_r\,\vec E\;},\qquad \varepsilon_r=1+\chi_e\ge 1.$$
> El número $\varepsilon_r$ es la **constante dieléctrica** (o permitividad relativa): vale $1$ en el vacío y crece con la "polarizabilidad" del medio (agua $\approx 80$, vidrio $\approx 5$). $\blacksquare$

> [!corolario] El campo se reduce por $\varepsilon_r$
> En un medio l.i.h. con la **misma carga libre** que en el vacío, $\vec D$ es idéntico (solo depende de $\rho_{\text{libre}}$), pero el campo se obtiene dividiendo por $\varepsilon$ en vez de por $\varepsilon_0$:
> $$\vec E=\frac{\vec D}{\varepsilon}=\frac{1}{\varepsilon_r}\,\frac{\vec D}{\varepsilon_0}.$$
> Es decir, **el campo dentro del dieléctrico es $\varepsilon_r$ veces menor** que el que produciría la misma carga libre en el vacío. La carga ligada se opone al campo externo y lo apantalla parcialmente; nunca lo anula (eso solo pasa en [[Conductores]], donde $\varepsilon_r\to\infty$ en cierto sentido).

---

## Condiciones de frontera

> [!teoria] Qué pasa al cruzar una interfase
> En la superficie que separa dos medios (o un medio y el vacío), $\vec D$ y $\vec E$ pueden saltar. Las dos ecuaciones fundamentales —$\nabla\cdot\vec D=\rho_{\text{libre}}$ y $\nabla\times\vec E=\vec 0$— fijan **qué componente es continua y cuál salta**. Demostremos ambas con los argumentos estándar de pastilla y lazo.

> [!demostracion] (a) La componente normal de $\vec D$ salta con la carga libre superficial
> **Paso 1 — Pastilla de Gauss.** Construimos una caja (pastilla) muy delgada que atraviesa la interfase, con tapas de área $A$ paralelas a la superficie —una arriba, otra abajo— y altura $\to 0$. Aplicamos la forma integral $\oint\vec D\cdot d\vec A=Q_{\text{libre,enc}}$.
>
> **Paso 2 — Anular la pared lateral.** Al hacer la altura tender a cero, el flujo por la pared lateral se anula (su área $\to 0$). Solo contribuyen las dos tapas, con normales **opuestas** $+\hat n$ (arriba) y $-\hat n$ (abajo):
> $$\oint\vec D\cdot d\vec A=\big(D_\perp^{\text{arriba}}-D_\perp^{\text{abajo}}\big)\,A,$$
> donde $D_\perp=\vec D\cdot\hat n$ es la componente normal.
>
> **Paso 3 — Carga libre encerrada.** La única carga libre dentro de la pastilla es la superficial sobre $A$: $Q_{\text{libre,enc}}=\sigma_{\text{libre}}\,A$.
>
> **Paso 4 — Igualar y cancelar $A$.** Igualando y dividiendo por $A$:
> $$\boxed{\;D_\perp^{\text{arriba}}-D_\perp^{\text{abajo}}=\sigma_{\text{libre}}\;}.$$
> La componente normal de $\vec D$ es continua **si no hay carga libre** en la interfase. $\blacksquare$

> [!demostracion] (b) La componente tangencial de $\vec E$ es continua
> **Paso 1 — Lazo amperiano.** Tomamos un rectángulo (lazo) delgado que cruza la interfase, con lados largos de longitud $\ell$ paralelos a la superficie —uno arriba, otro abajo— y lados cortos $\to 0$. La electrostática cumple $\nabla\times\vec E=\vec 0$, luego por el teorema de Stokes la **circulación** es nula:
> $$\oint\vec E\cdot d\vec l=0.$$
>
> **Paso 2 — Anular los lados cortos.** Con los lados cortos $\to 0$, solo contribuyen los dos lados largos, recorridos en sentidos **opuestos**:
> $$\oint\vec E\cdot d\vec l=\big(E_\parallel^{\text{arriba}}-E_\parallel^{\text{abajo}}\big)\,\ell,$$
> con $E_\parallel$ la componente tangente a la superficie.
>
> **Paso 3 — Igualar a cero y cancelar $\ell$.**
> $$\big(E_\parallel^{\text{arriba}}-E_\parallel^{\text{abajo}}\big)\,\ell=0\qquad\Longrightarrow\qquad \boxed{\;E_\parallel^{\text{arriba}}=E_\parallel^{\text{abajo}}\;}.$$
> La componente tangencial de $\vec E$ **siempre** es continua. $\blacksquare$

> [!regla] Resumen de fronteras
> - **Normal:** salta $\vec D$ con la carga **libre** superficial: $D_\perp^{\text{arr}}-D_\perp^{\text{ab}}=\sigma_{\text{libre}}$.
> - **Tangencial:** es continuo $\vec E$: $E_\parallel^{\text{arr}}=E_\parallel^{\text{ab}}$.
>
> (Para $\vec E$ normal y $\vec D$ tangencial los saltos involucran también carga ligada, por eso se prefiere esta pareja "limpia".)

---

## Ejemplo

> [!ejemplo] Condensador de placas planas relleno de dieléctrico
> Dos placas paralelas de área $A$ separadas una distancia $d$, con **carga libre** uniforme $\pm\sigma$ en ellas. El hueco está lleno de un dieléctrico l.i.h. de constante $\varepsilon_r$. Hallar $\vec D$, $\vec E$, la capacidad $C$ y la carga ligada $\sigma_b$ en las caras del dieléctrico.
>
> ![[condensador_dielectrico.svg|440]]
> *Condensador con dieléctrico: carga libre $\pm\sigma$ en las placas y carga ligada $\mp\sigma_b$ en las caras del dieléctrico. La carga ligada se opone a la libre, dejando una carga neta menor y un campo $E=\sigma/(\varepsilon_r\varepsilon_0)$ reducido por $\varepsilon_r$ frente al vacío.*

> [!solucion]
> **Paso 1 — Hallar $\vec D$ por Gauss (simetría plana).** Lejos de los bordes el campo es uniforme y perpendicular a las placas. Tomamos una pastilla gaussiana con una tapa dentro del conductor (donde $\vec D=\vec 0$) y la otra en el dieléctrico, de área $A_g$. El flujo de $\vec D$ atraviesa solo la tapa interior, y la carga libre encerrada es $\sigma A_g$:
> $$\oint\vec D\cdot d\vec A=D\,A_g=\sigma\,A_g\qquad\Longrightarrow\qquad D=\sigma.$$
> El desplazamiento vale lo mismo que con vacío entre placas: solo depende de la carga libre.
>
> **Paso 2 — Obtener $\vec E$ con la relación lineal.** Como $\vec D=\varepsilon\vec E$ con $\varepsilon=\varepsilon_r\varepsilon_0$:
> $$E=\frac{D}{\varepsilon}=\frac{\sigma}{\varepsilon_r\varepsilon_0}=\frac{1}{\varepsilon_r}\cdot\frac{\sigma}{\varepsilon_0}.$$
> El campo es $\varepsilon_r$ **veces menor** que el del condensador en vacío ($E_0=\sigma/\varepsilon_0$).
>
> **Paso 3 — Voltaje y capacidad.** La diferencia de potencial es $V=E\,d=\dfrac{\sigma d}{\varepsilon_r\varepsilon_0}$, y con carga total $Q=\sigma A$:
> $$C=\frac{Q}{V}=\frac{\sigma A}{\sigma d/(\varepsilon_r\varepsilon_0)}=\varepsilon_r\,\frac{\varepsilon_0 A}{d}=\varepsilon_r\,C_0.$$
> La capacidad **crece** por el factor $\varepsilon_r$: $\;\boxed{C=\varepsilon_r C_0}$. El dieléctrico reduce el campo a carga fija, baja el voltaje y por tanto permite almacenar más carga al mismo voltaje.
>
> **Paso 4 — Carga ligada en la cara del dieléctrico.** Necesitamos $\vec P$. De $\vec P=\varepsilon_0\chi_e\vec E$ con $\chi_e=\varepsilon_r-1$:
> $$P=\varepsilon_0(\varepsilon_r-1)\,E=\varepsilon_0(\varepsilon_r-1)\,\frac{\sigma}{\varepsilon_r\varepsilon_0}=\sigma\,\frac{\varepsilon_r-1}{\varepsilon_r}.$$
> En la cara del dieléctrico la carga ligada superficial es $\sigma_b=\vec P\cdot\hat n=P$ (la normal saliente del dieléctrico apunta hacia la placa positiva en sentido contrario a $\vec P$, dejando signo opuesto al de $\sigma$):
> $$\boxed{\;\sigma_b=\sigma\,\frac{\varepsilon_r-1}{\varepsilon_r}=\sigma\Big(1-\tfrac{1}{\varepsilon_r}\Big)\;}.$$
>
> **Verificación.** La carga **neta** sobre la cara junto a la placa $+$ es $\sigma-\sigma_b=\sigma/\varepsilon_r$, y produce un campo $E=(\sigma/\varepsilon_r)/\varepsilon_0=\sigma/(\varepsilon_r\varepsilon_0)$, que coincide con el Paso 2. La carga ligada apantalla justo la fracción $1-1/\varepsilon_r$ de la carga libre. $\blacksquare$

---

## En qué consiste

> [!resumen] Lectura física
> El campo $\vec D$ es un **truco contable**, no un campo "más fundamental" que $\vec E$. La física la lleva $\vec E$ (es el que ejerce fuerza, $\vec F=q\vec E$, y el que tiene rotacional nulo en electrostática). Pero $\vec E$ tiene como fuente *toda* la carga, incluida la ligada que no conocemos de antemano. Empaquetando $\varepsilon_0\vec E+\vec P$ en $\vec D$, conseguimos un campo cuya **única fuente es la carga libre**, la que manipulamos. Así, siempre que haya simetría suficiente (plana, cilíndrica, esférica), la ley de Gauss para $\vec D$ da $\vec D$ de inmediato a partir de $\rho_{\text{libre}}$; luego $\vec E=\vec D/\varepsilon$ recupera el campo físico, reducido por $\varepsilon_r$.

> [!warning] $\vec D$ no es conservativo y Gauss no siempre basta
> Cuidado con dos abusos frecuentes:
> - **$\vec D$ no es, en general, irrotacional.** Como $\vec D=\varepsilon_0\vec E+\vec P$ y $\nabla\times\vec E=\vec 0$ en electrostática,
> $$\nabla\times\vec D=\nabla\times\vec P,$$
> que **no tiene por qué anularse** (depende de la geometría de $\vec P$). Por eso $\vec D$ **no deriva de un potencial** ni es conservativo salvo casos especiales (medio l.i.h. con cargas libres apropiadas).
> - **Gauss para $\vec D$ no es magia.** Igual que con $\vec E$, $\oint\vec D\cdot d\vec A=Q_{\text{libre,enc}}$ solo permite **despejar** $\vec D$ cuando hay **simetría suficiente** que lo haga constante y paralelo sobre la gaussiana. Sin simetría, la ecuación sigue siendo cierta, pero no basta para hallar $\vec D$.

---

## Resumen

| Concepto | Expresión | Comentario |
| --- | --- | --- |
| Definición | $\vec D=\varepsilon_0\vec E+\vec P$ | Campo total más polarización |
| Gauss diferencial | $\nabla\cdot\vec D=\rho_{\text{libre}}$ | Solo carga libre como fuente |
| Gauss integral | $\oint_S\vec D\cdot d\vec A=Q_{\text{libre,enc}}$ | Despeja $\vec D$ si hay simetría |
| Medio lineal | $\vec D=\varepsilon\vec E,\ \ \varepsilon=\varepsilon_0\varepsilon_r$ | $\varepsilon_r=1+\chi_e$ (constante dieléctrica) |
| Reducción del campo | $\vec E=\vec D/\varepsilon=\dfrac{1}{\varepsilon_r}\,\vec D/\varepsilon_0$ | Campo $\varepsilon_r$ veces menor que en vacío |
| Frontera normal | $D_\perp^{\text{arr}}-D_\perp^{\text{ab}}=\sigma_{\text{libre}}$ | Salta con carga libre superficial |
| Frontera tangencial | $E_\parallel^{\text{arr}}=E_\parallel^{\text{ab}}$ | $\vec E$ tangencial siempre continuo |
| Rotacional | $\nabla\times\vec D=\nabla\times\vec P$ | $\vec D$ no es conservativo en general |
| Condensador | $C=\varepsilon_r C_0,\ \ \sigma_b=\sigma\!\left(1-\tfrac1{\varepsilon_r}\right)$ | El dieléctrico aumenta la capacidad |

> [!corolario] Idea para recordar
> $\vec D$ ve **solo la carga libre**; $\vec E$ ve **toda** la carga. En un dieléctrico lineal son proporcionales, $\vec D=\varepsilon\vec E$, y el campo físico queda **apantallado** por el factor $\varepsilon_r$. Esa atenuación es lo que hace que un condensador con dieléctrico guarde más carga.

> [!referencia]
> Griffiths, *Introduction to Electrodynamics*, cap. 4 (secciones sobre $\vec D$, medios lineales y condiciones de frontera). Para la pareja $(\vec E,\vec D)$ en electrodinámica y ondas en medios: Jackson, cap. 4; Landau & Lifshitz, *Electrodynamics of Continuous Media* (vol. 8).
