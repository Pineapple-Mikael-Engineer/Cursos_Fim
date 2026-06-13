---
title: Controlador PD
tags:
  - control-clasico
  - controladores
  - pid
draft: false
aliases:
  - PD
  - control PD
  - proporcional derivativo
---

# Controlador PD

> [!definicion]
> El control **proporcional-derivativo** suma a la acción proporcional un término proporcional a la derivada del error. En forma estándar (ISA) y en forma paralela:
> $$G_c(s)=K_p\left(1+T_d s\right)=K_p+K_d s=K_d\big(s+z\big),\qquad z=\frac{K_p}{K_d}=\frac{1}{T_d}.$$
> Añade **un cero** en $s=-1/T_d$ y ningún polo (forma ideal). Ese cero aporta **adelanto de fase**, que reubica los polos dominantes a la izquierda: más amortiguamiento $\zeta$ y más rapidez, sin tocar el error estacionario.

> [!info]
> Es una de las [[index | configuraciones del PID]], hermana de [[PI | PI]] y [[PID | PID]]. Combina las [[Acciones/index | acciones]] [[Proporcional P | P]] y [[Derivativo D | D]]. Es la versión ideal del compensador **lead** del [[Lugar Raices/index | lugar de raíces]].

---

## Ejemplo

> [!ejemplo]
> **Diseñar un PD para acelerar y amortiguar una planta de 2.º orden.** Sea la planta con realimentación unitaria
> $$G(s)=\frac{1}{s(s+2)}.$$
> Con solo ganancia $K_p$ los polos dominantes quedan poco amortiguados. Se pide $\zeta=0.5$ y $\omega_n=4\ \text{rad/s}$ (frente a lo que da $K_p$ solo). Diseñar $G_c(s)=K_p(1+T_d s)$.
>
> **Paso 1 — Polos deseados.** De $\zeta=0.5$, $\omega_n=4$:
> $$s_{1,2}=-\zeta\omega_n\pm j\,\omega_n\sqrt{1-\zeta^2}=-2\pm j\,4(0.866)=-2\pm j\,3.46.$$
>
> **Paso 2 — ¿Por qué P solo no basta?** Con $G_c=K_p$ el lazo es $\dfrac{K_p}{s^2+2s+K_p}$, de donde $2\zeta\omega_n=2\Rightarrow\omega_n\zeta=1$. Para $\omega_n=4$ haría falta $\zeta=0.25$: muy oscilatorio. P **no puede** fijar $\zeta$ y $\omega_n$ a la vez porque solo tiene un grado de libertad. El PD añade el cero que falta.
>
> **Paso 3 — Condición de ángulo (dónde poner el cero).** El punto $s_1=-2+j3.46$ debe estar en el lugar de raíces. Ángulos de los polos de la planta hacia $s_1$:
> $$\theta_{s=0}=180^\circ-\arctan\tfrac{3.46}{2}=180^\circ-60^\circ=120^\circ,\qquad \theta_{s=-2}=90^\circ.$$
> La condición de ángulo exige $\sum\angle\text{ceros}-\sum\angle\text{polos}=-180^\circ$, es decir el cero debe aportar
> $$\phi_z=180^\circ+\theta_{s=0}+\theta_{s=-2}-360^\circ\cdot k\;\Rightarrow\;\phi_z=120^\circ+90^\circ-180^\circ=30^\circ.$$
>
> **Paso 4 — Ubicar el cero.** El cero está en $-z$ sobre el eje real; el ángulo que forma con $s_1$ es $\phi_z=30^\circ$:
> $$\tan 30^\circ=\frac{3.46}{z-2}\;\Rightarrow\;z-2=\frac{3.46}{0.577}=6\;\Rightarrow\;z=8.$$
> Entonces $T_d=1/z=0.125\ \text{s}$. El controlador es $G_c(s)=K_p(1+0.125\,s)=K_p\dfrac{s+8}{8}$.
>
> **Paso 5 — Ganancia por condición de módulo.** $|G_c(s_1)G(s_1)|=1$:
> $$|s_1|=|{-2+j3.46}|=4,\quad |s_1+2|=3.46,\quad |s_1+8|=|6+j3.46|=6.93.$$
> $$\frac{K_p}{8}\cdot\frac{6.93}{4\cdot 3.46}=1\;\Rightarrow\;K_p=\frac{8\cdot 4\cdot 3.46}{6.93}=16.0,\qquad K_d=K_p T_d=16\cdot0.125=2.0.$$
>
> **Paso 6 — Verificación del efecto.** Lazo abierto $G_cG=\dfrac{2(s+8)}{s(s+2)}$. El cero en $-8$ "atrae" el lugar de raíces hacia la izquierda: los polos dominantes pasan a $-2\pm j3.46$ ($\zeta=0.5$, $\omega_n=4$). Frente a P solo: el **sobrepico baja** de $\sim44\%$ ($\zeta=0.25$) a $\sim16\%$ ($\zeta=0.5$) y el **tiempo de establecimiento** $t_s\approx 4/(\zeta\omega_n)=4/2=2\ \text{s}$ mejora. El **error estacionario** ante rampa no cambia (sigue fijado por el integrador de la planta): el PD no toca el tipo del sistema.

> [!ejemplo] Respuesta PD vs P
> ![[pd_vs_p_escalon.svg|550]]
>
> El PD amortigua las oscilaciones de P: menor sobrepico y establecimiento más rápido. El cero añade adelanto de fase que estabiliza el lazo.

---

## En qué consiste

> [!teoria]
> El PD reacciona a la **tendencia** del error, no solo a su valor. El término $K_d\dot e$ se adelanta a la señal: si el error está cayendo rápido, frena la acción antes de sobrepasar. En el dominio de la frecuencia, el cero $z=1/T_d$ introduce **adelanto de fase** $+90^\circ$ asintótico, que sube el [[Margenes MF MG | margen de fase]] y por tanto el amortiguamiento del lazo cerrado.
>
> El único parámetro libre además de $K_p$ es la posición del cero $z=K_p/K_d=1/T_d$. Colocarlo cerca de los polos dominantes maximiza la "atracción" del lugar de raíces hacia el semiplano izquierdo.

> [!teorema] PD como adelanto (lead)
> El PD es el caso límite del **compensador lead** $\dfrac{s+z}{s+p}$ con el polo en el infinito ($p\to\infty$):
> $$G_c(s)=K_d\,(s+z),\qquad z=\frac{K_p}{K_d}=\frac{1}{T_d}.$$
> El cero aporta adelanto de fase, que reubica los polos dominantes a la izquierda en el [[Lugar Raices/index | lugar de raíces]], aumentando $\zeta$ y $\omega_n$ simultáneamente.

> [!regla] Ubicación del cero
> Colocar el cero $z=K_p/K_d=1/T_d$ cerca de los **polos dominantes** para atraer el lugar de raíces hacia el semiplano izquierdo. Cuanto más a la izquierda el cero, más adelanto disponible, pero más se amplifica el ruido.

---

## Limitaciones

> [!warning] El PD ideal es impropio
> $G_c(s)=K_d s+K_p$ tiene más ceros que polos: **no es realizable** físicamente y su ganancia $|G_c|\to\infty$ con $\omega$, lo que **amplifica el ruido** de alta frecuencia. El PD real lleva un **polo de filtro**:
> $$G_c(s)=K_p+\frac{K_d s}{1+s/N},\qquad N\approx 8\text{–}20,$$
> que es exactamente un **compensador lead** $\dfrac{s+z}{s+p}$ con $p=N\,z\gg z$. Ver [[Derivativo D | derivativo filtrado]].

> [!warning]
> El PD **no corrige offset**: si hay error estacionario, usar [[PI | PI]] o [[PID | PID]]. Además es sensible al ruido, por lo que el filtro del derivativo es imprescindible.

---

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | FT (ISA) | $G_c(s)=K_p(1+T_d s)$ |
> | FT (paralela) | $K_p+K_d s=K_d(s+z)$ |
> | Aporta | un cero en $s=-1/T_d$, sin polo |
> | Equivale a | compensador **lead** |
> | Sobrepico $M_p$ | **baja** |
> | Tiempo de establecimiento | baja |
> | Estabilidad / margen de fase | **mejora** |
> | Error estacionario | sin cambio |
> | Ruido | amplifica (requiere filtro) |

> [!corolario]
> El PD añade un cero $z=1/T_d$ que inyecta adelanto de fase: reubica los polos dominantes a la izquierda y arriba en el plano $s$, subiendo $\zeta$ y $\omega_n$ a la vez —algo que P solo no puede—. A cambio no toca el tipo del sistema (no mejora $e_{ss}$) y amplifica el ruido, por lo que en la práctica se implementa como lead filtrado. Para corregir error estacionario hay que añadir acción integral ([[PI | PI]], [[PID | PID]]).

> [!referencia]
> - Acciones que combina: [[Proporcional P]] · [[Derivativo D]].
> - Para eliminar error estacionario: [[PI]] · [[PID]].
> - Compensador lead equivalente: [[Lugar Raices/index]] · [[Margenes MF MG]].
> - Marco general: [[index]].
> - Sintonización: [[Sintonizacion/index]].
