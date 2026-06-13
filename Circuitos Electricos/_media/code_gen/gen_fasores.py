import numpy as np
import ocean_forest as of


def _arrow(ax, ang_deg, r, c, lw=2.5):
    a = np.deg2rad(ang_deg)
    ax.annotate('', xy=(r*np.cos(a), r*np.sin(a)), xytext=(0, 0),
                arrowprops=dict(arrowstyle='-|>', color=c, lw=lw))
    return r*np.cos(a), r*np.sin(a)


def fig_fasor_diagrama():
    fig, ax = of.new_fig(figsize=(5.8, 5.2)); of.style_axes(ax)
    ax.axhline(0, color=of.BROWN, lw=1.0); ax.axvline(0, color=of.BROWN, lw=1.0)
    V = 1.0; phi = np.deg2rad(35)
    x, y = V*np.cos(phi), V*np.sin(phi)
    _arrow(ax, 35, V, of.CURVE, 2.8)
    ax.text(x*0.5-0.05, y*0.5+0.07, r'$\overline{V}=V\angle\varphi$', color=of.TEXT, fontsize=12.5, rotation=35)
    arc = np.linspace(0, phi, 40)
    ax.plot(0.3*np.cos(arc), 0.3*np.sin(arc), color=of.ACCENT, lw=1.6)
    ax.text(0.37, 0.09, r'$\varphi$', color=of.TEXT, fontsize=13)
    ax.plot([x, x], [0, y], color=of.GRID, lw=1.0, ls='--')
    ax.plot([0, x], [y, y], color=of.GRID, lw=1.0, ls='--')
    ax.text(x/2, -0.11, r'$V\cos\varphi$', color=of.TEXT, fontsize=9.5, ha='center')
    ax.text(x+0.03, y/2, r'$V\operatorname{sen}\varphi$', color=of.TEXT, fontsize=9.5)
    ax.set_xlim(-0.3, 1.28); ax.set_ylim(-0.3, 1.12); ax.set_aspect('equal')
    of.labels(ax, r'Re (eje real)', r'Im (eje imaginario)')
    of.title(ax, r'Fasor: $\overline{V}=V\angle\varphi=V\,e^{j\varphi}$')
    of.save(fig, 'fasor_diagrama')


def fig_fasores_RLC():
    fig, axs = of.plt.subplots(1, 3, figsize=(8.6, 3.3))
    fig.patch.set_facecolor(of.PANEL)
    specs = [
        (r'Resistencia: $v,i$ en fase', [(0, 0.92, 'V', of.ACCENT, 0.16), (0, 0.6, 'I', of.CURVE, -0.2)]),
        (r'Inductor: $v$ adelanta $90^\circ$ a $i$', [(90, 0.9, 'V', of.ACCENT, 0.0), (0, 0.75, 'I', of.CURVE, -0.18)]),
        (r'Condensador: $i$ adelanta $90^\circ$ a $v$', [(0, 0.75, 'V', of.ACCENT, -0.18), (90, 0.9, 'I', of.CURVE, 0.0)]),
    ]
    for ax, (title, arrows) in zip(axs, specs):
        of.style_axes(ax)
        ax.axhline(0, color=of.GRID, lw=0.9); ax.axvline(0, color=of.GRID, lw=0.9)
        for ang, r, lab, c, off in arrows:
            x, y = _arrow(ax, ang, r, c, 2.6)
            ax.text(x*1.08+(0.05 if ang == 0 else 0.06), y*1.08+off, r'$\overline{%s}$' % lab, color=c, fontsize=13)
        ax.set_xlim(-1.05, 1.15); ax.set_ylim(-0.55, 1.15); ax.set_aspect('equal')
        ax.set_title(title, color=of.TEXT, fontsize=9.5)
    fig.tight_layout(); of.save(fig, 'fasores_RLC')


def fig_tiempo_frecuencia():
    fig, (a1, a2) = of.plt.subplots(1, 2, figsize=(8.6, 3.7), gridspec_kw={'width_ratios': [1.7, 1]})
    fig.patch.set_facecolor(of.PANEL)
    for ax in (a1, a2): of.style_axes(ax)
    t = np.linspace(0, 2*np.pi, 400); phi = np.deg2rad(35)
    a1.plot(t, np.sin(t+phi), color=of.CURVE, lw=2.6)
    a1.axhline(0, color=of.GRID, lw=0.8)
    a1.set_title(r'dominio del tiempo:  $v=V_m\operatorname{sen}(\omega t+\varphi)$', color=of.TEXT, fontsize=10)
    a1.set_xlabel(r'$\omega t$'); a1.set_xlim(0, 2*np.pi); a1.set_ylim(-1.2, 1.2)
    a2.axhline(0, color=of.BROWN, lw=1.0); a2.axvline(0, color=of.BROWN, lw=1.0)
    x, y = _arrow(a2, 35, 1.0, of.ACCENT, 2.7)
    a2.text(x*0.45-0.05, y*0.45+0.1, r'$\overline{V}=V\angle\varphi$', color=of.TEXT, fontsize=11, rotation=35)
    arc = np.linspace(0, phi, 30); a2.plot(0.28*np.cos(arc), 0.28*np.sin(arc), color=of.CURVE, lw=1.4)
    a2.set_xlim(-0.35, 1.2); a2.set_ylim(-0.35, 1.12); a2.set_aspect('equal')
    a2.set_title('dominio de la frecuencia:  fasor', color=of.TEXT, fontsize=10)
    fig.tight_layout(); of.save(fig, 'tiempo_frecuencia')


if __name__ == '__main__':
    fig_fasor_diagrama(); fig_fasores_RLC(); fig_tiempo_frecuencia()
    print('listo')
