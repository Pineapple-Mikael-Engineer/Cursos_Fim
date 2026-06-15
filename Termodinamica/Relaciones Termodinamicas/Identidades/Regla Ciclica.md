---
title: "Aplicaciones de la regla cíclica"
tags:
  - termodinamica
  - relaciones_termodinamicas
  - identidades
  - regla_ciclica
draft: false
aliases:
  - regla triple producto termodinámica
  - presión interna
  - coeficiente de Grüneisen
---

# Aplicaciones de la regla cíclica

> [!definicion]
> La **regla cíclica** $(\partial x/\partial y)_z\,(\partial y/\partial z)_x\,(\partial z/\partial x)_y = -1$ tiene dos aplicaciones principales en termodinámica: (1) convertir cualquier derivada parcial en función de los coeficientes medibles $\alpha$, $\kappa_T$, $c_p$, y (2) calcular la **presión interna** $(\partial u/\partial v)_T$, que cuantifica la contribución de las fuerzas intermoleculares a la energía interna. Ver [[index | Identidades]] para la demostración de la regla.

---

## La conversión fundamental: $(\partial P/\partial T)_v = \alpha/\kappa_T$

> [!demostracion]
> **Paso 1 — Aplicar la regla cíclica** a las variables $P$, $v$, $T$ (las tres ligadas por la ecuación de estado):
> $$\left(\frac{\partial P}{\partial T}\right)_v\!\left(\frac{\partial T}{\partial v}\right)_P\!\left(\frac{\partial v}{\partial P}\right)_T = -1.$$
>
> **Paso 2 — Despejar** $(\partial P/\partial T)_v$:
> $$\left(\frac{\partial P}{\partial T}\right)_v = -\frac{1}{(\partial T/\partial v)_P\,(\partial v/\partial P)_T} = -\frac{(\partial v/\partial T)_P}{(\partial v/\partial P)_T}.$$
>
> **Paso 3 — Sustituir** $(\partial v/\partial T)_P = v\alpha$ y $(\partial v/\partial P)_T = -v\kappa_T$:
> $$\left(\frac{\partial P}{\partial T}\right)_v = -\frac{v\alpha}{-v\kappa_T} = \frac{\alpha}{\kappa_T}. \qquad \blacksquare$$
>
> Este resultado convierte la 3.ª relación de [[Maxwell]] en:
> $$\left(\frac{\partial s}{\partial v}\right)_T = \left(\frac{\partial P}{\partial T}\right)_v = \frac{\alpha}{\kappa_T}.$$

---

## Presión interna $(\partial u/\partial v)_T$

> [!teoria]
> La **presión interna** $\pi_T \equiv (\partial u/\partial v)_T$ mide la variación de energía interna al cambiar el volumen a temperatura constante. Es cero para el gas ideal (sin interacciones entre moléculas) y positiva para gases reales con atracción intermolecular.

> [!demostracion]
> **Paso 1 — Partir de** $du = T\,ds - P\,dv$. A $T$ constante, dividiendo por $dv$:
> $$\left(\frac{\partial u}{\partial v}\right)_T = T\left(\frac{\partial s}{\partial v}\right)_T - P.$$
>
> **Paso 2 — Sustituir** $(\partial s/\partial v)_T = \alpha/\kappa_T$ (3.ª relación de [[Maxwell]], derivada arriba):
> $$\pi_T = T\cdot\frac{\alpha}{\kappa_T} - P = \frac{T\alpha - P\kappa_T}{\kappa_T}.$$
>
> $$\boxed{\left(\frac{\partial u}{\partial v}\right)_T = T\left(\frac{\partial P}{\partial T}\right)_v - P = \frac{T\alpha}{\kappa_T} - P.} \qquad \blacksquare$$

> [!ejemplo]
> **Gas ideal.** $T(\partial P/\partial T)_v = T(R/v) = P$ (usando $Pv = RT$):
> $$\pi_T^{\rm ideal} = T\cdot\frac{R}{v} - P = P - P = 0.$$
> La energía interna de un gas ideal no depende del volumen, solo de la temperatura. $\blacksquare$

> [!ejemplo]
> **Gas de van der Waals.** $P = RT/(v-b) - a/v^2$, luego $(\partial P/\partial T)_v = R/(v-b)$:
> $$\pi_T^{\rm vdW} = T\cdot\frac{R}{v-b} - \left(\frac{RT}{v-b} - \frac{a}{v^2}\right) = \frac{RT}{v-b} - \frac{RT}{v-b} + \frac{a}{v^2} = \frac{a}{v^2}.$$
>
> El parámetro $a$ (atracción intermolecular) es el único responsable de $\pi_T^{\rm vdW} > 0$: al aumentar el volumen, el trabajo necesario para separar las moléculas aumenta la energía interna. Cuando $v \to \infty$ (gas enrarecido), $\pi_T \to 0$ y el comportamiento se acerca al ideal. $\blacksquare$

---

## Energía interna del gas de van der Waals

> [!proposicion]
> Integrando la presión interna a temperatura constante desde $v = \infty$ (gas ideal diluido) hasta $v$ finito:
> $$u(T,v) = u^{\rm ideal}(T) - \int_\infty^v \frac{a}{v'^2}\,dv' = u^{\rm ideal}(T) + \left[\frac{a}{v'}\right]_\infty^v = u^{\rm ideal}(T) - \frac{a}{v}.$$
>
> El término $-a/v$ es la contribución de las fuerzas atractivas a la energía interna: cuanto mayor es $a$ y menor $v$, más negativa es la energía potencial de interacción.

> [!ejemplo]
> **Cálculo de $\Delta u$ en calentamiento y compresión de $\mathrm{CO_2}$ real.** $a = 0.3658\,\mathrm{Pa\cdot m^6/mol^2}$, $b = 4.29\times10^{-5}\,\mathrm{m^3/mol}$. Estado $1$: $T_1 = 300\,\mathrm{K}$, $v_1 = 0.500\,\mathrm{m^3/kmol}$; estado $2$: $T_2 = 400\,\mathrm{K}$, $v_2 = 0.200\,\mathrm{m^3/kmol}$.
>
> **Paso 1 — Contribución por $T$:** $\Delta u_T = \bar{c}_v^{\rm ideal}\,\Delta T \approx (3.5\,R_u)\times100 = 2909\,\mathrm{kJ/kmol}$ (para $\mathrm{CO_2}$ lineal: $\bar{c}_v \approx 3.5\,R_u$ a $350\,\mathrm{K}$).
>
> **Paso 2 — Contribución por $v$** (a $T_2 = 400\,\mathrm{K}$):
> $$\Delta u_v = -\int_{v_1}^{v_2}\frac{\bar{a}}{v^2}\,dv = \bar{a}\left(\frac{1}{v_2}-\frac{1}{v_1}\right) = 365.8\left(\frac{1}{0.200}-\frac{1}{0.500}\right) = 365.8\times3.00 = 1097\,\mathrm{kJ/kmol}.$$
> (El signo es positivo: comprimir el gas aumenta la energía potencial de atracción.)
>
> **Paso 3 — Total:**
> $$\Delta\bar{u} = \Delta u_T + \Delta u_v = 2909 + 1097 = 4006\,\mathrm{kJ/kmol}. \qquad \blacksquare$$

---

## Otras derivadas importantes obtenidas con la regla cíclica

> [!proposicion] Tabla de derivadas clave
> | Derivada | Resultado | Método |
> |:---:|:---|:---|
> | $(\partial P/\partial v)_T$ | $-1/(v\kappa_T)$ | Definición de $\kappa_T$ + recíproca |
> | $(\partial T/\partial v)_s$ | $-T\alpha/(c_v\kappa_T)$ | Ecuación $T\,ds$ con $ds=0$ + cíclica |
> | $(\partial T/\partial P)_s$ | $Tv\alpha/c_p$ | Ecuación $T\,ds$ con $ds=0$ |
> | $(\partial u/\partial P)_T$ | $v(\kappa_T P - T\alpha)$ | $(\partial u/\partial v)_T\cdot(\partial v/\partial P)_T$ |
> | $(\partial h/\partial v)_T$ | $v/\kappa_T - Tv\alpha/\kappa_T + P$ | De $dh = T\,ds + v\,dP$ y cíclica |
>
> El método general para cualquier derivada se sistematiza con el [[Jacobianos/index | método de Jacobianos]].

---

## Relación con otras notas

> [!info]
> - La regla cíclica y la recíproca están demostradas en [[index | Identidades]].
> - $(\partial P/\partial T)_v = \alpha/\kappa_T$ alimenta las [[Maxwell | relaciones de Maxwell]] y las [[TdS | ecuaciones $T\,ds$]].
> - La presión interna $\pi_T = a/v^2$ distingue al gas de van der Waals del ideal.
> - El [[Jacobianos/index | método de Jacobianos]] sistematiza el cálculo de todas estas derivadas.

> [!referencia]
> Çengel & Boles, *Termodinámica*, §12-1 a 12-4; Callen, *Thermodynamics*, §7-2; Moran & Shapiro, §11.2; Borgnakke & Sonntag, §13.3.
