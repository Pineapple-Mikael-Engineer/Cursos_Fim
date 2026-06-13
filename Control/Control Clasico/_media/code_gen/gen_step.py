#!/usr/bin/env python3
"""Genera respuestas temporales al escalón (en ../img_gen/). Uso: python3 gen_step.py"""
import numpy as np
from numpy.polynomial.polynomial import polymul   # no usado; usamos np.polymul
import ocean_forest as of
from scipy import signal


def cl_step(numC, denC, numG, denG, t):
    """Respuesta al escalón del lazo cerrado con realimentación unitaria."""
    numOL = np.polymul(numC, numG)
    denOL = np.polymul(denC, denG)
    # T = OL / (1 + OL)
    numT = numOL
    denT = np.polyadd(denOL, numOL)
    _, y = signal.step((numT, denT), T=t)
    return y


PLANT = ([1.0], np.poly([-1, -1, -1]))   # G = 1/(s+1)^3 (tipo 0, dc=1)


def step_fig(title):
    fig, ax = of.new_fig(figsize=(6.2, 4.0)); of.style_axes(ax)
    of.labels(ax, 'tiempo [s]', 'salida $y(t)$'); of.title(ax, title)
    ax.axhline(1.0, color=of.BROWN, lw=0.8, ls='--', alpha=0.5)
    return fig, ax


# ---------- efecto de cada ganancia ----------
def efecto_kp():
    t = np.linspace(0, 12, 600); ng, dg = PLANT
    fig, ax = step_fig(r'Acción P: efecto de $K_p$')
    for kp, c in zip([1, 2, 4, 8], of.PALETTE):
        ax.plot(t, cl_step([kp], [1], ng, dg, t), color=c, lw=2, label=rf'$K_p={kp}$')
    of.legend(ax, fontsize=9); of.save(fig, 'p_efecto_kp_escalon')


def efecto_ki():
    t = np.linspace(0, 20, 700); ng, dg = PLANT
    fig, ax = step_fig(r'Acción I: efecto de $K_i$ (elimina el error)')
    for ki, c in zip([0.3, 0.8, 1.5], of.PALETTE):
        ax.plot(t, cl_step([2, ki], [1, 0], ng, dg, t), color=c, lw=2, label=rf'$K_i={ki}$')
    of.legend(ax, fontsize=9); of.save(fig, 'i_efecto_ki_escalon')


def efecto_kd():
    t = np.linspace(0, 12, 600); ng, dg = PLANT
    fig, ax = step_fig(r'Acción D: efecto de $K_d$ (amortigua)')
    for kd, c in zip([0, 1, 3], of.PALETTE):
        ax.plot(t, cl_step([kd, 4], [1], ng, dg, t), color=c, lw=2, label=rf'$K_d={kd}$')
    of.legend(ax, fontsize=9); of.save(fig, 'd_efecto_kd_escalon')


# ---------- comparaciones de configuraciones ----------
def pi_vs_p():
    t = np.linspace(0, 20, 700); ng, dg = PLANT
    fig, ax = step_fig('P vs PI (PI elimina el offset)')
    ax.plot(t, cl_step([2], [1], ng, dg, t), color=of.PALETTE[0], lw=2, label='P')
    ax.plot(t, cl_step([2, 0.8], [1, 0], ng, dg, t), color=of.PALETTE[1], lw=2, label='PI')
    of.legend(ax, fontsize=9); of.save(fig, 'pi_vs_p_escalon')


def pd_vs_p():
    t = np.linspace(0, 12, 600); ng, dg = PLANT
    fig, ax = step_fig('P vs PD (PD amortigua)')
    ax.plot(t, cl_step([4], [1], ng, dg, t), color=of.PALETTE[0], lw=2, label='P')
    ax.plot(t, cl_step([2, 4], [1], ng, dg, t), color=of.PALETTE[1], lw=2, label='PD')
    of.legend(ax, fontsize=9); of.save(fig, 'pd_vs_p_escalon')


def pid_comparacion():
    t = np.linspace(0, 20, 800); ng, dg = PLANT
    fig, ax = step_fig('Comparación P, PI, PD, PID')
    ax.plot(t, cl_step([3], [1], ng, dg, t),           color=of.PALETTE[0], lw=2, label='P')
    ax.plot(t, cl_step([2, 0.8], [1, 0], ng, dg, t),   color=of.PALETTE[1], lw=2, label='PI')
    ax.plot(t, cl_step([2, 4], [1], ng, dg, t),        color=of.PALETTE[2], lw=2, label='PD')
    ax.plot(t, cl_step([2, 4, 1.2], [1, 0], ng, dg, t),color=of.PALETTE[3], lw=2, label='PID')
    of.legend(ax, fontsize=9); of.save(fig, 'pid_comparacion_configuraciones')


def pid_efecto_acciones():
    t = np.linspace(0, 20, 800); ng, dg = PLANT
    fig, ax = step_fig('Efecto de las acciones sobre la respuesta')
    ax.plot(t, cl_step([2], [1], ng, dg, t),            color=of.PALETTE[0], lw=2, label='P')
    ax.plot(t, cl_step([2, 0.8], [1, 0], ng, dg, t),    color=of.PALETTE[1], lw=2, label='PI')
    ax.plot(t, cl_step([2, 4, 1.2], [1, 0], ng, dg, t), color=of.PALETTE[3], lw=2, label='PID')
    of.legend(ax, fontsize=9); of.save(fig, 'pid_efecto_acciones_escalon')


# ---------- segundo orden ----------
def segundo_orden_escalon():
    t = np.linspace(0, 14, 700); wn = 1.0
    fig, ax = step_fig(r'Respuesta al escalón de 2.º orden')
    for z, c in zip([0.1, 0.3, 0.707, 1.5], of.PALETTE):
        y = cl_step([wn**2], [1], [1], [1, 2*z*wn, 0], t)  # G=wn^2/(s^2+2zwn s) lazo cerrado
        ax.plot(t, y, color=c, lw=2, label=rf'$\zeta={z}$')
    of.legend(ax, fontsize=9); of.save(fig, 'segundo_orden_escalon')


def segundo_orden_envolvente():
    wn, z = 1.0, 0.2; t = np.linspace(0, 20, 800)
    wd = wn*np.sqrt(1-z**2)
    y = 1 - np.exp(-z*wn*t)/np.sqrt(1-z**2)*np.sin(wd*t + np.arccos(z))
    env = np.exp(-z*wn*t)/np.sqrt(1-z**2)
    fig, ax = step_fig(r'Respuesta de 2.º orden y su envolvente ($\zeta=0.2$)')
    ax.plot(t, y, color=of.CURVE, lw=2, label=r'$y(t)$')
    ax.plot(t, 1+env, color=of.ACCENT, lw=1.4, ls='--', label='Envolvente')
    ax.plot(t, 1-env, color=of.ACCENT, lw=1.4, ls='--')
    of.legend(ax, fontsize=9); of.save(fig, 'segundo_orden_envolvente')


def primer_orden_escalon():
    tau = 2.0; t = np.linspace(0, 12, 600)
    y = 1 - np.exp(-t/tau)
    fig, ax = step_fig(r'Respuesta al escalón de 1.er orden ($\tau=2$)')
    ax.plot(t, y, color=of.CURVE, lw=2)
    ax.plot(tau, 1-np.exp(-1), '*', color=of.ACCENT, ms=14)
    ax.annotate(r'$63\%$ en $t=\tau$', (tau, 1-np.exp(-1)), color=of.TEXT,
                xytext=(8, -16), textcoords='offset points')
    ax.axvline(tau, color=of.BROWN, lw=1, ls=':', alpha=0.6)
    of.save(fig, 'primer_orden_escalon')


# ---------- fase mínima vs no mínima ----------
def fase_minima():
    t = np.linspace(0, 8, 500)
    _, ymp = signal.step(([ -1, 2], [1, 3, 2]), T=t)   # cero en SPI
    _, ynmp = signal.step(([ 1, 2], [1, 3, 2]), T=t)   # cero en SPD (1 - s)... ajustar
    # no mínima: (1 - s/2)/((s+1)(s+2)) -> undershoot
    _, ynmp = signal.step(([-0.5, 1], np.poly([-1, -2])), T=t)
    _, ymp = signal.step(([0.5, 1], np.poly([-1, -2])), T=t)
    fig, ax = step_fig('Fase mínima vs no mínima (misma magnitud)')
    ax.plot(t, ymp, color=of.PALETTE[0], lw=2, label='Fase mínima')
    ax.plot(t, ynmp, color=of.PALETTE[1], lw=2, label='Fase no mínima (undershoot)')
    ax.axhline(0, color=of.BROWN, lw=0.8, alpha=0.5)
    of.legend(ax, fontsize=9); of.save(fig, 'fase_minima_vs_no_minima')


# ---------- Ziegler-Nichols ----------
def zn_oscilacion():
    t = np.linspace(0, 16, 700); Tu = 2*np.pi/2.0
    y = 1 + 0.5*np.sin(2.0*t - np.pi/2)   # oscilación sostenida amplitud cte
    fig, ax = step_fig(r'Oscilación sostenida en $K_u$ (periodo $T_u$)')
    ax.plot(t, y, color=of.CURVE, lw=2)
    ax.annotate('', xy=(np.pi/2+Tu, 1.5), xytext=(np.pi/2, 1.5),
                arrowprops=dict(arrowstyle='<->', color=of.ACCENT, lw=1.5))
    ax.annotate(r'$T_u$', (np.pi/2+Tu/2, 1.5), color=of.TEXT, ha='center',
                xytext=(0, 6), textcoords='offset points')
    of.save(fig, 'zn_oscilacion_sostenida')


def zn_curva_reaccion():
    t = np.linspace(0, 14, 700); K, L, T = 1.0, 1.5, 3.0
    y = np.where(t < L, 0, K*(1 - np.exp(-(t-L)/T)))
    fig, ax = step_fig('Curva de reacción (FOPDT): identificación de $L$ y $T$')
    ax.plot(t, y, color=of.CURVE, lw=2, label='Respuesta')
    # tangente en la inflexión (en t=L, pendiente K/T)
    tt = np.linspace(L, L+T+1, 50)
    ax.plot(tt, (K/T)*(tt-L), color=of.ACCENT, lw=1.6, ls='--', label='Tangente')
    ax.axhline(K, color=of.BROWN, lw=0.8, ls='--', alpha=0.5)
    for x, lab in [(L, '$L$'), (L+T, '$L+T$')]:
        ax.axvline(x, color=of.BROWN, lw=1, ls=':', alpha=0.6)
        ax.annotate(lab, (x, 0), color=of.TEXT, xytext=(3, 4), textcoords='offset points')
    of.legend(ax, fontsize=9); of.save(fig, 'zn_curva_reaccion')


def identificacion():
    t = np.linspace(0, 14, 700); K, L, T = 1.0, 1.0, 2.5
    y = np.where(t < L, 0, K*(1 - np.exp(-(t-L)/T)))
    fig, ax = step_fig('Identificación por respuesta al escalón')
    ax.plot(t, y, color=of.CURVE, lw=2)
    tt = np.linspace(L, L+T+1, 50)
    ax.plot(tt, (K/T)*(tt-L), color=of.ACCENT, lw=1.6, ls='--')
    ax.axhline(K, color=of.BROWN, lw=0.8, ls='--', alpha=0.5)
    ax.annotate('63%', (L+T, K*0.63), color=of.TEXT, xytext=(6, -4), textcoords='offset points')
    of.save(fig, 'identificacion_escalon')


if __name__ == '__main__':
    print('Generando respuestas al escalón...')
    efecto_kp(); efecto_ki(); efecto_kd()
    pi_vs_p(); pd_vs_p(); pid_comparacion(); pid_efecto_acciones()
    segundo_orden_escalon(); segundo_orden_envolvente(); primer_orden_escalon()
    fase_minima(); zn_oscilacion(); zn_curva_reaccion(); identificacion()
    print('OK')
