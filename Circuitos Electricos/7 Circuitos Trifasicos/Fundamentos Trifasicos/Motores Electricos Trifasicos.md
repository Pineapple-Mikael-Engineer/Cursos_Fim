---
title: Motores Eléctricos Trifásicos
order: 5
tags:
  - circuitos-electricos
  - teoria
  - trifasico
aliases:
  - motores eléctricos trifásicos
  - motor de inducción
  - motor asíncrono
  - motor monofásico
  - three-phase motor
  - induction motor
---

# Motores Eléctricos Trifásicos

> [!definicion]
> Un **motor eléctrico** convierte energía **eléctrica** en energía **mecánica** de rotación. El **motor de inducción trifásico** (o **asíncrono**) lo hace aprovechando el [[Ventajas del Trifasico| campo magnético giratorio]] que crean tres corrientes desfasadas $120^\circ$ en tres devanados a $120^\circ$: ese campo "arrastra" al rotor y lo hace girar **sin escobillas ni contactos** con la parte móvil. Es, con diferencia, el motor más usado en la industria por su robustez, bajo coste y arranque autónomo.

> [!info]
> Es la **aplicación estrella** de los [[Fundamentos Trifasicos/index| fundamentos trifásicos]] ([[7 Circuitos Trifasicos/index| capítulo 7]]): materializa el campo giratorio de las [[Ventajas del Trifasico| ventajas del trifásico]] y depende de la [[Secuencia de Fases| secuencia de fases]] (que fija el sentido de giro). Su consumo se calcula con la [[Potencia en Sistemas Balanceados| potencia trifásica]] y su [[Factor de Potencia| factor de potencia]]. Fraile Mora, cap. 3, §3.9 (y *Máquinas eléctricas*, mismo autor).

---

## Ejemplo

> [!ejemplo]
> **Corriente que absorbe un motor de su placa de características.**
>
> Un motor trifásico de inducción tiene en su **placa**: potencia $P_u=10\ \text{CV}$, tensión $400\ \text{V}$ (línea), rendimiento $\eta=0{,}88$ y factor de potencia $\cos\varphi=0{,}85$. Hallar la potencia que **absorbe** de la red y la **corriente de línea**.
>
> **Paso 1 — Potencia útil en vatios.** La placa da la potencia **mecánica de salida** en caballos; $1\ \text{CV}=735{,}5\ \text{W}$:
> $$P_u=10\cdot735{,}5\approx7{,}36\ \text{kW}.$$
>
> **Paso 2 — Potencia absorbida (eléctrica de entrada).** El rendimiento relaciona salida con entrada, $\eta=P_u/P_{abs}$:
> $$P_{abs}=\frac{P_u}{\eta}=\frac{7355}{0{,}88}\approx8{,}36\ \text{kW}.$$
> La diferencia $P_{abs}-P_u\approx1{,}0\ \text{kW}$ se **pierde** como calor (cobre, hierro, rozamiento).
>
> **Paso 3 — Corriente de línea.** De la [[Potencia en Sistemas Balanceados| potencia trifásica]] $P_{abs}=\sqrt3\,V_L I_L\cos\varphi$:
> $$I_L=\frac{P_{abs}}{\sqrt3\,V_L\cos\varphi}=\frac{8358}{\sqrt3\cdot400\cdot0{,}85}\approx14{,}2\ \text{A}.$$
>
> > [!solucion]
> > El motor entrega $7{,}36\ \text{kW}$ mecánicos, absorbe $8{,}36\ \text{kW}$ eléctricos (rinde el $88\%$) y toma $\approx14{,}2\ \text{A}$ por cada línea. La placa da la potencia **de salida** (en CV); para la **de entrada** y la corriente hay que dividir por $\eta$ y usar el FP.

---

## En qué consiste

> [!teoria] Cómo gira: campo giratorio y deslizamiento
> Las tres corrientes a $120^\circ$ del estator producen un **campo magnético giratorio** de módulo constante que gira a la **velocidad de sincronismo**
> $$n_s=\frac{120\,f}{p}\quad\text{(rpm)},$$
> donde $f$ es la frecuencia y $p$ el número de **polos**. Por ejemplo, a $50\ \text{Hz}$ y $4$ polos, $n_s=1500\ \text{rpm}$. Este campo induce corrientes en el rotor (de ahí "**inducción**") y el par resultante lo arrastra. El rotor gira algo **más despacio** que el campo —por eso es **asíncrono**—: si girara a la misma velocidad no habría variación de flujo ni corriente inducida. Esa diferencia relativa es el **deslizamiento**
> $$s=\frac{n_s-n}{n_s},$$
> típicamente del $2$–$5\%$ a plena carga. El **sentido de giro** lo fija la [[Secuencia de Fases| secuencia]]: permutar dos fases lo invierte.

> [!teoria] Trifásico frente a monofásico
> Un **motor monofásico** se alimenta de una sola fase. Su campo no gira, sino que **pulsa** (oscila sobre un eje fijo): por sí solo **no arranca** —produce par en ambos sentidos, que se anulan en reposo—. Necesita un **artificio de arranque** que cree una segunda "fase" ficticia y un campo algo giratorio: condensador de arranque (*capacitor-start*), bobinado auxiliar desfasado (*fase partida*) o espira de sombra (*shaded pole*) en los más pequeños. Por eso el monofásico se reserva para **baja potencia** (electrodomésticos, bombas pequeñas), donde solo hay una fase disponible.
>
> El **motor trifásico**, en cambio, dispone del campo giratorio "gratis" por tener tres fases a $120^\circ$: **arranca solo**, da par uniforme, vibra menos y, a igual potencia, es **más pequeño, barato y eficiente** que el monofásico. Es el motor estándar de la industria.

> [!proposicion] Las magnitudes de la placa: potencia, rendimiento y FP
> La **placa de características** resume el punto de funcionamiento nominal. Sus tres magnitudes energéticas son:
> - **Potencia nominal $P_u$** — la potencia **mecánica útil en el eje** (de **salida**), no la que consume. Se expresa en **caballos** o en kW. Conviene no confundir las unidades de "caballo":
>   - **CV** (caballo de vapor, métrico) $=735{,}5\ \text{W}$,
>   - **HP** (*horsepower*, inglés) $=746\ \text{W}$,
>   - en español a veces se escribe **CP** (caballos de potencia) como sinónimo de CV/HP.
> - **Rendimiento (eficiencia) $\eta$** — fracción de la potencia eléctrica que sale como mecánica:
>   $$\eta=\frac{P_{u}\ (\text{mecánica, salida})}{P_{abs}\ (\text{eléctrica, entrada})}\in(0,1),$$
>   típicamente $0{,}75$–$0{,}95$. Lo que falta ($1-\eta$) se disipa en calor: pérdidas en el cobre ($I^2R$), en el hierro y por rozamiento/ventilación.
> - **Factor de potencia $\cos\varphi$** — el motor es una carga **inductiva**; toma corriente reactiva para magnetizar. Su FP ($0{,}8$–$0{,}9$ a plena carga, mucho menor en vacío) entra en $P_{abs}=\sqrt3\,V_L I_L\cos\varphi$ y conviene **corregirlo** ([[Correccion FP Trifasico]]).
>
> La cadena de potencias es: $P_{abs}=\sqrt3\,V_L I_L\cos\varphi$ (entrada eléctrica) $\;\xrightarrow{\ \times\,\eta\ }\;$ $P_u=\eta\,P_{abs}$ (salida mecánica).

> [!warning]
> Errores típicos: (1) la potencia de la placa es la **útil de salida** —para la corriente hay que usar la **absorbida** $P_{abs}=P_u/\eta$, mayor—; (2) **CV $\ne$ HP $\ne$ kW**: convertir siempre a vatios antes de operar; (3) el **FP** no es el rendimiento: $\cos\varphi$ mide el desfase (potencia reactiva), $\eta$ mide las pérdidas (potencia perdida en calor); un motor puede tener buen $\eta$ y mal $\cos\varphi$; (4) en **vacío** el motor mantiene casi la misma corriente magnetizante pero con $\cos\varphi$ muy bajo, por eso conviene no sobredimensionarlo.

## Resumen

> [!resumen]
> | Magnitud | Significado | Relación |
> |:---|:---|:---|
> | Velocidad de sincronismo | giro del campo | $n_s=120f/p$ |
> | Deslizamiento | retraso relativo del rotor | $s=(n_s-n)/n_s$ |
> | Potencia útil $P_u$ | mecánica de **salida** (placa), en CV/HP/kW | $1\ \text{CV}=735{,}5\ \text{W}$ |
> | Potencia absorbida $P_{abs}$ | eléctrica de **entrada** | $\sqrt3\,V_L I_L\cos\varphi$ |
> | Rendimiento $\eta$ | salida/entrada (pérdidas) | $\eta=P_u/P_{abs}$ |
> | Factor de potencia $\cos\varphi$ | desfase (carga inductiva) | corrige con condensadores |
> | Sentido de giro | lo fija la secuencia | invertir = permutar 2 fases |

> [!corolario]
> El motor de inducción trifásico es la aplicación directa del campo giratorio: convierte tres corrientes a $120^\circ$ en rotación, arranca solo y rinde más que el monofásico (que necesita artificios por tener campo pulsante). Para dimensionarlo hay que distinguir tres cosas que la placa no debe mezclar: la **potencia útil** (CV/HP de salida), el **rendimiento** $\eta$ (pérdidas) y el **factor de potencia** $\cos\varphi$ (reactiva). Con ellas, $P_{abs}=P_u/\eta=\sqrt3\,V_L I_L\cos\varphi$ da la corriente que toma de la red.

> [!referencia]
> Fraile Mora, *Circuitos Eléctricos*, cap. 3, §3.9 (y *Máquinas Eléctricas*). Campo giratorio: [[Ventajas del Trifasico]]. Sentido de giro: [[Secuencia de Fases]]. Consumo: [[Potencia en Sistemas Balanceados]] y [[Factor de Potencia]]. Corrección: [[Correccion FP Trifasico]]. Marco: [[Fundamentos Trifasicos/index]].
