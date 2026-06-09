#!/usr/bin/env python3
"""Figuras del capitulo Difero-integrales (integro-dif. + calculo fraccionario).
Estilo Ocean Forest. Salida -> ../img_gen/*.svg"""
import numpy as np
from scipy.special import gamma
import matplotlib.pyplot as plt
from matplotlib.cm import ScalarMappable
from matplotlib.colors import Normalize, LinearSegmentedColormap
import ocean_forest as of

QCMAP = LinearSegmentedColormap.from_list('q', ['#2e4824', '#6a8858', '#cdbb86', '#b07828'])


# ---------------------------------------------------------- 1. el differintegral D^q x
def fig_differintegral():
    fig, ax = of.new_fig(figsize=(6.8, 4.6)); of.style_axes(ax)
    x = np.linspace(0.015, 2.0, 400)
    qs = [-1.0, -0.5, 0.0, 0.5, 1.0, 1.5]
    norm = Normalize(vmin=-1, vmax=2)
    # posición y manual de cada etiqueta (para evitar solapes en el borde derecho)
    ylab = {-1.0: 2.18, -0.5: 1.92, 0.0: 1.62, 0.5: 1.30, 1.0: 1.0, 1.5: 0.42}
    for q in qs:
        y = x**(1-q)/gamma(2-q)        # D^q x = x^{1-q}/Gamma(2-q)
        col = QCMAP(norm(q))
        ax.plot(x, y, color=col, lw=2.5)
        lbl = {-1: r'$q=-1$ (integral)', 0: r'$q=0$ (función)', 1: r'$q=1$ (derivada)'}.get(q, fr'$q={q}$')
        ax.text(2.05, ylab[q], lbl, color=col, fontsize=8.5, va='center')
    ax.axhline(0, color=of.BROWN, lw=0.8, alpha=0.5)
    ax.text(1.0, 0.06, r'$q=2$ (2ª derivada) $\to 0$', color=of.TICK, fontsize=8.5)
    ax.set_xlim(0, 2.7); ax.set_ylim(-0.1, 2.3)
    of.labels(ax, r'$x$', r'$D^{q}x$')
    of.title(ax, r'El differintegral: $D^{q}x=\dfrac{x^{1-q}}{\Gamma(2-q)}$ al variar el orden $q$')
    sm = ScalarMappable(norm=norm, cmap=QCMAP); sm.set_array([])
    cb = fig.colorbar(sm, ax=ax, fraction=0.04, pad=0.13)
    cb.set_label(r'orden $q$', color=of.TEXT); cb.ax.tick_params(colors=of.TICK)
    of.save(fig, 'differintegral')


# ---------------------------------------------------------- 2. memoria corta vs larga
def fig_memoria_viscoelasticidad():
    fig, ax = of.new_fig(figsize=(6.6, 4.4)); of.style_axes(ax)
    t = np.linspace(0.02, 6, 500)
    G_exp = np.exp(-t/0.8)                       # Maxwell: memoria corta
    al = 0.5
    G_pow = (1 + t/0.8)**(-al)                   # ley de potencias: memoria larga
    ax.plot(t, G_exp, color=of.ACCENT, lw=2.6, label=r'exponencial $e^{-t/\tau}$ (memoria corta)')
    ax.plot(t, G_pow, color=of.CURVE, lw=2.6, label=r'ley de potencias $\sim t^{-\alpha}$ (memoria larga)')
    ax.fill_between(t, 0, G_pow, color=of.CURVE, alpha=0.08)
    ax.annotate('cola larga:\nmemoria persistente', xy=(4.5, G_pow[np.argmin(np.abs(t-4.5))]),
                xytext=(3.0, 0.55), color=of.TEXT, fontsize=9.5,
                arrowprops=dict(arrowstyle='->', color=of.BROWN))
    ax.set_xlim(0, 6); ax.set_ylim(0, 1.03)
    of.labels(ax, r'$t$', r'módulo de relajación $G(t)$')
    of.title(ax, r'Núcleo de memoria: corta (exponencial) vs larga (ley de potencias)')
    of.legend(ax, loc='upper right')
    of.save(fig, 'memoria_viscoelasticidad')


if __name__ == '__main__':
    print('Generando figuras Difero-integrales:')
    fig_differintegral()
    fig_memoria_viscoelasticidad()
    print('Listo.')
