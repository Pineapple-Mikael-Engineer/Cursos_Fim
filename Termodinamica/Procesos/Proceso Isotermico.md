---
title: Proceso Isotérmico
order: 4
tags:
  - termodinamica
  - teoria
  - procesos
draft: false
aliases:
  - Proceso isotérmico
  - Proceso a temperatura constante
---

# Proceso Isotérmico $T=\text{cte},\quad w=q,\ \Delta u=0$

> [!definicion]
> Un **proceso isotérmico** es aquel que se desarrolla manteniendo la temperatura constante:
> $$T=\text{cte}\quad\Longrightarrow\quad dT=0.$$
> Para que la temperatura no cambie mientras el sistema intercambia trabajo, debe intercambiar simultáneamente calor con un foco térmico (la pared del recipiente, un baño, etc.); es por esto un proceso intrínsecamente **no adiabático**.
>
> Para un [[Gas Ideal | gas ideal]], cuya ecuación de estado es $Pv=RT$, la condición $T=\text{cte}$ implica
> $$Pv=RT=\text{cte}\quad\Longrightarrow\quad Pv=\text{cte},$$
> de modo que en el diagrama $P$–$v$ el lugar geométrico de los estados de un proceso isotérmico es una **hipérbola equilátera** ($P=\text{cte}/v$).

> [!info]
> Esta nota pertenece a la sección [[Procesos/index | Procesos Termodinámicos]]. Sus hermanas son [[Proceso Adiabatico | Proceso Adiabático]], [[Proceso Politropico | Proceso Politrópico]] y [[Proceso Isocorico | Proceso Isocórico]]. Para los balances se usan [[Primera Ley SC | Primera Ley (sistema cerrado)]], el modelo de [[Gas Ideal | Gas Ideal]] y el concepto de [[Entropia | Entropía]].

> [!teoria] Características del proceso isotérmico de gas ideal
> | Magnitud | Valor en el proceso isotérmico (gas ideal) |
> |---|---|
> | Temperatura | $T=\text{cte}$ |
> | Trayectoria $P$–$v$ | $Pv=\text{cte}$ (hipérbola) |
> | Energía interna | $\Delta u=0$ |
> | Entalpía | $\Delta h=0$ |
> | Primera ley | $q=w$ |
> | Trabajo | $w=RT\ln\dfrac{v_2}{v_1}=RT\ln\dfrac{P_1}{P_2}$ |
> | Entropía | $\Delta s=R\ln\dfrac{v_2}{v_1}=R\ln\dfrac{P_1}{P_2}$ |

## Energía interna y entalpía constantes

> [!proposicion]
> En un proceso isotérmico de **gas ideal**, la energía interna y la entalpía específicas no cambian:
> $$\Delta u=0,\qquad \Delta h=0.$$

> [!demostracion]
> **Paso 1 — La energía interna del gas ideal solo depende de $T$.** Una propiedad fundamental del gas ideal es que su energía interna específica es función exclusiva de la temperatura, $u=u(T)$ (resultado del experimento de expansión libre de Joule). Por tanto su diferencial es
> $$du=c_v\,dT,$$
> donde $c_v=\left(\dfrac{\partial u}{\partial T}\right)_v$ es el calor específico a volumen constante.
>
> **Paso 2 — Integrar entre los estados extremos.** Integrando entre el estado $1$ y el estado $2$,
> $$\Delta u=\int_1^2 c_v\,dT=c_v\,(T_2-T_1)=c_v\,\Delta T.$$
> Como el proceso es isotérmico, $T_2=T_1$, luego $\Delta T=0$ y
> $$\boxed{\Delta u=c_v\,\Delta T=0.}$$
>
> **Paso 3 — Entalpía.** La entalpía del gas ideal también depende solo de $T$, ya que $h=u+Pv=u(T)+RT=h(T)$, de modo que $dh=c_p\,dT$. Integrando,
> $$\Delta h=\int_1^2 c_p\,dT=c_p\,(T_2-T_1)=c_p\,\Delta T=0.$$
> $\blacksquare$

> [!proposicion] Todo el calor se convierte en trabajo
> En un proceso isotérmico de gas ideal el calor intercambiado es igual al trabajo:
> $$q=w.$$

> [!demostracion]
> **Paso 1 — Primera ley para sistema cerrado.** Por la [[Primera Ley SC | primera ley]] en forma específica,
> $$q=\Delta u+w.$$
>
> **Paso 2 — Anular $\Delta u$.** Por la proposición anterior, en el proceso isotérmico de gas ideal $\Delta u=0$. Sustituyendo,
> $$\boxed{q=w.}$$
> Es decir, todo el calor que entra al gas se transforma íntegramente en trabajo de frontera (y viceversa: para comprimirlo isotérmicamente, todo el trabajo que entra sale como calor). $\blacksquare$

## Trabajo del proceso isotérmico

> [!teorema]
> El trabajo de frontera específico de un proceso isotérmico **reversible** de gas ideal entre los estados $1$ y $2$ es
> $$w=RT\ln\frac{v_2}{v_1}=RT\ln\frac{P_1}{P_2}.$$

> [!demostracion]
> **Paso 1 — Definición del trabajo de frontera.** Para un proceso cuasiestático,
> $$w=\int_1^2 P\,dv.$$
>
> **Paso 2 — Sustituir la presión por la ecuación de estado.** Del modelo de gas ideal $Pv=RT$ se despeja $P=\dfrac{RT}{v}$. Como $T=\text{cte}$, el producto $RT$ sale de la integral:
> $$w=\int_1^2 \frac{RT}{v}\,dv=RT\int_{v_1}^{v_2}\frac{dv}{v}.$$
>
> **Paso 3 — Integrar.** La primitiva de $1/v$ es $\ln v$, luego
> $$w=RT\,\bigl[\ln v\bigr]_{v_1}^{v_2}=RT\ln\frac{v_2}{v_1}.$$
>
> **Paso 4 — Expresar en presiones.** Como $T$ es constante, $P_1v_1=P_2v_2=RT$, de donde $\dfrac{v_2}{v_1}=\dfrac{P_1}{P_2}$. Sustituyendo,
> $$\boxed{w=RT\ln\frac{v_2}{v_1}=RT\ln\frac{P_1}{P_2}.}$$
> Combinando con $q=w$, el calor vale $q=RT\ln\dfrac{v_2}{v_1}$. $\blacksquare$

## Entropía del proceso isotérmico

> [!teorema]
> La variación de entropía específica de un gas ideal en un proceso isotérmico es
> $$\Delta s=\frac{q}{T}=R\ln\frac{v_2}{v_1}=R\ln\frac{P_1}{P_2}.$$

> [!demostracion]
> **Paso 1 — Ecuación $T\,ds$.** Partimos de la primera relación de Gibbs (válida para cualquier sustancia simple compresible):
> $$T\,ds=du+P\,dv.$$
>
> **Paso 2 — Anular $du$.** En el proceso isotérmico de gas ideal $du=c_v\,dT=0$, luego
> $$T\,ds=P\,dv\quad\Longrightarrow\quad ds=\frac{P}{T}\,dv.$$
>
> **Paso 3 — Sustituir $P/T$.** De $Pv=RT$ se tiene $\dfrac{P}{T}=\dfrac{R}{v}$, por lo que
> $$ds=\frac{R}{v}\,dv.$$
>
> **Paso 4 — Integrar.**
> $$\Delta s=\int_{v_1}^{v_2}\frac{R}{v}\,dv=R\ln\frac{v_2}{v_1}=R\ln\frac{P_1}{P_2}.$$
>
> **Paso 5 — Relación con el calor.** Como $T$ es constante, $q=\displaystyle\int_1^2 T\,ds=T\,\Delta s$, de donde
> $$\boxed{\Delta s=\frac{q}{T}=R\ln\frac{v_2}{v_1}=R\ln\frac{P_1}{P_2}.}$$
> $\blacksquare$

> [!info] Representación en el diagrama $T$–$s$
> Como $T=\text{cte}$, el proceso isotérmico es una **recta horizontal** en el plano $T$–$s$. El área bajo esa recta es
> $$\int_1^2 T\,ds=T\,\Delta s=q=w,$$
> es decir, el área en $T$–$s$ representa directamente el calor intercambiado, que en el gas ideal coincide con el trabajo.

![[isotermico_pv_ts.svg|520]]
*Proceso isotérmico de un gas ideal. Izquierda: en el plano $P$–$v$ la trayectoria es una hipérbola $Pv=\text{cte}$, y el área bajo la curva entre $v_1$ y $v_2$ es el trabajo $w=RT\ln(v_2/v_1)$. Derecha: en el plano $T$–$s$ es una recta horizontal a $T=\text{cte}$, cuya área $T\,\Delta s$ es el calor $q=w$.*

> [!warning] $\Delta u=0$ es propio del gas ideal, no del proceso isotérmico
> La igualdad $\Delta u=0$ en un proceso isotérmico **solo es válida para el gas ideal**, porque en él $u=u(T)$. En un **gas real** (con interacciones moleculares) o en un **fluido bifásico** (cambio de fase a temperatura constante, como agua hirviendo) la energía interna depende también del volumen o del título, de modo que un proceso isotérmico puede tener $\Delta u\neq 0$. En esos casos $q\neq w$.
>
> No confundir tampoco **isotérmico** con **adiabático**: en el isotérmico $T=\text{cte}$ y hay calor ($q\neq 0$); en el [[Proceso Adiabatico | adiabático]] $q=0$ y la temperatura cambia. Son procesos esencialmente distintos.

## Ejemplo: compresión isotérmica de aire vs. compresión adiabática

> [!ejemplo]
> Se comprime aire (modelado como gas ideal, $R=0{,}287\ \mathrm{kJ/(kg\cdot K)}$, $\gamma=1{,}4$) en un cilindro desde $P_1=100\ \mathrm{kPa}$ y $T_1=300\ \mathrm{K}$ hasta $P_2=600\ \mathrm{kPa}$.
> **(a)** Para una compresión **isotérmica** reversible, calcule el trabajo específico $w_{\text{iso}}$ y el calor $q_{\text{iso}}$.
> **(b)** Calcule la variación de entropía $\Delta s$ del gas y verifique que el calor sale del gas.
> **(c)** Compare con una compresión **adiabática** reversible (isentrópica) entre las mismas presiones: ¿cuál requiere más trabajo y por qué? Dé el cociente de ambos trabajos de compresión.

> [!solucion]
> **Parte (a) — Trabajo y calor de la compresión isotérmica.**
>
> Usamos $w_{\text{iso}}=RT\ln\dfrac{P_1}{P_2}$, con $T=T_1=300\ \mathrm{K}$. La relación de presiones es $\dfrac{P_2}{P_1}=6$, luego $\ln\dfrac{P_1}{P_2}=-\ln 6=-1{,}7918$.
> $$w_{\text{iso}}=R\,T\,\ln\frac{P_1}{P_2}=0{,}287\times 300\times(-1{,}7918)=-154{,}3\ \mathrm{kJ/kg}.$$
> El signo **negativo** indica que el trabajo **entra** al gas (lo estamos comprimiendo), como debe ser. Por la primera ley con $\Delta u=0$:
> $$q_{\text{iso}}=w_{\text{iso}}=-154{,}3\ \mathrm{kJ/kg},$$
> calor **negativo**: durante la compresión el gas debe **expulsar** $154{,}3\ \mathrm{kJ/kg}$ al foco frío para mantener $T$ constante.
>
> **Parte (b) — Entropía del gas.**
> $$\Delta s=R\ln\frac{P_1}{P_2}=0{,}287\times(-1{,}7918)=-0{,}514\ \mathrm{kJ/(kg\cdot K)}.$$
> La entropía del gas **disminuye**. Esto es coherente: como el proceso es reversible e isotérmico, el calor intercambiado por el gas es
> $$q=T\,\Delta s=300\times(-0{,}514)=-154{,}3\ \mathrm{kJ/kg}<0,$$
> que coincide con el valor de (a) y confirma que el **calor sale** del gas. (La entropía del universo no disminuye: el foco frío recibe $|q|/T$, compensando exactamente la caída del gas.)
>
> **Parte (c) — Comparación con la compresión adiabática reversible.**
>
> En la compresión [[Proceso Adiabatico | adiabática reversible]] no hay calor, así que la temperatura **sube** según la relación isentrópica
> $$T_2=T_1\left(\frac{P_2}{P_1}\right)^{\frac{\gamma-1}{\gamma}}=300\times 6^{\,0{,}2857}=300\times 1{,}6685=500{,}6\ \mathrm{K}.$$
> El trabajo de compresión (de frontera) adiabático se obtiene de la primera ley con $q=0$, $w=-\Delta u=-c_v(T_2-T_1)$, con $c_v=\dfrac{R}{\gamma-1}=\dfrac{0{,}287}{0{,}4}=0{,}7175\ \mathrm{kJ/(kg\cdot K)}$:
> $$w_{\text{adi}}=-c_v\,(T_2-T_1)=-0{,}7175\times(500{,}6-300)=-0{,}7175\times 200{,}6=-143{,}9\ \mathrm{kJ/kg}.$$
>
> Para comparar de forma justa el **esfuerzo de compresión**, conviene usar el trabajo de **flujo** (compresor, $\int v\,dP$), que es la magnitud que paga una máquina real:
> $$w_{\text{flujo,iso}}=R\,T\ln\frac{P_1}{P_2}=-154{,}3\ \mathrm{kJ/kg},$$
> $$w_{\text{flujo,adi}}=\frac{\gamma}{\gamma-1}R\,(T_1-T_2)=\frac{1{,}4}{0{,}4}\times0{,}287\times(300-500{,}6)=3{,}5\times0{,}287\times(-200{,}6)=-201{,}5\ \mathrm{kJ/kg}.$$
>
> Tomando magnitudes de trabajo de flujo (lo relevante en un compresor):
> $$\frac{|w_{\text{flujo,iso}}|}{|w_{\text{flujo,adi}}|}=\frac{154{,}3}{201{,}5}=0{,}766.$$
> La compresión **isotérmica requiere menos trabajo**: solo el $76{,}6\%$ del trabajo de la adiabática, un ahorro cercano al $23\%$. El motivo físico es que al ir extrayendo calor mantenemos baja la temperatura y, por tanto, el volumen específico es menor a cada presión; como $w_{\text{flujo}}=\int v\,dP$, mover un gas "frío" (menos voluminoso) cuesta menos. La adiabática, al no evacuar calor, se calienta y se vuelve más difícil de comprimir. Este contraste es el fundamento del **enfriamiento intermedio** en los compresores. $\blacksquare$

> [!corolario] Por qué se refrigeran los compresores
> Como la compresión isotérmica exige menos trabajo que la adiabática entre las mismas presiones, en la práctica los [[Compresores | compresores]] reales se **refrigeran** (camisas de agua, aletas) y, sobre todo, se usa **enfriamiento intermedio** (*intercooling*) entre etapas: enfriar el gas entre compresiones sucesivas acerca el proceso global a la isoterma y reduce el trabajo total. La isoterma es así el **límite ideal de mínimo trabajo** de compresión, mientras que la adiabática es el de máximo.

> [!referencia]
> - Cengel, Y. & Boles, M. — *Termodinámica*, capítulos de trabajo de frontera, entropía y compresores.
> - Moran, M. & Shapiro, H. — *Fundamentals of Engineering Thermodynamics* (procesos politrópicos y trabajo de compresión $\int v\,dP$).
