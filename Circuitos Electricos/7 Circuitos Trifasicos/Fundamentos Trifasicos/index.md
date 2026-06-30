---
title: Fundamentos Trifásicos
order: 1
tags:
  - circuitos-electricos
  - teoria
  - trifasico
  - index
draft: false
aliases:
  - fundamentos trifásicos
  - sistema trifásico fundamentos
---

# Fundamentos Trifásicos

> [!definicion]
> Los fundamentos del trifásico: **qué es** un sistema polifásico, **cómo se generan** sus tres tensiones desfasadas $120^\circ$, en **qué orden** se suceden (secuencia de fases) y **por qué** se usa en vez del monofásico. Es la base conceptual antes de conectar y calcular.

> [!info]
> Primera sección del [[7 Circuitos Trifasicos/index| capítulo 7]]. Sienta las ideas que después aplican las [[Conexiones Balanceadas/index| conexiones]] y la [[Potencia Trifasica/index| potencia trifásica]]. Fraile Mora, cap. 3, §3.1-3.2.

---

## Las tres ideas de partida

> [!teoria] De una fase a tres
> Un **sistema polifásico** usa varias tensiones de la misma frecuencia desfasadas por igual; el **trifásico** ($n=3$) es el óptimo en la práctica. Sus tres tensiones de fase, equilibradas, son
> $$\overline{V}_a=V\angle0^\circ,\quad \overline{V}_b=V\angle{-}120^\circ,\quad \overline{V}_c=V\angle{+}120^\circ,$$
> con la propiedad esencial $\overline{V}_a+\overline{V}_b+\overline{V}_c=0$. → [[Sistema Polifasico]].
>
> Se **generan** haciendo girar un rotor dentro de **tres devanados** separados $120^\circ$ en el estator: cada uno induce una senoide desfasada $120^\circ$, como en el alternador monofásico pero por triplicado. → [[Generacion de Tensiones Trifasicas]].

> [!teoria] Secuencia y ventajas
> El **orden** en que las tensiones alcanzan su máximo —la **secuencia de fases** ($abc$ o $acb$)— determina el sentido de giro de los motores; invertir dos fases invierte el giro. → [[Secuencia de Fases]].
>
> ¿Por qué el trifásico se impuso? Porque entrega **potencia instantánea constante** (el monofásico pulsa a $2\omega$), crea un **campo magnético giratorio** (motores sin escobillas ni arranque especial) y transporta la misma potencia con **menos material conductor**. → [[Ventajas del Trifasico]].

## Mapa de la sección

> [!info] Qué desarrolla cada hija
> | Nota | Contenido |
> |:---|:---|
> | [[Sistema Polifasico]] | qué es un sistema de varias fases; el caso $n=3$ |
> | [[Generacion de Tensiones Trifasicas]] | el alternador trifásico; $120^\circ$ por construcción |
> | [[Secuencia de Fases]] | orden $abc$ / $acb$; sentido de giro |
> | [[Ventajas del Trifasico]] | potencia constante, campo giratorio, ahorro de cobre |

> [!corolario]
> Tres tensiones iguales a $120^\circ$ que suman cero: esa simetría es el origen de todas las virtudes del trifásico. Entender de dónde salen y por qué convienen prepara para conectarlas (Y/Δ) y calcular su potencia.

> [!referencia]
> Fraile Mora, cap. 3, §3.1-3.2. Siguiente sección: [[Conexiones Balanceadas/index| Conexiones balanceadas]].
