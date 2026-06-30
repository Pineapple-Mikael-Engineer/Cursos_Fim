---
title: Metodo de Energia Unicidad
order: 6
tags:
  - ecuaciones
  - edp
  - teoria
  - calor
  - energia
draft: false
aliases:
  - método de energía
  - unicidad por energía
  - energía decae
  - energy method heat
  - uniqueness heat equation
---

# Metodo de Energia Unicidad

> [!definicion]
> El **método de energía** demuestra la **unicidad** de la solución del calor controlando la cantidad
> $$E(t)=\int_0^L u(x,t)^2\,dx\ \ge 0,$$
> una "energía" (en realidad, la norma $L^2$ al cuadrado). Para el calor con frontera **homogénea** ($u(0,t)=u(L,t)=0$, Dirichlet) se prueba que esta energía **decae**:
> $$E'(t)\le0.$$
> El argumento es puramente integral —multiplicar la ecuación por $u$ e integrar por partes— y no necesita resolver nada: solo usa la estructura de la EDP y las condiciones de frontera.

> [!info]
> Da la unicidad de la [[Ecuacion del Calor/index| ecuación del calor]] dentro del [[2 Ecuaciones en Derivadas Parciales/index| capítulo de EDP]], por una ruta distinta a la del [[Principio del Maximo Parabolico| principio del máximo]]. Garantiza que la serie obtenida por [[Separacion Calor Dirichlet| separación con Dirichlet]] es la **única** solución. El mismo esquema (multiplicar por la solución e integrar por partes) se reutiliza en la [[Energia de la Onda| energía de la onda]], con un desenlace opuesto.

---

## Ejemplo

> [!ejemplo] Por qué dos soluciones con los mismos datos coinciden
> Imaginemos que alguien afirma haber hallado **dos** soluciones distintas, $u_1$ y $u_2$, del mismo problema: misma ecuación $u_t=\alpha^2u_{xx}$, mismo dato inicial $f$, mismos extremos a cero. Formamos su diferencia $w=u_1-u_2$. Por linealidad, $w$ también resuelve el calor, pero con datos **nulos**: $w(x,0)=f-f=0$ y $w(0,t)=w(L,t)=0$.
>
> Miramos su energía $E_w(t)=\int_0^L w^2\,dx$. Dos hechos la atrapan:
> - Arranca en cero: $E_w(0)=\int_0^L 0^2\,dx=0$.
> - Solo puede bajar: $E_w'(t)\le0$ (teorema de abajo), y además $E_w\ge0$ por ser integral de un cuadrado.
>
> Una cantidad que vale $0$, no puede subir y no puede bajar de $0$, está clavada en $0$: $E_w\equiv0$. Pero $\int_0^L w^2\,dx=0$ con $w$ continua obliga a $w\equiv0$. Por tanto $u_1\equiv u_2$: **no hay dos soluciones**, la del problema es **única**.

## En qué consiste

> [!teoria]
> La estrategia tiene tres movimientos que conviene memorizar porque reaparecen en muchas EDP:
> 1. **Multiplicar por la incógnita** $u$ e integrar en el dominio espacial — esto fabrica la derivada de la energía en el lado izquierdo.
> 2. **Integrar por partes** el término difusivo $\int u\,u_{xx}$ — esto baja una derivada de $u_{xx}$ a $u_x$ y saca un término de frontera.
> 3. **Anular el término de frontera** usando las condiciones (aquí, Dirichlet homogéneo) — lo que queda tiene **signo definido**. El signo es lo que decide el comportamiento: en el calor sale $-\int u_x^2\le0$ (decae), mientras que en la onda la misma maniobra deja la energía **constante**.

> [!teorema] La energía decae
> Si $u$ resuelve $u_t=\alpha^2u_{xx}$ en $[0,L]$ con $u(0,t)=u(L,t)=0$, entonces
> $$E(t)=\int_0^L u(x,t)^2\,dx\quad\text{cumple}\quad E'(t)=-2\alpha^2\int_0^L u_x^2\,dx\le0.$$

> [!demostracion]
> **Paso 1 — Derivar la energía y usar la ecuación.** Derivando bajo la integral (válido si $u$ es suave para $t>0$, cosa que garantiza el suavizado del calor) y aplicando luego $u_t=\alpha^2u_{xx}$:
> $$E'(t)=\frac{d}{dt}\int_0^L u^2\,dx=\int_0^L 2u\,u_t\,dx=2\alpha^2\int_0^L u\,u_{xx}\,dx.$$
> La ecuación nos ha cambiado la derivada temporal $u_t$ por la espacial $u_{xx}$.
>
> **Paso 2 — Integrar por partes.** Tomando la primitiva del segundo factor:
> $$\int_0^L u\,u_{xx}\,dx=\Big[\,u\,u_x\,\Big]_0^L-\int_0^L u_x\,u_x\,dx
> =\Big[\,u\,u_x\,\Big]_0^L-\int_0^L u_x^2\,dx.$$
> El **corchete de frontera** se anula: por Dirichlet homogéneo $u(0,t)=u(L,t)=0$, así que $u\,u_x$ vale cero en ambos extremos. Queda
> $$\int_0^L u\,u_{xx}\,dx=-\int_0^L u_x^2\,dx.$$
>
> **Paso 3 — Concluir el signo.** Sustituyendo en el Paso 1:
> $$E'(t)=-2\alpha^2\int_0^L u_x^2\,dx\le0,$$
> porque $\alpha^2>0$ y el integrando $u_x^2\ge0$. La energía **nunca crece**; decae estrictamente salvo que $u_x\equiv0$ (perfil plano). $\blacksquare$

> [!proposicion] Unicidad del problema de Dirichlet
> El problema $u_t=\alpha^2u_{xx}$ con dato inicial $u(x,0)=f(x)$ y frontera $u(0,t)=u(L,t)=0$ tiene a lo sumo **una** solución. En efecto, si $u_1,u_2$ son dos soluciones, $w=u_1-u_2$ resuelve el mismo problema con datos nulos; entonces $E_w(0)=0$, $E_w(t)\ge0$ y $E_w'(t)\le0$ fuerzan $E_w\equiv0$, de donde $w\equiv0$, es decir $u_1\equiv u_2$. (El mismo argumento cubre la frontera de **Neumann** $u_x(0,t)=u_x(L,t)=0$: el corchete $[u\,u_x]_0^L$ también se anula, ahora porque se anula $u_x$.)

> [!info] Contraste con la onda: disipación frente a conservación
> Si se repite esta cuenta para la [[Energia de la Onda| energía de la onda]], el balance da $E'(t)=0$: la energía se **conserva**, no decae. La diferencia nace de la estructura de cada EDP —una derivada temporal de primer orden (calor) frente a segundo orden (onda)—. Físicamente, el decaimiento $E'\le0$ es la huella de la **irreversibilidad** y el suavizado del calor, mientras que la conservación refleja que la onda no pierde energía: oscila sin amortiguar.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Energía | $E(t)=\int_0^L u^2\,dx\ge0$ |
> | Resultado | $E'(t)=-2\alpha^2\int_0^L u_x^2\,dx\le0$ (decae) |
> | Paso clave 1 | $E'=2\int u\,u_t=2\alpha^2\int u\,u_{xx}$ |
> | Paso clave 2 | $\int u\,u_{xx}=[u\,u_x]_0^L-\int u_x^2=-\int u_x^2$ |
> | Anula la frontera | Dirichlet $u(0)=u(L)=0$ (o Neumann $u_x=0$) |
> | Aplicación | unicidad de Dirichlet/Neumann + estabilidad $L^2$ |
> | Contraste | onda: $E'=0$ (se conserva) |

> [!corolario]
> El método de energía y el [[Principio del Maximo Parabolico| principio del máximo]] dan la misma conclusión —unicidad— por caminos distintos: uno mide en norma $L^2$ (energía), el otro en norma $L^\infty$ (máximo puntual). Tener ambos es útil porque el de energía se generaliza bien a varias dimensiones y a problemas no lineales, mientras que el del máximo da cotas puntuales finas.

> [!referencia]
> - La vía alternativa a la unicidad: [[Principio del Maximo Parabolico]].
> - El contraste conservativo: [[Energia de la Onda]].
> - El índice del tema: [[Ecuacion del Calor/index]].
