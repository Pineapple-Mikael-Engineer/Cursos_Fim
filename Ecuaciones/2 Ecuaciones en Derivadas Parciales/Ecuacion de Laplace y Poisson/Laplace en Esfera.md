---
title: Laplace en Esfera
tags:
  - ecuaciones
  - edp
  - teoria
  - laplace
  - armonicos-esfericos
draft: false
aliases:
  - Laplace en esfera
  - armónicos esféricos
  - polinomios de Legendre
  - Laplace in spherical coordinates
  - spherical harmonics
---

# Laplace en Esfera

> [!definicion]
> En coordenadas **esféricas** $(r,\theta,\varphi)$ —con $r\ge0$ el radio, $\theta\in[0,\pi]$ la **colatitud** (ángulo desde el eje $z$) y $\varphi\in[0,2\pi)$ el **azimut**— la separación de variables de la ecuación de Laplace $\nabla^2u=0$ descompone la solución en una **parte radial** y una **parte angular**. La parte angular son los **armónicos esféricos** $Y_\ell^m(\theta,\varphi)$ —que en la colatitud contienen los **polinomios de Legendre** $P_\ell(\cos\theta)$—, y la parte radial son las dos potencias $r^\ell$ y $r^{-(\ell+1)}$. La solución general es entonces
> $$u(r,\theta,\varphi)=\sum_{\ell=0}^{\infty}\sum_{m=-\ell}^{\ell}\big(A_{\ell m}\,r^{\ell}+B_{\ell m}\,r^{-(\ell+1)}\big)\,Y_\ell^m(\theta,\varphi).$$

> [!info]
> Quinta nota de geometría de la sección [[Ecuacion de Laplace y Poisson/index| Laplace y Poisson]], dentro del [[2 Ecuaciones en Derivadas Parciales/index| capítulo de EDP]]. Es el caso tridimensional con simetría esférica, hermano del bidimensional [[Laplace en Disco]] y del [[Laplace en Cilindro]]. Las funciones especiales que aquí emergen —Legendre y los armónicos esféricos— se estudian en detalle en [[Funciones Especiales/index]]. Su aplicación estrella es la **expansión multipolar** del potencial.

---

## Ejemplo

> [!ejemplo]
> **Potencial en el interior de una esfera con dato axisimétrico.** Queremos $u$ armónica dentro de la bola de radio $a$, con valor prescrito $u(a,\theta)=f(\theta)$ en la superficie. El dato **no depende de $\varphi$** (simetría axial alrededor del eje $z$), así que la solución tampoco: solo sobreviven los términos con $m=0$, donde $Y_\ell^0\propto P_\ell(\cos\theta)$. La solución general axisimétrica es
> $$u(r,\theta)=\sum_{\ell=0}^{\infty}\big(A_\ell\, r^{\ell}+B_\ell\, r^{-\ell-1}\big)\,P_\ell(\cos\theta).$$
>
> **Paso 1 — Eliminar lo singular.** En el **interior** ($r\to0$) los términos $r^{-\ell-1}$ explotan. Como el potencial debe ser finito en el centro, imponemos $B_\ell=0$:
> $$u(r,\theta)=\sum_{\ell=0}^{\infty}A_\ell\, r^{\ell}\,P_\ell(\cos\theta).$$
>
> **Paso 2 — Ajustar la frontera.** En $r=a$ debe valer $f(\theta)$:
> $$f(\theta)=\sum_{\ell=0}^{\infty}A_\ell\, a^{\ell}\,P_\ell(\cos\theta).$$
> Esto es una **serie de Legendre** de $f$. Usando la ortogonalidad $\displaystyle\int_0^\pi P_\ell(\cos\theta)P_n(\cos\theta)\operatorname{sen}\theta\,d\theta=\frac{2}{2\ell+1}\delta_{\ell n}$ se despejan los coeficientes:
> $$\boxed{\,A_\ell=\frac{2\ell+1}{2\,a^{\ell}}\int_0^\pi f(\theta)\,P_\ell(\cos\theta)\,\operatorname{sen}\theta\,d\theta\,}.$$
>
> **Paso 3 — Caso concreto.** Si $f(\theta)=\cos\theta=P_1(\cos\theta)$, la ortogonalidad selecciona solo $\ell=1$: $A_1 a=1\Rightarrow A_1=1/a$, y todos los demás se anulan. El potencial interior es entonces $u(r,\theta)=\dfrac{r}{a}\cos\theta=\dfrac{z}{a}$, un **campo uniforme** —exactamente lo esperado para un dipolo puro en la frontera—.

---

## En qué consiste

> [!teoria]
> El laplaciano en esféricas se escribe
> $$\nabla^2u=\frac{1}{r^2}\frac{\partial}{\partial r}\!\Big(r^2\frac{\partial u}{\partial r}\Big)+\frac{1}{r^2\operatorname{sen}\theta}\frac{\partial}{\partial\theta}\!\Big(\operatorname{sen}\theta\,\frac{\partial u}{\partial\theta}\Big)+\frac{1}{r^2\operatorname{sen}^2\theta}\frac{\partial^2 u}{\partial\varphi^2}.$$
> La gracia es que **la parte radial y la angular se separan limpiamente**. Proponemos $u=R(r)\,Y(\theta,\varphi)$ y, tras dividir por $u/r^2$, los términos radiales quedan a un lado y los angulares al otro. La constante de separación se escribe $\ell(\ell+1)$ (esta forma extraña se justifica al exigir que la parte angular sea regular en los polos). Resultan dos problemas:
>
> - **Radial (ecuación de Euler):** $\dfrac{d}{dr}\!\big(r^2 R'\big)=\ell(\ell+1)R$, cuya solución son las dos potencias $R(r)=r^{\ell}$ y $R(r)=r^{-(\ell+1)}$.
> - **Angular:** $Y$ satisface la ecuación de los **armónicos esféricos**, que a su vez se separa en $\Theta(\theta)\Phi(\varphi)$. La parte azimutal da $\Phi=e^{\pm im\varphi}$ (periodicidad $\Rightarrow m$ entero), y la parte en $\theta$ da la **ecuación asociada de Legendre**, cuyas soluciones regulares en $\theta=0,\pi$ son los polinomios asociados $P_\ell^m(\cos\theta)$.

> [!algoritmo] Resolver Laplace en una geometría esférica
> 1. **Identificar la simetría.** ¿El dato depende de $\varphi$? Si **no**, basta el caso axisimétrico con $P_\ell(\cos\theta)$ ($m=0$). Si **sí**, hace falta el armónico esférico completo $Y_\ell^m$.
> 2. **Elegir las potencias radiales según la región:**
>    - **Interior** de la esfera ($0\le r\le a$): conservar solo $r^{\ell}$ (regular en el origen).
>    - **Exterior** ($r\ge a$): conservar solo $r^{-(\ell+1)}$ (decae en el infinito).
>    - **Cáscara** ($a\le r\le b$): conservar **ambas** potencias.
> 3. **Imponer la frontera** $u(a,\theta,\varphi)=f$ y proyectar $f$ sobre la base angular usando ortogonalidad.
> 4. **Despejar los coeficientes** con las integrales de proyección (serie de Legendre o de armónicos esféricos).

> [!teorema] Ortogonalidad de Legendre y unicidad de la serie
> Los polinomios $\{P_\ell(\cos\theta)\}_{\ell\ge0}$ forman una **base ortogonal completa** en $[0,\pi]$ con peso $\operatorname{sen}\theta$. En consecuencia, toda función razonable $f(\theta)$ admite una **única** expansión $f=\sum_\ell c_\ell P_\ell(\cos\theta)$, lo que garantiza que el problema de Dirichlet axisimétrico tiene **solución única**.

> [!demostracion]
> **Paso 1 — Forma de Sturm–Liouville.** La ecuación de Legendre $\frac{d}{dx}\big[(1-x^2)P_\ell'\big]+\ell(\ell+1)P_\ell=0$ (con $x=\cos\theta$) es un problema de Sturm–Liouville con peso $w(x)=1$ y autovalores $\lambda_\ell=\ell(\ell+1)$, todos **distintos**.
>
> **Paso 2 — Ortogonalidad.** Para $\ell\ne n$, multiplicando la ecuación de $P_\ell$ por $P_n$ y restando la de $P_n$ por $P_\ell$ e integrando, los términos de frontera en $x=\pm1$ se anulan porque $(1-x^2)\to0$. Queda $(\lambda_\ell-\lambda_n)\int_{-1}^1 P_\ell P_n\,dx=0$, y como $\lambda_\ell\ne\lambda_n$, la integral es cero.
>
> **Paso 3 — Norma y completitud.** Se calcula $\int_{-1}^1 P_\ell^2\,dx=\frac{2}{2\ell+1}$. La completitud (densidad de los polinomios en $L^2$) cierra el argumento: cualquier $f$ se reconstruye sin pérdida con los coeficientes $c_\ell=\frac{2\ell+1}{2}\int_{-1}^1 f\,P_\ell\,dx$. La unicidad es inmediata: si dos series representan la misma $f$, restándolas y proyectando se obtiene $c_\ell-c_\ell'=0$ para todo $\ell$. $\blacksquare$

> [!info] Expansión multipolar
> Para una distribución de carga (o masa) **localizada**, el potencial **exterior** se escribe como suma de los términos $r^{-(\ell+1)}P_\ell(\cos\theta)$:
> $$u(r,\theta)=\frac{1}{r}\underbrace{q_0}_{\text{monopolo}}+\frac{1}{r^2}\underbrace{q_1\cos\theta}_{\text{dipolo}}+\frac{1}{r^3}\underbrace{q_2\,P_2(\cos\theta)}_{\text{cuadrupolo}}+\cdots$$
> Cada $\ell$ es un **multipolo**: $\ell=0$ monopolo (carga neta), $\ell=1$ dipolo, $\ell=2$ cuadrupolo, etc. Cada uno decae más rápido en $r$, de modo que a gran distancia **domina el multipolo no nulo de menor orden**. Es la herramienta básica de la electrostática y la gravitación.

> [!warning]
> La elección de potencia radial **depende de la región**, no de la ecuación. En el **interior** se usa $r^{\ell}$ (regular en $r=0$); en el **exterior** se usa $r^{-(\ell+1)}$ (decae en $r\to\infty$). Confundirlas mete una singularidad donde no la hay o impide cumplir la condición en el infinito. En una **cáscara esférica** sobreviven ambas y se necesitan **dos** condiciones de frontera (en $r=a$ y $r=b$) para fijar todos los coeficientes.

---

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Geometría | esférica $(r,\theta,\varphi)$ |
> | Solución general | $u=\sum_{\ell,m}\big(A_{\ell m}r^{\ell}+B_{\ell m}r^{-\ell-1}\big)Y_\ell^m(\theta,\varphi)$ |
> | Parte angular | armónicos esféricos $Y_\ell^m$; en colatitud, Legendre $P_\ell(\cos\theta)$ |
> | Parte radial | $r^{\ell}$ (interior) y $r^{-(\ell+1)}$ (exterior) |
> | Caso axisimétrico | $u=\sum_\ell(A_\ell r^{\ell}+B_\ell r^{-\ell-1})P_\ell(\cos\theta)$ |
> | Coeficiente interior | $A_\ell=\dfrac{2\ell+1}{2a^{\ell}}\displaystyle\int_0^\pi f\,P_\ell(\cos\theta)\operatorname{sen}\theta\,d\theta$ |
> | Aplicación | expansión multipolar (monopolo, dipolo, cuadrupolo…) |

> [!corolario]
> En una esfera, la geometría convierte la separación de variables en una **serie de Legendre** (o de armónicos esféricos): cada modo $\ell$ es un multipolo con su potencia radial propia. Conocer el dato en la superficie **basta** para reconstruir el potencial en todo el interior (o exterior), y los términos de menor $\ell$ son los que mandan lejos de la fuente.

> [!referencia]
> - El hermano 2D con coordenadas polares: [[Laplace en Disco]].
> - El caso cilíndrico (funciones de Bessel): [[Laplace en Cilindro]].
> - Las funciones especiales que aparecen: [[Funciones Especiales/index]].
> - El marco general de la sección: [[Ecuacion de Laplace y Poisson/index]].
