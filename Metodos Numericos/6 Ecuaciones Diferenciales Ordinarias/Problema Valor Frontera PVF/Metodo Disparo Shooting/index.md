---
title: Método de Disparo (Shooting)
order: 2
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - valor-frontera
  - disparo
  - index
draft: false
aliases:
  - Método de disparo
  - Shooting method
  - Disparo
---

# Método de Disparo (Shooting)

> [!definicion]
> El **método de disparo** resuelve un [[Problema Valor Frontera PVF/index|PVF]] convirtiéndolo en una sucesión de [[Problema Valor Inicial PVI/index|problemas de valor inicial]]: se **adivina** la condición inicial desconocida (la pendiente $y'(a)=s$), se integra como PVI, y se **ajusta** $s$ hasta que la solución acierte la condición del otro extremo $y(b)=\beta$.

> [!info]
> El nombre evoca la **artillería**: se "dispara" con un ángulo (pendiente) inicial, se observa dónde cae el proyectil ($y(b)$) y se corrige el ángulo hasta dar en el blanco ($\beta$). Reutiliza toda la maquinaria de PVI ([[RK4 Clasico Tabla Butcher y Orden Cuatro|RK4]]) más un método de búsqueda de raíces ([[Newton Raphson/index|Newton]]).

---

## Las dos piezas

> [!info]
> - **[[Transformacion PVF a PVI Valor Inicial Desconocido|Transformación a PVI]]:** cómo parametrizar el PVF por la pendiente inicial $s$ y definir la **función objetivo** $\phi(s) = y(b; s) - \beta$.
> - **[[Metodo Newton para Condicion Frontera Residual|Newton sobre el residuo]]:** cómo encontrar el $s$ que anula $\phi(s)$ mediante Newton o la secante, integrando la ecuación de sensibilidad.

---

## Ejemplo

> [!ejemplo]
> **Trayectoria de un proyectil con resistencia: alcanzar un blanco.** Un proyectil debe pasar por $(x_0, y_0)$ y dar en $(x_f, y_f)$. La ecuación de la trayectoria es un PVF (posición fija en dos puntos), pero el **ángulo de lanzamiento** $s = y'(x_0)$ es desconocido.
>
> | Disparo | Ángulo $s$ | $y(x_f)$ | Error $\phi(s)$ |
> |:---:|:---:|:---:|:---:|
> | 1 | 30° | cae corto | $\phi_1 < 0$ |
> | 2 | 45° | pasa largo | $\phi_2 > 0$ |
> | 3 | interpolado | da en el blanco | $\phi_3 \approx 0$ |
>
> Cada disparo es un PVI integrado con RK4; el ajuste del ángulo es búsqueda de raíz. Es literalmente el problema balístico que da nombre al método.

---

## Lógica del método

> [!teoria]
> 1. Parametrizar: el PVI con $y(a)=\alpha$, $y'(a)=s$ tiene solución $y(x;s)$ que depende de $s$.
> 2. Definir el residuo de frontera $\phi(s) = y(b;s) - \beta$.
> 3. Resolver $\phi(s)=0$ por [[Newton Raphson/index|Newton]]/secante: cada evaluación de $\phi$ es **una integración PVI completa**.
> 4. El $s^*$ que anula $\phi$ da la solución del PVF.

---

## Resumen

| Tema | Nota |
|:---|:---|
| Parametrización por pendiente inicial | [[Transformacion PVF a PVI Valor Inicial Desconocido]] |
| Newton sobre el residuo de frontera | [[Metodo Newton para Condicion Frontera Residual]] |
| Comparación con diferencias finitas | [[Comparacion Disparo vs Diferencias Finitas]] |

> [!corolario]
> El método de disparo transforma el PVF en una sucesión de [[Problema Valor Inicial PVI/index|PVI]]: adivina la pendiente inicial $s$, integra hacia adelante, y ajusta $s$ —por [[Metodo Newton para Condicion Frontera Residual|Newton sobre el residuo]] $\phi(s)=y(b;s)-\beta$— hasta acertar el extremo opuesto, como ajustar el ángulo de un cañón hasta dar en el blanco. Reutiliza los integradores de PVI ([[RK4 Clasico Tabla Butcher y Orden Cuatro|RK4]]) y los métodos de raíces ([[Newton Raphson/index|Newton]]/secante). Es simple y preciso para problemas bien condicionados, pero menos robusto que las [[Comparacion Disparo vs Diferencias Finitas|diferencias finitas]] cuando el PVI es sensible a la condición inicial.
