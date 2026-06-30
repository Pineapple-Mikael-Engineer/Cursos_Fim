---
title: Sistemas Eléctricos (Circuitos Pasivos)
order: 3
tags:
  - control-clasico
  - dominios-fisicos
  - modelado
draft: false
aliases:
  - electrico
  - circuitos pasivos
  - RLC
---

# Sistemas Eléctricos (Circuitos Pasivos)

> [!definicion]
> Un circuito pasivo se modela combinando tres elementos —resistencia $R$, inductancia $L$ y capacitancia $C$— mediante las leyes de Kirchhoff, trabajando con **impedancias** $Z(s)$ en Laplace. Para el RLC serie con entrada $V_i$ y salida en el capacitor $V_o$:
> $$Z_R=R,\quad Z_L=Ls,\quad Z_C=\frac{1}{Cs}\qquad\Longrightarrow\qquad G(s)=\frac{V_o(s)}{V_i(s)}=\frac{1}{LCs^2+RCs+1}.$$

> [!info]
> Es uno de los [[Funcion Transferencia/index | dominios físicos]] básicos del modelado. Es **análogo** al [[Mecanico Traslacional | mecánico traslacional]] (voltaje↔fuerza, corriente↔velocidad, $L$↔$m$, $1/C$↔$k$, $R$↔$b$) y comparte estructura $R$–$C$ con los dominios [[Termico | térmico]], [[Fluidos Nivel | hidráulico]] y [[Neumatico | neumático]]. Produce dinámica de [[Primer Orden]] (un reactivo) o de segundo orden (RLC).

---

## Ejemplo

> [!ejemplo]
> **RC serie con valores numéricos.** Sea $R=1\ \text{k}\Omega$, $C=1\ \mu\text{F}$, entrada $V_i$, salida $V_o$ en el capacitor. Hallar la FT, el polo y la constante de tiempo.
>
> ![[rc_serie.svg]]
>
> **Paso 1 — Malla (LVK):** $V_i(s)=V_R(s)+V_o(s)=R\,I(s)+V_o(s)$.
>
> **Paso 2 — Relación del capacitor:** la corriente que circula es $I(s)=C\,s\,V_o(s)$ (toda la corriente de la malla pasa por $C$).
>
> **Paso 3 — Sustituir y despejar:**
> $$V_i(s)=RC\,s\,V_o(s)+V_o(s)=V_o(s)\,(RCs+1)\;\Longrightarrow\;G(s)=\frac{V_o(s)}{V_i(s)}=\frac{1}{RCs+1}.$$
>
> **Paso 4 — Números:** $RC=(10^3)(10^{-6})=10^{-3}\ \text{s}$, luego
> $$G(s)=\frac{1}{10^{-3}s+1},\qquad \text{polo en } s=-\frac{1}{RC}=-1000\ \text{rad/s},\qquad \tau=RC=1\ \text{ms}.$$
> Primer orden, filtro **pasa bajos**: en DC ($s=0$) gana $1$; a alta frecuencia atenúa.

> [!ejemplo]
> **RLC serie (segundo orden).** Sea $R=2\ \Omega$, $L=1\ \text{H}$, $C=0.5\ \text{F}$, salida $V_o$ en el capacitor.
>
> ![[rlc_serie.svg]]
>
> **Paso 1 — Malla:** $V_i=V_R+V_L+V_o$, con $V_R=R\,I$, $V_L=Ls\,I$ y $I=Cs\,V_o$.
>
> **Paso 2 — Sustituir:**
> $$V_i(s)=\big(LCs^2+RCs+1\big)V_o(s)\;\Longrightarrow\;G(s)=\frac{1}{LCs^2+RCs+1}=\frac{1/LC}{s^2+\frac{R}{L}s+\frac{1}{LC}}.$$
>
> **Paso 3 — Parámetros de 2.º orden:**
> $$\omega_n=\frac{1}{\sqrt{LC}}=\frac{1}{\sqrt{0.5}}\approx1.41\ \text{rad/s},\qquad \zeta=\frac{R}{2}\sqrt{\frac{C}{L}}=\frac{2}{2}\sqrt{0.5}\approx0.71.$$
>
> **Paso 4 — Tipo de respuesta:** como $\zeta\approx0.71<1$, es **subamortiguado** (oscila con [[Sobrepico Mp | sobrepico]]). Los polos son $s=-1\pm j$. Si la salida se tomara en el inductor, $G(s)=s^2/(s^2+\frac{R}{L}s+\frac{1}{LC})$, un **pasa altos** de 2.º orden (doble cero en el origen).

---

## Elementos y leyes constitutivas

> [!teoria]
> El modelado eléctrico usa tres elementos pasivos. Cada uno fija una relación entre el voltaje que soporta y la corriente que lo atraviesa; en Laplace esa relación es la **impedancia** $Z(s)=V(s)/I(s)$:
>
> | Elemento | Parámetro (unidad) | Relación $v$–$i$ | Impedancia $Z(s)$ | Almacena / disipa |
> |---|---|---|---|---|
> | Resistencia | $R$ ($\Omega$) | $v=R\,i$ | $R$ (algebraico) | disipa (calor) |
> | Inductancia | $L$ (H) | $v=L\,\dot i$ | $Ls$ (derivador) | energía magnética |
> | Capacitancia | $C$ (F) | $i=C\,\dot v$ | $1/Cs$ (integrador) | energía eléctrica |
>
> Las leyes que las unen son las de **Kirchhoff**: la suma de voltajes en una malla es cero (LVK, $\sum V_k=0$) y la suma de corrientes en un nodo es cero (LCK, $\sum I_k=0$). Trabajando con impedancias, $R$, $L$ y $C$ se combinan en serie y paralelo igual que resistencias.

> [!info] Carácter integrador/derivador
> - **Inductor:** $V=Ls\,I$ → el voltaje es la derivada de la corriente (cero en el origen visto desde $I$).
> - **Capacitor:** $V=\frac{1}{Cs}I$ → el voltaje es la integral de la corriente (polo en el origen).
> - **Resistencia:** relación algebraica, sin dinámica.

---

## Más configuraciones resueltas

> [!ejemplo] RC, salida en la resistencia
> Entrada $V_i$, salida $V_R$. Con $V_R=R\,I=RC\,s\,V_C$ y $V_C=V_i-V_R$:
> $$V_R(1+RCs)=RCs\,V_i\;\Longrightarrow\;G(s)=\frac{RCs}{RCs+1}.$$
> Cero en $s=0$ → **pasa altos** de 1er orden (derivador filtrado).

> [!ejemplo] RL serie
> ![[rl_serie.svg]]
> Salida en el inductor: $G(s)=\dfrac{Ls}{R+Ls}=\dfrac{s}{s+R/L}$ (pasa altos). Salida en la resistencia: $G(s)=\dfrac{R/L}{s+R/L}$ (pasa bajos). Ambos comparten el polo $s=-R/L$.

> [!ejemplo] Divisor de voltaje (atajo)
> En un circuito **serie** el voltaje se reparte en proporción a las impedancias:
> $$V_k(s)=\frac{Z_k(s)}{Z_{\text{total}}(s)}\,V_{\text{total}}(s).$$
> Para el RC: $Z_{\text{total}}=R+\frac{1}{Cs}=\frac{RCs+1}{Cs}$, luego $V_C=\frac{1/Cs}{(RCs+1)/Cs}V_i=\frac{1}{RCs+1}V_i$ (mismo resultado que el ejemplo, sin escribir la malla). El divisor de corriente es el dual para ramas en paralelo (en admitancias).

---

## Tabla de funciones de transferencia

> [!info] Circuitos pasivos comunes
> | Circuito | Entrada | Salida | $G(s)$ | Tipo |
> |---|---|---|---|---|
> | RC serie | $V_i$ | $V_C$ | $\dfrac{1}{RCs+1}$ | Pasa bajos 1er orden |
> | RC serie | $V_i$ | $V_R$ | $\dfrac{RCs}{RCs+1}$ | Pasa altos 1er orden |
> | RL serie | $V_i$ | $V_R$ | $\dfrac{R/L}{s+R/L}$ | Pasa bajos 1er orden |
> | RL serie | $V_i$ | $V_L$ | $\dfrac{s}{s+R/L}$ | Pasa altos 1er orden |
> | RLC serie | $V_i$ | $V_C$ | $\dfrac{1/LC}{s^2+\frac{R}{L}s+\frac{1}{LC}}$ | Pasa bajos 2do orden |
> | RLC serie | $V_i$ | $V_L$ | $\dfrac{s^2}{s^2+\frac{R}{L}s+\frac{1}{LC}}$ | Pasa altos 2do orden |

---

## Receta de modelado

> [!algoritmo]
> Para obtener la FT de un circuito pasivo:
> 1. **Impedancias.** Sustituir cada elemento por su $Z(s)$: $R\to R$, $L\to Ls$, $C\to 1/Cs$.
> 2. **Topología.** Identificar mallas (serie) y nodos (paralelo); combinar impedancias o plantear LVK/LCK.
> 3. **Variable común.** En serie, la corriente $I$ es la misma; en paralelo, el voltaje es el mismo. Expresar todo en función de esa variable.
> 4. **Divisor (atajo).** Si es un divisor serie/paralelo, aplicar la fórmula del divisor directamente.
> 5. **Despejar la FT** $V_{\text{sal}}(s)/V_{\text{ent}}(s)$ con CI nulas.

> [!info] Analogía fuerza-voltaje
> | Eléctrico | Mecánico (traslacional) |
> |---|---|
> | Voltaje $V$ | Fuerza $F$ |
> | Corriente $I$ | Velocidad $v$ |
> | Resistencia $R$ | Amortiguador $b$ |
> | Inductancia $L$ | Masa $m$ |
> | Capacitancia $C$ | Compliancia $1/k$ (inverso del resorte) |
>
> Permite reutilizar la intuición mecánica: un inductor "se opone a cambios de corriente" igual que una masa a cambios de velocidad. Ver [[Mecanico Traslacional | mecánico traslacional]].

> [!info] En MATLAB
> ```matlab
> R=2; L=1; C=0.5;
> G = tf([1], [L*C R*C 1]);   % RLC serie, salida en C
> damp(G)                     % polos, wn y zeta
> step(G)                     % respuesta al escalon
> ```

---

## Limitaciones

> [!warning]
> 1. **Circuitos pasivos lineales:** solo combina $R$, $L$, $C$; no incluye fuentes controladas, op-amps ni transistores (ver [[Electronica]]).
> 2. **Componentes ideales:** $R$, $L$, $C$ constantes, sin tolerancias ni parásitos.
> 3. **Rango de frecuencia:** a alta frecuencia inductores y capacitores se comportan de forma no ideal.
> 4. **Condiciones iniciales nulas:** la FT asume CI nulas.

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Elementos | $R$, $L$, $C$ |
> | Impedancias | $R$, $Ls$, $1/Cs$ |
> | Leyes | Kirchhoff (LVK, LCK) |
> | FT típica (RLC) | $G(s)=\dfrac{1/LC}{s^2+\frac{R}{L}s+\frac{1}{LC}}$ |
> | Parámetros | $\omega_n=1/\sqrt{LC}$, $\zeta=\frac{R}{2}\sqrt{C/L}$ |
> | Orden | 1 por reactivo independiente |

> [!corolario]
> Modelar un circuito pasivo es sustituir cada elemento por su impedancia y aplicar Kirchhoff (o el divisor de voltaje como atajo): un reactivo da 1er orden ($RC$, $RL$); dos dan 2.º orden (RLC) con $\omega_n$ y $\zeta$ análogos a los del [[Mecanico Traslacional | sistema mecánico]]. La misma estructura $R$–$C$ reaparece en los dominios [[Termico | térmico]], [[Fluidos Nivel | hidráulico]] y [[Neumatico | neumático]].

> [!referencia]
> - Dominio análogo mecánico: [[Mecanico Traslacional]].
> - Elementos activos (op-amps): [[Electronica]].
> - Respuesta de primer orden: [[Primer Orden]].
> - Analogías $R$–$C$: [[Termico]] · [[Fluidos Nivel]] · [[Neumatico]].
