# 💥 Constante de restitución en choques (3D y 2D — **general y completo**)

La **constante de restitución** $e$ describe cuánta “elasticidad” tiene un choque entre dos cuerpos.  
Mide la **capacidad de recuperar velocidad relativa** a lo largo de la línea normal de impacto.

---

# 🔹 1. Definición fundamental

| Concepto | Ecuación | Descripción |
|---------|----------|-------------|
| Definición | $e = -\dfrac{v_{f,n}^{(2)} - v_{f,n}^{(1)}}{v_{i,n}^{(2)} - v_{i,n}^{(1)}}$ | Razón entre velocidades relativas **después** y **antes** del choque, proyectadas sobre la **normal de impacto**. |
| Velocidad relativa inicial normal | $v_{i,n} = (\vec{v}_2-\vec{v}_1)\cdot\hat{n}$ | Componente normal de la velocidad relativa antes del choque. |
| Velocidad relativa final normal | $v_{f,n} = (\vec{v}_2'-\vec{v}_1')\cdot\hat{n}$ | Después del choque. |
| Normal del impacto | $\hat{n}=\dfrac{\vec{r}_{c2}-\vec{r}_{c1}}{\|\vec{r}_{c2}-\vec{r}_{c1}\|}$ | Línea que une los puntos de contacto. |

**Interpretación física**:  
- $e=1$ → choque **perfectamente elástico**, se conserva energía cinética normal.  
- $e=0$ → choque **perfectamente inelástico**, los cuerpos quedan con la misma velocidad normal.  
- $0<e<1$ → choque real con pérdidas.  
- $e>1$ (raro): interacción con energía añadida (trampolines, resortes, etc.).

---

# 🔹 2. Aplicación general (3D) — Cuerpos rígidos con rotación

Sea un punto de contacto $C$ en cada cuerpo:

| Elemento | Expresión | Descripción |
|----------|-----------|-------------|
| Velocidad del punto de contacto (cuerpo 1) | $\vec{v}_{C1}=\vec{v}_{G1}+\vec{\omega}_1\times\vec{r}_{C/G1}$ | Traslación + rotación. |
| Velocidad del punto de contacto (cuerpo 2) | $\vec{v}_{C2}=\vec{v}_{G2}+\vec{\omega}_2\times\vec{r}_{C/G2}$ | Igual para cuerpo 2. |
| Velocidad relativa normal | $v_{i,n}=(\vec{v}_{C2}-\vec{v}_{C1})\cdot\hat{n}$ | Antes del choque. |
| Velocidad relativa final | $v_{f,n}=(\vec{v}_{C2}'-\vec{v}_{C1}')\cdot\hat{n}$ | Después del choque. |
| Definición general de $e$ | $e=-\dfrac{v_{f,n}}{v_{i,n}}$ | La forma más compacta y general. |

> ✔️ **La constante de restitución siempre actúa SOLO en la dirección normal**.  
> ✔️ La componente tangencial involucra **fricción de impacto**, no $e$.

---

# 🔹 3. Impulso normal del choque

Si durante el choque actúa un **impulso normal** $J_n$ en dirección $\hat{n}$:

| Magnitud | Ecuación | Comentario |
|----------|----------|------------|
| Velocidad del CM tras choque | $\vec{v}_G'=\vec{v}_G+\dfrac{J_n}{m}\hat{n}$ | Para un cuerpo sin rotación. |
| Con rotación | $\vec{\omega}'=\vec{\omega}+\mathbf{I}^{-1}(\vec{r}_{C/G}\times J_n\hat{n})$ | Incremento rotacional. |
| Velocidad relativa final normal | $v_{f,n}=v_{i,n}-J_n\left(\dfrac{1}{m_1}+\dfrac{1}{m_2}+\Phi_1+\Phi_2\right)$ | $\Phi$ representan efectos rotacionales. |
| Fórmula completa del impulso | $J_n=-\dfrac{(1+e)v_{i,n}}{\left(\frac{1}{m_1}+\frac{1}{m_2}+\Phi_1+\Phi_2\right)}$ | **Impulso normal que impone el valor de $e$**. |

Donde  
$\Phi_1 = \hat{n}\cdot[(\mathbf{I}_1^{-1}(\vec{r}_{C/G1}\times\hat{n}))\times\vec{r}_{C/G1}]$  
y lo mismo para $\Phi_2$.

---

# 🔹 4. Casos especiales (resumen rápido)

| Caso | Resultado | Comentario |
|------|-----------|-------------|
| Cuerpos sin rotación | $J_n=-\dfrac{(1+e)v_{i,n}}{\frac{1}{m_1}+\frac{1}{m_2}}$ | Fórmula más usada en física básica. |
| Cuerpo chocando contra pared rígida | $v_{f,n}=-ev_{i,n}$ | Se refleja con factor $e$. |
| Choque totalmente inelástico ($e=0$) | $v_{f,n}=0$ | Velocidades normales quedan iguales. |
| Choque elástico ($e=1$) | $v_{f,n}=-v_{i,n}$ | Se conserva energía cinética normal. |
| Si solo se conocen velocidades escalares 1D | $e=\dfrac{v_2'-v_1'}{v_1-v_2}$ | Versión 1D típica en exámenes. |

---

# 🔹 5. Conservación de energía (normal)

El choque solo conserva energía normal si $e=1$:

$$
\frac{1}{2}\mu v_{i,n}^2 = \frac{1}{2}\mu v_{f,n}^2
$$

donde $\mu=\dfrac{m_1 m_2}{m_1+m_2}$ es la **masa reducida**.

Para $e<1$:

$$
\frac{v_{f,n}}{v_{i,n}}=-e
$$

---

# 🔹 6. Procedimiento estándar en problemas (paso a paso)

1. Identificar el punto de contacto $C$ y el vector normal $\hat{n}$.  
2. Calcular $\vec{v}_{C1}$ y $\vec{v}_{C2}$ antes del choque.  
3. Obtener la velocidad relativa inicial $v_{i,n}$.  
4. Aplicar la definición de $e$ para obtener $v_{f,n}$.  
5. Usar el impulso normal  
   $J_n=-\dfrac{(1+e)v_{i,n}}{D}$  
   donde $D$ depende de masas e inercias.  
6. Actualizar $\vec{v}_G'$ y $\vec{\omega}'$ de cada cuerpo.  

---

# 🔹 7. Resumen final (para examen)

| Concepto | Fórmula clave | Uso |
|----------|----------------|-----|
| Definición de $e$ | $e = -\dfrac{v_{f,n}}{v_{i,n}}$ | Núcleo de todo el método. |
| Velocidad relativa normal | $v_n=(\vec{v}_{C2}-\vec{v}_{C1})\cdot\hat{n}$ | Solo la componente normal importa. |
| Impulso normal | $J_n=-\dfrac{(1+e)v_{i,n}}{D}$ | Para obtener velocidades finales. |
| Caso pared rígida | $v_{f,n}=-ev_{i,n}$ | Forma directa. |
| $e=1$ | Choque perfectamente elástico | Conservación de energía normal. |
| $e=0$ | Choque perfectamente inelástico | Se adhieren en la normal. |

---

## ✔️ Notas finales

- La **componente tangencial no depende** de $e$ → depende de fricción de impacto.  
- El choque puede ser 3D, pero el análisis **siempre se proyecta sobre la normal**.  
- El uso de velocidades de **punto de contacto** es obligatorio en cuerpos rígidos.  
- Para choques complicados (rotación + 3D), la fórmula del **impulso general** es indispensable.

---
