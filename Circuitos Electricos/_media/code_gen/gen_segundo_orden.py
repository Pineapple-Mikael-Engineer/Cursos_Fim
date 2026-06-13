import numpy as np
import ocean_forest as of


def fig_amortiguamiento():
    fig, ax = of.new_fig(figsize=(6.9, 4.5)); of.style_axes(ax)
    t = np.linspace(0, 12, 900); w0 = 1.0
    for zeta, c, lab, ls in [(0.25, of.CURVE, r'subamortiguado $\zeta=0.25$', '-'),
                             (1.0, of.ACCENT, r'crítico $\zeta=1$', '--'),
                             (2.5, of.BROWN, r'sobreamortiguado $\zeta=2.5$', '-.')]:
        if zeta < 1:
            wd = w0*np.sqrt(1-zeta**2)
            x = 1-np.exp(-zeta*w0*t)*(np.cos(wd*t)+(zeta/np.sqrt(1-zeta**2))*np.sin(wd*t))
        elif zeta == 1:
            x = 1-np.exp(-w0*t)*(1+w0*t)
        else:
            s1 = -zeta*w0+w0*np.sqrt(zeta**2-1); s2 = -zeta*w0-w0*np.sqrt(zeta**2-1)
            x = 1-(s2*np.exp(s1*t)-s1*np.exp(s2*t))/(s2-s1)
        ax.plot(t, x, color=c, lw=2.7, ls=ls, label=lab)
    ax.axhline(1, color=of.GRID, lw=0.9, ls='--')
    ax.set_xlim(0, 12); ax.set_ylim(0, 1.45)
    of.labels(ax, r'$\omega_0 t$', r'respuesta (normalizada)')
    of.title(ax, r'Los tres regímenes de amortiguamiento (respuesta al escalón)')
    of.legend(ax, loc='lower right')
    of.save(fig, 'amortiguamiento')


def fig_oscilacion_amortiguada():
    fig, ax = of.new_fig(figsize=(6.9, 4.0)); of.style_axes(ax)
    t = np.linspace(0, 12, 900); alpha = 0.32; wd = 2.0
    env = np.exp(-alpha*t); x = env*np.cos(wd*t)
    ax.plot(t, x, color=of.CURVE, lw=2.4, label=r'$e^{-\alpha t}\cos(\omega_d t)$')
    ax.plot(t, env, color=of.BROWN, lw=1.5, ls='--', label=r'envolvente $\pm e^{-\alpha t}$')
    ax.plot(t, -env, color=of.BROWN, lw=1.5, ls='--')
    ax.axhline(0, color=of.GRID, lw=0.7)
    ax.set_xlim(0, 12); ax.set_ylim(-1.1, 1.15)
    of.labels(ax, r'$t$', r'$x(t)$')
    of.title(ax, r'Oscilación amortiguada (subamortiguado): $e^{-\alpha t}\cos\omega_d t$')
    of.legend(ax, loc='upper right')
    of.save(fig, 'oscilacion_amortiguada')


def fig_funciones_singulares():
    fig, (a1, a2, a3) = of.plt.subplots(1, 3, figsize=(8.6, 3.0))
    fig.patch.set_facecolor(of.PANEL)
    for ax in (a1, a2, a3): of.style_axes(ax)
    t = np.linspace(-1, 3, 500)
    a1.plot(t, np.where(t >= 0, 1.0, 0.0), color=of.CURVE, lw=2.6)
    a1.set_title(r'escalón $u(t)$', color=of.TEXT, fontsize=11.5); a1.set_ylim(-0.3, 1.6)
    a2.plot(t, np.zeros_like(t), color=of.CURVE, lw=1.8)
    a2.annotate('', xy=(0, 1.2), xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=of.ACCENT, lw=2.6))
    a2.text(0.12, 1.05, r'$(1)$', color=of.TEXT, fontsize=10)
    a2.set_title(r'impulso $\delta(t)$', color=of.TEXT, fontsize=11.5); a2.set_ylim(-0.3, 1.6)
    a3.plot(t, np.where(t >= 0, t, 0.0), color=of.CURVE, lw=2.6)
    a3.set_title(r'rampa $r(t)=t\,u(t)$', color=of.TEXT, fontsize=11.5); a3.set_ylim(-0.3, 3)
    for ax in (a1, a2, a3):
        ax.set_xlabel(r'$t$', fontsize=10); ax.axvline(0, color=of.GRID, lw=0.7, ls=':')
    fig.tight_layout(); of.save(fig, 'funciones_singulares')


if __name__ == '__main__':
    fig_amortiguamiento(); fig_oscilacion_amortiguada(); fig_funciones_singulares()
    print('listo')
