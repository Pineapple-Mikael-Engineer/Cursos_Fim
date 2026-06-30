---
title: Metodo de las Imagenes
order: 3
tags:
  - ecuaciones
  - edp
  - teoria
  - funcion-green
  - metodo-imagenes
draft: false
aliases:
  - método de las imágenes
  - cargas imagen
  - imagen de Kelvin
  - method of images
---

# Método de las Imágenes

> [!definicion]
> El **método de las imágenes** construye la corrección armónica $h$ de la [[Funcion de Green y Condiciones| función de Green]] mediante un truco geométrico: para dominios simples (un **plano**, una **esfera**), $h$ es el potencial de una o varias **cargas imagen** colocadas **fuera** del dominio, elegidas de modo que $G$ se anule sobre la frontera. Como las imágenes están fuera de $\Omega$, su potencial es armónico **dentro** (sin singularidades nuevas), así que cumple lo que se le pide a $h$ sin alterar el impulso interior.

> [!info]
> Es la tercera pieza de [[Funciones de Green para EDP/index| Funciones de Green para EDP]], en el [[2 Ecuaciones en Derivadas Parciales/index| capítulo de EDP]]. Es la manera práctica de obtener la corrección $h$ de [[Funcion de Green y Condiciones]] cuando hay simetría, partiendo siempre de la [[Solucion Fundamental]] como ladrillo básico.

---

## Ejemplo

> [!ejemplo] Carga puntual y su imagen frente a un plano a tierra
> ![[cargas_imagen.svg|460]]
>
> La carga $+q$ y su imagen $-q$ (reflejada en el plano) producen un potencial que se anula sobre el plano: las equipotenciales y las líneas de campo cruzan el conductor perpendicularmente.

> [!solucion] Construcción de $G$ para el semiespacio
> Consideremos una fuente unidad en $\boldsymbol{\xi}=(0,0,d)$ por encima del **plano conductor a tierra** $z=0$, y busquemos $G$ en el semiespacio $\Omega=\{z>0\}$ con $G=0$ en $z=0$.
>
> La solución fundamental sola, $\Phi(\mathbf{x}-\boldsymbol{\xi})$, no se anula en el plano. La idea física: un conductor a tierra reacomoda su carga superficial de tal forma que, **vista desde arriba**, equivale a haber puesto una carga **opuesta** $-q$ en la posición espejo $\boldsymbol{\xi}^*=(0,0,-d)$. Sumando ambos potenciales,
> $$G(\mathbf{x},\boldsymbol{\xi})=\Phi(\mathbf{x}-\boldsymbol{\xi})-\Phi(\mathbf{x}-\boldsymbol{\xi}^*)
> =\frac{1}{4\pi\lvert\mathbf{x}-\boldsymbol{\xi}\rvert}-\frac{1}{4\pi\lvert\mathbf{x}-\boldsymbol{\xi}^*\rvert}.$$
> **Verificación en la frontera:** si $\mathbf{x}=(x,y,0)$ está sobre el plano, la distancia a $\boldsymbol{\xi}=(0,0,d)$ y a su espejo $\boldsymbol{\xi}^*=(0,0,-d)$ es **la misma**, $\sqrt{x^2+y^2+d^2}$, porque el punto del plano equidista de un punto y su reflejo. Luego los dos términos se cancelan y $G=0$ en $z=0$, como se quería.
>
> Aquí la corrección armónica es $h(\mathbf{x},\boldsymbol{\xi})=-\Phi(\mathbf{x}-\boldsymbol{\xi}^*)$: su única singularidad está en $\boldsymbol{\xi}^*$, que cae en $z<0$, **fuera** de $\Omega$. Dentro del dominio $h$ es perfectamente armónica.

## En qué consiste

> [!teoria]
> ¿Por qué funciona el truco? Hay que comprobar las dos propiedades que definen a $G$:
> - **El impulso interior se conserva.** La imagen vive fuera de $\Omega$, así que dentro del dominio su potencial no tiene singularidad: $\nabla^2(\text{imagen})=0$ en $\Omega$. Por tanto $G$ sigue teniendo **exactamente** el mismo $\delta$ que $\Phi$ en $\boldsymbol{\xi}$, y la ecuación $-\nabla^2 G=\delta$ no se estropea. La imagen solo añade una pieza armónica, que es justo lo que se permite a $h$.
> - **La frontera se anula por simetría.** La elección del signo y la posición de la imagen está hecha a propósito para que, sobre $\partial\Omega$, los potenciales de fuente e imagen se cancelen (caso Dirichlet) — o sumen, si se buscara Neumann con imagen del mismo signo.
>
> **Esfera (imagen de Kelvin).** Para una esfera de radio $a$ la reflexión simple no basta; la imagen de una fuente en $\boldsymbol{\xi}$ (a distancia $\rho=\lvert\boldsymbol{\xi}\rvert$ del centro) se coloca en el **punto inverso** $\boldsymbol{\xi}^*=\dfrac{a^2}{\rho^2}\,\boldsymbol{\xi}$ (sobre la misma recta radial, pero a distancia $a^2/\rho$) y con la carga **escalada** por un factor $-a/\rho$. Esa combinación logra de nuevo $G=0$ sobre la esfera. Es la generalización geométrica de la reflexión, adaptada a la curvatura.

> [!algoritmo] Construir $G$ por imágenes
> 1. **Identifica la simetría** de la frontera (plano, esfera, par de planos...). Sin simetría, el método no aplica.
> 2. **Coloca la imagen** (o imágenes) **fuera** del dominio en la posición espejo/inversa, con el signo y la escala que **anulen** $G$ sobre la frontera (Dirichlet) — o den el flujo correcto (Neumann).
> 3. **Suma los potenciales** de fuente e imágenes: $G=\Phi(\mathbf{x}-\boldsymbol{\xi})\ \pm\ \Phi(\mathbf{x}-\boldsymbol{\xi}^*)+\dots$
> 4. **Verifica** que $G$ cumple la condición de frontera y que las imágenes quedan fuera de $\Omega$ (para no introducir singularidades espurias dentro).

> [!warning] El método exige simetría especular o esférica
> Las imágenes solo resuelven $h$ cuando la frontera tiene una simetría que permita "reflejar" la fuente a un punto exterior bien definido: un plano, una esfera, una cuña de ángulo $\pi/n$ (varias imágenes), o combinaciones. Para una frontera **arbitraria** no hay punto imagen y hay que volver al problema de Laplace general de [[Funcion de Green y Condiciones]] (o métodos numéricos). El método es elegante, pero no universal.

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Idea | $h=$ potencial de cargas imagen fuera de $\Omega$ |
> | Plano $z=0$ | imagen $-q$ en el reflejo $\boldsymbol{\xi}^*=(\xi_1,\xi_2,-\xi_3)$ |
> | $G$ (semiespacio) | $\Phi(\mathbf{x}-\boldsymbol{\xi})-\Phi(\mathbf{x}-\boldsymbol{\xi}^*)$ |
> | Esfera radio $a$ | imagen de Kelvin: punto inverso $\dfrac{a^2}{\rho^2}\boldsymbol{\xi}$, carga $-\dfrac{a}{\rho}$ |
> | Por qué funciona | imagen armónica dentro ($\delta$ intacta) + frontera nula por simetría |
> | Límite | solo geometrías con simetría especular/esférica |

> [!corolario]
> Cuando la geometría coopera, el método de las imágenes da la función de Green **sin resolver ninguna EDP adicional**: basta colocar la fuente espejo correcta. Convierte un problema de frontera en pura geometría —reflejar un punto— y entrega $G$ en forma cerrada para el plano, la esfera y sus variantes.

> [!referencia]
> - La corrección $h$ y la fórmula de representación: [[Funcion de Green y Condiciones]].
> - El ladrillo básico $\Phi$: [[Solucion Fundamental]].
> - El índice de la sección: [[Funciones de Green para EDP/index]].
