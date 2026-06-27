---
title: Sustancias Puras
order: 3
tags:
  - termodinamica
  - teoria
  - sustancias-puras
  - fases
  - indice
draft: false
aliases:
  - Sustancias Puras
---

# Sustancias Puras

> [!definicion]
> Una **sustancia pura** es aquella cuya composición química es homogénea e invariante. Puede coexistir en múltiples fases siempre que cada fase tenga la misma composición. El agua ($\mathrm{H_2O}$), el refrigerante R-134a y el nitrógeno son sustancias puras. El aire húmedo no lo es: al condensar agua cambia la composición de la fase gaseosa.

> [!info]
> **Ubicación.** Curso MN121 · sección Propiedades / Sustancias Puras. Esta sección fundamenta el uso de las tablas termodinámicas (CATT3) y los ciclos de vapor ([[../../../Conversion de Energia/Ciclos Potencia/index | Ciclos de Potencia]]). Se apoya en [[Variables de Estado/index | Variables de Estado]] y alimenta directamente los balances de [[../../../Conservacion/Volumenes de Control/Balance de Energia VC | energía en volúmenes de control]].

---

## Principio de estado y la superficie $P$–$v$–$T$

Para una sustancia pura **simple** (un solo modo relevante de trabajo reversible: $\delta w = -P\,dv$), el **principio de estado** establece que dos propiedades intensivas independientes fijan el estado de equilibrio. La información completa de equilibrio reside en la superficie termodinámica $P$–$v$–$T$.

Las fases se separan por **líneas de coexistencia** en el plano $P$–$T$. En cada punto de esas líneas dos fases coexisten; la relación entre presión y temperatura a lo largo de cada curva está gobernada por la [[Diagramas de Fase | ecuación de Clausius-Clapeyron]]:

$$\frac{dP}{dT}\bigg|_{\rm coex} = \frac{\Delta h}{T\,\Delta v}$$

donde $\Delta h$ y $\Delta v$ son los saltos de entalpía y volumen específico entre las dos fases.

---

## Las tres regiones y la cúpula de saturación

La proyección de la superficie $P$–$v$–$T$ sobre el plano $T$–$v$ produce la **cúpula de saturación**, que divide el espacio en tres regiones operativas:

| Región | Nombre | Estado fijado por |
|:---|:---|:---|
| Izquierda de la cúpula | Líquido comprimido (subenfriado) | $(T,\,P)$ |
| Bajo la cúpula | Mezcla líquido-vapor | $(T,\,x)$ o $(P,\,x)$ |
| Derecha de la cúpula | Vapor sobrecalentado | $(T,\,P)$ |

La cúpula culmina en el **punto crítico** $(T_c, P_c, v_c)$; para el agua: $T_c=374.14\,°\mathrm{C}$, $P_c=22.09\,\mathrm{MPa}$, $v_c=0.003155\,\mathrm{m^3/kg}$. Por encima de $T_c$ no existe distinción líquido/vapor.

![[diagrama_tv_cupula.svg|460]]
*Diagrama $T$–$v$ con la cúpula de saturación del agua. Las isotermas por debajo de $T_c$ presentan un tramo horizontal (coexistencia a $P$ constante) que desaparece en el punto crítico $\mathbf{C}$. El punto triple $\mathbf{T}$ marca la temperatura mínima de coexistencia líquido-vapor.*

---

## Singularidades: punto triple y punto crítico

**Punto triple.** Las tres curvas de coexistencia (fusión, vaporización, sublimación) convergen en un único punto $(T_t,\,P_t)$ donde las tres fases coexisten en equilibrio. Para el agua: $T_t=273.16\,\mathrm{K}$, $P_t=611.73\,\mathrm{Pa}$. La regla de fases de Gibbs confirma que el punto triple tiene cero grados de libertad: $F=C-\phi+2=1-3+2=0$.

**Punto crítico.** Al final de la curva de vaporización, el límite entre líquido y vapor desaparece. En el punto crítico se cumple:
$$\left(\frac{\partial P}{\partial v}\right)_{T_c}=0,\qquad \left(\frac{\partial^2 P}{\partial v^2}\right)_{T_c}=0.$$
Estas dos condiciones, impuestas sobre la ecuación de estado, permiten determinar $T_c$, $P_c$ y $v_c$ para cualquier fluido.

![[diagrama_pt_fases.svg|400]]
*Diagrama $P$–$T$: curvas de fusión, vaporización y sublimación. La flecha indica un proceso de calentamiento isobárico a $P < P_t$ que causa sublimación directa (sólido → vapor), característico del $\mathrm{CO_2}$ sólido a presión atmosférica.*

---

## Notas de esta sección

> [!info] Mapa
> - [[Diagramas de Fase]] — diagramas $P$–$T$, $T$–$v$, $P$–$v$; superficie termodinámica $P$–$v$–$T$; demostración de Clausius-Clapeyron.
> - [[Cambio de Fase]] — entalpía de vaporización $h_{fg}$; correlación de Watson; punto crítico y triple.
> - [[Propiedades en la Region Bifasica]] — calidad $x$; regla de la palanca; tablas de saturación; ejemplos con vapor de agua.
> - [[Liquido Comprimido]] — región subenfriada; aproximación $v\approx v_f(T)$; corrección de presión $h\approx h_f+v_f\Delta P$.
> - [[Vapor Sobrecalentado]] — uso de tablas de vapor sobrecalentado; interpolación; desviación del gas ideal; factor $Z$.

> [!referencia]
> Çengel & Boles, *Termodinámica*, cap. 3; Moran & Shapiro, *Fundamentals of Engineering Thermodynamics*, cap. 3; Borgnakke & Sonntag, *Fundamentals of Thermodynamics*, cap. 2. Tablas numéricas con **CATT3**.
