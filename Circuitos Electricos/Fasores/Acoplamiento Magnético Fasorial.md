---
title: Acoplamiento Inductivo en Régimen Fasorial
tags:
  - inductancia
  - acoplamiento_multiple
  - regimen_fasorial
  - impedancia_matricial
draft: true
---

# Acoplamiento Inductivo en Régimen Fasorial

Considérese un sistema de $n$ inductores linealmente acoplados, descrito en el dominio temporal por:

$$
\mathbf{v}(t) = \mathbf{L}\frac{d\mathbf{I}(t)}{dt}
$$

donde:

- $\mathbf{L}$ es la matriz de inductancias, simétrica y definida positiva.
- $\mathbf{I}(t)$ es el vector de corrientes instantáneas.

Supondremos régimen sinusoidal permanente a frecuencia angular $\omega$.

---

# 1) Representación Fasorial

Si las corrientes son sinusoidales:

$$
\mathbf{I}(t) = \Re \left\{ \tilde{\mathbf{I}} e^{j\omega t} \right\}
$$

entonces:

$$
\frac{d}{dt} \rightarrow j\omega
$$

Por lo tanto, la ecuación dinámica se transforma en:

$$
\boxed{
\tilde{\mathbf{V}} = j\omega \mathbf{L}\tilde{\mathbf{I}}
}
$$

Esta es la ecuación matricial del sistema acoplado en régimen fasorial.

---

# 2) Matriz de Impedancia Inductiva

Definimos la matriz de impedancias inductivas como:

$$
\boxed{
\mathbf{Z}_L = j\omega \mathbf{L}
}
$$

De modo que:

$$
\tilde{\mathbf{V}} = \mathbf{Z}_L \tilde{\mathbf{I}}
$$

La estructura del acoplamiento se conserva íntegramente en el dominio fasorial.

---

# 3) Forma Expandida

Para cada inductor $i$:

$$
\tilde{V}_i =
j\omega
\sum_{j=1}^{n}
L_{ij} \tilde{I}_j
$$

Separando autoinducción y mutua:

$$
\tilde{V}_i =
j\omega L_{ii} \tilde{I}_i
+
j\omega
\sum_{j\ne i}
L_{ij} \tilde{I}_j
$$

Cada tensión fasorial depende linealmente de todas las corrientes fasoriales del sistema.

---

# 4) Propiedades Estructurales

Dado que $\mathbf{L}$ es:

- Simétrica
- Definida positiva

entonces $\mathbf{Z}_L$ es:

- Simétrica
- Puramente imaginaria
- Hermítica (cuando se considera la estructura compleja del espacio fasorial)

Además:

$$
\tilde{\mathbf{I}}^\dagger \mathbf{Z}_L \tilde{\mathbf{I}}
=
j\omega
\tilde{\mathbf{I}}^\dagger
\mathbf{L}
\tilde{\mathbf{I}}
$$

lo que implica que el sistema no disipa potencia activa, sino que intercambia energía reactiva.

---

# 5) Potencia Compleja

La potencia compleja es:

$$
S =
\frac{1}{2}
\tilde{\mathbf{V}}^\dagger
\tilde{\mathbf{I}}
$$

Sustituyendo:

$$
S =
\frac{1}{2}
j\omega
\tilde{\mathbf{I}}^\dagger
\mathbf{L}
\tilde{\mathbf{I}}
$$

Como $\mathbf{L}$ es real y simétrica:

- La parte real de $S$ es cero.
- Toda la potencia es reactiva.

El sistema almacena y devuelve energía magnética sin disipación.

---

# 6) Interpretación Física

En régimen fasorial:

- El acoplamiento magnético se convierte en una interacción algebraica compleja.
- La derivada temporal desaparece como operador diferencial y se reemplaza por el factor $j\omega$.
- La estructura energética del sistema permanece codificada en $\mathbf{L}$.

El acoplamiento múltiple no se modifica conceptualmente; simplemente se expresa como una impedancia matricial.

---

# Resultado Final

En régimen sinusoidal permanente, un sistema de inductores acoplados queda completamente descrito por:

$$
\boxed{
\tilde{\mathbf{V}} = j\omega \mathbf{L}\tilde{\mathbf{I}}
}
$$

donde la matriz $\mathbf{L}$ determina la interacción magnética entre todos los devanados, y el factor $j\omega$ introduce la naturaleza reactiva del fenómeno.