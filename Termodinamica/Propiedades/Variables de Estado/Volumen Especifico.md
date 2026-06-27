---
title: "Volumen específico $v$"
order: 3
tags:
  - termodinamica
  - propiedades
  - variables_de_estado
  - volumen_especifico
draft: false
aliases:
  - specific volume
  - v
  - volumen especifico
---

# Volumen específico $v$

> [!definicion]
> El **volumen específico** es el volumen que ocupa la unidad de masa de una sustancia:
> $$v \equiv \frac{V}{m} \quad [\text{m}^3/\text{kg}],$$
> y su inverso es la densidad másica: $\rho = 1/v$. Mientras que $\rho$ es útil en mecánica de fluidos (donde aparece en $\rho\,\mathbf{v}$ y $\rho g h$), la termodinámica prefiere $v$ porque la relación fundamental $dU = T\,dS - P\,dV$ y la ecuación de trabajo $\delta w = P\,dv$ se escriben de forma natural en términos del volumen. Los órdenes de magnitud caracterizan el estado de la materia:
>
> | Sustancia | $v$ [m³/kg] | Interpretación |
> |:---|:---:|:---|
> | Agua líquida (20 °C) | $0.001002$ | 1 kg ocupa 1 litro |
> | Vapor de agua (100 °C, 1 atm) | $1.6720$ | 1 kg ocupa 1672 litros |
> | Aire (25 °C, 1 atm) | $0.8428$ | 1 kg ocupa 843 litros |
> | Acero | $\approx 1.27 \times 10^{-4}$ | 1 kg ocupa 0.127 litros |
>
> El factor $v_{\rm vapor}/v_{\rm líquido} \approx 1670$ del agua a 100 °C explica el principio de la máquina de vapor: el mismo kilogramo de agua se expande a 1670 veces su volumen original al evaporarse, generando el trabajo de empuje sobre el pistón.

---

## Por qué la termodinámica usa $v$ y no $\rho$

> [!teoria]
> Las dos formas equivalentes son $v = 1/\rho$, pero no son intercambiables conceptualmente en termodinámica:
>
> 1. **Trabajo de frontera.** El trabajo reversible de un sistema simple compresible es $\delta w = P\,dv$. Integrar $\int P\,dv$ a lo largo de una curva en el plano $P$-$v$ es natural; la forma en $\rho$ requiere un cambio de variable que complica los diferenciales.
>
> 2. **Ecuación de estado.** Para el gas ideal, $Pv = RT$ (forma de Clausius-Clapeyron). En forma de densidad: $P = \rho R T$. Ambas son equivalentes, pero la forma con $v$ es la que aparece en la relación fundamental y en los potenciales termodinámicos.
>
> 3. **Variables naturales.** La energía interna $U$ tiene a $(S, V)$ como variables naturales: $dU = T\,dS - P\,dV$. El volumen $V$ (o $v$ específico) es la variable de estado, no la densidad.
>
> 4. **Regla del cuadrado mágico.** En la representación de Gibbs de los cuatro potenciales, las esquinas son $(S, V, T, P)$ y las variables de Maxwell se derivan de $V$, no de $\rho$.

---

## Extensivo, intensivo y molar

> [!proposicion]
> | Magnitud | Símbolo | Definición | Unidades |
> |:---|:---:|:---|:---|
> | Volumen total (extensivo) | $V$ | volumen del sistema | m³ |
> | Volumen específico (intensivo) | $v = V/m$ | volumen por unidad de masa | m³/kg |
> | Volumen molar (intensivo) | $\bar{v} = V/n$ | volumen por mol | m³/mol |
>
> La relación entre las tres: $V = mv = n\bar{v}$ con $m = nM$ ($M$ = masa molar en kg/mol). Conversión: $\bar{v} = Mv$ (por ejemplo, para agua: $\bar{v} = 0.018015\,\text{kg/mol} \times 0.001002\,\text{m}^3/\text{kg} = 1.804 \times 10^{-5}\,\text{m}^3/\text{mol}$).

---

## Región bifásica: regla de la palanca

> [!proposicion]
> En la región de coexistencia líquido–vapor, el volumen específico de la mezcla se obtiene a partir de la [[Calidad]] $x$:
> $$v = v_f + x\,v_{fg}, \qquad v_{fg} = v_g - v_f,$$
> donde $v_f$ y $v_g$ son los volúmenes específicos del líquido saturado y el vapor saturado a esa temperatura o presión. La misma expresión es válida para **cualquier** propiedad específica extensiva: $y = y_f + x\,y_{fg}$ para $y \in \{u, h, s\}$.

> [!demostracion]
> **Hipótesis:** el sistema es una mezcla en equilibrio de líquido saturado (masa $m_f$, volumen específico $v_f$) y vapor saturado (masa $m_g$, volumen específico $v_g$), sin efectos de superficie.
>
> **Paso 1 — Aditividad del volumen total.**
> El volumen total de la mezcla es la suma de los volúmenes de las dos fases (el volumen es propiedad extensiva):
> $$V = V_f + V_g = m_f\,v_f + m_g\,v_g.$$
> Aquí se usa que cada fase ocupa un volumen $V_f = m_f v_f$ y $V_g = m_g v_g$ con sus propiedades de fase saturada.
>
> **Paso 2 — Dividir por la masa total.**
> La masa total de la mezcla es $m = m_f + m_g$. Dividiendo la expresión del paso 1:
> $$v \equiv \frac{V}{m} = \frac{m_f\,v_f + m_g\,v_g}{m_f + m_g}.$$
>
> **Paso 3 — Introducir la calidad $x = m_g/m$.**
> Entonces $m_f/m = 1 - x$ y $m_g/m = x$:
> $$v = \frac{m_f}{m}\,v_f + \frac{m_g}{m}\,v_g = (1-x)\,v_f + x\,v_g.$$
>
> **Paso 4 — Reescribir en forma estándar.**
> Expandiendo y agrupando:
> $$v = v_f - x\,v_f + x\,v_g = v_f + x\,(v_g - v_f) = v_f + x\,v_{fg}.$$
> $$\boxed{v = v_f + x\,v_{fg}.} \qquad \blacksquare$$
>
> **Paso 5 — Extensión a otras propiedades.**
> El argumento de los pasos 1–4 aplica a cualquier propiedad extensiva $Y$: $Y = m_f y_f + m_g y_g$. Dividiendo por $m$ y usando $x = m_g/m$:
> $$y = y_f + x\,y_{fg} \qquad \text{para } y \in \{u, h, s\}.$$
> Esta generalización es exacta: no requiere hipótesis adicionales más allá de que $u$, $h$, $s$ sean extensivas y estén en equilibrio termodinámico.
>
> **Verificación de límites:** para $x = 0$ (líquido puro), $v = v_f$. Para $x = 1$ (vapor puro), $v = v_f + v_{fg} = v_g$. Ambos límites son correctos. $\checkmark$

> [!ejemplo]
> **Agua a $P = 200\,\text{kPa}$, calidad $x = 0.4$.** De tablas de vapor saturado: $T_{sat} = 120.23\,°\text{C}$, $v_f = 0.001061\,\text{m}^3/\text{kg}$, $v_g = 0.8857\,\text{m}^3/\text{kg}$.
>
> **Paso 1 — Calcular $v_{fg}$:**
> $$v_{fg} = v_g - v_f = 0.8857 - 0.001061 = 0.8846\,\text{m}^3/\text{kg}.$$
>
> **Paso 2 — Aplicar la regla de la palanca:**
> $$v = v_f + x\,v_{fg} = 0.001061 + 0.4 \times 0.8846 = 0.001061 + 0.3538 = 0.3549\,\text{m}^3/\text{kg}.$$
>
> **Interpretación:** aunque el 40% de la masa es vapor, ese vapor ocupa $0.3538\,\text{m}^3/\text{kg}$ del volumen total $0.3549\,\text{m}^3/\text{kg}$ — el 99.7% del volumen. El 60% de la masa (líquido) solo ocupa el 0.3% del volumen, porque $v_g \gg v_f$. Esta asimetría es característica de cualquier mezcla líquido–vapor en condiciones alejadas del punto crítico. $\blacksquare$

---

![[volumen_especifico_campana_Pv.svg|460]]
*Diagrama $P$–$v$ con la campana de saturación. Las líneas de $v$ constante (isocoras) son verticales. Dentro de la campana, $v$ varía de $v_f$ (extremo izquierdo) a $v_g$ (extremo derecho) a presión fija; la escala logarítmica es necesaria para mostrar el factor $\sim 1000$ entre $v_f$ y $v_g$ a baja presión.*

## Casos especiales: gas ideal y líquido incompresible

> [!proposicion]
> **Gas ideal.** De $Pv = RT$ (con $R$ constante específica del gas):
> $$v = \frac{RT}{P}.$$
> El volumen específico crece con $T$ (expansión térmica) y decrece con $P$ (compresión).
>
> **Líquido o sólido (modelo incompresible).** A presión y temperatura que no se alejen demasiado de las condiciones de referencia:
> $$v \approx v_f(T) \qquad \text{(independiente de }P\text{)}.$$
> El coeficiente de expansión térmica $\alpha = (1/v)(\partial v/\partial T)_P$ es pequeño pero no nulo: el agua líquida se dilata al calentar (excepto entre 0 y 4 °C donde tiene comportamiento anómalo). La corrección de entalpía a presión variable es $h(T,P) \approx h_f(T) + v_f\,[P - P_{sat}(T)]$ (ver [[Liquido Comprimido]]).

---

## Relación con otras propiedades

> [!info]
> - **Trabajo de frontera:** $w = \int_1^2 P\,dv$ (área bajo la curva $P$-$v$); $v$ define el eje horizontal del diagrama $P$-$v$.
> - **Relación fundamental:** $dU = T\,dS - P\,dV$; $V$ (o $v$) es la variable conjugada de $-P$.
> - **Variables naturales:** $v$ es variable natural de la [[Energia Interna]] $U$ y de [[Helmholtz]] $F$.
> - **Regla de la palanca:** en región bifásica, $v$ y la [[Calidad]] se determinan mutuamente con $P$ o $T$.
> - **Coeficiente de expansión:** $\alpha \equiv (1/v)(\partial v/\partial T)_P$ y compresibilidad $\kappa_T \equiv -(1/v)(\partial v/\partial P)_T$; ver [[Relaciones Termodinamicas/index | Relaciones Termodinámicas]].

> [!info]
> **Convención de notación:**
> - $v$: volumen específico [m³/kg]; $\bar{v}$: molar [m³/mol]; $V$: total [m³]
> - $v_f$, $v_g$: líquido y vapor saturados; $v_{fg} = v_g - v_f$
> - $\rho = 1/v$: densidad [kg/m³]

> [!referencia]
> Borgnakke & Sonntag, *Fundamentals of Thermodynamics*, §2.3–2.5; Çengel & Boles, *Termodinámica*, §2-2 a 2-4; Moran & Shapiro, *Fundamentals of Engineering Thermodynamics*, §3.1; Callen, *Thermodynamics*, §1-3.
