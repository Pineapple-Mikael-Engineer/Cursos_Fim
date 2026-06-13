---
title: Tensor Energía-Momento
tags:
  - electromagnetismo
  - teoria
  - covariante
draft: false
aliases:
  - Tensor energía-momento
  - Tensor de esfuerzos de Maxwell
  - T^μν
---

# Tensor Energía-Momento $T^{\mu\nu}=\dfrac{1}{\mu_0}\left(F^{\mu\alpha}{F_\alpha}^{\nu}+\tfrac14\eta^{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}\right)$

---

> [!definicion] Tensor energía-momento del campo electromagnético
> El **tensor energía-momento** (o tensor de esfuerzos-energía) del campo electromagnético es el tensor de rango $2$
> $$T^{\mu\nu}=\frac{1}{\mu_0}\left(F^{\mu\alpha}{F_{\alpha}}^{\nu}+\frac14\,\eta^{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}\right),\qquad {F_\alpha}^{\nu}=\eta_{\alpha\beta}F^{\beta\nu},$$
> construido únicamente con el [[Tensor de Campo | tensor de campo]] $F^{\mu\nu}$ y la métrica $\eta_{\mu\nu}=\mathrm{diag}(+1,-1,-1,-1)$.
>
> Sus dos propiedades estructurales son:
> - **Simétrico:** $T^{\mu\nu}=T^{\nu\mu}$.
> - **De traza nula:** $T^{\mu}{}_{\mu}=0$ (manifestación de que el fotón no tiene masa).
>
> Sus componentes empaquetan, en un solo objeto covariante, la densidad de energía $u$, el vector de Poynting $\vec S$ y el tensor de esfuerzos de Maxwell $\sigma_{ij}$.

---

> [!info] Ubicación y dependencias
> - **Sección:** [[6 Formulacion Covariante/index | Formulación Covariante]].
> - **Notas hermanas:** [[Tensor de Campo]], [[Maxwell Covariante]].
> - **Usa:** [[Energia y Momento]] (densidad de energía, Poynting y esfuerzos de Maxwell en lenguaje vectorial 3D).
> - **Referencias:** Griffiths, *Introduction to Electrodynamics*, cap. 12; Landau & Lifshitz, *Teoría clásica de los campos* (Vol. 2).
>
> **Convenio fijo de esta sección:** métrica $(+,-,-,-)$; $F^{0i}=-E_i/c$, $F^{ij}=-\epsilon_{ijk}B_k$; invariante $F_{\alpha\beta}F^{\alpha\beta}=2\!\left(B^2-\dfrac{E^2}{c^2}\right)$; identidad $\dfrac{1}{\mu_0 c^2}=\varepsilon_0$.

---

## Ejemplo

> [!ejemplo] Onda plana electromagnética en el vacío
> Una onda plana que se propaga en $+\hat x$ tiene $\vec E\perp\vec B\perp\hat x$, con $E=cB$ (es decir $B=E/c$). Calcula $u$, $\vec S$ y la **presión de radiación** $P$ que ejerce al incidir sobre un absorbente perfecto.

> [!solucion] Desarrollo
> **Densidad de energía.** Como $B^2=E^2/c^2$, las contribuciones eléctrica y magnética coinciden:
> $$u=\frac{\varepsilon_0}{2}E^2+\frac{1}{2\mu_0}B^2=\frac{\varepsilon_0}{2}E^2+\frac{1}{2\mu_0}\frac{E^2}{c^2}=\frac{\varepsilon_0}{2}E^2+\frac{\varepsilon_0}{2}E^2=\varepsilon_0 E^2,$$
> donde se usó $\dfrac{1}{\mu_0 c^2}=\varepsilon_0$.
>
> **Vector de Poynting.** Con $\vec S=\dfrac{1}{\mu_0}\vec E\times\vec B$ y $B=E/c$:
> $$S=\frac{1}{\mu_0}E\,B=\frac{1}{\mu_0 c}E^2=\varepsilon_0 c\,E^2=c\,u.$$
> El flujo de energía es $c$ veces la densidad de energía, como cabe esperar de algo que viaja a la velocidad de la luz.
>
> **Presión de radiación.** El momento por unidad de volumen es $g=u/c$, y al incidir sobre un absorbente perfecto la fuerza por unidad de área es
> $$P=c\,g=u.$$
> La presión de radiación de una onda plana sobre un absorbente perfecto iguala numéricamente a la densidad de energía instantánea. $\blacksquare$
>
> Estas tres cantidades son exactamente las componentes $T^{00}=u$, $T^{0i}=S_i/c$ y $-T^{ii}=\sigma_{ii}$ del tensor que deduciremos a continuación.

---

## En qué consiste

El tensor $T^{\mu\nu}$ es la pieza que **unifica** la energía y el momento del campo. Cada bloque de componentes tiene un significado físico directo, y todos se siguen de la única definición de arriba. A lo largo de esta sección verificaremos sus propiedades y calcularemos cada bloque, signo a signo.

### Simetría y traza nula

> [!proposicion] $T^{\mu\nu}$ es simétrico y de traza nula
> $$T^{\mu\nu}=T^{\nu\mu},\qquad T^{\mu}{}_{\mu}=0.$$

> [!demostracion] Simetría
> El término de traza es manifiestamente simétrico, porque $\eta^{\mu\nu}=\eta^{\nu\mu}$ y el invariante $F_{\alpha\beta}F^{\alpha\beta}$ es un escalar.
>
> Para el primer término, escribimos la contracción bajando el índice mudo:
> $$F^{\mu\alpha}{F_\alpha}^{\nu}=F^{\mu\alpha}\,\eta_{\alpha\beta}F^{\beta\nu}.$$
> Renombrando los mudos $\alpha\leftrightarrow\beta$ y usando la antisimetría $F^{\mu\alpha}=-F^{\alpha\mu}$ dos veces (una por cada factor),
> $$F^{\mu\alpha}\,\eta_{\alpha\beta}F^{\beta\nu}=F^{\mu\beta}\,\eta_{\beta\alpha}F^{\alpha\nu}=(-F^{\beta\mu})\,\eta_{\beta\alpha}\,(-F^{\nu\alpha})=F^{\nu\alpha}\,\eta_{\alpha\beta}F^{\beta\mu}=F^{\nu\alpha}{F_\alpha}^{\mu}.$$
> Es decir, $F^{\mu\alpha}{F_\alpha}^{\nu}=F^{\nu\alpha}{F_\alpha}^{\mu}$, que es simétrico en $\mu\leftrightarrow\nu$. Por tanto $T^{\mu\nu}=T^{\nu\mu}$. $\blacksquare$

> [!demostracion] Traza nula
> Contraemos con $\eta_{\mu\nu}$. Para el primer término,
> $$\eta_{\mu\nu}F^{\mu\alpha}{F_\alpha}^{\nu}=F_{\nu}{}^{\alpha}{F_\alpha}^{\nu}={F_\alpha}^{\nu}F_{\nu}{}^{\alpha}=-F^{\alpha\nu}F_{\nu}{}^{\alpha}=-F_{\alpha\beta}F^{\alpha\beta},$$
> donde se usó la antisimetría para reordenar los índices y reconocer el invariante $F_{\alpha\beta}F^{\alpha\beta}$.
>
> Para el término de traza, $\eta_{\mu\nu}\eta^{\mu\nu}=\delta^{\mu}{}_{\mu}=4$ (dimensión del espacio-tiempo), de modo que
> $$\tfrac14\,\eta_{\mu\nu}\eta^{\mu\nu}\,F_{\alpha\beta}F^{\alpha\beta}=\tfrac14\cdot4\cdot F_{\alpha\beta}F^{\alpha\beta}=F_{\alpha\beta}F^{\alpha\beta}.$$
>
> Sumando ambos,
> $$T^{\mu}{}_{\mu}=\frac{1}{\mu_0}\left(-F_{\alpha\beta}F^{\alpha\beta}+F_{\alpha\beta}F^{\alpha\beta}\right)=0.$$
> La traza nula refleja que el **fotón no tiene masa**: un campo de partículas masivas tendría traza proporcional a esa masa. $\blacksquare$

### Componente $T^{00}=u$: densidad de energía

> [!teorema] La componente temporal-temporal es la densidad de energía
> $$T^{00}=u=\frac{\varepsilon_0}{2}E^2+\frac{1}{2\mu_0}B^2.$$

> [!demostracion] Cálculo de $T^{00}$
> **Paso 1 — Escribir la componente.** Con $\mu=\nu=0$ y $\eta^{00}=+1$,
> $$T^{00}=\frac{1}{\mu_0}\left(F^{0\alpha}{F_\alpha}^{0}+\tfrac14\,F_{\alpha\beta}F^{\alpha\beta}\right).$$
>
> **Paso 2 — La contracción $F^{0\alpha}{F_\alpha}^{0}$.** El término $\alpha=0$ se anula porque $F^{00}=0$. Para $\alpha=i$ (espacial) bajamos el índice:
> $${F_i}^{0}=\eta_{ij}F^{j0}=-F^{i0}=-(-F^{0i})=F^{0i}=-\frac{E_i}{c}.$$
> Entonces, usando $F^{0i}=-E_i/c$ en ambos factores,
> $$F^{0\alpha}{F_\alpha}^{0}=\sum_i F^{0i}{F_i}^{0}=\sum_i\left(-\frac{E_i}{c}\right)\left(-\frac{E_i}{c}\right)=+\frac{E^2}{c^2}.$$
>
> **Paso 3 — El término de traza.** Con $F_{\alpha\beta}F^{\alpha\beta}=2\!\left(B^2-\dfrac{E^2}{c^2}\right)$,
> $$\tfrac14\,F_{\alpha\beta}F^{\alpha\beta}=\tfrac14\cdot2\!\left(B^2-\frac{E^2}{c^2}\right)=\tfrac12\!\left(B^2-\frac{E^2}{c^2}\right).$$
>
> **Paso 4 — Sumar (todo cierra).** Reunimos los dos resultados:
> $$T^{00}=\frac{1}{\mu_0}\left[\frac{E^2}{c^2}+\frac12 B^2-\frac12\frac{E^2}{c^2}\right]=\frac{1}{\mu_0}\left[\frac12\frac{E^2}{c^2}+\frac12 B^2\right].$$
> Usando $\dfrac{1}{\mu_0 c^2}=\varepsilon_0$ en el primer término,
> $$T^{00}=\frac{\varepsilon_0}{2}E^2+\frac{1}{2\mu_0}B^2=u.\ \blacksquare$$

### Componente $T^{0i}=S_i/c$: densidad de momento $\times\,c$

> [!teorema] Las componentes temporal-espaciales dan el vector de Poynting
> $$T^{0i}=\frac{S_i}{c},\qquad \vec S=\frac{1}{\mu_0}\,\vec E\times\vec B.$$

> [!demostracion] Cálculo de $T^{0i}$
> **Paso 1 — La traza desaparece.** Para $\mu=0,\ \nu=i$ se tiene $\eta^{0i}=0$, de modo que el término de traza no contribuye:
> $$T^{0i}=\frac{1}{\mu_0}F^{0\alpha}{F_\alpha}^{i}.$$
>
> **Paso 2 — Solo contribuye $\alpha=j$ espacial.** El término $\alpha=0$ se anula ($F^{00}=0$). Para $\alpha=j$ bajamos el índice usando $F^{ji}=-\epsilon_{jik}B_k$:
> $${F_j}^{i}=\eta_{jk}F^{ki}=-F^{ji}=-(-\epsilon_{jik}B_k)=\epsilon_{jik}B_k.$$
> Con $F^{0j}=-E_j/c$,
> $$T^{0i}=\frac{1}{\mu_0}\sum_j\left(-\frac{E_j}{c}\right)\epsilon_{jik}B_k=-\frac{1}{\mu_0 c}\,\epsilon_{jik}E_jB_k.$$
> Usando $-\epsilon_{jik}=\epsilon_{ijk}$ (intercambio de los dos primeros índices del símbolo de Levi-Civita),
> $$T^{0i}=\frac{1}{\mu_0 c}\,\epsilon_{ijk}E_jB_k=\frac{1}{\mu_0 c}(\vec E\times\vec B)_i=\frac{S_i}{c}.\ \blacksquare$$
>
> **Interpretación.** Podemos escribir $T^{0i}=\dfrac{S_i}{c}=c\,g_i$, donde
> $$\vec g=\frac{\vec S}{c^2}=\varepsilon_0\,\vec E\times\vec B$$
> es la **densidad de momento** del campo (usando $\dfrac{1}{\mu_0 c^2}=\varepsilon_0$). Así, el flujo de energía $\vec S$ y la densidad de momento $\vec g$ son la misma fila del tensor, a un factor $c$ de distancia: energía que fluye es momento que se transporta.

### Componentes $T^{ij}=-\sigma_{ij}$: esfuerzos de Maxwell

> [!teorema] El bloque espacial es (menos) el tensor de esfuerzos de Maxwell
> $$T^{ij}=-\sigma_{ij},\qquad \sigma_{ij}=\varepsilon_0\!\left(E_iE_j-\tfrac12\delta_{ij}E^2\right)+\frac{1}{\mu_0}\!\left(B_iB_j-\tfrac12\delta_{ij}B^2\right).$$

> [!demostracion] Esquema del cálculo de $T^{ij}$
> Para $\mu=i,\ \nu=j$ se usa $\eta^{ij}=-\delta_{ij}$:
> $$T^{ij}=\frac{1}{\mu_0}\left(F^{i\alpha}{F_\alpha}^{j}-\tfrac14\,\delta_{ij}\,F_{\alpha\beta}F^{\alpha\beta}\right).$$
>
> La contracción bilineal $F^{i\alpha}{F_\alpha}^{j}$ se separa en una parte con $\alpha=0$ (temporal) y otra con $\alpha=k$ (espacial). La parte temporal genera los productos $E_iE_j$ (con $F^{i0}=E_i/c$ y un factor $1/c^2$ que se reabsorbe vía $\varepsilon_0$); la parte espacial genera los productos $B_iB_j$ (vía $F^{ik}=-\epsilon_{ikl}B_l$ y la identidad $\epsilon_{ikl}\epsilon_{jkm}=\delta_{ij}\delta_{lm}-\delta_{im}\delta_{lj}$, que produce $B_iB_j$ más términos $\delta_{ij}B^2$).
>
> El término de traza $-\tfrac14\delta_{ij}F_{\alpha\beta}F^{\alpha\beta}=-\tfrac12\delta_{ij}\!\left(B^2-\dfrac{E^2}{c^2}\right)$ es exactamente lo que completa los términos isótropos $-\tfrac12\delta_{ij}E^2$ y $-\tfrac12\delta_{ij}B^2$. Reuniendo todo y cambiando de signo,
> $$T^{ij}=-\sigma_{ij},$$
> con $\sigma_{ij}$ el [[Energia y Momento | tensor de esfuerzos de Maxwell]]. No hace falta el desarrollo exhaustivo de las nueve componentes: la estructura es clara, el bilineal aporta $E_iE_j$ y $B_iB_j$, y la traza aporta los $-\tfrac12\delta_{ij}$. $\blacksquare$

### La matriz $T^{\mu\nu}$ por bloques

Reuniendo los cuatro resultados, el tensor se organiza en cuatro bloques con significado físico inmediato:

$$T^{\mu\nu}=\begin{pmatrix} u & S_x/c & S_y/c & S_z/c\\ S_x/c & -\sigma_{xx} & -\sigma_{xy} & -\sigma_{xz}\\ S_y/c & -\sigma_{yx} & -\sigma_{yy} & -\sigma_{yz}\\ S_z/c & -\sigma_{zx} & -\sigma_{zy} & -\sigma_{zz}\end{pmatrix}.$$

![[tensor_T.svg|520]]

*Estructura por bloques del tensor energía-momento: la esquina $T^{00}$ es la densidad de energía $u$; la primera fila y columna $T^{0i}=S_i/c$ son el flujo de energía / densidad de momento; el bloque espacial $T^{ij}=-\sigma_{ij}$ son los esfuerzos de Maxwell. La simetría hace que la matriz sea espejo respecto a la diagonal.*

> [!warning] Por qué importa este objeto
> El tensor $T^{\mu\nu}$ **unifica** la densidad de energía $u$, el vector de Poynting $\vec S$ y el tensor de esfuerzos de Maxwell $\sigma_{ij}$ —piezas que en el [[Energia y Momento | tratamiento vectorial 3D]] aparecían sueltas (capítulo 4)— en un único objeto covariante. Además, en relatividad general es precisamente el tensor energía-momento el que actúa como **fuente del campo gravitatorio** en la ecuación de Einstein $G^{\mu\nu}=\dfrac{8\pi G}{c^4}T^{\mu\nu}$: este es el puente hacia Landau Vol. 2.

### Conservación: $\partial_\mu T^{\mu\nu}=-{F^\nu}_{\lambda}J^{\lambda}$

> [!teorema] Ley de conservación local
> $$\partial_\mu T^{\mu\nu}=-{F^\nu}_{\lambda}\,J^{\lambda},$$
> donde el miembro derecho es la **densidad de cuadrifuerza de Lorentz** que el campo ejerce sobre las cargas.

> [!demostracion] Conservación a partir de Maxwell covariante
> **Paso 1 — Derivar.** Tomamos $\partial_\mu T^{\mu\nu}$ y aplicamos las [[Maxwell Covariante | ecuaciones de Maxwell covariantes]]: la **inhomogénea**
> $$\partial_\mu F^{\mu\alpha}=\mu_0 J^{\alpha},$$
> y la **identidad de Bianchi** (ecuaciones homogéneas)
> $$\partial^\mu F^{\nu\lambda}+\partial^\nu F^{\lambda\mu}+\partial^\lambda F^{\mu\nu}=0.$$
> Al derivar el término bilineal $F^{\mu\alpha}{F_\alpha}^{\nu}$ aparece un término en el que la inhomogénea reduce $\partial_\mu F^{\mu\alpha}$ a $\mu_0 J^{\alpha}$, dando una contribución $\propto {F^\nu}_{\alpha}J^{\alpha}$; el término restante, junto con la derivada del término de traza, se cancela exactamente gracias a la identidad de Bianchi.
>
> **Paso 2 — Resultado.** Tras la cancelación de Bianchi queda
> $$\partial_\mu T^{\mu\nu}=-{F^\nu}_{\lambda}\,J^{\lambda},$$
> la densidad de cuadrifuerza de Lorentz (con su signo) sobre las cargas. El tensor del campo no se conserva por sí solo si hay fuentes: cede energía y momento a la materia.
>
> **Paso 3 — En el vacío** ($J^{\lambda}=0$):
> $$\partial_\mu T^{\mu\nu}=0,$$
> conservación pura de energía-momento del campo. $\blacksquare$

> [!corolario] Las dos leyes que esconde $\partial_\mu T^{\mu\nu}=0$
> - **$\nu=0$** reproduce el **teorema de Poynting**:
> $$\partial_t u+\nabla\cdot\vec S=-\vec J\cdot\vec E,$$
> el balance de energía del campo (enlaza con [[Energia y Momento]]).
> - **$\nu=i$** da la **conservación del momento**: la divergencia de los esfuerzos de Maxwell equilibra la fuerza sobre las cargas (presión de radiación, esfuerzos de Maxwell).

---

## Resumen

> [!resumen] Componentes y significado de $T^{\mu\nu}$
>
> | Componente | Expresión | Significado físico |
> | --- | --- | --- |
> | $T^{00}$ | $u=\dfrac{\varepsilon_0}{2}E^2+\dfrac{1}{2\mu_0}B^2$ | Densidad de energía |
> | $T^{0i}=T^{i0}$ | $\dfrac{S_i}{c}=c\,g_i$ | Flujo de energía / densidad de momento $\times c$ |
> | $T^{ij}$ | $-\sigma_{ij}$ | Tensor de esfuerzos de Maxwell (con signo) |
> | $T^{\mu}{}_{\mu}$ | $0$ | Traza nula (fotón sin masa) |
> | $\partial_\mu T^{\mu\nu}$ | $-{F^\nu}_{\lambda}J^{\lambda}$ | Cuadrifuerza de Lorentz; $=0$ en el vacío |

> [!corolario] Lo esencial
> - $T^{\mu\nu}=\dfrac{1}{\mu_0}\!\left(F^{\mu\alpha}{F_\alpha}^{\nu}+\tfrac14\eta^{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}\right)$ es **simétrico** y de **traza nula**.
> - Empaqueta en un solo objeto la densidad de energía $u$, el Poynting $\vec S$ y los esfuerzos $\sigma_{ij}$.
> - Su conservación $\partial_\mu T^{\mu\nu}=-{F^\nu}_{\lambda}J^{\lambda}$ reúne el teorema de Poynting ($\nu=0$) y la conservación del momento ($\nu=i$).
> - Es la **fuente del campo gravitatorio** en relatividad general.

> [!referencia] Bibliografía
> - Griffiths, D. J. *Introduction to Electrodynamics*, cap. 12 (electrodinámica relativista; tensor energía-momento).
> - Landau, L. D. & Lifshitz, E. M. *Teoría clásica de los campos* (Vol. 2), capítulos sobre el tensor energía-momento del campo electromagnético.
> - Notas relacionadas: [[Tensor de Campo]], [[Maxwell Covariante]], [[Energia y Momento]].
