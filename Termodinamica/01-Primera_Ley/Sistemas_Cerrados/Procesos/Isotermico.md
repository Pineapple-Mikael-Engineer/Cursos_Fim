---
title: Proceso Isotérmico
tags:
  - termodinamica
  - procesos-termodinamicos
  - temperatura-constante
  - trabajo-termico
  - gases-ideales
  - gases-reales
draft: true
---

# Proceso Isotérmico

> [!abstract] Resumen
> Un **proceso isotérmico** es una transformación termodinámica en la que la temperatura $T$ permanece constante. Es una restricción cinemática aplicable a cualquier sustancia, pero sus consecuencias energéticas (trabajo, calor, cambio de energía interna) dependen fuertemente del modelo termodinámico utilizado. En [[Gases Ideales]] el proceso se simplifica notablemente ($\Delta u = 0$), mientras que en [[Gases Reales]] o sustancias generales aparecen contribuciones adicionales.

---

## Definición General

> [!definicion] Proceso Isotérmico
> Un proceso isotérmico satisface:
> 
> $$
> T = \text{constante} \quad \Rightarrow \quad dT = 0
> $$

Esta condición es **independiente** de:
- el tipo de sustancia
- la ecuación de estado
- la reversibilidad del proceso

> [!info] Reversibilidad
> Aunque la condición $T = \text{cte}$ puede darse en procesos irreversibles (ej: un sistema en contacto con un termostato), el análisis matemático del trabajo suele asumir **cuasiestaticidad** para poder escribir $W = \int P \, dv$.

---

## Formulación General

Para un proceso cuasiestático, el trabajo específico está dado por:

$$
w = \int_{v_i}^{v_f} P \, dv
$$

En un proceso isotérmico, la presión es función solo del volumen específico a temperatura fija:

$$
P = P(T, v) \quad \xrightarrow{T=\text{cte}} \quad P = P(v)
$$

Por lo tanto:

$$
w = \int_{v_i}^{v_f} P(v) \, dv
$$

---

## Relación con la Primera Ley

La [[Primera Ley de la Termodinámica]] para un sistema cerrado, en forma específica:

$$
\Delta u = q - w
$$

Para cualquier sustancia, la energía interna específica depende de $T$ y $v$:

$$
u = u(T, v) \quad \Rightarrow \quad du = \left( \frac{\partial u}{\partial T} \right)_v dT + \left( \frac{\partial u}{\partial v} \right)_T dv
$$

En un proceso isotérmico ($dT = 0$):

$$
du = \left( \frac{\partial u}{\partial v} \right)_T dv
$$

Por lo tanto:

$$
\Delta u = \int_{v_i}^{v_f} \left( \frac{\partial u}{\partial v} \right)_T dv
$$

> [!warning] Conclusión Clave
> **En general, $\Delta u \neq 0$ en un proceso isotérmico**. La creencia común de que "isotérmico implica $\Delta u = 0$" es **solo válida para el [[Gases Ideales|gas ideal]]** (y aproximadamente para sólidos/líquidos incompresibles).

---

## Modelo 1: Gas Ideal

> [!teoria] Comportamiento Isotérmico en [[Gases Ideales]]
> 
> Ecuación de estado:
> $$
> Pv = RT \quad \Rightarrow \quad P = \frac{RT}{v}
> $$
> 
> Con $T = \text{cte}$:
> $$
> P(v) = \frac{\text{constante}}{v} \quad \text{(hipérbola rectangular)}
> $$

### Trabajo Específico

$$
w = \int_{v_i}^{v_f} \frac{RT}{v} dv = RT \ln\left(\frac{v_f}{v_i}\right) = RT \ln\left(\frac{P_i}{P_f}\right)
$$

### Energía Interna y Calor

Para un gas ideal, $u = u(T)$, por lo tanto:

$$
\Delta u = 0
$$

De la primera ley:

$$
q = \Delta u + w = w = RT \ln\left(\frac{v_f}{v_i}\right)
$$

> [!example] Interpretación
> En un gas ideal, todo el calor absorbido se convierte íntegramente en trabajo (expansión) o viceversa (compresión).

---

## Modelo 2: Gas Real (Ejemplo: Van der Waals)

> [!teoria] Comportamiento Isotérmico en [[Gases Reales]]
> 
> Ecuación de Van der Waals:
> $$
> \left(P + \frac{a}{v^2}\right)(v - b) = RT
> $$
> 
> Despejando $P$ a $T$ constante:
> $$
> P = \frac{RT}{v - b} - \frac{a}{v^2}
> $$

### Trabajo Específico

$$
w = \int_{v_i}^{v_f} \left( \frac{RT}{v - b} - \frac{a}{v^2} \right) dv
$$

Integrando:

$$
w = RT \ln\left(\frac{v_f - b}{v_i - b}\right) + a \left( \frac{1}{v_f} - \frac{1}{v_i} \right)
$$

### Energía Interna

Para un gas de Van der Waals, se puede demostrar:

$$
\left( \frac{\partial u}{\partial v} \right)_T = \frac{a}{v^2}
$$

Por lo tanto:

$$
\Delta u = \int_{v_i}^{v_f} \frac{a}{v^2} dv = a \left( \frac{1}{v_i} - \frac{1}{v_f} \right)
$$

### Calor

De la primera ley:

$$
q = \Delta u + w = \underbrace{a \left( \frac{1}{v_i} - \frac{1}{v_f} \right)}_{\Delta u} + \underbrace{RT \ln\left(\frac{v_f - b}{v_i - b}\right) + a \left( \frac{1}{v_f} - \frac{1}{v_i} \right)}_{w}
$$

Simplificando:

$$
q = RT \ln\left(\frac{v_f - b}{v_i - b}\right)
$$

> [!note] Observación
> El término $a$ se cancela en $q$ pero no en $w$ ni $\Delta u$. El calor isotérmico en un gas real **no** es simplemente $RT\ln(v_f/v_i)$, sino que incorpora la corrección de volumen $b$.

---

## Modelo 3: Relación General desde la Termodinámica

> [!teoria] Expresión General para $(\partial u/\partial v)_T$
> 
> Usando la identidad termodinámica (deducida de $du = Tds - Pdv$ y Maxwell):
> $$
> \left( \frac{\partial u}{\partial v} \right)_T = T \left( \frac{\partial P}{\partial T} \right)_v - P
> $$

Por lo tanto, para un proceso isotérmico:

$$
du = \left[ T \left( \frac{\partial P}{\partial T} \right)_v - P \right] dv
$$

Integrando:

$$
\Delta u = \int_{v_i}^{v_f} \left[ T \left( \frac{\partial P}{\partial T} \right)_v - P \right] dv
$$

Y el trabajo:

$$
w = \int_{v_i}^{v_f} P \, dv
$$

El calor se obtiene de $q = \Delta u + w$.

> [!info] Caso particular
> Para un gas ideal: $\left( \frac{\partial P}{\partial T} \right)_v = \frac{R}{v}$, entonces el integrando se anula, recuperando $\Delta u = 0$.

---

## Interpretación gráfica
 ![Isotermas de CO₂](isotermas_comparacion.png)


> [!note] Interpretación gráfica
> 
> - **Gas ideal (350 K)**: Sigue la ley de los gases ideales ($PV = nRT$), mostrando una relación hiperbólica presión-volumen.
> - **Gas real (350 K)**: A altas presiones, se desvía del modelo ideal debido a fuerzas intermoleculares y volumen finito.
> - **Isoterma real (280 K)**: Por debajo de la temperatura crítica, presenta una zona de condensación.
> - **Punto crítico**: $T_c = 304.1$ K, $P_c = 7377$ kPa
> - **Región ideal**: $P < 1$ Pa
> - **Área sombreada**: Desviación acumulada entre modelo ideal y real, útil para calcular el factor de compresibilidad $Z$.

---

## Tabla Comparativa de Modelos

| Modelo | $P(v)$ a $T$ cte | $w = \int P dv$ | $\Delta u$ | $q$ |
|--------|------------------|-----------------|------------|-----|
| **Gas ideal** | $\frac{RT}{v}$ | $RT\ln\frac{v_f}{v_i}$ | $0$ | $w$ |
| **Van der Waals** | $\frac{RT}{v-b} - \frac{a}{v^2}$ | $RT\ln\frac{v_f-b}{v_i-b} + a\left(\frac{1}{v_f}-\frac{1}{v_i}\right)$ | $a\left(\frac{1}{v_i}-\frac{1}{v_f}\right)$ | $RT\ln\frac{v_f-b}{v_i-b}$ |
| **Sustancia general** | $P(T,v)$ | $\int P dv$ | $\int\left[T\left(\frac{\partial P}{\partial T}\right)_v-P\right]dv$ | $\Delta u + w$ |
| **Líquido/sólido incompresible** | $P(v)$ (muy pendiente) | $\approx 0$ (o $\int v dP$ para trabajo de flujo) | $c\Delta T = 0$ | $0$ (aprox.) |

---

## Demostraciones Clave

### 1. Condición para $\Delta u = 0$ en un Proceso Isotérmico

> [!demostracion] Demostración
> 
> Queremos determinar bajo qué condición se cumple $\Delta u = 0$ para cualquier proceso isotérmico.
> 
> De la expresión general:
> $$
> du = \left( \frac{\partial u}{\partial v} \right)_T dv
> $$
> 
> Para que $\Delta u = 0$ independientemente de $dv$, debe cumplirse:
> $$
> \left( \frac{\partial u}{\partial v} \right)_T = 0
> $$
> 
> Usando la identidad termodinámica:
> $$
> \left( \frac{\partial u}{\partial v} \right)_T = T \left( \frac{\partial P}{\partial T} \right)_v - P = 0
> $$
> 
> Es decir:
> $$
> T \left( \frac{\partial P}{\partial T} \right)_v = P
> $$
> 
> Esta es una **ecuación diferencial parcial** para $P(T,v)$. Su solución general es:
> $$
> P = T \cdot f(v)
> $$
> 
> La ecuación de estado del gas ideal ($P = RT/v$) satisface esta condición con $f(v) = R/v$. También la cumplen sustancias con ecuación $P = T \cdot g(v)$, pero la mayoría de las sustancias reales no la satisfacen.
> 
> $\square$

### 2. Diferencia de Calores Específicos a partir de la Isoterma

> [!demostracion] Relación con $c_p - c_v$
> 
> Partiendo de $ds = \frac{c_v}{T}dT + \left( \frac{\partial P}{\partial T} \right)_v dv$:
> 
> En una isoterma ($dT = 0$):
> $$
> ds = \left( \frac{\partial P}{\partial T} \right)_v dv
> $$
> 
> Pero también $ds = \frac{\delta q}{T} = \frac{du + Pdv}{T}$.
> 
> Igualando y usando $\left( \frac{\partial u}{\partial v} \right)_T = T \left( \frac{\partial P}{\partial T} \right)_v - P$, se recupera la expresión general para $c_p - c_v$.
> 
> $\square$

---

## Ejercicios Propuestos

> [!question] Ejercicio 1
> Un mol de gas ideal se expande isotérmicamente a 300 K desde 0.1 m³ hasta 0.3 m³. Calcule:
> a) El trabajo realizado por el gas
> b) El calor absorbido
> c) El cambio de energía interna

<details>
<summary>Solución</summary>

a) $W = nRT\ln(V_f/V_i) = 1 \cdot 8.314 \cdot 300 \cdot \ln(0.3/0.1) = 2494.2 \cdot \ln 3 = 2494.2 \cdot 1.099 = 2741\ \text{J}$
b) $\Delta U = 0 \Rightarrow Q = W = 2741\ \text{J}$
c) $\Delta U = 0$
</details>

> [!question] Ejercicio 2
> Un gas de Van der Waals ($a = 0.137\ \text{Pa·m}^6/\text{mol}^2$, $b = 3.87 \times 10^{-5}\ \text{m}^3/\text{mol}$) se expande isotérmicamente a 300 K desde $v_i = 1 \times 10^{-4}\ \text{m}^3/\text{mol}$ hasta $v_f = 5 \times 10^{-4}\ \text{m}^3/\text{mol}$. Calcule $\Delta u$, $w$ y $q$ por mol.

<details>
<summary>Solución</summary>

$\Delta u = a(1/v_i - 1/v_f) = 0.137 \cdot (10000 - 2000) = 0.137 \cdot 8000 = 1096\ \text{J/mol}$
$w = RT\ln\frac{v_f-b}{v_i-b} + a(1/v_f - 1/v_i)$
$v_i-b \approx 1\times10^{-4} - 0.0387\times10^{-3} = 0.0613\times10^{-3} = 6.13\times10^{-5}$
$v_f-b \approx 5\times10^{-4} - 0.0387\times10^{-3} = 4.613\times10^{-4}$
$RT\ln(...) = 2494.2 \cdot \ln(4.613/0.613) = 2494.2 \cdot \ln 7.53 = 2494.2 \cdot 2.02 = 5038\ \text{J}$
$a(1/v_f - 1/v_i) = 0.137 \cdot (2000 - 10000) = -1096\ \text{J}$
$w = 5038 - 1096 = 3942\ \text{J/mol}$
$q = \Delta u + w = 1096 + 3942 = 5038\ \text{J/mol}$ (que es justo $RT\ln(...)$)
</details>

> [!question] Ejercicio 3
> Demuestre que para un gas ideal, el coeficiente de expansión térmica $\beta = \frac{1}{v}\left(\frac{\partial v}{\partial T}\right)_P$ es igual a $1/T$. ¿Qué implica esto para la forma de las isotermas?

<details>
<summary>Solución</summary>

Para gas ideal $v = RT/P$, entonces $(\partial v/\partial T)_P = R/P$, por lo tanto $\beta = (1/v)(R/P) = (P/RT)(R/P) = 1/T$.
Implica que la pendiente de las isotermas en el plano $P$-$v$ es $(\partial P/\partial v)_T = -P/v$, y el espaciado entre isotermas sigue una ley simple.
</details>

---

## Notas Relacionadas

- [[Primera Ley de la Termodinámica]]
- [[Gases Ideales]]
- [[Gases Reales]]
- [[Energía Interna]]
- [[Proceso Adiabatico Reversible]]
- [[Proceso Politropico]]
- [[Proceso Isobarico]]
- [[Proceso Isometrico]]
- [[Factor de Compresibilidad]]
- [[Ecuación de Van der Waals]]
