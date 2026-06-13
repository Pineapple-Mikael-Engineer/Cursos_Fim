#!/usr/bin/env python3
"""Figura del método de las imágenes (función de Green).
Estilo Ocean Forest. Salida -> ../img_gen/cargas_imagen.svg"""
import numpy as np
import ocean_forest as of


def fig_cargas_imagen():
    fig, ax = of.new_fig(figsize=(6.0, 5.6)); of.style_axes(ax)
    d = 1.0
    g = np.linspace(-3, 3, 400)
    X, Z = np.meshgrid(g, g)
    eps = 0.04
    phi = 1/np.sqrt(X**2+(Z-d)**2+eps) - 1/np.sqrt(X**2+(Z+d)**2+eps)
    # equipotenciales (solo semiplano superior, donde vive el problema)
    phim = np.ma.masked_where(Z < 0, phi)
    levels = [-2.0, -1.0, -0.5, 0.5, 1.0, 2.0]
    ax.contour(X, Z, phim, levels=levels, colors=[of.ACCENT], linewidths=1.1, alpha=0.85)
    # líneas de campo E = -grad phi
    Ex = -np.gradient(phi, g, axis=1)
    Ez = -np.gradient(phi, g, axis=0)
    Exm = np.ma.masked_where(Z < 0.02, Ex)
    Ezm = np.ma.masked_where(Z < 0.02, Ez)
    ax.streamplot(X, Z, Exm, Ezm, color=of.GRID, density=1.0, linewidth=0.7, arrowsize=0.8)
    # plano conductor (z=0) y cargas
    ax.axhline(0, color=of.BROWN, lw=2.6)
    ax.fill_between(g, -3, 0, color=of.BROWN, alpha=0.10)
    ax.plot(0, d, 'o', color=of.CURVE, ms=13, zorder=6)
    ax.text(0.18, d, r'$+q$', color=of.TEXT, fontsize=13, va='center')
    ax.plot(0, -d, 'o', mfc='none', mec=of.BROWN, mew=2.2, ms=13, zorder=6)
    ax.text(0.18, -d, r'$-q$ (imagen)', color=of.TICK, fontsize=11, va='center')
    ax.text(-2.85, 0.12, r'plano a tierra ($\phi=0$)', color=of.TEXT, fontsize=9)
    ax.set_xlim(-3, 3); ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    of.labels(ax, r'$x$', r'$z$')
    of.title(ax, r'Método de las imágenes: carga frente a un plano a tierra')
    of.save(fig, 'cargas_imagen')


if __name__ == '__main__':
    print('Generando figura cargas_imagen:')
    fig_cargas_imagen()
    print('Listo.')
