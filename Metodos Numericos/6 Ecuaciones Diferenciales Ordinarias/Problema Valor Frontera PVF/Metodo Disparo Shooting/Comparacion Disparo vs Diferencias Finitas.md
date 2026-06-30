---
title: Comparación — Disparo vs Diferencias Finitas
order: 3
tags:
  - metodos-numericos
  - teoria
  - ecuaciones-diferenciales
  - valor-frontera
draft: false
aliases:
  - Disparo vs diferencias finitas
  - Comparación de métodos PVF
  - Shooting vs finite differences
---

# Comparación: Disparo vs Diferencias Finitas

> [!definicion]
> Los dos métodos para [[Problema Valor Frontera PVF/index|PVF]] adoptan filosofías opuestas: el [[Metodo Disparo Shooting/index|disparo]] **marcha** (integra como PVI y ajusta la condición inicial), mientras que las [[Metodo Diferencias Finitas/index|diferencias finitas]] **discretizan globalmente** (resuelven todos los nodos a la vez en un sistema lineal).

> [!info]
> No hay un ganador absoluto: el disparo es simple y muy preciso si el PVI subyacente es estable; las diferencias finitas son más robustas, especialmente cuando el PVI es sensible o el problema es de gran escala. Conocer las ventajas de cada uno guía la elección según el problema físico.

---

## Comparación directa

> [!info]
> | Aspecto | [[Metodo Disparo Shooting/index\|Disparo]] | [[Metodo Diferencias Finitas/index\|Diferencias finitas]] |
> |:---|:---|:---|
> | Estrategia | reduce a PVI + raíces | sistema lineal global |
> | Reutiliza | [[RK4 Clasico Tabla Butcher y Orden Cuatro\|RK4]], [[Newton Raphson/index\|Newton]] | [[Construccion Sistema Tridiagonal Lineal\|Thomas]] |
> | Precisión | la del integrador (alta, $O(h^4)$ con RK4) | $O(h^2)$ (centrada) |
> | Robustez | frágil si el PVI es sensible | robusta |
> | No linealidad | Newton externo (1 parámetro) | Newton sobre todo el sistema |
> | Condiciones complejas | fácil (Dirichlet, Neumann en la integración) | Neumann necesita nodos fantasma |
> | Coste | (nº disparos) × integración | un sistema tridiagonal $O(N)$ |
> | Escala (sistemas grandes, EDPs) | mala | excelente (base de EDPs) |

---

## Cuándo usar cada uno

> [!info]
> | Situación | Método recomendado |
> |:---|:---|
> | PVI estable, alta precisión deseada | **Disparo** (con RK4) |
> | PVI inestable / solución que crece exponencialmente | **Diferencias finitas** |
> | Problema lineal pequeño | cualquiera (disparo lineal: 2 integraciones) |
> | Extensión a EDPs (2D, 3D) | **Diferencias finitas** |
> | Implementación rápida reutilizando un integrador | **Disparo** |
> | Problema de autovalores (modos propios) | Diferencias finitas (problema de autovalores matricial) |

> [!warning]
> **El punto débil del disparo: sensibilidad.** Si la solución del PVI crece como $e^{Lx}$, un cambio minúsculo en $s$ amplifica enormemente $y(b)$, haciendo $\phi(s)$ casi discontinua y Newton inestable. Las diferencias finitas no sufren esto porque imponen ambas fronteras simultáneamente. Para PVI sensibles, el **disparo múltiple** (subdividir el dominio en tramos y empalmar) mitiga el problema, acercándose a las diferencias finitas.

---

## Ejemplo comparativo

> [!ejemplo]
> **Capa límite: $\epsilon y'' + y' = 0$, $y(0)=0$, $y(1)=1$, con $\epsilon=0.01$.** La solución tiene una capa límite abrupta cerca de $x=0$.
>
> | Método | Comportamiento |
> |:---|:---|
> | Disparo | el PVI es **rígido/sensible**; $\phi(s)$ varía bruscamente, Newton lucha |
> | Diferencias finitas | robusto, pero la malla uniforme resuelve mal la capa (necesita refinamiento local) |
> | Diferencias finitas + malla adaptada | captura la capa límite con precisión |
>
> Ningún método es trivial aquí: el problema (capa límite) es intrínsecamente difícil, y la elección se inclina hacia diferencias finitas con malla refinada.

---

## Síntesis del capítulo

> [!teoria]
> El PVF cierra el panorama de las EDOs uniendo casi todo el curso: usa la [[Aproximacion Diferencias Finitas Serie Taylor|diferenciación numérica]] (esquemas centrados), la resolución de [[Construccion Sistema Tridiagonal Lineal|sistemas lineales tridiagonales]] (Thomas, diagonal dominancia), la [[Newton Raphson Multivariable/index|búsqueda de raíces no lineal]] (Newton en disparo y en diferencias finitas no lineales), y los [[RK4 Clasico Tabla Butcher y Orden Cuatro|integradores de PVI]] (en el disparo). Es la confluencia de los seis capítulos de métodos numéricos.

---

## Relación con otras notas

> [!info]
> - Los dos métodos comparados: [[Metodo Disparo Shooting/index]] y [[Metodo Diferencias Finitas/index]].
> - El integrador reutilizado por el disparo: [[RK4 Clasico Tabla Butcher y Orden Cuatro]].
> - El sistema lineal de diferencias finitas: [[Construccion Sistema Tridiagonal Lineal]].
> - La fragilidad por sensibilidad: [[Metodo Newton para Condicion Frontera Residual]] y [[Teoremas Existencia Unicidad Picard Lindelof]].

---

## Resumen

| Criterio | Disparo | Diferencias finitas |
|:---|:---|:---|
| Filosofía | marchar + ajustar | discretización global |
| Precisión | alta (RK4) | $O(h^2)$ |
| Robustez | frágil (PVI sensible) | robusta |
| No lineal | Newton 1 parámetro | Newton sistema completo |
| Escala / EDPs | mala | excelente |

> [!corolario]
> El disparo y las diferencias finitas resuelven el PVF con filosofías opuestas: el disparo marcha como [[Problema Valor Inicial PVI/index|PVI]] ajustando la pendiente inicial —simple y muy preciso con [[RK4 Clasico Tabla Butcher y Orden Cuatro|RK4]], pero frágil si el PVI es sensible—, mientras que las diferencias finitas resuelven un [[Construccion Sistema Tridiagonal Lineal|sistema global]] —robustas y escalables a EDPs, con precisión $O(h^2)$—. La elección depende de la estabilidad del PVI y de la escala del problema; para PVI sensibles o problemas de capa límite, las diferencias finitas (con malla adaptada) ganan. El PVF, al combinar diferenciación, sistemas lineales, raíces e integración, es la síntesis de todo el curso de métodos numéricos.
