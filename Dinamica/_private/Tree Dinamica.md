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
│   ├── Cinematica/                                  # los sistemas de coordenadas SÍ ramifican
│   │   ├── index.md                                 # r,v,a; cartesianas (versores fijos); panorama de sistemas
│   │   ├── Componentes Intrinsecas.md               # Frenet-Serret 3D: t,n,b; curvatura y TORSIÓN; a=v' t+(v^2/rho) n (sin componente binormal)   # fig: triedro t-n
│   │   ├── Coordenadas Cilindricas.md               # (r,theta,z)=polares+z; v, a; término de Coriolis 2 r' theta'   # fig: polares
│   │   └── Coordenadas Esfericas.md                 # (r,theta,phi); v=r' e_r+r theta' e_theta+r sin(theta) phi' e_phi; a deducida vía base móvil   # fig
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
├── 3 Inercia/                                        # ANTES del cuerpo rígido (prerrequisito); ramifica hondo (material profundo del usuario)
│   ├── index.md
│   ├── Tensor de Inercia.md                         # INTEGRAR ("Tensor de Inercia" 3D + "Inercia/Tensor de Inercia" convenciones); I_ij=int(r^2 delta-r_i r_j)dm; I=Tr(Q)1-Q; productos; UNA convención de signo
│   ├── Ejes Principales de Inercia.md               # problema de autovalores I v=lambda v; diagonalización; significado físico
│   ├── Teorema del Eje Paralelo.md                  # forma tensorial I_O=I_G+m[(d.d)1-d d^T] (con demostración)
│   ├── Momentos de Inercia de Figuras.md            # INTEGRAR ("Clasificacion de Inercia"); tabla varilla/disco/esfera...; masa (dm) vs área (dA); radio de giro
│   └── Deducciones/                                 # tus "Integrales Útiles" — qué produce el tensor, desde primeros principios
│       ├── index.md
│       ├── Deduccion del Momento Angular.md         # INTEGRAR ("Cantidad de Movimiento Angular y Tensor de Inercia"); H=I omega desde int r x v dm
│       ├── Deduccion del Torque.md                  # INTEGRAR ("Torque y Tensor de Inercia"); tau=I alpha+omega x(I omega) desde dtau=r x a dm
│       └── Deduccion de la Energia Cinetica.md      # INTEGRAR ("Energia y Tensor de Inercia"); T=½ omega.I omega
│
├── 4 Cuerpo Rigido/                                 # UNA sola sección: cinemática y cinética juntas (usa la Inercia ya construida)
│   ├── index.md
│   ├── Cinematica Plana.md                          # tipos; rotación eje fijo; velocidad y aceleración relativa; centro instantáneo (CIR); rodadura sin deslizamiento   # fig: CIR, rodadura
│   ├── Cinematica en 3D.md                          # omega vector; v_P=v_G+omega x r, a_P=... (vía el Operador Derivada en Base Movil); ángulos de Euler (opc.)
│   ├── Dinamica Plana 2D.md                         # INTEGRAR (las 3 notas 2D: "Leyes de Newton 2D","Momento Lineal y Angular 2D","Trabajo y Energía 2D"); Newton-Euler, energía, impulso-momento 2D   # fig: DCL
│   ├── Ecuaciones de Euler 3D.md                    # INTEGRAR (las 3D: "Leyes de Newton 3D","Momento Lineal y Angular 3D","Cinetica Angular","Trabajo y Energía 3D"); sum M=I alpha+omega x(I omega), usando Inercia/Deducciones; energía 3D
│   └── Movimiento Giroscopico.md                    # precesión estacionaria; giróscopo; estabilidad de la rotación (eje intermedio)   # fig
│
└── 5 Vibraciones/
    ├── index.md
    ├── Vibracion Libre.md                           # no amortiguada (omega_n) y amortiguada (zeta; sub/crítico/sobre); deducir solución de m x''+c x'+k x=0   # fig
    └── Vibracion Forzada.md                         # excitación armónica; resonancia; factor de amplificación   # fig
```

> **Filosofía del árbol:** ramificar como un árbol real. La **partícula** (4 temas + sistemas) vive en
> UN directorio; el **cuerpo rígido** es UNA sección (no dos) que agrupa cinemática (plana, 3D) y
> cinética (2D, Euler 3D, giróscopo). La **Inercia** va ANTES del cuerpo rígido —es su prerrequisito— y
> ramifica hondo (tensor, ejes principales, eje paralelo, figuras y la subcarpeta `Deducciones/` con tus
> "Integrales Útiles"). Conceptos finos colapsados en una nota (coordenadas; los 3 tipos de vibración).
> Notas `# INTEGRAR` reescriben las viejas al estándar; el tensor de inercia (repetido ~4 veces) queda
> deduplicado, y el basename duplicado `Tensor de Inercia.md` se resuelve en una sola nota. Cada
> resultado se **demuestra** (regla rectora de `Reglas.md`).
