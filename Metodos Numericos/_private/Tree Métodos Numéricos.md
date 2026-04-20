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
│   │   ├── Jacobi/
│   │   │   ├── Descomposicion D L U Formulacion Matricial.md
│   │   │   └── Matriz Iteracion T J y Radio Espectral.md
│   │   ├── Gauss Seidel/
│   │   │   ├── Formulacion Matricial y Matriz Iteracion T GS.md
│   │   │   └── Comparacion Asintotica Convergencia Jacobi.md
│   │   └── Convergencia Iterativos/
│   │       ├── Teorema Diagonal Dominante Estricta.md
│   │       ├── Criterio Radio Espectral Convergencia.md
│   │       └── Estimacion Error y Cotas A Priori.md
│   │
│   └── Valores Vectores Propios/
│       ├── Metodo Potencia Directo/
│       │   ├── Fundamentos Valor Propio Dominante.md
│       │   ├── Velocidad Convergencia Razon Lambda2 Lambda1.md
│       │   └── Calculo Constante Normalizacion Rayleigh.md
│       └── Variantes Metodo Potencia/
│           ├── Potencia Inversa Valor Propio Menor Modulo.md
│           └── Potencia Desplazada Aceleracion Convergencia.md
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



