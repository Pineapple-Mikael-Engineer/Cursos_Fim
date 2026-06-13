---
title: Reglas de redacción — Métodos Numéricos
draft: true
---

# Reglas de redacción — Métodos Numéricos

> Especialización de las reglas canónicas de la vault para el curso de Métodos Numéricos (MB536).
> Destilada de las notas ya existentes en el directorio. Sirve de verificación de estilo antes de
> redactar nuevas notas.

---

## Rol y filosofía

Notas de **referencia para relectura frecuente**, no textbook ni explicación pedagógica: rigurosas,
modulares, densas pero navegables, autocontenidas en su núcleo, expansibles por wikilinks.

Orden por **valor de relectura**: *lo que se consulta cien veces va antes que lo que se lee una vez*.
Fórmulas operativas y ejemplo temprano arriba; demostraciones en medio; algoritmo/código/contexto al
final. Prohibido `Introducción`, `Objetivos`, `Panorama`, `Estructura del directorio`.

---

## YAML obligatorio

```yaml
---
title: <nombre legible>
tags:
  - metodos-numericos
  - teoria
  - <tema-de-capitulo>      # error-numerico, algebra-lineal-numerica, ecuaciones-no-lineales, ...
  - <subtema>               # newton-raphson, convergencia, metodos-iterativos, ...
draft: false
aliases:
  - <sinónimo en español>
  - <nombre en inglés>      # Bisection method, Power method, ...
---
```

- `title` puede diferir del nombre del archivo.
- Siempre `metodos-numericos` + `teoria` + al menos un tema específico.
- Los `index.md` añaden el tag `index`.

---

## Título principal

`# <Nombre del concepto> $<notación si aplica>$`

Un **solo `#`** por nota. Ejemplos reales: `# Método de Bisección`,
`# Condicionamiento Numérico y Número de Condición $\kappa(A)$`,
`# Orden de Convergencia Cuadrática en Raíces Simples`. Secciones internas con `##`; separadas por
`---`.

---

## Notación específica del curso

| Símbolo | Significado |
|:---|:---|
| `x^{(k)}` | sucesión **escalar** (ecuaciones no lineales 1 variable) |
| `y^{(k)}` | sucesión **vectorial** (sistemas, métodos iterativos, autovectores) |
| `x = A^{-1}b` | solución exacta de un sistema lineal |
| `r` | raíz exacta de $f(x)=0$ |
| `e^{(k)}`, `ε^{(k)}` | error de la iteración $k$ ($x^{(k)}-r$ o $y^{(k)}-x$) |
| `T` | matriz de iteración (no `M`) |
| `A = D - E - F` | partición de $A$ (reservar `L, U` para factorización LU) |
| `ρ(T)` | radio espectral; `κ(A)` número de condición; `λ_i`, `σ_i` autovalores/valores singulares |
| `p` | orden de convergencia ($p=1$ lineal, $p\approx1.618$ superlineal, $p=2$ cuadrático) |

Código: **Python** para ejemplos numéricos, **MATLAB** para álgebra lineal. Referencias de estilo:
Burden & Faires, Quarteroni.

---

## Anatomía de una nota hoja (sustantiva)

Patrón observado, de arriba abajo, con `---` entre bloques:

1. `> [!definicion]` — definición formal, primera línea de la nota.
2. `> [!info]` — aclaración / ubicación dentro del panorama, con wikilink al método hermano.
3. `## Ejemplo` — `> [!ejemplo]` con **tabla de 3-5 iteraciones** y problema concreto (recurrente: $f(x)=x^2-2$, raíz $\sqrt 2$; o $A=\begin{psmallmatrix}2&1\\1&2\end{psmallmatrix}$).
4. `## En qué consiste el método` — `> [!teoria]` con algoritmo descrito e interpretación geométrica.
5. `## Teorema ...` + `## Demostración` — `[!teorema]` seguido de `[!demostracion]` estructurada en **Paso 1 / Paso 2 / …**.
6. Secciones de propiedades, comparativas y casos: tablas (`[!info]`, `[!proposicion]`, `[!corolario]`).
7. `## Algoritmo` — `> [!algoritmo]` con pseudocódigo en español y luego bloque ```python (o MATLAB).
8. `## Limitaciones` — `> [!warning]` con lista numerada.
9. `## Resumen` — **tabla** de aspectos clave (`| Aspecto | Descripción |`) y/o `> [!corolario]` final que cierra delegando a notas vecinas con wikilinks.

No todas las notas usan todas las secciones; las teóricas (teoremas, convergencia) pesan más en
demostración y comparativa, las de método pesan más en ejemplo + algoritmo.

## Anatomía de un `index.md`

1. `[!definicion]` marco del capítulo.
2. `[!info]` por cada sub-método, delegando a la hija con `[[Sub/index]]` o `[[Hija]]`.
3. `## Ejemplo` comparativo (tabla con varios métodos sobre el mismo problema).
4. `## Motivación` (al final) con `[!teoria]`.
5. `## Resumen` con tabla `| Categoría | Subdirectorio |` y `[!corolario]` de cierre.

---

## Callouts permitidos

Núcleo: `definicion`, `teorema`, `demostracion`, `lema`, `proposicion`, `corolario`, `axioma`,
`ejemplo`, `teoria`, `info`, `warning`, `algoritmo`.
Extensiones con mesura: `regla`, `solucion`, `referencia`.
**Nunca** `nota`, `conclusion`, `observacion`, `importante`. Regla: si quitar el callout no cambia
nada, estaba mal puesto.

---

## Wikilinks y delegación

- Formato `[[archivo | Texto]]`; enlace desnudo `[[Jacobi]]` válido cuando el nombre ya es el texto.
- Carpetas **siempre** con `/index`: `[[Variantes Metodo Potencia/index | …]]`.
- Nombres coinciden EXACTAMENTE con el árbol. Se enlaza aunque la nota no exista todavía (promesa de
  expansión) — práctica frecuente en las notas actuales (`[[Normas Matriciales Inducidas]]`, etc.).
- **Nunca** wikilinks dentro de `$…$`, `$$…$$`, headers ni bloques de código.
- Si un concepto tiene nota propia: **no** desarrollarlo, solo mencionarlo y enlazar.

---

## Estilo de redacción

Económico, denso, preciso. Preferir *se deduce de…*, *se obtiene…*, *bajo la hipótesis de…*,
*satisface la relación…*. Evitar *recordemos*, *veamos*, *intuitivamente*. Ninguna fórmula sin
hipótesis (qué matriz, qué condiciones, qué teorema). Sin texto-borrador ni auto-preguntas. Verificar
que `$$` cierre con `$$` y que toda línea dentro de un callout empiece con `>`.

---

## Alcance de esta tanda (notas a crear, en orden del árbol)

**Cap. 1 — Teoría de Errores**
1. `Estabilidad Algoritmos Forward Backward.md`
2. `Propagacion Errores Operaciones Matriciales.md`

**Cap. 2 — Sistemas Lineales**
3. `Metodos Directos/Analisis Error Directos/Residuo vs Error Relativo Solucion.md`
4. `Metodos Directos/Analisis Error Directos/Sensibilidad Solucion Numero Condicion.md`
5. `Metodos Iterativos/Convergencia Iterativos/Estimacion Error y Cotas A Priori.md`
6. `Valores Vectores Propios/Metodo Potencia Directo/Fundamentos Valor Propio Dominante.md`
7. `Valores Vectores Propios/Metodo Potencia Directo/(opcional) Caso Simetrico Convergencia Acelerada.md`
8. `Valores Vectores Propios/Metodo QR/Fundamentos Transformaciones Householder.md`
9. `Valores Vectores Propios/Metodo QR/Iteracion QR Descomposicion.md`
10. `Valores Vectores Propios/Metodo QR/Convergencia y Desplazamientos.md`

**Cap. 3 — Ecuaciones No Lineales**
11. `Metodos Abiertos Una Variable/Newton Raphson/Metodo Secante Orden Convergencia Fi.md`
12. `Metodos Abiertos Una Variable/Comparacion Analitica Orden Convergencia.md`
13. `Sistemas Ecuaciones No Lineales/Newton Raphson Multivariable/Matriz Jacobiana y Sistema Lineal Asociado.md`
14. `Sistemas Ecuaciones No Lineales/Newton Raphson Multivariable/Convergencia Local Cuadratica.md`
15. `Sistemas Ecuaciones No Lineales/Newton Raphson Multivariable/Costo Computacional Evaluacion Jacobiano.md`
16. `Sistemas Ecuaciones No Lineales/Condicion Contraccion Norma Matricial.md`

> Decisión pendiente de confirmar: si conviene añadir `index.md` a las carpetas nuevas
> (`Analisis Error Directos/`, `Metodo QR/`, `Sistemas Ecuaciones No Lineales/`,
> `Newton Raphson Multivariable/`) para mantener la convención de carpetas con índice.
