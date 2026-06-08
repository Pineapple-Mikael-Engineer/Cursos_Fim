#!/usr/bin/env python3
"""Figuras del bloque Lineales de Orden Superior — Oscilaciones.
Estilo Ocean Forest. Salida -> ../img_gen/*.svg"""
import numpy as np
import ocean_forest as of


# ---------------------------------------------------------- 1. regímenes de amortiguamiento
def fig_oscilador_regimenes():
    fig, ax = of.new_fig(figsize=(6.6, 4.4)); of.style_axes(ax)
    t = np.linspace(0, 12, 700)
    w0 = 1.0
    # subamortiguado zeta=0.2
    z = 0.2; wd = w0*np.sqrt(1-z**2)
    x_sub = np.exp(-z*w0*t)*(np.cos(wd*t) + (z*w0/wd)*np.sin(wd*t))
    # crítico zeta=1
    x_cri = (1 + w0*t)*np.exp(-w0*t)
    # sobreamortiguado zeta=2
    z = 2.0; r1 = -z*w0 + w0*np.sqrt(z**2-1); r2 = -z*w0 - w0*np.sqrt(z**2-1)
    A = r2/(r2-r1); B = 1-A
    x_sob = A*np.exp(r1*t) + B*np.exp(r2*t)

    ax.axhline(0, color=of.BROWN, lw=0.9, alpha=0.6)
    ax.plot(t, x_sub, color=of.CURVE, lw=2.3, label=r'subamortiguado ($\zeta=0.2$)')
    ax.plot(t, x_cri, color=of.ACCENT, lw=2.3, label=r'crítico ($\zeta=1$)')
    ax.plot(t, x_sob, color=of.BROWN, lw=2.3, ls='--', label=r'sobreamortiguado ($\zeta=2$)')
    ax.set_xlim(0, 12); ax.set_ylim(-0.6, 1.05)
    of.labels(ax, r'$t$', r'$x(t)$')
    of.title(ax, r'Oscilador libre: $\ddot x+2\zeta\omega_0\dot x+\omega_0^2x=0,\ x(0)=1,\ \dot x(0)=0$')
    of.legend(ax, loc='upper right')
    of.save(fig, 'oscilador_regimenes')


# ---------------------------------------------------------- 2. curva de resonancia A(w)
def fig_curva_resonancia():
    fig, ax = of.new_fig(figsize=(6.4, 4.5)); of.style_axes(ax)
    w = np.linspace(0, 2.5, 600)
    m = k = F0 = 1.0   # w0 = 1
    cols = of.PALETTE
    for i, c in enumerate([0.15, 0.3, 0.5, 1.0]):
        A = F0/np.sqrt((k - m*w**2)**2 + (c*w)**2)
        ax.plot(w, A, color=cols[i % len(cols)], lw=2.2,
                label=fr'$c={c}$')
    ax.axvline(1.0, color=of.BROWN, ls=':', lw=1.0, alpha=0.5)
    ax.annotate(r'$\omega\approx\omega_0$', xy=(1.0, 0.3), xytext=(1.35, 1.2),
                color=of.TEXT, fontsize=10,
                arrowprops=dict(arrowstyle='->', color=of.BROWN))
    ax.set_xlim(0, 2.5); ax.set_ylim(0, 3.6)
    of.labels(ax, r'$\omega$', r'amplitud $A(\omega)$')
    of.title(ax, r'Curva de resonancia: $A(\omega)=F_0/\sqrt{(k-m\omega^2)^2+(c\omega)^2}$')
    of.legend(ax, loc='upper right')
    of.save(fig, 'curva_resonancia')


# ---------------------------------------------------------- 3. resonancia pura en el tiempo
def fig_resonancia_tiempo():
    fig, ax = of.new_fig(figsize=(6.8, 4.2)); of.style_axes(ax)
    t = np.linspace(0, 30, 1200)
    x = 0.5*t*np.sin(t)           # F0=m=w0=1  ->  x = (1/2) t sin t
    ax.plot(t, x, color=of.CURVE, lw=1.8, label=r'$x=\frac{F_0}{2m\omega_0}\,t\,\sin\omega_0 t$')
    ax.plot(t, 0.5*t, color=of.ACCENT, lw=1.6, ls='--', label=r'envolvente $\pm t/2$')
    ax.plot(t, -0.5*t, color=of.ACCENT, lw=1.6, ls='--')
    ax.axhline(0, color=of.BROWN, lw=0.9, alpha=0.6)
    ax.set_xlim(0, 30); ax.set_ylim(-16, 16)
    of.labels(ax, r'$t$', r'$x(t)$')
    of.title(ax, r'Resonancia pura ($\omega=\omega_0$, sin amortiguamiento)')
    of.legend(ax, loc='upper left')
    of.save(fig, 'resonancia_tiempo')


if __name__ == '__main__':
    print('Generando figuras de oscilaciones:')
    fig_oscilador_regimenes()
    fig_curva_resonancia()
    fig_resonancia_tiempo()
    print('Listo.')
