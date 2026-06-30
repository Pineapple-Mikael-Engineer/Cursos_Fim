---
title: Ley de Faraday
order: 1
tags:
  - electromagnetismo
  - teoria
  - electrodinamica
draft: false
aliases:
  - Ley de Faraday
  - Inducción electromagnética
  - Ley de Lenz
---

# Ley de Faraday $\nabla\times\vec E=-\dfrac{\partial\vec B}{\partial t}$

---

> [!definicion] Ley de Faraday
> Un campo magnético variable en el tiempo genera un campo eléctrico que circula. La **fuerza electromotriz (fem) inducida** $\varepsilon$ en un circuito cerrado es igual a menos la tasa de cambio del **flujo magnético** $\Phi_B$ que lo atraviesa.
>
> **Forma integral:**
> $$
> \varepsilon=\oint_{\partial S}\vec E\cdot d\vec l=-\frac{d\Phi_B}{dt},\qquad \Phi_B=\int_S\vec B\cdot d\vec A.
> $$
>
> **Forma diferencial (local):**
> $$
> \boxed{\;\nabla\times\vec E=-\frac{\partial\vec B}{\partial t}\;}
> $$
>
> El signo menos es la **ley de Lenz**: la corriente inducida circula de modo que su propio campo se opone al cambio de flujo que la origina.

---

> [!info] Ubicación y conexiones
> - **Sección:** [[4 Electrodinamica/index | Electrodinámica]].
> - **Notas hermanas:** [[Corriente de Desplazamiento]], [[Ecuaciones de Maxwell]].
> - **Herramienta:** el teorema de Stokes de [[Teoremas Integrales]] conecta la forma integral con la diferencial.
> - **Referencia base:** Griffiths, *Introduction to Electrodynamics*, capítulo 7 (Electrodinámica).
>
> Esta es la tercera ecuación de Maxwell. Junto con la [[Corriente de Desplazamiento]] (que corrige la ley de Ampère) completa el acople dinámico entre $\vec E$ y $\vec B$ que da lugar a las ondas electromagnéticas.

---

## Demostración — De la forma integral a la diferencial

Partimos de la **regla del flujo** para un circuito **fijo** en el espacio (la superficie $S$ y su borde $\partial S$ no cambian con el tiempo):
$$
\oint_{\partial S}\vec E\cdot d\vec l=-\frac{d}{dt}\int_S\vec B\cdot d\vec A.
$$

> [!demostracion] Obtención de $\nabla\times\vec E=-\partial_t\vec B$
> **Paso 1 — La derivada temporal entra en la integral.** Como la superficie $S$ es fija en el tiempo, los límites de integración no dependen de $t$. Entonces la derivada total respecto del tiempo conmuta con la integral de superficie y se vuelve una derivada parcial sobre el integrando:
> $$
> \frac{d}{dt}\int_S\vec B\cdot d\vec A=\int_S\frac{\partial\vec B}{\partial t}\cdot d\vec A.
> $$
> Esto **solo** es lícito porque el circuito no se mueve ni se deforma; toda la variación del flujo proviene de que $\vec B$ cambia en el tiempo.
>
> **Paso 2 — Teorema de Stokes en el lado izquierdo.** Por el teorema de Stokes ([[Teoremas Integrales]]), la circulación de $\vec E$ a lo largo del borde $\partial S$ es el flujo de su rotacional:
> $$
> \oint_{\partial S}\vec E\cdot d\vec l=\int_S(\nabla\times\vec E)\cdot d\vec A.
> $$
>
> **Paso 3 — Igualar los integrandos.** Sustituyendo los Pasos 1 y 2 en la regla del flujo:
> $$
> \int_S(\nabla\times\vec E)\cdot d\vec A=-\int_S\frac{\partial\vec B}{\partial t}\cdot d\vec A
> \;\Longrightarrow\;
> \int_S\left(\nabla\times\vec E+\frac{\partial\vec B}{\partial t}\right)\cdot d\vec A=0.
> $$
>
> **Paso 4 — Validez para toda superficie.** La igualdad anterior vale para **cualquier** superficie $S$ y cualquier borde $\partial S$. Si la integral de un campo vectorial sobre toda superficie es nula, el integrando debe anularse punto a punto:
> $$
> \nabla\times\vec E+\frac{\partial\vec B}{\partial t}=0
> \;\Longrightarrow\;
> \nabla\times\vec E=-\frac{\partial\vec B}{\partial t}.
> $$
> $\blacksquare$

---

## Demostración — fem de movimiento $\varepsilon=BLv$ y la regla del flujo

Una barra conductora de longitud $L$ se desliza con velocidad $\vec v$ perpendicular a un campo uniforme $\vec B$ constante en el tiempo. Aquí el flujo **no** cambia porque $\vec B$ varíe, sino porque el **circuito se mueve**. Veremos que el origen físico es la fuerza magnética sobre los portadores, y que aun así coincide con $-d\Phi_B/dt$.

> [!demostracion] fem de movimiento desde la fuerza de Lorentz
> **Paso 1 — Fuerza sobre los portadores.** Cada carga $q$ dentro de la barra viaja con la barra a velocidad $\vec v$. La parte magnética de la fuerza de Lorentz es
> $$
> \vec F_{\text{mag}}=q\,\vec v\times\vec B.
> $$
> Con $\vec v\perp\vec B$, su módulo es $F_{\text{mag}}=qvB$, dirigido a lo largo de la barra. Esta fuerza por unidad de carga actúa como un campo efectivo $\vec f=\vec v\times\vec B$ que empuja las cargas.
>
> **Paso 2 — fem como trabajo por unidad de carga.** La fem es la integral de la fuerza por unidad de carga a lo largo de la barra (longitud $L$, donde $\vec f$ es paralelo al recorrido):
> $$
> \varepsilon=\int_{\text{barra}}(\vec v\times\vec B)\cdot d\vec l=\int_0^L vB\,dl=BLv.
> $$
>
> **Paso 3 — Conexión con la regla del flujo.** Sea la barra deslizando sobre dos rieles separados $L$, con el circuito cerrado por la izquierda. Si en un tiempo $dt$ la barra avanza $dx=v\,dt$, el área encerrada crece $dA=L\,dx=Lv\,dt$, y el flujo aumenta
> $$
> d\Phi_B=B\,dA=BLv\,dt
> \;\Longrightarrow\;
> \left|\frac{d\Phi_B}{dt}\right|=BLv.
> $$
> Por tanto $\varepsilon=\left|-\dfrac{d\Phi_B}{dt}\right|=BLv$, idéntico al resultado por fuerza de Lorentz. $\blacksquare$

> [!corolario] Regla universal del flujo
> La regla $\varepsilon=-\dfrac{d\Phi_B}{dt}$ unifica **dos mecanismos físicamente distintos**:
> - **Circuito fijo, $\vec B$ variable:** la fem proviene del campo eléctrico inducido $\nabla\times\vec E=-\partial_t\vec B$ (ley de Faraday propiamente dicha).
> - **Circuito en movimiento, $\vec B$ constante:** la fem proviene de la fuerza magnética $q\vec v\times\vec B$ sobre los portadores (fem de movimiento).
>
> Ambos casos dan el mismo $-d\Phi_B/dt$. Es uno de los hechos que motivó a Einstein a formular la relatividad especial.

---

## En qué consiste — Ley de Lenz y energía

El signo menos no es un capricho: garantiza la **conservación de la energía**.

![[faraday.svg|400]]
*Espira atravesada por un flujo $\vec B$ creciente (entrante). La corriente inducida $I$ circula en el sentido que genera un campo $\vec B_{\text{ind}}$ saliente dentro de la espira, oponiéndose al aumento de flujo (ley de Lenz).*

Imagina que acercas un imán a una espira, aumentando el flujo $\Phi_B$. Si la corriente inducida **reforzara** el flujo en lugar de oponerse, el campo inducido atraería aún más al imán, que se aceleraría solo, produciendo más corriente, en un ciclo que crearía energía de la nada. La ley de Lenz invierte esa lógica:

- La corriente inducida crea un campo que **se opone** al cambio de flujo.
- Esto genera una fuerza que **frena** el movimiento del imán.
- Para mantener el cambio de flujo hay que hacer **trabajo mecánico** contra esa fuerza.
- Ese trabajo es exactamente la energía eléctrica disipada en la espira. La cuenta cierra.

> [!warning] El campo $\vec E$ inducido NO es conservativo
> En electrostática $\nabla\times\vec E=0$, de modo que $\vec E=-\nabla V$ deriva de un potencial escalar y $\oint\vec E\cdot d\vec l=0$ siempre.
>
> Cuando $\partial_t\vec B\neq0$ esto **deja de valer**:
> $$
> \nabla\times\vec E=-\frac{\partial\vec B}{\partial t}\neq0
> \;\Longrightarrow\;
> \oint\vec E\cdot d\vec l=\varepsilon\neq0.
> $$
> El campo eléctrico inducido tiene **circulación no nula**: sus líneas de campo se cierran sobre sí mismas formando bucles, y **no** puede escribirse como $-\nabla V$ de un potencial escalar solo. Esta es la diferencia esencial entre el campo electrostático (irrotacional) y el campo inducido (rotacional).

---

## Ejemplo — Espira en un campo variable

> [!ejemplo] Espira cuadrada con $B(t)$
> Una espira cuadrada de lado $a=0{,}20\ \text{m}$ y resistencia $R=2{,}0\ \Omega$ está en un plano perpendicular a un campo magnético uniforme que crece linealmente según
> $$
> B(t)=B_0+k\,t,\qquad B_0=0{,}50\ \text{T},\quad k=0{,}30\ \text{T/s}.
> $$
> Calcula: (a) la fem inducida $\varepsilon$, (b) la corriente inducida $I$ y su sentido por la ley de Lenz.

> [!solucion] Resolución
> **Paso 1 — Flujo magnético.** Como $\vec B\perp$ al plano de la espira y es uniforme, con área $A=a^2$:
> $$
> \Phi_B(t)=B(t)\,a^2=(B_0+k\,t)\,a^2.
> $$
> Numéricamente $A=(0{,}20)^2=0{,}040\ \text{m}^2$.
>
> **Paso 2 — fem inducida.** Derivamos respecto del tiempo (solo depende de $t$ el término $k\,t$):
> $$
> \varepsilon=-\frac{d\Phi_B}{dt}=-a^2\frac{dB}{dt}=-a^2\,k.
> $$
> En módulo:
> $$
> |\varepsilon|=a^2\,k=(0{,}040)(0{,}30)=0{,}012\ \text{V}=12\ \text{mV}.
> $$
>
> **Paso 3 — Corriente inducida.** Por la ley de Ohm en el circuito:
> $$
> I=\frac{|\varepsilon|}{R}=\frac{0{,}012}{2{,}0}=6{,}0\times10^{-3}\ \text{A}=6{,}0\ \text{mA}.
> $$
>
> **Paso 4 — Sentido por Lenz.** El flujo entrante **aumenta** ($dB/dt=k>0$). La corriente inducida debe oponerse, creando un campo $\vec B_{\text{ind}}$ **saliente** dentro de la espira. Por la regla de la mano derecha, $I$ circula en sentido **antihorario** visto desde el lado hacia el que sale $\vec B_{\text{ind}}$ (es decir, mirando contra $\vec B$).
>
> **Resultado:** $|\varepsilon|=12\ \text{mV}$, $I=6{,}0\ \text{mA}$, sentido antihorario. $\blacksquare$

---

## Resumen

> [!resumen] Ley de Faraday de un vistazo
>
> | Concepto | Expresión | Significado |
> |---|---|---|
> | Flujo magnético | $\Phi_B=\int_S\vec B\cdot d\vec A$ | Cantidad de campo que atraviesa $S$ |
> | Forma integral | $\varepsilon=\oint\vec E\cdot d\vec l=-\,d\Phi_B/dt$ | fem $=$ menos tasa de cambio del flujo |
> | Forma diferencial | $\nabla\times\vec E=-\partial_t\vec B$ | Ley local (tercera de Maxwell) |
> | fem de movimiento | $\varepsilon=BLv$ | Barra de largo $L$ a velocidad $v$ en $\vec B$ |
> | Ley de Lenz | signo $-$ | $I_{\text{ind}}$ se opone al cambio de flujo |
> | Campo inducido | $\oint\vec E\cdot d\vec l\neq0$ | $\vec E$ **no** conservativo si $\partial_t\vec B\neq0$ |
>
> Donde $\varepsilon$ es la fem [V], $\Phi_B$ el flujo [Wb], $L$ longitud [m] y $v$ rapidez [m/s].

> [!corolario] Ideas clave
> - La **regla del flujo** $\varepsilon=-d\Phi_B/dt$ vale tanto si cambia $\vec B$ como si se mueve el circuito.
> - El **signo menos** (Lenz) impone la conservación de la energía: la inducción siempre frena el cambio.
> - El campo eléctrico inducido es **rotacional**: tiene líneas cerradas y no deriva de un potencial escalar.
> - Acoplada con la [[Corriente de Desplazamiento]], cierra el sistema de [[Ecuaciones de Maxwell]] y permite las ondas electromagnéticas.

> [!referencia] Fuentes
> - Griffiths, D. J., *Introduction to Electrodynamics*, 4.ª ed., capítulo 7 (§7.1 y §7.2).
> - Jackson, J. D., *Classical Electrodynamics*, capítulo 5–6.
> - Landau & Lifshitz, *Teoría Clásica de Campos*, vol. 2.
