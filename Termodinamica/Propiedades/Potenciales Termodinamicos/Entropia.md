---
title: "Entropía $S$"
order: 3
tags:
  - termodinamica
  - potenciales_termodinamicos
  - segunda_ley
draft: false
aliases:
  - entropy
  - S
  - segunda ley
---

# Entropía $S$

> [!definicion]
> La **entropía** $S$ es la propiedad termodinámica que mide la "dispersión" del estado microscópico de un sistema: cuántas formas diferentes existen de distribuir la energía entre los grados de libertad microscópicos del sistema sin cambiar su estado macroscópico. En termodinámica clásica, $S$ se introduce como la propiedad que hace exacta la forma diferencial $\delta Q_{\rm rev}/T$: para cualquier proceso internamente reversible,
> $$dS = \frac{\delta Q_{\rm rev}}{T},$$
> con $S$ medida en J/K o kJ/K. La entropía es la única propiedad termodinámica que tiene una dirección preferida de cambio: en un proceso real $dS_{\rm total} > 0$, lo que le da a la termodinámica su "flecha del tiempo".

---

## El problema con el calor: ¿por qué $\delta Q$ no es suficiente?

> [!teoria]
> La primera ley establece que $dU = \delta Q - \delta W$, pero ni $\delta Q$ ni $\delta W$ son diferenciales exactas — dependen del camino. Un ciclo cerrado en el diagrama $P$-$v$ puede extraer calor de una fuente y convertirlo en trabajo (ciclo de potencia) o viceversa (ciclo de refrigeración), y la cantidad de calor transferida en cada dirección depende de cómo se construya el ciclo. Esto revela que el calor por sí solo no caracteriza el estado: necesitamos una **función de estado** que cuantifique la "calidad" del calor.
>
> La intuición de Clausius (1854) fue que la razón $\delta Q/T$ es más fundamental que $\delta Q$ solo: no es lo mismo absorber 100 J a 1000 K (calor "de alta calidad", motor de vapor) que a 300 K (calor "de baja calidad", calefacción residual). La entropía cuantifica precisamente esta distinción.

---

## La desigualdad de Clausius

> [!teorema]
> Para cualquier ciclo termodinámico que intercambia calor con reservorios a temperaturas $T_b$ (temperatura de frontera):
> $$\oint \frac{\delta Q}{T_b} \le 0,$$
> con igualdad si y solo si el ciclo es **internamente reversible**. El signo $<$ corresponde a ciclo irreversible.

> [!demostracion]
> **Meta:** probar la desigualdad de Clausius a partir del enunciado de Kelvin-Planck de la segunda ley.
>
> **Hipótesis:** sistema cerrado que ejecuta un ciclo intercambiando calor $\delta Q$ con un reservorio a temperatura de frontera $T_b$; la segunda ley de Kelvin-Planck prohíbe convertir todo el calor en trabajo en un ciclo.
>
> **Paso 1 — Conectar el sistema a un reservorio único a $T_0$.**
> Para cada proceso elemental del ciclo, suponemos que el calor $\delta Q$ se transfiere desde un reservorio auxiliar a temperatura $T_0$ al sistema a través de un dispositivo reversible (máquina de Carnot reversible) de modo que el dispositivo entregue $\delta Q$ al sistema y reciba $\delta Q_0$ del reservorio a $T_0$.
>
> **Paso 2 — Aplicar la eficiencia de Carnot al dispositivo auxiliar.**
> La eficiencia de Carnot del dispositivo reversible entre $T_0$ y $T_b$ es:
> $$\eta_{\rm Carnot} = 1 - \frac{T_b}{T_0}.$$
> El trabajo del dispositivo es $\delta W_d = \delta Q_0 - \delta Q$, y la relación de calores:
> $$\frac{\delta Q_0}{\delta Q} = \frac{T_0}{T_b} \implies \delta Q_0 = T_0\,\frac{\delta Q}{T_b}.$$
>
> **Paso 3 — Balance del sistema combinado (sistema original + dispositivo reversible).**
> El sistema combinado recibe del único reservorio a $T_0$ un calor total por ciclo:
> $$Q_{0,\rm ciclo} = \oint \delta Q_0 = T_0 \oint \frac{\delta Q}{T_b}.$$
> El trabajo total del sistema combinado en el ciclo es $W_{\rm ciclo,total} = W_{\rm ciclo} + W_d$.
>
> **Paso 4 — Aplicar la primera ley al ciclo.**
> Para el ciclo: $\Delta U = 0$, luego $W_{\rm ciclo,total} = Q_{0,\rm ciclo}$.
>
> **Paso 5 — Aplicar la segunda ley (enunciado de Kelvin-Planck).**
> El enunciado de Kelvin-Planck prohíbe que un sistema que interactúa con un solo reservorio produzca trabajo neto: $W_{\rm ciclo,total} \le 0$, luego:
> $$T_0\oint \frac{\delta Q}{T_b} \le 0 \implies \oint \frac{\delta Q}{T_b} \le 0. \qquad \blacksquare$$

---

## Definición de entropía como función de estado

> [!demostracion]
> **Meta:** probar que $\int_1^2 \delta Q_{\rm rev}/T$ es independiente del camino reversible elegido, y definir $S$ como función de estado.
>
> **Hipótesis:** dos procesos internamente reversibles que conectan los estados 1 y 2; la desigualdad de Clausius es válida.
>
> **Paso 1 — Construir un ciclo con los dos caminos.**
> Sean A y B dos procesos reversibles de 1 a 2. El ciclo $1\to 2$ por A y $2\to 1$ por B (invertido) es un ciclo reversible. Por la desigualdad de Clausius con igualdad para proceso reversible:
> $$\oint_{\rm rev}\frac{\delta Q}{T} = 0 \implies \int_{1\to 2,\,A}\frac{\delta Q}{T} + \int_{2\to 1,\,B}\frac{\delta Q}{T} = 0.$$
>
> **Paso 2 — Invertir el sentido de integración de B.**
> $$\int_{1\to 2,\,A}\frac{\delta Q}{T} - \int_{1\to 2,\,B}\frac{\delta Q}{T} = 0 \implies \int_{1\to 2,\,A}\frac{\delta Q}{T} = \int_{1\to 2,\,B}\frac{\delta Q}{T}.$$
>
> **Paso 3 — Conclusión: $\int \delta Q_{\rm rev}/T$ no depende del camino.**
> Como A y B son cualesquiera dos caminos reversibles de 1 a 2, la integral solo depende de los estados extremos. Por tanto existe una función de estado $S$ tal que:
> $$S_2 - S_1 = \int_{1}^{2}\left(\frac{\delta Q}{T}\right)_{\rm rev}. \qquad \blacksquare$$

> [!warning]
> Esta definición da el **cambio** $\Delta S$, no el valor absoluto. El tercer principio (entropía nula para cristal perfecto a 0 K) fija el cero absoluto. En ingeniería siempre se trabaja con diferencias $\Delta s$ o se tabula $s$ con un estado de referencia arbitrario.

---

## Producción de entropía: desigualdad de Clausius aplicada a procesos

> [!teorema]
> Para un proceso real (no necesariamente un ciclo) entre los estados 1 y 2:
> $$S_2 - S_1 \ge \int_1^2 \frac{\delta Q}{T_b},$$
> con igualdad para proceso internamente reversible. Esto se escribe compactamente como:
> $$dS = \frac{\delta Q}{T_b} + \delta S_{\rm gen}, \qquad \delta S_{\rm gen} \ge 0,$$
> donde $\delta S_{\rm gen}$ es la **entropía generada** por irreversibilidades internas (fricción, mezcla, reacción, transferencia de calor con gradiente finito). La entropía de un sistema puede bajar ($dS < 0$) si se extrae calor suficiente; lo que nunca puede bajar es la entropía del **universo** (sistema + entorno).

---

## La segunda ecuación $T\,ds$

> [!proposicion]
> Combinando $dU = T\,dS - P\,dV$ con $h = u + Pv$:
>
> **Primera ecuación $T\,ds$** (en función de $u$ y $v$):
> $$T\,ds = du + P\,dv.$$
>
> **Segunda ecuación $T\,ds$** (en función de $h$ y $P$):
> $$T\,ds = dh - v\,dP.$$
>
> Ambas son relaciones entre funciones de estado y son válidas para cualquier proceso (no solo reversible) entre estados de equilibrio de un sistema simple compresible.

---

## Entropía del gas ideal

> [!demostracion]
> **Meta:** obtener $\Delta s$ para un gas ideal en función de $T$ y $P$ (o $T$ y $v$).
>
> **Hipótesis:** gas ideal — $Pv = RT$ y $c_p, c_v$ (posiblemente funciones de $T$).
>
> **Paso 1 — Partir de la segunda ecuación $T\,ds$:**
> $$T\,ds = dh - v\,dP.$$
>
> **Paso 2 — Para gas ideal, $dh = c_p\,dT$ y $v = RT/P$.**
> $$T\,ds = c_p\,dT - \frac{RT}{P}\,dP.$$
>
> **Paso 3 — Dividir por $T$:**
> $$ds = c_p\,\frac{dT}{T} - R\,\frac{dP}{P}.$$
>
> **Paso 4 — Integrar de estado 1 a estado 2:**
> $$\Delta s = s_2 - s_1 = \int_{T_1}^{T_2}c_p(T)\,\frac{dT}{T} - R\ln\frac{P_2}{P_1}.$$
>
> Si $c_p \approx \text{const}$:
> $$\boxed{\Delta s = c_p\ln\frac{T_2}{T_1} - R\ln\frac{P_2}{P_1}.}$$
>
> **Paso 5 — Formulación alternativa (primera ecuación $T\,ds$ con $c_v$ y $v$):**
> $$\Delta s = c_v\ln\frac{T_2}{T_1} + R\ln\frac{v_2}{v_1}.$$
>
> **Verificación:** proceso isotérmico ($T_1 = T_2$): $\Delta s = -R\ln(P_2/P_1) = R\ln(v_2/v_1)$. Al expandirse ($P_2 < P_1$, $v_2 > v_1$): $\Delta s > 0$ — entropía crece al expandirse el gas a $T$ cte, consistente con Boltzmann. $\checkmark$ $\blacksquare$

---

## Interpretación estadística: $S = k_B \ln \Omega$

> [!teoria]
> La interpretación macroscópica de Clausius conecta con la mecánica estadística de Boltzmann (1877). Para un sistema con $\Omega$ microestados accesibles (configuraciones microscópicas compatibles con el estado macroscópico):
> $$S = k_B \ln\Omega,$$
> donde $k_B = 1.380649 \times 10^{-23}\,\text{J/K}$ es la constante de Boltzmann.
>
> **¿Por qué crece $S$ en procesos irreversibles?** Si se abren compartimentos (gas que se expande libremente) o se mezclan sustancias, el número de microestados compatibles aumenta enormemente. La "flecha del tiempo" es la tendencia estadística de ir de estados de baja $\Omega$ (altamente organizados) a estados de alta $\Omega$ (más dispersos).
>
> Relación cuantitativa: $R = N_A k_B$. La entropía específica $s$ de 1 mol es:
> $$s = \frac{S}{n} = k_B N_A \ln \Omega^{1/N_A} = R \ln \Omega^{1/N_A} \quad [{\rm J/(mol\cdot K)}].$$
>
> **Tercer principio:** a $T \to 0$ K, un cristal perfecto tiene $\Omega = 1$ (un único microestado): $S = k_B \ln 1 = 0$. Esto fija el cero absoluto de la entropía.

![[entropia_microestados_expansion.svg|440]]
*Expansión libre de gas: antes de abrir la válvula, el gas está confinado a la mitad izquierda del recipiente — pocos microestados accesibles ($\Omega_1$). Tras abrir, el gas ocupa todo el volumen — muchos más microestados ($\Omega_2 \gg \Omega_1$). La entropía crece como $\Delta S = k_B \ln(\Omega_2/\Omega_1) > 0$.*

---

## Entropía de sustancias: cálculo en la región bifásica

> [!proposicion]
> En la región de saturación, la entropía específica de la mezcla se calcula por la regla de la palanca:
> $$s = s_f + x\,s_{fg}, \qquad s_{fg} = s_g - s_f = \frac{h_{fg}}{T_{sat}},$$
> donde la última igualdad proviene del proceso de cambio de fase isobárico-isotérmico: a presión constante, el calor de vaporización $h_{fg}$ se intercambia a temperatura constante $T_{sat}$, por lo que $\Delta s = h_{fg}/T_{sat}$.

---

## Ejemplo: generación de entropía en intercambiador de calor

> [!ejemplo]
> **Vapor de agua a $P = 1\,\text{MPa}$, $T_1 = 400\,°\text{C}$ se condensa en un intercambiador adiabático hasta $T_2 = 40\,°\text{C}$ (líquido). El agua de enfriamiento entra a $20\,°\text{C}$ y sale a $35\,°\text{C}$.** Calcular la entropía generada por kg de vapor.
>
> **Paso 1 — Estado del vapor:** de tablas a $1\,\text{MPa}$, $400\,°\text{C}$: $h_1 = 3263.9\,\text{kJ/kg}$, $s_1 = 7.4651\,\text{kJ/(kg·K)}$.
>
> **Paso 2 — Estado de salida:** líquido a $40\,°\text{C}$, $1\,\text{MPa}$ (líquido comprimido $\approx$ saturado a $40\,°\text{C}$): $h_2 \approx 167.5\,\text{kJ/kg}$, $s_2 \approx 0.5721\,\text{kJ/(kg·K)}$.
>
> **Paso 3 — Calor cedido al agua de enfriamiento por kg de vapor:**
> $$q_{\rm agua} = h_1 - h_2 = 3263.9 - 167.5 = 3096.4\,\text{kJ/kg_{vapor}}.$$
>
> **Paso 4 — Cambio de entropía del agua de enfriamiento** (con $c_p = 4.18\,\text{kJ/(kg·K)}$, $T_{\rm ent} = 293\,\text{K}$, $T_{\rm sal} = 308\,\text{K}$):
> $$\dot{m}_{\rm agua} = \frac{q_{\rm agua}}{c_p\Delta T_{\rm agua}} = \frac{3096.4}{4.18 \times 15} = 49.4\,\text{kg agua/kg vapor.}$$
> $$\Delta s_{\rm agua} = 49.4 \times 4.18 \times \ln\frac{308}{293} = 49.4 \times 4.18 \times 0.0499 = 10.31\,\text{kJ/(K·kg_{vapor})}.$$
>
> **Paso 5 — Entropía generada por la Segunda Ley:**
> $$s_{\rm gen} = (s_2 - s_1) + \Delta s_{\rm agua} = (0.5721 - 7.4651) + 10.31 = -6.893 + 10.31 = 3.42\,\text{kJ/(kg·K)}.$$
> $s_{\rm gen} > 0$ confirma que el proceso es irreversible. La irreversibilidad principal es la transferencia de calor a través de una diferencia de temperatura finita ($\sim 365\,°\text{C}$ → $35\,°\text{C}$). $\blacksquare$

---

## Relación con otras notas

> [!info]
> - Las cuatro relaciones de Maxwell incluyen derivadas de $S$: ver [[Maxwell]].
> - Procesos isentrópicos ($\Delta s = 0$): se analizan en turbinas y compresores ideales; ver [[Turbinas Ideales]].
> - El principio de aumento de entropía organiza el análisis de ciclos: ver [[Segunda Ley SC]].
> - La entropía conecta con la exergía: $\dot{E}x_{\rm destruida} = T_0 \dot{S}_{\rm gen}$; ver [[Exergia]].
> - La función de entropía $s(T,P)$ para gases ideales se tabula en tablas de aire estándar; ver [[Gas Ideal]].

> [!info]
> **Convención:** $S$: extensiva [kJ/K]; $s = S/m$ [kJ/(kg·K)]; $\bar{s}$ [kJ/(mol·K)].
> Subíndices: $s_f$ líquido sat., $s_g$ vapor sat., $s_{fg} = s_g - s_f$.

> [!referencia]
> Borgnakke & Sonntag, *Fundamentals of Thermodynamics*, caps. 8–9 y §12.1; Çengel & Boles, *Termodinámica*, §6-1 a 6-5 y §7-1 a 7-7; Callen, *Thermodynamics*, §1-7 a 1-10 y cap. 4; Fermi, *Thermodynamics*, cap. IV; Boltzmann, *Vorlesungen über Gastheorie* (1896).
