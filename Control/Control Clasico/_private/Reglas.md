---
title: Reglas
tags:
  - control-clasico
  - meta
  - escritura
  - convenciones
draft: true
aliases:
  - Guía de redacción
  - Convenciones del vault
  - Reglas de notas
---

# Reglas

# Filosofía de estas notas

Estas notas NO siguen estructura de textbook.

No son capítulos.

No son apuntes corridos.

No son explicaciones pedagógicas.

Son base de conocimiento para relectura frecuente:

- rigurosas  
- modulares  
- densas pero navegables  
- matemáticamente precisas  
- orientadas a análisis y diseño  
- autocontenidas en su núcleo  
- expansibles mediante wikilinks

Escribir como notas técnicas serias de consulta.

No escribir como IA pedagógica.

No escribir como manual narrativo.

---

# Principio rector

> Lo que se consulta cien veces va antes que lo que se lee una sola vez.

Ordenar por frecuencia de consulta.

No por convención de libro.

---

# YAML obligatorio

Toda nota debe comenzar con:

```yaml
---
title: <nombre legible>
tags:
  - control-clasico
  - teoria
  - <tema-especifico>
draft: false
aliases:
  - <sinonimos si aplica>
---
```

## Reglas del YAML

- `title` puede diferir del nombre del archivo.
- `draft` usar `true` solo para borradores.
- Toda nota debe tener al menos:
  - `control-clasico`
  - `teoria`
  - un tag específico

No omitir YAML.

---

# Título principal

Formato:

```markdown
# Nombre del concepto $notación si aplica$
```

Ejemplos:

```markdown
# Error estacionario $e_{ss}$

# Criterio de Routh-Hurwitz

# Compensador lead $G_c(s)$
```

---

# Orden interno por capas

## Capa 1 — Consulta frecuente (arriba)

Priorizar:

- definiciones estructurales
- ecuaciones fundamentales
- fórmulas operativas
- criterios de diseño
- teoremas centrales
- ejemplos operativos tempranos

Jerarquía:

```text
Fórmulas útiles
> criterios de diseño
> ejemplos
> teoremas
```

---

## Capa 2 — Profundización

- derivaciones
- demostraciones
- deducciones
- interpretación geométrica
- hipótesis
- límites
- warnings

---

## Capa 3 — Complementario

- algoritmos
- MATLAB si aporta
- implementación
- extensiones
- contexto histórico

Regla resumen:

```text
Cheat sheet arriba
Teoría en medio
Apéndice abajo
```

---

# Estructura típica de notas sustantivas

Orden típico:

1 Definición formal

2 Relaciones estructurales fundamentales

3 Fórmulas principales

4 Ejemplo operativo temprano

5 Desarrollo matemático

6 Propiedades / teoremas

7 Casos particulares

8 Relación con otras notas

9 Complementos (si aplica)

---

# Estructura para index.md

Orden:

1 Definición marco

2 Idea unificadora

3 Ejemplo breve

4 Submétodos delegados a hijas

5 Propiedades globales

6 Motivación al final si aporta

---

# Callouts permitidos

Usar EXACTAMENTE:

```text
[!definicion]
[!teorema]
[!demostracion]
[!lema]
[!proposicion]
[!corolario]
[!axioma]
[!ejemplo]
[!teoria]
[!info]
[!warning]
[!regla]
[!solucion]
[!referencia]
```

> [!warning] Soporte de tema
> `[!regla]`, `[!solucion]` y `[!referencia]` requieren definir su estilo en el CSS del tema (Ocean Forest) para renderizar con color/ícono propio. Mientras no se definan, Obsidian los muestra con el estilo de callout por defecto.

No usar:

```text
[!nota]
[!conclusion]
[!observacion]
[!importante]
```

Regla:

Si quitar el callout no cambia nada,

estaba mal usado.

---

# Wikilinks

## Formato obligatorio

Siempre:

```text
[[archivo | Texto visible]]
```

Ejemplo:

```text
[[Polos_Ceros | polos y ceros]]
```

---

## Para índices

Usar:

```text
[[directorio/index | texto visible]]
```

Ejemplo:

```text
[[Lugar_Raices/index | lugar de raíces]]
```

---

## Nombres de archivo

Deben coincidir EXACTAMENTE con el árbol.

No inventar variantes.

Si la nota no existe aún:

se puede wikilinkear como promesa futura.

---

## Dónde sí pueden aparecer

- texto normal
- listas
- callouts
- tablas con criterio

---

## Dónde NO pueden aparecer

No en:

- headers
- ecuaciones
- bloques de código

---

## Frecuencia

No saturar.

Un wikilink por concepto que merezca nota propia.

No repetir el mismo cerca.

---

# Principio de delegación

Si un concepto tiene nota propia:

NO desarrollarlo completo aquí.

Solo mencionarlo y delegarlo.

Regla:

No duplicar conocimiento.

La nota debe ser útil por sí misma,

pero no repetir contenido del vault.

---

# Secciones genéricas prohibidas

No usar:

- Introducción
- Panorama general
- Objetivos
- Motivación (salvo al final si realmente aporta)

Solo secciones con valor de revisita.

---

# Para control clásico priorizar

Siempre priorizar:

- función de transferencia
- ecuación característica
- polos y ceros
- estabilidad
- especificaciones
- plano-$s$
- relaciones diseño–respuesta

Siempre indicar:

- sistema asumido
- lazo abierto o cerrado
- realimentación unitaria o no
- hipótesis usadas
- aproximación o exactitud
- dominio temporal o frecuencial

No fórmulas sin hipótesis.

---

# Para notas de diseño

Incluir:

- objetivo del compensador
- restricciones
- trade-offs
- efecto sobre polos
- efecto sobre error estacionario
- efecto sobre márgenes
- cuándo usarlo
- cuándo no

Diseño no es recetario.

---

# Para notas de análisis

Priorizar estructura sobre memorización.

Si aparece un resultado clásico:

dar:

- derivación si importa
- interpretación geométrica si existe
- relación con desempeño

No fórmulas aisladas.

---

# Notación

Mantener consistencia.

Usar:

- $G(s)$
- $H(s)$
- $L(s)=G(s)H(s)$
- $T(s)$
- $e_{ss}$
- $\zeta$
- $\omega_n$
- $\omega_d$
- $K$
- $s=\sigma+j\omega$

No mezclar convenciones.

---

# Ejemplos

Preferir:

- masa-resorte-amortiguador
- RLC
- servomecanismo
- compensación lead/lag
- root locus
- Bode

No ejemplos algebraicos vacíos.

---

# MATLAB y código

No asumir que toda nota requiere código.

Solo incluir si aporta.

Ejemplos válidos:

- root locus
- bode
- nyquist
- simulación
- Control Toolbox
- Simulink

Si no aporta:

omitir.

---

# Estilo de redacción

Preferir:

- se deduce de...
- se obtiene...
- satisface la relación...
- bajo realimentación unitaria...
- el sistema queda caracterizado por...

Evitar:

- recordemos
- veamos
- notemos
- intuitivamente
- en palabras simples

Sonar como nota técnica.

---

# Referencia de estilo

Imitar:

- Ogata
- Nise
- Dorf & Bishop
- Franklin Powell Emami

Buscar:

- economía verbal
- precisión matemática
- modularidad
- alta densidad conceptual

---

# Test rápido para aceptar una nota

Debe pasar:

- ¿Tiene YAML correcto?
- ¿Usa wikilinks correctos?
- ¿Lo más consultado está arriba?
- ¿Las fórmulas clave aparecen temprano?
- ¿Se delegó contenido duplicable?
- ¿La notación es consistente?
- ¿Los callouts aportan?
- ¿Funciona como referencia reusable?

Si falla alguna:

revisar.