---
title: "Razón de calores específicos $\\gamma$"
order: 1
tags:
  - termodinamica
  - relaciones_termodinamicas
  - calores_especificos
  - isentropico
draft: false
aliases:
  - gamma termodinámico
  - razón de calores específicos
  - exponent isentrópico
---

# Razón de calores específicos $\gamma = c_p/c_v$

> [!definicion]
> El cociente $\gamma \equiv c_p/c_v$ caracteriza la respuesta de una sustancia a procesos adiabáticos y gobierna las relaciones isentrópicas. Para un gas ideal con estructura molecular fija, $\gamma$ es constante; para sustancias reales, $\gamma = \gamma(T,P)$. Un resultado exacto —válido para cualquier sustancia estable— liga $\gamma$ con la razón de compresibilidades:
> $$\gamma = \frac{c_p}{c_v} = \frac{\kappa_T}{\kappa_s},$$
> donde $\kappa_T = -(1/v)(\partial v/\partial P)_T$ y $\kappa_s = -(1/v)(\partial v/\partial P)_s$ son las compresibilidades isoterma e isentrópica.

---

## Derivación: $\gamma = \kappa_T/\kappa_s$

> [!demostracion]
> **Paso 1 — Relacionar $(\partial v/\partial P)_s$ con $(\partial v/\partial P)_T$.** Usando la [[Identidades/index | regla de la cadena]] a $s$ constante:
> $$\left(\frac{\partial v}{\partial P}\right)_s = \left(\frac{\partial v}{\partial P}\right)_T + \left(\frac{\partial v}{\partial T}\right)_P\!\left(\frac{\partial T}{\partial P}\right)_s.$$
>
> **Paso 2 — Expresar $(\partial T/\partial P)_s$.** De la 2.ª ecuación [[TdS]] con $ds = 0$:
> $$0 = c_p\,dT - T\!\left(\frac{\partial v}{\partial T}\right)_P\!dP \;\Longrightarrow\; \left(\frac{\partial T}{\partial P}\right)_s = \frac{T}{c_p}\!\left(\frac{\partial v}{\partial T}\right)_P.$$
>
> **Paso 3 — Sustituir en el Paso 1:**
> $$\left(\frac{\partial v}{\partial P}\right)_s = \left(\frac{\partial v}{\partial P}\right)_T + \frac{T}{c_p}\!\left(\frac{\partial v}{\partial T}\right)_P^{\!2}.$$
>
> **Paso 4 — Dividir por $(\partial v/\partial P)_T$ (negativo):**
> $$\frac{(\partial v/\partial P)_s}{(\partial v/\partial P)_T} = 1 + \frac{T\,[(\partial v/\partial T)_P]^2}{c_p\,(\partial v/\partial P)_T} = 1 + \frac{T\,v^2\alpha^2}{c_p\,(-v\kappa_T)} = 1 - \frac{Tv\,\alpha^2}{c_p\,\kappa_T}.$$
>
> Simplificando con $c_p - c_v = Tv\alpha^2/\kappa_T$ (ver [[Cp Cv/index | $c_p - c_v$]]):
> $$\frac{(\partial v/\partial P)_s}{(\partial v/\partial P)_T} = 1 - \frac{c_p - c_v}{c_p} = \frac{c_v}{c_p}.$$
>
> **Paso 5 — Expresar en términos de $\kappa_s$ y $\kappa_T$:**
> $$\frac{\kappa_s}{\kappa_T} = \frac{-(1/v)(\partial v/\partial P)_s}{-(1/v)(\partial v/\partial P)_T} = \frac{c_v}{c_p} = \frac{1}{\gamma}.$$
> $$\boxed{\gamma = \frac{\kappa_T}{\kappa_s}.} \qquad \blacksquare$$

---

## Valores de $\gamma$ para gases ideales

> [!teoria] Equipartición y $\gamma$
> Para un gas ideal con $f$ grados de libertad activos: $c_v = (f/2)\,R$ y $c_p = c_v + R = (f/2+1)R$, luego:
> $$\gamma = \frac{f/2 + 1}{f/2} = 1 + \frac{2}{f}.$$
>
> | Tipo de gas | Grados de libertad $f$ | $\gamma$ |
> |:---:|:---:|:---:|
> | Monoatómico ($\mathrm{He}$, $\mathrm{Ar}$) | 3 (traslación) | $5/3 \approx 1.667$ |
> | Diatómico ($\mathrm{N_2}$, $\mathrm{O_2}$, aire) | 5 (trasl. + rotac.) | $7/5 = 1.40$ |
> | Lineal poliatómico ($\mathrm{CO_2}$) | 7 (trasl. + 2 rot. + 2 vib. a altas $T$) | $9/7 \approx 1.29$ |
> | No lineal poliatómico ($\mathrm{H_2O}$, $\mathrm{CH_4}$) | 6 (trasl. + rotac.) | $8/6 \approx 1.33$ |
>
> Los valores son aproximados a temperatura ambiente; $\gamma$ decrece al aumentar $T$ (más vibraciones activas).

---

## Velocidad del sonido

> [!proposicion]
> La velocidad de propagación de una onda de presión (sonido) en un fluido es:
> $$c^2 = \left(\frac{\partial P}{\partial\rho}\right)_s = -v^2\!\left(\frac{\partial P}{\partial v}\right)_s = \frac{v}{\kappa_s} = \frac{\gamma\,v}{\kappa_T} = \gamma\,P\,v.$$
>
> Para gas ideal con $Pv = R_s T$ (donde $R_s = R_u/M$ es la constante específica):
> $$c^2 = \gamma\,P\,v = \gamma\,R_s\,T \;\Longrightarrow\; c = \sqrt{\gamma\,R_s\,T}.$$

> [!ejemplo]
> **Velocidad del sonido en aire a $20\,°\mathrm{C}$.** $\gamma = 1.40$, $R_s = 8314/28.97 = 287\,\mathrm{J/(kg\cdot K)}$, $T = 293\,\mathrm{K}$:
> $$c = \sqrt{1.40\times287\times293} = \sqrt{117\,768} = 343\,\mathrm{m/s}. \qquad \blacksquare$$

---

## Relaciones isentrópicas del gas ideal

> [!proposicion]
> Para gas ideal ($Pv = R_s T$, $\gamma = \text{cte}$) con $ds = 0$ (proceso isentrópico):
> $$Pv^\gamma = \text{cte}, \qquad Tv^{\gamma-1} = \text{cte}, \qquad T\,P^{-(\gamma-1)/\gamma} = \text{cte}.$$
>
> La primera se demuestra combinando las dos formas de $ds = 0$ de las [[TdS | ecuaciones $T\,ds$]]:
> $$0 = c_v\frac{dT}{T} + R\frac{dv}{v} = c_p\frac{dT}{T} - R\frac{dP}{P}.$$
> Dividiendo y usando $R/c_v = \gamma - 1$:
> $$\frac{dP}{P} = -\gamma\frac{dv}{v} \;\Longrightarrow\; Pv^\gamma = \text{cte}. \qquad \blacksquare$$

---

## Relación con otras notas

> [!info]
> - La relación $\gamma = \kappa_T/\kappa_s$ se demuestra con las [[TdS | ecuaciones $T\,ds$]] y la relación [[index | $c_p - c_v$]].
> - El [[Efecto Joule Thomson]] depende de $\alpha$ y $c_p$ pero no de $\gamma$ directamente.
> - Las relaciones isentrópicas del gas ideal son la base de los ciclos de la nota [[Sistemas/Dispositivos Flujo/Turbinas | Turbinas]] y del ciclo Brayton.

> [!referencia]
> Çengel & Boles, *Termodinámica*, §12-4 a 12-5; Moran & Shapiro, §11.4; Callen, *Thermodynamics*, §7-3.
