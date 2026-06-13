---
title: Construcción de la Tabla de Routh
tags:
  - control-clasico
  - teoria
  - analisis
  - estabilidad
  - routh-hurwitz
draft: false
aliases:
  - tabla de routh
  - construir tabla routh
  - algoritmo routh
---

# Construcción de la Tabla de Routh

> [!definicion]
> La tabla de Routh se arma colocando los coeficientes de $P(s)=a_n s^n+\dots+a_0$ alternados en dos filas iniciales y generando las restantes con
> $$c_i=\frac{g_1\,f_{i+1}-f_1\,g_{i+1}}{g_1},$$
> donde $f_\bullet$ es la fila inmediatamente superior y $g_\bullet$ la de dos arriba. Se itera hasta la fila $s^0$. La **primera columna** decide la estabilidad: tantos polos inestables como cambios de signo presente.

> [!info]
> Procedimiento base del criterio de [[Routh Hurwitz/index | Routh-Hurwitz]]. Si aparece un cero en la primera columna o una fila nula, ir a [[Casos Especiales | casos especiales]]; con un parámetro $K$, a [[Ajuste Parametros | ajuste de parámetros]].

---

## Ejemplo

> [!ejemplo] Cuarto orden completo, fila por fila
> $$P(s)=s^4+3s^3+3s^2+2s+2.$$
>
> **Paso 0 — Condición necesaria.** Coeficientes $1,3,3,2,2$: todos positivos y ninguno nulo ✓. Sigue indeciso → construir la tabla.
>
> **Paso 1 — Dos primeras filas.** $s^4$ toma los coeficientes pares ($a_4,a_2,a_0$) y $s^3$ los impares ($a_3,a_1$):
> $$
> \begin{array}{c|ccc}
> s^4 & 1 & 3 & 2 \\
> s^3 & 3 & 2 & 0
> \end{array}
> $$
>
> **Paso 2 — Fila $s^2$.** Con $g=(1,3,2)$ arriba-arriba y $f=(3,2,0)$ arriba:
> $$b_1=\frac{3\cdot3-1\cdot2}{3}=\frac{9-2}{3}=\frac{7}{3}\approx2.33,\qquad
> b_2=\frac{3\cdot2-1\cdot0}{3}=2.$$
> $$
> \begin{array}{c|ccc}
> s^4 & 1 & 3 & 2 \\
> s^3 & 3 & 2 & 0 \\
> s^2 & 7/3 & 2 & 0
> \end{array}
> $$
>
> **Paso 3 — Fila $s^1$.** Ahora $g=(3,2,0)$ y $f=(7/3,2,0)$:
> $$c_1=\frac{(7/3)\cdot2-3\cdot2}{7/3}=\frac{14/3-6}{7/3}=\frac{-4/3}{7/3}=-\frac{4}{7}\approx-0.57.$$
> $$
> \begin{array}{c|ccc}
> s^4 & 1 & 3 & 2 \\
> s^3 & 3 & 2 & 0 \\
> s^2 & 7/3 & 2 & 0 \\
> s^1 & -4/7 & 0 &
> \end{array}
> $$
>
> **Paso 4 — Fila $s^0$.** Con $g=(7/3,2)$ y $f=(-4/7,0)$:
> $$d_1=\frac{(-4/7)\cdot2-(7/3)\cdot0}{-4/7}=\frac{-8/7}{-4/7}=2.$$
> $$
> \begin{array}{c|ccc}
> s^4 & 1 & 3 & 2 \\
> s^3 & 3 & 2 & 0 \\
> s^2 & 7/3 & 2 & 0 \\
> s^1 & -4/7 & 0 & \\
> s^0 & 2 & &
> \end{array}
> $$
>
> **Paso 5 — Leer la primera columna.** $1,\ 3,\ 7/3,\ -4/7,\ 2$. Signos: $+,+,+,-,+$ → **dos cambios** ($7/3\to-4/7$ y $-4/7\to2$).
>
> **Conclusión:** **2 polos con $\Re>0$** → sistema **inestable**, pese a cumplir la condición necesaria.

> [!ejemplo] Tercer orden estable (verificación)
> $$P(s)=s^3+6s^2+11s+6=(s+1)(s+2)(s+3).$$
> $$
> \begin{array}{c|cc}
> s^3 & 1 & 11 \\
> s^2 & 6 & 6 \\
> s^1 & \frac{6\cdot11-1\cdot6}{6}=10 & 0 \\
> s^0 & 6 &
> \end{array}
> $$
> Primera columna $1,6,10,6$: sin cambios → **0 inestables** → **estable**, coherente con los polos $-1,-2,-3$.

---

## Algoritmo

> [!algoritmo] Construcción paso a paso
> Dado $P(s)=a_n s^n+a_{n-1}s^{n-1}+\dots+a_0$:
> 1. **Filtro.** Verificar la [[Condicion Necesaria | condición necesaria]]; si falla, el sistema es inestable y no hace falta tabla.
> 2. **Filas semilla.** Fila $s^n$: $a_n,a_{n-2},a_{n-4},\dots$ Fila $s^{n-1}$: $a_{n-1},a_{n-3},a_{n-5},\dots$
> 3. **Filas siguientes.** Para cada elemento usar $c_i=\dfrac{g_1 f_{i+1}-f_1 g_{i+1}}{g_1}$, con $f$ la fila de arriba y $g$ la de dos arriba; rellenar con $0$ las posiciones que falten.
> 4. **Parar** al llegar a la fila $s^0$ (un solo elemento).
> 5. **Contar** los cambios de signo en la primera columna = número de polos con $\Re>0$.

> [!info] La fórmula es un determinante $2\times2$
> Cada elemento es $-\dfrac{1}{g_1}\det\begin{bmatrix} g_1 & g_{i+1}\\ f_1 & f_{i+1}\end{bmatrix}$: columna izquierda fija (los primeros elementos de las dos filas superiores) y columna derecha desplazándose una posición a la derecha en cada paso.

> [!info] Conteo de cambios de signo
> Para la primera columna $1,3,-2,4,-1$: $3\to-2$, $-2\to4$, $4\to-1$ → **3 cambios** → 3 polos con $\Re>0$. Multiplicar toda una fila por una constante positiva no altera los signos (útil para limpiar fracciones).

> [!info] En MATLAB
> ```matlab
> P = [1 3 3 2 2];      % s^4 + 3s^3 + 3s^2 + 2s + 2
> r = roots(P);          % polos exactos
> nInest = sum(real(r) > 0)   % # con parte real positiva
> ```

---

## Limitaciones

> [!warning]
> 1. El algoritmo se detiene si el primer elemento de una fila es $0$ con resto no nulo, o si aparece una fila entera de ceros → ver [[Casos Especiales | casos especiales]].
> 2. En grado alto los cálculos se alargan (conviene automatizar).
> 3. Solo cuenta polos inestables; no localiza los estables.
> 4. No aplica a sistemas con retardo.

---

## Demostración

> [!teorema] Por qué funciona
> La primera columna de Routh reproduce los signos de los **determinantes de Hurwitz** $\Delta_i$; sus cambios de signo cuentan las raíces de $P(s)$ con $\Re(s)>0$.

> [!demostracion] Transformación bilineal y conteo
> **Paso 1 — Mapa al disco.** La bilineal $z=\dfrac{1+s}{1-s}$ (inversa $s=\dfrac{z-1}{z+1}$) envía el semiplano izquierdo $\Re(s)<0$ al interior del círculo $|z|<1$, el eje $j\omega$ al círculo $|z|=1$ y el semiplano derecho a $|z|>1$.
>
> **Paso 2 — Polinomio transformado.** Sustituyendo, $P\!\left(\frac{z-1}{z+1}\right)=\dfrac{Q(z)}{(z+1)^n}$ con $Q(z)$ de grado $n$. Las raíces de $P$ con $\Re<0$ corresponden a raíces de $Q$ dentro del disco.
>
> **Paso 3 — Schur-Cohn / Sturm.** Contar las raíces de $Q$ fuera del disco equivale, por el teorema de Sturm, a contar cambios de signo en una secuencia; Routh ejecuta ese conteo recursivamente sobre los coeficientes de $P$ **sin** transformar explícitamente.
>
> **Paso 4 — Recursión.** La tabla usa $c_{i,j}=\dfrac{c_{i-2,1}\,c_{i-1,j+1}-c_{i-1,1}\,c_{i-2,j+1}}{c_{i-1,1}}$, equivalente a propagar los menores de Hurwitz.
>
> **Paso 5 — Principio del argumento.** El número de ceros en el semiplano derecho es $N=\dfrac{1}{2\pi j}\oint_\Gamma \dfrac{P'(s)}{P(s)}\,ds$ sobre el contorno de Nyquist. Routh sustituye esa integral por álgebra de coeficientes vía los menores
> $$\Delta_1=a_{n-1},\quad \Delta_2=\det\begin{bmatrix}a_{n-1}&a_{n-3}\\a_n&a_{n-2}\end{bmatrix},\quad \Delta_3=\det\begin{bmatrix}a_{n-1}&a_{n-3}&a_{n-5}\\a_n&a_{n-2}&a_{n-4}\\0&a_{n-1}&a_{n-3}\end{bmatrix},\dots$$
> El sistema es estable si y solo si todos los $\Delta_i>0$. $\blacksquare$

---

## Resumen

> [!resumen]
> | Paso | Acción |
> |---|---|
> | 0 | condición necesaria como filtro |
> | 1 | filas $s^n$ (pares) y $s^{n-1}$ (impares) |
> | 2 | $c_i=\dfrac{g_1 f_{i+1}-f_1 g_{i+1}}{g_1}$ hasta $s^0$ |
> | 3 | contar cambios de signo en la 1.ª columna |
> | Salida | #cambios = #polos con $\Re>0$ |

> [!corolario]
> Construir la tabla es mecánico: dos filas semilla y una recursión de determinantes $2\times2$ hasta $s^0$. El veredicto vive entero en la primera columna; cualquier cero allí remite a [[Casos Especiales | casos especiales]] y la presencia de un parámetro, a [[Ajuste Parametros | ajuste de parámetros]].

> [!referencia]
> - Criterio y enunciado: [[Control/Control Clasico/3 Analisis/Estabilidad/Routh Hurwitz/index]].
> - Filtro previo: [[Condicion Necesaria]].
> - Ceros y filas nulas: [[Casos Especiales]].
> - Rango de un parámetro: [[Ajuste Parametros]].
