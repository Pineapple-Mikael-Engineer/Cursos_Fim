---
title: Ecuación de Lippmann-Schwinger
order: 3
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - multivariable
  - dispersion
draft: false
aliases:
  - ecuación de Lippmann-Schwinger
  - dispersión de ondas
  - scattering integral equation
  - Lippmann-Schwinger equation
  - aproximación de Born
---

# Ecuación de Lippmann-Schwinger

> [!definicion]
> En un problema de **dispersión** (scattering), una onda **incidente** $u_{\text{inc}}$ choca con un obstáculo descrito por un **potencial dispersor** $V$ y genera una onda **dispersada** $u_{\text{sc}}$. El campo total $u=u_{\text{inc}}+u_{\text{sc}}$ satisface la **ecuación de Lippmann–Schwinger**, una **[[Fredholm Segunda Especie| Fredholm de 2ª especie]]** sobre $\mathbb{R}^3$:
> $$u(\mathbf{x})=u_{\text{inc}}(\mathbf{x})+\int_{\mathbb{R}^3}G(\mathbf{x},\mathbf{y})\,V(\mathbf{y})\,u(\mathbf{y})\,d\mathbf{y},$$
> donde $G$ es la **función de Green saliente** de la ecuación de Helmholtz $(\nabla^2+k^2)G=-\delta$:
> $$G(\mathbf{x},\mathbf{y})=\frac{e^{ik\lvert\mathbf{x}-\mathbf{y}\rvert}}{4\pi\,\lvert\mathbf{x}-\mathbf{y}\rvert}.$$
> El campo se determina **autoconsistentemente**: $u$ aparece dentro y fuera de la integral porque la onda dispersada vuelve a dispersarse en el obstáculo (dispersión múltiple).

> [!info]
> La nota donde la [[Solucion Fundamental| solución fundamental]] de Helmholtz se vuelve el núcleo de una ecuación integral física. Reescribe una **EDP** (Helmholtz/Schrödinger en todo el espacio, con condición de radiación en el infinito) como una **Fredholm** sobre el soporte del potencial. Vive en [[Multivariable/index| Multivariable y Física]], capítulo [[3 Ecuaciones Integrales/index| Ecuaciones Integrales]].

---

## Ejemplo

> [!ejemplo] Onda incidente y onda dispersada
> ![[dispersion_lippmann.svg|470]]
>
> Una onda plana $u_{\text{inc}}=e^{i\mathbf{k}\cdot\mathbf{x}}$ incide desde la izquierda sobre un obstáculo (el potencial $V$, en gris) y genera una onda **dispersada** que se aleja en frentes circulares; el campo total es la **suma** de ambas. La ecuación de Lippmann–Schwinger fija ese campo de forma autoconsistente: cada punto del obstáculo radía proporcionalmente al campo $u$ que **ya** lo atraviesa, y esa radiación contribuye de vuelta al mismo $u$. Lejos del obstáculo, $u_{\text{sc}}\sim f(\theta)\,\dfrac{e^{ikr}}{r}$: la onda esférica saliente modulada por la **amplitud de dispersión** $f(\theta)$, que es lo que mide un detector.

---

## En qué consiste

> [!teoria] Origen: de Helmholtz a la integral
> Partimos de $(\nabla^2+k^2)u=V\,u$ (Helmholtz con fuente $Vu$; en cuántica, la de Schrödinger con $V=2mU/\hbar^2$). Separando $u=u_{\text{inc}}+u_{\text{sc}}$ con $(\nabla^2+k^2)u_{\text{inc}}=0$, la onda dispersada cumple $(\nabla^2+k^2)u_{\text{sc}}=V\,u$. Invirtiendo con la función de Green **saliente** $G$ (la que satisface la condición de radiación de Sommerfeld, onda hacia afuera):
> $$u_{\text{sc}}(\mathbf{x})=\int G(\mathbf{x},\mathbf{y})\,V(\mathbf{y})\,u(\mathbf{y})\,d\mathbf{y}
> \;\Longrightarrow\; u=u_{\text{inc}}+G*(Vu).$$
> El operador $K\,u=\int G\,V\,u\,d\mathbf{y}$ tiene núcleo **débilmente singular** ($G\sim 1/\lvert\mathbf{x}-\mathbf{y}\rvert$, integrable en 3D porque $\alpha=1<n=3$, ver [[Fredholm Multidimensional]]). Si $V$ tiene soporte compacto, $K$ es **compacto** y aplica toda la teoría de Fredholm.

> [!algoritmo] Aproximación de Born (serie de Neumann)
> 1. Toma como punto de partida $u^{(0)}=u_{\text{inc}}$ (sin dispersión).
> 2. **Itera la serie de Neumann**: $u^{(m+1)}=u_{\text{inc}}+K\,u^{(m)}$. Cada iteración añade un orden de dispersión múltiple.
> 3. La **primera aproximación de Born** es la primera iterada:
>    $$u(\mathbf{x})\approx u_{\text{inc}}(\mathbf{x})+\int G(\mathbf{x},\mathbf{y})\,V(\mathbf{y})\,u_{\text{inc}}(\mathbf{y})\,d\mathbf{y}.$$
>    Sustituye el campo total **desconocido** por el incidente **conocido** dentro de la integral.
> 4. **Validez:** converge cuando el dispersor es **débil** ($\lVert K\rVert<1$): potencial pequeño o energía alta ($k$ grande). Para dispersores fuertes (resonancias) hay que resolver la ecuación completa.

> [!teorema] Campo lejano y amplitud de dispersión
> Para $r=\lvert\mathbf{x}\rvert\to\infty$ con dirección $\hat{\mathbf{x}}$, el campo dispersado adopta la forma asintótica
> $$u_{\text{sc}}(\mathbf{x})\sim \frac{e^{ikr}}{r}\,f(\hat{\mathbf{x}}),\qquad
> f(\hat{\mathbf{x}})=-\frac{1}{4\pi}\int e^{-ik\,\hat{\mathbf{x}}\cdot\mathbf{y}}\,V(\mathbf{y})\,u(\mathbf{y})\,d\mathbf{y},$$
> donde $f$ es la **amplitud de dispersión**. La sección eficaz diferencial es $d\sigma/d\Omega=\lvert f\rvert^2$ —el observable—.

> [!demostracion] Esquema del campo lejano
> **Paso 1 — expandir la fase.** Para $\lvert\mathbf{x}\rvert\gg\lvert\mathbf{y}\rvert$, $\lvert\mathbf{x}-\mathbf{y}\rvert\approx r-\hat{\mathbf{x}}\cdot\mathbf{y}$. **Paso 2 — sustituir en $G$.** Entonces $G\approx\dfrac{e^{ikr}}{4\pi r}\,e^{-ik\,\hat{\mathbf{x}}\cdot \mathbf{y}}$, sacando el factor común $e^{ikr}/r$ fuera de la integral. **Paso 3 — leer $f$.** Lo que queda dentro es justamente $f(\hat{\mathbf{x}})$. $\blacksquare$ El campo lejano **no** depende de $r$ salvo por la onda esférica $e^{ikr}/r$: toda la información del obstáculo se concentra en la dependencia angular $f(\theta)$.

> [!info] Dónde aparece y el problema inverso
> Es la ecuación maestra de la **dispersión**:
> - **Mecánica cuántica**: dispersión de partículas por un potencial (Schrödinger).
> - **Acústica**: ondas sonoras sobre objetos sumergidos (sonar).
> - **Electromagnetismo**: dispersión de luz/radar por blancos (versión vectorial).
>
> El **problema inverso** —reconstruir el potencial $V$ (la forma/composición del obstáculo) a partir del campo lejano $f(\theta)$ medido— es una ecuación integral **mal planteada**: pequeños errores de medida se amplifican enormemente. Es la base de la **tomografía** y la imagenología por difracción, y exige regularización.

## Resumen

> [!resumen]
> | Elemento | Significado |
> |---|---|
> | $u=u_{\text{inc}}+u_{\text{sc}}$ | campo total = incidente + dispersado |
> | $G=\dfrac{e^{ik\lvert\mathbf{x}-\mathbf{y}\rvert}}{4\pi\lvert\mathbf{x}-\mathbf{y}\rvert}$ | Green **saliente** de Helmholtz (núcleo) |
> | $V$ | potencial dispersor (el obstáculo) |
> | Tipo | Fredholm **2ª especie**, núcleo débilmente singular |
> | Born | 1ª iterada de Neumann; vale si el dispersor es débil |
> | $f(\theta)$ | amplitud de dispersión (campo lejano), lo medible |

> [!corolario]
> Lippmann–Schwinger convierte el problema de dispersión —una EDP en todo el espacio con condición de radiación— en una Fredholm de 2ª especie sobre el **soporte del obstáculo**. El campo total se determina solo: la onda que dispersa es la misma que ya ha sido dispersada. De ese campo, el límite lejano destila la amplitud $f(\theta)$, el puente entre la teoría y el detector.

> [!referencia]
> - El núcleo como solución fundamental de Helmholtz: [[Solucion Fundamental]].
> - La teoría que la respalda: [[Fredholm Segunda Especie]], [[Fredholm Multidimensional]].
> - El primo electrostático: [[Teoria de Potencial]].
> - El índice de la sección: [[Multivariable/index]].
