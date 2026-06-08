#!/usr/bin/env python3
"""Figuras de los fundamentos de EDP: características y serie de Fourier.
Estilo Ocean Forest. Salida -> ../img_gen/*.svg"""
import numpy as np
import ocean_forest as of


# ---------------------------------------------------------- 1. características (transporte)
def fig_caracteristicas():
    fig, ax = of.new_fig(figsize=(6.6, 4.6)); of.style_axes(ax)
    c = 1.5
    T = 4.0
    tt = np.array([0, T])
    # haz de características x = x0 + c t  (en el plano x-t)
    for i, x0 in enumerate(np.arange(-3, 9.5, 1.0)):
        xs = x0 + c*tt
        ax.plot(xs, tt, color=of.GRID, lw=1.3, alpha=0.85)
    # tres características destacadas que transportan un valor
    for x0, col in [(0.0, of.CURVE), (1.0, of.ACCENT), (2.0, of.BROWN)]:
        xs = x0 + c*tt
        ax.plot(xs, tt, color=col, lw=2.6)
        ax.annotate('', xy=(x0+c*T, T), xytext=(x0+c*(T-1.1), T-1.1),
                    arrowprops=dict(arrowstyle='-|>', color=col, lw=2.4))
    # perfil inicial f(x) dibujado sobre t=0 (pequeño, escalado) y transportado a t=T
    xg = np.linspace(-3, 9.5, 400)
    f = 0.8*np.exp(-((xg-1.0)/0.6)**2)
    ax.plot(xg, f*0.0, color=of.TICK, lw=0)            # base
    ax.fill_between(xg, 0, 0.7*np.exp(-((xg-1.0)/0.6)**2), color=of.ACCENT, alpha=0.18)
    ax.fill_between(xg, T, T+0.7*np.exp(-((xg-1.0-c*T)/0.6)**2), color=of.ACCENT, alpha=0.18)
    ax.text(1.0, 0.85, r'$f(x)$', color=of.TICK, ha='center', fontsize=10)
    ax.text(1.0+c*T, T+0.85, r'$f(x-cT)$', color=of.TICK, ha='center', fontsize=10)
    ax.text(7.4, 1.7, r'$u$ constante' '\n' r'sobre $x-ct=$cte', color=of.TEXT, fontsize=10)
    ax.set_xlim(-3, 9.5); ax.set_ylim(-0.1, T+1.2)
    of.labels(ax, r'$x$', r'$t$')
    of.title(ax, r"Características de $u_t+c\,u_x=0$:  $u(x,t)=f(x-ct)$")
    of.save(fig, 'caracteristicas')


# ---------------------------------------------------------- 2. serie de Fourier (onda cuadrada)
def fig_serie_fourier():
    fig, ax = of.new_fig(figsize=(6.8, 4.4)); of.style_axes(ax)
    x = np.linspace(-np.pi, np.pi, 2000)

    def parcial(x, K):                # K armónicos impares
        s = np.zeros_like(x)
        for k in range(1, K+1):
            n = 2*k-1
            s += np.sin(n*x)/n
        return (4/np.pi)*s

    # onda cuadrada objetivo
    sq = np.sign(x)
    ax.plot(x, sq, color=of.BROWN, lw=2.2, label=r'onda cuadrada $\operatorname{sgn}x$')
    cols = [of.PALETTE[3], of.PALETTE[2], of.ACCENT, of.CURVE]
    for (K, lbl), col in zip([(1, '$N=1$'), (3, '$N=3$'), (7, '$N=7$'), (20, '$N=20$')], cols):
        ax.plot(x, parcial(x, K), color=col, lw=1.5,
                ls='-' if K == 20 else '--', label=lbl)
    ax.axhline(0, color=of.BROWN, lw=0.7, alpha=0.4)
    ax.annotate('Gibbs\n($\\approx9\\%$)', xy=(0.18, 1.18), xytext=(1.0, 1.55),
                color=of.TEXT, fontsize=9,
                arrowprops=dict(arrowstyle='->', color=of.BROWN))
    ax.set_xlim(-np.pi, np.pi); ax.set_ylim(-1.6, 1.8)
    ax.set_xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi])
    ax.set_xticklabels([r'$-\pi$', r'$-\pi/2$', '0', r'$\pi/2$', r'$\pi$'])
    of.labels(ax, r'$x$', r'$f(x)$')
    of.title(ax, r'Serie de Fourier de una onda cuadrada (sumas parciales)')
    of.legend(ax, loc='lower right', ncol=2)
    of.save(fig, 'serie_fourier')


if __name__ == '__main__':
    print('Generando figuras EDP (fundamentos):')
    fig_caracteristicas()
    fig_serie_fourier()
    print('Listo.')
