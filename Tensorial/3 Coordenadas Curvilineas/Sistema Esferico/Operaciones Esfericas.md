---
title: Operaciones Diferenciales Esféricas
order: 2
tags:
  - analisis-tensorial
  - teoria
  - coordenadas-curvilineas
  - esfericas
  - divergencia
draft: false
aliases:
  - operaciones esfericas
  - gradiente divergencia rotor esferico
  - spherical vector operators
---

# Operaciones Diferenciales Esféricas

> [!definicion]
> En el sistema esférico $(r,\theta,\phi)$, con factores de escala $h_r=1,\ h_\theta=r,\ h_\phi=r\operatorname{sen}\theta$, los operadores diferenciales son
> $$\vec\nabla\Phi=\frac{\partial\Phi}{\partial r}\hat e_r+\frac1r\frac{\partial\Phi}{\partial\theta}\hat e_\theta+\frac1{r\operatorname{sen}\theta}\frac{\partial\Phi}{\partial\phi}\hat e_\phi,$$
> $$\vec\nabla\cdot\vec A=\frac1{r^2}\frac{\partial(r^2A_r)}{\partial r}+\frac1{r\operatorname{sen}\theta}\frac{\partial(\operatorname{sen}\theta\,A_\theta)}{\partial\theta}+\frac1{r\operatorname{sen}\theta}\frac{\partial A_\phi}{\partial\phi},$$
> $$\vec\nabla\times\vec A=\frac1{r\operatorname{sen}\theta}\!\left[\frac{\partial(\operatorname{sen}\theta\,A_\phi)}{\partial\theta}-\frac{\partial A_\theta}{\partial\phi}\right]\hat e_r+\frac1r\!\left[\frac1{\operatorname{sen}\theta}\frac{\partial A_r}{\partial\phi}-\frac{\partial(rA_\phi)}{\partial r}\right]\hat e_\theta+\frac1r\!\left[\frac{\partial(rA_\theta)}{\partial r}-\frac{\partial A_r}{\partial\theta}\right]\hat e_\phi.$$

> [!info]
> Sección **3.5.2** del [[index | sistema esférico]] (libro, cap. 3.5.2). Estas tres fórmulas no son nuevas: salen de las formas curvilíneas generales sin más que sustituir $h_r=1,h_\theta=r,h_\phi=r\operatorname{sen}\theta$ (ver [[Vectores Base y Factores Escala]]). La deducción de las fórmulas maestras vive en [[Sistemas Curvilineos Generales/Divergencia General | divergencia general]], [[Sistemas Curvilineos Generales/Gradiente General | gradiente general]] y [[Sistemas Curvilineos Generales/Rotor General | rotor general]].

---

## Ejemplo

> [!ejemplo]
> **Divergencia del campo radial $\vec A=\dfrac{1}{r^2}\hat e_r$ (campo de una carga puntual).** El campo eléctrico de una carga $q$ en el origen es $\vec E=\dfrac{q}{4\pi\varepsilon_0}\dfrac{1}{r^2}\hat e_r$; basta analizar $\vec A=\dfrac{1}{r^2}\hat e_r$. Aquí $A_r=\dfrac{1}{r^2}$, $A_\theta=A_\phi=0$, así que solo sobrevive el primer término de la divergencia:
> $$\vec\nabla\cdot\vec A=\frac1{r^2}\frac{\partial(r^2A_r)}{\partial r}=\frac1{r^2}\frac{\partial}{\partial r}\!\left(r^2\cdot\frac1{r^2}\right)=\frac1{r^2}\frac{\partial}{\partial r}(1)=0\qquad(r\neq0).$$
> La divergencia se **anula** en todo el espacio salvo el origen: $\vec A$ es solenoidal fuera de la carga, coherente con que la fuente está concentrada en $r=0$. El $r^2$ dentro de la derivada (herencia de $h_\theta h_\phi=r^2\operatorname{sen}\theta$) es justo lo que cancela el $1/r^2$ del campo; ignorarlo y escribir $\partial A_r/\partial r=-2/r^3$ daría un resultado erróneo. La fuente en el origen se captura con la delta de Dirac: $\vec\nabla\cdot(\hat e_r/r^2)=4\pi\,\delta^3(\vec r)$.

> [!ejemplo]
> **Laplaciano de $\Phi(r)=1/r$ (potencial de Coulomb).** El potencial de una carga puntual es $\Phi=\dfrac{q}{4\pi\varepsilon_0}\dfrac{1}{r}$; analizamos $\Phi=1/r$. Como solo depende de $r$, el laplaciano $\nabla^2\Phi=\vec\nabla\cdot(\vec\nabla\Phi)$ se reduce a la parte radial:
> $$\nabla^2\Phi=\frac1{r^2}\frac{\partial}{\partial r}\!\left(r^2\,\frac{\partial\Phi}{\partial r}\right).$$
> Con $\dfrac{\partial\Phi}{\partial r}=-\dfrac{1}{r^2}$,
> $$\nabla^2\Phi=\frac1{r^2}\frac{\partial}{\partial r}\!\left(r^2\cdot\left(-\frac1{r^2}\right)\right)=\frac1{r^2}\frac{\partial}{\partial r}(-1)=0\qquad(r\neq0).$$
> El potencial $\Phi=1/r$ es **armónico** fuera del origen, consistente con que no hay carga allí. Es el mismo resultado que la divergencia anterior: $\vec\nabla\Phi=-\hat e_r/r^2$, de modo que $\nabla^2(1/r)=\vec\nabla\cdot(-\hat e_r/r^2)=0$ para $r\neq0$, y $=-4\pi\,\delta^3(\vec r)$ en sentido distribucional.

---

## En qué consiste

> [!teoria]
> Las fórmulas curvilíneas generales son
> $$\vec\nabla\Phi=\sum_i\frac{1}{h_i}\frac{\partial\Phi}{\partial q_i}\hat e_i,\qquad \vec\nabla\cdot\vec A=\frac{1}{h_r h_\theta h_\phi}\sum_i\frac{\partial}{\partial q_i}\!\left(\frac{h_r h_\theta h_\phi}{h_i}A_i\right).$$
> Sustituyendo $h_r=1,\ h_\theta=r,\ h_\phi=r\operatorname{sen}\theta$ (de modo que $h_r h_\theta h_\phi=r^2\operatorname{sen}\theta$) se obtienen directamente las tres fórmulas de la definición. El término radial de la divergencia, por ejemplo, sale de $\dfrac{1}{r^2\operatorname{sen}\theta}\dfrac{\partial}{\partial r}\!\left(\dfrac{r^2\operatorname{sen}\theta}{1}A_r\right)=\dfrac{1}{r^2}\dfrac{\partial(r^2A_r)}{\partial r}$, donde $\operatorname{sen}\theta$ se cancela por no depender de $r$.

> [!proposicion] Rotor como determinante
> El rotor general $\vec\nabla\times\vec A=\dfrac{1}{h_r h_\theta h_\phi}\,\det\!\begin{pmatrix}h_r\hat e_r & h_\theta\hat e_\theta & h_\phi\hat e_\phi\\[2pt]\partial_r & \partial_\theta & \partial_\phi\\[2pt]h_r A_r & h_\theta A_\theta & h_\phi A_\phi\end{pmatrix}$ se especializa, con los $h_i$ esféricos, en
> $$\vec\nabla\times\vec A=\frac1{r^2\operatorname{sen}\theta}\,\det\!\begin{pmatrix}\hat e_r & r\,\hat e_\theta & r\operatorname{sen}\theta\,\hat e_\phi\\[2pt]\partial_r & \partial_\theta & \partial_\phi\\[2pt]A_r & rA_\theta & r\operatorname{sen}\theta\,A_\phi\end{pmatrix},$$
> que reproduce las tres componentes de la definición.

> [!info] Laplaciano esférico
> Componiendo $\nabla^2\Phi=\vec\nabla\cdot(\vec\nabla\Phi)$:
> $$\nabla^2\Phi=\frac1{r^2}\frac{\partial}{\partial r}\!\left(r^2\frac{\partial\Phi}{\partial r}\right)+\frac1{r^2\operatorname{sen}\theta}\frac{\partial}{\partial\theta}\!\left(\operatorname{sen}\theta\frac{\partial\Phi}{\partial\theta}\right)+\frac1{r^2\operatorname{sen}^2\theta}\frac{\partial^2\Phi}{\partial\phi^2}.$$
> Es la forma usada para resolver la ecuación de Laplace, de Poisson y de Schrödinger con simetría central; la parte angular conduce a los **armónicos esféricos**.

---

## Resumen

> [!resumen]
> | Operador | Fórmula esférica |
> |---|---|
> | Gradiente | $\partial_r\Phi\,\hat e_r+\tfrac1r\partial_\theta\Phi\,\hat e_\theta+\tfrac1{r\operatorname{sen}\theta}\partial_\phi\Phi\,\hat e_\phi$ |
> | Divergencia | $\tfrac1{r^2}\partial_r(r^2A_r)+\tfrac1{r\operatorname{sen}\theta}\partial_\theta(\operatorname{sen}\theta\,A_\theta)+\tfrac1{r\operatorname{sen}\theta}\partial_\phi A_\phi$ |
> | Rotor $\hat e_r$ | $\tfrac1{r\operatorname{sen}\theta}\!\left[\partial_\theta(\operatorname{sen}\theta\,A_\phi)-\partial_\phi A_\theta\right]$ |
> | Rotor $\hat e_\theta$ | $\tfrac1r\!\left[\tfrac1{\operatorname{sen}\theta}\partial_\phi A_r-\partial_r(rA_\phi)\right]$ |
> | Rotor $\hat e_\phi$ | $\tfrac1r\!\left[\partial_r(rA_\theta)-\partial_\theta A_r\right]$ |
> | Laplaciano | $\tfrac1{r^2}\partial_r(r^2\partial_r\Phi)+\tfrac1{r^2\operatorname{sen}\theta}\partial_\theta(\operatorname{sen}\theta\,\partial_\theta\Phi)+\tfrac1{r^2\operatorname{sen}^2\theta}\partial_\phi^2\Phi$ |

> [!corolario]
> Todo el sabor esférico de estos operadores está en los factores $1/r$, $1/(r\operatorname{sen}\theta)$ y en las derivadas $\partial(r^2\,\cdot)/\partial r$ y $\partial(\operatorname{sen}\theta\,\cdot)/\partial\theta$, herencia directa de $h_\theta=r$ y $h_\phi=r\operatorname{sen}\theta$. Por eso un campo dependiente solo de $r$ (como $1/r^2\,\hat e_r$ o el potencial $1/r$) reduce gradiente, divergencia y laplaciano a su parte radial, que es donde aparece la simetría central del problema.

> [!referencia]
> - Deducción general de los operadores: [[Sistemas Curvilineos Generales/Divergencia General]], [[Sistemas Curvilineos Generales/Gradiente General]], [[Sistemas Curvilineos Generales/Rotor General]].
> - Factores de escala que originan los $1/r$: [[Vectores Base y Factores Escala]].
> - Versión cilíndrica: [[Sistema Cilindrico/Operaciones Cilindricas]].
