---
title: Estabilidad de Sistemas
order: 4
tags:
  - control-clasico
  - teoria
  - analisis
  - estabilidad
draft: false
aliases:
  - estabilidad
  - estabilidad BIBO
  - estabilidad interna
  - estabilidad asintotica
---

# Estabilidad de Sistemas

> [!definicion]
> Un sistema LTI es **estable** si todos los polos de su función de transferencia $G(s)$ están en el **semiplano izquierdo** ($\Re(p_i)<0$). Equivalen tres lecturas: *BIBO* (toda entrada acotada da salida acotada), *asintótica* (con entrada nula el estado tiende a cero) y *de polos* (todos con parte real negativa). Polos sobre el eje imaginario simples → marginal; alguno en el derecho → inestable.

> [!info]
> Carpeta `3 Analisis/Estabilidad`. Reúne el criterio algebraico de [[Routh Hurwitz/index | Routh-Hurwitz]] y su [[Condicion Necesaria | condición necesaria]]. Los polos se calculan desde la [[Funcion Transferencia/index | función de transferencia]]; el análisis gráfico vive en [[Lugar Raices/index | lugar de las raíces]] y [[Respuesta Frecuencial/Nyquist/index | Nyquist]].

---

## Ejemplo

> [!ejemplo] Clasificar tres sistemas por sus polos
> Decidir la estabilidad de cada $G(s)$ ubicando sus polos.
>
> **Sistema A — $G(s)=\dfrac{1}{s^2+3s+2}$.** Denominador $s^2+3s+2=(s+1)(s+2)$ → polos $s=-1,-2$. Ambos con $\Re<0$ → **asintóticamente estable** (y por tanto BIBO).
>
> **Sistema B — $G(s)=\dfrac{1}{s^2+4}$.** Polos $s=\pm j2$, simples sobre el eje imaginario → **marginalmente estable**. Una entrada acotada ($\sin t$) produce salida acotada, pero la respuesta libre **oscila sin decaer**, no tiende a cero.
>
> **Sistema C — $G(s)=\dfrac{1}{s^2-s-2}$.** $s^2-s-2=(s-2)(s+1)$ → polos $s=2,-1$. Hay un polo en $\Re>0$ → **inestable**: un coeficiente negativo ($-s$) ya lo delata.
>
> | Sistema | Polos | $\Re(p_i)$ | Veredicto |
> |---|---|---|---|
> | A | $-1,\,-2$ | $<0$ | estable |
> | B | $\pm j2$ | $=0$ simples | marginal |
> | C | $2,\,-1$ | uno $>0$ | inestable |

> [!ejemplo] BIBO no es lo mismo que asintótica
> $G(s)=\dfrac{1}{s(s+1)}$ tiene polos $0,-1$. El polo en $s=0$ es simple, así que la respuesta libre queda acotada, pero ante un **escalón** la salida contiene un término $\propto t$ que crece sin cota → **no es BIBO estable**. El polo en el origen, marginal en respuesta libre, se vuelve no acotado al integrar la entrada.

---

## En qué consiste

> [!teoria]
> Para un sistema LTI con polos $p_i$, la respuesta libre es combinación de modos $e^{p_i t}$ (y $t^k e^{p_i t}$ si hay repetición). El signo de $\Re(p_i)$ fija el destino de cada modo:
>
> | Ubicación de polos | Estabilidad | Modo característico |
> |---|---|---|
> | Todos $\Re(p_i)<0$ | asintóticamente estable | $e^{\sigma t},\ \sigma<0$ (decae) |
> | Polo $s=0$ simple, resto $\Re<0$ | marginal | constante |
> | Par $\pm j\omega$ simple, resto $\Re<0$ | marginal | $\sin(\omega t)$ sostenido |
> | Algún $\Re(p_i)>0$ | inestable | $e^{\sigma t},\ \sigma>0$ (crece) |
> | Eje imaginario con multiplicidad $\ge2$ | inestable | $t\sin(\omega t)$, $t$ |

> [!teorema] BIBO vs. asintótica (sin cancelaciones polo-cero)
> - Asintóticamente estable (todos $\Re<0$) $\implies$ BIBO estable.
> - BIBO estable $\implies$ todos $\Re\le0$, y los de $\Re=0$ deben ser simples.
>
> La diferencia es el trato de los polos sobre el eje imaginario.

> [!warning] Cancelaciones ocultan inestabilidad interna
> $G(s)=\dfrac{s-1}{(s-1)(s+2)}$ se simplifica a $\dfrac{1}{s+2}$: la FT parece estable (polo en $-2$). Pero el modo interno asociado a $s=1$ sigue ahí y puede crecer sin cota. La estabilidad **interna** depende de **todos** los polos antes de cancelar; la **externa** (BIBO), solo de la FT simplificada. Ver [[Espacio Estados/index | espacio de estados]] para los autovalores de $\mathbf{A}$.

---

## Criterios disponibles

> [!info]
> | Método | Aplica a | Ventaja | Ver |
> |---|---|---|---|
> | Cálculo directo de polos | orden bajo | exacto | [[Polos Ceros \| polos y ceros]] |
> | Condición necesaria | cualquier orden | descarte rápido | [[Condicion Necesaria \| condición necesaria]] |
> | Routh-Hurwitz | cualquier orden | no factoriza | [[Routh Hurwitz/index \| Routh-Hurwitz]] |
> | Lugar de las raíces | un parámetro variable | muestra tendencia | [[Lugar Raices/index \| lugar de raíces]] |
> | Nyquist | realimentación | da márgenes | [[Respuesta Frecuencial/Nyquist/index \| Nyquist]] |
> | Autovalores de $\mathbf{A}$ | espacio de estados | estabilidad interna | [[Espacio Estados/index \| espacio de estados]] |

---

## Resumen

> [!resumen]
> | Concepto | Criterio |
> |---|---|
> | BIBO | toda entrada acotada → salida acotada |
> | Asintótica | $\lim_{t\to\infty}\lVert x(t)\rVert=0$ con entrada nula |
> | Polos | todos $\Re(p_i)<0$ |
> | Marginal | $\pm j\omega$ o $s=0$ **simples**, resto $\Re<0$ |
> | Inestable | algún $\Re(p_i)>0$, o eje imaginario con mult. $\ge2$ |
> | Conteo de inestables | cambios de signo en 1.ª columna de Routh |

> [!corolario]
> La estabilidad LTI se reduce a la geografía de los polos en el plano $s$: todos a la izquierda → estable; alguno a la derecha → inestable; sobre el eje (simples) → marginal. Cuando factorizar es costoso, [[Routh Hurwitz/index | Routh-Hurwitz]] da el veredicto y cuenta los polos inestables sin resolver el polinomio; la [[Condicion Necesaria | condición necesaria]] sirve de filtro previo.

> [!referencia]
> - Filtro previo: [[Condicion Necesaria]].
> - Criterio algebraico completo: [[Routh Hurwitz/index]].
> - Análisis gráfico con un parámetro: [[Lugar Raices/index]].
> - Estabilidad por frecuencia y márgenes: [[Respuesta Frecuencial/Nyquist/index | Nyquist]].
> - Modos naturales y polos: [[Polos Ceros]].
