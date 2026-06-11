---
title: Reglas
tags:
  - dinamica
  - meta
  - escritura
  - convenciones
draft: true
aliases:
  - Guía de redacción
  - Convenciones del curso Dinámica
  - Reglas de notas
---

# Reglas — Curso Dinámica

## Filosofía

Notas técnicas de **referencia para relectura**, no textbook ni apuntes corridos ni explicación
pedagógica de IA. Rigurosas, modulares, densas pero navegables, autocontenidas en su núcleo y
expansibles por wikilinks. Este curso es **teórico-deductivo** (mecánica clásica tipo física): se
privilegia **deducir desde primeros principios** sobre el recetario. Lo más consultado va arriba.

> Lo que se consulta cien veces va antes que lo que se lee una sola vez.

---

## YAML obligatorio

```yaml
---
title: <nombre legible>
tags:
  - dinamica
  - teoria
  - <tema-especifico>
draft: false
aliases:
  - <sinónimos / nombre en inglés si aplica>
---
```

---

## Anatomía de una nota sustantiva

Separar bloques con `---`. Orden típico:

1. `# Título $notación$` (p. ej. `# Ecuaciones de Euler $\vec\tau=\mathbf{I}\vec\alpha+\vec\omega\times(\mathbf{I}\vec\omega)$`)
2. `> [!definicion]` — primera línea del cuerpo, define el concepto con su ecuación central.
3. `> [!info]` — ubicación (sección, wikilinks a vecinas), referencia al libro.
4. `## Ejemplo` — `> [!ejemplo]` con un problema **resuelto** (DCL, números, pasos) y `> [!solucion]` anidada.
5. `## En qué consiste` / desarrollo — `> [!teoria]`, `> [!teorema]` + `> [!demostracion]` (con
   **Paso 1 — …** y cierre `$\blacksquare$`), `> [!proposicion]`, `> [!warning]`.
6. `## Resumen` — `> [!resumen]` (tabla) + `> [!corolario]` + `> [!referencia]`.

Para `index.md`: definición marco + idea unificadora + **teoría propia** (no solo listar hijas) +
mapa de hijas delegando la profundidad + corolario. Un índice **enseña**; puede llevar figuras y
ecuaciones.

---

## Callouts permitidos

Usar EXACTAMENTE (en español, minúscula):

```
definicion · teorema · demostracion · lema · proposicion · corolario · axioma
ejemplo · solucion · teoria · info · warning · algoritmo · regla · referencia · resumen
```

Prohibidos: `nota`, `observacion`, `conclusion`, `importante` y cualquier callout en inglés.
Regla: si quitar el callout no cambia nada, estaba mal usado. Dado el carácter deductivo del curso,
**usar `demostracion`** generosamente para las derivaciones desde primeros principios.

---

## Notación (mantener UNA convención, sin mezclar)

| Concepto | Notación |
|:---|:---|
| Vectores | flecha: $\vec{r}$, $\vec{v}$, $\vec{a}$, $\vec{F}$, $\vec{\omega}$, $\vec{\alpha}$, $\vec{\tau}$ |
| Posición relativa | $\vec{r}_{P/O}$ (de $O$ a $P$) |
| Centro de masa | $G$ (o $C$); su velocidad $\vec{v}_G$, aceleración $\vec{a}_G$ |
| Derivada temporal | $\dot{\vec{r}}=d\vec{r}/dt$, $\ddot{\vec{r}}$ |
| Tensor de inercia | $\mathbf{I}$ (negrita); identidad $\mathbb{1}$ |
| Momento angular | $\vec{H}_O$ (respecto a $O$); $\vec{H}_G=\mathbf{I}_G\vec{\omega}$ |
| Energía cinética | $T$; potencial $V$ |
| Notación indicial | $\delta_{ij}$ (Kronecker), $\epsilon_{ijk}$ (Levi-Civita), convenio de suma |
| Segundo momento | $Q_{ij}=\int r_i r_j\,dm$ |

**Convenio del tensor de inercia (FIJO, no mezclar):** se usan las **componentes del tensor**
$$\mathbf{I}=\mathrm{Tr}(Q)\,\mathbb{1}-Q,\qquad I_{ij}=\int(r^2\delta_{ij}-r_i r_j)\,dm,$$
de modo que los términos cruzados **ya incluyen el signo**: $I_{xy}=-\int xy\,dm$. La matriz se
escribe **directa con $I_{ij}$, sin signos extra**. Cuando un texto use el *producto de inercia*
$P_{ij}=\int r_i r_j\,dm$ (notación de ingeniería), recordar $I_{ij}=-P_{ij}$ y que entonces la
matriz lleva $-P_{ij}$ fuera de la diagonal. La nota [[Convenciones de Signo]] documenta esto; el
**resto de notas usa solo la convención de componentes**.

Unidades SI con espacio fino: `5\ \text{kg}`, `9{,}81\ \text{m/s}^2`. Decimales con coma.

---

## Figuras

Dos estilos (como en el resto de la vault), generadas en `Dinamica/_media/code_gen/` →
`Dinamica/_media/img_gen/*.svg`, embebidas con `![[nombre.svg|ancho]]`:

- **Diagramas** (DCL, sistemas de coordenadas, mecanismos, giróscopo, esquemas): **TikZ** en
  blanco y negro.
- **Gráficas** (respuesta de vibraciones, plano de fase, curvas $x(t)$): **matplotlib** con la
  paleta **Ocean Forest** (`ocean_forest.py`).

Regla de oro: renderizar SVG→PNG y **revisar la figura** antes de darla por buena. Dejar
*placeholder* `![[...]]` mientras no exista, y generar al final de cada parte.

---

## Wikilinks

`[[Archivo | texto visible]]`; índices `[[Carpeta/index | texto]]`. Basename exacto del árbol para
hojas únicas. Nunca `[[index]]` solo, ni `../`, ni saltos de línea dentro de `[[ ]]`. En tablas,
escapar `|`→`\|` dentro de `$...$`. No saturar: un wikilink por concepto que merezca nota propia.
**No duplicar**: si algo tiene nota propia, delegar por wikilink (lección del tensor de inercia, que
las notas viejas repetían 4 veces).

---

## Estilo de redacción

Deductivo y económico. Preferir "se deduce de…", "se obtiene…", "integrando sobre el cuerpo…",
"proyectando en…". Evitar "recordemos", "veamos", "intuitivamente", "en palabras simples". Siempre
declarar: **marco de referencia** (inercial o no), **punto** respecto al cual se toman momentos ($G$,
$O$ fijo, punto arbitrario), y las **hipótesis** (cuerpo rígido, sin deslizamiento, fuerza
conservativa…). No fórmulas sin hipótesis.

## Referencia de estilo

Imitar la mecánica teórica vectorial: **Taylor** (*Classical Mechanics*), **Goldstein** (cap. 4-5,
cuerpo rígido), **Marion & Thornton**, **Symon**. Buscar economía verbal, precisión y la deducción
desde $d\vec{F}=\vec{a}\,dm$ / $d\vec{\tau}=\vec{r}\times\vec{a}\,dm$ que caracteriza las propias
"Integrales Útiles" del usuario.
