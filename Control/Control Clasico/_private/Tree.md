---
draft: "false"
---

# Tree

```tree
Control Clasico/
│
├── 1 Conceptos Fundamentales/              # NUEVO - estaba faltando
│   ├── Lazo Abierto Cerrado.md
│   ├── Sensibilidad.md                     # S = 1/(1+GH)
│   └── Componentes Sistema.md              # planta, actuador, sensor, referencia
│
├── 2 Modelado/                             # ¿Cómo represento el sistema?
│   ├── Dominios Fisicos/
│   │   ├── Mecanico Traslacional.md
│   │   ├── Mecanico Rotacional.md
│   │   ├── Electrico.md
│   │   ├── Fluidos Nivel.md
│   │   ├── Neumatico.md
│   │   └── Termico.md
│   │
│   ├── Transformada Laplace/               # del sílabo semana 2
│   │   ├── Tabla Pares.md                  # δ, u, t^n, e^-at, sen, cos
│   │   ├── Propiedades.md                  # derivación, integración, traslación
│   │   └── Convolucion.md
│   │
│   ├── Funcion Transferencia/              # del sílabo semana 2
│   │   ├── Definicion.md                   # G(s) = Y(s)/U(s)
│   │   ├── Polos Ceros.md
│   │   ├── Orden.md                        # grado del denominador
│   │   ├── Ganancia Estatica.md
│   │   ├── Teorema Valor Inicial Final.md
│   │   └── Algebra Diagramas.md            # serie, paralelo, realimentación
│   │
│   ├── Espacio Estados/                    # del sílabo semana 2
│   │   ├── Forma General.md                # x_dot = Ax + Bu
│   │   ├── Pasar a FT.md
│   │   └── Pasar desde FT.md
│   │
│   └── Linealizacion/                      # del sílabo semana 2
│       ├── Serie Taylor.md
│       └── Variables Desviacion.md
│
├── 3 Analisis/                             # ¿Cómo se comporta?
│   ├── Señales Prueba/                     # NUEVO - del sílabo semana 5 (estaba faltando)
│   │   ├── Escalon.md
│   │   ├── Rampa.md
│   │   ├── Parabola.md
│   │   └── Impulso.md
│   │
│   ├── Respuesta Temporal/                 # del sílabo semana 5
│   │   ├── Primer Orden.md                 # τ, t_s=4τ, t_r=2.2τ
│   │   ├── Segundo Orden/
│   │   │   ├── Formula General.md          # y(t) = 1 - e^-ζωnt/√... sin(ωdt+φ)
│   │   │   ├── Sobrepico Mp.md             # e^(-πζ/√(1-ζ^2))
│   │   │   ├── Tiempo Pico Tp.md           # π/ωd
│   │   │   ├── Tiempo Establecimiento Ts.md # 4/(ζωn) para 2%
│   │   │   └── Tiempo Subida Tr.md         # ≈1.8/ωn
│   │   ├── Orden Superior.md               # polos dominantes
│   │   └── Reduccion Orden.md
│   │
│   ├── Error Estacionario/                 # del sílabo semana 5
│   │   ├── Coeficientes Kp Kv Ka.md
│   │   ├── Tabla Tipos.md                  # tipo 0,1,2 vs escalón/rampa/parábola
│   │   ├── Tipo Sistema.md                
│   │   └── Formula General.md              # e_ss = lim sE(s)
│   │
│   ├── Estabilidad/                        # del sílabo semana 5
│   │   ├── Routh Hurwitz/
│   │   │   ├── Construccion Tabla.md
│   │   │   ├── Casos Especiales.md         # fila de ceros, primera columna cero
│   │   │   └── Ajuste Parametros.md
│   │   └── Condicion Necesaria.md          # todos los coeficientes > 0
│   │
│   └── Respuesta Frecuencial/              # del sílabo semana 9
│       ├── Bode/
│       │   ├── Factores Basicos.md         # K, jω, 1/jω, 1+jω/ω0, 2do orden
│       │   ├── Construccion Asintotica.md
│       │   └── Correcciones.md             # 3dB en esquina, picos resonantes
│       ├── Nyquist/
│       │   ├── Diagrama Polar.md
│       │   ├── Criterio Nyquist.md         # Z = N + P
│       │   └── Margenes MF MG.md           # frecuencia cruce ganancia/fase
│       └── Sistemas Fase Minima.md
│
├── 4 Diseno/                               # ¿Cómo lo modifico para que cumpla specs?
│   ├── Lugar Raices/                       # del sílabo semana 6 y 7
│   │   ├── Condicion Angulo Magnitud.md    # |GH| = 1/K, ∠GH = 180°(2k+1)
│   │   ├── Reglas Construccion.md          # simetría, eje real, asíntotas, etc.
│   │   ├── Puntos Ruptura.md               # dK/ds = 0
│   │   ├── Angulos Salida Llegada.md
│   │   ├── Cruce Eje Imaginario.md         # Routh-Hurwitz
│   │   ├── Lead.md                         # adelanto (mejora transitorio)
│   │   └── Lag.md                          # retardo (mejora error estático)
│   │
│   ├── Respuesta Frecuencia/               # del sílabo semana 12
│   │   ├── Lead.md                         # φm = arcsin((1-α)/(1+α))
│   │   ├── Lag.md                          # atenuación 20logβ
│   │   └── Lead Lag.md
│   │
│   └── Seleccion Metodo.md                 # ¿LGR o Bode? ¿Lead o Lag?
│
├── 5 Controladores/                        # ¿Qué controlador uso?
│   └── PID/                                # del sílabo semana 13 y 14
│       ├── Acciones/
│       │   ├── Proporcional P.md           # reduce error, afecta estabilidad
│       │   ├── Integral I.md               # elimina error, añade -90°
│       │   └── Derivativo D.md             # adelanto, amplifica ruido
│       ├── Configuraciones/
│       │   ├── PI.md                       # lag, mejora error estático
│       │   ├── PD.md                       # lead, mejora transitorio
│       │   └── PID.md                      # lead-lag
│       └── Sintonizacion/
│           ├── Ziegler Nichols Oscilacion.md    # Ku, Tu → tabla
│           └── Ziegler Nichols Curva Reaccion.md # K, L, T → tabla
│
└── 6 Apuntes Clase/                        # opcional: desordenado, para notas rápidas
    └── (cualquier nota suelta que aún no clasificas)
```


chat: [chat1](https://chat.deepseek.com/a/chat/s/b0ede620-65e0-4eb0-95a9-31ed226a6e28)

