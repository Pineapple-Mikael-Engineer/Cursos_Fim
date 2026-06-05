---
title: Inestabilidad y Error de Redondeo en el Paso h
tags:
  - metodos-numericos
  - teoria
  - diferenciacion-integracion
  - diferenciacion-numerica
  - error-numerico
draft: false
aliases:
  - Paso óptimo h
  - Inestabilidad de diferencias finitas
  - Truncamiento vs redondeo
  - Optimal step size
---

# Inestabilidad y Error de Redondeo en el Paso $h$

> [!definicion]
> La **diferenciación numérica está mal condicionada**: el error total combina el **truncamiento** (que decrece con $h$) y el **redondeo** (que crece al decrecer $h$). Existe un **paso óptimo** $h^*$ que minimiza el error; por debajo de él, reducir $h$ **empeora** el resultado.

> [!info]
> Es el comportamiento opuesto al de la integración. La causa es la [[Perdida Significancia y Cancelacion Catastrofica|cancelación catastrófica]]: al dividir una diferencia de valores casi iguales por un $h$ minúsculo, el ruido de redondeo de $f$ se amplifica por $1/h$.

---

## Descomposición del error total

> [!teorema]
> Para la diferencia progresiva $D(h) = \frac{f(x+h)-f(x)}{h}$, con [[Epsilon Maquina y Precision Relativa|unidad de redondeo]] $u$ y $|f| \sim M_0$, el error total se acota por
> $$E(h) \lesssim \underbrace{\frac{h}{2}M_2}_{\text{truncamiento}} + \underbrace{\frac{2 u M_0}{h}}_{\text{redondeo}},$$
> donde $M_2 = \max|f''|$. El primer término baja con $h$; el segundo sube.

> [!demostracion]
> El truncamiento es $\frac{h}{2}|f''(\xi)|$ (serie de Taylor). Para el redondeo: los valores calculados son $\tilde f(x) = f(x)(1+\delta_1)$, $\tilde f(x+h) = f(x+h)(1+\delta_2)$ con $|\delta_i|\leq u$. El error en el numerador es $\leq 2uM_0$, que al dividir entre $h$ da $\frac{2uM_0}{h}$.

---

## Paso óptimo

> [!teorema]
> Minimizando $E(h) = \frac{h}{2}M_2 + \frac{2uM_0}{h}$ respecto a $h$ (derivar e igualar a cero):
> $$h^* = 2\sqrt{\frac{u M_0}{M_2}} \sim \sqrt{u}, \qquad E(h^*) \sim \sqrt{u}.$$
> Para la diferencia **centrada** ($O(h^2)$), el equilibrio da $h^* \sim u^{1/3}$ y error mínimo $\sim u^{2/3}$.

> [!info]
> | Esquema | Truncamiento | Paso óptimo $h^*$ | Error mínimo |
> |:---|:---|:---:|:---:|
> | Progresiva | $O(h)$ | $\sim u^{1/2} \approx 10^{-8}$ | $\sim u^{1/2} \approx 10^{-8}$ |
> | Centrada | $O(h^2)$ | $\sim u^{1/3} \approx 10^{-5}$ | $\sim u^{2/3} \approx 10^{-11}$ |
>
> En doble precisión ($u\approx10^{-16}$), la derivada numérica **nunca** alcanza precisión de máquina: lo mejor es $\sim10^{-8}$ (progresiva) o $\sim10^{-11}$ (centrada).

---

## Ejemplo: la curva en "V"

> [!ejemplo]
> **$f(x)=e^x$ en $x=0$, diferencia centrada** ($f'(0)=1$):
>
> | $h$ | Error total | Régimen dominante |
> |:---:|:---:|:---|
> | $10^{-1}$ | $1.7\times10^{-3}$ | truncamiento |
> | $10^{-3}$ | $1.7\times10^{-7}$ | truncamiento |
> | $10^{-5}$ | $\sim2\times10^{-11}$ | **óptimo** ($h^*\approx u^{1/3}$) |
> | $10^{-8}$ | $\sim7\times10^{-9}$ | redondeo |
> | $10^{-12}$ | $\sim7\times10^{-5}$ | redondeo (catastrófico) |
>
> El error en escala log-log forma una **"V"**: baja con pendiente $2$ (truncamiento), toca el mínimo en $h^*$ y sube con pendiente $-1$ (redondeo). Reducir $h$ más allá de $h^*$ es contraproducente.

---

## Cómo mitigar la inestabilidad

> [!info]
> | Estrategia | Efecto |
> |:---|:---|
> | Usar el paso óptimo $h^* \sim u^{1/3}$ (centrada) | minimiza el error |
> | [[Extrapolacion Richardson Aceleracion Convergencia\|Richardson]] | mayor orden ⇒ $h$ mayor ⇒ menos redondeo |
> | **Diferenciación compleja** $\operatorname{Im}[f(x+ih)]/h$ | sin cancelación, error $O(h^2)$ sin barrera de redondeo |
> | Diferenciación automática | derivada exacta, sin $h$ |

> [!teoria]
> **El truco del paso complejo.** Si $f$ es analítica, $f'(x) \approx \frac{\operatorname{Im}[f(x+ih)]}{h}$ con error $O(h^2)$ y **sin** resta de cantidades casi iguales: no hay cancelación, así que $h$ puede tomarse tan pequeño como $10^{-200}$ y se alcanza precisión de máquina. Supera la barrera fundamental de las diferencias finitas reales.

---

## Relación con otras notas

> [!info]
> - La causa raíz: [[Perdida Significancia y Cancelacion Catastrofica]].
> - La unidad de redondeo $u$: [[Epsilon Maquina y Precision Relativa]].
> - Los esquemas afectados: [[Orden Error Progresiva Regresiva Centrada]].
> - La aceleración que reduce la presión sobre $h$: [[Extrapolacion Richardson Aceleracion Convergencia]].
> - El contraste con la estabilidad de la integración: [[Trapecio Compuesto Convergencia O h2]].

---

## Resumen

| Aspecto | Descripción |
|:---|:---|
| Error total | truncamiento $O(h^p)$ + redondeo $O(u/h)$ |
| Paso óptimo (progresiva) | $h^* \sim u^{1/2}$ |
| Paso óptimo (centrada) | $h^* \sim u^{1/3}$ |
| Error mínimo (centrada) | $\sim u^{2/3} \approx 10^{-11}$ |
| Curva del error | "V" en log-log |
| Remedio sin barrera | paso complejo, dif. automática |

> [!corolario]
> La diferenciación numérica está mal condicionada porque su error total suma truncamiento $O(h^p)$ —que baja con $h$— y redondeo $O(u/h)$ —que sube—, produciendo un paso óptimo $h^*\sim u^{1/3}$ (centrada) más allá del cual reducir $h$ empeora el resultado por [[Perdida Significancia y Cancelacion Catastrofica|cancelación]]. En doble precisión la derivada nunca alcanza precisión de máquina con diferencias reales: lo mejor es $\sim10^{-11}$. La [[Extrapolacion Richardson Aceleracion Convergencia|extrapolación]], el paso complejo o la diferenciación automática mitigan o eluden la barrera. Esta fragilidad es el rasgo que distingue a la diferenciación de la estable [[Integracion Numerica Newton Cotes/index|integración numérica]].
