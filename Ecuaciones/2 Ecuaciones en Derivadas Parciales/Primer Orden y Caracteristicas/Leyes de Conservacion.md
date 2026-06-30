---
title: Leyes de Conservación
order: 3
tags:
  - ecuaciones
  - edp
  - teoria
  - caracteristicas
  - leyes-conservacion
draft: false
aliases:
  - Ley de conservación escalar
  - Rankine-Hugoniot
  - Conservation Laws
---

# Leyes de Conservación

> [!definicion]
> Una **ley de conservación** escalar es una EDP de primer orden de la forma
> $$u_t+f(u)_x=0,$$
> donde $u$ es una **densidad** (de masa, de coches, de probabilidad…) y $f(u)$ es el **flujo** asociado. En **forma integral**, integrando sobre un intervalo $[a,b]$,
> $$\frac{d}{dt}\int_a^b u\,dx=f\big(u(a,t)\big)-f\big(u(b,t)\big):$$
> la cantidad total entre $a$ y $b$ **solo cambia por lo que entra o sale por los bordes**. Sus características satisfacen $\dfrac{dx}{dt}=f'(u)$.

> [!info]
> Es la forma "física" de las EDP [[Cuasilineal y No Lineal| cuasilineales]]: da el significado conservativo de los choques y la regla para su velocidad. Su modelo de cabecera es [[Ondas de Choque y Burgers| Burgers]]. Parte de [[Primer Orden y Caracteristicas/index| Primer Orden y Características]].

---

## Ejemplo

> [!ejemplo] Tráfico / Burgers: $f(u)=\tfrac12 u^2$
> El flujo cuadrático $f(u)=\tfrac12 u^2$ da la ley de conservación
> $$u_t+\Big(\tfrac12 u^2\Big)_x=0\quad\Longleftrightarrow\quad u_t+u\,u_x=0,$$
> es decir, **Burgers no viscoso** escrito en forma conservativa. Las características avanzan a $f'(u)=u$ (cada altura viaja a su propia velocidad). Cuando se forma un **choque** entre un estado izquierdo $u_L$ y uno derecho $u_R$, su velocidad la da la fórmula de Rankine-Hugoniot (abajo):
> $$s=\frac{f(u_L)-f(u_R)}{u_L-u_R}=\frac{\tfrac12 u_L^2-\tfrac12 u_R^2}{u_L-u_R}
> =\frac{u_L+u_R}{2}.$$
> El choque viaja a la **velocidad media** de los dos estados que separa: un resultado limpio y memorable que es la base del modelado de embotellamientos de tráfico.

---

## En qué consiste

> [!teoria]
> La diferencia entre escribir $u_t+f(u)_x=0$ (forma conservativa) y $u_t+f'(u)u_x=0$ (forma cuasilineal) parece cosmética mientras $u$ es suave —son equivalentes por la regla de la cadena— pero **deja de serlo en cuanto aparece una discontinuidad**. La forma integral $\frac{d}{dt}\int_a^b u\,dx=f(u(a,t))-f(u(b,t))$ **sigue teniendo sentido** aunque $u$ sea discontinua, porque no contiene derivadas de $u$. Es esta forma integral la que define qué es una **solución débil** y la que fija la velocidad del choque. La forma diferencial es solo su sombra en la región donde $u$ es suave.

> [!teorema] Condición de Rankine-Hugoniot
> Si una solución débil de $u_t+f(u)_x=0$ tiene una discontinuidad (choque) que se mueve a lo largo de la curva $x=\xi(t)$, con estados $u_L$ a la izquierda y $u_R$ a la derecha, entonces la velocidad del frente $s=\dot\xi$ satisface
> $$s=\frac{[f]}{[u]}=\frac{f(u_L)-f(u_R)}{u_L-u_R},$$
> el **cociente de los saltos** del flujo y de la densidad.

> [!demostracion]
> **Paso 1 — Forma integral alrededor del frente.** Tomemos $a<\xi(t)<b$ y apliquemos la conservación al intervalo $[a,b]$ que contiene la discontinuidad:
> $$\frac{d}{dt}\int_a^b u(x,t)\,dx=f\big(u(a,t)\big)-f\big(u(b,t)\big)=f(u_L)-f(u_R),$$
> donde en los bordes $u$ es suave y vale $u_L$, $u_R$ a cada lado.
>
> **Paso 2 — Derivar la integral con frontera móvil.** Partimos la integral en los dos tramos separados por $x=\xi(t)$ y usamos la regla de Leibniz (los integrandos son suaves en cada tramo):
> $$\frac{d}{dt}\!\left[\int_a^{\xi}u\,dx+\int_{\xi}^{b}u\,dx\right]
> =\int_a^{\xi}u_t\,dx+\int_{\xi}^{b}u_t\,dx+\dot\xi\,\big(u_L-u_R\big),$$
> porque la frontera móvil aporta $u_L\dot\xi$ por el extremo superior del primer tramo y $-u_R\dot\xi$ por el inferior del segundo.
>
> **Paso 3 — Anular las integrales y despejar.** En cada tramo $u$ es suave y cumple $u_t=-f(u)_x$; al hacer $a\to\xi^-$ y $b\to\xi^+$ las integrales de $u_t$ tienden a cero (intervalos que se encogen), mientras los términos de frontera de esas integrales reproducen $f(u_L)-f(u_R)$. Igualando con el Paso 1 queda
> $$\dot\xi\,(u_L-u_R)=f(u_L)-f(u_R)\quad\Longrightarrow\quad s=\frac{f(u_L)-f(u_R)}{u_L-u_R}.$$
> $\blacksquare$

> [!info] Soluciones débiles y condición de entropía
> Tras el choque la solución **no es derivable** en el frente, de modo que la EDP diferencial no tiene sentido allí. Se interpreta en sentido **integral (débil)**: $u$ es solución débil si cumple $\int\!\int\big(u\,\varphi_t+f(u)\,\varphi_x\big)\,dx\,dt=0$ para toda función de prueba $\varphi$ de soporte compacto. El precio de admitir discontinuidades es que aparecen **muchas** soluciones débiles para el mismo dato (no unicidad). Para quedarse con la **física** se impone una **condición de entropía** (p. ej. $f'(u_L)>s>f'(u_R)$: las características deben *entrar* al choque, no salir de él). Es lo que distingue un choque admisible de una rarefacción —ver [[Ondas de Choque y Burgers]].

> [!proposicion]
> La velocidad de Rankine-Hugoniot **depende de la forma del flujo $f$**, no solo del salto de $u$. Por eso una misma transición $u_L\to u_R$ se mueve distinto según el problema: $s=\tfrac{u_L+u_R}2$ para Burgers, pero otro valor para tráfico con $f(u)=u(1-u)$, etc.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Forma diferencial | $u_t+f(u)_x=0$ |
> | Forma integral | $\dfrac{d}{dt}\displaystyle\int_a^b u\,dx=f(u(a,t))-f(u(b,t))$ |
> | Características | $\dfrac{dx}{dt}=f'(u)$ |
> | Velocidad del choque | $s=\dfrac{f(u_L)-f(u_R)}{u_L-u_R}=\dfrac{[f]}{[u]}$ |
> | Burgers $f=\tfrac12u^2$ | $s=\dfrac{u_L+u_R}{2}$ |

> [!corolario]
> La forma conservativa no es una elección estética: es la **única** que sobrevive a las discontinuidades. De ella sale, vía la forma integral, la regla de Rankine-Hugoniot que fija *unívocamente* a qué velocidad viaja un choque, y la noción de solución débil + entropía que lo hace bien planteado.

> [!referencia]
> - El modelo donde se aplica todo esto: [[Ondas de Choque y Burgers]].
> - De dónde viene la singularidad: [[Cuasilineal y No Lineal]].
> - Vuelta al mapa: [[Primer Orden y Caracteristicas/index]].
