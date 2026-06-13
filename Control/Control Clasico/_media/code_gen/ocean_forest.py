"""
Estilo "Ocean Forest" — paleta y helpers compartidos para las gráficas.
Hex extraídos de los SVG de lugar de raíces del usuario.
Importado por los demás scripts de code_gen/.
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# --- Paleta ---
FIG_BG = '#d8e4cc'   # fondo figura
PANEL  = '#f3f8ee'   # fondo panel (axes)
GRID   = '#6a8858'   # grid verde
CURVE  = '#2e4824'   # curva principal (verde oscuro)
ACCENT = '#b07828'   # asíntotas / marcadores / segunda curva (dorado)
BROWN  = '#6a3e18'   # ejes / polos
TICK   = '#4a2810'   # números de eje
TEXT   = '#2e1a08'   # título / etiquetas
GRIDGY = '#cccccc'   # borde de leyenda

# Curvas secundarias (familias): tonos derivados de la paleta
PALETTE = [CURVE, ACCENT, BROWN, '#6a8858', '#9a7030', '#3a5a2a']


def setup():
    rcParams['font.family'] = 'DejaVu Sans'
    rcParams['mathtext.fontset'] = 'cm'   # math estilo LaTeX (Computer Modern)


def style_axes(ax):
    ax.set_facecolor(PANEL)
    ax.grid(True, which='both', ls='--', dashes=(3.7, 1.6), color=GRID, alpha=0.25)
    for sp in ax.spines.values():
        sp.set_color(BROWN); sp.set_linewidth(1.0)
    ax.tick_params(colors=TICK, which='both')
    for lbl in ax.get_xticklabels() + ax.get_yticklabels():
        lbl.set_color(TICK)


def new_fig(**kw):
    setup()
    kw.setdefault('facecolor', FIG_BG)
    return plt.subplots(**kw)


def title(ax, s):
    ax.set_title(s, color=TEXT, fontsize=12)


def labels(ax, x=None, y=None):
    if x: ax.set_xlabel(x, color=TEXT)
    if y: ax.set_ylabel(y, color=TEXT)


def legend(ax, **kw):
    kw.setdefault('facecolor', PANEL)
    kw.setdefault('edgecolor', GRIDGY)
    kw.setdefault('labelcolor', TEXT)
    kw.setdefault('framealpha', 0.85)
    ax.legend(**kw)


def splane(ax, xlim=(-3, 1), ylim=(-3, 3)):
    """Configura un plano-s: ejes real/imag, aspecto, etiquetas."""
    style_axes(ax)
    ax.axhline(0, color=BROWN, lw=1.0, alpha=0.7)
    ax.axvline(0, color=BROWN, lw=1.0, alpha=0.7)
    ax.set_xlim(*xlim); ax.set_ylim(*ylim)
    ax.set_aspect('equal', adjustable='box')
    labels(ax, r'$\sigma$', r'$j\omega$')


def pole(ax, p, **kw):
    kw.setdefault('color', BROWN); kw.setdefault('ms', 11); kw.setdefault('mew', 3)
    ax.plot(np.real(p), np.imag(p), 'x', **kw)


def zero(ax, z, **kw):
    kw.setdefault('mec', BROWN); kw.setdefault('mfc', 'none')
    kw.setdefault('ms', 11); kw.setdefault('mew', 2)
    ax.plot(np.real(z), np.imag(z), 'o', **kw)


def save(fig, name):
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, '..', 'img_gen', name + '.svg')
    fig.savefig(out, facecolor=FIG_BG, bbox_inches='tight')
    plt.close(fig)
    print('  ->', name + '.svg')
