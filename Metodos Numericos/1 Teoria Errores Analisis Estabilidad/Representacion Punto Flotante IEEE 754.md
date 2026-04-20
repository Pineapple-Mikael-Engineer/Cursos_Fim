---
title: Representacion Punto Flotante IEEE 754
tags:
  - metodos-numericos
  - teoria
  - aritmetica-computacional
  - error-numerico
draft: false
aliases:
  - IEEE 754
  - Punto flotante
  - Formato binary32
  - Formato binary64
---

# Representación Punto Flotante IEEE 754

> [!definicion]
> Un número en punto flotante según el estándar IEEE 754 se representa mediante la terna $(s, e, f)$ y se interpreta como:
> $$x = (-1)^s \cdot (1 + f) \cdot 2^{e - \text{sesgo}}$$
> donde:
> - $s \in \{0,1\}$ es el **bit de signo**.
> - $e$ es el **exponente sesgado** (entero sin signo).
> - $f$ es la **fracción** (parte fraccionaria del significando).
> - $\text{sesgo}$ es una constante que depende de la precisión.

El estándar define varios formatos. Los más utilizados en métodos numéricos son la precisión simple (32 bits) y la doble (64 bits).

| Parámetro       | Precisión simple (binary32) | Precisión doble (binary64) |
| :-------------- | :-------------------------: | :------------------------: |
| Bits totales    |            $32$             |            $64$            |
| Signo ($s$)     |           $1$ bit           |          $1$ bit           |
| Exponente ($e$) |          $8$ bits           |         $11$ bits          |
| Mantisa ($f$)   |          $23$ bits          |         $52$ bits          |
| Sesgo           |            $127$            |           $1023$           |
 - **binary32:**
   `s eeeeeeee fffffffffffffffffffffff` 
 - **binary64:**
   `s eeeeeeeeeee fffff...` 

---

## Normalización y el bit implícito

Para números en rango normalizado ($1 \leq e \leq 2^k-2$), el significando efectivo $M$ es $1.f$. El $1$ a la izquierda del punto binario **no se almacena**, lo que otorga un bit extra de precisión (bit implícito u *hidden bit*).

La fracción almacenada $f$ representa la suma:
$$f = b_1 2^{-1} + b_2 2^{-2} + \dots + b_{p-1} 2^{-(p-1)}$$
donde $p$ es la precisión ($24$ para simple, $53$ para doble).

> [!info]
> **Valores especiales del exponente $e$.**
> El estándar reserva los valores extremos del exponente para casos excepcionales:
> - **$e = 0$ y $f = 0$:** Cero ($\pm 0$).
> - **$e = 0$ y $f \neq 0$:** Números **subnormales** (Ver [[Underflow y Numeros Subnormales]]).
> - **$e = 2^k-1$ y $f = 0$:** Infinito ($\pm\infty$) (Ver [[Overflow e Infinito]]).
> - **$e = 2^k-1$ y $f \neq 0$:** **NaN** (*Not a Number*).

---

## Conversión Decimal a Binario IEEE 754 (Ejemplo Fundamental)

Para entender cómo se almacena un número real, es necesario dominar el proceso de codificación manual.

> [!ejemplo]
> **Codificar el número $-12.625$ en formato binary32 (precisión simple).**
> 
> **1. Bit de signo $s$:**
> El número es negativo $\implies s = 1$.
> 
> **2. Convertir valor absoluto a binario:**
> - Parte entera $12$: $12_{10} = 1100_2$.
> - Parte fraccionaria $0.625$:
>   - $0.625 \times 2 = 1.25 \to 1$
>   - $0.25 \times 2 = 0.5 \to 0$
>   - $0.5 \times 2 = 1.0 \to 1$
>   - Resultado: $0.101_2$.
> 
> Valor absoluto en binario: $1100.101_2$.
> 
> **3. Normalizar a la forma $1.f \times 2^E$:**
> $$1100.101_2 = 1.100101_2 \times 2^3$$
> El exponente real es $E = 3$.
> 
> **4. Calcular exponente sesgado $e$:**
> $e = E + \text{sesgo} = 3 + 127 = 130_{10}$.
> Convertir $130$ a binario de $8$ bits: $130 = 128 + 2 \implies 10000010_2$.
> 
> **5. Extraer la fracción $f$ (23 bits):**
> Del significando normalizado $1.100101$, tomamos la parte fraccionaria y rellenamos con ceros:
> $f = 10010100000000000000000_2$.
> 
> **6. Representación final (32 bits):**
> ```
> s |    e    |            f
> 1 | 10000010 | 10010100000000000000000
> ```
> En hexadecimal: `0xC14B0000`.

> [!ejemplo]
> **Decodificar el valor binary32 `0x40A00000` a decimal.**
> 
> **1. Descomponer en bits:**
> `0x40A00000` = `0100 0000 1010 0000 0000 0000 0000 0000`
> - $s = 0$ (positivo)
> - $e = 10000001_2 = 129_{10}$
> - $f = 01000000000000000000000_2$
> 
> **2. Calcular exponente real $E$:**
> $E = e - \text{sesgo} = 129 - 127 = 2$.
> 
> **3. Reconstruir significando:**
> $M = 1.f = 1.01_2 = 1 + 0 \cdot 2^{-1} + 1 \cdot 2^{-2} = 1.25_{10}$.
> 
> **4. Valor final:**
> $$x = (-1)^0 \cdot 1.25 \cdot 2^2 = 1.25 \cdot 4 = 5.0$$
> El número representado es $5.0$.

---

## Errores inherentes a la representación

Debido a que la mantisa tiene longitud finita, la mayoría de los números reales no pueden representarse exactamente.

> [!info]
> El **error de redondeo** al almacenar un número real $x$ está acotado por la [[Epsilon Maquina y Precision Relativa|Unidad de Redondeo]] $u$.
> $$\frac{|x - \text{fl}(x)|}{|x|} \leq u$$
> Para precisión doble, $u = 2^{-52} \approx 2.22 \times 10^{-16}$.

La acumulación de estos errores es el objeto de estudio del [[Propagacion Errores Operaciones Matriciales|Análisis de Propagación de Errores]].

### Aritmética y Modos de Redondeo

El estándar exige que las operaciones básicas se comporten como si se calcularan exactamente y luego se redondearan. El comportamiento específico de este redondeo se estudia en detalle en la nota [[Modos de Redondeo IEEE 754]].

### Limitaciones del Rango: Underflow y Overflow

Cuando el exponente $E$ es demasiado grande o demasiado pequeño, el sistema sale del rango normalizado. Estos fenómenos se tratan en profundidad en las notas específicas:
- [[Underflow y Numeros Subnormales]]: Explica cómo el sistema maneja la transición suave hacia el cero.
- [[Overflow e Infinito]]: Explica la generación de $\pm\infty$ y su propagación en cálculos subsiguientes.

---

## Implicaciones prácticas

Conocer la estructura de bits permite entender por qué:
1. $0.1 + 0.2 \neq 0.3$ en precisión simple.
2. Existe un límite en la precisión al resolver sistemas lineales (Ver [[Sensibilidad Solucion Numero Condicion]]).
3. La [[Cancelacion Catastrofica|Cancelación Catastrófica]] ocurre al restar números cercanos, incluso si la representación es exacta.

> [!warning]
> **No-asociatividad.** En aritmética flotante, $(a + b) + c \neq a + (b + c)$. Esto tiene consecuencias directas en la suma de series y en la [[Eliminacion Gaussiana]].