---
title: "Efecto Joule-Thomson"
order: 2
tags:
  - termodinamica
  - relaciones_termodinamicas
  - calores_especificos
  - joule_thomson
draft: false
aliases:
  - coeficiente de Joule-Thomson
  - efecto JT
  - expansión isentálpica
---

# Efecto Joule-Thomson

> [!definicion]
> El **coeficiente de Joule-Thomson** caracteriza el cambio de temperatura de un fluido al atravesar una estricción adiabática (válvula, tapón poroso) sin trabajo de eje. El proceso es a **entalpía constante** ($h = \text{cte}$) y el coeficiente mide la pendiente de las curvas $h = \text{cte}$ en el plano $T$-$P$:
> $$\mu_{JT} \equiv \left(\frac{\partial T}{\partial P}\right)_h \quad [\mathrm{K/Pa}] \quad\text{o}\quad [\mathrm{K/bar}].$$
> Un fluido con $\mu_{JT} > 0$ se enfría al bajar la presión (efecto refrigerante); con $\mu_{JT} < 0$ se calienta. Para el gas ideal, $\mu_{JT} = 0$ exactamente.

---

## Derivación de $\mu_{JT}$

### Paso intermedio: $(\partial h/\partial P)_T$

> [!demostracion]
> **Paso 1 — Diferencial de $h$ en variables $(T,P)$.** $h = h(T,P)$:
> $$dh = \left(\frac{\partial h}{\partial T}\right)_P\!dT + \left(\frac{\partial h}{\partial P}\right)_T\!dP = c_p\,dT + \left(\frac{\partial h}{\partial P}\right)_T\!dP.$$
>
> **Paso 2 — Calcular $(\partial h/\partial P)_T$.** De $dh = T\,ds + v\,dP$ (diferencial de $h$):
> $$\left(\frac{\partial h}{\partial P}\right)_T = T\left(\frac{\partial s}{\partial P}\right)_T + v.$$
>
> **Paso 3 — Sustituir la 4.ª relación de [[Maxwell]]** (desde $g$):
> $$\left(\frac{\partial s}{\partial P}\right)_T = -\left(\frac{\partial v}{\partial T}\right)_P = -v\,\alpha.$$
>
> **Paso 4 — Resultado:**
> $$\left(\frac{\partial h}{\partial P}\right)_T = T\cdot(-v\,\alpha) + v = v(1 - T\,\alpha). \qquad \blacksquare$$

### Coeficiente $\mu_{JT}$

> [!demostracion]
> Aplicando la [[Identidades/index | regla cíclica]] a la función $h(T,P)$:
> $$\left(\frac{\partial T}{\partial P}\right)_h = -\frac{(\partial h/\partial P)_T}{(\partial h/\partial T)_P} = -\frac{v(1-T\alpha)}{c_p}.$$
>
> $$\boxed{\mu_{JT} = \frac{v(T\alpha - 1)}{c_p}.} \qquad \blacksquare$$
>
> El signo de $\mu_{JT}$ depende de si $T\alpha \gtrless 1$: enfriamiento cuando $T\alpha > 1$, calentamiento cuando $T\alpha < 1$.

---

## Gas ideal: $\mu_{JT} = 0$

> [!proposicion]
> Para gas ideal ($Pv = RT$): $\alpha = (1/v)(\partial v/\partial T)_P = 1/T$, luego $T\alpha = 1$ y:
> $$\mu_{JT}^{\rm ideal} = \frac{v(T\cdot\frac{1}{T} - 1)}{c_p} = \frac{v\cdot 0}{c_p} = 0.$$
> Al expandir a través de una estricción, la temperatura de un gas ideal no cambia. El efecto Joule-Thomson es una consecuencia de las interacciones intermoleculares (desviación del comportamiento ideal). $\blacksquare$

---

## Curva de inversión

> [!teoria]
> La **curva de inversión** ($\mu_{JT} = 0$) divide el plano $T$-$P$ en la región de enfriamiento ($\mu_{JT} > 0$) y la de calentamiento ($\mu_{JT} < 0$). La condición de inversión es:
> $$T\alpha = 1 \;\Longrightarrow\; T\left(\frac{\partial v}{\partial T}\right)_P = v.$$
>
> ![[joule_thomson_curva_inversion.svg|460]]
> *Curva de inversión en el plano $T$-$P$. La refrigeración por Joule-Thomson solo es posible dentro de la curva (región sombreada). La temperatura de inversión a baja presión es el valor máximo de $T$ en la curva.*
>
> La temperatura de inversión a baja presión ($P \to 0$) se denomina **temperatura de inversión superior** $T_{\rm inv}^+$. Para enfriar un gas con este efecto se necesita que la temperatura inicial sea menor que $T_{\rm inv}^+$.

> [!teoria] Temperatura de inversión del gas de van der Waals
> Para el gas de vdW $(P + a/v^2)(v-b) = RT$. La condición $T(\partial v/\partial T)_P = v$ se resuelve analíticamente en el límite $P \to 0$ (expansión virial):
> $$T_{\rm inv}^+ \approx \frac{2a}{Rb}.$$
>
> | Gas | $T_{\rm inv}^+$ (vdW, K) | $T_{\rm inv}^+$ (exp., K) |
> |:---:|:---:|:---:|
> | $\mathrm{H_2}$ | $\approx 224$ | $202$ |
> | $\mathrm{He}$ | $\approx 35$ | $40$ |
> | $\mathrm{N_2}$ | $\approx 851$ | $621$ |
> | $\mathrm{CO_2}$ | $\approx 2000$ | $1500$ |
>
> La ecuación de vdW sobreestima $T_{\rm inv}^+$; las magnitudes son del orden correcto.

---

## Ejemplo: nitrógeno a 200 K y 10 MPa

> [!ejemplo]
> $\mathrm{N_2}$ a $T_1 = 200\,\mathrm{K}$, $P_1 = 10\,\mathrm{MPa}$ se expande hasta $P_2 = 0.1\,\mathrm{MPa}$ a través de una válvula adiabática. ¿Se calienta o se enfría?
>
> **Paso 1 — Verificar que $T_1 < T_{\rm inv}^+$.** Para $\mathrm{N_2}$, $T_{\rm inv}^+ \approx 621\,\mathrm{K}$ (experimental). Como $200\,\mathrm{K} < 621\,\mathrm{K}$, el nitrógeno está dentro de la curva de inversión a estas condiciones: $\mu_{JT} > 0$ y el gas **se enfría** al expandirse.
>
> **Paso 2 — Estimar $\mu_{JT}$ a esas condiciones.** De tablas criogénicas para $\mathrm{N_2}$ a $200\,\mathrm{K}$ y $10\,\mathrm{MPa}$: $v \approx 6.0\times10^{-3}\,\mathrm{m^3/kg}$, $\alpha \approx 5.5\times10^{-3}\,\mathrm{K^{-1}}$, $c_p \approx 1.12\,\mathrm{kJ/(kg\cdot K)}$.
> $$\mu_{JT} = \frac{v(T\alpha-1)}{c_p} = \frac{6.0\times10^{-3}(200\times5.5\times10^{-3}-1)}{1120} = \frac{6.0\times10^{-3}\times0.10}{1120} = 5.4\times10^{-7}\,\mathrm{K/Pa}.$$
>
> **Paso 3 — Estimación lineal de $\Delta T$:**
> $$\Delta T \approx \mu_{JT}\cdot\Delta P = 5.4\times10^{-7}\times(0.1\times10^6 - 10\times10^6) = 5.4\times10^{-7}\times(-9.9\times10^6)\approx -5.3\,\mathrm{K}.$$
>
> La estimación lineal indica $T_2 \approx 194.7\,\mathrm{K}$; el valor real (de tablas de $h = h_1$) es algo diferente porque $\mu_{JT}$ varía con $P$. La dirección es correcta: enfriamiento. $\blacksquare$

---

## Aplicación: licuefacción de gases

> [!proposicion]
> El proceso de **Linde-Hampson** utiliza el efecto Joule-Thomson para licuar gases:
> 1. Comprimir el gas isotérmicamente (eliminando el calor de compresión).
> 2. Precolar el gas comprimido en un intercambiador de calor recuperativo con gas frío que retorna.
> 3. Expandir el gas preenfriado a través de una válvula Joule-Thomson: la caída de temperatura produce licuefacción parcial.
> 4. El gas sin licuar regresa al intercambiador y preenfría el siguiente ciclo (efecto regenerativo).
>
> Para $\mathrm{H_2}$ y $\mathrm{He}$, cuya $T_{\rm inv}^+ < 300\,\mathrm{K}$, el gas debe preenfriarse por debajo de $T_{\rm inv}^+$ antes de la expansión JT (con nitrógeno líquido para $\mathrm{H_2}$ y con hidrógeno líquido para $\mathrm{He}$).

---

## Relación con otras notas

> [!info]
> - $\mu_{JT}$ se deriva usando la 4.ª relación de [[Maxwell]] y la [[Identidades/index | regla cíclica]].
> - Depende de $\alpha$, $v$ y $c_p$, todos conectados por la relación [[Cp Cv/index | $c_p - c_v$]].
> - La válvula Joule-Thomson es el dispositivo de expansión del ciclo de refrigeración por compresión de vapor (ver [[Compresión de Vapor | Ciclo de refrigeración]]).

> [!referencia]
> Çengel & Boles, *Termodinámica*, §12-5; Moran & Shapiro, §11.4; Callen, *Thermodynamics*, §8-3; Smith, Van Ness & Abbott, *Introduction to Chemical Engineering Thermodynamics*, §7.4.
