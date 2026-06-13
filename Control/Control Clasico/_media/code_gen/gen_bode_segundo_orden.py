#!/usr/bin/env python3
"""
Genera: bode_segundo_orden.svg  (en ../img_gen/)
Estilo: paleta "Ocean Forest" extraída de los SVG de lugar de raíces del usuario.
Uso:    python3 gen_bode_segundo_orden.py
Requiere: numpy, matplotlib
"""
import os
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rcParams

# --- Paleta "Ocean Forest" (hex exactos de los SVG del usuario) ---
FIG_BG = '#d8e4cc'   # fondo figura
PANEL  = '#f3f8ee'   # fondo panel (axes)
GRID   = '#6a8858'   # grid verde
CURVE  = '#2e4824'   # curva (verde oscuro)
ACCENT = '#b07828'   # asíntotas / marcadores (dorado)
BROWN  = '#6a3e18'   # ejes / polos
TICK   = '#4a2810'   # números de eje
TEXT   = '#2e1a08'   # título / etiquetas

rcParams['font.family'] = 'DejaVu Sans'
rcParams['mathtext.fontset'] = 'cm'   # math tipo LaTeX (Computer Modern)


def estilo(ax):
    ax.set_facecolor(PANEL)
    ax.grid(True, which='both', ls='--', dashes=(3.7, 1.6), color=GRID, alpha=0.25)
    for sp in ax.spines.values():
        sp.set_color(BROWN); sp.set_linewidth(1.0)
    ax.tick_params(colors=TICK, which='both')
    for lbl in ax.get_xticklabels() + ax.get_yticklabels():
        lbl.set_color(TICK)


def main():
    wn, zeta = 1.0, 0.3
    w = np.logspace(-1, 1, 600)
    s = 1j * w
    G = wn**2 / (s**2 + 2*zeta*wn*s + wn**2)
    mag = 20*np.log10(np.abs(G))
    phase = np.degrees(np.angle(G))
    asy = np.where(w < wn, 0.0, -40*np.log10(w/wn))   # asíntotas 0 / -40 dB/dec

    fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(6.4, 5.6), sharex=True,
                                   facecolor=FIG_BG)

    ax1.semilogx(w, mag, color=CURVE, lw=2, solid_capstyle='round', label='Magnitud')
    ax1.semilogx(w, asy, color=ACCENT, lw=2, ls='--', dashes=(7.4, 3.2),
                 alpha=0.85, label='Asíntotas')
    ax1.axvline(wn, color=ACCENT, lw=1.2, ls=':', alpha=0.7)
    ax1.plot(wn, 20*np.log10(1/(2*zeta)), '*', color=ACCENT, ms=14, label=r'Pico $M_r$')
    ax1.set_ylabel('Magnitud [dB]', color=TEXT)
    ax1.set_title(r'Bode de $G(s)=\dfrac{\omega_n^2}{s^2+2\zeta\omega_n s+\omega_n^2}$'
                  + r'  $(\zeta=0.3)$', color=TEXT, fontsize=12)
    ax1.legend(facecolor=PANEL, edgecolor='#cccccc', labelcolor=TEXT, framealpha=0.85)
    estilo(ax1)

    ax2.semilogx(w, phase, color=CURVE, lw=2, solid_capstyle='round')
    ax2.axvline(wn, color=ACCENT, lw=1.2, ls=':', alpha=0.7)
    ax2.axhline(-90, color=BROWN, lw=0.8, alpha=0.5)
    ax2.annotate(r'$\omega_n$', (wn, -90), color=TEXT, fontsize=11,
                 xytext=(6, 6), textcoords='offset points')
    ax2.set_ylabel('Fase [°]', color=TEXT)
    ax2.set_xlabel(r'$\omega$ [rad/s]', color=TEXT)
    ax2.set_yticks([0, -45, -90, -135, -180])
    estilo(ax2)

    plt.tight_layout()
    here = os.path.dirname(os.path.abspath(__file__))
    out = os.path.join(here, '..', 'img_gen', 'bode_segundo_orden.svg')
    plt.savefig(out, facecolor=FIG_BG)
    print('guardado:', os.path.normpath(out))


if __name__ == '__main__':
    main()
