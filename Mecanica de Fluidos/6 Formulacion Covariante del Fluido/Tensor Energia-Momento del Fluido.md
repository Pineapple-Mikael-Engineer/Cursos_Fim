---
title: Tensor Energía-Momento del Fluido
tags:
  - fluidos
  - teoria
  - covariante
draft: false
aliases:
  - Tensor energía-momento del fluido
  - Fluido perfecto relativista
  - T^μν del fluido
---

# Tensor Energía-Momento del Fluido $T^{\mu\nu}=(\varepsilon+p)\dfrac{u^\mu u^\nu}{c^2}-p\,\eta^{\mu\nu}$

> [!definicion]
> El **tensor energía-momento** $T^{\mu\nu}$ de un **fluido perfecto** es el objeto tensorial de rango 2 que reúne, en el espaciotiempo de Minkowski, la **densidad de energía**, el **flujo de momento** y la **presión** del fluido. Para un fluido perfecto (sin viscosidad ni conducción de calor) vale
> $$T^{\mu\nu}=(\varepsilon+p)\,\dfrac{u^\mu u^\nu}{c^2}-p\,\eta^{\mu\nu},$$
> donde $\varepsilon$ es la **densidad de energía propia** (medida en el marco que se mueve con el fluido), $p$ la **presión**, $u^\mu=\gamma(c,\vec v)$ la **cuadrivelocidad** y $\eta_{\mu\nu}=\mathrm{diag}(+1,-1,-1,-1)$ la métrica. Es **simétrico**, $T^{\mu\nu}=T^{\nu\mu}$, y su conservación $\partial_\mu T^{\mu\nu}=0$ contiene toda la dinámica del fluido.

---

> [!info]
> Nota central de la sección [[6 Formulacion Covariante del Fluido/index | Formulación Covariante del Fluido]]. Es la pieza que conecta sus hermanas: el puente clásico [[Flujo Compresible y Ondas de Choque]] (cuando $U\to c$ la energía deja de desacoplarse) y la dinámica [[Hidrodinamica Relativista]] (que sale de proyectar $\partial_\mu T^{\mu\nu}=0$). Es el **análogo** del [[Tensor Energia-Momento | tensor energía-momento del campo EM]]: la misma maquinaria de índices, pero la fuente ahora es el fluido en vez del campo.
> **Convenio.** Métrica $\eta_{\mu\nu}=\mathrm{diag}(+1,-1,-1,-1)$; cuadrivelocidad $u^\mu=\gamma(c,\vec v)$ con $u_\mu u^\mu=c^2$; índices griegos $0\!-\!3$, latinos $1\!-\!3$; suma de Einstein. Fuente: **Landau-Lifshitz Vol. 6** §133 y **Vol. 2** (*Teoría Clásica de Campos*).

---

## La cuadrivelocidad y su normalización

> [!teoria] La cuadrivelocidad $u^\mu$
> La **cuadrivelocidad** es la derivada de la posición $x^\mu=(ct,\vec x)$ respecto al **tiempo propio** $\tau$ (el medido por un reloj que viaja con el fluido). Como $dt=\gamma\,d\tau$, con $\gamma=(1-v^2/c^2)^{-1/2}$:
> $$u^\mu=\frac{dx^\mu}{d\tau}=\frac{dx^\mu}{dt}\frac{dt}{d\tau}=\gamma\,\frac{d}{dt}(ct,\vec x)=\gamma\,(c,\vec v).$$
> Sus componentes son $u^0=\gamma c$ y $u^i=\gamma v^i$. A diferencia de la velocidad ordinaria $\vec v$, esta es un **cuadrivector** que transforma covariantemente bajo Lorentz.

> [!proposicion] Normalización $u_\mu u^\mu=c^2$
> La cuadrivelocidad tiene **norma constante** $c^2$.
>
> **Demostración.**
>
> **Paso 1 —** Bajamos un índice con la métrica: $u_\mu=\eta_{\mu\nu}u^\nu$. Componente temporal $u_0=\eta_{00}u^0=(+1)\gamma c=\gamma c$; componentes espaciales $u_i=\eta_{ij}u^j=(-\delta_{ij})\gamma v^j=-\gamma v^i$.
>
> **Paso 2 —** Contraemos $u_\mu u^\mu$ sumando sobre $\mu=0,1,2,3$:
> $$u_\mu u^\mu=u_0u^0+u_iu^i=(\gamma c)(\gamma c)+(-\gamma v^i)(\gamma v^i)=\gamma^2c^2-\gamma^2 v^2.$$
>
> **Paso 3 —** Factorizamos $\gamma^2$ y usamos su definición:
> $$u_\mu u^\mu=\gamma^2(c^2-v^2)=\frac{c^2-v^2}{1-v^2/c^2}=\frac{c^2(1-v^2/c^2)}{1-v^2/c^2}=c^2.$$
> $\blacksquare$
>
> Esta identidad $u_\mu u^\mu=c^2$ es la **piedra angular** de todos los cálculos que siguen: aparece al evaluar la traza, al construir el proyector y al proyectar $\partial_\mu T^{\mu\nu}=0$.

---

## El tensor del fluido perfecto

> [!definicion] $T^{\mu\nu}$ del fluido perfecto
> $$\boxed{\,T^{\mu\nu}=(\varepsilon+p)\,\dfrac{u^\mu u^\nu}{c^2}-p\,\eta^{\mu\nu}\,}$$
> El primer término $\propto u^\mu u^\nu$ transporta energía y momento **a lo largo** del flujo; el segundo $-p\,\eta^{\mu\nu}$ inyecta la **presión isótropa**. La combinación $\varepsilon+p$ es la **entalpía** por unidad de volumen propio, la cantidad que efectivamente "se mueve" con el fluido relativista.

> [!proposicion] Simetría
> $T^{\mu\nu}=T^{\nu\mu}$.
>
> **Demostración.** El producto de cuadrivelocidades es simétrico, $u^\mu u^\nu=u^\nu u^\mu$ (números que conmutan), y la métrica es simétrica, $\eta^{\mu\nu}=\eta^{\nu\mu}$. Por tanto
> $$T^{\nu\mu}=(\varepsilon+p)\frac{u^\nu u^\mu}{c^2}-p\,\eta^{\nu\mu}=(\varepsilon+p)\frac{u^\mu u^\nu}{c^2}-p\,\eta^{\mu\nu}=T^{\mu\nu}.\qquad\blacksquare$$
> La simetría es la que permite interpretar $T^{0i}$ a la vez como densidad de momento ($T^{i0}/c$) y como flujo de energía ($T^{0i}$).

![[tensor_T_fluido.svg|460]]
*El tensor energía-momento del fluido perfecto. En el marco en reposo es la matriz diagonal $\mathrm{diag}(\varepsilon,p,p,p)$: la esquina temporal guarda la densidad de energía $\varepsilon$ y la diagonal espacial la presión isótropa $p$. Toda la dinámica del fluido vive en $\partial_\mu T^{\mu\nu}=0$.*

---

## Componentes en el marco en reposo

> [!teorema] En reposo $T^{\mu\nu}=\mathrm{diag}(\varepsilon,p,p,p)$
> En el **marco comóvil** (el que viaja con el fluido) la velocidad ordinaria es $\vec v=\vec 0$, luego $\gamma=1$ y la cuadrivelocidad se reduce a $u^\mu=(c,\vec 0)$, es decir $u^0=c$, $u^i=0$. Evaluamos cada bloque de $T^{\mu\nu}$ por separado.
>
> **Demostración.**
>
> **Paso 1 — Componente $T^{00}$ (densidad de energía).** Con $u^0=c$ y $\eta^{00}=+1$:
> $$T^{00}=(\varepsilon+p)\frac{u^0u^0}{c^2}-p\,\eta^{00}=(\varepsilon+p)\frac{c\cdot c}{c^2}-p(+1)=(\varepsilon+p)-p=\varepsilon.$$
> La esquina temporal es la **densidad de energía** $\varepsilon$.
>
> **Paso 2 — Componentes $T^{0i}$ (flujo de momento/energía).** Como $u^i=0$ y $\eta^{0i}=0$ (la métrica es diagonal):
> $$T^{0i}=(\varepsilon+p)\frac{u^0u^i}{c^2}-p\,\eta^{0i}=(\varepsilon+p)\frac{c\cdot 0}{c^2}-p\cdot 0=0.$$
> En reposo **no hay flujo neto** de energía ni momento.
>
> **Paso 3 — Componentes $T^{ij}$ (tensor de presiones).** Con $u^i=u^j=0$ y $\eta^{ij}=-\delta_{ij}$:
> $$T^{ij}=(\varepsilon+p)\frac{u^iu^j}{c^2}-p\,\eta^{ij}=(\varepsilon+p)\frac{0}{c^2}-p(-\delta_{ij})=p\,\delta_{ij}.$$
> El bloque espacial es la **presión isótropa**: $p$ en cada dirección, nada fuera de la diagonal (un fluido perfecto no tiene esfuerzos cortantes).
>
> **Paso 4 — Ensamblaje.** Reuniendo los tres bloques:
> $$T^{\mu\nu}\big|_{\text{reposo}}=\begin{pmatrix}\varepsilon & 0 & 0 & 0\\ 0 & p & 0 & 0\\ 0 & 0 & p & 0\\ 0 & 0 & 0 & p\end{pmatrix}=\mathrm{diag}(\varepsilon,p,p,p).$$
> $\blacksquare$
>
> Esta es la **forma canónica** que da intuición a todo lo demás: una sola densidad de energía y una presión repetida tres veces.

---

## El proyector espacial

> [!definicion] Proyector $h^{\mu\nu}$
> Se define el **proyector espacial** (ortogonal a la cuadrivelocidad)
> $$h^{\mu\nu}=\eta^{\mu\nu}-\frac{u^\mu u^\nu}{c^2}.$$
> Su misión es seleccionar las direcciones **perpendiculares** al flujo: separa la parte "temporal" (a lo largo de $u$) de la parte "espacial" (la presión).

> [!lema] $h^{\mu\nu}u_\nu=0$
> El proyector aniquila la cuadrivelocidad.
>
> **Demostración.**
>
> **Paso 1 —** Contraemos $h^{\mu\nu}$ con $u_\nu$, término a término:
> $$h^{\mu\nu}u_\nu=\eta^{\mu\nu}u_\nu-\frac{u^\mu u^\nu}{c^2}u_\nu.$$
>
> **Paso 2 —** El primer término sube el índice: $\eta^{\mu\nu}u_\nu=u^\mu$. En el segundo aparece la contracción $u^\nu u_\nu=u_\nu u^\nu=c^2$ (la normalización demostrada arriba):
> $$h^{\mu\nu}u_\nu=u^\mu-\frac{u^\mu}{c^2}\,(u^\nu u_\nu)=u^\mu-\frac{u^\mu}{c^2}\,c^2=u^\mu-u^\mu=0.\qquad\blacksquare$$
>
> Geométricamente, $h^{\mu\nu}$ proyecta cualquier cuadrivector sobre el **subespacio espacial** del marco comóvil: lo que es paralelo a $u$ se elimina.

> [!proposicion] Forma con el proyector
> El tensor del fluido perfecto se reescribe como
> $$T^{\mu\nu}=\frac{\varepsilon}{c^2}\,u^\mu u^\nu-p\,h^{\mu\nu}.$$
>
> **Demostración.**
>
> **Paso 1 —** Partimos de la definición y reagrupamos el coeficiente del término $u^\mu u^\nu$:
> $$T^{\mu\nu}=(\varepsilon+p)\frac{u^\mu u^\nu}{c^2}-p\,\eta^{\mu\nu}=\frac{\varepsilon}{c^2}u^\mu u^\nu+\frac{p}{c^2}u^\mu u^\nu-p\,\eta^{\mu\nu}.$$
>
> **Paso 2 —** Sacamos $-p$ como factor común de los dos últimos términos:
> $$\frac{p}{c^2}u^\mu u^\nu-p\,\eta^{\mu\nu}=-p\left(\eta^{\mu\nu}-\frac{u^\mu u^\nu}{c^2}\right)=-p\,h^{\mu\nu}.$$
>
> **Paso 3 —** Sustituyendo:
> $$T^{\mu\nu}=\frac{\varepsilon}{c^2}\,u^\mu u^\nu-p\,h^{\mu\nu}.\qquad\blacksquare$$
>
> **Interpretación.** El término $\dfrac{\varepsilon}{c^2}u^\mu u^\nu$ proyecta la **energía a lo largo** del flujo; el término $-p\,h^{\mu\nu}$ aporta la **presión en las direcciones espaciales** (justo donde $h^{\mu\nu}$ es no nulo). La descomposición separa limpiamente "lo que fluye" de "lo que empuja".

---

## La traza

> [!teorema] Traza $T^\mu{}_\mu=\varepsilon-3p$
> La traza del tensor es la diferencia entre densidad de energía y tres veces la presión.
>
> **Demostración.**
>
> **Paso 1 —** La traza se obtiene contrayendo con la métrica, $T^\mu{}_\mu=\eta_{\mu\nu}T^{\mu\nu}$. Aplicamos $\eta_{\mu\nu}$ a la definición:
> $$T^\mu{}_\mu=\eta_{\mu\nu}\left[(\varepsilon+p)\frac{u^\mu u^\nu}{c^2}-p\,\eta^{\mu\nu}\right]=(\varepsilon+p)\frac{\eta_{\mu\nu}u^\mu u^\nu}{c^2}-p\,\eta_{\mu\nu}\eta^{\mu\nu}.$$
>
> **Paso 2 —** El primer factor usa de nuevo la normalización: $\eta_{\mu\nu}u^\mu u^\nu=u_\nu u^\nu=c^2$.
>
> **Paso 3 —** El segundo factor es la **traza de la métrica**, $\eta_{\mu\nu}\eta^{\mu\nu}=\eta^\mu{}_\mu=\delta^\mu{}_\mu=4$ (suma de los cuatro unos de la delta en cuatro dimensiones).
>
> **Paso 4 —** Sustituyendo ambos resultados:
> $$T^\mu{}_\mu=(\varepsilon+p)\frac{c^2}{c^2}-p\cdot 4=(\varepsilon+p)-4p=\varepsilon-3p.\qquad\blacksquare$$
>
> **Comprobación** con la forma diagonal del marco en reposo: $T^\mu{}_\mu=\eta_{\mu\nu}\mathrm{diag}(\varepsilon,p,p,p)=(+1)\varepsilon+(-1)p+(-1)p+(-1)p=\varepsilon-3p$. Coincide.

> [!corolario] Traza nula del fluido ultrarrelativista
> Para un **fluido de radiación** (gas de fotones, plasma ultrarrelativista) la ecuación de estado es $p=\varepsilon/3$. Entonces
> $$T^\mu{}_\mu=\varepsilon-3p=\varepsilon-3\cdot\frac{\varepsilon}{3}=\varepsilon-\varepsilon=0.$$
> La **traza se anula**, exactamente como en el [[Tensor Energia-Momento | tensor energía-momento del campo EM]] ($T^\mu{}_\mu=0$). No es casualidad: ambos describen materia "sin masa en reposo", invariante de escala.

---

## Límite no relativista

> [!teorema] Recuperación de las cantidades clásicas
> En el límite $v\ll c$, escribiendo la densidad de energía como $\varepsilon\approx\rho c^2$ (la **energía en reposo** domina sobre la interna y la presión), el tensor reproduce las densidades clásicas de masa-energía y de momento.
>
> **Demostración.**
>
> **Paso 1 — Componente $T^{00}$.** Para velocidad $\vec v$ general, $u^0=\gamma c$, $\eta^{00}=+1$:
> $$T^{00}=(\varepsilon+p)\frac{u^0u^0}{c^2}-p\,\eta^{00}=(\varepsilon+p)\frac{\gamma^2c^2}{c^2}-p=(\varepsilon+p)\gamma^2-p.$$
> En el límite $v\ll c$ tenemos $\gamma\to 1$, y como $p\ll\varepsilon\approx\rho c^2$:
> $$T^{00}\to(\varepsilon+p)-p=\varepsilon\approx\rho c^2.$$
> Recuperamos la **densidad de masa-energía** $\rho c^2$.
>
> **Paso 2 — Componente $T^{0i}$.** Con $u^0=\gamma c$, $u^i=\gamma v^i$ y $\eta^{0i}=0$:
> $$T^{0i}=(\varepsilon+p)\frac{u^0u^i}{c^2}-p\,\eta^{0i}=(\varepsilon+p)\frac{\gamma c\cdot\gamma v^i}{c^2}=(\varepsilon+p)\gamma^2\frac{v^i}{c}.$$
> En el límite $\gamma\to 1$, $\varepsilon+p\to\rho c^2$:
> $$T^{0i}\to\rho c^2\,\frac{v^i}{c}=\rho c\,v^i\quad\Longrightarrow\quad \frac{T^{0i}}{c}\to\rho\,v^i.$$
> El cociente $T^{0i}/c$ es la **densidad de momento** clásica $\rho v^i$. $\blacksquare$
>
> **Lectura.** El bloque temporal $T^{00}$ es la densidad de energía; el bloque mixto $T^{0i}/c$ es la densidad de momento. La **presión** $p\ll\rho c^2$ es, en este régimen, una pequeña corrección relativista: en la mecánica clásica de fluidos contribuye al flujo de momento, pero no a la densidad de masa-energía dominante.

---

## Ejemplo

> [!ejemplo] Fluido en movimiento con $\vec v=v\,\hat x$ y gas de fotones
> **(a)** Un fluido se mueve con velocidad $\vec v=v\,\hat x$ a lo largo del eje $x$. Su tensor es el **boost** del de reposo. Calculemos $T^{00}$ y $T^{0x}$ mostrando los factores $\gamma$.
>
> **Solución (a).** La cuadrivelocidad es $u^\mu=\gamma(c,v,0,0)$, esto es $u^0=\gamma c$, $u^1=u^x=\gamma v$, $u^2=u^3=0$.
>
> **Paso 1 — $T^{00}$.** Igual que en el límite, pero sin aproximar:
> $$T^{00}=(\varepsilon+p)\frac{u^0u^0}{c^2}-p\,\eta^{00}=(\varepsilon+p)\frac{\gamma^2c^2}{c^2}-p(+1)=(\varepsilon+p)\gamma^2-p.$$
> La densidad de energía vista en el laboratorio es **mayor** que $\varepsilon$ por el factor $\gamma^2$ (un efecto relativista: a la energía propia se suma la energía cinética del flujo).
>
> **Paso 2 — $T^{0x}$.** Con $u^0=\gamma c$, $u^x=\gamma v$ y $\eta^{0x}=0$:
> $$T^{0x}=(\varepsilon+p)\frac{u^0u^x}{c^2}-p\,\eta^{0x}=(\varepsilon+p)\frac{\gamma c\cdot\gamma v}{c^2}=(\varepsilon+p)\gamma^2\frac{v}{c}.$$
> Hay **flujo de energía** en la dirección $x$, proporcional a la entalpía $\varepsilon+p$ y a $\gamma^2 v/c$.
>
> **(b)** Un **gas de fotones** (radiación) tiene la ecuación de estado $p=\varepsilon/3$. Su tensor, en reposo, es
> $$T^{\mu\nu}=\mathrm{diag}\!\left(\varepsilon,\tfrac{\varepsilon}{3},\tfrac{\varepsilon}{3},\tfrac{\varepsilon}{3}\right),\qquad T^\mu{}_\mu=\varepsilon-3\cdot\frac{\varepsilon}{3}=0.$$
> La **traza nula** lo identifica como fluido sin masa en reposo, idéntico en esto al campo electromagnético. Es el tensor que rige la presión de radiación en el interior estelar y la dinámica del universo dominado por radiación.

---

## En qué consiste

> [!teoria] El significado físico, bloque a bloque
> El tensor $T^{\mu\nu}$ es una **matriz $4\times 4$** que empaqueta toda la energía y el momento del fluido. La regla mnemotécnica de sus bloques:
>
> - $T^{00}$ = densidad de **energía** (en reposo, $\varepsilon$).
> - $T^{0i}=T^{i0}$ = densidad de **flujo de energía** / densidad de **momento** ($T^{i0}/c$). En reposo son nulos.
> - $T^{ij}$ = **flujo de momento** = tensor de esfuerzos. Para el fluido perfecto es $p\,\delta_{ij}$: presión isótropa, sin cortantes.
>
> La estructura $(\varepsilon+p)u^\mu u^\nu/c^2-p\,\eta^{\mu\nu}$ es la **única** combinación de $u^\mu$ y $\eta^{\mu\nu}$ que (i) es simétrica, (ii) reproduce $\mathrm{diag}(\varepsilon,p,p,p)$ en reposo y (iii) es covariante Lorentz. Toda la mecánica de fluidos relativista se reduce a imponer su conservación $\partial_\mu T^{\mu\nu}=0$, de donde —proyectando a lo largo y perpendicular a $u$— salen la continuidad y el Euler relativistas que se desarrollan en [[Hidrodinamica Relativista]].

> [!warning] Tres advertencias sobre $\varepsilon$ y el fluido perfecto
> 1. **$\varepsilon$ es la densidad de energía en el marco propio** (comóvil), no en el del laboratorio. Por eso al boostear aparece $T^{00}=(\varepsilon+p)\gamma^2-p\neq\varepsilon$: el laboratorio mide más energía por el movimiento.
> 2. **$\varepsilon$ incluye la energía en reposo** $\rho c^2$ **más** la energía interna del fluido. En el límite no relativista $\varepsilon\approx\rho c^2$ porque la energía en reposo domina ampliamente.
> 3. **"Perfecto" significa sin viscosidad ni conducción de calor.** Un fluido real añade términos disipativos a $T^{\mu\nu}$ (el análogo covariante del tensor de esfuerzos viscoso $\tau_{ij}$ clásico y del flujo de calor), que rompen la forma diagonal $\mathrm{diag}(\varepsilon,p,p,p)$ del marco en reposo.

---

## Resumen

> [!resumen]
> | Magnitud | Expresión | Significado |
> |:---|:---|:---|
> | Cuadrivelocidad | $u^\mu=\gamma(c,\vec v)$, $u_\mu u^\mu=c^2$ | tiempo propio + movimiento |
> | Tensor del fluido | $T^{\mu\nu}=(\varepsilon+p)\dfrac{u^\mu u^\nu}{c^2}-p\,\eta^{\mu\nu}$ | energía + momento + presión |
> | Forma con proyector | $T^{\mu\nu}=\dfrac{\varepsilon}{c^2}u^\mu u^\nu-p\,h^{\mu\nu}$ | energía $\parallel u$ + presión $\perp u$ |
> | Proyector | $h^{\mu\nu}=\eta^{\mu\nu}-\dfrac{u^\mu u^\nu}{c^2}$, $h^{\mu\nu}u_\nu=0$ | selecciona lo espacial |
> | En reposo | $T^{\mu\nu}=\mathrm{diag}(\varepsilon,p,p,p)$ | $\varepsilon$ y presión isótropa |
> | Traza | $T^\mu{}_\mu=\varepsilon-3p$ | $=0$ si $p=\varepsilon/3$ |
> | Límite $v\ll c$ | $T^{00}\to\rho c^2$, $T^{0i}/c\to\rho v_i$ | masa-energía + momento clásicos |
>
> **Notación.** $\varepsilon$ densidad de energía propia, $p$ presión, $\rho$ densidad de masa en reposo, $\gamma=(1-v^2/c^2)^{-1/2}$, $\eta_{\mu\nu}=\mathrm{diag}(+1,-1,-1,-1)$.

> [!corolario] Lo esencial
> El fluido perfecto relativista se describe **por completo** con un único tensor simétrico $T^{\mu\nu}$ construido a partir de dos escalares ($\varepsilon$, $p$) y la cuadrivelocidad $u^\mu$. En el marco en reposo se reduce a $\mathrm{diag}(\varepsilon,p,p,p)$; su traza $\varepsilon-3p$ distingue materia ordinaria de radiación ($p=\varepsilon/3$, traza nula); y su conservación $\partial_\mu T^{\mu\nu}=0$ —tratada en [[Hidrodinamica Relativista]]— genera la dinámica completa, reduciéndose a Euler y continuidad cuando $v\ll c$. En relatividad general, este $T^{\mu\nu}$ es la **fuente** del campo gravitatorio.

> [!referencia]
> Landau-Lifshitz, Vol. 6 (*Mecánica de Fluidos*), §133 ("Hidrodinámica relativista"); Vol. 2 (*Teoría Clásica de Campos*) para el aparato tensorial y el análogo del campo electromagnético. Weinberg, *Gravitation and Cosmology*, cap. 2, §10, para $T^{\mu\nu}$ del fluido perfecto como fuente de la gravedad.
