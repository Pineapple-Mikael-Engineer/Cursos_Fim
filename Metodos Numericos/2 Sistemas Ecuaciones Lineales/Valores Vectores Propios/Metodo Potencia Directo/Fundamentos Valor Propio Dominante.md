---
title: Fundamentos del Valor Propio Dominante
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - autovalores
  - metodo-potencia
draft: false
aliases:
  - Valor propio dominante
  - Autovalor dominante
  - Dominant eigenvalue
  - Hipótesis del método de la potencia
---

# Fundamentos del Valor Propio Dominante

> [!definicion]
> Sea $A \in \mathbb{R}^{n\times n}$ con autovalores $\lambda_1, \dots, \lambda_n$. Se dice que $\lambda_1$ es el **autovalor dominante** si es estrictamente mayor en módulo que todos los demás:
> $$|\lambda_1| > |\lambda_2| \geq |\lambda_3| \geq \cdots \geq |\lambda_n|.$$
> Su autovector asociado $v_1$ es la **dirección dominante**. La existencia de un autovalor dominante (con esta desigualdad **estricta**) es la hipótesis básica del [[Metodo Potencia Directo/index|método de la potencia]].

> [!info]
> Esta nota fija las hipótesis estructurales que hacen converger al método: dominancia estricta, diagonalizabilidad y componente inicial no nula en $v_1$. El algoritmo y su demostración de convergencia están en el [[Metodo Potencia Directo/index|índice del método]]; aquí se justifica *por qué* esas condiciones son necesarias.

---

## Las tres hipótesis

> [!axioma]
> El método de la potencia converge a $(\lambda_1, v_1)$ si:
> 1. **Diagonalizabilidad:** $A$ admite una base de autovectores $\{v_1, \dots, v_n\}$ de $\mathbb{R}^n$.
> 2. **Dominancia estricta:** $|\lambda_1| > |\lambda_2|$.
> 3. **Componente inicial:** el vector de arranque $y^{(0)} = \sum_i c_i v_i$ tiene $c_1 \neq 0$.

> [!teoria]
> El mecanismo es la **amplificación relativa** del modo dominante. Como $A^k v_i = \lambda_i^k v_i$,
> $$A^k y^{(0)} = \lambda_1^k\Big(c_1 v_1 + \sum_{i\geq 2} c_i \big(\tfrac{\lambda_i}{\lambda_1}\big)^k v_i\Big),$$
> y los cocientes $|\lambda_i/\lambda_1| < 1$ aniquilan toda componente salvo la de $v_1$. La dominancia estricta es lo que garantiza ese decaimiento; sin ella, dos modos sobreviven y la dirección no se estabiliza.

---

## Existencia del autovalor dominante

> [!teorema]
> **Teorema de Perron–Frobenius (caso suficiente).** Si $A$ es una matriz cuadrada con todas sus entradas positivas ($a_{ij} > 0$), entonces:
> 1. Existe un autovalor real $\lambda_1 > 0$ con $\lambda_1 = \rho(A)$ (radio espectral), estrictamente dominante.
> 2. Su autovector $v_1$ puede elegirse con todas las componentes positivas.
> 3. $\lambda_1$ es simple (multiplicidad algebraica $1$).

> [!info]
> Perron–Frobenius garantiza la hipótesis de dominancia para clases importantes: matrices estocásticas (cadenas de Markov), matrices de adyacencia de grafos conexos, matrices de Leslie en dinámica de poblaciones. Es la base teórica de aplicaciones como **PageRank**, donde el autovector dominante de una matriz estocástica gigante es el vector de relevancia.

---

## Ejemplo: identificación del modo dominante

> [!ejemplo]
> **Matriz con dominancia clara.** Para
> $$A = \begin{pmatrix} 4 & 1 \\ 2 & 3 \end{pmatrix},$$
> los autovalores son $\lambda_1 = 5$, $\lambda_2 = 2$, con $|\lambda_2/\lambda_1| = 0.4$. El autovector dominante es $v_1 = (1,1)^T$.
>
> Partiendo de $y^{(0)} = (1,0)^T = c_1 v_1 + c_2 v_2$ (con $c_1 \neq 0$), la componente de $v_2$ se atenúa por $0.4^k$:
>
> | $k$ | $(\lambda_2/\lambda_1)^k$ | peso relativo de $v_2$ |
> |:---:|:---:|:---:|
> | 1 | 0.400 | 40 % |
> | 2 | 0.160 | 16 % |
> | 3 | 0.064 | 6.4 % |
> | 5 | 0.010 | 1.0 % |
>
> Tras pocas iteraciones la dirección es esencialmente $v_1$. La velocidad de esta atenuación se cuantifica en [[Velocidad Convergencia Razon Lambda2 Lambda1]].

---

## Cuándo falla cada hipótesis

> [!warning]
> | Hipótesis violada | Síntoma | Remedio |
> |:---|:---|:---|
> | $\|\lambda_1\| = \|\lambda_2\|$ (p. ej. $\pm\lambda$ o par complejo conjugado) | la dirección **oscila**, no converge | desplazamiento $A - \mu I$, o método para bloques |
> | $c_1 = 0$ (arranque ortogonal a $v_1$) | en aritmética exacta converge a $v_2$ | en la práctica, el redondeo reintroduce $c_1 \neq 0$ y reaparece $v_1$ |
> | $A$ no diagonalizable (bloque de Jordan) | convergencia degradada a orden polinómico | análisis vía forma de Jordan |
> | $\|\lambda_2/\lambda_1\| \approx 1$ | convergencia muy lenta | [[Potencia Desplazada Aceleracion Convergencia\|desplazamiento]] |

> [!proposicion]
> Para matrices **simétricas** ($A = A^T$) la diagonalizabilidad está garantizada (teorema espectral): autovalores reales y autovectores ortogonales. Esto refuerza las hipótesis y mejora la convergencia, como se detalla en [[Caso Simetrico Convergencia Acelerada]].

---

## Relación con otras notas

> [!info]
> - El algoritmo completo, normalización y cociente de Rayleigh están en [[Metodo Potencia Directo/index]].
> - La tasa de convergencia $|\lambda_2/\lambda_1|$ se analiza en [[Velocidad Convergencia Razon Lambda2 Lambda1]].
> - El caso $A = A^T$ y su aceleración en [[Caso Simetrico Convergencia Acelerada]].
> - Para obtener autovalores **no** dominantes se rompe esta hipótesis a propósito mediante [[Variantes Metodo Potencia/index|potencia inversa y desplazada]].

---

## Resumen

| Elemento | Condición |
|:---|:---|
| Dominante | $|\lambda_1| > |\lambda_2|$ (estricto) |
| Diagonalizable | base de autovectores existe |
| Arranque válido | $c_1 \neq 0$ |
| Garantía de existencia | Perron–Frobenius si $a_{ij} > 0$ |
| Tasa | $|\lambda_2/\lambda_1|$ |

> [!corolario]
> El método de la potencia descansa sobre tres hipótesis: diagonalizabilidad, dominancia estricta $|\lambda_1| > |\lambda_2|$ y componente inicial no nula en $v_1$. La dominancia es la clave: convierte la aplicación repetida de $A$ en un filtro que amplifica el modo $v_1$ y atenúa los demás por $(\lambda_i/\lambda_1)^k$. El teorema de Perron–Frobenius asegura esta dominancia para matrices positivas, fundamentando aplicaciones como PageRank y las cadenas de Markov. Cuando la dominancia se rompe, el método oscila o se ralentiza, lo que motiva las [[Variantes Metodo Potencia/index|variantes desplazada e inversa]] y el tratamiento especial del [[Caso Simetrico Convergencia Acelerada|caso simétrico]].
