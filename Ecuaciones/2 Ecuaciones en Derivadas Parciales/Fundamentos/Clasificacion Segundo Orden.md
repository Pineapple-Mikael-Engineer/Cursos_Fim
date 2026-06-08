---
title: Clasificación de Segundo Orden
tags:
  - ecuaciones
  - edp
  - teoria
  - fundamentos
  - clasificacion
draft: false
aliases:
  - clasificación de EDP
  - elíptica parabólica hiperbólica
  - discriminante EDP
  - classification of PDEs
---

# Clasificación de EDP de Segundo Orden

> [!definicion]
> Una EDP lineal de segundo orden en dos variables
> $$A\,u_{xx}+B\,u_{xy}+C\,u_{yy}+(\text{términos de orden menor})=0$$
> se clasifica por el **discriminante** $\Delta=B^2-4AC$ (igual que una cónica):
> $$\Delta<0\ \text{**elíptica**},\qquad \Delta=0\ \text{**parabólica**},\qquad \Delta>0\ \text{**hiperbólica**}.$$
> El tipo lo fijan **solo** los coeficientes de las derivadas de **orden máximo** (la *parte
> principal*); puede variar de región a región si $A,B,C$ dependen de $(x,y)$.

> [!info]
> Nota central de los [[Fundamentos/index| fundamentos de EDP]]. El tipo decide la física, las
> [[Tipos de Condiciones| condiciones]] bien planteadas y el método; las
> [[Formas Canonicas| formas canónicas]] llevan cada tipo a su prototipo (Laplace, calor, onda).

---

## Ejemplo

> [!ejemplo] Clasificar las tres ecuaciones madre
> **Calor** $u_t=\alpha^2u_{xx}$, con variables $(x,t)$: la parte principal es $\alpha^2u_{xx}$, así
> $A=\alpha^2,\ B=0,\ C=0$ (no hay $u_{tt}$). $\Delta=0-0=0$ → **parabólica**.
> **Onda** $u_{tt}=c^2u_{xx}$: $A=c^2,\ B=0,\ C=-1$ (escrita $c^2u_{xx}-u_{tt}=0$). $\Delta=0-4(c^2)(-1)=4c^2>0$ → **hiperbólica**.
> **Laplace** $u_{xx}+u_{yy}=0$: $A=1,\ B=0,\ C=1$. $\Delta=0-4=-4<0$ → **elíptica**.
> Las tres "madres" son una de cada tipo: difusión, propagación y equilibrio.

> [!ejemplo] Tipo que cambia de región: la ecuación de Tricomi
> **$u_{xx}+x\,u_{yy}=0$.** Aquí $A=1,B=0,C=x$, $\Delta=-4x$. Entonces es **elíptica** donde $x>0$,
> **hiperbólica** donde $x<0$ y **parabólica** sobre $x=0$. Las EDP de tipo **mixto** modelan flujos
> transónicos (subsónico elíptico / supersónico hiperbólico).

---

## En qué consiste

> [!teoria] La analogía con las cónicas (por qué un discriminante)
> Si se hace un cambio lineal de variables y se mira cómo se transforma la parte principal, el papel
> de $A,B,C$ es idéntico al de los coeficientes de una **forma cuadrática** $A\xi^2+B\xi\eta+C\eta^2$.
> Sus "direcciones características" (donde la forma se degenera) son reales y distintas si $\Delta>0$
> (dos familias → hiperbólica), reales coincidentes si $\Delta=0$ (una familia → parabólica) o
> complejas si $\Delta<0$ (ninguna real → elíptica). Esas **direcciones características** son las
> curvas a lo largo de las cuales se propaga la información (ver
> [[Primer Orden y Caracteristicas/index| características]]); que existan o no marca la diferencia
> entre propagar (hiperbólica) y promediar (elíptica).

> [!proposicion] Lo que implica cada tipo
> | Tipo | Características reales | Comportamiento | Condiciones bien planteadas |
> |---|---|---|---|
> | Hiperbólica | **dos** familias | propaga frentes a velocidad finita; **no** suaviza | inicial ($u,u_t$) + frontera |
> | Parabólica | **una** familia | difunde; **suaviza** al instante; irreversible | inicial + frontera |
> | Elíptica | **ninguna** real | equilibrio; solución muy suave; **promedia** | solo frontera (Dirichlet/Neumann) |

> [!demostracion] Invariancia del tipo bajo cambios de variable
> **Paso 1 — cambio de coordenadas.** Bajo $\xi=\xi(x,y),\eta=\eta(x,y)$ (suave, invertible), la parte
> principal $Au_{xx}+Bu_{xy}+Cu_{yy}$ se transforma en otra $A^*u_{\xi\xi}+B^*u_{\xi\eta}+C^*u_{\eta\eta}$.
> **Paso 2 — cómo cambia el discriminante.** Un cálculo directo da $(B^*)^2-4A^*C^*=(B^2-4AC)\,J^2$,
> donde $J=\det\partial(\xi,\eta)/\partial(x,y)$ es el jacobiano.
> **Paso 3 — concluir.** Como $J\neq0$ (cambio invertible), $J^2>0$: el **signo** de $\Delta$ se
> conserva. Por tanto el **tipo** es una propiedad intrínseca de la EDP, no del sistema de
> coordenadas. $\blacksquare$ Esto justifica reducir cada tipo a su [[Formas Canonicas| forma canónica]].

> [!algoritmo] Clasificar una EDP de segundo orden
> 1. Aísla la **parte principal** (solo derivadas de orden 2): identifica $A,B,C$ (con $B$ el
>    coeficiente de $u_{xy}$).
> 2. Calcula $\Delta=B^2-4AC$.
> 3. $\Delta<0$ elíptica · $\Delta=0$ parabólica · $\Delta>0$ hiperbólica.
> 4. Si $A,B,C$ dependen del punto, el tipo puede **cambiar** de región (EDP mixta).

## Resumen

> [!resumen]
> | $\Delta=B^2-4AC$ | Tipo | Prototipo |
> |:--:|:--|:--|
> | $<0$ | elíptica | Laplace $u_{xx}+u_{yy}=0$ |
> | $=0$ | parabólica | calor $u_t=\alpha^2u_{xx}$ |
> | $>0$ | hiperbólica | onda $u_{tt}=c^2u_{xx}$ |

> [!corolario]
> Una sola cuenta —el signo de $B^2-4AC$— separa los tres mundos de las EDP. No es casualidad que las
> tres ecuaciones de la física (calor, onda, Laplace) sean una de cada tipo: agotan los
> comportamientos cualitativos posibles de una EDP lineal de segundo orden.

> [!referencia]
> - Reducir cada tipo a su prototipo: [[Formas Canonicas]].
> - Las curvas que propagan la información: [[Metodo de las Caracteristicas]].
> - Qué datos hacen bien planteado cada tipo: [[Tipos de Condiciones]], [[Problemas Bien Planteados]].
