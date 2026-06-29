---
title: "Variables de Estado"
order: 1
tags:
  - termodinamica
  - propiedades
  - variables_de_estado
  - index
draft: false
aliases:
  - propiedades de estado
  - funciones de estado
  - postulado de estado
---

# Variables de Estado

> [!definicion]
> Una **variable de estado** (o función de estado) es una propiedad termodinámica cuyo valor depende únicamente del **estado actual** del sistema, sin importar el camino seguido para alcanzarlo. Ejemplos: $P$, $T$, $v$, $u$, $h$, $s$. Contraste: el calor $Q$ y el trabajo $W$ son **funciones de proceso** — su valor depende de la trayectoria. La distinción tiene consecuencia algebraica: las variables de estado tienen diferenciales exactas ($du$, $dh$, $ds$); $Q$ y $W$ tienen diferenciales inexactas ($\delta Q$, $\delta W$).

---

## ¿Por qué importa que algo sea función de estado?

> [!teoria]
> Si $y$ es función de estado, entonces $\oint dy = 0$ en cualquier ciclo cerrado, y $\Delta y = y_2 - y_1$ depende solo de los estados extremos — no del proceso. Esto tiene tres consecuencias prácticas:
>
> 1. **Tablas de propiedades.** Toda la información del agua, por ejemplo, se puede tabular en función de $(P, T)$, porque $v$, $u$, $h$, $s$ son funciones de estado y no del camino. Las tablas de vapor son posibles precisamente por esto.
> 2. **Análisis de ciclos.** En un ciclo $1\to2\to1$, el cambio neto de cualquier variable de estado es cero: $\Delta u_{\text{ciclo}} = 0$, $\Delta s_{\text{ciclo}} = 0$. Lo que no es cero son $Q_{\text{neto}}$ y $W_{\text{neto}}$ — esas son las cantidades de interés en ciclos de potencia y refrigeración.
> 3. **Integración libre de camino.** Para calcular $\Delta h$ entre dos estados, se puede elegir cualquier camino conveniente — isobárico, isotérmico, ideal — aunque el proceso real sea otro. La libertad de camino es la herramienta analítica clave en termodinámica.

---

## Postulado de estado

> [!axioma]
> Para un **sistema simple compresible** — aquel cuyo único modo de trabajo reversible es $P\,dV$ —, el estado termodinámico de equilibrio queda completamente determinado por **dos propiedades intensivas independientes**.
>
> *Consecuencia:* todas las demás propiedades intensivas ($v$, $u$, $h$, $s$, $c_p$, $\alpha$, $\kappa_T$, etc.) quedan fijas. Elegir dos variables es suficiente; elegir tres es redundante en tanto haya una ecuación de estado que las relacione.
>
> *Condición "simple compresible":* no hay efectos eléctricos, magnéticos ni de tensión superficial relevantes. Cubre prácticamente toda la termodinámica de ingeniería: vapor, gases, líquidos, mezclas no reactivas.

> [!teoria] Ejemplo concreto del postulado
> Agua líquida comprimida a $P = 1\,\text{MPa}$, $T = 170\,°\text{C}$ (por debajo de $T_{\rm sat}=179.9\,°\text{C}$, así que $T$ y $P$ son independientes): el volumen específico vale $v = 0.001114\,\text{m}^3/\text{kg}$, la entalpía $h = 719.3\,\text{kJ/kg}$, la entropía $s = 2.042\,\text{kJ/(kg·K)}$. No importa cómo llegó el agua a ese estado — calentada isobaramente desde 20 °C, o comprimida isotérmicamente desde 0.1 MPa — el estado y todas sus propiedades son idénticos. El postulado no se demuestra: es un hecho experimental verificado con cualquier sustancia.

---

## Propiedades intensivas y extensivas

> [!teoria]
> | Tipo | Característica | Ejemplos |
> |:---|:---|:---|
> | **Intensiva** | No cambia si se subdivide el sistema | $P$, $T$, $v$, $u$, $h$, $s$, $\rho$ |
> | **Extensiva** | Proporcional al tamaño del sistema | $V$, $U$, $H$, $S$, $m$ |
>
> El postulado de estado se enuncia con propiedades **intensivas** porque dos sistemas a la misma $T$ y $P$ tienen el mismo estado termodinámico específico, aunque tengan distinta masa y por tanto distintos $V$, $U$, $H$, $S$.
>
> Notación del vault: **mayúscula** → extensiva total ($U$, $H$, $V$); **minúscula** → específica por kg ($u$, $h$, $v$); **barra** → molar ($\bar{u}$, $\bar{h}$, $\bar{v}$). La conversión es $u = U/m$, $\bar{u} = U/n = Mu$ con $M$ la masa molar.

---

## El trío $P$, $T$, $v$ y la ecuación de estado

> [!teoria]
> Para una sustancia pura en **una sola fase**, las variables $P$, $T$ y $v$ están ligadas por la **ecuación de estado** $f(P, v, T) = 0$: tres variables, una restricción, dos grados de libertad — consistente con el postulado. Conocer dos de las tres determina la tercera.
>
> Ecuaciones de estado típicas:
> - Gas ideal: $Pv = RT$ (válida a presiones bajas y temperaturas altas respecto al punto crítico)
> - van der Waals: $(P + a/v^2)(v-b) = RT$ (incluye atracción y volumen excluido)
> - Redlich-Kwong, Peng-Robinson: mayor precisión para gases reales
>
> Las dos variables más fáciles de medir experimentalmente son $P$ y $T$ (manómetro, termómetro). A partir de ellas, $v$ se obtiene de la ecuación de estado o de tablas. Ver [[Ecuaciones de Estado/index | Ecuaciones de Estado]] para el tratamiento completo.

---

## Región bifásica: $P$ y $T$ dejan de ser independientes

![[variables_estado_diagrama_Pv.svg|480]]
*Diagrama $P$–$v$ con las tres regiones (líquido comprimido, campana bifásica, vapor sobrecalentado). Cada punto del diagrama es un estado; dos propiedades independientes lo fijan. En la campana, las iso-$P$ y las iso-$T$ son paralelas (degeneradas), de ahí que se necesite $x$ como tercera variable.*

> [!proposicion]
> Dentro de la **campana de saturación** (coexistencia líquido–vapor), la presión de saturación y la temperatura de saturación están ligadas por $P_{sat} = P_{sat}(T)$: no son independientes. El postulado de estado sigue siendo válido, pero la pareja $(P, T)$ ya no es un conjunto de dos variables independientes. Se necesita una **tercera propiedad** para fijar el estado: la [[Calidad]] $x$ (fracción másica de vapor).
>
> Resumen de combinaciones válidas para fijar el estado:
>
> | Región | Par que fija el estado |
> |:---|:---|
> | Una sola fase (líquido comprimido, vapor SC) | $(P, T)$, $(P, v)$, $(T, v)$, $(P, h)$, … |
> | Bifásica (mezcla saturada) | $(P, x)$ o $(T, x)$ o $(P, v)$ o $(T, v)$ — nunca $(P,T)$ solos |

---

## Mapa de notas

> [!info]
> - [[Presion]] (order 2) — fuerza normal por unidad de área; presión absoluta vs. manométrica.
> - [[Temperatura]] (order 3) — propiedad del equilibrio térmico; escala de Kelvin.
> - [[Volumen Especifico]] (order 4) — volumen por unidad de masa; $v = 1/\rho$.
> - [[Calidad]] (order 5) — fracción másica de vapor en la región bifásica.
> - [[Ecuaciones de Estado/index | Ecuaciones de Estado]] — relaciones $f(P,v,T) = 0$ para gases y fluidos reales.
> - [[Propiedades en la Region Bifasica]] — cómo obtener $v$, $u$, $h$, $s$ en la campana.

> [!referencia]
> Borgnakke & Sonntag, *Fundamentals of Thermodynamics*, §2.1–2.4; Çengel & Boles, *Termodinámica*, §1-7 a 2-5; Callen, *Thermodynamics*, §1-1 a 1-3; Moran & Shapiro, §3.1.
