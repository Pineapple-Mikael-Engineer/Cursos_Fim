---
title: "Energía de Helmholtz $F$"
order: 4
tags:
  - termodinamica
  - potenciales_termodinamicos
  - helmholtz
draft: false
aliases:
  - Helmholtz free energy
  - energía libre de Helmholtz
  - F
  - trabajo máximo isotérmico
---

# Energía de Helmholtz $F$

> [!definicion]
> La **energía libre de Helmholtz** se define como:
> $$F \equiv U - TS,$$
> y es el potencial termodinámico con variables naturales $(T, V)$. Su significado físico central es: **$-\Delta F$ es el trabajo máximo que puede extraer un sistema en un proceso isotérmico reversible** (con entorno a temperatura $T$). Lo que el sistema no puede convertir en trabajo queda "atrapado" como energía interna térmica — esa fracción es $T\Delta S$. La letra $F$ viene del alemán *Freie Energie* (Helmholtz, 1882).
>
> En sistemas a temperatura y volumen controlados ($T, V = \text{cte}$), $F$ tiene un mínimo en el equilibrio: es el potencial que rige los procesos con baño térmico en recipiente rígido.

---

## Diferencial y variables naturales

> [!proposicion]
> De $F = U - TS$ y $dU = T\,dS - P\,dV$:
> $$dF = dU - T\,dS - S\,dT = (T\,dS - P\,dV) - T\,dS - S\,dT$$
> $$\boxed{dF = -S\,dT - P\,dV.}$$
> Variables naturales: $(T, V)$. Derivadas primeras:
> $$S = -\left(\frac{\partial F}{\partial T}\right)_V, \qquad P = -\left(\frac{\partial F}{\partial V}\right)_T.$$
> La primera derivada da la entropía como pendiente negativa de $F$ respecto a $T$: cuanto más baja la energía libre al calentar, más entropía tiene el sistema.

---

## Tercer relación de Maxwell (desde $F$)

> [!proposicion]
> Por igualdad de derivadas cruzadas de $dF = -S\,dT - P\,dV$:
> $$\left(\frac{\partial S}{\partial V}\right)_T = \left(\frac{\partial P}{\partial T}\right)_V.$$
> Esta es la tercera (y más usada) relación de Maxwell. Conecta la variación de entropía con el volumen con la variación de presión con la temperatura, que es medible. Su aplicación directa: para cualquier sustancia, $(\partial P/\partial T)_V = \alpha/\kappa_T$, donde $\alpha$ es el coeficiente de expansión térmica y $\kappa_T$ la compresibilidad isotérmica. Ver [[Maxwell]].

---

## $-\Delta F$ es el trabajo máximo en proceso isotérmico

> [!demostracion]
> **Meta:** probar que el trabajo máximo extraíble en un proceso a temperatura constante (con baño térmico) es $-\Delta F$.
>
> **Hipótesis:** sistema cerrado en contacto con un reservorio a temperatura $T$; el proceso puede ser reversible o irreversible pero $T$ del sistema permanece igual al reservorio.
>
> **Paso 1 — Primera ley del proceso isotérmico:**
> $$\Delta U = Q - W \implies W = Q - \Delta U.$$
>
> **Paso 2 — Acotar el calor intercambiado con el reservorio.**
> Por la segunda ley (desigualdad de Clausius): el calor que entra al sistema desde el reservorio a temperatura $T$ satisface:
> $$Q \le T\,\Delta S,$$
> con igualdad para proceso reversible (todo el cambio de entropía del sistema viene del calor reversible).
>
> **Paso 3 — Acotar el trabajo.**
> Sustituyendo la cota del paso 2 en la primera ley:
> $$W = Q - \Delta U \le T\,\Delta S - \Delta U = -\Delta(U - TS) = -\Delta F.$$
>
> **Paso 4 — El máximo se alcanza en el proceso reversible.**
> La igualdad $W_{\rm máx} = -\Delta F$ se logra cuando $Q = T\,\Delta S$, es decir, cuando el proceso es internamente reversible e isotérmico. En ese caso, el sistema puede intercambiar calor con el reservorio de forma cuasiestática sin generar entropía.
>
> **Paso 5 — Verificación para proceso en que $W = 0$.**
> Si no se realiza trabajo ($W = 0$) y el proceso ocurre a $T, V$ constantes: $\Delta F = -W + Q - Q\,(\text{rev}) = 0 - T\,\Delta S + Q$... En un sistema a $T, V$ constantes sin trabajo, la primera ley da $\Delta U = Q$ y la segunda $Q \le T\,\Delta S$, luego:
> $$\Delta F = \Delta U - T\,\Delta S = Q - T\,\Delta S \le 0.$$
> El equilibrio se alcanza cuando $\Delta F = 0$ (mínimo de $F$ a $T, V$ constantes). $\blacksquare$

![[helmholtz_trabajo_maximo.svg|420]]
*Proceso isotérmico: el sistema va del estado 1 al estado 2 a temperatura $T$ constante (baño térmico). El trabajo máximo extraíble es $W_{\rm máx} = F_1 - F_2 = -\Delta F$. La porción $T\Delta S$ del cambio de $U$ no puede convertirse en trabajo — es el calor que debe cederse al reservorio para que el proceso sea reversible.*

---

## Criterio de equilibrio a $(T, V)$ constantes

> [!proposicion]
> Para un sistema a $T$ y $V$ constantes en contacto con un baño térmico:
> $$\left.\Delta F\right|_{T,V} \le 0 \quad \text{(proceso espontáneo)}, \qquad F = \text{mínimo} \quad \text{(equilibrio)}.$$
> Cualquier fluctuación que lleve al sistema fuera del equilibrio aumenta $F$, y la fuerza de restauración lo devuelve al mínimo. Este criterio es la base del tratamiento estadístico de fluctuaciones (mecánica estadística canónica).

---

## Conexión con mecánica estadística: $F = -k_B T \ln Z$

> [!teoria]
> En mecánica estadística, la función de partición canónica $Z$ (suma sobre todos los microestados $i$ del sistema a temperatura $T$) es:
> $$Z = \sum_i e^{-E_i/(k_B T)},$$
> donde $E_i$ son las energías de los microestados. La energía libre de Helmholtz es exactamente:
> $$F = -k_B T\ln Z.$$
> De aquí se deriva **todo**: $S = -(\partial F/\partial T)_V = k_B(\ln Z + T/Z\,\partial Z/\partial T)$, $U = F + TS$, $P = -(\partial F/\partial V)_T$.
>
> Esta conexión justifica por qué $F$ es el potencial central de la mecánica estadística de equilibrio: minimizar $F$ a $T, V$ constantes equivale a maximizar la función de partición $Z$, que es la suma ponderada de todos los microestados accesibles — es decir, el estado macroscópico más probable.

---

## La relación de Gibbs-Helmholtz

> [!proposicion]
> Partiendo de $F = U - TS$ y $S = -(\partial F/\partial T)_V$:
> $$U = F + TS = F - T\left(\frac{\partial F}{\partial T}\right)_V = -T^2 \left(\frac{\partial(F/T)}{\partial T}\right)_V.$$
> Esta es la **relación de Gibbs-Helmholtz**, que permite obtener la energía interna $U$ a partir de $F(T,V)$, o calcular cómo varía $F$ con $T$ si se conoce $U$:
> $$\frac{\partial}{\partial T}\!\left(\frac{F}{T}\right)_V = -\frac{U}{T^2}.$$

---

## Ejemplo: trabajo máximo de una batería

> [!ejemplo]
> **Una batería de Li-ion a $T = 298\,\text{K}$ tiene $\Delta U = -200\,\text{kJ/mol}$ y $\Delta S = -10\,\text{J/(mol·K)}$ en la reacción de descarga.** ¿Cuánto trabajo eléctrico puede extraerse como máximo?
>
> **Paso 1 — Calcular $\Delta F$:**
> $$\Delta F = \Delta U - T\,\Delta S = -200{,}000 + 298 \times (-10) = -200{,}000 - 2{,}980 = -202{,}980\,\text{J/mol}.$$
>
> **Paso 2 — Trabajo eléctrico máximo:**
> $$W_{\rm máx} = -\Delta F = 202{,}980\,\text{J/mol} \approx 203\,\text{kJ/mol}.$$
>
> **Paso 3 — Calor cedido al entorno en proceso reversible:**
> $$Q_{\rm rev} = T\,\Delta S = 298 \times (-10) = -2{,}980\,\text{J/mol}.$$
> En el proceso reversible, la batería cede 2.98 kJ/mol al entorno (enfriamiento leve). En operación real con corriente alta, se generan pérdidas óhmicas que $\Delta F$ no incluye y se disipa más calor.
>
> **Paso 4 — Comparar con la energía interna:**
> $-\Delta U = 200\,\text{kJ/mol}$, pero $W_{\rm máx} = 203\,\text{kJ/mol}$: el sistema extrae más trabajo que su disminución de energía interna porque también "toma prestada" entropía del entorno. $\blacksquare$

---

## Relación con otras notas

> [!info]
> - La relación de Maxwell $(\partial S/\partial V)_T = (\partial P/\partial T)_V$ de $F$ produce la presión interna $\pi_T$; ver [[Maxwell]] y [[Identidades/index | Presión interna]].
> - $G = F + PV$: Gibbs añade el trabajo de frontera a Helmholtz; ver [[Gibbs]].
> - La exergía de flujo cerrado generaliza $-\Delta F$ al caso con ambiente; ver [[Exergia]].
> - La función de partición $Z$ y la termodinámica estadística se desarrollan en [[Mecánica Estadística]].

> [!info]
> **Convención:** $F$: extensiva [kJ]; $f = F/m$ [kJ/kg]. También escrita como $A$ (IUPAC) en textos europeos.

> [!referencia]
> Borgnakke & Sonntag, *Fundamentals of Thermodynamics*, §12.2; Callen, *Thermodynamics*, §5-3; Çengel & Boles, *Termodinámica*, §12-1; Landau & Lifshitz, *Statistical Physics* §15; Helmholtz, "Über die Thermodynamik chemischer Vorgänge" (1882).
