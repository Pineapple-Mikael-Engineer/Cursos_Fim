---
title: Tree Ecuaciones
draft: true
---
# Tree

> Árbol del curso **Ecuaciones Diferenciales, Integrales y Difero-integrales**, a **profundidad de
> campo real** (no limitado al contenido de una sola fuente).
>
> **Estilo (no alcance):** *Apuntes de Ecuaciones Diferenciales* de **Mariano Echeverría**
> (`apuntesma1005.pdf`) es el **modelo de cómo explicar** — intuición, ejemplos resueltos paso a
> paso, interpretación geométrica/cualitativa. El **alcance** va mucho más allá de él.
>
> **Fuentes de contenido:** Echeverría (intro EDO/EDP); Krasnov–Kiseliov–Makarenko, *Ecuaciones
> Integrales* (Mir); y la teoría estándar del campo (Coddington–Levinson, Evans/Strauss para EDP,
> Tricomi para integrales, Oldham–Spanier / Podlubny para cálculo fraccionario).
>
> Profundidad **irregular a propósito**. `# fig:` marca figuras planeadas (`_media/img_gen/`).
> `(opcional)` = posponible; `(panorama)` = nota de visión general, no exhaustiva.

```tree
Ecuaciones/
│
├── index.md                                      # portada: las 3 familias y cómo se conectan
│
├── 1 Ecuaciones Diferenciales Ordinarias/        # EDO
│   ├── index.md
│   │
│   ├── Fundamentos y Teoria Cualitativa/
│   │   ├── index.md
│   │   ├── Concepto General de ODE.md            # orden, grado, lineal/no lineal, PVI vs PVF
│   │   ├── Campo de Direcciones e Isoclinas.md   # método geométrico  # fig: campo de direcciones
│   │   ├── Curvas Integrales y Soluciones.md     # general, particular, singular
│   │   ├── Existencia y Unicidad Picard.md       # Lipschitz; Picard-Lindelöf
│   │   ├── Teorema de Peano.md                   # solo continuidad; sin unicidad
│   │   ├── Iteracion de Picard.md                # aproximaciones sucesivas (constructivo)
│   │   ├── Desigualdad de Gronwall.md            # acotación, dependencia continua
│   │   ├── Prolongacion de Soluciones.md         # intervalo maximal, escape
│   │   └── Dependencia de Condiciones y Parametros.md
│   │
│   ├── Metodos de Primer Orden/
│   │   ├── index.md
│   │   ├── Variables Separables.md               # dy/dx=f(x)/g(y)
│   │   ├── Ecuaciones Homogeneas.md              # y'=F(y/x), v=y/x
│   │   ├── Coeficientes Lineales.md              # (ax+by+c)/(dx+ey+f)
│   │   ├── Ecuaciones Exactas.md                 # M dx+N dy=0, ∂M/∂y=∂N/∂x
│   │   ├── Factor Integrante.md                  # μ(x), μ(y)
│   │   ├── Lineal Primer Orden.md                # y'+p y=q; factor integrante e^∫p
│   │   ├── Bernoulli.md                          # y'+p y=q y^n → v=y^{1-n}
│   │   ├── Riccati.md                            # y'=p+qy+ry²; solución particular conocida
│   │   ├── Trayectorias Ortogonales e Isogonales.md   # y'=-1/y'_c  # fig: familia + ortogonales
│   │   └── No Resueltas en y prima/
│   │       ├── index.md
│   │       ├── Lagrange.md                       # y=x f(y')+g(y')
│   │       ├── Clairaut.md                       # y=x y'+g(y')
│   │       └── Solucion Singular y Envolvente.md  # p-discriminante, envolvente de la familia
│   │
│   ├── Lineales de Orden Superior/
│   │   ├── index.md
│   │   ├── Operador Diferencial Lineal.md        # L[y], núcleo, superposición
│   │   ├── Wronskiano e Independencia Lineal.md  # W≠0
│   │   ├── Formula de Abel.md                    # W'=-(p)W; W=W_0 e^{-∫p}
│   │   ├── Coeficientes Constantes Homogenea.md  # ecuación característica; raíces reales/complejas/repetidas
│   │   ├── Orden n Coeficientes Constantes.md
│   │   ├── Reduccion de Orden.md                 # segunda solución conocida una
│   │   ├── Cauchy-Euler.md                       # x²y''+axy'+by=0 → x=e^t
│   │   ├── No Homogenea/
│   │   │   ├── index.md
│   │   │   ├── Coeficientes Indeterminados.md    # forma del fuente; aniquiladores; superposición
│   │   │   └── Variacion de Parametros.md        # y_p vía Wronskiano
│   │   ├── Oscilaciones/                         # aplicación física central
│   │   │   ├── index.md
│   │   │   ├── Oscilador Libre y Amortiguado.md  # sub/crítico/sobreamortiguado  # fig: regímenes
│   │   │   └── Oscilaciones Forzadas y Resonancia.md   # resonancia, batido  # fig: curva de resonancia
│   │   └── Problemas de Frontera EDO/
│   │       ├── index.md
│   │       ├── Condiciones de Frontera.md        # Dirichlet/Neumann/Robin/periódicas
│   │       └── Funcion de Green para EDO.md       # resolver PVF; → ver Herramientas
│   │
│   ├── Sistemas y Dinamica/
│   │   ├── index.md
│   │   ├── Forma Matricial y Eliminacion.md      # x'=Ax; reducir a una ODE
│   │   ├── Matriz Fundamental.md                 # Wronskiano matricial
│   │   ├── Sistemas Lineales Autovalores.md      # reales distintos, complejos, repetidos
│   │   ├── Exponencial de una Matriz.md          # e^{At}; forma de Jordan
│   │   ├── Variacion de Parametros Sistemas.md
│   │   ├── Puntos de Equilibrio y Plano de Fase.md   # nodo, foco, centro, silla  # fig: retratos de fase
│   │   ├── Estabilidad de Lyapunov.md            # linealización; función de Lyapunov
│   │   ├── Linealizacion y Hartman-Grobman.md    # (panorama) cerca de equilibrios
│   │   └── Ciclos Limite y Poincare-Bendixson.md  # (opcional) dinámica no lineal 2D
│   │
│   └── Soluciones por Series/
│       ├── index.md
│       ├── Puntos Ordinarios.md                  # serie de potencias, recurrencia
│       └── Frobenius/                            # puntos singulares regulares
│           ├── index.md
│           ├── Puntos Singulares Regulares.md
│           ├── Ecuacion Indicial.md             # exponentes
│           ├── Raices Diferencia No Entera.md
│           ├── Raices Diferencia Entera.md
│           └── Raices Repetidas.md
│
├── 2 Ecuaciones en Derivadas Parciales/          # EDP — teoría propia profunda
│   ├── index.md
│   │
│   ├── Fundamentos/
│   │   ├── index.md
│   │   ├── Concepto y Notacion EDP.md            # orden, lineal/cuasilineal/no lineal
│   │   ├── Clasificacion Segundo Orden.md        # elíptica/parabólica/hiperbólica; discriminante
│   │   ├── Formas Canonicas.md                   # cambio de variable a forma estándar
│   │   ├── Problemas Bien Planteados.md          # Hadamard: existencia, unicidad, estabilidad
│   │   └── Tipos de Condiciones.md               # Cauchy, Dirichlet, Neumann, Robin
│   │
│   ├── Primer Orden y Caracteristicas/
│   │   ├── index.md
│   │   ├── Metodo de las Caracteristicas.md      # EDP lineal/cuasilineal  # fig: curvas características
│   │   ├── Cuasilineal y No Lineal.md            # Charpit, Lagrange-Charpit
│   │   ├── Leyes de Conservacion.md              # forma integral/diferencial
│   │   └── Ondas de Choque y Burgers.md          # (opcional) Rankine-Hugoniot, rarefacción
│   │
│   ├── Separacion de Variables y Fourier/
│   │   ├── index.md
│   │   ├── Tecnica de Separacion.md              # u=X(x)T(t); problema de autovalores asociado
│   │   ├── Funciones Ortogonales.md              # producto interno, base; → Sturm-Liouville
│   │   ├── Series de Fourier.md                  # senos/cosenos/completa  # fig: armónicos
│   │   ├── Convergencia y Gibbs.md               # Dirichlet, fenómeno de Gibbs
│   │   ├── Identidad de Parseval.md              # energía, completitud
│   │   └── Desarrollo en Autofunciones.md        # generaliza Fourier (Bessel, Legendre)
│   │
│   ├── Ecuacion del Calor/                        # parabólica
│   │   ├── index.md
│   │   ├── Derivacion del Calor.md               # difusión, ley de Fourier  # fig: evolución temporal
│   │   ├── Separacion Calor Dirichlet.md         # extremos fijos
│   │   ├── Separacion Calor Neumann.md           # extremos aislados
│   │   ├── Calor en Dominio Infinito.md          # transformada de Fourier; solución fundamental (núcleo de calor)
│   │   ├── Principio del Maximo Parabolico.md
│   │   └── Metodo de Energia Unicidad.md
│   │
│   ├── Ecuacion de Onda/                          # hiperbólica
│   │   ├── index.md
│   │   ├── Derivacion de Onda.md                 # cuerda/membrana vibrante  # fig: modos normales
│   │   ├── Separacion Onda y Modos Normales.md
│   │   ├── Solucion de dAlembert.md              # u=F(x-ct)+G(x+ct); dominio de dependencia  # fig: cono de dependencia
│   │   ├── Ondas en 2D y 3D.md                   # Huygens; Kirchhoff/Poisson
│   │   └── Energia de la Onda.md                 # conservación, unicidad
│   │
│   ├── Ecuacion de Laplace y Poisson/             # elíptica
│   │   ├── index.md
│   │   ├── Funciones Armonicas.md                # propiedades, valor medio
│   │   ├── Laplace en Rectangulo.md              # separación cartesiana, Dirichlet/Neumann
│   │   ├── Laplace en Disco.md                   # polares; fórmula integral de Poisson  # fig: núcleo de Poisson
│   │   ├── Laplace en Cilindro.md                # → funciones de Bessel
│   │   ├── Laplace en Esfera.md                  # → Legendre, armónicos esféricos
│   │   ├── Principio del Maximo Eliptico.md
│   │   └── Teorema del Valor Medio.md
│   │
│   ├── Funciones de Green para EDP/
│   │   ├── index.md
│   │   ├── Solucion Fundamental.md               # del Laplaciano, calor, onda
│   │   ├── Funcion de Green y Condiciones.md
│   │   └── Metodo de las Imagenes.md             # fig: cargas imagen
│   │
│   └── Teoria Avanzada/                           # (panorama) hacia el análisis moderno
│       ├── index.md
│       ├── Distribuciones y Soluciones Debiles.md  # (panorama) funciones generalizadas en EDP
│       ├── Espacios de Sobolev.md               # (panorama) formulación variacional
│       └── EDP No Lineales.md                    # (panorama) ejemplos: KdV, reacción-difusión
│
├── 3 Ecuaciones Integrales/                       # Krasnov + teoría estándar
│   ├── index.md                                   # clasificación: Volterra/Fredholm, 1ª/2ª especie, núcleo K(x,t)
│   ├── Conceptos Fundamentales.md                # incógnita bajo la integral; especie; homogénea
│   ├── Nexo EDO e Integrales.md                  # PVI/PVF ⇄ ecuación integral
│   │
│   ├── Volterra/                                  # límite superior variable
│   │   ├── index.md
│   │   ├── Volterra Segunda Especie.md           # φ=f+λ∫₀^x K φ
│   │   ├── Resolvente y Nucleos Iterados.md      # serie de Neumann
│   │   ├── Aproximaciones Sucesivas.md           # iteración de Picard
│   │   ├── Ecuaciones de Convolucion.md          # K(x-t); resolver con Laplace
│   │   ├── Volterra Primera Especie.md
│   │   ├── Problema de Abel.md                   # núcleo singular 1/√(x-t)
│   │   └── (opcional) Integrales de Euler.md     # beta/gamma como herramienta
│   │
│   ├── Fredholm/                                  # límites fijos
│   │   ├── index.md
│   │   ├── Fredholm Segunda Especie.md           # φ=f+λ∫_a^b K φ
│   │   ├── Fredholm Primera Especie y Problemas Mal Planteados.md  # mal planteado; regularización de Tikhonov
│   │   ├── Nucleo Degenerado.md                  # K=Σa_i(x)b_i(t) → sistema lineal
│   │   ├── Determinantes de Fredholm.md          # D(λ), menores
│   │   ├── Nucleos Iterados y Resolvente.md
│   │   ├── Raices Caracteristicas y Funciones Propias.md   # autovalores del núcleo
│   │   ├── Alternativa de Fredholm.md            # existencia/unicidad; homogénea adjunta
│   │   ├── Nucleos Simetricos/                   # teoría espectral
│   │   │   ├── index.md
│   │   │   ├── Teoria de Hilbert-Schmidt.md      # autovalores reales, autofunciones ortogonales
│   │   │   ├── Teorema de Mercer.md              # desarrollo del núcleo en autofunciones
│   │   │   └── Ecuaciones Simetricas No Homogeneas.md   # solución por desarrollo en autofunciones
│   │   └── Reduccion de Problemas de Frontera.md  # PVF (Sturm-Liouville) → ecuación integral vía función de Green
│   │
│   ├── No Lineales/                               # la incógnita entra de forma no lineal
│   │   ├── index.md
│   │   ├── Ecuacion de Hammerstein.md            # f(x)+λ∫K(x,t)g(t,φ(t))dt
│   │   └── Ecuacion de Urysohn.md                # núcleo no lineal general K(x,t,φ)
│   │
│   ├── Singulares/                                # núcleos no integrables / dominio infinito
│   │   ├── index.md
│   │   ├── Ecuacion de Abel Generalizada.md
│   │   ├── Nucleo de Cauchy y Riemann-Hilbert.md  # (panorama)
│   │   └── Metodo de Wiener-Hopf.md              # (panorama) factorización
│   │
│   ├── Metodos Aproximados/
│   │   ├── index.md
│   │   ├── Sustitucion Nucleo Degenerado.md
│   │   ├── Aproximaciones Sucesivas Numericas.md
│   │   ├── Metodo de Bubnov-Galiorkin.md
│   │   ├── Metodo de Colocacion.md               # imponer la ecuación en puntos discretos
│   │   ├── Cuadratura y Nystrom.md               # discretizar la integral
│   │   └── Raices Caracteristicas Aproximadas.md   # Ritz, trazas, Kellog
│   │
│   └── (opcional) Multivariable y Fisica.md      # Fredholm en dominios n-dim; teoría de potencial, dispersión
│
├── 4 Ecuaciones Difero-integrales/                # DOS campos: integro-diferenciales + cálculo fraccionario
│   ├── index.md                                   # qué une derivar e integrar; las dos ramas y su relación
│   │
│   ├── Integro-Diferenciales/                     # derivada E integral de la incógnita (Krasnov §6)
│   │   ├── index.md
│   │   ├── Concepto y Clasificacion.md           # φ'(x)=f+∫K φ; Volterra vs Fredholm integro-dif.
│   │   ├── Resolucion por Transformada de Laplace.md   # convierte en algebraica
│   │   ├── Reduccion a Sistemas.md               # a EDO/ecuación integral equivalente
│   │   ├── Ecuaciones con Memoria.md             # ecuación de renovación, núcleo de memoria
│   │   └── Aplicaciones Integro-Diferenciales.md  # viscoelasticidad, poblaciones con retardo, transporte (panorama)
│   │
│   └── Calculo Fraccionario/                      # el *differintegral* D^q de orden arbitrario
│       ├── index.md                               # idea: derivar/integrar como un continuo de órdenes
│       ├── Operador Differintegral.md            # D^q unifica d^n/dx^n e integrales repetidas  # fig: orden continuo
│       ├── Integral de Riemann-Liouville.md      # integral fraccionaria; fórmula de Cauchy iterada
│       ├── Derivada de Riemann-Liouville.md
│       ├── Derivada de Caputo.md                 # condiciones iniciales "físicas"
│       ├── Derivada de Grunwald-Letnikov.md      # límite de diferencias; base numérica
│       ├── Funcion de Mittag-Leffler.md          # la "exponencial" fraccionaria  # fig: E_α(x) vs exp
│       ├── Laplace de Derivadas Fraccionarias.md
│       ├── Ecuaciones Diferenciales Fraccionarias.md   # EDF lineales; solución por Laplace/Mittag-Leffler
│       └── Aplicaciones Fraccionarias.md         # viscoelasticidad, difusión anómala, memoria (panorama)
│
├── 5 Herramientas Transversales/                  # usadas por EDO, EDP e integrales — no duplicar
│   ├── index.md
│   │
│   ├── Transformada de Laplace/
│   │   ├── index.md
│   │   ├── Funciones Generalizadas.md            # delta de Dirac, escalón de Heaviside
│   │   ├── Definicion y Existencia.md            # F(s)=∫₀^∞ e^{-st}f dt; orden exponencial
│   │   ├── Propiedades Laplace.md                # tabla: linealidad, derivada, desplazamiento, escalado
│   │   ├── Convolucion Laplace.md                # L{f*g}=F·G; función de transferencia
│   │   ├── Transformada Inversa.md               # fracciones parciales; (panorama) Bromwich
│   │   └── Solucion de EDO con Laplace.md        # PVI/sistemas → algebraico → inversa
│   │
│   ├── Analisis de Fourier/
│   │   ├── index.md
│   │   ├── Transformada de Fourier.md            # dominios infinitos; pares de transformadas
│   │   └── (panorama) Hankel y Mellin.md         # simetría cilíndrica / escala
│   │
│   ├── Sturm-Liouville/                           # corazón de la separación de variables
│   │   ├── index.md
│   │   ├── Problema Regular de Sturm-Liouville.md  # forma autoadjunta (p y')'+(q+λw)y=0
│   │   ├── Autovalores y Autofunciones.md        # reales, ortogonalidad respecto al peso w
│   │   ├── Completitud y Desarrollo.md           # base para series de autofunciones
│   │   └── (opcional) Sturm-Liouville Singular.md  # Bessel/Legendre como casos
│   │
│   ├── Funciones Especiales/                      # nacen de series (EDO) y separación (EDP)
│   │   ├── index.md
│   │   ├── Gamma y Beta.md                        # base de lo fraccionario y de Euler
│   │   ├── Funciones de Bessel.md                # cilíndricas  # fig: J_n(x)
│   │   ├── Polinomios de Legendre.md             # esféricas  # fig: P_n(x)
│   │   ├── Armonicos Esfericos.md                # Y_l^m; Laplace en la esfera
│   │   └── (opcional) Hermite Laguerre Chebyshev.md  # ortogonales clásicos (panorama)
│   │
│   └── Funcion de Green/                          # inversa de un operador diferencial
│       ├── index.md
│       ├── Green para Operadores Lineales.md     # idea general; L G=δ
│       └── Construccion y Propiedades.md         # continuidad y salto de la derivada
│
├── 6 Ejercicios/                                  # problemas resueltos al estilo Echeverría
│   └── (cualquier ejercicio resuelto que quieras guardar)
│
└── 7 Apuntes Clase/                               # opcional: cajón de notas sueltas
    └── (cualquier nota suelta que aún no clasificas)
```

**Fuentes:**
- *Apuntes de Ecuaciones Diferenciales*, **Mariano Echeverría** — **modelo de estilo** (`_private/apuntesma1005.pdf`).
- *Ecuaciones Integrales*, **M. Krasnov, A. Kiseliov, G. Makarenko** (Mir, 1982) — parte integral y difero-integral (`_private/`).
- Teoría estándar del campo para la profundidad: Coddington–Levinson (EDO), Strauss/Evans (EDP),
  Tricomi (integrales), Oldham–Spanier / Podlubny (cálculo fraccionario).
