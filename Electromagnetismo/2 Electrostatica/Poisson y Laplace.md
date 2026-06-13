---
title: Poisson y Laplace
tags:
  - electromagnetismo
  - teoria
  - electrostatica
draft: false
aliases:
  - Ecuación de Poisson
  - Ecuación de Laplace
  - Método de imágenes
---

# Poisson y Laplace $\nabla^2 V=-\dfrac{\rho}{\varepsilon_0}$

> [!definicion]
> El potencial electrostático $V(\vec r)$ satisface la **ecuación de Poisson**:
> $$\boxed{\ \nabla^2 V=-\frac{\rho}{\varepsilon_0}\ }$$
> donde $\nabla^2=\nabla\cdot\nabla=\partial_x^2+\partial_y^2+\partial_z^2$ es el **laplaciano** y $\rho$ la densidad volumétrica de carga. En toda región **sin carga** ($\rho=0$) se reduce a la **ecuación de Laplace**:
> $$\boxed{\ \nabla^2 V=0\ }$$
> Las soluciones de Laplace se llaman **funciones armónicas**. Resolver la electrostática con condiciones de frontera (potenciales o cargas fijados en los bordes) es, en esencia, resolver Poisson/Laplace.

---

> [!info]
> Cuarta nota de la sección [[2 Electrostatica/index | Electrostática]]. Es la **vía potencial** llevada al límite: en lugar de integrar $\rho$ conocida, se resuelve una EDP con datos en la frontera. Hermanas: [[Potencial Electrico]] (define $V$ y $\vec E=-\nabla V$) y [[Conductores]] (la frontera típica: superficies equipotenciales). Usa la herramienta [[Delta de Dirac y Singularidades]] para tratar las cargas puntuales como fuentes localizadas. Referencia: Griffiths, *Introduction to Electrodynamics*, cap. 3.

---

## En qué consiste

> [!teoria] De Gauss a Poisson
> Toda la electrostática se condensa en dos ecuaciones locales: $\nabla\cdot\vec E=\rho/\varepsilon_0$ (Gauss) y $\nabla\times\vec E=\vec 0$ (campo conservativo). La segunda garantiza que existe un **potencial** $V$ con $\vec E=-\nabla V$. Sustituyendo en la primera se obtiene **una sola ecuación escalar** para $V$: la de Poisson. La gran ventaja es que pasamos de buscar tres funciones ($E_x,E_y,E_z$) a buscar **una** ($V$), y luego derivamos.

> [!demostracion] Deducción de la ecuación de Poisson
> **Paso 1 —** Partimos de la primera ecuación de Maxwell estática (ley de Gauss diferencial):
> $$\nabla\cdot\vec E=\frac{\rho}{\varepsilon_0}.$$
>
> **Paso 2 —** Como $\nabla\times\vec E=\vec 0$, el campo deriva de un potencial escalar:
> $$\vec E=-\nabla V.$$
>
> **Paso 3 —** Sustituimos $\vec E$ en Gauss:
> $$\nabla\cdot(-\nabla V)=\frac{\rho}{\varepsilon_0}\;\Longrightarrow\; -\nabla\cdot(\nabla V)=\frac{\rho}{\varepsilon_0}.$$
>
> **Paso 4 —** Por definición $\nabla\cdot\nabla=\nabla^2$, de modo que
> $$\nabla^2 V=-\frac{\rho}{\varepsilon_0}.$$
> En una región de **vacío de carga** ($\rho=0$) queda $\nabla^2 V=0$, la ecuación de Laplace. $\blacksquare$

> [!proposicion] Por qué importa Laplace
> En la práctica casi nunca conocemos $\rho$ en toda la región: conocemos el potencial en unos conductores (sus bordes) y queremos $V$ en el **espacio vacío** entre ellos. Allí $\rho=0$, así que $V$ es **armónica** y el problema se reduce a Laplace con condiciones de frontera. Las dos propiedades siguientes explican por qué esas soluciones son tan "suaves" y tan únicas.

---

## Propiedades de las funciones armónicas

> [!teorema] Propiedad del valor medio
> Si $\nabla^2 V=0$ en una región, el valor de $V$ en cualquier punto $P$ es **igual al promedio** de $V$ sobre la superficie de cualquier esfera centrada en $P$ (siempre que la esfera esté contenida en la región sin carga):
> $$V(P)=\frac{1}{4\pi R^2}\oint_{S_R} V\,dA.$$

> [!demostracion] Valor medio mediante el flujo
> Sea una esfera $S_R$ de radio $R$ centrada en el punto $P$, en una región **sin carga encerrada**.
>
> **Paso 1 —** Por la ley de Gauss, el flujo de $\vec E$ que atraviesa $S_R$ es proporcional a la carga encerrada, que es nula:
> $$\oint_{S_R}\vec E\cdot d\vec A=\frac{Q_{\text{enc}}}{\varepsilon_0}=0.$$
>
> **Paso 2 —** Sobre la esfera, $d\vec A=\hat r\,dA$ y $\vec E\cdot\hat r=E_r=-\partial_r V$. El flujo se escribe
> $$\oint_{S_R}\vec E\cdot d\vec A=-\oint_{S_R}\frac{\partial V}{\partial r}\,dA=0.$$
>
> **Paso 3 —** Definimos el **valor promedio** de $V$ sobre la esfera de radio $R$:
> $$\bar V(R)=\frac{1}{4\pi R^2}\oint_{S_R} V\,dA.$$
> Conviene parametrizar por el ángulo sólido $d\Omega=dA/R^2$, de modo que $\bar V(R)=\dfrac{1}{4\pi}\displaystyle\int V\,d\Omega$, donde la integral angular **no** depende de $R$.
>
> **Paso 4 —** Derivamos $\bar V$ respecto de $R$. Como el dominio angular es fijo, la derivada entra en la integral:
> $$\frac{d\bar V}{dR}=\frac{1}{4\pi}\int\frac{\partial V}{\partial r}\,d\Omega=\frac{1}{4\pi R^2}\oint_{S_R}\frac{\partial V}{\partial r}\,dA.$$
> Por el **Paso 2**, esa integral de superficie es cero, así que
> $$\frac{d\bar V}{dR}=0.$$
>
> **Paso 5 —** Luego $\bar V(R)$ es **constante** en $R$. Tomando el límite $R\to 0$, la esfera colapsa al punto $P$ y el promedio tiende a $V(P)$. Por tanto, para todo $R$,
> $$\bar V(R)=V(P)\quad\Longrightarrow\quad V(P)=\frac{1}{4\pi R^2}\oint_{S_R}V\,dA.\qquad\blacksquare$$

> [!corolario] No hay máximos ni mínimos locales
> Una función armónica **no puede** tener un máximo ni un mínimo local en el interior de la región. Si $V(P)$ fuera, por ejemplo, un máximo estricto, entonces $V(P)$ sería **mayor** que el valor en todos los puntos de una esfera pequeña a su alrededor; pero el valor medio sobre esa esfera no puede superar al máximo de los valores promediados, contradiciendo $V(P)=\bar V(R)$. En consecuencia, los **extremos de $V$ están siempre en la frontera**. Físicamente: una carga de prueba en equilibrio en el vacío sería inestable (teorema de Earnshaw).

---

## Teorema de unicidad

> [!teorema] Unicidad de Dirichlet
> Si el potencial $V$ está **especificado en toda la frontera** $S$ de una región (problema de Dirichlet), entonces la solución de la ecuación de Poisson $\nabla^2 V=-\rho/\varepsilon_0$ en el interior es **única**.

> [!demostracion] Unicidad por la energía de la diferencia
> Supongamos que existen **dos** soluciones $V_1$ y $V_2$ con la misma $\rho$ y el mismo dato en la frontera.
>
> **Paso 1 —** Definimos la diferencia $W=V_1-V_2$. Como ambas cumplen Poisson con la misma $\rho$:
> $$\nabla^2 W=\nabla^2V_1-\nabla^2V_2=-\frac{\rho}{\varepsilon_0}+\frac{\rho}{\varepsilon_0}=0.$$
> Así, $W$ es **armónica**. Además, como ambas valen lo mismo en $S$, se tiene $W=0$ **en toda la frontera**.
>
> **Paso 2 —** Usamos la identidad vectorial (regla del producto para la divergencia):
> $$\nabla\cdot(W\,\nabla W)=(\nabla W)\cdot(\nabla W)+W\,\nabla^2 W=|\nabla W|^2+W\,\nabla^2 W.$$
> Como $\nabla^2 W=0$, el último término desaparece:
> $$\nabla\cdot(W\,\nabla W)=|\nabla W|^2.$$
>
> **Paso 3 —** Integramos sobre el volumen $\mathcal V$ y aplicamos el **teorema de la divergencia** al miembro izquierdo:
> $$\int_{\mathcal V}|\nabla W|^2\,dV=\int_{\mathcal V}\nabla\cdot(W\,\nabla W)\,dV=\oint_{S}(W\,\nabla W)\cdot d\vec A.$$
>
> **Paso 4 —** En la frontera $S$ tenemos $W=0$, así que el integrando de la superficie se anula punto a punto. Por tanto el flujo es cero y queda
> $$\int_{\mathcal V}|\nabla W|^2\,dV=0.$$
>
> **Paso 5 —** El integrando $|\nabla W|^2\ge 0$ es no negativo; una integral nula de algo no negativo obliga a
> $$|\nabla W|^2=0\;\Longrightarrow\;\nabla W=\vec 0\;\Longrightarrow\;W=\text{cte}.$$
>
> **Paso 6 —** Pero $W=0$ en la frontera y es constante; esa constante debe ser $0$ en todo el volumen. Luego
> $$W=0\;\Longrightarrow\;V_1=V_2.$$
> Las dos soluciones coinciden: la solución es **única**. $\blacksquare$

> [!regla] Para qué sirve la unicidad
> La unicidad transforma la electrostática en un juego de **adivinar y verificar**: si por cualquier medio (intuición, simetría, una carga ficticia) hallamos **una** función que (1) satisface Poisson en la región física y (2) reproduce el dato de frontera, entonces es **LA** solución, sin más. Esto es exactamente lo que legitima el método de imágenes.

---

## Método de imágenes

> [!teoria] La idea
> Consideremos una carga puntual $+q$ situada a una distancia $d$ de un **plano conductor infinito conectado a tierra** ($V=0$). El conductor reacomoda su carga libre creando una densidad inducida $\sigma$ desconocida, y queremos el potencial en el semiespacio que contiene la carga. El truco: **retiramos el plano** y lo reemplazamos por una **carga imagen** $-q$ colocada en la posición especular, a distancia $d$ al otro lado. El nuevo problema (dos cargas en el vacío) es trivial, y por unicidad da la misma respuesta en la región física.

![[imagenes.svg|440]]
*Carga real $+q$ a distancia $d$ del plano conductor a tierra ($V=0$). El método sustituye el plano por la carga imagen $-q$ en la posición especular; en la región física ($z>0$) el potencial coincide con el del problema original. Las distancias $r_+$ y $r_-$ van del punto de campo a la carga real y a la imagen.*

> [!demostracion] El potencial imagen resuelve el problema original
> Colocamos $+q$ en $(0,0,d)$, la imagen $-q$ en $(0,0,-d)$, y el plano conductor en $z=0$. Para un punto $\vec r=(x,y,z)$ definimos
> $$r_+=\sqrt{x^2+y^2+(z-d)^2},\qquad r_-=\sqrt{x^2+y^2+(z+d)^2}.$$
> El potencial propuesto en la región física $z>0$ es
> $$V(\vec r)=\frac{1}{4\pi\varepsilon_0}\left(\frac{q}{r_+}-\frac{q}{r_-}\right).$$
>
> **Paso 1 (frontera) —** Sobre el plano $z=0$ se cumple $r_+=\sqrt{x^2+y^2+d^2}=r_-$, los dos términos son iguales y opuestos:
> $$V(z=0)=\frac{1}{4\pi\varepsilon_0}\left(\frac{q}{r_+}-\frac{q}{r_+}\right)=0.$$
> El dato de frontera ($V=0$ en el conductor a tierra) **se cumple**. En el infinito $V\to 0$, lo que también es correcto.
>
> **Paso 2 (Poisson en la región física) —** En el semiespacio $z>0$, la **única** carga presente es la real $+q$ (la imagen está en $z<0$, **fuera** de la región física). El potencial propuesto satisface, para $z>0$:
> $$\nabla^2 V=-\frac{\rho_{\text{real}}}{\varepsilon_0},$$
> con $\rho_{\text{real}}$ la sola carga puntual $+q$, exactamente la ecuación de Poisson del problema original.
>
> **Paso 3 (unicidad) —** Tenemos una función que satisface Poisson en la región física **y** reproduce el dato de frontera ($V=0$ en $z=0$). Por el **teorema de unicidad**, es LA solución del problema con el conductor. $\blacksquare$

> [!solucion] Densidad de carga inducida en el plano
> El campo perpendicular en la cara del conductor determina $\sigma$ vía $\sigma=-\varepsilon_0\,\partial V/\partial z$ evaluado en $z=0$. Derivando $V$ y evaluando en el plano se obtiene
> $$\sigma(s)=-\frac{q\,d}{2\pi\,(s^2+d^2)^{3/2}},\qquad s=\sqrt{x^2+y^2},$$
> una densidad **negativa** (la carga $+q$ atrae carga negativa hacia el punto más cercano del plano), máxima justo bajo la carga ($s=0$) y que decae al alejarse. Integrándola sobre todo el plano se recupera $\displaystyle\int\sigma\,dA=-q$: la carga inducida total iguala a la imagen, como debía.

> [!demostracion] Fuerza sobre la carga real
> La carga $+q$ siente el campo de **toda** la carga inducida del plano. Por el método de imágenes, ese campo en la posición de $+q$ es idéntico al que produciría la imagen $-q$ situada a distancia $2d$ (de $z=+d$ a $z=-d$).
>
> **Paso 1 —** La separación entre la carga y su imagen es $2d$. La fuerza es la de Coulomb entre $+q$ y $-q$:
> $$\vec F=\frac{1}{4\pi\varepsilon_0}\frac{q\,(-q)}{(2d)^2}\,\hat z=-\frac{1}{4\pi\varepsilon_0}\frac{q^2}{4d^2}\,\hat z.$$
>
> **Paso 2 —** La componente, tomando $\hat z$ alejándose del plano, es
> $$F=-\frac{1}{4\pi\varepsilon_0}\frac{q^2}{(2d)^2}<0,$$
> es decir, **atractiva**: la carga es atraída hacia el plano conductor. $\blacksquare$

> [!ejemplo] Carga puntual frente a un plano conductor a tierra
> **Enunciado.** Una carga $q=2{,}0$ nC está a $d=3{,}0$ cm de un plano conductor infinito conectado a tierra. Halla la fuerza sobre la carga.
>
> **Solución.**
>
> **Paso 1 —** Por imágenes, equivale a una carga $-q$ a distancia $2d=6{,}0$ cm. La magnitud de la fuerza es
> $$|F|=\frac{1}{4\pi\varepsilon_0}\frac{q^2}{(2d)^2}.$$
>
> **Paso 2 —** Con $\dfrac{1}{4\pi\varepsilon_0}=8{,}99\times10^{9}\ \text{N·m}^2/\text{C}^2$, $q=2{,}0\times10^{-9}$ C y $2d=6{,}0\times10^{-2}$ m:
> $$|F|=8{,}99\times10^{9}\cdot\frac{(2{,}0\times10^{-9})^2}{(6{,}0\times10^{-2})^2}=8{,}99\times10^{9}\cdot\frac{4{,}0\times10^{-18}}{3{,}6\times10^{-3}}.$$
>
> **Paso 3 —** Operando:
> $$|F|\approx 9{,}99\times10^{-6}\ \text{N}\approx 1{,}0\times10^{-5}\ \text{N},$$
> dirigida **hacia el plano** (atractiva). La carga se "ve" atraída por su propia imagen.

> [!warning] La energía NO es la del par real
> Es tentador escribir la energía como la de un par carga–imagen, $-\dfrac{1}{4\pi\varepsilon_0}\dfrac{q^2}{2d}$, pero **es incorrecto**: en el sistema físico hay **una sola** carga real; la imagen es una ficción de cálculo. La energía correcta se obtiene **integrando la fuerza** al traer la carga desde el infinito hasta la distancia $d$. Tomando la fuerza atractiva $F(z)=-\dfrac{1}{4\pi\varepsilon_0}\dfrac{q^2}{(2z)^2}$ y calculando el trabajo:
> $$W=-\int_{\infty}^{d}F(z)\,dz=-\int_{\infty}^{d}\frac{1}{4\pi\varepsilon_0}\frac{q^2}{4z^2}\,dz=-\frac{1}{4\pi\varepsilon_0}\frac{q^2}{4d}.$$
> Resulta la **mitad** de la energía del par real $-\dfrac{1}{4\pi\varepsilon_0}\dfrac{q^2}{2d}$: el factor $\tfrac12$ aparece porque al mover la carga real la imagen también se mueve, y la región $z<0$ no es física (no almacena energía de campo).

---

## Resumen

> [!resumen]
> | Concepto | Expresión | Idea clave |
> | --- | --- | --- |
> | Ecuación de Poisson | $\nabla^2 V=-\dfrac{\rho}{\varepsilon_0}$ | De $\nabla\cdot\vec E=\rho/\varepsilon_0$ y $\vec E=-\nabla V$ |
> | Ecuación de Laplace | $\nabla^2 V=0$ | Región sin carga; $V$ armónica |
> | Valor medio | $V(P)=\dfrac{1}{4\pi R^2}\oint V\,dA$ | $V$ es el promedio sobre esferas |
> | Sin extremos internos | máx./mín. en la frontera | inestabilidad de Earnshaw |
> | Unicidad (Dirichlet) | $V$ fijo en $S\Rightarrow$ solución única | $\int\|\nabla W\|^2dV=0$ |
> | Imágenes (plano a tierra) | $V=\dfrac{1}{4\pi\varepsilon_0}\!\left(\dfrac{q}{r_+}-\dfrac{q}{r_-}\right)$ | $-q$ especular; $V=0$ en el plano |
> | Fuerza sobre $q$ | $F=-\dfrac{1}{4\pi\varepsilon_0}\dfrac{q^2}{(2d)^2}$ | atractiva, hacia el plano |
> | Densidad inducida | $\sigma=-\dfrac{q\,d}{2\pi(s^2+d^2)^{3/2}}$ | $\int\sigma\,dA=-q$ |
> | Energía del sistema | $W=-\dfrac{1}{4\pi\varepsilon_0}\dfrac{q^2}{4d}$ | mitad del par real |

> [!corolario] El programa de la teoría de potencial
> Poisson/Laplace cierra la **vía potencial** del capítulo: en vez de integrar $\rho$, se resuelve una EDP escalar con datos de frontera. La unicidad convierte cualquier solución hallada en LA solución, y el método de imágenes la explota para reemplazar conductores por cargas ficticias. Este mismo esquema —EDP, condiciones de frontera, unicidad— reaparece en [[Conductores]], en magnetostática (potencial vectorial $\vec A$) y en toda la física matemática de campos.

> [!referencia]
> Griffiths, *Introduction to Electrodynamics*, cap. 3 (Potenciales especiales: Laplace, unicidad, imágenes, separación de variables). Para mayor profundidad y la función de Green: Jackson, *Classical Electrodynamics*, caps. 1–2.
