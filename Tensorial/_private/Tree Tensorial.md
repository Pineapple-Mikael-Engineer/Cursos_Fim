---
title: Tree Tensorial
draft: true
---
# Tree

> Árbol del curso de **Análisis Tensorial**, alineado con la **Parte I** del libro
> *Física Matemática* de **J. Rogan y V. Muñoz** (U. de Chile): capítulos 1-7.
> Las secciones `1`-`7` siguen los capítulos del libro (ver `# cap N.M`); cada
> hoja `.md` es un concepto consultable aislado y cada carpeta con hijas lleva su
> `index.md`.
>
> El libro enfoca los tensores desde la **física/ingeniería** (Cartesianas primero,
> notación diádica, motivado por el tensor de conductividad) y alcanza la física
> "pura" vía el **grupo de Lorentz y la covarianza de Maxwell** —no vía geometría
> riemanniana—. Por eso la geometría diferencial / Relatividad General queda como
> **sección 10 opcional "más allá del libro"** (tu vocación de GR).
>
> Marcadores: `# ✔` = nota ya existente (renombrar/adecuar); sin marca = por crear;
> `(opcional)` = posponible.

```tree
Tensorial/
│
├── index.md                                      # ✔ (vacío) — portada del curso
│
├── 1 Algebra Lineal y Notacion/                  # cap 1
│   ├── index.md
│   ├── Notacion Indices Sumatorias.md            # ✔ cap 1.1 — mudo/libre, Einstein
│   ├── Algebra Lineal para Tensores.md           # ✔ vectores, bases, producto
│   ├── Operaciones Vectoriales/                  # cap 1.2
│   │   ├── index.md
│   │   ├── Rotacion de Vectores.md               # cap 1.2.1
│   │   ├── Productos Vectoriales.md              # cap 1.2.2 — punto y cruz
│   │   └── Calculos con Notacion Einstein.md     # cap 1.2.3
│   └── Simbolos Especiales/                      # δ y ε (introducidos en 1.2.3)
│       ├── index.md
│       ├── Delta Kronecker.md                    # ✔ δ_ij; δ_ii=n, sustitución
│       ├── Simbolo Levi-Civita.md               # ε_ijk; arreglo 3×3×3
│       └── Identidad Epsilon-Delta.md           # ε_ijk ε_ilm = δ_jl δ_km − δ_jm δ_kl
│
├── 2 Operadores en Campos/                       # cap 2 — cálculo vectorial
│   ├── index.md
│   ├── Campos Escalares y Vectoriales.md         # cap 2.1 — dibujar campos
│   ├── Operadores Integrales/                    # cap 2.2
│   │   ├── index.md
│   │   ├── Integral de Linea.md                  # cap 2.2.2
│   │   ├── Integral de Superficie.md             # cap 2.2.3
│   │   └── Integral de Volumen.md                # cap 2.2.4
│   ├── Operadores Diferenciales/                 # cap 2.3
│   │   ├── index.md
│   │   ├── Gradiente.md                          # cap 2.3.1 — vista física
│   │   ├── Divergencia.md                        # cap 2.3.2
│   │   ├── Rotor.md                              # cap 2.3.3
│   │   ├── Identidades Operadores.md             # cap 2.3.4
│   │   └── Definiciones Integrales Operadores.md # cap 2.4
│   └── Teoremas Integrales/                      # cap 2.5
│       ├── index.md
│       ├── Teorema de Gauss.md                   # cap 2.5.1
│       ├── Teorema de Green.md                   # cap 2.5.2
│       ├── Teorema de Stokes.md                  # cap 2.5.3
│       └── Teorema de Helmholtz.md               # cap 2.5.4
│
├── 3 Coordenadas Curvilineas/                    # cap 3
│   ├── index.md
│   ├── Vector Posicion.md                        # cap 3.1
│   ├── Sistema Cilindrico.md                     # cap 3.2 — h_r=1, h_θ=r, h_z=1
│   ├── Sistema Esferico.md                       # cap 3.3 — h_r=1, h_θ=r, h_φ=r sinθ
│   ├── Operaciones Cilindricas y Esfericas.md    # cap 3.5 — grad/div/rot explícitos
│   └── Sistemas Curvilineos Generales/           # cap 3.4
│       ├── index.md
│       ├── Coordenadas Vectores Base Factores Escala.md  # cap 3.4.1
│       ├── Elementos Linea Superficie Volumen.md         # cap 3.4.5-3.4.7
│       └── Gradiente Divergencia Rotor Generales.md      # cap 3.4.8-3.4.10
│
├── 4 Introduccion a Tensores/                    # cap 4 — Cartesianas, notación diádica
│   ├── index.md
│   ├── Tensor Conductividad y Ley de Ohm.md      # cap 4.1 — motivación física: J_i = σ_ij E_j
│   ├── Notacion Tensorial y Terminologia.md      # cap 4.2 — σ = σ_ij ê_i ê_j; orden/rango
│   ├── Diagonalizacion de Tensores.md            # cap 4.4 — valores y vectores propios
│   ├── Transformaciones entre Sistemas/          # cap 4.3
│   │   ├── index.md
│   │   ├── Transformaciones Vectoriales Cartesianas.md  # cap 4.3.1
│   │   ├── Matriz de Transformacion.md           # cap 4.3.2
│   │   ├── Transformaciones Tensoriales.md       # cap 4.3.4
│   │   └── (opcional) Transformaciones en Curvilineas.md # cap 4.5
│   └── Pseudo-objetos/                           # cap 4.6 — mano derecha vs izquierda
│       ├── index.md
│       ├── Pseudo-vectores.md                    # cap 4.6.1
│       ├── Pseudo-escalares.md                   # cap 4.6.2
│       └── Pseudo-tensores.md                    # cap 4.6.3
│
├── 5 Coordenadas No Ortogonales/                 # cap 5 — covarianza y contravarianza
│   ├── index.md
│   ├── Sistema Inclinado.md                      # cap 5.2.1 — base no ortogonal
│   ├── Covarianza Contravarianza Metrica.md      # cap 5.2.2 — g_ij, núcleo del capítulo
│   ├── Notacion Subindices Superindices.md       # cap 5.2.4 — A_i vs A^i
│   ├── Transformaciones Contravariantes.md       # cap 5.2.3
│   ├── Transformaciones Covariantes.md           # cap 5.2.5
│   ├── Covarianza Contravarianza en Tensores.md  # cap 5.2.6
│   └── Derivadas Parciales Co y Contravariantes.md # cap 5.2.7
│
├── 6 Determinantes y Matrices/                   # cap 6
│   ├── index.md
│   ├── Determinantes.md                          # cap 6.1
│   ├── Matrices.md                               # cap 6.2
│   ├── Matrices Ortogonales.md                   # cap 6.3
│   ├── Matrices Hermiticas y Unitarias.md        # cap 6.4
│   ├── Diagonalizacion de Matrices.md            # cap 6.5
│   └── Matrices Normales.md                      # cap 6.6
│
├── 7 Teoria de Grupo/                            # cap 7 — el puente a la física
│   ├── index.md
│   ├── Generadores de Grupos Continuos.md        # cap 7.2
│   ├── Momento Angular Orbital.md                # cap 7.3
│   ├── Grupo Homogeneo de Lorentz.md             # cap 7.4
│   └── Covarianza de Lorentz de Maxwell.md       # cap 7.5
│
├── 8 Ejercicios/                                 # ✔ problemas resueltos
│   ├── index.md
│   ├── Ejercicios Notacion Indices Algebra Lineal.md      # ✔
│   ├── Distribucion Sumatorias Indices Libres Mudos.md    # ✔
│   ├── Derivada Forma Cuadratica Notacion Indices.md      # ✔
│   └── Derivada Monomio Cuartico Indices Repetidos.md     # ✔
│
├── 9 Apuntes Clase/                              # opcional: cajón de notas sueltas
│   └── (cualquier nota suelta que aún no clasificas)
│
└── (opcional) 10 Extension Geometria Diferencial/  # MÁS ALLÁ DEL LIBRO — vocación GR
    ├── index.md
    ├── Tensor Metrico Riemanniano.md             # g_ij con curvatura, no solo coords
    ├── Simbolos Christoffel.md                   # Γ^k_ij = ½ g^kl(∂g+∂g−∂g)
    ├── Derivada Covariante.md                    # ∇_j A^i = ∂_j A^i + Γ^i_jk A^k
    ├── Tensor de Riemann.md                      # R^i_jkl; curvatura
    ├── Geodesicas.md                             # ẍ^i + Γ^i_jk ẋ^j ẋ^k = 0
    └── (opcional) Ecuaciones de Einstein.md      # G_μν = 8πG T_μν
```

**Libro:** *Física Matemática*, J. Rogan C. y V. Muñoz G., 3ª ed. — Parte I (cap. 1-7).
Cap. 4 basado en *Mathematical Physics* de Kusse & Westwig.
