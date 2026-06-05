---
title: Matriz Jacobiana y Sistema Lineal Asociado
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-no-lineales
  - sistemas-no-lineales
  - newton-raphson
draft: false
aliases:
  - Matriz jacobiana
  - Jacobian matrix
  - Sistema lineal de Newton
  - Linealización de F
---

# Matriz Jacobiana y Sistema Lineal Asociado

> [!definicion]
> La **matriz jacobiana** de $F = (f_1, \dots, f_n)^T : \mathbb{R}^n \to \mathbb{R}^n$ en $x$ es la matriz de derivadas parciales
> $$J(x) = \frac{\partial F}{\partial x} = \begin{pmatrix} \dfrac{\partial f_1}{\partial x_1} & \cdots & \dfrac{\partial f_1}{\partial x_n} \\ \vdots & \ddots & \vdots \\ \dfrac{\partial f_n}{\partial x_1} & \cdots & \dfrac{\partial f_n}{\partial x_n} \end{pmatrix}, \qquad J_{ij}(x) = \frac{\partial f_i}{\partial x_j}(x).$$
> Es el análogo multivariable de la derivada $f'(x)$ del caso escalar.

> [!info]
> La jacobiana es la mejor aproximación lineal local de $F$. Sobre ella se construye el paso de [[Newton Raphson Multivariable/index|Newton multivariable]]: cada iteración reduce el problema no lineal a un **sistema lineal** $J\,\Delta x = -F$.

---

## Linealización: de Taylor al paso de Newton

> [!teorema]
> El desarrollo de Taylor de primer orden de $F$ alrededor de $x^{(k)}$ es
> $$F(x) = F(x^{(k)}) + J(x^{(k)})\,(x - x^{(k)}) + O(\|x - x^{(k)}\|^2).$$
> Igualar el modelo lineal a cero ($F(x) \approx 0$) define la siguiente iterada $x^{(k+1)}$ mediante el **sistema lineal asociado**
> $$J(x^{(k)})\,\Delta x^{(k)} = -F(x^{(k)}), \qquad x^{(k+1)} = x^{(k)} + \Delta x^{(k)}.$$

> [!demostracion]
> Buscar el cero de la aproximación lineal $L(x) = F(x^{(k)}) + J(x^{(k)})(x - x^{(k)})$:
> $$L(x^{(k+1)}) = 0 \;\Longrightarrow\; J(x^{(k)})(x^{(k+1)} - x^{(k)}) = -F(x^{(k)}).$$
> Llamando $\Delta x^{(k)} = x^{(k+1)} - x^{(k)}$ se obtiene el sistema lineal. Formalmente $x^{(k+1)} = x^{(k)} - J^{-1}F$, pero la inversa **no** se calcula: se resuelve el sistema por [[Factorizacion LU/index|factorización LU]], lo que cuesta $\frac{2}{3}n^3$ frente a los $2n^3$ de invertir.

> [!warning]
> **Nunca invertir la jacobiana.** Escribir $x^{(k+1)} = x^{(k)} - J^{-1}F$ es notación; computar $J^{-1}$ explícitamente es más caro y menos [[Estabilidad Algoritmos Forward Backward|estable]] que resolver $J\Delta x = -F$. La regla del álgebra lineal numérica —"resolver, no invertir"— se aplica en cada paso.

---

## Ejemplo: construcción del sistema

> [!ejemplo]
> **Sistema $2\times2$.**
> $$F(x,y) = \begin{pmatrix} x^2 + y^2 - 4 \\ e^x + y - 1 \end{pmatrix}, \qquad J(x,y) = \begin{pmatrix} 2x & 2y \\ e^x & 1 \end{pmatrix}.$$
> En $x^{(0)} = (1, -1)^T$:
> $$F(x^{(0)}) = \begin{pmatrix} -2 \\ e - 2 \end{pmatrix} \approx \begin{pmatrix} -2 \\ 0.718 \end{pmatrix}, \qquad J(x^{(0)}) = \begin{pmatrix} 2 & -2 \\ e & 1 \end{pmatrix} \approx \begin{pmatrix} 2 & -2 \\ 2.718 & 1 \end{pmatrix}.$$
> El paso resuelve
> $$\begin{pmatrix} 2 & -2 \\ 2.718 & 1 \end{pmatrix}\begin{pmatrix} \Delta x \\ \Delta y \end{pmatrix} = \begin{pmatrix} 2 \\ -0.718 \end{pmatrix},$$
> cuya solución $\Delta x^{(0)} \approx (0.117, -0.883)^T$ actualiza $x^{(1)} = x^{(0)} + \Delta x^{(0)} \approx (1.117, -1.883)^T$.

---

## Cálculo de la jacobiana

> [!info]
> Tres formas de obtener $J(x)$, en orden de preferencia por exactitud:
>
> | Método | Exactitud | Costo |
> |:---|:---|:---|
> | **Analítica** | exacta | derivar a mano / simbólicamente, $n^2$ expresiones |
> | **Diferenciación automática** | exacta (hasta redondeo) | $\sim$ costo de evaluar $F$, sin error de truncamiento |
> | **Diferencias finitas** | $O(h)$ o $O(h^2)$ | $n$ evaluaciones extra de $F$ por columna |

> [!teoria]
> **Aproximación por diferencias finitas.** Columna a columna,
> $$J(x)\,e_j \approx \frac{F(x + h e_j) - F(x)}{h},$$
> con paso óptimo $h \approx \sqrt{u}\,\|x\|$ para equilibrar [[Perdida Significancia y Cancelacion Catastrofica|cancelación]] (error $\sim u/h$) y truncamiento (error $\sim h$). Es la base de los métodos cuasi-Newton cuando la jacobiana analítica no está disponible ([[Costo Computacional Evaluacion Jacobiano]]).

---

## La jacobiana como objeto geométrico

> [!proposicion]
> Propiedades relevantes de $J(x)$:
> 1. **Invertibilidad local:** si $J(r)$ es no singular en la raíz $r$, esta es **aislada** y Newton converge localmente (teorema de la función inversa).
> 2. **Condicionamiento:** el [[Condicionamiento Numerico Numero Condicion|número de condición]] $\kappa(J(r))$ controla la sensibilidad de la raíz y la fiabilidad del paso lineal.
> 3. **Simetría:** si $F = \nabla \phi$ es un gradiente (optimización), $J = \nabla^2\phi$ es la **hessiana**, simétrica; Newton para sistemas coincide con Newton para minimizar $\phi$.

---

## Relación con otras notas

> [!info]
> - El método que usa este sistema lineal en cada paso: [[Newton Raphson Multivariable/index]].
> - Cómo el sistema lineal por paso se resuelve: [[Factorizacion LU/index]] y [[Eliminacion Gaussiana]].
> - El orden que produce esta linealización: [[Convergencia Local Cuadratica]].
> - El costo de formar y factorizar $J$, y cómo evitarlo: [[Costo Computacional Evaluacion Jacobiano]].
> - Caso escalar análogo ($f'$ en lugar de $J$): [[Derivacion Geometrica y Serie Taylor]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Jacobiana | $J_{ij} = \partial f_i/\partial x_j$ |
| Linealización | $F(x) \approx F(x^{(k)}) + J(x^{(k)})(x - x^{(k)})$ |
| Sistema por paso | $J(x^{(k)})\,\Delta x = -F(x^{(k)})$ |
| Regla | resolver, **no** invertir ($\frac{2}{3}n^3$) |
| Cálculo de $J$ | analítica / automática / diferencias finitas |

> [!corolario]
> La matriz jacobiana $J(x) = [\partial f_i/\partial x_j]$ es la derivada multivariable que linealiza $F$ alrededor de la iterada actual. Igualar esa linealización a cero convierte cada paso de Newton en el sistema lineal $J(x^{(k)})\,\Delta x = -F(x^{(k)})$, que se resuelve —nunca se invierte— por factorización LU. La calidad del paso depende de la invertibilidad y el [[Condicionamiento Numerico Numero Condicion|condicionamiento]] de $J$ en la raíz, y la jacobiana puede obtenerse de forma analítica, automática o por diferencias finitas. Esta construcción es el corazón de [[Newton Raphson Multivariable/index]]; su consecuencia es la [[Convergencia Local Cuadratica|convergencia cuadrática]].
