---
title: Caso Simétrico y Convergencia Acelerada
tags:
  - metodos-numericos
  - teoria
  - algebra-lineal-numerica
  - autovalores
  - metodo-potencia
  - convergencia
draft: false
aliases:
  - Potencia para matrices simétricas
  - Convergencia cuadrática de Rayleigh
  - Symmetric power method
---

# Caso Simétrico y Convergencia Acelerada

> [!definicion]
> Cuando $A = A^T$ es **simétrica**, el [[Metodo Potencia Directo/index|método de la potencia]] hereda propiedades del teorema espectral que aceleran la convergencia: el [[Calculo Constante Normalizacion Rayleigh|cociente de Rayleigh]] aproxima el autovalor dominante con **error cuadrático** en el error del autovector, en lugar de lineal.

> [!info]
> El teorema espectral garantiza que toda matriz simétrica real tiene autovalores reales y una base **ortonormal** de autovectores $\{v_1,\dots,v_n\}$ ($v_i^T v_j = \delta_{ij}$). Esta ortogonalidad es la responsable de la aceleración: elimina el término lineal del error del cociente de Rayleigh.

---

## Convergencia cuadrática del cociente de Rayleigh

> [!teorema]
> Sea $A = A^T$ con autovalor dominante $\lambda_1$ y autovector unitario $v_1$. Si el iterado normalizado $y^{(k)}$ satisface $y^{(k)} = v_1 + O(\theta^k)$ con $\theta = |\lambda_2/\lambda_1|$, entonces el cociente de Rayleigh
> $$\lambda^{(k)} = \frac{y^{(k)T} A y^{(k)}}{y^{(k)T} y^{(k)}}$$
> aproxima $\lambda_1$ con error
> $$|\lambda^{(k)} - \lambda_1| = O(\theta^{2k}),$$
> **el cuadrado** del error del autovector $O(\theta^k)$.

> [!demostracion]
> Sea $y = v_1 + \sum_{i\geq 2} \epsilon_i v_i$ con $\|y\|=1$ aproximadamente y $\epsilon_i = O(\theta^k)$. Por ortonormalidad $v_i^T v_j = \delta_{ij}$ y $A v_i = \lambda_i v_i$:
> $$y^T A y = \Big(v_1 + \sum_{i\geq2}\epsilon_i v_i\Big)^T\Big(\lambda_1 v_1 + \sum_{i\geq2}\epsilon_i \lambda_i v_i\Big) = \lambda_1 + \sum_{i\geq 2}\epsilon_i^2 \lambda_i,$$
> $$y^T y = 1 + \sum_{i\geq2}\epsilon_i^2.$$
> Los términos cruzados $\epsilon_i v_1^T v_i$ se **anulan** por ortogonalidad (aquí está la clave). Entonces
> $$\lambda^{(k)} = \frac{\lambda_1 + \sum_{i\geq2}\epsilon_i^2\lambda_i}{1 + \sum_{i\geq2}\epsilon_i^2} = \lambda_1 + \sum_{i\geq2}\epsilon_i^2(\lambda_i - \lambda_1) + O(\epsilon^4),$$
> de modo que $|\lambda^{(k)} - \lambda_1| = O(\epsilon^2) = O(\theta^{2k})$.

> [!info]
> En el caso **no simétrico** los términos cruzados no se cancelan y el error del autovalor es $O(\theta^k)$, igual que el del autovector. La simetría duplica la velocidad efectiva con que se estima $\lambda_1$.

---

## Ejemplo: comparación de tasas

> [!ejemplo]
> **Matriz simétrica $A = \begin{pmatrix} 2 & 1 \\ 1 & 2 \end{pmatrix}$**, autovalores $\lambda_1 = 3$, $\lambda_2 = 1$, $\theta = 1/3$. Partiendo de $y^{(0)} = (1,0)^T$:
>
> | $k$ | error autovector $\sim\theta^k$ | error autovalor $|\lambda^{(k)}-3|$ | $\sim\theta^{2k}$ |
> |:---:|:---:|:---:|:---:|
> | 1 | 0.333 | $0.5$ | 0.111 |
> | 2 | 0.111 | $0.1$ | 0.0123 |
> | 3 | 0.037 | $0.02$ | 0.00137 |
> | 4 | 0.012 | $0.004$ | 0.000152 |
>
> El error del autovalor decae aproximadamente como $\theta^{2k}$ (columna derecha), mientras que el del autovector lo hace como $\theta^k$: el cociente de Rayleigh gana **el doble** de dígitos por iteración para $\lambda_1$.

---

## Propiedades adicionales del caso simétrico

> [!proposicion]
> Para $A = A^T$:
> 1. **Autovalores reales** y autovectores ortogonales (teorema espectral): se evitan pares complejos conjugados que romperían la dominancia.
> 2. **Principio minimax (Courant–Fischer):** $\lambda_1 = \max_{\|y\|=1} y^T A y$, de modo que el cociente de Rayleigh es una cota inferior monótona de $\lambda_1$ y su maximización tiene sentido variacional.
> 3. **Deflación estable:** tras hallar $(\lambda_1, v_1)$, la matriz deflactada $A - \lambda_1 v_1 v_1^T$ conserva la simetría y los demás autovalores, permitiendo iterar para $\lambda_2$.

> [!warning]
> La aceleración cuadrática afecta solo a la **estimación del autovalor**, no a la del **autovector**, que sigue convergiendo linealmente con factor $\theta = |\lambda_2/\lambda_1|$. Para acelerar también el autovector se recurre a la [[Potencia Desplazada Aceleracion Convergencia|iteración del cociente de Rayleigh]] (RQI), que para matrices simétricas alcanza convergencia **cúbica**.

---

## Iteración del cociente de Rayleigh (RQI)

> [!teoria]
> Combinando [[Potencia Inversa Valor Propio Menor Modulo|potencia inversa]] con desplazamiento adaptativo $\mu_k = \lambda^{(k)}$ (el propio cociente de Rayleigh), se obtiene la RQI:
> $$(A - \mu_k I)\,z = y^{(k)}, \qquad y^{(k+1)} = z/\|z\|, \qquad \mu_{k+1} = y^{(k+1)T}A\,y^{(k+1)}.$$
> Para matrices simétricas su convergencia es **cúbica** (el número de dígitos correctos se triplica), a costa de resolver un sistema con matriz cambiante en cada paso.

---

## Relación con otras notas

> [!info]
> - El cociente de Rayleigh y su normalización: [[Calculo Constante Normalizacion Rayleigh]].
> - La tasa lineal $\theta = |\lambda_2/\lambda_1|$ del autovector: [[Velocidad Convergencia Razon Lambda2 Lambda1]].
> - Las hipótesis que la simetría refuerza: [[Fundamentos Valor Propio Dominante]].
> - El desplazamiento adaptativo y la potencia inversa: [[Variantes Metodo Potencia/index]].

---

## Resumen

| Aspecto | No simétrico | Simétrico ($A=A^T$) |
|:---|:---|:---|
| Autovalores | posibles complejos | reales |
| Autovectores | base general | base ortonormal |
| Error autovector | $O(\theta^k)$ | $O(\theta^k)$ |
| Error autovalor (Rayleigh) | $O(\theta^k)$ | $O(\theta^{2k})$ |
| RQI | cuadrática | cúbica |

> [!corolario]
> La simetría de $A$ acelera el método de la potencia gracias a la ortogonalidad de los autovectores del teorema espectral: los términos cruzados del cociente de Rayleigh se cancelan y la estimación del autovalor dominante converge cuadráticamente $O(\theta^{2k})$ frente a la lineal $O(\theta^k)$ del autovector. Sumado al principio minimax y a la deflación estable, esto hace del caso simétrico el escenario más favorable, y abre la puerta a la iteración del cociente de Rayleigh con convergencia cúbica. La tasa base sigue siendo $\theta = |\lambda_2/\lambda_1|$, analizada en [[Velocidad Convergencia Razon Lambda2 Lambda1]].
