---
title: Tree Ecuaciones
draft: true
---
# Tree

> Árbol del curso **Ecuaciones Diferenciales, Integrales y Difero-integrales**. Tres partes:
> **Diferenciales** (EDO + EDP), **Integrales** y **Difero-integrales**.
>
> **Fuentes:** la parte diferencial sigue *Apuntes de Ecuaciones Diferenciales* de **Mariano
> Echeverría** (`apuntesma1005.pdf`) — es el **modelo de estilo** (pedagógico, ejemplos resueltos,
> campos de direcciones); la parte integral/difero-integral sigue **Krasnov, Kiseliov, Makarenko**,
> *Ecuaciones Integrales* (Mir) para la clasificación Volterra/Fredholm/métodos.
>
> Profundidad **irregular a propósito**: un tema se subdivide solo cuando tiene varios resultados
> independientes. `# fig:` marca figuras planeadas (`_media/img_gen/`). `(opcional)` = posponible.

```tree
Ecuaciones/
│
├── index.md                                      # portada: las 3 familias de ecuaciones
│
├── 1 Ecuaciones Diferenciales Ordinarias/        # EDO — apuntes caps. 1-5
│   ├── index.md
│   │
│   ├── Teoria Elemental/                          # cap. 1
│   │   ├── index.md
│   │   ├── Metodos Analitico Geometrico Cualitativo.md   # campo de direcciones, curvas integrales  # fig: campo de direcciones
│   │   ├── Concepto General de ODE.md            # orden, grado, PVI, solución general/particular
│   │   ├── Existencia y Unicidad.md              # teorema de Picard-Lindelöf; determinismo
│   │   ├── Variables Separables.md               # dy/dx=f(x)/g(y)
│   │   ├── Trayectorias Ortogonales.md           # y'=-1/y'_c  # fig: familia + ortogonales
│   │   ├── Ecuaciones Homogeneas.md              # y'=F(y/x), sustitución v=y/x
│   │   ├── Coeficientes Lineales.md              # (ax+by+c)/(dx+ey+f)
│   │   ├── Ecuaciones Exactas.md                 # M dx+N dy=0, ∂M/∂y=∂N/∂x
│   │   └── Factor Integrante.md                  # μ(x), μ(y) para volver exacta
│   │
│   ├── Lineales/                                  # cap. 2
│   │   ├── index.md
│   │   ├── Lineal Primer Orden.md                # y'+p(x)y=q(x); factor integrante e^∫p
│   │   ├── Segundo Orden/
│   │   │   ├── index.md
│   │   │   ├── Operador Diferencial Lineal.md    # L[y]; linealidad, superposición
│   │   │   ├── Wronskiano e Independencia Lineal.md  # W≠0
│   │   │   ├── Coeficientes Constantes Homogenea.md  # ecuación característica; casos de raíces
│   │   │   └── Reduccion de Orden.md             # segunda solución y_2=y_1∫...
│   │   ├── Orden n Coeficientes Constantes.md    # característica de grado n
│   │   ├── No Homogenea/
│   │   │   ├── index.md
│   │   │   ├── Coeficientes Indeterminados.md    # forma del término fuente; superposición
│   │   │   ├── Variacion de Parametros.md        # y_p=−y_1∫(y_2 g/W)+y_2∫(y_1 g/W)
│   │   │   └── Oscilaciones Forzadas.md          # resonancia, batido  # fig: resonancia
│   │   ├── Cauchy-Euler.md                       # x²y''+axy'+by=0 → x=e^t
│   │   └── Otras ODEs/
│   │       ├── index.md
│   │       ├── Bernoulli.md                      # y'+p y=q y^n → v=y^{1-n}
│   │       ├── Riccati.md                        # y'=p+qy+ry²
│   │       ├── Lagrange.md                       # y=x f(y')+g(y')
│   │       └── Clairaut.md                       # y=x y'+g(y'); solución singular
│   │
│   ├── Sistemas/                                  # cap. 3
│   │   ├── index.md
│   │   ├── Operadores y Eliminacion.md           # reducir sistema a una ODE
│   │   ├── Forma Matricial.md                    # x'=Ax
│   │   ├── Sistemas Homogeneos.md                # autovalores/autovectores de A
│   │   ├── Exponencial de una Matriz.md          # e^{At}, solución x=e^{At}x_0
│   │   ├── Variacion de Parametros Sistemas.md
│   │   └── (opcional) Plano de Fase.md           # nodos, focos, sillas  # fig: retratos de fase
│   │
│   ├── Series/                                    # cap. 4
│   │   ├── index.md
│   │   ├── Puntos Ordinarios.md                  # serie de potencias, recurrencia
│   │   └── Frobenius/                            # puntos singulares regulares
│   │       ├── index.md
│   │       ├── Ecuacion Indicial.md             # exponentes de la singularidad
│   │       ├── Raices Diferencia No Entera.md
│   │       ├── Raices Diferencia Entera.md
│   │       └── Raices Repetidas.md
│   │
│   └── Transformada de Laplace/                   # cap. 5
│       ├── index.md
│       ├── Funciones Generalizadas.md            # delta de Dirac, escalón
│       ├── Definicion Transformada Laplace.md    # F(s)=∫₀^∞ e^{-st}f(t)dt
│       ├── Propiedades Transformada Laplace.md   # tabla: linealidad, derivada, desplazamiento
│       ├── Convolucion.md                        # L{f*g}=F·G; función de transferencia
│       ├── Transformada Inversa.md               # fracciones parciales
│       └── Solucion de ODEs con Laplace.md       # PVI → algebraico → inversa
│
├── 2 Ecuaciones en Derivadas Parciales/          # EDP — apuntes cap. 6
│   ├── index.md
│   ├── Clasificacion EDP.md                      # elíptica/parabólica/hiperbólica
│   ├── Fourier/
│   │   ├── index.md
│   │   ├── Funciones Ortogonales.md              # producto interno, base
│   │   ├── Series de Fourier.md                  # senos y cosenos  # fig: aproximación por armónicos
│   │   └── Convergencia.md                       # Dirichlet, fenómeno de Gibbs
│   ├── Separacion de Variables.md                # técnica general u=X(x)T(t)
│   ├── Ecuacion del Calor/
│   │   ├── index.md
│   │   ├── Derivacion.md                         # difusión, ley de Fourier  # fig: evolución temporal
│   │   ├── Separacion de Variables Calor.md
│   │   ├── Condiciones de Dirichlet.md           # extremos fijos
│   │   └── Condiciones de Neumann.md             # extremos aislados
│   ├── Ecuacion de Laplace/
│   │   ├── index.md
│   │   ├── Derivacion.md                         # estado estacionario, armónicas
│   │   ├── Separacion de Variables Laplace.md
│   │   ├── Problema de Dirichlet.md
│   │   └── Problema de Neumann.md
│   └── Ecuacion de Onda/
│       ├── index.md
│       ├── Derivacion.md                         # cuerda vibrante  # fig: modos normales
│       ├── Separacion de Variables Onda.md
│       ├── Condiciones de Dirichlet.md
│       ├── Condiciones de Neumann.md
│       └── (opcional) Solucion de d'Alembert.md  # u=F(x-ct)+G(x+ct)
│
├── 3 Ecuaciones Integrales/                       # Krasnov
│   ├── index.md                                   # clasificación: Volterra/Fredholm, 1ª/2ª especie, núcleo K(x,t)
│   ├── Conceptos Fundamentales.md                # incógnita bajo la integral; núcleo, especie
│   ├── Volterra/                                  # límite superior variable
│   │   ├── index.md
│   │   ├── Volterra Segunda Especie.md           # φ(x)=f(x)+λ∫₀^x K(x,t)φ(t)dt
│   │   ├── Nexo con ODEs Lineales.md             # PVI ⇄ ecuación integral
│   │   ├── Resolvente.md                         # núcleos iterados, serie de Neumann
│   │   ├── Aproximaciones Sucesivas.md           # iteración de Picard
│   │   ├── Ecuaciones de Convolucion.md          # núcleo K(x-t); resolver con Laplace
│   │   ├── Volterra Primera Especie.md
│   │   ├── Problema de Abel.md                   # núcleo singular 1/√(x-t)
│   │   └── (opcional) Integrales de Euler.md     # función beta/gamma
│   ├── Fredholm/                                  # límites fijos
│   │   ├── index.md
│   │   ├── Fredholm Segunda Especie.md           # φ(x)=f(x)+λ∫_a^b K(x,t)φ(t)dt
│   │   ├── Determinantes de Fredholm.md
│   │   ├── Nucleos Iterados y Resolvente.md
│   │   ├── Nucleo Degenerado.md                  # K=Σa_i(x)b_i(t); Hammerstein
│   │   ├── Raices Caracteristicas y Funciones Propias.md   # autovalores del núcleo
│   │   ├── Ecuaciones Simetricas.md              # Hilbert-Schmidt
│   │   ├── Alternativa de Fredholm.md            # existencia/unicidad
│   │   ├── Funcion de Green/
│   │   │   ├── index.md
│   │   │   ├── Construccion para ODEs.md
│   │   │   └── Aplicacion a Problemas de Frontera.md
│   │   ├── Problemas de Frontera con Parametro.md   # Sturm-Liouville
│   │   └── (opcional) Ecuaciones Integrales Singulares.md
│   ├── Metodos Aproximados/
│   │   ├── index.md
│   │   ├── Sustitucion Nucleo Degenerado.md
│   │   ├── Aproximaciones Sucesivas Numericas.md
│   │   ├── Metodo de Bubnov-Galiorkin.md
│   │   └── Raices Caracteristicas Aproximadas.md   # Ritz, trazas, Kellog
│   └── (opcional) Multivariable.md               # ecuaciones integrales en dominios n-dimensionales (Fredholm multidim)
│
├── 4 Ecuaciones Difero-integrales/                # mezclan derivadas e integrales (Krasnov §6)
│   ├── index.md                                   # qué son; dónde aparecen (viscoelasticidad, control, poblaciones con memoria)
│   ├── Concepto y Clasificacion.md               # φ'(x)=f(x)+∫K(x,t)φ(t)dt
│   ├── Resolucion por Transformada de Laplace.md  # convierte la integro-diferencial en algebraica
│   └── (opcional) Aplicaciones.md                # ecuación de renovación, memoria
│
├── 5 Ejercicios/                                  # problemas resueltos
│   └── (cualquier ejercicio resuelto que quieras guardar)
│
└── 6 Apuntes Clase/                               # opcional: cajón de notas sueltas
    └── (cualquier nota suelta que aún no clasificas)
```

**Fuentes:**
- *Apuntes de Ecuaciones Diferenciales*, **Mariano Echeverría** — modelo de estilo; parte EDO+EDP (`_private/apuntesma1005.pdf`).
- *Ecuaciones Integrales*, **M. Krasnov, A. Kiseliov, G. Makarenko** (Editorial Mir, 1982) — parte integral y difero-integral (`_private/`).
