#!/usr/bin/env python3
"""Figuras de Fredholm (capitulo Ecuaciones Integrales).
Estilo Ocean Forest. Salida -> ../img_gen/*.svg"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
import ocean_forest as of

# colormap on-brand: crema -> dorado -> verde
CMAP = LinearSegmentedColormap.from_list('oceanforest', ['#f3f8ee', '#cdbb86', '#b07828', '#2e4824'])


# ---------------------------------------------------------- 1. autofunciones del nucleo
def fig_autofunciones_fredholm():
    fig, ax = of.new_fig(figsize=(6.6, 4.4)); of.style_axes(ax)
    x = np.linspace(0, np.pi, 400)
    cols = [of.CURVE, of.ACCENT, of.BROWN]
    for n, c in zip([1, 2, 3], cols):
        ax.plot(x, np.sin(n*x), color=c, lw=2.4,
                label=fr'$\varphi_{n}=\operatorname{{sen}}({n}x)$,  $\lambda_{n}={n**2}$')
    ax.axhline(0, color=of.BROWN, lw=0.8, alpha=0.5)
    ax.set_xlim(0, np.pi); ax.set_ylim(-1.25, 1.45)
    ax.set_xticks([0, np.pi/2, np.pi]); ax.set_xticklabels(['0', r'$\pi/2$', r'$\pi$'])
    of.labels(ax, r'$x$', r'$\varphi_n(x)$')
    of.title(ax, r'Funciones propias de un núcleo de Green (ortogonales)')
    of.legend(ax, loc='upper right')
    of.save(fig, 'autofunciones_fredholm')


# ---------------------------------------------------------- 2. problema mal planteado
def fig_mal_planteado():
    fig, (ax1, ax2) = of.new_fig(ncols=2, figsize=(7.6, 4.0))
    n = np.arange(1, 16)
    sig = np.exp(-0.55*n)                     # valores singulares decaen rapido
    of.style_axes(ax1)
    ax1.semilogy(n, sig, 'o-', color=of.CURVE, lw=2, ms=5)
    ax1.set_xlim(0.5, 15.5)
    of.labels(ax1, r'$n$', r'valor singular $\sigma_n$')
    of.title(ax1, 'Decaen rápido')
    of.style_axes(ax2)
    alpha = 1e-3
    ax2.semilogy(n, 1/sig, 's--', color=of.BROWN, lw=2, ms=5, label=r'$1/\sigma_n$ (sin regularizar)')
    ax2.semilogy(n, sig/(sig**2+alpha), 'o-', color=of.ACCENT, lw=2, ms=5,
                 label=r'$\sigma_n/(\sigma_n^2+\alpha)$ (Tikhonov)')
    ax2.set_xlim(0.5, 15.5)
    of.labels(ax2, r'$n$', 'amplificación')
    of.title(ax2, 'Inversión: explota vs. filtrada')
    of.legend(ax2, loc='upper left', fontsize=8)
    fig.suptitle('Fredholm de 1ª especie: mal planteamiento y regularización',
                 color=of.TEXT, fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    of.save(fig, 'mal_planteado')


# Green simetrico del operador -u'' en [0,pi], u(0)=u(pi)=0
def _green(N=200):
    x = np.linspace(0, np.pi, N)
    X, T = np.meshgrid(x, x)
    G = np.where(X <= T, X*(np.pi-T), T*(np.pi-X))/np.pi
    return x, G


# ---------------------------------------------------------- 3. nucleo de Green simetrico
def fig_green_kernel():
    of.setup()
    fig, ax = plt.subplots(figsize=(5.2, 4.6), facecolor=of.FIG_BG)
    x, G = _green()
    im = ax.imshow(G, origin='lower', extent=(0, np.pi, 0, np.pi), cmap=CMAP, aspect='equal')
    ax.plot([0, np.pi], [0, np.pi], color=of.BROWN, lw=1.2, ls='--', alpha=0.7)
    ax.text(2.3, 0.45, r'$x=t$', color=of.TEXT, fontsize=10, rotation=33)
    ax.set_xticks([0, np.pi/2, np.pi]); ax.set_xticklabels(['0', r'$\pi/2$', r'$\pi$'])
    ax.set_yticks([0, np.pi/2, np.pi]); ax.set_yticklabels(['0', r'$\pi/2$', r'$\pi$'])
    for sp in ax.spines.values():
        sp.set_color(of.BROWN)
    of.labels(ax, r'$t$', r'$x$')
    of.title(ax, r'Núcleo de Green $G(x,t)$: simétrico')
    cb = fig.colorbar(im, ax=ax, fraction=0.046, pad=0.04)
    cb.ax.tick_params(colors=of.TICK)
    of.save(fig, 'green_kernel')


# ---------------------------------------------------------- 4. descomposicion de Mercer
def fig_nucleo_mercer():
    of.setup()
    fig, axs = plt.subplots(1, 2, figsize=(7.8, 4.0), facecolor=of.FIG_BG)
    x, G = _green()
    N = len(x)
    # aproximacion de Mercer de rango 3: sum 2/pi sin(nx)sin(nt)/n^2
    xx = np.linspace(0, np.pi, N)
    Xv, Tv = np.meshgrid(xx, xx)
    G3 = np.zeros_like(G)
    for nn in range(1, 4):
        G3 += (2/np.pi)*np.sin(nn*Xv)*np.sin(nn*Tv)/nn**2
    vmin, vmax = G.min(), G.max()
    for ax, M, ttl in [(axs[0], G, r'núcleo $G(x,t)$'),
                       (axs[1], G3, r'Mercer rango 3: $\sum_{n\leq 3}\varphi_n\varphi_n/\lambda_n$')]:
        im = ax.imshow(M, origin='lower', extent=(0, np.pi, 0, np.pi), cmap=CMAP,
                       aspect='equal', vmin=vmin, vmax=vmax)
        ax.set_xticks([0, np.pi]); ax.set_xticklabels(['0', r'$\pi$'])
        ax.set_yticks([0, np.pi]); ax.set_yticklabels(['0', r'$\pi$'])
        for sp in ax.spines.values():
            sp.set_color(of.BROWN)
        ax.set_title(ttl, color=of.TEXT, fontsize=11)
        ax.set_xlabel(r'$t$', color=of.TEXT); ax.set_ylabel(r'$x$', color=of.TEXT)
    fig.suptitle('Teorema de Mercer: el núcleo es su descomposición espectral',
                 color=of.TEXT, fontsize=12)
    fig.tight_layout(rect=(0, 0, 1, 0.95))
    of.save(fig, 'nucleo_mercer')


if __name__ == '__main__':
    print('Generando figuras Fredholm:')
    fig_autofunciones_fredholm()
    fig_mal_planteado()
    fig_green_kernel()
    fig_nucleo_mercer()
    print('Listo.')
