---
title: Dispositivos de Flujo
tags:
  - termodinamica
  - dispositivos_flujo
  - formulario
  - examen
draft: false
aliases:
  - cheat sheet dispositivos
  - resumen dispositivos
  - hoja de formulas flujo
---

# Dispositivos de Flujo (Formulario)

> [!info]
> **Hipótesis comunes para TODOS**:
> - [[Flujo Estacionario]] ($dm/dt = 0$, $dE/dt = 0$)
> - Una entrada, una salida (excepto [[Intercambiadores de Calor]] y [[Flash]])
> - Despreciables $\Delta EC$ y $\Delta EP$ (excepto [[Toberas]] y [[Difusores]])
> - Adiabáticos ($\dot{Q} = 0$) excepto [[Intercambiadores de Calor]]

---

## Turbinas

Ver nota: [[Turbinas]]

**Función**: Produce trabajo por expansión de $P_1$ a $P_2$

| Magnitud | Fórmula |
|----------|---------|
| Trabajo | $\dot{W} = \dot{m}(h_1 - h_2)$ |
| Eficiencia isoentrópica | $\eta_t = \dfrac{h_1 - h_2}{h_1 - h_{2s}}$ |
| $2s$ (isentrópico) | $s_{2s} = s_1$, $P_{2s} = P_2$ |
| Gas ideal | $\eta_t \approx \dfrac{T_1 - T_2}{T_1 - T_{2s}}$, $T_{2s} = T_1\left(\dfrac{P_2}{P_1}\right)^{(\gamma-1)/\gamma}$ |
| Destrucción exergía | $\dot{B}_{dest} = \dot{m}(\psi_1 - \psi_2) - \dot{W} = T_0\dot{S}_{gen}$ |

**Rango típico**: $\eta_t = 0.85 - 0.92$

---

## Compresores

Ver nota: [[Compresores]]

**Función**: Consume trabajo para aumentar presión de $P_1$ a $P_2$

| Magnitud | Fórmula |
|----------|---------|
| Trabajo | $\dot{W} = \dot{m}(h_2 - h_1)$ |
| Eficiencia isoentrópica | $\eta_c = \dfrac{h_{2s} - h_1}{h_2 - h_1}$ |
| $2s$ (isentrópico) | $s_{2s} = s_1$, $P_{2s} = P_2$ |
| Gas ideal | $\eta_c \approx \dfrac{T_{2s} - T_1}{T_2 - T_1}$, $T_{2s} = T_1\left(\dfrac{P_2}{P_1}\right)^{(\gamma-1)/\gamma}$ |
| Destrucción exergía | $\dot{B}_{dest} = \dot{W} - \dot{m}(\psi_2 - \psi_1)$ |

**Rango típico**: $\eta_c = 0.80 - 0.88$

---

## Toberas

Ver nota: [[Toberas]]

**Función**: Acelera fluido ($C_2 \gg C_1$), convierte $h$ en $C^2$

| Magnitud | Fórmula |
|----------|---------|
| Energía | $h_1 + \dfrac{C_1^2}{2} = h_2 + \dfrac{C_2^2}{2}$ |
| Velocidad real | $C_2 = \sqrt{C_1^2 + 2(h_1 - h_2)}$ |
| Velocidad isentrópica | $C_{2s} = \sqrt{C_1^2 + 2(h_1 - h_{2s})}$ |
| Eficiencia | $\eta_n = \dfrac{C_2^2}{C_{2s}^2} = \dfrac{h_1 - h_2}{h_1 - h_{2s}}$ |
| Gas ideal ($C_1 \approx 0$) | $C_2 = \sqrt{2c_p(T_1 - T_2)}$, $T_{2s} = T_1(P_2/P_1)^{(\gamma-1)/\gamma}$ |

**Rango típico**: $\eta_n = 0.90 - 0.98$

---

## Difusores

Ver nota: [[Difusores]]

**Función**: Desacelera fluido ($C_1 \gg C_2$), convierte $C^2$ en $P$

| Magnitud | Fórmula |
|----------|---------|
| Energía | $h_1 + \dfrac{C_1^2}{2} = h_2 + \dfrac{C_2^2}{2}$ |
| Aumento entalpía | $h_2 - h_1 = \dfrac{C_1^2 - C_2^2}{2}$ |
| Eficiencia (presión) | $\eta_d = \dfrac{P_2 - P_1}{P_{2s} - P_1}$ |
| Eficiencia (gas ideal) | $\eta_d = \dfrac{h_{2s} - h_1}{h_2 - h_1} \approx \dfrac{T_{2s} - T_1}{T_2 - T_1}$ |
| Incompresible | $P_{2s} = P_1 + \dfrac{\rho}{2}(C_1^2 - C_2^2)$ |

**Rango típico**: $\eta_d = 0.80 - 0.92$

---

## Válvulas

Ver nota: [[Valvulas]]

**Función**: Reduce presión mediante estrangulamiento

| Magnitud | Fórmula |
|----------|---------|
| **Proceso clave** | $\boxed{h_2 = h_1}$ (isentálpico) |
| Generación entropía | $\dot{S}_{gen} = \dot{m}(s_2 - s_1)$ |
| Destrucción exergía | $\dot{B}_{dest} = \dot{m}(\psi_1 - \psi_2) = T_0\dot{S}_{gen}$ |
| Coeficiente Joule-Thomson | $\mu_{JT} = \left(\dfrac{\partial T}{\partial P}\right)_h$ |
| Gas ideal | $\mu_{JT} = 0$ (no cambia $T$) |
| Incompresible | $T_2 - T_1 = -\dfrac{v}{c}(P_2 - P_1)$ (se calienta) |

> [!warning]
> **No existe eficiencia** de primera ley porque no hay producción de trabajo. Solo se evalúa destrucción de exergía.

---

## Intercambiadores de Calor

Ver nota: [[Intercambiadores de Calor]]

**Función**: Transfiere calor entre dos corrientes sin mezcla

| Magnitud | Fórmula |
|----------|---------|
| Balance global | $\dot{Q} = \dot{m}_h(h_{h,ent} - h_{h,sal}) = \dot{m}_c(h_{c,sal} - h_{c,ent})$ |
| Capacidad térmica | $C = \dot{m}c_p$ (sin cambio de fase) |
| Calor máximo | $\dot{Q}_{max} = C_{min}(T_{h,ent} - T_{c,ent})$ |
| Eficiencia | $\varepsilon = \dfrac{\dot{Q}}{\dot{Q}_{max}}$ |
| **Contraflujo** ($C_r < 1$) | $\varepsilon = \dfrac{1 - e^{-NTU(1-C_r)}}{1 - C_r e^{-NTU(1-C_r)}}$ |
| **Contraflujo** ($C_r = 1$) | $\varepsilon = \dfrac{NTU}{1 + NTU}$ |
| **Flujo paralelo** | $\varepsilon = \dfrac{1 - e^{-NTU(1+C_r)}}{1 + C_r}$ |
| NTU | $NTU = \dfrac{UA}{C_{min}}$ |
| Relación capacidades | $C_r = \dfrac{C_{min}}{C_{max}}$ |
| Generación entropía | $\dot{S}_{gen} = \dot{m}_c\Delta s_c + \dot{m}_h\Delta s_h$ |

**Rango típico**: $\varepsilon = 0.60 - 0.95$ según configuración

---

## Flash (Vaporización instantánea)

Ver nota: [[Flash]]

**Función**: Separar líquido en dos fases por caída brusca de presión

| Magnitud | Fórmula |
|----------|---------|
| Balance masa global | $F = L + V$ |
| Balance por componente | $F z_i = L x_i + V y_i$ |
| Equilibrio de fases | $y_i = K_i(T,P) \cdot x_i$ |
| Balance energía (adiabático) | $F h_F = L h_L + V H_V$ |
| Fracción vaporizada | $f = \dfrac{V}{F} = \dfrac{z_i - x_i}{y_i - x_i} = \dfrac{h_F - h_L}{H_V - h_L}$ |

> [!warning]
> **Cálculo iterativo**: $T_{tambor}$ debe cumplir simultáneamente balances y equilibrio.

---

## Tabla Resumen Rápida

| Dispositivo (wikilink) | $\dot{W}$ | $\dot{Q}$ | $\Delta EC$ | Ecuación clave | Eficiencia |
|------------------------|-----------|-----------|-------------|----------------|------------|
| [[Turbinas]] | $+$ (sale) | $0$ | $\approx 0$ | $\dot{W} = \dot{m}(h_1-h_2)$ | $\eta_t = \frac{h_1-h_2}{h_1-h_{2s}}$ |
| [[Compresores]] | $-$ (entra) | $0$ | $\approx 0$ | $\dot{W} = \dot{m}(h_2-h_1)$ | $\eta_c = \frac{h_{2s}-h_1}{h_2-h_1}$ |
| [[Toberas]] | $0$ | $0$ | $\gg 0$ | $h_1 + C_1^2/2 = h_2 + C_2^2/2$ | $\eta_n = C_2^2/C_{2s}^2$ |
| [[Difusores]] | $0$ | $0$ | $\gg 0$ | $h_2 - h_1 = (C_1^2-C_2^2)/2$ | $\eta_d = (P_2-P_1)/(P_{2s}-P_1)$ |
| [[Valvulas]] | $0$ | $0$ | $\approx 0$ | $\boxed{h_2 = h_1}$ | No aplica |
| [[Intercambiadores de Calor]] | $0$ | $\neq 0$ | $\approx 0$ | $\dot{Q} = \dot{m}_h\Delta h_h = \dot{m}_c\Delta h_c$ | $\varepsilon = \dot{Q}/\dot{Q}_{max}$ |
| [[Flash]] | $0$ | $0$ | $\approx 0$ | $F = L + V$, $Fz_i = Lx_i + Vy_i$ | No aplica |

> [!info]
> **Convención de signos para $\dot{W}$** (en esta tabla):
> - $+$ (sale): trabajo producido por el dispositivo
> - $-$ (entra): trabajo consumido por el dispositivo
> - $0$: no hay intercambio de trabajo