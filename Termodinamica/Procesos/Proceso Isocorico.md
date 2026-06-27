---
title: Proceso Isocórico
order: 2
tags:
  - termodinamica
  - teoria
  - procesos
draft: false
aliases:
  - Proceso isocórico
  - Proceso isométrico
  - Proceso a volumen constante
---

# Proceso Isocórico $v=\text{cte},\quad q_v=\Delta u$

> [!definicion]
> Un **proceso isocórico** (o **isométrico**, o **a volumen constante**) es aquel en el que el sistema evoluciona entre dos estados de equilibrio sin que su volumen específico cambie:
> $$v=\text{cte}\quad\Longleftrightarrow\quad dv=0.$$
> El caso típico es el de una sustancia confinada en un **recipiente rígido y cerrado** (volumen fijo, frontera indeformable). Como la frontera del sistema no se desplaza, el proceso no admite **trabajo de frontera móvil**, y todo el calor intercambiado se invierte en cambiar la energía interna:
> $$q_v=\Delta u.$$

> [!info]
> **Ubicación.** Esta nota pertenece a la sección [[Procesos/index | Procesos Termodinámicos]]. Sus notas hermanas son [[Proceso Isobarico | el proceso isobárico]] ($P=$cte), [[Proceso Adiabatico | el proceso adiabático]] ($q=0$) y [[Proceso Politropico | el proceso politrópico]] ($Pv^n=$cte). El análisis se apoya en [[Primera Ley SC | la primera ley para sistemas cerrados]] y en el modelo de [[Gas Ideal | gas ideal]].

---

## 1. Definición geométrica y representación

La condición $v=\text{cte}$ fija una coordenada del estado. En el **plano $P$–$v$**, el lugar de todos los estados con el mismo volumen específico es una **recta vertical**: el estado puede subir o bajar en presión (y, con ella, en temperatura), pero nunca se desplaza horizontalmente. El recorrido del proceso es, pues, un segmento vertical entre $(v,P_1)$ y $(v,P_2)$.

Esta verticalidad es justamente la que anula el trabajo: el área bajo la curva en el plano $P$–$v$ —que mide el trabajo de frontera— es nula para un segmento de ancho cero.

![[isocorico_pv_ts.svg|520]]

*Figura. Izquierda: en el plano $P$–$v$ la isócora es una recta vertical; el área bajo ella es nula, de modo que $w=0$. Derecha: en el plano $T$–$s$ la isócora es una curva exponencial creciente, y el área bajo ella iguala el calor transferido $q=\Delta u$ (a trabajo de frontera nulo).*

---

## 2. Trabajo de frontera nulo y primera ley

> [!teorema]
> En todo proceso isocórico el **trabajo de frontera móvil** es nulo:
> $$w=\int_1^2 P\,dv=0,$$
> y, en ausencia de otros modos de trabajo, la primera ley se reduce a
> $$q_v=\Delta u.$$

> [!demostracion]
> **Paso 1 — Trabajo de frontera.** El trabajo de frontera móvil por unidad de masa entre los estados $1$ y $2$ es, por definición,
> $$w=\int_1^2 P\,dv.$$
> Como el proceso es isocórico, $v=\text{cte}$ y por tanto $dv=0$ en todo el recorrido. El integrando se multiplica por un diferencial idénticamente nulo, de modo que
> $$w=\int_1^2 P\cdot 0=0.$$
> Físicamente, la frontera del sistema (las paredes rígidas) no se desplaza, así que ningún elemento de superficie realiza trabajo de compresión o expansión.
>
> **Paso 2 — Primera ley.** [[Primera Ley SC | La primera ley para un sistema cerrado]] en forma diferencial es
> $$\delta q-\delta w=du,$$
> con $\delta q,\delta w$ diferenciales **inexactos** (dependen de la trayectoria) y $du$ **exacto**. Integrando entre $1$ y $2$,
> $$q-w=\Delta u.$$
>
> **Paso 3 — Sustitución.** Con $w=0$ (Paso 1), y si no existe ningún otro modo de transferir trabajo,
> $$q_v=\Delta u.$$
> El subíndice $v$ recuerda que la igualdad vale a volumen constante. $\blacksquare$

> [!warning]
> La afirmación "isocórico $\Rightarrow w=0$" se refiere **exclusivamente al trabajo de frontera móvil**. Aunque el volumen no cambie, el sistema puede recibir o entregar trabajo por **otros modos**: trabajo **eléctrico** (una resistencia interna), trabajo de **eje** (un agitador), etc. Estos modos no requieren que la frontera se mueva. En consecuencia, la igualdad $q_v=\Delta u$ **solo es válida si todos esos otros trabajos son nulos**; en caso contrario hay que retener el balance completo $\Delta u=q-w$ con $w$ incluyendo todos los modos. Este es el punto fino del ejemplo de la resistencia eléctrica de la sección 7.

---

## 3. Calor específico a volumen constante

Para un **gas ideal** la energía interna depende solo de la temperatura, $u=u(T)$, y su variación se expresa mediante el **calor específico a volumen constante** $c_v$:

$$q_v=\Delta u=c_v\,\Delta T=c_v(T_2-T_1).$$

> [!teoria]
> El resultado $q_v=\Delta u$ tiene una lectura **operacional**: define cómo medir $c_v$. Si se calienta una sustancia a volumen constante y se mide el calor $q_v$ necesario para elevar su temperatura $\Delta T$, entonces $c_v=q_v/\Delta T$. En el límite diferencial, como $q_v=\Delta u$ y a volumen constante $du=c_v\,dT$,
> $$\boxed{\,c_v=\left(\dfrac{\partial u}{\partial T}\right)_v\,}$$
> Esta es la **definición termodinámica** de $c_v$: la tasa de cambio de la energía interna con la temperatura, manteniendo el volumen fijo. El proceso isocórico es el escenario natural en el que esta derivada parcial se materializa como un experimento medible.

---

## 4. Relación entre estados (ley de Gay-Lussac)

> [!proposicion]
> Para un gas ideal que evoluciona a volumen constante, la presión es proporcional a la temperatura absoluta:
> $$\frac{P_1}{T_1}=\frac{P_2}{T_2}\qquad(v=\text{cte}).$$
> Esta es la **ley de Gay-Lussac**.

> [!demostracion]
> **Paso 1 — Ecuación de estado.** El [[Gas Ideal | gas ideal]] satisface
> $$Pv=RT.$$
>
> **Paso 2 — Despejar el invariante.** Reordenando,
> $$\frac{P}{T}=\frac{R}{v}.$$
> El miembro derecho contiene la constante del gas $R$ y el volumen específico $v$, que en este proceso es **constante**. Por tanto el cociente $P/T$ es el mismo en todos los estados de la isócora.
>
> **Paso 3 — Igualar estados.** Aplicando lo anterior a los estados $1$ y $2$:
> $$\frac{P_1}{T_1}=\frac{R}{v}=\frac{P_2}{T_2}\quad\Longrightarrow\quad \frac{P_1}{T_1}=\frac{P_2}{T_2}.\qquad\blacksquare$$

Consecuencia práctica: al calentar un gas en un recipiente rígido, la presión sube linealmente con la temperatura absoluta. Conocidos $P_1,T_1$ y la nueva temperatura $T_2$, la presión final es $P_2=P_1\,T_2/T_1$.

---

## 5. Cambio de entropía

> [!teorema]
> El cambio de entropía específica de un gas ideal en un proceso isocórico es
> $$\Delta s=\int_1^2 c_v\,\frac{dT}{T}=c_v\ln\frac{T_2}{T_1}\qquad(c_v\ \text{cte}),$$
> y equivalentemente, usando Gay-Lussac,
> $$\Delta s=c_v\ln\frac{P_2}{P_1}.$$

> [!demostracion]
> **Paso 1 — Primera ecuación $T\,ds$.** Partimos de la relación fundamental
> $$du=T\,ds-P\,dv.$$
> En el proceso isocórico $dv=0$, de modo que el término $P\,dv$ se anula:
> $$du=T\,ds\quad\Longrightarrow\quad T\,ds=du.$$
>
> **Paso 2 — Modelo de gas ideal.** Para gas ideal $du=c_v\,dT$. Sustituyendo,
> $$T\,ds=c_v\,dT\quad\Longrightarrow\quad ds=c_v\,\frac{dT}{T}.$$
>
> **Paso 3 — Integración.** Con $c_v$ constante,
> $$\Delta s=\int_1^2 c_v\,\frac{dT}{T}=c_v\ln\frac{T_2}{T_1}.$$
>
> **Paso 4 — Forma en presiones.** Por la ley de Gay-Lussac (sección 4), a volumen constante $T_2/T_1=P_2/P_1$. Por tanto,
> $$\Delta s=c_v\ln\frac{P_2}{P_1}.\qquad\blacksquare$$

---

## 6. Lectura en el plano $T$–$s$

Despejando la temperatura de la expresión $\Delta s=c_v\ln(T_2/T_1)$ se obtiene la **forma explícita de la isócora** en el plano $T$–$s$. Tomando un estado de referencia $(s_1,T_1)$ y un estado genérico $(s,T)$ sobre la misma isócora,

$$s-s_1=c_v\ln\frac{T}{T_1}\quad\Longrightarrow\quad \boxed{\,T=T_1\,e^{(s-s_1)/c_v}\,}=T_1\,e^{\Delta s/c_v}.$$

> [!teoria]
> La isócora es, por tanto, una **exponencial creciente** en el plano $T$–$s$. Su pendiente local se obtiene derivando: a partir de $T\,ds=c_v\,dT$,
> $$\left(\frac{\partial T}{\partial s}\right)_v=\frac{T}{c_v}.$$
> El análogo para la isóbara da $(\partial T/\partial s)_P=T/c_p$. Como para un gas ideal $c_p>c_v$ (recuérdese $c_p-c_v=R$, con $R>0$), se cumple
> $$\frac{T}{c_v}>\frac{T}{c_p},$$
> es decir, **a una misma temperatura la isócora es más empinada que la isóbara**. Esto es coherente con la figura: ambas curvas crecen, pero la de volumen constante sube más rápido.

El área bajo la isócora en el plano $T$–$s$, $\int T\,ds$, representa el calor transferido $q$; y como en este proceso (sin otros trabajos) $q=\Delta u$, ese área mide directamente el cambio de energía interna.

---

## 7. Ejemplo: tanque rígido con resistencia eléctrica

> [!ejemplo]
> Un **tanque rígido y sellado** de volumen $V=2{,}0\ \text{m}^3$ contiene aire a $P_1=150\ \text{kPa}$ y $T_1=300\ \text{K}$. En su interior hay una **resistencia eléctrica** que, al circular corriente, entrega un trabajo eléctrico $W_{elec}=200\ \text{kJ}$ al aire. Simultáneamente, el tanque recibe calor $Q=100\ \text{kJ}$ de una **fuente térmica** a $T_{fuente}=600\ \text{K}$. Trate el aire como gas ideal con $c_v=0{,}718\ \text{kJ/kg·K}$ y $R=0{,}287\ \text{kJ/kg·K}$.
>
> Determine: **(a)** la masa de aire y las condiciones finales $T_2$ y $P_2$; **(b)** verifique el balance de energía; **(c)** el cambio de entropía $\Delta S$ del aire; **(d)** la entropía generada $S_{gen}$.

> [!solucion]
> **Paso 1 — Masa de aire.** De la ecuación de estado en el estado $1$, $P_1 V=m R T_1$:
> $$m=\frac{P_1 V}{R\,T_1}=\frac{150\ \text{kPa}\times 2{,}0\ \text{m}^3}{0{,}287\ \text{kJ/kg·K}\times 300\ \text{K}}=\frac{300}{86{,}1}\approx 3{,}484\ \text{kg}.$$
> (Coherencia de unidades: $\text{kPa·m}^3=\text{kJ}$.)
>
> **Paso 2 — Balance de energía (a) y (b).** El sistema es cerrado y rígido, luego el **trabajo de frontera es nulo** ($W_{front}=0$). Pero la resistencia entrega trabajo **eléctrico al sistema**: con el convenio $w>0$ por el sistema, el trabajo eléctrico que **entra** es negativo,
> $$W=-W_{elec}=-200\ \text{kJ}.$$
> La primera ley para el sistema cerrado da
> $$\Delta U=Q-W=Q-(-W_{elec})=Q+W_{elec}=100+200=300\ \text{kJ}.$$
> Este es justamente el **punto fino**: aunque $W_{front}=0$, el trabajo eléctrico sí transfiere energía, y por eso $\Delta U\neq Q$. La igualdad $q_v=\Delta u$ de la sección 2 **no aplica aquí** porque existe un segundo modo de trabajo.
>
> **Paso 3 — Temperatura final $T_2$.** Como $\Delta U=m\,c_v(T_2-T_1)$,
> $$T_2=T_1+\frac{\Delta U}{m\,c_v}=300+\frac{300}{3{,}484\times 0{,}718}=300+\frac{300}{2{,}502}=300+119{,}9\approx 419{,}9\ \text{K}.$$
>
> **Paso 4 — Presión final $P_2$.** El volumen es constante, así que aplica la ley de Gay-Lussac (sección 4):
> $$P_2=P_1\,\frac{T_2}{T_1}=150\times\frac{419{,}9}{300}=150\times 1{,}400\approx 210{,}0\ \text{kPa}.$$
>
> **Paso 5 — Cambio de entropía del aire (c).** A volumen constante, de la sección 5,
> $$\Delta S=m\,c_v\ln\frac{T_2}{T_1}=3{,}484\times 0{,}718\times\ln\frac{419{,}9}{300}.$$
> El cociente $T_2/T_1=1{,}400$, con $\ln 1{,}400=0{,}3365$. Entonces
> $$\Delta S=3{,}484\times 0{,}718\times 0{,}3365=2{,}502\times 0{,}3365\approx 0{,}842\ \text{kJ/K}.$$
>
> **Paso 6 — Entropía generada (d).** La fuente entrega el calor $Q$ a $T_{fuente}=600\ \text{K}$. El balance de entropía para el aire entre los estados $1$ y $2$ es
> $$\Delta S=\frac{Q}{T_{fuente}}+S_{gen}\quad\Longrightarrow\quad S_{gen}=\Delta S-\frac{Q}{T_{fuente}}.$$
> Sustituyendo,
> $$S_{gen}=0{,}842-\frac{100}{600}=0{,}842-0{,}1667\approx 0{,}675\ \text{kJ/K}.$$
> Como $S_{gen}>0$, el proceso es **irreversible** —consistente con la presencia de disipación eléctrica (resistencia) y de transferencia de calor a través de una diferencia finita de temperatura ($600\ \text{K}\to T_{aire}$). $\blacksquare$

---

## 8. Resumen operativo de fórmulas

| Magnitud | Expresión (gas ideal, $v=$cte) |
|---|---|
| Condición | $v=\text{cte},\ dv=0$ |
| Trabajo de frontera | $w=\displaystyle\int_1^2 P\,dv=0$ |
| Primera ley (sin otros trabajos) | $q_v=\Delta u=c_v\,\Delta T$ |
| Definición de $c_v$ | $c_v=\left(\partial u/\partial T\right)_v$ |
| Relación de estados | $P_1/T_1=P_2/T_2$ (Gay-Lussac) |
| Cambio de entropía | $\Delta s=c_v\ln(T_2/T_1)=c_v\ln(P_2/P_1)$ |
| Curva en $T$–$s$ | $T=T_1\,e^{\Delta s/c_v}$ |
| Pendiente en $T$–$s$ | $(\partial T/\partial s)_v=T/c_v$ |

> [!warning]
> Antes de escribir $q_v=\Delta u$, verifique que el **único** modo de trabajo es el de frontera (que aquí es nulo). Si hay resistencias eléctricas, agitadores u otros, use el balance completo $\Delta u=q-w$ con $w$ acumulando todos los modos, y recuerde que el trabajo que **entra** lleva signo negativo en el convenio $w>0$ por el sistema.
