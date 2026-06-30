---
title: Electrónica (Amplificadores Operacionales)
order: 7
tags:
  - control-clasico
  - dominios-fisicos
  - modelado
draft: false
aliases:
  - electronica
  - amplificadores
  - op-amp
  - operacional
---

# Electrónica-Amplificadores Operacionales

> [!definicion]
> Un amplificador operacional (op-amp) con realimentación negativa se modela como un **bloque** cuya FT depende solo de las impedancias de entrada $Z_1(s)$ y realimentación $Z_f(s)$. En configuración inversora:
> $$G(s)=\frac{V_{out}(s)}{V_{in}(s)}=-\frac{Z_f(s)}{Z_1(s)}.$$
> Las dos reglas del op-amp ideal ($I_+=I_-=0$ y $V_+=V_-$) bastan para deducir cualquier configuración.

> [!info]
> Es uno de los [[Funcion Transferencia/index | dominios físicos]] del modelado; añade **elementos activos** a los circuitos pasivos de [[Electrico | sistemas eléctricos]]. Eligiendo $Z_1$, $Z_f$ se construyen ganancias, integradores y derivadores → bloques directos de un [[PID/index | controlador PID]].

---

## Ejemplo

> [!ejemplo]
> **Amplificador inversor con valores numéricos.** Sea $R_1=10\ \text{k}\Omega$, $R_f=100\ \text{k}\Omega$. Hallar la FT.
>
> ![[inversor.svg]]
>
> **Paso 1 — Masa virtual:** la entrada $+$ está a tierra, $V_+=0$. Por la regla 2, $V_-=V_+=0$ (la realimentación fuerza esta condición).
>
> **Paso 2 — Corriente de entrada** (regla 1, no entra corriente al op-amp):
> $$I_1=\frac{V_{in}-V_-}{R_1}=\frac{V_{in}}{R_1}.$$
>
> **Paso 3 — Toda $I_1$ pasa por $R_f$:** $I_f=I_1$, y $I_f=\dfrac{V_--V_{out}}{R_f}=\dfrac{-V_{out}}{R_f}$.
>
> **Paso 4 — Igualar y despejar:**
> $$\frac{V_{in}}{R_1}=-\frac{V_{out}}{R_f}\;\Longrightarrow\;G(s)=\frac{V_{out}}{V_{in}}=-\frac{R_f}{R_1}=-\frac{100}{10}=-10.$$
> Ganancia $-10$: amplifica $10\times$ e invierte la fase. Impedancia de entrada $Z_{in}=R_1=10\ \text{k}\Omega$.

> [!ejemplo]
> **Integrador (Miller).** Mismo esquema inversor pero con $Z_f=1/(C_f s)$ en lugar de $R_f$. Sea $R_1=10\ \text{k}\Omega$, $C_f=1\ \mu\text{F}$.
>
> ![[integrador.svg]]
>
> **Paso 1 — Reglas:** $V_-=0$, $I_1=V_{in}/R_1$.
>
> **Paso 2 — Corriente por $C_f$:** $I_f=\dfrac{V_--V_{out}}{1/(C_f s)}=-C_f s\,V_{out}$.
>
> **Paso 3 — Igualar $I_1=I_f$:**
> $$\frac{V_{in}}{R_1}=-C_f s\,V_{out}\;\Longrightarrow\;G(s)=-\frac{1}{R_1 C_f s}=-\frac{1}{(10^4)(10^{-6})\,s}=-\frac{100}{s}.$$
> Un **polo en el origen** → integrador puro (ganancia infinita en DC). Atajo: $G=-Z_f/Z_1=-\dfrac{1/(C_f s)}{R_1}$, mismo resultado.

---

## Reglas del op-amp ideal

> [!teoria]
> ![[opamp_ideal.svg]]
>
> Un op-amp ideal cumple: ganancia diferencial $A_{ol}\to\infty$, impedancia de entrada $Z_{in}\to\infty$, impedancia de salida $Z_{out}=0$, ancho de banda infinito y offset nulo. Con **realimentación negativa** estas idealizaciones se condensan en dos reglas de análisis:
>
> | Regla | Enunciado | Por qué |
> |---|---|---|
> | 1 | $I_+=I_-=0$ | impedancia de entrada infinita: no entra corriente |
> | 2 | $V_+=V_-$ | ganancia infinita: la salida ajusta hasta igualar las entradas |
>
> La regla 3 (auxiliar): la salida hace lo necesario para mantener $V_+=V_-$ mientras no se sature. Cuando $V_+$ está a tierra, la regla 2 crea una **masa virtual** ($V_-\approx0$) sin conexión física a tierra.

> [!info] Conservación de energía
> $$P_{\text{entrada}}+P_{\text{alimentación}}=P_{\text{salida}}+P_{\text{disipada}}.$$
> El op-amp no "crea" energía: la potencia de salida proviene de la fuente de alimentación ($\pm15\,$V típica); la entrada aporta muy poca (alta impedancia). Por eso la salida nunca supera los rieles de alimentación (saturación).

---

## Más configuraciones resueltas

> [!ejemplo] No inversor
> ![[no_inversor.svg]]
> $V_+=V_{in}\Rightarrow V_-=V_{in}$. Corriente en $R_1$ (de $V_-$ a tierra): $I_1=V_{in}/R_1$. Como $I_f=I_1=\dfrac{V_{out}-V_{in}}{R_f}$:
> $$G(s)=1+\frac{R_f}{R_1}\;\;(\ge1,\ \text{sin inversión}).$$
> Impedancia de entrada idealmente infinita.

> [!ejemplo] Seguidor (buffer)
> ![[seguidor.svg]]
> Salida conectada a $V_-$ ($R_f=0$, $R_1=\infty$): $V_{out}=V_-=V_+=V_{in}$, luego $G(s)=1$. Aísla etapas (separador de impedancias).

> [!ejemplo] Derivador
> ![[derivador.svg]]
> Con $Z_1=1/(C_1 s)$, $Z_f=R_f$: $I_1=C_1 s\,V_{in}$, $I_f=-V_{out}/R_f$, luego
> $$G(s)=-R_f C_1 s\;\;(\text{cero en el origen}).$$
> Muy ruidoso: amplifica alta frecuencia; en la práctica se añade $R_1$ en serie con $C_1$.

> [!ejemplo] Filtro activo pasa bajos (inversor)
> ![[filtro_pasa_bajos.svg]]
> $R_f$ en paralelo con $C_f$ da $Z_f=\dfrac{R_f}{R_f C_f s+1}$, luego
> $$G(s)=-\frac{Z_f}{R_1}=-\frac{R_f/R_1}{R_f C_f s+1}.$$
> Polo en $s=-1/(R_f C_f)$; ganancia DC $-R_f/R_1$. (También es el integrador práctico, con $R_f$ que evita la saturación DC del integrador puro.)

> [!ejemplo] Filtro activo pasa altos (inversor)
> ![[filtro_pasa_altos.svg]]
> Con $Z_1=1/(C_1 s)$ y $R_1$ en serie para limitar la ganancia: $G(s)=-\dfrac{R_f C_1 s}{R_1 C_1 s+1}$. Un cero en el origen y un polo en $s=-1/(R_1C_1)$ → pasa altos de 1er orden (derivador filtrado).

> [!ejemplo] Filtro Sallen-Key (pasa bajos 2.º orden)
> ![[sallen_key.svg]]
> Configuración no inversora con seguidor ($G=1$) y dos $RC$:
> $$G(s)=\frac{1}{R_1R_2C_1C_2\,s^2+(R_1C_2+R_2C_2)\,s+1},$$
> $$\omega_n=\frac{1}{\sqrt{R_1R_2C_1C_2}},\qquad \zeta=\frac{R_1C_2+R_2C_2}{2\sqrt{R_1R_2C_1C_2}}.$$
> Segundo orden **sin inductores**; ajustando $\zeta$ se obtiene Butterworth, Chebyshev, etc.

---

## Receta de modelado

> [!algoritmo]
> Para la FT de un circuito con op-amp ideal (configuración inversora):
> 1. **Impedancias.** Identificar $Z_1(s)$ (rama de entrada hacia $V_-$) y $Z_f(s)$ (realimentación de $V_{out}$ a $V_-$).
> 2. **Masa virtual.** Si $V_+$ está a tierra, $V_-=0$.
> 3. **Igualar corrientes.** $I_1=I_f$ porque no entra corriente al op-amp (regla 1).
> 4. **Aplicar la fórmula:** $G(s)=-Z_f/Z_1$. (No inversor: $G=1+Z_f/Z_1$.)
> 5. **Identificar polos/ceros** según las impedancias elegidas.

> [!info] Tabla de configuraciones (op-amp ideal)
> | Configuración | $G(s)$ | Tipo |
> |---|---|---|
> | Inversor | $-\dfrac{R_f}{R_1}$ | ganancia constante |
> | No inversor | $1+\dfrac{R_f}{R_1}$ | ganancia constante |
> | Seguidor | $1$ | buffer |
> | Integrador | $-\dfrac{1}{R_1C_f s}$ | polo en 0 |
> | Derivador | $-R_f C_1 s$ | cero en 0 |
> | Pasa bajos (inv.) | $-\dfrac{R_f/R_1}{R_f C_f s+1}$ | polo real |
> | Pasa altos (inv.) | $-\dfrac{R_f C_1 s}{R_1 C_1 s+1}$ | cero + polo |
> | Sallen-Key (bajos) | $\dfrac{1}{R_1R_2C_1C_2 s^2+(R_1C_2+R_2C_2)s+1}$ | 2.º orden |

> [!info] Op-amp como controlador
> - Inversor con ganancia $K$ → acción **proporcional** ($P$).
> - Integrador → acción **integral** ($I$).
> - Derivador → acción **derivativa** ($D$, ruidosa).
> - Combinaciones → **PID** analógico. Ver [[PID/index | PID]].

> [!info] En MATLAB
> ```matlab
> R1=1e4; Rf=1e5; Cf=1e-6;
> G_inv  = tf(-Rf/R1, 1);            % inversor: ganancia -10
> G_int  = tf(-1, [R1*Cf 0]);        % integrador: -1/(R1 Cf s)
> G_lp   = tf(-Rf/R1, [Rf*Cf 1]);    % pasa bajos activo
> bode(G_lp)
> ```

---

## Limitaciones del op-amp real

> [!warning]
> 1. **Ganancia finita:** $A_{ol}\sim10^5$–$10^6$, no infinita; afecta a ganancias altas.
> 2. **Corriente de polarización:** entran corrientes de bias (nA) → offset.
> 3. **Voltaje de offset:** diferencia residual entre entradas (mV) para salida nula.
> 4. **Ancho de banda limitado:** producto ganancia-ancho de banda constante (p.ej. 1 MHz); más ganancia, menos ancho de banda.
> 5. **Saturación:** la salida no supera los rieles $V_+$, $V_-$.
> 6. **Slew rate:** velocidad máxima de cambio (V/µs); distorsiona señales rápidas.

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Reglas ideales | $I_+=I_-=0$, $V_+=V_-$ |
> | FT inversora | $G(s)=-Z_f/Z_1$ |
> | FT no inversora | $G(s)=1+Z_f/Z_1$ |
> | Integrador | $-1/(R_1C_f s)$ |
> | Derivador | $-R_f C_1 s$ |
> | Uso en control | bloques $P$, $I$, $D$ del PID |

> [!corolario]
> Modelar un op-amp ideal con realimentación negativa se reduce a dos reglas y a la fórmula $G=-Z_f/Z_1$: cambiando $R$ por $C$ en $Z_1$ o $Z_f$ se pasa de ganancia constante a integrador, derivador o filtro. Es la base física del [[PID/index | controlador PID]] analógico y extiende los circuitos pasivos de [[Electrico | sistemas eléctricos]] al dominio activo.

> [!referencia]
> - Circuitos pasivos base: [[Electrico]].
> - Controlador que implementa: [[PID/index]].
> - Función de transferencia: [[Funcion Transferencia/index]].
