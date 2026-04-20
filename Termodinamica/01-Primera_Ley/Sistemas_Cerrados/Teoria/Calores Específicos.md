---
title: Calores Específicos
tags:
  - termodinamica
  - calores-especificos
  - propiedades-termicas
  - gases-ideales
  - sustancias-puras
  - funciones-estado
draft: true
---

# Calores Específicos

> [!abstract] Resumen
> Los calores específicos $c_p$ y $c_v$ son propiedades termodinámicas fundamentales que cuantifican la capacidad de una sustancia para almacenar energía térmica. Representan la energía necesaria para aumentar la temperatura de una unidad de masa en un grado, ya sea a presión constante ($c_p$) o a volumen constante ($c_v$). Su diferencia está íntimamente ligada al comportamiento de la materia y su ecuación de estado, y su razón $\gamma = c_p/c_v$ es un parámetro clave en procesos isentrópicos, flujo compresible y ondas de choque.

---

## Definición Formal

> [!definicion] Calor Específico
> El calor específico $c$ de una sustancia es la cantidad de energía necesaria para elevar la temperatura de una unidad de masa en una unidad de temperatura:
> 
> $$
> c = \frac{1}{m} \frac{\delta Q}{dT} = \frac{\delta q}{dT}
> $$
> 
> donde $q = Q/m$ es el **calor específico transferido** (energía por unidad de masa). Dado que $\delta q$ depende del proceso, existen distintos calores específicos según la restricción impuesta durante el calentamiento.

### Formas de Representación

| Forma | Notación | Definición | Relación | Unidades (SI) |
|-------|----------|------------|----------|---------------|
| **Extensiva** | $C$ | $C = m c$ | Capacidad calorífica | J/K |
| **Específica** | $c$ | $c = C/m$ | Por unidad de masa | J/(kg·K) |
| **Molar** | $\bar{c}$ | $\bar{c} = C/n$ | Por unidad de mol | J/(mol·K) |

> [!info] Convención de Notación
> A lo largo de esta nota se seguirá la convención estándar:
> - **Mayúsculas**: propiedades extensivas ($U$, $H$, $Q$, $W$, $S$, $V$, $m$, $n$)
> - **Minúsculas**: propiedades específicas ($u = U/m$, $h = H/m$, $q = Q/m$, $w = W/m$, $s = S/m$, $v = V/m$)

---

## Tipos de Calores Específicos

### A Volumen Constante ($c_v$)

> [!definicion] Calor Específico a Volumen Constante
> $$
> c_v = \left( \frac{\partial u}{\partial T} \right)_v
> $$
> 
> **Interpretación**: Energía necesaria para aumentar la temperatura de una unidad de masa en una unidad manteniendo el volumen constante. En este caso, **no hay trabajo de expansión** ($\delta w = 0$), por lo que todo el calor se convierte en aumento de la energía interna específica:
> 
> $$
> \delta q_v = du \quad \Rightarrow \quad c_v = \frac{\delta q_v}{dT}
> $$

**Aplicaciones típicas**:
- Sistemas cerrados con paredes rígidas
- Bombas calorimétricas
- Análisis de motores de combustión interna (carrera de compresión)

---

### A Presión Constante ($c_p$)

> [!definicion] Calor Específico a Presión Constante
> $$
> c_p = \left( \frac{\partial h}{\partial T} \right)_p
> $$
> 
> **Interpretación**: Energía necesaria para aumentar la temperatura de una unidad de masa en una unidad manteniendo la presión constante. En este caso, parte del calor se usa para aumentar la energía interna específica, y otra parte para realizar **trabajo de expansión** contra la presión externa:
> 
> $$
> \delta q_p = dh \quad \Rightarrow \quad c_p = \frac{\delta q_p}{dT}
> $$

**Aplicaciones típicas**:
- Procesos industriales a presión atmosférica
- Intercambiadores de calor
- Calderas y condensadores
- Análisis de flujo en sistemas abiertos

> [!info] Importancia Práctica
> La mayoría de los procesos reales ocurren a presión constante (o aproximadamente constante), lo que hace que $c_p$ sea el calor específico más utilizado en ingeniería.

---

## Relación entre $c_p$ y $c_v$

### Expresión General

> [!teorema] Diferencia Fundamental
> Para cualquier sustancia compresible simple:
> 
> $$
> c_p - c_v = T v \frac{\beta^2}{\kappa_T}
> $$
> 
> donde:
> - $\beta = \frac{1}{v} \left( \frac{\partial v}{\partial T} \right)_p$ = coeficiente de expansión térmica
> - $\kappa_T = -\frac{1}{v} \left( \frac{\partial v}{\partial P} \right)_T$ = compresibilidad isoterma

> [!demostracion] Demostración de $c_p - c_v$
> 
> Partimos de $h = u + Pv$ y diferenciamos:
> $$
> dh = du + P\,dv + v\,dP
> $$
> 
> Pero $du = c_v\,dT + \left( \frac{\partial u}{\partial v} \right)_T dv$
> 
> Usando la relación termodinámica $\left( \frac{\partial u}{\partial v} \right)_T = T \left( \frac{\partial P}{\partial T} \right)_v - P$:
> 
> $$
> dh = c_v\,dT + \left[ T \left( \frac{\partial P}{\partial T} \right)_v - P \right] dv + P\,dv + v\,dP
> $$
> 
> Simplificando:
> $$
> dh = c_v\,dT + T \left( \frac{\partial P}{\partial T} \right)_v dv + v\,dP
> $$
> 
> Por otro lado, $dh = c_p\,dT + \left( \frac{\partial h}{\partial P} \right)_T dP$
> 
> Igualando y usando relaciones de Maxwell, se obtiene:
> $$
> c_p - c_v = T \left( \frac{\partial P}{\partial T} \right)_v \left( \frac{\partial v}{\partial T} \right)_p
> $$
> 
> Finalmente, usando la identidad cíclica y las definiciones de $\beta$ y $\kappa_T$:
> $$
> c_p - c_v = T v \frac{\beta^2}{\kappa_T}
> $$
> 
> $\square$

### Razón de Calores Específicos

> [!definicion] Gamma ($\gamma$)
> $$
> \gamma = \frac{c_p}{c_v}
> $$
> 
> Este parámetro es **fundamental** en:
> - Procesos isentrópicos: $Pv^\gamma = \text{constante}$
> - Flujo compresible: número de Mach, ondas de choque
> - Velocidad del sonido: $c = \sqrt{\gamma R T}$

> [!proposicion] Propiedades de $\gamma$
> - Siempre $\gamma > 1$ (pues $c_p > c_v$)
> - Para gases ideales, $\gamma$ depende de la estructura molecular
> - En líquidos y sólidos, $\gamma \approx 1$ (pero el concepto pierde relevancia práctica)

---

## Modelos por Tipo de Sustancia

### 1. Gas Ideal

> [!teoria] Características
> Para un [[Gases Ideales|gas ideal]]:
> 1. **Dependencia solo de temperatura**: $c_p = c_p(T)$, $c_v = c_v(T)$
> 2. **Relación exacta**: $c_p - c_v = R$ (base molar)
> 3. **Comportamiento**: $c_p$ y $c_v$ aumentan con $T$ (excepto gases monoatómicos)

#### Gases Monoatómicos

| Gas | $\bar{c}_v$ | $\bar{c}_p$ | $\gamma$ |
|-----|-------------|-------------|----------|
| He, Ne, Ar, Kr, Xe | $\frac{3}{2}R$ | $\frac{5}{2}R$ | $1.667$ |

**Fundamento**: Solo grados de libertad traslacionales (3).

#### Gases Diatómicos (temperatura ambiente)

| Gas | $\bar{c}_v$ | $\bar{c}_p$ | $\gamma$ |
|-----|-------------|-------------|----------|
| H₂, N₂, O₂, CO, aire | $\frac{5}{2}R$ | $\frac{7}{2}R$ | $1.4$ |

**Fundamento**: 3 traslacionales + 2 rotacionales (vibración no activada).

#### Gases Poliatómicos (lineales)

| Tipo | $\bar{c}_v$ | $\bar{c}_p$ | $\gamma$ |
|------|-------------|-------------|----------|
| CO₂ (lineal) | $\frac{7}{2}R$ | $\frac{9}{2}R$ | $1.286$ |

**Fundamento**: 3 traslacionales + 2 rotacionales + 2 vibracionales (aprox.)

#### Gases Poliatómicos (no lineales)

| Tipo | $\bar{c}_v$ | $\bar{c}_p$ | $\gamma$ |
|------|-------------|-------------|----------|
| H₂O, CH₄, NH₃ | $3R$ | $4R$ | $1.333$ |

**Fundamento**: 3 traslacionales + 3 rotacionales + modos vibracionales.

> [!warning] Dependencia con la Temperatura
> A altas temperaturas, los modos vibracionales se activan, aumentando los calores específicos y reduciendo $\gamma$. Por ejemplo, el aire:
> - $T \approx 300\ \text{K}$: $\gamma = 1.4$
> - $T \approx 1000\ \text{K}$: $\gamma \approx 1.3$
> - $T \approx 2000\ \text{K}$: $\gamma \approx 1.2$

#### Modelos de $c_p(T)$ para Gases Ideales

> [!example] Aire (gas ideal, modelo polinomial)
> $$
> \frac{c_p}{R} = a + bT + cT^2 + dT^3
> $$
> 
> Valores típicos (rangos limitados):
> - $300\ \text{K} < T < 600\ \text{K}$: $c_p \approx 1.005\ \text{kJ/(kg·K)}$ (constante)
> - $600\ \text{K} < T < 1500\ \text{K}$: $c_p \approx 1.1\ \text{kJ/(kg·K)}$

---

### 2. Gases Reales

> [!teoria] Desviaciones del Comportamiento Ideal
> Para [[Gases Reales|gases reales]], los calores específicos dependen de **presión y temperatura**:
> 
> $$
> c_p = c_p(T, P), \quad c_v = c_v(T, v)
> $$
> 
> La diferencia $c_p - c_v$ sigue la expresión general, pero ahora $\beta$ y $\kappa_T$ se calculan con la ecuación de estado real.

#### Correcciones para Gases Reales

> [!proposicion] Relación General para Gases Reales
> Usando el factor de compresibilidad $Z = Pv/RT$:
> 
> $$
> c_p - c_v = R \left[ 1 + \frac{T}{Z} \left( \frac{\partial Z}{\partial T} \right)_P^2 \left( \frac{\partial Z}{\partial P} \right)_T^{-1} \right]
> $$
> 
> En el límite de gas ideal ($Z=1$), recuperamos $c_p - c_v = R$.

> [!example] Aplicación con Ecuación de Van der Waals
> Para la ecuación $\left(P + \frac{a}{v^2}\right)(v - b) = RT$, se puede demostrar:
> 
> $$
> c_p - c_v = \frac{R}{1 - \frac{2a(v-b)^2}{RTv^3}}
> $$
> 
> Notar que $c_p - c_v > R$ debido a las fuerzas intermoleculares.

---

### 3. Líquidos

> [!teoria] Características de Líquidos
> En [[Sustancia_Pura|líquidos]], la diferencia $c_p - c_v$ es **muy pequeña** pero no nula:
> 
> - Para agua a $20^\circ\text{C}$: $c_p = 4.18\ \text{kJ/(kg·K)}$, $c_v \approx 4.12\ \text{kJ/(kg·K)}$
> - Diferencia: $c_p - c_v \approx 0.06\ \text{kJ/(kg·K)} \ll R \approx 0.461\ \text{kJ/(kg·K)}$
> 
> La razón $\gamma = c_p/c_v$ es cercana a 1 (agua: $\gamma \approx 1.015$).

#### Modelo de Líquido Incompresible

> [!definicion] Aproximación de Incompresibilidad
> Para muchos líquidos (y sólidos), se usa la aproximación:
> 
> $$
> c_p \approx c_v \approx c
> $$
> 
> Y además:
> $$
> du = c\,dT, \quad dh = c\,dT + v\,dP
> $$
> 
> Esta aproximación es válida cuando $\beta$ y $\kappa_T$ son pequeños, lo cual ocurre en líquidos lejos del punto crítico.

---

### 4. Sólidos

> [!teoria] Capacidad Calorífica de Sólidos
> En sólidos cristalinos, los calores específicos siguen leyes características:

#### Ley de Dulong-Petit (altas temperaturas)

> [!teoria] Modelo Clásico
> Para $T > \Theta_D$ (temperatura de Debye):
> $$
> \bar{c}_v \approx 3R \approx 25\ \text{J/(mol·K)}
> $$
> 
> Es decir, $c \approx 3R/M$, donde $M$ es la masa molar.

#### Modelo de Debye (bajas temperaturas)

> [!teoria] Comportamiento Cuántico
> A bajas temperaturas ($T \ll \Theta_D$):
> $$
> \bar{c}_v \propto T^3
> $$
> 
> Esta es una predicción clave de la mecánica cuántica y fue un éxito temprano del modelo de Debye.

#### Relación $c_p - c_v$ en Sólidos

> [!proposicion] Diferencia Pequeña
> En sólidos, la diferencia es aún menor que en líquidos:
> 
> $$
> c_p - c_v = \frac{9\alpha^2 V T}{\kappa_T}
> $$
> 
> Para la mayoría de los sólidos a temperatura ambiente:
> - $c_p \approx c_v$ (diferencia < 5%)
> - $\gamma \approx 1.0$ a $1.1$

> [!example] Ejemplos de Sólidos
> 
> | Material | $c_p$ (J/kg·K) | $\gamma$ (aprox.) |
> |----------|----------------|-------------------|
> | Cobre (Cu) | 385 | 1.02 |
> | Aluminio (Al) | 900 | 1.02 |
> | Hierro (Fe) | 450 | 1.01 |
> | Concreto | 880 | ~1.00 |

---

## Comparativa entre Modelos

| Modelo | $c_p - c_v$ | Dependencia | $\gamma$ típico |
|--------|-------------|-------------|-----------------|
| **Gas ideal monoatómico** | $R$ | $\bar{c}_v = \frac{3}{2}R$ | 1.667 |
| **Gas ideal diatómico** | $R$ | $\bar{c}_v = \frac{5}{2}R$ | 1.4 |
| **Gas real (Van der Waals)** | $> R$ | $c_p(T,P)$, $c_v(T,v)$ | Variable |
| **Líquido** | $c_p - c_v \ll R$ | $c(T,P)$ | ~1.0–1.1 |
| **Sólido (Dulong-Petit)** | $c_p \approx c_v$ | $\bar{c}_v \approx 3R$ | ~1.0–1.1 |
| **Sólido (Debye, $T \ll \Theta_D$)** | $c_p \approx c_v$ | $\bar{c}_v \propto T^3$ | ~1.0 |

---

## Relación con Energía Interna y Entalpía

> [!teoria] Formas Diferenciales Fundamentales
> 
> Para cualquier sustancia:
> $$
> du = c_v\,dT + \left[ T \left( \frac{\partial P}{\partial T} \right)_v - P \right] dv
> $$
> 
> $$
> dh = c_p\,dT + \left[ v - T \left( \frac{\partial v}{\partial T} \right)_P \right] dP
> $$

### Casos Especiales

> [!example] Gas Ideal
> $$
> du = c_v(T)\,dT, \quad dh = c_p(T)\,dT
> $$

> [!example] Líquido/Sólido Incompresible
> $$
> du = c\,dT, \quad dh = c\,dT + v\,dP
> $$

---

## Demostraciones Clave

### 1. Derivación de $c_p - c_v$ a partir de la Entropía

> [!demostracion] Demostración Alternativa
> 
> Partimos de $s = s(T, v)$:
> $$
> ds = \left( \frac{\partial s}{\partial T} \right)_v dT + \left( \frac{\partial s}{\partial v} \right)_T dv
> $$
> 
> Por definición, $T \left( \frac{\partial s}{\partial T} \right)_v = c_v$, y usando Maxwell: $\left( \frac{\partial s}{\partial v} \right)_T = \left( \frac{\partial P}{\partial T} \right)_v$
> 
> Así:
> $$
> T\,ds = c_v\,dT + T \left( \frac{\partial P}{\partial T} \right)_v dv
> $$
> 
> Ahora, $s = s(T, P)$:
> $$
> ds = \left( \frac{\partial s}{\partial T} \right)_P dT + \left( \frac{\partial s}{\partial P} \right)_T dP
> $$
> 
> Por definición, $T \left( \frac{\partial s}{\partial T} \right)_P = c_p$, y usando Maxwell: $\left( \frac{\partial s}{\partial P} \right)_T = -\left( \frac{\partial v}{\partial T} \right)_P$
> 
> Así:
> $$
> T\,ds = c_p\,dT - T \left( \frac{\partial v}{\partial T} \right)_P dP
> $$
> 
> Igualando ambas expresiones:
> $$
> c_v\,dT + T \left( \frac{\partial P}{\partial T} \right)_v dv = c_p\,dT - T \left( \frac{\partial v}{\partial T} \right)_P dP
> $$
> 
> Despejando $c_p - c_v$ y usando la identidad cíclica:
> $$
> c_p - c_v = T \left( \frac{\partial P}{\partial T} \right)_v \left( \frac{\partial v}{\partial T} \right)_P
> $$
> 
> $\square$

### 2. Límite $c_p - c_v \to 0$ en Líquidos y Sólidos

> [!demostracion] Demostración
> 
> De la expresión general:
> $$
> c_p - c_v = T v \frac{\beta^2}{\kappa_T}
> $$
> 
> En líquidos y sólidos:
> - $\beta$ es pequeño (baja expansividad térmica)
> - $\kappa_T$ es muy pequeño (alta incompresibilidad)
> 
> Sin embargo, $\beta^2 \propto \kappa_T$ cerca del punto triple, resultando en una diferencia pequeña pero finita. En el límite de incompresibilidad perfecta ($\kappa_T \to 0$), la expresión es indeterminada, pero físicamente la diferencia tiende a cero.
> 
> $\square$

### 3. Demostración de $c_p - c_v = R$ para Gas Ideal

> [!demostracion] Demostración
> 
> Para [[Gases Ideales|gas ideal]]: $Pv = RT$
> 
> Calculamos $\beta = \frac{1}{v} \left( \frac{\partial v}{\partial T} \right)_P = \frac{1}{v} \cdot \frac{R}{P} = \frac{1}{T}$
> 
> Calculamos $\kappa_T = -\frac{1}{v} \left( \frac{\partial v}{\partial P} \right)_T = -\frac{1}{v} \cdot \left( -\frac{RT}{P^2} \right) = \frac{1}{P}$
> 
> Sustituyendo:
> $$
> c_p - c_v = T v \frac{(1/T)^2}{1/P} = T v \frac{1}{T^2} P = \frac{Pv}{T} = R
> $$
> 
> $\square$

---

## Tabla de Correspondencias

| Concepto | Notación (Extensiva) | Notación (Específica) | Notación (Molar) |
|----------|---------------------|----------------------|------------------|
| Calor específico a $v$ cte. | $C_v$ | $c_v$ | $\bar{c}_v$ |
| Calor específico a $P$ cte. | $C_p$ | $c_p$ | $\bar{c}_p$ |
| Razón de calores específicos | - | $\gamma = c_p/c_v$ | $\gamma = \bar{c}_p/\bar{c}_v$ |
| Diferencia (gas ideal) | - | $c_p - c_v = R$ | $\bar{c}_p - \bar{c}_v = R$ |
| Capacidad calorífica | $C$ | $c = C/m$ | $\bar{c} = C/n$ |

---

## Ejercicios Propuestos

> [!question] Ejercicio 1
> Un gas ideal diatómico ($\gamma = 1.4$) tiene $c_p = 1.005\ \text{kJ/(kg·K)}$ a temperatura ambiente. Determine:
> a) $c_v$
> b) $R$ (constante específica del gas)

<details>
<summary>Solución</summary>

a) $c_v = c_p / \gamma = 1.005 / 1.4 = 0.718\ \text{kJ/(kg·K)}$
b) $R = c_p - c_v = 1.005 - 0.718 = 0.287\ \text{kJ/(kg·K)}$
</details>

> [!question] Ejercicio 2
> Verifique que para un gas ideal monoatómico, $\gamma = 5/3$.

<details>
<summary>Solución</summary>

Para gas monoatómico: $\bar{c}_v = \frac{3}{2}R$, $\bar{c}_p = \bar{c}_v + R = \frac{5}{2}R$
$\gamma = \frac{5R/2}{3R/2} = \frac{5}{3} \approx 1.667$
</details>

> [!question] Ejercicio 3
> El agua a $20^\circ\text{C}$ tiene $\beta = 2.07 \times 10^{-4}\ \text{K}^{-1}$, $\kappa_T = 4.59 \times 10^{-10}\ \text{Pa}^{-1}$, $v = 0.001\ \text{m}^3/\text{kg}$. Calcule $c_p - c_v$ y compárelo con $R$ del vapor de agua ($R = 0.461\ \text{kJ/(kg·K)}$).

<details>
<summary>Solución</summary>

$c_p - c_v = T v \frac{\beta^2}{\kappa_T} = (293)(0.001) \frac{(2.07 \times 10^{-4})^2}{4.59 \times 10^{-10}}$
$= 0.293 \cdot \frac{4.285 \times 10^{-8}}{4.59 \times 10^{-10}} = 0.293 \cdot 93.35 = 27.35\ \text{J/(kg·K)} = 0.027\ \text{kJ/(kg·K)}$
Comparado con $R = 0.461\ \text{kJ/(kg·K)}$, la diferencia es ~17 veces menor.
</details>

> [!question] Ejercicio 4
> Un bloque de cobre ($c_p = 385\ \text{J/(kg·K)}$, $M = 63.5\ \text{g/mol}$) se calienta desde $20^\circ\text{C}$ hasta $100^\circ\text{C}$. Calcule:
> a) El cambio de energía interna específica (suponiendo $c_v \approx c_p$)
> b) La capacidad calorífica molar según Dulong-Petit

<details>
<summary>Solución</summary>

a) $\Delta u \approx c \Delta T = 385 \cdot 80 = 30,800\ \text{J/kg} = 30.8\ \text{kJ/kg}$
b) Dulong-Petit: $\bar{c}_v \approx 3R = 3 \cdot 8.314 = 24.94\ \text{J/(mol·K)}$
Valor experimental: $\bar{c}_p(\text{Cu}) \approx 24.4\ \text{J/(mol·K)}$ (buena aproximación)
</details>

> [!question] Ejercicio 5
> Demuestre que para un gas ideal, $\gamma$ está relacionado con los grados de libertad $f$ mediante $\gamma = 1 + 2/f$.

<details>
<summary>Solución</summary>

Para un gas ideal, $\bar{c}_v = \frac{f}{2}R$ (teorema de equipartición)
$\bar{c}_p = \bar{c}_v + R = \frac{f}{2}R + R = \frac{f+2}{2}R$
$\gamma = \frac{\bar{c}_p}{\bar{c}_v} = \frac{(f+2)/2}{f/2} = \frac{f+2}{f} = 1 + \frac{2}{f}$
</details>

---

## Notas Relacionadas

- [[Gases Ideales]]
- [[Gases Reales]]
- [[Energía Interna]]
- [[Entalpía]]
- [[Primera Ley de la Termodinámica]]
- [[Proceso Adiabatico Reversible]]
- [[Sustancia_Pura]]
- [[Tablas Termodinámicas]]
- [[Teoría cinética de gases]]
- [[Equipartición de la energía]]
- [[Modelo de Debye]]
- [[Ley de Dulong-Petit]]