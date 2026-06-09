#!/usr/bin/env python3
"""Figuras de No Lineales y Singulares (Ecuaciones Integrales).
Estilo Ocean Forest. Salida -> ../img_gen/*.svg"""
import numpy as np
import ocean_forest as of


# ---------------------------------------------------------- 1. bifurcacion de Hammerstein
def fig_bifurcacion_hammerstein():
    fig, ax = of.new_fig(figsize=(6.4, 4.4)); of.style_axes(ax)
    l1 = 1.0
    lam = np.linspace(0, 3, 300)
    # rama trivial
    ax.plot(lam[lam <= l1], 0*lam[lam <= l1], color=of.CURVE, lw=2.6, label=r'trivial $\varphi\equiv0$ (estable)')
    ax.plot(lam[lam >= l1], 0*lam[lam >= l1], color=of.CURVE, lw=2.2, ls=':', label=r'trivial (inestable)')
    # ramas no triviales
    lr = lam[lam >= l1]
    A = np.sqrt(lr - l1)
    ax.plot(lr, A, color=of.ACCENT, lw=2.6, label=r'rama no trivial $\sim\sqrt{\lambda-\lambda_1}$')
    ax.plot(lr, -A, color=of.ACCENT, lw=2.6)
    ax.plot(l1, 0, 'o', color=of.BROWN, ms=8, zorder=6)
    ax.annotate(r'$\lambda_1$ (1ª raíz característica)', xy=(l1, 0), xytext=(1.25, 0.9),
                color=of.TEXT, fontsize=10, arrowprops=dict(arrowstyle='->', color=of.BROWN))
    ax.set_xlim(0, 3); ax.set_ylim(-1.6, 1.7)
    of.labels(ax, r'$\lambda$', r'amplitud $\|\varphi\|$')
    of.title(ax, r'Bifurcación de horquilla (Hammerstein)')
    of.legend(ax, loc='lower left', fontsize=8)
    of.save(fig, 'bifurcacion_hammerstein')


# ---------------------------------------------------------- 2. nucleos singulares
def fig_nucleos_singulares():
    fig, ax = of.new_fig(figsize=(6.6, 4.4)); of.style_axes(ax)
    s = np.linspace(0.04, 1.0, 400)
    for a, c, lbl in [(0.5, of.CURVE, r'$\alpha=1/2$ (débil, integrable)'),
                      (1.0, of.ACCENT, r'$\alpha=1$ (Cauchy, v.p.)'),
                      (1.5, of.BROWN, r'$\alpha=3/2$ (hipersingular)')]:
        ax.plot(s, s**(-a), color=c, lw=2.4, label=lbl)
    ax.fill_between(s, 0, s**(-0.5), color=of.CURVE, alpha=0.10)
    ax.set_xlim(0, 1.0); ax.set_ylim(0, 10)
    of.labels(ax, r'$s=x-t$', r'$1/s^{\alpha}$')
    of.title(ax, r'Fuerza de la singularidad del núcleo $1/(x-t)^{\alpha}$')
    of.legend(ax, loc='upper right')
    of.save(fig, 'nucleos_singulares')


# ---------------------------------------------------------- 3. salto de Plemelj (Cauchy)
def fig_plemelj_cauchy():
    fig, ax = of.new_fig(figsize=(6.4, 4.4)); of.style_axes(ax)
    t = np.linspace(-2.4, 2.4, 300)
    L = 0.35*np.sin(1.3*t)              # contorno L (curva)
    ax.fill_between(t, L, 2.4, color=of.CURVE, alpha=0.10)
    ax.fill_between(t, -2.4, L, color=of.ACCENT, alpha=0.10)
    ax.plot(t, L, color=of.BROWN, lw=2.6)
    ax.text(2.0, 1.7, r'$\Phi^{+}$', color=of.CURVE, fontsize=15, ha='center')
    ax.text(2.0, -1.8, r'$\Phi^{-}$', color=of.ACCENT, fontsize=15, ha='center')
    ax.text(-2.05, 0.55, r'contorno $L$', color=of.TEXT, fontsize=10)
    # punto x sobre L con el salto
    x0 = 0.6; y0 = 0.35*np.sin(1.3*x0)
    ax.plot(x0, y0, 'o', color=of.BROWN, ms=7, zorder=6)
    ax.annotate('', xy=(x0, y0+0.7), xytext=(x0, y0-0.7),
                arrowprops=dict(arrowstyle='<->', color=of.TICK, lw=1.8))
    ax.text(x0+0.12, y0+0.55, r'salto $\Phi^{+}-\Phi^{-}=\varphi(x)$', color=of.TEXT, fontsize=10)
    ax.set_xlim(-2.4, 2.4); ax.set_ylim(-2.4, 2.4)
    ax.set_xticks([]); ax.set_yticks([])
    of.labels(ax, r'$\operatorname{Re}z$', r'$\operatorname{Im}z$')
    of.title(ax, r'Fórmulas de Plemelj: la integral de Cauchy salta en $L$')
    of.save(fig, 'plemelj_cauchy')


# ---------------------------------------------------------- 4. factorizacion de Wiener-Hopf
def fig_wiener_hopf():
    fig, ax = of.new_fig(figsize=(6.4, 4.4)); of.style_axes(ax)
    xs = np.linspace(-3, 3, 10)
    ax.fill_between([-3, 3], 0.25, 3, color=of.CURVE, alpha=0.13)
    ax.fill_between([-3, 3], -3, -0.25, color=of.ACCENT, alpha=0.13)
    ax.fill_between([-3, 3], -0.25, 0.25, color=of.BROWN, alpha=0.10)
    ax.axhline(0, color=of.BROWN, lw=1.4)
    ax.text(0, 2.0, r'$G_{+}(\xi)$ analítica  ($\operatorname{Im}\xi>0$)',
            color=of.TEXT, ha='center', fontsize=11)
    ax.text(0, -2.0, r'$G_{-}(\xi)$ analítica  ($\operatorname{Im}\xi<0$)',
            color=of.TEXT, ha='center', fontsize=11)
    ax.text(0, 0.0, r'franja común  $\to$  Liouville', color=of.TICK, ha='center', fontsize=9)
    ax.text(2.55, 0.12, r'eje real', color=of.TEXT, fontsize=8)
    ax.set_xlim(-3, 3); ax.set_ylim(-3, 3)
    ax.set_xticks([]); ax.set_yticks([])
    of.labels(ax, r'$\operatorname{Re}\xi$', r'$\operatorname{Im}\xi$')
    of.title(ax, r'Wiener-Hopf: $1-\hat K(\xi)=G_{+}(\xi)\,G_{-}(\xi)$')
    of.save(fig, 'wiener_hopf')


if __name__ == '__main__':
    print('Generando figuras No Lineales + Singulares:')
    fig_bifurcacion_hammerstein()
    fig_nucleos_singulares()
    fig_plemelj_cauchy()
    fig_wiener_hopf()
    print('Listo.')
