---
title: Perdida Significancia y Cancelacion Catastrofica
tags:
  - metodos-numericos
  - teoria
  - error-numerico
  - estabilidad-numerica
draft: false
aliases:
  - Cancelación catastrófica
  - Pérdida de dígitos significativos
  - Resta cancelativa
---

# Pérdida de Significancia y Cancelación Catastrófica

> [!definicion]
> La **cancelación catastrófica** es la pérdida masiva de dígitos significativos que ocurre al restar dos números de magnitud similar que ya contienen error de redondeo debido a la [[Representacion Punto Flotante IEEE 754|representación finita]].

El fenómeno es *catastrófico* porque el error relativo del resultado puede ser órdenes de magnitud mayor que la [[Epsilon Maquina y Precision Relativa|unidad de redondeo]] $u$, incluso cuando los operandos individuales tienen error relativo $\leq u$.

---

## Mecanismo del error

Supongamos que tenemos dos números $\tilde{a}$ y $\tilde{b}$ que son aproximaciones flotantes de valores exactos $a$ y $b$. Por la propiedad del redondeo:
$$\tilde{a} = a(1 + \delta_a), \quad \tilde{b} = b(1 + \delta_b), \quad |\delta_a|, |\delta_b| \leq u$$

Al calcular la diferencia $\tilde{a} - \tilde{b}$:

$$
\begin{align*}
\tilde{a} - \tilde{b} &= a(1 + \delta_a) - b(1 + \delta_b) \\
&= (a - b) + (a\delta_a - b\delta_b)
\end{align*}
$$

> [!teoria]
> **Amplificación del error relativo.**
> El error relativo de la diferencia es:
> $$\frac{|(\tilde{a} - \tilde{b}) - (a - b)|}{|a - b|} = \frac{|a\delta_a - b\delta_b|}{|a - b|}$$
> 
> Si $a \approx b$, el denominador $|a - b|$ es muy pequeño, mientras que el numerador $|a\delta_a - b\delta_b|$ es proporcional a $|a|u$. Esto produce un factor de amplificación $\approx |a| / |a - b| \gg 1$.

En el peor caso, cuando $a$ y $b$ coinciden en sus primeros $k$ dígitos significativos, la resta elimina esos $k$ dígitos, dejando solo los dígitos contaminados por el error de redondeo preexistente.

> [!ejemplo]
> **Ilustración numérica con precisión finita.**
> 
> Supongamos que trabajamos con $5$ dígitos decimales de precisión. Sean:
> $$\tilde{a} = 1.2345 \times 10^0, \quad \tilde{b} = 1.2344 \times 10^0$$
> 
> Ambos tienen error relativo $\approx 10^{-5}$ respecto a sus valores exactos.
> 
> La diferencia es $\tilde{a} - \tilde{b} = 0.0001 \times 10^0 = 1.0000 \times 10^{-4}$.
> 
> Ahora, si el valor exacto de $a$ era $1.234567\dots$ y el de $b$ era $1.234432\dots$, la diferencia exacta es $0.000135\dots$
> 
> El error relativo del resultado es:
> $$\frac{|0.000100 - 0.000135|}{0.000135} \approx 0.26 = 26\%$$
> 
> De $5$ dígitos de precisión en los operandos, ¡el resultado tiene apenas $1$ dígito significativo correcto!

---

## Ejemplo clásico: Raíces de la ecuación cuadrática

> [!ejemplo]
> **Cancelación en la fórmula cuadrática estándar.**
> 
> Para $ax^2 + bx + c = 0$ con $a=1$, $b=10^8$, $c=1$:
> $$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$
> 
> **Análisis en Python:**
> ```python
> import math
> 
> a, b, c = 1.0, 1e8, 1.0
> 
> # Método directo (inestable)
> discriminante = math.sqrt(b**2 - 4*a*c)
> x1_directo = (-b + discriminante) / (2*a)
> x2_directo = (-b - discriminante) / (2*a)
> 
> print(f"x1 (directo): {x1_directo:.16e}")
> print(f"x2 (directo): {x2_directo:.16e}")
> ```
> 
> Salida típica:
> ```
> x1 (directo): -1.4901161193847656e-08
> x2 (directo): -1.0000000000000000e+08
> ```
> 
> La raíz $x_1$ exacta es aproximadamente $-10^{-8}$. El valor calculado tiene solo $7$-$8$ dígitos correctos en lugar de $16$.
> 
> **Causa:** $\sqrt{b^2 - 4ac} \approx 10^8 - 2 \times 10^{-8}$. Al calcular $-b + \sqrt{\cdots}$, se cancelan los primeros $8$ dígitos, dejando solo los dígitos afectados por el redondeo en el cálculo de la raíz cuadrada.

---

## Cancelación en evaluación de funciones

> [!ejemplo]
> **Evaluación de $f(x) = \frac{1 - \cos x}{x^2}$ para $x \approx 0$.**
> 
> ```python
> import math
> 
> def f_inestable(x):
>     return (1 - math.cos(x)) / (x**2)
> 
> def f_estable(x):
>     # Identidad trigonométrica: 1 - cos(x) = 2 sin^2(x/2)
>     if x == 0:
>         return 0.5
>     return 2 * (math.sin(x/2) / x)**2
> 
> x = 1e-8
> print(f"Método inestable: {f_inestable(x):.16f}")
> print(f"Método estable:    {f_estable(x):.16f}")
> print("Valor exacto:      0.5000000000000000")
> ```
> 
> Salida típica:
> ```
> Método inestable: 0.0000000000000000
> Método estable:    0.5000000000000000
> Valor exacto:      0.5000000000000000
> ```
> 
> **Explicación:** Para $x = 10^{-8}$, $\cos x \approx 1 - 5 \times 10^{-17}$. La resta $1 - \cos x$ produce $5 \times 10^{-17}$, pero con pérdida de precisión porque $1$ y $\cos x$ coinciden en $16$ dígitos. El método estable usa una identidad trigonométrica que evita la resta cancelativa.
> ![[Error_Funcion_estable_inestable.png]]



---

## Cancelación en sumas acumulativas

> [!ejemplo]
> **Suma de una serie alternante.**
> 
> Calculemos $S = \sum_{k=1}^{\infty} \frac{(-1)^{k+1}}{k} = \ln 2 \approx 0.6931471805599453$.
> 
> ```python
> def suma_directa(n):
>     s = 0.0
>     signo = 1.0
>     for k in range(1, n + 1):
>         s += signo / k
>         signo = -signo
>     return s
> 
> def suma_por_partes(n):
>     s_pos = sum(1.0 / k for k in range(1, n + 1, 2))
>     s_neg = sum(1.0 / k for k in range(2, n + 1, 2))
>     return s_pos - s_neg
> 
> n = 10_000_000
> print(f"Suma directa:    {suma_directa(n):.16f}")
> print(f"Suma por partes: {suma_por_partes(n):.16f}")
> print(f"Valor exacto:    {math.log(2):.16f}")
> ```
> Salida:
>```
>Suma directa:    0.6931471305601064
>Suma por partes: 0.6931471305598418
>Valor exacto:    0.6931471805599453
>``` 
> **Observación:** La suma directa sufre cancelación en cada paso al alternar signos. La suma por partes (agrupando positivos y negativos por separado) retiene mayor precisión. Para análisis detallado del error en sumas, véase [[Propagacion Errores Operaciones Matriciales]].

---

## Estrategias para mitigar la cancelación catastrófica

La cancelación catastrófica es un problema del **algoritmo**, no de la precisión del hardware. Aumentar la precisión (ej. usar `float128`) solo pospone el problema, no lo elimina.

> [!info]
> **Técnicas estándar de mitigación:**
> 
> 1. **Reformulación algebraica:** Usar identidades que eviten la resta (racionalización, expansiones en serie).
> 2. **Reordenamiento de operaciones:** Agrupar términos del mismo signo antes de restar.
> 3. **Uso de expansiones de Taylor:** Evaluar funciones cerca de puntos singulares mediante series.
> 4. **Algoritmos compensados:** Como la [[Suma de Kahan]], que mantiene un término de corrección para el error de redondeo.

Cada una de estas estrategias se estudia en el contexto de [[Estabilidad Algoritmos Forward Backward]].

> [!ejemplo]
> **Racionalización para $f(x) = \sqrt{x+1} - \sqrt{x}$.**
> 
> La expresión es inestable para $x$ grande. Multiplicando y dividiendo por el conjugado:
> $$f(x) = \frac{(x+1) - x}{\sqrt{x+1} + \sqrt{x}} = \frac{1}{\sqrt{x+1} + \sqrt{x}}$$
> 
> Esta forma **no contiene resta cancelativa** y es numéricamente estable para todo $x > 0$.

---

## Relación con el número de condición

Es crucial distinguir entre **condicionamiento del problema** y **estabilidad del algoritmo**.

> [!warning]
> **Cancelación catastrófica vs. Mal condicionamiento.**
> - La cancelación catastrófica es un artefacto de **cómo** se calcula (inestabilidad algorítmica).
> - El [[Condicionamiento Numerico Numero Condicion|mal condicionamiento]] es una propiedad intrínseca del problema matemático, independiente del algoritmo.
> 
> Una resta de números cercanos puede ser un problema **bien condicionado** (si los operandos son exactos, la diferencia se calcula con alta precisión relativa), pero si los operandos ya vienen con error, el algoritmo se vuelve inestable.

---

## Ejemplo adicional: Cálculo de la varianza

> [!ejemplo]
> **Fórmula clásica vs. fórmula de dos pasadas.**
> 
> La varianza de un conjunto $\{x_1, \dots, x_n\}$ puede calcularse como:
> $$\sigma^2 = \frac{1}{n}\sum x_i^2 - \left(\frac{1}{n}\sum x_i\right)^2 \quad \text{(Inestable)}$$
> 
> Esta fórmula sufre cancelación catastrófica cuando la media es grande comparada con la desviación estándar.
> 
> ```python
> import numpy as np
> 
> # Datos con media grande y pequeña varianza
> x = np.array([1e8 + 1, 1e8 + 2, 1e8 + 3])
> n = len(x)
> 
> # Método inestable (fórmula de una pasada)
> var_inestable = np.mean(x**2) - np.mean(x)**2
> 
> # Método estable (dos pasadas)
> media = np.mean(x)
> var_estable = np.mean((x - media)**2)
> 
> print(f"Varianza inestable: {var_inestable:.16f}")
> print(f"Varianza estable:    {var_estable:.16f}")
> print("Valor exacto:        0.6666666666666666")
> ```
> 
> Salida típica:
> ```
> Varianza inestable: 0.6666666666278616
> Varianza estable:    0.6666666666666666
> Valor exacto:        0.6666666666666666
> ```
> 
> La fórmula inestable pierde dígitos porque $\sum x_i^2 \approx 3 \times 10^{16}$ y $(\sum x_i)^2/n \approx 3 \times 10^{16}$, y su diferencia es solo $0.666\dots$
