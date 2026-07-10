---
title: Euler Implícito y Estabilidad Incondicional
order: 3
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - valor-inicial
  - euler-taylor
  - estabilidad
draft: false
aliases:
  - Euler implícito
  - Backward Euler
  - Euler hacia atrás
  - Estabilidad incondicional
---

# Euler Implícito y Estabilidad Incondicional

> [!definicion]
> El **método de Euler implícito** (o hacia atrás) evalúa la pendiente en el punto de **llegada** $t_{n+1}$:
> $$y_{n+1} = y_n + h\,f(t_{n+1},\, y_{n+1}).$$
> Como $y_{n+1}$ aparece en ambos lados, cada paso requiere **resolver una ecuación** (lineal o no lineal).

> [!info]
> Comparte el orden 1 de [[Euler Explicito Orden 1 Interpretacion Geometrica|Euler explícito]], pero gana **estabilidad incondicional**: cualquier paso $h$ produce una solución acotada para problemas disipativos. Es la herramienta básica para sistemas [[Rigidez Stiffness Problemas Ingenieria|rígidos]], donde la estabilidad —no la precisión— limita el paso.

---

## Por qué es implícito

> [!teoria]
> Euler explícito calcula $y_{n+1}$ directamente; el implícito lo deja **dentro** de $f$. Para EDOs lineales $y'=\lambda y$ se despeja:
> $$y_{n+1} = y_n + h\lambda y_{n+1} \;\Rightarrow\; y_{n+1} = \frac{y_n}{1 - h\lambda}.$$
> Para $f$ no lineal, cada paso resuelve $g(y_{n+1}) = y_{n+1} - y_n - hf(t_{n+1},y_{n+1}) = 0$ por [[Newton Raphson Multivariable/index|Newton]], lo que exige la jacobiana de $f$.

---

## Estabilidad incondicional

> [!teorema]
> Aplicado a la ecuación de prueba $y'=\lambda y$ con $\operatorname{Re}(\lambda)<0$, el factor de amplificación de Euler implícito es
> $$R(z) = \frac{1}{1 - z}, \qquad z = h\lambda.$$
> Como $|R(z)| < 1$ para **todo** $z$ con $\operatorname{Re}(z)<0$, el método es **A-estable**: estable para cualquier paso $h>0$.

> [!demostracion]
> De $y_{n+1} = y_n/(1-z)$ se sigue $y_n = R(z)^n y_0$ con $R(z) = 1/(1-z)$. Para $\operatorname{Re}(z)<0$, $|1-z|^2 = (1-\operatorname{Re}z)^2 + (\operatorname{Im}z)^2 > 1$, luego $|R(z)|<1$ y $y_n\to0$, replicando el decaimiento exacto. La [[Regiones Estabilidad Absoluta A Estabilidad|región de estabilidad]] contiene **todo** el semiplano izquierdo (y más).

> [!info]
> Contraste con [[Euler Explicito Orden 1 Interpretacion Geometrica|Euler explícito]], cuyo factor es $R(z)=1+z$ y exige $|1+z|\leq1$ (un disco pequeño): pasos grandes lo hacen explotar. El implícito nunca explota, a cambio de resolver una ecuación por paso.

---

## Ejemplo: sistema rígido

> [!ejemplo]
> **$y' = -100(y - \cos t) - \sin t$, $y(0)=0$** (rígido: $\lambda=-100$, escala rápida $1/100$, solución suave $y\approx\cos t$).
>
> | $h$ | Euler explícito | Euler implícito |
> |:---:|:---|:---|
> | 0.01 | estable | estable |
> | 0.05 | **explota** ($\|1+h\lambda\|=4$) | estable |
> | 0.5 | explota catastróficamente | estable, sigue $\cos t$ |
>
> Euler explícito requiere $h < 2/100 = 0.02$ por **estabilidad**, aunque la solución sea suave. Euler implícito usa $h=0.5$ sin problema: la rigidez no lo afecta. Esta es la razón de ser de los métodos implícitos.

---

## Algoritmo

> [!algoritmo]
> **Euler implícito (caso no lineal, con Newton interno).**
>
> ```python
> import numpy as np
>
> def euler_implicito(f, jac, t0, y0, h, N):
>     t, y = t0, np.array(y0, float)
>     traj = [y.copy()]
>     for n in range(N):
>         tn1 = t + h
>         z = y.copy()                                  # iterada inicial
>         for _ in range(20):                           # Newton para g(z)=0
>             g  = z - y - h * f(tn1, z)
>             Jg = np.eye(len(z)) - h * jac(tn1, z)     # jacobiana de g
>             dz = np.linalg.solve(Jg, -g)
>             z += dz
>             if np.linalg.norm(dz) < 1e-12:
>                 break
>         y, t = z, tn1
>         traj.append(y.copy())
>     return np.array(traj)
> ```

---

## Costo frente a beneficio

> [!info]
> | | Explícito | Implícito |
> |:---|:---|:---|
> | Costo por paso | 1 evaluación de $f$ | resolver sistema (Newton + jacobiana) |
> | Paso máximo | limitado por estabilidad | ilimitado |
> | Problema no rígido | preferible (barato) | innecesariamente caro |
> | Problema [[Rigidez Stiffness Problemas Ingenieria\|rígido]] | inviable ($h$ minúsculo) | **imprescindible** |

> [!warning]
> Euler implícito es **demasiado disipativo** para sistemas conservativos: amortigua artificialmente las oscilaciones (un péndulo simulado se "frena" hasta pararse). Para mecánica conservativa no se usa ni el explícito (gana energía) ni el implícito (pierde energía), sino los [[Integradores Simplecticos Conservacion|métodos simplécticos]].

---

## Relación con otras notas

> [!info]
> - La variante explícita y su inestabilidad: [[Euler Explicito Orden 1 Interpretacion Geometrica]].
> - El análisis general de estabilidad: [[Regiones Estabilidad Absoluta A Estabilidad]].
> - El problema que justifica los implícitos: [[Rigidez Stiffness Problemas Ingenieria]].
> - El sistema interno que se resuelve: [[Newton Raphson Multivariable/index]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Fórmula | $y_{n+1} = y_n + hf(t_{n+1}, y_{n+1})$ |
| Cálculo | resolver ecuación (Newton) |
| Factor | $R(z) = 1/(1-z)$ |
| Estabilidad | A-estable (incondicional) |
| Orden | 1 |
| Idóneo | sistemas rígidos |

> [!corolario]
> Euler implícito evalúa la pendiente en el punto de llegada, $y_{n+1}=y_n+hf(t_{n+1},y_{n+1})$, lo que obliga a resolver una ecuación por paso pero otorga estabilidad incondicional: su factor $R(z)=1/(1-z)$ cumple $|R|<1$ en todo el semiplano izquierdo (A-estabilidad). Por eso es la base para sistemas [[Rigidez Stiffness Problemas Ingenieria|rígidos]], donde [[Euler Explicito Orden 1 Interpretacion Geometrica|Euler explícito]] exigiría pasos minúsculos. Su contrapartida es ser disipativo —amortigua oscilaciones físicas reales—, por lo que la mecánica conservativa requiere [[Integradores Simplecticos Conservacion|integradores simplécticos]], no implícitos.
