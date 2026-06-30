---
title: Laplace y Poisson
order: 6
tags:
  - ecuaciones
  - edp
  - teoria
  - laplace
  - index
draft: false
aliases:
  - ecuación de Laplace
  - ecuación de Poisson
  - funciones armónicas
  - Laplace equation
---

# Ecuación de Laplace y Poisson

> [!definicion]
> La **ecuación de Laplace** describe estados de **equilibrio** (sin dependencia del tiempo):
> $$\nabla^2u=u_{xx}+u_{yy}(+u_{zz})=0.$$
> Sus soluciones son las **funciones armónicas**. Con fuente, es la ecuación de **Poisson** $\nabla^2u=-\rho$. Es la EDP **elíptica** prototipo: solución máximamente **suave**, que **promedia** los valores de la frontera.

> [!info]
> Tercera ecuación madre del [[2 Ecuaciones en Derivadas Parciales/index| capítulo de EDP]] (tipo **elíptico**, ver [[Clasificacion Segundo Orden| clasificación]]). Aparece como **estado estacionario** del [[Ecuacion del Calor/index| calor]] ($u_t=0$) y rige el potencial electrostático, gravitatorio y de fluidos incompresibles.

---

## Qué la hace especial: equilibrio y promedio

> [!teoria]
> La ecuación de Laplace no tiene tiempo: representa el **balance final** al que tiende un sistema difusivo. Sus propiedades, todas elípticas, giran en torno a una idea —**promediar**:
> 1. **Propiedad del valor medio.** El valor de una función armónica en un punto es **exactamente el promedio** de sus valores sobre cualquier círculo (o esfera) centrado en él. No hay "grumos": cada punto es la media de su entorno ([[Teorema del Valor Medio| teorema del valor medio]]).
> 2. **Principio del máximo.** Por lo anterior, una función armónica **no puede tener máximos ni mínimos interiores**: sus extremos están siempre en la **frontera** ([[Principio del Maximo Eliptico| principio del máximo]]). El interior solo "interpola" el borde.
> 3. **Suavidad y unicidad.** Las soluciones son analíticas (infinitamente suaves) en el interior y quedan **unívocamente determinadas por su valor en la frontera** (problema de Dirichlet).
> 4. **Solo datos de frontera.** Al no haber tiempo, no hay condición inicial: el problema bien planteado es puramente de [[Tipos de Condiciones| frontera]] (Dirichlet o Neumann).
>
> El método de solución vuelve a ser [[Tecnica de Separacion| separación de variables]], pero la **geometría manda**: en un rectángulo da senos/cosenos, en un disco da la [[Laplace en Disco| fórmula de Poisson]], en una esfera da los **armónicos esféricos**.

> [!info] Recorrido de la sección
> | Nota | Aporte |
> |---|---|
> | [[Funciones Armonicas\|Funciones Armónicas]] | definición y propiedades clave |
> | [[Laplace en Rectangulo\|Laplace en Rectángulo]] | separación cartesiana; Dirichlet/Neumann |
> | [[Laplace en Disco\|Laplace en Disco]] | coordenadas polares; **fórmula integral de Poisson** |
> | [[Laplace en Cilindro\|Laplace en Cilindro]] | separación → funciones de **Bessel** |
> | [[Laplace en Esfera\|Laplace en Esfera]] | separación → **armónicos esféricos** (Legendre) |
> | [[Principio del Maximo Eliptico\|Principio del Máximo]] | extremos en la frontera; unicidad |
> | [[Teorema del Valor Medio\|Teorema del Valor Medio]] | armónica = promedio sobre esferas |

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Ecuación | $\nabla^2u=0$ (Laplace) / $\nabla^2u=-\rho$ (Poisson) |
> | Tipo | elíptica; solo datos de **frontera** |
> | Valor medio | $u(P)=$ promedio sobre esferas centradas en $P$ |
> | Máximo | en la **frontera** (sin extremos interiores) |
> | Método | separación; geometría → senos / Poisson / Bessel / armónicos esféricos |

> [!corolario]
> Laplace es la ecuación del **equilibrio perfecto**: cada punto es la media de su entorno, así que la solución es lo más suave posible compatible con la frontera. Conocer el borde **basta** para conocerlo todo —la rigidez de lo armónico—.

> [!referencia]
> - El objeto central: [[Funciones Armonicas]].
> - El caso con geometría rica: [[Laplace en Disco]] y [[Laplace en Esfera]].
> - El equilibrio del calor: [[Ecuacion del Calor/index]].
