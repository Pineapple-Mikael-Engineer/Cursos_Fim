---
title: Problemas Realistas — Parcial de Métodos Numéricos
tags:
  - metodos-numericos
  - parcial-realista
  - jacobi
  - gauss-seidel
  - LU
  - newton
  - matlab
draft: true
---

# Problema 01 — Jacobi y Radio Espectral

Considérese el sistema:

$$
\begin{bmatrix}
5 & -a & 0 & 0 \\
-a & 6 & -a & 0 \\
0 & -a & 6 & -a \\
0 & 0 & -a & 5
\end{bmatrix}
\begin{bmatrix}
x_1\\
x_2\\
x_3\\
x_4
\end{bmatrix}
=
\begin{bmatrix}
5\\
6\\
6\\
5
\end{bmatrix}
$$

Se pide:

1. Construir la matriz de iteración de Jacobi.
2. Determinar para qué valores de $a$ converge por diagonal dominante estricta.
3. Determinar los valores propios de la matriz iterativa.
4. Hallar el radio espectral.
5. Determinar para qué valores de $a$ converge por criterio espectral.
6. Para:

$$
a=2
$$

realizar tres iteraciones usando:

$$
x^{(0)}=(0,0,0,0)^T
$$

7. Estimar el error usando:

$$
||x^{(k)}-x^{(k-1)}||_\infty
$$

hasta que:

$$
||e^{(k)}||_\infty<10^{-2}
$$

---

# Problema 02 — Factorización LU Paramétrica

Sea:

$$
A=
\begin{bmatrix}
2 & -1 & 0 & 0 \\
-1 & 2 & -1 & 0 \\
0 & -1 & 2 & -1 \\
0 & 0 & -1 & 2+a
\end{bmatrix}
$$

Se pide:

1. Determinar para qué valores de $a$ existe factorización LU sin pivoteo.
2. Obtener:

$$
A=LU
$$

en función de $a$.
3. Resolver el sistema:

$$
Ax=b
$$

para:

$$
b=
\begin{bmatrix}
1\\
0\\
0\\
1
\end{bmatrix}
$$

tomando:

$$
a=1
$$

4. Indicar el número total de operaciones elementales requeridas.
5. Comparar el costo contra eliminación gaussiana si deben resolverse 10 sistemas con distinta $b$.

---

# Problema 03 — Newton-Raphson y Multiplicidad

Considérese:

$$
f(x)=x^3-6x^2+12x-8
$$

Se pide:

1. Determinar analíticamente la raíz y su multiplicidad.
2. Obtener la fórmula iterativa de Newton-Raphson.
3. Usando:

$$
x_0=5
$$

realizar cuatro iteraciones.
4. Calcular el error absoluto en cada iteración.
5. Determinar experimentalmente el orden de convergencia.
6. Comparar el comportamiento con el caso de raíces simples.

---

# Problema 04 — Método de Potencia Inversa

Considérese:

$$
A=
\begin{bmatrix}
4 & 1 & 0 \\
1 & 3 & 1 \\
0 & 1 & 2
\end{bmatrix}
$$

Se pide:

1. Aplicar una iteración del método de potencia inversa usando:

$$
x^{(0)}=
\begin{bmatrix}
1\\
1\\
1
\end{bmatrix}
$$

2. Resolver el sistema lineal asociado mediante LU.
3. Normalizar con norma infinito.
4. Estimar el menor valor propio en módulo.
5. Realizar dos iteraciones adicionales.
6. Comparar la convergencia respecto al método de potencia directo.

---

# Problema 05 — Error de Redondeo y Estabilidad

Usando aritmética decimal de 4 cifras significativas, evaluar:

$$
I_1=\int_0^1 \frac{1}{x+10}\,dx
$$

mediante la recurrencia:

$$
I_n=\frac{1}{n}-10I_{n-1}
$$

Se sabe:

$$
I_0=\ln\left(\frac{11}{10}\right)
$$

Se pide:

1. Calcular:
   - $I_1$
   - $I_2$
   - $I_3$
2. Analizar la propagación del error.
3. Indicar si el algoritmo es estable o inestable.
4. Explicar cómo influye el factor multiplicativo en la acumulación del error.

---

# Problema 06 — MATLAB Completar Código

Considere el siguiente código incompleto:

```matlab
A = [4 -1 0 0;
    -1 4 -1 0;
     0 -1 4 -1;
     0 0 -1 4];

b = [1;4;4;1];

x = zeros(4,1);

for k = 1:5

    x_new(1) = ________________________;

    x_new(2) = ________________________;

    x_new(3) = ________________________;

    x_new(4) = ________________________;

    x = x_new;

end
```

Se pide:

1. Completar el código para Jacobi.
2. Modificarlo para Gauss-Seidel.
3. Agregar cálculo del error:

```matlab
norm(x_new - x, inf)
```

4. Agregar criterio de parada:

$$
||e^{(k)}||_\infty<10^{-4}
$$

5. Determinar teóricamente si converge.

---

# Problema 07 — Teorema de Banach

Considérese:

$$
g(x)=\frac{x^2+2}{3}
$$

Se pide:

1. Determinar los puntos fijos.
2. Verificar si existe contracción en:

$$
[0,2]
$$

3. Determinar una cota para:

$$
|g'(x)|
$$

4. Aplicar el teorema de Banach.
5. Realizar tres iteraciones usando:

$$
x_0=1
$$

6. Estimar el error usando:

$$
\frac{|x^{(k)}-x^{(k-1)}|}{|x^{(k)}|}
$$

---

# Problema 08 — Pivoteo Parcial

Considérese:

$$
\begin{cases}
0.0001x+y+z=2 \\
x+y+2z=4 \\
2x+4y-z=2
\end{cases}
$$

Se pide:

1. Resolver SIN pivoteo usando eliminación gaussiana con aritmética de 4 cifras significativas.
2. Resolver CON pivoteo parcial.
3. Comparar ambas soluciones.
4. Calcular el error relativo porcentual en cada caso.
5. Determinar cuál procedimiento es más estable.

---

# Comentario

> [!important]
> Esto ya se parece mucho más a un parcial real:
>
> - matrices tridiagonales,
> - parámetros,
> - LU simbólico,
> - criterios espectrales,
> - convergencia experimental,
> - errores numéricos acumulativos,
> - potencia inversa,
> - MATLAB incompleto,
> - aritmética finita,
> - problemas largos donde una parte depende de la anterior.
>
> Ese tipo de examen busca:
>
> - cansarte,
> - hacerte cometer errores algebraicos,
> - ver si entiendes convergencia,
> - y medir si puedes sostener cálculos largos bajo presión.