"""Diagramas conceptuales: cuadro termodinámico, 1ª ley P-v, gas ideal vs real,
rutas T-s, barras de exergía y Helmholtz. Estilo Ocean Forest."""
import numpy as np
import ocean_forest as of
of.setup()


def cuadrado(ax):
    """Dibuja el cuadrado termodinámico de Born. Corners V,T,P,S; edges F,G,H,U."""
    ax.plot([0, 1, 1, 0, 0], [1, 1, 0, 0, 1], color=of.BROWN, lw=2.2)
    # esquinas (variables naturales)
    for (x, y, s, ha, va) in [(-0.02, 1.04, r'$V$', 'right', 'bottom'),
                              (1.02, 1.04, r'$T$', 'left', 'bottom'),
                              (1.02, -0.04, r'$P$', 'left', 'top'),
                              (-0.02, -0.04, r'$S$', 'right', 'top')]:
        ax.text(x, y, s, color=of.TEXT, fontsize=15, ha=ha, va=va, weight='bold')
    # lados (potenciales)
    for (x, y, s) in [(0.5, 1.06, r'$F$'), (1.07, 0.5, r'$G$'),
                      (0.5, -0.07, r'$H$'), (-0.07, 0.5, r'$U$')]:
        ax.text(x, y, s, color=of.CURVE, fontsize=15, ha='center', va='center', weight='bold')
    ax.set_xlim(-0.35, 1.35); ax.set_ylim(-0.3, 1.3); ax.set_aspect('equal')
    ax.axis('off')


# 1) Cuadro de Born (potenciales y variables naturales)
fig, ax = of.new_fig(figsize=(5.6, 5.0)); cuadrado(ax)
ax.text(0.5, 1.42, 'Cuadro termodinámico de Born', color=of.TEXT, fontsize=12, ha='center')
ax.text(0.5, -0.22,
        r'$dU=T\,dS-P\,dV$   $dH=T\,dS+V\,dP$' '\n'
        r'$dF=-S\,dT-P\,dV$   $dG=-S\,dT+V\,dP$',
        color=of.TEXT, fontsize=9.5, ha='center', va='top')
# flechas conjugadas (diagonales)
ax.annotate('', (1, 1), (0, 0), arrowprops=dict(arrowstyle='->', color=of.ACCENT, lw=1.2, alpha=0.6))
ax.annotate('', (0, 1), (1, 0), arrowprops=dict(arrowstyle='->', color=of.ACCENT, lw=1.2, alpha=0.6))
of.save(fig, 'potenciales_cuadro_Born')

# 2) Rueda de Maxwell (relaciones desde el cuadrado)
fig, ax = of.new_fig(figsize=(5.6, 5.0)); cuadrado(ax)
ax.text(0.5, 1.42, 'Relaciones de Maxwell desde el cuadrado', color=of.TEXT, fontsize=11.5, ha='center')
ax.text(0.5, -0.20,
        r'$\left(\frac{\partial T}{\partial V}\right)_S=-\left(\frac{\partial P}{\partial S}\right)_V$   '
        r'$\left(\frac{\partial S}{\partial V}\right)_T=\left(\frac{\partial P}{\partial T}\right)_V$',
        color=of.CURVE, fontsize=10, ha='center', va='top')
ax.text(0.5, -0.40,
        r'$\left(\frac{\partial T}{\partial P}\right)_S=\left(\frac{\partial V}{\partial S}\right)_P$   '
        r'$\left(\frac{\partial S}{\partial P}\right)_T=-\left(\frac{\partial V}{\partial T}\right)_P$',
        color=of.CURVE, fontsize=10, ha='center', va='top')
of.save(fig, 'maxwell_rueda_potenciales')

# 3) Primera ley SC: área = W en P-v
fig, ax = of.new_fig(figsize=(6.0, 4.4)); of.style_axes(ax)
v = np.linspace(1, 2.4, 200); Pp = 3 / v
ax.plot(v, Pp, color=of.CURVE, lw=2.6)
ax.fill_between(v, Pp, 0, color=of.CURVE, alpha=0.16)
ax.plot([v[0], v[-1]], [Pp[0], Pp[-1]], 'o', color=of.TEXT, ms=7, zorder=6)
ax.annotate('1', (v[0], Pp[0]), (6, 6), textcoords='offset points', color=of.TEXT, fontsize=11, weight='bold')
ax.annotate('2', (v[-1], Pp[-1]), (6, 6), textcoords='offset points', color=of.TEXT, fontsize=11, weight='bold')
ax.text(1.6, 0.9, r'$W=\int_1^2 P\,dV$', color=of.CURVE, fontsize=12, ha='center')
ax.text(1.7, 2.6, r'$\Delta U = Q - W$', color=of.BROWN, fontsize=12, ha='center')
of.labels(ax, x=r'volumen  $V$', y=r'presión  $P$')
of.title(ax, r'Primera ley (sistema cerrado): el trabajo es el área bajo $P$–$V$')
ax.set_xlim(0.9, 2.6); ax.set_ylim(0, 3.4)
of.save(fig, 'primera_ley_SC_diagrama_Pv')

# 4) Entalpía: trabajo de flujo Pv como área
fig, ax = of.new_fig(figsize=(6.0, 4.2)); of.style_axes(ax)
# barra apilada h = u + Pv
ax.bar(0, 3.2, width=0.5, color=of.CURVE, label=r'$u$ (energía interna)')
ax.bar(0, 1.1, width=0.5, bottom=3.2, color=of.ACCENT, label=r'$Pv$ (trabajo de flujo)')
ax.annotate(r'$h=u+Pv$', (0.32, 3.75), color=of.TEXT, fontsize=13)
ax.annotate('', (0.28, 0), (0.28, 4.3), arrowprops=dict(arrowstyle='<->', color=of.BROWN, lw=1.4))
ax.text(0.4, 2.0, r'$h$', color=of.BROWN, fontsize=14)
of.labels(ax, y='energía específica  [kJ/kg]')
of.title(ax, r'La entalpía suma el trabajo de flujo $Pv$ a $u$')
ax.set_xlim(-0.6, 0.9); ax.set_ylim(0, 4.6); ax.set_xticks([])
of.legend(ax, loc='upper right', fontsize=9)
of.save(fig, 'entalpia_flujo_trabajo_Pv')

# 5) Exergía: balance de Gouy-Stodola (barras)
fig, ax = of.new_fig(figsize=(6.2, 4.2)); of.style_axes(ax)
ax.bar(0, 100, width=0.55, color=of.CURVE)
ax.bar(1, 62, width=0.55, color=of.ACCENT, label=r'trabajo útil $W$')
ax.bar(1, 26, width=0.55, bottom=62, color='#6a8858', label=r'exergía de salida')
ax.bar(1, 12, width=0.55, bottom=88, color=of.BROWN, label=r'destruida $T_0\dot S_{gen}$')
ax.text(0, 103, r'exergía' '\n' r'de entrada', color=of.TEXT, fontsize=9, ha='center')
ax.annotate('', (0.32, 50), (0.68, 50), arrowprops=dict(arrowstyle='->', color=of.TEXT, lw=1.4))
of.labels(ax, y='exergía  [%]')
of.title(ax, r'Balance de exergía:  destrucción $=T_0\,\dot S_{gen}$')
ax.set_xlim(-0.6, 1.6); ax.set_ylim(0, 118); ax.set_xticks([0, 1]); ax.set_xticklabels(['entrada', 'salida'])
of.legend(ax, loc='upper left', fontsize=8.5)
of.save(fig, 'exergia_destruccion_Gouy_Stodola')

# 6) Helmholtz: W_max = -ΔF (barras)
fig, ax = of.new_fig(figsize=(6.0, 4.2)); of.style_axes(ax)
ax.bar(0, 100, width=0.5, color=of.CURVE)
ax.text(0, 103, r'$-\Delta U$', color=of.TEXT, fontsize=11, ha='center')
ax.bar(1, 82, width=0.5, color=of.ACCENT, label=r'$W_{max}=-\Delta F$')
ax.bar(1, 18, width=0.5, bottom=82, color=of.BROWN, label=r'$T\Delta S$ (calor cedido)')
of.labels(ax, y='energía  [%]')
of.title(ax, r'Trabajo máximo isotérmico:  $W_{max}=-\Delta F=-\Delta U+T\Delta S$')
ax.set_xlim(-0.6, 1.6); ax.set_ylim(0, 118); ax.set_xticks([0, 1])
ax.set_xticklabels([r'$-\Delta U$', 'reparto'])
of.legend(ax, loc='upper right', fontsize=8.5)
of.save(fig, 'helmholtz_trabajo_maximo')

# 7) Gas ideal vs real (moléculas)
fig, (a1, a2) = of.new_fig(ncols=2, figsize=(8.4, 4.2))
rng_x = [0.13, 0.27, 0.42, 0.55, 0.68, 0.81, 0.22, 0.36, 0.49, 0.62, 0.75, 0.88,
         0.18, 0.31, 0.45, 0.58, 0.71, 0.84, 0.25, 0.4, 0.66, 0.5, 0.3, 0.7]
rng_y = [0.18, 0.72, 0.35, 0.85, 0.22, 0.6, 0.48, 0.15, 0.78, 0.4, 0.66, 0.28,
         0.55, 0.88, 0.62, 0.2, 0.45, 0.75, 0.32, 0.5, 0.82, 0.12, 0.9, 0.58]
for ax, tit, jit in [(a1, 'Gas ideal: sin interacciones', 0.0), (a2, 'Gas real: atracción + volumen propio', 1.0)]:
    of.style_axes(ax)
    xs = np.array(rng_x); ys = np.array(rng_y)
    if jit:  # agrupar (atracción) para el gas real
        xs = 0.5 + (xs - 0.5) * 0.72; ys = 0.5 + (ys - 0.5) * 0.72
    ax.scatter(xs, ys, s=90, color=of.CURVE, edgecolors=of.BROWN, linewidths=0.8, zorder=5)
    if jit:
        ax.annotate('atracción', (0.5, 0.5), (0.18, 0.08), color=of.ACCENT, fontsize=9,
                    arrowprops=dict(arrowstyle='->', color=of.ACCENT, lw=1))
    of.title(ax, tit)
    ax.set_xlim(0, 1); ax.set_ylim(0, 1); ax.set_xticks([]); ax.set_yticks([])
of.save(fig, 'gas_ideal_moleculas_vs_real')

# 8) Rutas de integración en T-s (función de estado)
fig, ax = of.new_fig(figsize=(6.0, 4.4)); of.style_axes(ax)
A = (0.4, 0.6); B = (1.6, 1.5)
# ruta 1: a T cte luego a s cte (escalón)
ax.plot([A[0], B[0], B[0]], [A[1], A[1], B[1]], color=of.ACCENT, lw=2.0, label='ruta 1')
# ruta 2: diagonal directa
ax.plot([A[0], B[0]], [A[1], B[1]], color=of.CURVE, lw=2.0, ls='--', dashes=(6, 3), label='ruta 2')
# ruta 3: curva
sc = np.linspace(A[0], B[0], 50)
ax.plot(sc, A[1] + (B[1] - A[1]) * ((sc - A[0]) / (B[0] - A[0])) ** 2, color=of.BROWN, lw=2.0, label='ruta 3')
ax.plot(*A, 'o', color=of.TEXT, ms=8, zorder=6); ax.annotate('1', A, (-14, -2), textcoords='offset points', color=of.TEXT, fontsize=12, weight='bold')
ax.plot(*B, 'o', color=of.TEXT, ms=8, zorder=6); ax.annotate('2', B, (8, 2), textcoords='offset points', color=of.TEXT, fontsize=12, weight='bold')
ax.text(1.0, 0.4, r'$\Delta s = s_2-s_1$  igual por toda ruta', color=of.TEXT, fontsize=9, ha='center')
of.labels(ax, x=r'entropía  $s$', y=r'temperatura  $T$')
of.title(ax, r'$s$ es función de estado: $\Delta s$ independiente del camino')
ax.set_xlim(0.2, 1.9); ax.set_ylim(0.3, 1.8); of.legend(ax, loc='upper left', fontsize=8.5)
of.save(fig, 'tds_rutas_integracion')

print('OK conceptual: 8 figuras')
