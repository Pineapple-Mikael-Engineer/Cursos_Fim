#!/usr/bin/env python3
"""Figuras de Sistemas y Dinámica + Soluciones por Series.
Estilo Ocean Forest. Salida -> ../img_gen/*.svg"""
import numpy as np
import matplotlib.pyplot as plt
import ocean_forest as of
from math import factorial


# ---------------------------------------------------------- 1. retratos de fase (4 tipos)
def fig_retratos_fase():
    of.setup()
    fig, axs = plt.subplots(2, 2, figsize=(7.4, 7.0), facecolor=of.FIG_BG)
    casos = [
        ("Silla", np.array([[1.0, 0.0], [0.0, -1.0]])),
        ("Nodo estable", np.array([[-1.0, 0.0], [0.0, -2.0]])),
        ("Foco estable", np.array([[-0.35, -1.0], [1.0, -0.35]])),
        ("Centro", np.array([[0.0, -1.0], [1.0, 0.0]])),
    ]
    L = 2.2
    x = np.linspace(-L, L, 24); y = np.linspace(-L, L, 24)
    X, Y = np.meshgrid(x, y)
    for ax, (nombre, A) in zip(axs.ravel(), casos):
        ax.set_facecolor(of.PANEL)
        U = A[0, 0]*X + A[0, 1]*Y
        V = A[1, 0]*X + A[1, 1]*Y
        ax.streamplot(X, Y, U, V, color=of.CURVE, density=1.1, linewidth=0.9,
                      arrowsize=0.9)
        ax.plot(0, 0, 'o', color=of.ACCENT, ms=7, zorder=5)
        ax.set_xlim(-L, L); ax.set_ylim(-L, L)
        ax.set_aspect('equal')
        ax.set_xticks([]); ax.set_yticks([])
        for sp in ax.spines.values():
            sp.set_color(of.BROWN); sp.set_linewidth(1.0)
        ax.set_title(nombre, color=of.TEXT, fontsize=12)
    fig.suptitle("Retratos de fase de un sistema lineal " r"$\dot{\mathbf{x}}=A\mathbf{x}$",
                 color=of.TEXT, fontsize=13)
    fig.tight_layout(rect=(0, 0, 1, 0.97))
    of.save(fig, 'retratos_fase')


# ---------------------------------------------------------- 2. convergencia de la serie (cos x)
def fig_convergencia_serie():
    fig, ax = of.new_fig(figsize=(6.8, 4.4)); of.style_axes(ax)
    xx = np.linspace(-np.pi, 2*np.pi, 600)

    def parcial(x, N):
        s = np.zeros_like(x)
        for k in range(N+1):
            s += (-1)**k * x**(2*k) / factorial(2*k)
        return s

    ax.plot(xx, np.cos(xx), color=of.CURVE, lw=2.8, label=r'$\cos x$ (exacta)', zorder=5)
    estilos = [(1, '$S_1$ (hasta $x^2$)'), (2, '$S_2$ (hasta $x^4$)'),
               (3, '$S_3$ (hasta $x^6$)'), (5, '$S_5$ (hasta $x^{10}$)')]
    cols = [of.PALETTE[3], of.PALETTE[2], of.ACCENT, of.PALETTE[4]]
    for (N, lbl), c in zip(estilos, cols):
        ax.plot(xx, parcial(xx, N), color=c, lw=1.6, ls='--', label=lbl)
    ax.axhline(0, color=of.BROWN, lw=0.8, alpha=0.5)
    ax.set_xlim(-np.pi, 2*np.pi); ax.set_ylim(-2.2, 2.2)
    of.labels(ax, r'$x$', r'$y$')
    of.title(ax, r"Sumas parciales de la serie de $\cos x$ (solución de $y''+y=0$)")
    of.legend(ax, loc='lower left', ncol=2)
    of.save(fig, 'convergencia_serie')


if __name__ == '__main__':
    print('Generando figuras Sistemas + Series:')
    fig_retratos_fase()
    fig_convergencia_serie()
    print('Listo.')
