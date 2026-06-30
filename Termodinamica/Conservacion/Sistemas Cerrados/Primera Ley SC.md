---
title: "Primera Ley (Sistema Cerrado)"
order: 1
tags:
  - termodinamica
  - conservacion
  - energia
  - primera_ley
  - sistema_cerrado
draft: false
aliases:
  - primera ley SC
  - balance energetico SC
  - conservacion energia SC
---

# Primera Ley — Sistema Cerrado

> [!definicion]
> Para un [[Sistemas Cerrados/index | sistema cerrado]] (masa fija), la **primera ley de la termodinámica** establece:
> $$\boxed{\Delta U = Q - W.}$$
> En forma diferencial: $dU = \delta Q - \delta W$.
>
> - $U$ [kJ]: energía interna total del sistema.
> - $Q > 0$ [kJ]: calor **que entra** al sistema.
> - $W > 0$ [kJ]: trabajo **que realiza** el sistema sobre el entorno.
>
> La primera ley no es un axioma matemático — es una generalización de la observación experimental de Joule (1843–1849): la combinación $Q - W$ siempre produce el mismo cambio de estado, sin importar el camino tomado. Eso implica que existe una función de estado $U$ tal que $\Delta U = Q - W$.

---

## Por qué $Q - W$ es función de estado (experimentos de Joule)

> [!demostracion]
> **Meta:** argumentar que $Q - W$ es independiente del camino entre dos estados, lo que implica la existencia de $U$ como función de estado.
>
> **Hipótesis:** consideramos un sistema cerrado que pasa del estado 1 al estado 2 por dos caminos distintos: A (calentamiento reversible) y B (agitación mecánica adiabática). Ambos caminos producen el mismo cambio de temperatura medible.
>
> **Paso 1 — Camino A: calentamiento a volumen constante.**
> El sistema absorbe calor $Q_A$, realiza trabajo nulo ($W_A = 0$ si el volumen es constante). Resultado observable: temperatura sube de $T_1$ a $T_2$.
>
> **Paso 2 — Camino B: agitación mecánica adiabática.**
> El sistema recibe trabajo de paletas agitadoras $W_B < 0$ (trabajo entra), no hay calor ($Q_B = 0$). Resultado observable: temperatura sube de $T_1$ a la misma $T_2$.
>
> **Paso 3 — Observación de Joule.**
> Si los mismos estados 1 y 2 son alcanzables por dos caminos tan diferentes (A y B), el cambio de temperatura — y por tanto el cambio de "contenido energético" — es el mismo en ambos. Es decir, $Q_A - W_A = Q_B - W_B$, aunque $Q_A \ne Q_B$ y $W_A \ne W_B$ individualmente.
>
> **Paso 4 — Definir $U$ como la función de estado subyacente.**
> El argumento anterior (generalizable a cualquier par de caminos entre 1 y 2) implica que la cantidad $Q - W$ solo depende de los estados extremos:
> $$U_2 - U_1 = \Delta U \equiv Q - W.$$
> $U$ es el nombre que se le da a esa función de estado. $\blacksquare$
>
> **Paso 5 — Verificación de límites.**
> - Sistema aislado ($Q = 0$, $W = 0$): $\Delta U = 0$ — la energía se conserva.
> - Ciclo ($\Delta U = 0$): $Q_{\rm neto} = W_{\rm neto}$ — la eficiencia de un ciclo de potencia está limitada por este balance.

---

## Trabajo de frontera y su representación en el diagrama $P$-$v$

> [!teoria]
> El trabajo más común en sistemas cerrados es el **trabajo de frontera** (boundary work): la fuerza $P_{\rm ext}\,A$ sobre el pistón multiplicada por el desplazamiento $dL = dV/A$:
> $$\delta W_b = P_{\rm ext}\,dV.$$
> Para un proceso **cuasiestático** (equilibrio en todo momento), $P_{\rm ext} = P_{\rm sistema}$ y:
> $$W_b = \int_1^2 P\,dV.$$
> Esta integral es el **área bajo la curva $P$-$v$** en el diagrama de estados. Por eso el diagrama $P$-$v$ es central: el área debajo del proceso es el trabajo intercambiado.
>
> Para proceso **irreversible** (expansión libre, por ejemplo): $W_{\rm irr} < \int P\,dV$. El gas expande pero no toda la caída de presión se convierte en trabajo — parte se disipa como irreversibilidad interna.

![[primera_ley_SC_diagrama_Pv.svg|440]]
*Dos caminos entre los estados 1 y 2 en el diagrama $P$-$v$: el área bajo el camino A (sombreado oscuro) es mayor que el área bajo el camino B (sombreado claro), mostrando que el trabajo $W$ depende del camino. Pero $\Delta U = Q_A - W_A = Q_B - W_B$ es el mismo — $U$ no depende del camino.*

---

## Formas particulares según el proceso

> [!proposicion]
> **Proceso isocórico** ($V = \text{cte}$, $W_b = 0$, sin trabajo de eje):
> $$\Delta U = Q_v.$$
> El calor medido a volumen constante es exactamente $\Delta U$ — esto es lo que mide la **bomba calorimétrica**.
>
> **Proceso isobárico** ($P = \text{cte}$, trabajo de eje nulo):
> $$Q_P = \Delta U + P\Delta V = \Delta(U + PV) = \Delta H.$$
> El calor a presión constante es exactamente $\Delta H$ — esto define la entalpía como la variable natural del proceso isobárico. Ver [[Entalpia]].
>
> **Proceso adiabático** ($Q = 0$):
> $$\Delta U = -W.$$
> Todo el cambio de energía interna proviene del trabajo realizado.
>
> **Ciclo** ($\Delta U = 0$):
> $$Q_{\rm neto} = W_{\rm neto}.$$
> La primera ley de los ciclos de potencia: el calor neto absorbido es igual al trabajo neto producido.

---

## Para gas ideal: $\Delta U = c_v\,\Delta T$

> [!proposicion]
> Para gas ideal ($u = u(T)$ por el experimento de Joule-expansión libre), la energía interna específica solo depende de $T$:
> $$du = c_v(T)\,dT \implies \Delta u = \int_{T_1}^{T_2} c_v(T)\,dT.$$
> Para $c_v \approx \text{const}$ (rango de temperatura moderado): $\Delta u = c_v\,\Delta T$.
>
> **Importancia:** aunque el proceso no sea isocórico, si la sustancia es gas ideal, $\Delta u$ solo depende del cambio de temperatura y se puede calcular siempre con $c_v\,\Delta T$. No hay que conocer el camino.

---

## Ejemplo 1: expansión isotérmica de gas ideal

> [!ejemplo]
> **Gas ideal** ($m = 1\,\text{kg}$, $R = 0.287\,\text{kJ/(kg·K)}$, $T = 300\,\text{K}$) **se expande reversiblemente de $P_1 = 500\,\text{kPa}$ a $P_2 = 100\,\text{kPa}$.** Calcular $Q$ y $W$.
>
> **Paso 1 — Identificar el tipo de sustancia y proceso.** Gas ideal isotérmico: $u = u(T)$, $T = \text{cte}$ → $\Delta u = 0$ → $\Delta U = 0$.
>
> **Paso 2 — Primera ley con $\Delta U = 0$:** $Q = W$.
>
> **Paso 3 — Calcular el trabajo reversible** (el proceso es cuasiestático, $P = mRT/V$):
> $$W = \int_1^2 P\,dV = mRT\int_{V_1}^{V_2}\frac{dV}{V} = mRT\ln\frac{V_2}{V_1} = mRT\ln\frac{P_1}{P_2}.$$
>
> **Paso 4 — Sustituir valores:**
> $$W = 1 \times 0.287 \times 300 \times \ln\frac{500}{100} = 86.1 \times \ln 5 = 86.1 \times 1.609 = 138.5\,\text{kJ}.$$
>
> **Paso 5 — Verificar e interpretar:** $Q = W = 138.5\,\text{kJ}$. El sistema absorbe calor del entorno ($Q > 0$) y lo convierte íntegramente en trabajo ($W > 0$). Que $Q = W$ no viola la segunda ley (ciclo no): el proceso no es cíclico — el sistema pasa de un estado de menor volumen a uno de mayor volumen, por lo que la entropía crece ($\Delta S = Q/T > 0$). $\blacksquare$

---

## Ejemplo 2: compresión adiabática reversible

> [!ejemplo]
> **Aire** ($m = 2\,\text{kg}$, $c_v = 0.718\,\text{kJ/(kg·K)}$, $\gamma = 1.4$) **se comprime adiabáticamente de $T_1 = 300\,\text{K}$, $P_1 = 100\,\text{kPa}$ a $P_2 = 600\,\text{kPa}$.** Calcular $W$.
>
> **Paso 1 — Proceso adiabático:** $Q = 0$ → $\Delta U = -W$.
>
> **Paso 2 — Estado final por relación isentrópica** (proceso reversible → $s_2 = s_1$ → proceso isentrópico):
> $$T_2 = T_1\left(\frac{P_2}{P_1}\right)^{(\gamma-1)/\gamma} = 300 \times 6^{0.2857} = 300 \times 1.669 = 500.7\,\text{K}.$$
>
> **Paso 3 — Calcular $\Delta U$:**
> $$\Delta U = m\,c_v\,(T_2 - T_1) = 2 \times 0.718 \times (500.7 - 300) = 2 \times 0.718 \times 200.7 = 288.2\,\text{kJ}.$$
>
> **Paso 4 — Trabajo:**
> $$W = -\Delta U = -288.2\,\text{kJ}.$$
> El signo negativo indica que el **trabajo entra** al sistema (el compresor hace trabajo sobre el gas). En un compresor, $W < 0$ es lo esperado: la energía interna sube porque el trabajo comprime y calienta el gas. $\blacksquare$

---

## Relación con otras notas

> [!info]
> - [[Segunda Ley SC]] — añade la restricción de dirección: $\Delta S \ge \int \delta Q/T$.
> - [[Balance de Exergia SC]] — cuantifica el trabajo útil máximo y las pérdidas por irreversibilidad.
> - [[Energia Interna]] — definición y propiedades de $U$ como función de estado.
> - [[Entalpia]] — explica por qué $Q_P = \Delta H$ y cómo la entalpía aparece en los balances de VC.
> - [[Procesos/index | Procesos Termodinámicos]] — aplicaciones a procesos isocórico, isobárico, isotérmico, adiabático y politrópico.

> [!warning]
> - **Signo de $W$:** algunos textos (especialmente europeos) definen $W$ positivo cuando entra al sistema, dando $\Delta U = Q + W$. Verificar la convención antes de usar datos de otra fuente.
> - **Trabajo de frontera vs. trabajo total:** $W$ incluye todos los modos de trabajo. Para sistema cerrado sin trabajo de eje ni eléctrico, $W = W_b = \int P\,dV$, pero si hay un agitador o resistencia eléctrica, hay que sumarlos.
> - **$dU = T\,dS - P\,dV$ solo para procesos reversibles** en el sentido de que $\delta Q_{\rm rev} = T\,dS$ y $\delta W_{\rm rev} = P\,dV$, pero $\Delta U = Q - W$ es general para cualquier proceso entre estados de equilibrio.

> [!referencia]
> Borgnakke & Sonntag, *Fundamentals of Thermodynamics*, cap. 4; Çengel & Boles, *Termodinámica*, cap. 4; Fermi, *Thermodynamics*, cap. II; Joule, "On the Mechanical Equivalent of Heat", *Phil. Trans. R. Soc.* 140 (1850).
