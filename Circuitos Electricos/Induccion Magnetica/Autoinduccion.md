---
title: Autoinducción — Fundamento Físico y Deducción Matemática
tags:
  - induccion
  - autoinduccion
  - magnetismo
  - campos
  - maxwell
draft: true
---

# Autoinducción

La **autoinducción** es el fenómeno mediante el cual una corriente variable en un conductor genera un flujo magnético que, al variar en el tiempo, induce una fem en el mismo conductor que la produjo.

Es un fenómeno de retroalimentación electromagnética.

---

# 1) Origen Físico del Fenómeno

## 🔹 Ley de Ampère (corriente → campo magnético)

Una corriente $i(t)$ genera un campo magnético $\mathbf{B}$:

$$
\nabla \times \mathbf{B} = \mu_0 \mathbf{J}
$$

En una bobina, el campo magnético es aproximadamente:

$$
\boxed{
B = \mu n i
}
$$

donde:

- $\mu = \mu_0 \mu_r$
- $n = \frac{N}{\ell}$ (espiras por unidad de longitud)

---

## 🔹 Flujo Magnético

El flujo a través de una espira es:

$$
\boxed{
\Phi = \int \mathbf{B} \cdot d\mathbf{A}
}
$$

Si el campo es uniforme:

$$
\Phi = B A
$$

Entonces para una bobina de $N$ espiras:

$$
\boxed{
\Phi_{total} = N B A
}
$$

Sustituyendo $B$:

$$
\Phi_{total} = N (\mu n i) A
$$

Como $n = \frac{N}{\ell}$:

$$
\Phi_{total} =
\frac{\mu N^2 A}{\ell} i
$$

---

# 2) Definición Formal de Inductancia

Se define la inductancia como la constante de proporcionalidad entre flujo y corriente:

$$
\boxed{
L = \frac{\Phi_{total}}{i}
}
$$

Por tanto:

$$
\boxed{
L = \frac{\mu N^2 A}{\ell}
}
$$

Esta es la inductancia de un solenoide ideal largo.

---

# 3) Ley de Faraday (flujo variable → fem inducida)

La ley de Faraday establece:

$$
\boxed{
\mathcal{E} = - \frac{d\Phi_{total}}{dt}
}
$$

Como:

$$
\Phi_{total} = L i
$$

Entonces:

$$
\boxed{
\mathcal{E} = - L \frac{di}{dt}
}
$$

Esta es la ecuación fundamental de la autoinducción.

---

# 4) Significado del Signo Negativo (Ley de Lenz)

El signo negativo indica oposición:

- Si la corriente aumenta → la fem inducida se opone.
- Si la corriente disminuye → la fem inducida intenta mantenerla.

El inductor se opone a cambios bruscos de corriente.

---

# 5) Energía Almacenada

La potencia instantánea es:

$$
p(t) = v(t)i(t)
$$

Pero:

$$
v(t) = L \frac{di}{dt}
$$

Entonces:

$$
p(t) = L i \frac{di}{dt}
$$

Integrando:

$$
W_L = \int p(t)\, dt
= \int L i \frac{di}{dt} dt
$$

Cambio de variable:

$$
W_L = \int L i\, di
$$

$$
\boxed{
W_L = \frac{1}{2} L i^2
}
$$

La energía se almacena en el campo magnético.

---

# 6) Interpretación Energética en el Espacio

La densidad de energía magnética es:

$$
\boxed{
u_B = \frac{B^2}{2\mu}
}
$$

La energía total es:

$$
W = \int u_B \, dV
$$

En un solenoide uniforme se obtiene exactamente:

$$
W = \frac{1}{2} L i^2
$$

Esto demuestra que la energía no está “en el alambre”, sino en el campo.


---

# 7) Resumen Conceptual

| Etapa | Relación |
|-------|----------|
| Corriente → Campo | $B = \mu n i$ |
| Campo → Flujo | $\Phi = B A$ |
| Flujo → fem | $\mathcal{E} = -\frac{d\Phi}{dt}$ |
| Definición | $\Phi = L i$ |
| Resultado final | $v = L \frac{di}{dt}$ |
| Energía | $W = \frac{1}{2} L i^2$ |

---

> [!idea] # Idea Central
> 
> La autoinducción no es una propiedad “misteriosa” del inductor.
> 
> Es la consecuencia encadenada de:
> 
> 1. Corriente produce campo magnético.
> 2. El campo genera flujo.
> 3. Si la corriente cambia, el flujo cambia.
> 4. El flujo variable induce una fem que se opone al cambio.
>
> Es una manifestación directa de las ecuaciones de Maxwell.

---
