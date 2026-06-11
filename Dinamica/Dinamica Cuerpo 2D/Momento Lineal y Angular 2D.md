# 💠 Cantidad de movimiento lineal y angular (2D, general y correcta)

---

## 🔹 1. Cantidad de movimiento lineal

| Concepto | Ecuación | Descripción breve |
|-----------|-----------|-------------------|
| Definición | $P = m v_G$ | Cantidad de movimiento del cuerpo. |
| Ecuación fundamental | $\dfrac{dP}{dt} = \sum F$ | La fuerza neta produce cambio en $P$. |
| Componentes | $\sum F_x = m a_{Gx}$<br>$\sum F_y = m a_{Gy}$ | Forma escalar en 2D. |
| Impulso lineal | $\Delta P = \int \sum F\,dt$ | Cambio de $P$ = impulso neto. |

---

## 🔹 2. Cantidad de movimiento angular (general respecto a un punto O)

| Concepto | Ecuación | Descripción breve |
|-----------|-----------|-------------------|
| Definición general | $H_O = I_G \omega + m(r_{G/O} \times v_G)$ | Momento angular respecto a $O$. |
| Derivada general | $\dfrac{dH_O}{dt} = \sum M_O - m(v_O \times v_G)$ | Válida aunque $O$ se mueva. |
| Si $O$ fijo ($v_O=0$) | $\dfrac{dH_O}{dt} = \sum M_O$ | Forma simplificada. |
| Si $O = G$ | $H_G = I_G \omega$<br>$\dfrac{dH_G}{dt} = \sum M_G = I_G \alpha$ | Centro de masa. |
| Relación de momentos | $\sum M_O = \sum M_G + (r_{G/O} \times \sum F)$ | Traslada el momento entre puntos. |
| Relación con aceleraciones | $\sum M_O = I_G \alpha + m(r_{G/O} \times a_G)$ | Ecuación de movimiento rotacional general. |

---

## 🔹 3. Momento de inercia (traslación entre puntos)

| Concepto | Ecuación | Descripción breve |
|-----------|-----------|-------------------|
| Teorema del eje paralelo | $I_O = I_G + m d^2$ | $d =$ distancia entre $O$ y $G$. |
| Aplicación (O fijo) | $\sum M_O = I_O \alpha$ | Solo si $O$ no acelera. |

---

## 🔹 4. Formas escalares en 2D

| Concepto | Ecuación escalar (z) | Descripción breve |
|-----------|----------------------|-------------------|
| Momento angular en $O$ | $H_O = I_G \omega + m(x_{G/O} v_{Gy} - y_{G/O} v_{Gx})$ | Momento angular total. |
| Derivada general | $\dfrac{dH_O}{dt} = \sum M_O - m(v_{Ox} v_{Gy} - v_{Oy} v_{Gx})$ | Forma generalizada. |
| Con aceleraciones | $\sum M_O = I_G \alpha + m(x_{G/O} a_{Gy} - y_{G/O} a_{Gx})$ | Movimiento plano. |
| Si $O$ fijo | $\dfrac{dH_O}{dt} = \sum M_O$ | Simplificación usual. |

---

## 🔹 5. Resumen final (para examen)

| Tipo | Expresión general | Comentario |
|------|-------------------|-------------|
| Lineal | $\dfrac{dP}{dt} = \sum F$ | Fuerzas → traslación. |
| Angular (general) | $\dfrac{dH_O}{dt} = \sum M_O - m(v_O \times v_G)$ | Torques → rotación. |
| Relación útil | $\sum M_O = I_G \alpha + m(r_{G/O} \times a_G)$ | Vincula aceleraciones. |
| Si $O$ fijo | $\sum M_O = I_O \alpha$ | Caso más común en 2D. |

---

✅ **Uso recomendado:**  
Estas son **todas las ecuaciones generales** de cantidad de movimiento lineal y angular en 2D.  
Recuerda que los productos cruzados en 2D se reducen a escalares:  
$r \times F = xF_y - yF_x$.
