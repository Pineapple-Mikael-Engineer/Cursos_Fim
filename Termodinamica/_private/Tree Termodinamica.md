---
title: Tree Termodinamica
draft: true
---

# Tree

```tree
Termodinamica/
│
│   Leyenda:  NEW = archivo nuevo · REWRITE = reescritura completa
│             FIX = contenido OK, corregir callouts/estructura + order
│             +order = solo agregar campo order al frontmatter
│
├── Propiedades/
│   │
│   ├── Variables de Estado/
│   │   ├── index.md                                  # NEW · order:1 — qué es una variable de estado y el postulado de estado
│   │   ├── Presion.md                                # FIX · order:2 — contenido OK, consolidar callouts
│   │   ├── Temperatura.md                            # REWRITE · order:3 — escala absoluta y significado estadístico
│   │   ├── Volumen Especifico.md                     # REWRITE · order:4
│   │   └── Calidad.md                                # REWRITE · order:5 — qué mide x físicamente
│   │
│   ├── Potenciales Termodinamicos/
│   │   ├── index.md                                  # REWRITE · order:1 — narrativa Legendre: por qué existen, qué mide cada uno
│   │   ├── Energia Interna.md                        # REWRITE · order:2 — experimento de Joule, u(T,v)
│   │   ├── Entalpia.md                               # REWRITE · order:3 — por qué H = U + PV, flujo estacionario
│   │   ├── Entropia.md                               # REWRITE · order:4 — criterio de dirección, producción de entropía
│   │   ├── Helmholtz.md                              # REWRITE · order:5 — trabajo máximo isotérmico
│   │   ├── Gibbs.md                                  # REWRITE · order:6 — equilibrio a T,P constantes; Gibbs-Duhem
│   │   └── Exergia.md                                # REWRITE · order:7 — trabajo útil máximo respecto al ambiente
│   │
│   ├── Sustancias Puras/
│   │   ├── index.md                                  # +order:1
│   │   ├── Diagramas de Fase.md                      # +order:2
│   │   ├── Cambio de Fase.md                         # +order:3
│   │   ├── Propiedades en la Region Bifasica.md      # +order:4
│   │   ├── Liquido Comprimido.md                     # +order:5
│   │   └── Vapor Sobrecalentado.md                   # +order:6
│   │
│   └── Ecuaciones de Estado/
│       ├── index.md                                  # REWRITE · order:1 — qué hace una EOS, cuándo usar cuál
│       ├── Gas Ideal.md                              # REWRITE · order:2 — hipótesis, límites de validez, Mayer
│       └── Gas Real.md                               # REWRITE · order:3 — van der Waals, Peng-Robinson, factor Z
│
├── Conservacion/
│   │
│   ├── Sistemas Cerrados/
│   │   ├── index.md                                  # NEW · order:1 — qué es SC, frontera, masa fija
│   │   ├── Primera Ley SC.md                         # REWRITE · order:2 — ΔU = Q − W con física clara
│   │   ├── Segunda Ley SC.md                         # REWRITE · order:3 — Clausius, producción de entropía
│   │   └── Balance de Exergia SC.md                  # REWRITE · order:4 — destrucción de exergía = T₀ Ṡgen
│   │
│   └── Volumenes de Control/
│       ├── index.md                                  # NEW · order:1 — VC vs SC, flujo de masa y entalpía de flujo
│       ├── Balance de Masa VC.md                     # REWRITE · order:2
│       ├── Balance de Energia VC.md                  # REWRITE · order:3 — por qué aparece h en vez de u
│       ├── Balance de Entropia VC.md                 # REWRITE · order:4
│       └── Balance de Exergia VC.md                  # REWRITE · order:5
│
├── Sistemas/
│   ├── index.md                                      # NEW · order:1 — tipología SC/VC/estacionario
│   ├── Sistemas Cerrados.md                          # REWRITE · order:2
│   ├── Volumenes de Control.md                       # REWRITE · order:3
│   ├── Flujo Estacionario.md                         # REWRITE · order:4 — hipótesis SFSS y sus consecuencias
│   └── Dispositivos Flujo/
│       ├── index.md                                  # REWRITE · order:1 — mapa de dispositivos y criterio de selección
│       ├── Turbinas.md                               # FIX · order:2 — contenido OK, arreglar [!regla] y añadir más intuición física
│       ├── Compresores.md                            # FIX · order:3
│       ├── Toberas.md                                # REWRITE · order:4 — convergente vs divergente, Mach
│       ├── Difusores.md                              # REWRITE · order:5
│       ├── Valvulas.md                               # REWRITE · order:6 — proceso irreversible, h=cte
│       ├── Intercambiadores.md                       # REWRITE · order:7
│       └── Flash.md                                  # REWRITE · order:8
│
├── Procesos/
│   ├── index.md                                      # FIX · order:1 — estructura sólida; corregir callouts, añadir order
│   ├── Procesos Reversibles e Irreversibles.md       # REWRITE · order:2 — qué hace irreversible a un proceso
│   ├── Proceso Isocorico.md                          # REWRITE · order:3
│   ├── Proceso Isobarico.md                          # REWRITE · order:4
│   ├── Proceso Isotermico.md                         # REWRITE · order:5
│   ├── Proceso Adiabatico.md                         # REWRITE · order:6
│   └── Proceso Politropico.md                        # REWRITE · order:7 — n como unificador; límites n→0,1,γ,∞
│
├── Relaciones Termodinamicas/
│   ├── index.md                                      # +order:1
│   ├── Maxwell.md                                    # +order:2
│   ├── TdS.md                                        # +order:3
│   ├── Identidades/
│   │   ├── index.md                                  # +order:1
│   │   ├── Regla Ciclica.md                          # +order:2
│   │   └── Presion Interna.md                        # +order:3
│   ├── Cp Cv/
│   │   ├── index.md                                  # +order:1
│   │   ├── Razon de Calores.md                       # +order:2
│   │   └── Efecto Joule Thomson.md                   # +order:3
│   └── Jacobianos/
│       ├── index.md                                  # +order:1
│       ├── Aplicaciones Termodinamicas.md            # +order:2
│       └── Derivadas Isentropicas.md                 # +order:3
│
├── Mezclas/
│   ├── index.md                                      # REWRITE · order:1 — Dalton y Amagat, mezcla ideal vs real
│   ├── Mezclas de Gases.md                           # REWRITE · order:2 — fracciones másicas/molares, propiedades aparentes
│   ├── Psicrometria/
│   │   ├── index.md                                  # FIX · order:1 — contenido muy bueno (añadido por usuario); eliminar [!observacion] y prosa bajo ###
│   │   ├── Carta Psicrometrica.md                    # REWRITE · order:2 — cómo leer las 5 familias de curvas
│   │   ├── Procesos Psicrometricos.md                # REWRITE · order:3 — calentamiento, enfriamiento, humidificación, mezcla
│   │   └── Torres de Enfriamiento.md                 # REWRITE · order:4
│   └── Combustion/
│       ├── index.md                                  # REWRITE · order:1 — estequiometría, exceso de aire, razón A/F
│       ├── Combustion Incompleta.md                  # REWRITE · order:2 — CO, análisis Orsat
│       └── Temperatura Adiabatica de Llama.md        # REWRITE · order:3 — T_AF como límite superior
│
└── Conversion de Energia/
    ├── index.md                                      # NEW · order:1 — eficiencia de Carnot como límite universal
    ├── Ciclos de Potencia/
    │   ├── index.md                                  # NEW · order:1 — criterios para comparar ciclos (η, trabajo neto, BSR)
    │   ├── Rankine/
    │   │   ├── index.md                              # NEW · order:1 — por qué vapor; los 4 procesos
    │   │   ├── Ciclo Rankine Simple.md               # NEW · order:2 — η ideal, calidad a la salida de turbina
    │   │   ├── Rankine con Recalentamiento.md        # NEW · order:3 — por qué: evitar humedad; cuánto mejora η
    │   │   └── Rankine Regenerativo.md               # NEW · order:4 — feedwater heating; FWH abierto y cerrado
    │   ├── Brayton/
    │   │   ├── index.md                              # NEW · order:1 — turbina de gas: aire estándar, BSR
    │   │   ├── Ciclo Brayton.md                      # NEW · order:2 — η vs relación de presiones, punto óptimo BSR
    │   │   └── Brayton con Regeneracion.md           # NEW · order:3 — condición ε > 0: T₃ < T₅; intercooling y recalentamiento
    │   └── Ciclos Combustion Interna/
    │       ├── index.md                              # NEW · order:1 — diferencia Otto/Diesel: cómo se añade calor
    │       ├── Ciclo Otto.md                         # NEW · order:2 — η = 1 − r^(1−γ); relación de compresión
    │       └── Ciclo Diesel.md                       # NEW · order:3 — η vs r y relación de corte r_c
    └── Refrigeracion/
        ├── index.md                                  # NEW · order:1 — COP, ciclo inverso de Carnot
        ├── Ciclo de Compresion de Vapor.md           # NEW · order:2 — los 4 procesos, diagrama P-h
        └── Bomba de Calor.md                         # NEW · order:3 — COP_BC = COP_R + 1
```

---

## Resumen del alcance

| Estado | Secciones | N.º archivos |
|:---|:---|:---:|
| **NEW** — crear desde cero | Variables de Estado index · Conservacion indexes (×2) · Sistemas index · Conversion de Energia completa | 17 |
| **REWRITE** — reescritura completa | Potenciales (7) · Conservacion notas (7) · Sistemas notas (3+7) · Procesos notas (6) · Mezclas (6) · Ecuaciones de Estado (3) | 39 |
| **FIX** — contenido OK, arreglar callouts prohibidos + order | Presión · Procesos/index · Psicrometria/index · Turbinas · Compresores | 5 |
| **+order** — solo campo order en frontmatter | Sustancias Puras (6) · Relaciones Termodinamicas (12) | 18 |
| **Total** | | **79** |

## Orden de ejecución por sesión

1. **Potenciales Termodinámicos** (7 REWRITE) — base conceptual de todo
2. **Variables de Estado** (1 NEW + 4 REWRITE) — fundamentos
3. **Conservacion** (2 NEW index + 7 REWRITE) — leyes de balance
4. **Procesos** (1 FIX + 6 REWRITE)
5. **Sistemas** (1 NEW + 3 REWRITE + 1 FIX + 7 mix) — dispositivos
6. **Mezclas** (2 FIX + 9 REWRITE)
7. **Ecuaciones de Estado** (3 REWRITE)
8. **+order en Relaciones y Sustancias Puras** — batch rápido
9. **Conversion de Energia** (17 NEW) — ciclos completos
