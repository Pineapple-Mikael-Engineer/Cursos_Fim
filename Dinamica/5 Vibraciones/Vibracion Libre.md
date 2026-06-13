---
title: Vibración Libre
tags:
  - dinamica
  - teoria
  - vibraciones
draft: false
aliases:
  - vibración libre
  - oscilador armónico
  - amortiguamiento
  - frecuencia natural
  - regímenes de amortiguamiento
---

# Vibración Libre $\;m\ddot x+c\dot x+kx=0$

> [!definicion]
> La **vibración libre** es la oscilación de un sistema **sin excitación externa**, $m\ddot x+c\dot x+kx=0$.
> **Sin amortiguamiento** ($c=0$) oscila eternamente a su **frecuencia natural**
> $$\omega_n=\sqrt{\frac{k}{m}},\qquad x(t)=A\cos(\omega_n t+\varphi).$$
> **Con amortiguamiento**, el **factor de amortiguamiento** $\zeta=\dfrac{c}{2\sqrt{km}}$ decide el
> comportamiento: oscila y decae ($\zeta<1$), vuelve sin oscilar ($\zeta=1$) o repta ($\zeta>1$).

> [!info]
> Primera nota de las [[5 Vibraciones/index | vibraciones]] ([[Dinamica/index | Dinámica]]). Es
> $\sum F=m\ddot x$ con la fuerza recuperadora del resorte y la disipativa del amortiguador. La
> excitación la añade [[Vibracion Forzada]]. Referencia: Taylor §5.4.

---

## Ejemplo

> [!ejemplo]
> **Frecuencia natural y regímenes.**
>
> Una masa $m=2\ \text{kg}$ cuelga de un resorte $k=200\ \text{N/m}$. Hallar $\omega_n$, el período, y
> el amortiguamiento crítico.
>
> ![[vibracion_amortiguada.svg|640]]
>
> *La respuesta $x(t)$ según $\zeta$: sin amortiguar oscila constante; subamortiguada decae dentro de
> una envolvente exponencial; crítica y sobreamortiguada vuelven sin oscilar.*
>
> **Frecuencia natural.** $\omega_n=\sqrt{k/m}=\sqrt{200/2}=10\ \text{rad/s}$, período
> $T=2\pi/\omega_n\approx0{,}63\ \text{s}$.
> **Amortiguamiento crítico** ($\zeta=1$): $c_c=2\sqrt{km}=2\sqrt{200\cdot2}=40\ \text{N·s/m}$.
>
> > [!solucion]
> > $\omega_n=10\ \text{rad/s}$, $T\approx0{,}63\ \text{s}$, $c_c=40\ \text{N·s/m}$. Con $c<40$ el
> > sistema **oscila** decayendo; con $c\ge40$, vuelve al equilibrio **sin** oscilar.

---

## En qué consiste

> [!teorema] Oscilador no amortiguado
> Para $c=0$, $m\ddot x+kx=0$ tiene solución $x(t)=A\cos(\omega_n t+\varphi)$ con
> $\omega_n=\sqrt{k/m}$; la amplitud $A$ y la fase $\varphi$ las fijan las condiciones iniciales.

> [!demostracion]
> Ensayando $x=e^{st}$ en $m\ddot x+kx=0$: $(ms^2+k)e^{st}=0\Rightarrow s^2=-k/m$, luego
> $s=\pm i\omega_n$ con $\omega_n=\sqrt{k/m}$. La solución real es
> $x=C_1\cos\omega_n t+C_2\operatorname{sen}\omega_n t=A\cos(\omega_n t+\varphi)$. La frecuencia **no
> depende de la amplitud** (isocronía). $\blacksquare$

> [!teorema] Oscilador amortiguado: tres regímenes
> Para $m\ddot x+c\dot x+kx=0$, la **ecuación característica** $ms^2+cs+k=0$ da
> $$s=-\zeta\omega_n\pm\omega_n\sqrt{\zeta^2-1},\qquad \zeta=\frac{c}{2\sqrt{km}}.$$
> El signo de $\zeta^2-1$ separa tres comportamientos:
> - **Subamortiguado** ($\zeta<1$): raíces complejas → **oscila** y decae,
>   $x=e^{-\zeta\omega_n t}\,A\cos(\omega_d t+\varphi)$ con $\omega_d=\omega_n\sqrt{1-\zeta^2}$.
> - **Crítico** ($\zeta=1$): raíz doble → vuelve **sin oscilar**, lo más rápido posible,
>   $x=(A+Bt)e^{-\omega_n t}$.
> - **Sobreamortiguado** ($\zeta>1$): dos raíces reales negativas → vuelve **reptando**.

> [!demostracion]
> Ensayando $x=e^{st}$ en $m\ddot x+c\dot x+kx=0$: $ms^2+cs+k=0$, cuyas raíces son
> $s=\dfrac{-c\pm\sqrt{c^2-4km}}{2m}$. Dividiendo por $2m$ y usando $\omega_n^2=k/m$,
> $\zeta=\dfrac{c}{2\sqrt{km}}=\dfrac{c}{2m\omega_n}$:
> $$s=-\zeta\omega_n\pm\sqrt{\zeta^2\omega_n^2-\omega_n^2}=-\zeta\omega_n\pm\omega_n\sqrt{\zeta^2-1}.$$
> El discriminante $\zeta^2-1$ es negativo, nulo o positivo según $\zeta\lessgtr1$, lo que da los tres
> regímenes. $\blacksquare$

> [!proposicion] La frecuencia baja con el amortiguamiento
> El amortiguamiento **reduce** la frecuencia de oscilación: $\omega_d=\omega_n\sqrt{1-\zeta^2}<\omega_n$.
> El **decremento logarítmico** $\delta=\ln\dfrac{x(t)}{x(t+T_d)}=\zeta\omega_n T_d$ mide la pérdida de
> amplitud por ciclo y permite hallar $\zeta$ experimentalmente.

> [!warning]
> No confundir la frecuencia natural $\omega_n=\sqrt{k/m}$ con la amortiguada
> $\omega_d=\omega_n\sqrt{1-\zeta^2}$ (la que realmente se observa con rozamiento). El régimen
> **crítico** ($\zeta=1$) es el retorno **más rápido** sin oscilación: por eso se diseñan así
> amortiguadores y cierrapuertas. Todo esto supone sistema **lineal** (pequeñas oscilaciones).

## Resumen

> [!resumen]
> | Magnitud | Expresión |
> |:---|:---|
> | Frecuencia natural | $\omega_n=\sqrt{k/m}$ |
> | Factor de amortiguamiento | $\zeta=c/(2\sqrt{km})$ |
> | Raíces | $s=-\zeta\omega_n\pm\omega_n\sqrt{\zeta^2-1}$ |
> | Subamortiguado ($\zeta<1$) | $x=e^{-\zeta\omega_n t}A\cos(\omega_d t+\varphi)$, $\omega_d=\omega_n\sqrt{1-\zeta^2}$ |
> | Crítico / sobre ($\zeta\ge1$) | retorno sin oscilar |

> [!corolario]
> La vibración libre revela las dos constantes que caracterizan al sistema: su **frecuencia natural**
> (cuán rápido oscila) y su **amortiguamiento** (cuán rápido decae). Con ellas queda descrito todo el
> comportamiento transitorio; la respuesta a una excitación la añade la [[Vibracion Forzada]].

> [!referencia]
> Taylor §5.4. Excitación y resonancia: [[Vibracion Forzada]]. Paralelo eléctrico: el circuito RLC.
