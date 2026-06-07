---
title: Operaciones Diferenciales Cilíndricas
tags:
  - analisis-tensorial
  - teoria
  - coordenadas-curvilineas
  - cilindricas
  - divergencia
draft: false
aliases:
  - operaciones cilindricas
  - gradiente divergencia rotor cilindrico
  - cylindrical vector operators
---

# Operaciones Diferenciales Cilíndricas

> [!definicion]
> En el sistema cilíndrico $(\rho,\phi,z)$, con factores de escala $h_\rho=1,\ h_\phi=\rho,\ h_z=1$, los operadores diferenciales son
> $$\vec\nabla\Phi=\frac{\partial\Phi}{\partial\rho}\hat e_\rho+\frac1\rho\frac{\partial\Phi}{\partial\phi}\hat e_\phi+\frac{\partial\Phi}{\partial z}\hat e_z,$$
> $$\vec\nabla\cdot\vec A=\frac1\rho\frac{\partial(\rho A_\rho)}{\partial\rho}+\frac1\rho\frac{\partial A_\phi}{\partial\phi}+\frac{\partial A_z}{\partial z},$$
> $$\vec\nabla\times\vec A=\left[\frac1\rho\frac{\partial A_z}{\partial\phi}-\frac{\partial A_\phi}{\partial z}\right]\hat e_\rho+\left[\frac{\partial A_\rho}{\partial z}-\frac{\partial A_z}{\partial\rho}\right]\hat e_\phi+\frac1\rho\left[\frac{\partial(\rho A_\phi)}{\partial\rho}-\frac{\partial A_\rho}{\partial\phi}\right]\hat e_z.$$

> [!info]
> Sección **3.5.1** del [[index | sistema cilíndrico]] (libro, cap. 3.5.1). Estas tres fórmulas no son nuevas: salen de las formas curvilíneas generales sin más que sustituir $h_\rho=1,h_\phi=\rho,h_z=1$ (ver [[Vectores Base y Factores Escala]]). La deducción de las fórmulas maestras vive en [[Sistemas Curvilineos Generales/Divergencia General | divergencia general]], [[Sistemas Curvilineos Generales/Gradiente General | gradiente general]] y [[Sistemas Curvilineos Generales/Rotor General | rotor general]].

---

## Ejemplo

> [!ejemplo]
> **Laplaciano de $\Phi(\rho)=\ln\rho$ (potencial de una línea de carga).** El potencial de un hilo cargado infinito sobre el eje $z$ es $\Phi=-\dfrac{\lambda}{2\pi\varepsilon_0}\ln\rho$; basta analizar $\Phi=\ln\rho$. Como solo depende de $\rho$, el laplaciano $\nabla^2\Phi=\vec\nabla\cdot(\vec\nabla\Phi)$ se reduce a la parte radial:
> $$\nabla^2\Phi=\frac1\rho\frac{\partial}{\partial\rho}\!\left(\rho\,\frac{\partial\Phi}{\partial\rho}\right).$$
> Con $\dfrac{\partial\Phi}{\partial\rho}=\dfrac{1}{\rho}$,
> $$\nabla^2\Phi=\frac1\rho\frac{\partial}{\partial\rho}\!\left(\rho\cdot\frac1\rho\right)=\frac1\rho\frac{\partial}{\partial\rho}(1)=0\qquad(\rho\neq0).$$
> El laplaciano se anula fuera del eje: $\Phi=\ln\rho$ es **armónica**, consistente con que no hay carga fuera del hilo. (En $\rho=0$, donde sí está la carga, la fórmula no aplica.)

> [!ejemplo]
> **Divergencia de un campo radial $\vec A=\rho\,\hat e_\rho$.** Aquí $A_\rho=\rho$, $A_\phi=A_z=0$. Solo sobrevive el primer término de la divergencia:
> $$\vec\nabla\cdot\vec A=\frac1\rho\frac{\partial(\rho A_\rho)}{\partial\rho}=\frac1\rho\frac{\partial(\rho\cdot\rho)}{\partial\rho}=\frac1\rho\frac{\partial(\rho^2)}{\partial\rho}=\frac1\rho\,(2\rho)=2.$$
> La divergencia es constante e igual a $2$. El factor $1/\rho$ y el $\rho$ dentro de la derivada (ambos herencia de $h_\phi=\rho$) son imprescindibles: ignorarlos y escribir $\partial A_\rho/\partial\rho=1$ daría un resultado equivocado.

---

## En qué consiste

> [!teoria]
> Las fórmulas curvilíneas generales son
> $$\vec\nabla\Phi=\sum_i\frac{1}{h_i}\frac{\partial\Phi}{\partial q_i}\hat e_i,\qquad \vec\nabla\cdot\vec A=\frac{1}{h_\rho h_\phi h_z}\sum_i\frac{\partial}{\partial q_i}\!\left(\frac{h_\rho h_\phi h_z}{h_i}A_i\right).$$
> Sustituyendo $h_\rho=1,\ h_\phi=\rho,\ h_z=1$ (de modo que $h_\rho h_\phi h_z=\rho$) se obtienen directamente las tres fórmulas de la definición. Conviene notar dónde aparece $\rho$: divide en las derivadas respecto a $\phi$ (porque $h_\phi=\rho$) y entra dentro de la derivada radial de la divergencia.

> [!proposicion] Rotor como determinante
> El rotor general $\vec\nabla\times\vec A=\dfrac{1}{h_\rho h_\phi h_z}\,\det\!\begin{pmatrix}h_\rho\hat e_\rho & h_\phi\hat e_\phi & h_z\hat e_z\\[2pt]\partial_\rho & \partial_\phi & \partial_z\\[2pt]h_\rho A_\rho & h_\phi A_\phi & h_z A_z\end{pmatrix}$ se especializa, con los $h_i$ cilíndricos, en
> $$\vec\nabla\times\vec A=\frac1\rho\,\det\!\begin{pmatrix}\hat e_\rho & \rho\,\hat e_\phi & \hat e_z\\[2pt]\partial_\rho & \partial_\phi & \partial_z\\[2pt]A_\rho & \rho A_\phi & A_z\end{pmatrix},$$
> que reproduce las tres componentes de la definición.

> [!info] Laplaciano cilíndrico
> Componiendo $\nabla^2\Phi=\vec\nabla\cdot(\vec\nabla\Phi)$:
> $$\nabla^2\Phi=\frac1\rho\frac{\partial}{\partial\rho}\!\left(\rho\frac{\partial\Phi}{\partial\rho}\right)+\frac{1}{\rho^2}\frac{\partial^2\Phi}{\partial\phi^2}+\frac{\partial^2\Phi}{\partial z^2}.$$
> Es la forma usada para resolver la ecuación de Laplace y de Helmholtz con simetría axial.

---

## Resumen

> [!resumen]
> | Operador | Fórmula cilíndrica |
> |---|---|
> | Gradiente | $\partial_\rho\Phi\,\hat e_\rho+\tfrac1\rho\partial_\phi\Phi\,\hat e_\phi+\partial_z\Phi\,\hat e_z$ |
> | Divergencia | $\tfrac1\rho\partial_\rho(\rho A_\rho)+\tfrac1\rho\partial_\phi A_\phi+\partial_z A_z$ |
> | Rotor $\hat e_\rho$ | $\tfrac1\rho\partial_\phi A_z-\partial_z A_\phi$ |
> | Rotor $\hat e_\phi$ | $\partial_z A_\rho-\partial_\rho A_z$ |
> | Rotor $\hat e_z$ | $\tfrac1\rho\!\left[\partial_\rho(\rho A_\phi)-\partial_\phi A_\rho\right]$ |
> | Laplaciano | $\tfrac1\rho\partial_\rho(\rho\,\partial_\rho\Phi)+\tfrac1{\rho^2}\partial_\phi^2\Phi+\partial_z^2\Phi$ |

> [!corolario]
> Todo el sabor cilíndrico de estos operadores está en los factores $1/\rho$ y $\partial(\rho\,\cdot)/\partial\rho$, herencia directa de $h_\phi=\rho$. Por eso un campo dependiente solo de $\rho$ (como $\ln\rho$ o $\rho\,\hat e_\rho$) reduce gradiente, divergencia y laplaciano a su parte radial, que es donde aparece la simetría axial del problema.

> [!referencia]
> - Deducción general de los operadores: [[Sistemas Curvilineos Generales/Divergencia General]], [[Sistemas Curvilineos Generales/Gradiente General]], [[Sistemas Curvilineos Generales/Rotor General]].
> - Factores de escala que originan los $1/\rho$: [[Vectores Base y Factores Escala]].
> - Versión esférica: [[Sistema Esferico/Operaciones Esfericas]].
