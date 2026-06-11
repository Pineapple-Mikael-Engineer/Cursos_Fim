---
title: Tree Dinamica
draft: true
---
# Tree

```tree
Dinamica/
│
├── 1 Particula/                                     # toda la mecánica de la partícula, agrupada
│   ├── index.md
│   ├── Cinematica de la Particula.md                # cartesianas + intrínsecas (n-t) + polares/cilíndricas; v, a; a_n=v^2/rho; término 2 r' theta'   # fig: triedro t-n, polares
│   ├── Cinetica de la Particula.md                  # leyes de Newton; ecuaciones de movimiento proyectadas en t-n y polares; fuerzas comunes   # fig: DCL
│   ├── Trabajo y Energia.md                         # U=int F.dr; teorema T-E; conservativas F=-grad V; conservación
│   ├── Impulso y Momento.md                         # impulso-lineal; momento angular H_O=r x mv; conservación; choques + coef. restitución (INTEGRAR "Coeficiente de Restitucion")   # fig
│   └── Sistemas de Particulas.md                    # centro de masa; sum F_ext=m a_G; dH_O/dt=sum M_ext; energía y teorema de König (puente al rígido)
│
├── 2 Movimiento Relativo/                           # sistemas de referencia (Lección 2 del PDF)
│   ├── index.md
│   ├── Marcos en Traslacion.md                      # transformaciones de Galileo; r=R_M+r'; a=a'   # fig: F y M
│   └── Operador Derivada en Base Movil.md           # CLAVE (PDF): Poisson di'/dt=omega x i'; (d/dt)_F=(d/dt)_M+omega x; velocidad de arrastre; Coriolis a=a'+a_M+2 omega x v'+omega x(omega x r')+alpha x r'   # fig: F y M rotando
│
├── 3 Cinematica del Cuerpo Rigido/                  # plano y 3D juntos
│   ├── index.md
│   ├── Movimiento Plano.md                          # tipos; rotación eje fijo; velocidad y aceleración relativa; centro instantáneo (CIR); rodadura sin deslizamiento   # fig: CIR, rodadura
│   └── Movimiento en 3D.md                          # omega vector; v_P=v_G+omega x r, a_P=a_G+alpha x r+omega x(omega x r) (vía el operador); ángulos de Euler (opc.)
│
├── 4 Inercia/                                        # ramifica HONDO (material profundo del usuario)
│   ├── index.md
│   ├── Tensor de Inercia.md                         # INTEGRAR ("Tensor de Inercia" 3D + "Inercia/Tensor de Inercia" convenciones); I_ij=int(r^2 delta-r_i r_j)dm; I=Tr(Q)1-Q; productos; UNA convención de signo
│   ├── Ejes Principales de Inercia.md               # problema de autovalores I v=lambda v; diagonalización; significado físico
│   ├── Teorema del Eje Paralelo.md                  # forma tensorial I_O=I_G+m[(d.d)1-d d^T] (con demostración)
│   ├── Momentos de Inercia de Figuras.md            # INTEGRAR ("Clasificacion de Inercia"); tabla varilla/disco/esfera...; masa (dm) vs área (dA); radio de giro
│   └── Deducciones/                                 # tus "Integrales Útiles" — desde primeros principios
│       ├── index.md
│       ├── Deduccion del Momento Angular.md         # INTEGRAR ("Cantidad de Movimiento Angular y Tensor de Inercia"); H=I omega desde int r x v dm
│       ├── Deduccion del Torque.md                  # INTEGRAR ("Torque y Tensor de Inercia"); tau=I alpha+omega x(I omega) desde dtau=r x a dm
│       └── Deduccion de la Energia Cinetica.md      # INTEGRAR ("Energia y Tensor de Inercia"); T=½ omega.I omega
│
├── 5 Cinetica del Cuerpo Rigido/                    # dinámica del rígido: plano y 3D juntos
│   ├── index.md
│   ├── Dinamica Plana 2D.md                         # INTEGRAR (las 3 notas 2D: "Leyes de Newton 2D","Momento Lineal y Angular 2D","Trabajo y Energía 2D"); Newton-Euler, energía, impulso-momento 2D   # fig: DCL
│   ├── Ecuaciones de Euler 3D.md                    # INTEGRAR (las 3D: "Leyes de Newton 3D","Momento Lineal y Angular 3D","Cinetica Angular","Trabajo y Energía 3D"); sum M=I alpha+omega x(I omega) deducido vía el operador sobre H; energía 3D
│   └── Movimiento Giroscopico.md                    # precesión estacionaria; giróscopo; estabilidad de la rotación (eje intermedio)   # fig
│
└── 6 Vibraciones/
    ├── index.md
    ├── Vibracion Libre.md                           # no amortiguada (omega_n) y amortiguada (zeta; sub/crítico/sobre); deducir solución de m x''+c x'+k x=0   # fig
    └── Vibracion Forzada.md                         # excitación armónica; resonancia; factor de amplificación   # fig
```

> **Filosofía del árbol:** ramificar como un árbol real. Lo de **partícula** (4 temas) vive en UN
> directorio de notas ricas, no 4 directorios; **cinemática** y **cinética** del rígido agrupan 2D+3D;
> los conceptos finos (sistemas de coordenadas, los tres tipos de vibración) se **colapsan** en una
> nota cada uno. En cambio **Inercia** ramifica hondo (tensor, ejes principales, eje paralelo, figuras
> y la subcarpeta `Deducciones/`) porque el material lo merece. Notas marcadas `# INTEGRAR` reescriben
> las notas viejas de `Dinamica/` al estándar; el tensor de inercia (repetido ~4 veces) queda
> deduplicado aquí, y el basename duplicado `Tensor de Inercia.md` se resuelve en una sola nota.
> Cada resultado se **demuestra** (regla rectora de `Reglas.md`).
