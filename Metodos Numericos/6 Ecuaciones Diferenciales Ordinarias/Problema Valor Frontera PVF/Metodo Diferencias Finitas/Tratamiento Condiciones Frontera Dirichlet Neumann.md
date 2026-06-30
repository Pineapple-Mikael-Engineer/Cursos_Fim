---
title: Tratamiento de Condiciones de Frontera (Dirichlet y Neumann)
order: 4
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - valor-frontera
  - diferencias-finitas
draft: false
aliases:
  - Condiciones de frontera
  - Dirichlet y Neumann
  - Boundary conditions
  - Frontera de Robin
---

# Tratamiento de Condiciones de Frontera (Dirichlet y Neumann)

> [!definicion]
> Las **condiciones de frontera** especifican el comportamiento de la solución en los extremos $a$ y $b$:
> - **Dirichlet:** se fija el **valor**, $y(a)=\alpha$. (Temperatura impuesta, extremo sujeto.)
> - **Neumann:** se fija la **derivada**, $y'(a)=\gamma$. (Flujo de calor impuesto, extremo libre.)
> - **Robin (mixta):** combinación, $\mu\,y(a) + \nu\,y'(a) = \delta$. (Convección.)

> [!info]
> Cómo se incorporan al [[Construccion Sistema Tridiagonal Lineal|sistema tridiagonal]] determina la precisión en los bordes. Dirichlet es trivial (el valor pasa al lado derecho); Neumann requiere cuidado para no degradar el orden $O(h^2)$ del esquema centrado. La distinción es física: valor fijo vs flujo fijo.

---

## Dirichlet: el valor conocido

> [!teoria]
> Con $y(a)=\alpha$, el valor $y_0=\alpha$ es **conocido**: no es incógnita. En la primera ecuación nodal ($i=1$), el término $a_1 y_0 = a_1\alpha$ pasa al [[Construccion Sistema Tridiagonal Lineal|lado derecho]]:
> $$b_1 y_1 + c_1 y_2 = d_1 - a_1\alpha.$$
> El sistema tiene $N-1$ incógnitas (los nodos internos). Es el caso más simple y mantiene el orden $O(h^2)$.

---

## Neumann: la derivada conocida

> [!teorema]
> Con $y'(a)=\gamma$, el valor $y_0$ es **incógnita** (hay $N$ incógnitas). Para mantener orden $O(h^2)$ se usa un **nodo fantasma** $y_{-1}$ y la diferencia centrada:
> $$y'(a) \approx \frac{y_1 - y_{-1}}{2h} = \gamma \;\Rightarrow\; y_{-1} = y_1 - 2h\gamma.$$
> Sustituyendo $y_{-1}$ en la ecuación nodal del borde ($i=0$) se elimina el fantasma y se obtiene una ecuación adicional para $y_0$, conservando $O(h^2)$.

> [!demostracion]
> La ecuación discreta en el nodo $i=0$ sería $y_{-1} - 2y_0 + y_1 = h^2(\cdots)$, que usa el fantasma $y_{-1}$. Reemplazando $y_{-1} = y_1 - 2h\gamma$:
> $$(y_1 - 2h\gamma) - 2y_0 + y_1 = h^2(\cdots) \;\Rightarrow\; -2y_0 + 2y_1 = h^2(\cdots) + 2h\gamma.$$
> Esta es la fila de frontera del sistema, ahora con $y_0$ como incógnita y orden $O(h^2)$ conservado.

> [!warning]
> **No usar diferencia adelantada de orden 1** ($y'(a)\approx(y_1-y_0)/h$) para Neumann: degrada el esquema global a $O(h)$, desperdiciando la precisión $O(h^2)$ del interior. El nodo fantasma (o una fórmula adelantada de 3 puntos $O(h^2)$) preserva el orden.

---

## Ejemplo: barra con un extremo aislado

> [!ejemplo]
> **Conducción $-T''=q/k$, extremo izquierdo a temperatura fija $T(0)=T_0$ (Dirichlet), extremo derecho aislado $T'(L)=0$ (Neumann).** Físicamente: una barra calentada, con un extremo a temperatura controlada y el otro sin pérdida de calor (flujo nulo).
>
> | Frontera | Condición | Tratamiento |
> |:---|:---|:---|
> | $x=0$ | $T(0)=T_0$ | $T_0$ al lado derecho |
> | $x=L$ | $T'(L)=0$ | nodo fantasma $T_{N+1}=T_{N-1}$ |
>
> El extremo aislado ($T'=0$) hace que el perfil de temperatura llegue **horizontal** a $x=L$: la solución es plana allí, reflejo del flujo nulo.

---

## Tabla resumen de tratamientos

> [!info]
> | Tipo | Condición | Incógnitas | Tratamiento | Orden |
> |:---|:---|:---:|:---|:---:|
> | Dirichlet | $y(a)=\alpha$ | $N-1$ | valor al lado derecho | $O(h^2)$ |
> | Neumann | $y'(a)=\gamma$ | $N$ | nodo fantasma | $O(h^2)$ |
> | Robin | $\mu y + \nu y'=\delta$ | $N$ | combinar valor + fantasma | $O(h^2)$ |

---

## Significado físico

> [!teoria]
> La condición de frontera codifica la **física del borde**:
> - **Dirichlet** = estado impuesto (temperatura del baño térmico, posición sujeta de una viga).
> - **Neumann** = flujo impuesto ($-k T' = $ flujo de calor; $y'=$ pendiente/momento en una viga). $y'=0$ es aislamiento o extremo libre.
> - **Robin** = intercambio con el entorno (ley de enfriamiento de Newton: flujo proporcional a la diferencia de temperatura).
>
> Elegir la condición correcta es modelar bien el problema, no solo un detalle numérico.

---

## Relación con otras notas

> [!info]
> - El sistema al que se incorporan: [[Construccion Sistema Tridiagonal Lineal]].
> - Las fórmulas de derivada usadas: [[Orden Error Progresiva Regresiva Centrada]] y [[Aproximacion Diferencias Finitas Serie Taylor]].
> - El orden que hay que preservar: [[Consistencia Estabilidad Convergencia Lax]].
> - En disparo, las fronteras se tratan distinto: [[Transformacion PVF a PVI Valor Inicial Desconocido]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Dirichlet | valor fijo $y(a)=\alpha$, al lado derecho |
| Neumann | derivada fija $y'(a)=\gamma$, nodo fantasma |
| Robin | mixta $\mu y+\nu y'=\delta$ |
| Clave Neumann | usar centrada $O(h^2)$, no adelantada $O(h)$ |
| Física | valor impuesto vs flujo impuesto |

> [!corolario]
> Las condiciones de frontera se incorporan al sistema tridiagonal según su tipo: Dirichlet (valor fijo) pasa el dato al lado derecho de forma trivial, mientras que Neumann (derivada fija) introduce un nodo fantasma para mantener el orden $O(h^2)$ —usar una diferencia adelantada de orden 1 lo degradaría—. Robin combina ambos. La elección no es un detalle numérico sino el modelado físico del borde: temperatura impuesta, flujo impuesto o intercambio convectivo. Bien tratadas, preservan la convergencia $O(h^2)$ garantizada por [[Consistencia Estabilidad Convergencia Lax|Lax]], cerrando el método de [[Metodo Diferencias Finitas/index|diferencias finitas]].
