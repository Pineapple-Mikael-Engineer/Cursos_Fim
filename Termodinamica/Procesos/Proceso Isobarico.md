---
title: Proceso Isobárico
tags:
  - termodinamica
  - teoria
  - procesos
draft: false
aliases:
  - Proceso isobárico
  - Proceso a presión constante
---

# Proceso Isobárico $P=\text{cte},\quad q_p=\Delta h$

> [!definicion]
> Un **proceso isobárico** es aquel en que la **presión permanece constante** durante toda la trayectoria, $P_1=P_2=P=\text{cte}$. En el plano $P$–$v$ es una **recta horizontal** que une los estados $1$ y $2$; el trabajo de frontera es el **área del rectángulo** bajo esa recta. Físicamente lo realiza un dispositivo **pistón–cilindro** en equilibrio mecánico con una carga exterior fija (un émbolo libre con un peso encima, o la atmósfera): mientras el sistema intercambia calor, el émbolo se desplaza para mantener constante la presión interior.

---

> [!info]
> **Ubicación.** Curso de Termodinámica (MN121) · sección [[Procesos/index | Procesos Termodinámicos]]. Es el caso $n=0$ del politrópico. Sus **hermanas** son [[Proceso Isocorico | el isocórico]] ($v=$cte), [[Proceso Isotermico | el isotérmico]] ($T=$cte) y [[Proceso Politropico | el politrópico]] ($Pv^n=$cte). Se apoya en la [[Primera Ley SC | primera ley para sistemas cerrados]], en la [[Entalpia | entalpía]] $h=u+Pv$ y en las propiedades del [[Gas Ideal | gas ideal]].
> **Convención.** SI; $w,q$ específicos (por unidad de masa); $\delta q,\delta w$ inexactos, $du,dh,ds$ exactos; $q>0$ hacia el sistema, $w>0$ realizado por el sistema; gas ideal con $Pv=RT$, $c_p-c_v=R$, $\gamma=c_p/c_v$.

---

> [!teoria] Lectura gráfica: el área es el trabajo y el calor
> La isóbara concentra dos lecturas geométricas en una sola figura:
>
> ![[isobarico_pv_ts.svg|520]]
> *Izquierda: en el plano $P$–$v$ la isóbara es una recta horizontal; el área del rectángulo $P\,(v_2-v_1)$ bajo ella es el trabajo de frontera $w$. Derecha: en el plano $T$–$s$ la isóbara es una curva creciente cuya área bajo ella es el calor $q=\Delta h$; es **menos empinada** que la isócora porque $c_p>c_v$.*

---

## Trabajo de frontera

> [!teorema] Trabajo isobárico
> En un proceso isobárico cuasiestático el trabajo de frontera por unidad de masa vale
> $$w=P\,(v_2-v_1)=P\,\Delta v,$$
> y para gas ideal equivale a $w=R\,(T_2-T_1)$.

> [!demostracion]
> **Paso 1 — Definición de trabajo de frontera.** Para un sistema cerrado con frontera móvil cuasiestática, el trabajo elemental específico es $\delta w=P\,dv$, de modo que
> $$w=\int_1^2 P\,dv.$$
>
> **Paso 2 — Extraer la presión de la integral.** Como $P$ es constante en todo el proceso, sale fuera del signo integral:
> $$w=P\int_1^2 dv=P\,(v_2-v_1)=P\,\Delta v.$$
> Esto es exactamente el área del rectángulo de base $\Delta v$ y altura $P$ bajo la recta horizontal en el plano $P$–$v$.
>
> **Paso 3 — Versión para gas ideal.** De $Pv=RT$ evaluada en cada estado, $Pv_1=RT_1$ y $Pv_2=RT_2$ (la misma $P$). Restando,
> $$P\,(v_2-v_1)=R\,(T_2-T_1)\quad\Longrightarrow\quad w=R\,(T_2-T_1)=R\,\Delta T.$$
> $\blacksquare$

> [!info]
> Si el sistema se **expande** ($v_2>v_1$, calentamiento) entonces $w>0$: el sistema realiza trabajo empujando el émbolo. Si se **comprime** ($v_2<v_1$, enfriamiento) entonces $w<0$: el entorno realiza trabajo sobre el sistema.

---

## El calor es el cambio de entalpía

Este es el resultado central del proceso isobárico, y la razón histórica de que se defina la [[Entalpia | entalpía]].

> [!teorema] $q_p=\Delta h$
> En un proceso a presión constante con solo trabajo de frontera, el calor intercambiado es igual al **cambio de entalpía**:
> $$q_p=\Delta h=h_2-h_1.$$
> Para gas ideal, $q_p=c_p\,\Delta T=c_p\,(T_2-T_1)$.

> [!demostracion]
> **Paso 1 — Primera ley para sistema cerrado.** Por unidad de masa,
> $$q=\Delta u+w.$$
>
> **Paso 2 — Sustituir el trabajo isobárico.** Del teorema anterior $w=P\,\Delta v$, luego
> $$q=\Delta u+P\,\Delta v=(u_2-u_1)+P\,(v_2-v_1).$$
>
> **Paso 3 — Reconocer el cambio de entalpía.** Como $P$ es **constante**, $P_1=P_2=P$ y podemos meter $P$ dentro de cada término:
> $$q=(u_2+P_2v_2)-(u_1+P_1v_1)=(u_2+Pv_2)-(u_1+Pv_1).$$
> Pero $u+Pv\equiv h$ es por definición la entalpía específica. Por tanto cada paréntesis es una entalpía:
> $$q=h_2-h_1=\Delta h.$$
>
> **Paso 4 — Forma diferencial y caso gas ideal.** En forma infinitesimal, de $h=u+Pv$ se tiene $dh=du+P\,dv+v\,dP$; con $dP=0$ queda $dh=du+P\,dv=\delta q$ (primera ley), es decir $\delta q_p=dh$. Para gas ideal $dh=c_p\,dT$, de donde
> $$q_p=\int_1^2 c_p\,dT=c_p\,(T_2-T_1)=c_p\,\Delta T\qquad(c_p\text{ constante}).$$
> $\blacksquare$

> [!info]
> Este resultado **motiva** la propiedad entalpía: en flujos y en calentamientos a presión constante (calderas, intercambiadores abiertos a la atmósfera, calorímetros isobáricos) el calor se contabiliza directamente como $\Delta h$. Y justifica la definición del calor específico a presión constante
> $$c_p\equiv\left(\frac{\partial h}{\partial T}\right)_P,$$
> que mide cuánta entalpía (es decir, cuánto calor en isobárico) se necesita para subir un grado la temperatura.

---

## Relación de estado: ley de Charles

> [!proposicion] Ley de Charles ($P$ constante)
> Para un gas ideal a presión constante el volumen específico es proporcional a la temperatura absoluta:
> $$\frac{v_1}{T_1}=\frac{v_2}{T_2}.$$

> [!demostracion]
> **Paso 1 — Ecuación de estado en cada extremo.** $Pv_1=RT_1$ y $Pv_2=RT_2$.
>
> **Paso 2 — Despejar la constante.** Dividiendo cada igualdad entre $T$ con $P=$cte:
> $$\frac{v_1}{T_1}=\frac{R}{P}=\frac{v_2}{T_2}.$$
> Como $R/P$ es el mismo valor en ambos estados (misma $P$), se concluye
> $$\frac{v_1}{T_1}=\frac{v_2}{T_2}.$$
> $\blacksquare$

---

## Cambio de entropía

> [!teorema] Entropía isobárica
> Para gas ideal a presión constante,
> $$\Delta s=\int_1^2 c_p\,\frac{dT}{T}=c_p\ln\frac{T_2}{T_1}\qquad(c_p\text{ constante}).$$

> [!demostracion]
> **Paso 1 — Relación $T\,ds$ con la entalpía.** La segunda relación de Gibbs es
> $$dh=T\,ds+v\,dP.$$
>
> **Paso 2 — Imponer $P$ constante.** Con $dP=0$ desaparece el último término:
> $$T\,ds=dh\quad\Longrightarrow\quad ds=\frac{dh}{T}.$$
>
> **Paso 3 — Usar $dh=c_p\,dT$ (gas ideal).** Sustituyendo,
> $$ds=\frac{c_p\,dT}{T}.$$
>
> **Paso 4 — Integrar.** Con $c_p$ constante,
> $$\Delta s=\int_1^2 c_p\,\frac{dT}{T}=c_p\ln\frac{T_2}{T_1}.$$
> $\blacksquare$

> [!info]
> Comparada con la isócora, $\Delta s_v=c_v\ln(T_2/T_1)$, ambas son curvas **logarítmicas** en $T$–$s$, pero como $c_p>c_v$ la isóbara necesita **más** entropía para el mismo salto de temperatura: por eso en el plano $T$–$s$ la isóbara es **menos empinada** (más tendida) que la isócora. La pendiente local es $(\partial T/\partial s)_P=T/c_p<T/c_v=(\partial T/\partial s)_v$.

---

## Relación de Mayer $c_p=c_v+R$

> [!proposicion] Relación de Mayer
> Para un gas ideal los calores específicos se relacionan por
> $$c_p=c_v+R\qquad\Longleftrightarrow\qquad c_p-c_v=R.$$

> [!demostracion]
> Comparamos el calentamiento del **mismo** gas ideal, el **mismo** salto de temperatura $\Delta T$, por dos caminos: a volumen constante y a presión constante.
>
> **Paso 1 — Definición termodinámica de los dos calores específicos.** Como $u=u(T)$ y $h=h(T)$ para gas ideal,
> $$c_v=\left(\frac{\partial u}{\partial T}\right)_v=\frac{du}{dT},\qquad c_p=\left(\frac{\partial h}{\partial T}\right)_P=\frac{dh}{dT}.$$
>
> **Paso 2 — Derivar la definición de entalpía.** De $h=u+Pv$ y $Pv=RT$ (gas ideal) se tiene
> $$h=u+RT.$$
>
> **Paso 3 — Derivar respecto de $T$.** Derivando término a término,
> $$\frac{dh}{dT}=\frac{du}{dT}+R\quad\Longrightarrow\quad c_p=c_v+R.$$
>
> **Interpretación energética.** A volumen constante todo el calor sube la energía interna: $q_v=c_v\,\Delta T$. A presión constante hace falta **lo mismo** para subir $u$ **más** el trabajo de expansión $P\,\Delta v=R\,\Delta T$ que el gas hace contra el émbolo:
> $$q_p=\underbrace{c_v\,\Delta T}_{\Delta u}+\underbrace{R\,\Delta T}_{w}=(c_v+R)\,\Delta T=c_p\,\Delta T.$$
> El exceso $c_p-c_v=R$ es precisamente el trabajo de frontera por grado. $\blacksquare$

---

## Ejemplo: pistón–cilindro con peso encima

> [!ejemplo]
> Un dispositivo **pistón–cilindro** vertical contiene aire (gas ideal, $R=0{,}287\ \text{kJ/kg·K}$, $c_p=1{,}005\ \text{kJ/kg·K}$). El émbolo, libre y sin rozamiento, lleva un peso encima que junto con la atmósfera fija la presión interior en $P=300\ \text{kPa}$ y la mantiene **constante** mientras el émbolo pueda moverse. La masa de aire es $m=2\ \text{kg}$ y parte del estado $1$ a $T_1=300\ \text{K}$.
>
> Se calienta el aire en **dos etapas a la misma presión**:
> - **Etapa A:** de $1$ a $2$, de $300\ \text{K}$ a $600\ \text{K}$.
> - **Etapa B:** de $2$ a $3$, de $600\ \text{K}$ a $900\ \text{K}$.
>
> Para el proceso global $1\to3$ (que sigue siendo isobárico) calcule el trabajo de frontera $W$, el calor $Q=\Delta H$, la variación de energía interna $\Delta U$ y la variación de entropía $\Delta S$. Verifique el balance $Q=\Delta U+W$ e indique qué fracción del calor se va en trabajo de expansión y cuál en energía interna.

> [!solucion]
> Trabajamos con magnitudes específicas y luego multiplicamos por $m=2\ \text{kg}$. Primero las propiedades derivadas:
> $$c_v=c_p-R=1{,}005-0{,}287=0{,}718\ \text{kJ/kg·K},\qquad \Delta T=T_3-T_1=900-300=600\ \text{K}.$$
> Como el émbolo nunca se traba, las dos etapas comparten la misma presión: el proceso $1\to3$ es **una sola isóbara**; basta usar los extremos $1$ y $3$.
>
> **Paso 1 — Trabajo de frontera.** Por gas ideal a $P$ constante, $w=R\,\Delta T$:
> $$w=0{,}287\times 600=172{,}2\ \text{kJ/kg}\quad\Longrightarrow\quad W=m\,w=2\times 172{,}2=344{,}4\ \text{kJ}.$$
> Como $W>0$ el aire se expande y empuja el peso hacia arriba.
>
> **Paso 2 — Calor = cambio de entalpía.** Por ser isobárico, $q=\Delta h=c_p\,\Delta T$:
> $$q=1{,}005\times 600=603{,}0\ \text{kJ/kg}\quad\Longrightarrow\quad Q=\Delta H=2\times 603{,}0=1206{,}0\ \text{kJ}.$$
>
> **Paso 3 — Cambio de energía interna.** $\Delta u=c_v\,\Delta T$ (vale para gas ideal en cualquier proceso):
> $$\Delta u=0{,}718\times 600=430{,}8\ \text{kJ/kg}\quad\Longrightarrow\quad \Delta U=2\times 430{,}8=861{,}6\ \text{kJ}.$$
>
> **Paso 4 — Verificación de la primera ley.**
> $$\Delta U+W=861{,}6+344{,}4=1206{,}0\ \text{kJ}=Q.\quad\checkmark$$
> El balance cierra exactamente, como debe.
>
> **Paso 5 — Cambio de entropía.** $\Delta s=c_p\ln(T_3/T_1)$:
> $$\Delta s=1{,}005\,\ln\frac{900}{300}=1{,}005\times\ln 3=1{,}005\times 1{,}0986=1{,}104\ \text{kJ/kg·K},$$
> $$\Delta S=m\,\Delta s=2\times 1{,}104=2{,}208\ \text{kJ/K}.$$
>
> **Paso 6 — Reparto del calor.** El calor aportado se divide entre energía interna y trabajo de frontera:
> $$\frac{\Delta U}{Q}=\frac{861{,}6}{1206{,}0}=0{,}714\;(71{,}4\,\%),\qquad \frac{W}{Q}=\frac{344{,}4}{1206{,}0}=0{,}286\;(28{,}6\,\%).$$
> Es decir, de cada unidad de calor que entra, el $71{,}4\,\%$ eleva la energía interna (la temperatura) del aire y el $28{,}6\,\%$ se gasta en el trabajo de expansión contra el émbolo. Nótese que estas fracciones coinciden con $c_v/c_p$ y $R/c_p$ respectivamente:
> $$\frac{c_v}{c_p}=\frac{0{,}718}{1{,}005}=0{,}714,\qquad \frac{R}{c_p}=\frac{0{,}287}{1{,}005}=0{,}286,$$
> lo que confirma que el reparto **no depende del salto de temperatura**, solo de la naturaleza del gas. $\blacksquare$
>
> **Comentario sobre el cambio de fase.** Si en lugar de aire el cilindro contuviera **agua** calentándose isobáricamente (por ejemplo a $P=300\ \text{kPa}$), el cálculo sería conceptualmente idéntico, $q=\Delta h=h_2-h_1$, pero las entalpías se leerían de **tablas de vapor** y no de $c_p\,\Delta T$: durante la **ebullición** la temperatura permanecería constante (a $T_{\text{sat}}$ de esa presión) mientras la entalpía crece por el calor latente $h_{fg}$. La relación central $q_p=\Delta h$ sigue valiendo; lo único que cambia es de dónde se obtiene $\Delta h$.

---

> [!warning]
> La igualdad $q_p=\Delta h$ exige **dos** condiciones: que la presión sea constante **y** que el único trabajo sea el de frontera ($\delta w=P\,dv$). Si hay otros trabajos (eje, eléctrico, agitación) o $P$ varía, $q\neq\Delta h$. Además, la **entalpía es una propiedad** (función de estado): $h_2-h_1$ depende solo de los estados extremos, mientras que el calor $q$ depende del camino; aquí coinciden **numéricamente** por las dos condiciones citadas, pero conceptualmente no son lo mismo. En otros procesos $\Delta h$ existe igual pero **no** es el calor.

---

> [!referencia]
> Çengel & Boles, *Termodinámica*, caps. 4 (trabajo de frontera) y 7 (entropía); Moran & Shapiro, *Fundamentos de Termodinámica Técnica*, caps. 2–3 y 6; Borgnakke & Sonntag, *Fundamentals of Thermodynamics*. Tablas/diagramas con **CATT3**.
