---
title: "Aplicaciones de la regla cíclica"
order: 1
tags:
  - termodinamica
  - relaciones_termodinamicas
  - identidades
  - regla_ciclica
draft: false
aliases:
  - regla triple producto termodinámica
  - aplicaciones regla cíclica
---

# Aplicaciones de la regla cíclica

> [!definicion]
> La **regla cíclica** $(\partial x/\partial y)_z\,(\partial y/\partial z)_x\,(\partial z/\partial x)_y = -1$ es la herramienta que convierte cualquier derivada parcial termodinámica en función de los coeficientes medibles $\alpha$, $\kappa_T$, $c_p$. Su aplicación más usada produce $(\partial P/\partial T)_v = \alpha/\kappa_T$, que a su vez alimenta las [[Maxwell | relaciones de Maxwell]], las [[TdS | ecuaciones $T\,ds$]] y la [[Presion Interna | presión interna]]. La demostración de la regla está en [[index | Identidades]].

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
> Este es el resultado más reutilizado de las relaciones termodinámicas: expresa una derivada de presión (difícil de medir directamente) en términos de $\alpha$ y $\kappa_T$, ambos tabulados. Convierte además la 3.ª relación de [[Maxwell]] en una forma medible:
> $$\left(\frac{\partial s}{\partial v}\right)_T = \left(\frac{\partial P}{\partial T}\right)_v = \frac{\alpha}{\kappa_T}.$$

---

## Aplicación a la presión interna

> [!proposicion]
> Sustituyendo $(\partial s/\partial v)_T = \alpha/\kappa_T$ en $du = T\,ds - P\,dv$ a $T$ constante se obtiene la **presión interna**:
> $$\left(\frac{\partial u}{\partial v}\right)_T = T\left(\frac{\partial P}{\partial T}\right)_v - P = \frac{T\alpha}{\kappa_T} - P.$$
> Su interpretación física (energía configuracional, valor nulo del gas ideal, $\pi_T = a/v^2$ del gas de van der Waals, conexión con Joule-Thomson y el ejemplo del agua líquida) se desarrolla en [[Presion Interna]]. La regla cíclica es solo el paso algebraico que la hace calculable.

---

## Otras derivadas obtenidas con la regla cíclica

> [!proposicion] Tabla de derivadas clave
> | Derivada | Resultado | Método |
> |:---:|:---|:---|
> | $(\partial P/\partial v)_T$ | $-1/(v\kappa_T)$ | Definición de $\kappa_T$ + recíproca |
> | $(\partial T/\partial v)_s$ | $-T\alpha/(c_v\kappa_T)$ | Ecuación $T\,ds$ con $ds=0$ + cíclica |
> | $(\partial T/\partial P)_s$ | $Tv\alpha/c_p$ | Ecuación $T\,ds$ con $ds=0$ |
> | $(\partial u/\partial P)_T$ | $v(\kappa_T P - T\alpha)$ | $(\partial u/\partial v)_T\cdot(\partial v/\partial P)_T$ |
> | $(\partial h/\partial v)_T$ | $\dfrac{T\alpha-1}{\kappa_T}$ | De $dh = T\,ds + v\,dP$ a $T$ cte |
>
> (Comprobación: en el límite de gas ideal $\alpha=1/T$, $\kappa_T=1/P$, las dos últimas se anulan, como debe ser para $u(T)$ y $h(T)$.) El método general para cualquier derivada se sistematiza con el [[Jacobianos/index | método de Jacobianos]].

---

## Relación con otras notas

> [!info]
> - La regla cíclica y la recíproca están demostradas en [[index | Identidades]].
> - $(\partial P/\partial T)_v = \alpha/\kappa_T$ alimenta las [[Maxwell | relaciones de Maxwell]] y las [[TdS | ecuaciones $T\,ds$]].
> - La [[Presion Interna | presión interna]] $\pi_T = T\alpha/\kappa_T - P$ y su energía configuracional se desarrollan en su nota propia.
> - El [[Jacobianos/index | método de Jacobianos]] sistematiza el cálculo de todas estas derivadas.

> [!referencia]
> Çengel & Boles, *Termodinámica*, §12-1 a 12-4; Callen, *Thermodynamics*, §7-2; Moran & Shapiro, §11.2; Borgnakke & Sonntag, §13.3.
