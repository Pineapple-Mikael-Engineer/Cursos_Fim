---
title: Tree Circuitos Electricos
draft: true
---
# Tree

> Árbol del curso **Circuitos Eléctricos (ML 140)**. Orden = **sílabo** (7 capítulos, columna
> vertebral); profundidad y presentación = **Jesús Fraile Mora**, *Circuitos Eléctricos* (Pearson,
> 2012) — modelo de estilo (muchos ejemplos resueltos, figuras claras, normas CENELEC/IEC).
>
> `✔` = nota ya existente (por integrar/renombrar). `# fig:` = figura planeada (`_media/img_gen/`):
> los **circuitos** se dibujan con **circuitikz** (B/N) y las **ondas/fasores/potencia** con
> **matplotlib** (paleta Ocean Forest). `(opcional)` = posponible.

```tree
Circuitos Electricos/
│
├── index.md                                       # portada: qué es un circuito, las 2 grandes partes (DC y AC)
│
├── 1 Conceptos Fundamentales y Resistivos/        # Cap I (sem 1-2)
│   ├── index.md
│   │
│   ├── Fundamentos/
│   │   ├── index.md
│   │   ├── Variables del Circuito.md             # carga, corriente i, tensión v
│   │   ├── Convenio de Signos.md                 # signo pasivo (carga) vs activo (generador)  # fig: convenios
│   │   ├── Potencia y Energia.md                 # p=vi; W=∫p dt; absorbida/entregada
│   │   ├── Sistema de Unidades.md                # SI, prefijos, magnitudes
│   │   ├── Tipos de Corriente.md                 # CC, CA, formas de onda
│   │   └── Instrumentos de Medicion.md           # voltímetro, amperímetro, vatímetro  # fig: conexión
│   │
│   ├── Elementos del Circuito/
│   │   ├── index.md
│   │   ├── Resistencia y Ley de Ohm.md           # R, v=Ri, conductancia G  # fig: símbolo R
│   │   ├── Fuentes Independientes.md             # fuente de tensión y de corriente ideales  # fig: símbolos
│   │   ├── Fuentes Dependientes.md               # VCVS, VCCS, CCVS, CCCS  # fig: símbolos
│   │   ├── Fuentes Reales.md                     # con resistencia interna; recta de carga
│   │   └── Elementos Activos y Pasivos.md        # clasificación; modelos lineales
│   │
│   ├── Leyes de Kirchhoff/
│   │   ├── index.md
│   │   ├── Ley de Corrientes LKC.md              # primer lema; Σi en un nodo = 0  # fig: nodo
│   │   ├── Ley de Voltajes LKV.md                # segundo lema; Σv en una malla = 0  # fig: malla
│   │   ├── Ecuaciones Independientes.md          # cuántas LKC/LKV independientes (topología)
│   │   └── Balance de Potencias.md               # Σ generada = Σ disipada (Tellegen)
│   │
│   └── Reduccion de Circuitos/
│       ├── index.md
│       ├── Resistencias en Serie y Paralelo.md   # # fig: serie/paralelo
│       ├── Divisor de Voltaje.md                 # # fig: divisor
│       ├── Divisor de Corriente.md
│       ├── Transformacion de Fuentes.md          # equivalencia fuente V real ↔ fuente I real  # fig
│       ├── Estrella-Triangulo (Kennelly).md      # Y↔Δ  # fig: Y-Δ
│       ├── RINCE.md                              # ramas independientes para el equivalente
│       └── Simetria en Circuitos.md              # explotar simetrías
│
├── 2 Metodos de Analisis y Teoremas/              # Cap II (sem 3-4)
│   ├── index.md
│   │
│   ├── Topologia de Redes/
│   │   ├── index.md
│   │   ├── Definiciones Topologicas.md           # rama, nodo, lazo, malla, árbol, cuerda
│   │   └── Ramas y Mallas Independientes.md      # r = b-n+1
│   │
│   ├── Metodos de Analisis/
│   │   ├── index.md
│   │   ├── Analisis de Mallas.md                 # formulación matricial general  # fig: mallas
│   │   ├── Mallas con Fuentes de Corriente.md    # supermalla
│   │   ├── Analisis de Nodos.md                  # formulación matricial general  # fig: nodos
│   │   ├── Nodos con Fuentes de Voltaje.md       # supernodo
│   │   └── Ecuaciones de Restriccion.md          # fuentes dependientes
│   │
│   ├── Teoremas/
│   │   ├── index.md
│   │   ├── Proporcionalidad y Superposicion.md   # # fig: descomposición
│   │   ├── Teorema de Thevenin.md                # V_Th, R_Th  # fig: equivalente
│   │   ├── Teorema de Norton.md                  # I_N, R_N  # fig
│   │   ├── Maxima Transferencia de Potencia.md   # R_L=R_Th  # fig: P vs R_L
│   │   ├── Teorema de Millman.md
│   │   └── (opcional) Sustitucion Reciprocidad Tellegen.md
│   │
│   ├── (opcional) Cuadripolos.md                 # parámetros Z, Y, h, ABCD (Fraile 1.17)
│   └── (opcional) Amplificador Operacional.md    # AO ideal (Fraile 1.18)  # fig: inversor
│
├── 3 Almacenamiento y Transitorios/               # Cap III (sem 5-7)
│   ├── index.md
│   │
│   ├── Elementos de Almacenamiento/
│   │   ├── index.md
│   │   ├── Capacitor.md                          # i=C dv/dt; W=½CV²  # fig: símbolo C
│   │   ├── Inductor.md                           # v=L di/dt; W=½LI²  # fig: símbolo L
│   │   ├── Asociacion de C y L.md                # serie/paralelo
│   │   ├── Condiciones Iniciales.md              # continuidad de v_C e i_L
│   │   └── Circuitos DC en Estado Estable.md     # C→abierto, L→corto
│   │
│   ├── Transitorios Primer Orden/
│   │   ├── index.md
│   │   ├── Circuito RL.md                        # respuesta natural y forzada  # fig: RL + respuesta
│   │   ├── Circuito RC.md                        # # fig: RC + respuesta
│   │   ├── Constante de Tiempo.md                # τ; decaimiento exponencial  # fig: e^{-t/τ}
│   │   └── Respuesta Completa Primer Orden.md    # método sistemático (x∞ + (x0-x∞)e^{-t/τ})
│   │
│   ├── Transitorios Segundo Orden/
│   │   ├── index.md
│   │   ├── Circuito RLC Serie.md                 # # fig: RLC
│   │   ├── Circuito RLC Paralelo.md
│   │   ├── Regimenes de Amortiguamiento.md       # sub/crítico/sobreamortiguado  # fig: 3 regímenes
│   │   └── Funciones Singulares.md               # escalón, impulso, rampa  # fig
│   │
│   └── Laplace en Circuitos/
│       ├── index.md
│       ├── Transformada de Laplace.md            # definición, pares y propiedades (tabla)
│       ├── Circuitos en el Dominio de s.md       # impedancia operacional; modelos con C.I.  # fig
│       ├── Funcion de Transferencia.md           # H(s); diagrama de polos y ceros  # fig: polos-ceros
│       └── Solucion de Transitorios con Laplace.md
│
├── 4 Ondas Periodicas Sinusoidales/               # Cap IV (sem 9)
│   ├── index.md
│   ├── Onda Sinusoidal.md                        # A·sen(ωt+φ); generación  # fig: senoide
│   ├── Caracteristicas de Ondas Periodicas.md    # período, frecuencia, fase, amplitud
│   ├── Valor Medio.md                            # promedio en un período
│   ├── Valor Eficaz RMS.md                       # raíz del valor cuadrático medio; V_rms=V_m/√2
│   ├── Factor de Forma y Cresta.md
│   └── Generacion de Tension Alterna.md          # alternador elemental  # fig: espira girando
│
├── 5 Circuitos AC Sinusoidal y Fasores/           # Cap V (sem 10-11)
│   ├── index.md
│   │
│   ├── Fasores/                                   # ✔ carpeta existente
│   │   ├── index.md
│   │   ├── Representacion de Fasores.md          # ✔ fasor V∠φ ; del tiempo a la frecuencia  # fig: fasor
│   │   ├── Fasores Electricos.md                 # ✔ representación compleja de la senoide
│   │   └── Dominio del Tiempo y Frecuencia.md    # derivada→jω; transformación fasorial
│   │
│   ├── Impedancia y Admitancia/
│   │   ├── index.md
│   │   ├── Respuesta de Elementos Pasivos.md     # R, L, C puros en AC; desfases  # fig: v-i por elemento
│   │   ├── Impedancia Compleja.md                # Z=R+jX; Z_R, Z_L=jωL, Z_C=1/jωC
│   │   ├── Admitancia.md                         # Y=1/Z=G+jB
│   │   └── Asociacion de Impedancias.md          # serie/paralelo; divisores fasoriales
│   │
│   ├── Analisis Fasorial/
│   │   ├── index.md
│   │   ├── Metodos en Regimen Fasorial.md        # mallas, nodos, Thévenin en fasorial
│   │   └── Diagramas Fasoriales.md               # # fig: diagrama fasorial
│   │
│   ├── Potencia en AC/
│   │   ├── index.md
│   │   ├── Potencia Instantanea.md               # p(t)=v·i
│   │   ├── Potencia en Elementos Puros.md        # ✔ R disipa, L y C no  # fig
│   │   ├── Potencia en Sinuidal y Fasorial.md    # ✔ activa P, reactiva Q, aparente S
│   │   ├── Potencia Compleja.md                  # S=VI*=P+jQ  # fig: triángulo de potencias
│   │   ├── Factor de Potencia.md                 # cos φ
│   │   ├── Correccion del Factor de Potencia.md  # banco de capacitores  # fig
│   │   ├── Maxima Transferencia AC.md            # Z_L=Z_Th*
│   │   └── (opcional) Lugares Geometricos.md
│   │
│   └── (opcional) Resonancia.md                  # RLC resonante; ancho de banda, Q  # fig: |Z|(ω)
│
├── 6 Acoplamiento Magnetico/                      # Cap VI (sem 12) — aplanado (purga 2026)
│   ├── index.md                                  # absorbe la inducción magnética (autoind./mutua/k/signo)
│   ├── Autoinduccion.md                          # L; delega derivación a Inductor
│   ├── Inductancia Mutua.md                      # M; ecuaciones del par; coef. de acoplamiento k  # fig: dos bobinas
│   ├── Regla de los Puntos.md                    # convención de puntos (signo ±M)  # fig: puntos
│   ├── Acoplamiento Multiple.md                  # matriz [L]
│   ├── Energia en Bobinas Acopladas.md           # W=½L1I1²+½L2I2²±MI1I2; única demo de la cota M≤√(L1L2)
│   ├── Acoplamiento Magnetico Fasorial.md        # respuesta sinusoidal acoplada (jωM)
│   ├── Transformador con Nucleo de Aire.md       # impedancia reflejada  # fig: transformador
│   ├── Transformador Ideal.md                    # relación n; reflejo de impedancias  # fig
│   └── Circuito Equivalente con Acoplo Conductivo.md  # T equivalente  # fig: T
│   # PURGA: eliminados Induccion Magnetica/ (subcarpeta+index) y Coeficiente de Acoplamiento (→ Inductancia Mutua)
│
├── 7 Circuitos Trifasicos/                        # Cap VII (sem 13-15)
│   ├── index.md
│   │
│   ├── Fundamentos Trifasicos/
│   │   ├── index.md
│   │   ├── Sistema Polifasico.md                 # qué es; por qué trifásico
│   │   ├── Generacion de Tensiones Trifasicas.md # 3 fases a 120°  # fig: 3 senoides + fasores
│   │   ├── Secuencia de Fases.md                 # ABC vs ACB
│   │   └── Ventajas del Trifasico.md             # transporte; vs monofásico
│   │
│   ├── Conexiones Balanceadas/
│   │   ├── index.md
│   │   ├── Conexion Estrella.md                  # Y; V_L=√3 V_F  # fig: Y
│   │   ├── Conexion Triangulo.md                 # Δ; I_L=√3 I_F  # fig: Δ
│   │   ├── Sistemas Y-Y, Delta-Delta, Y-Delta.md # combinaciones fuente-carga
│   │   └── Circuito Equivalente Monofasico.md    # análisis por fase
│   │
│   ├── Potencia Trifasica/
│   │   ├── index.md
│   │   ├── Potencia en Sistemas Balanceados.md   # P=√3 V_L I_L cos φ
│   │   ├── Medicion con Dos Vatimetros.md        # método de los 2 vatímetros  # fig: conexión
│   │   └── Correccion FP Trifasico.md
│   │
│   └── Sistemas Desbalanceados/
│       ├── index.md
│       ├── Cargas Desbalanceadas Estrella.md     # con/sin neutro
│       ├── Cargas Desbalanceadas Triangulo.md
│       └── (opcional) Componentes Simetricas.md  # secuencias +, -, 0 (Fraile 3.10)
│
└── 8 Apuntes Clase/                               # opcional: notas sueltas / ejercicios de PC
    └── (cualquier nota suelta o problema resuelto que aún no clasificas)
```

**Fuentes:**
- *Circuitos Eléctricos*, **Jesús Fraile Mora** (Pearson, 2012) — modelo de estilo y de profundidad.
- **Sílabo ML 140 (2026-I)** — columna vertebral del orden y alcance (7 capítulos, 16 semanas).
- Bibliografía de apoyo del sílabo: Boylestad, Dorf, Nilsson, Hayt-Kemmerly, Alexander-Sadiku.
