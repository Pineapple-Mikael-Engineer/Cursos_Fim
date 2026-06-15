---
title: Procesos Reversibles e Irreversibles
tags:
  - termodinamica
  - teoria
  - procesos
draft: false
aliases:
  - Procesos reversibles e irreversibles
  - Reversibilidad
  - Irreversibilidad
---

# Procesos Reversibles e Irreversibles $S_{gen}\ge 0$

> [!definicion]
> Un proceso es **reversible** si, una vez ejecutado, puede invertirse de modo que tanto el **sistema** como el **entorno** regresen a sus estados iniciales **sin dejar rastro neto** en ninguno de los dos. Si el sistema vuelve pero el entorno no, o viceversa, el proceso es irreversible.
>
> - **Internamente reversible**: no hay irreversibilidades **dentro** de la frontera del sistema. El proceso es cuasiestático (sucesión de estados de equilibrio), sin fricción interna, sin gradientes finitos de presión ni de temperatura dentro del sistema. Puede haber irreversibilidad en el entorno (p. ej. una transferencia de calor con $\Delta T$ finito en la frontera).
> - **Totalmente (externamente) reversible**: internamente reversible **y** sin irreversibilidades en el entorno.
> - **Irreversible**: todo proceso **real**. Las **fuentes de irreversibilidad** son la **fricción**, la **expansión libre**, la **transferencia de calor a través de una diferencia de temperatura finita**, la **mezcla** de sustancias y las **reacciones químicas**.
>
> El indicador cuantitativo de la irreversibilidad es la **generación de entropía** $S_{gen}\ge 0$, nula solo en el límite reversible.

> [!info]
> Esta nota pertenece a la sección [[Procesos/index | Procesos Termodinámicos]]. Notas hermanas: [[Proceso Isotermico]] y [[Proceso Adiabatico]]. La maquinaria que justifica $S_{gen}\ge 0$ está en [[Segunda Ley SC]] y en [[Entropia]]; la lectura del coste de la irreversibilidad como trabajo perdido se desarrolla en [[Balance de Exergia SC]].
> Convenio: gas ideal $Pv=RT$ (base másica, $R$ constante específica), trabajo de frontera por unidad de masa $w=\int P\,dv$, calor $q$, $\delta Q/T$ evaluado en la frontera.

---

## 1. Cuasiestático implica trayectoria definida

> [!teoria]
> Solo un proceso **cuasiestático** (sucesión continua de estados de equilibrio interno) posee una **curva** bien definida en el plano $P$–$v$, y por tanto un trabajo de frontera
> $$ w=\int_{1}^{2} P\,dv $$
> con valor inequívoco. En un proceso **brusco** (rápido, real) el sistema no está en equilibrio: la presión no es uniforme, no existe un único valor de $P$ para todo el sistema y los estados intermedios **no son puntos** del diagrama. La "trayectoria" deja de estar definida y la integral $\int P\,dv$ pierde sentido como propiedad del sistema.

**Consecuencia operativa.** En un proceso irreversible el trabajo se calcula con la presión que actúa **en la frontera móvil**, es decir la presión externa $P_{ext}$ que el sistema vence (o que vence al sistema):
$$ w=\int_{1}^{2} P_{ext}\,dv .$$
Solo cuando el proceso es internamente reversible se cumple $P_{ext}=P$ en todo instante y entonces $w_{rev}=\int P\,dv$.

---

## 2. El trabajo reversible es el extremo

> [!teorema]
> Entre dos estados de volumen $v_1$ y $v_2$, el trabajo de frontera reversible es **extremo**:
> - En una **expansión** ($v_2>v_1$): $\quad w_{rev}=\displaystyle\int_{1}^{2}P\,dv \;>\; w_{irrev}=\displaystyle\int_{1}^{2}P_{ext}\,dv.$ El trabajo útil obtenido es **máximo** en el límite reversible.
> - En una **compresión** ($v_2<v_1$): $\quad w_{rev}<w_{irrev}.$ El trabajo que hay que **aportar** es **mínimo** en el límite reversible.

> [!demostracion]
> **Paso 1 — Modelo de la presión externa.** Para que el émbolo se mueva en un proceso real hace falta un **desequilibrio finito** entre la presión interna $P$ y la presión que actúa en la frontera, además de vencer la **fricción**. Escribimos
> $$ P_{ext}=P\mp\varepsilon,\qquad \varepsilon>0,$$
> donde $\varepsilon$ engloba el desequilibrio mecánico y la fricción. El signo se fija por la dirección del movimiento.
>
> **Paso 2 — Expansión.** Para que el gas **se expanda** ($dv>0$) la presión externa debe ser **menor** que la interna; el sistema empuja contra una resistencia inferior:
> $$ P_{ext}=P-\varepsilon \;<\; P.$$
> Integrando con $dv>0$:
> $$ w_{irrev}=\int_{1}^{2}(P-\varepsilon)\,dv=\int_{1}^{2}P\,dv-\int_{1}^{2}\varepsilon\,dv= w_{rev}-\underbrace{\int_{1}^{2}\varepsilon\,dv}_{>0}.$$
> Por tanto $w_{irrev}<w_{rev}$. El trabajo entregado por el sistema es **máximo** cuando $\varepsilon\to 0$, esto es, en el límite reversible.
>
> **Paso 3 — Compresión.** Para **comprimir** el gas ($dv<0$) hay que aplicar una presión externa **mayor** que la interna:
> $$ P_{ext}=P+\varepsilon \;>\; P.$$
> El trabajo recibido por el sistema (entrante) es $|w|=\int |P_{ext}|\,|dv|$. Con la convención $w=\int P_{ext}\,dv$ y $dv<0$, el trabajo que **debe aportar el entorno** es
> $$ w_{ent}=-\int_{1}^{2}(P+\varepsilon)\,dv= -\int_{1}^{2}P\,dv-\int_{1}^{2}\varepsilon\,dv = w_{ent,rev}+\underbrace{\Big(-\int_{1}^{2}\varepsilon\,dv\Big)}_{>0\ \text{pues } dv<0}.$$
> Es decir $w_{ent}>w_{ent,rev}$: **comprimir irreversiblemente cuesta más trabajo**. Equivalentemente $w_{rev}<w_{irrev}$ en la convención del sistema.
>
> **Paso 4 — Conclusión.** El término $\int\varepsilon\,dv\ge 0$ es la "penalización" de la irreversibilidad, y se anula solo cuando $\varepsilon\to 0$. Luego el **trabajo útil máximo** (expansión) y el **trabajo aportado mínimo** (compresión) se alcanzan en el **límite reversible**. $\blacksquare$

---

## 3. Generación de entropía

> [!teorema]
> Para un sistema **cerrado** que evoluciona del estado $1$ al estado $2$, el **balance de entropía** es
> $$ \boxed{\;\Delta S=S_2-S_1=\int_{1}^{2}\frac{\delta Q}{T}+S_{gen},\qquad S_{gen}\ge 0\;}$$
> donde $T$ es la temperatura de la frontera por donde entra $\delta Q$. La igualdad $S_{gen}=0$ ocurre **si y solo si** el proceso es reversible; $S_{gen}>0$ para todo proceso irreversible. $S_{gen}$ es una medida directa de la irreversibilidad.

> [!demostracion]
> **Paso 1 — Desigualdad de Clausius.** De la [[Segunda Ley SC]], para todo ciclo
> $$ \oint\frac{\delta Q}{T}\le 0,$$
> con igualdad solo si el ciclo es reversible.
>
> **Paso 2 — Definición de entropía.** Para un proceso **reversible**, $dS\equiv\delta Q_{rev}/T$ es diferencial exacta, de modo que $S$ es una **propiedad** (ver [[Entropia]]) y $\Delta S$ depende solo de los estados.
>
> **Paso 3 — Ciclo mixto.** Consideramos un ciclo formado por el proceso real $1\to 2$ (irreversible) y un regreso $2\to 1$ por un camino reversible. Aplicando el Paso 1:
> $$ \int_{1}^{2}\frac{\delta Q}{T}+\int_{2}^{1}\Big(\frac{\delta Q}{T}\Big)_{rev}\le 0.$$
> Como $\int_{2}^{1}(\delta Q/T)_{rev}=S_1-S_2$, se sigue
> $$ \int_{1}^{2}\frac{\delta Q}{T}\le S_2-S_1.$$
>
> **Paso 4 — Cierre del balance.** Definimos $S_{gen}$ como la cantidad **no negativa** que restablece la igualdad:
> $$ S_2-S_1=\int_{1}^{2}\frac{\delta Q}{T}+S_{gen},\qquad S_{gen}\ge 0.$$
> Del Paso 3, $S_{gen}=(S_2-S_1)-\int\delta Q/T\ge 0$, y vale $0$ exactamente cuando el ciclo (y por tanto el tramo real) es reversible. $\blacksquare$

> [!regla]
> **Cómo se lee el balance.** El término $\int\delta Q/T$ es **transporte** de entropía por calor (puede ser positivo o negativo). $S_{gen}\ge 0$ es **producción interna**, nunca destrucción. Para un sistema **adiabático** ($\delta Q=0$) queda $\Delta S=S_{gen}\ge 0$: la entropía de un sistema aislado nunca disminuye.

---

## 4. El contraste central: tres caminos entre los mismos estados

> [!ejemplo]
> Un gas ideal evoluciona del estado $1$ al estado $2$ a la **misma temperatura** $T$ (proceso isotérmico global), expandiéndose desde $P_1$ hasta $P_2<P_1$, con $v_2/v_1=P_1/P_2$. Recorre los **mismos estados extremos** por tres caminos distintos:
> (a) expansión **isotérmica reversible**; (b) **expansión libre** de Joule contra el vacío; (c) expansión **contra presión externa constante** $P_{ext}=P_2$, con calor intercambiado con una fuente a $T_{fuente}=T$.
> Comparar $w$, $q$, $\Delta s_{sis}$ y $S_{gen}$ en los tres casos.

> [!solucion]
> Como $s$ es **propiedad** y los tres caminos unen los mismos estados $1$ y $2$, el cambio de entropía del sistema es **idéntico** en los tres. Para gas ideal isotérmico, de $T\,ds=du+P\,dv$ con $du=0$ ($u=u(T)$) y $P=RT/v$:
> $$ \Delta s_{sis}=\int_{1}^{2}\frac{P}{T}\,dv=\int_{1}^{2}\frac{R}{v}\,dv=R\ln\frac{v_2}{v_1}=R\ln\frac{P_1}{P_2}>0.$$
>
> **Paso a — Expansión isotérmica reversible.**
> El trabajo de frontera, con $P=RT/v$:
> $$ w_{rev}=\int_{1}^{2}P\,dv=RT\int_{1}^{2}\frac{dv}{v}=RT\ln\frac{v_2}{v_1}.$$
> Como $\Delta u=0$, la primera ley da $q_{rev}=\Delta u+w_{rev}=w_{rev}=RT\ln(v_2/v_1)>0$.
> El calor se intercambia con una fuente a $T_{fuente}=T$ (igual temperatura, $\Delta T\to 0$), luego es **internamente y externamente reversible**:
> $$ S_{gen}^{(a)}=\Delta s_{sis}-\frac{q_{rev}}{T_{fuente}}=R\ln\frac{v_2}{v_1}-\frac{RT\ln(v_2/v_1)}{T}=0.$$
>
> **Paso b — Expansión libre (Joule) contra el vacío.**
> El gas se expande en un recipiente **rígido y aislado** que contenía vacío. No hay frontera móvil que empuje nada: $w=0$. Por ser aislado, $q=0$. La primera ley da
> $$ \Delta u=q-w=0 \ \Rightarrow\ u_2=u_1\ \Rightarrow\ T_2=T_1=T$$
> (para gas ideal $u=u(T)$). Aunque $w=q=0$, el cambio de entropía es el de propiedad:
> $$ \Delta s_{sis}=R\ln\frac{v_2}{v_1}>0.$$
> Como $q=0$, todo el cambio es generación:
> $$ S_{gen}^{(b)}=\Delta s_{sis}-\frac{q}{T}=R\ln\frac{v_2}{v_1}=\Delta s_{sis}.$$
> Es el caso de **máxima irreversibilidad**: misma variación de estado, cero trabajo aprovechado y toda la entropía generada internamente.
>
> **Paso c — Expansión contra $P_{ext}=P_2$ constante.**
> El émbolo vence una presión externa fija $P_2$. El trabajo de frontera es
> $$ w_{c}=\int_{1}^{2}P_{ext}\,dv=P_2\,(v_2-v_1).$$
> Usando $v=RT/P$: $\;v_2-v_1=RT\big(\tfrac{1}{P_2}-\tfrac{1}{P_1}\big)$, luego
> $$ w_{c}=P_2\,RT\Big(\frac{1}{P_2}-\frac{1}{P_1}\Big)=RT\Big(1-\frac{P_2}{P_1}\Big)<w_{rev}.$$
> Como $\Delta u=0$ (isotérmico, gas ideal), la primera ley da $q_c=w_c=RT\big(1-\tfrac{P_2}{P_1}\big)$.
> El cambio de entropía del sistema es el de propiedad, **igual que en (a)**:
> $$ \Delta s_{sis}=R\ln\frac{v_2}{v_1}.$$
> El calor entra desde una fuente a $T_{fuente}=T$, así que
> $$ S_{gen}^{(c)}=\Delta s_{sis}-\frac{q_c}{T_{fuente}}=R\ln\frac{v_2}{v_1}-R\Big(1-\frac{P_2}{P_1}\Big)>0.$$
> La positividad se ve porque $\ln(v_2/v_1)=\ln(P_1/P_2)>1-P_2/P_1$ para $P_1>P_2$ (la cuerda queda por debajo del logaritmo).

> [!solucion]
> **Tabla comparativa numérica.** Tomamos $R=0{,}287\ \text{kJ/(kg·K)}$ (aire), $T=300\ \text{K}$, $P_1=200\ \text{kPa}$, $P_2=100\ \text{kPa}$, de modo que $v_2/v_1=P_1/P_2=2$ y $\ln 2=0{,}6931$.
>
> Valores base: $\;RT=86{,}10\ \text{kJ/kg}$, $\;\Delta s_{sis}=R\ln 2=0{,}1989\ \text{kJ/(kg·K)}$ (idéntico en los tres),
> $\;w_{rev}=RT\ln 2=59{,}68\ \text{kJ/kg}$, $\;w_c=RT(1-P_2/P_1)=86{,}10\cdot 0{,}5=43{,}05\ \text{kJ/kg}$.
>
> | Camino | $w$ (kJ/kg) | $q$ (kJ/kg) | $\Delta s_{sis}$ (kJ/(kg·K)) | $S_{gen}$ (kJ/(kg·K)) |
> |---|---|---|---|---|
> | (a) Isotérmico reversible | $59{,}68$ | $59{,}68$ | $0{,}1989$ | $0$ |
> | (b) Expansión libre | $0$ | $0$ | $0{,}1989$ | $0{,}1989$ |
> | (c) Contra $P_{ext}=P_2$ | $43{,}05$ | $43{,}05$ | $0{,}1989$ | $0{,}0554$ |
>
> Cálculo de $S_{gen}^{(c)}$: $\;0{,}1989-43{,}05/300=0{,}1989-0{,}1435=0{,}0554\ \text{kJ/(kg·K)}$.
> Lectura: el **mismo** $\Delta s_{sis}$ en los tres casos, pero el trabajo aprovechado cae de $59{,}68$ a $43{,}05$ y a $0$, mientras la generación de entropía sube de $0$ a $0{,}0554$ y a $0{,}1989$. A mayor irreversibilidad, **menos trabajo útil y más entropía generada**.

![[reversibilidad.svg|520]]

*Expansión isotérmica reversible (curva $P=RT/v$): el área bajo la curva es $W_{rev}$, el trabajo máximo. Frente a ella, la expansión irreversible contra $P_{ext}=P_2$ constante encierra el área del rectángulo $P_2(v_2-v_1)$, estrictamente menor. La diferencia de áreas es el trabajo perdido por irreversibilidad.*

---

## 5. Camino frente a propiedad

> [!corolario]
> El cambio de entropía del sistema $\Delta s_{sis}$ depende **solo de los estados** inicial y final (es una **propiedad**), mientras que $S_{gen}$ y el **trabajo** $w$ dependen del **camino** seguido. La irreversibilidad "cuesta" trabajo útil: el déficit $w_{rev}-w_{irrev}\ge 0$ es **trabajo aprovechable perdido**.

> [!proposicion]
> En un entorno con temperatura ambiente de referencia $T_0$, el trabajo perdido por irreversibilidad es proporcional a la entropía generada:
> $$ w_{perdido}=T_0\,S_{gen}\ge 0 \qquad\text{(teorema de Gouy–Stodola)}.$$
> Esta es la **destrucción de exergía**; su deducción y aplicaciones se desarrollan en [[Balance de Exergia SC]]. La generación de entropía no es solo un número abstracto: es trabajo que el ingeniero **podría haber obtenido** y no obtuvo.

> [!warning]
> El proceso reversible es una **idealización límite inalcanzable**: requiere desequilibrios infinitesimales ($\varepsilon\to 0$) y, por tanto, tiempo infinito. Su utilidad es servir de **referencia** para medir el desempeño real (eficiencia isentrópica de turbinas y compresores, trabajo máximo extraíble, trabajo mínimo de compresión).
> Cuidado con un error frecuente: un proceso **adiabático irreversible** tiene $q=0$ pero **no** es isentrópico. Su balance es $\Delta s=S_{gen}>0$. Solo el adiabático **reversible** es isentrópico ($\Delta s=0$). Véase [[Proceso Adiabatico]].

---

> [!referencia]
> - Çengel, Y. & Boles, M., *Termodinámica*, cap. 7 (entropía) y cap. 8 (exergía).
> - Moran, M. & Shapiro, H., *Fundamentos de Termodinámica Técnica*, balance de entropía de sistemas cerrados.
> - Notas relacionadas: [[Segunda Ley SC]], [[Entropia]], [[Balance de Exergia SC]], [[Proceso Isotermico]], [[Proceso Adiabatico]].
