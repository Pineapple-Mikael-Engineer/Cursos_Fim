import numpy as np
import ocean_forest as of


def fig_diagrama_fasorial():
    fig, ax = of.new_fig(figsize=(6.2, 5.0)); of.style_axes(ax)
    ax.axhline(0, color=of.BROWN, lw=1.0); ax.axvline(0, color=of.BROWN, lw=1.0)
    VR, VL = 0.6, 0.8
    # I reference (corta)
    ax.annotate('', xy=(0.32, 0), xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=of.GRID, lw=2.0))
    ax.text(0.33, -0.07, r'$\overline{I}$ (ref)', color=of.TEXT, fontsize=10)
    # V_R en fase con I
    ax.annotate('', xy=(VR, 0), xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=of.ACCENT, lw=2.6))
    ax.text(VR/2-0.02, -0.09, r'$\overline{V}_R$', color=of.ACCENT, fontsize=12)
    # V_L 90 desde la punta de V_R
    ax.annotate('', xy=(VR, VL), xytext=(VR, 0), arrowprops=dict(arrowstyle='-|>', color=of.BROWN, lw=2.6))
    ax.text(VR+0.03, VL/2, r'$\overline{V}_L$', color=of.BROWN, fontsize=12)
    # V suma
    ax.annotate('', xy=(VR, VL), xytext=(0, 0), arrowprops=dict(arrowstyle='-|>', color=of.CURVE, lw=2.9))
    ax.text(VR/2-0.16, VL/2+0.04, r'$\overline{V}=\overline{V}_R+\overline{V}_L$', color=of.CURVE, fontsize=12, rotation=53)
    # angulo
    arc = np.linspace(0, np.arctan2(VL, VR), 40)
    ax.plot(0.2*np.cos(arc), 0.2*np.sin(arc), color=of.GRID, lw=1.4)
    ax.text(0.23, 0.07, r'$\varphi$', color=of.TEXT, fontsize=12)
    ax.set_xlim(-0.15, 0.95); ax.set_ylim(-0.2, 0.95); ax.set_aspect('equal')
    of.labels(ax, r'Re', r'Im')
    of.title(ax, r'Diagrama fasorial de un RL serie ($\overline{V}$ adelanta a $\overline{I}$)')
    of.save(fig, 'diagrama_fasorial')


if __name__ == '__main__':
    fig_diagrama_fasorial()
    print('listo')
