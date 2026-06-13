#!/usr/bin/env python3
"""Figuras del capitulo Ecuaciones Integrales.
Estilo Ocean Forest. Salida -> ../img_gen/*.svg"""
import numpy as np
import ocean_forest as of


# ---------------------------------------------------------- tautocrona (cicloide de Abel)
def fig_abel_tautocrona():
    fig, ax = of.new_fig(figsize=(6.8, 4.4)); of.style_axes(ax)
    a = 1.0
    th = np.linspace(0, 2*np.pi, 500)
    x = a*(th - np.sin(th))
    y = -a*(1 - np.cos(th))            # cicloide invertida (valle)
    ax.plot(x, y, color=of.CURVE, lw=2.8, zorder=3)
    # fondo (theta = pi)
    xb, yb = a*np.pi, -2*a
    ax.plot(xb, yb, 'o', color=of.BROWN, ms=8, zorder=5)
    ax.text(xb, yb-0.22, 'fondo', color=of.TEXT, ha='center', fontsize=10)
    # cuentas a distintas alturas que llegan al fondo en el mismo tiempo
    cols = [of.ACCENT, of.PALETTE[3], of.BROWN]
    for thb, c in zip([0.45*np.pi, 0.7*np.pi, 1.45*np.pi], cols):
        xb0 = a*(thb - np.sin(thb)); yb0 = -a*(1 - np.cos(thb))
        ax.plot(xb0, yb0, 'o', color=c, ms=12, zorder=6)
        ax.annotate('', xy=(xb + 0.25*np.sign(np.pi-thb), yb+0.18),
                    xytext=(xb0, yb0),
                    arrowprops=dict(arrowstyle='->', color=c, lw=1.8,
                                    connectionstyle="arc3,rad=0.15"))
    ax.text(a*np.pi, 0.15,
            r'cuentas soltadas a alturas distintas $\to$ mismo tiempo de bajada $T_0$',
            color=of.TEXT, ha='center', fontsize=10)
    ax.text(0.2, -2.55, r'$f(x)=\int_0^x \dfrac{\varphi(t)}{\sqrt{x-t}}\,dt$  (ecuación de Abel)',
            color=of.TICK, fontsize=10)
    ax.set_xlim(-0.4, 2*np.pi*a+0.4); ax.set_ylim(-2.9, 0.6)
    ax.set_aspect('equal')
    of.labels(ax, r'$x$', r'$y$')
    of.title(ax, r'La tautócrona de Abel: una cicloide isócrona')
    of.save(fig, 'abel_tautocrona')


if __name__ == '__main__':
    print('Generando figura abel_tautocrona:')
    fig_abel_tautocrona()
    print('Listo.')
