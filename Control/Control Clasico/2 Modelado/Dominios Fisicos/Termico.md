---
title: Sistemas Térmicos
tags:
  - control-clasico
  - dominios-fisicos
  - modelado
draft: false
aliases:
  - térmico
  - sistemas térmicos
  - transferencia de calor
---

# Sistemas Térmicos

> [!definicion]
> Un sistema térmico se modela con dos elementos —resistencia térmica $R$ y capacitancia térmica $C=mc_p$— mediante el balance de energía. Para un cuerpo con flujo de calor de entrada $q$ y pérdida al ambiente:
> $$C\frac{dT}{dt}=q-\frac{T-T_a}{R}\qquad\Longrightarrow\qquad G(s)=\frac{\theta(s)}{Q(s)}=\frac{R}{RCs+1},\quad \theta=T-T_a.$$
> Carece de inductancia: es **siempre de primer orden** por capacitancia (no oscila, no tiene sobrepico).

> [!info]
> Es uno de los [[Funcion Transferencia/index | dominios físicos]] del modelado, con la misma estructura $R$–$C$ que los dominios [[Fluidos Nivel | hidráulico]] y [[Neumatico | neumático]], y **análogo** al [[Electrico | circuito RC]] (temperatura↔voltaje, flujo de calor↔corriente). Es la base del modelo **FOPDT** típico de procesos.

---

## Ejemplo

> [!ejemplo]
> **Cuerpo calentado con pérdida al ambiente, valores numéricos.** Cuerpo de capacitancia $C=200\ \text{J/K}$ y resistencia al ambiente $R=0.5\ \text{K/W}$. Entrada flujo de calor $q$, salida temperatura sobre el ambiente $\theta=T-T_a$.
>
> ![[sistema_termico.svg|450]]
>
> **Paso 1 — Balance de energía** (el calor neto que entra cambia la temperatura):
> $$C\frac{dT}{dt}=q-\frac{T-T_a}{R}.$$
>
> **Paso 2 — Variables de desviación** ($\theta=T-T_a$, $\dot\theta=\dot T$) y Laplace (CI nulas):
> $$Cs\,\theta(s)=Q(s)-\frac{\theta(s)}{R}\;\Longrightarrow\;\theta(s)\Big(Cs+\tfrac{1}{R}\Big)=Q(s).$$
>
> **Paso 3 — Función de transferencia:**
> $$G(s)=\frac{\theta(s)}{Q(s)}=\frac{R}{RCs+1}=\frac{0.5}{100\,s+1}.$$
>
> **Paso 4 — Interpretación:** primer orden con $\tau=RC=(0.5)(200)=100\ \text{s}$, ganancia DC $R=0.5\ \text{K/W}$, polo en $s=-0.01\ \text{rad/s}$. Para $q=100\,$W en régimen, $\theta\to R\,q=50\ \text{K}$ sobre el ambiente, alcanzado en $\approx4\tau=400\,$s. **Sin sobrepico** (un solo polo real).

---

## Elementos y leyes constitutivas

> [!teoria]
> El dominio térmico usa dos elementos. La variable de **esfuerzo** es la temperatura $T$ [K]; la de **flujo** es el flujo de calor $q$ [W = J/s]:
>
> | Elemento | Definición | Relación | Unidad |
> |---|---|---|---|
> | Resistencia $R$ | oposición al flujo de calor | $R=\dfrac{\Delta T}{q}$ | K/W |
> | Capacitancia $C$ | calor almacenado por grado | $C=m\,c_p$ | J/K |
>
> La ley que las une es el **balance de energía**: $C\,\dfrac{dT}{dt}=q_{in}-q_{out}$. Casos de resistencia: **conducción** $R=L/(kA)$; **convección** $R=1/(hA)$.

> [!warning] No hay inductancia térmica
> El dominio térmico **carece de análogo a la inductancia**: el calor no tiene inercia. Por eso los sistemas térmicos son **siempre de primer orden** por cada capacitancia, no oscilan y no presentan sobrepico.

---

## Más configuraciones

> [!ejemplo] Con retardo de transporte (FOPDT)
> Si el sensor está alejado de la fuente (fluido recorriendo una tubería), aparece un **tiempo muerto** $e^{-Ls}$:
> $$G(s)=\frac{R\,e^{-Ls}}{RCs+1}.$$
> Es el modelo **FOPDT** (primer orden con tiempo muerto), base de la sintonización por [[Ziegler Nichols Curva Reaccion | curva de reacción]]. El retardo es de [[Sistemas Fase Minima | fase no mínima]] y complica el control.

> [!info] Tabla de funciones de transferencia
> | Sistema | Entrada | Salida | $G(s)$ | Tipo |
> |---|---|---|---|---|
> | Cuerpo único | $q$ | $T$ | $\dfrac{R}{RCs+1}$ | 1er orden |
> | Con tiempo muerto | $q$ | $T$ | $\dfrac{R\,e^{-Ls}}{RCs+1}$ | 1er orden + retardo |
> | Dos masas (pared) | $q$ | $T_2$ | $\dfrac{R_2}{(R_1C_1s+1)(R_2C_2s+1)}$ | 2do orden |

---

## Receta de modelado

> [!algoritmo]
> Para la FT de un sistema térmico:
> 1. **Balance de energía** por cuerpo: $C\dfrac{dT}{dt}=\sum q_{in}-\sum q_{out}$, con $C=mc_p$.
> 2. **Resistencias:** expresar cada pérdida como $q=\Delta T/R$ (conducción/convección).
> 3. **Variables de desviación** respecto al ambiente (ver [[Variables Desviacion]]).
> 4. **Retardo:** añadir $e^{-Ls}$ si hay transporte entre fuente y sensor.
> 5. **Laplace con CI nulas** y despejar $\theta(s)/Q(s)$.

> [!info] Analogía térmico-eléctrica
> | Térmico | Eléctrico |
> |---|---|
> | Temperatura $T$ | Voltaje $V$ |
> | Flujo de calor $q$ | Corriente $I$ |
> | Resistencia térmica $R$ | Resistencia $R$ |
> | Capacitancia $C=mc_p$ | Capacitancia $C$ |
> | — (sin inercia) | Inductancia $L$ |
>
> El cuerpo térmico es el análogo del condensador con fuga: **integra** el calor neto. Ver [[Electrico | sistemas eléctricos]].

> [!info] En MATLAB
> ```matlab
> R=0.5; C=200;
> G = tf(R, [R*C 1]);        % R/(RCs+1), tau = 100 s
> G_fopdt = G;
> G_fopdt.InputDelay = 30;   % tiempo muerto L = 30 s
> step(G_fopdt)
> ```

---

## Limitaciones

> [!warning]
> 1. **Parámetros distribuidos:** la temperatura real varía con la posición; el modelo R-C agrupa (*lumped*) y asume cuerpo isotérmico.
> 2. **$R$ no lineal:** la radiación va con $T^4$ y la convección depende de $\Delta T$; requiere [[Serie Taylor | linealización]].
> 3. **Retardo de transporte** frecuente y difícil de controlar.
> 4. **CI nulas:** variables de desviación respecto al ambiente (ver [[Variables Desviacion]]).

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Elementos | resistencia $R$, capacitancia $C=mc_p$ |
> | Ley | balance de energía $C\dot T=q_{in}-q_{out}$ |
> | FT | $G(s)=\dfrac{R}{RCs+1}$ |
> | Constante de tiempo | $\tau=RC$ |
> | Orden | 1 por capacitancia (sin inercia, sin oscilación) |

> [!corolario]
> Modelar un sistema térmico es escribir el balance de energía y sustituir $q=\Delta T/R$: cada cuerpo aporta un polo real, dando primer orden sin sobrepico; el transporte añade un retardo $e^{-Ls}$ (modelo FOPDT). La estructura $R$–$C$ es idéntica a la de los dominios [[Fluidos Nivel | hidráulico]] y [[Neumatico | neumático]] y análoga al [[Electrico | circuito RC]], pero sin inductancia.

> [!referencia]
> - Respuesta de primer orden: [[Primer Orden]].
> - Retardo y FOPDT: [[Sistemas Fase Minima]] · [[Ziegler Nichols Curva Reaccion]].
> - Linealización: [[Serie Taylor]] · [[Variables Desviacion]].
> - Analogías $R$–$C$: [[Electrico]] · [[Fluidos Nivel]] · [[Neumatico]].
