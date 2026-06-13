---
title: Energía de la Onda
tags:
  - ecuaciones
  - edp
  - teoria
  - onda
  - energia
draft: false
aliases:
  - energía de la onda
  - conservación de la energía
  - método de energía onda
  - wave energy
  - energy conservation
---

# Energía de la Onda

> [!definicion]
> A una solución de la ecuación de onda $u_{tt}=c^2u_{xx}$ se le asocia la **energía**
> $$E(t)=\frac12\int \big(u_t^2+c^2u_x^2\big)\,dx,$$
> suma de una parte **cinética** $\tfrac12 u_t^2$ (qué tan rápido se mueve cada punto) y una parte
> **potencial** $\tfrac12 c^2u_x^2$ (cuánto está estirada/curvada la cuerda). Para extremos **fijos**
> o **libres**, esa energía **se conserva**: $E'(t)=0$.

> [!info]
> Es el rasgo dinámico que distingue a la [[Ecuacion de Onda/index| onda]] del
> [[Ecuacion del Calor/index| calor]]: la onda **conserva**, el calor **disipa**. La conservación se
> hereda de los [[Separacion Onda y Modos Normales| modos normales]] (que oscilan sin decaer) y es la
> base del [[Metodo de Energia Unicidad| método de energía]] para probar unicidad de soluciones de
> EDP.

---

## Ejemplo

> [!ejemplo] Una cuerda fija no pierde energía
> Toma una cuerda con extremos fijos $u(0,t)=u(L,t)=0$ y descompónla en modos normales (ver
> [[Separacion Onda y Modos Normales]]):
> $u=\sum_n \operatorname{sen}\frac{n\pi x}{L}\,[a_n\cos\omega_n t+b_n\operatorname{sen}\omega_n t]$.
> Al sustituir en $E(t)$ y usar la ortogonalidad de los senos, los términos cruzados se anulan y la
> energía de cada modo resulta constante en el tiempo:
> $$E=\frac{L}{4}\sum_{n=1}^\infty \omega_n^2\,(a_n^2+b_n^2),\qquad \omega_n=\frac{n\pi c}{L}.$$
> Dentro de **cada** modo la energía oscila entre cinética y potencial (como un péndulo entre velocidad
> y altura), pero la **suma** $u_t^2+c^2u_x^2$ integrada se mantiene fija: la cuerda jamás se detiene
> sola. Esto contrasta de plano con el calor, donde la "energía" análoga $\int u^2$ **decae** hacia
> cero. La conservación es la firma de que la onda es **hiperbólica** y no parabólica.

## En qué consiste

> [!teorema] Conservación de la energía
> Si $u$ resuelve $u_{tt}=c^2u_{xx}$ en $[0,L]$ con extremos **fijos** ($u_t=0$ en los bordes) o
> **libres** ($u_x=0$ en los bordes), entonces $E(t)=\tfrac12\int_0^L (u_t^2+c^2u_x^2)\,dx$ es
> **constante**: $E'(t)=0$.

> [!demostracion]
> **Paso 1 — Derivar la energía bajo la integral.**
> Derivando respecto de $t$ y metiendo la derivada dentro de la integral,
> $$E'(t)=\int_0^L \big(u_t\,u_{tt}+c^2 u_x\,u_{xt}\big)\,dx.$$
>
> **Paso 2 — Usar la ecuación e integrar por partes.**
> Sustituimos $u_{tt}=c^2u_{xx}$ en el primer sumando y aplicamos integración por partes al segundo
> (con $u_{xt}=\partial_x u_t$):
> $$\int_0^L c^2 u_x\,u_{xt}\,dx=\Big[c^2 u_x\,u_t\Big]_0^L-\int_0^L c^2 u_{xx}\,u_t\,dx.$$
> Por tanto
> $$E'(t)=\int_0^L c^2 u_{xx}\,u_t\,dx+\Big[c^2u_xu_t\Big]_0^L-\int_0^L c^2u_{xx}\,u_t\,dx
> =\Big[c^2u_xu_t\Big]_0^L.$$
>
> **Paso 3 — Anular el término de frontera.**
> El corchete se evalúa en los extremos. Con extremos **fijos**, $u(0,t)=u(L,t)=0$ para todo $t$, así
> que $u_t=0$ ahí; con extremos **libres**, $u_x=0$ ahí. En ambos casos el producto $u_xu_t$ se anula
> en $x=0$ y $x=L$, de modo que
> $$E'(t)=0.\qquad\blacksquare$$
> Las dos integrales de volumen se cancelaron exactamente entre sí; lo único que podía estropear la
> conservación era el flujo por la frontera, y las condiciones de contorno lo apagan.

> [!proposicion] Unicidad por energía
> La conservación de la energía da **gratis** la unicidad de soluciones. Supongamos dos soluciones
> $u_1,u_2$ con los **mismos** datos iniciales y de frontera. Su diferencia $w=u_1-u_2$ resuelve la
> misma ecuación con datos **nulos**: $w(x,0)=0$ y $w_t(x,0)=0$. Entonces:
> 1. $E_w(0)=\tfrac12\int(w_t^2+c^2w_x^2)\big|_{t=0}=0$, porque $w_t=0$ y $w_x=0$ en $t=0$ (la última,
>    por ser $w(\cdot,0)\equiv0$).
> 2. Por el teorema, $E_w(t)$ es **constante**, luego $E_w(t)=0$ para todo $t$.
> 3. Pero $E_w$ es una integral de cuadrados; si es cero, el integrando es cero: $w_t\equiv0$ y
>    $w_x\equiv0$ en todas partes. Así $w$ es constante, y como vale $0$ en $t=0$, $w\equiv0$.
>
> Por tanto $u_1=u_2$: **la solución es única**. Este argumento es el corazón del
> [[Metodo de Energia Unicidad| método de energía]].

> [!info] Conservar frente a decaer
> La energía es la huella que separa los dos tipos de EDP de evolución. En la **onda** (hiperbólica),
> $E$ se conserva: el sistema es reversible y no hay flecha del tiempo. En el **calor** (parabólica),
> la cantidad análoga $\int u^2$ **decae** monótonamente hacia cero, reflejando la disipación
> irreversible. Misma estrategia (multiplicar por la derivada temporal e integrar por partes), dos
> destinos opuestos: ese contraste **conservación vs decaimiento** es la firma de **hiperbólica vs
> parabólica**.

## Resumen

> [!resumen]
> | Cantidad | Expresión / propiedad |
> |---|---|
> | Energía | $E(t)=\tfrac12\int (u_t^2+c^2u_x^2)\,dx$ |
> | Cinética / potencial | $\tfrac12 u_t^2$ y $\tfrac12 c^2u_x^2$ |
> | Conservación | $E'(t)=0$ (extremos fijos o libres) |
> | Clave de la prueba | sustituir $u_{tt}=c^2u_{xx}$ + integrar por partes |
> | Consecuencia | unicidad: datos iguales $\Rightarrow$ $w\equiv0$ |

> [!corolario]
> La ecuación de onda es **conservativa**: lo que se le entrega de energía permanece, repartiéndose
> entre cinética y potencial pero sin fugarse. Esa conservación, además de su lectura física, es una
> herramienta matemática potente: convierte la unicidad de soluciones en un cálculo de tres líneas.

> [!referencia]
> - Los modos que oscilan sin decaer: [[Separacion Onda y Modos Normales]].
> - El método general de unicidad: [[Metodo de Energia Unicidad]].
> - El panorama de la sección: [[Ecuacion de Onda/index]].
