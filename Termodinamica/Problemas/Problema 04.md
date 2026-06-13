---
title: "Problema 04 — Relaciones de propiedades para un gas de van der Waals"
tags:
  - termodinamica
  - problemas
  - relaciones_termodinamicas
  - maxwell
draft: false
aliases:
  - van der Waals propiedades
  - energía interna gas real
---

# Problema 04 — Relaciones de propiedades para un gas de van der Waals

> [!definicion] Enunciado
> Un gas obedece la ecuación de estado de van der Waals (forma molar):
> $$
> \left(P + \frac{a}{\bar v^{\,2}}\right)(\bar v - b) = R T \quad\Longleftrightarrow\quad P = \frac{RT}{\bar v - b} - \frac{a}{\bar v^{\,2}}
> $$
>
> Se pide, usando solo relaciones de propiedades:
> 1. Demostrar que $\left(\partial \bar u/\partial \bar v\right)_T = a/\bar v^{\,2}$ y evaluar $\Delta \bar u$ en una expansión isotérmica.
> 2. Obtener $\Delta \bar s$ entre dos estados.
> 3. Obtener $c_p - c_v$ y verificar el límite de [[Gas Ideal]].

## Estrategia

> [!teoria]
> El objetivo es expresar magnitudes no medibles ([[Energia Interna | energía interna]], [[Entropia | entropía]]) en términos de la ecuación de estado $P\text{-}\bar v\text{-}T$ y los calores específicos. Las herramientas son las relaciones de [[Maxwell]] y las ecuaciones [[TdS]].
>
> Derivada que se reutiliza en todo el problema:
> $$
> \left(\frac{\partial P}{\partial T}\right)_{\bar v} = \frac{R}{\bar v - b}
> $$

## Inciso 1 — Dependencia de la energía interna con el volumen

> [!demostracion]
> De $\bar u = \bar u(T,\bar v)$ y la primera ecuación [[TdS]], $T\,d\bar s = d\bar u + P\,d\bar v$, se obtiene la **ecuación térmica de estado de la energía**:
> $$
> \left(\frac{\partial \bar u}{\partial \bar v}\right)_T = T\left(\frac{\partial P}{\partial T}\right)_{\bar v} - P
> $$
> donde el término $T(\partial P/\partial T)_{\bar v}$ proviene de la relación de [[Maxwell]] desde la energía de Helmholtz. Sustituyendo van der Waals:
> $$
> \left(\frac{\partial \bar u}{\partial \bar v}\right)_T = T\,\frac{R}{\bar v - b} - \left(\frac{RT}{\bar v - b} - \frac{a}{\bar v^{\,2}}\right) = \frac{a}{\bar v^{\,2}}
> $$

> [!info]
> A diferencia del [[Gas Ideal]] —donde $\bar u = \bar u(T)$ y $(\partial \bar u/\partial \bar v)_T = 0$—, en un gas real la energía interna **sí depende del volumen**: el término $a/\bar v^{\,2}$ mide el trabajo contra las fuerzas atractivas al separar las moléculas.

> [!ejemplo]
> **Expansión isotérmica de CO₂.** Con $a = 0.3643\ \text{Pa·m}^6/\text{mol}^2$, expandiendo de $\bar v_1 = 5\times10^{-4}$ a $\bar v_2 = 1\times10^{-3}\ \text{m}^3/\text{mol}$ a $T$ constante:
> $$
> \Delta \bar u = \int_{\bar v_1}^{\bar v_2} \frac{a}{\bar v^{\,2}}\,d\bar v = a\left(\frac{1}{\bar v_1} - \frac{1}{\bar v_2}\right) = 0.3643\,(2000 - 1000) = 364.3\ \text{J/mol}
> $$
> La energía interna **aumenta** aunque $T$ no cambie: energía almacenada contra la atracción intermolecular, invisible para el modelo de gas ideal.

## Inciso 2 — Cambio de entropía

> [!solucion]
> De la primera ecuación [[TdS]] dividida entre $T$:
> $$
> d\bar s = \frac{c_v}{T}\,dT + \left(\frac{\partial P}{\partial T}\right)_{\bar v} d\bar v = \frac{c_v}{T}\,dT + \frac{R}{\bar v - b}\,d\bar v
> $$
> Integrando entre dos estados:
> $$
> \Delta \bar s = \int_{T_1}^{T_2} \frac{c_v}{T}\,dT + R\,\ln\frac{\bar v_2 - b}{\bar v_1 - b}
> $$
> El covolumen $b$ corrige el término de volumen del [[Gas Ideal]] ($R\ln(\bar v_2/\bar v_1)$): el espacio realmente accesible es $\bar v - b$, no $\bar v$.

## Inciso 3 — Diferencia de calores específicos

> [!proposicion]
> Igualando las dos ecuaciones [[TdS]] se obtiene la relación general (ver [[Cp Cv/index | $c_p - c_v$]]):
> $$
> c_p - c_v = T\left(\frac{\partial P}{\partial T}\right)_{\bar v}\!\left(\frac{\partial \bar v}{\partial T}\right)_P = -\,T\,\frac{\left(\partial P/\partial T\right)_{\bar v}^{\,2}}{\left(\partial P/\partial \bar v\right)_T}
> $$

> [!solucion]
> Con $\left(\partial P/\partial T\right)_{\bar v} = R/(\bar v - b)$ y $\left(\partial P/\partial \bar v\right)_T = -RT/(\bar v - b)^2 + 2a/\bar v^{\,3}$:
> $$
> c_p - c_v = \frac{R}{\,1 - \dfrac{2a\,(\bar v - b)^2}{R T\,\bar v^{\,3}}\,}
> $$

> [!info] Verificación del límite ideal
> Cuando $a \to 0$ y $b \to 0$, el denominador tiende a $1$ y se recupera la relación de Mayer del [[Gas Ideal]]:
> $$
> c_p - c_v = R
> $$
> El cociente $> 1$ para $a>0$ muestra que en el gas real $c_p - c_v$ excede a $R$, salvo cancelaciones por el covolumen.

## Notas usadas

> [!referencia]
> [[Maxwell]] · [[TdS]] · [[Cp Cv/index | $c_p - c_v$]] · [[Energia Interna]] · [[Entropia]] · [[Entalpia]] · [[Gas Ideal]]

> [!info]
> **Convención de notación**:
> - barra: magnitudes **molares** ($\bar u$, $\bar v$, $\bar s$); $a$, $b$: constantes de van der Waals.
> - derivadas $\left(\partial P/\partial T\right)_{\bar v}$, etc.: evaluadas desde la ecuación de estado.
