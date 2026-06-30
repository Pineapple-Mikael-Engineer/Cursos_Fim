---
title: "Temperatura $T$"
order: 2
tags:
  - termodinamica
  - propiedades
  - variables_de_estado
  - temperatura
draft: false
aliases:
  - temperature
  - T
  - escala Kelvin
---

# Temperatura $T$

> [!definicion]
> La **temperatura** es la propiedad intensiva que caracteriza el equilibrio térmico: dos sistemas en contacto térmico alcanzan el equilibrio cuando sus temperaturas se igualan, y entonces cesa la transferencia de calor. El calor fluye espontáneamente del sistema de **mayor** $T$ al de **menor** $T$ — nunca en sentido contrario sin intervención externa. La escala termodinámica absoluta, medida en **kelvin** (K), asigna $T = 0$ al cero absoluto: el estado de mínima energía térmica posible, donde todos los modos de vibración molecular están en su estado fundamental y es imposible extraer más calor de un sistema como fuente.

---

## Ley Cero y medibilidad de la temperatura

> [!axioma]
> **Ley Cero de la termodinámica.** Si el sistema $A$ está en equilibrio térmico con el sistema $C$, y el sistema $B$ también está en equilibrio térmico con $C$, entonces $A$ y $B$ están en equilibrio térmico entre sí.
>
> *Por qué es necesaria.* La Ley Cero no se deriva de las demás leyes de la termodinámica — es un postulado independiente. Su importancia es conceptual: garantiza que la temperatura es una propiedad bien definida y **transitiva**, lo que hace posible la medición mediante termómetros. Sin la Ley Cero, no podría establecerse que un termómetro en equilibrio con un sistema indica la temperatura de ese sistema.

> [!teoria] El termómetro como consecuencia de la Ley Cero
> El termómetro (sistema $C$) se pone en contacto con el sistema a medir ($A$) hasta alcanzar equilibrio. La Ley Cero garantiza que cuando el termómetro también esté en equilibrio con el patrón de calibración ($B$), los tres tendrán la misma temperatura. La propiedad del termómetro que varía con $T$ — la dilatación del mercurio, la resistencia eléctrica del platino, la presión de un gas — se usa como indicador. Cualquier propiedad que varíe de forma monótona con $T$ y sea reproducible sirve como termómetro; la Ley Cero garantiza la coherencia de las lecturas.

---

## Escala termodinámica absoluta de Kelvin

> [!demostracion]
> **Meta:** construir una escala de temperatura que sea independiente de la sustancia termométrica, usando solo la segunda ley.
>
> **Hipótesis:** existe un motor de Carnot (ciclo reversible) operando entre un foco caliente a temperatura $T_H$ y un foco frío a temperatura $T_C$, absorbiendo calor $Q_H$ y cediendo $Q_C$.
>
> **Paso 1 — Resultado de Carnot: la eficiencia solo depende de las temperaturas.**
> Carnot demostró que la eficiencia $\eta = 1 - Q_C/Q_H$ de un motor reversible no depende de la sustancia de trabajo — solo de $T_H$ y $T_C$. Por tanto, el cociente $Q_C/Q_H$ es una función universal:
> $$\frac{Q_C}{Q_H} = f(T_H, T_C).$$
> La prueba usa la segunda ley por contradicción: si existieran dos motores reversibles entre los mismos focos con distinta eficiencia, el motor menos eficiente podría operar como bomba de calor y la combinación produciría una transferencia neta de calor del foco frío al caliente sin trabajo externo, violando el enunciado de Clausius.
>
> **Paso 2 — Restricción funcional por cadena de motores.**
> Se conectan tres motores reversibles en cascada entre focos a $T_A > T_B > T_C$:
> $$\frac{Q_C}{Q_A} = \frac{Q_C}{Q_B} \cdot \frac{Q_B}{Q_A} \implies f(T_A, T_C) = f(T_A, T_B)\cdot f(T_B, T_C).$$
> Esta ecuación funcional restringe la forma posible de $f$. La familia de soluciones es:
> $$f(T_H, T_C) = \frac{\varphi(T_C)}{\varphi(T_H)}$$
> para cualquier función positiva $\varphi$.
>
> **Paso 3 — Definición de la escala de Kelvin.**
> Kelvin eligió $\varphi(T) = T$ (la opción más simple y consistente), lo que define la **escala termodinámica**:
> $$\boxed{\frac{Q_C}{Q_H} = \frac{T_C}{T_H}} \qquad \text{(motor de Carnot reversible).}$$
> Esta elección no es arbitraria en el sentido de que cualquier otra función $\varphi$ produce una escala equivalente; la escala de Kelvin se distingue por la proporcionalidad lineal $Q \propto T$.
>
> **Paso 4 — Punto de referencia: el punto triple del agua.**
> La escala requiere fijar la unidad. La Conferencia Internacional de Pesos y Medidas (1954) estableció:
> $$T_{\text{triple, agua}} = 273.16\,\text{K} \quad \text{(exacto por definición).}$$
> Operativamente: $T = 273.16\,(Q/Q_{\text{triple}})$ donde $Q$ y $Q_{\text{triple}}$ son calores intercambiados por un motor de Carnot reversible con el foco de interés y con el foco a la temperatura del punto triple, respectivamente.
>
> **Paso 5 — Coincidencia con el termómetro de gas ideal.**
> Se puede demostrar que la escala termodinámica de Kelvin coincide con la del termómetro de gas ideal:
> $$T = \lim_{P \to 0} \frac{P v}{R},$$
> donde $R = 8.314\,\text{J/(mol·K)}$ es la constante universal de los gases. Ambas escalas son idénticas por construcción: el gas ideal fue el patrón de temperatura primario antes de 1954. $\blacksquare$

---

## Definición desde la relación fundamental

> [!proposicion]
> La termodinámica clásica (Callen) define la temperatura como la derivada de la energía interna respecto a la entropía a volumen constante:
> $$T \equiv \left(\frac{\partial U}{\partial S}\right)_V.$$
> Esta expresión surge de la relación fundamental $dU = T\,dS - P\,dV$: $T$ es el "precio" en energía por unidad de entropía generada a volumen constante. Cuando dos sistemas intercambian calor reversiblemente, la condición de equilibrio es que sus $(\partial U/\partial S)_V$ se igualen — es decir, que sus temperaturas sean iguales.

---

## Interpretación estadística

> [!teoria]
> A nivel microscópico, $T$ cuantifica la agitación térmica de las moléculas. Para un gas ideal monoatómico:
> $$\frac{3}{2}k_B T = \frac{1}{2}m\langle v^2 \rangle \quad \Longrightarrow \quad T = \frac{m\langle v^2\rangle}{3k_B},$$
> donde $k_B = 1.381 \times 10^{-23}\,\text{J/K}$ es la constante de Boltzmann y $\langle v^2\rangle$ es el cuadrado de la velocidad cuadrática media de las moléculas. A $T = 300\,\text{K}$, el nitrógeno ($M = 28\,\text{g/mol}$) tiene $v_{\rm rms} = \sqrt{3RT/M} = \sqrt{3 \times 8.314 \times 300/0.028} = 517\,\text{m/s}$.
>
> Esta interpretación explica por qué $T = 0\,\text{K}$ es el cero absoluto: a esa temperatura la energía cinética traslacional es cero (en la descripción clásica). En la mecánica cuántica, permanece la energía de punto cero de los osciladores, pero $T = 0\,\text{K}$ sigue siendo el estado de mínima energía térmica accesible.

---

## Escalas prácticas y conversiones

> [!proposicion]
> La **escala Celsius** usa el mismo tamaño de grado que Kelvin pero un origen distinto:
> $$T\,[\text{K}] = T\,[°\text{C}] + 273.15.$$
> Una **diferencia** de temperatura es idéntica en ambas escalas: $\Delta T\,[\text{K}] = \Delta T\,[°\text{C}]$.
>
> Puntos de referencia históricos:
> | Evento | $T\,[\text{K}]$ | $T\,[°\text{C}]$ |
> |:---|:---:|:---:|
> | Cero absoluto | $0$ | $-273.15$ |
> | Punto triple del agua | $273.16$ | $0.01$ |
> | Punto de fusión del agua (1 atm) | $273.15$ | $0$ |
> | Punto de ebullición del agua (1 atm) | $373.15$ | $100$ |

> [!warning]
> **Usar siempre kelvin en ecuaciones termodinámicas.** Cualquier relación que contiene $T$ de forma no diferencial — $\eta_{\rm Carnot} = 1 - T_C/T_H$, $Pv = RT$, $\delta Q_{\rm rev} = T\,dS$, $s = c_v \ln T + R\ln v + \text{cte}$ — exige **temperatura absoluta**. Sustituir grados Celsius produce errores del orden de $T[\text{K}]/273 \approx 10\text{–}100\%$ en los cálculos. El grado Celsius solo es aceptable en **diferencias** de temperatura.

---

## Papel en el estado termodinámico y conexión con otras propiedades

> [!info]
> - **Postulado de estado:** junto con [[Presion]] y [[Volumen Especifico]], fija el estado de una sustancia simple compresible; ver [[Variables de Estado/index | Variables de Estado]].
> - **Variables naturales:** $T$ es la variable conjugada de la entropía. Es variable natural de [[Helmholtz]] ($F$) y de [[Gibbs]] ($G$): $dF = -S\,dT - P\,dV$, $dG = -S\,dT + V\,dP$.
> - **Calores específicos:** $c_v = (\partial u/\partial T)_v$ y $c_p = (\partial h/\partial T)_P$ miden cómo cambia la energía almacenada con $T$.
> - **Transferencia de calor:** $\delta Q_{\rm rev} = T\,dS$ (ver [[TdS]]).
> - **Región bifásica:** en la mezcla líquido–vapor, $T = T_{sat}(P)$ está fijada por la presión; ver [[Calidad]].

> [!referencia]
> Borgnakke & Sonntag, *Fundamentals of Thermodynamics*, §2.2, §7.5; Çengel & Boles, *Termodinámica*, §1-8 a 1-10; Callen, *Thermodynamics*, §1-8, §4-4; Fermi, *Thermodynamics*, cap. IV.
