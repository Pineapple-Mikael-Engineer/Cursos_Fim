"""Gráficas de datos: factor Z, energía configuracional, inversión J-T,
Clapeyron, T_llama vs exceso de aire, entropía en expansión libre."""
import numpy as np
import ocean_forest as of
of.setup()

# ---------- 1) Factor de compresibilidad Z(Pr, Tr) ----------
def Zmodel(Pr, Tr):
    a = -0.5 / Tr ** 1.5 + 0.1
    b = 0.06 / Tr
    return 1 + a * Pr + b * Pr ** 2


def carta_Z(nombre, titulo):
    fig, ax = of.new_fig(figsize=(6.4, 4.6)); of.style_axes(ax)
    Pr = np.linspace(0, 7, 200)
    ax.axhline(1.0, color=of.BROWN, lw=1.4, ls='--', dashes=(6, 3), alpha=0.8)
    ax.annotate('gas ideal  $Z=1$', (5.2, 1.02), color=of.BROWN, fontsize=8.5)
    for Tr, col in zip([1.0, 1.2, 1.5, 2.0, 5.0], of.PALETTE):
        ax.plot(Pr, Zmodel(Pr, Tr), color=col, lw=2.2, label=f'$T_r={Tr}$')
    of.labels(ax, x=r'presión reducida  $P_r=P/P_c$', y=r'factor  $Z=Pv/RT$')
    of.title(ax, titulo)
    ax.set_xlim(0, 7); ax.set_ylim(0.2, 1.5)
    of.legend(ax, loc='lower right', fontsize=8.5)
    of.save(fig, nombre)


carta_Z('factor_compresibilidad_Z', r'Factor de compresibilidad  $Z(P_r,T_r)$')
carta_Z('gas_real_factor_Z_Nelson_Obert', r'Carta generalizada de Nelson–Obert  $Z(P_r,T_r)$')

# ---------- 2) Energía configuracional de van der Waals: -a/v ----------
fig, ax = of.new_fig(figsize=(6.2, 4.2)); of.style_axes(ax)
v = np.linspace(0.6, 6, 300)
a = 3.0
ax.plot(v, -a / v, color=of.CURVE, lw=2.6)
ax.axhline(0, color=of.BROWN, lw=1.0, ls='--', dashes=(5, 3), alpha=0.7)
ax.annotate(r'$u^{\rm config}=-a/v$', (3.2, -a / 3.2), (3.4, -1.6), color=of.CURVE, fontsize=10)
ax.annotate(r'$v\to\infty$: gas ideal ($u^{\rm config}\to0$)', (5.6, -a / 5.6),
            (2.6, -0.35), color=of.BROWN, fontsize=8.5)
ax.annotate('compresión\n(moléculas se acercan)', (0.85, -a / 0.85), (1.2, -4.4),
            color=of.ACCENT, fontsize=8.5,
            arrowprops=dict(arrowstyle='->', color=of.ACCENT, lw=1))
of.labels(ax, x=r'volumen molar  $v$', y=r'energía configuracional  $-a/v$')
of.title(ax, r'Energía de cohesión del gas de van der Waals')
ax.set_xlim(0.6, 6); ax.set_ylim(-5.2, 0.6)
of.save(fig, 'energia_configuracional_vdW')

# ---------- 3) Curva de inversión Joule-Thomson (vdW reducida) ----------
fig, ax = of.new_fig(figsize=(6.2, 4.6)); of.style_axes(ax)
Tr = np.linspace(0.752, 6.748, 700)
Pr = 24 * np.sqrt(3 * Tr) - 12 * Tr - 27          # curva de inversión vdW reducida (domo)
m = Pr >= 0
ax.fill(Pr[m], Tr[m], color=of.CURVE, alpha=0.12)
ax.plot(Pr[m], Tr[m], color=of.CURVE, lw=2.6)
ax.annotate(r'$\mu_{JT}>0$' '\n(enfriamiento)', (3.0, 3.4), color=of.CURVE, fontsize=9.5, ha='center')
ax.annotate(r'$\mu_{JT}<0$' '\n(calentamiento)', (8.3, 5.2), color=of.BROWN, fontsize=9.5, ha='center')
ax.annotate(r'$T_{inv}^{+}=\dfrac{2a}{Rb}$', (0.1, Tr[m].max()), (1.6, 6.4),
            color=of.ACCENT, fontsize=9.5,
            arrowprops=dict(arrowstyle='->', color=of.ACCENT, lw=1))
of.labels(ax, x=r'presión reducida  $P_r$', y=r'temperatura reducida  $T_r$')
of.title(ax, r'Curva de inversión Joule–Thomson (van der Waals)')
ax.set_xlim(0, 11); ax.set_ylim(0.6, 7.2)
of.save(fig, 'joule_thomson_curva_inversion')

# ---------- 4) Curva de saturación P-T y pendiente de Clapeyron ----------
fig, ax = of.new_fig(figsize=(6.2, 4.4)); of.style_axes(ax)
T = np.linspace(0.45, 1.0, 200)
Psat = np.exp(5.5 * (1 - 1 / T))
ax.plot(T, Psat, color=of.CURVE, lw=2.6)
ax.fill_between(T, Psat, 3, color=of.BROWN, alpha=0.05)
ax.fill_between(T, 0, Psat, color=of.ACCENT, alpha=0.05)
ax.text(0.55, 1.1, 'líquido', color=of.BROWN, fontsize=10)
ax.text(0.85, 0.18, 'vapor', color=of.ACCENT, fontsize=10)
# punto con su tangente dP/dT
T0 = 0.85; P0 = np.exp(5.5 * (1 - 1 / T0)); slope = P0 * 5.5 / T0 ** 2
ax.plot(T0, P0, 'o', color=of.TEXT, ms=8, zorder=6)
tt = np.array([T0 - 0.09, T0 + 0.09])
ax.plot(tt, P0 + slope * (tt - T0), color=of.ACCENT, lw=1.8, ls='--', dashes=(5, 3))
ax.annotate(r'$\dfrac{dP}{dT}=\dfrac{h_{fg}}{T\,v_{fg}}$', (T0, P0), (T0 - 0.30, P0 + 0.55),
            color=of.ACCENT, fontsize=10)
of.labels(ax, x=r'temperatura  $T$', y=r'presión  $P$')
of.title(ax, r'Curva de saturación y ecuación de Clapeyron')
ax.set_xlim(0.45, 1.02); ax.set_ylim(0, 2.6)
of.save(fig, 'gibbs_curva_saturacion_Clapeyron')

# ---------- 5) Temperatura adiabática de llama vs exceso de aire ----------
fig, ax = of.new_fig(figsize=(6.2, 4.2)); of.style_axes(ax)
pct = np.linspace(60, 200, 300)             # % de aire teórico
# pico cerca del estequiométrico (100%); cae por aire en defecto (combustión incompleta)
# y por aire en exceso (dilución). Modelo esquemático.
Tmax = 2300
Taf = np.where(pct <= 100,
               Tmax * (1 - 0.9 * ((100 - pct) / 100) ** 1.4),
               Tmax * (100 / pct) ** 0.55)
ax.plot(pct, Taf, color=of.CURVE, lw=2.6)
ax.axvline(100, color=of.ACCENT, lw=1.4, ls='--', dashes=(5, 3))
ax.annotate('estequiométrico\n(100% aire teórico)', (100, 1500), (108, 1350),
            color=of.ACCENT, fontsize=8.5)
ax.annotate('exceso de aire\n(dilución enfría)', (165, Tmax * (100 / 165) ** 0.55),
            (140, 1950), color=of.BROWN, fontsize=8.5)
ax.annotate('aire en defecto\n(comb. incompleta)', (70, Tmax * (1 - 0.9 * (0.3) ** 1.4)),
            (62, 1100), color=of.BROWN, fontsize=8.5)
of.labels(ax, x=r'% de aire teórico', y=r'$T_{\rm llama\ adiab.}$ [K]')
of.title(ax, r'Temperatura adiabática de llama vs exceso de aire')
ax.set_xlim(60, 200); ax.set_ylim(800, 2500)
of.save(fig, 'taf_vs_exceso_aire')

# ---------- 6) Entropía en la expansión libre (microestados) ----------
fig, ax = of.new_fig(figsize=(6.2, 4.2)); of.style_axes(ax)
r = np.linspace(1, 2, 200)                  # V/V0
dS = np.log(r)                              # ΔS/(Nk) = ln(V/V0)
ax.plot(r, dS, color=of.CURVE, lw=2.6)
ax.fill_between(r, dS, 0, color=of.CURVE, alpha=0.12)
ax.plot([1, 2], [0, np.log(2)], 'o', color=of.TEXT, ms=7, zorder=6)
ax.annotate('estado inicial\n($V_0$, un compartimento)', (1, 0), (1.02, 0.18),
            color=of.TEXT, fontsize=8.5)
ax.annotate(r'$\Delta s=R\ln 2$' '\n(expansión a $2V_0$)', (2, np.log(2)), (1.45, 0.30),
            color=of.ACCENT, fontsize=9,
            arrowprops=dict(arrowstyle='->', color=of.ACCENT, lw=1))
ax.text(1.5, 0.05, r'$\Delta s = R\,\ln(V/V_0) = k_B\ln(\Omega/\Omega_0)$',
        color=of.BROWN, fontsize=9, ha='center')
of.labels(ax, x=r'razón de expansión  $V/V_0$', y=r'$\Delta s / R$')
of.title(ax, r'Aumento de entropía en la expansión libre')
ax.set_xlim(1, 2.02); ax.set_ylim(0, 0.78)
of.save(fig, 'entropia_microestados_expansion')

print('OK datos2: 7 figuras')
