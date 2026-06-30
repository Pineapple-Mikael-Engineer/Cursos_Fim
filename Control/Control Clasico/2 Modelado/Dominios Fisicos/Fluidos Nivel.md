---
title: Sistemas de Fluidos y Nivel
order: 4
tags:
  - control-clasico
  - dominios-fisicos
  - modelado
draft: false
aliases:
  - fluidos
  - nivel
  - sistemas hidráulicos
  - tanques
---

# Sistemas de Fluidos y Nivel

> [!definicion]
> Un sistema de nivel se modela con dos elementos —resistencia hidráulica $R$ (válvula) y capacitancia $C$ (área del tanque)— mediante el balance de masa. Para un tanque con caudal de entrada $q_{in}$ y salida en el nivel $h$:
> $$C\frac{dh}{dt}=q_{in}-\frac{h}{R}\qquad\Longrightarrow\qquad G(s)=\frac{H(s)}{Q_{in}(s)}=\frac{R}{RCs+1}.$$
> Es un dominio de **primer orden** ($R$–$C$): la inertancia del fluido se desprecia.

> [!info]
> Es uno de los [[Funcion Transferencia/index | dominios físicos]] del modelado, con la misma estructura $R$–$C$ que los dominios [[Termico | térmico]] y [[Neumatico | neumático]], y **análogo** al [[Electrico | circuito RC]] (altura↔voltaje, caudal↔corriente). El tanque es el "condensador" que integra el caudal neto.

---

## Ejemplo

> [!ejemplo]
> **Tanque único con valores numéricos.** Tanque de área $A=2\ \text{m}^2$ y válvula de salida laminar con $R=5\ \text{s/m}^2$. Entrada $q_{in}$, salida nivel $h$.
>
> ![[tanque_nivel.svg|450]]
>
> **Paso 1 — Balance de masa** (lo que entra menos lo que sale cambia el volumen $V=A\,h$):
> $$C\frac{dh}{dt}=q_{in}-q_{out},\qquad C=A=2\ \text{m}^2.$$
>
> **Paso 2 — Salida laminar:** $q_{out}=h/R$. Sustituyendo y pasando a Laplace (variables de desviación, CI nulas):
> $$Cs\,H(s)=Q_{in}(s)-\frac{H(s)}{R}\;\Longrightarrow\;H(s)\Big(Cs+\tfrac{1}{R}\Big)=Q_{in}(s).$$
>
> **Paso 3 — Función de transferencia:**
> $$G(s)=\frac{H(s)}{Q_{in}(s)}=\frac{R}{RCs+1}=\frac{5}{10\,s+1}.$$
>
> **Paso 4 — Interpretación:** primer orden con $\tau=RC=(5)(2)=10\ \text{s}$ y ganancia DC $R=5$. Polo en $s=-1/RC=-0.1\ \text{rad/s}$. Sin sobrepico; el nivel se estabiliza en $\approx5\,q_{in}$ tras unos $4\tau=40\,$s. Si la salida fuera el **caudal** $q_{out}=h/R$, la ganancia DC pasa a $1$: $G(s)=1/(RCs+1)$.

---

## Elementos y leyes constitutivas

> [!teoria]
> El dominio hidráulico de nivel usa dos elementos. La variable de **esfuerzo** es la altura/carga $h$ [m] (o presión $P=\rho g h$); la de **flujo** es el caudal volumétrico $q$ [m³/s]:
>
> | Elemento | Definición | Relación | Unidad |
> |---|---|---|---|
> | Resistencia $R$ | oposición de válvula/tubería | $R=\dfrac{dh}{dq}$ | $\text{m·s/m}^3$ |
> | Capacitancia $C$ | almacenamiento del tanque | $C=\dfrac{dV}{dh}=A$ | $\text{m}^2$ |
>
> La ley que las une es el **balance de masa**: $C\,\dfrac{dh}{dt}=q_{in}-q_{out}$. En flujo **laminar** la resistencia es lineal ($h=Rq$); en flujo **turbulento** $q=k\sqrt h$, que se [[Serie Taylor | lineariza]] en el punto de operación.

> [!info] No hay (casi) inductancia
> En la mayoría de sistemas de nivel la **inertancia** (inercia del fluido) es despreciable: el dominio es de **primer orden** por cada tanque. La inertancia solo importa en tuberías largas con flujo rápido (golpe de ariete), donde actuaría como una inductancia.

---

## Más configuraciones

> [!ejemplo] Dos tanques en cascada
> ![[dos_tanques_nivel.svg|500]]
> Dos tanques en serie ($R_1,C_1,R_2,C_2$) sin interacción dan **segundo orden**:
> $$G(s)=\frac{H_2(s)}{Q_{in}(s)}=\frac{R_2}{(R_1C_1s+1)(R_2C_2s+1)}.$$
> Si los tanques **interactúan** (la salida del primero depende del nivel del segundo) aparece un término cruzado y los polos se acoplan, pero el sistema sigue siendo de 2.º orden sin sobrepico (polos reales).

> [!info] Tabla de funciones de transferencia
> | Sistema | Entrada | Salida | $G(s)$ | Tipo |
> |---|---|---|---|---|
> | Tanque único | $q_{in}$ | $h$ | $\dfrac{R}{RCs+1}$ | 1er orden |
> | Tanque (salida en caudal) | $q_{in}$ | $q_{out}$ | $\dfrac{1}{RCs+1}$ | 1er orden |
> | Dos tanques (sin interacción) | $q_{in}$ | $h_2$ | $\dfrac{R_2}{(R_1C_1s+1)(R_2C_2s+1)}$ | 2do orden |

---

## Receta de modelado

> [!algoritmo]
> Para la FT de un sistema de nivel:
> 1. **Balance de masa** por tanque: $C\dfrac{dh}{dt}=\sum q_{in}-\sum q_{out}$, con $C=A$ (área).
> 2. **Resistencias:** expresar cada caudal de salida como $q=\Delta h/R$ (laminar) o linealizar $q=k\sqrt h$ si es turbulento.
> 3. **Variables de desviación** respecto al punto de operación (ver [[Variables Desviacion]]).
> 4. **Laplace con CI nulas** y despejar $H(s)/Q_{in}(s)$.

> [!info] Analogía hidráulico-eléctrica
> | Hidráulico | Eléctrico |
> |---|---|
> | Altura $h$ (o presión) | Voltaje $V$ |
> | Caudal $q$ | Corriente $I$ |
> | Resistencia $R$ (válvula) | Resistencia $R$ |
> | Capacitancia $C$ (área tanque) | Capacitancia $C$ |
> | Inertancia (tubería larga) | Inductancia $L$ |
>
> El tanque es el análogo del condensador: **integra** el caudal neto. Ver [[Electrico | sistemas eléctricos]].

> [!info] En MATLAB
> ```matlab
> R=5; C=2;
> G = tf(R, [R*C 1]);   % R/(RCs+1), tau = 10 s
> step(G)               % respuesta de nivel al escalon de caudal
> ```

---

## Limitaciones

> [!warning]
> 1. **Flujo turbulento:** $q=k\sqrt h$ es no lineal; las FT asumen flujo laminar o un punto de operación [[Serie Taylor | linealizado]].
> 2. **$R$ variable:** la resistencia de válvula depende del punto de operación.
> 3. **Inertancia despreciada:** válido salvo en tuberías largas/flujo rápido.
> 4. **CI nulas:** variables de desviación (ver [[Variables Desviacion]]).

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Elementos | resistencia $R$, capacitancia $C=A$ |
> | Ley | balance de masa $C\dot h=q_{in}-q_{out}$ |
> | FT (nivel) | $G(s)=\dfrac{R}{RCs+1}$ |
> | Constante de tiempo | $\tau=RC$ |
> | Orden | 1 por tanque (sin inertancia) |

> [!corolario]
> Modelar un sistema de nivel es escribir el balance de masa por tanque y sustituir $q=\Delta h/R$: cada tanque aporta un polo real, dando primer orden ($\tau=RC$) sin sobrepico. La estructura $R$–$C$ es idéntica a la de los dominios [[Termico | térmico]] y [[Neumatico | neumático]] y análoga al [[Electrico | circuito RC]]; el flujo turbulento exige [[Serie Taylor | linealizar]].

> [!referencia]
> - Linealización del flujo turbulento: [[Serie Taylor]] · [[Variables Desviacion]].
> - Respuesta de primer orden: [[Primer Orden]].
> - Analogías $R$–$C$: [[Electrico]] · [[Termico]] · [[Neumatico]].
