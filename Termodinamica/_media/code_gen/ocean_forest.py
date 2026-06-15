"""
Estilo de gráficas para las notas del usuario — paleta y helpers compartidos.
Cópialo al code_gen/ del curso o impórtalo. Hex extraídos de los SVG del usuario.

Paleta por defecto: "ocean_forest". Para otro curso:
    import ocean_forest as of
    of.set_palette('ocean_forest')   # o añade tu paleta a PALETAS y selecciónala
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# --- Paletas disponibles (añade más por curso si quieres) ---
PALETAS = {
    'ocean_forest': dict(
        FIG_BG='#d8e4cc', PANEL='#f3f8ee', GRID='#6a8858', CURVE='#2e4824',
        ACCENT='#b07828', BROWN='#6a3e18', TICK='#4a2810', TEXT='#2e1a08',
        GRIDGY='#cccccc',
    ),
}

# Variables de módulo (se rellenan con set_palette); usa of.CURVE, of.PANEL, etc.
FIG_BG = PANEL = GRID = CURVE = ACCENT = BROWN = TICK = TEXT = GRIDGY = None
PALETTE = []   # tonos para familias de curvas


def set_palette(nombre='ocean_forest'):
    g = globals()
    g.update(PALETAS[nombre])
    g['PALETTE'] = [CURVE, ACCENT, BROWN, '#6a8858', '#9a7030', '#3a5a2a']


set_palette()   # ocean_forest por defecto


def setup():
    rcParams['font.family'] = 'DejaVu Sans'
    rcParams['mathtext.fontset'] = 'cm'   # matemática estilo LaTeX


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


def title(ax, s):  ax.set_title(s, color=TEXT, fontsize=12)


def labels(ax, x=None, y=None):
    if x: ax.set_xlabel(x, color=TEXT)
    if y: ax.set_ylabel(y, color=TEXT)


def legend(ax, **kw):
    kw.setdefault('facecolor', PANEL); kw.setdefault('edgecolor', GRIDGY)
    kw.setdefault('labelcolor', TEXT); kw.setdefault('framealpha', 0.85)
    ax.legend(**kw)


def splane(ax, xlim=(-3, 1), ylim=(-3, 3)):
    """Plano-s: ejes real/imag, aspecto igual, etiquetas sigma/jomega."""
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


def mag_phase(G):
    """Magnitud (dB) y fase (deg) SIN saltos — usa unwrap."""
    return 20*np.log10(np.abs(G)), np.degrees(np.unwrap(np.angle(G)))


def root_locus(num, den, Kmax=200, nK=4000):
    """Lugar de raíces de 1 + K num/den = 0 para K en [0, Kmax]."""
    num = np.atleast_1d(num).astype(float); den = np.atleast_1d(den).astype(float)
    Ks = np.linspace(1e-3, Kmax, nK); n = len(den)
    npad = np.zeros(n); npad[n-len(num):] = num
    R = np.zeros((nK, n-1), dtype=complex)
    for i, K in enumerate(Ks):
        R[i] = np.roots(den + K*npad)
    return R


def save(fig, name, subdir='img_gen'):
    """Guarda el SVG en <code_gen>/../img_gen/name.svg (relativo a este archivo)."""
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, '..', subdir, name + '.svg')
    os.makedirs(os.path.dirname(out), exist_ok=True)
    fig.savefig(out, facecolor=FIG_BG, bbox_inches='tight')
    plt.close(fig)
    print('  ->', name + '.svg')
