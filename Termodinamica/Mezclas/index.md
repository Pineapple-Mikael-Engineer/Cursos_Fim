---
title: Mezclas Termodinámicas
tags:
  - termodinamica
  - teoria
  - mezclas
  - indice
draft: false
aliases:
  - Mezclas
  - Mezclas Termodinámicas
---

# Mezclas Termodinámicas

> [!definicion]
> Una **mezcla** es un sistema termodinámico compuesto por dos o más sustancias puras que no reaccionan entre sí (mezcla no reactiva) o que sí lo hacen (combustión). En ambos casos la composición determina las propiedades: masa molecular aparente, presión parcial, entalpía de formación. Las mezclas de gases ideales son el modelo base; la psicrometría es el caso especial aire seco-vapor de agua; la combustión extiende el análisis a mezclas reactivas.

> [!info]
> **Ubicación.** Curso MN121 · sección Mezclas. Se apoya en [[../Propiedades/Sustancias Puras/index | Sustancias Puras]], [[../Propiedades/Ecuaciones de Estado/Gas Ideal | Gas Ideal]] y los balances de [[../Conservacion/Volumenes de Control/Balance de Energia VC | volúmenes de control]]. Alimenta los ciclos (Brayton con aire húmedo, calderas).

---

## Clasificación

| Tipo de mezcla | Modelo | Notas |
|:---|:---|:---|
| Gases ideales no reactivos | Dalton / Amagat | [[Mezclas de Gases]] |
| Aire húmedo (aire + vapor H₂O) | Psicrometría | [[Psicrometria/index \| Psicrometría]] |
| Combustibles + oxidante | Estequiometría, entalpía de formación | [[Combustion/index \| Combustión]] |

---

## Principio unificador: aditividad de extensivas

Para cualquier mezcla no reactiva, las propiedades extensivas específicas se obtienen por suma ponderada (fracción molar o másica):
$$y_{\rm mezcla} = \sum_i y_i \cdot y_i^{(\rm componente)},$$
donde $y_i$ es la fracción molar (o másica según la base). La entropía es la excepción: cada componente se evalúa a su **presión parcial**, no a la presión total, lo que genera la **entropía de mezcla** (siempre positiva para gases distintos).

---

## Notas de esta sección

> [!info] Mapa
> - [[Mezclas de Gases]] — composición (fracciones molar/másica), modelos de Dalton y Amagat, propiedades $u$, $h$, $s$; entropía de mezcla; ejemplo con gas de síntesis.
> - [[Psicrometria/index | Psicrometría]] — propiedades del aire húmedo ($\omega$, $\phi$, $T_d$, $T_{bh}$); diagrama psicrométrico.
> - [[Psicrometria/Procesos Psicrometricos | Procesos Psicrométricos]] — calentamiento, enfriamiento, humidificación, deshumidificación, mezcla de corrientes; ejemplos con balance de masa y energía.
> - [[Combustion/index | Combustión]] — estequiometría, relación aire-combustible, poder calorífico (PCS/PCI), análisis de productos.
> - [[Combustion/Temperatura Adiabatica de Llama | Temperatura Adiabática de Llama]] — balance entálpico para $T_{\rm AFT}$; ejemplo con metano y exceso de aire.

> [!referencia]
> Çengel & Boles, *Termodinámica*, caps. 13–15; Moran & Shapiro, *Fundamentals of Engineering Thermodynamics*, caps. 12–13; Borgnakke & Sonntag, caps. 12–13.
