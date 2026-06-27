---
title: "Ecuaciones de Estado"
order: 4
tags:
  - termodinamica
  - propiedades
  - ecuaciones_de_estado
  - index
draft: false
aliases:
  - equations of state
  - EOS
  - ecuación de estado
---

# Ecuaciones de Estado $f(P,\,v,\,T) = 0$

> [!definicion]
> Una **ecuación de estado** (EOS) es la relación algebraica entre las tres propiedades $P$, $v$ y $T$ de una sustancia simple compresible. Una vez conocidas dos de ellas, la EOS fija la tercera. Es el ingrediente que cierra todos los balances y permite calcular variaciones de energía interna, entalpía y entropía para sustancias que no tienen tablas disponibles.
>
> *¿Por qué no siempre usar tablas?* Las tablas son exactas pero discretas y limitadas a las sustancias tabuladas. Una EOS analítica permite interpolar, derivar, integrar y automatizar cálculos para cualquier sustancia una vez conocidas unas pocas constantes de la sustancia.

![[EOS_jerarquia_modelos.svg|440]]
*Jerarquía de modelos de EOS. El gas ideal ($Z=1$) es el límite a baja presión. El factor $Z$ cuantifica el desvío. Las EOS cúbicas (van der Waals, SRK, PR) corrigen el desvío analíticamente. Las tablas son la referencia de exactitud máxima.*

---

## ¿Por qué existe el desvío del gas ideal?

Dos efectos moleculares que el gas ideal ignora:

1. **Fuerzas atractivas** entre moléculas (tipo Van der Waals, dipolo-dipolo, inducción): hacen que las moléculas «quieran» estar juntas y que la presión efectiva sobre las paredes sea *menor* de lo esperado → $Z < 1$.

2. **Volumen propio** de las moléculas: el espacio disponible para moverse es $v - b$ en lugar de $v$ → a alta presión, la molécula «tropieza» antes → $Z > 1$.

A presiones moderadas, ambos efectos se compensan. A alta presión ($P \gg P_c$), domina el covolumen. Cerca de la saturación, dominan las atracciones.

---

## Factor de compresibilidad

> [!proposicion]
> El apartamiento del comportamiento ideal se cuantifica con:
> $$
> Z = \frac{Pv}{RT}, \qquad Z = 1 \text{ (gas ideal)}.
> $$
> El **principio de estados correspondientes** afirma que $Z \approx Z(P_r, T_r)$ es casi universal para gases no polares, con $P_r = P/P_c$ y $T_r = T/T_c$. Esto justifica las cartas de compresibilidad generalizadas de Nelson-Obert, usadas cuando no se tiene EOS específica de la sustancia.

---

## Jerarquía de modelos

| Modelo | Ecuación | Cuándo usar |
|:---|:---|:---|
| [[Gas Ideal]] | $Pv = RT$ | $T_r > 2$ o $P_r < 0.1$; gases a condiciones atmosféricas |
| Factor $Z$ | $Pv = ZRT$ | Desvío moderado; se lee $Z(P_r, T_r)$ de cartas Nelson-Obert |
| Van der Waals | $(P+a/\bar{v}^2)(\bar{v}-b)=R_uT$ | Ilustración conceptual; error ~30% cerca del crítico |
| SRK / PR | EOS cúbicas con $\alpha(T_r,\omega)$ | Ingeniería de procesos; hidrocarburos y mezclas |
| Tablas | datos tabulados exactos | Sustancias puras: agua, refrigerantes, aire tabulado |

---

## Papel en las relaciones de propiedades

> [!teoria]
> La EOS provee las derivadas parciales $(\partial P/\partial T)_v$ y $(\partial v/\partial T)_P$ que aparecen en:
> - Las **relaciones de Maxwell** (ver [[../../Relaciones Termodinamicas/Maxwell | Maxwell]]): para calcular variaciones de entropía desde $P$, $T$, $v$.
> - Las **ecuaciones $TdS$**: para integrar $du$, $dh$, $ds$ en sustancias sin tablas.
> - La diferencia $c_p - c_v = -T[(\partial P/\partial T)_v]^2/(\partial P/\partial v)_T$ (ver [[../../Relaciones Termodinamicas/Cp Cv/index | $c_p - c_v$]]).
>
> Por eso, conocida la EOS y los calores específicos $c_v(T)$ o $c_p(T)$ a baja presión, quedan determinados todos los cambios de propiedades termodinámicas a cualquier estado.

---

## Mapa de notas

> [!info]
> - [[Gas Ideal]] — hipótesis moleculares, $Pv=RT$, $u=u(T)$, relación de Mayer $c_p-c_v=R$, procesos isentrópicos, validez.
> - [[Gas Real]] — factor $Z$, van der Waals (deducción de $a$, $b$ desde el punto crítico), principio de estados correspondientes, EOS mejoradas (SRK, PR), ejemplo numérico con $\mathrm{N_2}$.

> [!referencia]
> Borgnakke & Sonntag, *Fundamentals of Thermodynamics*, caps. 3 y 12; Çengel & Boles, *Termodinámica*, cap. 3; Callen, *Thermodynamics*, §9 (EOS como postulado); Smith, Van Ness & Abbott, *Introduction to Chemical Engineering Thermodynamics*, cap. 3 (EOS cúbicas en simuladores).
