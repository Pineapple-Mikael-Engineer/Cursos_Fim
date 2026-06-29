---
title: "Método de Jacobianos termodinámicos"
order: 3
tags:
  - termodinamica
  - relaciones_termodinamicas
  - jacobianos
  - calculo
  - index
draft: false
aliases:
  - jacobianos termodinámicos
  - tabla de Bridgman
  - método sistemático derivadas parciales
---

# Método de Jacobianos termodinámicos

> [!definicion]
> El **método de Jacobianos** (Bridgman, 1925) sistematiza el cálculo de cualquier derivada parcial termodinámica en función de los tres coeficientes medibles $c_p$, $\alpha$, $\kappa_T$ y la presión $P$. Se basa en el **determinante jacobiano** $J(x,y)$, definido respecto a las variables independientes $(T,P)$, cuya potencia es que toda derivada parcial se reduce a un cociente de dos jacobianos: elimina el álgebra de sustituciones encadenadas y produce el resultado de forma mecánica.

---

## Definición del jacobiano termodinámico

> [!teoria] Jacobiano $J(x,y)$
> Dado un par de propiedades $(x,y)$, el jacobiano termodinámico $J(x,y)$ se define respecto a las variables base $(T,P)$:
> $$J(x,y) \equiv \frac{\partial(x,y)}{\partial(T,P)} \equiv \begin{vmatrix} \left(\partial x/\partial T\right)_P & \left(\partial x/\partial P\right)_T \\ \left(\partial y/\partial T\right)_P & \left(\partial y/\partial P\right)_T \end{vmatrix} = \left(\frac{\partial x}{\partial T}\right)_P\!\left(\frac{\partial y}{\partial P}\right)_T - \left(\frac{\partial x}{\partial P}\right)_T\!\left(\frac{\partial y}{\partial T}\right)_P.$$
>
> La propiedad central: toda derivada parcial $(\partial x/\partial y)_z$ se expresa como:
> $$\left(\frac{\partial x}{\partial y}\right)_z = \frac{J(x,z)}{J(y,z)}.$$
>
> Esta fórmula es exacta para cualquier trío de propiedades $(x,y,z)$.

---

## Demostración de la fórmula central

> [!demostracion]
> **Paso 1 — Expresar $x = x(T,P)$ y $z = z(T,P)$ en diferenciales:**
> $$dx = \left(\frac{\partial x}{\partial T}\right)_P\!dT + \left(\frac{\partial x}{\partial P}\right)_T\!dP, \qquad dz = \left(\frac{\partial z}{\partial T}\right)_P\!dT + \left(\frac{\partial z}{\partial P}\right)_T\!dP.$$
>
> **Paso 2 — Imponer $z = \text{cte}$** ($dz = 0$): de la segunda ecuación:
> $$\left(\frac{\partial z}{\partial T}\right)_P\!dT = -\left(\frac{\partial z}{\partial P}\right)_T\!dP \;\Longrightarrow\; dT = -\frac{(\partial z/\partial P)_T}{(\partial z/\partial T)_P}\,dP.$$
>
> **Paso 3 — Sustituir en $dx$** a $z$ constante:
> $$dx\big|_{dz=0} = \left[\left(\frac{\partial x}{\partial T}\right)_P\!\left(-\frac{(\partial z/\partial P)_T}{(\partial z/\partial T)_P}\right) + \left(\frac{\partial x}{\partial P}\right)_T\right]dP.$$
>
> **Paso 4 — La derivada pedida es $dx/dP$ a $z$ constante:**
> $$\left(\frac{\partial x}{\partial P}\right)_z = \left(\frac{\partial x}{\partial P}\right)_T - \frac{(\partial x/\partial T)_P\,(\partial z/\partial P)_T}{(\partial z/\partial T)_P} = \frac{(\partial x/\partial P)_T\,(\partial z/\partial T)_P - (\partial x/\partial T)_P\,(\partial z/\partial P)_T}{(\partial z/\partial T)_P}.$$
> El numerador es exactamente $J(x,z)$ (con signo según orden de columnas); el denominador es $J(z,P) = (\partial z/\partial T)_P$ (el jacobiano de $z$ con la variable $P$, que tiene $(\partial P/\partial T)_P = 0$ y $(\partial P/\partial P)_T = 1$).
>
> **Paso 5 — Generalizando** para $(\partial x/\partial y)_z$ en lugar de $(\partial x/\partial P)_z$, el mismo razonamiento da:
> $$\left(\frac{\partial x}{\partial y}\right)_z = \frac{J(x,z)}{J(y,z)}. \qquad \blacksquare$$

---

## Tabla de Bridgman: jacobianos de las propiedades principales

> [!teoria] Jacobianos elementales $J(x,P)$ y $J(x,T)$
> Con variables base $(T,P)$, los jacobianos de las variables más usadas son (usando $\alpha$, $\kappa_T$, $c_p$):
>
> | $x$ | $J(x,P) = (\partial x/\partial T)_P$ | $J(x,T) = -(\partial x/\partial P)_T$ |
> |:---:|:---:|:---:|
> | $T$ | $1$ | $0$ |
> | $P$ | $0$ | $-1$ |
> | $v$ | $v\alpha$ | $v\kappa_T$ |
> | $s$ | $c_p/T$ | $v\alpha$ |
> | $u$ | $c_p - Pv\alpha$ | $v(T\alpha - \kappa_T P)$ |
> | $h$ | $c_p$ | $v(T\alpha - 1)$ |
> | $f$ | $-(Pv\alpha + s)$ | $-Pv\kappa_T$ |
> | $g$ | $-s$ | $-v$ |
>
> Con estos bloques, $(\partial x/\partial y)_z = J(x,z)/J(y,z)$ se calcula expandiendo el determinante $2\times2$.

---

## Derivar las relaciones de Maxwell con jacobianos

> [!demostracion]
> **3.ª relación de Maxwell** $(\partial s/\partial v)_T = (\partial P/\partial T)_v$:
>
> **Lado izquierdo:**
> $$\left(\frac{\partial s}{\partial v}\right)_T = \frac{J(s,T)}{J(v,T)} = \frac{v\alpha}{v\kappa_T} = \frac{\alpha}{\kappa_T}.$$
>
> **Lado derecho:**
> $$\left(\frac{\partial P}{\partial T}\right)_v = \frac{J(P,v)}{J(T,v)} = \frac{(\partial P/\partial T)_P(\partial v/\partial P)_T - (\partial P/\partial P)_T(\partial v/\partial T)_P}{(\partial T/\partial T)_P(\partial v/\partial P)_T - (\partial T/\partial P)_T(\partial v/\partial T)_P}.$$
> Con $(\partial P/\partial T)_P = 0$, $(\partial P/\partial P)_T = 1$, $(\partial T/\partial P)_T = 0$:
> $$= \frac{0\cdot(-v\kappa_T) - 1\cdot v\alpha}{1\cdot(-v\kappa_T) - 0\cdot v\alpha} = \frac{-v\alpha}{-v\kappa_T} = \frac{\alpha}{\kappa_T}.$$
>
> Ambos lados son $\alpha/\kappa_T$: la identidad se verifica. $\blacksquare$

---

## Derivar la relación $c_p - c_v$ con jacobianos

> [!demostracion]
> **Paso 1 — Expresar $c_v$ como jacobiano.** $c_v = T(\partial s/\partial T)_v$:
> $$\left(\frac{\partial s}{\partial T}\right)_v = \frac{J(s,v)}{J(T,v)}.$$
>
> **Calcular $J(s,v)$:**
> $$J(s,v) = \left(\frac{\partial s}{\partial T}\right)_P\!\left(\frac{\partial v}{\partial P}\right)_T - \left(\frac{\partial s}{\partial P}\right)_T\!\left(\frac{\partial v}{\partial T}\right)_P = \frac{c_p}{T}\cdot(-v\kappa_T) - (-v\alpha)\cdot v\alpha = -\frac{c_p v\kappa_T}{T} + v^2\alpha^2.$$
>
> **Calcular $J(T,v)$:**
> $$J(T,v) = 1\cdot(-v\kappa_T) - 0\cdot v\alpha = -v\kappa_T.$$
>
> **Paso 2 — Calcular $c_v$:**
> $$c_v = T\cdot\frac{J(s,v)}{J(T,v)} = T\cdot\frac{-c_pv\kappa_T/T + v^2\alpha^2}{-v\kappa_T} = c_p - \frac{Tv^2\alpha^2}{v\kappa_T} = c_p - \frac{Tv\alpha^2}{\kappa_T}.$$
>
> **Paso 3 — Resultado:**
> $$c_p - c_v = \frac{Tv\alpha^2}{\kappa_T}. \qquad \blacksquare$$
>
> La relación $c_p - c_v$ surge de forma mecánica del determinante jacobiano, sin necesidad de igualar las ecuaciones $T\,ds$ como en [[Cp Cv/index | $c_p - c_v$]].

---

## Relación con otras notas

> [!info]
> - La tabla de Bridgman es la herramienta operativa; el cálculo mecánico se aplica en [[Aplicaciones Termodinamicas]].
> - Reproduce como casos particulares las [[Maxwell | relaciones de Maxwell]] y la relación [[Cp Cv/index | $c_p - c_v$]].
> - Depende de los coeficientes $\alpha$, $\kappa_T$, $c_p$ definidos en el [[index | índice de Relaciones Termodinámicas]].

> [!referencia]
> Bridgman, *A Complete Collection of Thermodynamic Formulas* (1925); Callen, *Thermodynamics*, §7-4; Smith, Van Ness & Abbott, *Chemical Engineering Thermodynamics*, §6.4; Moran & Shapiro, §11.6.
