# 🧩 Resumen de fórmulas — Cuerpo rígido en 2D

| **Concepto** | **Ecuación general** | **Descripción / Variables** |
|---------------|----------------------|------------------------------|
| **1️⃣ Segunda ley de Newton (traslación)** | $\sum \vec{F} = m \vec{a}_G$ | Relación entre la fuerza neta y la aceleración del centro de gravedad (G). |
| **2️⃣ Ecuaciones escalares (componentes)** | $\sum F_x = m a_{Gx}$  <br> $\sum F_y = m a_{Gy}$ | Descomposición en ejes cartesianos. |
| **3️⃣ Momento respecto al centro de gravedad (G)** | $\sum M_G = I_G \alpha$ | Rotación pura alrededor del centro de masa. |
| **4️⃣ Momento respecto a un punto arbitrario (O)** | $\sum M_O = I_G \alpha + m (\vec{r}_{G/O} \times \vec{a}_G)$ | Aplica cuando el punto O **no coincide con G**. |
| **5️⃣ Momento respecto a O usando inercia en O** | $\sum M_O = I_O \alpha$ | Forma simplificada usando el **momento de inercia trasladado** al punto O. |
| **6️⃣ Teorema del eje paralelo (para trasladar inercia)** | $I_O = I_G + m d^2$ | $d =$ distancia entre el punto O y el centro de gravedad G. |
| **7️⃣ Relación general entre momentos (O y G)** | $\sum M_O = \sum M_G + \vec{r}_{G/O} \times (m \vec{a}_G)$ | Expresa el momento total en O como suma del momento en G más el efecto de la traslación. |
| **8️⃣ Aceleración de un punto P del cuerpo** | $\vec{a}_P = \vec{a}_G + \vec{\alpha} \times \vec{r}_{P/G} - \omega^2 \vec{r}_{P/G}$ | Describe la aceleración de cualquier punto del cuerpo. |
| **9️⃣ En forma escalar (para 2D)** | $\sum M_G = I_G \alpha$  <br> $\sum M_O = I_O \alpha$  <br> $I_O = I_G + m d^2$ | En 2D, solo interviene la componente $z$ (momento y aceleración angular). |

---

✅ **Resumen rápido para examen:**

- **Traslación:** $\sum \vec{F} = m \vec{a}_G$  
- **Rotación (en G):** $\sum M_G = I_G \alpha$  
- **Rotación (en O):** $\sum M_O = I_G \alpha + m(\vec{r}_{G/O} \times \vec{a}_G)$  
- **Con inercia trasladada:** $\sum M_O = I_O \alpha$  
- **Eje paralelo:** $I_O = I_G + m d^2$

---


