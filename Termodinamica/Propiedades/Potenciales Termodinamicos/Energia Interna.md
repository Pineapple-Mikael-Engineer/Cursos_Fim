---
title: "Energía Interna $U$"
order: 1
tags:
  - termodinamica
  - potenciales_termodinamicos
  - primera_ley
draft: false
aliases:
  - internal energy
  - U
  - energía interna
---

# Energía Interna $U$

> [!definicion]
> La **energía interna** $U$ es la energía total del sistema a escala microscópica: la suma de las energías cinéticas traslacionales, rotacionales y vibratorias de todas las moléculas, más las energías potenciales de las interacciones intermoleculares (enlaces de van der Waals, puentes de hidrógeno, etc.), más la energía interna de los núcleos atómicos. **No incluye** la energía cinética ni la potencial gravitatoria macroscópica del sistema como conjunto (esas son $EC$ y $EP$ del balance energético completo). En termodinámica de ingeniería solo los cambios $\Delta U$ son medibles; el valor absoluto de $U$ no tiene significado operativo por sí solo.
>
> Es un **potencial termodinámico** con variables naturales $(S, V)$: su diferencial $dU = T\,dS - P\,dV$ produce directamente $T$ y $P$ como derivadas parciales y genera la primera [[Maxwell | relación de Maxwell]].

---

## La relación fundamental $dU = T\,dS - P\,dV$

> [!demostracion]
> **Meta:** derivar la relación fundamental combinando la primera y segunda ley para un sistema cerrado simple compresible.
>
> **Hipótesis:** sistema cerrado, simple compresible (único modo de trabajo reversible: $P\,dV$), proceso cuasiestático.
>
> **Paso 1 — Primera ley en forma diferencial.**
> Para cualquier proceso infinitesimal en un sistema cerrado:
> $$dU = \delta Q - \delta W.$$
> Aquí $\delta Q$ y $\delta W$ son inexactas (dependen del camino), pero su diferencia $dU$ es exacta (función de estado).
>
> **Paso 2 — Expresar el trabajo para proceso cuasiestático.**
> El único modo de trabajo reversible es el de frontera:
> $$\delta W_{\rm rev} = P\,dV.$$
> Para proceso irreversible, $\delta W < P\,dV$ (se disipa trabajo en fricción); la igualdad es para proceso reversible.
>
> **Paso 3 — Segunda ley: definición de entropía.**
> Para cualquier proceso real o reversible que intercambia calor $\delta Q$ con la frontera a temperatura $T$:
> $$dS \ge \frac{\delta Q}{T} \quad \Longrightarrow \quad \delta Q \le T\,dS,$$
> con igualdad solo para procesos internamente reversibles.
>
> **Paso 4 — Combinar los pasos 1–3 para proceso reversible.**
> Sustituyendo $\delta Q_{\rm rev} = T\,dS$ y $\delta W_{\rm rev} = P\,dV$ en la primera ley:
> $$dU = T\,dS - P\,dV.$$
>
> **Paso 5 — Verificar que la relación es universal, no solo reversible.**
> Aunque la derivación usó procesos reversibles, el resultado es una relación entre **funciones de estado** ($U$, $S$, $V$) y variables de estado ($T$, $P$). Por tanto, es válida entre cualesquiera dos estados de equilibrio, independientemente del proceso que los conecte. $\blacksquare$
>
> **Interpretación:** $T\,dS$ es el calor reversible que entra al sistema; $P\,dV$ es el trabajo de expansión que el sistema realiza. La diferencia es el cambio de energía interna.

---

## Variables naturales y derivadas primeras

> [!proposicion]
> De $dU = T\,dS - P\,dV$ se leen directamente las propiedades como derivadas de $U$ respecto a sus variables naturales $(S, V)$:
> $$T = \left(\frac{\partial U}{\partial S}\right)_V, \qquad P = -\left(\frac{\partial U}{\partial V}\right)_S.$$
> La primera dice que la temperatura es el "precio en energía" por unidad de entropía ganada a volumen constante. La segunda dice que la presión es la resistencia del sistema a la expansión en proceso adiabático.

---

## Primera relación de Maxwell

> [!proposicion]
> Por la igualdad de derivadas cruzadas de $dU$ (condición de exactitud del diferencial):
> $$\frac{\partial^2 U}{\partial S\,\partial V} = \frac{\partial^2 U}{\partial V\,\partial S} \quad \Longrightarrow \quad \left(\frac{\partial T}{\partial V}\right)_S = -\left(\frac{\partial P}{\partial S}\right)_V.$$
> Es la primera relación de Maxwell; tiene menor uso práctico que la 3.ª y 4.ª (las de Helmholtz y Gibbs), que involucran $T$ y $P$ en lugar de $S$. Ver [[Maxwell]] para el desarrollo completo.

---

## El experimento de Joule: $u = u(T)$ para gas ideal

> [!teoria]
> En 1843, Joule realizó un experimento que mide directamente $(\partial U/\partial V)_T$: el coeficiente de Joule. Un recipiente de doble cámara adiabático contiene gas en una cámara y vacío en la otra. Al abrir la válvula que las separa, el gas se expande libremente hacia el vacío. Resultado: **la temperatura del gas no cambia** (medida con termómetro de alta sensibilidad). Esto implica que no se intercambió calor ($Q = 0$, sistema adiabático) ni trabajo ($W = 0$, expansión libre contra el vacío), por lo que $\Delta U = 0$ aunque $V$ cambió.

![[experimento_Joule_expansion_libre.svg|400]]
*Experimento de Joule: gas en cámara izquierda se expande libremente al vacío en cámara derecha. Sistema adiabático, sin trabajo. Si $T$ no cambia: $(\partial U/\partial V)_T = 0$ → $u = u(T)$ para el gas ideal.*

> [!demostracion]
> **Demostración de $(\partial u/\partial v)_T = 0$ para gas ideal a partir del resultado de Joule:**
>
> **Paso 1 — Resultado experimental.**
> En la expansión libre de Joule: $Q = 0$, $W = 0$ → $\Delta U = 0$. El volumen cambió ($\Delta V \neq 0$) pero la temperatura no ($\Delta T = 0$).
>
> **Paso 2 — Interpretar como derivada parcial.**
> Si $U$ pudiera depender de $V$ a $T$ constante, entonces el cambio de volumen con $\Delta T = 0$ habría cambiado $U$. Como $\Delta U = 0$ con $\Delta V \neq 0$ y $\Delta T = 0$:
> $$\left(\frac{\partial U}{\partial V}\right)_T = 0.$$
>
> **Paso 3 — Escribir la diferencial completa de $U(T,V)$.**
> $$dU = \left(\frac{\partial U}{\partial T}\right)_V\!dT + \underbrace{\left(\frac{\partial U}{\partial V}\right)_T}_{=\,0}\!dV = \left(\frac{\partial U}{\partial T}\right)_V\!dT = c_v\,dT.$$
>
> **Paso 4 — Conclusión: $U$ depende solo de $T$ para gas ideal.**
> $$dU = c_v(T)\,dT \quad \Longrightarrow \quad U = U(T) \text{ únicamente.}$$
> Esta propiedad caracteriza al gas ideal y es consecuencia de la ausencia de fuerzas intermoleculares: no hay energía potencial de interacción que dependa del volumen (la separación entre moléculas). Para gases reales, $(\partial u/\partial v)_T = \pi_T = T\alpha/\kappa_T - P \neq 0$; ver [[Identidades/index | Presión interna]]. $\blacksquare$

---

## Calor específico a volumen constante $c_v$

> [!proposicion]
> De la definición de $c_v$:
> $$c_v \equiv \left(\frac{\partial u}{\partial T}\right)_v.$$
> Para un proceso isocórico ($dv = 0$), la primera ley $du = \delta q - P\,dv$ se reduce a $du = \delta q$, y por tanto el calor intercambiado es exactamente $\Delta u = \int c_v\,dT$.
>
> *Para gas ideal:* $\Delta u = \int_{T_1}^{T_2} c_v(T)\,dT = c_v\,\Delta T$ (con $c_v$ constante en ciertos rangos).
>
> *Para sustancia incompresible:* $dv = 0$ siempre, y $c_p = c_v \equiv c$, luego $\Delta u = c\,\Delta T$.

---

## Ejemplo: cambio de energía interna en proceso no isocórico

> [!ejemplo]
> **Aire (gas ideal) comprimido de $T_1 = 300\,\text{K}$, $P_1 = 100\,\text{kPa}$ a $T_2 = 500\,\text{K}$, $P_2 = 500\,\text{kPa}$.**
> Calcular $\Delta u$.
>
> **Paso 1 — Identificar el tipo de sustancia.** Aire ≈ gas ideal; por tanto $u = u(T)$.
>
> **Paso 2 — Consecuencia clave.** $\Delta u$ depende solo de $\Delta T$, no del camino ni del cambio de $P$.
>
> **Paso 3 — Aplicar $\Delta u = c_v \Delta T$** (con $c_v = 0.718\,\text{kJ/(kg·K)}$ para aire):
> $$\Delta u = 0.718 \times (500 - 300) = 0.718 \times 200 = 143.6\,\text{kJ/kg}.$$
>
> **Paso 4 — Verificar dimensiones.** $[\text{kJ/(kg·K)}] \times [\text{K}] = [\text{kJ/kg}]$. ✓
>
> **Interpretación:** $\Delta u = 143.6\,\text{kJ/kg}$ es la energía microscópica adicional almacenada en cada kilogramo de aire — en mayor agitación traslacional y rotacional de las moléculas. Este resultado es independiente de si el proceso fue isobárico, isocórico, politrópico, etc. $\blacksquare$

---

## Relación con otras propiedades y notas

> [!info]
> - $U$ es la raíz de los otros tres potenciales: $H = U+PV$, $F = U-TS$, $G = U-TS+PV$; ver [[Potenciales Termodinamicos/index | índice de Potenciales]].
> - Primera ley para sistema cerrado: $\Delta U = Q - W$; ver [[Primera Ley SC]].
> - La presión interna $\pi_T = (\partial u/\partial v)_T$ generaliza el resultado de Joule a sustancias reales; ver [[Identidades/index | Presión interna]].
> - $c_v$ y su relación con $c_p$ se desarrollan en [[Cp Cv/index | $c_p - c_v$]].

> [!info]
> **Convención de notación:** $U$: energía interna extensiva [kJ]; $u = U/m$: específica [kJ/kg]; $\bar{u} = U/n$: molar [kJ/mol].

> [!referencia]
> Borgnakke & Sonntag, *Fundamentals of Thermodynamics*, §2.6, §12.1; Çengel & Boles, *Termodinámica*, §2-6 a 4-1; Callen, *Thermodynamics*, §1-9, §3-1; Fermi, *Thermodynamics*, cap. II.
