---
title: Tree Tensorial
draft: true
---
# Tree

> Árbol del curso de **Análisis Tensorial**, alineado con la **Parte I** del libro
> *Física Matemática* de **J. Rogan y V. Muñoz** (U. de Chile): capítulos 1-7.
> Secciones `1`-`7` = capítulos del libro (`# cap N.M`). Cada hoja `.md` es un concepto
> consultable aislado; cada carpeta con hijas lleva su `index.md`.
>
> Las figuras planeadas se anotan `# fig:` y van en `_media/img_gen/` (código en `_media/code_gen/`),
> embebidas con `![[nombre.svg|ancho]]`. La geometría diferencial / Relatividad General (más allá del
> libro) queda como **sección 10 opcional**.
>
> Marcadores: `# ✔` = nota ya existente; sin marca = por crear; `(opcional)` = posponible.

```tree
Tensorial/
│
├── index.md                                      # ✔ (vacío) — portada del curso
│
├── _media/                                       # recursos visuales
│   ├── img_gen/                                  # ✔ figuras generadas (.svg)
│   └── code_gen/                                 # ✔ código generador (.py matplotlib / .tex TikZ)
│
├── 1 Algebra Lineal y Notacion/                  # cap 1
│   ├── index.md                                  # ✔
│   ├── Notacion Indices Sumatorias.md            # ✔ mudo/libre, Einstein   # fig: sistema cartesiano ê_i
│   ├── Algebra Lineal para Tensores.md           # ✔ vectores, [M], M_ij N_jk = P_ik
│   ├── Operaciones Vectoriales/                  # cap 1.2
│   │   ├── index.md                              # ✔
│   │   ├── Rotacion de Vectores.md               # ✔ [R(φ)], a'_i=R_ij a_j   # fig: rotación 2D
│   │   ├── Producto Punto.md                     # A·B=A_iB_i=A_iB_jδ_ij     # fig: proyección |A||B|cosθ
│   │   ├── Producto Cruz.md                      # A×B=ε_ijk A_iB_j ê_k       # fig: regla mano derecha + determinante
│   │   ├── Productos Vectoriales.md              # ✔ (índice/resumen de los dos productos)
│   │   └── Calculos con Notacion Einstein.md     # ✔ |A| invariante + BAC-CAB
│   └── Simbolos Especiales/                      # δ y ε
│       ├── index.md                              # ✔
│       ├── Delta Kronecker.md                    # ✔ δ_ij; δ_ii=n, sustitución
│       ├── Simbolo Levi-Civita.md                # ✔ ε_ijk; permutaciones    # fig: arreglo 3×3×3
│       └── Identidad Epsilon-Delta.md            # ✔ ε_ijk ε_mnk = δ_im δ_jn − δ_in δ_jm
│
├── 2 Operadores en Campos/                       # cap 2 — cálculo vectorial
│   ├── index.md                                  # ✔
│   ├── Campos Escalares y Vectoriales.md         # ✔   # fig: equipotenciales + líneas de campo (2 cargas, Φ=−xy)
│   ├── Operadores Integrales/                    # cap 2.2 — todas actúan sobre escalar Y vector
│   │   ├── index.md                              # ✔ notación de operador ∫dx f(x)
│   │   ├── Integral de Linea.md                  # ✔ ∮dr·F=∫dx_i F_i (escalar); ∫dr Φ, ∫dr×v (vector)  # fig: dr tangente a C
│   │   ├── Integral de Superficie.md             # ✔ ∫dσ·v=∫dσ_i v_i; ∫dσ Φ, ∫dσ×v (vector)            # fig: dσ=n̂dσ
│   │   └── Integral de Volumen.md                # ✔ ∫dτ Φ (escalar) y ∫dτ v (vector)                   # fig: dτ=dx dy dz
│   ├── Operadores Diferenciales/                 # cap 2.3
│   │   ├── index.md                              # ✔ ∇=ê_i ∂/∂x_i
│   │   ├── Gradiente.md                          # ✔ dΦ=∇Φ·dr; ⟂ equipotenciales   # fig: ∇Φ normal a Φ=cte
│   │   ├── Divergencia.md                        # ✔ demo ecuación de continuidad   # fig: flujo por 6 caras del cubo
│   │   ├── Rotor.md                              # ✔ demo circulación/área          # fig: camino C1..C4 + vórtice vs rígido
│   │   ├── Identidades Operadores.md             # ✔ ∇·∇Φ=∇²Φ; ∇×∇×v=∇(∇·v)−∇²v
│   │   └── Definiciones Integrales Operadores.md # ✔ ∇Φ, ∇·A, ∇×A como límites integrales
│   └── Teoremas Integrales/                      # cap 2.5
│       ├── index.md                              # ✔
│       ├── Teorema de Gauss.md                   # ✔ ∫dτ∇·A=∮dσ·A   # fig: volúmenes adyacentes, caras internas se cancelan
│       ├── Teorema de Green.md                   # ✔ dos formas
│       ├── Teorema de Stokes.md                  # ✔ ∫dσ·(∇×A)=∮dr·A; campo conservativo   # fig: superficies adyacentes
│       └── Teorema de Helmholtz.md               # ✔ unicidad + descomposición solenoidal/irrotacional
│
├── 3 Coordenadas Curvilineas/                    # cap 3
│   ├── index.md                                  # fig: comparación cartesiano/cilíndrico/esférico
│   ├── Vector Posicion.md                        # cap 3.1   # fig: r en coordenadas
│   ├── Sistema Cilindrico/                        # cap 3.2
│   │   ├── index.md                              # (ρ,φ,z)   # fig: sistema cilíndrico
│   │   ├── Vectores Base y Factores Escala.md    # h_ρ=1, h_φ=ρ, h_z=1; q̂_ρ,q̂_φ,q̂_z
│   │   └── Operaciones Cilindricas.md            # cap 3.5.1 — grad/div/rot explícitos   # ej: laplaciano de Φ(ρ)
│   ├── Sistema Esferico/                          # cap 3.3
│   │   ├── index.md                              # (r,θ,φ)   # fig: sistema esférico
│   │   ├── Vectores Base y Factores Escala.md    # h_r=1, h_θ=r, h_φ=r sen θ
│   │   └── Operaciones Esfericas.md              # cap 3.5.2   # ej: divergencia de campo radial
│   └── Sistemas Curvilineos Generales/           # cap 3.4
│       ├── index.md
│       ├── Coordenadas y Vectores Base.md        # cap 3.4.1   # fig: base curvilínea local
│       ├── Factores de Escala.md                 # cap 3.4.1 — h_i=|∂r/∂q_i|; base física vs coordenada
│       ├── Geometria Diferencial Local.md        # cap 3.4.2
│       ├── Elementos Linea Superficie Volumen.md # cap 3.4.5-3.4.7   # dl, dσ, dτ en curvilíneas
│       ├── Gradiente General.md                  # cap 3.4.8 — ∇Φ=Σ (1/h_i)(∂Φ/∂q_i) q̂_i
│       ├── Divergencia General.md                # cap 3.4.9
│       └── Rotor General.md                      # cap 3.4.10
│
├── 4 Introduccion a Tensores/                    # cap 4 — Cartesianas, notación diádica
│   ├── index.md
│   ├── Tensor Conductividad y Ley de Ohm.md      # cap 4.1 — motivación: J_i=σ_ij E_j   # fig: J no paralelo a E
│   ├── Notacion Tensorial y Terminologia.md      # cap 4.2 — σ=σ_ij ê_i ê_j; orden/rango
│   ├── Operaciones con Tensores.md               # suma, producto diádico, contracción a nivel tensorial   # ej resueltos
│   ├── Transformaciones entre Sistemas/          # cap 4.3
│   │   ├── index.md
│   │   ├── Transformaciones Vectoriales Cartesianas.md  # cap 4.3.1   # fig: sistemas rotados
│   │   ├── Matriz de Transformacion.md           # cap 4.3.2 — [a]'=[R][a], ortogonalidad
│   │   ├── Transformaciones Tensoriales.md       # cap 4.3.4 — σ'_ij=R_ik R_jl σ_kl
│   │   └── (opcional) Transformaciones en Curvilineas.md # cap 4.5
│   ├── Diagonalizacion de Tensores/              # cap 4.4
│   │   ├── index.md                              # problema de valores propios
│   │   ├── Valores y Vectores Propios.md         # det(σ−λI)=0   # ej: diagonalizar un tensor 3×3
│   │   └── Ejes Principales.md                   # interpretación   # fig: elipsoide del momento de inercia
│   └── Pseudo-objetos/                           # cap 4.6 — mano derecha vs izquierda
│       ├── index.md                              # fig: sistema mano derecha vs izquierda
│       ├── Pseudo-vectores.md                    # cap 4.6.1
│       ├── Pseudo-escalares.md                   # cap 4.6.2
│       └── Pseudo-tensores.md                    # cap 4.6.3
│
├── 5 Coordenadas No Ortogonales/                 # cap 5 — covarianza y contravarianza
│   ├── index.md                                  # fig: sistemas de la relatividad especial/general
│   ├── Sistema Inclinado.md                      # cap 5.2.1   # fig: base oblicua
│   ├── Metrica/                                   # el corazón del capítulo
│   │   ├── index.md
│   │   ├── Covarianza Contravarianza.md          # cap 5.2.2 — componentes A^i vs A_i   # fig: proyecciones
│   │   ├── Tensor Metrico.md                     # g_ij = e_i·e_j; subir/bajar índices
│   │   └── Base Dual Reciproca.md                # e^i·e_j=δ^i_j
│   ├── Transformaciones Contravariantes.md       # cap 5.2.3 — A'^i=(∂x'^i/∂x^j)A^j
│   ├── Transformaciones Covariantes.md           # cap 5.2.5 — A'_i=(∂x^j/∂x'^i)A_j
│   ├── Notacion Subindices Superindices.md       # cap 5.2.4 — convenio arriba/abajo
│   ├── Covarianza Contravarianza en Tensores.md  # cap 5.2.6 — T^ij, T_ij, T^i_j
│   └── Derivadas Parciales Co y Contravariantes.md # cap 5.2.7
│
├── 6 Determinantes y Matrices/                   # cap 6
│   ├── index.md
│   ├── Determinantes.md                          # cap 6.1 — definición, propiedades   # ej: cofactores, Cramer
│   ├── Matrices/                                  # cap 6.2 + tipos
│   │   ├── index.md                              # operaciones, traza, inversa
│   │   ├── Operaciones Basicas.md                # suma, producto, transpuesta
│   │   └── Matriz Inversa.md                     # ej: cálculo de inversa
│   ├── Matrices Ortogonales.md                   # cap 6.3 — R^T R=I, rotaciones
│   ├── Matrices Hermiticas y Unitarias.md        # cap 6.4 — A†=A, U†U=I
│   ├── Diagonalizacion de Matrices.md            # cap 6.5 — semejanza, autovalores   # ej resuelto
│   └── Matrices Normales.md                      # cap 6.6 — AA†=A†A
│
├── 7 Teoria de Grupo/                            # cap 7 — el puente a la física
│   ├── index.md                                  # cap 7.1 — definición de grupo, ejemplos
│   ├── Generadores de Grupos Continuos.md        # cap 7.2 — grupos de Lie, generadores   # ej: SO(2), SU(2)
│   ├── Momento Angular Orbital.md                # cap 7.3 — generadores de rotación
│   ├── Grupo Homogeneo de Lorentz.md             # cap 7.4 — boosts + rotaciones   # fig: cono de luz
│   └── Covarianza de Lorentz de Maxwell.md       # cap 7.5 — F_μν, ecuaciones de Maxwell covariantes
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
    ├── Tensor Metrico Riemanniano.md             # g_ij con curvatura
    ├── Simbolos Christoffel.md                   # Γ^k_ij = ½ g^kl(∂g+∂g−∂g)
    ├── Derivada Covariante.md                    # ∇_j A^i = ∂_j A^i + Γ^i_jk A^k
    ├── Tensor de Riemann.md                      # R^i_jkl; curvatura   # fig: transporte paralelo
    ├── Geodesicas.md                             # ẍ^i + Γ^i_jk ẋ^j ẋ^k = 0
    └── (opcional) Ecuaciones de Einstein.md      # G_μν = 8πG T_μν
```

**Libro:** *Física Matemática*, J. Rogan C. y V. Muñoz G., 3ª ed. — Parte I (cap. 1-7).
Cap. 4 basado en *Mathematical Physics* de Kusse & Westwig. PDF en `_private/`.
