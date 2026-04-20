---
title: Gases Ideales
tags:
  - termodinamica
  - gases-ideales
  - ecuacion-estado
  - modelo-termico
  - propiedades-termicas
draft: true
---

# Gases Ideales

> [!abstract] Resumen
> El modelo de gas ideal es una simplificación fundamental en termodinámica que describe el comportamiento de gases a baja presión y alta temperatura. Se caracteriza por la ausencia de interacciones intermoleculares y volumen molecular despreciable, lo que conduce a una ecuación de estado simple $Pv = RT$ y a la independencia de la energía interna y entalpía respecto de la presión y el volumen. Este modelo es la base para el estudio de ciclos de potencia, sistemas de refrigeración y flujo compresible.

---

## Definición Operativa

> [!definicion] Gas Ideal
> Un **gas ideal** es un modelo teórico que cumple con dos hipótesis fundamentales:
> 
> 1. **Interacciones moleculares despreciables**: Las fuerzas de atracción y repulsión entre moléculas son nulas.
> 2. **Volumen molecular despreciable**: El volumen ocupado por las moléculas es insignificante comparado con el volumen total del sistema.
> 
> Estas condiciones se satisfacen en la práctica cuando el gas se encuentra a **baja presión** y **alta temperatura** relativa a su punto crítico.

> [!info] Consecuencia Fundamental
> Bajo estas hipótesis, el estado termodinámico queda completamente definido por una ecuación de estado simple que relaciona presión, volumen específico y temperatura.

---

## Ecuación de Estado

> [!teorema] Ecuación de Estado del Gas Ideal
> 
> $$
> PV = nRT
> $$
> 
> o en forma específica (por unidad de masa):
> 
> $$
> Pv = RT
> $$
> 
> donde:
> - $P$ = presión absoluta (Pa)
> - $V$ = volumen total (m³)
> - $v = V/m$ = volumen específico (m³/kg)
> - $n$ = número de moles (mol)
> - $R$ = constante universal de los gases (8.314 J/(mol·K))
> - $\bar{R} = R/M$ = constante específica del gas (J/(kg·K))
> - $M$ = masa molar (kg/mol)

### Formas Alternativas

| Expresión | Descripción |
|-----------|-------------|
| $P \bar{v} = \bar{R} T$ | Base molar ($\bar{v}$ = volumen molar) |
| $P = \rho R T$ | En términos de densidad $\rho = 1/v$ |
| $PV = mRT$ | Forma más común en problemas |

> [!example] Constantes Específicas para Gases Comunes
> 
> | Gas | Masa molar $M$ (kg/kmol) | Constante específica $R$ (kJ/(kg·K)) |
> |-----|--------------------------|-------------------------------------|
> | Aire | 28.97 | 0.287 |
> | Hidrógeno (H₂) | 2.016 | 4.124 |
> | Nitrógeno (N₂) | 28.01 | 0.297 |
> | Oxígeno (O₂) | 32.00 | 0.260 |
> | Dióxido de carbono (CO₂) | 44.01 | 0.189 |
> | Vapor de agua (H₂O) | 18.02 | 0.461 |

---

## Hipótesis del Modelo y Rango de Validez

> [!teoria] Condiciones de Validez
> El modelo de gas ideal es una buena aproximación cuando:
> 
> 1. **Baja presión**: $P \ll P_{\text{crítico}}$
> 2. **Alta temperatura**: $T \gg T_{\text{crítico}}$
> 3. **Gas diluido**: Baja densidad, gran separación molecular
> 
> En la práctica, se utiliza el [[Factor de Compresibilidad]] $Z = Pv/RT$ para cuantificar la desviación:
> - $Z \approx 1$: comportamiento de gas ideal
> - $Z \neq 1$: se requieren modelos de [[Gases Reales|gas real]]

> [!example] Regla Empírica
> Muchos gases a temperatura ambiente y presión atmosférica ($P \approx 1\ \text{atm}$) se comportan como gases ideales con error < 1%. Excepciones: gases cerca de su punto de condensación (vapor de agua saturado, refrigerantes).

---

## Relaciones Energéticas Fundamentales

> [!teoria] Propiedades Clave
> Para un gas ideal, la [[Energía Interna]] específica $u$ y la [[Entalpía]] específica $h$ dependen **únicamente** de la temperatura:
> 
> $$
> u = u(T) \quad \text{y} \quad h = h(T)
> $$
> 
> Es decir:
> $$
> \left( \frac{\partial u}{\partial v} \right)_T = 0, \quad
> \left( \frac{\partial u}{\partial P} \right)_T = 0
> $$
> $$
> \left( \frac{\partial h}{\partial P} \right)_T = 0, \quad
> \left( \frac{\partial h}{\partial v} \right)_T = 0
> $$

### Consecuencias

| Propiedad | Implicación |
|-----------|-------------|
| $u = u(T)$ | En procesos isotérmicos, $\Delta u = 0$ |
| $h = h(T)$ | En procesos isotérmicos, $\Delta h = 0$ |
| Independencia de $P$ y $v$ | Simplifica cálculos en cambios de estado |

---

## Calores Específicos

> [!definicion] Calores Específicos
> 
> Por definición:
> $$
> c_v = \left( \frac{\partial u}{\partial T} \right)_v, \qquad
> c_p = \left( \frac{\partial h}{\partial T} \right)_p
> $$
> 
> Para un [[Gases Ideales|gas ideal]], dado que $u$ y $h$ dependen solo de $T$, los calores específicos también dependen **solo de la temperatura**:
> 
> $$
> c_v = c_v(T), \qquad c_p = c_p(T)
> $$

### Relación entre $c_p$ y $c_v$

> [!teorema] Relación de Mayer
> 
> $$
> c_p - c_v = R
> $$
> 
> o en forma molar:
> $$
> \bar{c}_p - \bar{c}_v = R_u
> $$
> 
> donde $R_u = 8.314\ \text{J/(mol·K)}$ es la constante universal de los gases.

> [!demostracion] Demostración de $c_p - c_v = R$
> 
> Partimos de la definición de entalpía:
> $$
> h = u + Pv
> $$
> 
> Para un gas ideal: $Pv = RT$
> 
> Derivando respecto a $T$:
> $$
> \frac{dh}{dT} = \frac{du}{dT} + R
> $$
> 
> Por definición:
> $$
> c_p = \frac{dh}{dT}, \quad c_v = \frac{du}{dT}
> $$
> 
> Por lo tanto:
> $$
> c_p = c_v + R \quad \Rightarrow \quad c_p - c_v = R
> $$
> 
> $\square$

---

## Razón de Calores Específicos

> [!definicion] Gamma ($\gamma$)
> $$
> \gamma = \frac{c_p}{c_v}
> $$
> 
> Este parámetro es fundamental en procesos adiabáticos y flujo compresible. Para gases ideales:
> - $\gamma > 1$ siempre
> - Depende de la estructura molecular y la temperatura

### Valores Teóricos para Gases Ideales

| Tipo de Gas | Grados de libertad $f$ | $\bar{c}_v$ | $\bar{c}_p$ | $\gamma$ |
|-------------|----------------------|-------------|-------------|----------|
| Monoatómico (He, Ar) | 3 | $\frac{3}{2}R$ | $\frac{5}{2}R$ | 1.667 |
| Diatómico (N₂, O₂, aire) | 5 | $\frac{5}{2}R$ | $\frac{7}{2}R$ | 1.4 |
| Poliatómico lineal (CO₂) | 7 | $\frac{7}{2}R$ | $\frac{9}{2}R$ | 1.286 |
| Poliatómico no lineal (H₂O, CH₄) | 6 | $3R$ | $4R$ | 1.333 |

> [!warning] Dependencia con la Temperatura
> Los valores anteriores son aproximaciones a baja temperatura (modos vibracionales no activados). A altas temperaturas, los modos vibracionales se activan, aumentando $c_v$, $c_p$ y reduciendo $\gamma$.

---

## Formas Diferenciales Útiles

> [!teoria] Diferenciales Fundamentales
> 
> Para un gas ideal:
> 
> $$
> du = c_v(T) \, dT
> $$
> 
> $$
> dh = c_p(T) \, dT
> $$
> 
> $$
> ds = c_v(T) \frac{dT}{T} + R \frac{dv}{v}
> $$
> 
> $$
> ds = c_p(T) \frac{dT}{T} - R \frac{dP}{P}
> $$

### Caso de Calores Específicos Constantes

Si $c_p$ y $c_v$ se consideran constantes (aproximación válida para rangos limitados de temperatura):

$$
\Delta u = c_v \Delta T
$$

$$
\Delta h = c_p \Delta T
$$

$$
\Delta s = c_v \ln \frac{T_2}{T_1} + R \ln \frac{v_2}{v_1}
$$

$$
\Delta s = c_p \ln \frac{T_2}{T_1} - R \ln \frac{P_2}{P_1}
$$

---

## Procesos con Gas Ideal

> [!teoria] Ecuaciones para Procesos Específicos
> 
> Para un gas ideal con calores específicos constantes:

| Proceso | Ecuación | Relaciones |
|---------|----------|------------|
| **Isotérmico** ($T = \text{cte}$) | $Pv = \text{cte}$ | $\Delta u = 0$, $\Delta h = 0$ |
| **Isobárico** ($P = \text{cte}$) | $v/T = \text{cte}$ | $q = \Delta h = c_p \Delta T$ |
| **Isocórico** ($v = \text{cte}$) | $P/T = \text{cte}$ | $q = \Delta u = c_v \Delta T$ |
| **Adiabático reversible** | $Pv^\gamma = \text{cte}$ | $Tv^{\gamma-1} = \text{cte}$, $TP^{(1-\gamma)/\gamma} = \text{cte}$ |
| **Politrópico** ($n = \text{cte}$) | $Pv^n = \text{cte}$ | $Tv^{n-1} = \text{cte}$, $TP^{(1-n)/n} = \text{cte}$ |

> [!info] Relación entre $\gamma$ y $n$
> En el proceso adiabático reversible, el exponente politrópico $n$ es igual a $\gamma$.

---

## Demostraciones Clave

### 1. Demostración de $u = u(T)$

> [!demostracion] Demostración
> 
> Partimos de la relación fundamental:
> $$
> du = T\,ds - P\,dv
> $$
> 
> Dividiendo por $dv$ a temperatura constante:
> $$
> \left( \frac{\partial u}{\partial v} \right)_T = T \left( \frac{\partial s}{\partial v} \right)_T - P
> $$
> 
> Usando la relación de Maxwell $\left( \frac{\partial s}{\partial v} \right)_T = \left( \frac{\partial P}{\partial T} \right)_v$:
> $$
> \left( \frac{\partial u}{\partial v} \right)_T = T \left( \frac{\partial P}{\partial T} \right)_v - P
> $$
> 
> Para un gas ideal, $P = RT/v$, entonces:
> $$
> \left( \frac{\partial P}{\partial T} \right)_v = \frac{R}{v}
> $$
> 
> Sustituyendo:
> $$
> \left( \frac{\partial u}{\partial v} \right)_T = T \cdot \frac{R}{v} - P = \frac{RT}{v} - P = P - P = 0
> $$
> 
> Por lo tanto, $u$ no depende de $v$ (ni de $P$), solo de $T$:
> $$
> u = u(T)
> $$
> 
> $\square$

### 2. Demostración de $h = h(T)$

> [!demostracion] Demostración
> 
> Por definición, $h = u + Pv$. Para gas ideal, $Pv = RT$, entonces:
> $$
> h = u(T) + RT
> $$
> 
> Como $u$ depende solo de $T$ y $RT$ también, $h$ depende solo de $T$:
> $$
> h = h(T)
> $$
> 
> Alternativamente, partiendo de $dh = T\,ds + v\,dP$ y siguiendo un procedimiento análogo al de $u$:
> $$
> \left( \frac{\partial h}{\partial P} \right)_T = v - T \left( \frac{\partial v}{\partial T} \right)_P
> $$
> 
> Para gas ideal, $v = RT/P$, entonces $\left( \frac{\partial v}{\partial T} \right)_P = R/P$:
> $$
> \left( \frac{\partial h}{\partial P} \right)_T = \frac{RT}{P} - T \cdot \frac{R}{P} = 0
> $$
> 
> $\square$

### 3. Deducción de $ds$ para Gas Ideal

> [!demostracion] Demostración
> 
> Partimos de la relación fundamental $T\,ds = du + P\,dv$:
> $$
> ds = \frac{du}{T} + \frac{P}{T} dv
> $$
> 
> Para gas ideal:
> - $du = c_v(T)\,dT$
> - $P/T = R/v$
> 
> Sustituyendo:
> $$
> ds = c_v(T) \frac{dT}{T} + R \frac{dv}{v}
> $$
> 
> Alternativamente, usando $dh = T\,ds + v\,dP$:
> $$
> ds = \frac{dh}{T} - \frac{v}{T} dP
> $$
> 
> Con $dh = c_p(T)\,dT$ y $v/T = R/P$:
> $$
> ds = c_p(T) \frac{dT}{T} - R \frac{dP}{P}
> $$
> 
> $\square$

### 4. Deducción de la Relación Adiabática Reversible

> [!demostracion] Demostración de $Pv^\gamma = \text{cte}$
> 
> Para un proceso adiabático reversible, $ds = 0$. Usando:
> $$
> ds = c_v \frac{dT}{T} + R \frac{dv}{v} = 0
> $$
> 
> Reordenando:
> $$
> c_v \frac{dT}{T} = -R \frac{dv}{v}
> $$
> 
> Pero $R = c_p - c_v$, entonces:
> $$
> c_v \frac{dT}{T} = -(c_p - c_v) \frac{dv}{v}
> $$
> 
> Dividiendo por $c_v$:
> $$
> \frac{dT}{T} = -(\gamma - 1) \frac{dv}{v}
> $$
> 
> Integrando:
> $$
> \ln T = -(\gamma - 1) \ln v + \text{cte}
> $$
> $$
> T v^{\gamma-1} = \text{cte}
> $$
> 
> Usando $Pv = RT$ para eliminar $T$:
> $$
> \frac{Pv}{R} v^{\gamma-1} = \text{cte} \quad \Rightarrow \quad Pv^\gamma = \text{cte}
> $$
> 
> $\square$

---

## Tabla de Correspondencias

| Concepto | Notación | Relación |
|----------|----------|----------|
| Ecuación de estado | $Pv = RT$ | $P = \rho RT$ |
| Energía interna | $u = u(T)$ | $du = c_v(T)\,dT$ |
| Entalpía | $h = h(T)$ | $dh = c_p(T)\,dT$ |
| Calor específico a $v$ cte. | $c_v(T)$ | $c_p - c_v = R$ |
| Calor específico a $P$ cte. | $c_p(T)$ | $\gamma = c_p/c_v$ |
| Entropía | $ds$ | $c_v\frac{dT}{T} + R\frac{dv}{v}$ |

---

## Ejercicios Propuestos

> [!question] Ejercicio 1
> Un recipiente de 0.5 m³ contiene 2 kg de aire a 300 K. Determine la presión absoluta. ($R_{\text{aire}} = 0.287\ \text{kJ/(kg·K)}$)

<details>
<summary>Solución</summary>

$P = \frac{mRT}{V} = \frac{2 \cdot 0.287 \cdot 300}{0.5} = 344.4\ \text{kPa}$
</details>

> [!question] Ejercicio 2
> Un gas ideal monoatómico ($c_v = 3R/2$) se calienta a volumen constante desde 300 K hasta 500 K. Calcule:
> a) $\Delta u$ (por mol)
> b) $\Delta h$ (por mol)

<details>
<summary>Solución</summary>

a) $\Delta \bar{u} = \bar{c}_v \Delta T = \frac{3}{2}R \cdot 200 = 300R = 2494.2\ \text{J/mol}$
b) $\Delta \bar{h} = \bar{c}_p \Delta T = \frac{5}{2}R \cdot 200 = 500R = 4157\ \text{J/mol}$
</details>

> [!question] Ejercicio 3
> Demuestre que para un proceso adiabático reversible en un gas ideal, $T_2/T_1 = (P_2/P_1)^{(\gamma-1)/\gamma}$.

<details>
<summary>Solución</summary>

De $Pv^\gamma = \text{cte}$ y $Pv = RT$, eliminamos $v$:
$v = RT/P \Rightarrow P \left(\frac{RT}{P}\right)^\gamma = \text{cte} \Rightarrow P^{1-\gamma} T^\gamma = \text{cte}$
Por lo tanto, $P^{1-\gamma} T^\gamma = \text{cte} \Rightarrow T^\gamma \propto P^{\gamma-1} \Rightarrow T \propto P^{(\gamma-1)/\gamma}$
Así: $\frac{T_2}{T_1} = \left(\frac{P_2}{P_1}\right)^{(\gamma-1)/\gamma}$
</details>

> [!question] Ejercicio 4
> Un gas ideal ($c_p = 1.005\ \text{kJ/(kg·K)}$, $R = 0.287\ \text{kJ/(kg·K)}$) experimenta un proceso politrópico con $n = 1.3$ desde $P_1 = 100\ \text{kPa}$, $T_1 = 300\ \text{K}$ hasta $P_2 = 500\ \text{kPa}$. Determine $T_2$.

<details>
<summary>Solución</summary>

Para proceso politrópico: $T_2/T_1 = (P_2/P_1)^{(n-1)/n}$
$T_2 = 300 \cdot (500/100)^{(1.3-1)/1.3} = 300 \cdot 5^{0.3/1.3} = 300 \cdot 5^{0.2308} = 300 \cdot 1.456 = 436.8\ \text{K}$
</details>

> [!question] Ejercicio 5
> Verifique que para un gas ideal diatómico a baja temperatura, $\gamma = 1.4$.

<details>
<summary>Solución</summary>

Para gas diatómico: $\bar{c}_v = \frac{5}{2}R$, $\bar{c}_p = \bar{c}_v + R = \frac{7}{2}R$
$\gamma = \frac{7R/2}{5R/2} = \frac{7}{5} = 1.4$
</details>

---

## Notas Relacionadas

- [[Gases Reales]]
- [[Calores Específicos]]
- [[Factor de Compresibilidad]]
- [[Energía Interna]]
- [[Entalpía]]
- [[Primera Ley de la Termodinámica]]
- [[Proceso Adiabatico Reversible]]
- [[Proceso Politropico]]
- [[Tablas Termodinámicas]]
- [[Teoría cinética de gases]]