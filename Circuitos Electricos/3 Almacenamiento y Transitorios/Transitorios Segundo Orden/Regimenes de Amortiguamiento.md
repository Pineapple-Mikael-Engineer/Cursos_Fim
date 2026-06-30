---
title: Regímenes de Amortiguamiento
order: 3
tags:
  - circuitos-electricos
  - teoria
  - transitorios
  - segundo-orden
  - amortiguamiento
draft: false
aliases:
  - regímenes de amortiguamiento
  - amortiguamiento
  - sobreamortiguado crítico subamortiguado
  - damping regimes
---

# Regímenes de Amortiguamiento

> [!definicion]
> Según cómo compitan el amortiguamiento $\alpha$ y la frecuencia natural $\omega_0$ —resumidos en el **factor de amortiguamiento** $\zeta=\alpha/\omega_0$—, la respuesta natural de un circuito de segundo orden adopta uno de **tres regímenes**: **sobreamortiguado** ($\zeta>1$, decae sin oscilar), **crítico** ($\zeta=1$, el decaimiento más rápido sin oscilar) y **subamortiguado** ($\zeta<1$, **oscila** mientras se amortigua).

> [!info]
> El corazón de los [[Transitorios Segundo Orden/index| transitorios de segundo orden]] del [[3 Almacenamiento y Transitorios/index| capítulo 3]]: clasifica la respuesta del [[Circuito RLC Serie]] y el [[Circuito RLC Paralelo]] según las raíces de su ecuación característica. Fraile Mora, cap. 4, §4.6.

---

## Ejemplo

> [!ejemplo]
> **Los tres regímenes, lado a lado.**
>
> Para una misma $\omega_0$, al aumentar el amortiguamiento (más $R$ en serie, menos en paralelo) la respuesta pasa de oscilante a lenta sin oscilar:
>
> ![[amortiguamiento.svg|600]]
>
> *Respuesta al escalón. **Subamortiguado** ($\zeta<1$): sobrepasa y oscila. **Crítico** ($\zeta=1$): llega lo más rápido posible sin sobrepasar. **Sobreamortiguado** ($\zeta>1$): lento, sin oscilar.*
>
> > [!solucion]
> > El régimen lo fija $\zeta=\alpha/\omega_0$: $0{,}25$ (oscila con sobrepico), $1$ (frontera, sin sobrepico y rápido), $2{,}5$ (lento). El crítico es el **más veloz que no oscila**.

---

## En qué consiste

> [!teoria] Tres formas según las raíces $s=-\alpha\pm\sqrt{\alpha^2-\omega_0^2}$
> El discriminante $\alpha^2-\omega_0^2$ de la [[Circuito RLC Serie| ecuación característica]] decide la forma de la respuesta natural:
>
> - **Sobreamortiguado** ($\alpha>\omega_0$, $\zeta>1$): dos raíces **reales** negativas $s_1,s_2$. La respuesta es suma de dos exponenciales, $x(t)=A\,e^{s_1 t}+B\,e^{s_2 t}$. **No oscila**; domina el decaimiento más lento. La resistencia se "lleva" la energía antes de que pueda ir y venir.
>
> - **Crítico** ($\alpha=\omega_0$, $\zeta=1$): raíz **doble** $s=-\alpha$. La respuesta es $x(t)=(A+Bt)\,e^{-\alpha t}$. Es la frontera: **el regreso más rápido al reposo sin oscilar**, muy buscado en sistemas de control (medidores, suspensiones).
>
> - **Subamortiguado** ($\alpha<\omega_0$, $\zeta<1$): raíces **complejas conjugadas** $s=-\alpha\pm j\omega_d$. La respuesta **oscila** dentro de una envolvente que decae:
>   $$x(t)=e^{-\alpha t}\big(A\cos\omega_d t+B\sin\omega_d t\big),\qquad \omega_d=\sqrt{\omega_0^2-\alpha^2}.$$

> [!ejemplo] La oscilación subamortiguada y su envolvente
> ![[oscilacion_amortiguada.svg|560]]
>
> *La respuesta subamortiguada oscila a la **frecuencia amortiguada** $\omega_d$, encerrada entre las envolventes $\pm e^{-\alpha t}$: $\alpha$ marca lo rápido que se apaga; $\omega_d$, lo rápido que oscila.*

> [!info] Las tres frecuencias y el factor $\zeta$
> | Régimen | Condición | Raíces | Respuesta natural |
> |:---|:---|:---|:---|
> | Sobreamortiguado | $\zeta>1$ | reales $s_1,s_2$ | $A e^{s_1 t}+B e^{s_2 t}$ |
> | Crítico | $\zeta=1$ | doble $-\alpha$ | $(A+Bt)e^{-\alpha t}$ |
> | Subamortiguado | $\zeta<1$ | $-\alpha\pm j\omega_d$ | $e^{-\alpha t}(A\cos\omega_d t+B\sin\omega_d t)$ |
>
> con $\zeta=\dfrac{\alpha}{\omega_0}$ y $\omega_d=\omega_0\sqrt{1-\zeta^2}$ (solo si $\zeta<1$).

> [!proposicion] Sobrepico y asentamiento
> En el régimen subamortiguado, cuanto menor es $\zeta$ mayor es el **sobrepico** (lo que la respuesta rebasa su valor final) y más oscilaciones hay antes de asentarse. El **tiempo de asentamiento** lo fija la envolvente: $\approx 4/\alpha$ a $5/\alpha$ (análogo a los $5\tau$ del primer orden, con $\tau=1/\alpha$).

> [!warning]
> El régimen **no** depende de la excitación, solo de los elementos ($\alpha$ y $\omega_0$). Más amortiguamiento no siempre es mejor: el sobreamortiguado es **lento**; el crítico da el mejor compromiso velocidad-estabilidad. Y "oscilar" aquí significa oscilación **amortiguada** (se extingue), no permanente.

## Resumen

> [!resumen]
> | Aspecto | Resumen |
> |:---|:---|
> | Parámetro decisivo | $\zeta=\alpha/\omega_0$ |
> | $\zeta>1$ | sobreamortiguado: 2 exponenciales, lento, sin oscilar |
> | $\zeta=1$ | crítico: $(A+Bt)e^{-\alpha t}$, más rápido sin oscilar |
> | $\zeta<1$ | subamortiguado: oscila a $\omega_d=\omega_0\sqrt{1-\zeta^2}$ bajo $e^{-\alpha t}$ |
> | Envolvente / asentamiento | $\pm e^{-\alpha t}$, $\sim 4/\alpha$ |

> [!corolario]
> Un solo número, $\zeta=\alpha/\omega_0$, clasifica toda la dinámica de segundo orden. El crítico separa el mundo monótono (sobre) del oscilante (sub). Esta misma idea —polos reales vs. complejos— reaparece, ya en el plano $s$, con la [[Laplace en Circuitos/index| transformada de Laplace]].

> [!referencia]
> Fraile Mora, cap. 4, §4.6. Aplicado en: [[Circuito RLC Serie]] y [[Circuito RLC Paralelo]]. Visto en el plano $s$: [[Funcion de Transferencia]].
