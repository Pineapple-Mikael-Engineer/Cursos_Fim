---
title: Flujo Estacionario
order: 3
tags:
  - termodinamica
  - sistemas
  - flujo-estacionario
  - SFEE
draft: false
aliases:
  - steady flow
  - SFEE
  - flujo permanente
  - régimen estacionario
---

# Flujo Estacionario

> [!definicion]
> El **flujo estacionario** (o flujo permanente) es el régimen de un [[Volumenes de Control | volumen de control]] en que **ninguna propiedad varía con el tiempo**: ni dentro del VC ni en las corrientes de entrada/salida. Es la hipótesis de operación normal de la práctica totalidad de los equipos termodinámicos de planta continua.
>
> Matemáticamente: $dm_{\rm vc}/dt = 0$ y $dE_{\rm vc}/dt = 0$ (y lo mismo para la entropía del VC).
>
> *¿Cuándo es válida esta hipótesis?* Cuando el sistema ha alcanzado el "estado de régimen" después de un transitorio de arranque. Una turbina de vapor, un compresor, un intercambiador de calor o una tobera operan en estado estacionario durante horas o días; el transitorio de arranque dura segundos y se suele despreciar.
>
> *¿Cuándo no vale?* En procesos de carga/descarga de tanques, en el arranque de calderas, en motores alternativos (donde el pistón crea ciclos no estacionarios). En estos casos se usa el balance completo del [[Volumenes de Control | VC]].

---

## Ecuación de energía SFEE

> [!teorema]
> Para un VC en flujo estacionario con **una entrada** (estado 1) y **una salida** (estado 2):
>
> **Balance de masa:** $\dot{m}_1 = \dot{m}_2 = \dot{m}$.
>
> **Ecuación de energía para flujo estacionario (SFEE):**
> $$\boxed{\dot{Q} - \dot{W} = \dot{m}\!\left[(h_2-h_1) + \frac{C_2^2-C_1^2}{2} + g(z_2-z_1)\right].}$$
>
> Por unidad de masa ($q=\dot{Q}/\dot{m}$, $w=\dot{W}/\dot{m}$):
> $$q - w = (h_2-h_1) + \frac{C_2^2-C_1^2}{2} + g(z_2-z_1).$$

> [!demostracion]
> **Hipótesis:** VC estacionario ($dE_{\rm vc}/dt=0$, $dm_{\rm vc}/dt=0$), una entrada, una salida.
>
> **Paso 1 — Balance de masa.** Con $dm_{\rm vc}/dt=0$:
> $$0 = \dot{m}_1 - \dot{m}_2 \implies \dot{m}_1 = \dot{m}_2 = \dot{m}.$$
>
> **Paso 2 — Balance de energía general del VC.**
> $$\frac{dE_{\rm vc}}{dt} = \dot{Q} - \dot{W} + \dot{m}_1\theta_1 - \dot{m}_2\theta_2,$$
> donde $\theta = h + C^2/2 + gz$.
>
> **Paso 3 — Aplicar $dE_{\rm vc}/dt = 0$.** El miembro izquierdo se anula:
> $$0 = \dot{Q} - \dot{W} + \dot{m}(\theta_1 - \theta_2).$$
>
> **Paso 4 — Despejar $\dot{Q}-\dot{W}$.** Reorganizando:
> $$\dot{Q} - \dot{W} = \dot{m}(\theta_2-\theta_1) = \dot{m}\!\left[(h_2-h_1)+\frac{C_2^2-C_1^2}{2}+g(z_2-z_1)\right].$$
>
> **Paso 5 — Generalización a múltiples corrientes.** Para $n_e$ entradas y $n_s$ salidas con $dm_{\rm vc}/dt=0$:
> $$\dot{Q} - \dot{W} = \sum_e \dot{m}_e\theta_e - \sum_i \dot{m}_i\theta_i.$$
> La conservación de masa impone la restricción adicional $\sum_i\dot{m}_i=\sum_e\dot{m}_e$. $\blacksquare$

---

## Hipótesis habituales por tipo de dispositivo

> [!teoria]
> En la mayoría de los dispositivos se desprecian algunos términos de la SFEE según la física del equipo:
>
> | Término eliminado | Justificación | Dispositivos donde SÍ importa |
> |:---|:---|:---|
> | $\Delta EC = \frac{1}{2}(C_2^2-C_1^2)$ | Velocidades similares en entrada y salida | [[Toberas]], [[Difusores]] |
> | $\Delta EP = g(z_2-z_1)$ | Desnivel < 10 m | Columnas de líquido, bombas hidráulicas |
> | $\dot{Q}=0$ (adiabático) | Aislamiento térmico bueno; proceso rápido | [[Intercambiadores]] (en el lado caliente) |
> | $\dot{W}=0$ (sin eje) | No hay conexión mecánica al exterior | [[Turbinas]], [[Compresores]] |
>
> Balances reducidos para cada dispositivo:
>
> | Dispositivo | Hipótesis extra | Balance simplificado |
> |:---|:---|:---|
> | [[Turbinas]] / [[Compresores]] | $\dot{Q}=0$, $\Delta EC\approx0$, $\Delta EP\approx0$ | $\dot{W} = \dot{m}(h_1-h_2)$ |
> | [[Toberas]] / [[Difusores]] | $\dot{Q}=0$, $\dot{W}=0$, $\Delta EP\approx0$ | $h_1+C_1^2/2 = h_2+C_2^2/2$ |
> | [[Valvulas]] | $\dot{Q}=0$, $\dot{W}=0$, $\Delta EC\approx0$ | $h_2 = h_1$ |
> | [[Intercambiadores]] | $\dot{W}=0$, $\dot{Q}_{\rm ext}=0$, $\Delta EC\approx0$ | $\sum \dot{m}_i h_i = \sum \dot{m}_e h_e$ |

---

## Balance de entropía en flujo estacionario

> [!proposicion]
> Para flujo estacionario con una entrada y una salida, el balance de entropía reduce a:
> $$\dot{S}_{\rm gen} = \dot{m}(s_2-s_1) - \frac{\dot{Q}}{T_b} \geq 0,$$
> donde $T_b$ es la temperatura de la frontera por donde entra el calor. En dispositivos adiabáticos:
> $$\dot{S}_{\rm gen} = \dot{m}(s_2-s_1) \geq 0.$$
>
> Esto implica $s_2 \geq s_1$: la entropía nunca puede disminuir a lo largo de un VC adiabático estacionario. El proceso isentrópico ($s_2=s_1$) es el límite reversible ideal.

---

## Ejemplo: caldera de caldera recuperadora

> [!ejemplo]
> Agua líquida a $P_1=10\,\mathrm{MPa}$, $T_1=30\,°\mathrm{C}$ ($h_1=134.2\,\mathrm{kJ/kg}$) entra a una caldera y sale como vapor sobrecalentado a $P_2=10\,\mathrm{MPa}$, $T_2=550\,°\mathrm{C}$ ($h_2=3500.9\,\mathrm{kJ/kg}$). Caudal $\dot{m}=50\,\mathrm{kg/s}$. Calcular el calor suministrado y la potencia calorífica.

> [!solucion]
> **Paso 1 — Identificar hipótesis.** Caldera: $\dot{W}=0$ (no hay eje), $\Delta EC\approx0$, $\Delta EP\approx0$, $\dot{Q}>0$ (calor entrante).
>
> **Paso 2 — Aplicar SFEE.** Con $\dot{W}=0$:
> $$\dot{Q} = \dot{m}(h_2-h_1) = 50\times(3500.9-134.2) = 50\times3366.7 = 168\,335\,\mathrm{kW} \approx 168.3\,\mathrm{MW}.$$
>
> **Paso 3 — Por unidad de masa.** $q = h_2-h_1 = 3366.7\,\mathrm{kJ/kg}$.
>
> **Paso 4 — Segunda ley.** La caldera no es adiabática, así que no podemos hablar de $\dot{S}_{\rm gen}$ sin conocer la temperatura de los gases de combustión. Pero sí podemos calcular la variación de entropía del agua: $\Delta s = s_2-s_1 = 6.7585-0.4369 = 6.3216\,\mathrm{kJ/(kg\cdot K)}$; $\dot{m}\Delta s = 316.1\,\mathrm{kW/K}$.
>
> **Paso 5 — Razonabilidad.** La diferencia de entalpía de 3366.7 kJ/kg es consistente con pasar de agua a $30°C$ (muy subenfriada) hasta vapor sobrecalentado a 550°C, incluyendo calor sensible del líquido ($\sim170$ kJ/kg), calor latente ($\sim1580$ kJ/kg a 10 MPa), y calor sensible del vapor ($\sim1617$ kJ/kg). La suma da $\approx3367$ kJ/kg ✓.
>
> $\boxed{\dot{Q}=168.3\,\mathrm{MW},\quad q=3366.7\,\mathrm{kJ/kg}.}$ $\blacksquare$

> [!info]
> **Notación:** $\dot{m}$ [kg/s]; $C$ [m/s]; $z$ [m]; $\theta=h+C^2/2+gz$ energía específica de la corriente. Los balances completos no estacionarios están en [[Balance de Energia VC]]. Los dispositivos de flujo individuales se desarrollan en [[Dispositivos Flujo/index | Dispositivos de Flujo]].

> [!referencia]
> Borgnakke & Sonntag, §6.1–§6.2; Çengel & Boles, §5-1; Moran & Shapiro, §4.1–4.2.
