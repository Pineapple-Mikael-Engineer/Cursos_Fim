#!/usr/bin/env python3
"""Figuras del cap. 1 (EDO) — Fundamentos y Métodos de Primer Orden.
Estilo Ocean Forest. Salida -> ../img_gen/*.svg"""
import numpy as np
from matplotlib.collections import LineCollection
import ocean_forest as of


def slope_field(ax, slope, xlim, ylim, nx=19, ny=15, h=0.16, color=None, alpha=0.55, lw=1.0):
    """Dibuja segmentos cortos de pendiente fija (campo de direcciones)."""
    color = color or of.GRID
    xs = np.linspace(xlim[0], xlim[1], nx)
    ys = np.linspace(ylim[0], ylim[1], ny)
    X, Y = np.meshgrid(xs, ys)
    segs = []
    for x, y in zip(X.ravel(), Y.ravel()):
        m = slope(x, y)
        if not np.isfinite(m):
            continue
        norm = np.hypot(1.0, m)
        dx, dy = h / norm, h * m / norm
        segs.append([(x - dx, y - dy), (x + dx, y + dy)])
    ax.add_collection(LineCollection(segs, colors=color, linewidths=lw, alpha=alpha))


# ---------------------------------------------------------------- 1. campo de direcciones y'=2x
def fig_campo_direcciones():
    fig, ax = of.new_fig(figsize=(6.4, 4.6)); of.style_axes(ax)
    xlim, ylim = (-2, 2), (-1.2, 3.2)
    slope_field(ax, lambda x, y: 2 * x, xlim, ylim, color=of.GRID, alpha=0.7)
    # isoclinas verticales (pendiente fija sobre cada x)
    for xv in (-1.5, -1, -0.5, 0, 0.5, 1, 1.5):
        ax.axvline(xv, color=of.BROWN, ls=':', lw=0.9, alpha=0.35)
    # curvas integrales y = x^2 + c
    xx = np.linspace(*xlim, 400)
    for c, lbl in [(-1, None), (0, r'$y=x^2+c$'), (1, None), (2, None)]:
        ax.plot(xx, xx**2 + c, color=of.ACCENT, lw=2.1, label=lbl)
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    of.labels(ax, r'$x$', r'$y$')
    of.title(ax, r"Campo de direcciones de $y'=2x$  (isoclinas verticales)")
    of.legend(ax, loc='upper center')
    of.save(fig, 'campo_direcciones')


# ---------------------------------------------------------------- 2. curvas integrales y=x^2+c
def fig_curvas_integrales():
    fig, ax = of.new_fig(figsize=(6.4, 4.6)); of.style_axes(ax)
    xlim, ylim = (-2, 2), (-2.3, 3.3)
    slope_field(ax, lambda x, y: 2 * x, xlim, ylim, color=of.GRID, alpha=0.30, h=0.13)
    xx = np.linspace(*xlim, 400)
    cols = of.PALETTE
    for i, c in enumerate([-2, -1, 0, 1]):
        ax.plot(xx, xx**2 + c, color=cols[i % len(cols)], lw=2.2,
                label=fr'$c={c}$')
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    of.labels(ax, r'$x$', r'$y$')
    of.title(ax, r"Curvas integrales $y=x^2+c$  (no se cruzan)")
    of.legend(ax, loc='upper center', ncol=4)
    of.save(fig, 'curvas_integrales')


# ---------------------------------------------------------------- 3. no unicidad (Peano)
def fig_no_unicidad_peano():
    fig, ax = of.new_fig(figsize=(6.6, 4.4)); of.style_axes(ax)
    xx = np.linspace(0, 2.2, 500)

    def y_delayed(x, a):
        out = np.zeros_like(x)
        m = x > a
        out[m] = ((x[m]**2 - a**2) / 4.0)**2
        return out

    ax.plot(xx, np.zeros_like(xx), color=of.BROWN, lw=2.4, label=r'$y\equiv 0$')
    ax.plot(xx, y_delayed(xx, 0.0), color=of.ACCENT, lw=2.4, label=r'$y=x^4/16$')
    ax.plot(xx, y_delayed(xx, 0.9), color=of.CURVE, lw=2.2, ls='--',
            label=r'$y_a,\ a=0.9$')
    ax.plot(xx, y_delayed(xx, 1.4), color='#6a8858', lw=2.2, ls='-.',
            label=r'$y_a,\ a=1.4$')
    ax.plot([0], [0], 'o', color=of.BROWN, ms=7, zorder=5)
    ax.annotate('mismo PVI\n$y(0)=0$', xy=(0, 0), xytext=(0.45, 0.55),
                color=of.TEXT, fontsize=10,
                arrowprops=dict(arrowstyle='->', color=of.BROWN))
    ax.set_xlim(0, 2.2); ax.set_ylim(-0.15, 1.25)
    of.labels(ax, r'$x$', r'$y$')
    of.title(ax, r"No unicidad de $y'=x\,y^{1/2},\ y(0)=0$")
    of.legend(ax, loc='upper left')
    of.save(fig, 'no_unicidad_peano')


# ---------------------------------------------------------------- 4. iteradas de Picard
def fig_iteracion_picard():
    fig, ax = of.new_fig(figsize=(6.4, 4.5)); of.style_axes(ax)
    xx = np.linspace(0, 2, 400)
    y0 = np.ones_like(xx)
    y1 = 1 + xx
    y2 = 1 + xx + xx**2 / 2
    y3 = 1 + xx + xx**2 / 2 + xx**3 / 6
    cols = of.PALETTE
    ax.plot(xx, y0, color=cols[3], lw=1.6, ls=':', label=r'$y_0=1$')
    ax.plot(xx, y1, color=cols[2], lw=1.8, ls='--', label=r'$y_1=1+x$')
    ax.plot(xx, y2, color=cols[4], lw=1.8, ls='-.', label=r'$y_2$')
    ax.plot(xx, y3, color=of.ACCENT, lw=2.0, label=r'$y_3$')
    ax.plot(xx, np.exp(xx), color=of.CURVE, lw=2.6, label=r'$e^x$ (exacta)')
    ax.set_xlim(0, 2); ax.set_ylim(0.8, 7.6)
    of.labels(ax, r'$x$', r'$y$')
    of.title(ax, r"Iteradas de Picard de $y'=y,\ y(0)=1\ \to\ e^x$")
    of.legend(ax, loc='upper left')
    of.save(fig, 'iteracion_picard')


# ---------------------------------------------------------------- 5. trayectorias ortogonales
def fig_trayectorias_ortogonales():
    fig, ax = of.new_fig(figsize=(5.6, 5.4)); of.style_axes(ax)
    lim = 2.5
    xx = np.linspace(-lim, lim, 500)
    # parábolas y = c x^2 (dorado)
    first = True
    for c in (-1.5, -0.7, -0.3, 0.3, 0.7, 1.5):
        ax.plot(xx, c * xx**2, color=of.ACCENT, lw=1.8,
                label=r'$y=c\,x^2$' if first else None)
        first = False
    # elipses x^2 + 2 y^2 = k (verde)
    th = np.linspace(0, 2 * np.pi, 400)
    first = True
    for k in (0.5, 1.2, 2.2, 3.6, 5.2):
        ax.plot(np.sqrt(k) * np.cos(th), np.sqrt(k / 2) * np.sin(th),
                color=of.CURVE, lw=1.8,
                label=r'$x^2+2y^2=k$' if first else None)
        first = False
    ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim)
    ax.set_aspect('equal', adjustable='box')
    of.labels(ax, r'$x$', r'$y$')
    of.title(ax, r"Trayectorias ortogonales")
    of.legend(ax, loc='upper right')
    of.save(fig, 'trayectorias_ortogonales')


# ---------------------------------------------------------------- 6. envolvente (Clairaut)
def fig_envolvente_clairaut():
    fig, ax = of.new_fig(figsize=(6.2, 4.8)); of.style_axes(ax)
    xx = np.linspace(-2.2, 2.2, 400)
    first = True
    for c in np.linspace(-3, 3, 13):
        ax.plot(xx, c * xx - c**2 / 4, color=of.GRID, lw=1.0, alpha=0.8,
                label=r'$y=cx-c^2/4$' if first else None)
        first = False
    ax.plot(xx, xx**2, color=of.ACCENT, lw=2.8, label=r'envolvente $y=x^2$')
    ax.set_xlim(-2.2, 2.2); ax.set_ylim(-2.4, 4.2)
    of.labels(ax, r'$x$', r'$y$')
    of.title(ax, r"Envolvente: haz de rectas y la parábola $y=x^2$")
    of.legend(ax, loc='upper center')
    of.save(fig, 'envolvente_clairaut')


if __name__ == '__main__':
    print('Generando figuras EDO cap.1:')
    fig_campo_direcciones()
    fig_curvas_integrales()
    fig_no_unicidad_peano()
    fig_iteracion_picard()
    fig_trayectorias_ortogonales()
    fig_envolvente_clairaut()
    print('Listo.')
