---
cssclasses:
  - idea
tags:
  - analisis
  - continuidad
materia: calculo
dificultad: intermedio
fuente: Rudin, Análisis Matemático §4
draft: true
---

# Teorema del Valor Intermedio

Demostramos que toda función continua en $[a,b]$ toma todos los valores entre $f(a)$ y $f(b)$.

## Hipótesis

Sea $f:[a,b]\to\mathbb{R}$ continua, con $f(a) < k < f(b)$. Construimos el conjunto:

$$S = \{ x \in [a,b] \mid f(x) < k \}$$

$S$ es no vacío (contiene a $a$) y acotado superiormente por $b$.

## El candidato $c$

Por el axioma del supremo existe $c = \sup S \in [a,b]$. Probaremos que $f(c) = k$ descartando las otras dos posibilidades.

## Descartar $f(c) < k$

Sea $\varepsilon = k - f(c) > 0$. Por continuidad existe $\delta > 0$ tal que para $x \in (c, c+\delta)$:

$$f(x) < f(c) + \varepsilon = k$$

Esto implicaría $x \in S$ con $x > c$, contradiciendo que $c = \sup S$.

## Descartar $f(c) > k$

Sea $\varepsilon = f(c) - k > 0$. Por continuidad existe $\delta > 0$ tal que para $x \in (c-\delta, c)$:

$$f(x) > k \implies x \notin S$$

Entonces $c - \delta$ sería cota superior de $S$ menor que $c$. Contradicción.

Habiendo descartado ambas posibilidades, concluimos que $f(c) = k$.

> [!cuidado] La continuidad es esencial
> La función de Heaviside $H(x)$ satisface $H(-1)=0$ y $H(1)=1$, pero no existe $c$ con $H(c) = \tfrac{1}{2}$ porque es discontinua en $0$.
