---
title: "Identidades de derivadas parciales"
order: 1
tags:
  - termodinamica
  - relaciones_termodinamicas
  - calculo
  - identidades
  - index
draft: false
aliases:
  - regla recíproca
  - regla cíclica
  - triple producto
  - identidades termodinámicas
---

# Identidades de derivadas parciales

> [!definicion]
> Tres identidades de cálculo diferencial son el punto de partida del análisis de sustancias reales en termodinámica: la **regla recíproca**, la **regla triple producto** (cíclica) y la **regla de la cadena**. Las tres se derivan de la álgebra de diferenciales exactos y se aplican sistemáticamente para convertir derivadas no medibles (de $s$, $u$, $h$) en derivadas de $P$, $v$, $T$.

---

## Las tres identidades

> [!teoria] Las tres identidades fundamentales
> Sea $z = z(x,y)$ una relación diferenciable entre tres variables termodinámicas, de modo que cualquiera de las tres puede escribirse como función de las otras dos.
>
> **1. Regla recíproca:**
> $$\left(\frac{\partial x}{\partial y}\right)_z = \frac{1}{\left(\partial y/\partial x\right)_z}.$$
>
> **2. Regla triple producto (cíclica):**
> $$\left(\frac{\partial x}{\partial y}\right)_z\!\left(\frac{\partial y}{\partial z}\right)_x\!\left(\frac{\partial z}{\partial x}\right)_y = -1.$$
>
> **3. Regla de la cadena** (cambio de variable fija):
> $$\left(\frac{\partial x}{\partial y}\right)_w = \left(\frac{\partial x}{\partial z}\right)_w\!\left(\frac{\partial z}{\partial y}\right)_w.$$
> Variante con variable fija distinta:
> $$\left(\frac{\partial x}{\partial y}\right)_z = \left(\frac{\partial x}{\partial y}\right)_w + \left(\frac{\partial x}{\partial w}\right)_y\!\left(\frac{\partial w}{\partial y}\right)_z.$$

---

## Demostración de las tres identidades

### Regla recíproca

> [!demostracion]
> **Paso 1.** Si $z = \text{cte}$, la relación $z(x,y) = z_0$ define $y$ como función de $x$ (o viceversa). Sea $dx = (\partial x/\partial y)_z\,dy$ la relación diferencial a $z$ constante.
>
> **Paso 2.** Despejando $dy$: $dy = \frac{1}{(\partial x/\partial y)_z}\,dx$.
>
> **Paso 3.** Por definición, $(\partial y/\partial x)_z$ es el coeficiente que multiplica $dx$ en la expresión de $dy$ a $z$ constante. Luego:
> $$\left(\frac{\partial y}{\partial x}\right)_z = \frac{1}{(\partial x/\partial y)_z}. \qquad \blacksquare$$

### Regla triple producto

> [!demostracion]
> **Paso 1.** Escribir el diferencial total de $z = z(x,y)$:
> $$dz = \left(\frac{\partial z}{\partial x}\right)_y\!dx + \left(\frac{\partial z}{\partial y}\right)_x\!dy. \tag{*}$$
>
> **Paso 2.** Imponer $z = \text{cte}$ ($dz = 0$) en (*):
> $$0 = \left(\frac{\partial z}{\partial x}\right)_y\!dx + \left(\frac{\partial z}{\partial y}\right)_x\!dy \;\Longrightarrow\; \frac{dy}{dx}\bigg|_{z=\text{cte}} = -\frac{(\partial z/\partial x)_y}{(\partial z/\partial y)_x}.$$
>
> **Paso 3.** La derivada $dy/dx$ a $z$ constante es por definición $(\partial y/\partial x)_z$:
> $$\left(\frac{\partial y}{\partial x}\right)_z = -\frac{(\partial z/\partial x)_y}{(\partial z/\partial y)_x}.$$
>
> **Paso 4.** Multiplicar ambos lados por $(\partial x/\partial z)_y\,(\partial z/\partial y)_x$:
> $$\left(\frac{\partial y}{\partial x}\right)_z\!\left(\frac{\partial x}{\partial z}\right)_y = -\frac{1}{(\partial z/\partial y)_x} = -\left(\frac{\partial y}{\partial z}\right)_x \quad\Longrightarrow\quad \left(\frac{\partial y}{\partial x}\right)_z\!\left(\frac{\partial x}{\partial z}\right)_y\!\left(\frac{\partial z}{\partial y}\right)_x = -1.$$
>
> Reordenando cíclicamente ($x\to y$, $y\to z$, $z\to x$):
> $$\boxed{\left(\frac{\partial x}{\partial y}\right)_z\!\left(\frac{\partial y}{\partial z}\right)_x\!\left(\frac{\partial z}{\partial x}\right)_y = -1.} \qquad \blacksquare$$

### Regla de la cadena

> [!demostracion]
> **Paso 1.** Sea $x = x(z,w)$ y $z = z(y,w)$. Diferenciando $x$ a $w$ constante:
> $$dx\big|_w = \left(\frac{\partial x}{\partial z}\right)_w\!dz\big|_w.$$
>
> **Paso 2.** Dividiendo por $dy$ a $w$ constante:
> $$\left(\frac{\partial x}{\partial y}\right)_w = \left(\frac{\partial x}{\partial z}\right)_w\!\left(\frac{\partial z}{\partial y}\right)_w. \qquad \blacksquare$$

---

## Identidades termodinámicas clave

> [!proposicion] Conversión entre derivadas con $P$, $v$, $T$
> Con las tres identidades se expresan todas las derivadas de primer orden en términos de $\alpha$ y $\kappa_T$:
>
> | Derivada | Resultado | Usando |
> |:---:|:---|:---|
> | $\left(\partial P/\partial T\right)_v$ | $\alpha/\kappa_T$ | Regla cíclica en $P(T,v)$ |
> | $\left(\partial v/\partial P\right)_T$ | $-v\kappa_T$ | Definición de $\kappa_T$ |
> | $\left(\partial v/\partial T\right)_P$ | $v\alpha$ | Definición de $\alpha$ |
> | $\left(\partial T/\partial P\right)_v$ | $\kappa_T/\alpha$ | Recíproca de $(\partial P/\partial T)_v$ |
> | $\left(\partial T/\partial v\right)_P$ | $1/(v\alpha)$ | Regla recíproca |
> | $\left(\partial P/\partial v\right)_T$ | $-1/(v\kappa_T)$ | Regla recíproca |
>
> Todas las relaciones de [[Maxwell]] y las [[TdS | ecuaciones $T\,ds$]] son consecuencias de estas tres reglas aplicadas a las propiedades de estado.

---

## Ejemplo: derivar $(\partial P/\partial T)_v$ desde $\alpha$ y $\kappa_T$

> [!ejemplo]
> Calcular $(\partial P/\partial T)_v$ para el agua líquida a $20\,°\mathrm{C}$, sabiendo que $\alpha = 2.07\times10^{-4}\,\mathrm{K^{-1}}$ y $\kappa_T = 4.6\times10^{-10}\,\mathrm{Pa^{-1}}$.
>
> **Paso 1 — Regla cíclica** en las variables $P$, $v$, $T$:
> $$\left(\frac{\partial P}{\partial T}\right)_v\!\left(\frac{\partial T}{\partial v}\right)_P\!\left(\frac{\partial v}{\partial P}\right)_T = -1.$$
>
> **Paso 2 — Despejar** $(\partial P/\partial T)_v$:
> $$\left(\frac{\partial P}{\partial T}\right)_v = -\frac{1}{(\partial T/\partial v)_P\,(\partial v/\partial P)_T} = -\frac{(\partial v/\partial T)_P}{(\partial v/\partial P)_T} = \frac{\alpha/v}{1/(v\kappa_T)} = \frac{\alpha}{\kappa_T}.$$
>
> **Paso 3 — Sustituir:**
> $$\left(\frac{\partial P}{\partial T}\right)_v = \frac{2.07\times10^{-4}}{4.6\times10^{-10}} = 4.5\times10^{5}\,\mathrm{Pa/K} = 4.5\,\mathrm{bar/K}. \qquad \blacksquare$$
>
> Este resultado es útil para estimar el aumento de presión cuando el agua líquida en un contenedor rígido se calienta: a $20\,°\mathrm{C}$, un calentamiento de $1\,°\mathrm{C}$ aumenta la presión en $\approx4.5\,\mathrm{bar}$ si el contenedor es perfectamente rígido.

---

## Relación con otras notas

> [!info]
> - La regla cíclica es la base de la [[Regla Ciclica | nota de aplicaciones]]: se usa para derivar $(\partial P/\partial T)_v = \alpha/\kappa_T$ y para la presión interna $(\partial u/\partial v)_T$.
> - Las tres identidades se aplican en la derivación de [[Maxwell | Maxwell]], [[TdS | $T\,ds$]] y [[Cp Cv/index | $c_p - c_v$]].
> - El [[Jacobianos/index | método de Jacobianos]] generaliza estas reglas en una notación matricial que sistematiza el cálculo.

> [!referencia]
> Çengel & Boles, *Termodinámica*, §12-1; Callen, *Thermodynamics*, §4-1; Moran & Shapiro, §11.1; Borgnakke & Sonntag, §13.1.
