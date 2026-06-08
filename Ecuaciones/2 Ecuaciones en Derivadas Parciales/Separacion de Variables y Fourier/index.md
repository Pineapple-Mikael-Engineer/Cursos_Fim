---
title: Separación de Variables y Fourier
tags:
  - ecuaciones
  - edp
  - teoria
  - separacion-variables
  - fourier
  - index
draft: false
aliases:
  - separación de variables
  - series de Fourier
  - método maestro EDP
---

# Separación de Variables y Fourier

> [!definicion]
> El **método maestro** para EDP lineales en dominios acotados: se busca una solución producto
> $$u(x,t)=X(x)\,T(t),$$
> lo que **separa** la EDP en dos EDO acopladas por una **constante de separación** $-\lambda$. Las
> condiciones de frontera convierten una de ellas en un **problema de autovalores**
> ([[Sturm-Liouville/index| Sturm-Liouville]]) con autofunciones $X_n(x)$; la condición inicial se
> ajusta superponiéndolas en una **serie de Fourier** $u=\sum_n c_n X_n(x)T_n(t)$.

> [!info]
> Es la maquinaria que resuelve el [[Ecuacion del Calor/index| calor]], la
> [[Ecuacion de Onda/index| onda]] y [[Ecuacion de Laplace y Poisson/index| Laplace]] en regiones
> acotadas. Su base teórica —la **ortogonalidad** de las autofunciones— es lo que hace posible
> "extraer" los coeficientes $c_n$. Las [[Funciones Especiales/index| funciones especiales]]
> (Bessel, Legendre) son las autofunciones cuando el dominio es un disco o una esfera.

---

## La idea, en una frase

> [!teoria]
> Una EDP acopla espacio y tiempo; **separar variables** apuesta a que existen soluciones donde ese
> acoplamiento se factoriza, $u=X(x)T(t)$. Al sustituir y dividir por $XT$, los términos espaciales
> quedan a un lado y los temporales al otro:
> $$\frac{T'(t)}{T(t)}=\alpha^2\frac{X''(x)}{X(x)}=-\lambda\quad(\text{constante}).$$
> Como un lado depende solo de $t$ y el otro solo de $x$, **ambos** deben igualar una **constante**
> $-\lambda$. Eso parte la EDP en dos EDO. Las condiciones de frontera homogéneas solo admiten
> solución no trivial para ciertos $\lambda=\lambda_n$ (**autovalores**), con autofunciones $X_n$. La
> solución general es la **superposición** $u=\sum_n c_n X_n(x)T_n(t)$, y los $c_n$ se calculan
> imponiendo la condición inicial: ahí entra **Fourier**.

> [!teoria] Por qué funciona Fourier: ortogonalidad
> Las autofunciones $X_n$ de un problema de Sturm-Liouville son **ortogonales**:
> $\int X_n X_m\,w\,dx=0$ si $n\neq m$. Por eso, dada la condición inicial $f(x)=\sum_n c_nX_n(x)$,
> se "proyecta" multiplicando por $X_m$ e integrando: todos los términos se anulan salvo el $n=m$, y
> $$c_m=\frac{\int f\,X_m\,w\,dx}{\int X_m^2\,w\,dx}.$$
> Es el mismo gesto que extraer una componente de un vector con el producto punto: la **base
> ortogonal** lo hace trivial. Eso es una [[Series de Fourier| serie de Fourier]] generalizada.

---

## Mapa de la sección

> [!info]
> | Nota | Aporte |
> |---|---|
> | [[Tecnica de Separacion\|Técnica de Separación]] | el procedimiento $u=X(x)T(t)$ y la constante $-\lambda$ |
> | [[Funciones Ortogonales\|Funciones Ortogonales]] | producto interno, base ortogonal, proyección |
> | [[Series de Fourier\|Series de Fourier]] | senos/cosenos; cálculo de los coeficientes |
> | [[Convergencia y Gibbs\|Convergencia y Gibbs]] | en qué sentido converge; el salto y el fenómeno de Gibbs |
> | [[Identidad de Parseval\|Identidad de Parseval]] | energía = suma de cuadrados; completitud |
> | [[Desarrollo en Autofunciones\|Desarrollo en Autofunciones]] | Fourier generalizado (Bessel, Legendre) |

## Resumen

> [!resumen]
> | Paso | Acción |
> |---|---|
> | Separar | $u=X(x)T(t)$ → dos EDO con constante $-\lambda$ |
> | Autovalores | la frontera cuantiza $\lambda_n$, da autofunciones $X_n$ |
> | Superponer | $u=\sum_n c_nX_n(x)T_n(t)$ |
> | Coeficientes | $c_n$ por ortogonalidad (Fourier) desde la condición inicial |

> [!corolario]
> Separación de variables convierte una EDP en una **infinidad de EDO desacopladas**, una por modo;
> Fourier las recombina para ajustar el dato inicial. La pieza que lo hace posible es la
> **ortogonalidad** de las autofunciones —el mismo principio que descompone un vector en una base—.

> [!referencia]
> - El procedimiento concreto: [[Tecnica de Separacion]].
> - La base teórica: [[Funciones Ortogonales]] y [[Series de Fourier]].
> - El problema de autovalores subyacente: [[Sturm-Liouville/index]].
