---
title: Oscilador Libre y Amortiguado
tags:
  - ecuaciones
  - edo
  - teoria
  - lineales
  - oscilaciones
  - amortiguamiento
draft: false
aliases:
  - oscilador libre
  - oscilador amortiguado
  - regímenes de amortiguamiento
  - damped free oscillator
  - damping regimes
---

# Oscilador Libre y Amortiguado

> [!definicion]
> El **oscilador libre** (sin fuerza externa) es
> $$m\ddot x+c\dot x+kx=0.$$
> Con la frecuencia natural $\omega_0=\sqrt{k/m}$ y la razón de amortiguamiento
> $\zeta=\dfrac{c}{2\sqrt{mk}}$, la forma canónica es $\ddot x+2\zeta\omega_0\dot x+\omega_0^2 x=0$ y la
> ecuación característica $r^2+2\zeta\omega_0 r+\omega_0^2=0$ tiene raíces
> $$r=-\zeta\omega_0\pm\omega_0\sqrt{\zeta^2-1}.$$
> El signo del radicando $\zeta^2-1$ separa **tres regímenes** de movimiento: subamortiguado ($\zeta<1$),
> crítico ($\zeta=1$) y sobreamortiguado ($\zeta>1$).

> [!info]
> Es la lectura **física** de los tres casos de raíces de la
> [[Coeficientes Constantes Homogenea| ecuación característica]] dentro del bloque
> [[Oscilaciones/index| oscilaciones]]. Aquí $F=0$: solo actúan la inercia, el resorte y la disipación. El
> caso con fuerza se trata en [[Oscilaciones Forzadas y Resonancia| oscilaciones forzadas]].

---

## Ejemplo

> [!ejemplo] Los tres regímenes de amortiguamiento
> ![[oscilador_regimenes.svg|480]]
>
> Respuesta libre desde $x(0)=1,\ \dot x(0)=0$: subamortiguado (oscila y decae), crítico (retorno más
> rápido sin pasar de cero) y sobreamortiguado (decae lento sin oscilar).

> [!ejemplo] Caso subamortiguado resuelto
> **Resolver $\ddot x+2\dot x+5x=0$ con $x(0)=1,\ \dot x(0)=0$.**
>
> Identificamos $\omega_0^2=5\Rightarrow\omega_0=\sqrt5$ y $2\zeta\omega_0=2\Rightarrow
> \zeta=\dfrac{1}{\sqrt5}\approx0.45<1$: **subamortiguado**. La característica $r^2+2r+5=0$ da
> $$r=\frac{-2\pm\sqrt{4-20}}{2}=-1\pm2i,$$
> de modo que $\omega_d=\omega_0\sqrt{1-\zeta^2}=\sqrt5\cdot\sqrt{1-\tfrac15}=2$. Solución general
> $$x(t)=e^{-t}\big(A\cos2t+B\operatorname{sen}2t\big).$$
> Imponiendo $x(0)=1$ se obtiene $A=1$. Derivando,
> $\dot x=e^{-t}\big[(-A+2B)\cos2t-(B+2A)\operatorname{sen}2t\big]$, y $\dot x(0)=0$ da $-A+2B=0\Rightarrow
> B=\tfrac12$. Por tanto
> $$\boxed{\,x(t)=e^{-t}\Big(\cos2t+\tfrac12\operatorname{sen}2t\Big)\,}$$
> una oscilación de frecuencia $\omega_d=2$ bajo una envolvente $e^{-t}$ que la apaga.

---

## En qué consiste

> [!teoria] Qué dice cada raíz
> La parte **real** $-\zeta\omega_0$ es siempre el ritmo de decaimiento: la energía mecánica se disipa por
> el amortiguamiento y la amplitud cae como $e^{-\zeta\omega_0 t}$. La parte bajo la raíz, $\zeta^2-1$,
> decide si además **oscila**:
> - si $\zeta<1$, $\sqrt{\zeta^2-1}$ es imaginario → hay frecuencia de oscilación;
> - si $\zeta\ge1$, es real → no hay oscilación, solo decaimiento.
> Esto es exactamente el discriminante de la característica leído como movimiento.

> [!proposicion] Los tres regímenes
> Según $\zeta$, la solución de $m\ddot x+c\dot x+kx=0$ adopta tres formas (con
> $\omega_d=\omega_0\sqrt{1-\zeta^2}$ y $r_{1,2}=-\zeta\omega_0\pm\omega_0\sqrt{\zeta^2-1}$):
> | Régimen | Condición | Raíces | Solución | Comportamiento |
> |:--|:--:|:--|:--|:--|
> | Subamortiguado | $\zeta<1$ | $-\zeta\omega_0\pm i\omega_d$ | $e^{-\zeta\omega_0 t}(A\cos\omega_d t+B\operatorname{sen}\omega_d t)$ | oscila con amplitud decreciente |
> | Crítico | $\zeta=1$ | $-\omega_0$ (doble) | $(A+Bt)\,e^{-\omega_0 t}$ | retorno más rápido sin oscilar |
> | Sobreamortiguado | $\zeta>1$ | $r_1,r_2<0$ reales | $A\,e^{r_1 t}+B\,e^{r_2 t}$ | decae lento sin oscilar |

> [!algoritmo] Clasificar y resolver un oscilador libre
> 1. Lee $m,c,k$ y calcula $\omega_0=\sqrt{k/m}$ y $\zeta=\dfrac{c}{2\sqrt{mk}}$.
> 2. Compara $\zeta$ con $1$ para saber el régimen (o calcula el discriminante $c^2-4mk$).
> 3. Escribe las raíces $r=-\zeta\omega_0\pm\omega_0\sqrt{\zeta^2-1}$.
> 4. Elige la forma de la solución de la tabla anterior.
> 5. Fija $A,B$ con las condiciones iniciales $x(0)$ y $\dot x(0)$.

> [!proposicion] Por qué el crítico aparece con factor $t$
> En el caso crítico la característica tiene la raíz **doble** $r=-\omega_0$. Como en cualquier raíz
> repetida de la [[Coeficientes Constantes Homogenea| ecuación característica]], la segunda solución gana
> un factor $t$: $\{e^{-\omega_0 t},\,t\,e^{-\omega_0 t}\}$, de donde $x=(A+Bt)e^{-\omega_0 t}$. Es la
> frontera exacta entre oscilar y no oscilar.

> [!info] La importancia del amortiguamiento crítico
> Entre todos los regímenes, el **crítico** ($\zeta=1$) es el que devuelve el sistema al equilibrio en el
> **menor tiempo posible sin sobreoscilar**. Por eso se diseñan en torno a $\zeta=1$ (o ligeramente por
> debajo) las suspensiones de automóvil, los cierrapuertas, los amortiguadores de instrumentos de medida y
> las agujas de los galvanómetros: se busca que la respuesta se asiente rápido sin rebotes. Un sistema muy
> subamortiguado vibra molestamente; uno muy sobreamortiguado es lento y "perezoso".

## Resumen

> [!resumen]
> | Régimen | $\zeta$ | Raíces | Forma de $x(t)$ |
> |:--|:--:|:--|:--|
> | Subamortiguado | $<1$ | complejas $-\zeta\omega_0\pm i\omega_d$ | $e^{-\zeta\omega_0 t}(A\cos\omega_d t+B\operatorname{sen}\omega_d t)$ |
> | Crítico | $=1$ | doble $-\omega_0$ | $(A+Bt)e^{-\omega_0 t}$ |
> | Sobreamortiguado | $>1$ | reales $r_1,r_2<0$ | $A e^{r_1 t}+B e^{r_2 t}$ |

> [!corolario]
> Un único parámetro adimensional, $\zeta$, organiza todo el oscilador libre: dice si el sistema oscila o
> no y a qué velocidad vuelve al equilibrio. La frontera $\zeta=1$ (raíz doble de la característica) marca
> el retorno más rápido sin sobreoscilación.

> [!referencia]
> - La maquinaria de raíces: [[Coeficientes Constantes Homogenea]].
> - Qué pasa al añadir una fuerza externa: [[Oscilaciones Forzadas y Resonancia]].
> - El panorama físico completo: [[Oscilaciones/index]].
