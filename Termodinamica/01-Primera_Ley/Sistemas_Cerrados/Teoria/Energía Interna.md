---
title: Energía Interna
tags:
  - termodinámica
  - primera-ley
  - energía-interna
  - función-estado
  - sistemas-cerrados
  - gases-ideales
draft: true
---

# Energía Interna

> [!abstract] Resumen
> La energía interna $U$ es la energía microscópica total contenida en un sistema termodinámico. Es una [[función de estado]] fundamental que representa la suma de todas las formas de energía asociadas con la estructura molecular y atómica del sistema. Su variación constituye el núcleo de la [[Primera Ley de la Termodinámica]] para [[Sistemas Cerrados|sistemas cerrados]].

---

## Definición Formal

> [!definicion] Energía Interna
> La energía interna $U$ de un sistema termodinámico es la suma de todas las formas de energía microscópica asociadas con sus constituyentes:
> 
> $$
> U = E_{\text{cinética, molecular}} + E_{\text{potencial, intermolecular}} + E_{\text{electrónica}} + E_{\text{nuclear}} + \dots
> $$

### Componentes Incluidos

| Componente | Descripción |
|------------|-------------|
| **Energía cinética molecular** | Traslación, rotación y vibración de moléculas |
| **Energía potencial intermolecular** | Fuerzas de atracción/repulsión entre moléculas |
| **Energía electrónica** | Energía de electrones en orbitales atómicos/moleculares |
| **Energía nuclear** | Energía de enlace nuclear (relevante en procesos nucleares) |

### Componentes Excluidos

> [!info] Energía Macroscópica
> La energía interna **no incluye**:
> - [[Energía cinética]] macroscópica ($\frac{1}{2}mv^2$ del sistema como un todo)
> - [[Energía potencial]] macroscópica ($mgh$ en campos externos)
> 
> Estas se consideran por separado en el balance energético total.

---

## Interpretación Física

> [!teoria] Función de Estado
> La energía interna es una **[[función de estado]]**, lo que implica:
> - Depende únicamente del estado termodinámico actual del sistema
> - Es independiente de la trayectoria o proceso seguido para alcanzar dicho estado
> - Su diferencial $dU$ es una **diferencial exacta**

> [!proposicion] Propiedades Fundamentales
> 1. **Extensiva**: Si se divide el sistema en subsistemas, $U_{\text{total}} = \sum U_i$
> 2. **Aditiva**: Para sistemas no interactuantes, la energía interna total es la suma
> 3. **Monótona con T**: En condiciones normales, $U$ aumenta con la temperatura

---

## Forma Diferencial

Para un proceso infinitesimal en un [[Sistemas Cerrados|sistema cerrado]]:

> [!axioma] Primera Ley en Forma Diferencial
> $$
> dU = \delta Q - \delta W
> $$
> 
> donde:
> - $\delta Q$ = [[calor]] transferido al sistema (infinitesimal)
> - $\delta W$ = [[trabajo termodinámico|trabajo]] realizado por el sistema (infinitesimal)

> [!warning] Diferenciales Exactas vs. Inexactas
> $dU$ es una **diferencial exacta** (depende solo del estado), mientras que $\delta Q$ y $\delta W$ son **diferenciales inexactas** (dependen del proceso). Por ello se usa la notación $\delta$ en lugar de $d$.

---

## Primera Ley de la Termodinámica

> [!teorema] [[Primera Ley de la Termodinámica|Primera Ley]] para Sistema Cerrado
> Para un proceso finito entre dos estados:
> 
> $$
> \Delta U = Q - W
> $$
> 
> donde:
> - $\Delta U = U_2 - U_1$ = cambio de energía interna
> - $Q$ = calor neto transferido al sistema
> - $W$ = trabajo neto realizado por el sistema

### Casos Particulares

| Proceso | Condición | Relación |
|---------|-----------|----------|
| **[[Proceso Adiabatico Reversible\|Adiabático]]** | $Q = 0$ | $\Delta U = -W$ |
| **[[Proceso Isometrico\|Isocórico (volumen constante)]]** | $W = 0$ | $\Delta U = Q_V$ |
| **[[Ciclos Termodinámicos\|Cíclico]]** | $\Delta U = 0$ | $Q = W$ |
| **Aislado** | $Q = 0, W = 0$ | $\Delta U = 0$ |

---

## Dependencia con Variables de Estado

> [!teoria] Variables Naturales
> Para un sistema simple compresible, la energía interna tiene como variables naturales:
> 
> $$
> U = U(S, V, n)
> $$
> 
> donde:
> - $S$ = [[entropía]]
> - $V$ = volumen
> - $n$ = número de moles

### Dependencia en T y v

En términos de variables más prácticas para el ingeniero:

> [!proposicion] Caso General
> Para una **[[Sustancia_Pura|sustancia pura]]**:
> 
> $$
> U = U(T, v)
> $$
> 
> donde $T$ es temperatura y $v$ es volumen específico.

> [!proposicion] [[Gases Ideales|Gas Ideal]]
> Para un **gas ideal**, la energía interna depende **únicamente** de la temperatura:
> 
> $$
> U = U(T) \quad \text{(solo)}
> $$
> 
> Esto se conoce como la **[[Ley de Joule]]** y es consecuencia de que en un gas ideal no existen fuerzas intermoleculares.

---

## Relación con la Temperatura

> [!demostracion] Deducción: [[Calores_Especificos_Gases_Ideales|Calor Específico a Volumen Constante]]
> 
> Por definición, el calor específico a volumen constante es:
> 
> $$
> c_v = \left(\frac{\partial u}{\partial T}\right)_v
> $$
> 
> donde $u = U/m$ es la energía interna específica.
> 
> Para un **gas ideal** ($u$ independiente de $v$):
> 
> $$
> du = c_v(T) \, dT
> $$
> 
> Integrando entre dos estados:
> 
> $$
> \Delta u = \int_{T_1}^{T_2} c_v(T) \, dT
> $$

### Casos Prácticos

> [!example] Gas Ideal con $c_v$ Constante
> Si $c_v$ se considera constante (aproximación válida para gases monoatómicos o para rangos limitados de temperatura):
> 
> $$
> \Delta U = m \, c_v \, (T_2 - T_1)
> $$
> 
> o en términos molares:
> 
> $$
> \Delta U = n \, \bar{c}_v \, (T_2 - T_1)
> $$

> [!example] Sustancia Real
> Para [[Sustancia_Pura|sustancias reales]], se deben utilizar:
> - **[[Tablas Termodinámicas]]** (vapor de agua, refrigerantes)
> - **[[Gases Reales|Ecuaciones de estado]]** (Van der Waals, Redlich-Kwong, etc.)
> - **Diagramas** ($T$-$v$, $P$-$v$, $T$-$s$)

---

## Relación con Otras Propiedades

### [[Entalpía|Entalpía]]

> [!teoria] Relación Fundamental
> La **entalpía** $H$ se define como:
> 
> $$
> H = U + PV
> $$
> 
> Esta relación es crucial porque:
> - En [[Proceso Isobarico|procesos a presión constante]], $Q_P = \Delta H$
> - En [[Flujo_Estacionario_SSP|flujos de fluidos]], la entalpía representa la energía total transportada

### Diferencial Fundamental

> [!lema] Ecuación de Gibbs
> Combinando la [[Primera Ley de la Termodinámica|Primera Ley]] con la definición de [[entropía]]:
> 
> $$
> dU = T \, dS - P \, dV
> $$
> 
> Esta es la **relación fundamental** de la termodinámica, válida para [[Sistemas Cerrados|sistemas cerrados]] en equilibrio.

---

## Casos de Estudio Importantes

### [[Sistemas Cerrados|Sistema Cerrado]] No Reactivo

> [!teoria] Balance Energético
> Para un sistema cerrado que intercambia calor y trabajo con sus alrededores:
> 
> $$
> U_2 - U_1 = Q - W
> $$
> 
> **Convención de signos**:
> - $Q > 0$: calor **entra** al sistema
> - $W > 0$: trabajo **sale** del sistema

### [[Proceso Adiabatico Reversible|Proceso Adiabático Reversible]]

> [!teoria] Relación con Trabajo
> En un proceso adiabático ($Q = 0$):
> 
> $$
> \Delta U = -W
> $$
> 
> Para un **[[Gases Ideales|gas ideal]]** con $c_v$ constante:
> 
> $$
> m c_v (T_2 - T_1) = -W
> $$

### [[Proceso Isometrico|Proceso Isocórico (Volumen Constante)]]

> [!teoria] Calor Medido
> Cuando el volumen es constante ($W = 0$):
> 
> $$
> Q_V = \Delta U
> $$
> 
> Por esta razón, las mediciones de calor en **bombas calorimétricas** (volumen constante) determinan directamente $\Delta U$.

---

## Modelos Útiles

| Modelo | Característica | Aplicación |
|--------|----------------|------------|
| **[[Gases Ideales\|Gas Ideal]]** | $U = U(T)$ independiente de $P$ y $v$ | Gases a baja presión, alta temperatura |
| **Gas Ideal con $c_v$ constante** | $\Delta U = n \bar{c}_v \Delta T$ | Gases monoatómicos, rangos pequeños de T |
| **Sustancia incompresible** | $U \approx U(T)$; $c_v = c_p$ | Líquidos, sólidos |
| **[[Tablas Termodinámicas]]** | $u = u(T, P)$ o $u = u(T, v)$ | Vapor de agua, refrigerantes |

---

## Demostraciones Clave

### Derivación de $dU = m c_v dT$ para [[Gases Ideales|Gas Ideal]]

> [!demostracion] Demostración
> 
> 1. Para un gas ideal, por la [[Ley de Joule]]:
>    $$
>    \left(\frac{\partial u}{\partial v}\right)_T = 0
>    $$
> 
> 2. La diferencial total de $u(T, v)$ es:
>    $$
>    du = \left(\frac{\partial u}{\partial T}\right)_v dT + \left(\frac{\partial u}{\partial v}\right)_T dv
>    $$
> 
> 3. Por definición de $c_v$:
>    $$
>    c_v = \left(\frac{\partial u}{\partial T}\right)_v
>    $$
> 
> 4. Usando (1), el segundo término se anula:
>    $$
>    du = c_v(T) \, dT
>    $$
> 
> 5. Multiplicando por la masa $m$:
>    $$
>    dU = m \, c_v(T) \, dT
>    $$
> 
> $\square$

### Relación entre $c_p$ y $c_v$

> [!demostracion] Relación General
> 
> Para cualquier sustancia:
> 
> $$
> c_p - c_v = T v \frac{\beta^2}{\kappa_T}
> $$
> 
> donde:
> - $\beta = \frac{1}{v} \left(\frac{\partial v}{\partial T}\right)_P$ = coeficiente de expansión térmica
> - $\kappa_T = -\frac{1}{v} \left(\frac{\partial v}{\partial P}\right)_T$ = compresibilidad isoterma
> 
> Para un **[[Gases Ideales|gas ideal]]** ($Pv = RT$):
> 
> $$
> \beta = \frac{1}{T}, \quad \kappa_T = \frac{1}{P}
> $$
> 
> Sustituyendo:
> 
> $$
> c_p - c_v = T v \frac{(1/T)^2}{1/P} = \frac{Pv}{T} = R
> $$
> 
> Es decir:
> 
> $$
> \bar{c}_p - \bar{c}_v = R \quad \text{(base molar)}
> $$
> 
> $\square$

---

## Tabla de Correspondencias

| Concepto | Notación | Unidades (SI) |
|----------|----------|---------------|
| Energía interna (total) | $U$ | J |
| Energía interna específica | $u = U/m$ | J/kg |
| Energía interna molar | $\bar{u} = U/n$ | J/mol |
| [[Calores_Especificos_Gases_Ideales\|Calor específico a volumen constante]] | $c_v$ | J/(kg·K) |
| Calor específico molar a volumen constante | $\bar{c}_v$ | J/(mol·K) |

---

## Ejercicios Propuestos

> [!question] Ejercicio 1
> Un [[Sistemas Cerrados|sistema cerrado]] contiene 2 kg de aire ([[Gases Ideales|gas ideal]], $c_v = 0.718$ kJ/kg·K). El sistema se calienta desde 300 K hasta 500 K a volumen constante. Calcular:
> a) El cambio de energía interna
> b) El calor transferido
> c) El trabajo realizado

<details>
<summary>Solución</summary>

a) $\Delta U = m c_v (T_2 - T_1) = 2 \cdot 0.718 \cdot (500 - 300) = 287.2$ kJ
b) [[Proceso Isometrico|Proceso isocórico]]: $W = 0$, por lo tanto $Q = \Delta U = 287.2$ kJ
c) $W = 0$ (no hay cambio de volumen)
</details>

> [!question] Ejercicio 2
> Demostrar que para un [[Gases Ideales|gas ideal]], la energía interna es independiente del volumen.

<details>
<summary>Solución</summary>

Para un gas ideal, las partículas no interactúan (no hay fuerzas intermoleculares), por lo que la energía potencial intermolecular es cero. La energía interna consiste solo en energía cinética molecular, que depende únicamente de la temperatura según la [[teoría cinética de gases]]: $U = \frac{3}{2} nRT$ para gas monoatómico. Por lo tanto, $\left(\frac{\partial U}{\partial V}\right)_T = 0$.
</details>

> [!question] Ejercicio 3
> Un [[Gases Ideales|gas ideal]] experimenta un [[Proceso Adiabatico Reversible|proceso adiabático reversible]] desde $T_1 = 300$ K hasta $T_2 = 400$ K. Si $m = 1$ kg y $c_v = 0.718$ kJ/kg·K, determinar:
> a) El cambio de energía interna
> b) El trabajo realizado

<details>
<summary>Solución</summary>

a) $\Delta U = m c_v (T_2 - T_1) = 1 \cdot 0.718 \cdot (400 - 300) = 71.8$ kJ
b) Proceso adiabático: $Q = 0$, por lo tanto $\Delta U = -W \Rightarrow W = -\Delta U = -71.8$ kJ
El signo negativo indica que el trabajo es realizado **sobre** el sistema.
</details>

> [!question] Ejercicio 4
> Explica por qué la energía interna es una [[función de estado]] mientras que el [[calor]] y el [[trabajo termodinámico|trabajo]] no lo son.

<details>
<summary>Solución</summary>

La energía interna es una función de estado porque depende únicamente del estado termodinámico actual del sistema (T, P, V, etc.), no de cómo se alcanzó ese estado. En contraste, el calor y el trabajo son formas de transferencia de energía que dependen del camino o proceso seguido. Dos trayectorias diferentes entre los mismos estados inicial y final pueden producir diferentes cantidades de calor y trabajo, pero su diferencia (Q - W) siempre será igual al cambio de energía interna, que es independiente del camino.
</details>

---

## Notas Relacionadas

- [[Primera Ley de la Termodinámica]]
- [[Entalpía]]
- [[Calores_Especificos_Gases_Ideales]]
- [[Sistemas Cerrados]]
- [[Gases Ideales]]
- [[Tablas Termodinámicas]]
- [[Proceso_Isotermico]]
- [[Proceso_Adiabatico_Reversible]]
- [[Proceso Isobarico]]
- [[Proceso Isometrico]]
- [[Entropía]]
- [[Gases Reales]]