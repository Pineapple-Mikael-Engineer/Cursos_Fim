---
title: Formas Canónicas
tags:
  - ecuaciones
  - edp
  - teoria
  - fundamentos
  - formas-canonicas
draft: false
aliases:
  - formas canónicas EDP
  - curvas características
  - reducción a forma canónica
  - canonical forms of PDEs
  - characteristic curves
---

# Formas Canónicas de EDP de Segundo Orden

> [!definicion]
> Toda EDP lineal de segundo orden $A\,u_{xx}+B\,u_{xy}+C\,u_{yy}+\dots=0$ se puede llevar, mediante
> un **cambio de variables** $\xi=\xi(x,y),\ \eta=\eta(x,y)$, a una de tres **formas canónicas** en
> que la **parte principal** queda lo más simple posible:
> $$\text{hiperbólica}\ \ u_{\xi\eta}=\dots\quad(\text{o }u_{\sigma\sigma}-u_{\tau\tau}=\dots),\qquad
> \text{parabólica}\ \ u_{\eta\eta}=\dots,\qquad
> \text{elíptica}\ \ u_{\xi\xi}+u_{\eta\eta}=\dots.$$
> Las nuevas coordenadas se eligen **constantes a lo largo de las curvas características** de la
> ecuación.

> [!info]
> Continúa la [[Clasificacion Segundo Orden| clasificación]]: una vez conocido el tipo, la forma
> canónica lo reduce a su **prototipo** (onda, calor, Laplace) y muchas veces lo deja resoluble por
> integración directa. Es el puente con el [[Metodo de las Caracteristicas| método de las características]] y con la [[Solucion de dAlembert| solución de d'Alembert]] de la ecuación de
> onda.

---

## Ejemplo

> [!ejemplo] Hiperbólica → forma de d'Alembert
> **$u_{xx}-u_{yy}=0$.** Aquí $A=1,\ B=0,\ C=-1$, así $\Delta=B^2-4AC=4>0$: **hiperbólica**. La EDO
> característica $A\,dy^2-B\,dx\,dy+C\,dx^2=0$ se reduce a $dy^2-dx^2=0$, es decir
> $$\frac{dy}{dx}=\pm1\ \Longrightarrow\ y=x+\text{cte},\quad y=-x+\text{cte}.$$
> Las dos familias de características son $x-y=\text{cte}$ y $x+y=\text{cte}$. Tomamos coordenadas
> **constantes sobre ellas**:
> $$\xi=x+y,\qquad \eta=x-y.$$
> Aplicando la regla de la cadena ($u_{xx}=u_{\xi\xi}+2u_{\xi\eta}+u_{\eta\eta}$,
> $u_{yy}=u_{\xi\xi}-2u_{\xi\eta}+u_{\eta\eta}$), la ecuación pasa a
> $$u_{xx}-u_{yy}=4\,u_{\xi\eta}=0\ \Longrightarrow\ u_{\xi\eta}=0.$$
> Integrando (como en $u_{xy}=0$): $u=F(\xi)+G(\eta)=F(x+y)+G(x-y)$ — ¡exactamente la
> [[Solucion de dAlembert| solución de d'Alembert]] de la ecuación de onda!

> [!ejemplo] Parabólica → una sola característica
> **$u_{xx}+2u_{xy}+u_{yy}=0$.** Ahora $A=1,\ B=2,\ C=1$, luego $\Delta=4-4=0$: **parabólica**. La
> EDO característica $dy^2-2\,dx\,dy+dx^2=(dy-dx)^2=0$ da una **característica doble**:
> $$\frac{dy}{dx}=\frac{B}{2A}=1\ \Longrightarrow\ y-x=\text{cte}.$$
> Tomamos $\xi=y-x$ (constante en la característica) y como segunda coordenada **independiente** una
> cualquiera, digamos $\eta=y$. Sustituyendo, los términos en $u_{\xi\xi}$ y $u_{\xi\eta}$ se cancelan
> y queda
> $$u_{\eta\eta}=0,$$
> la forma canónica parabólica. Su solución general es $u=\eta\,P(\xi)+Q(\xi)=y\,P(y-x)+Q(y-x)$.

---

## En qué consiste

> [!teoria] De dónde sale la EDO característica
> Buscamos un cambio $\xi,\eta$ tal que desaparezca algún término de orden 2. Al transformar la
> parte principal, el nuevo coeficiente de $u_{\xi\xi}$ resulta ser
> $$A\,\xi_x^2+B\,\xi_x\xi_y+C\,\xi_y^2.$$
> Anularlo equivale a pedir que las curvas $\xi=\text{cte}$ —cuyas pendientes cumplen
> $dy/dx=-\xi_x/\xi_y$— satisfagan $A\,dy^2-B\,dx\,dy+C\,dx^2=0$. Resolviendo esta cuadrática en
> $dy/dx$:
> $$\frac{dy}{dx}=\frac{B\pm\sqrt{B^2-4AC}}{2A}.$$
> El **signo del discriminante** decide cuántas familias reales hay: **dos** si $\Delta>0$
> (hiperbólica), **una doble** si $\Delta=0$ (parabólica), **ninguna real / complejas conjugadas**
> si $\Delta<0$ (elíptica). Por eso el tipo y la forma canónica son dos caras de lo mismo.

> [!proposicion] Caso elíptico: características complejas
> Si $\Delta<0$, las raíces $dy/dx=(B\pm i\sqrt{4AC-B^2})/2A$ son **complejas conjugadas**. Sus
> "características" $\phi(x,y)=\alpha(x,y)\pm i\,\beta(x,y)=\text{cte}$ no son curvas reales; al tomar
> $\xi=\alpha,\ \eta=\beta$ (parte real e imaginaria) la parte principal se reduce a
> $u_{\xi\xi}+u_{\eta\eta}=\dots$, la forma de **Laplace**. Es la razón profunda de que las EDP
> elípticas se comporten como problemas de equilibrio: **no** tienen direcciones reales de
> propagación.

> [!algoritmo] Reducir una EDP a forma canónica
> 1. **Clasifica**: calcula $\Delta=B^2-4AC$ y determina el tipo.
> 2. Resuelve la **EDO característica** $\dfrac{dy}{dx}=\dfrac{B\pm\sqrt{B^2-4AC}}{2A}$.
> 3. Toma $\xi,\eta$ **constantes sobre las características** (hiperbólica: las dos familias;
>    parabólica: la familia doble como $\xi$ y una segunda coordenada independiente como $\eta$;
>    elíptica: partes real e imaginaria).
> 4. Reescribe la EDP con la regla de la cadena: aparece la forma canónica del tipo.

> [!warning]
> En el caso **parabólico** solo hay una familia de características; la segunda coordenada $\eta$ debe
> elegirse **independiente** de $\xi$ (jacobiano $\neq0$). Una mala elección degenera el cambio de
> variable y no produce forma canónica.

## Resumen

> [!resumen]
> | Tipo | $\Delta$ | Características | Forma canónica |
> |:--|:--:|:--|:--|
> | Hiperbólica | $>0$ | dos familias reales | $u_{\xi\eta}=\dots$ o $u_{\sigma\sigma}-u_{\tau\tau}=\dots$ |
> | Parabólica | $=0$ | una familia (doble) | $u_{\eta\eta}=\dots$ |
> | Elíptica | $<0$ | complejas conjugadas | $u_{\xi\xi}+u_{\eta\eta}=\dots$ |

> [!corolario]
> Las **características** son el esqueleto geométrico de la EDP: las curvas a lo largo de las cuales
> "viaja" la información. Alinearse con ellas (forma canónica) convierte una ecuación complicada en
> uno de tres prototipos conocidos; en el caso hiperbólico, esa alineación **es** la solución de
> d'Alembert.

> [!referencia]
> - Cómo se obtiene el tipo y el discriminante: [[Clasificacion Segundo Orden]].
> - Las características como método de resolución: [[Metodo de las Caracteristicas]].
> - El prototipo hiperbólico resuelto: [[Solucion de dAlembert]].
> - Marco de la sección: [[Fundamentos/index]].
