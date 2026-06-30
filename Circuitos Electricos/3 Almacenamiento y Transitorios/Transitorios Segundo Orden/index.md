---
title: Transitorios de Segundo Orden
order: 3
tags:
  - circuitos-electricos
  - teoria
  - transitorios
  - segundo-orden
  - index
draft: false
aliases:
  - transitorios de segundo orden
  - circuitos RLC
  - circuitos de segundo orden
---

# Transitorios de Segundo Orden

> [!definicion]
> Un circuito de **segundo orden** tiene **dos** elementos almacenadores (un $L$ y un $C$). Al aplicar Kirchhoff aparece una **ecuación diferencial de segundo orden**
> $$\frac{d^2x}{dt^2}+2\alpha\,\frac{dx}{dt}+\omega_0^2\,x = \text{(forzamiento)},$$
> cuya respuesta natural puede, por primera vez, **oscilar**. Todo depende de dos parámetros: el **coeficiente de amortiguamiento** $\alpha$ y la **frecuencia natural** $\omega_0=1/\sqrt{LC}$.

> [!info]
> Tercera sección del [[3 Almacenamiento y Transitorios/index| capítulo 3]]. Generaliza los [[Transitorios Primer Orden/index| transitorios de primer orden]] añadiendo un segundo almacenador; reutiliza la continuidad de [[Capacitor]] e [[Inductor]]. Fraile Mora, cap. 4, §4.6.

---

## Por qué ahora puede oscilar

> [!teoria] Dos almacenadores intercambian energía
> Con un solo almacenador, la energía solo podía **disiparse** (decaimiento exponencial). Con **dos** —un inductor y un condensador— la energía puede **ir y venir** entre el campo magnético y el eléctrico: ese vaivén es la **oscilación**. La resistencia, mientras tanto, la **amortigua**. El resultado depende de quién gane:
> $$s^2+2\alpha s+\omega_0^2=0 \;\Longrightarrow\; s=-\alpha\pm\sqrt{\alpha^2-\omega_0^2}.$$
> El signo de $\alpha^2-\omega_0^2$ decide la forma de la respuesta y da los **tres regímenes** de amortiguamiento. → [[Regimenes de Amortiguamiento]].

> [!teoria] Los dos parámetros, y el cociente que manda
> - $\omega_0=\dfrac{1}{\sqrt{LC}}$ es la **frecuencia natural** (a la que oscilaría sin pérdidas), igual en serie y en paralelo.
> - $\alpha$ es el **amortiguamiento**, y **sí** cambia según la topología: $\alpha=\dfrac{R}{2L}$ en el [[Circuito RLC Serie| RLC serie]] y $\alpha=\dfrac{1}{2RC}$ en el [[Circuito RLC Paralelo| RLC paralelo]] (¡fíjate en la dualidad!).
>
> Su cociente, el **factor de amortiguamiento** $\zeta=\alpha/\omega_0$, resume todo: $\zeta>1$ sobreamortiguado, $\zeta=1$ crítico, $\zeta<1$ subamortiguado (oscila).

## Mapa de la sección

> [!info] Qué desarrolla cada hija
> | Nota | Contenido |
> |:---|:---|
> | [[Circuito RLC Serie]] | la EDO del RLC serie; $\alpha=R/2L$, $\omega_0=1/\sqrt{LC}$ |
> | [[Circuito RLC Paralelo]] | el dual; $\alpha=1/2RC$, misma $\omega_0$ |
> | [[Regimenes de Amortiguamiento]] | los tres regímenes (sub/crítico/sobre) y la oscilación |
> | [[Funciones Singulares]] | escalón, impulso y rampa: las excitaciones de prueba |

> [!corolario]
> El segundo orden añade una posibilidad nueva —la oscilación— al repertorio del primer orden. Dos números, $\alpha$ y $\omega_0$, y su cociente $\zeta$, deciden si la respuesta decae sin más o **oscila** mientras se amortigua. Resolverlo es lo que prepara para el régimen sinusoidal.

> [!referencia]
> Fraile Mora, cap. 4, §4.6. Anterior: [[Transitorios Primer Orden/index| Transitorios de primer orden]]. Siguiente: [[Laplace en Circuitos/index| Laplace en circuitos]].
