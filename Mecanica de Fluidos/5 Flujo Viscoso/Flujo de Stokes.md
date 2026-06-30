---
title: Flujo de Stokes
order: 4
tags:
  - fluidos
  - teoria
  - flujo-viscoso
draft: false
aliases:
  - Flujo de Stokes
  - Flujo reptante
  - Arrastre de Stokes
---

# Flujo de Stokes $\nabla p=\mu\nabla^2\vec v,\quad F_D=6\pi\mu R U$

> [!definicion]
> El **flujo de Stokes** (o **flujo reptante**, *creeping flow*) es el régimen del flujo viscoso en el que el número de Reynolds es muy pequeño, $\mathrm{Re}=\rho U R/\mu\ll1$. En este límite el **término inercial** de las [[Ecuaciones de Navier-Stokes]] es despreciable frente al **viscoso**, y la ecuación del movimiento se reduce a las **ecuaciones de Stokes**, lineales:
> $$\nabla p=\mu\nabla^2\vec v,\qquad \nabla\cdot\vec v=0.$$
> Su resultado emblemático es el **arrastre de Stokes** sobre una esfera de radio $R$ en un flujo uniforme $U$:
> $$F_D=6\pi\mu R U.$$
> Es el mundo de las bacterias, el polen, la niebla y la microfluídica: dominado por la **viscosidad**, no por la inercia.

---

> [!info]
> **Nota de la sección [[5 Flujo Viscoso/index | Flujo Viscoso]]** (Capítulo 5 del curso Mecánica de Fluidos). Es el límite $\mathrm{Re}\ll1$ del mapa de regímenes; su contraparte de alto Reynolds es la [[Capa Limite]], y el parámetro que separa ambos se construye en [[Numero de Reynolds y Adimensionalizacion]]. **Usa.** Las [[Ecuaciones de Navier-Stokes]] estacionarias como punto de partida. **Hermanas.** [[Numero de Reynolds y Adimensionalizacion]], [[Capa Limite]], [[Soluciones Viscosas Exactas]]. **Referencia.** Landau-Lifshitz, *Mecánica de Fluidos* (Vol. 6), §20.

---

## En qué consiste

A bajo Reynolds la intuición cotidiana del fluido —chapotear, deslizarse, dejar estela— se rompe. La viscosidad es tan dominante que el fluido "olvida" todo movimiento en cuanto cesa el forzamiento: no hay inercia que mantenga las corrientes. Un microorganismo nadando en agua a su escala vive, en términos de $\mathrm{Re}$, como un ser humano nadaría en miel espesa.

### Las ecuaciones de Stokes

> [!teorema] Reducción de Navier–Stokes a $\mathrm{Re}\ll1$
> Para $\mathrm{Re}\ll1$, la ecuación de Navier–Stokes estacionaria e incompresible se reduce a las **ecuaciones de Stokes**
> $$\nabla p=\mu\nabla^2\vec v,\qquad \nabla\cdot\vec v=0,$$
> y la presión es **armónica**: $\nabla^2 p=0$.

> [!demostracion]
> Partimos de la [[Ecuaciones de Navier-Stokes]] estacionaria e incompresible:
> $$\rho(\vec v\cdot\nabla)\vec v=-\nabla p+\mu\nabla^2\vec v.$$
>
> **Paso 1 — Adimensionalizar.** Con las escalas $\vec v=U\vec v^{\,*}$, $\nabla=R^{-1}\nabla^*$ y $p=(\mu U/R)\,p^*$ (escala viscosa de presión, apropiada a bajo $\mathrm{Re}$, [[Numero de Reynolds y Adimensionalizacion]]), el término inercial vale $\rho U^2/R\cdot(\vec v^{\,*}\cdot\nabla^*)\vec v^{\,*}$ y el viscoso vale $\mu U/R^2\cdot\nabla^{*2}\vec v^{\,*}$. Dividiendo todo entre $\mu U/R^2$:
> $$\underbrace{\frac{\rho U R}{\mu}}_{\mathrm{Re}}(\vec v^{\,*}\cdot\nabla^*)\vec v^{\,*}=-\nabla^* p^*+\nabla^{*2}\vec v^{\,*}.$$
>
> **Paso 2 — Tomar el límite.** El término inercial es exactamente $\mathrm{Re}$ veces el viscoso. Como $\mathrm{Re}\ll1$, lo despreciamos. Volviendo a variables dimensionales queda
> $$\nabla p=\mu\nabla^2\vec v,\qquad \nabla\cdot\vec v=0.$$
> El sistema es **lineal** en $(\vec v,p)$: he ahí toda la fuerza del régimen reptante.
>
> **Paso 3 — Presión armónica.** Tomamos la **divergencia** de $\nabla p=\mu\nabla^2\vec v$:
> $$\nabla\cdot(\nabla p)=\mu\,\nabla\cdot(\nabla^2\vec v)=\mu\,\nabla^2(\nabla\cdot\vec v).$$
> El lado izquierdo es $\nabla^2 p$. El derecho contiene $\nabla\cdot\vec v=0$ por incompresibilidad. Por tanto
> $$\nabla^2 p=0. \qquad\blacksquare$$

### Propiedades del flujo reptante

> [!proposicion] Linealidad, reversibilidad e instantaneidad
> Por ser lineales, las ecuaciones de Stokes dotan al flujo reptante de tres rasgos peculiares:
> 1. **Linealidad.** La respuesta es lineal en el forzamiento: si se duplica $U$, se duplican $\vec v$, $p$ y la fuerza $F_D$. No hay términos cuadráticos como $(\vec v\cdot\nabla)\vec v$.
> 2. **Reversibilidad temporal.** Si se invierte el forzamiento ($U\to-U$), el campo se invierte **exactamente** ($\vec v\to-\vec v$, $p\to-p$): sin inercia, el fluido no tiene "memoria". Una gota de tinte deformada por un movimiento se **recompone** al deshacerlo.
> 3. **Instantaneidad.** Sin término temporal dominante, el campo se ajusta de inmediato a las condiciones de contorno actuales: el flujo es **cuasiestático**.

> [!corolario] Teorema de la vieira (*scallop theorem*)
> Como consecuencia de la reversibilidad, **un nadador recíproco no avanza** a $\mathrm{Re}\ll1$. Una vieira que abre y cierra su concha (un único grado de libertad, movimiento recíproco) deshace en el cierre todo el avance del abrir: termina donde empezó. Por eso los microorganismos nadan con **movimientos no recíprocos** —flagelos en forma de sacacorchos, batido coordinado de cilios— que rompen la simetría temporal. (Purcell, *Life at low Reynolds number*.)

---

### Arrastre de Stokes sobre una esfera

Este es el resultado central del régimen. Consideramos una **esfera rígida de radio $R$** inmersa en un fluido viscoso que lejos de ella se mueve con velocidad uniforme $U\hat x$ (equivalente: la esfera se mueve con $-U\hat x$ en fluido en reposo).

> [!teoria] Planteamiento del problema
> Buscamos $(\vec v,p)$ que cumplan las ecuaciones de Stokes con dos **condiciones de contorno**:
> - **No deslizamiento** en la superficie de la esfera: $\vec v=\vec 0$ en $r=R$ (el fluido se pega a la pared).
> - **Flujo uniforme** en el infinito: $\vec v\to U\hat x$ y $p\to p_\infty$ cuando $r\to\infty$.
>
> La solución (axisimétrica, obtenida con la función de corriente de Stokes) da un campo de velocidades cuya perturbación **decae lentamente** como $\sim R/r$ —mucho más lento que en flujo potencial—: la esfera "se siente" a gran distancia. Esa cola larga es la firma de la viscosidad.

> [!proposicion] La forma del arrastre por análisis dimensional
> Antes del cálculo completo se puede **predecir la forma** del resultado. A $\mathrm{Re}\ll1$ la densidad $\rho$ es irrelevante (no hay inercia), así que la fuerza solo puede depender de
> $$F_D=f(\mu,R,U).$$
> Sus dimensiones son $[\mu]=\mathrm{Pa\cdot s}=\mathrm{kg\,m^{-1}s^{-1}}$, $[R]=\mathrm m$, $[U]=\mathrm{m\,s^{-1}}$ y $[F_D]=\mathrm{kg\,m\,s^{-2}}$. El **único** monomio $\mu^a R^b U^c$ con dimensiones de fuerza es $a=b=c=1$:
> $$[\mu R U]=\mathrm{kg\,m^{-1}s^{-1}}\cdot\mathrm m\cdot\mathrm{m\,s^{-1}}=\mathrm{kg\,m\,s^{-2}}=[F_D].$$
> Luego forzosamente $F_D=C\,\mu R U$ con $C$ una **constante numérica adimensional**. El cálculo completo fija $C=6\pi$.

> [!teorema] Ley de arrastre de Stokes
> La fuerza de arrastre sobre la esfera es
> $$\boxed{F_D=6\pi\mu R U.}$$
> De ella, **un tercio** proviene del **arrastre de presión** (la presión empuja más por delante que por detrás) y **dos tercios** del **arrastre de fricción viscosa** (tangencial sobre la superficie):
> $$F_D=\underbrace{2\pi\mu R U}_{\text{presión }(1/3)}+\underbrace{4\pi\mu R U}_{\text{fricción }(2/3)}.$$
> Nótese la **linealidad** en $U$ (no $U^2$ como en alto Reynolds) y la simetría adelante-atrás del flujo: sin desprendimiento ni estela.

![[flujo_stokes.svg|460]]
*Flujo reptante alrededor de una esfera ($\mathrm{Re}\ll1$): las líneas de corriente son simétricas adelante-atrás, sin estela, y la esfera experimenta el arrastre $F_D=6\pi\mu R U$.*

---

### Velocidad terminal de sedimentación

La aplicación más útil de la ley de Stokes: una partícula esférica que cae en un fluido alcanza una **velocidad terminal** constante cuando el arrastre equilibra al peso aparente.

> [!teorema] Velocidad terminal (ley de Stokes para sedimentación)
> Una esfera de radio $R$ y densidad $\rho_s$ que sedimenta en un fluido de densidad $\rho_f$ y viscosidad $\mu$ alcanza la velocidad terminal
> $$\boxed{U_t=\frac{2R^2(\rho_s-\rho_f)\,g}{9\mu}.}$$
> En particular $U_t\propto R^2$: las partículas grandes caen mucho más rápido.

> [!demostracion]
> **Paso 1 — Balance de fuerzas.** En régimen estacionario (velocidad constante) la suma de fuerzas verticales es nula. Sobre la esfera actúan:
> - el **peso** $W=\tfrac43\pi R^3\rho_s\,g$ (hacia abajo),
> - el **empuje** de Arquímedes $E=\tfrac43\pi R^3\rho_f\,g$ (hacia arriba),
> - el **arrastre de Stokes** $F_D=6\pi\mu R U_t$ (hacia arriba, opuesto al movimiento).
>
> El peso aparente (peso menos empuje) se equilibra con el arrastre:
> $$\underbrace{\tfrac43\pi R^3(\rho_s-\rho_f)\,g}_{\text{peso aparente}}=\underbrace{6\pi\mu R U_t}_{\text{arrastre}}.$$
>
> **Paso 2 — Despejar $U_t$.** Cancelamos el factor común $\pi R$:
> $$\tfrac43 R^2(\rho_s-\rho_f)\,g=6\mu U_t
> \;\Longrightarrow\;
> U_t=\frac{4}{3}\cdot\frac{R^2(\rho_s-\rho_f)\,g}{6\mu}=\frac{2R^2(\rho_s-\rho_f)\,g}{9\mu}. \qquad\blacksquare$$

---

## Ejemplo

> [!ejemplo] Velocidad terminal de una gotita de niebla en aire
> Una gotita de agua de radio $R=10\ \mu\mathrm m=1{,}0\times10^{-5}\ \mathrm m$ cae en aire en reposo. Datos: $\rho_s=1\,000\ \mathrm{kg/m^3}$ (agua), $\rho_f=1{,}2\ \mathrm{kg/m^3}$ (aire), $\mu=1{,}8\times10^{-5}\ \mathrm{Pa\cdot s}$ (aire), $g=9{,}8\ \mathrm{m/s^2}$. Halla $U_t$ y comprueba $\mathrm{Re}\ll1$.

> [!solucion]
> **Paso 1 — Aplicar la ley de Stokes.** Como $\rho_f\ll\rho_s$, tomamos $\rho_s-\rho_f\approx998{,}8\ \mathrm{kg/m^3}$:
> $$U_t=\frac{2R^2(\rho_s-\rho_f)g}{9\mu}
> =\frac{2\,(1{,}0\times10^{-5})^2\,(998{,}8)\,(9{,}8)}{9\,(1{,}8\times10^{-5})}.$$
> Numerador: $2\times1{,}0\times10^{-10}\times998{,}8\times9{,}8\approx1{,}957\times10^{-6}$. Denominador: $9\times1{,}8\times10^{-5}=1{,}62\times10^{-4}$.
> $$U_t\approx\frac{1{,}957\times10^{-6}}{1{,}62\times10^{-4}}\approx1{,}2\times10^{-2}\ \mathrm{m/s}=1{,}2\ \mathrm{cm/s}.$$
> La gotita cae a poco más de un centímetro por segundo: la niebla "flota" porque sedimenta despacísimo.
>
> **Paso 2 — Verificar $\mathrm{Re}\ll1$ a posteriori.** Con $\rho=\rho_f=1{,}2\ \mathrm{kg/m^3}$, $U=U_t=1{,}2\times10^{-2}\ \mathrm{m/s}$, $R=1{,}0\times10^{-5}\ \mathrm m$:
> $$\mathrm{Re}=\frac{\rho U R}{\mu}=\frac{1{,}2\times1{,}2\times10^{-2}\times1{,}0\times10^{-5}}{1{,}8\times10^{-5}}\approx8\times10^{-3}.$$
> Como $\mathrm{Re}\approx0{,}008\ll1$, el uso de la ley de Stokes está **plenamente justificado**. $\quad\blacksquare$

> [!warning] Cuándo deja de valer la ley de Stokes
> La ley $F_D=6\pi\mu R U$ y la velocidad terminal $U_t\propto R^2$ valen **solo** para $\mathrm{Re}=\rho U R/\mu\lesssim1$. Para **gotas grandes o rápidas** la inercia deja de ser despreciable: aparecen correcciones (Oseen, y a alto $\mathrm{Re}$ el arrastre pasa a $F_D\propto\rho U^2 R^2$ con estela turbulenta, [[Capa Limite]]). Una gota de lluvia de milímetros **no** sigue Stokes. El régimen reptante es el de lo pequeño y lo lento: bacterias, polen, niebla, microfluídica.

---

## Resumen

> [!resumen]
> | Concepto | Expresión | Observación |
> |:---|:---|:---|
> | Régimen | $\mathrm{Re}=\rho U R/\mu\ll1$ | viscosidad domina; sin inercia |
> | Ecuaciones de Stokes | $\nabla p=\mu\nabla^2\vec v,\ \ \nabla\cdot\vec v=0$ | **lineales** |
> | Presión | $\nabla^2 p=0$ | armónica |
> | Propiedades | linealidad, reversibilidad, instantaneidad | \| sin memoria \| |
> | Microorganismos | teorema de la vieira | nadador recíproco no avanza |
> | Arrastre sobre esfera | $F_D=6\pi\mu R U$ | $1/3$ presión, $2/3$ fricción |
> | Forma dimensional | $F_D\sim\mu R U$ | $\rho$ irrelevante a $\mathrm{Re}\ll1$ |
> | Velocidad terminal | $U_t=\dfrac{2R^2(\rho_s-\rho_f)g}{9\mu}$ | $U_t\propto R^2$ |

> [!corolario] La idea para recordar
> A bajo Reynolds la viscosidad lo gobierna todo: las ecuaciones se **linealizan**, el flujo se vuelve **reversible** y sin estela, y el arrastre crece **linealmente** con la velocidad, $F_D=6\pi\mu R U$ —no como $U^2$—. De ahí sale la sedimentación de Stokes ($U_t\propto R^2$) y la física exótica de los micronadadores. Es el extremo opuesto de la [[Capa Limite]], donde $\mathrm{Re}\gg1$ confina la viscosidad a una franja delgada.

> [!referencia]
> Landau-Lifshitz, *Mecánica de Fluidos* (Vol. 6), §20 (flujo a pequeños números de Reynolds, fórmula de Stokes). Batchelor, *An Introduction to Fluid Dynamics*, §4.9; Acheson, *Elementary Fluid Dynamics*, §7. Purcell, *Life at low Reynolds number*, Am. J. Phys. 45 (1977).
