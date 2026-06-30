---
title: Potencia Trifásica
order: 3
tags:
  - circuitos-electricos
  - teoria
  - trifasico
  - index
draft: false
aliases:
  - potencia trifásica
  - potencia en trifásico
---

# Potencia Trifásica

> [!definicion]
> La potencia de un sistema trifásico equilibrado es la **suma de las tres fases**. En función de las magnitudes de **línea** —las que se miden— toma la forma compacta
> $$P=\sqrt3\,V_L I_L\cos\varphi,\qquad Q=\sqrt3\,V_L I_L\operatorname{sen}\varphi,\qquad S=\sqrt3\,V_L I_L,$$
> donde $\varphi$ es el ángulo de la impedancia de **fase**. Su gran virtud: la potencia instantánea es **constante** en el tiempo.

> [!info]
> Tercera sección del [[7 Circuitos Trifasicos/index| capítulo 7]]. Aplica la [[Potencia en AC/index| potencia en CA]] (cap. 5) al sistema trifásico, usando las [[Conexiones Balanceadas/index| conexiones Y/Δ]]. Fraile Mora, cap. 3, §3.7-3.9.

---

## Las tres potencias y cómo se miden

> [!teoria] De fase a línea: el $\sqrt3$
> Por fase, la potencia es la de un circuito monofásico, $P_F=V_F I_F\cos\varphi$, y el total es el triple: $P=3V_F I_F\cos\varphi$. Al pasar a magnitudes de línea (con las relaciones $\sqrt3$, que se cancelan de forma que **da igual la conexión**), queda
> $$\boxed{\,P=\sqrt3\,V_L I_L\cos\varphi\,}$$
> y análogamente $Q$ y $S$. La fórmula es **la misma en Y y en Δ**: solo hay que usar las magnitudes de línea y el $\cos\varphi$ de la carga. → [[Potencia en Sistemas Balanceados]].

> [!teoria] Medir con dos vatímetros, y corregir el FP
> En la práctica, la potencia trifásica se mide con **dos** vatímetros (no tres), por el **teorema de Blondel**: con la línea $b$ de referencia, $P=W_1+W_2$ y además $Q=\sqrt3\,(W_2-W_1)$.
>
> ![[dos_vatimetros.svg|560]]
>
> *Las bobinas de corriente de $W_1$ y $W_2$ van en las líneas $a$ y $c$; las de tensión, referidas a $b$. La suma da $P$; la diferencia, $Q$.*
>
> → [[Medicion con Dos Vatimetros]]. Y como en monofásico, un **factor de potencia** bajo penaliza: se corrige con condensadores. → [[Correccion FP Trifasico]].

## Mapa de la sección

> [!info] Las notas de esta sección
> | Nota | Contenido |
> |:---|:---|
> | [[Potencia en Sistemas Balanceados]] | $P=\sqrt3\,V_LI_L\cos\varphi$; $P,Q,S$; potencia constante |
> | [[Medicion con Dos Vatimetros]] | método de Blondel; $P=W_1+W_2$, $Q=\sqrt3(W_2-W_1)$ |
> | [[Correccion FP Trifasico]] | condensadores para subir $\cos\varphi$ |

> [!corolario]
> Una sola fórmula, $P=\sqrt3\,V_LI_L\cos\varphi$, vale para Y y Δ; dos vatímetros bastan para medirla; y unos condensadores corrigen su factor de potencia. La potencia trifásica, además, no pulsa: es constante, la base del par uniforme de los motores.

> [!referencia]
> Fraile Mora, cap. 3, §3.7-3.9. Anterior: [[Conexiones Balanceadas/index| Conexiones balanceadas]]. Siguiente: [[Sistemas Desbalanceados/index| Sistemas desbalanceados]].
