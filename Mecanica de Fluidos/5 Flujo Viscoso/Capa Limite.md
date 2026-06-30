---
title: Capa Límite
order: 3
tags:
  - fluidos
  - teoria
  - flujo-viscoso
draft: false
aliases:
  - Capa límite
  - Boundary layer
  - Prandtl
---

# Capa Límite $\delta(x)\sim\sqrt{\dfrac{\nu x}{U}}$

> [!definicion]
> La **capa límite** es la región delgada de espesor $\delta(x)$, pegada a una pared sólida, en la que la velocidad del fluido pasa de **cero** en el contacto (condición de **no deslizamiento**) hasta prácticamente la velocidad $U$ del flujo libre. Dentro de ella la **viscosidad es decisiva** (los gradientes $\partial_y u$ son enormes); fuera de ella el flujo se comporta como **ideal**. Su espesor crece con la distancia $x$ al borde de ataque como
> $$\boxed{\ \delta(x)\sim\sqrt{\dfrac{\nu x}{U}}\ }\qquad\Longleftrightarrow\qquad \frac{\delta}{x}\sim\frac{1}{\sqrt{\mathrm{Re}_x}},\qquad \mathrm{Re}_x=\frac{Ux}{\nu}.$$
> Es la idea con que **Ludwig Prandtl** (1904) reconcilió el flujo ideal con la realidad: la viscosidad no es despreciable en todo el dominio, pero sí se **confina** a esta capa cuando $\mathrm{Re}\gg1$.

---

> [!info]
> Nota de la sección [[5 Flujo Viscoso/index | Flujo Viscoso]]. Sus hermanas son [[Numero de Reynolds y Adimensionalizacion]] (de donde sale $\mathrm{Re}_x$) y [[Flujo de Stokes]] (el límite opuesto $\mathrm{Re}\ll1$). La capa límite conecta directamente con el [[Flujo Potencial]], al que **resuelve la paradoja de d'Alembert**: explica de dónde nace el arrastre que el flujo ideal predecía nulo. **Referencia.** Landau-Lifshitz, *Mecánica de Fluidos*, Vol. 6, §39.

---

## Ejemplo

> [!ejemplo] Espesor de la capa límite al final de una placa
> Una placa plana de longitud $L=1{,}0\ \mathrm{m}$ se expone a una corriente. Estimemos $\delta(L)$ en **aire** y en **agua** a $U=2{,}0\ \mathrm{m/s}$.
>
> Datos: aire $\nu_{\text{aire}}\approx1{,}5\times10^{-5}\ \mathrm{m^2/s}$; agua $\nu_{\text{agua}}\approx1{,}0\times10^{-6}\ \mathrm{m^2/s}$.

> [!solucion]
> **Paso 1 — Reynolds en el extremo de la placa.** Con $x=L=1{,}0\ \mathrm{m}$,
> $$\mathrm{Re}_L^{\text{aire}}=\frac{UL}{\nu_{\text{aire}}}=\frac{2{,}0\cdot1{,}0}{1{,}5\times10^{-5}}\approx1{,}3\times10^{5},\qquad \mathrm{Re}_L^{\text{agua}}=\frac{2{,}0\cdot1{,}0}{1{,}0\times10^{-6}}=2{,}0\times10^{6}.$$
> En ambos casos $\mathrm{Re}_L\gg1$: la hipótesis de capa límite delgada es válida.
>
> **Paso 2 — Espesor de Blasius.** Usamos $\delta\approx 5{,}0\,L/\sqrt{\mathrm{Re}_L}$:
> $$\delta_{\text{aire}}\approx\frac{5{,}0\cdot1{,}0}{\sqrt{1{,}3\times10^{5}}}\approx\frac{5{,}0}{3{,}6\times10^{2}}\approx1{,}4\times10^{-2}\ \mathrm{m}=14\ \mathrm{mm}.$$
> $$\delta_{\text{agua}}\approx\frac{5{,}0\cdot1{,}0}{\sqrt{2{,}0\times10^{6}}}\approx\frac{5{,}0}{1{,}4\times10^{3}}\approx3{,}5\times10^{-3}\ \mathrm{m}=3{,}5\ \mathrm{mm}.$$
>
> **Paso 3 — Lectura física.** Sobre una placa de un metro la capa límite mide apenas **milímetros**: en efecto es **delgada** frente a $L$. Y es más fina en agua que en aire porque su viscosidad cinemática $\nu$ es menor (mayor $\mathrm{Re}$). $\blacksquare$
>
> **Transición a turbulencia.** La placa deja de ser laminar cuando $\mathrm{Re}_x$ alcanza $\sim5\times10^{5}$. En aire eso ocurre en $x_{\text{tr}}=\nu\,\mathrm{Re}_{\text{tr}}/U\approx (1{,}5\times10^{-5})(5\times10^{5})/2{,}0\approx3{,}8\ \mathrm{m}$: toda esta placa es laminar. En agua, $x_{\text{tr}}\approx0{,}25\ \mathrm{m}$, así que pasa a turbulenta antes del extremo.

---

## En qué consiste

### La idea de Prandtl (1904)

> [!teoria] El truco de las dos regiones
> Durante el siglo XIX la teoría se dividía: el [[Flujo Potencial | flujo ideal]] daba ecuaciones manejables pero predecía **arrastre nulo** (paradoja de d'Alembert), mientras que [[Ecuaciones de Navier-Stokes | Navier–Stokes]] completo era intratable. Prandtl observó que, a **alto $\mathrm{Re}$**, ambas visiones son ciertas **en regiones distintas**:
> - **Lejos de la pared:** la viscosidad es irrelevante y el flujo es **esencialmente ideal** (gobernado por [[Flujo Potencial]] o por la ecuación de Euler).
> - **En una capa delgada $\delta$ pegada a la pared:** la velocidad debe caer de $U$ a $0$ en una distancia diminuta, de modo que el gradiente $\partial_y u$ —y con él el término viscoso $\mu\,\partial_y^2u$— **no es despreciable**, por pequeño que sea $\mu$.
>
> Así la viscosidad, despreciable en casi todo el dominio, es **gobernante** justo donde el fluido toca el sólido. Esta separación reconcilia el flujo ideal con la realidad.

### Estimación del espesor $\delta(x)$ por balance de órdenes

> [!demostracion] De dónde sale $\delta\sim\sqrt{\nu x/U}$
> El espesor sale, sin resolver ninguna ecuación, de **comparar el tamaño de los términos** de la ecuación de momento dentro de la capa. Trabajamos en 2D estacionario sobre una placa, con $x$ a lo largo de la pared y $y$ perpendicular.
>
> **Paso 1 — Escalas.** Asignamos a cada variable su magnitud típica dentro de la capa:
> $$u\sim U,\qquad x\sim x,\qquad y\sim\delta.$$
> La coordenada longitudinal vive sobre la escala $x$ (la distancia al borde de ataque); la transversal, sobre la escala $\delta\ll x$ del espesor.
>
> **Paso 2 — Tamaño del término convectivo (inercia).** El término $\rho\,u\,\partial_x u$ involucra una variación de $u$ (de orden $U$) sobre una longitud $x$:
> $$\rho\,u\,\partial_x u\ \sim\ \rho\,U\cdot\frac{U}{x}=\frac{\rho U^2}{x}.$$
>
> **Paso 3 — Tamaño del término viscoso.** La derivada **dominante** es la transversal, porque $u$ varía de $0$ a $U$ sobre el pequeño espesor $\delta$ (no sobre $x$). Entonces $\partial_y^2 u\sim U/\delta^2$ y
> $$\mu\,\partial_y^2 u\ \sim\ \mu\,\frac{U}{\delta^2}.$$
>
> **Paso 4 — El equilibrio que define la capa.** La capa límite es, por definición, la región donde la viscosidad **logra equilibrar** a la inercia. Igualando los dos órdenes:
> $$\frac{\rho U^2}{x}\ \sim\ \frac{\mu U}{\delta^2}.$$
>
> **Paso 5 — Despejar $\delta$.** Despejando $\delta^2$:
> $$\delta^2\ \sim\ \frac{\mu\,x}{\rho\,U}=\frac{\nu\,x}{U}\qquad\Longrightarrow\qquad \delta(x)\sim\sqrt{\frac{\nu x}{U}}.$$
> Dividiendo por $x$ se obtiene la forma adimensional, en términos del **Reynolds local** $\mathrm{Re}_x=Ux/\nu$:
> $$\frac{\delta}{x}\sim\frac{1}{\sqrt{\mathrm{Re}_x}}.$$
> $\blacksquare$
>
> **Lectura.** La capa crece como $\sqrt{x}$ (es más gruesa corriente abajo) y se **adelgaza** al aumentar $U$ o disminuir $\nu$, es decir, al crecer $\mathrm{Re}$. A altísimo Reynolds, $\delta/x\to0$: la capa se vuelve infinitamente fina, justificando el límite ideal exterior.

### La figura

![[capa_limite.svg|480]]
*La capa límite crece como $\delta\sim\sqrt{\nu x/U}$ sobre una placa plana; dentro de ella el perfil de velocidad va de $0$ en la pared (no deslizamiento) a $U$ en el borde de la capa, donde empalma con el flujo libre.*

### Ecuaciones de capa límite de Prandtl

> [!proposicion] Navier–Stokes simplificado por escalas
> Partiendo de Navier–Stokes 2D estacionario e incompresible, la hipótesis $\delta\ll x$ permite descartar términos por su orden de magnitud (el término viscoso longitudinal $\nu\,\partial_x^2u\sim\nu U/x^2$ es despreciable frente al transversal $\nu\,\partial_y^2u\sim\nu U/\delta^2$, pues $\delta\ll x$). Lo que queda son las **ecuaciones de capa límite**:
> $$u\,\partial_x u+v\,\partial_y u=-\frac{1}{\rho}\,\partial_x p+\nu\,\partial_y^2 u,\qquad \partial_y p\approx0.$$
> La segunda ecuación es la clave operativa: **la presión no varía a través de la capa**, de modo que $p(x)$ la **impone el flujo exterior ideal** y entra en la capa como un dato conocido. Esto desacopla el problema: primero se resuelve el flujo potencial afuera para obtener $p(x)$, y luego la capa límite con esa presión.

> [!teorema] Solución de Blasius para placa plana
> Cuando el flujo exterior es uniforme ($U$ constante, $\partial_x p=0$), Blasius (1908) redujo las ecuaciones anteriores a una sola **EDO ordinaria** mediante la variable de semejanza $\eta=y\sqrt{U/(\nu x)}$. La solución numérica da:
> $$\boxed{\ \delta(x)\approx\frac{5{,}0\,x}{\sqrt{\mathrm{Re}_x}}\ },\qquad\qquad C_f(x)\approx\frac{0{,}664}{\sqrt{\mathrm{Re}_x}},$$
> donde $C_f=\tau_w/(\tfrac12\rho U^2)$ es el **coeficiente de fricción local**. El factor $5{,}0$ confirma el orden de magnitud del balance ($\delta\sim\sqrt{\nu x/U}$) y le pone el coeficiente exacto.

### Arrastre de fricción (skin friction)

> [!proposicion] El esfuerzo en la pared y su integral
> Dentro de la capa el gradiente de velocidad es máximo en la pared; allí nace el **esfuerzo cortante**
> $$\tau_w=\mu\left(\frac{\partial u}{\partial y}\right)_{y=0}.$$
> Para placa plana, con $C_f\approx0{,}664/\sqrt{\mathrm{Re}_x}$, se tiene $\tau_w(x)=\tfrac12\rho U^2 C_f\propto \sqrt{\mu\rho U^3/x}$. El **arrastre viscoso** total sobre una cara de la placa de longitud $L$ y ancho $b$ es la integral de $\tau_w$:
> $$F_D=b\int_0^L\tau_w(x)\,dx\ \propto\ b\,\sqrt{\mu\rho\,U^3\,L}.$$
> Esta dependencia $F_D\propto\sqrt{\mu\rho U^3 L}\times b$ es la firma del arrastre de fricción: crece con $\sqrt{U^3}$ (no con $U^2$, como el arrastre de presión) y con $\sqrt{L}$.

### Separación, estela y la paradoja de d'Alembert

> [!teoria] Cuando la capa se desprende
> Hasta aquí la presión exterior era favorable o constante. Si el cuerpo es **romo** (una esfera, un cilindro), corriente abajo el flujo exterior **desacelera** y aparece un **gradiente de presión adverso** $\partial_x p>0$: la presión empuja al fluido **hacia atrás**.
>
> **Mecanismo de la separación.** En la capa límite, el fluido cercano a la pared ya viaja lento (la fricción lo ha frenado) y tiene poca energía cinética. Un gradiente adverso lo frena aún más hasta **detenerlo y revertirlo**: el punto donde $(\partial u/\partial y)_{y=0}=0$ marca la **separación**. Más allá, el flujo retrocede junto a la pared, la capa límite **se despega** de la superficie y se forma una ancha **estela** de baja presión detrás del cuerpo.
>
> **Resolución de d'Alembert.** El [[Flujo Potencial]] predecía presiones simétricas adelante y atrás, y por tanto **arrastre nulo**. La separación rompe esa simetría: la estela posterior queda a baja presión mientras el frente sufre alta presión, y la diferencia produce el **arrastre de presión** (o de forma). Sumado al arrastre de fricción, este es el arrastre **real** de los cuerpos. Así la capa límite —y sobre todo su separación— es la pieza física que faltaba para entender la paradoja.

> [!warning]
> La capa límite es delgada **solo a alto $\mathrm{Re}$**: a bajo Reynolds ($\mathrm{Re}\lesssim1$, [[Flujo de Stokes]]) no existe tal capa fina y la viscosidad domina todo el campo. Además, en cuerpos romos (una pelota, un coche) lo que más arrastre causa no es el **espesor** de la capa, sino su **separación**: la estela de presión supera con creces a la fricción superficial. Por eso la aerodinámica se ocupa, ante todo, de **retrasar la separación** (perfiles fuselados, hoyuelos de la pelota de golf que la hacen turbulenta y más pegada), no de eliminar la capa.

---

## Resumen

> [!resumen]
> | Concepto | Expresión | Lectura física |
> |:---|:---|:---|
> | Espesor (orden) | $\delta(x)\sim\sqrt{\dfrac{\nu x}{U}}$ | crece como $\sqrt{x}$; se adelgaza al subir $\mathrm{Re}$ |
> | Forma adimensional | $\dfrac{\delta}{x}\sim\dfrac{1}{\sqrt{\mathrm{Re}_x}}$ | $\mathrm{Re}_x=Ux/\nu$ |
> | Blasius (placa) | $\delta\approx\dfrac{5{,}0\,x}{\sqrt{\mathrm{Re}_x}}$ | coeficiente exacto del balance |
> | Fricción local | $C_f\approx\dfrac{0{,}664}{\sqrt{\mathrm{Re}_x}}$ | $C_f=\tau_w/(\tfrac12\rho U^2)$ |
> | Esfuerzo en pared | $\tau_w=\mu\left(\dfrac{\partial u}{\partial y}\right)_{y=0}$ | origen del arrastre de fricción |
> | Arrastre de fricción | $F_D\propto b\,\sqrt{\mu\rho U^3 L}$ | $\propto\sqrt{U^3}$, $\sqrt{L}$ |
> | Ecuaciones de Prandtl | $u\partial_x u+v\partial_y u=-\tfrac1\rho\partial_x p+\nu\,\partial_y^2u$, $\ \partial_y p\approx0$ | la presión la fija el flujo exterior |

> [!corolario] La moraleja
> La viscosidad, despreciable lejos del cuerpo, es **decisiva** en una capa de espesor $\delta\sim\sqrt{\nu x/U}$ junto a la pared. Esa capa hace dos cosas: genera el **arrastre de fricción** (la integral de $\tau_w$) y, al **separarse** bajo gradiente de presión adverso, genera el **arrastre de presión** y la estela. Entre ambas resuelven la **paradoja de d'Alembert**: el arrastre real no contradice al flujo ideal, nace de la fina costura viscosa que el flujo ideal ignoraba.

> [!referencia]
> Landau-Lifshitz, *Mecánica de Fluidos*, Vol. 6, §39 (capa límite laminar) y §§40–41 (separación y estela). Para la solución de semejanza: Schlichting, *Boundary-Layer Theory*; Batchelor, cap. 5; Acheson, cap. 8.
