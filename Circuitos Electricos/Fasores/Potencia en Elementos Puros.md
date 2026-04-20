---
title: Potencia en Régimen Sinusoidal – Casos Puros (R, L, C)
tags:
  - potencia
  - AC
  - fasores
  - RLC
draft: true
---


# Elementos Reactivos Puros — Energía y Potencia

---

## 🔹 Capacitor Puro (C)

### Impedancia

$$
Z_C = \frac{1}{j\omega C}
$$

$$
\theta = -90^\circ
$$

---

## 1) Energía Almacenada (Instantánea)

La energía eléctrica almacenada es:

$$
\boxed{
W_C(t) = \frac{1}{2} C v^2(t)
}
$$

Si:

$$
v(t) = V_m \cos(\omega t)
$$

Entonces:

$$
W_C(t) =
\frac{C V_m^2}{4}
\left(1 + \cos(2\omega t)\right)
$$

Observaciones:

- Siempre positiva
- Oscila a frecuencia $2\omega$
- No tiene promedio cero

---

## 2) Potencia Instantánea

Por definición:

$$
p(t) = v(t)i(t)
$$

Como:

$$
i(t) = C \frac{dv}{dt}
$$

Se obtiene:

$$
\boxed{
p(t) =
- \frac{\omega C V_m^2}{2}
\sin(2\omega t)
}
$$

Observaciones:

- Oscila alrededor de cero
- Promedio nulo
- Representa intercambio de energía

---

## 3) Potencia Activa

$$
\boxed{
P = 0
}
$$

---

## 4) Potencia Reactiva

En valores eficaces:

$$
\boxed{
Q =
- \omega C V_{ef}^2
}
$$

O en términos de valor máximo:

$$
Q =
- \frac{\omega C V_m^2}{2}
$$

---

## 🔹 Inductor Puro (L)

### Impedancia

$$
Z_L = j\omega L
$$

$$
\theta = +90^\circ
$$

---

## 1) Energía Almacenada (Instantánea)

$$
\boxed{
W_L(t) = \frac{1}{2} L i^2(t)
}
$$

Si:

$$
i(t) = I_m \cos(\omega t - 90^\circ)
$$

Entonces:

$$
W_L(t) =
\frac{L I_m^2}{4}
\left(1 + \cos(2\omega t)\right)
$$

---

## 2) Potencia Instantánea

$$
\boxed{
p(t) =
\frac{\omega L I_m^2}{2}
\sin(2\omega t)
}
$$

---

## 3) Potencia Activa

$$
P = 0
$$

---

## 4) Potencia Reactiva

$$
\boxed{
Q =
\omega L I_{ef}^2
}
$$

---

# 🔎 Idea Central

En elementos reactivos:

- La energía almacenada nunca es negativa.
- La potencia instantánea cambia de signo.
- La potencia promedio es cero.
- La potencia reactiva mide la amplitud del intercambio energético.

---
