---
title: Teoría de Potencial
order: 2
tags:
  - ecuaciones
  - ecuaciones-integrales
  - teoria
  - multivariable
  - potencial
draft: false
aliases:
  - teoría de potencial
  - potencial de capa simple
  - potencial de capa doble
  - ecuaciones integrales de frontera
  - boundary integral equations
  - potential theory
---

# Teoría de Potencial

> [!definicion]
> La **teoría de potencial** representa una función armónica mediante una **densidad sobre la frontera** $\partial\Omega$. Con la [[Solucion Fundamental| solución fundamental]] $\Phi$ del laplaciano se forman dos potenciales:
> $$\underbrace{u(\mathbf{x})=\int_{\partial\Omega}\sigma(\mathbf{y})\,\Phi(\mathbf{x}-\mathbf{y})\,dS_y}_{\text{capa simple}},\qquad \underbrace{u(\mathbf{x})=\int_{\partial\Omega}\mu(\mathbf{y})\,\frac{\partial\Phi}{\partial n_y}(\mathbf{x}-\mathbf{y})\,dS_y}_{\text{capa doble}}.$$
> Imponer la condición de frontera convierte el **problema de Laplace** en una **ecuación integral de Fredholm de 2ª especie sobre $\partial\Omega$** para la densidad — el método de **elementos de frontera**.

> [!info]
> El puente central entre [[Ecuacion de Laplace y Poisson/index| EDP]] y ecuaciones integrales ([[Multivariable/index| multivariable]]). Reduce un problema en el **volumen** a uno sobre la **superficie**, con núcleo singular ($\Phi\sim 1/r$ o $\ln r$) — de ahí su parentesco con [[Singulares/index| las singulares]].

---

## Ejemplo

> [!ejemplo] Una densidad de frontera que genera el campo
> ![[potencial_capas.svg|460]]
>
> Una **capa simple** $\sigma$ sobre $\partial\Omega$ es como una distribución de **carga superficial**: genera un potencial $u$ armónico dentro y fuera, **continuo** al cruzar la frontera pero con la **derivada normal saltando** en $\sigma$ (campo eléctrico discontinuo, como en un conductor cargado). Una **capa doble** $\mu$ es como una capa de **dipolos**: el potencial **salta** en $\mu$ al cruzar la superficie. Para resolver el problema de **Dirichlet** ($u=g$ en $\partial\Omega$) con una capa doble, al tomar el valor de frontera y usar el salto se obtiene
> $$\tfrac12\mu(\mathbf{x})+\int_{\partial\Omega}\mu(\mathbf{y})\,\frac{\partial\Phi}{\partial n_y}\,dS_y=g(\mathbf{x}),$$
> una **Fredholm de 2ª especie** para la densidad $\mu$ sobre la frontera.

---

## En qué consiste

> [!teorema] Relaciones de salto
> Al cruzar $\partial\Omega$ (con normal exterior $n$):
> - la **capa simple** $u$ es **continua**, pero su derivada normal salta: $\dfrac{\partial u}{\partial n}\Big|_{\pm}=\mp\tfrac12\sigma+\displaystyle\int_{\partial\Omega}\sigma\,\dfrac{\partial\Phi}{\partial n_x}\,dS$;
> - la **capa doble** $u$ **salta**: $u_{\pm}=\pm\tfrac12\mu+\displaystyle\int_{\partial\Omega}\mu\,\dfrac{\partial\Phi}{\partial n_y}\,dS$.

> [!demostracion] Origen del salto (capa doble, esquema)
> **Paso 1 — la singularidad.** El núcleo $\partial\Phi/\partial n_y$ se comporta cerca de $\mathbf{x}=\mathbf{y}$ como el **ángulo sólido** subtendido por un elemento de superficie. **Paso 2 — integrar el ángulo sólido.** Al acercar $\mathbf{x}$ a la frontera desde dentro/fuera, la contribución de la vecindad de $\mathbf{x}$ es **medio** ángulo sólido completo ($\pm 2\pi$ en 3D), que aporta el término $\pm\tfrac12\mu(\mathbf{x})$; el resto de la superficie da la integral (valor principal). **Paso 3 — sumar.** $u_\pm=\pm\tfrac12\mu+\int\mu\,\partial_{n}\Phi$. $\blacksquare$ Ese **$\tfrac12$** es lo que convierte la ecuación de frontera en una **2ª especie** (bien planteada), no en una 1ª especie.

> [!algoritmo] Resolver un problema de frontera con potenciales
> 1. Elige la representación: **capa doble** para Dirichlet, **capa simple** para Neumann (da 2ª especie).
> 2. Toma el valor (o derivada) de frontera usando la **relación de salto**.
> 3. Resulta una **Fredholm de 2ª especie** sobre $\partial\Omega$ para la densidad.
> 4. Resuélvela ([[Nucleo Degenerado| degenerado]] / [[Cuadratura y Nystrom| Nyström]] → **BEM**).
> 5. Sustituye la densidad en el potencial para evaluar $u$ en cualquier punto.

> [!info] Por qué BEM es tan eficiente
> El **método de elementos de frontera** discretiza solo la **superficie** (dimensión $n-1$), no el volumen: menos incógnitas que diferencias/elementos finitos, y trata sin esfuerzo los **dominios no acotados** (la condición en el infinito la cumple $\Phi$). Su precio es una matriz **llena** (el núcleo acopla todos los puntos) y la integración de la **singularidad** del núcleo.

## Resumen

> [!resumen]
> | Potencial | Densidad | Continuidad al cruzar | Sirve para |
> |---|---|---|---|
> | Capa simple | $\sigma$ (carga) | $u$ continuo, $\partial_n u$ salta | Neumann |
> | Capa doble | $\mu$ (dipolos) | $u$ salta en $\mu$ | Dirichlet |
> | Ecuación de frontera | — | Fredholm **2ª especie** | BEM |

> [!corolario]
> La teoría de potencial **traslada la incógnita a la frontera**: en vez de hallar $u$ en todo el dominio, se busca una densidad superficial que lo genere. El milagro es que la condición de frontera da una **Fredholm de 2ª especie** (gracias al $\tfrac12$ del salto), bien planteada y resoluble — la idea que sostiene el método de elementos de frontera.

> [!referencia]
> - El núcleo que se usa: [[Solucion Fundamental]].
> - La EDP de origen: [[Ecuacion de Laplace y Poisson/index]].
> - La discretización: [[Cuadratura y Nystrom]].
