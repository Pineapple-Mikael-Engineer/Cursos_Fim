---
title: "Gas ideal"
order: 1
tags:
  - termodinamica
  - propiedades
  - ecuaciones_de_estado
  - gas_ideal
draft: false
aliases:
  - ideal gas
  - gas perfecto
  - ley de los gases ideales
---

# Gas ideal $Pv = RT$

> [!definicion]
> El **gas ideal** es un modelo donde las moléculas son puntos materiales sin volumen propio y sin fuerzas de interacción entre sí. Bajo estas hipótesis, la única energía cinética disponible es la translacional/rotacional de cada molécula, y la presión surge puramente del choque mecánico con las paredes. La ecuación de estado resultante relaciona presión, volumen específico y temperatura:
> $$
> Pv = RT \qquad \Longleftrightarrow \qquad PV = mRT \qquad \Longleftrightarrow \qquad P\bar{v} = R_u T
> $$
> donde $R = R_u/M$ es la constante particular del gas [kJ/kg·K], $R_u = 8.314\,\mathrm{kJ/(kmol\cdot K)}$ y $\bar{v} = V/n$ el volumen molar. El modelo es preciso a baja presión y alta temperatura (lejos de la curva de saturación y del punto crítico), donde el volumen entre moléculas $\gg$ volumen de las moléculas y las fuerzas de Van der Waals son despreciables.

![[gas_ideal_moleculas_vs_real.svg|440]]
*Comparación esquemática: gas ideal (moléculas puntales, sin interacción) vs. gas real (moléculas con volumen y atracción). A la derecha, el factor $Z = Pv/RT$ para ambos: el ideal tiene $Z=1$ exacto; el real desvía según dominen atracción ($Z<1$) o covolumen ($Z>1$).*

---

## Consecuencia fundamental: $u = u(T)$, $h = h(T)$

> [!teorema]
> Para un gas ideal, la **energía interna** y la **entalpía** dependen **únicamente de la temperatura** (ley de Joule):
> $$
> u = u(T), \qquad h = u + Pv = u(T) + RT = h(T).
> $$
> En consecuencia, los calores específicos también son solo función de $T$:
> $$
> du = c_v(T)\,dT, \qquad dh = c_p(T)\,dT.
> $$

> [!demostracion]
> **Hipótesis:** gas ideal ($Pv = RT$).
>
> **Paso 1 — Expresión general para $(\partial u/\partial v)_T$.** De la primera ecuación $TdS$ y la relación de Maxwell correspondiente (ver [[TdS | $TdS$]]):
> $$
> \left(\frac{\partial u}{\partial v}\right)_T = T\left(\frac{\partial P}{\partial T}\right)_v - P.
> $$
> Esta es la **presión interna** del fluido: mide cuánto cambia la energía al expandir isotérmicamente.
>
> **Paso 2 — Evaluar la derivada parcial para gas ideal.** De $P = RT/v$:
> $$
> \left(\frac{\partial P}{\partial T}\right)_v = \frac{R}{v}.
> $$
>
> **Paso 3 — Sustituir.** Entonces:
> $$
> \left(\frac{\partial u}{\partial v}\right)_T = T\cdot\frac{R}{v} - P = \frac{RT}{v} - P = P - P = 0.
> $$
>
> **Paso 4 — Conclusión para $u$.** Como $u$ no depende de $v$ (a $T$ fija), depende solo de $T$: $u = u(T)$.
>
> **Paso 5 — Consecuencia para $h$.** Por definición $h = u + Pv = u(T) + RT$. Como $u$ y $RT$ dependen solo de $T$, también $h = h(T)$. $\blacksquare$
>
> *Interpretación física:* en un gas ideal no hay energía potencial intermolecular. Al expandir, las moléculas no hacen trabajo contra las atracciones — toda la energía interna es cinética y depende solo de $T$.

---

## Relación de Mayer: $c_p - c_v = R$

> [!proposicion]
> Para un gas ideal, la diferencia entre calores específicos es exactamente igual a la constante del gas:
> $$
> c_p - c_v = R.
> $$

> [!demostracion]
> **Hipótesis:** gas ideal, por lo que $u = u(T)$ y $h = h(T)$.
>
> **Paso 1 — Definiciones.** Por definición:
> $$
> c_v = \left(\frac{\partial u}{\partial T}\right)_v = \frac{du}{dT}, \qquad c_p = \left(\frac{\partial h}{\partial T}\right)_P = \frac{dh}{dT}.
> $$
> (Los parciales son totales porque $u$ y $h$ dependen solo de $T$.)
>
> **Paso 2 — Relación entre $h$ y $u$.** Diferenciando $h = u + Pv = u + RT$:
> $$
> dh = du + R\,dT.
> $$
>
> **Paso 3 — Dividir por $dT$.** Dividiendo ambos lados por $dT$:
> $$
> \frac{dh}{dT} = \frac{du}{dT} + R \implies c_p = c_v + R \implies \boxed{c_p - c_v = R.} \qquad \blacksquare
> $$
>
> *Interpretación física:* el término $R$ en $c_p - c_v$ representa el **trabajo de expansión** que hace el fluido al calentarse a presión constante. En un calentamiento isocórico, toda la energía va a aumentar $u$ (cinética). En un isobárico, parte de la energía también hace trabajo $P\,dv = R\,dT$, por lo que se necesita más calor para el mismo incremento de temperatura.

---

## Cambios de propiedades (calóricamente perfecto: $c_v$, $c_p$ constantes)

> [!proposicion]
> Cuando $c_v$ y $c_p$ se tratan como constantes (gas calóricamente perfecto, válido en rangos moderados de temperatura):
> $$
> \Delta u = c_v (T_2 - T_1), \qquad \Delta h = c_p (T_2 - T_1).
> $$
> El cambio de [[Entropia | entropía]] se obtiene de las ecuaciones $TdS$:
> $$
> \Delta s = c_v \ln\frac{T_2}{T_1} + R \ln\frac{v_2}{v_1} = c_p \ln\frac{T_2}{T_1} - R \ln\frac{P_2}{P_1}.
> $$

> [!info]
> A temperatura alta o variable, se integra $c_p(T)$ tabulado. Las tablas de aire (Apéndice A, Çengel) dan $h(T)$ y $s^\circ(T) = \int c_p/T\,dT$, con la corrección de presión: $\Delta s = s^\circ(T_2) - s^\circ(T_1) - R\ln(P_2/P_1)$.

---

## Procesos isentrópicos ($\Delta s = 0$, $c_v$, $c_p$ constantes)

> [!proposicion]
> Imponiendo $\Delta s = 0$ con calores específicos constantes y definiendo $\gamma = c_p/c_v$:
> $$
> Tv^{\gamma-1} = \text{cte}, \qquad T P^{(1-\gamma)/\gamma} = \text{cte}, \qquad Pv^{\gamma} = \text{cte}.
> $$

> [!demostracion]
> **Hipótesis:** gas ideal calóricamente perfecto, proceso isentrópico ($ds=0$).
>
> **Paso 1.** De $ds = c_v\,dT/T + R\,dv/v = 0$: dividir por $c_v$:
> $$
> \frac{dT}{T} = -\frac{R}{c_v}\,\frac{dv}{v} = -(\gamma-1)\,\frac{dv}{v}.
> $$
>
> **Paso 2.** Integrar: $\ln T_2/T_1 = -(\gamma-1)\ln v_2/v_1 = \ln(v_1/v_2)^{\gamma-1}$. Por lo tanto:
> $$
> T_2/T_1 = (v_1/v_2)^{\gamma-1} \implies Tv^{\gamma-1} = \text{cte.}
> $$
>
> **Paso 3.** Usando $Pv = RT$, eliminar $T$: $P_1 v_1^\gamma/(R) = P_2 v_2^\gamma/(R)$:
> $$
> Pv^\gamma = \text{cte.} \qquad \blacksquare
> $$
>
> La tercera relación $TP^{(1-\gamma)/\gamma}=\text{cte}$ se obtiene combinando las dos anteriores o eliminando $v$.

---

## Ejemplo: compresor adiabático de aire (gas ideal)

> [!ejemplo]
> Un compresor adiabático eleva la presión del aire de $P_1 = 100\,\mathrm{kPa}$, $T_1 = 300\,\mathrm{K}$ a $P_2 = 800\,\mathrm{kPa}$. La eficiencia isentrópica es $\eta_C = 0.85$. Calcular: (a) $T_{2s}$ y $w_s$ isentrópico; (b) $T_2$ real y $w_{\rm real}$; (c) $s_{\rm gen}$ por kg.
>
> Datos: aire, $c_p = 1.005\,\mathrm{kJ/(kg\cdot K)}$, $\gamma = 1.4$, $R = 0.287\,\mathrm{kJ/(kg\cdot K)}$.

> [!solucion]
> **(a) Proceso isentrópico (ideal).**
>
> $T_{2s} = T_1(P_2/P_1)^{(\gamma-1)/\gamma} = 300\times(8)^{0.2857} = 300\times1.8114 = 543.4\,\mathrm{K}.$
>
> Trabajo específico isentrópico (primera ley, adiabático): $w_s = -\Delta h_s = -c_p(T_{2s}-T_1) = -1.005\times(543.4-300) = -244.6\,\mathrm{kJ/kg}.$
>
> (El trabajo es negativo: el compresor recibe trabajo del entorno.)
>
> **(b) Proceso real.**
>
> La eficiencia isentrópica del compresor es $\eta_C = w_s / w_{\rm real}$ (relación entre trabajo ideal y real; como ambos son negativos, $|w_{\rm real}|>|w_s|$): $w_{\rm real} = w_s/\eta_C = -244.6/0.85 = -287.8\,\mathrm{kJ/kg}.$
>
> $T_2 = T_1 - w_{\rm real}/c_p = 300 + 287.8/1.005 = 300 + 286.4 = 586.4\,\mathrm{K}.$
>
> **(c) Generación de entropía.**
>
> El proceso es adiabático ($\dot{Q}=0$) pero irreversible. Por la segunda ley: $s_{\rm gen} = \Delta s = c_p\ln(T_2/T_{2s}) - R\ln(P_2/P_2) = c_p\ln(T_2/T_{2s}).$
>
> Aquí $P_2$ es el mismo en el proceso real e ideal (misma presión de salida), así que el término $R\ln(P_2/P_2)=0$: $s_{\rm gen} = 1.005\times\ln(586.4/543.4) = 1.005\times\ln(1.0792) = 1.005\times0.07621 = 0.0766\,\mathrm{kJ/(kg\cdot K)} > 0.$ ✓

---

## Dominio de validez

> [!warning]
> El modelo falla cerca del **punto crítico** y en la **región bifásica** (donde hay interacciones fuertes y cambio de fase). Las condiciones de validez práctica son:
> - $P_r = P/P_c \ll 1$ o $T_r = T/T_c \gg 1$ (por encima de 2.0 es seguro a casi cualquier $P$).
> - El factor de compresibilidad $Z = Pv/(RT) \approx 1$ (desvío menor al 5%).
>
> Para el **aire** a condiciones atmosféricas, $T_r \approx 6$: el modelo es excelente. Para el **vapor de agua** en una caldera a 10 MPa, $T_r \approx 1.4$: se requieren tablas.

> [!info]
> **Convención de notación usada en este curso:** $R$ constante particular [kJ/kg·K]; $R_u = 8.314\,\mathrm{kJ/(kmol\cdot K)}$ universal; $\gamma = c_p/c_v$; $Z = Pv/RT$; barra sobre variable ($\bar{v}$, $\bar{u}$, $\bar{h}$, $\bar{s}$): magnitudes molares [kmol].

> [!referencia]
> Borgnakke & Sonntag, *Fundamentals of Thermodynamics*, §3.6–3.7, §8.5; Çengel & Boles, *Termodinámica*, cap. 3 y apéndice A; Callen, *Thermodynamics*, §3.4 (demostración rigurosa de $u=u(T)$ desde postulados).
