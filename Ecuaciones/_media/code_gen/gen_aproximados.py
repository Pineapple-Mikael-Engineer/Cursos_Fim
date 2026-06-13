#!/usr/bin/env python3
"""Figuras de Metodos Aproximados y Multivariable (Ecuaciones Integrales).
Estilo Ocean Forest. Salida -> ../img_gen/*.svg"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import ocean_forest as of

CMAP = LinearSegmentedColormap.from_list(
    'of_div', ['#2e4824', '#6a8858', '#f3f8ee', '#cdbb86', '#b07828'])


# ---------------------------------------------------------- 1. convergencia de metodos
def fig_convergencia_metodos():
    fig, ax = of.new_fig(figsize=(6.4, 4.4)); of.style_axes(ax)
    N = np.arange(2, 21)
    ax.semilogy(N, 0.8*N**(-2.0), 's--', color=of.BROWN, lw=2, ms=5,
                label=r'Colocación ($\sim N^{-2}$)')
    ax.semilogy(N, 0.5*N**(-3.0), '^--', color=of.ACCENT, lw=2, ms=5,
                label=r'Galerkin ($\sim N^{-3}$)')
    ax.semilogy(N, 2.0*np.exp(-0.85*N), 'o-', color=of.CURVE, lw=2.2, ms=5,
                label=r'Nyström gaussiano (espectral)')
    ax.set_xlim(2, 20)
    of.labels(ax, r'$N$ (nodos / términos)', r'error $\|\varphi-\varphi_N\|$')
    of.title(ax, r'Convergencia de los métodos aproximados (núcleo suave)')
    of.legend(ax, loc='upper right')
    of.save(fig, 'convergencia_metodos')


# ---------------------------------------------------------- 2. teoria de potencial (capas)
def fig_potencial_capas():
    of.setup()
    fig, ax = plt.subplots(figsize=(6.0, 5.4), facecolor=of.FIG_BG)
    ax.set_facecolor(of.PANEL)
    a, b = 1.55, 1.05
    th = np.linspace(0, 2*np.pi, 360)
    bx, by = a*np.cos(th), b*np.sin(th)
    # potencial de capa simple (cargas en la frontera, 2D: -ln r)
    cth = np.linspace(0, 2*np.pi, 160, endpoint=False)
    cx, cy = a*np.cos(cth), b*np.sin(cth)
    L = 2.35
    g = np.linspace(-L, L, 480)
    X, Y = np.meshgrid(g, g)
    V = np.zeros_like(X)
    for xc, yc in zip(cx, cy):
        V += -np.log(np.hypot(X - xc, Y - yc) + 0.05)
    V /= len(cx)
    # campo relleno (llena el cuadro) + equipotenciales encima
    levels = np.linspace(np.percentile(V, 3), np.percentile(V, 99), 22)
    cf = ax.contourf(X, Y, V, levels=levels, cmap=CMAP, extend='both')
    ax.contour(X, Y, V, levels=levels[1::3], colors=[of.BROWN], linewidths=0.7, alpha=0.5)
    # frontera y normales
    ax.plot(bx, by, color=of.BROWN, lw=3.2)
    for t in np.linspace(0, 2*np.pi, 16, endpoint=False):
        px, py = a*np.cos(t), b*np.sin(t)
        nx, ny = np.cos(t)/a, np.sin(t)/b
        nrm = np.hypot(nx, ny); nx, ny = nx/nrm, ny/nrm
        ax.annotate('', xy=(px + 0.36*nx, py + 0.36*ny), xytext=(px, py),
                    arrowprops=dict(arrowstyle='-|>', color=of.TICK, lw=1.5))
    ax.text(0, 0, r'$\Omega$', color=of.TEXT, fontsize=18, ha='center', va='center')
    ax.text(0, -1.28, r'$\partial\Omega,\ \sigma$', color=of.TEXT, fontsize=12, ha='center',
            bbox=dict(boxstyle='round,pad=0.15', fc=of.PANEL, ec='none', alpha=0.7))
    ax.set_xlim(-L, L); ax.set_ylim(-L, L); ax.set_aspect('equal')
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_color(of.BROWN)
    cb = fig.colorbar(cf, ax=ax, fraction=0.046, pad=0.03)
    cb.set_label('potencial', color=of.TEXT); cb.ax.tick_params(colors=of.TICK)
    of.title(ax, r'Potencial de capa simple: densidad $\sigma$ sobre la frontera')
    of.save(fig, 'potencial_capas')


# ---------------------------------------------------------- 3. dispersion (Lippmann-Schwinger)
def fig_dispersion_lippmann():
    of.setup()
    fig, ax = plt.subplots(figsize=(6.2, 4.8), facecolor=of.FIG_BG)
    ax.set_facecolor(of.PANEL)
    g = np.linspace(-4, 4, 500)
    X, Y = np.meshgrid(g, g)
    k = 4.0
    r = np.hypot(X, Y) + 1e-6
    u_inc = np.cos(k*X)                         # onda plana incidente (Re)
    u_sc = 0.9*np.cos(k*r)/np.sqrt(r)           # onda dispersada (circular)
    U = u_inc + u_sc
    r0 = 0.45
    U = np.ma.masked_where(r < r0, U)
    ax.imshow(U, origin='lower', extent=(-4, 4, -4, 4), cmap=CMAP,
              vmin=-1.6, vmax=1.6, aspect='equal')
    obst = plt.Circle((0, 0), r0, color=of.BROWN, zorder=5)
    ax.add_patch(obst)
    ax.text(0, 0, r'$V$', color='white', ha='center', va='center', fontsize=12, zorder=6)
    # flechas de la onda incidente (desde la izquierda)
    for yv in np.linspace(-3.2, 3.2, 5):
        ax.annotate('', xy=(-2.7, yv), xytext=(-3.7, yv),
                    arrowprops=dict(arrowstyle='-|>', color=of.TICK, lw=1.6))
    ax.text(-3.7, 3.6, r'onda incidente $u_{\mathrm{inc}}$', color=of.TEXT, fontsize=9)
    ax.text(1.5, 3.4, r'onda dispersada $u_{\mathrm{sc}}$', color=of.TEXT, fontsize=9)
    ax.set_xlim(-4, 4); ax.set_ylim(-4, 4)
    ax.set_xticks([]); ax.set_yticks([])
    for sp in ax.spines.values():
        sp.set_color(of.BROWN)
    of.title(ax, r'Dispersión: $u=u_{\mathrm{inc}}+u_{\mathrm{sc}}$ (Lippmann-Schwinger)')
    of.save(fig, 'dispersion_lippmann')


if __name__ == '__main__':
    print('Generando figuras Aproximados + Multivariable:')
    fig_convergencia_metodos()
    fig_potencial_capas()
    fig_dispersion_lippmann()
    print('Listo.')
