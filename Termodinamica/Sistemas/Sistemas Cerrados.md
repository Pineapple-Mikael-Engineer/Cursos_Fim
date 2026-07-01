---
title: Sistema Cerrado
order: 1
tags:
  - termodinamica
  - sistemas
  - sistema-cerrado
draft: false
aliases:
  - closed system
  - masa de control
  - sistemas cerrados
  - SC
---

# Sistema Cerrado

> [!definicion]
> Un **sistema cerrado** (SC) — también llamado *masa de control* — es una región del espacio cuya **masa es fija**: no cruza materia a través de su frontera, aunque sí pueden cruzar calor y trabajo. La frontera puede ser rígida o móvil (pistón).
>
> *¿Por qué este modelo?* En muchos procesos de interés la masa de fluido es siempre la misma: gas atrapado en un cilindro, una bomba de calor por lotes, un globo que se infla. Fijar la masa elimina el término de flujo másico y simplifica radicalmente los balances.
>
> *Aplicaciones:* pistón-cilindro (ciclos Otto, Diesel), reactores batch, globos y cámaras de gas, recipientes a presión sin flujo.

> [!info]
> Esta nota es el **encuadre** del modelo: qué es un SC y cuándo elegirlo. Los balances que lo gobiernan se desarrollan en su carpeta propia: [[Conservacion/Sistemas Cerrados/index | Conservación — Sistema Cerrado]].

---

## Sistema cerrado vs. volumen de control

> [!teoria]
> La elección del modelo depende de una sola pregunta: **¿cruza masa la frontera?**
>
> | | Sistema cerrado (SC) | [[Volumenes de Control \| Volumen de control (VC)]] |
> |:---|:---|:---|
> | Masa | Fija ($m=\text{cte}$) | Variable; entra/sale por corrientes |
> | Frontera | Sigue a la misma masa | Fija en el espacio (superficie de control) |
> | Propiedad natural | [[Energia Interna \| energía interna]] $U$ | [[Entalpia \| entalpía]] $h$ (incluye el trabajo de flujo $Pv$) |
> | Trabajo característico | Frontera móvil $\int P\,dV$ | Trabajo de eje $\dot W_{\rm eje}$ |
> | Ejemplos | pistón-cilindro, recipiente cerrado | turbina, tobera, intercambiador |
>
> La diferencia esencial: en el SC **no hay entalpía transportada** por corrientes de masa — por eso su variable natural es $U$ y no $h$. El paso de SC a VC consiste precisamente en añadir los términos de flujo $\dot m(h+V^2/2+gz)$; ver [[Flujo Estacionario]].

> [!teoria] Cuándo modelar como SC
> Conviene el modelo de sistema cerrado cuando la **misma porción de materia** permanece identificable durante el proceso:
> - Gas confinado que se comprime o expande (un tiempo del ciclo de un motor).
> - Sustancia en un tanque rígido sellado que se calienta o enfría.
> - Procesos por lotes (carga → proceso → descarga analizada aparte).
>
> Si en cambio el fluido **circula** de forma continua a través del dispositivo (régimen estacionario), el modelo natural es el [[Volumenes de Control | volumen de control]].

---

## Leyes que lo gobiernan (resumen y delegación)

> [!teorema] Primera ley
> $$\Delta U = U_2 - U_1 = Q_{12} - W_{12},$$
> con $Q>0$ el calor que **entra** y $W>0$ el trabajo realizado **por** el sistema. La derivación desde el balance general de energía, la descomposición del trabajo y los ejemplos están en [[Primera Ley SC]].

> [!teorema] Segunda ley
> $$S_2 - S_1 = \int_1^2 \frac{\delta Q}{T_b} + S_{\rm gen}, \qquad S_{\rm gen}\ge 0.$$
> El significado de $S_{\rm gen}$, su deducción desde la desigualdad de Clausius y los ejemplos están en [[Segunda Ley SC]]. La destrucción de exergía asociada, $B_{\rm dest}=T_0 S_{\rm gen}$, se trata en [[Balance de Exergia SC]].

> [!proposicion] Trabajo de frontera
> Para un proceso **cuasiestático** con frontera móvil, $W_{\rm frontera}=\int_1^2 P\,dV$ (área bajo la curva $P$–$V$). Las expresiones cerradas por tipo de proceso (isocórico, isobárico, isotérmico, politrópico) se tabulan y deducen en [[Procesos/index | Procesos]]. Para un proceso irreversible contra presión externa constante, $W=P_{\rm ext}(V_2-V_1)$, menor que el trabajo reversible.

---

## Relación con otras notas

> [!info]
> - [[Conservacion/Sistemas Cerrados/index | Conservación — Sistema Cerrado]] — los tres balances (energía, entropía, exergía) en detalle.
> - [[Volumenes de Control]] — el modelo complementario, con flujo de masa.
> - [[Procesos/index | Procesos]] — el trabajo de frontera para cada trayectoria.
> - [[Primera Ley SC]], [[Segunda Ley SC]], [[Balance de Exergia SC]] — derivaciones y ejemplos.

> [!info]
> **Convención:** $Q>0$ calor que entra al SC; $W>0$ trabajo realizado por el SC. Propiedades extensivas en mayúscula ($U$, $S$, $V$); específicas en minúscula ($u$, $s$, $v$).

> [!referencia]
> Borgnakke & Sonntag, Cap. 4–5; Çengel & Boles, Cap. 4; Moran & Shapiro, Cap. 2.
