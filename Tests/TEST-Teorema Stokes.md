---
titulo: Teorema de Stokes
tema: Cálculo Vectorial
dificultad: avanzado
fuente: Stewart, Cálculo 8va ed. §16.8
cssclasses:
  - teorema
draft: true
---


# Teorema de Stokes

El Teorema de Stokes generaliza el Teorema de Green a superficies en $\mathbb{R}^3$. Relaciona la integral de línea de un campo vectorial sobre una curva cerrada $C$ con la integral de superficie del rotacional sobre cualquier superficie que tenga $C$ como frontera.

---

## Enunciado

> [!teorema] Teorema de Stokes 
> Sea $S$ una superficie orientable con frontera $C = \partial S$ con orientación positiva. Si $\mathbf{F}$ tiene derivadas parciales continuas en una región que contiene a $S$:
> 
> $$\oint_C \mathbf{F} \cdot d\mathbf{r} = \iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S}$$

---

## Forma del rotacional

El rotacional de $\mathbf{F} = P,\mathbf{i} + Q,\mathbf{j} + R,\mathbf{k}$ se calcula como el determinante formal:

$$\nabla \times \mathbf{F} = \begin{vmatrix} \mathbf{i} & \mathbf{j} & \mathbf{k} \ \partial_x & \partial_y & \partial_z \ P & Q & R \end{vmatrix}$$

Expandido explícitamente:

$$\nabla \times \mathbf{F} = \left(\frac{\partial R}{\partial y} - \frac{\partial Q}{\partial z}\right)\mathbf{i} - \left(\frac{\partial R}{\partial x} - \frac{\partial P}{\partial z}\right)\mathbf{j} + \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)\mathbf{k}$$

---

## Contexto teórico

> [!teoria] Orientación de la superficie 
> La orientación positiva de $C$ se determina por la **regla de la mano derecha**: si el pulgar apunta en la dirección del vector normal $\mathbf{n}$ de $S$, los dedos indican la orientación positiva de $C$.
> 
> Esto asegura coherencia entre la orientación de la curva frontera y la de la superficie.

---

## Definiciones previas

> [!definicion] Campo conservativo 
> Un campo vectorial $\mathbf{F}$ es **conservativo** en una región $D$ si existe una función escalar $f$ tal que: $$\mathbf{F} = \nabla f$$ En tal caso, $f$ se denomina **función potencial** de $\mathbf{F}$.

> [!definicion] Rotacional 
> El **rotacional** de $\mathbf{F}$ mide la tendencia de $\mathbf{F}$ a hacer rotar un objeto. Si $\nabla \times \mathbf{F} = \mathbf{0}$, el campo es **irrotacional**.

---

## Demostración (caso especial)

> [!demostracion] 
> Para $S$ gráfica de $z = g(x,y)$ Parametrizamos $S$ con $\mathbf{r}(x,y) = (x,, y,, g(x,y))$ sobre una región $D$ en el plano $xy$.
> 
> La integral de línea sobre $C$ se transforma en integral sobre $\partial D$ mediante el cambio de variable inducido por la parametrización. Aplicando el **Teorema de Green** a la región $D$:
> 
> $$\oint_{\partial D} \left(P + R,g_x\right)dx + \left(Q + R,g_y\right)dy$$
> 
> Expandiendo con la regla de la cadena y comparando con la integral de superficie de $\nabla \times \mathbf{F}$, los términos se cancelan simétricamente, obteniendo la igualdad deseada.

---

## Corolarios importantes

> [!corolario] 
> Campo irrotacional implica conservativo Si $\mathbf{F}$ es un campo irrotacional ($\nabla \times \mathbf{F} = \mathbf{0}$) en un dominio simplemente conexo, entonces $\mathbf{F}$ es conservativo: $$\oint_C \mathbf{F} \cdot d\mathbf{r} = 0 \quad \text{para toda curva cerrada } C$$

> [!corolario]
>  Independencia de la superficie La integral $\iint_S (\nabla \times \mathbf{F}) \cdot d\mathbf{S}$ es la misma para cualquier superficie $S$ con la misma frontera $C$ y la misma orientación.

---

## Lemas auxiliares

> [!lema] Lema de regularidad 
> Si $\mathbf{F} \in C^2$ en una región abierta, entonces $\nabla \cdot (\nabla \times \mathbf{F}) = 0$, es decir, el rotacional de cualquier campo es siempre un campo solenoidal.

---

## Proposición relacionada

> [!proposicion] Relación con el Teorema de Green
>  El Teorema de Green es un caso especial de Stokes donde $S$ es una región plana en $\mathbb{R}^2$ con $\mathbf{n} = \mathbf{k}$: $$\oint_C P,dx + Q,dy = \iint_D \left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)dA$$

---

## Axioma fundamental

> [!axioma] Axioma de orientabilidad 
> Toda superficie suave compacta en $\mathbb{R}^3$ que admite un campo normal continuo y no nulo es **orientable**. La esfera $S^2$ y el toro son orientables; la banda de Möbius no lo es.

---

## Ejemplo de aplicación

> [!ejemplo] Calcular $\oint_C \mathbf{F} \cdot d\mathbf{r}$ 
> Sea $\mathbf{F} = (-y^2,, x,, z^2)$ y $C$ la intersección del paraboloide $z = x^2 + y^2$ con el cilindro $x^2 + y^2 = 1$, orientada en sentido antihorario visto desde arriba.
> 
> **Rotacional:** $\nabla \times \mathbf{F} = (0,, 0,, 1 + 2y)$
> 
> **Superficie:** El disco $D: x^2 + y^2 \leq 1$ con $\mathbf{n} = \mathbf{k}$
> 
> $$\iint_D (1 + 2y),dA = \iint_D 1,dA + 2\iint_D y,dA = \pi + 0 = \pi$$
> 
> El segundo término es cero por simetría. **Resultado:** $\oint_C \mathbf{F} \cdot d\mathbf{r} = \pi$

---

## Notas adicionales

> [!note] Versión más general 
> El Teorema de Stokes generalizado (en el lenguaje de formas diferenciales) se enuncia como: $$\int_{\partial \Omega} \omega = \int_\Omega d\omega$$ donde $\omega$ es una $(n-1)$-forma diferencial y $\Omega$ es una $n$-variedad con frontera.

> [!tip] Estrategia de cálculo 
> Cuando $C$ es complicada pero existe una superficie $S$ con $\partial S = C$ simple, **siempre conviene usar Stokes** y calcular la integral de superficie en lugar de la integral de línea directamente.

> [!warning] Orientación crítica 
> Un error frecuente es no verificar la coherencia entre la orientación de $C$ y el vector normal elegido para $S$. Una orientación incorrecta invierte el signo del resultado.