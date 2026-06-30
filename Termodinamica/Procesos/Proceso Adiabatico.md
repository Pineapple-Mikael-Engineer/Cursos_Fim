---
title: Proceso Adiabático
order: 5
tags:
  - termodinamica
  - teoria
  - procesos
draft: false
aliases:
  - Proceso adiabático
  - Proceso isentrópico
  - Proceso adiabático reversible
---

# Proceso Adiabático $q=0,\quad Pv^\gamma=\text{cte}$

> [!definicion]
> Un **proceso adiabático** es aquel en el que el sistema no intercambia calor con su entorno:
> $$
> q = 0 \qquad (\delta q = 0 \text{ en todo el proceso}).
> $$
> Esto ocurre en dos situaciones físicas típicas:
> - El sistema está **térmicamente aislado** (paredes adiabáticas, p. ej. recubiertas de material aislante).
> - El proceso es **muy rápido** comparado con el tiempo característico de la transferencia de calor (compresiones y expansiones súbitas en compresores, turbinas y toberas), de modo que no hay tiempo para que fluya calor apreciable.
>
> Aplicando la [[Primera Ley SC | Primera Ley para sistemas cerrados]] $\Delta u = q - w$ con $q=0$:
> $$
> \boxed{\,w = -\,\Delta u\,}
> $$
> es decir, **todo el trabajo se realiza a costa de la energía interna**: si el gas se expande ($w>0$), su energía interna baja y se enfría; si se comprime ($w<0$), su energía interna sube y se calienta.

> [!info]
> Esta nota pertenece a la sección [[Procesos/index | Procesos Termodinámicos]]. Sus hermanas son [[Proceso Isotermico]], [[Proceso Politropico]] y [[Proceso Isobarico]]. Usaremos resultados de [[Primera Ley SC | Primera Ley]], [[Entropia | Entropía]] y [[Gas Ideal]] (donde $Pv=RT$ y $\gamma=c_p/c_v$).

---

## 1. La relación $Pv^\gamma=\text{cte}$

> [!teorema]
> Para un proceso **adiabático reversible** de un [[Gas Ideal | gas ideal]] con calores específicos constantes se cumplen las tres formas equivalentes:
> $$
> Tv^{\gamma-1} = \text{cte}, \qquad Pv^{\gamma} = \text{cte}, \qquad TP^{(1-\gamma)/\gamma} = \text{cte},
> $$
> donde $\gamma = c_p/c_v$ es el coeficiente adiabático.

> [!demostracion]
> Partimos de la forma diferencial de la [[Primera Ley SC | Primera Ley]] para un proceso cuasiestático sin otros trabajos que el de frontera $\delta w = P\,dv$:
> $$
> du = \delta q - \delta w = \delta q - P\,dv.
> $$
>
> **Paso 1 — Imponer la condición adiabática.** Como $\delta q = 0$,
> $$
> du = -P\,dv.
> $$
>
> **Paso 2 — Sustituir la energía interna del gas ideal.** Para un gas ideal $du = c_v\,dT$, de modo que
> $$
> c_v\,dT = -P\,dv.
> $$
>
> **Paso 3 — Eliminar la presión con la ecuación de estado.** De $Pv = RT$ se tiene $P = RT/v$. Entonces
> $$
> c_v\,dT = -\frac{RT}{v}\,dv.
> $$
>
> **Paso 4 — Separar variables.** Dividimos entre $T$ (ambos miembros) para agrupar cada variable en un lado:
> $$
> \frac{c_v}{T}\,dT = -\frac{R}{v}\,dv
> \quad\Longrightarrow\quad
> \frac{dT}{T} = -\frac{R}{c_v}\,\frac{dv}{v}.
> $$
>
> **Paso 5 — Reescribir el coeficiente $R/c_v$ con $\gamma$.** Para el gas ideal vale la relación de Mayer $R = c_p - c_v$. Dividiendo entre $c_v$:
> $$
> \frac{R}{c_v} = \frac{c_p - c_v}{c_v} = \frac{c_p}{c_v} - 1 = \gamma - 1.
> $$
> Por tanto
> $$
> \frac{dT}{T} = -(\gamma-1)\,\frac{dv}{v}.
> $$
>
> **Paso 6 — Integrar entre el estado 1 y el estado 2.**
> $$
> \int_{T_1}^{T_2}\frac{dT}{T} = -(\gamma-1)\int_{v_1}^{v_2}\frac{dv}{v}
> \quad\Longrightarrow\quad
> \ln\frac{T_2}{T_1} = -(\gamma-1)\ln\frac{v_2}{v_1} = (\gamma-1)\ln\frac{v_1}{v_2}.
> $$
> Tomando exponencial y reordenando,
> $$
> \frac{T_2}{T_1} = \left(\frac{v_1}{v_2}\right)^{\gamma-1}
> \quad\Longrightarrow\quad
> T_2\,v_2^{\,\gamma-1} = T_1\,v_1^{\,\gamma-1}
> \quad\Longrightarrow\quad
> \boxed{\,Tv^{\gamma-1} = \text{cte}\,}.
> $$
>
> **Paso 7 — Pasar a la forma $Pv^\gamma$.** Sustituimos $T = Pv/R$ en $Tv^{\gamma-1}=\text{cte}$:
> $$
> \frac{Pv}{R}\,v^{\gamma-1} = \text{cte}
> \quad\Longrightarrow\quad
> \frac{P\,v^{\gamma}}{R} = \text{cte}
> \quad\Longrightarrow\quad
> \boxed{\,Pv^{\gamma} = \text{cte}\,}.
> $$
>
> **Paso 8 — Pasar a la forma $TP^{(1-\gamma)/\gamma}$.** De $Pv^\gamma=\text{cte}$ despejamos $v = (\text{cte}/P)^{1/\gamma}\propto P^{-1/\gamma}$ y lo metemos en $Tv^{\gamma-1}=\text{cte}$:
> $$
> T\left(P^{-1/\gamma}\right)^{\gamma-1} = \text{cte}
> \quad\Longrightarrow\quad
> T\,P^{-(\gamma-1)/\gamma} = \text{cte}
> \quad\Longrightarrow\quad
> \boxed{\,T\,P^{(1-\gamma)/\gamma} = \text{cte}\,}.
> $$
> Las tres expresiones son equivalentes; se usa la más cómoda según las variables dato. $\blacksquare$

> [!info]
> En la práctica, la forma más usada para relacionar estados es
> $$
> \frac{T_2}{T_1} = \left(\frac{P_2}{P_1}\right)^{(\gamma-1)/\gamma} = \left(\frac{v_1}{v_2}\right)^{\gamma-1}.
> $$
> Para aire diatómico $\gamma = 1{,}4$, de modo que el exponente $(\gamma-1)/\gamma = 0{,}4/1{,}4 \approx 0{,}2857$.

---

## 2. El proceso adiabático reversible es isentrópico

> [!proposicion]
> Un proceso **adiabático y reversible** es **isentrópico**: $\Delta s = 0$.

> [!demostracion]
> La variación de [[Entropia | entropía]] para un proceso reversible se define por
> $$
> ds = \frac{\delta q_{rev}}{T}.
> $$
>
> **Paso 1 —** Por ser adiabático, $\delta q_{rev} = 0$ en cada etapa del camino.
>
> **Paso 2 —** Entonces $ds = 0/T = 0$ a lo largo de todo el proceso.
>
> **Paso 3 —** Integrando entre los estados extremos,
> $$
> \Delta s = \int_1^2 ds = 0
> \quad\Longrightarrow\quad
> \boxed{\,s_2 = s_1\,}.
> $$
> Por eso al adiabático reversible se le llama **isentrópico**. En un diagrama $T$–$s$ corresponde a una **recta vertical** ($s=\text{cte}$). $\blacksquare$

> [!warning]
> **Adiabático no es sinónimo de isentrópico.** La condición $q=0$ por sí sola no implica $\Delta s=0$. Para un proceso adiabático **real con irreversibilidades** (fricción, gradientes finitos, turbulencia) el balance de entropía da
> $$
> \Delta s = \underbrace{\int \frac{\delta q}{T}}_{=\,0} + s_{gen} = s_{gen} > 0.
> $$
> Es decir, un adiabático irreversible tiene $q=0$ **pero** $\Delta s>0$. Solo el adiabático **reversible** es isentrópico. Consecuencia técnica: respecto al caso ideal isentrópico, una turbina adiabática real produce **menos** trabajo y un compresor adiabático real exige **más** trabajo.

---

## 3. Trabajo en el proceso adiabático

> [!teorema]
> El trabajo de frontera en un proceso adiabático de un gas ideal vale
> $$
> w = -\Delta u = c_v\,(T_1 - T_2) = \frac{P_1 v_1 - P_2 v_2}{\gamma - 1} = \frac{R\,(T_1 - T_2)}{\gamma - 1}.
> $$

> [!demostracion]
> **Paso 1 — Desde la Primera Ley.** Con $q=0$ ya vimos que $w = -\Delta u$. Para el gas ideal $\Delta u = c_v\,(T_2 - T_1)$, por tanto
> $$
> w = -c_v\,(T_2 - T_1) = c_v\,(T_1 - T_2).
> $$
>
> **Paso 2 — Escribir $c_v$ en función de $R$ y $\gamma$.** De $R = c_p - c_v$ y $\gamma = c_p/c_v$ se obtiene $c_p = \gamma c_v$, luego
> $$
> R = \gamma c_v - c_v = (\gamma-1)\,c_v
> \quad\Longrightarrow\quad
> c_v = \frac{R}{\gamma-1}.
> $$
> Sustituyendo:
> $$
> w = \frac{R\,(T_1 - T_2)}{\gamma - 1}.
> $$
>
> **Paso 3 — Pasar a presiones y volúmenes.** Usando $RT_1 = P_1 v_1$ y $RT_2 = P_2 v_2$,
> $$
> w = \frac{R T_1 - R T_2}{\gamma-1} = \frac{P_1 v_1 - P_2 v_2}{\gamma - 1}.
> $$
> Quedan así establecidas las cuatro formas equivalentes. $\blacksquare$

> [!info]
> El mismo resultado se obtiene integrando directamente $w=\int_1^2 P\,dv$ con $P = C\,v^{-\gamma}$ (siendo $C=P_1v_1^\gamma=P_2v_2^\gamma$):
> $$
> w = \int_{v_1}^{v_2} C\,v^{-\gamma}\,dv = C\,\frac{v^{1-\gamma}}{1-\gamma}\Bigg|_{v_1}^{v_2}
> = \frac{C v_2^{1-\gamma} - C v_1^{1-\gamma}}{1-\gamma} = \frac{P_2 v_2 - P_1 v_1}{1-\gamma} = \frac{P_1 v_1 - P_2 v_2}{\gamma-1}.
> $$

---

## 4. Comparación con la isoterma en el plano $P$–$v$

![[adiabatico_pv_ts.svg|520]]
*Adiabática reversible de un gas ideal. Izquierda ($P$–$v$): la curva $Pv^\gamma=\text{cte}$ es una hipérbola más empinada que la isoterma $Pv=\text{cte}$; el área bajo la curva es el trabajo $w$. Derecha ($T$–$s$): el proceso isentrópico es una recta vertical ($q=0$, $s=\text{cte}$).*

> [!proposicion]
> En el plano $P$–$v$, la curva adiabática es **más empinada** que la isoterma que pasa por el mismo punto, en un factor $\gamma$.

> [!demostracion]
> **Paso 1 — Pendiente de la isoterma.** Para [[Proceso Isotermico | la isoterma]] $Pv=\text{cte}$, diferenciando: $P\,dv + v\,dP = 0$, de donde
> $$
> \left(\frac{dP}{dv}\right)_T = -\frac{P}{v}.
> $$
>
> **Paso 2 — Pendiente de la adiabática.** Para $Pv^\gamma=\text{cte}$, diferenciando: $v^\gamma\,dP + P\,\gamma v^{\gamma-1}\,dv = 0$, de donde
> $$
> \left(\frac{dP}{dv}\right)_s = -\gamma\,\frac{P}{v}.
> $$
>
> **Paso 3 — Comparar.** En un mismo punto $(P,v)$,
> $$
> \left(\frac{dP}{dv}\right)_s = \gamma\left(\frac{dP}{dv}\right)_T,
> $$
> y como $\gamma>1$, la pendiente adiabática (en valor absoluto) es $\gamma$ veces mayor: **la adiabática cae más rápido**. $\blacksquare$

---

## 5. Ejemplo: compresión adiabática en un compresor

> [!ejemplo]
> Un compresor de flujo estacionario aspira **aire** a $P_1 = 100\ \text{kPa}$ y $T_1 = 300\ \text{K}$ y lo comprime hasta $P_2 = 800\ \text{kPa}$. El equipo se considera **adiabático**. Tome $c_p = 1{,}005\ \text{kJ/(kg·K)}$, $R = 0{,}287\ \text{kJ/(kg·K)}$ y $\gamma = 1{,}4$. Se pide: a) la temperatura de salida **isentrópica** $T_{2s}$; b) el trabajo **isentrópico** $w_s$; c) si la **eficiencia isentrópica** del compresor es $\eta_s = 0{,}82$, la temperatura real de salida $T_2$ y el trabajo real $w_{real}$; d) la **entropía generada** $s_{gen}$ en el proceso real.

> [!solucion]
> Como es un volumen de control en flujo estacionario, la primera ley por unidad de masa (despreciando energías cinética y potencial) es $q - w = h_2 - h_1$; siendo adiabático ($q=0$):
> $$
> w = h_1 - h_2 = c_p\,(T_1 - T_2).
> $$
> Aquí $w$ es trabajo **de salida** del sistema; en un compresor el sistema recibe trabajo, así que $w<0$. Trabajaremos con la magnitud de **entrada** $w_{c} = -w = c_p(T_2 - T_1)>0$.
>
> **a) Temperatura isentrópica de salida.** El caso ideal es adiabático **y** reversible, luego isentrópico. Usamos la relación demostrada en la sección 1:
> $$
> T_{2s} = T_1\left(\frac{P_2}{P_1}\right)^{(\gamma-1)/\gamma}.
> $$
> El exponente es $(\gamma-1)/\gamma = 0{,}4/1{,}4 = 0{,}285714$ y la razón de presiones $P_2/P_1 = 8$:
> $$
> T_{2s} = 300\cdot 8^{\,0{,}285714} = 300\cdot 1{,}81147 = 543{,}4\ \text{K}.
> $$
>
> **b) Trabajo isentrópico.** Con $h=c_pT$,
> $$
> w_{c,s} = c_p\,(T_{2s} - T_1) = 1{,}005\,(543{,}4 - 300) = 1{,}005\cdot 243{,}4 = 244{,}6\ \text{kJ/kg}.
> $$
> Equivalentemente $w_s = h_1 - h_{2s} = -244{,}6\ \text{kJ/kg}$ (sale negativo porque se aporta trabajo al gas).
>
> **c) Caso real con eficiencia isentrópica.** Para un **compresor**, la eficiencia isentrópica compara el trabajo ideal (mínimo) con el real:
> $$
> \eta_s = \frac{w_{c,s}}{w_{c,real}} = \frac{h_{2s} - h_1}{h_2 - h_1} = \frac{T_{2s} - T_1}{T_2 - T_1}.
> $$
> El proceso real exige **más** trabajo, luego
> $$
> w_{c,real} = \frac{w_{c,s}}{\eta_s} = \frac{244{,}6}{0{,}82} = 298{,}3\ \text{kJ/kg}.
> $$
> La temperatura real de salida se obtiene de $w_{c,real}=c_p(T_2-T_1)$:
> $$
> T_2 = T_1 + \frac{w_{c,real}}{c_p} = 300 + \frac{298{,}3}{1{,}005} = 300 + 296{,}8 = 596{,}8\ \text{K}.
> $$
> Como era de esperar, $T_2 = 596{,}8\ \text{K} > T_{2s} = 543{,}4\ \text{K}$: las irreversibilidades calientan más el aire para una misma presión de salida.
>
> **d) Entropía generada del proceso real.** El proceso real es adiabático ($q=0$) pero irreversible, así que $s_{gen} = \Delta s = s_2 - s_1$. Para un gas ideal de $c_p$ constante:
> $$
> s_{gen} = c_p\ln\frac{T_2}{T_1} - R\ln\frac{P_2}{P_1}.
> $$
> Numéricamente, con $T_2/T_1 = 596{,}8/300 = 1{,}9893$ y $P_2/P_1 = 8$:
> $$
> s_{gen} = 1{,}005\,\ln(1{,}9893) - 0{,}287\,\ln(8)
> = 1{,}005\cdot 0{,}68775 - 0{,}287\cdot 2{,}07944,
> $$
> $$
> s_{gen} = 0{,}69119 - 0{,}59680 = 0{,}0944\ \text{kJ/(kg·K)} > 0.
> $$
> El signo positivo confirma la segunda ley: el proceso real **genera** entropía. En el caso isentrópico (ideal) sería $s_{gen}=0$, lo que da exactamente $T_{2s}=543{,}4\ \text{K}$ resolviendo $c_p\ln(T_{2s}/T_1)=R\ln(P_2/P_1)$ — el mismo resultado del apartado (a). $\blacksquare$

> [!info]
> Lectura física del ejemplo: el caso **ideal** (isentrópico) fija el límite teórico del menor trabajo posible para esa relación de compresión; el caso **real** se aparta de él según $\eta_s$, gastando trabajo extra que termina como entropía generada y como mayor temperatura de salida.
