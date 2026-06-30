---
title: Operador Derivada en Base Móvil
order: 2
tags:
  - dinamica
  - teoria
  - movimiento-relativo
draft: false
aliases:
  - operador derivada en base móvil
  - derivada en base móvil
  - fórmula de Poisson
  - aceleración de Coriolis
  - teorema del transporte
---

# Operador Derivada en Base Móvil $\;\left.\dfrac{d}{dt}\right|_F=\left.\dfrac{d}{dt}\right|_M+\vec\omega\times$

> [!definicion]
> Cuando el marco $M$ **rota** con velocidad angular $\vec\omega$ respecto al fijo $F$, la derivada temporal de **cualquier** vector $\vec A$ es distinta vista desde cada marco, y ambas se relacionan por el **operador derivada en base móvil**:
> $$\boxed{\;\left.\frac{d\vec A}{dt}\right|_F=\left.\frac{d\vec A}{dt}\right|_M+\vec\omega\times\vec A\;}$$
> Su raíz es la **fórmula de Poisson** $\dot{\hat e}'=\vec\omega\times\hat e'$: los versores de $M$, al girar, tienen derivada no nula. De este operador salen la velocidad de arrastre, la aceleración de **Coriolis**, la cinemática del cuerpo rígido y el término giroscópico de Euler.

> [!info]
> El resultado central del [[2 Movimiento Relativo/index | movimiento relativo]] ([[Dinamica/index | Dinámica]]). Generaliza las derivadas de las bases polar/esférica de la [[Cinematica/index | cinemática]]; lo aplica el [[4 Cuerpo Rigido/index| cuerpo rígido]] y, sobre el momento angular, produce las [[Ecuaciones de Euler 3D | ecuaciones de Euler]]. Referencia: PDF *Física I* (GETI), §2.2; Taylor §9.

---

## Ejemplo

> [!ejemplo]
> **El aspersor (velocidad y aceleración del agua).**
>
> El agua sube por el tubo recto de un aspersor a $v'=2\ \text{m/s}$ respecto al tubo, a $r'=4\ \text{cm}$ del eje, mientras el tubo gira a $\omega=16\pi\ \text{rad/s}$. Hallar la velocidad y la aceleración **absolutas** (origen común, $\vec V_M=\vec A_M=\vec 0$; tubo radial, $\vec a\,'=\vec0$).
>
> ![[marcos_referencia.svg|560]]
>
> *La partícula se mueve respecto a $M$ (el tubo) mientras $M$ gira con $\vec\omega$; las fórmulas de abajo dan su movimiento visto desde $F$.*
>
> **Velocidad** ($\vec v=\vec v\,'+\vec\omega\times\vec r\,'$), con $\vec v\,'=2\,\hat e_r$, $\vec\omega\times\vec r\,'=16\pi(0{,}04)\,\hat e_\theta=2{,}01\,\hat e_\theta$:
> $$v=\sqrt{2^2+2{,}01^2}\approx2{,}83\ \text{m/s}.$$
>
> **Aceleración** ($\vec a=\underbrace{\vec a\,'}_{0}+2\vec\omega\times\vec v\,'+\vec\omega\times(\vec\omega\times\vec r\,')$): Coriolis $2\vec\omega\times\vec v\,'=2(16\pi)(2)\,\hat e_\theta=201\,\hat e_\theta$; centrípeta $\vec\omega\times(\vec\omega\times\vec r\,')=-\omega^2 r'\,\hat e_r=-(16\pi)^2(0{,}04)\,\hat e_r=-101\,\hat e_r$.
> $$a=\sqrt{201^2+101^2}\approx225\ \text{m/s}^2.$$
>
> > [!solucion]
> > $v\approx2{,}83\ \text{m/s}$, $a\approx225\ \text{m/s}^2$. La **Coriolis** ($201\ \text{m/s}^2$, tangencial) domina sobre la **centrípeta** ($101\ \text{m/s}^2$, radial): el giro le imprime al agua mucha más aceleración que su propio avance por el tubo.

---

## En qué consiste

> [!teorema] Fórmula de Poisson
> Los versores $\hat e'$ de un marco que rota con $\vec\omega$ cumplen
> $$\frac{d\hat e'}{dt}=\vec\omega\times\hat e'.$$

> [!demostracion]
> Los versores son **ortonormales en todo instante**, así que $M$ gira **rígidamente**. En un intervalo $dt$, $M$ rota un ángulo $d\phi$ en torno a un eje $\hat n$; todo vector ligado a $M$ gira ese mismo $d\phi$, lo que para un versor significa $d\hat e'=d\phi\,\hat n\times\hat e'$ (un giro infinitesimal desplaza la punta perpendicularmente, en $\hat n\times\hat e'$, una cantidad $d\phi$). Dividiendo por $dt$ y definiendo $\vec\omega=\dot\phi\,\hat n$: $\dfrac{d\hat e'}{dt}=\vec\omega\times\hat e'$. (Coherente con que $\hat e'$ unitario obliga a $\dot{\hat e}'\perp\hat e'$.) $\blacksquare$

> [!teorema] El operador
> Para cualquier vector $\vec A$, $\ \left.\dfrac{d\vec A}{dt}\right|_F=\left.\dfrac{d\vec A}{dt}\right|_M+\vec\omega\times\vec A$.

> [!demostracion]
> **Paso 1 — Componentes en $M$:** $\vec A=A_x'\hat\imath'+A_y'\hat\jmath'+A_z'\hat k'$. **Paso 2 — Derivar en $F$** (regla del producto sobre componentes **y** versores):
> $$\left.\frac{d\vec A}{dt}\right|_F=\underbrace{\dot A_x'\hat\imath'+\dot A_y'\hat\jmath'+\dot A_z'\hat k'}_{\text{(a)}}+\underbrace{A_x'\dot{\hat\imath}'+A_y'\dot{\hat\jmath}'+A_z'\dot{\hat k}'}_{\text{(b)}}.$$
> **Paso 3 — Identificar.** El bloque (a) es lo que mide el observador de $M$ (solo varían las componentes): $(a)=\left.\dfrac{d\vec A}{dt}\right|_M$. En el bloque (b), por **Poisson** $\dot{\hat e}'=\vec\omega\times\hat e'$, así que $(b)=\vec\omega\times(A_x'\hat\imath'+A_y'\hat\jmath'+A_z'\hat k')=\vec\omega\times\vec A$. Sumando, $\left.\dfrac{d\vec A}{dt}\right|_F=\left.\dfrac{d\vec A}{dt}\right|_M+\vec\omega\times\vec A$. $\blacksquare$

> [!teorema] Composición de velocidades (arrastre)
> $$\vec v=\vec v\,'+\underbrace{\vec V_M+\vec\omega\times\vec r\,'}_{\text{velocidad de arrastre}}.$$

> [!demostracion]
> De $\vec r=\vec R_M+\vec r\,'$, derivando en $F$ y aplicando el operador a $\vec r\,'$:
> $$\vec v=\left.\frac{d\vec R_M}{dt}\right|_F+\left.\frac{d\vec r\,'}{dt}\right|_F=\vec V_M+\left(\left.\frac{d\vec r\,'}{dt}\right|_M+\vec\omega\times\vec r\,'\right)=\vec v\,'+\vec V_M+\vec\omega\times\vec r\,',$$
> con $\vec v\,'=\left.\frac{d\vec r\,'}{dt}\right|_M$ la velocidad **relativa**. $\blacksquare$

> [!teorema] Composición de aceleraciones (Coriolis)
> $$\boxed{\;\vec a=\vec a\,'+\vec A_M+2\,\vec\omega\times\vec v\,'+\vec\omega\times(\vec\omega\times\vec r\,')+\vec\alpha\times\vec r\,'\;}$$
> con $2\vec\omega\times\vec v\,'$ la **aceleración de Coriolis**, $\vec\omega\times(\vec\omega\times\vec r\,')$ la **centrípeta** y $\vec\alpha\times\vec r\,'$ la **acimutal** ($\vec\alpha=\dot{\vec\omega}$).

> [!demostracion]
> Derivar $\vec v=\vec v\,'+\vec V_M+\vec\omega\times\vec r\,'$ en $F$, término a término, usando el operador donde haga falta:
> - $\left.\dfrac{d\vec v\,'}{dt}\right|_F=\vec a\,'+\vec\omega\times\vec v\,'$ (operador sobre $\vec v\,'$).
> - $\left.\dfrac{d\vec V_M}{dt}\right|_F=\vec A_M$.
> - $\left.\dfrac{d(\vec\omega\times\vec r\,')}{dt}\right|_F=\dot{\vec\omega}\times\vec r\,'+\vec\omega\times\left.\dfrac{d\vec r\,'}{dt}\right|_F=\vec\alpha\times\vec r\,'+\vec\omega\times(\vec v\,'+\vec\omega\times\vec r\,')$. (Nota: $\dot{\vec\omega}|_F=\dot{\vec\omega}|_M+\vec\omega\times\vec\omega=\vec\alpha$, igual en ambos marcos.)
>
> Sumando y agrupando los dos $\vec\omega\times\vec v\,'$:
> $$\vec a=\vec a\,'+\vec A_M+2\,\vec\omega\times\vec v\,'+\vec\omega\times(\vec\omega\times\vec r\,')+\vec\alpha\times\vec r\,'.\qquad\blacksquare$$

> [!proposicion] Casos particulares
> - $\vec\omega=$ cte ($\vec\alpha=\vec0$): desaparece $\vec\alpha\times\vec r\,'$.
> - **Origen común** ($\vec V_M=\vec A_M=\vec0$) y $\vec\omega=$ cte: $\vec a=\vec a\,'+2\vec\omega\times\vec v\,'+\vec\omega\times(\vec\omega\times\vec r\,')$ — la forma usada en la **rotación de la Tierra**.

> [!proposicion] Newton en el marco rotante: pseudofuerzas
> Despejando $m\vec a\,'$ de $\sum\vec F=m\vec a$, en $M$ se cumple un Newton "con trampa":
> $$m\vec a\,'=\sum\vec F-m\vec A_M-2m\,\vec\omega\times\vec v\,'-m\,\vec\omega\times(\vec\omega\times\vec r\,')-m\,\vec\alpha\times\vec r\,'.$$
> Aparecen la **fuerza centrífuga** $-m\,\vec\omega\times(\vec\omega\times\vec r\,')$ (hacia afuera) y la de **Coriolis** $-2m\,\vec\omega\times\vec v\,'$: no son fuerzas reales, sino el precio de usar un marco no inercial.

> [!proposicion] El mismo operador da las ecuaciones de Euler
> Aplicado al **momento angular** de un sólido, $\left.\dfrac{d\vec H}{dt}\right|_F=\left.\dfrac{d\vec H}{dt}\right|_M+\vec\omega\times\vec H$; con $\vec H=\mathbf I\vec\omega$ en ejes del cuerpo aparece el término giroscópico $\vec\omega\times(\mathbf I\vec\omega)$. → [[Ecuaciones de Euler 3D]].

> [!warning]
> $\vec a\,'$ y $\vec v\,'$ son **relativas a $M$** (lo que mediría un observador solidario a $M$). El operador vale para **todo** vector, no solo la posición. $\vec\alpha=\dot{\vec\omega}$ es la misma en $F$ y en $M$ (porque $\vec\omega\times\vec\omega=\vec0$). No olvidar el **factor 2** en Coriolis.

## Resumen

> [!resumen]
> | Resultado | Expresión |
> |:---|:---|
> | Poisson | $\dot{\hat e}'=\vec\omega\times\hat e'$ |
> | Operador | $\left.\frac{d\vec A}{dt}\right\|_F=\left.\frac{d\vec A}{dt}\right\|_M+\vec\omega\times\vec A$ |
> | Velocidad | $\vec v=\vec v\,'+\vec V_M+\vec\omega\times\vec r\,'$ |
> | Aceleración | $\vec a=\vec a\,'+\vec A_M+2\vec\omega\times\vec v\,'+\vec\omega\times(\vec\omega\times\vec r\,')+\vec\alpha\times\vec r\,'$ |
> | Coriolis / centrífuga | $-2m\vec\omega\times\vec v\,'$ / $-m\vec\omega\times(\vec\omega\times\vec r\,')$ |

> [!corolario]
> Un solo hecho —los versores de una base que gira tienen derivada $\vec\omega\times\hat e'$— genera, al aplicarlo en cadena, toda la cinemática en marcos rotantes: arrastre, Coriolis, las pseudofuerzas y, sobre el momento angular, las ecuaciones de Euler. Es la herramienta más rentable del curso.

> [!referencia]
> PDF *Física I* (GETI), §2.2; Taylor §9. Origen plano: [[Cinematica/index | cinemática]]. Aplicación: [[4 Cuerpo Rigido/index| cuerpo rígido]] y [[Ecuaciones de Euler 3D]].
