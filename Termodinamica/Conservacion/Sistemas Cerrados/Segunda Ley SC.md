---
title: "Segunda Ley (Sistema Cerrado)"
order: 2
tags:
  - termodinamica
  - conservacion
  - entropia
  - segunda_ley
  - sistema_cerrado
draft: false
aliases:
  - segunda ley SC
  - balance entropico SC
  - desigualdad de Clausius
---

# Segunda Ley — Sistema Cerrado

> [!definicion]
> Para un [[Sistemas Cerrados/index | sistema cerrado]] (masa fija), el balance de entropía es:
> $$\boxed{S_2 - S_1 = \int_1^2 \frac{\delta Q}{T_b} + S_{\rm gen},}$$
> donde $T_b$ es la temperatura en la frontera donde se transfiere el calor $\delta Q$, y $S_{\rm gen} \ge 0$ es la entropía generada por irreversibilidades internas. Este balance no es un postulado: se **deduce** de la desigualdad de Clausius (sección [[#Del enunciado de Clausius al balance de entropía|más abajo]]). Forma diferencial:
> $$dS = \frac{\delta Q}{T_b} + \delta S_{\rm gen}, \qquad \delta S_{\rm gen} \ge 0.$$
>
> La primera ley ($\Delta U = Q - W$) no impone dirección: dice cuánta energía cambia, no en qué dirección puede fluir el proceso. La segunda ley impone la dirección: $S_{\rm gen} \ge 0$ hace que los procesos reales siempre generen entropía; la igualdad $S_{\rm gen} = 0$ solo se alcanza en el límite reversible (idealización). **Lo que nunca puede decrecer es la entropía del universo (sistema + entorno).**

---

## Qué significa físicamente $S_{\rm gen}$

> [!teoria]
> La entropía del sistema puede tanto subir como bajar:
> - Si se transfiere calor hacia afuera ($Q < 0$, e.g., una nevera), la entropía del sistema disminuye.
> - Si hay irreversibilidades internas (fricción, mezcla, reacción espontánea), la entropía del sistema sube.
>
> La restricción de la segunda ley no es sobre $\Delta S$ del sistema, sino sobre $S_{\rm gen}$:
> - $S_{\rm gen} = 0$: proceso **internamente reversible** (ninguna fuente de irreversibilidad dentro del sistema).
> - $S_{\rm gen} > 0$: proceso irreversible; hubo fricción, conducción de calor con gradiente de temperatura, expansión libre, mezcla, reacción, etc.
>
> Las fuentes de $S_{\rm gen}$ en un sistema cerrado son:
> 1. Fricción mecánica (rozamiento pistón-cilindro, viscosidad del fluido).
> 2. Transferencia de calor a través de gradiente de temperatura finito dentro del sistema.
> 3. Mezcla de sustancias.
> 4. Reacciones químicas espontáneas.

---

## Cómo calcular $\Delta S$ para procesos irreversibles

> [!teoria]
> La entropía es función de estado: $\Delta S$ entre los estados 1 y 2 no depende del camino. Por tanto, para calcular $\Delta S$ en un proceso **irreversible**, se diseña un proceso **reversible** auxiliar entre los mismos estados 1 y 2, y se integra $\delta Q_{\rm rev}/T$ a lo largo de ese proceso. El resultado es el mismo $\Delta S$ que el proceso real, aunque los valores de $Q$ y $W$ sean distintos.
>
> El $S_{\rm gen}$ del proceso real se obtiene de la diferencia:
> $$S_{\rm gen} = \Delta S - \int_1^2 \frac{\delta Q_{\rm real}}{T_b}.$$
> Si $S_{\rm gen} > 0$: proceso real irreversible. Si se calculara $S_{\rm gen} < 0$: el proceso viola la segunda ley (imposible).

---

## La desigualdad de Clausius y su origen

> [!teorema]
> Para cualquier ciclo termodinámico (cerrado en el diagrama de estados):
> $$\oint \frac{\delta Q}{T_b} \le 0,$$
> con igualdad para ciclos **reversibles** e inigualdad estricta para ciclos **irreversibles**.

> [!demostracion]
> **Meta:** probar la desigualdad de Clausius a partir de la segunda ley (enunciado de Kelvin-Planck).
>
> **Hipótesis:** sistema cerrado que ejecuta un ciclo; interactúa con $N$ reservorios a temperaturas $T_k$ (cada uno transfiere calor $\delta Q_k$ al sistema); la segunda ley de Kelvin-Planck prohíbe extraer trabajo neto de un solo reservorio en un ciclo.
>
> **Paso 1 — Conectar cada interacción de calor a un dispositivo auxiliar Carnot.**
> Para cada reservorio $k$ a temperatura $T_k$, se interpone una máquina de Carnot reversible entre ese reservorio y un reservorio único a temperatura $T_0$. La máquina transfiere calor $\delta Q_k$ al sistema y extrae $\delta Q_{0k}$ de $T_0$. Por la eficiencia de Carnot:
> $$\frac{\delta Q_{0k}}{\delta Q_k} = \frac{T_0}{T_k} \implies \delta Q_{0k} = T_0\frac{\delta Q_k}{T_k}.$$
>
> **Paso 2 — Calor total extraído del reservorio único por ciclo.**
> $$Q_{0,\rm ciclo} = \oint \delta Q_0 = T_0 \oint \frac{\delta Q}{T_b}.$$
>
> **Paso 3 — Balance de energía del sistema combinado.**
> Sistema original + todas las máquinas de Carnot: el conjunto extrae $Q_{0,\rm ciclo}$ del único reservorio $T_0$ y produce trabajo $W_{\rm ciclo,total}$. Por la primera ley de los ciclos: $W_{\rm ciclo,total} = Q_{0,\rm ciclo}$.
>
> **Paso 4 — Aplicar la segunda ley (Kelvin-Planck).**
> Si $W_{\rm ciclo,total} > 0$, el sistema combinado convertiría todo el calor del reservorio único en trabajo: viola Kelvin-Planck. Luego:
> $$W_{\rm ciclo,total} = Q_{0,\rm ciclo} \le 0 \implies T_0 \oint \frac{\delta Q}{T_b} \le 0 \implies \oint \frac{\delta Q}{T_b} \le 0. \qquad \blacksquare$$
>
> **Paso 5 — Verificación de límites.**
> Si el ciclo es reversible, también puede ejecutarse en sentido contrario (igual pero con signos opuestos), y para que ambas desigualdades sean compatibles: $\oint \delta Q/T = 0$. Si es irreversible, solo puede haber la desigualdad estricta $< 0$. ✓

---

## Del enunciado de Clausius al balance de entropía

> [!demostracion]
> **Meta:** deducir el balance $S_2 - S_1 = \int_1^2 \delta Q/T_b + S_{\rm gen}$ a partir de la desigualdad de Clausius $\oint \delta Q/T_b \le 0$.
>
> **Paso 1 — Cerrar un ciclo.** Sea un proceso **real** (posiblemente irreversible) que lleva el sistema del estado 1 al 2. Se completa un ciclo con un camino de retorno $2\to1$ **internamente reversible** — siempre existe, porque $S$ es función de estado y los estados 1 y 2 son fijos. El ciclo combinado es $1 \xrightarrow{\text{real}} 2 \xrightarrow{\text{rev}} 1$.
>
> **Paso 2 — Aplicar la desigualdad de Clausius al ciclo.** La integral cíclica se parte en los dos tramos:
> $$\oint \frac{\delta Q}{T_b} = \int_1^2 \left(\frac{\delta Q}{T_b}\right)_{\rm real} + \int_2^1 \left(\frac{\delta Q}{T}\right)_{\rm rev} \le 0.$$
> En el tramo reversible la temperatura de frontera coincide con la del sistema ($T_b = T$), por ser cuasiestático.
>
> **Paso 3 — Evaluar el tramo reversible.** Por la definición de entropía, $dS = \delta Q_{\rm rev}/T$ sobre cualquier camino reversible, de modo que
> $$\int_2^1 \left(\frac{\delta Q}{T}\right)_{\rm rev} = \int_2^1 dS = S_1 - S_2.$$
>
> **Paso 4 — Despejar.** Sustituyendo en el Paso 2:
> $$\int_1^2 \left(\frac{\delta Q}{T_b}\right)_{\rm real} + (S_1 - S_2) \le 0 \;\Longrightarrow\; S_2 - S_1 \ge \int_1^2 \frac{\delta Q}{T_b}.$$
>
> **Paso 5 — Definir $S_{\rm gen}$.** La desigualdad se convierte en igualdad introduciendo el **déficit** no negativo
> $$S_{\rm gen} \equiv (S_2 - S_1) - \int_1^2 \frac{\delta Q}{T_b} \ge 0,$$
> que es precisamente la entropía generada por las irreversibilidades internas del tramo real. Reordenando se obtiene el balance:
> $$\boxed{S_2 - S_1 = \int_1^2 \frac{\delta Q}{T_b} + S_{\rm gen}, \qquad S_{\rm gen} \ge 0.}$$
> El déficit es estrictamente positivo ($S_{\rm gen} > 0$) cuando el tramo $1\to2$ es irreversible, y nulo solo en el límite reversible. $\blacksquare$

---

## Casos particulares del balance de entropía

> [!proposicion]
> **Proceso adiabático** ($\delta Q = 0$):
> $$\Delta S = S_{\rm gen} \ge 0.$$
> La entropía nunca disminuye en un proceso adiabático. Un proceso adiabático reversible ($S_{\rm gen} = 0$) es **isentrópico** ($\Delta S = 0$).
>
> **Proceso reversible** ($S_{\rm gen} = 0$):
> $$\Delta S = \int_1^2 \frac{\delta Q_{\rm rev}}{T}.$$
>
> **Proceso isotérmico reversible** ($T_b = T = \text{cte}$, $S_{\rm gen} = 0$):
> $$\Delta S = \frac{Q_{\rm rev}}{T}.$$
>
> **Gas ideal** (cualquier proceso reversible):
> $$\Delta s = c_p\ln\frac{T_2}{T_1} - R\ln\frac{P_2}{P_1} = c_v\ln\frac{T_2}{T_1} + R\ln\frac{v_2}{v_1}.$$
>
> **Sustancia incompresible** ($c_p = c_v = c$, proceso reversible):
> $$\Delta s = c\ln\frac{T_2}{T_1}.$$

---

## Ejemplo 1: expansión libre irreversible (gas ideal)

> [!ejemplo]
> **Gas ideal en un recipiente adiabático de doble cámara** ($V_1 \to V_2 = 2V_1$). Se rompe la membrana — expansión libre al vacío (proceso adiabático, sin trabajo). Calcular $S_{\rm gen}$.
>
> **Paso 1 — Primera ley.** $Q = 0$, $W = 0$ (expansión libre contra el vacío) → $\Delta U = 0$ → para gas ideal, $T_2 = T_1$.
>
> **Paso 2 — Diseñar un proceso reversible auxiliar entre los mismos estados.** Los estados 1 ($T_1, V_1$) y 2 ($T_1, V_2$) tienen la misma temperatura. Un camino reversible que los conecte es la **expansión isotérmica reversible** de $V_1$ a $V_2$ a temperatura $T_1$.
>
> **Paso 3 — Calcular $\Delta S$ por el camino reversible.**
> $$\Delta S = \frac{Q_{\rm rev}}{T_1} = \frac{mRT_1\ln(V_2/V_1)}{T_1} = mR\ln\frac{V_2}{V_1} = mR\ln 2 > 0.$$
>
> **Paso 4 — Calcular $S_{\rm gen}$ del proceso real.**
> El proceso real es adiabático: $\int \delta Q_{\rm real}/T_b = 0$. Por tanto:
> $$S_{\rm gen} = \Delta S - \int\frac{\delta Q_{\rm real}}{T_b} = mR\ln 2 - 0 = mR\ln 2 > 0.$$
>
> **Paso 5 — Interpretación.** El proceso es irreversible: la expansión libre genera entropía sin producir trabajo ni intercambiar calor. Toda la "calidad" de ese diferencial de presión se disipa — es el ejemplo más claro de que una expansión incontrolada destruye trabajo potencial. $\blacksquare$

---

## Ejemplo 2: transferencia de calor con gradiente de temperatura

> [!ejemplo]
> **Dos bloques idénticos** ($C = mc$, capacidad calorífica total) a $T_A = 400\,\text{K}$ y $T_B = 200\,\text{K}$ se ponen en contacto térmico hasta alcanzar equilibrio. El conjunto está aislado del entorno.
>
> **Paso 1 — Temperatura final.** Balance de energía (sistema aislado): $C\Delta T_A + C\Delta T_B = 0$ → $T_f = (T_A + T_B)/2 = 300\,\text{K}$.
>
> **Paso 2 — Variación de entropía de cada bloque** (la entropía es función de estado; calculamos $\Delta S$ por camino reversible para cada bloque individualmente):
> $$\Delta S_A = C\ln\frac{T_f}{T_A} = C\ln\frac{300}{400} = C\ln 0.75 = -0.2877\,C.$$
> $$\Delta S_B = C\ln\frac{T_f}{T_B} = C\ln\frac{300}{200} = C\ln 1.50 = +0.4055\,C.$$
>
> **Paso 3 — Entropía total generada.** El conjunto es adiabático ($\int \delta Q/T = 0$):
> $$S_{\rm gen} = \Delta S_A + \Delta S_B = C(-0.2877 + 0.4055) = 0.1178\,C > 0.$$
>
> **Paso 4 — Verificar la dirección del proceso.** $S_{\rm gen} > 0$: el proceso es irreversible. Jamás se observaría que los dos bloques a 300 K espontáneamente se separen en uno a 400 K y otro a 200 K — eso requeriría $S_{\rm gen} < 0$, imposible. $\blacksquare$

---

## Relación con otras notas

> [!info]
> - [[Primera Ley SC]] — complementa: la primera ley da el balance energético; la segunda ley da la dirección.
> - [[Entropia]] — definición, desigualdad de Clausius, y la fórmula $S = k_B\ln\Omega$.
> - [[Balance de Exergia SC]] — consecuencia de combinar primera ley + segunda ley: $B_{\rm dest} = T_0 S_{\rm gen}$.
> - [[Balance de Entropia VC]] — extensión a sistemas abiertos; $\dot{S}_{\rm gen}$ por unidad de tiempo.

> [!warning]
> - $S_{\rm gen} \ge 0$ siempre; $\Delta S$ puede ser negativo si sale calor suficiente.
> - Para calcular $\Delta S$ entre dos estados, **siempre** usar un camino reversible auxiliar, aunque el proceso real sea irreversible. La entropía es función de estado.
> - La temperatura $T_b$ en $\delta Q/T_b$ es la temperatura **en la frontera** donde ocurre el intercambio de calor, no la temperatura interior del sistema.

> [!referencia]
> Borgnakke & Sonntag, *Fundamentals of Thermodynamics*, caps. 8–9; Çengel & Boles, *Termodinámica*, caps. 6–7; Callen, *Thermodynamics*, caps. 2–4; Clausius, "Über verschiedene für die Anwendung bequeme Formen der Hauptgleichungen der mechanischen Wärmetheorie" (1865).
