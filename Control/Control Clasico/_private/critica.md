---
title: Crítica del vault de Control Clásico
tags:
  - control-clasico
  - meta
  - revision
draft: true
aliases:
  - critica
  - revision notas
  - feedback vault
---

# Crítica del vault de Control Clásico

> [!info] Alcance de esta revisión
> Revisión de las 45 notas de contenido de `Control Clasico/` (capítulos 2 Modelado, 3 Análisis y 4 Diseño) contra las convenciones de [[Reglas]] y el plan de [[Tree]]. Fecha: 2026-05-29.
>
> El balance es **muy positivo**: hay una base de conocimiento densa, matemáticamente correcta en su gran mayoría, con derivaciones reales y excelente coherencia de notación. Lo que sigue son ajustes para llevarla del 90 % al 100 %, ordenados por impacto.

---

# Lo que está muy bien (mantener)

> [!teoria] Fortalezas reales
> 1. **Notación consistente** en todo el vault: $G(s)$, $H(s)$, $\zeta$, $\omega_n$, $\omega_d$, $K_p/K_v/K_a$, $e_{ss}$, $s=\sigma+j\omega$. Se cumple [[Reglas]] al pie.
> 2. **Derivaciones genuinas, no recetario**: $M_p$, $T_p$, $T_s$, fórmulas de error, transformación EE↔FT, Routh por transformación bilineal + Schur-Cohn. Cada resultado clásico tiene su deducción.
> 3. **Hipótesis explícitas**: casi todas las fórmulas indican "CI nulas", "realimentación unitaria", "$0<\zeta<1$", "sistema estable". Es exactamente lo que pide [[Reglas]].
> 4. **Delegación correcta**: las notas índice resumen y delegan a hijas sin duplicar las demostraciones (p. ej. [[Funcion Transferencia/index]] → [[Polos Ceros]], [[Teorema Valor Inicial Final]]).
> 5. **Coherencia cruzada de tablas**: las analogías fuerza–voltaje de [[Electrico]] y [[Mecanico Traslacional]] coinciden; las tablas de error estacionario de [[Coeficientes Kp Kv Ka]], [[Tabla Tipos]], [[Escalon]], [[Rampa]] y [[Parabola]] son idénticas. Excelente.
> 6. **Honestidad sobre aproximaciones**: [[Tiempo Subida Tr]] tabula los errores de las fórmulas empíricas (hasta 49 %) en lugar de venderlas como exactas. Es el nivel Ogata/Franklin que busca [[Reglas]].

---

# 1. Errores de contenido (prioridad alta)

> [!warning] 1.1 — Signo de la realimentación en [[Algebra Diagramas]] (crítico)
> Es la única inconsistencia **matemática** de fondo del vault y conviene corregirla primero porque contradice al resto.
>
> En `Algebra Diagramas.md` la definición de realimentación y su demostración usan **realimentación positiva** ($E = U + HY$) y entregan:
> $$G_{eq}=\frac{G}{1-GH}, \qquad \text{(unitaria) } \frac{G}{1-G}$$
>
> Pero el resto del vault usa correctamente la convención **negativa**:
> - [[Funcion Transferencia/index]]: "Realimentación unitaria negativa $\frac{G}{1+G}$", "general $\frac{G}{1+GH}$".
> - [[Error Estacionario/index]], [[Lugar Raices/index]], [[Ajuste Parametros]]: todos con $1+GH$.
>
> **Problema:** la nota nombra "Realimentación" (la operación por defecto en control) al resultado de la **positiva**, y la fórmula estándar negativa $\frac{G}{1+GH}$ **no aparece**. Un lector que llegue por delegación verá $1-GH$ y chocará con el $1+GH$ de las demás notas.
>
> **Sugerencia:** poner la realimentación **negativa** ($E=R-HY \Rightarrow T=\frac{G}{1+GH}$) como caso principal y dejar la positiva como variante explícita. Así se alinea con `Retroalimentacion_unitario.svg` y con [[Error Estacionario/index]].

> [!warning] 1.2 — "Tipo de sistema" vs grado relativo en [[Trayectoria eje real y Asintotas]]
> La sección *"Relación con el tipo de sistema"* dice:
> > Tipo 0 ($n=m$) … Tipo 1 ($n-m=1$) … Tipo 2 ($n-m=2$) …
>
> Esto confunde dos conceptos distintos:
> - **Tipo** = número de integradores (polos en $s=0$). Así se define en [[Tabla Tipos]].
> - **Grado relativo** $n-m$ = lo que fija el número y los ángulos de las asíntotas.
>
> El número de asíntotas depende de $n-m$, **no** del tipo. Un sistema tipo 1 puede tener cualquier $n-m$. Recomiendo renombrar la sección a *"Asíntotas según el grado relativo $n-m$"* y quitar la palabra "Tipo".

> [!warning] 1.3 — Convención de signos del ángulo de salida (inconsistencia entre notas)
> Dos notas dan la fórmula del ángulo de salida con convenciones distintas:
> - [[Reglas Construccion]] (Regla 6): $\theta_{salida}=180^\circ-\sum_{i\neq j}\angle(p_j+p_i)+\sum_k\angle(p_j+z_k)$ — usa $(p_j+p_i)$.
> - [[Trayectoria eje real y Asintotas]]: usa $\angle(p_0-z_i)$ y $\angle(p_0-p_j)$ — usa diferencias.
>
> Ambas pueden ser coherentes según se definan los polos como $-p_j$ o como ubicación, pero **mezclar las dos formas entre notas hermanas** invita al error de signo. Unificar a una sola convención (sugiero diferencias $\angle(p_0-p_j)$, que es la habitual en Ogata/Nise).

---

# 2. Wikilinks rotos o que apuntan a notas inexistentes (prioridad alta)

> [!warning] 2.1 — Enlaces a notas que aún no existen
> Estos destinos no tienen archivo `.md`. [[Reglas]] permite el wikilink como "promesa futura", así que **no es un error fatal**, pero conviene saber qué hueco crea cada uno (todos están en el plan de [[Tree]], pendientes de redactar):
>
> | Enlace | Aparece en | Estado en Tree |
> |--------|-----------|----------------|
> | `[[Controladores/PID]]`, `[[PID]]` | Electronica, Ganancia Estatica, Tabla Tipos, FT/index | Cap. 5 sin crear |
> | `[[Lead]]`, `[[Lag]]`, `[[Diseno/Lead]]`, `[[Diseno/Lag]]` | Ganancia Estatica, Estabilidad/index, LGR/index, Tabla Tipos | Cap. 4 sin crear |
> | `[[Nyquist]]`, `[[Respuesta Frecuencia]]` | Estabilidad/index, FT/index | Cap. 3/4 sin crear |
> | `[[Cruce Eje Imaginario]]` (×3) | LGR/index, Reglas Construccion | Cap. 4 sin crear |
> | `[[Angulos Salida Llegada]]` (×4) | LGR/index, Reglas Construccion, Trayectoria | Cap. 4 sin crear |
> | `[[Controlabilidad]]`, `[[Observabilidad]]` | Pasar a FT | sin crear |
> | `[[Forma Canónica Controlable]]`, `[[Forma Canónica Observable]]`, `[[Forma Diagonal]]`, `[[Forma de Jordan]]` | Espacio Estados/index | sin crear |
> | `[[Formula Mason]]` (×2) | Algebra Diagramas | sin crear |
> | `[[Reduccion Sistematica]]` | Algebra Diagramas | sin crear |
>
> **Recomendación:** o crear stubs con YAML `draft:true`, o marcar estos enlaces de forma uniforme para no perder de vista cuáles son promesas. Hoy se mezclan promesas reales con lo ya escrito sin distinción visual.

> [!warning] 2.2 — Enlaces a carpeta en lugar de a `index` (probablemente rotos)
> [[Reglas]] exige la forma `[[directorio/index | texto]]`. Estos apuntan al **nombre de carpeta**, que no resuelve a ningún `.md`:
>
> | Enlace usado | Debería ser |
> |--------------|-------------|
> | `[[Espacio Estados]]` (×5) | `[[Espacio Estados/index]]` |
> | `[[Lugar Raices]]` | `[[Lugar Raices/index]]` |
> | `[[Linealizacion]]` | `[[Linealizacion/index]]` |
> | `[[Error Estacionario]]` (en FT/index) | `[[Error Estacionario/index]]` |
> | `[[Respuesta Temporal/Segundo Orden]]` (×2) | `[[Respuesta Temporal/Segundo Orden/index]]` |
>
> Aparecen sobre todo en [[Funcion Transferencia/index]], [[Orden]] y [[Espacio Estados/index]]. Es el tipo de rotura más silencioso porque Obsidian no siempre avisa.

> [!warning] 2.3 — Anclas de encabezado que no coinciden (rotas)
> En [[Routh Hurwitz/index]] la tabla de casos especiales enlaza a encabezados que **no existen con ese texto**:
>
> | Ancla usada | Encabezado real en [[Casos Especiales]] |
> |-------------|------------------------------------------|
> | `#Caso 1: Primer elemento cero` | `# Caso 1: Primer elemento de una fila es cero` |
> | `#Caso 2: Fila de ceros` | `# Caso 2: Fila completa de ceros` |
>
> El `#ancla` debe ser **idéntico** al texto del encabezado. Hay que igualar uno de los dos lados.

---

# 3. Embeds de imagen faltantes (prioridad media-alta)

> [!warning] 3.1 — 20 SVG referenciados que no están en `_media`
> Capítulos enteros embeben figuras que no existen aún. El embed se ve roto en lectura.
>
> **`Dominios Fisicos` (excepto traslacional) — todo el material gráfico falta:**
> - [[Electrico]]: `rc_serie.svg`, `rl_serie.svg`, `rlc_serie.svg`
> - [[Electronica]]: `opamp_ideal.svg`, `inversor.svg`, `no_inversor.svg`, `seguidor.svg`, `integrador.svg`, `derivador.svg`, `filtro_pasa_bajos.svg`, `filtro_pasa_altos.svg`, `sallen_key.svg`
> - [[Mecanico Rotacional]]: `eje_torques.svg`, `ejes_compartidos.svg`, `eje_flexible.svg`, `engranajes.svg`, `tren_engranajes.svg`
>
> **Respuesta temporal:**
> - [[Primer Orden]]: `primer_orden_escalon.svg`
> - [[Segundo Orden/index]]: `segundo_orden_escalon.svg`
> - [[Escalon]]: `identificacion_escalon.svg`
>
> Contraste: [[Mecanico Traslacional]] y todo el capítulo de [[Lugar Raices/index]] sí tienen sus figuras (`mra_*`, `lgr_*`, `root_locus*.gif`). El modelado físico se quedó a medias en lo gráfico mientras el texto está completo.
>
> **Recomendación:** priorizar `primer_orden_escalon.svg` y `segundo_orden_escalon.svg` (son las curvas más consultadas del vault) y el set de op-amps, que sin diagrama pierden mucho.

---

# 4. Desviaciones de las propias [[Reglas]] (prioridad media)

> [!info] 4.1 — Wikilinks sin texto visible
> [[Reglas]] dice: *"Siempre `[[archivo | Texto visible]]`"*. En la práctica la **mayoría** de los enlaces son desnudos: `[[Polos Ceros]]`, `[[Escalon]]`, `[[Rampa]]`, `[[Construccion Tabla]]`, etc. Funcionan en Obsidian, pero incumplen la regla autoimpuesta. Dos caminos:
> - relajar la regla (los enlaces desnudos son legibles cuando el nombre del archivo ya es el texto deseado), o
> - añadir alias donde el nombre de archivo no encaje con la frase (que es el caso real que la regla quería cubrir).

> [!info] 4.2 — Callouts fuera de la lista permitida
> [[Reglas]] fija una lista cerrada de callouts. Se usan algunos no incluidos:
> - `[!regla]` — en [[Polos Ceros]], [[Orden]]
> - `[!solucion]` — en [[Casos Especiales]]
> - `[!referencia]` — en [[Construccion Tabla]]
>
> Son callouts útiles y bien usados. Sugiero **ampliar la lista permitida en [[Reglas]]** en vez de eliminarlos.

> [!info] 4.3 — Jerarquía de encabezados inconsistente
> Conviven dos estilos:
> - **Plano** (todo `#`): la mayoría de "2 Modelado" y "3 Análisis" usan `#` tanto para el título como para cada sección → múltiples H1 por nota.
> - **Jerárquico** (`#` título + `##` secciones): el capítulo [[Lugar Raices/index]] lo hace bien.
>
> Unificar a "un `#` para el título, `##` para secciones" mejora el outline de Obsidian y la navegación. Es puramente mecánico.

> [!info] 4.4 — Secciones/estilo desaconsejados
> - "## Introducción" en [[Reglas Construccion]] y [[Casos Especiales]] (sección genérica que [[Reglas]] desaconseja).
> - "en palabras simples" en el resumen de [[Condicion Angulo Magnitud]] (expresión que [[Reglas]] pide evitar).
> Menores, pero son justo los casos que la guía nombra.

---

# 5. Detalles de redacción y formato (prioridad baja)

> [!info] 5.1 — Delimitadores y bloques mal cerrados
> - [[Tabla Pares]]: en el ejemplo de raíces repetidas, `$$\frac{1}{2} = A + 1 + \frac{1}{2} \implies A = -1$` **abre con `$$` y cierra con `$`** → no renderiza. Cerrar con `$$`.
> - [[Propiedades]]: en la demostración de la integración, la línea `Pero $\mathcal{L}\{g'(t)\}...` **no lleva `>`** y rompe el callout. Añadir el `>`.

> [!info] 5.2 — Texto en estado de borrador (notas a uno mismo)
> - [[Teorema Valor Inicial Final]]: en el ejemplo $F(s)=1/s^2$ quedó un razonamiento dubitativo con interrogante (*"…no es simple en $sF(s)$? En realidad es simple pero…"*). Lee como pensamiento en voz alta; conviene reescribirlo en seco.
> - [[Casos Especiales]] (Caso 1, conclusión): mismo patrón (*"$2 \to \varepsilon$? en realidad…"*). Limpiar la auto-pregunta y dejar el conteo de cambios de signo directo.

> [!info] 5.3 — `Algebra Diagramas`, tabla de movimiento de sumadores
> La fila *"Mover sumador antes de bloque"* tiene un `!` huérfano (`!$G$ →`), resto de un embed o tipeo. Además la columna "Equivalencia" es vaga ("sumador se multiplica por $1/G$"); con el SVG correspondiente o una fórmula explícita ganaría.

> [!info] 5.4 — Ejemplo no estándar en [[Ajuste Parametros]]
> Los ejemplos 1 y 2 ponen $K$ **sumando dentro del denominador** ($G(s)=\frac{1}{s(s+1)(s+2)+K}$). Es matemáticamente válido pero atípico: en control la ganancia casi siempre **multiplica** ($G=\frac{K}{s(s+1)(s+2)}$). Para una base de consulta, un ejemplo con $K$ multiplicando es más transferible al [[Lugar Raices/index]]. El ejemplo 3 (con $K$ en la realimentación) sí es del tipo habitual.

> [!info] 5.5 — Matiz en [[Primer Orden]] (respuesta a rampa)
> Se da $e_{ss}=K\tau$ para la rampa. Eso es el desfase salida–entrada **solo si $K=1$** (seguimiento). Con $K\neq 1$ el "error" $r(t)-y(t)$ diverge porque la pendiente no coincide. Conviene aclarar "para $K=1$" o llamarlo "retardo de seguimiento $\tau$".

---

# 6. Oportunidades de conexión (mejoras, no errores)

> [!info] Enlaces que enriquecerían la red
> - [[Convolucion]] y [[Impulso]] desarrollan ambos la respuesta impulsional $h(t)$ y su relación con el escalón; podrían enlazarse mutuamente de forma explícita (hoy solo Impulso→Convolucion).
> - [[Espacio Estados/index]] menciona controlabilidad/observabilidad con buen detalle inline, mientras [[Pasar a FT]] enlaza a `[[Controlabilidad]]`/`[[Observabilidad]]` inexistentes. Si no se crean esas notas, redirigir esos enlaces a la sección correspondiente de [[Espacio Estados/index]] (`[[Espacio Estados/index#Conceptos avanzados]]`).
> - [[Sensibilidad]] y [[Lazo Abierto Cerrado]] (cap. 1 del [[Tree]]) están totalmente ausentes; varias notas asumen el concepto de lazo cerrado/realimentación sin una nota raíz a la que apuntar. Es el hueco conceptual más grande del vault.

---

# 7. Checklist de acción sugerida (orden de impacto)

> [!info] De mayor a menor retorno
> 1. **Corregir el signo de realimentación** en [[Algebra Diagramas]] → coherencia con todo el vault. *(§1.1)*
> 2. **Arreglar enlaces a carpeta** (`[[Espacio Estados]]` → `/index`, etc.) y **anclas rotas** de Routh. *(§2.2, §2.3)*
> 3. **Renombrar** "tipo de sistema" → "grado relativo" en asíntotas. *(§1.2)*
> 4. **Unificar** convención de signos del ángulo de salida. *(§1.3)*
> 5. **Generar los SVG** de primer/segundo orden y op-amps (los más consultados). *(§3.1)*
> 6. **Cerrar delimitadores/callouts** mal formados y limpiar texto-borrador. *(§5.1, §5.2)*
> 7. **Decidir política de wikilinks** (con/sin alias) y **ampliar la lista de callouts** en [[Reglas]]. *(§4.1, §4.2)*
> 8. **Unificar jerarquía de encabezados** (`#`/`##`). *(§4.3)*
> 9. **Crear stubs** o marcar uniformemente las promesas (PID, Lead/Lag, Nyquist, etc.). *(§2.1)*

> [!teoria] Veredicto
> El vault ya es una base de consulta seria, rigurosa y navegable — exactamente lo que pide [[Reglas]]. El 80 % de esta lista son enlaces e imágenes pendientes propios de un vault en construcción; el contenido matemático está, salvo el signo de realimentación de [[Algebra Diagramas]] y el matiz tipo/grado-relativo, **correcto y bien deducido**. Arreglando los puntos de §1 a §3 queda sólido de punta a punta.
