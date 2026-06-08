---
title: Tipos de Condiciones
tags:
  - ecuaciones
  - edp
  - teoria
  - fundamentos
  - condiciones
draft: false
aliases:
  - condiciones de contorno
  - Dirichlet Neumann Robin
  - condiciones iniciales y de frontera
  - boundary and initial conditions
  - Cauchy data
---

# Tipos de Condiciones para EDP

> [!definicion]
> Las **condiciones** son los datos que se añaden a una EDP para **cerrar** el problema y seleccionar
> una solución concreta entre las infinitas posibles. Se dividen en:
> - **Iniciales** (datos de **Cauchy**): valores de $u$ —y de $u_t$ si la ecuación es de **segundo
>   orden en $t$**— en el instante $t=0$.
> - **De frontera**, impuestas sobre el borde $\partial\Omega$ del dominio espacial:
>   - **Dirichlet**: se fija el **valor** $u=g$ en la frontera;
>   - **Neumann**: se fija la **derivada normal** $\dfrac{\partial u}{\partial n}=g$ (flujo);
>   - **Robin** (mixta): combinación $\alpha\,u+\beta\,\dfrac{\partial u}{\partial n}=g$;
>   - **periódicas**: $u$ y sus derivadas coinciden en extremos opuestos del dominio.

> [!info]
> Complementa [[Problemas Bien Planteados| problemas bien planteados]]: aquí está el **catálogo** de
> condiciones, y allí el criterio de cuáles hacen sano cada problema. La elección depende del
> [[Clasificacion Segundo Orden| tipo]] de la EDP y determina el problema de autovalores que aparece
> al aplicar la [[Tecnica de Separacion| separación de variables]].

---

## Ejemplo

> [!ejemplo] Una barra: extremos fijos (Dirichlet) vs aislados (Neumann)
> Calor en una barra $[0,L]$, $u_t=\alpha^2u_{xx}$, con dato inicial $u(x,0)=f(x)$. Comparemos dos
> maneras de tratar los extremos.
>
> **(a) Extremos a temperatura cero — Dirichlet.**
> $$u(0,t)=0,\qquad u(L,t)=0.$$
> Al separar $u=X(x)T(t)$, $X$ resuelve $X''+\lambda X=0$ con $X(0)=X(L)=0$. Las autofunciones son
> $$X_n(x)=\operatorname{sen}\!\Big(\frac{n\pi x}{L}\Big),\qquad \lambda_n=\Big(\frac{n\pi}{L}\Big)^2,\quad n=1,2,\dots$$
> El desarrollo natural es una **serie de senos**.
>
> **(b) Extremos aislados (flujo nulo) — Neumann.**
> $$u_x(0,t)=0,\qquad u_x(L,t)=0.$$
> Ahora $X'(0)=X'(L)=0$ y las autofunciones son
> $$X_n(x)=\cos\!\Big(\frac{n\pi x}{L}\Big),\qquad \lambda_n=\Big(\frac{n\pi}{L}\Big)^2,\quad n=0,1,2,\dots$$
> Aparece una **serie de cosenos** e incluye el modo **constante** $n=0$: con extremos aislados el
> calor total se conserva y la barra tiende a su **temperatura media**, mientras que con Dirichlet
> tiende a $0$. La **misma** EDP da problemas de autovalores **distintos** según la condición de
> frontera.

---

## En qué consiste

> [!teoria] Significado físico de cada condición
> - **Dirichlet** ($u=g$): se **prescribe el estado** en el borde — la temperatura del extremo, la
>   posición fija de una cuerda atada, el potencial de un conductor.
> - **Neumann** ($\partial u/\partial n=g$): se **prescribe el flujo** que cruza el borde — flujo de
>   calor; el caso $g=0$ es un borde **aislado** (cuerda con extremo libre, pared adiabática).
> - **Robin** ($\alpha u+\beta\,\partial u/\partial n=g$): modela un **intercambio convectivo** con
>   el entorno (ley de enfriamiento de Newton): el flujo depende de la diferencia entre $u$ y la
>   temperatura ambiente.
> - **Periódicas**: el dominio "se cierra" sobre sí mismo (anillo, ángulo en coordenadas polares).
>
> La **derivada normal** $\partial u/\partial n=\nabla u\cdot \mathbf{n}$ apunta hacia fuera del
> dominio; por eso Neumann es literalmente "cuánto sale por el borde".

> [!proposicion] Qué condición acompaña a cada tipo de EDP
> | Tipo | Condiciones típicas | Problema bien planteado |
> |---|---|---|
> | **Hiperbólica** (onda) | **Cauchy** ($u,u_t$ en $t=0$) + frontera | sí |
> | **Parabólica** (calor) | **inicial** ($u$ en $t=0$) + frontera | sí |
> | **Elíptica** (Laplace) | **solo de frontera** (Dirichlet / Neumann / Robin) | sí |
>
> Cruzar las columnas —p. ej. dar **Cauchy** a una elíptica— produce un problema **mal planteado**
> (ver [[Problemas Bien Planteados| problemas bien planteados]]).

> [!algoritmo] Elegir las condiciones de un problema
> 1. **Clasifica** la EDP (tipo) y mira su orden en el tiempo.
> 2. Si hay evolución temporal: añade **condiciones iniciales** ($u$, y también $u_t$ si es de
>    segundo orden en $t$).
> 3. Sobre el borde espacial: elige Dirichlet (valor), Neumann (flujo) o Robin (intercambio) según
>    la física.
> 4. Verifica que el conjunto sea **bien planteado** para ese tipo (tabla de arriba).

> [!warning]
> En **Neumann puro** (flujo prescrito en todo el borde) para Laplace/Poisson, la solución es única
> **solo salvo una constante aditiva**, y existe únicamente si el flujo total cumple una condición de
> **compatibilidad** ($\oint_{\partial\Omega}\partial u/\partial n\,ds=$ fuente total). Es un caso de
> unicidad/existencia "al filo" del criterio de Hadamard.

## Resumen

> [!resumen]
> | Condición | Forma | Fija físicamente | Autofunciones (barra) |
> |---|---|---|---|
> | Inicial / Cauchy | $u(x,0)=f$, $u_t(x,0)=g$ | estado de partida | — |
> | Dirichlet | $u=g$ en $\partial\Omega$ | valor en el borde | senos |
> | Neumann | $\partial u/\partial n=g$ | flujo en el borde | cosenos |
> | Robin | $\alpha u+\beta\,\partial u/\partial n=g$ | intercambio convectivo | mixtas |
> | Periódicas | igualdad en bordes opuestos | dominio cerrado | senos y cosenos |

> [!corolario]
> Las condiciones no son un añadido cosmético: **definen** el problema tanto como la EDP. Una misma
> ecuación con Dirichlet o con Neumann da espectros distintos (senos vs cosenos) y soluciones de
> equilibrio distintas (tiende a $0$ vs a la media). Casar el tipo de EDP con la condición correcta
> es lo que garantiza un problema **bien planteado**.

> [!referencia]
> - Por qué la condición debe casar con el tipo: [[Problemas Bien Planteados]].
> - De dónde sale el tipo: [[Clasificacion Segundo Orden]].
> - Cómo las condiciones generan autovalores: [[Tecnica de Separacion]].
> - Marco general: [[Fundamentos/index]].
