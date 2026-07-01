---
title: Diagramas de Fase
order: 1
tags:
  - termodinamica
  - teoria
  - sustancias-puras
  - diagramas
  - clausius-clapeyron
draft: false
aliases:
  - Diagramas de Fase
  - Diagrama PV
  - Diagrama TV
  - Diagrama PT
---

# Diagramas de Fase

> [!definicion]
> Los **diagramas de fase** son proyecciones de la superficie termodinámica $P$–$v$–$T$ sobre planos bidimensionales. Para una sustancia pura simple, los tres diagramas relevantes son: $P$–$T$ (muestra las líneas de coexistencia), $T$–$v$ y $P$–$v$ (muestran la región bifásica como área). La ecuación que gobierna cada línea de coexistencia es la **ecuación de Clausius-Clapeyron**.

---

## Ecuación de Clausius-Clapeyron

> [!teorema] Clausius-Clapeyron
> Para cualquier curva de coexistencia entre dos fases $\alpha$ y $\beta$ de una sustancia pura:
> $$\boxed{\frac{dP}{dT}\bigg|_{\rm coex} = \frac{h_{\beta\alpha}}{T\,v_{\beta\alpha}}}$$
> donde $h_{\beta\alpha}=h_\beta - h_\alpha$ es la entalpía de transición y $v_{\beta\alpha}=v_\beta-v_\alpha$ es el cambio de volumen específico.

> [!demostracion]
> **Paso 1 — Condición de equilibrio de fases.** Dos fases coexisten en equilibrio mecánico ($P_\alpha=P_\beta\equiv P$) y térmico ($T_\alpha=T_\beta\equiv T$) si y solo si sus potenciales de Gibbs específicos son iguales:
> $$g_\alpha(T,P)=g_\beta(T,P).$$
> Esta es la condición de equilibrio químico para una sustancia pura (corolario de la igualdad de potenciales químicos).
>
> **Paso 2 — Diferenciación a lo largo de la curva de coexistencia.** Sobre la curva, $g_\alpha=g_\beta$ para todo $(T,P)$ que satisfaga la relación de coexistencia $P=P_{\rm sat}(T)$. Diferenciando ambos lados:
> $$dg_\alpha = dg_\beta.$$
> Usando la identidad de Gibbs-Duhem para cada fase (a composición constante de sustancia pura):
> $$dg = -s\,dT + v\,dP,$$
> se obtiene:
> $$-s_\alpha\,dT + v_\alpha\,dP = -s_\beta\,dT + v_\beta\,dP.$$
>
> **Paso 3 — Despejar $dP/dT$.** Reagrupando:
> $$(v_\beta - v_\alpha)\,dP = (s_\beta - s_\alpha)\,dT$$
> $$\frac{dP}{dT} = \frac{s_{\beta\alpha}}{v_{\beta\alpha}}.$$
>
> **Paso 4 — Expresar en términos de entalpía.** La transición de fase ocurre a temperatura $T$ constante. Para un proceso isotérmico reversible entre dos estados de equilibrio:
> $$\Delta g = 0 \implies h_{\beta\alpha} = T\,s_{\beta\alpha} \implies s_{\beta\alpha} = \frac{h_{\beta\alpha}}{T}.$$
> Sustituyendo:
> $$\frac{dP}{dT} = \frac{h_{\beta\alpha}}{T\,v_{\beta\alpha}}. \qquad \blacksquare$$

---

## Diagrama $P$–$T$

El diagrama $P$–$T$ muestra la **proyección** de la superficie termodinámica sobre el plano de las variables intensivas $(T,P)$. Las **regiones de fase pura** (sólido, líquido, gas) son áreas; las **curvas de coexistencia** son líneas.

**Curva de vaporización** (líquido ↔ vapor):
$$\frac{dP_{\rm sat}}{dT} = \frac{h_{fg}}{T\,v_{fg}}>0$$
siempre positiva (al aumentar $T$, $P_{\rm sat}$ aumenta). Termina en el **punto crítico** $C=(T_c,P_c)$.

**Curva de fusión** (sólido ↔ líquido):
$$\frac{dP_{\rm fus}}{dT} = \frac{h_{sl}}{T\,v_{sl}}$$
positiva para la mayoría de sustancias ($v_{\rm liq}>v_{\rm sol}$); negativa para el agua ($v_{\rm liq}<v_{\rm sol}$ porque el hielo flota).

**Curva de sublimación** (sólido ↔ vapor):
$$\frac{dP_{\rm sub}}{dT} = \frac{h_{sg}}{T\,v_{sg}}>0, \qquad h_{sg}=h_{sl}+h_{lg}.$$

Las tres curvas se cruzan en el **punto triple** $(T_t,P_t)$.

![[diagrama_pt_fases.svg|440]]
*Diagrama $P$–$T$: curvas de fusión (pendiente negativa para el agua), vaporización y sublimación. El punto triple $\mathbf{T}$ y el punto crítico $\mathbf{C}$ son los dos puntos singulares. Para $P>P_c$: fluido supercrítico (sin distinción líquido/vapor).*

> [!proposicion] Integración aproximada de Clausius-Clapeyron para la curva de vaporización
> Si $h_{fg}$ es aproximadamente constante y $v_{fg}\approx v_g = RT/P$ (vapor como gas ideal, $v_g\gg v_f$):
> $$\frac{dP_{\rm sat}}{dT}=\frac{h_{fg}}{T}\cdot\frac{P_{\rm sat}}{RT^2}$$
> $$\frac{d\ln P_{\rm sat}}{d(1/T)}=-\frac{h_{fg}}{R}.$$
> Integrando entre $(T_1,P_1)$ y $(T_2,P_2)$:
> $$\ln\frac{P_2}{P_1}=-\frac{h_{fg}}{R}\left(\frac{1}{T_2}-\frac{1}{T_1}\right).$$
> Esta es la **ecuación de Clausius-Clapeyron integrada** o ecuación de Antoine simplificada; válida lejos del punto crítico donde la hipótesis de gas ideal es razonable.

> [!demostracion]
> **Paso 1.** Aproximar $v_{fg}\approx v_g$: válido cuando $v_g\gg v_f$, lo cual se cumple lejos del punto crítico (por ejemplo, para agua a 100°C: $v_g=1.673\,\mathrm{m^3/kg}$ vs. $v_f=0.001044\,\mathrm{m^3/kg}$, razón $\approx1600$).
>
> **Paso 2.** Usar gas ideal $Pv_g=RT$ (por unidad de masa, $R=R_u/M$):
> $$\frac{dP_{\rm sat}}{dT}=\frac{h_{fg}}{T\,v_g}=\frac{h_{fg}}{T}\cdot\frac{P_{\rm sat}}{RT^2}=\frac{h_{fg}\,P_{\rm sat}}{RT^2}.$$
>
> **Paso 3.** Separar variables:
> $$\frac{dP_{\rm sat}}{P_{\rm sat}}=\frac{h_{fg}}{R}\frac{dT}{T^2}=-\frac{h_{fg}}{R}\,d\!\left(\frac{1}{T}\right).$$
>
> **Paso 4.** Integrar con $h_{fg}=$ cte:
> $$\ln P_{\rm sat}\Big|_1^2 = -\frac{h_{fg}}{R}\cdot\frac{1}{T}\bigg|_1^2$$
> $$\ln\frac{P_2}{P_1}=-\frac{h_{fg}}{R}\left(\frac{1}{T_2}-\frac{1}{T_1}\right). \qquad \blacksquare$$

---

## Diagrama $T$–$v$

En el plano $T$–$v$ la región bifásica aparece como un **área** (la cúpula de saturación), en contraste con el punto o línea que la representa en el plano $P$–$T$.

- La **línea de líquido saturado** ($x=0$, izquierda) y la **línea de vapor saturado** ($x=1$, derecha) forman la cúpula; se unen en el punto crítico.
- Las isotermas ($T=$ cte) son horizontales dentro de la cúpula (cambio de fase isobárico e isotérmico).
- Para $T>T_c$: no existe región bifásica; la isoterma cruza de comprimido a sobrecalentado sin discontinuidad.

![[diagrama_tv_cupula.svg|460]]
*Diagrama $T$–$v$ con isotermas seleccionadas. La isoterma $T_c$ tiene un punto de inflexión horizontal en el punto crítico. Las isotermas $T < T_c$ presentan tramos planos (región bifásica) cuya longitud $v_g-v_f$ decrece con la temperatura hasta anularse en $C$.*

---

## Diagrama $P$–$v$

En el plano $P$–$v$ la región bifásica también es un área. Las **isotermas** para $T<T_c$ consisten en tres segmentos: líquido comprimido (casi vertical), tramo horizontal de coexistencia (isobárico: $P=P_{\rm sat}(T)$), y vapor sobrecalentado (hipérbola aproximada).

$$\text{Isobara de coexistencia:}\quad P=P_{\rm sat}(T)=\text{cte},\quad v\in[v_f(T),\,v_g(T)].$$

Para $T>T_c$ la isoterma es continua (fluido supercrítico); para $T=T_c$ la isoterma tiene un punto de inflexión con pendiente nula en $(P_c,v_c)$.

![[diagrama_pv_isotermas.svg|440]]
*Diagrama $P$–$v$ con isotermas $T_1<T_2<T_c<T_3$. La región bifásica (sombreada) queda encerrada por las líneas de líquido y vapor saturado. Los tramos horizontales son las isobaras de saturación $P_{\rm sat}(T)$.*

---

## Superficie termodinámica $P$–$v$–$T$

Los tres diagramas anteriores son proyecciones de la **superficie** $P$–$v$–$T$, la hipersuperficie de equilibrio en el espacio de las tres variables de estado. La ecuación de estado $f(P,v,T)=0$ define esta superficie.

Las regiones de la superficie corresponden a:
- **Planos inclinados** en las zonas de fase pura (líquido, sólido, gas).
- **Canales horizontales** en las regiones de coexistencia (donde $P$ y $T$ están ligadas por Clausius-Clapeyron).
- **Punto singular** (punto crítico).

![[superficie_pvt.svg|480]]
*Superficie termodinámica $P$–$v$–$T$ para una sustancia que se expande al solidificarse (tipo agua). Las tres proyecciones ($P$–$T$, $T$–$v$, $P$–$v$) se obtienen proyectando esta superficie sobre los planos coordenados.*

---

## Ejemplo: estimar la presión de vapor del agua a $80\,°\mathrm{C}$ y a $120\,°\mathrm{C}$

> [!ejemplo]
> **Datos.** A $T_1=100\,°\mathrm{C}$ (373.15 K): $P_1=101.325\,\mathrm{kPa}$, $h_{fg,1}=2256.5\,\mathrm{kJ/kg}$. Estimar $P_{\rm sat}$ a $T_2=80\,°\mathrm{C}$ y a $T_3=120\,°\mathrm{C}$ con la ecuación integrada de Clausius-Clapeyron.
>
> **Constante de gas para el agua.** $R=R_u/M=8.314/18.015=0.4615\,\mathrm{kJ/(kg\cdot K)}$.

> [!solucion]
> **Paso 1 — Aplicar la ecuación integrada.**
> $$\ln\frac{P_2}{P_1}=-\frac{h_{fg}}{R}\left(\frac{1}{T_2}-\frac{1}{T_1}\right).$$
>
> **Paso 2 — Para $T_2=80\,°\mathrm{C}=353.15\,\mathrm{K}$.**
> $$\frac{1}{T_2}-\frac{1}{T_1}=\frac{1}{353.15}-\frac{1}{373.15}=2.832\times10^{-3}-2.680\times10^{-3}=1.52\times10^{-4}\,\mathrm{K^{-1}}.$$
> $$\ln\frac{P_2}{101.325}=-\frac{2256.5}{0.4615}\times 1.52\times10^{-4}=-4888\times1.52\times10^{-4}=-0.743.$$
> $$P_2=101.325\times e^{-0.743}=101.325\times 0.476=48.2\,\mathrm{kPa}.$$
> Valor tabular (CATT3): $47.39\,\mathrm{kPa}$ — error $\approx 1.7\%$, razonable pues $h_{fg}$ varía.
>
> **Paso 3 — Para $T_3=120\,°\mathrm{C}=393.15\,\mathrm{K}$.**
> $$\frac{1}{T_3}-\frac{1}{T_1}=\frac{1}{393.15}-\frac{1}{373.15}=2.544\times10^{-3}-2.680\times10^{-3}=-1.36\times10^{-4}\,\mathrm{K^{-1}}.$$
> $$\ln\frac{P_3}{101.325}=-4888\times(-1.36\times10^{-4})=+0.665.$$
> $$P_3=101.325\times e^{0.665}=101.325\times1.944=197.0\,\mathrm{kPa}.$$
> Valor tabular: $198.5\,\mathrm{kPa}$ — error $\approx 0.8\%$.
>
> **Conclusión.** La ecuación integrada predice $P_{\rm sat}$ con error $<2\%$ en el rango $80$–$120\,°\mathrm{C}$, confirmando que $h_{fg}$ y $v_{fg}\approx v_g$ (gas ideal) son hipótesis aceptables lejos del punto crítico.

> [!referencia]
> Çengel & Boles §3-7; Moran & Shapiro §11.2; Callen, *Thermodynamics*, §9.1 (derivación formal de Clausius-Clapeyron desde los postulados).
