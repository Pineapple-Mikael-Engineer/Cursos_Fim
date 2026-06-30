---
title: Métodos de Serie de Taylor de Orden Superior
order: 4
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - valor-inicial
  - euler-taylor
draft: false
aliases:
  - Métodos de Taylor
  - Taylor de orden superior
  - Taylor series methods
---

# Métodos de Serie de Taylor de Orden Superior

> [!definicion]
> Un **método de Taylor de orden $p$** aproxima $y(t_{n+1})$ conservando $p$ términos de la serie de Taylor de la solución:
> $$y_{n+1} = y_n + h\,y'_n + \frac{h^2}{2!}y''_n + \cdots + \frac{h^p}{p!}y^{(p)}_n,$$
> donde las derivadas se obtienen **derivando la EDO**: $y' = f$, $y'' = f_t + f_y f$, etc.

> [!info]
> Suben el orden de [[Euler Explicito Orden 1 Interpretacion Geometrica|Euler]] ($p=1$) a cualquier $p$, con error local $O(h^{p+1})$ y global $O(h^p)$. Su defecto es que exigen calcular **derivadas totales de $f$** analíticamente, lo que se vuelve impracticable para $f$ complicadas. Resolver esto sin derivadas es la motivación de [[Metodos Runge Kutta/index|Runge-Kutta]].

---

## Derivadas totales

> [!teoria]
> Como $y' = f(t,y)$, las derivadas superiores se obtienen por la regla de la cadena:
> $$y'' = \frac{d}{dt}f(t,y) = f_t + f_y\,y' = f_t + f_y\,f,$$
> $$y''' = f_{tt} + 2f_{ty}f + f_{yy}f^2 + f_y(f_t + f_y f),$$
> y así sucesivamente. El número de términos **crece rápidamente** (combinatoria de derivadas parciales), lo que hace tedioso el cálculo manual para $p\geq3$.

---

## Método de Taylor de orden 2

> [!teorema]
> El método de Taylor de orden 2 es
> $$y_{n+1} = y_n + h\,f(t_n,y_n) + \frac{h^2}{2}\big[f_t(t_n,y_n) + f_y(t_n,y_n)\,f(t_n,y_n)\big],$$
> con error local $O(h^3)$ y orden global 2.

> [!demostracion]
> De la serie de Taylor $y(t_{n+1}) = y_n + hy'_n + \frac{h^2}{2}y''_n + O(h^3)$, sustituyendo $y'_n = f$ y $y''_n = f_t + f_y f$ se obtiene la fórmula. Truncar en $h^2$ deja error local $\frac{h^3}{6}y'''(\xi) = O(h^3)$.

---

## Ejemplo

> [!ejemplo]
> **$y' = t + y$, $y(0)=1$** (exacta $y = 2e^t - t - 1$). Aquí $f_t=1$, $f_y=1$, así $y'' = 1 + (t+y)$. Taylor orden 2 con $h=0.1$:
> $$y_1 = 1 + 0.1(0+1) + \frac{0.01}{2}[1 + (0+1)] = 1 + 0.1 + 0.01 = 1.11000.$$
> Exacta: $y(0.1)=1.11034$. Error $3.4\times10^{-4}$, frente al $5.2\times10^{-3}$ de [[Euler Explicito Orden 1 Interpretacion Geometrica|Euler]]: un orden de magnitud mejor con el término cuadrático.

---

## Ventajas y el defecto fatal

> [!info]
> **Ventaja.** Orden arbitrario $p$ con un solo "paso" conceptual; muy preciso para $f$ con derivadas simples (polinómicas, exponenciales).

> [!warning]
> **Defecto.** Requiere **derivadas analíticas** de $f$:
> - Para $f$ complicada (tablas, funciones implícitas, lados derechos largos de sistemas físicos), derivar a mano es inviable.
> - El número de términos crece combinatoriamente con $p$.
> - No se generaliza fácilmente a sistemas grandes.
>
> Por eso, en la práctica, los métodos de Taylor de orden alto **rara vez se usan**: [[Metodos Runge Kutta/index|Runge-Kutta]] alcanza el mismo orden evaluando $f$ en puntos intermedios, **sin** ninguna derivada.

---

## Conexión con Runge-Kutta

> [!teoria]
> Runge-Kutta nace de imitar la serie de Taylor **sin derivarla**: en lugar de calcular $f_t, f_y$, evalúa $f$ en varios puntos y combina los resultados con pesos elegidos para que la expansión coincida con la de Taylor hasta orden $p$. Es "Taylor sin derivadas". La [[Construccion General Etapas s y Orden p|construcción general de RK]] formaliza esta idea.

> [!info]
> **Excepción moderna:** la **diferenciación automática** vuelve a hacer atractivos los métodos de Taylor de orden muy alto (decenas), porque calcula las derivadas totales exactamente y sin esfuerzo manual. Se usan en integración de alta precisión (mecánica celeste, aritmética de intervalos).

---

## Relación con otras notas

> [!info]
> - El caso $p=1$: [[Euler Explicito Orden 1 Interpretacion Geometrica]].
> - El orden que alcanzan: [[Error Local Truncamiento vs Error Global Acumulado]].
> - La alternativa sin derivadas: [[Metodos Runge Kutta/index]] y [[Construccion General Etapas s y Orden p]].
> - La serie de Taylor base: [[Aproximacion Diferencias Finitas Serie Taylor]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Fórmula | $y_{n+1} = \sum_{k=0}^p \frac{h^k}{k!}y^{(k)}_n$ |
| Derivadas | totales de $f$ (regla de la cadena) |
| Orden | $p$ |
| Ventaja | orden arbitrario |
| Defecto | requiere derivar $f$ analíticamente |
| Alternativa | Runge-Kutta (sin derivadas) |

> [!corolario]
> Los métodos de Taylor de orden $p$ conservan $p$ términos de la serie de la solución, alcanzando orden global $p$ con error local $O(h^{p+1})$, pero exigen las derivadas totales de $f$ —$f_t + f_y f$ y superiores— cuyo cálculo manual es inviable para $f$ complicadas. Este defecto es precisamente lo que motiva [[Metodos Runge Kutta/index|Runge-Kutta]], que reproduce la misma expansión de Taylor evaluando $f$ en puntos intermedios sin derivar. Solo con [[Construccion General Etapas s y Orden p|diferenciación automática]] vuelven a ser competitivos, en aplicaciones de altísima precisión.
