---
title: "Derivadas isentrópicas y velocidad del sonido"
order: 2
tags:
  - termodinamica
  - relaciones_termodinamicas
  - jacobianos
  - isentropico
draft: false
aliases:
  - coeficientes isentrópicos
  - compresibilidad isentrópica
  - velocidad del sonido termodinámica
---

# Derivadas isentrópicas y velocidad del sonido

> [!definicion]
> Las **derivadas isentrópicas** son derivadas parciales tomadas a entropía constante ($s = \text{cte}$). Su cálculo con el [[index | método de Jacobianos]] da expresiones exactas en función de $c_p$, $c_v$, $\alpha$, $\kappa_T$ para cualquier sustancia. La más importante es la **compresibilidad isentrópica**:
> $$\kappa_s \equiv -\frac{1}{v}\!\left(\frac{\partial v}{\partial P}\right)_s = \frac{\kappa_T}{\gamma} = \frac{c_v}{c_p}\,\kappa_T,$$
> que entra directamente en la velocidad de propagación del sonido: $c_{\rm son}^2 = v/\kappa_s$.

---

## Las cinco derivadas isentrópicas principales

### $(\partial T/\partial P)_s$ — gradiente adiabático en presión

> [!demostracion]
> De las [[TdS | ecuaciones $T\,ds$]] con $ds = 0$:
> $$0 = c_p\,dT - T\!\left(\frac{\partial v}{\partial T}\right)_P\!dP \;\Longrightarrow\; \left(\frac{\partial T}{\partial P}\right)_s = \frac{T}{c_p}\!\left(\frac{\partial v}{\partial T}\right)_P = \frac{Tv\alpha}{c_p}.$$
>
> $$\boxed{\left(\frac{\partial T}{\partial P}\right)_s = \frac{Tv\alpha}{c_p}.} \qquad \blacksquare$$
>
> Para gas ideal: $v\alpha = v/T = R/P$, luego $(\partial T/\partial P)_s = TR/(c_p P) = RT/c_p P$, que integra a $T \propto P^{R/c_p} = P^{(\gamma-1)/\gamma}$. $\checkmark$

### $(\partial T/\partial v)_s$ — gradiente adiabático en volumen

> [!demostracion]
> De las [[TdS | ecuaciones $T\,ds$]] con $ds = 0$:
> $$0 = c_v\,dT + T\!\left(\frac{\partial P}{\partial T}\right)_v\!dv \;\Longrightarrow\; \left(\frac{\partial T}{\partial v}\right)_s = -\frac{T}{c_v}\!\left(\frac{\partial P}{\partial T}\right)_v = -\frac{T\alpha}{c_v\kappa_T}.$$
>
> $$\boxed{\left(\frac{\partial T}{\partial v}\right)_s = -\frac{T\alpha}{c_v\kappa_T}.} \qquad \blacksquare$$
>
> Para gas ideal: $(\partial P/\partial T)_v = R/v$, luego $(\partial T/\partial v)_s = -TR/(c_vv)$, que integra a $Tv^{R/c_v} = Tv^{\gamma-1} = \text{cte}$. $\checkmark$

### $(\partial P/\partial v)_s$ — módulo de compresión isentrópico

> [!demostracion]
> Usando la [[Identidades/index | regla cíclica]] a $s$ constante:
> $$\left(\frac{\partial P}{\partial v}\right)_s = \frac{(\partial P/\partial T)_s}{(\partial v/\partial T)_s} = \frac{(\partial P/\partial T)_s}{(\partial v/\partial s)_T\,(\partial s/\partial T)_s + \ldots}$$
> Más directo: usar $(\partial P/\partial v)_s = (\partial P/\partial v)_T\cdot(\kappa_T/\kappa_s)$ (ratio de compresibilidades):
> $$\left(\frac{\partial P}{\partial v}\right)_s = \left(\frac{\partial P}{\partial v}\right)_T\cdot\frac{\kappa_T}{\kappa_s} = \frac{-1}{v\kappa_T}\cdot\gamma = -\frac{\gamma}{v\kappa_T} = -\frac{\gamma}{v}\cdot\frac{1}{\kappa_T}.$$
>
> $$\boxed{\left(\frac{\partial P}{\partial v}\right)_s = -\frac{\gamma}{v\kappa_T}.} \qquad \blacksquare$$
>
> Para gas ideal: $\kappa_T = 1/P$, $\gamma = $ cte., luego $(\partial P/\partial v)_s = -\gamma P/v$, que integra a $Pv^\gamma = \text{cte}$. $\checkmark$

### $(\partial P/\partial T)_s$ — pendiente $P$-$T$ isentrópica

> [!demostracion]
> Por la [[Identidades/index | regla cíclica]] a $s$ constante en $(P,T)$:
> $$\left(\frac{\partial P}{\partial T}\right)_s = \frac{1}{(\partial T/\partial P)_s} = \frac{c_p}{Tv\alpha}. \qquad \blacksquare$$
>
> Equivalentemente, por la [[Identidades/index | regla recíproca]].

### Compresibilidad isentrópica $\kappa_s$

> [!demostracion]
> De la definición y de $(\partial P/\partial v)_s = -\gamma/(v\kappa_T)$:
> $$\kappa_s \equiv -\frac{1}{v}\!\left(\frac{\partial v}{\partial P}\right)_s = \frac{-1/v}{(\partial P/\partial v)_s} = \frac{-1/v}{-\gamma/(v\kappa_T)} = \frac{\kappa_T}{\gamma} = \frac{c_v}{c_p}\,\kappa_T.$$
>
> $$\boxed{\kappa_s = \frac{\kappa_T}{\gamma} \;\Longleftrightarrow\; \gamma = \frac{\kappa_T}{\kappa_s}.} \qquad \blacksquare$$

---

## Velocidad del sonido

> [!proposicion]
> En un fluido, las perturbaciones de presión (ondas de sonido) se propagan isentrópicamente. La velocidad de propagación es:
> $$c_{\rm son}^2 = -v^2\!\left(\frac{\partial P}{\partial v}\right)_s = \frac{\gamma v^2}{v\kappa_T} = \frac{\gamma v}{\kappa_T} = \frac{v}{\kappa_s}.$$
>
> Expresado en función de la densidad $\rho = 1/v$:
> $$c_{\rm son}^2 = \frac{\gamma}{\rho\kappa_T} = \frac{1}{\rho\kappa_s}.$$
>
> Para gas ideal: $\kappa_T = 1/P$ y $P/\rho = P v = R_s T$, luego $c_{\rm son} = \sqrt{\gamma R_s T}$.

> [!ejemplo]
> **Comparación: gas ideal vs. vapor de agua real a $200\,°\mathrm{C}$, $P = 1\,\mathrm{MPa}$.**
>
> *Gas ideal (vapor de agua):* $R_s = 8314/18.015 = 461.5\,\mathrm{J/(kg\cdot K)}$, $\gamma \approx 1.32$, $T = 473\,\mathrm{K}$:
> $$c_{\rm son}^{\rm ideal} = \sqrt{1.32\times461.5\times473} = \sqrt{288\,684} = 537\,\mathrm{m/s}.$$
>
> *Vapor real* (de tablas: $v = 0.2060\,\mathrm{m^3/kg}$, $\kappa_T \approx 1.60\times10^{-6}\,\mathrm{Pa^{-1}}$, $\gamma \approx 1.28$):
> $$c_{\rm son}^{\rm real} = \sqrt{\frac{\gamma v}{\kappa_T}} = \sqrt{\frac{1.28\times0.2060}{1.60\times10^{-6}}} = \sqrt{164\,800} = 406\,\mathrm{m/s}.$$
>
> La diferencia ($537$ vs. $406\,\mathrm{m/s}$, un $24\%$) refleja la desviación del vapor de agua respecto al gas ideal a $1\,\mathrm{MPa}$: la compresibilidad real es mayor que la ideal, reduciendo la velocidad del sonido. $\blacksquare$

---

## Tabla de coeficientes isentrópicos

> [!teoria]
> | Magnitud | Fórmula general | Gas ideal |
> |:---:|:---|:---:|
> | $(\partial T/\partial P)_s$ | $Tv\alpha/c_p$ | $T/c_p P\cdot R = RT/c_pP$ |
> | $(\partial T/\partial v)_s$ | $-T\alpha/(c_v\kappa_T)$ | $-TR/(c_vv)$ |
> | $(\partial P/\partial v)_s$ | $-\gamma/(v\kappa_T)$ | $-\gamma P/v$ |
> | $(\partial P/\partial T)_s$ | $c_p/(Tv\alpha)$ | $c_pP/(TR)$ |
> | $\kappa_s$ | $\kappa_T/\gamma$ | $1/(\gamma P)$ |
> | $c_{\rm son}^2$ | $v/\kappa_s = \gamma v/\kappa_T$ | $\gamma R_s T$ |

---

## Coeficiente de Grüneisen

> [!teoria]
> El **coeficiente de Grüneisen** $\Gamma$ aparece en el estudio de sólidos a altas presiones y en astrofísica estelar:
> $$\Gamma \equiv \frac{v\alpha}{c_v\kappa_T} = \frac{v}{c_v}\!\left(\frac{\partial P}{\partial T}\right)_v = \frac{v\alpha\,c_p}{c_p\,c_v\kappa_T}.$$
> Relaciona $(\partial T/\partial v)_s = -T\Gamma/v$ con el calentamiento adiabático al comprimir: cuanto mayor es $\Gamma$, mayor es el calentamiento al comprimir el material. Para metales sólidos, $\Gamma \approx 1$–$3$; para gases ideales monoatómicos, $\Gamma = (\gamma-1) = 2/3$.

---

## Relación con otras notas

> [!info]
> - Los cinco coeficientes se derivan con el [[index | método de Jacobianos]] (ver [[Aplicaciones Termodinamicas]] para el cálculo detallado).
> - $\kappa_s$ entra en la relación $\gamma = \kappa_T/\kappa_s$ de la nota [[Razon de Calores | Razón $\gamma$]].
> - La velocidad del sonido conecta con la mecánica de fluidos (ver el módulo de [[Mecanica de Fluidos/index | Mecánica de Fluidos]]).
> - Las relaciones $Tv^{\gamma-1} = \text{cte}$ y $Pv^\gamma = \text{cte}$ son base de los ciclos Brayton y Otto.

> [!referencia]
> Çengel & Boles, *Termodinámica*, §12-4; Callen, *Thermodynamics*, §7-3; Landau & Lifshitz, *Mecánica de Fluidos* (vol. 6), §1; Moran & Shapiro, §11.4.
