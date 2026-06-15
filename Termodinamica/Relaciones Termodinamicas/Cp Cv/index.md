---
title: "Relación $c_p - c_v$"
tags:
  - termodinamica
  - relaciones_termodinamicas
  - calores_especificos
  - index
draft: false
aliases:
  - cp menos cv
  - relación de Mayer
  - diferencia de calores específicos
---

# Relación $c_p - c_v$

> [!definicion]
> Los calores específicos $c_v$ y $c_p$ miden la respuesta térmica de $u$ y $h$:
> $$c_v \equiv \left(\frac{\partial u}{\partial T}\right)_v = T\left(\frac{\partial s}{\partial T}\right)_v, \qquad c_p \equiv \left(\frac{\partial h}{\partial T}\right)_P = T\left(\frac{\partial s}{\partial T}\right)_P.$$
> Su diferencia se expresa enteramente en términos de la [[Ecuaciones de Estado/index | ecuación de estado]] $P$-$v$-$T$, sin hipótesis de gas ideal. El resultado es $c_p - c_v = Tv\alpha^2/\kappa_T \ge 0$, siempre no negativo para toda sustancia estable.

---

## Derivación completa: igualando las dos ecuaciones $T\,ds$

> [!demostracion]
> **Paso 1 — Escribir las dos ecuaciones [[TdS | $T\,ds$]]:**
> $$T\,ds = c_v\,dT + T\!\left(\frac{\partial P}{\partial T}\right)_v\!dv, \tag{1}$$
> $$T\,ds = c_p\,dT - T\!\left(\frac{\partial v}{\partial T}\right)_P\!dP. \tag{2}$$
>
> **Paso 2 — Expresar $dv$ en función de $(T,P)$.** La ecuación de estado fija $v = v(T,P)$:
> $$dv = \left(\frac{\partial v}{\partial T}\right)_P\!dT + \left(\frac{\partial v}{\partial P}\right)_T\!dP.$$
>
> **Paso 3 — Sustituir $dv$ en la ecuación (1):**
> $$T\,ds = c_v\,dT + T\!\left(\frac{\partial P}{\partial T}\right)_v\!\left[\left(\frac{\partial v}{\partial T}\right)_P\!dT + \left(\frac{\partial v}{\partial P}\right)_T\!dP\right].$$
> Reagrupando por $dT$ y $dP$:
> $$T\,ds = \left[c_v + T\!\left(\frac{\partial P}{\partial T}\right)_v\!\left(\frac{\partial v}{\partial T}\right)_P\right]dT + T\!\left(\frac{\partial P}{\partial T}\right)_v\!\left(\frac{\partial v}{\partial P}\right)_T\!dP. \tag{1'}$$
>
> **Paso 4 — Igualar con la ecuación (2).** Como $T$, $P$ son las variables independientes, los coeficientes de $dT$ y $dP$ deben ser iguales en (1') y (2):
>
> *Coeficiente de $dT$:*
> $$c_v + T\!\left(\frac{\partial P}{\partial T}\right)_v\!\left(\frac{\partial v}{\partial T}\right)_P = c_p$$
> $$\Longrightarrow\; c_p - c_v = T\!\left(\frac{\partial P}{\partial T}\right)_v\!\left(\frac{\partial v}{\partial T}\right)_P. \tag{3}$$
>
> *Coeficiente de $dP$:*
> $$T\!\left(\frac{\partial P}{\partial T}\right)_v\!\left(\frac{\partial v}{\partial P}\right)_T = -T\!\left(\frac{\partial v}{\partial T}\right)_P \;\Longrightarrow\; \left(\frac{\partial P}{\partial T}\right)_v\!\left(\frac{\partial v}{\partial P}\right)_T = -\left(\frac{\partial v}{\partial T}\right)_P,$$
> que es exactamente la [[Identidades/index | regla cíclica]] $(\partial P/\partial T)_v(\partial T/\partial v)_P(\partial v/\partial P)_T = -1$: el resultado es consistente. $\checkmark$
>
> **Paso 5 — Reescribir en términos de coeficientes medibles.** Aplicando la [[Identidades/index | regla cíclica]] a la ecuación (3):
> $$\left(\frac{\partial P}{\partial T}\right)_v = -\frac{(\partial v/\partial T)_P}{(\partial v/\partial P)_T} = \frac{v\alpha}{v\kappa_T} = \frac{\alpha}{\kappa_T},$$
> con $\alpha = (1/v)(\partial v/\partial T)_P$ y $\kappa_T = -(1/v)(\partial v/\partial P)_T$. Sustituyendo:
> $$c_p - c_v = T\cdot\frac{\alpha}{\kappa_T}\cdot v\,\alpha = \frac{Tv\,\alpha^2}{\kappa_T}. \qquad \blacksquare$$

---

## Signo: $c_p \ge c_v$

> [!proposicion]
> La estabilidad mecánica de toda sustancia en equilibrio exige $(\partial v/\partial P)_T < 0$, es decir, $\kappa_T > 0$. Como $\alpha^2 \ge 0$ y $v > 0$:
> $$c_p - c_v = \frac{Tv\,\alpha^2}{\kappa_T} \ge 0 \;\Longrightarrow\; c_p \ge c_v.$$
> La igualdad $c_p = c_v$ se alcanza cuando $\alpha = (\partial v/\partial T)_P/v = 0$, es decir, cuando la densidad alcanza su máximo con $T$. Para el agua líquida esto ocurre a $4\,°\mathrm{C}$ (anomalía del agua).

---

## Casos particulares

> [!proposicion] Gas ideal — relación de Mayer
> Con $Pv = RT$: $(\partial P/\partial T)_v = R/v$ y $(\partial v/\partial T)_P = R/P$:
> $$c_p - c_v = T\cdot\frac{R}{v}\cdot\frac{R}{P} = \frac{R^2 T}{Pv} = R.$$
> La diferencia es exactamente la constante del gas específica $R = R_u/M$ (relación de Mayer, 1842). $\blacksquare$

> [!proposicion] Gas de van der Waals
> Con $(P + a/\bar{v}^2)(\bar{v}-b) = R_u T$ (forma molar): las derivadas dan
> $$\left(\frac{\partial P}{\partial T}\right)_{\bar{v}} = \frac{R_u}{\bar{v}-b}, \qquad \left(\frac{\partial \bar{v}}{\partial T}\right)_P = \frac{R_u}{\;(\partial P/\partial \bar{v})_T\cdot(-1)\cdot T/\bar{v}\;}\cdots$$
> El resultado completo (vía la regla cíclica molar) es:
> $$\bar{c}_p - \bar{c}_v = \frac{R_u}{\,1 - \dfrac{2a(\bar{v}-b)^2}{R_u T\,\bar{v}^3}\,}.$$
> Cuando $a, b \to 0$: $\bar{c}_p - \bar{c}_v \to R_u$ (límite ideal). La corrección por $a$ y $b$ puede ser significativa cerca del punto crítico, donde la compresibilidad $\kappa_T \to \infty$ y $c_p - c_v \to \infty$. $\blacksquare$

> [!proposicion] Sustancia incompresible
> $v = \text{cte}$, luego $(\partial v/\partial T)_P = 0$ → $\alpha = 0$:
> $$c_p - c_v = \frac{Tv\cdot 0^2}{\kappa_T} = 0 \;\Longrightarrow\; c_p = c_v = c.$$
> Un único calor específico. Usado para líquidos y sólidos en rangos moderados de presión. $\blacksquare$

---

## Ejemplo numérico: agua líquida a 100 °C

> [!ejemplo]
> Agua líquida a $T = 373.15\,\mathrm{K}$, $P = 101.325\,\mathrm{kPa}$. Verificar cuantitativamente que $c_p - c_v \ll c_p$.
>
> **Datos tabulados** (Çengel, Apéndice):
> $v = 0.001044\,\mathrm{m^3/kg}$; $\alpha = 7.52\times10^{-4}\,\mathrm{K^{-1}}$; $\kappa_T = 4.90\times10^{-10}\,\mathrm{Pa^{-1}}$; $c_p = 4.216\,\mathrm{kJ/(kg\cdot K)}$.
>
> **Cálculo:**
> $$c_p - c_v = \frac{Tv\,\alpha^2}{\kappa_T} = \frac{373.15\times0.001044\times(7.52\times10^{-4})^2}{4.90\times10^{-10}}$$
> $$= \frac{373.15\times0.001044\times5.655\times10^{-7}}{4.90\times10^{-10}} = \frac{2.20\times10^{-7}}{4.90\times10^{-10}} = 0.449\,\mathrm{kJ/(kg\cdot K)}.$$
>
> **Resultado:**
> $c_v = 4.216 - 0.449 = 3.767\,\mathrm{kJ/(kg\cdot K)}$.
> La diferencia es $c_p - c_v = 0.449\,\mathrm{kJ/(kg\cdot K)} \approx 10.6\%$ de $c_p$: no despreciable para el agua líquida a alta temperatura. Para agua a $20\,°\mathrm{C}$, la diferencia baja a $\approx 1\%$. $\blacksquare$

---

## Relación con otras notas de esta sección

> [!info]
> | Nota | Conexión |
> |:---|:---|
> | [[Razon de Calores \| Razón $\gamma = c_p/c_v$]] | Cociente que gobierna procesos isentrópicos; relación $\kappa_T/\kappa_s = \gamma$ |
> | [[Efecto Joule Thomson \| Efecto Joule-Thomson]] | $\mu_{JT} = (\partial T/\partial P)_h$; se expresa en función de $\alpha$, $c_p$ y la EdE |
> | [[TdS | Ecuaciones $T\,ds$]] | Punto de partida de la derivación |
> | [[Maxwell]] | Relaciones de Maxwell que entran en las ecuaciones $T\,ds$ |
> | [[Identidades/index \| Identidades]] | Regla triple producto usada en el Paso 5 |

> [!referencia]
> Çengel & Boles, *Termodinámica*, §12-4; Callen, *Thermodynamics*, §7-2; Moran & Shapiro, §11.3; Borgnakke & Sonntag, §13.4.
