---
title: "Presión interna y energía configuracional"
order: 2
tags:
  - termodinamica
  - relaciones_termodinamicas
  - identidades
  - presion_interna
draft: false
aliases:
  - presión interna termodinámica
  - energía de cohesión
  - energía de Frenkel
---

# Presión interna y energía configuracional

> [!definicion]
> La **presión interna** $\pi_T \equiv (\partial u/\partial v)_T$ cuantifica el cambio de energía interna al variar el volumen a temperatura constante. A diferencia de la presión mecánica $P$, que actúa hacia afuera, $\pi_T$ refleja la resistencia de las fuerzas intermoleculares a la expansión: es cero para el gas ideal y positiva cuando dominan las atracciones. La relación exacta:
> $$\pi_T = T\left(\frac{\partial P}{\partial T}\right)_v - P = \frac{T\alpha}{\kappa_T} - P$$
> permite calcularla con la [[Ecuaciones de Estado/index | ecuación de estado]] o con los coeficientes medibles $\alpha$ y $\kappa_T$.

---

## Demostración

> [!demostracion]
> **Paso 1 — Diferencial de $u$ a $T$ constante.** De $du = T\,ds - P\,dv$, dividiendo por $dv$ a $T$ fija:
> $$\left(\frac{\partial u}{\partial v}\right)_T = T\left(\frac{\partial s}{\partial v}\right)_T - P.$$
>
> **Paso 2 — Sustituir** $(\partial s/\partial v)_T$ con la 3.ª relación de [[Maxwell]] (desde Helmholtz):
> $$\left(\frac{\partial s}{\partial v}\right)_T = \left(\frac{\partial P}{\partial T}\right)_v = \frac{\alpha}{\kappa_T}.$$
>
> **Paso 3 — Resultado:**
> $$\pi_T = T\cdot\frac{\alpha}{\kappa_T} - P. \qquad \blacksquare$$

---

## Gas ideal: $\pi_T = 0$

> [!proposicion]
> Para $Pv = RT$: $(\partial P/\partial T)_v = P/T$, luego $\pi_T = T(P/T) - P = 0$.
>
> Este resultado fue verificado experimentalmente por Joule (1843) —sin ecuación de estado— y es el fundamento del teorema de Joule: *la energía interna de un gas ideal depende solo de la temperatura*. $\blacksquare$

---

## Gas de van der Waals: $\pi_T = a/v^2$

> [!demostracion]
> De $P = RT/(v-b) - a/v^2$: $(\partial P/\partial T)_v = R/(v-b)$. Luego:
> $$\pi_T = T\cdot\frac{R}{v-b} - \left(\frac{RT}{v-b} - \frac{a}{v^2}\right) = \frac{a}{v^2}. \qquad \blacksquare$$
>
> El parámetro $a$ es la única fuente de $\pi_T \ne 0$: cuanto mayor es la atracción intermolecular, mayor es la energía necesaria para separar las moléculas al expandir.

---

## Energía configuracional

> [!teoria]
> Integrando $\pi_T$ a temperatura constante desde el estado de gas ideal ($v = \infty$, donde $u = u^{\rm ideal}(T)$) hasta $v$ finito:
> $$u(T,v) = u^{\rm ideal}(T) + \int_\infty^v \pi_T(T,v')\,dv'.$$
>
> La integral es la **energía configuracional** o energía de cohesión: la contribución de las interacciones intermoleculares a $u$.
>
> Para el gas de van der Waals:
> $$u^{\rm vdW}(T,v) = u^{\rm ideal}(T) - \frac{a}{v}.$$
>
> ![[energia_configuracional_vdW.svg|420]]
> *Energía configuracional $-a/v$ del gas de van der Waals como función del volumen molar. La energía disminuye al comprimir (las moléculas se acercan y la atracción crece) hasta que el volumen excluido $b$ hace la repulsión dominante.*

---

## Verificación experimental: criterio de van der Waals

> [!proposicion]
> El experimento de Joule-Thomson (expansión a $h = \text{cte}$) mide indirectamente $\pi_T$. De $dh = T\,ds + v\,dP$ y la 4.ª relación de [[Maxwell]]:
> $$\left(\frac{\partial h}{\partial P}\right)_T = v - T\!\left(\frac{\partial v}{\partial T}\right)_P = v(1-T\alpha).$$
> Para el gas de van der Waals a bajas presiones ($v \gg b$): $v(1-T\alpha) \approx b - 2a/(RT)$, que es negativo (enfriamiento) cuando $T < 2a/(Rb) = T_{\rm inv}^+$. Esta condición conecta la presión interna con el efecto Joule-Thomson (ver [[Efecto Joule Thomson]]).

---

## Ejemplo: diferencia $u(v,T) - u^{\rm ideal}(T)$ para agua líquida

> [!ejemplo]
> Agua líquida a $T = 300\,\mathrm{K}$. Estimar la energía configuracional por diferencia entre $u$ real y el límite de vapor ideal usando la fórmula con $\alpha$ y $\kappa_T$.
>
> **Datos tabulados:** $v = 0.001004\,\mathrm{m^3/kg}$, $\alpha = 2.76\times10^{-4}\,\mathrm{K^{-1}}$, $\kappa_T = 4.5\times10^{-10}\,\mathrm{Pa^{-1}}$, $P = 0.1\,\mathrm{MPa}$.
>
> **Paso 1 — Calcular $\pi_T$:**
> $$\pi_T = \frac{T\alpha}{\kappa_T} - P = \frac{300\times2.76\times10^{-4}}{4.5\times10^{-10}} - 10^5 = \frac{8.28\times10^{-2}}{4.5\times10^{-10}} - 10^5.$$
> $$= 1.84\times10^{8}\,\mathrm{Pa} - 10^5\,\mathrm{Pa} \approx 184\,\mathrm{MPa}.$$
>
> **Paso 2 — Interpretar.** La presión interna del agua líquida es $\approx184\,\mathrm{MPa}$, enormemente mayor que la presión mecánica $P = 0.1\,\mathrm{MPa}$: la cohesión de las moléculas de agua (puentes de hidrógeno) genera una presión interna de $\approx1800\,\mathrm{atm}$. Este es el origen de la altísima energía de vaporización del agua. $\blacksquare$

---

## Relación con otras notas

> [!info]
> - La demostración usa la 3.ª relación de [[Maxwell]] y la [[index | regla cíclica]].
> - La energía configuracional del gas de vdW es $-a/v$; determina la corrección a $u$ respecto al gas ideal.
> - $\pi_T$ se conecta con el [[Efecto Joule Thomson]] y con la presión de vapor de las sustancias.

> [!referencia]
> Atkins, *Physical Chemistry*, §2B; Smith, Van Ness & Abbott, §6.2; Callen, *Thermodynamics*, §8-2.
