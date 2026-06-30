---
title: Ecuación del Calor
order: 4
tags:
  - ecuaciones
  - edp
  - teoria
  - calor
  - index
draft: false
aliases:
  - ecuación del calor
  - ecuación de difusión
  - heat equation
---

# Ecuación del Calor

> [!definicion]
> La **ecuación del calor** (o de difusión) gobierna cómo se reparte una cantidad —temperatura, concentración— que fluye de donde hay más a donde hay menos:
> $$u_t=\alpha^2\,u_{xx}\qquad(\text{en 1D}),\qquad u_t=\alpha^2\,\nabla^2u\ \ (\text{general}),$$
> con $\alpha^2$ la **difusividad**. Es la EDP **parabólica** prototipo: **suaviza** los datos al instante y es **irreversible** en el tiempo.

> [!info]
> Primera de las tres ecuaciones madre del [[2 Ecuaciones en Derivadas Parciales/index| capítulo de EDP]] (tipo **parabólico**, ver [[Clasificacion Segundo Orden| clasificación]]). Se resuelve por [[Tecnica de Separacion| separación de variables]] en dominios acotados y por [[Calor en Dominio Infinito| transformada de Fourier]] en la recta.

---

## Qué la hace especial: difusión que suaviza

> [!teoria]
> La ecuación del calor tiene tres rasgos que la distinguen de la onda y de Laplace, todos consecuencia de su carácter parabólico:
> 1. **Suavizado instantáneo.** Por discontinuo que sea el dato inicial, para $t>0$ la solución es **infinitamente diferenciable**: la difusión lima toda aspereza de inmediato.
> 2. **Irreversibilidad.** La ecuación distingue el futuro del pasado: avanzar en el tiempo suaviza, pero **retroceder** (calor hacia atrás) es un problema mal planteado que amplifica el ruido. Es la flecha del tiempo de la termodinámica.
> 3. **Velocidad infinita de propagación.** Un cambio local de temperatura se "siente" en todo el dominio instantáneamente (aunque exponencialmente débil) — a diferencia de la onda.
>
> Estos rasgos se formalizan en el [[Principio del Maximo Parabolico| principio del máximo]] (la temperatura no crea picos nuevos) y en el [[Metodo de Energia Unicidad| método de energía]] (la "energía" decae, lo que da unicidad).

> [!info] Recorrido de la sección
> | Nota | Aporte |
> |---|---|
> | [[Derivacion del Calor\|Derivación]] | de la conservación + ley de Fourier a $u_t=\alpha^2u_{xx}$ |
> | [[Separacion Calor Dirichlet\|Separación con Dirichlet]] | extremos a temperatura fija; serie de senos |
> | [[Separacion Calor Neumann\|Separación con Neumann]] | extremos aislados; serie de cosenos |
> | [[Calor en Dominio Infinito\|Dominio Infinito]] | transformada de Fourier; solución fundamental (núcleo de calor) |
> | [[Principio del Maximo Parabolico\|Principio del Máximo]] | máximo en el borde o en $t=0$ |
> | [[Metodo de Energia Unicidad\|Método de Energía]] | la energía decae ⇒ unicidad |

## Resumen

> [!resumen]
> | Aspecto | Contenido |
> |---|---|
> | Ecuación | $u_t=\alpha^2 u_{xx}$ (parabólica) |
> | Datos | inicial $u(x,0)=f$ + frontera |
> | Método (acotado) | separación → $u=\sum b_n\operatorname{sen}\frac{n\pi x}{L}e^{-\alpha^2(n\pi/L)^2t}$ |
> | Método (recta) | transformada de Fourier; núcleo de calor |
> | Rasgos | suaviza, irreversible, decae |

> [!corolario]
> El calor es la ecuación del **olvido**: cada modo de Fourier decae como $e^{-\alpha^2\lambda_n t}$, y los más oscilantes (mayor $\lambda_n$) mueren primero. Por eso la solución se suaviza y tiende al equilibrio —una solución de [[Ecuacion de Laplace y Poisson/index| Laplace]]—.

> [!referencia]
> - De dónde sale: [[Derivacion del Calor]].
> - El método base: [[Separacion Calor Dirichlet]] y [[Tecnica de Separacion]].
> - El contraste hiperbólico: [[Ecuacion de Onda/index]].
