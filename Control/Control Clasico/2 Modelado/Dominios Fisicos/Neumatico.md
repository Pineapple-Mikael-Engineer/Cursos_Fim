---
title: Sistemas Neumáticos
tags:
  - control-clasico
  - dominios-fisicos
  - modelado
draft: false
aliases:
  - neumático
  - sistemas neumáticos
  - gas a presión
---

# Sistemas Neumáticos

> [!definicion]
> Un sistema neumático se modela con dos elementos —resistencia neumática $R$ (restricción) y capacitancia neumática $C=V/(R_{gas}T)$— mediante el balance de masa de gas. Para un volumen con presión de suministro $P_i$ y presión interna $P_o$:
> $$C\frac{dP_o}{dt}=\frac{P_i-P_o}{R}\qquad\Longrightarrow\qquad G(s)=\frac{P_o(s)}{P_i(s)}=\frac{1}{RCs+1}.$$
> Primer orden $R$–$C$; lo distintivo frente a los líquidos es la **compresibilidad** del gas.

> [!info]
> Es uno de los [[Funcion Transferencia/index | dominios físicos]] del modelado, con la misma estructura $R$–$C$ que los dominios [[Fluidos Nivel | hidráulico]] y [[Termico | térmico]], y **análogo exacto** al [[Electrico | circuito RC]] (presión↔voltaje, caudal másico↔corriente). Base de los actuadores y [[PID/index | controladores PID]] neumáticos.

---

## Ejemplo

> [!ejemplo]
> **Tanque de gas con restricción, valores numéricos.** Volumen con capacitancia $C=2\times10^{-6}\ \text{kg/Pa}$ y restricción $R=5\times10^{6}\ \text{Pa·s/kg}$. Entrada presión de suministro $P_i$, salida presión interna $P_o$.
>
> ![[sistema_neumatico.svg|450]]
>
> **Paso 1 — Flujo por la restricción** (linealizado en el punto de operación): $q_m=(P_i-P_o)/R$.
>
> **Paso 2 — Balance de masa** (el gas que entra eleva la presión del volumen):
> $$C\frac{dP_o}{dt}=q_m=\frac{P_i-P_o}{R}.$$
>
> **Paso 3 — Laplace (variables de desviación, CI nulas):**
> $$Cs\,P_o(s)=\frac{P_i(s)-P_o(s)}{R}\;\Longrightarrow\;P_o(s)\,(RCs+1)=P_i(s).$$
>
> **Paso 4 — Función de transferencia e interpretación:**
> $$G(s)=\frac{P_o(s)}{P_i(s)}=\frac{1}{RCs+1}=\frac{1}{10\,s+1}.$$
> Primer orden con $\tau=RC=(5\times10^6)(2\times10^{-6})=10\ \text{s}$, ganancia DC $1$ (la presión interna iguala a la de suministro en régimen), polo en $s=-0.1\ \text{rad/s}$. Análogo exacto del [[Electrico | circuito RC]].

---

## Elementos y leyes constitutivas

> [!teoria]
> El dominio neumático usa dos elementos. La variable de **esfuerzo** es la presión $P$ [Pa]; la de **flujo** es el caudal másico $q_m$ [kg/s]:
>
> | Elemento | Definición | Relación | Unidad |
> |---|---|---|---|
> | Resistencia $R$ | oposición de la restricción | $R=\dfrac{dP}{dq_m}$ | Pa·s/kg |
> | Capacitancia $C$ | masa almacenada por presión | $C=\dfrac{dm}{dP}=\dfrac{V}{R_{gas}T}$ | kg/Pa |
>
> La ley que las une es el **balance de masa de gas**: $C\,\dfrac{dP}{dt}=q_{m,in}-q_{m,out}$ ($R_{gas}$ = constante del gas, proceso isotérmico). El flujo por un orificio es **no lineal** (régimen sónico/subsónico) y se [[Serie Taylor | lineariza]] en el punto de operación.

> [!info] Compresibilidad = capacitancia
> A diferencia de los [[Fluidos Nivel | líquidos]] (casi incompresibles), el gas **se comprime**: el volumen actúa como un resorte/condensador que almacena energía en la presión. Por lo demás, la estructura $R$–$C$ es idéntica a la de los demás dominios.

---

## Más configuraciones

> [!ejemplo] Dos volúmenes / línea larga
> Dos volúmenes en cascada dan **segundo orden** $G(s)=1/[(R_1C_1s+1)(R_2C_2s+1)]$. Una línea larga añade retardo de transporte (la onda de presión viaja a velocidad finita): $G(s)=e^{-Ls}/(RCs+1)$.

> [!info] Tabla de funciones de transferencia
> | Sistema | Entrada | Salida | $G(s)$ | Tipo |
> |---|---|---|---|---|
> | Volumen único | $P_i$ | $P_o$ | $\dfrac{1}{RCs+1}$ | 1er orden |
> | Dos volúmenes | $P_i$ | $P_2$ | $\dfrac{1}{(R_1C_1s+1)(R_2C_2s+1)}$ | 2do orden |
> | Con línea larga | $P_i$ | $P_o$ | $\dfrac{e^{-Ls}}{RCs+1}$ | 1er orden + retardo |

> [!info] Relevancia industrial
> Los **controladores PID neumáticos** (toberas-aleta, relés) dominaron la industria de procesos antes de la electrónica, y los **actuadores neumáticos** (válvulas de control, pistones) siguen siendo estándar. Las acciones [[PID/index | integral y derivativa]] se implementaban con combinaciones de restricciones ($R$) y volúmenes/fuelles ($C$).

---

## Receta de modelado

> [!algoritmo]
> Para la FT de un sistema neumático:
> 1. **Balance de masa** por volumen: $C\dfrac{dP}{dt}=\sum q_{m,in}-\sum q_{m,out}$, con $C=V/(R_{gas}T)$.
> 2. **Resistencias:** expresar el flujo como $q_m=\Delta P/R$, **linealizando** el orificio no lineal en el punto de operación.
> 3. **Variables de desviación** (ver [[Variables Desviacion]]).
> 4. **Retardo:** añadir $e^{-Ls}$ en líneas largas.
> 5. **Laplace con CI nulas** y despejar $P_o(s)/P_i(s)$.

> [!info] Analogía neumático-eléctrica
> | Neumático | Eléctrico |
> |---|---|
> | Presión $P$ | Voltaje $V$ |
> | Caudal másico $q_m$ | Corriente $I$ |
> | Resistencia $R$ | Resistencia $R$ |
> | Capacitancia (volumen) $C$ | Capacitancia $C$ |
> | Inertancia (línea larga) | Inductancia $L$ |
>
> Misma estructura $R$–$C$ que [[Fluidos Nivel | fluidos]] y [[Termico | térmico]]; la diferencia es la **compresibilidad**. Ver [[Electrico | sistemas eléctricos]].

> [!info] En MATLAB
> ```matlab
> R=5e6; C=2e-6;
> G = tf(1, [R*C 1]);        % 1/(RCs+1), tau = 10 s
> G.InputDelay = 2;          % retardo de linea L = 2 s
> step(G)
> ```

---

## Limitaciones

> [!warning]
> 1. **Flujo no lineal:** régimen sónico/subsónico en restricciones; FT válida solo [[Serie Taylor | linealizada]] en el punto de operación.
> 2. **$C$ depende de la temperatura** ($C=V/R_{gas}T$): supone proceso isotérmico.
> 3. **Retardos** en líneas largas (la onda de presión viaja a velocidad finita).
> 4. **CI nulas:** variables de desviación (ver [[Variables Desviacion]]).

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Elementos | resistencia $R$, capacitancia $C=V/R_{gas}T$ |
> | Ley | balance de masa $C\dot P=q_{m,in}-q_{m,out}$ |
> | FT | $G(s)=\dfrac{1}{RCs+1}$ |
> | Constante de tiempo | $\tau=RC$ |
> | Distintivo | compresibilidad del gas |

> [!corolario]
> Modelar un sistema neumático es escribir el balance de masa de gas y sustituir el flujo linealizado $q_m=\Delta P/R$: cada volumen aporta un polo real, dando primer orden ($\tau=RC$). Es el análogo exacto del [[Electrico | circuito RC]] y comparte estructura con los dominios [[Fluidos Nivel | hidráulico]] y [[Termico | térmico]]; la compresibilidad del gas hace de capacitancia y sustenta los [[PID/index | controladores]] y actuadores neumáticos.

> [!referencia]
> - Linealización del flujo: [[Serie Taylor]] · [[Variables Desviacion]].
> - Respuesta de primer orden: [[Primer Orden]].
> - Controladores que implementa: [[PID/index]].
> - Analogías $R$–$C$: [[Electrico]] · [[Fluidos Nivel]] · [[Termico]].
