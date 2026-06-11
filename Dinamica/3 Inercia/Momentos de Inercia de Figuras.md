---
title: Momentos de Inercia de Figuras
tags:
  - dinamica
  - teoria
  - inercia
draft: false
aliases:
  - momentos de inercia de cuerpos comunes
  - radio de giro
  - moments of inertia table
---

# Momentos de Inercia de Figuras

> [!definicion]
> El **momento de inercia de masa** de un cuerpo respecto a un eje es
> $$I=\int r^2\,dm,$$
> donde $r$ es la distancia de cada elemento de masa $dm$ **al eje**. Es la "masa rotacional": cuanto
> mayor es $I$, más cuesta cambiar el estado de giro del cuerpo. Para los cuerpos comunes (varilla,
> disco, esfera…) está **tabulado**, casi siempre respecto a un eje que pasa por el **centro de masa**.
> El **radio de giro**
> $$k=\sqrt{\dfrac{I}{m}}$$
> es la distancia al eje a la que habría que concentrar **toda** la masa $m$ para reproducir el mismo
> $I$ (es decir, $I=mk^2$). NO confundir este $I$ con el **momento de inercia de área** $I=\int r^2\,dA$,
> que sirve para la flexión de vigas y **no** para la dinámica de rotación.

> [!info]
> Cierra la [[3 Inercia/index | inercia]] con los **valores prácticos** que se usan a diario: una vez
> tabulado $I$ en el centro de masa, se combina con el [[Teorema del Eje Paralelo]] para llevarlo a
> cualquier otro eje paralelo. Estos números son el catálogo de referencia para el
> [[Tensor de Inercia]] de cuerpos con simetría. Referencia: Hibbeler / Beer, apéndice de propiedades
> geométricas.

---

## Ejemplo

Deducimos de cero el valor más usado: el de la **varilla**.

Varilla uniforme de masa $m$ y longitud $L$, eje que pasa por su **centro** y es perpendicular a la
varilla. La masa se reparte por igual a lo largo de la longitud, así que la **densidad lineal** es
constante, $\lambda=m/L$, y un trozo de longitud $dx$ situado a distancia $x$ del centro tiene
$dm=\lambda\,dx$. Como el eje es perpendicular y pasa por el centro, la distancia de ese trozo al eje
es justamente $|x|$, con $x$ recorriendo $[-L/2,\,L/2]$:
$$
I=\int_{-L/2}^{L/2}x^2\,\lambda\,dx
 =\lambda\,\frac{x^3}{3}\Bigg|_{-L/2}^{L/2}
 =\frac{\lambda}{3}\left[\left(\frac{L}{2}\right)^3-\left(-\frac{L}{2}\right)^3\right]
 =\frac{\lambda}{3}\cdot\frac{L^3}{4}
 =\frac{\lambda L^3}{12}.
$$
Sustituyendo $\lambda=m/L$ queda $I=\dfrac{(m/L)L^3}{12}=\dfrac{1}{12}mL^2$.

> [!solucion]
> $$I=\frac{1}{12}mL^2,\qquad k=\sqrt{\frac{I}{m}}=\sqrt{\frac{L^2}{12}}=\frac{L}{\sqrt{12}}.$$
> Toda la masa de la varilla equivale, para rotar, a un punto a distancia $k=L/\sqrt{12}\approx0{,}289\,L$
> del centro.

---

## En qué consiste

> [!teoria] Cómo se usa la tabla
> Cada entrada de la tabla es una integral $\int r^2\,dm$ ya resuelta para una geometría con masa
> uniforme. El procedimiento de trabajo es siempre el mismo:
> 1. Identificar la figura y el eje que coinciden con el problema; leer $I$ en la tabla (está en el
>    **CM** salvo indicación).
> 2. Si el eje real es **paralelo** pero no pasa por el CM, aplicar el [[Teorema del Eje Paralelo]],
>    $I=I_{cm}+md^2$.
> 3. Para un cuerpo compuesto, **sumar** los $I$ de cada parte respecto al **mismo** eje (la integral
>    es aditiva).
>
> Todas las entradas se deducen por el mismo método del ejemplo: elegir la densidad ($\lambda$, $\sigma$
> o $\rho$ según el cuerpo sea lineal, plano o volumétrico) y montar $\int r^2\,dm$ con la geometría.

> [!teorema] Momentos de inercia de masa (eje por el CM, salvo indicación)
> | Cuerpo | Eje | $I$ |
> |:---|:---|:---:|
> | Partícula | a distancia $r$ del eje | $mr^2$ |
> | Varilla delgada | por el centro, $\perp$ a la varilla | $\tfrac{1}{12}mL^2$ |
> | Varilla delgada | por un extremo, $\perp$ a la varilla | $\tfrac{1}{3}mL^2$ |
> | Anillo delgado | eje de simetría, $\perp$ al plano | $mR^2$ |
> | Disco / cilindro | eje de simetría | $\tfrac{1}{2}mR^2$ |
> | Esfera maciza | diámetro (por el centro) | $\tfrac{2}{5}mR^2$ |
> | Cáscara esférica | diámetro (por el centro) | $\tfrac{2}{3}mR^2$ |

> [!demostracion] Partícula: $I=mr^2$
> Una partícula es masa concentrada en un punto a distancia $r$ del eje. La integral colapsa a un solo
> término: $I=\int r^2\,dm=r^2\!\int dm=mr^2$. Es el ladrillo del que salen todas las demás (cada $dm$
> de un cuerpo extenso es una partícula).

> [!demostracion] Varilla por un extremo: $I=\tfrac13 mL^2$
> Igual que en el ejemplo, $\lambda=m/L$ y $dm=\lambda\,dx$, pero ahora el origen está en el extremo, de
> modo que $x$ recorre $[0,\,L]$:
> $$I=\int_{0}^{L}x^2\,\lambda\,dx=\lambda\,\frac{x^3}{3}\Bigg|_{0}^{L}=\frac{\lambda L^3}{3}=\frac13 mL^2.$$
> Coincide con aplicar el [[Teorema del Eje Paralelo]] al valor del centro:
> $I=\tfrac{1}{12}mL^2+m\!\left(\tfrac{L}{2}\right)^2=\tfrac{1}{12}mL^2+\tfrac14 mL^2=\tfrac13 mL^2.$

> [!demostracion] Anillo delgado: $I=mR^2$
> Eje por el centro, perpendicular al plano del anillo. **Todo** el material está a la misma distancia
> $r=R$ del eje, así que $r^2$ sale de la integral:
> $$I=\int R^2\,dm=R^2\!\int dm=mR^2.$$

> [!demostracion] Disco / cilindro: $I=\tfrac12 mR^2$
> Disco de radio $R$, masa $m$, eje de simetría perpendicular al plano. Densidad superficial
> $\sigma=m/(\pi R^2)$. Se descompone en **anillos** de radio $r$ y espesor $dr$, cada uno con
> $dm=\sigma\,(2\pi r)\,dr$ y todo su material a distancia $r$ del eje:
> $$I=\int_{0}^{R}r^2\,\sigma\,2\pi r\,dr=2\pi\sigma\!\int_{0}^{R}r^3\,dr=2\pi\sigma\,\frac{R^4}{4}=\frac{\pi\sigma R^4}{2}.$$
> Con $\sigma=m/(\pi R^2)$: $I=\dfrac{\pi R^4}{2}\cdot\dfrac{m}{\pi R^2}=\dfrac12 mR^2$. El cilindro
> macizo da lo mismo: es una pila de discos idénticos respecto al mismo eje.

> [!demostracion] Esfera maciza: $I=\tfrac25 mR^2$
> Esfera de radio $R$, masa $m$, densidad $\rho=\dfrac{m}{\tfrac43\pi R^3}$, eje un diámetro (eje $z$).
> Se rebana en **discos** perpendiculares al eje; el disco a altura $z$ tiene radio
> $a=\sqrt{R^2-z^2}$, espesor $dz$ y masa $dm=\rho\,\pi a^2\,dz$. Por el resultado del disco, su aporte
> al momento respecto al eje $z$ es $dI=\tfrac12 a^2\,dm=\tfrac12\rho\,\pi a^4\,dz$:
> $$I=\int_{-R}^{R}\frac{\rho\pi}{2}\,(R^2-z^2)^2\,dz
>    =\frac{\rho\pi}{2}\int_{-R}^{R}\!\big(R^4-2R^2z^2+z^4\big)\,dz.$$
> La integral vale $2R^4\!\cdot\! R-2R^2\cdot\tfrac{2R^3}{3}+\tfrac{2R^5}{5}=2R^5\!\left(1-\tfrac23+\tfrac15\right)=\tfrac{16}{15}R^5$, luego
> $I=\dfrac{\rho\pi}{2}\cdot\dfrac{16}{15}R^5=\dfrac{8\pi\rho R^5}{15}.$ Sustituyendo
> $\rho=\dfrac{3m}{4\pi R^3}$:
> $$I=\frac{8\pi R^5}{15}\cdot\frac{3m}{4\pi R^3}=\frac{2}{5}mR^2.$$

> [!demostracion] Cáscara esférica: $I=\tfrac23 mR^2$
> Superficie esférica de radio $R$ y masa $m$, densidad superficial $\sigma=\dfrac{m}{4\pi R^2}$, eje un
> diámetro. Se parametriza por el ángulo polar $\theta$ medido desde el eje: el anillo entre $\theta$ y
> $\theta+d\theta$ tiene radio (distancia al eje) $r=R\sin\theta$, ancho $R\,d\theta$, perímetro
> $2\pi R\sin\theta$ y por tanto $dm=\sigma\,(2\pi R\sin\theta)(R\,d\theta)$. Como todo su material está
> a distancia $r=R\sin\theta$ del eje,
> $$I=\int_{0}^{\pi}(R\sin\theta)^2\,\sigma\,2\pi R^2\sin\theta\,d\theta
>    =2\pi\sigma R^4\!\int_{0}^{\pi}\sin^3\theta\,d\theta.$$
> Con $\displaystyle\int_{0}^{\pi}\sin^3\theta\,d\theta=\tfrac43$ y $\sigma=\dfrac{m}{4\pi R^2}$:
> $$I=2\pi R^4\cdot\frac{m}{4\pi R^2}\cdot\frac43=\frac{2}{3}mR^2.$$
> Sale mayor que el de la esfera maciza ($\tfrac23>\tfrac25$): en la cáscara **toda** la masa está en el
> borde, lejos del eje.

> [!proposicion] Masa vs. área: "mirar la diferencial"
> Dos objetos comparten el nombre "momento de inercia" pero son distintos; lo que los separa es la
> **diferencial** que se integra:
>
> | | Integral | Unidades | Para qué |
> |:---|:---:|:---:|:---|
> | Inercia de **masa** | $\int r^2\,dm$ | $\mathrm{kg\,m^2}$ | dinámica de **rotación** ($H=I\omega$, $T=\tfrac12 I\omega^2$) |
> | Inercia de **área** | $\int r^2\,dA$ | $\mathrm{m^4}$ | **flexión** de vigas (resistencia de materiales) |
>
> La inercia de área tiene además su **momento polar** $J=\displaystyle\int r^2\,dA=I_x+I_y$ (suma de
> los dos momentos planos), que gobierna la **torsión** de ejes circulares. Regla mnemotécnica: si en la
> integral aparece $dm$ es masa (rotación); si aparece $dA$ es área (flexión).

> [!warning]
> - Los valores de la tabla están en el **centro de masa** (o en el eje indicado). Para cualquier **otro
>   eje paralelo** hay que usar el [[Teorema del Eje Paralelo]], $I=I_{cm}+md^2$; sumar $md^2$ "a ojo"
>   sin pasar por el CM es un error frecuente.
> - No mezclar la inercia de **masa** ($dm$, $\mathrm{kg\,m^2}$) con la de **área** ($dA$,
>   $\mathrm{m^4}$): tienen **unidades** y **usos** distintos pese al nombre común.

---

## Resumen

> [!resumen]
> | Cuerpo (eje por el CM, salvo indicación) | $I$ | $k=\sqrt{I/m}$ |
> |:---|:---:|:---:|
> | Partícula (a distancia $r$) | $mr^2$ | $r$ |
> | Varilla, centro $\perp$ | $\tfrac{1}{12}mL^2$ | $L/\sqrt{12}$ |
> | Varilla, extremo $\perp$ | $\tfrac{1}{3}mL^2$ | $L/\sqrt{3}$ |
> | Anillo delgado, eje $\perp$ | $mR^2$ | $R$ |
> | Disco / cilindro, eje | $\tfrac{1}{2}mR^2$ | $R/\sqrt{2}$ |
> | Esfera maciza, diámetro | $\tfrac{2}{5}mR^2$ | $R\sqrt{2/5}$ |
> | Cáscara esférica, diámetro | $\tfrac{2}{3}mR^2$ | $R\sqrt{2/3}$ |
>
> **Masa vs. área:** $\int r^2\,dm$ ($\mathrm{kg\,m^2}$, rotación) frente a $\int r^2\,dA$
> ($\mathrm{m^4}$, flexión). "Mirar la diferencial."

> [!corolario]
> Estas siete entradas, más el [[Teorema del Eje Paralelo]] y la aditividad de la integral, bastan para
> obtener el momento de inercia de casi cualquier cuerpo de ingeniería: se descompone en piezas
> tabuladas, se traslada cada una a un eje común y se suman. El radio de giro $k$ resume cada valor en
> una sola longitud, la "distancia eficaz" de la masa al eje.

> [!referencia]
> Tablas de propiedades: Hibbeler / Beer, apéndice. Cambio de eje: [[Teorema del Eje Paralelo]]. Objeto
> general que estas figuras particularizan: [[Tensor de Inercia]]. Marco del bloque:
> [[3 Inercia/index]].
