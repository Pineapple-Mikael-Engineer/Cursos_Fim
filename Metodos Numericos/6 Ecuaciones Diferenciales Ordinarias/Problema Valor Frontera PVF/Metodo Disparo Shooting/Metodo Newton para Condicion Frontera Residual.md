---
title: Método de Newton para la Condición de Frontera Residual
order: 2
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - valor-frontera
  - disparo
  - newton-raphson
draft: false
aliases:
  - Newton en el disparo
  - Residuo de frontera
  - Ecuación de sensibilidad
  - Newton shooting
---

# Método de Newton para la Condición de Frontera Residual

> [!definicion]
> En el [[Metodo Disparo Shooting/index|disparo]] de un PVF **no lineal**, el parámetro $s=y'(a)$ se ajusta resolviendo $\phi(s) = y(b;s) - \beta = 0$ por el [[Newton Raphson/index|método de Newton]]:
> $$s_{k+1} = s_k - \frac{\phi(s_k)}{\phi'(s_k)}.$$
> El reto es calcular $\phi'(s) = \partial y(b;s)/\partial s$, la sensibilidad de la solución a la pendiente inicial.

> [!info]
> Como $y(b;s)$ es el resultado de **integrar** un PVI, su derivada respecto a $s$ no es analítica. Se obtiene integrando una **ecuación de sensibilidad** (variacional) junto al PVI original, o aproximando con la secante. Es la combinación de dos capítulos: [[Problema Valor Inicial PVI/index|integración de EDOs]] y [[Newton Raphson/index|búsqueda de raíces]].

---

## La ecuación de sensibilidad (variacional)

> [!teorema]
> Sea $v(x) = \partial y(x;s)/\partial s$ la sensibilidad. Derivando el PVI $y'' = f(x,y,y')$ respecto a $s$ se obtiene la **ecuación variacional**:
> $$v'' = \frac{\partial f}{\partial y}\,v + \frac{\partial f}{\partial y'}\,v', \qquad v(a) = 0, \quad v'(a) = 1,$$
> y entonces $\phi'(s) = v(b)$.

> [!demostracion]
> Derivando $y'' = f(x,y,y')$ respecto al parámetro $s$ (con $x$ fijo), por la regla de la cadena:
> $$\frac{\partial y''}{\partial s} = f_y\frac{\partial y}{\partial s} + f_{y'}\frac{\partial y'}{\partial s} \;\Rightarrow\; v'' = f_y v + f_{y'}v'.$$
> Las condiciones iniciales salen de derivar $y(a)=\alpha$ (constante ⟹ $v(a)=0$) e $y'(a)=s$ (⟹ $v'(a)=1$). Integrando este sistema **junto** al original se obtiene $\phi'(s)=v(b)$ en la misma pasada.

> [!info]
> Se integra el **sistema ampliado** $(y, y', v, v')$ de una vez. Una sola integración da $\phi(s)$ **y** $\phi'(s)$, haciendo cada paso de Newton tan caro como una integración. Es exacto (hasta el error del integrador), a diferencia de la secante.

---

## Alternativa: secante (sin variacional)

> [!info]
> Si calcular $f_y, f_{y'}$ es engorroso, se aproxima $\phi'$ por diferencias y se usa la [[Metodo Secante Orden Convergencia Fi|secante]]:
> $$s_{k+1} = s_k - \phi(s_k)\frac{s_k - s_{k-1}}{\phi(s_k) - \phi(s_{k-1})}.$$
> No requiere la ecuación variacional (ni derivadas de $f$), solo dos integraciones por la diferencia. Converge superlinealmente ($\varphi\approx1.618$) en vez de cuadráticamente, pero es más simple — el mismo compromiso [[Comparacion Analitica Orden Convergencia|Newton vs secante]] del capítulo 3.

---

## Ejemplo

> [!ejemplo]
> **PVF no lineal $y'' = \frac{3}{2}y^2$, $y(0)=4$, $y(1)=1$** (problema clásico). Newton con ecuación variacional ($f_y = 3y$, $f_{y'}=0$ ⟹ $v''=3y\,v$):
>
> | $k$ | $s_k = y'(0)$ | $\phi(s_k) = y(1;s_k)-1$ |
> |:---:|:---:|:---:|
> | 0 | $-5$ | $+6.1$ |
> | 1 | $-8.2$ | $+1.8$ |
> | 2 | $-35.9$ | $-0.31$ |
> | 3 | $-35.86$ | $\sim10^{-4}$ |
>
> Converge a $s^*\approx-35.86$ (el problema tiene además una segunda solución, típico de PVF no lineales). Newton acelera al acercarse a la raíz; la secante daría una convergencia algo más lenta sin la variacional.

---

## Algoritmo

> [!algoritmo]
> **Disparo con Newton y ecuación de sensibilidad.**
>
> ```python
> import numpy as np
> from scipy.integrate import solve_ivp
>
> def disparo_newton(f, fy, fyp, a, b, alpha, beta, s0, tol=1e-8):
>     def ampliado(x, U):
>         y, yp, v, vp = U
>         return [yp, f(x, y, yp), vp, fy(x, y, yp)*v + fyp(x, y, yp)*vp]
>     s = s0
>     for _ in range(50):
>         sol = solve_ivp(ampliado, [a, b], [alpha, s, 0.0, 1.0], rtol=1e-10)
>         yb, vb = sol.y[0, -1], sol.y[2, -1]
>         phi = yb - beta
>         if abs(phi) < tol:
>             return s
>         s -= phi / vb                          # paso de Newton, φ'(s) = v(b)
>     return s
> ```

---

## Dificultades

> [!warning]
> - **PVI sensible:** si el PVI es inestable (crece exponencialmente), pequeñas variaciones de $s$ producen enormes cambios en $y(b)$: $\phi(s)$ es casi vertical y Newton se vuelve frágil. Es el talón de Aquiles del disparo, que motiva el **disparo múltiple** (subdividir el intervalo) o las [[Comparacion Disparo vs Diferencias Finitas|diferencias finitas]].
> - **Múltiples soluciones:** los PVF no lineales pueden tener varias soluciones; Newton converge a una u otra según $s_0$.

---

## Relación con otras notas

> [!info]
> - La parametrización que define $\phi(s)$: [[Transformacion PVF a PVI Valor Inicial Desconocido]].
> - El método de raíces empleado: [[Newton Raphson/index]] y [[Metodo Secante Orden Convergencia Fi]].
> - La integración del sistema ampliado: [[Acoplamiento Metodos Sistemas Runge Kutta]].
> - Cuándo el disparo falla frente a diferencias finitas: [[Comparacion Disparo vs Diferencias Finitas]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Iteración | $s_{k+1} = s_k - \phi(s_k)/\phi'(s_k)$ |
| Residuo | $\phi(s) = y(b;s) - \beta$ |
| Derivada | $\phi'(s) = v(b)$, ecuación variacional |
| Variacional | $v'' = f_y v + f_{y'}v'$, $v(a)=0$, $v'(a)=1$ |
| Alternativa | secante (sin derivadas) |
| Riesgo | PVI sensible, múltiples soluciones |

> [!corolario]
> En el disparo no lineal, el parámetro $s$ se ajusta por [[Newton Raphson/index|Newton]] sobre el residuo $\phi(s)=y(b;s)-\beta$, cuya derivada $\phi'(s)=v(b)$ se obtiene integrando la ecuación variacional $v''=f_yv+f_{y'}v'$ junto al PVI —una sola pasada da $\phi$ y $\phi'$—. La [[Metodo Secante Orden Convergencia Fi|secante]] evita la variacional a costa de convergencia superlineal. El método combina integración de EDOs y búsqueda de raíces, pero hereda la fragilidad del disparo cuando el PVI es sensible, lo que orienta hacia el disparo múltiple o las [[Comparacion Disparo vs Diferencias Finitas|diferencias finitas]].
