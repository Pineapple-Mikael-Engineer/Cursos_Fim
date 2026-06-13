---
title: Oscilaciones Forzadas y Resonancia
tags:
  - ecuaciones
  - edo
  - teoria
  - lineales
  - oscilaciones
  - resonancia
draft: false
aliases:
  - oscilaciones forzadas
  - resonancia
  - estado estacionario
  - forced oscillations
  - resonance
---

# Oscilaciones Forzadas y Resonancia

> [!definicion]
> El **oscilador forzado** por una fuerza armónica es
> $$m\ddot x+c\dot x+kx=F_0\cos\omega t.$$
> Su solución se separa en dos partes:
> $$x(t)=\underbrace{x_h(t)}_{\text{transitorio (decae)}}+\underbrace{x_p(t)}_{\text{estacionario (persiste)}},
> \qquad x_p=A(\omega)\cos(\omega t-\delta),$$
> donde la **amplitud estacionaria** y el **desfase** son
> $$A(\omega)=\frac{F_0}{\sqrt{(k-m\omega^2)^2+(c\omega)^2}},\qquad
> \tan\delta=\frac{c\omega}{k-m\omega^2}.$$
> La **resonancia** es el pico de $A(\omega)$ que aparece cuando la frecuencia de la fuerza $\omega$ se
> acerca a la frecuencia natural $\omega_0=\sqrt{k/m}$.

> [!info]
> Es el caso $F\neq0$ del bloque [[Oscilaciones/index| oscilaciones]]: el transitorio $x_h$ es el
> [[Oscilador Libre y Amortiguado| oscilador libre]] (decae), y la particular $x_p$ se obtiene
> con los métodos de la [[No Homogenea/index| parte no homogénea]]. La maquinaria de raíces de fondo es la
> de [[Coeficientes Constantes Homogenea| la ecuación característica]].

---

## Ejemplo

> [!ejemplo] Curva de resonancia: amplitud frente a la frecuencia
> ![[curva_resonancia.svg|470]]
>
> Amplitud estacionaria $A(\omega)$ para varios amortiguamientos: el pico cerca de $\omega_0$ es la
> resonancia; crece y se afila al disminuir $\zeta$.

> [!ejemplo] Amplitud y desfase en un caso concreto
> **Sistema $\ddot x+2\dot x+5x=10\cos\omega t$** (es decir $m=1,\ c=2,\ k=5,\ F_0=10$), con
> $\omega_0=\sqrt5\approx2.24$. La amplitud estacionaria es
> $$A(\omega)=\frac{10}{\sqrt{(5-\omega^2)^2+(2\omega)^2}}.$$
> A baja frecuencia ($\omega\to0$): $A\to 10/5=2$ (respuesta cuasi-estática, $x_p\approx F_0/k$). En
> $\omega=2$ (cerca de $\omega_0$): $A=\dfrac{10}{\sqrt{(5-4)^2+16}}=\dfrac{10}{\sqrt{17}}\approx2.43$, ya
> por encima del valor estático: estamos cerca de la resonancia. A alta frecuencia ($\omega\to\infty$):
> $A\to0$, la masa "no alcanza" a seguir a la fuerza. El desfase pasa de $0$ (baja $\omega$) a $\pi/2$ en
> $\omega=\omega_0$ y tiende a $\pi$ (alta $\omega$): cerca de la resonancia la respuesta va **en cuadratura**
> con la fuerza.

---

## En qué consiste

> [!teorema] Amplitud y fase del estado estacionario
> Para $m\ddot x+c\dot x+kx=F_0\cos\omega t$, la solución particular es $x_p=A(\omega)\cos(\omega t-\delta)$ con
> $$A(\omega)=\frac{F_0}{\sqrt{(k-m\omega^2)^2+(c\omega)^2}},\qquad
> \tan\delta=\frac{c\omega}{k-m\omega^2}.$$

> [!demostracion]
> **Paso 1 — pasar a exponencial compleja (fasores).** Escribimos la fuerza como
> $F_0\cos\omega t=\operatorname{Re}\big(F_0 e^{i\omega t}\big)$ y buscamos $x_p=\operatorname{Re}\big(X
> e^{i\omega t}\big)$ con $X\in\mathbb{C}$ la **amplitud compleja** (fasor) que codifica amplitud y fase.
>
> **Paso 2 — sustituir.** Como $\dot x_p\to i\omega X e^{i\omega t}$ y $\ddot x_p\to -\omega^2 X e^{i\omega t}$,
> la EDO sobre el fasor queda
> $$\big(-m\omega^2+ic\omega+k\big)X\,e^{i\omega t}=F_0\,e^{i\omega t}.$$
>
> **Paso 3 — despejar el fasor.** Cancelando $e^{i\omega t}$,
> $$X=\frac{F_0}{k-m\omega^2+ic\omega}.$$
>
> **Paso 4 — amplitud y fase.** El módulo da la amplitud y el argumento (cambiado de signo) el desfase:
> $$A=|X|=\frac{F_0}{\sqrt{(k-m\omega^2)^2+(c\omega)^2}},\qquad
> \tan\delta=\frac{c\omega}{k-m\omega^2}.$$
> Tomando la parte real, $x_p=A\cos(\omega t-\delta)$. $\blacksquare$

> [!proposicion] Caso sin amortiguamiento ($c=0$)
> Sin disipación la EDO es $m\ddot x+kx=F_0\cos\omega t$ y aparecen dos subcasos:
> - **Fuera de sintonía ($\omega\neq\omega_0$):** la amplitud es **acotada**,
>   $$A=\frac{F_0}{m(\omega_0^2-\omega^2)},$$
>   que sin embargo se dispara cuando $\omega\to\omega_0$.
> - **En sintonía exacta ($\omega=\omega_0$):** ahora $\cos\omega_0 t$ es **solución de la homogénea**, así
>   que por la **regla de modificación** de los
>   [[Coeficientes Indeterminados| coeficientes indeterminados]] hay que multiplicar por $t$.
>   El resultado es la **resonancia pura**
>   $$x_p=\frac{F_0}{2m\omega_0}\,t\,\operatorname{sen}\omega_0 t,$$
>   una oscilación cuya amplitud **crece linealmente** con el tiempo y no tiene cota.

> [!info] Batidos cerca de la resonancia
> Cuando $c=0$ y $\omega$ está **muy cerca** (pero no igual) de $\omega_0$, la suma de dos cosenos de
> frecuencias casi iguales produce **batidos**: una oscilación rápida a frecuencia $\approx\omega_0$ dentro de
> una envolvente lenta que late a la frecuencia $|\omega-\omega_0|/2$. Es el preludio de la resonancia pura:
> a medida que $\omega\to\omega_0$, el periodo del batido se hace infinito y la envolvente se "estira" hasta
> convertirse en el crecimiento lineal $t\operatorname{sen}\omega_0 t$.

> [!ejemplo] Resonancia pura sin amortiguamiento
> ![[resonancia_tiempo.svg|460]]
>
> Con $\omega=\omega_0$ y $c=0$, la solución $x\propto t\operatorname{sen}\omega_0 t$ oscila con amplitud que
> crece sin cota.

> [!warning] La resonancia puede ser destructiva
> Si $\zeta$ es pequeño, el pico de $A(\omega)$ es enorme: una fuerza modesta a la frecuencia adecuada produce
> oscilaciones gigantescas. Esto ha roto puentes (marcha de tropas, viento sobre el Tacoma Narrows), ha hecho
> fallar álabes de turbinas y alas de avión por *flutter*, y obliga a "desafinar" las frecuencias naturales de
> las estructuras respecto de las excitaciones esperadas. El **amortiguamiento** es justamente lo que limita
> la altura del pico: a mayor $\zeta$, menor y más ancha la resonancia.

> [!info] Aplicación: el circuito RLC sintonizado
> El mismo análisis describe un circuito RLC en serie $L\ddot q+R\dot q+q/C=V_0\cos\omega t$, con
> $\omega_0=\dfrac{1}{\sqrt{LC}}$. En resonancia la corriente es máxima: así **sintoniza** una radio, que
> selecciona la emisora cuya frecuencia coincide con $\omega_0$ del circuito y rechaza las demás. Aquí la
> resonancia, lejos de ser un peligro, es la función deseada.

## Resumen

> [!resumen]
> | Magnitud | Expresión | Lectura física |
> |:--|:--|:--|
> | Amplitud estacionaria | $A(\omega)=\dfrac{F_0}{\sqrt{(k-m\omega^2)^2+(c\omega)^2}}$ | pico cerca de $\omega_0$ |
> | Desfase | $\tan\delta=\dfrac{c\omega}{k-m\omega^2}$ | $0\to\pi$ al cruzar $\omega_0$ |
> | Transitorio | $x_h$ (homogénea) | decae como $e^{-\zeta\omega_0 t}$ |
> | Estacionario | $x_p=A\cos(\omega t-\delta)$ | persiste a la frecuencia de la fuerza |
> | Resonancia ($c=0$, $\omega=\omega_0$) | $x_p=\dfrac{F_0}{2m\omega_0}t\operatorname{sen}\omega_0 t$ | amplitud $\to\infty$ |

> [!corolario]
> La respuesta de un oscilador forzado depende **drásticamente** de cuán cerca esté la frecuencia de
> excitación de su frecuencia natural. En $\omega\approx\omega_0$ la amplitud se maximiza: la resonancia. El
> amortiguamiento $\zeta$ decide si ese pico es un fenómeno útil (sintonía) o catastrófico (estructuras), pero
> nunca lo elimina del todo.

> [!referencia]
> - El transitorio es el oscilador libre: [[Oscilador Libre y Amortiguado]].
> - La regla de modificación de la particular: [[Coeficientes Indeterminados]].
> - La maquinaria de raíces: [[Coeficientes Constantes Homogenea]].
> - El panorama físico completo: [[Oscilaciones/index]].
