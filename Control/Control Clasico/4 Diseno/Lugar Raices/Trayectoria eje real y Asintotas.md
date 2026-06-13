---
title: Trayectoria en el Eje Real y Asíntotas
tags:
  - control-clasico
  - diseño
  - lugar-raices
draft: false
aliases:
  - eje real
  - asintotas
  - regla eje real
  - regla asintotas
---

# Trayectoria en el Eje Real y Asíntotas

> [!definicion]
> Dos reglas del [[Reglas Construccion | trazado del LGR]]. **Eje real:** un punto real $\sigma$ pertenece al LGR si el número de polos+ceros reales a su derecha (con multiplicidad) es **impar**. **Asíntotas:** las $n-m$ ramas que no terminan en ceros finitos escapan al infinito siguiendo rectas de centro y ángulos
> $$\sigma_a=\frac{\sum p_j-\sum z_i}{n-m},\qquad \theta_a=\frac{180^\circ(2k+1)}{n-m},\quad k=0,1,\dots,n-m-1.$$
> con $n$ polos y $m$ ceros (contando multiplicidades).

> [!info]
> Reglas 3 y 4 de [[Reglas Construccion | construcción del LGR]], dentro de la sección [[index | lugar de las raíces]]. Ambas salen de la [[Condicion Angulo Magnitud | condición de ángulo]]. Donde dos ramas del eje real se separan aparece un [[Puntos Ruptura | punto de ruptura]]; no confundir las asíntotas (comportamiento lejano, $K\to\infty$) con los [[Angulos Salida Llegada | ángulos de salida]] (local). Ver también [[Polos Ceros | polos y ceros]].

---

## Ejemplo

> [!ejemplo]
> **Eje real y asíntotas de $G(s)H(s)=\dfrac{K}{s(s+2)(s+4)}$.**
>
> ![[root_locus_completo.gif|600]]
>
> Polos $0,-2,-4$ ($n=3$), sin ceros ($m=0$), grado relativo $n-m=3$.
>
> **Paso 1 — Tramos del eje real** (paridad de polos/ceros a la derecha):
>
> | Tramo | a la derecha | paridad | ¿LGR? |
> |---|---|---|---|
> | $(0,\infty)$ | 0 | par | No |
> | $(-2,0)$ | 1 | impar | **Sí** |
> | $(-4,-2)$ | 2 | par | No |
> | $(-\infty,-4)$ | 3 | impar | **Sí** |
>
> **Paso 2 — Centro de las asíntotas:**
> $$\sigma_a=\frac{\sum p_j-\sum z_i}{n-m}=\frac{(0-2-4)-0}{3}=\frac{-6}{3}=-2.$$
>
> **Paso 3 — Ángulos** ($n-m=3$, $k=0,1,2$):
> $$\theta_a=\frac{180^\circ(2k+1)}{3}=60^\circ,\;180^\circ,\;300^\circ.$$
>
> **Paso 4 — Interpretación.** Dos ramas suben del tramo $(-2,0)$ y se alejan por las asíntotas de $\pm60^\circ$ ancladas en $\sigma_a=-2$; la tercera escapa por la asíntota de $180^\circ$ a lo largo del eje real negativo. Las tres asíntotas se cortan en $s=-2$ y reparten el plano en sectores de $120^\circ$.

> [!ejemplo]
> **Caso de dos polos: $G(s)H(s)=\dfrac{K}{s(s+2)}$.**
>
> Eje real: solo $(-2,0)$ es LGR (1 polo a la derecha, impar).
>
> ![[lgr_eje_real.svg|600]]
>
> Asíntotas: $n-m=2$, $\sigma_a=\dfrac{0+(-2)}{2}=-1$, $\theta_a=\dfrac{180^\circ(2k+1)}{2}=90^\circ,\;270^\circ$. Las dos ramas dejan el eje real en el [[Puntos Ruptura | punto de ruptura]] $s=-1$ y suben verticalmente sobre la recta $\sigma=-1$.
>
> ![[lgr_asintotas.svg|500]]

---

## En qué consiste

> [!info] Punto de ruptura en el eje real
> Cuando dos ramas del eje real se acercan y se separan hacia el plano complejo (o al revés), hay un [[Puntos Ruptura | punto de ruptura]].
>
> ![[lgr_punto_ruptura.svg|600]]

> [!info] Número de asíntotas según $n-m$
> Depende solo del **grado relativo** $n-m$, no del tipo del sistema:
> - $n-m=0$: sin asíntotas (todas las ramas mueren en ceros finitos).
> - $n-m=1$: una asíntota a $180^\circ$.
> - $n-m=2$: dos a $\pm90^\circ$ (recta vertical en $\sigma_a$).
> - $n-m=3$: tres a $60^\circ,180^\circ,300^\circ$.

---

## Demostración

> [!teorema] Regla del eje real
> Para $s=\sigma$ real, $\angle G(\sigma)H(\sigma)=180^\circ(2k+1)$ exige paridad impar a la derecha.

> [!demostracion] Paso 1 — Ángulos de los polos/ceros reales
> El vector $s+p_j$ apunta del polo a $\sigma$. Si el polo está a la **izquierda** de $\sigma$, el vector apunta a la derecha → ángulo $0^\circ$. Si está a la **derecha**, apunta a la izquierda → ángulo $180^\circ$.

> [!demostracion] Paso 2 — Los complejos se cancelan
> Polos y ceros complejos vienen en pares conjugados; sus ángulos a un punto del eje real son opuestos ($+\phi$ y $-\phi$) y suman $0^\circ$. No afectan la condición de ángulo en el eje real.

> [!demostracion] Paso 3 — Condición de ángulo
> Solo cuentan los que están a la derecha:
> $$\angle G(\sigma)H(\sigma)=180^\circ M_{\text{der}}-180^\circ N_{\text{der}}=180^\circ(M_{\text{der}}-N_{\text{der}}),$$
> con $N_{\text{der}}$ polos y $M_{\text{der}}$ ceros reales a la derecha. Esto es múltiplo impar de $180^\circ$ ssi $N_{\text{der}}+M_{\text{der}}$ es **impar** (misma paridad que la diferencia). $\blacksquare$

> [!teorema] Asíntotas
> Para $|s|$ grande, $G(s)H(s)\approx\dfrac{1}{s^{\,n-m}}\Big(1+\dfrac{B_1-A_1}{s}+\cdots\Big)$, con $A_1=\sum p_j$, $B_1=\sum z_i$.

> [!demostracion] Paso 1 — Expansión de $G(s)H(s)$
> $\prod(s+p_j)=s^n+(\sum p_j)s^{n-1}+\cdots$ y $\prod(s+z_i)=s^m+(\sum z_i)s^{m-1}+\cdots$, así que
> $$G(s)H(s)=\frac{s^m+B_1s^{m-1}+\cdots}{s^n+A_1s^{n-1}+\cdots}=\frac{1}{s^{n-m}}\cdot\frac{1+B_1/s+\cdots}{1+A_1/s+\cdots}.$$

> [!demostracion] Paso 2 — Ecuación característica para $|s|$ grande
> De $KG(s)H(s)=-1$, multiplicando por $s^{n-m}$:
> $$K\Big(1+\frac{B_1-A_1}{s}+\cdots\Big)=-s^{n-m}.$$

> [!demostracion] Paso 3 — Ángulos
> A primer orden $s^{n-m}\approx-K$. Tomando argumento:
> $$(n-m)\theta_a=180^\circ(2k+1)\Rightarrow\theta_a=\frac{180^\circ(2k+1)}{n-m}.$$

> [!demostracion] Paso 4 — Centro $\sigma_a$
> Escribiendo $s=\sigma_a+re^{j\theta_a}$ e igualando el término de orden $s^{n-m-1}$ del desarrollo de $(s-\sigma_a)^{n-m}$ con $A_1-B_1$ se obtiene
> $$\sigma_a=\frac{A_1-B_1}{\,n-m\,}=\frac{\sum p_j-\sum z_i}{n-m}.$$
> Es el "centro de gravedad" de polos menos ceros. $\blacksquare$

> [!demostracion] Paso 5 — Verificación
> $G(s)H(s)=\dfrac{K}{s(s+2)}$: $\sum p_j=-2$, $\sum z_i=0$, $n-m=2$ → $\sigma_a=\dfrac{-2-0}{2}=-1$. ✓
>
> ![[lgr_asintotas.svg|500]]

---

## Limitaciones

> [!warning] Distinguir asíntotas de ángulos de salida
> - **Asíntotas:** comportamiento **lejano** ($K\to\infty$, lejos del origen).
> - **Ángulos de salida:** comportamiento **local** cerca de un polo múltiple o complejo ([[Angulos Salida Llegada]]).
>
> Son cosas distintas. Para un polo múltiple en $p_0$ de multiplicidad $q$:
> $$\theta_k=\frac{(2k+1)180^\circ+\sum\angle(p_0-z_i)-\sum_{j\neq\text{múlt.}}\angle(p_0-p_j)}{q}.$$
> Ej.: $G(s)H(s)=\dfrac{K}{(s+1)^2(s+2)}$, polo doble en $-1$ ($q=2$), otro polo en $-2$ (ángulo $180^\circ$): $\theta_k=\dfrac{(2k+1)180^\circ-180^\circ}{2}=0^\circ,180^\circ$ (salen por el eje real).

> [!warning] Sistemas impropios ($n<m$)
> Si hay más ceros que polos, $G(s)H(s)$ no es realizable; aun así $m-n$ ramas nacen en infinito y las asíntotas usan $\theta_a=\dfrac{180^\circ(2k+1)}{m-n}$ (denominador positivo).

## Resumen

> [!resumen]
> | Regla | Fórmula | Notas |
> |---|---|---|
> | Eje real | nº impar de polos+ceros a la derecha | complejos se cancelan |
> | Centro asíntotas | $\sigma_a=\dfrac{\sum p_j-\sum z_i}{n-m}$ | real |
> | Ángulos asíntotas | $\theta_a=\dfrac{180^\circ(2k+1)}{n-m}$ | $k=0,\dots,n{-}m{-}1$ |
> | Nº asíntotas | $n-m$ | grado relativo |

> [!corolario]
> El eje real se sombrea por simple paridad y las $n-m$ ramas restantes escapan por asíntotas ancladas en $\sigma_a$ con ángulos $\theta_a$ equiespaciados. Estas dos reglas fijan el esqueleto del LGR; los [[Puntos Ruptura | puntos de ruptura]] y los [[Cruce Eje Imaginario | cruces con $j\omega$]] precisan el resto.

> [!referencia]
> - Contexto: [[Reglas Construccion]] y [[index]].
> - Origen: [[Condicion Angulo Magnitud]].
> - Donde el LGR deja el eje real: [[Puntos Ruptura]].
> - Comportamiento local en polos complejos: [[Angulos Salida Llegada]].
