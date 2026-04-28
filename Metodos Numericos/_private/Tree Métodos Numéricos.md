---
title: Tree Métodos Numéricos
draft: true
---
# Tree 

```tree 

Metodos Numericos Teoria/
├── 1 Teoria Errores Analisis Estabilidad/
│   ├── Representacion Punto Flotante IEEE 754.md
│   ├── Epsilon Maquina y Precision Relativa.md
│   ├── Perdida Significancia y Cancelacion Catastrofica.md
│   ├── Condicionamiento Numerico Numero Condicion.md
│   ├── Estabilidad Algoritmos Forward Backward.md
│   └── Propagacion Errores Operaciones Matriciales.md
│
├── 2 Sistemas Ecuaciones Lineales/
│   ├── Metodos Directos/
│   │   ├── Eliminacion Gaussiana/
│   │   │   ├── Pivoteo Parcial Total Estabilidad.md
│   │   │   ├── Conteo Operaciones Complejidad O n3.md
│   │   │   └── Acumulacion Error Redondeo Gauss.md
│   │   ├── Factorizacion LU/
│   │   │   ├── Existencia Unicidad LU Matrices No Singulares.md
│   │   │   ├── Variantes Doolittle Crout Cholesky.md
│   │   │   ├── Factorizacion Cholesky Matrices Definidas Positivas.md
│   │   │   └── Costo Computacional vs Eliminacion Gaussiana.md
│   │   └── Analisis Error Directos/
│   │       ├── Residuo vs Error Relativo Solucion.md
│   │       └── Sensibilidad Solucion Numero Condicion.md
│   │
│   ├── Metodos Iterativos/
│   │   ├── Fundamentos Iteracion Punto Fijo Lineal.md
│   │   ├── Jacobi.md
│   │   ├── Gauss Seidel.md
│   │   └── Convergencia Iterativos/
│   │       ├── Teorema Diagonal Dominante Estricta.md
│   │       ├── Criterio Radio Espectral Convergencia.md
│   │       └── Estimacion Error y Cotas A Priori.md
│   │
│   └── Valores Vectores Propios/
│       ├── Metodo Potencia Directo/
│       │   ├── Fundamentos Valor Propio Dominante.md
│       │   ├── Velocidad Convergencia Razon Lambda2 Lambda1.md
│       │   ├── Calculo Constante Normalizacion Rayleigh.md
│       │   └── (opcional) Caso Simetrico Convergencia Acelerada.md
│       ├── Variantes Metodo Potencia/
│       │    ├── Potencia Inversa Valor Propio Menor Modulo.md
│       │    ├── Potencia Desplazada Aceleracion Convergencia.md
│       │    └── (opcional) Potencia Subespacio Iteracion Simultanea.md
│       └── (opcional) Metodo QR/ 
│            ├── Fundamentos Transformaciones Householder.md
│            ├── Iteracion QR Descomposicion.md
│            └── Convergencia y Desplazamientos.md
│
├── 3 Ecuaciones No Lineales/
│   ├── Localizacion Raices/
│   │   ├── Teorema Bolzano y Existencia Intervalo.md
│   │   ├── Metodo Grafico Analisis Cualitativo.md
│   │   └── Separacion Raices Reales Multiplicidad.md
│   │
│   ├── Metodos Cerrados Una Variable/
│   │   ├── Biseccion/
│   │   │   ├── Algoritmo y Teorema Convergencia.md
│   │   │   ├── Orden Convergencia Lineal Cota Error.md
│   │   │   └── Ventaja Robustez vs Lentitud.md
│   │   └── Regula Falsi/
│   │       ├── Convergencia Unilateral y Estancamiento.md
│   │       └── Modificaciones Illinois Pegasus.md
│   │
│   ├── Metodos Abiertos Una Variable/
│   │   ├── Punto Fijo Aproximaciones Sucesivas/
│   │   │   ├── Teorema Punto Fijo Banach Contraccion.md
│   │   │   ├── Funcion Iteracion g x y Convergencia Local.md
│   │   │   └── Orden Convergencia Lineal Constante Asintotica.md
│   │   ├── Newton Raphson/
│   │   │   ├── Derivacion Geometrica y Serie Taylor.md
│   │   │   ├── Orden Convergencia Cuadratica Simple.md
│   │   │   ├── Convergencia Lineal Raices Multiples.md
│   │   │   ├── Criterios Fallo Divergencia Oscilacion.md
│   │   │   └── Metodo Secante Orden Convergencia Fi.md
│   │   └── Comparacion Analitica Orden Convergencia.md
│   │
│   └── Sistemas Ecuaciones No Lineales/
│       ├── Newton Raphson Multivariable/
│       │   ├── Matriz Jacobiana y Sistema Lineal Asociado.md
│       │   ├── Convergencia Local Cuadratica.md
│       │   └── Costo Computacional Evaluacion Jacobiano.md
│       └── Aproximaciones Sucesivas Multivariable/
│           └── Condicion Contraccion Norma Matricial.md
│
├── 4 Aproximacion Funciones/
│   ├── Interpolacion Polinomica/
│   │   ├── Existencia Unicidad Polinomio Interpolador.md
│   │   ├── Matriz Vandermonde Mal Condicionamiento.md
│   │   ├── Lagrange/
│   │   │   ├── Formulacion Polinomios Cardinales L i x.md
│   │   │   └── Costo Computacional Evaluacion Directa.md
│   │   ├── Newton Diferencias Divididas/
│   │   │   ├── Tabla Diferencias Divididas y Coeficientes.md
│   │   │   ├── Forma Anidada y Eficiencia Algoritmo Horner.md
│   │   │   ├── Relacion Diferencias Divididas Derivadas.md
│   │   │   └── Error Interpolacion Formula Cauchy.md
│   │   └── Fenomeno Runge y Nodos Chebyshev.md
│   │
│   ├── Interpolacion Tramos Splines/
│   │   ├── Splines Lineales Continuidad C0.md
│   │   ├── Splines Cubicos Naturales Sujetos.md
│   │   ├── Condiciones Continuidad C2 y Sistema Tridiagonal.md
│   │   ├── Propiedad Minima Curvatura.md
│   │   └── Convergencia y Estabilidad vs Polinomios Grado Alto.md
│   │
│   └── Ajuste Minimos Cuadrados/
│       ├── Formulacion Residuos y Norma Euclidea.md
│       ├── Ecuaciones Normales y Matriz Gram.md
│       ├── Condicionamiento Ecuaciones Normales.md
│       └── Regresion Lineal Multiple y Polinomial.md
│
├── 5 Diferenciacion Integracion Numerica/
│   ├── Diferenciacion Numerica/
│   │   ├── Aproximacion Diferencias Finitas Serie Taylor.md
│   │   ├── Orden Error Progresiva Regresiva Centrada.md
│   │   ├── Extrapolacion Richardson Aceleracion Convergencia.md
│   │   └── Inestabilidad Error Redondeo Paso h.md
│   │
│   ├── Integracion Numerica Newton Cotes/
│   │   ├── Formulacion General Pesos Newton Cotes.md
│   │   ├── Reglas Cerradas/
│   │   │   ├── Trapecio Error Truncamiento Segunda Derivada.md
│   │   │   ├── Simpson 1 3 Orden Precision y Error Cuarta Derivada.md
│   │   │   ├── Simpson 3 8 y Reglas Grado Superior.md
│   │   │   └── Inestabilidad Pesos Negativos Grado Alto.md
│   │   └── Metodos Compuestos/
│   │       ├── Trapecio Compuesto Convergencia O h2.md
│   │       └── Simpson Compuesto Convergencia O h4.md
│   │
│   └── Cuadratura Gaussiana/
│       ├── Fundamentos Gauss Legendre Polinomios Ortogonales.md
│       ├── Determinacion Nodos y Pesos Optimos.md
│       ├── Grado Exactitud Polinomica 2n 1.md
│       ├── Comparacion Eficiencia vs Newton Cotes.md
│       └── Cambio Variable Intervalo General.md
│
└── 6 Ecuaciones Diferenciales Ordinarias/
    ├── Problema Valor Inicial PVI/
    │   ├── Teoremas Existencia Unicidad Picard Lindelof.md
    │   ├── Metodos Taylor Euler/
    │   │   ├── Euler Explicito Orden 1 Interpretacion Geometrica.md
    │   │   ├── Error Local Truncamiento vs Error Global Acumulado.md
    │   │   ├── Euler Implicito Estabilidad Incondicional.md
    │   │   └── Metodos Serie Taylor Orden Superior.md
    │   ├── Metodos Runge Kutta/
    │   │   ├── Construccion General Etapas s y Orden p.md
    │   │   ├── RK2 Heun Euler Modificado Punto Medio.md
    │   │   ├── RK4 Clasico Tabla Butcher y Orden Cuatro.md
    │   │   ├── Control Paso Adaptativo RK45 Dormand Prince.md
    │   │   └── Regiones Estabilidad Absoluta A Estabilidad.md
    │   └── Sistemas EDO y Orden Superior/
    │       ├── Reduccion EDO Orden n a Sistema Primer Orden.md
    │       ├── Acoplamiento Metodos Sistemas Runge Kutta.md
    │       └── Rigidez Stiffness Problemas Ingenieria.md
    │
    └── Problema Valor Frontera PVF/
        ├── Metodo Diferencias Finitas/
        │   ├── Discretizacion Dominio y Aproximacion Centrada.md
        │   ├── Construccion Sistema Tridiagonal Lineal.md
        │   ├── Consistencia Estabilidad Convergencia Lax.md
        │   └── Tratamiento Condiciones Frontera Dirichlet Neumann.md
        └── Metodo Disparo Shooting/
            ├── Transformacion PVF a PVI Valor Inicial Desconocido.md
            ├── Metodo Newton para Condicion Frontera Residual.md
            └── Comparacion Disparo vs Diferencias Finitas.md
            
```


**Chat:** [chat](https://chat.deepseek.com/a/chat/s/8876a460-8b8a-432d-b853-575bb01c118c)



## Promt

```
Estoy construyendo un directorio de notas en Obsidian para el curso universitario de Métodos Numéricos (MB536). El objetivo es crear notas de teoría matemática rigurosa, estilo universitario, autocontenidas en su núcleo pero que delegan desarrollos profundos a notas hijas mediante wikilinks.

## ÁRBOL DE DIRECTORIOS (lo creado hasta ahora)

Metodos Numericos Teoria/
├── 1 Teoria Errores Analisis Estabilidad/
│   ├── Representacion Punto Flotante IEEE 754.md ✅
│   ├── Epsilon Maquina y Precision Relativa.md ✅
│   ├── Perdida Significancia y Cancelacion Catastrofica.md ✅
│   ├── Condicionamiento Numerico Numero Condicion.md ✅
│   ├── Estabilidad Algoritmos Forward Backward.md ⏳
│   └── Propagacion Errores Operaciones Matriciales.md ⏳
│
├── 2 Sistemas Ecuaciones Lineales/
│   ├── Metodos Directos/
│   │   ├── Eliminacion Gaussiana/
│   │   │   ├── index.md ✅
│   │   │   ├── Pivoteo Parcial Total Estabilidad.md ✅
│   │   │   ├── Conteo Operaciones Complejidad O n3.md ✅
│   │   │   └── Acumulacion Error Redondeo Gauss.md ✅
│   │   ├── Factorizacion LU/
│   │   │   ├── index.md ✅
│   │   │   ├── Existencia Unicidad LU Matrices No Singulares.md ✅
│   │   │   ├── Variantes Doolittle Crout Cholesky.md ✅
│   │   │   ├── Factorizacion Cholesky Matrices Definidas Positivas.md ✅
│   │   │   └── Costo Computacional vs Eliminacion Gaussiana.md ✅
│   │   └── Analisis Error Directos/ ⏳
│   │
│   ├── Metodos Iterativos/
│   │   ├── index.md ✅
│   │   ├── Fundamentos Iteracion Punto Fijo Lineal.md ⏳ ← PRÓXIMA
│   │   ├── Jacobi/
│   │   │   ├── Descomposicion D L U Formulacion Matricial.md ⏳
│   │   │   └── Matriz Iteracion T J y Radio Espectral.md ⏳
│   │   ├── Gauss Seidel/
│   │   │   ├── Formulacion Matricial y Matriz Iteracion T GS.md ⏳
│   │   │   └── Comparacion Asintotica Convergencia Jacobi.md ⏳
│   │   └── Convergencia Iterativos/
│   │       ├── Teorema Diagonal Dominante Estricta.md ⏳
│   │       ├── Criterio Radio Espectral Convergencia.md ⏳
│   │       └── Estimacion Error y Cotas A Priori.md ⏳
│   │
│   └── Valores Vectores Propios/ ⏳
│
├── 3 Ecuaciones No Lineales/ ⏳
├── 4 Aproximacion Funciones/ ⏳
├── 5 Diferenciacion Integracion Numerica/ ⏳
└── 6 Ecuaciones Diferenciales Ordinarias/ ⏳

## ESTRUCTURA DE CADA NOTA

### YAML obligatorio al inicio:
---
title: <nombre legible, no necesariamente idéntico al archivo>
tags:
  - metodos-numericos
  - teoria
  - <tema específico>
draft: false
aliases:
  - <sinónimos si aplica>
---

### Título principal:
# <Nombre del concepto> $<notación matemática si aplica>$

### Flujo de contenido (el orden depende del tipo de nota):

**Para un index.md (nota con hijas):**
1. Definición formal ([!definicion])
2. Idea fundamental o marco teórico común
3. Ejemplo concreto (3-5 iteraciones si es método numérico)
4. Presentación de métodos o variantes (delegando a notas hijas con wikilinks)
5. Convergencia o propiedades (delegando a notas hijas)
6. Motivación AL FINAL (se lee pocas veces, es contexto histórico/práctico)

**Para una nota sustantiva (hoja sin hijas):**
1. Definición formal ([!definicion])
2. Desarrollo teórico (alternando texto normal con callouts)
3. Demostraciones ([!demostracion])
4. Ejemplos concretos ([!ejemplo])
5. Propiedades o implicaciones
6. Relación con otras notas (wikilinks)

**Principio clave:** "Si se quita el callout y no cambia nada, estaba mal usado"

## CALLOUTS PERMITIDOS (EXACTAMENTE ESTOS, NO INVENTAR)

- [!definicion] → definiciones formales
- [!teorema] → resultados importantes
- [!demostracion] → pruebas matemáticas
- [!lema] → resultados auxiliares
- [!proposicion] → propiedades
- [!corolario] → consecuencias
- [!axioma] → supuestos base
- [!ejemplo] → ejemplos ilustrativos
- [!teoria] → explicación conceptual
- [!info] → aclaraciones importantes
- [!warning] → limitaciones o condiciones
- [!algoritmo] → pseudocódigo o pasos algorítmicos

NO usar: [!conclusion], [!nota], [!observacion], [!importante], ni ningún otro no listado.

## REGLAS DE WIKILINKS

**Formato obligatorio:**
- [[nombre_archivo | Texto visible]]
- Excepción index: [[nombre_directorio/index | texto visible]]

**Nombres de archivo:**
- Deben coincidir EXACTAMENTE con los del árbol
- Si el archivo no existe aún, igual se wikilinkea (es promesa de expansión futura)

**Dónde SÍ pueden aparecer:**
- Párrafos de texto normal
- Listas y viñetas
- Dentro de callouts
- Tablas (con cuidado)

**Dónde NO pueden aparecer:**
- Headers (##, ###, etc.)
- Bloques de código
- Entornos matemáticos ($$, $)

**Frecuencia:**
- Sin límite estricto, pero no saturar
- Un wikilink por cada concepto que merece su propia nota
- No wikilinkear dos veces el mismo concepto en párrafos cercanos

**Principio de delegación:**
- Si un concepto tiene su propia nota en el árbol, NO desarrollarlo, solo mencionarlo y wikilinkearlo
- La nota actual debe ser útil por sí misma, pero no duplicar contenido

## REGLAS DE CONTENIDO

- NO repetir contenido de otras notas
- SI delegar con wikilinks
- NO usar secciones genéricas tipo "Introducción" o "Estructura del directorio"
- NO escribir como texto plano continuo sin estructura
- SI estructurar como documento técnico con secciones claras
- Mantener profundidad matemática rigurosa
- Notación clara y consistente

## NOTACIÓN ESPECÍFICA PARA MÉTODOS ITERATIVOS

- Sucesión de vectores: y^{(k)} (no x^{(k)})
- Solución exacta: x = A^{-1}b
- Error: ε^{(k)} = y^{(k)} - x
- Matriz de iteración: T (no M)
- Partición de A: A = D - E - F (no L y U, reservados para factorización LU)
- Producto matriz-vector: A v

## LENGUAJES PARA CÓDIGO

Si se requiere código, usar según contexto: MATLAB, Python, Julia o C++. Preferir Python para ejemplos numéricos, MATLAB para álgebra lineal.

## ESTILO GENERAL

- Formal pero claro
- Matemático pero legible
- Técnico pero estructurado
- Visualmente limpio (alternar texto con callouts para ritmo visual)
- Cada callout debe aportar valor real (no decorativo)

## PRÓXIMA TAREA

Crear la nota: Fundamentos Iteracion Punto Fijo Lineal.md

Es una nota sustantiva (hoja) dentro de Metodos Iterativos/. Debe desarrollar el marco teórico unificado de los métodos iterativos estacionarios, que el index.md solo esboza. Debe incluir:

- Descomposición A = M - N con M no singular
- Deducción de la iteración y^{(k+1)} = M^{-1}N y^{(k)} + M^{-1}b
- Definición de la matriz de iteración T = M^{-1}N
- Ecuación del error ε^{(k+1)} = T ε^{(k)}
- Relación entre convergencia y ρ(T)
- Ejemplo de cómo distintas elecciones de M generan los métodos clásicos
- Wikilinks a las notas hijas de Jacobi y Gauss-Seidel para desarrollos específicos

Responde SOLO con la nota en Markdown, sin explicaciones externas.

```

Chat 2: [Chat 2](https://chat.deepseek.com/a/chat/s/7d556ac4-bb8e-4b76-9b8e-594219cda571)

