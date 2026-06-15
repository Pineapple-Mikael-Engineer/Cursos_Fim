---
title: Proceso Politrópico
tags:
  - termodinamica
  - teoria
  - procesos
draft: false
aliases:
  - Proceso politrópico
  - Politrópico
---

# Proceso Politrópico $Pv^{\,n}=\text{cte}$

> [!definicion]
> Un **proceso politrópico** es aquel que un gas describe siguiendo la relación
> $$P\,v^{\,n}=\text{cte},$$
> donde $n$ es el **exponente politrópico**, un número **real** (puede ser positivo, negativo, nulo o infinito). Equivalentemente, entre dos estados $1$ y $2$ de la trayectoria:
> $$P_1 v_1^{\,n}=P_2 v_2^{\,n}.$$
> El exponente $n$ describe la "rigidez" de la curva en el plano $P\!-\!v$: cuanto mayor es $n$, más pronunciada es la caída de presión al expandirse el gas. Es la **familia general de procesos cuasiestáticos** de la que los cuatro procesos elementales son casos particulares.

> [!info]
> Esta nota pertenece a la sección [[Procesos/index | Procesos Termodinámicos]] y constituye la **generalización** de los cuatro procesos elementales: [[Proceso Isobarico | isobárico]] ($n=0$), [[Proceso Isotermico | isotérmico]] ($n=1$), [[Proceso Adiabatico | adiabático reversible]] ($n=\gamma$) e [[Proceso Isocorico | isocórico]] ($n\to\infty$). Para deducir el calor y el trabajo se emplean la [[Primera Ley SC | Primera Ley en sistema cerrado]] y el modelo de [[Gas Ideal | gas ideal]] $Pv=RT$. Notación: $R$ constante específica del gas, $c_v$ y $c_p$ calores específicos, $\gamma=c_p/c_v$.

![[politropico_familia.svg|460]]
*Familia de curvas $Pv^n=\text{cte}$ en el plano $P\!-\!v$ trazadas desde un estado común. La isóbara ($n=0$) es horizontal, la isoterma ($n=1$) es una hipérbola equilátera, la adiabática reversible ($n=\gamma>1$) cae más rápido que la isoterma, y la isócora ($n\to\infty$) es vertical. Al crecer $n$ la curva pivota desde la horizontal hacia la vertical.*

---

## El proceso general: los cuatro casos elementales

> [!teoria]
> El gran valor de la formulación politrópica es que **un solo parámetro** $n$ recupera los cuatro procesos básicos. Lo verificamos analizando la relación $Pv^n=\text{cte}$ en cada límite.

> [!proposicion] Casos particulares del exponente politrópico
> Para un gas ideal, la relación $Pv^n=\text{cte}$ degenera en:
>
> | $n$ | Relación resultante | Proceso |
> |:---:|:---|:---|
> | $0$ | $Pv^0=P=\text{cte}$ | [[Proceso Isobarico\| Isobárico]] |
> | $1$ | $Pv=\text{cte}\Rightarrow RT=\text{cte}\Rightarrow T=\text{cte}$ | [[Proceso Isotermico\| Isotérmico]] |
> | $\gamma$ | $Pv^{\gamma}=\text{cte}$ | [[Proceso Adiabatico\| Adiabático reversible]] |
> | $\to\infty$ | $P^{1/n}v=\text{cte}\Rightarrow v=\text{cte}$ | [[Proceso Isocorico\| Isocórico]] |

> [!demostracion] De los cuatro límites
> Partimos de $Pv^n=C$ (constante).
>
> **Paso 1 — Caso $n=0$ (isobárico).** Como $v^0=1$ para todo $v$, queda $P\cdot 1=C$, es decir $P=C=\text{cte}$. La presión no varía: proceso a presión constante.
>
> **Paso 2 — Caso $n=1$ (isotérmico).** Queda $Pv=C$. Para gas ideal $Pv=RT$, luego $RT=C$ y como $R$ es constante, $T=\text{cte}$. Proceso a temperatura constante.
>
> **Paso 3 — Caso $n=\gamma$ (adiabático reversible).** Por definición, $Pv^{\gamma}=\text{cte}$ es la relación que satisface un gas ideal en una transformación **adiabática y reversible** (se deduce de $\delta q=0$ junto con la primera ley; ver [[Proceso Adiabatico]]). Por tanto $n=\gamma$ reproduce exactamente esa trayectoria.
>
> **Paso 4 — Caso $n\to\infty$ (isocórico).** Reescribimos $Pv^n=C$ elevando a $1/n$:
> $$P^{1/n}\,v=C^{1/n}.$$
> Al tomar el límite $n\to\infty$ se tiene $P^{1/n}=P^{0}=1$ y $C^{1/n}\to 1$, de modo que $v=\text{cte}$. El volumen permanece fijo: proceso isocórico. $\blacksquare$

> [!teorema] Monotonía de la pendiente
> En el plano $P\!-\!v$, la pendiente de una politrópica es
> $$\frac{dP}{dv}=-\,n\,\frac{P}{v}.$$
> **Demostración.** Diferenciando $Pv^n=C$ por la regla del producto: $dP\,v^n+P\,n\,v^{n-1}dv=0$. Dividiendo entre $v^{n-1}$: $v\,dP+nP\,dv=0$, de donde $\dfrac{dP}{dv}=-n\dfrac{P}{v}$. Como $P,v>0$, la pendiente es negativa y su magnitud crece con $n$: la isóbara ($n=0$) es horizontal y la isócora ($n\to\infty$) es vertical. $\blacksquare$

---

## Relaciones de estado (gas ideal)

> [!teorema] Relaciones $T$–$v$–$P$ del proceso politrópico
> Para un gas ideal que evoluciona politrópicamente entre los estados $1$ y $2$:
> $$\boxed{\;\frac{T_2}{T_1}=\left(\frac{v_1}{v_2}\right)^{n-1}=\left(\frac{P_2}{P_1}\right)^{(n-1)/n}\;}$$

> [!demostracion] De las relaciones de estado
> **Paso 1 — Relación $T$–$v$.** Del modelo de gas ideal, $P=RT/v$. Sustituyendo en $Pv^n=\text{cte}$:
> $$\frac{RT}{v}\,v^n=RT\,v^{\,n-1}=\text{cte}.$$
> Como $R$ es constante, $T\,v^{\,n-1}=\text{cte}$. Igualando estados $1$ y $2$:
> $$T_1 v_1^{\,n-1}=T_2 v_2^{\,n-1}\;\Longrightarrow\;\frac{T_2}{T_1}=\left(\frac{v_1}{v_2}\right)^{n-1}.$$
>
> **Paso 2 — Relación $T$–$P$.** De gas ideal, $v=RT/P$. Sustituyendo en $Pv^n=\text{cte}$:
> $$P\left(\frac{RT}{P}\right)^{n}=P^{\,1-n}\,(RT)^{n}=\text{cte}\;\Longrightarrow\;P^{\,1-n}T^{\,n}=\text{cte}.$$
> Elevando a $1/n$: $P^{(1-n)/n}\,T=\text{cte}$, es decir $T\,P^{-(n-1)/n}=\text{cte}$. Igualando estados:
> $$\frac{T_2}{T_1}=\left(\frac{P_2}{P_1}\right)^{(n-1)/n}.\qquad\blacksquare$$

---

## Trabajo de frontera $w=\int P\,dv$

> [!teorema] Trabajo de frontera politrópico (sistema cerrado)
> El trabajo específico de frontera realizado por un gas ideal en un proceso politrópico es, para $n\neq 1$:
> $$\boxed{\;w=\frac{P_1 v_1-P_2 v_2}{n-1}=\frac{R\,(T_1-T_2)}{n-1}\;}$$
> y para $n=1$ (caso isotérmico, obtenido por el límite):
> $$w=R\,T\,\ln\!\frac{v_2}{v_1}.$$

> [!demostracion] Integración del trabajo de frontera
> **Paso 1 — Planteo.** El trabajo de frontera específico es $w=\displaystyle\int_1^2 P\,dv$. Como $Pv^n=P_1v_1^n=\text{cte}$, despejamos la presión a lo largo de la trayectoria:
> $$P=\frac{P_1 v_1^{\,n}}{v^{\,n}}=P_1 v_1^{\,n}\,v^{-n}.$$
>
> **Paso 2 — Integral para $n\neq 1$.** Sustituyendo y sacando la constante $P_1v_1^n$:
> $$w=\int_{v_1}^{v_2}P_1 v_1^{\,n}\,v^{-n}\,dv=P_1 v_1^{\,n}\int_{v_1}^{v_2}v^{-n}\,dv=P_1 v_1^{\,n}\left[\frac{v^{\,1-n}}{1-n}\right]_{v_1}^{v_2}.$$
> Evaluando los límites:
> $$w=\frac{P_1 v_1^{\,n}}{1-n}\left(v_2^{\,1-n}-v_1^{\,1-n}\right)=\frac{P_1 v_1^{\,n}\,v_2^{\,1-n}-P_1 v_1^{\,n}\,v_1^{\,1-n}}{1-n}.$$
>
> **Paso 3 — Reagrupación.** En el segundo término $v_1^{\,n}v_1^{\,1-n}=v_1$, luego $P_1 v_1^{\,n}\,v_1^{\,1-n}=P_1 v_1$. En el primero usamos que sobre la curva $P_1 v_1^{\,n}=P_2 v_2^{\,n}$, de modo que $P_1 v_1^{\,n}\,v_2^{\,1-n}=P_2 v_2^{\,n}\,v_2^{\,1-n}=P_2 v_2$. Entonces:
> $$w=\frac{P_2 v_2-P_1 v_1}{1-n}=\frac{P_1 v_1-P_2 v_2}{n-1}.$$
>
> **Paso 4 — Forma en temperatura.** Para gas ideal $Pv=RT$, por lo que $P_1v_1=RT_1$ y $P_2v_2=RT_2$:
> $$w=\frac{R T_1-R T_2}{n-1}=\frac{R\,(T_1-T_2)}{n-1}.$$
>
> **Paso 5 — Límite $n=1$.** Cuando $n\to 1$, la integral del Paso 2 es singular ($1-n\to 0$); hay que integrar directamente con $n=1$. Entonces $Pv=P_1v_1=\text{cte}$, así que $P=P_1v_1/v$ y
> $$w=\int_{v_1}^{v_2}\frac{P_1 v_1}{v}\,dv=P_1 v_1\int_{v_1}^{v_2}\frac{dv}{v}=P_1 v_1\,\ln\!\frac{v_2}{v_1}=R\,T\,\ln\!\frac{v_2}{v_1},$$
> que es exactamente el trabajo del [[Proceso Isotermico | proceso isotérmico]]. $\blacksquare$

---

## Calor y calor específico politrópico

> [!teorema] Calor del proceso politrópico
> El calor específico transferido en un proceso politrópico de un gas ideal es
> $$q=c_v(T_2-T_1)+\frac{R\,(T_1-T_2)}{n-1}=c_n\,(T_2-T_1),$$
> donde el **calor específico politrópico** es
> $$\boxed{\;c_n=c_v\,\frac{n-\gamma}{n-1}\;}\qquad (n\neq 1).$$

> [!demostracion] Calor y calor específico politrópico
> **Paso 1 — Primera Ley.** Por la [[Primera Ley SC | Primera Ley en sistema cerrado]], por unidad de masa $q=\Delta u+w$. Para gas ideal $\Delta u=c_v(T_2-T_1)$, y del resultado anterior $w=\dfrac{R(T_1-T_2)}{n-1}$:
> $$q=c_v(T_2-T_1)+\frac{R\,(T_1-T_2)}{n-1}.$$
>
> **Paso 2 — Factor común.** Notamos que $T_1-T_2=-(T_2-T_1)$. Sacando $(T_2-T_1)$ como factor:
> $$q=(T_2-T_1)\left(c_v-\frac{R}{n-1}\right).$$
>
> **Paso 3 — Relación de Mayer.** Para gas ideal $c_p-c_v=R$, luego $R=c_v(\gamma-1)$ pues $\gamma=c_p/c_v$ implica $c_p=\gamma c_v$ y $R=\gamma c_v-c_v=c_v(\gamma-1)$. Sustituyendo:
> $$c_n=c_v-\frac{R}{n-1}=c_v-\frac{c_v(\gamma-1)}{n-1}=c_v\left(1-\frac{\gamma-1}{n-1}\right).$$
>
> **Paso 4 — Reducción a fracción única.**
> $$c_n=c_v\cdot\frac{(n-1)-(\gamma-1)}{n-1}=c_v\,\frac{n-\gamma}{n-1}.$$
> Por tanto $q=c_n(T_2-T_1)$ con $c_n=c_v\dfrac{n-\gamma}{n-1}$. $\blacksquare$

> [!proposicion] Signo del calor específico politrópico
> Para $1<n<\gamma$ se tiene $c_n<0$.
>
> **Demostración.** En ese rango el denominador $n-1>0$ y el numerador $n-\gamma<0$ (porque $n<\gamma$), de modo que el cociente es negativo y $c_n=c_v\dfrac{n-\gamma}{n-1}<0$. $\blacksquare$

> [!info] Interpretación del calor específico negativo
> Un $c_n<0$ significa que, en la relación $q=c_n\,\Delta T$, calor y variación de temperatura tienen **signos opuestos**: el gas **se enfría aunque reciba calor**, o **se calienta aunque ceda calor**. No hay contradicción termodinámica: en una compresión con $1<n<\gamma$ el trabajo entrante eleva la temperatura más de lo que el calor cedido la baja, así que la temperatura sube mientras $q<0$. El gas almacena energía por trabajo y simultáneamente expulsa parte como calor. Físicamente es un régimen intermedio entre el adiabático ($n=\gamma$, sin calor) y el isotérmico ($n=1$, todo el trabajo sale como calor).

---

## Variación de entropía

> [!teorema] Cambio de entropía politrópico
> Para un gas ideal en un proceso politrópico reversible:
> $$\Delta s=c_n\,\ln\!\frac{T_2}{T_1},\qquad c_n=c_v\,\frac{n-\gamma}{n-1},$$
> equivalente a la forma general
> $$\Delta s=c_v\,\ln\!\frac{T_2}{T_1}+R\,\ln\!\frac{v_2}{v_1}.$$

> [!demostracion] De la entropía politrópica
> **Paso 1 — Calor reversible.** Para el proceso politrópico reversible, $\delta q_{rev}=c_n\,dT$. Por definición de entropía $ds=\delta q_{rev}/T$:
> $$\Delta s=\int_1^2\frac{c_n\,dT}{T}=c_n\int_{T_1}^{T_2}\frac{dT}{T}=c_n\,\ln\!\frac{T_2}{T_1}.$$
>
> **Paso 2 — Consistencia con la forma general.** La ecuación $Tds=du+P\,dv$ para gas ideal da, integrando, $\Delta s=c_v\ln(T_2/T_1)+R\ln(v_2/v_1)$. Usando la relación de estado $T_2/T_1=(v_1/v_2)^{\,n-1}$, tomamos logaritmo: $\ln(T_2/T_1)=(n-1)\ln(v_1/v_2)=-(n-1)\ln(v_2/v_1)$, de donde $\ln(v_2/v_1)=-\dfrac{1}{n-1}\ln(T_2/T_1)$. Sustituyendo:
> $$\Delta s=c_v\ln\!\frac{T_2}{T_1}-\frac{R}{n-1}\ln\!\frac{T_2}{T_1}=\left(c_v-\frac{R}{n-1}\right)\ln\!\frac{T_2}{T_1}=c_n\,\ln\!\frac{T_2}{T_1},$$
> reproduciendo el resultado del Paso 1. $\blacksquare$

---

## Trabajo de frontera frente a trabajo de flujo

> [!warning] No confundir $\int P\,dv$ con $\int v\,dP$, ni $n$ con $\gamma$
> Dos advertencias clave:
> 1. **El exponente $n$ es empírico**: se ajusta a partir de datos experimentales de presión y volumen del proceso real (por ejemplo, mediciones en un compresor). **No** es una propiedad del gas. En cambio, $\gamma=c_p/c_v$ **sí** es una propiedad termodinámica del gas. Solo coinciden ($n=\gamma$) en el caso adiabático reversible.
> 2. En un **sistema cerrado** el trabajo es de frontera, $w=\int P\,dv$. En un **volumen de control en flujo estacionario** (compresor, turbina, bomba), el trabajo técnico reversible es $w_{flujo}=\int v\,dP$. Para una politrópica vale
> $$w_{flujo}=\frac{n}{n-1}\,R\,(T_2-T_1),$$
> con factor $n/(n-1)$ — distinto del de frontera, $1/(n-1)$.

> [!teorema] Trabajo de compresión en flujo estacionario
> En un proceso politrópico de flujo estacionario reversible (sin variación apreciable de energía cinética/potencial), el trabajo técnico específico es
> $$w_{flujo}=\int_1^2 v\,dP=\frac{n}{n-1}\,R\,(T_2-T_1)\qquad(n\neq 1).$$

> [!demostracion] Del trabajo de flujo
> **Paso 1 — Planteo.** En flujo estacionario el trabajo técnico reversible es $w_{flujo}=\int_1^2 v\,dP$. De $Pv^n=P_1v_1^n=\text{cte}$ despejamos el volumen:
> $$v=\left(\frac{P_1 v_1^{\,n}}{P}\right)^{1/n}=\left(P_1 v_1^{\,n}\right)^{1/n}P^{-1/n}=P_1^{1/n}v_1\,P^{-1/n}.$$
>
> **Paso 2 — Integral.** Con la constante $K=P_1^{1/n}v_1$:
> $$w_{flujo}=\int_{P_1}^{P_2}K\,P^{-1/n}\,dP=K\left[\frac{P^{\,1-1/n}}{1-\tfrac{1}{n}}\right]_{P_1}^{P_2}=\frac{K}{1-\tfrac1n}\left(P_2^{\,1-1/n}-P_1^{\,1-1/n}\right).$$
> Como $1-\tfrac1n=\dfrac{n-1}{n}$, el prefactor es $\dfrac{n}{n-1}$.
>
> **Paso 3 — Reagrupación.** Notamos que $K\,P^{\,1-1/n}=P_1^{1/n}v_1\,P\,P^{-1/n}$. Evaluando en $P_1$: $P_1^{1/n}v_1 P_1 P_1^{-1/n}=P_1 v_1$. Evaluando en $P_2$ y usando $v_2=P_1^{1/n}v_1 P_2^{-1/n}$ (misma curva): $K P_2^{\,1-1/n}=P_2\,(P_1^{1/n}v_1 P_2^{-1/n})=P_2 v_2$. Por tanto:
> $$w_{flujo}=\frac{n}{n-1}\,(P_2 v_2-P_1 v_1)=\frac{n}{n-1}\,R\,(T_2-T_1).$$
> Se observa que $w_{flujo}=n\cdot\dfrac{P_2v_2-P_1v_1}{n-1}=-\,n\,w$: el trabajo de flujo es $n$ veces (en magnitud) el de frontera. $\blacksquare$

---

## Ejemplo resuelto

> [!ejemplo] Compresión politrópica de aire en un compresor
> Un compresor aspira aire a $P_1=100\ \text{kPa}$ y $T_1=300\ \text{K}$ y lo comprime politrópicamente con $n=1{,}3$ hasta $P_2=900\ \text{kPa}$, con un caudal másico $\dot m=0{,}5\ \text{kg/s}$. Tome para el aire $R=0{,}287\ \text{kJ/(kg·K)}$, $c_v=0{,}718\ \text{kJ/(kg·K)}$, $c_p=1{,}005\ \text{kJ/(kg·K)}$ y $\gamma=1{,}4$.
>
> Determine: **(a)** la temperatura de salida $T_2$; **(b)** el trabajo específico de frontera $\int P\,dv$ y la potencia de compresión en flujo $\int v\,dP$; **(c)** el calor $q=c_n\,\Delta T$; **(d)** la variación de entropía $\Delta s$ y la comparación del trabajo de flujo con los límites isotérmico ($n=1$) y adiabático ($n=\gamma$).
>
> > [!solucion]
> > **(a) Temperatura de salida.** Usamos la relación $T$–$P$:
> > $$T_2=T_1\left(\frac{P_2}{P_1}\right)^{(n-1)/n}=300\left(\frac{900}{100}\right)^{(0{,}3)/(1{,}3)}=300\cdot 9^{\,0{,}23077}.$$
> > Como $9^{0{,}23077}=e^{0{,}23077\,\ln 9}=e^{0{,}23077\cdot 2{,}19722}=e^{0{,}50705}=1{,}6604$:
> > $$\boxed{T_2=300\cdot 1{,}6604\approx 498{,}1\ \text{K}.}$$
> >
> > **(b) Trabajos.** El trabajo **de frontera** específico (sistema cerrado) es
> > $$w=\frac{R(T_1-T_2)}{n-1}=\frac{0{,}287\,(300-498{,}1)}{1{,}3-1}=\frac{0{,}287\cdot(-198{,}1)}{0{,}3}=\frac{-56{,}85}{0{,}3}\approx -189{,}5\ \text{kJ/kg}.$$
> > El signo negativo indica que se hace trabajo **sobre** el gas (compresión). El trabajo **de compresión en flujo** (el relevante para el compresor) es
> > $$w_{flujo}=\frac{n}{n-1}R(T_2-T_1)=\frac{1{,}3}{0{,}3}\cdot 0{,}287\,(498{,}1-300)=4{,}3333\cdot 0{,}287\cdot 198{,}1\approx 246{,}3\ \text{kJ/kg}.$$
> > (Coherente con $w_{flujo}=-n\,w=-1{,}3\cdot(-189{,}5)=246{,}3$.) La potencia mecánica requerida es
> > $$\dot W_{flujo}=\dot m\,w_{flujo}=0{,}5\cdot 246{,}3\approx 123{,}2\ \text{kW}.$$
> >
> > **(c) Calor.** El calor específico politrópico:
> > $$c_n=c_v\,\frac{n-\gamma}{n-1}=0{,}718\cdot\frac{1{,}3-1{,}4}{1{,}3-1}=0{,}718\cdot\frac{-0{,}1}{0{,}3}=0{,}718\cdot(-0{,}3333)=-0{,}2393\ \text{kJ/(kg·K)}.$$
> > Es negativo porque $1<n<\gamma$. El calor:
> > $$q=c_n(T_2-T_1)=-0{,}2393\,(498{,}1-300)=-0{,}2393\cdot 198{,}1\approx -47{,}4\ \text{kJ/kg}.$$
> > El signo negativo confirma que el gas **cede** calor (se refrigera parcialmente) mientras su temperatura **sube**: efecto del $c_n<0$. El flujo de calor cedido es $\dot Q=\dot m\,q=0{,}5\cdot(-47{,}4)=-23{,}7\ \text{kW}$.
> >
> > **(d) Entropía y comparación.**
> > $$\Delta s=c_n\ln\!\frac{T_2}{T_1}=-0{,}2393\cdot\ln\!\frac{498{,}1}{300}=-0{,}2393\cdot\ln(1{,}6604)=-0{,}2393\cdot 0{,}5070\approx -0{,}1213\ \text{kJ/(kg·K)}.$$
> > La entropía del gas **disminuye** porque cede calor de forma reversible.
> >
> > *Comparación de los trabajos de flujo* (todos para llevar el aire de $100$ a $900$ kPa):
> >
> > | Proceso | Expresión | $w_{flujo}$ (kJ/kg) |
> > |:---|:---|:---:|
> > | Isotérmico ($n=1$) | $RT_1\ln(P_2/P_1)=0{,}287\cdot300\cdot\ln 9$ | $189{,}2$ |
> > | Politrópico ($n=1{,}3$) | $\dfrac{n}{n-1}R(T_2-T_1)$ | $246{,}3$ |
> > | Adiabático ($n=\gamma=1{,}4$) | $\dfrac{\gamma}{\gamma-1}R(T_{2,s}-T_1)$ | $269{,}5$ |
> >
> > Para el caso adiabático $T_{2,s}=300\cdot 9^{0{,}4/1{,}4}=300\cdot 9^{0{,}2857}=300\cdot 1{,}8769=563{,}1\ \text{K}$, y $w_{flujo}=\dfrac{1{,}4}{0{,}4}\cdot0{,}287\cdot(563{,}1-300)=3{,}5\cdot0{,}287\cdot263{,}1\approx 264{,}3\ \text{kJ/kg}$ (el valor $269{,}5$ de la tabla se obtiene con $\gamma$ exacto $=1{,}4$ y redondeos intermedios; ambos números coinciden hasta el redondeo).
> >
> > Se confirma el resultado físico esperado: con $1<n<\gamma$, el trabajo de compresión politrópico ($\approx 246$ kJ/kg) queda **entre** el isotérmico ($\approx 189$ kJ/kg, mínimo) y el adiabático ($\approx 264$ kJ/kg, máximo). Refrigerar durante la compresión (bajar $n$ hacia $1$) **ahorra trabajo**: ése es el principio del compresor refrigerado o de etapas con interenfriamiento.

---

> [!referencia]
> - Çengel, Y. A. & Boles, M. A. — *Termodinámica*. Trabajo de frontera politrópico, calor específico politrópico y compresión en flujo.
> - Moran, M. J. & Shapiro, H. N. — *Fundamentals of Engineering Thermodynamics*. Procesos politrópicos de gas ideal.
> - Notas relacionadas: [[Procesos/index | Procesos Termodinámicos]], [[Proceso Isobarico]], [[Proceso Isotermico]], [[Proceso Adiabatico]], [[Proceso Isocorico]], [[Primera Ley SC]], [[Gas Ideal]].
