---
title: Sílabo de Termodinámica
tags:
  - silabo
  - termodinamica
  - indice
  - estructura
type: index
status: activo
aliases:
  - Estructura Termodinámica
  - Índice Termodinámica
draft: true
---
---

# 📚 Sílabo de Termodinámica

## Estructura del Curso

```
Termodinamica/
├── 1_Primera_Ley/
│   ├── Sistemas_Cerrados/
│   │   ├── Teoria/
│   │   │   ├── Energia_Interna.md
│   │   │   ├── Entalpia.md
│   │   │   └── Calores_Especificos_Gases_Ideales.md
│   │   ├── Procesos/
│   │   │   ├── Isotermico.md
│   │   │   ├── Isobarico.md
│   │   │   ├── Isometrico.md
│   │   │   ├── Adiabatico_Reversible.md
│   │   │   └── Politropico.md
│   │   ├── Demostraciones/
│   │   │   └── Deduccion_Trabajo_Politropico.md
│   │   └── Problemas/
│   │       └── Balance_Energia_Sistemas_Cerrados.md
│   └── Volumenes_de_Control/
│       ├── Teoria/
│       │   ├── Flujo_Estacionario_SSP.md
│       │   ├── Proceso_Estrangulacion.md
│       │   └── Flujo_Transitorio_PT.md
│       ├── Demostraciones/
│       │   └── Balance_Energia_Volumen_Control.md
│       └── Problemas/
│           └── Aplicaciones_Toberas_Difusores.md
│
├── 2_Segunda_Ley/
│   ├── Entropia/
│   │   ├── Teoria/
│   │   │   ├── Desigualdad_Clausius.md
│   │   │   ├── Principio_Incremento_Entropia.md
│   │   │   └── Diagramas_T-s_h-s_P-h.md
│   │   ├── Calculo_Cambio_Entropia/
│   │   │   ├── Sustancias_Puras.md
│   │   │   └── Gases_Ideales.md
│   │   └── Problemas/
│   │       └── Generacion_Entropia_Procesos.md
│   ├── Exergia_Irreversibilidad/
│   │   ├── Teoria/
│   │   │   ├── Exergia_Sistema_Cerrado.md
│   │   │   ├── Exergia_Flujo_Estacionario.md
│   │   │   └── Destruccion_Exergia.md
│   │   ├── Demostraciones/
│   │   │   └── Eficiencia_Segunda_Ley.md
│   │   └── Problemas/
│   │       └── Analisis_Exergetico_Componentes.md
│   └── Maquinas_Termicas_Ciclos_Inversos/
│       ├── Teoria/
│       │   ├── Eficiencia_Termica.md
│       │   ├── Coeficiente_Operacion_COP.md
│       │   └── Bombas_Calor.md
│       └── Problemas/
│           └── Evaluacion_Rendimiento.md
│
├── 3_Sustancia_Pura_Mezclas/
│   ├── Sustancia_Pura/
│   │   ├── Teoria/
│   │   │   ├── Superficie_Termodinamica.md
│   │   │   └── Punto_Triple_Critico.md
│   │   └── Propiedades_Mezcla_Liquido_Vapor/
│   │       ├── Calidad_Vapor.md
│   │       ├── Liquido_Comprimido.md
│   │       └── Vapor_Sobrecalentado.md
│   └── Mezclas/
│       ├── Mezcla_Gases_Ideales/
│       │   ├── Teoria/
│       │   │   ├── Ley_Dalton_Amagat.md
│       │   │   └── Propiedades_Mezcla_Gases.md
│       │   └── Problemas/
│       │       └── Presion_Parcial_Constante_Universo.md
│       ├── Psicrometria/
│       │   ├── Teoria/
│       │   │   ├── Humedad_Absoluta_Relativa.md
│       │   │   └── Temperatura_Bulbo_Humedo_Seco.md
│       │   ├── Procesos/
│       │   │   ├── Calentamiento_Enfriamiento_Sensible.md
│       │   │   ├── Humidificacion_Deshumidificacion.md
│       │   │   └── Torre_Enfriamiento.md
│       │   └── Problemas/
│       │       └── Acondicionamiento_Aire_Carta_Psicrometrica.md
│       └── Gas_Vapor_Condensable/
│           └── Problemas/
│               └── Mezcla_Combustible_Aire_Combustion.md
│
├── 4_Ciclos_Termodinamicos/
│   ├── Ciclos_Potencia_Vapor/
│   │   ├── Ciclo_Rankine/
│   │   │   ├── Teoria/
│   │   │   │   └── Rankine_Basico.md
│   │   │   ├── Modificaciones/
│   │   │   │   ├── Recalentamiento.md
│   │   │   │   ├── Regenerativo_Extraccion_Vapor.md
│   │   │   │   └── Ciclos_Cogeneracion.md
│   │   │   └── Problemas/
│   │   │       └── Eficiencia_Trabajo_Red_Caldera_Condensador.md
│   │   └── Ciclos_Combinados/
│   │       └── Teoria/
│   │           └── Vapor_Gas_Configuracion.md
│   ├── Ciclos_Potencia_Gas/
│   │   ├── Ciclo_Joule_Brayton/
│   │   │   ├── Teoria/
│   │   │   │   └── Brayton_Basico_Modificaciones.md
│   │   │   ├── Aplicaciones/
│   │   │   │   └── Propulsion_Aeronautica.md
│   │   │   └── Problemas/
│   │   │       └── Eficiencia_Relacion_Presiones.md
│   │   └── Motores_Combustion_Interna/
│   │       ├── Ciclo_Otto.md
│   │       ├── Ciclo_Diesel.md
│   │       ├── Ciclo_Dual.md
│   │       └── Eficiencia/
│   │           └── Relacion_Compresion_Calor_Especifico.md
│   ├── Ciclos_Refrigeracion/
│   │   ├── Compresion_Vapor/
│   │   │   ├── Teoria/
│   │   │   │   ├── Diagrama_P-h_Refrigerantes.md
│   │   │   │   ├── Ciclo_Simple.md
│   │   │   │   ├── Ciclo_Multiples_Etapas.md
│   │   │   │   └── Ciclo_Cascada.md
│   │   │   └── Problemas/
│   │   │       └── Analisis_Energia_Camaras_Frigorificas.md
│   │   └── Ciclos_Alternativos/
│   │       ├── Ciclo_Stirling.md
│   │       ├── Ciclo_Atkinson.md
│   │       └── Ciclo_Miller.md
│   └── Parametros_Desempeno_Motores/
│       ├── Teoria/
│       │   ├── Potencia_Teorica_Indicada_Freno.md
│       │   ├── Eficiencia_Mecanica_Volumetrica.md
│       │   └── Consumo_Especifico_Combustible.md
│       └── Problemas/
│           └── Analisis_Motores_Combustion_Alternativos.md
│
└── 5_Gases_Reales_Combustion/
    ├── Gases_Reales/
    │   ├── Teoria/
    │   │   ├── Factor_Compresibilidad_Generalizado.md
    │   │   └── Ecuaciones_Estado_Cubicas.md
    │   └── Problemas/
    │       └── Propiedades_Desviacion_Idealidad.md
    └── Combustion/
        ├── Estequiometria/
        │   └── Relacion_Aire_Combustible.md
        ├── Procesos/
        │   ├── Combustion_Completa_Incompleta.md
        │   └── Temperatura_Adiabatica_Llama.md
        └── Problemas/
            └── Analisis_Productos_Combustion.md
```

---

## 📝 Leyenda

| Símbolo | Significado |
|---------|-------------|
| `📁/` | Carpeta / Directorio |
| `.md` | Archivo Markdown |
| `├──` | Elemento dentro de la jerarquía |
| `└──` | Último elemento del nivel |

---
Chat:
[chat](https://chat.deepseek.com/a/chat/s/01ce516a-15c7-4d8b-b343-bacf0994499a)
