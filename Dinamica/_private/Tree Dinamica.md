---
title: Tree Dinamica
draft: true
---
# Tree

```tree
Dinamica/
│
├── 1 Cinematica de la Particula/
│   ├── index.md
│   ├── Posicion Velocidad Aceleracion.md            # r, v=dr/dt, a=dv/dt
│   ├── Coordenadas Cartesianas.md
│   ├── Coordenadas Intrinsecas.md                   # tangencial-normal; a_t, a_n=v^2/rho; radio de curvatura   # fig: triedro t-n
│   ├── Coordenadas Polares y Cilindricas.md         # v_r, v_theta; a con termino de Coriolis 2 r' theta'      # fig
│   ├── Coordenadas Esfericas.md                     # (opcional)
│   ├── Movimiento Relativo Traslacion.md            # marcos en traslacion: r_A = r_B + r_{A/B}
│   └── Movimiento Dependiente.md                    # (opcional) poleas, restricciones de cuerda
│
├── 2 Cinetica de la Particula/
│   ├── index.md
│   ├── Leyes de Newton.md                           # marco inercial; sum F = m a; 1a/2a/3a ley
│   ├── Ecuaciones de Movimiento.md                  # proyeccion en t-n y en polares
│   └── Fuerzas Comunes.md                           # (opcional) peso, normal, friccion, resorte, tension
│
├── 3 Trabajo y Energia Particula/
│   ├── index.md
│   ├── Trabajo de una Fuerza.md                     # U = int F . dr
│   ├── Teorema Trabajo Energia.md                   # T2 - T1 = U_{1->2}
│   ├── Fuerzas Conservativas y Potencial.md         # F = -grad V; gravitatorio, elastico
│   └── Conservacion de la Energia.md                # T + V = cte
│
├── 4 Impulso y Momento Particula/
│   ├── index.md
│   ├── Impulso y Cantidad de Movimiento Lineal.md   # int F dt = Delta(m v)
│   ├── Momento Angular de una Particula.md          # H_O = r x m v; dH_O/dt = M_O
│   ├── Conservacion del Momento.md                  # lineal y angular
│   └── Choques y Coeficiente de Restitucion.md      # INTEGRAR (vieja "Coeficiente de Restitucion"); e=(v'_2-v'_1)/(v_1-v_2)   # fig
│
├── 5 Sistemas de Particulas/
│   ├── index.md
│   ├── Centro de Masa.md                            # r_G = (1/m) sum m_i r_i
│   ├── Momento Lineal del Sistema.md                # sum F_ext = m a_G
│   ├── Momento Angular del Sistema.md               # dH_O/dt = sum M_ext; fuerzas internas se cancelan
│   └── Energia de un Sistema.md                     # T total; teorema de Konig
│
├── 6 Cinematica del Cuerpo Rigido Plano/
│   ├── index.md
│   ├── Tipos de Movimiento Plano.md                 # traslacion, rotacion eje fijo, movimiento general
│   ├── Rotacion Alrededor de Eje Fijo.md            # v = omega x r; a = alpha x r - omega^2 r
│   ├── Velocidad Relativa.md                        # v_A = v_B + omega x r_{A/B}        # fig
│   ├── Centro Instantaneo de Rotacion.md            # CIR                                # fig
│   ├── Aceleracion Relativa.md                      # a_A = a_B + alpha x r - omega^2 r
│   └── Rodadura sin Deslizamiento.md                # v_contacto = 0; a_G = alpha R
│
├── 7 Cinetica del Cuerpo Rigido Plano/
│   ├── index.md
│   ├── Momento de Inercia de Masa.md                # I = int r^2 dm (escalar 2D); radio de giro
│   ├── Ecuaciones de Newton Euler 2D.md             # INTEGRAR (vieja "Leyes de Newton 2D"); sum F=m a_G, sum M_G=I_G alpha   # fig: DCL
│   ├── Momento respecto a Punto Arbitrario.md       # sum M_O = I_G alpha + m (r_{G/O} x a_G)
│   ├── Trabajo y Energia 2D.md                      # INTEGRAR (vieja "Trabajo y Energía 2D"); T=½ m v_G^2+½ I_G omega^2
│   └── Impulso y Momento 2D.md                      # INTEGRAR (vieja "Momento Lineal y Angular 2D")
│
├── 8 Cinematica del Cuerpo Rigido 3D/
│   ├── index.md
│   ├── Velocidad Angular en 3D.md                   # vector omega; composicion de rotaciones
│   ├── Velocidad y Aceleracion de Puntos.md         # v_P=v_G+omega x r; a_P=a_G+alpha x r+omega x(omega x r)
│   ├── Derivada en Marco Rotante.md                 # teorema del transporte: (d/dt)_fijo = (d/dt)_rel + omega x
│   ├── Movimiento con Marco Rotante.md              # Coriolis: a_abs = a_rel + 2 omega x v_rel + ...   # fig
│   └── Angulos de Euler.md                          # (opcional) precesion-nutacion-spin
│
├── 9 Inercia/
│   ├── index.md
│   ├── Tensor de Inercia.md                         # INTEGRAR (vieja "Tensor de Inercia" 3D); I_ij=int(r^2 delta_ij - r_i r_j)dm; I=Tr(Q)1-Q
│   ├── Convenciones de Signo.md                     # INTEGRAR (vieja "Inercia/Tensor de Inercia"); componente vs producto P_xy=∫xy dm
│   ├── Ejes Principales de Inercia.md               # problema de autovalores I v = lambda v; matriz diagonal
│   ├── Teorema del Eje Paralelo Tensorial.md        # I_O = I_G + m[(d.d)1 - d d^T]
│   ├── Momentos de Inercia de Figuras.md            # INTEGRAR (de "Clasificacion de Inercia"); tabla varilla/disco/esfera...
│   ├── Inercia de Masa vs Area.md                   # INTEGRAR (de "Clasificacion de Inercia"); dm vs dA, momento polar
│   └── Deducciones/                                 # las "Integrales Utiles" del usuario (primeros principios)
│       ├── index.md
│       ├── Deduccion del Momento Angular.md         # INTEGRAR ("Cantidad de Movimiento Angular y Tensor de Inercia")
│       ├── Deduccion del Torque.md                  # INTEGRAR ("Torque y Tensor de Inercia"); tau=I alpha+omega x(I omega)
│       └── Deduccion de la Energia Cinetica.md      # INTEGRAR ("Energia y Tensor de Inercia"); T=½ omega.I omega
│
├── 10 Cinetica del Cuerpo Rigido 3D/
│   ├── index.md
│   ├── Momento Angular 3D.md                        # INTEGRAR ("Momento Lineal y Angular 3D","Cinetica Angular"); H=I omega; H_O=H_G+m r x v_G
│   ├── Ecuaciones de Euler.md                       # INTEGRAR ("Leyes de Newton 3D"); sum M=I alpha+omega x(I omega); forma en ejes ppales
│   ├── Energia Cinetica 3D.md                       # INTEGRAR ("Trabajo y Energía 3D"); T=½ m v_G^2+½ omega.I_G omega
│   ├── Movimiento Giroscopico.md                    # precesion estacionaria; giroscopo                  # fig
│   └── Cuerpo Libre de Torque.md                    # (opcional) estabilidad de la rotacion, ejes intermedios
│
├── 11 Vibraciones/
│   ├── index.md
│   ├── Vibracion Libre No Amortiguada.md            # m x'' + k x = 0; omega_n=sqrt(k/m)                 # fig
│   ├── Vibracion Libre Amortiguada.md               # zeta; sub/critico/sobre-amortiguado                # fig
│   ├── Vibracion Forzada y Resonancia.md            # excitacion armonica; factor de amplificacion       # fig
│   └── Vibracion Torsional y Pendulos.md            # (opcional) pendulo fisico, eje torsional
│
└── 12 Apuntes Clase/                                # opcional: cajon de notas sueltas sin clasificar
    └── (notas rapidas aun sin ubicar)
```

> Notas viejas marcadas `# INTEGRAR` están en `Dinamica/` (estilo con emojis, sin estándar) y se
> reescriben a su nota destino. El tensor de inercia, que las notas viejas redefinían ~4 veces, queda
> deduplicado en `9 Inercia/`. Las "Integrales Útiles" (deducciones desde primeros principios) van en
> `9 Inercia/Deducciones/`. El basename duplicado `Tensor de Inercia.md` se resuelve: el de definición
> queda como `Tensor de Inercia.md` y el de convenciones como `Convenciones de Signo.md`.
