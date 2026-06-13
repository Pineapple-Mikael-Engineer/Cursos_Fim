---
title: Soluciones Viscosas Exactas
tags:
  - fluidos
  - teoria
  - flujo-viscoso
draft: false
aliases:
  - Soluciones viscosas exactas
  - Flujo de Couette
  - Flujo de Poiseuille
---

# Soluciones Viscosas Exactas $u(y)=\dfrac{U y}{h}\ \text{(Couette)},\quad u\propto\left(\dfrac{h^2}{4}-y^2\right)\ \text{(Poiseuille)}$

> [!definicion]
> Las **soluciones viscosas exactas** son las pocas situaciones en que las [[Ecuaciones de Navier-Stokes]] completas —no linealizadas, no aproximadas— se resuelven **analíticamente y sin error**. Todas comparten la misma geometría privilegiada: un **flujo unidireccional, completamente desarrollado y estacionario**,
> $$\vec v=\big(u(y),\,0,\,0\big),$$
> en el que el término convectivo $(\vec v\cdot\nabla)\vec v$ —la pieza no lineal que normalmente impide resolver Navier–Stokes— **se anula idénticamente**. Lo que queda es una EDO lineal en $u$. Los dos arquetipos son el **flujo de Couette** (arrastre entre placas, perfil **lineal**) y el **flujo de Poiseuille** (gradiente de presión, perfil **parabólico**), con su versión cilíndrica de **Hagen–Poiseuille** y su célebre **ley $R^4$**.

---

> [!info]
> **Nota de la sección [[5 Flujo Viscoso/index | Flujo Viscoso]] (Capítulo 5).** Aquí explotamos los casos en que la viscosidad domina o convive con un gradiente de presión sin que la no linealidad estorbe.
> **Hermanas.** [[Numero de Reynolds y Adimensionalizacion]] (cuándo el flujo sigue siendo laminar y, por tanto, estas soluciones valen) y [[Capa Limite]] (qué ocurre cuando el flujo **no** está plenamente desarrollado).
> **Usa.** Las [[Ecuaciones de Navier-Stokes]] del [[3 Ecuaciones de Conservacion/index | Capítulo 3]].
> **Referencia.** Landau-Lifshitz, Vol. 6, §17 (flujo entre placas y por tubería); Batchelor §4.2; White, *Viscous Fluid Flow*, cap. 3.

---

## Ejemplo

> [!ejemplo] Caudal de aceite por una tubería y esfuerzo en un Couette
> **(a) Hagen–Poiseuille.** Por una tubería horizontal de radio $R=5\ \text{mm}=5\times10^{-3}\ \text{m}$ y longitud $L=2\ \text{m}$ circula aceite de viscosidad $\mu=0{,}1\ \text{Pa·s}$ impulsado por una diferencia de presión $\Delta p=4000\ \text{Pa}$. Hallar el caudal $Q$.
>
> Aplicamos la ley de Hagen–Poiseuille (demostrada abajo):
> $$Q=\frac{\pi R^4\,\Delta p}{8\mu L}.$$
> Calculamos $R^4=(5\times10^{-3})^4=6{,}25\times10^{-10}\ \text{m}^4$. Entonces
> $$Q=\frac{\pi\,(6{,}25\times10^{-10})(4000)}{8\,(0{,}1)(2)}=\frac{\pi\,(2{,}5\times10^{-6})}{1{,}6}\approx4{,}91\times10^{-6}\ \text{m}^3/\text{s}.$$
> Es decir $Q\approx4{,}91\ \text{cm}^3/\text{s}\approx 4{,}91\ \text{mL/s}$.
>
> **Sensibilidad al radio.** Si el radio se duplicara a $R=10\ \text{mm}$, el factor $R^4$ se multiplicaría por $2^4=16$: el caudal saltaría a $\approx78{,}5\ \text{mL/s}$ con la **misma** presión. Esa es la **ley $R^4$**.
>
> **(b) Couette.** Dos placas separadas $h=2\ \text{mm}=2\times10^{-3}\ \text{m}$; la superior se mueve a $U=0{,}5\ \text{m/s}$ sobre el mismo aceite ($\mu=0{,}1\ \text{Pa·s}$). El esfuerzo cortante necesario para arrastrarla es **constante**:
> $$\tau=\mu\,\frac{U}{h}=0{,}1\cdot\frac{0{,}5}{2\times10^{-3}}=25\ \text{Pa}.$$
> La fuerza por unidad de área sobre la placa es $25\ \text{N/m}^2$.

---

## En qué consiste

### Por qué existe la solución exacta

> [!teorema] La no linealidad se anula en flujo unidireccional desarrollado
> Para $\vec v=(u(y),0,0)$ estacionario, las [[Ecuaciones de Navier-Stokes]] incompresibles
> $$\rho\,(\vec v\cdot\nabla)\vec v=-\nabla p+\mu\nabla^2\vec v,\qquad \nabla\cdot\vec v=0,$$
> se reducen a la **EDO lineal**
> $$\boxed{\;\mu\,u''(y)=\frac{\partial p}{\partial x}\;}$$

> [!demostracion]
> **Paso 1 — Continuidad.** Con $\vec v=(u(x,y,z),0,0)$, la incompresibilidad da
> $$\nabla\cdot\vec v=\frac{\partial u}{\partial x}=0\ \Rightarrow\ u\ \text{no depende de}\ x.$$
> Por simetría del problema (placas infinitas, sin variación en $z$) tomamos $u=u(y)$ únicamente.
>
> **Paso 2 — El término convectivo se anula EXACTAMENTE.** El operador convectivo es
> $$(\vec v\cdot\nabla)\vec v=\Big(u\,\frac{\partial}{\partial x}+v\,\frac{\partial}{\partial y}+w\,\frac{\partial}{\partial z}\Big)\vec v.$$
> Como $v=w=0$ y la única componente no nula de $\vec v$ es $u$, solo sobrevive
> $$(\vec v\cdot\nabla)\vec v=u\,\frac{\partial u}{\partial x}\,\hat x=u\cdot 0\,\hat x=\vec 0,$$
> porque $\partial_x u=0$ por el Paso 1. **La pieza no lineal desaparece sin aproximación alguna.**
>
> **Paso 3 — Componente $x$ del momento.** Sin convección ni dependencia temporal, la ecuación en $\hat x$ es
> $$0=-\frac{\partial p}{\partial x}+\mu\Big(\underbrace{\frac{\partial^2 u}{\partial x^2}}_{=0}+\frac{\partial^2 u}{\partial y^2}+\underbrace{\frac{\partial^2 u}{\partial z^2}}_{=0}\Big)=-\frac{\partial p}{\partial x}+\mu\,u''(y).$$
>
> **Paso 4 — Componentes $y$, $z$.** Como $v=w=0$, ellas dan $\partial p/\partial y=0$ y $\partial p/\partial z=0$ (descontando la gravedad hidrostática): la presión solo depende de $x$. Luego en $\mu\,u''(y)=\partial_x p$ el miembro izquierdo depende de $y$ y el derecho de $x$; ambos deben igualar una **constante**. Queda la EDO lineal anunciada. $\blacksquare$

> [!regla] Receta común
> Toda solución exacta de este tipo se obtiene en tres pasos: **(1)** fijar el gradiente de presión $\partial_x p=-G$ (constante); **(2)** integrar dos veces $\mu u''=-G$; **(3)** fijar las dos constantes con la condición de **no deslizamiento** $u=0$ (o $u=U$) en cada pared.

### Flujo de Couette

> [!proposicion] Perfil lineal
> Entre dos placas separadas $h$, con la inferior fija y la superior moviéndose a velocidad $U$, **sin gradiente de presión**, el perfil es lineal:
> $$\boxed{\,u(y)=\frac{U\,y}{h}\,},\qquad 0\le y\le h.$$

> [!demostracion]
> **Paso 1 — EDO.** Sin gradiente de presión, $\partial_x p=0$, de modo que
> $$\mu\,u''(y)=0\ \Rightarrow\ u''(y)=0.$$
>
> **Paso 2 — Integrar.** Integrando dos veces, $u(y)=Ay+B$ (perfil **lineal**).
>
> **Paso 3 — No deslizamiento.** Las condiciones de contorno son $u(0)=0$ (placa fija) y $u(h)=U$ (placa móvil):
> $$u(0)=B=0,\qquad u(h)=Ah=U\ \Rightarrow\ A=\frac{U}{h}.$$
> Por tanto $u(y)=Uy/h$. $\blacksquare$

> [!corolario] Esfuerzo, caudal y velocidad media
> **Esfuerzo cortante** (ley de Newton de la viscosidad, **constante** en todo el canal):
> $$\tau=\mu\,\frac{du}{dy}=\mu\,\frac{U}{h}=\text{const}.$$
> **Caudal por unidad de ancho:**
> $$q=\int_0^h u\,dy=\int_0^h \frac{U y}{h}\,dy=\frac{U}{h}\cdot\frac{h^2}{2}=\frac{U h}{2}.$$
> **Velocidad media:** $\bar u=q/h=U/2$, exactamente la mitad de la velocidad de la placa.

### Flujo de Poiseuille plano

> [!proposicion] Perfil parabólico
> Entre dos placas **fijas** separadas $h$ (con $-h/2\le y\le h/2$) bajo un gradiente de presión favorable $\partial_x p=-G$ (con $G>0$), el perfil es parabólico:
> $$\boxed{\,u(y)=\frac{G}{2\mu}\left(\frac{h^2}{4}-y^2\right)\,},$$
> con máximo en el centro $u_{\max}=\dfrac{G h^2}{8\mu}$.

> [!demostracion]
> **Paso 1 — EDO.** Con $\partial_x p=-G$ constante,
> $$\mu\,u''(y)=-G\ \Rightarrow\ u''(y)=-\frac{G}{\mu}.$$
>
> **Paso 2 — Integrar dos veces.**
> $$u'(y)=-\frac{G}{\mu}\,y+C_1,\qquad u(y)=-\frac{G}{2\mu}\,y^2+C_1 y+C_2.$$
>
> **Paso 3 — Simetría.** El problema es simétrico respecto a $y=0$, luego $u'(0)=0\Rightarrow C_1=0$. (Equivalentemente, las condiciones $u(\pm h/2)=0$ fuerzan $C_1=0$ por simetría.)
>
> **Paso 4 — No deslizamiento.** $u(h/2)=0$:
> $$-\frac{G}{2\mu}\,\frac{h^2}{4}+C_2=0\ \Rightarrow\ C_2=\frac{G}{2\mu}\,\frac{h^2}{4}=\frac{G h^2}{8\mu}.$$
> Sustituyendo,
> $$u(y)=\frac{G}{2\mu}\left(\frac{h^2}{4}-y^2\right),$$
> una **parábola** con máximo en $y=0$. $\blacksquare$

> [!corolario] Caudal por unidad de ancho
> $$q=\int_{-h/2}^{h/2}u\,dy=\frac{G}{2\mu}\int_{-h/2}^{h/2}\left(\frac{h^2}{4}-y^2\right)dy.$$
> La integral vale $\left[\dfrac{h^2}{4}y-\dfrac{y^3}{3}\right]_{-h/2}^{h/2}=2\left(\dfrac{h^3}{8}-\dfrac{h^3}{24}\right)=2\cdot\dfrac{h^3}{12}=\dfrac{h^3}{6}.$ Por tanto
> $$\boxed{\,q=\frac{G\,h^3}{12\,\mu}\,}.$$
> La velocidad media es $\bar u=q/h=\dfrac{Gh^2}{12\mu}=\dfrac{2}{3}\,u_{\max}$.

![[perfiles_couette_poiseuille.svg|620]]
*Los dos arquetipos: a la izquierda el perfil **lineal** de Couette (una placa móvil arrastra el fluido); a la derecha el perfil **parabólico** de Poiseuille (un gradiente de presión empuja entre placas fijas, con máximo en el centro y velocidad nula en las paredes por no deslizamiento).*

### Flujo de Hagen–Poiseuille (tubería cilíndrica)

> [!teorema] Ley $R^4$
> En una tubería cilíndrica de radio $R$ bajo gradiente de presión $\partial_x p=-G$, el perfil es un **paraboloide de revolución**
> $$\boxed{\,u(r)=\frac{G}{4\mu}\big(R^2-r^2\big)\,},$$
> y el caudal total obedece la **ley de Hagen–Poiseuille**
> $$\boxed{\,Q=\frac{\pi R^4 G}{8\mu}=\frac{\pi R^4\,\Delta p}{8\mu L}\,}.$$

> [!demostracion]
> **Paso 1 — EDO en cilíndricas.** Para $\vec v=(u(r),0,0)$ a lo largo del eje, el laplaciano de la componente axial en coordenadas cilíndricas es $\dfrac1r\dfrac{d}{dr}\!\left(r\dfrac{du}{dr}\right)$, así que el momento axial da
> $$\mu\,\frac1r\frac{d}{dr}\!\left(r\frac{du}{dr}\right)=-G.$$
>
> **Paso 2 — Primera integración.** Multiplicando por $r/\mu$ e integrando:
> $$\frac{d}{dr}\!\left(r\frac{du}{dr}\right)=-\frac{G}{\mu}\,r\ \Rightarrow\ r\frac{du}{dr}=-\frac{G}{2\mu}\,r^2+C_1.$$
> Dividiendo por $r$: $\dfrac{du}{dr}=-\dfrac{G}{2\mu}\,r+\dfrac{C_1}{r}.$
>
> **Paso 3 — Regularidad en el eje.** Para que $u$ sea **finita** en $r=0$ necesitamos $C_1=0$ (si no, $\ln r$ diverge). Entonces $\dfrac{du}{dr}=-\dfrac{G}{2\mu}\,r$.
>
> **Paso 4 — Segunda integración.**
> $$u(r)=-\frac{G}{4\mu}\,r^2+C_2.$$
>
> **Paso 5 — No deslizamiento.** $u(R)=0\Rightarrow C_2=\dfrac{G}{4\mu}R^2$, de modo que
> $$u(r)=\frac{G}{4\mu}\big(R^2-r^2\big),$$
> un **paraboloide** con máximo $u_{\max}=GR^2/(4\mu)$ en el centro.
>
> **Paso 6 — Caudal.** Integramos sobre la sección en coronas circulares $dA=2\pi r\,dr$:
> $$Q=\int_0^R u(r)\,2\pi r\,dr=\frac{2\pi G}{4\mu}\int_0^R\big(R^2-r^2\big)r\,dr=\frac{\pi G}{2\mu}\left[\frac{R^2 r^2}{2}-\frac{r^4}{4}\right]_0^R.$$
> El corchete vale $\dfrac{R^4}{2}-\dfrac{R^4}{4}=\dfrac{R^4}{4}$, luego
> $$Q=\frac{\pi G}{2\mu}\cdot\frac{R^4}{4}=\frac{\pi R^4 G}{8\mu}.$$
>
> **Paso 7 — En términos de $\Delta p$.** Para una tubería de longitud $L$ con caída de presión $\Delta p$, el gradiente constante es $G=\Delta p/L$, así que
> $$Q=\frac{\pi R^4\,\Delta p}{8\mu L}.\qquad\blacksquare$$

> [!corolario] El radio lo gobierna todo
> Como $Q\propto R^4$, **cuadruplicar el radio multiplica el caudal por $4^4=256$**. Dicho de otro modo, a igual caída de presión, un tubo del doble de radio transporta $16$ veces más fluido. Esta dependencia exquisitamente fuerte explica por qué pequeñas variaciones de calibre tienen efectos enormes (sección [[Numero de Reynolds y Adimensionalizacion]] para el límite de validez).

---

> [!warning] Estas soluciones solo valen en régimen **laminar**
> Toda la derivación supone flujo **laminar**, ordenado en capas, con número de Reynolds bajo ([[Numero de Reynolds y Adimensionalizacion]]). Por encima del **$\mathrm{Re}$ crítico** (≈ $2300$ en tubería, con $\mathrm{Re}=\rho\bar u\,D/\mu$) el flujo **transiciona a turbulento**: aparecen fluctuaciones tridimensionales, el término convectivo deja de anularse y el **perfil parabólico ya no vale** (el perfil turbulento es mucho más plano en el centro). Además, la **ley $R^4$** es tan sensible al radio que tiene consecuencias fisiológicas notables: en los **vasos sanguíneos**, una pequeña vasoconstricción (radio menor) dispara enormemente la resistencia al flujo, y la presión arterial necesaria para mantener el caudal.

---

## Resumen

> [!resumen]
> | Caso | Geometría / motor | Perfil $u$ | Caudal | Clave |
> |:---|:---|:---|:---|:---|
> | **Couette** | placas, una móvil ($U$); sin $\partial_x p$ | $u=\dfrac{Uy}{h}$ (lineal) | $q=\dfrac{Uh}{2}$ | $\tau=\mu U/h$ constante |
> | **Poiseuille plano** | placas fijas; $\partial_x p=-G$ | $u=\dfrac{G}{2\mu}\!\left(\dfrac{h^2}{4}-y^2\right)$ | $q=\dfrac{Gh^3}{12\mu}$ | parábola; $\bar u=\tfrac23 u_{\max}$ |
> | **Hagen–Poiseuille** | tubería radio $R$; $\partial_x p=-G$ | $u=\dfrac{G}{4\mu}(R^2-r^2)$ | $Q=\dfrac{\pi R^4 G}{8\mu}=\dfrac{\pi R^4\Delta p}{8\mu L}$ | ley $R^4$ |

> [!corolario] Lo esencial
> La **clave física** de toda solución exacta es que el flujo unidireccional desarrollado **mata el término convectivo** $(\vec v\cdot\nabla)\vec v=\vec 0$, dejando Navier–Stokes como una **EDO lineal** $\mu u''=\partial_x p$. De ahí dos perfiles canónicos —**lineal** (arrastre puro, Couette) y **parabólico** (presión pura, Poiseuille)— y su síntesis cilíndrica con la **ley $R^4$**. Todo ello vive solo mientras el flujo sea **laminar**; pasado el $\mathrm{Re}$ crítico, la turbulencia destruye estos perfiles ([[Capa Limite]], [[Numero de Reynolds y Adimensionalizacion]]).

> [!referencia]
> - **Landau-Lifshitz**, *Fluid Mechanics* (Vol. 6), §17 — flujo entre placas y por tubería, ley de Poiseuille.
> - **Batchelor**, *An Introduction to Fluid Dynamics*, §4.2 — flujos unidireccionales exactos.
> - **F. White**, *Viscous Fluid Flow*, cap. 3 — soluciones exactas de Navier–Stokes.
> - Notas relacionadas: [[Ecuaciones de Navier-Stokes]], [[Numero de Reynolds y Adimensionalizacion]], [[Capa Limite]], [[5 Flujo Viscoso/index | Flujo Viscoso]].
