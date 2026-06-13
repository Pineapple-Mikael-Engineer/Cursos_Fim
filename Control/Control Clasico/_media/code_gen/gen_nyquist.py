#!/usr/bin/env python3
"""Genera los diagramas de Nyquist (en ../img_gen/). Uso: python3 gen_nyquist.py"""
import numpy as np
import ocean_forest as of


def polar_axes(title, lim=2.0):
    fig, ax = of.new_fig(figsize=(5.6, 5.2)); of.style_axes(ax)
    ax.axhline(0, color=of.BROWN, lw=1.0, alpha=0.7)
    ax.axvline(0, color=of.BROWN, lw=1.0, alpha=0.7)
    ax.set_aspect('equal', adjustable='box')
    ax.plot(-1, 0, 'x', color=of.ACCENT, ms=12, mew=3)               # punto crítico
    ax.annotate(r'$-1$', (-1, 0), color=of.TEXT, xytext=(-2, 8), textcoords='offset points')
    of.labels(ax, r'$\mathrm{Re}\{L\}$', r'$\mathrm{Im}\{L\}$'); of.title(ax, title)
    ax.set_xlim(-lim, lim); ax.set_ylim(-lim, lim)
    return fig, ax


def Lval(num, den, w):
    s = 1j*w
    return np.polyval(num, s)/np.polyval(den, s)


def diagrama_polar():
    w = np.logspace(-1.5, 2, 1500)
    L = Lval([1], np.poly([-1, -1, -1]), w)   # 1/(s+1)^3
    fig, ax = polar_axes('Diagrama de Nyquist', lim=1.3)
    ax.plot(L.real, L.imag, color=of.CURVE, lw=2)
    ax.plot(L.real, -L.imag, color=of.CURVE, lw=2, alpha=0.5)   # espejo conjugado
    of.save(fig, 'nyquist_diagrama_polar')


def polar_tipo1():
    w = np.logspace(-1, 2, 2000)
    L = Lval([1], [1, 1, 0], w)   # 1/(s(s+1)) tipo 1
    fig, ax = polar_axes('Lugar polar — sistema tipo 1', lim=2.0)
    ax.plot(L.real, L.imag, color=of.CURVE, lw=2)
    ax.plot(L.real, -L.imag, color=of.CURVE, lw=2, alpha=0.5)
    ax.annotate(r'$\omega\to0^+$', (-1.0, -1.8), color=of.TEXT)
    ax.annotate(r'$\omega\to\infty$', (0.1, 0.15), color=of.TEXT)
    of.save(fig, 'nyquist_polar_tipo1')


def contorno():
    """Contorno de Nyquist en el plano-s (encierra el SPD)."""
    fig, ax = of.new_fig(figsize=(5.2, 5.6)); of.style_axes(ax)
    ax.axhline(0, color=of.BROWN, lw=1.0, alpha=0.7)
    ax.axvline(0, color=of.BROWN, lw=1.0, alpha=0.7)
    ax.set_aspect('equal', adjustable='box')
    R = 2.5
    th = np.linspace(-np.pi/2, np.pi/2, 200)
    ax.plot(R*np.cos(th), R*np.sin(th), color=of.CURVE, lw=2)   # semicírculo derecho
    ax.plot([0, 0], [-R, R], color=of.CURVE, lw=2)              # eje imaginario
    # flechas de sentido (horario)
    ax.annotate('', xy=(0, 0.3), xytext=(0, -0.3),
                arrowprops=dict(arrowstyle='-|>', color=of.CURVE, lw=2))
    ax.annotate('', xy=(R*np.cos(0.2), R*np.sin(0.2)), xytext=(R*np.cos(-0.2), R*np.sin(-0.2)),
                arrowprops=dict(arrowstyle='-|>', color=of.CURVE, lw=2))
    of.pole(ax, -1+1j); of.pole(ax, -1-1j); of.pole(ax, -0.5)   # polos de L (en SPI)
    ax.annotate(r'$R\to\infty$', (0.75, 1.35), color=of.TEXT,
                xytext=(0, 0), textcoords='offset points')
    ax.annotate(r'$\Gamma$', (0.18, 2.05), color=of.TEXT, fontsize=13)
    of.labels(ax, r'$\sigma$', r'$j\omega$'); of.title(ax, 'Contorno de Nyquist (encierra el SPD)')
    ax.set_xlim(-3, 3); ax.set_ylim(-3, 3)
    of.save(fig, 'nyquist_contorno')


def margenes():
    w = np.logspace(-1, 2, 3000)
    num, den = [2], [1, 1.5, 0.5, 0]   # 2/(s(s+1)(s+0.5))
    L = Lval(num, den, w)
    fig, ax = polar_axes('Márgenes en Nyquist (distancia a $-1$)', lim=2.0)
    ax.plot(L.real, L.imag, color=of.CURVE, lw=2)
    ax.plot(L.real, -L.imag, color=of.CURVE, lw=2, alpha=0.4)
    th = np.linspace(0, 2*np.pi, 200)
    ax.plot(np.cos(th), np.sin(th), color=of.BROWN, lw=1, ls='--', alpha=0.6)  # círculo unitario
    # cruce con eje real negativo (MG)
    ireal = np.argmin(np.abs(L.imag[w > 0.3]) + (L.real[w > 0.3] > 0)*10)
    xreal = L.real[w > 0.3][ireal]
    ax.plot([xreal, -1], [0, 0], color=of.ACCENT, lw=2.5)
    ax.annotate('MG', ((xreal-1)/2, 0), color=of.TEXT, xytext=(-4, 8), textcoords='offset points')
    of.save(fig, 'nyquist_margenes')


if __name__ == '__main__':
    print('Generando Nyquist...')
    diagrama_polar(); polar_tipo1(); contorno(); margenes()
    print('OK')
