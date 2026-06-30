---
title: Diferenciación Numérica
order: 1
tags:
  - metodos-numericos
  - teoria
  - diferenciacion-integracion
  - diferenciacion-numerica
  - index
draft: false
aliases:
  - Diferenciación numérica
  - Diferencias finitas
  - Numerical differentiation
---

# Diferenciación Numérica

> [!definicion]
> La **diferenciación numérica** aproxima derivadas $f'(x), f''(x), \dots$ mediante combinaciones lineales de valores de $f$ en puntos cercanos (diferencias finitas), deducidas de la serie de Taylor.

> [!info]
> Es la herramienta para derivar funciones tabuladas o sin forma cerrada, y la base de los métodos de [[6 Ecuaciones Diferenciales Ordinarias/index|EDOs]] y de diferencias finitas para EDPs. A diferencia de la integración, está **mal condicionada**: el paso $h$ enfrenta un compromiso entre truncamiento y redondeo.

---

## Esquemas y su orden

> [!info]
> Las [[Aproximacion Diferencias Finitas Serie Taylor|fórmulas de diferencias finitas]] se derivan de la serie de Taylor; según los puntos usados, su [[Orden Error Progresiva Regresiva Centrada|orden de error]] es $O(h)$ (progresiva/regresiva) u $O(h^2)$ (centrada). La [[Extrapolacion Richardson Aceleracion Convergencia|extrapolación de Richardson]] combina pasos para subir el orden.

## El compromiso del paso $h$

> [!warning]
> Reducir $h$ disminuye el error de **truncamiento** ($\sim h^p$) pero aumenta el de **redondeo** ($\sim u/h$). Existe un $h$ óptimo; por debajo, la [[Inestabilidad Error Redondeo Paso h|cancelación]] domina y la derivada calculada empeora. Es lo opuesto a la integración.

---

## Ejemplo

> [!ejemplo]
> **Derivada de $f(x)=e^x$ en $x=0$ ($f'(0)=1$) por diferencia centrada:**
>
> | $h$ | $\frac{f(h)-f(-h)}{2h}$ | error |
> |:---:|:---:|:---:|
> | $10^{-1}$ | 1.001667 | $1.7\times10^{-3}$ |
> | $10^{-3}$ | 1.000000167 | $1.7\times10^{-7}$ |
> | $10^{-5}$ | 1.0000000000 | $\sim10^{-11}$ |
> | $10^{-8}$ | 0.999999994 | $\sim10^{-8}$ (¡empeora!) |
>
> El error baja como $h^2$ hasta $h\approx10^{-5}$ y luego **sube** por redondeo: la firma del mal condicionamiento.

---

## Resumen

| Tema | Nota |
|:---|:---|
| Deducción por serie de Taylor | [[Aproximacion Diferencias Finitas Serie Taylor]] |
| Orden: progresiva, regresiva, centrada | [[Orden Error Progresiva Regresiva Centrada]] |
| Aceleración de convergencia | [[Extrapolacion Richardson Aceleracion Convergencia]] |
| Inestabilidad y paso óptimo | [[Inestabilidad Error Redondeo Paso h]] |

> [!corolario]
> La diferenciación numérica aproxima derivadas por diferencias finitas deducidas de la [[Aproximacion Diferencias Finitas Serie Taylor|serie de Taylor]], con [[Orden Error Progresiva Regresiva Centrada|orden]] $O(h)$ o $O(h^2)$ según el esquema, mejorable por [[Extrapolacion Richardson Aceleracion Convergencia|Richardson]]. Su rasgo distintivo es el mal condicionamiento: el [[Inestabilidad Error Redondeo Paso h|paso óptimo $h$]] equilibra truncamiento y redondeo, y reducir $h$ en exceso empeora el resultado. Es la base de la discretización de [[6 Ecuaciones Diferenciales Ordinarias/index|ecuaciones diferenciales]].
