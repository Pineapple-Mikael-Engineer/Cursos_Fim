---
title: Prolongación de Soluciones e Intervalo Maximal
tags:
  - ecuaciones
  - edo
  - teoria
  - fundamentos
  - prolongacion
draft: false
aliases:
  - prolongación de soluciones
  - intervalo maximal de existencia
  - explosión en tiempo finito
  - blow-up
  - continuation of solutions
  - maximal interval of existence
  - finite-time blow-up
---

# Prolongación de Soluciones e Intervalo Maximal

> [!definicion]
> El [[Existencia y Unicidad Picard | teorema de Picard]] solo da una solución **local**: vive en un
> intervalo pequeño $|x-x_0|\le h$ alrededor del dato inicial. Pero esa solución se puede **extender**:
> al llegar a un extremo del intervalo, ese extremo es un nuevo "dato inicial" desde el que volver a
> aplicar Picard y avanzar un poco más. Pegando todas las extensiones posibles se obtiene un único
> **intervalo maximal de existencia** $(\omega_-,\omega_+)$, el mayor abierto en el que la solución
> está definida. En cada extremo finito $\omega_\pm$ ocurre **forzosamente** una de dos cosas: o el
> intervalo es infinito ($\omega_+=+\infty$, $\omega_-=-\infty$), o la solución **escapa de todo
> compacto** del dominio de $f$ —típicamente $|y(x)|\to\infty$ (**explosión** o *blow-up*) o bien
> $(x,y(x))$ se acerca a la **frontera** del dominio donde $f$ deja de estar definida—. Lo que **no**
> puede pasar es que la solución simplemente "se pare" en medio del dominio con $\omega_+<\infty$
> estando acotada: si pudiera, se prolongaría.

> [!info]
> Cierra el bloque de [[index | fundamentos cualitativos]] respondiendo la pregunta "¿hasta dónde vive
> la solución?" (libro, teoría de prolongación y existencia global). Continúa el carácter **local** de
> [[Existencia y Unicidad Picard | Picard]] y usa la [[Desigualdad de Gronwall | desigualdad de
> Gronwall]] para descartar la explosión en el caso lineal. El ejemplo clave se resuelve por
> [[../Metodos de Primer Orden/Variables Separables | variables separables]]. Acompaña a
> [[Dependencia de Condiciones y Parametros | la dependencia respecto a los datos]] en la lista de
> propiedades "globales" de las soluciones.

---

## Ejemplo

> [!ejemplo] La explosión en tiempo finito: $y'=y^2,\ y(0)=1$
> Este es el ejemplo que conviene **memorizar**, porque desmiente la intuición ingenua de que "si la
> ecuación es bonita, la solución existe siempre". El campo $f(x,y)=y^2$ es un polinomio: continuo,
> derivable, **suave en todo el plano**, Lipschitz local en cualquier región acotada. Picard garantiza
> una única solución local. Resolvámosla por [[../Metodos de Primer Orden/Variables Separables |
> separables]]:
> $$\frac{dy}{y^2}=dx\ \Longrightarrow\ -\frac{1}{y}=x+C.$$
> Imponiendo $y(0)=1$: $-1/1=0+C\Rightarrow C=-1$, de modo que $-1/y=x-1$ y
> $$\boxed{\,y(x)=\frac{1}{1-x}\,}.$$
> Ahora la sorpresa: aunque $f=y^2$ es perfecta en **todas partes**, la solución tiene una **asíntota
> vertical** en $x=1$. Cuando $x\to 1^-$, $y(x)\to+\infty$: la solución **explota en tiempo finito**.
> El intervalo maximal hacia la derecha es por tanto $\omega_+=1$, y el intervalo completo es
> $$(\omega_-,\omega_+)=(-\infty,\,1).$$
> La moraleja es contundente: **la suavidad de $f$ solo compra existencia local**. La solución, al
> crecer, abandona toda región acotada del plano antes de llegar a $x=1$; no hay manera de prolongarla
> más allá porque sencillamente *ya no es finita*. El "tiempo de vida" $\omega_+=1$ depende del dato
> inicial: con $y(0)=y_0>0$ se obtiene $y=1/(1/y_0-x)$, que explota en $x=1/y_0$ —cuanto mayor el
> arranque, antes la catástrofe—.

---

## En qué consiste

> [!teoria] Construcción del intervalo maximal
> Partimos de la solución local que da [[Existencia y Unicidad Picard | Picard]] en $|x-x_0|\le h$.
> En el extremo derecho $x_1=x_0+h$ tenemos un nuevo punto $(x_1,y(x_1))$; si sigue dentro del dominio
> de $f$ y se cumplen las hipótesis de Picard, volvemos a aplicarlo y **continuamos** la solución un
> tramo más a la derecha. Repitiendo, generamos una cadena de extensiones. La **unión** de todas las
> soluciones que coinciden donde se solapan (la unicidad garantiza que coinciden) es una única solución
> definida en un intervalo **abierto maximal** $(\omega_-,\omega_+)$: maximal porque, por construcción,
> ya no admite ninguna prolongación. La pregunta interesante es entonces **qué impide seguir** al
> llegar a $\omega_+$ si este es finito.

> [!teorema] Lema de escape (prolongación)
> Sea $y$ la solución maximal del PVI $y'=f(x,y),\ y(x_0)=y_0$, con $f$ continua y Lipschitz local en
> un dominio abierto $\Omega$, y sea $(\omega_-,\omega_+)$ su intervalo maximal. Si $\omega_+<\infty$,
> entonces la trayectoria $(x,y(x))$ **abandona todo compacto** $K\subset\Omega$ cuando $x\to\omega_+^-$:
> para cada compacto $K$ existe un instante a partir del cual $(x,y(x))\notin K$. En particular, o bien
> $|y(x)|\to\infty$ (**explosión**), o bien $(x,y(x))$ tiende a la **frontera** $\partial\Omega$.
> Recíprocamente —y es la versión útil en la práctica—: **si la solución permanece dentro de un
> compacto $K\subset\Omega$ cuando $x\to\omega_+^-$, entonces $\omega_+=+\infty$** (no puede haber
> extremo finito). El mismo enunciado vale, simétricamente, para $\omega_-$.

> [!demostracion]
> Probamos la forma contrapositiva: si la solución se queda en un compacto cerca de $\omega_+$,
> entonces $\omega_+$ **no puede ser finito**.
>
> **Paso 1 — el límite $\lim_{x\to\omega_+^-}y(x)$ existe.** Supongamos $\omega_+<\infty$ y que
> $(x,y(x))$ permanece en un compacto $K\subset\Omega$ para $x$ cerca de $\omega_+$. Sobre el compacto
> $K$ la función continua $f$ está **acotada**: $|f(x,y)|\le M$. Como $y'=f$, la solución es
> Lipschitz con esa misma constante $M$: para $x_0\le s<t<\omega_+$,
> $$|y(t)-y(s)|=\Bigl|\int_s^t f(\tau,y(\tau))\,d\tau\Bigr|\le M\,(t-s).$$
> Cuando $s,t\to\omega_+^-$ el lado derecho $\to 0$, así que $\{y(x)\}$ es de **Cauchy** y existe el
> límite finito $y^\*:=\lim_{x\to\omega_+^-}y(x)$. El punto $(\omega_+,y^\*)$ pertenece a $K\subset\Omega$
> (compacto, luego cerrado), es decir, **sigue dentro del dominio** de $f$.
>
> **Paso 2 — se prolonga, contradiciendo la maximalidad.** Como $(\omega_+,y^\*)\in\Omega$ y allí
> $f$ es continua y Lipschitz local, aplicamos [[Existencia y Unicidad Picard | Picard]] al PVI
> $y'=f(x,y),\ y(\omega_+)=y^\*$: existe solución en un entorno $[\omega_+,\omega_++\delta]$. Pegándola
> con la anterior (coinciden en $\omega_+$ por continuidad, y la unicidad las hace una sola) obtenemos
> una solución definida **más allá** de $\omega_+$. Pero eso contradice que $(\omega_-,\omega_+)$ fuera
> **maximal**. Luego la hipótesis $\omega_+<\infty$ era imposible: necesariamente $\omega_+=+\infty$.
> Equivalentemente, si $\omega_+<\infty$, la solución **no** podía haberse quedado en ningún compacto,
> es decir, escapó de todos ellos. $\blacksquare$

> [!info] Cómo se lee el lema en la práctica
> El lema convierte la pregunta abstracta "¿hasta dónde vive la solución?" en un test concreto:
> **basta acotar la solución** para garantizar que existe globalmente. Si por algún argumento (una
> energía, una cota *a priori*, una desigualdad de Gronwall) se demuestra que $|y(x)|$ no puede
> dispararse, entonces $\omega_+=+\infty$ automáticamente. Toda la teoría de existencia global se
> reduce a **encontrar cotas que impidan la explosión**.

> [!proposicion] Las EDO lineales no explotan: existencia global
> Para la **EDO lineal** de primer orden
> $$y'+p(x)\,y=q(x),\qquad p,q\ \text{continuas en un intervalo } I,$$
> toda solución existe en **todo** $I$: el intervalo maximal es el propio $I$, sin explosión interna.
> La razón es que el crecimiento de $y$ está controlado linealmente por la propia $y$, y eso —vía
> [[Desigualdad de Gronwall | Gronwall]]— **impide** el blow-up. En forma de cota: escribiendo
> $y(x)=y_0+\int_{x_0}^x[q(t)-p(t)y(t)]\,dt$, sobre cualquier subintervalo compacto $[a,b]\subset I$
> donde $|p|\le P$ y $|q|\le Q$ se tiene $|y(x)|\le \bigl(|y_0|+Q(b-a)\bigr)e^{P|x-x_0|}$, que es
> **finita** en todo $[a,b]$. La solución no puede escaparse a infinito en tiempo finito; se queda
> acotada en cada compacto y, por el lema de escape, vive en todo $I$. La **linealidad mata la
> explosión**.

> [!warning]
> **Suavidad de $f$ NO implica existencia global.** Que $f$ sea continua, derivable o incluso de clase
> $C^\infty$ en todo el plano solo garantiza existencia **local** (y, con Lipschitz, unicidad local).
> El ejemplo $y'=y^2$ es la prueba: $f$ es un polinomio perfecto y, aun así, la solución explota en
> $x=1$. La explosión proviene del **crecimiento superlineal** del campo en $y$ (aquí cuadrático), no
> de ninguna patología de regularidad. Para asegurar existencia global hace falta un control extra
> sobre el *tamaño* de $f$ (crecimiento a lo más lineal en $y$, una cota de energía, etc.), no más
> derivadas.

## Interpretación física

> [!teoria] El blow-up como catástrofe del modelo
> En muchos modelos, una realimentación positiva produce un término del tipo $y'\sim y^2$: la tasa de
> crecimiento crece con la propia magnitud. El resultado es la **explosión en tiempo finito**: la
> variable se hace infinita en un instante $\omega_+$ concreto y *anterior* al que ingenuamente se
> esperaría. Aparece en combustión, en reacciones autocatalíticas, en colapso gravitatorio o en ciertos
> modelos de población sin saturación. El instante $\omega_+$ es físicamente significativo: marca el
> límite de validez del modelo —más allá hay que añadir mecanismos de saturación (un término $-y^3$,
> por ejemplo) que devuelvan la existencia global—. Que las EDO **lineales** no exploten es la otra
> cara: los sistemas lineales son "dóciles", su respuesta nunca se dispara a infinito en tiempo finito.

## Resumen

> [!resumen]
> | Concepto | Enunciado | Consecuencia |
> |---|---|---|
> | Intervalo maximal | mayor abierto $(\omega_-,\omega_+)$ donde vive la solución | único, por pegado |
> | Lema de escape | si $\omega_+<\infty$, la solución abandona todo compacto | explota o toca $\partial\Omega$ |
> | Test de globalidad | si la solución se queda en un compacto $\Rightarrow \omega_+=+\infty$ | basta acotar $\|y\|$ |
> | Ejemplo blow-up | $y'=y^2,\ y(0)=1\Rightarrow y=\tfrac{1}{1-x}$ | explota en $x=1$; maximal $(-\infty,1)$ |
> | Caso lineal | $y'+p\,y=q$ con $p,q$ continuas en $I$ | solución global en todo $I$ (vía [[Desigualdad de Gronwall\|Gronwall]]) |
> | No lineal | crecimiento superlineal en $y$ | **puede** explotar en tiempo finito |

> [!corolario]
> La existencia es, por defecto, un fenómeno **local**: la suavidad del campo no la hace global. La
> frontera entre "vive un rato" y "vive siempre" la decide el **crecimiento** del campo, no su
> regularidad. Por eso el caso lineal es excepcionalmente bueno —nunca explota— y el caso no lineal
> exige, antes de hablar de la solución "para todo $x$", una cota *a priori* que descarte el blow-up.

> [!referencia]
> - El teorema local que se prolonga: [[Existencia y Unicidad Picard]].
> - La herramienta que descarta la explosión: [[Desigualdad de Gronwall]].
> - El método que resuelve el ejemplo estrella: [[../Metodos de Primer Orden/Variables Separables]].
> - La otra propiedad global de las soluciones: [[Dependencia de Condiciones y Parametros]].
> - Marco general: [[index]].
