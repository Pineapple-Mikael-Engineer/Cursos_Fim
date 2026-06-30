---
title: Pseudo-tensores
order: 3
tags:
  - analisis-tensorial
  - teoria
  - tensores
  - pseudo-objetos
  - levi-civita
draft: false
aliases:
  - pseudotensor
  - pseudo-tensores
  - tensor axial
  - pseudotensor
---

# Pseudo-tensores

> [!definicion]
> Un **pseudo-tensor** transforma como un tensor regular **salvo por un factor $|a|$ extra**:
> $$\text{tensor: } T'_{rs\dots}=T_{ij\dots}\,a_{ri}a_{sj}\dots\qquad\Longleftrightarrow\qquad\text{pseudo-tensor: } T'_{rs\dots}=|a|\,T_{ij\dots}\,a_{ri}a_{sj}\dots,$$
> un factor $a$ por cada índice más **un** factor $|a|=\det[a]=\pm1$. El **símbolo de Levi-Civita** $\varepsilon_{ijk}$ es el pseudo-tensor por excelencia: invariante bajo rotaciones, cambia de signo bajo reflexiones.

> [!info]
> Sección **4.6.3** del libro; cierra [[index | Pseudo-objetos]]. Generaliza a rango arbitrario lo visto en [[Pseudo-vectores]] (rango 1) y [[Pseudo-escalares]] (rango 0). El protagonista es el [[Simbolo Levi-Civita | símbolo $\varepsilon_{ijk}$]], que define el [[Producto Cruz]] y por tanto es la fuente del carácter axial de toda la familia.

---

## Ejemplo

> [!ejemplo]
> **El símbolo de Levi-Civita es un pseudo-tensor.** Se demuestra usando que el producto cruz $\vec A\times\vec B$ apunta en direcciones físicas distintas en un sistema derecho y en uno izquierdo.
>
> > [!demostracion]
> > **Paso 1 — El cruz en ambos sistemas.** Sea el sistema primado derecho y el no primado izquierdo. Generando $\vec A\times\vec B$ con $\varepsilon$ en cada sistema:
> > $$A_iB_j\,\varepsilon_{ijk}\,\hat e_k=-A'_rB'_s\,\varepsilon'_{rst}\,\hat e'_t.$$
> > El signo menos aparece porque la dirección física del producto cruz **difiere** entre los dos sistemas (orientaciones opuestas).
> >
> > **Paso 2 — Transformar los vectores regulares.** $\vec A$, $\vec B$ y los vectores base son **regulares**, así que transforman sin $|a|$: $A'_r=a_{ri}A_i$, etc. Escribiendo las cantidades primadas en términos de las no primadas, la igualdad del Paso 1 se vuelve
> > $$A_iB_j\,\varepsilon_{ijk}\,\hat e_k=-A_iB_j\,a_{ri}a_{sj}a_{tk}\,\varepsilon'_{rst}\,\hat e_k.$$
> >
> > **Paso 3 — Cancelar los vectores arbitrarios.** Como la identidad vale para $\vec A$ y $\vec B$ **cualesquiera**, igualan los coeficientes:
> > $$\varepsilon_{ijk}=-\,a_{ri}a_{sj}a_{tk}\,\varepsilon'_{rst}.$$
> >
> > **Paso 4 — Generalizar con $|a|$.** El signo menos surgió por tener orientaciones opuestas ($|a|=-1$). Si ambos sistemas tienen la misma orientación, el signo desaparece. El caso general de una transformación ortonormal arbitraria se escribe con $|a|$:
> > $$\boxed{\ \varepsilon_{ijk}=|a|\,a_{ri}a_{sj}a_{tk}\,\varepsilon'_{rst}\ }.$$
> > Esta es la ley de un pseudo-tensor de rango 3. **Conclusión:** $\varepsilon_{ijk}$ es un pseudo-tensor.

---

## En qué consiste

> [!teoria]
> La ley de un pseudo-tensor es la del tensor regular con un $|a|$ pegado adelante:
> $$T'_{rs\dots}=|a|\,T_{ij\dots}\,a_{ri}a_{sj}\dots$$
> Para $|a|=+1$ (rotaciones) es indistinguible de un tensor. Bajo reflexiones ($|a|=-1$) cambia de signo. Que $\varepsilon_{ijk}$ sea un pseudo-tensor es coherente: sus **componentes son las mismas en todo sistema ortonormal** ($\varepsilon_{123}=+1$, etc.), lo cual solo es posible si el factor $|a|$ compensa exactamente el cambio de signo que las reflexiones inducirían en un tensor ordinario. Por eso $\varepsilon_{ijk}$ se llama, con propiedad, un **pseudo-tensor isótropo**.

> [!info] Regulares vs pseudo, por rango
> | Rango | Regular | Ley regular | Pseudo | Ley pseudo |
> |---|---|---|---|---|
> | 0 | escalar | $S'=S$ | pseudo-escalar | $S'=\|a\|\,S$ |
> | 1 | vector (polar) | $v'_r=v_i a_{ri}$ | pseudo-vector (axial) | $v'_r=\|a\|\,v_i a_{ri}$ |
> | 2 | tensor | $T'_{rs}=T_{ij}a_{ri}a_{sj}$ | pseudo-tensor | $T'_{rs}=\|a\|\,T_{ij}a_{ri}a_{sj}$ |
> | 3 | tensor rango 3 | $T'=T\,a\,a\,a$ | pseudo-tensor ($\varepsilon_{ijk}$) | $T'=\|a\|\,T\,a\,a\,a$ |

> [!info] Contar factores $|a|$
> Un objeto construido combinando regulares y pseudo es pseudo si el número total de factores $\varepsilon$ (o de productos cruz) es **impar**, y regular si es **par**. Así, $\vec A\times\vec B$ (un $\varepsilon$) es pseudo-vector; $(\vec A\times\vec B)\cdot\vec C$ (un $\varepsilon$) es pseudo-escalar; pero $(\vec A\times\vec B)\cdot(\vec C\times\vec D)$ (dos $\varepsilon$) es un escalar verdadero, pues $|a|^2=1$.

## Resumen

> [!resumen]
> | Aspecto | Resultado |
> |---|---|
> | Tensor | $T'_{rs\dots}=T_{ij\dots}a_{ri}a_{sj}\dots$ |
> | Pseudo-tensor | $T'_{rs\dots}=\|a\|\,T_{ij\dots}a_{ri}a_{sj}\dots$ |
> | Pseudo-tensor estrella | símbolo de Levi-Civita $\varepsilon_{ijk}$ |
> | Bajo rotación ($\|a\|=+1$) | idéntico a un tensor |
> | Bajo reflexión ($\|a\|=-1$) | cambia de signo |
> | Regla de paridad | nº impar de $\varepsilon$ $\Rightarrow$ pseudo |

> [!corolario]
> Un pseudo-tensor es un tensor con un factor $|a|$ extra en su ley de transformación. El símbolo de Levi-Civita $\varepsilon_{ijk}$ es el caso canónico: sus componentes son invariantes en todo sistema ortonormal precisamente porque el $|a|$ cancela el efecto de las reflexiones. Es la fuente común del carácter axial de los [[Pseudo-vectores]] y [[Pseudo-escalares]], ya que define el [[Producto Cruz]].

> [!referencia]
> - El símbolo $\varepsilon_{ijk}$ en detalle: [[Simbolo Levi-Civita]].
> - Casos de rango 1 y 0: [[Pseudo-vectores]], [[Pseudo-escalares]].
> - Marco general: [[index | Pseudo-objetos]].
