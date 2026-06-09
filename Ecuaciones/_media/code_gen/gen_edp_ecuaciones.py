#!/usr/bin/env python3
"""Figuras de las tres ecuaciones clasicas: calor, onda, Laplace.
Estilo Ocean Forest. Salida -> ../img_gen/*.svg"""
import numpy as np
import ocean_forest as of


# ---------------------------------------------------------- 1. difusion del calor
def fig_evolucion_calor():
    fig, ax = of.new_fig(figsize=(6.6, 4.4)); of.style_axes(ax)
    x = np.linspace(-4, 4, 600)
    cols = [of.CURVE, of.PALETTE[4], of.ACCENT, of.PALETTE[3]]
    for t, c in zip([0.02, 0.25, 1.0, 3.0], cols):
        w = 1 + 4*t                       # alpha=1, dato inicial gaussiano exp(-x^2)
        u = 1/np.sqrt(w)*np.exp(-x**2/w)
        ax.plot(x, u, color=c, lw=2.3, label=fr'$t={t}$')
        ax.fill_between(x, 0, u, color=c, alpha=0.07)
    ax.set_xlim(-4, 4); ax.set_ylim(0, 1.05)
    of.labels(ax, r'$x$', r'$u(x,t)$')
    of.title(ax, r'Difusión del calor: el perfil se aplana y ensancha')
    of.legend(ax, loc='upper right')
    of.save(fig, 'evolucion_calor')


# ---------------------------------------------------------- 2. modos normales de la cuerda
def fig_modos_onda():
    fig, ax = of.new_fig(figsize=(6.4, 4.8)); of.style_axes(ax)
    x = np.linspace(0, 1, 400)
    cols = of.PALETTE
    for n in range(1, 5):
        off = (4-n)*2.4
        y = np.sin(n*np.pi*x)
        ax.plot(x, y+off, color=cols[(n-1) % len(cols)], lw=2.3)
        ax.plot(x, off+0*x, color=of.BROWN, lw=0.7, alpha=0.4)
        # nodos
        nodos = np.arange(0, n+1)/n
        ax.plot(nodos, off+0*nodos, 'o', color=of.BROWN, ms=5, zorder=5)
        ax.text(1.03, off, fr'$n={n}$', color=of.TEXT, va='center', fontsize=11)
        ax.text(1.03, off-0.55, fr'$\omega_{n}={n}\omega_1$', color=of.TICK, va='center', fontsize=8)
    ax.set_xlim(0, 1.2); ax.set_ylim(-1.4, 9.0)
    ax.set_yticks([])
    of.labels(ax, r'$x/L$', None)
    of.title(ax, r'Modos normales de una cuerda fija: $\sin\frac{n\pi x}{L}$')
    of.save(fig, 'modos_onda')


# ---------------------------------------------------------- 3. cono de dependencia (dAlembert)
def fig_cono_dependencia():
    fig, ax = of.new_fig(figsize=(6.6, 4.6)); of.style_axes(ax)
    c = 1.0
    # cono de dependencia (hacia abajo) desde P=(0,2)
    P = (0.0, 2.0)
    ax.fill([P[0]-c*P[1], P[0]+c*P[1], P[0]], [0, 0, P[1]], color=of.ACCENT, alpha=0.16)
    ax.plot([P[0], P[0]-c*P[1]], [P[1], 0], color=of.ACCENT, lw=2.2)
    ax.plot([P[0], P[0]+c*P[1]], [P[1], 0], color=of.ACCENT, lw=2.2)
    ax.plot(*P, 'o', color=of.ACCENT, ms=8, zorder=6)
    ax.text(P[0], P[1]+0.12, r'$(x_0,t_0)$', color=of.TEXT, ha='center', fontsize=11)
    ax.plot([P[0]-c*P[1], P[0]+c*P[1]], [0, 0], color=of.ACCENT, lw=3.5, alpha=0.5)
    ax.text(0, -0.35, r'dominio de dependencia $[x_0-ct_0,\,x_0+ct_0]$',
            color=of.TEXT, ha='center', fontsize=9)
    # cono de influencia (hacia arriba) desde Q=(3.5,0)
    Q = (3.5, 0.0); H = 2.6
    ax.fill([Q[0], Q[0]-c*H, Q[0]+c*H], [0, H, H], color=of.CURVE, alpha=0.16)
    ax.plot([Q[0], Q[0]-c*H], [0, H], color=of.CURVE, lw=2.2)
    ax.plot([Q[0], Q[0]+c*H], [0, H], color=of.CURVE, lw=2.2)
    ax.plot(*Q, 'o', color=of.CURVE, ms=8, zorder=6)
    ax.text(Q[0], H+0.12, r'cono de influencia', color=of.TEXT, ha='center', fontsize=9)
    ax.text(Q[0], -0.35, r'$(x_1,0)$', color=of.TEXT, ha='center', fontsize=10)
    ax.axhline(0, color=of.BROWN, lw=1.0)
    ax.set_xlim(-2.7, 6.4); ax.set_ylim(-0.6, 3.0)
    of.labels(ax, r'$x$', r'$t$')
    of.title(ax, r"d'Alembert: velocidad finita de propagación ($c=1$)")
    of.save(fig, 'cono_dependencia')


# ---------------------------------------------------------- 4. nucleo de Poisson
def fig_nucleo_poisson():
    fig, ax = of.new_fig(figsize=(6.6, 4.4)); of.style_axes(ax)
    phi = np.linspace(-np.pi, np.pi, 800)
    cols = [of.PALETTE[3], of.ACCENT, of.CURVE]
    for rho, c in zip([0.3, 0.6, 0.88], cols):
        K = (1-rho**2)/(1-2*rho*np.cos(phi)+rho**2)
        ax.plot(phi, K, color=c, lw=2.4, label=fr'$r/a={rho}$')
    ax.axhline(1, color=of.BROWN, lw=0.7, alpha=0.4, ls=':')
    ax.set_xlim(-np.pi, np.pi)
    ax.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
    ax.set_xticklabels([r'$-\pi$', r'$-\pi/2$', '0', r'$\pi/2$', r'$\pi$'])
    of.labels(ax, r'$\theta-\phi$', r'núcleo de Poisson $P$')
    of.title(ax, r'Núcleo de Poisson: se concentra al acercarse a la frontera')
    of.legend(ax, loc='upper right')
    of.save(fig, 'nucleo_poisson')


if __name__ == '__main__':
    print('Generando figuras EDP (ecuaciones clasicas):')
    fig_evolucion_calor()
    fig_modos_onda()
    fig_cono_dependencia()
    fig_nucleo_poisson()
    print('Listo.')
