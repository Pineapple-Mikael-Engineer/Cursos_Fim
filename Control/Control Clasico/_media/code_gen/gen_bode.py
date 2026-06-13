#!/usr/bin/env python3
"""Genera las gráficas de Bode (en ../img_gen/). Uso: python3 gen_bode.py"""
import numpy as np
import ocean_forest as of


def bode_axes():
    fig, (a1, a2) = of.new_fig(nrows=2, ncols=1, figsize=(6.4, 5.6), sharex=True)
    of.style_axes(a1); of.style_axes(a2)
    of.labels(a1, y='Magnitud [dB]')
    of.labels(a2, x=r'$\omega$ [rad/s]', y='Fase [°]')
    return fig, a1, a2


def mag_phase(G):
    return 20*np.log10(np.abs(G)), np.degrees(np.unwrap(np.angle(G)))


# ---------- factores básicos ----------
def factores_basicos():
    w = np.logspace(-2, 2, 600)
    fig, a1, a2 = bode_axes()
    factores = {
        r'$K=10$':            10*np.ones_like(w*1j),
        r'Integrador $1/j\omega$': 1/(1j*w),
        r'Polo $1/(1+j\omega)$':   1/(1+1j*w),
        r'Cero $1+j\omega$':       1+1j*w,
    }
    for (lbl, G), c in zip(factores.items(), of.PALETTE):
        m, p = mag_phase(G)
        a1.semilogx(w, m, color=c, lw=2, label=lbl)
        a2.semilogx(w, p, color=c, lw=2)
    a1.set_ylim(-40, 40); a2.set_yticks([-90, -45, 0, 45, 90])
    of.title(a1, 'Factores básicos de Bode')
    of.legend(a1, fontsize=8, loc='lower left')
    of.save(fig, 'bode_factores_basicos')


# ---------- segundo orden variando zeta ----------
def segundo_orden_zeta():
    wn = 1.0; w = np.logspace(-1, 1, 600)
    fig, a1, a2 = bode_axes()
    for z, c in zip([0.1, 0.3, 0.707, 1.5], of.PALETTE):
        G = wn**2/((1j*w)**2 + 2*z*wn*(1j*w) + wn**2)
        m, p = mag_phase(G)
        a1.semilogx(w, m, color=c, lw=2, label=rf'$\zeta={z}$')
        a2.semilogx(w, p, color=c, lw=2)
    a1.axvline(wn, color=of.ACCENT, lw=1, ls=':', alpha=0.6)
    a2.set_yticks([0, -45, -90, -135, -180])
    of.title(a1, r'Segundo orden: efecto de $\zeta$ (pico resonante)')
    of.legend(a1, fontsize=9)
    of.save(fig, 'bode_segundo_orden_zeta')


# ---------- construcción asintótica ----------
def construccion_asintotica():
    w = np.logspace(-1, 2.5, 700)
    G = 10/((1j*w)*(1+1j*w/10))   # K=10, integrador, polo en 10
    m, p = mag_phase(G)
    asy = 20*np.log10(10) - 20*np.log10(w) - np.where(w > 10, 20*np.log10(w/10), 0)
    fig, a1, a2 = bode_axes()
    a1.semilogx(w, m, color=of.CURVE, lw=2, label='Real')
    a1.semilogx(w, asy, color=of.ACCENT, lw=2, ls='--', dashes=(7.4, 3.2), label='Asíntotas')
    a1.axvline(10, color=of.BROWN, lw=1, ls=':', alpha=0.5)
    a2.semilogx(w, p, color=of.CURVE, lw=2)
    a2.set_yticks([-90, -135, -180])
    of.title(a1, r'Construcción asintótica: $G(s)=\dfrac{100}{s(s+10)}$')
    of.legend(a1, fontsize=9)
    of.save(fig, 'bode_construccion_asintotica')


# ---------- corrección de esquina ----------
def correccion_esquina():
    w = np.logspace(-1, 1, 600); w0 = 1.0
    G = 1/(1+1j*w/w0)
    m, _ = mag_phase(G)
    asy = np.where(w > w0, -20*np.log10(w/w0), 0)
    fig, (ax) = of.new_fig(figsize=(6.2, 4.2))
    of.style_axes(ax)
    ax.semilogx(w, m, color=of.CURVE, lw=2, label='Real')
    ax.semilogx(w, asy, color=of.ACCENT, lw=2, ls='--', dashes=(7.4, 3.2), label='Asíntota')
    ax.plot(w0, -3, '*', color=of.ACCENT, ms=14)
    ax.annotate('-3 dB', (w0, -3), color=of.TEXT, xytext=(8, 4), textcoords='offset points')
    of.labels(ax, r'$\omega$ [rad/s]', 'Magnitud [dB]')
    of.title(ax, 'Corrección en la frecuencia de esquina (polo simple)')
    of.legend(ax, fontsize=9)
    of.save(fig, 'bode_correccion_esquina')


# ---------- pico resonante ----------
def pico_resonante():
    wn = 1.0; w = np.logspace(-1, 1, 600)
    fig, (ax) = of.new_fig(figsize=(6.2, 4.2)); of.style_axes(ax)
    for z, c in zip([0.1, 0.25, 0.5], of.PALETTE):
        m, _ = mag_phase(wn**2/((1j*w)**2 + 2*z*wn*(1j*w) + wn**2))
        ax.semilogx(w, m, color=c, lw=2, label=rf'$\zeta={z}$')
        wr = wn*np.sqrt(1-2*z**2)
        Mr = 20*np.log10(1/(2*z*np.sqrt(1-z**2)))
        ax.plot(wr, Mr, '*', color=of.ACCENT, ms=13)
    asy = np.where(w > wn, -40*np.log10(w/wn), 0)
    ax.semilogx(w, asy, color=of.BROWN, lw=1.2, ls='--', alpha=0.6, label='Asíntota')
    of.labels(ax, r'$\omega$ [rad/s]', 'Magnitud [dB]')
    of.title(ax, r'Pico resonante $M_r$ vs $\zeta$')
    of.legend(ax, fontsize=9); of.save(fig, 'bode_pico_resonante')


# ---------- márgenes ----------
def margenes():
    w = np.logspace(-1, 1.5, 800)
    L = 5/((1j*w)*(1+1j*w)*(1+1j*w/3))
    m, p = mag_phase(L)
    fig, a1, a2 = bode_axes()
    a1.semilogx(w, m, color=of.CURVE, lw=2)
    a1.axhline(0, color=of.BROWN, lw=0.8, alpha=0.6)
    a2.semilogx(w, p, color=of.CURVE, lw=2)
    a2.axhline(-180, color=of.BROWN, lw=0.8, alpha=0.6)
    # cruces
    igc = np.argmin(np.abs(m)); wgc = w[igc]
    ipc = np.argmin(np.abs(p+180)); wpc = w[ipc]
    a1.axvline(wgc, color=of.ACCENT, lw=1.2, ls=':'); a2.axvline(wgc, color=of.ACCENT, lw=1.2, ls=':')
    a1.axvline(wpc, color=of.BROWN, lw=1.2, ls=':'); a2.axvline(wpc, color=of.BROWN, lw=1.2, ls=':')
    a2.annotate('MF', (wgc, p[igc]), color=of.TEXT, xytext=(6, 20), textcoords='offset points')
    a1.annotate('MG', (wpc, m[ipc]), color=of.TEXT, xytext=(6, 10), textcoords='offset points')
    a2.set_yticks([0, -90, -180, -270])
    of.title(a1, 'Márgenes de fase (MF) y ganancia (MG)')
    of.save(fig, 'bode_margenes')


# ---------- compensadores ----------
def comp_lead():
    w = np.logspace(-1, 2, 600); alpha = 0.1; T = 1.0
    Gc = (1j*w*T + 1)/(alpha*1j*w*T + 1)
    m, p = mag_phase(Gc)
    fig, a1, a2 = bode_axes()
    a1.semilogx(w, m, color=of.CURVE, lw=2); a2.semilogx(w, p, color=of.CURVE, lw=2)
    wm = 1/(T*np.sqrt(alpha)); phim = np.degrees(np.arcsin((1-alpha)/(1+alpha)))
    a2.plot(wm, phim, '*', color=of.ACCENT, ms=14)
    a2.annotate(r'$\phi_m$', (wm, phim), color=of.TEXT, xytext=(6, -14), textcoords='offset points')
    of.title(a1, r'Compensador lead $\dfrac{Ts+1}{\alpha Ts+1}$ (joroba de fase)')
    of.save(fig, 'bode_lead_compensador')


def comp_lag():
    w = np.logspace(-2, 1, 600); beta = 10.0; T = 1.0
    Gc = (1j*w*T + 1)/(beta*1j*w*T + 1)
    m, p = mag_phase(Gc)
    fig, a1, a2 = bode_axes()
    a1.semilogx(w, m, color=of.CURVE, lw=2); a2.semilogx(w, p, color=of.CURVE, lw=2)
    a1.axhline(-20*np.log10(beta), color=of.ACCENT, lw=1.2, ls='--', alpha=0.7)
    a1.annotate(r'$-20\log\beta$', (w[10], -20*np.log10(beta)), color=of.TEXT,
                xytext=(4, 4), textcoords='offset points')
    of.title(a1, r'Compensador lag $\dfrac{Ts+1}{\beta Ts+1}$ (atenuación)')
    of.save(fig, 'bode_lag_compensador')


def comp_lead_lag():
    w = np.logspace(-2, 2, 800)
    lag = (1j*w*10 + 1)/(100*1j*w*10 + 1) * 100   # ganancia lag a baja frec
    # más simple: lag con beta y lead con alpha en bandas separadas
    lag = (1j*w + 1)/(8*1j*w + 1)
    lead = (1j*w/3 + 1)/(0.1*1j*w/3 + 1)
    Gc = lag*lead
    m, p = mag_phase(Gc)
    fig, a1, a2 = bode_axes()
    a1.semilogx(w, m, color=of.CURVE, lw=2); a2.semilogx(w, p, color=of.CURVE, lw=2)
    of.title(a1, 'Compensador lead-lag (lag baja frec + lead media frec)')
    of.save(fig, 'bode_lead_lag')


# ---------- sensibilidad S y T ----------
def sensibilidad():
    w = np.logspace(-2, 2, 700)
    L = 20/((1j*w)*(1+1j*w))
    S = 1/(1+L); T = L/(1+L)
    fig, (ax) = of.new_fig(figsize=(6.2, 4.2)); of.style_axes(ax)
    ax.semilogx(w, 20*np.log10(np.abs(S)), color=of.CURVE, lw=2, label=r'$S=1/(1+L)$')
    ax.semilogx(w, 20*np.log10(np.abs(T)), color=of.ACCENT, lw=2, label=r'$T=L/(1+L)$')
    ax.axhline(0, color=of.BROWN, lw=0.8, alpha=0.5)
    ax.set_ylim(-40, 10)
    of.labels(ax, r'$\omega$ [rad/s]', 'Magnitud [dB]')
    of.title(ax, r'Sensibilidad $S$ y complementaria $T$  ($S+T=1$)')
    of.legend(ax, fontsize=9); of.save(fig, 'sensibilidad_S_T_frecuencia')


if __name__ == '__main__':
    print('Generando Bode...')
    factores_basicos(); segundo_orden_zeta(); construccion_asintotica()
    correccion_esquina(); pico_resonante(); margenes()
    comp_lead(); comp_lag(); comp_lead_lag(); sensibilidad()
    print('OK')
