---
title: "Ciclos de Combustión Interna"
order: 2
tags:
  - termodinamica
  - ciclos
  - combustion_interna
  - otto
  - diesel
  - index
draft: false
aliases:
  - Ciclos de Combustión Interna
  - ICE cycles
  - ciclos recíprocos
---

# Ciclos de Combustión Interna

> [!definicion]
> Los **ciclos de combustión interna** modelan los motores de **pistón reciprocante**: el motor de gasolina (Otto) y el motor diésel (Diesel). En estos dispositivos el fluido de trabajo (mezcla aire-combustible o solo aire) cambia de volumen en una cámara cerrada, y la combustión ocurre **dentro** del sistema — a diferencia de las turbinas de gas (Brayton) donde el fluido circula por dispositivos separados.
>
> El análisis estándar usa la **hipótesis aire-estándar con calor específico constante**: se reemplaza la combustión por adición de calor externo, y la purga de gases quemados por rechazo de calor. El fluido es aire ideal con $c_v = 0.718\,\mathrm{kJ/(kg\cdot K)}$ y $\gamma = 1.4$.
>
> *Variable clave:* la **relación de compresión volumétrica** $r = V_1/V_2$, donde $V_1$ es el volumen máximo (PMS, punto muerto superior inferior) y $V_2$ el mínimo (PMI, punto muerto superior). A mayor $r$, mayor eficiencia — pero limitado por la detonación (Otto) o los esfuerzos mecánicos (Diesel).

![[CCI_PV_otto_diesel.svg|480]]
*Diagramas $P$-$v$ del ciclo Otto (izquierda) y Diesel (derecha). En el Otto, la adición de calor es isocórica (volumen constante). En el Diesel, la adición es isobárica (presión constante), lo que permite mayor relación de compresión sin detonación.*

---

## Comparación Otto vs Diesel

| Característica | Otto | Diesel |
|:---|:---:|:---:|
| Motor tipo | Gasolina (encendido por chispa) | Diésel (encendido por compresión) |
| Proceso de adición de calor | Isocórico ($v = \text{cte}$) | Isobárico ($P = \text{cte}$) |
| Relación de compresión típica | $r \approx 8{-}11$ | $r \approx 14{-}22$ |
| Temperatura de ignición | Baja (bujía) | Alta (solo por compresión) |
| Eficiencia (ideal) | $\eta = 1 - r^{-(γ-1)}$ | $\eta = 1 - r^{-(γ-1)}\frac{r_c^\gamma - 1}{\gamma(r_c-1)}$ |
| Variable adicional | — | Relación de corte $r_c = V_3/V_2$ |

---

## Relaciones comunes

> [!proposicion]
> Ambos ciclos tienen **dos procesos isentrópicos** (1→2 compresión, y 3→4 ó 4→1 expansión). Las relaciones de temperatura para los procesos isentrópicos son:
> $$
> \frac{T_2}{T_1} = \left(\frac{V_1}{V_2}\right)^{\gamma-1} = r^{\gamma-1}.
> $$
>
> Con $\gamma = 1.4$ y $r = 8$: $T_2/T_1 = 8^{0.4} = 2.297$ → el aire se comprime de $300\,\mathrm{K}$ a $689\,\mathrm{K}$ (416°C).

---

## Mapa de notas

> [!info]
> - [[Ciclo Otto]] — motor de gasolina; adición isocórica; $\eta = 1-r^{-(γ-1)}$; ejemplo completo con $r=8$.
> - [[Ciclo Diesel]] — motor diésel; adición isobárica; relación de corte $r_c$; ejemplo con $r=18$.

> [!referencia]
> Borgnakke & Sonntag, §13.1–13.3; Çengel & Boles, §9-3 a 9-5; Moran & Shapiro, §9.3–9.4.
