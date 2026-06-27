---
title: "Aplicaciones termodinámicas de los jacobianos"
order: 1
tags:
  - termodinamica
  - relaciones_termodinamicas
  - jacobianos
  - calculo
draft: false
aliases:
  - tabla de Bridgman aplicada
  - derivadas con jacobianos
---

# Aplicaciones termodinámicas de los jacobianos

> [!definicion]
> Este nodo aplica el [[index | método de Jacobianos]] para derivar sistemáticamente las relaciones que más se utilizan en análisis de sustancias reales: cambios de $u$, $h$, $s$ a lo largo de procesos generales; coeficientes isentrópicos; y la presión interna. En todos los casos la mecánica es la misma: calcular dos determinantes $2\times2$ de la tabla de Bridgman y dividirlos.

---

## Procedimiento general

> [!teoria] Receta en tres pasos
> Para calcular $(\partial x/\partial y)_z$:
>
> **Paso 1 — Escribir** los jacobianos elementales de $x$, $y$, $z$ desde la tabla de [[index | Bridgman]]:
> $$J(x,P) = \left(\frac{\partial x}{\partial T}\right)_P, \qquad J(x,T) = -\left(\frac{\partial x}{\partial P}\right)_T$$
> (y análogos para $y$, $z$).
>
> **Paso 2 — Calcular** $J(x,z)$ y $J(y,z)$ como determinantes $2\times 2$:
> $$J(x,z) = J(x,P)\cdot J(z,T) - J(x,T)\cdot J(z,P) \quad\text{(filando con }P\text{)}$$
> o directamente:
> $$J(x,z) = \left(\frac{\partial x}{\partial T}\right)_P\!\left(\frac{\partial z}{\partial P}\right)_T - \left(\frac{\partial x}{\partial P}\right)_T\!\left(\frac{\partial z}{\partial T}\right)_P.$$
>
> **Paso 3 — Dividir:**
> $$\left(\frac{\partial x}{\partial y}\right)_z = \frac{J(x,z)}{J(y,z)}.$$

---

## Cambio de entalpía $(\partial h/\partial P)_T$: presión interna de $h$

> [!demostracion]
> $$\left(\frac{\partial h}{\partial P}\right)_T = \frac{J(h,T)}{J(P,T)}.$$
>
> De la tabla: $J(h,T) = -(\partial h/\partial P)_T$. Pero calculemos directamente con el determinante:
> $$J(h,T) = \left(\frac{\partial h}{\partial T}\right)_P\!\underbrace{\left(\frac{\partial T}{\partial P}\right)_T}_{=0} - \left(\frac{\partial h}{\partial P}\right)_T\!\underbrace{\left(\frac{\partial T}{\partial T}\right)_P}_{=1} = -\left(\frac{\partial h}{\partial P}\right)_T.$$
>
> Entonces $J(h,T) = -(c_p\cdot 0 - v(1-T\alpha)\cdot 1) = v(1-T\alpha)$.
>
> Y $J(P,T) = (\partial P/\partial T)_P\,(\partial T/\partial P)_T - (\partial P/\partial P)_T\,(\partial T/\partial T)_P = 0 - 1 = -1$.
>
> Resultado:
> $$\left(\frac{\partial h}{\partial P}\right)_T = \frac{v(1-T\alpha)}{-1}\cdot(-1) = v(1-T\alpha). \qquad \blacksquare$$
>
> Este resultado es la entrada del [[Efecto Joule Thomson | efecto Joule-Thomson]]: $\mu_{JT} = -v(1-T\alpha)/c_p = v(T\alpha-1)/c_p$.

---

## Cambio de entropía $(\partial s/\partial P)_v$

> [!demostracion]
> $$\left(\frac{\partial s}{\partial P}\right)_v = \frac{J(s,v)}{J(P,v)}.$$
>
> **Calcular $J(s,v)$:**
> $$J(s,v) = \left(\frac{\partial s}{\partial T}\right)_P\!\left(\frac{\partial v}{\partial P}\right)_T - \left(\frac{\partial s}{\partial P}\right)_T\!\left(\frac{\partial v}{\partial T}\right)_P = \frac{c_p}{T}\cdot(-v\kappa_T) - (-v\alpha)\cdot v\alpha = -\frac{c_pv\kappa_T}{T} + v^2\alpha^2.$$
>
> **Calcular $J(P,v)$:**
> $$J(P,v) = \left(\frac{\partial P}{\partial T}\right)_P\!\left(\frac{\partial v}{\partial P}\right)_T - \left(\frac{\partial P}{\partial P}\right)_T\!\left(\frac{\partial v}{\partial T}\right)_P = 0\cdot(-v\kappa_T) - 1\cdot v\alpha = -v\alpha.$$
>
> **Resultado:**
> $$\left(\frac{\partial s}{\partial P}\right)_v = \frac{-c_pv\kappa_T/T + v^2\alpha^2}{-v\alpha} = \frac{c_p\kappa_T}{\alpha T} - \frac{v\alpha}{\alpha} = \frac{c_p\kappa_T}{\alpha T} - v. \qquad \blacksquare$$
>
> Para gas ideal: $\alpha = 1/T$, $\kappa_T = v/(RT) = 1/P$, luego $c_p\kappa_T/(\alpha T) = c_p/(P) \cdot (1/T)\cdot T = c_p/P$... verificación: de $ds = c_p\,dT/T - R\,dP/P$, a $v=\text{cte}$ (isocora ideal: $dv=0$ implica $dT/T = dP/P$), $ds = (c_p - R)dP/P = c_v\,dP/P$, es decir $(\partial s/\partial P)_v^{\rm ideal} = c_v/P$. $\checkmark$

---

## $(\partial T/\partial v)_s$ — gradiente adiabático en volumen

> [!demostracion]
> Este coeficiente determina el cambio de temperatura al comprimir adiabáticamente (p. ej. en ondas de sonido).
> $$\left(\frac{\partial T}{\partial v}\right)_s = \frac{J(T,s)}{J(v,s)}.$$
>
> **Calcular $J(T,s)$:**
> $$J(T,s) = \left(\frac{\partial T}{\partial T}\right)_P\!\left(\frac{\partial s}{\partial P}\right)_T - \left(\frac{\partial T}{\partial P}\right)_T\!\left(\frac{\partial s}{\partial T}\right)_P = 1\cdot(-v\alpha) - 0\cdot\frac{c_p}{T} = -v\alpha.$$
>
> **Calcular $J(v,s)$:**
> $$J(v,s) = \left(\frac{\partial v}{\partial T}\right)_P\!\left(\frac{\partial s}{\partial P}\right)_T - \left(\frac{\partial v}{\partial P}\right)_T\!\left(\frac{\partial s}{\partial T}\right)_P = v\alpha\cdot(-v\alpha) - (-v\kappa_T)\cdot\frac{c_p}{T} = -v^2\alpha^2 + \frac{v\kappa_T c_p}{T}.$$
>
> **Resultado:**
> $$\left(\frac{\partial T}{\partial v}\right)_s = \frac{-v\alpha}{-v^2\alpha^2 + v\kappa_T c_p/T} = \frac{-\alpha}{-v\alpha^2 + \kappa_T c_p/T} = \frac{-T\alpha}{-Tv\alpha^2 + \kappa_T c_p} = \frac{-T\alpha}{\kappa_T(c_p - c_v)/c_p\cdot c_p + \kappa_T c_v}.$$
>
> Simplificando con $c_p - c_v = Tv\alpha^2/\kappa_T$, es decir $Tv\alpha^2 = \kappa_T(c_p - c_v)$:
> $$\left(\frac{\partial T}{\partial v}\right)_s = \frac{-T\alpha}{-\kappa_T(c_p-c_v) + \kappa_T c_p} = \frac{-T\alpha}{\kappa_T c_v}.$$
> $$\boxed{\left(\frac{\partial T}{\partial v}\right)_s = -\frac{T\alpha}{c_v\kappa_T} = -\frac{T(\partial P/\partial T)_v}{c_v}.} \qquad \blacksquare$$
>
> Para gas ideal: $(\partial P/\partial T)_v = R/v$ → $(\partial T/\partial v)_s = -TR/(c_v v)$, que integra a $Tv^{R/c_v} = Tv^{\gamma-1} = \text{cte}$. $\checkmark$

---

## Tabla de derivadas usuales por jacobianos

> [!teoria] Resultados compilados
> | Derivada | Resultado | Caso ideal |
> |:---:|:---|:---:|
> | $(\partial h/\partial P)_T$ | $v(1-T\alpha)$ | $0$ |
> | $(\partial u/\partial v)_T$ | $T\alpha/\kappa_T - P$ | $0$ |
> | $(\partial s/\partial v)_T$ | $\alpha/\kappa_T$ | $R/v$ |
> | $(\partial s/\partial P)_T$ | $-v\alpha$ | $-R/P$ |
> | $(\partial T/\partial P)_s$ | $Tv\alpha/c_p$ | $RT/c_pP$ |
> | $(\partial T/\partial v)_s$ | $-T\alpha/(c_v\kappa_T)$ | $-TR/(c_vv)$ |
> | $(\partial P/\partial v)_s$ | $-\gamma/(v\kappa_T)$ | $-\gamma P/v$ |
> | $c_p - c_v$ | $Tv\alpha^2/\kappa_T$ | $R$ |
>
> Las dos últimas de la primera columna entran directamente en la velocidad del sonido $c^2 = -v^2(\partial P/\partial v)_s = \gamma v/\kappa_T$.

---

## Ejemplo complejo: propiedades de $\mathrm{CO_2}$ supercrítico

> [!ejemplo]
> $\mathrm{CO_2}$ a $T = 340\,\mathrm{K}$, $P = 8\,\mathrm{MPa}$ (supercrítico: $T_c = 304.2\,\mathrm{K}$, $P_c = 7.38\,\mathrm{MPa}$). Dados $\alpha = 1.42\times10^{-2}\,\mathrm{K^{-1}}$, $\kappa_T = 1.20\times10^{-7}\,\mathrm{Pa^{-1}}$, $v = 2.58\times10^{-3}\,\mathrm{m^3/kg}$, $c_p = 2.76\,\mathrm{kJ/(kg\cdot K)}$, calcular: (a) $c_p - c_v$, (b) $(\partial T/\partial P)_s$, (c) velocidad del sonido.
>
> **(a)** $c_p - c_v$:
> $$c_p - c_v = \frac{Tv\alpha^2}{\kappa_T} = \frac{340\times2.58\times10^{-3}\times(1.42\times10^{-2})^2}{1.20\times10^{-7}} = \frac{340\times2.58\times10^{-3}\times2.016\times10^{-4}}{1.20\times10^{-7}}.$$
> $$= \frac{1.769\times10^{-4}}{1.20\times10^{-7}} = 1474\,\mathrm{J/(kg\cdot K)} = 1.474\,\mathrm{kJ/(kg\cdot K)}.$$
> $c_v = 2.76 - 1.47 = 1.29\,\mathrm{kJ/(kg\cdot K)}$. $\gamma = c_p/c_v = 2.76/1.29 = 2.14$ (muy alto: fluido supercrítico compresible).
>
> **(b)** $(\partial T/\partial P)_s$:
> $$\left(\frac{\partial T}{\partial P}\right)_s = \frac{Tv\alpha}{c_p} = \frac{340\times2.58\times10^{-3}\times1.42\times10^{-2}}{2760} = \frac{1.245\times10^{-2}}{2760} = 4.51\times10^{-6}\,\mathrm{K/Pa} = 0.451\,\mathrm{K/bar}.$$
>
> **(c)** Velocidad del sonido:
> $$c^2 = \frac{\gamma v}{\kappa_T} = \frac{2.14\times2.58\times10^{-3}}{1.20\times10^{-7}} = \frac{5.52\times10^{-3}}{1.20\times10^{-7}} = 4.60\times10^4\,\mathrm{m^2/s^2}.$$
> $$c = \sqrt{4.60\times10^4} = 214\,\mathrm{m/s}.$$
> La velocidad del sonido en $\mathrm{CO_2}$ supercrítico ($214\,\mathrm{m/s}$) es mucho menor que en $\mathrm{CO_2}$ gaseoso a baja presión ($\approx270\,\mathrm{m/s}$ a $25\,°\mathrm{C}$): la alta compresibilidad supercrítica reduce $c$. $\blacksquare$

---

## Relación con otras notas

> [!info]
> - El procedimiento usa la tabla de [[index | Bridgman]] con los coeficientes $\alpha$, $\kappa_T$, $c_p$.
> - Los resultados de $(\partial u/\partial v)_T$ y $(\partial h/\partial P)_T$ se discuten en [[Presion Interna | presión interna]] y [[Efecto Joule Thomson | Joule-Thomson]].
> - Los coeficientes isentrópicos se completan en [[Derivadas Isentropicas]].

> [!referencia]
> Bridgman, *Complete Collection of Thermodynamic Formulas*; Callen, *Thermodynamics*, §7-4; Moran & Shapiro, §11.6.
