---
title: Plancha N-01
order: 1
tags:
  - metodos-numericos
draft: false
---

# Problema 01

Considérese el sistema lineal:

$$
\begin{bmatrix}
3 & -a & 0 & 0 \\
-a & 4 & -a & 0 \\
0 & -a & 5 & -a \\
0 & 0 & -a & 6
\end{bmatrix}
\begin{bmatrix}
x \\
y \\
z \\
w
\end{bmatrix}
=
\begin{bmatrix}
4-a \\
7-2a \\
7 \\
-4-a
\end{bmatrix}
$$

Se pide:

1. Determinar para qué valores de $a$ el método de Jacobi converge por criterio de diagonal estrictamente dominante.
2. Determinar para qué valores de $a$ converge por criterio del radio espectral.
3. Tomando $a=\frac{1}{2}$:
   - realizar iteraciones de Jacobi con vector inicial nulo,
   - estimar el error en cada iteración hasta obtener precisión $0.01$,
   - indicar la fórmula de error utilizada,
   - comentar los resultados de convergencia,
   - desarrollar explícitamente las dos primeras iteraciones.

---

# Inciso A — Criterio de diagonal estrictamente dominante

> [!definicion]
> Una matriz $A=(a_{ij})$ es estrictamente dominante por filas si:
>
> $$
> |a_{ii}| > \sum_{j \neq i} |a_{ij}|
> $$
>
> para toda fila $i$.

La matriz del sistema es:

$$
A=
\begin{bmatrix}
3 & -a & 0 & 0 \\
-a & 4 & -a & 0 \\
0 & -a & 5 & -a \\
0 & 0 & -a & 6
\end{bmatrix}
$$

Analizando fila por fila:

$$
\begin{aligned}
3 &> |a| \\
4 &> 2|a| \\
5 &> 2|a| \\
6 &> |a|
\end{aligned}
$$

Las restricciones equivalentes son:

$$
\begin{aligned}
|a| &< 3 \\
|a| &< 2 \\
|a| &< \frac{5}{2} \\
|a| &< 6
\end{aligned}
$$

La condición más restrictiva es:

$$
|a| < 2
$$

Por lo tanto:

> [!teorema]
> El método de Jacobi converge por criterio de diagonal estrictamente dominante si:
>
> $$
> -2 < a < 2
> $$

> [!info]
> Debido a la simetría de la matriz, las condiciones por columnas coinciden exactamente con las obtenidas por filas.

---

# Inciso B — Criterio del radio espectral

## Descomposición de Jacobi

> [!definicion]
> El método de Jacobi utiliza la descomposición:
>
> $$
> A = D - (L+U)
> $$
>
> donde:
>
> - $D$ contiene la diagonal de $A$,
> - $L$ la parte inferior,
> - $U$ la parte superior.

En este caso:

$$
D=
\begin{bmatrix}
3 & 0 & 0 & 0 \\
0 & 4 & 0 & 0 \\
0 & 0 & 5 & 0 \\
0 & 0 & 0 & 6
\end{bmatrix}
$$

y

$$
L+U=
\begin{bmatrix}
0 & a & 0 & 0 \\
a & 0 & a & 0 \\
0 & a & 0 & a \\
0 & 0 & a & 0
\end{bmatrix}
$$

La iteración de Jacobi queda:

$$
y^{(k+1)} = T_J y^{(k)} + C
$$

donde:

$$
T_J = D^{-1}(L+U)
$$

y

$$
C=D^{-1}b
$$

Por lo tanto:

$$
T_J=
\begin{bmatrix}
0 & \frac{a}{3} & 0 & 0 \\
\frac{a}{4} & 0 & \frac{a}{4} & 0 \\
0 & \frac{a}{5} & 0 & \frac{a}{5} \\
0 & 0 & \frac{a}{6} & 0
\end{bmatrix}
$$

---

## Polinomio característico

Se calcula:

$$
\det(T_J-\lambda I)=0
$$

obteniéndose:

$$
\lambda^4
-\frac{a^2}{4}\lambda^2
+\frac{a^4}{360}
=0
$$

Definiendo:

$$
\mu=\lambda^2
$$

se obtiene la ecuación cuadrática:

$$
\mu^2-\frac{a^2}{4}\mu+\frac{a^4}{360}=0
$$

Aplicando fórmula general:

$$
\mu=
\frac{a^2}{8}
\left(
1 \pm \sqrt{\frac{7}{15}}
\right)
$$

Luego:

$$
\lambda=
\pm |a|
\sqrt{
\frac{1}{8}
\left(
1 \pm \sqrt{\frac{7}{15}}
\right)
}
$$

---

## Condición de convergencia

> [!teorema]
> El método de Jacobi converge si y solo si:
>
> $$
> \rho(T_J)<1
> $$

El mayor autovalor en magnitud es:

$$
\rho(T_J)
=
|a|
\sqrt{
\frac{1}{8}
\left(
1+\sqrt{\frac{7}{15}}
\right)
}
$$

Imponiendo:

$$
\rho(T_J)<1
$$

se obtiene:

$$
|a|
<
\frac{
1
}{
\sqrt{
\frac{1}{8}
\left(
1+\sqrt{\frac{7}{15}}
\right)
}
}
$$

Numéricamente:

$$
|a| < 2.34445701573
$$

Por lo tanto:

> [!corolario]
> El método de Jacobi converge por criterio espectral si:
>
> $$
> -2.1801489018 < a < 2.1801489018
> $$

> [!info]
> El criterio espectral es más fuerte que el de diagonal dominante estricta. Existen valores de $a$ para los cuales la matriz no es diagonal dominante pero Jacobi aún converge.

---

# Inciso C — Iteraciones de Jacobi para $a=\frac{1}{2}$

Tomando:

$$
a=\frac{1}{2}
$$

la matriz iterativa es:

$$
T_J=
\begin{bmatrix}
0 & \frac{1}{6} & 0 & 0 \\
\frac{1}{8} & 0 & \frac{1}{8} & 0 \\
0 & \frac{1}{10} & 0 & \frac{1}{10} \\
0 & 0 & \frac{1}{12} & 0
\end{bmatrix}
$$

y

$$
C=
\begin{bmatrix}
\frac{7}{6} \\
\frac{3}{2} \\
\frac{7}{5} \\
-\frac{3}{4}
\end{bmatrix}
$$

La iteración queda:

$$
y^{(k+1)} = T_J y^{(k)} + C
$$

con:

$$
y^{(0)}=
\begin{bmatrix}
0\\
0\\
0\\
0
\end{bmatrix}
$$

---

# Primera iteración

> [!algoritmo]
> Se utiliza:
>
> $$
> y^{(1)} = T_J y^{(0)} + C
> $$

Como:

$$
T_J y^{(0)} = 0
$$

entonces:

$$
y^{(1)}=
\begin{bmatrix}
1.16666667 \\
1.50000000 \\
1.40000000 \\
-0.75000000
\end{bmatrix}
$$

---

# Segunda iteración

Primero se calcula:

$$
T_J y^{(1)}
=
\begin{bmatrix}
0.25000000 \\
0.32083333 \\
0.07500000 \\
0.11666667
\end{bmatrix}
$$

Luego:

$$
y^{(2)}
=
T_J y^{(1)}+C
$$

por lo que:

$$
y^{(2)}
=
\begin{bmatrix}
1.41666667 \\
1.82083333 \\
1.47500000 \\
-0.63333333
\end{bmatrix}
$$

---

# Fórmulas de error

> [!definicion]
> Se define el error absoluto iterativo como:
>
> $$
> \Delta^{(k)}
> =
> \left\|
> y^{(k)}-y^{(k-1)}
> \right\|_\infty
> $$

> [!definicion]
> El error relativo aproximado se define como:
>
> $$
> \tau^{(k)}
> =
> \frac{
> \left\|
> y^{(k)}-y^{(k-1)}
> \right\|_\infty
> }{
> \left\|
> y^{(k)}
> \right\|_\infty
> }
> $$

---

# Iteraciones posteriores

Continuando las iteraciones:

$$
y^{(4)}
=
\begin{bmatrix}
1.47690972 \\
1.87361111 \\
1.52343750 \\
-0.62343750
\end{bmatrix}
$$

y los errores obtenidos son:

$$
\Delta^{(4)}
=
0.01512610
$$

$$
\tau^{(4)}
=
0.00521862
$$

Como:

$$
\tau^{(4)} < 0.01
$$

la precisión requerida ya ha sido alcanzada.

---

# Comentarios sobre la convergencia

> [!info]
> Para $a=\frac{1}{2}$ se cumple:
>
> $$
> \rho(T_J)<1
> $$
>
> por lo tanto el método converge.
>
> Además:
>
> - La matriz es estrictamente dominante.
> - Los errores disminuyen en cada iteración.
> - La convergencia es relativamente rápida debido a que el radio espectral es pequeño.
> - El vector iterativo se estabiliza rápidamente alrededor de la solución exacta.

---

# Problema 02

Una masa $m_{1}$ sobre una superficie horizontal rugosa se conecta a una segunda masa $m_{2}$ que se mueve verticalmente por medio de una cuerda de peso despreciable sobre una polea sin fricción.

Una fuerza de magnitud $F$ forma un ángulo agudo $\theta$ con la horizontal y se aplica sobre $m_{1}$.

La aceleración del sistema está dada por:

$$
a=
\frac{
F(\cos\theta+\mu\sin\theta)-g(m_2+\mu m_1)
}{
m_1+m_2
}
$$

donde:

$$
\begin{aligned}
F &=100\text{ N} \\
\mu &=0.2 \\
g &=9.8\frac{m}{s^2} \\
m_1 &=10\text{ kg} \\
m_2 &=5\text{ kg}
\end{aligned}
$$

Se desea hallar el ángulo $\theta$ para que:

$$
a=1.5\frac{m}{s^2}
$$

---

# Planteamiento de la ecuación

Sustituyendo los datos:

$$
1.5=
\frac{
100(\cos\theta+0.2\sin\theta)-9.8(5+0.2(10))
}{
10+5
}
$$

Calculando:

$$
9.8(5+2)=68.6
$$

y:

$$
1.5(15)=22.5
$$

Entonces:

$$
22.5=
100(\cos\theta+0.2\sin\theta)-68.6
$$

por lo tanto:

$$
100(\cos\theta+0.2\sin\theta)=91.1
$$

Finalmente:

$$
\cos\theta+0.2\sin\theta=0.911
$$

Definimos:

$$
f(\theta)=\cos\theta+0.2\sin\theta-0.911
$$

y buscamos:

$$
f(\theta)=0
$$

---

# Inciso A — Localización de raíces

> [!definicion]
> Una raíz de $f(x)$ se encuentra en un intervalo $[a,b]$ si:
>
> $$
> f(a)f(b)<0
> $$
>
> es decir, existe cambio de signo.

Se evalúa la función en intervalos de longitud $0.5$ radianes.

| Intervalo | $f(a)$ | $f(b)$ | Cambio de signo |
|---|---:|---:|---|
| $[0,0.5]$ | $0.089$ | $0.061$ | No |
| $[0.5,1.0]$ | $0.061$ | $-0.202$ | Sí |

Por lo tanto:

> [!teorema]
> Existe una raíz en el intervalo:
>
> $$
> [0.5,1.0]
> $$

> [!info]
> Debido a que el problema especifica un ángulo agudo, únicamente interesa la raíz positiva en:
>
> $$
> 0<\theta<\frac{\pi}{2}
> $$

---

# Inciso B — Método de Bisección

## Fórmula del método

> [!algoritmo]
> Dado un intervalo $[a,b]$, el punto medio se calcula como:
>
> $$
> c=\frac{a+b}{2}
> $$
>
> Luego:
>
> - si $f(a)f(c)<0$, la raíz pertenece a $[a,c]$,
> - si $f(c)f(b)<0$, la raíz pertenece a $[c,b]$.

El error estimado en bisección es:

$$
E^{(k)}=
\frac{b-a}{2}
$$

---

# Iteración 1

Intervalo inicial:

$$
[a,b]=[0.5,1.0]
$$

Punto medio:

$$
c_1=\frac{0.5+1.0}{2}=0.75
$$

Evaluando:

$$
f(0.75)\approx -0.0478
$$

Como:

$$
f(0.5)>0
\quad\text{y}\quad
f(0.75)<0
$$

la raíz pertenece a:

$$
[0.5,0.75]
$$

Error estimado:

$$
E^{(1)}=\frac{1.0-0.5}{2}=0.25
$$

---

# Iteración 2

Nuevo intervalo:

$$
[0.5,0.75]
$$

Punto medio:

$$
c_2=\frac{0.5+0.75}{2}=0.625
$$

Evaluando:

$$
f(0.625)\approx 0.0127
$$

Como:

$$
f(0.625)>0
\quad\text{y}\quad
f(0.75)<0
$$

la raíz pertenece a:

$$
[0.625,0.75]
$$

Error estimado:

$$
E^{(2)}=\frac{0.75-0.5}{2}=0.125
$$

---

# Iteración 3

Nuevo intervalo:

$$
[0.625,0.75]
$$

Punto medio:

$$
c_3=\frac{0.625+0.75}{2}=0.6875
$$

Evaluando:

$$
f(0.6875)\approx -0.0157
$$

Como:

$$
f(0.625)>0
\quad\text{y}\quad
f(0.6875)<0
$$

la raíz pertenece a:

$$
[0.625,0.6875]
$$

Error estimado:

$$
E^{(3)}=\frac{0.75-0.625}{2}=0.0625
$$

---

# Resultado aproximado por bisección

> [!corolario]
> Luego de tres iteraciones:
>
> $$
> \theta \approx 0.6875 \text{ rad}
> $$
>
> con error estimado:
>
> $$
> E^{(3)}=0.0625
> $$

---

# Inciso C — Método de Newton-Raphson

## Fórmula iterativa

> [!algoritmo]
> El método de Newton-Raphson utiliza:
>
> $$
> x_{n+1}
> =
> x_n
> -
> \frac{f(x_n)}{f'(x_n)}
> $$

La función es:

$$
f(\theta)=\cos\theta+0.2\sin\theta-0.911
$$

Su derivada:

$$
f'(\theta)=-\sin\theta+0.2\cos\theta
$$

Tomamos como aproximación inicial el valor obtenido por bisección:

$$
\theta_0=0.6875
$$

---

# Iteración 1

Evaluando:

$$
f(0.6875)\approx -0.0157
$$

$$
f'(0.6875)\approx -0.4786
$$

Entonces:

$$
\theta_1
=
0.6875
-
\frac{-0.0157}{-0.4786}
$$

$$
\theta_1\approx 0.6547
$$

Error aproximado:

$$
E^{(1)}
=
|\theta_1-\theta_0|
\approx 0.0328
$$

---

# Iteración 2

Evaluando:

$$
f(0.6547)\approx -0.0005
$$

$$
f'(0.6547)\approx -0.4490
$$

Entonces:

$$
\theta_2
=
0.6547
-
\frac{-0.0005}{-0.4490}
$$

$$
\theta_2\approx 0.6536
$$

Error aproximado:

$$
E^{(2)}
=
|\theta_2-\theta_1|
\approx 0.0011
$$

---

# Iteración 3

Evaluando:

$$
f(0.6536)\approx -1.2\times10^{-6}
$$

$$
f'(0.6536)\approx -0.4480
$$

Entonces:

$$
\theta_3
=
0.6536
-
\frac{-1.2\times10^{-6}}{-0.4480}
$$

$$
\theta_3\approx 0.6536
$$

Error aproximado:

$$
E^{(3)}
\approx 2.7\times10^{-6}
$$

---

# Comentarios sobre la convergencia

> [!info]
> El método de Newton-Raphson converge mucho más rápido que bisección.
>
> Observaciones:
>
> - Bisección posee convergencia lineal.
> - Newton-Raphson posee convergencia cuadrática cerca de la raíz.
> - Después de tres iteraciones, Newton-Raphson alcanza una precisión extremadamente alta.
> - El valor hallado corresponde a:
>
> $$
> \theta \approx 0.6536\text{ rad}
> $$
>
> equivalente aproximadamente a:
>
> $$
> \theta \approx 37.45^\circ
> $$

---

# Resumen final

> [!corolario]
> La ecuación no lineal asociada al problema es:
>
> $$
> \cos\theta+0.2\sin\theta-0.911=0
> $$
>
> Resultados:
>
> - La raíz se localiza en:
>
> $$
> [0.5,1.0]
> $$
>
> - Bisección después de 3 iteraciones:
>
> $$
> \theta \approx 0.6875
> $$
>
> - Newton-Raphson después de 3 iteraciones:
>
> $$
> \theta \approx 0.6536
> $$
>
> - El valor físico buscado es:
>
> $$
> \boxed{
> \theta \approx 0.6536\text{ rad}
> }
> $$